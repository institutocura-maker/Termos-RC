#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (espelho leitura; Onda 1.7-c JSON-canônico)
"""Gera base-terminologica-leitura.docx — versão Word para LEITURA HUMANA.

A planilha XLSX continua sendo a fonte estruturada (para IAs e dados);
este documento converte o mesmo conteúdo em um arquivo Word legível:
capa, sumário, índice mestre por categoria, fichas detalhadas,
relações, bibliografia, categorias e pontos de atenção.

Fonte dos dados: base/canonico.json (espelho exportado do registro; Onda 1.7-c)
                 base/biblio.json (Onda 1.3)
                        termos/*.md (fichas)
                        README.md (pontos de atenção)
"""
import os, re, sys, datetime
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FER = os.path.join(RAIZ, "ferramentas")

# ---------------------------------------------------------------- carregar dados
# Onda 0.2: loader único (aposenta carregar_py/carregar_literal).
sys.path.insert(0, FER)
from loader import carregar_canonico, BIBLIO  # Onda 1.7-c: JSON-primeiro
TERMOS, RELACOES = carregar_canonico()

STATUS_LABEL = {"candidato": "⚪ candidato", "provisório": "🟡 provisório",
                "em análise": "🟠 em análise", "verificado": "🟢 verificado",
                "P": "🟡 provisório", "C": "⚪ candidato"}

# ---------------------------------------------------------------- helpers docx
AZUL = RGBColor(0x1F, 0x3A, 0x5F)
AZUL_CLARO = RGBColor(0x2E, 0x5E, 0x8C)
CINZA = RGBColor(0x55, 0x55, 0x55)

def config_doc(doc):
    for section in doc.sections:
        section.top_margin = Cm(2.0); section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.2); section.right_margin = Cm(2.2)
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"; estilo.font.size = Pt(10.5)
    estilo.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

def add_cabecalho_rodape(doc, texto):
    sec = doc.sections[0]
    # cabeçalho
    p = sec.header.paragraphs[0]; p.text = texto
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs: r.font.size = Pt(8); r.font.color.rgb = CINZA
    # rodapé com página
    p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Página ")
    run.font.size = Pt(8); run.font.color.rgb = CINZA
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    p._p.append(fld)
    run2 = p.add_run("  ·  Base Terminológica RC")
    run2.font.size = Pt(8); run2.font.color.rgb = CINZA

def add_heading(doc, texto, nivel=1, cor=AZUL):
    h = doc.add_heading(texto, level=nivel)
    for r in h.runs:
        r.font.color.rgb = cor if nivel <= 2 else AZUL_CLARO
    return h

def add_par(doc, texto, bold=False, italic=False, size=None, cor=None, space_after=4):
    p = doc.add_paragraph()
    r = p.add_run(texto); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    if cor: r.font.color.rgb = cor
    p.paragraph_format.space_after = Pt(space_after)
    return p

def estilo_tabela(tabela):
    tabela.style = "Table Grid"
    tabela.alignment = WD_TABLE_ALIGNMENT.CENTER
    # cabeçalho azul com texto branco
    for cell in tabela.rows[0].cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); r.font.size = Pt(9)
            p.paragraph_format.space_after = Pt(0)
        shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), "1F3A5F")
        cell._tc.get_or_add_tcPr().append(shd)
    for row in tabela.rows[1:]:
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs: r.font.size = Pt(9)
                p.paragraph_format.space_after = Pt(0)

def add_inline(doc, texto, estilo=None):
    """Adiciona parágrafo interpretando **negrito** e *itálico*."""
    p = doc.add_paragraph(style=estilo)
    for token in re.split(r"(\*\*.*?\*\*|\*.*?\*)", texto):
        if not token: continue
        if token.startswith("**") and token.endswith("**"):
            r = p.add_run(token[2:-2]); r.bold = True
        elif token.startswith("*") and token.endswith("*") and len(token) > 2:
            r = p.add_run(token[1:-1]); r.italic = True
        else:
            p.add_run(token)
    p.paragraph_format.space_after = Pt(4)
    return p

