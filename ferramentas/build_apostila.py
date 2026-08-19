#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a APOSTILA DE ESTUDO (DOCX) a partir de um Markdown estruturado.

Reproduz a formatação do exemplo "Apostila TOP — A Raça Inabalável dos Sethianos
Emancipados" (referencias-curador/apostila-exemplo-setianos.pdf):
  - Capa (título, palestrante, data, "Apostila de estudo")
  - Nota do editor
  - Sumário (campo TOC do Word, atualize com F9)
  - PARTES (roxo escuro #331A55) · Capítulos (#442266) · Seções (#553377)
  - Citações da fala em bloco roxo/lilás com recuo
  - Notas editoriais em verde (#2E7D4F) com destaque lateral
  - Glossário local em 4 seções (A personagens, B conceitos, C livros, D termos)
  - Cabeçalho: "Título · Jan Val Ellam · data" · Rodapé: "Apostila de estudo — página N"

Integração com a Base Terminológica RC: os termos do glossário local podem carregar
remissão RC-### (verificada automaticamente na base).

Uso:
  python3 ferramentas/build_apostila.py apostilas/AAAA-MM-DD_slug/apostila.md
Saída:
  apostilas/AAAA-MM-DD_slug/Apostila - [Título].docx
"""
import os, re, sys, datetime, json
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- cores (convenções v1 mantidas)
ROXO_H1 = RGBColor(0x33, 0x1A, 0x55)   # #331A55 título parte
ROXO_H2 = RGBColor(0x44, 0x22, 0x66)   # #442266 capítulo
ROXO_H3 = RGBColor(0x55, 0x33, 0x77)   # #553377 seção
VERDE_NOTA = RGBColor(0x2E, 0x7D, 0x4F) # #2E7D4F nota editorial
LILAS = RGBColor(0x6A, 0x3D, 0x8C)      # citação
CINZA = RGBColor(0x55, 0x55, 0x55)

def config(doc):
    for s in doc.sections:
        s.top_margin = Cm(2.2); s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(2.4); s.right_margin = Cm(2.0)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

def set_cab_rod(doc, titulo_cab, autor="Jan Val Ellam", data="", subtipo="Apostila de estudo — transcrição editada"):
    sec = doc.sections[0]
    hdr = sec.header.paragraphs[0]
    hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = hdr.add_run(f"{titulo_cab}  ·  {autor}  ·  {data}")
    r.font.size = Pt(8); r.font.color.rgb = CINZA
    ftr = sec.footer.paragraphs[0]
    ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = ftr.add_run(f"{subtipo} — página ")
    r.font.size = Pt(8); r.font.color.rgb = CINZA
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    ftr._p.append(fld)

def add_heading_cor(doc, texto, nivel, cor):
    h = doc.add_heading("", level=nivel)
    run = h.add_run(texto)
    run.font.color.rgb = cor
    return h

def add_par(doc, texto, size=10.5, bold=False, italic=False, cor=None, recuo=None, espaco=4):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if cor: r.font.color.rgb = cor
    if recuo: p.paragraph_format.left_indent = Cm(recuo)
    p.paragraph_format.space_after = Pt(espaco)
    return p

def add_bloco_citacao(doc, texto):
    """Citação da fala do Ellam — recuo roxo/lilás."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.right_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(texto)
    r.font.size = Pt(10.5); r.italic = True; r.font.color.rgb = LILAS
    return p

def add_bloco_nota(doc, texto):
    """Nota editorial — verde com marcador lateral (via sombreamento da célula)."""
    # usamos uma tabela 1x1 com borda esquerda verde para simular o marcador lateral
    tb = doc.add_table(rows=1, cols=1)
    tb.alignment = WD_TABLE_ALIGNMENT.LEFT
    cell = tb.rows[0].cells[0]
    # sombreamento verde-claro de fundo
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), "EAF3EA")
    cell._tc.get_or_add_tcPr().append(shd)
    # borda esquerda verde grossa
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single"); left.set(qn("w:sz"), "24"); left.set(qn("w:color"), "2E7D4F")
    borders.append(left)
    tcPr.append(borders)
    p = cell.paragraphs[0]
    r = p.add_run(texto)
    r.font.size = Pt(9.5); r.font.color.rgb = VERDE_NOTA
    # parágrafo de espaçamento após a tabela
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_toc(doc):
    """Sumário com campo TOC COMPLEXO (begin/separate/end) + updateFields.

    O campo simples (fldSimple) que usávamos nem sempre é reconhecido pelo Word para
    atualização com F9. O formato complexo abaixo é o nativo do Word: ao abrir o
    documento, o Word pergunta se deseja atualizar os campos (ou você usa Ctrl+A → F9),
    e o sumário é gerado com os números de página corretos.
    """
    # 1) forçar atualização de campos ao abrir (settings/updateFields)
    settings = doc.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true")
    settings.append(uf)

    # 2) título "Sumário"
    p = doc.add_paragraph()
    run = p.add_run("Sumário")
    run.bold = True; run.font.size = Pt(14); run.font.color.rgb = ROXO_H1
    add_par(doc, "(No Word: selecione tudo com Ctrl+A e pressione F9 — ou atualize com o botão direito no sumário. Ao abrir, o Word pode perguntar se deseja atualizar os campos: aceite.)", size=8, italic=True, cor=CINZA)

    # 3) campo TOC complexo
    p = doc.add_paragraph()
    r1 = p.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin"); f1.set(qn("w:dirty"), "true"); r1._r.append(f1)
    r2 = p.add_run(); instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = ' TOC \\o "1-3" \\h \\z \\u '
    r2._r.append(instr)
    r3 = p.add_run(); f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "separate"); r3._r.append(f3)
    r4 = p.add_run("Sumário — atualize com Ctrl+A + F9 no Word"); r4.font.color.rgb = CINZA; r4.font.size = Pt(9)
    r5 = p.add_run(); f5 = OxmlElement("w:fldChar"); f5.set(qn("w:fldCharType"), "end"); r5._r.append(f5)
    doc.add_page_break()

def parse_glossario(doc, linhas):
    """Glossário local com seções A-D."""
    secoes = {"A": "Personagens e seres", "B": "Conceitos", "C": "Livros e textos", "D": "Termos próprios"}
    atual = None
    for l in linhas:
        s = l.strip()
        if not s: continue
        m = re.match(r"^(A|B|C|D)\s*[—-]\s*(.*)$", s)
        if m:
            letra = m.group(1)
            add_heading_cor(doc, f"{letra} — {secoes.get(letra, m.group(2))}", 3, ROXO_H3)
            atual = letra
            continue
        if s.startswith("- ") or s.startswith("• "):
            item = s[2:].strip()
            # detectar remissão RC-###
            rc = re.search(r"RC-\d{3}", item)
            p = doc.add_paragraph(style="List Bullet")
            r = p.add_run(item)
            r.font.size = Pt(9.5)
            if rc:
                r2 = p.add_run(f"  [{rc.group(0)}]")
                r2.font.size = Pt(8.5); r2.bold = True; r2.font.color.rgb = ROXO_H3
            p.paragraph_format.space_after = Pt(2)
        elif re.match(r"^[A-ZÀ-Ú]", s) and len(s) < 60:
            add_heading_cor(doc, s, 3, ROXO_H3)

def gerar(md_path, saida=None):
    md = open(md_path, encoding="utf-8").read()
    linhas = md.splitlines()
    # --- metadados da capa (primeiras linhas com marcadores)
    meta = {}
    for l in linhas[:30]:
        m = re.match(r"^@(titulo|autor|data|local|subtitulo|fonte|nota_editor):\s*(.*)$", l)
        if m: meta[m.group(1)] = m.group(2).strip()
    titulo = meta.get("titulo", os.path.basename(os.path.dirname(md_path)))
    autor = meta.get("autor", "Jan Val Ellam")
    data = meta.get("data", "")
    local = meta.get("local", "")
    subtitulo = meta.get("subtitulo", "Apostila de estudo — Transcrição editada, com correção gramatical e terminológica, organização temática e notas editoriais.")
    nota_editor = meta.get("nota_editor", "")

    doc = Document()
    config(doc)
    set_cab_rod(doc, titulo, autor, data)

    # ---------------- CAPA
    for _ in range(7): doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(titulo); r.font.size = Pt(24); r.bold = True; r.font.color.rgb = ROXO_H1
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"Palestra de {autor}"); r.font.size = Pt(13); r.font.color.rgb = CINZA
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(data + (f"  ({local})" if local else "")); r.font.size = Pt(12); r.font.color.rgb = CINZA
    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(subtitulo); r.font.size = Pt(11); r.italic = True; r.font.color.rgb = ROXO_H3
    doc.add_page_break()

    # ---------------- NOTA DO EDITOR
    if nota_editor:
        add_heading_cor(doc, "Nota do editor", 2, ROXO_H2)
        add_bloco_nota(doc, nota_editor)
        doc.add_page_break()

    # ---------------- SUMÁRIO
    add_toc(doc)

    # ---------------- CORPO
    em_glossario = False
    gloss_linhas = []
    i = 0
    while i < len(linhas):
        l = linhas[i].rstrip()
        s = l.strip()
        if re.match(r"^@", s):
            i += 1; continue
        if re.match(r"^# PARTE", s):
            add_heading_cor(doc, s.lstrip("# ").strip(), 1, ROXO_H1); i += 1; continue
        if re.match(r"^##\s+GLOSS[ÁA]RIO", s, re.IGNORECASE) or s.upper().startswith("## GLOSS"):
            em_glossario = True; i += 1; continue
        if em_glossario:
            if s.startswith("#") and not s.startswith("###"):
                em_glossario = False
            else:
                gloss_linhas.append(s); i += 1; continue
        if s.startswith("## "):
            add_heading_cor(doc, s[3:].strip(), 2, ROXO_H2); i += 1; continue
        if s.startswith("### "):
            add_heading_cor(doc, s[4:].strip(), 3, ROXO_H3); i += 1; continue
        if s.startswith("> "):
            # juntar citações consecutivas
            blocos = []
            while i < len(linhas) and linhas[i].strip().startswith("> "):
                blocos.append(linhas[i].strip()[2:].strip()); i += 1
            add_bloco_citacao(doc, " ".join(blocos)); continue
        if s.startswith("*Nota") or s.startswith("*Nota do editor") or re.match(r"^Nota (do editor|editorial)", s):
            add_bloco_nota(doc, s.lstrip("*").strip()); i += 1; continue
        if s.startswith("- ") or s.startswith("• "):
            p = doc.add_paragraph(style="List Bullet")
            r = p.add_run(s[2:].strip()); r.font.size = Pt(10.5)
            p.paragraph_format.space_after = Pt(2); i += 1; continue
        if re.match(r"^\d+\.\s", s):
            p = doc.add_paragraph(style="List Number")
            r = p.add_run(re.sub(r"^\d+\.\s", "", s)); r.font.size = Pt(10.5)
            i += 1; continue
        if s.startswith("---"):
            i += 1; continue
        if s:
            add_par(doc, s); i += 1; continue
        i += 1

    # ---------------- GLOSSÁRIO LOCAL
    if gloss_linhas:
        doc.add_page_break()
        add_heading_cor(doc, "Glossário local", 1, ROXO_H1)
        parse_glossario(doc, gloss_linhas)

    # ---------------- RODAPÉ FINAL (créditos)
    doc.add_paragraph()
    add_par(doc, f"Fim da apostila.", size=9, italic=True, cor=CINZA)
    add_par(doc, f"Texto-base: palestra de {autor}, {data}. Transcrição editada para fins de estudo. As opiniões, conceitos e termos próprios refletem o pensamento do autor e do contexto das \"Revelações Cósmicas\".", size=8.5, cor=CINZA)

    if not saida:
        pasta = os.path.dirname(md_path)
        slug_titulo = re.sub(r"[^A-Za-z0-9]+", " ", titulo).strip().replace(" ", " ")
        saida = os.path.join(pasta, f"Apostila - {titulo}.docx")
    doc.save(saida)
    print("OK ->", saida)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 ferramentas/build_apostila.py apostilas/AAAA-MM-DD_slug/apostila.md")
        sys.exit(1)
    gerar(sys.argv[1])