def add_md_tabela(doc, linhas):
    """Converte blocos de tabela markdown (| a | b |) em tabela Word."""
    cells = [[c.strip() for c in l.strip().strip("|").split("|")] for l in linhas
             if l.strip().startswith("|")]
    cells = [c for c in cells if not all(re.fullmatch(r":?-+:?", x) for x in c)]
    if not cells: return
    ncols = max(len(c) for c in cells)
    t = doc.add_table(rows=len(cells), cols=ncols)
    for i, c in enumerate(cells):
        for j in range(ncols):
            t.rows[i].cells[j].text = c[j] if j < len(c) else ""
    estilo_tabela(t)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def md_para_docx(doc, md):
    """Converte markdown simples de ficha em elementos docx."""
    linhas = md.splitlines()
    i = 0
    while i < len(linhas):
        l = linhas[i].rstrip()
        s = l.strip()
        if not s:
            i += 1; continue
        if s.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                bloco.append(linhas[i]); i += 1
            add_md_tabela(doc, bloco)
            continue
        if s.startswith("### "):
            add_heading(doc, s[4:].strip(), 3); i += 1; continue
        if s.startswith("## "):
            add_heading(doc, s[3:].strip(), 2); i += 1; continue
        if s.startswith("# "):
            add_heading(doc, s[2:].strip(), 1); i += 1; continue
        if s.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.7)
            r = p.add_run(s[2:].strip()); r.italic = True; r.font.color.rgb = CINZA
            i += 1; continue
        if s.startswith("- ") or s.startswith("* "):
            p = doc.add_paragraph(style="List Bullet")
            add_inline_into(p, s[2:].strip())
            i += 1; continue
        if re.match(r"^\d+\.\s", s):
            p = doc.add_paragraph(style="List Number")
            add_inline_into(p, re.sub(r"^\d+\.\s", "", s))
            i += 1; continue
        add_inline(doc, s)
        i += 1

def add_inline_into(p, texto):
    for token in re.split(r"(\*\*.*?\*\*|\*.*?\*)", texto):
        if not token: continue
        if token.startswith("**") and token.endswith("**"):
            r = p.add_run(token[2:-2]); r.bold = True
        elif token.startswith("*") and token.endswith("*") and len(token) > 2:
            r = p.add_run(token[1:-1]); r.italic = True
        else:
            p.add_run(token)

# ---------------------------------------------------------------- documento
doc = Document()
config_doc(doc)
add_cabecalho_rodape(doc, "BASE TERMINOLÓGICA — REVELAÇÕES CÓSMICAS (Jan Val Ellam)")

# ---------------- CAPA
for _ in range(6): doc.add_paragraph()
add_heading(doc, "BASE TERMINOLÓGICA", 0 if False else 1)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("REVELAÇÕES CÓSMICAS — Jan Val Ellam"); r.font.size = Pt(22); r.bold = True; r.font.color.rgb = AZUL
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Edição de leitura humana — gerada a partir da planilha XLSX (fonte estruturada para IAs)")
r.font.size = Pt(12); r.italic = True; r.font.color.rgb = CINZA
doc.add_paragraph()
n_fichas = len([f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.startswith("RC-")])
n_fichas_marc = len([t for t in TERMOS if t[7]])
add_par(doc, f"Gerado em {datetime.date.today().strftime('%d/%m/%Y')} — {len(TERMOS)} termos · {len(RELACOES)} relações · {len(BIBLIO)} obras · {n_fichas} fichas disponíveis ({n_fichas_marc} marcadas no índice)", size=11)
doc.add_page_break()

# ---------------- SUMÁRIO
add_heading(doc, "Sumário", 1)
sumario = [
    "PARTE 1 — Índice Mestre (todos os termos, por categoria)",
    "PARTE 2 — Fichas detalhadas dos termos centrais",
    "PARTE 3 — Relações tipadas entre termos",
    "PARTE 4 — Bibliografia (obras cadastradas)",
    "PARTE 5 — Categorias e vocabulário controlado",
    "PARTE 6 — Pontos de atenção (revisões e pendências)",
]
for s in sumario:
    add_par(doc, s, size=11.5)
add_par(doc, "", size=4)
add_par(doc, "Legenda de status:", bold=True)
for k, v in [("candidato", "⚪ candidato — identificado, aguardando confirmação em fonte publicada"),
             ("provisório", "🟡 provisório — fonte publicada documentada, aguardando revisão cruzada"),
             ("em análise", "🟠 em análise — sob revisão"),
             ("verificado", "🟢 verificado — confirmado")]:
    add_par(doc, f"{v}", size=10)
doc.add_page_break()

# ---------------- PARTE 1 — ÍNDICE MESTRE
add_heading(doc, "PARTE 1 — ÍNDICE MESTRE", 1)
add_par(doc, "Todos os termos cadastrados, agrupados por categoria principal. Status: " +
             "⚪ candidato · 🟡 provisório · 🟠 em análise · 🟢 verificado.", italic=True, size=10)

# agrupar por categoria
categorias = {}
for cod, nome, cat, sub, status, fontes, rel, ficha in TERMOS:
    categorias.setdefault(cat, []).append((cod, nome, sub, status, fontes, ficha))

for cat in sorted(categorias):
    add_heading(doc, f"▸ {cat} ({len(categorias[cat])} termos)", 2)
    itens = sorted(categorias[cat], key=lambda x: x[0])
    t = doc.add_table(rows=1, cols=4)
    hdr = t.rows[0].cells
    for j, htxt in enumerate(["Código", "Termo", "Subcategoria", "Status"]):
        hdr[j].text = htxt
    for cod, nome, sub, status, fontes, ficha in itens:
        row = t.add_row().cells
        row[0].text = cod
        row[1].text = nome
        row[2].text = sub
        row[3].text = STATUS_LABEL.get(status, status)
    estilo_tabela(t)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
doc.add_page_break()

# ---------------- PARTE 2 — FICHAS
add_heading(doc, "PARTE 2 — FICHAS DETALHADAS DOS TERMOS CENTRAIS", 1)
add_par(doc, f"{len([f for f in os.listdir(os.path.join(RAIZ,'termos')) if f.startswith('RC-')])} fichas "
             "dos termos centrais do corpus. Cada ficha traz definição, contexto, etimologia, fontes, "
             "citações-chave, termos relacionados e observações.", italic=True, size=10)

fichas = sorted([f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.startswith("RC-")])
# mapear nome do termo para o heading
nome_por_cod = {t[0]: t[1] for t in TERMOS}
for f in fichas:
    cod = f.split("-")[0] + "-" + f.split("-")[1]
    nome = nome_por_cod.get(cod, "")
    md = open(os.path.join(RAIZ, "termos", f), encoding="utf-8").read()
    linhas = md.splitlines()
    if linhas and linhas[0].strip().startswith("# "):
        # a ficha já traz o título; usar como heading e não duplicar
        add_heading(doc, linhas[0].strip()[2:].strip(), 1)
        md = "\n".join(linhas[1:])
    else:
        add_heading(doc, f"{cod} — {nome}", 1)
    md_para_docx(doc, md)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
doc.add_page_break()

# ---------------- PARTE 3 — RELAÇÕES
add_heading(doc, "PARTE 3 — RELAÇÕES TIPADAS ENTRE TERMOS", 1)
add_par(doc, f"{len(RELACOES)} relações tipadas (é-um, parte-de, sinônimo, variação, relaciona-se-a, etc.).",
        italic=True, size=10)
t = doc.add_table(rows=1, cols=4)
for j, htxt in enumerate(["Termo A", "Relação", "Termo B", "Fonte"]):
    t.rows[0].cells[j].text = htxt
for a, rel, b, fonte in sorted(RELACOES, key=lambda x: x[0]):
    row = t.add_row().cells
    row[0].text = f"{a} — {nome_por_cod.get(a,'')}"
    row[1].text = rel
    row[2].text = f"{b} — {nome_por_cod.get(b,'')}"
    row[3].text = fonte
estilo_tabela(t)
doc.add_page_break()

# ---------------- PARTE 4 — BIBLIOGRAFIA
add_heading(doc, "PARTE 4 — BIBLIOGRAFIA (OBRAS CADASTRADAS)", 1)
add_par(doc, f"{len(BIBLIO)} obras cadastradas. Status: trabalhada (PDF processado) · identificada/anunciada "
             "(sem PDF) · minerada (fonte de candidatos) · a confirmar.", italic=True, size=10)
t = doc.add_table(rows=1, cols=6)
for j, htxt in enumerate(["Código", "Título", "Subtítulo", "Editora", "Ano", "Status"]):
    t.rows[0].cells[j].text = htxt
for b in BIBLIO:
    row = t.add_row().cells
    for j, val in enumerate(b[:6]):
        row[j].text = str(val)
estilo_tabela(t)
doc.add_page_break()

# ---------------- PARTE 5 — CATEGORIAS
add_heading(doc, "PARTE 5 — CATEGORIAS E VOCABULÁRIO CONTROLADO", 1)
cat_path = os.path.join(RAIZ, "02-vocabulario-controlado.md")
if os.path.exists(cat_path):
    md_para_docx(doc, open(cat_path, encoding="utf-8").read())
doc.add_page_break()

# ---------------- PARTE 6 — PONTOS DE ATENÇÃO
add_heading(doc, "PARTE 6 — PONTOS DE ATENÇÃO (REVISÕES E PENDÊNCIAS)", 1)
readme = open(os.path.join(RAIZ, "README.md"), encoding="utf-8").read()
m = re.search(r"## ⚠️ Pontos de atenção.*?\n(.*?)(?=\n## |\Z)", readme, re.S)
if m:
    sec = m.group(1)
    for linha in sec.splitlines():
        linha = linha.strip()
        if re.match(r"^\d+\.\s", linha):
            add_par(doc, linha, size=10)
else:
    add_par(doc, "(seção não localizada no README)", size=10)

# ---------------- salvar
saida = os.path.join(RAIZ, "base-terminologica-leitura.docx")
doc.save(saida)
print("OK ->", saida)
print(f"Termos: {len(TERMOS)} | Relações: {len(RELACOES)} | Obras: {len(BIBLIO)} | Fichas: {len(fichas)}")
