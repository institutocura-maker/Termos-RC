#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: PRODUÇÃO — campanha do livro "O Universo e seu Criador" (Fase 3 · Compilação)
"""Compila o livro "O Universo e seu Criador" a partir das fontes de capítulo.

Fase 3 do `pedagogico/livro/PLANO-LIVRO-UNIVERSO-E-SEU-CRIADOR.md` (despacho único):
    1. `pedagogico/livro/livro.md`            — o livro integrado (38 capítulos + Fecho F.1–F.6)
    2. `pedagogico/livro/O-Universo-e-seu-Criador.docx` — a obra acabada (formato final SÓ DOCX)

Regras de compilação (contrato `README-contrato.md`, cláusulas 2 e 7):
    - REGIME DE REFERÊNCIA ÚNICA: o corpo do livro NÃO exibe códigos `RC-###`, selos de
      status nem grades de fonte por trecho. Estes são removidos na compilação.
    - REMOVIDO da página (patrimônio interno): o bloco "**Este arquivo é fonte de
      trabalho…" (a cada capítulo) e o "Rodapé de método (auditoria interna)" do fim de
      cada arquivo.
    - PRESERVADA a caixa "Na voz do autor" (verbatim conferido) — sem o código entre
      parênteses na atribuição (ex.: "— *O Drama Cósmico de Javé* (B001)" vira
      "— O Drama Cósmico de Javé"). A caixa é a única citação literal do livro.
    - A atribuição passa a ser GLOBAL (uma única nota editorial — ABERTURA A.4).

Uso:  python3 ferramentas/build_livro.py
"""
import os, re, glob
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_LIVRO = os.path.join(RAIZ, "pedagogico", "livro")
DIR_CAP = os.path.join(DIR_LIVRO, "capitulos")
SAIDA_MD = os.path.join(DIR_LIVRO, "livro.md")
SAIDA_DOCX = os.path.join(DIR_LIVRO, "O-Universo-e-seu-Criador.docx")

# ---------------------------------------------------------------- identidade da obra
TITULO = "O Universo e seu Criador"
SUBTITULO = "Uma história do antes da Criação aos dias de hoje"
SUB_COVER = "Uma história do antes da Criação aos dias de hoje"
AUTOR = "Jan Val Ellam"
CURADORIA = "Curadoria editorial: Instituto Cura"
EDICAO = "Edição de trabalho · 2026.1"

NOTA_REFERENCIA = ("Todo o conteúdo deste livro provém dos Livros e Palestras de "
                   "Jan Val Ellam — a Revelação Cósmica. Nada aqui é apresentado como "
                   "consenso científico, religioso ou acadêmico: é a leitura do autor, "
                   "oferecida ao estudo.")

PALAVRAS_NOVAS = "Palavras novas desta parte"   # mini-título de fim de capítulo (fica)

# ---------------------------------------------------------------- cores (convenções do repositório)
ROXO_H1 = RGBColor(0x33, 0x1A, 0x55)   # #331A55 título de parte
ROXO_H2 = RGBColor(0x44, 0x22, 0x66)   # #442266 capítulo
ROXO_H3 = RGBColor(0x55, 0x33, 0x77)   # #553377 seção
VERDE_NOTA = RGBColor(0x2E, 0x7D, 0x4F) # #2E7D4F nota editorial
LILAS = RGBColor(0x6A, 0x3D, 0x8C)      # #6A3D8C citação "Na voz do autor"
CINZA = RGBColor(0x55, 0x55, 0x55)


# ================================================================ 1. LIMPEZA DO MD
# O regime de referência única (contrato §2.1/§7) vive aqui: o leitor não vê códigos
# RC-### / B### / P####-MM-DD, nem grades de fonte por trecho. As fontes
# (capitulos/*.md) permanecem intactas — a limpeza é feita SÓ na compilação.
CODE_PAT = re.compile(r"(?:RC-\d{1,3}(?:/RC-\d{1,3})*|B\d{3}|P\d{4}-\d{2}-\d{2}|F\d{3})")
PAREN = re.compile(r"\(([^()]*)\)")


def _tem_codigo(s):
    return bool(CODE_PAT.search(s))


def _estrutural(s):
    """Linha de bloco (não é prosa): quebras de parágrafo, títulos, tabelas, listas."""
    st = s.lstrip()
    return (not st or st.startswith((">", "#", "|", "-", "`", "!", "@"))
            or re.match(r"^\d+\.\s", st))


def _juntar_continuacoes(linhas):
    """Junta linhas de prosa partidas no meio de um parêntese de citação.

    Dois casos: (a) a linha anterior ficou com '(' sem fechar; (b) a linha começa com
    '(' (o parêntese de citação abriu na quebra de linha). Só toca em prosa — nunca em
    blockquote (verbatim), títulos, tabelas ou listas."""
    res = []
    for l in linhas:
        st = l.strip()
        if not res or st == "" or _estrutural(st):
            res.append(l)
            continue
        prev = res[-1]
        pst = prev.strip()
        if pst == "" or _estrutural(pst):
            res.append(l)
            continue
        if st.startswith("("):                      # (b) abre na quebra
            res[-1] = prev.rstrip() + " " + st
            continue
        if prev.count("(") > prev.count(")"):       # (a) ficou aberto
            res[-1] = prev.rstrip() + " " + st
            continue
        res.append(l)
    return res


def _filtrar_parenteses(l):
    """Remove códigos de citação DENTRO de parênteses; preserva o resto do parêntese.

    Parênteses sem código são preservados byte a byte (verbatim intocado)."""
    def repl(m):
        inner = m.group(1)
        if not _tem_codigo(inner):
            return m.group(0)
        pedacos = []
        for p in re.split(r"[,;/]", inner):
            limpo = CODE_PAT.sub("", p)
            # remove sobras de conjunção/separação deixadas pelo código removido
            limpo = re.sub(r"[\s—–/-]+$", "", limpo).strip()
            limpo = re.sub(r"^\s*[/-]+", "", limpo).strip()
            limpo = re.sub(r"\s+(?:e|ou)$", "", limpo).strip()
            if limpo:
                pedacos.append(limpo)
        recon = ", ".join(pedacos)
        return f"({recon})" if recon else ""
    return PAREN.sub(repl, l)


def _limpeza_pontuacao(l):
    """Corrige detritos de pontuação deixados pela remoção de parênteses."""
    l = re.sub(r"\s+([.,;:!?])", r"\1", l)
    l = re.sub(r"\(\s+", "(", l)
    l = re.sub(r"\s+\)", ")", l)
    l = re.sub(r"[—–]\s*:", "—", l)          # "— (RC-918): a ideia" -> "— a ideia"
    l = re.sub(r"\s{2,}", " ", l)
    return l


def _reescritas(l):
    """Ajustes pontuais de prosa em que o código estava entranhado na frase."""
    s = l
    # cap. 25: "o drama do Criador — o B002 — e" -> "o drama do Criador — e"
    s = re.sub(r"[—–]\s*(?:o |a |do |da )?B\d{3}\s*[—–]", "—", s)
    # cap. 23: "na descrição da ficha RC-771," -> "na descrição da ficha,"
    s = re.sub(r"\bficha\s+RC-\d{1,3}", "ficha", s)
    # cap. 14: aparato leve -> voz de leitor
    s = s.replace("cada item é fichado na Base e voltará em capítulos",
                  "cada item tem registro no acervo e voltará em capítulos")
    return s


def _reescrita_f6_par(linhas):
    """F.6: a menção à 'ficha RC-717' atravessa duas linhas — reescreve o par."""
    for i in range(len(linhas)):
        if "refletindo a ficha RC-717" in linhas[i]:
            linhas[i] = re.sub(
                r"— refletindo a ficha RC-717, que guarda a\s*$",
                "— refletindo a marca da mesma divergência preservada pela fonte.",
                linhas[i])
            if i + 1 < len(linhas) and linhas[i + 1].strip() == "marca da mesma divergência.":
                linhas[i + 1] = ""
            break
    return linhas


def sanitizar(linhas):
    """Corpo de capítulo -> linhas prontas para o leitor (sem aparato de citação)."""
    linhas = _juntar_continuacoes(linhas)
    linhas = _reescrita_f6_par(linhas)
    out = []
    i = 0
    while i < len(linhas):
        l = linhas[i]
        s = l.strip()
        # nota-meta das eras (cap. 29): linha inteira + continuação — fora da página
        if s.startswith("(Sumário da régua consolidada na Base RC"):
            i += 1
            if i < len(linhas) and linhas[i].strip().startswith("e de "):
                i += 1
            continue
        if s.startswith(">"):
            # blockquote: só tira os códigos da atribuição; nunca mexe no verbatim
            out.append(re.sub(r"^(>\s*#{1,6}\s*)[✔✓]\s*", r"\1", _filtrar_parenteses(l)))
        elif s.startswith("#"):
            # títulos: remove glifos de selo de estágio (✔ / ✓) — o contrato não exibe selos
            out.append(re.sub(r"^(#{1,6}\s*)[✔✓]\s*", r"\1", l))
        elif s:
            out.append(_limpeza_pontuacao(_filtrar_parenteses(_reescritas(l))))
        else:
            out.append(l)
        i += 1
    return out


# ================================================================ 2. FONTES
def ordem_fontes():
    """Ordem canônica: 00–38 (numérica), depois F1–F6. Retorna [(basename, path)]."""
    tudo = [f for f in sorted(glob.glob(os.path.join(DIR_CAP, "*.md")))
            if os.path.basename(f) != "README.md"]
    numericos = [f for f in tudo if re.match(r"\d\d-", os.path.basename(f))]
    fecho = [f for f in tudo if re.match(r"F\d-", os.path.basename(f))]
    numericos = sorted(numericos, key=lambda p: int(os.path.basename(p)[:2]))
    fecho = sorted(fecho, key=lambda p: os.path.basename(p))
    if len(numericos) != 39 or len(fecho) != 6:
        raise SystemExit(f"ERRO: esperava 39 capítulos (00–38) + 6 do Fecho; "
                         f"achei {len(numericos)} + {len(fecho)}.")
    return [(os.path.basename(p), p) for p in numericos + fecho]


def limpar_arquivo(caminho):
    """Retorna a lista de linhas do arquivo PRONTA PARA O LEITOR.

    Remove o bloco de cabeçalho interno ('Este arquivo é fonte de trabalho…'), o
    'Rodapé de método' final e o aparato de citação do corpo (códigos RC/B/P das
    citações inline e das listas 'Palavras novas'). Não reforma o conteúdo."""
    linhas = open(caminho, encoding="utf-8").read().split("\n")
    saida = []
    i = 0
    while i < len(linhas):
        s = linhas[i].strip()
        # ---- bloco de cabeçalho interno: "> **Este arquivo é fonte de trabalho…"
        if s.startswith("> **Este arquivo"):
            i += 1
            # consome as linhas seguintes do mesmo blockquote (não há, mas por segurança)
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                i += 1
            continue
        # ---- rodapé de método: tudo daqui até o fim do arquivo é auditoria interna
        if re.match(r"^\*\*Rodapé de método", s):
            break
        saida.append(linhas[i])
        i += 1
    return sanitizar(saida)


# ================================================================ 2. RENDER DE TEXTO
# Renders de texto com estado (correto para formatação que ATRAVESSA a quebra de
# linha suave das fontes — o watchdog de reflow junta as linhas de um parágrafo
# antes de renderizar, e o estado bold/italic persiste ao longo do fluxo).


def add_inline(p, texto, size=10.5, base_bold=False, base_italic=False, cor=None,
               state=None):
    """Tokenizador de formatação com estado (``**`` = bold, ``*`` = italic, `` ` `` = code).

    `state` (dict) permite que um `**` aberto numa linha feche na seguinte."""
    if state is None:
        state = {"bold": False, "italic": False}
    i, n = 0, len(texto)
    while i < n:
        ch = texto[i]
        if ch == "*":
            if i + 1 < n and texto[i + 1] == "*":
                state["bold"] = not state["bold"]
                i += 2
            else:
                state["italic"] = not state["italic"]
                i += 1
            continue
        if ch == "`":
            j = texto.find("`", i + 1)
            if j == -1:
                j = n
            r = p.add_run(texto[i + 1:j])
            r.font.name = "Consolas"
            r._element.rPr.rFonts.set(qn("w:eastAsia"), "Consolas")
            r.font.size = Pt(size - 1)
            if cor is not None:
                r.font.color.rgb = cor
            i = j + 1
            continue
        j = i
        while j < n and texto[j] not in "*`":
            j += 1
        if j > i:
            r = p.add_run(texto[i:j])
            r.font.size = Pt(size)
            r.bold = bool(state["bold"]) or base_bold
            r.italic = bool(state["italic"]) or base_italic
            if cor is not None:
                r.font.color.rgb = cor
        i = j
    return state


def limpar_codigo_citacao(texto):
    """Remove o código `(B001)` / `(P2024-02-25)` do fim de uma atribuição:
    '— *O Drama Cósmico de Javé* (B001)' -> '— O Drama Cósmico de Javé'."""
    return re.sub(r"\s*\((?:B\d{3}|P\d{4}-\d{2}-\d{2})\)\s*$", "", texto).strip()


def classificar_bloco(bloco):
    """Classifica um bloco de citação Markdown (`>`).

    Retorna dict: {tipo, header, corpo(lista), atribuicao(lista)}."""
    if not bloco:
        return {"tipo": "vazio"}
    linhas = [l for l in bloco]  # l já sem o '>'
    primeiro = linhas[0].strip()
    if primeiro.startswith("**Este arquivo"):
        return {"tipo": "ignorar"}
    # caixa "Na voz do autor"
    if primeiro == "**Na voz do autor**" or primeiro.startswith("**Na voz do autor** —"):
        if " — " in primeiro:
            texto_resto = primeiro.split(" — ", 1)[1]
            return {"tipo": "callout", "header": None, "corpo": [texto_resto], "atribuicao": []}
        corpo, atrib = [], []
        for l in linhas[1:]:
            if re.match(r"^\s*(—|–)\s", l):
                atrib.append(limpar_codigo_citacao(re.sub(r"^\s*(—|–)\s*", "", l)))
            elif l.strip():
                corpo.append(l.strip())
        return {"tipo": "voz", "header": "Na voz do autor",
                "corpo": corpo, "atribuicao": atrib}
    # checkpoint com marca #### ### dentro do bloco (Abertura)
    if primeiro.startswith("### "):
        return {"tipo": "checkpoint", "header": primeiro[4:].strip().lstrip("✔ ").strip(),
                "corpo": [l for l in linhas[1:] if l.strip()], "atribuicao": []}
    # checkpoint das partes (bloco *Checkpoint da Parte X — …)
    m = re.match(r"^\*?Checkpoint da (Parte [IVX]+)\s*—\s*(.*)$", primeiro)
    if m:
        corpo = [m.group(2).strip()] + [l.strip() for l in linhas[1:] if l.strip()]
        return {"tipo": "checkpoint", "header": f"Checkpoint da {m.group(1)}",
                "corpo": corpo, "atribuicao": []}
    # demais blocos (destaque da tese, equações-gancho, "como ler", recaps)
    corpo, atrib = [], []
    for l in linhas:
        if re.match(r"^\s*(—|–)\s", l):
            atrib.append(limpar_codigo_citacao(re.sub(r"^\s*(—|–)\s*", "", l)))
        elif l.strip():
            corpo.append(l.strip())
    return {"tipo": "callout", "header": None, "corpo": corpo, "atribuicao": atrib}


# ================================================================ 3. livro.md
def _reflow(linhas):
    """Junta linhas de prosa contíguas (quebra de linha suave das fontes) num só
    parágrafo, para o Markdown integrar e para o DOCX renderizar sem marcas partidas.

    Preserva: linhas vazias, títulos, blockquotes, tabelas, listas, '---' e o
    mini-título 'Palavras novas'."""
    saida = []
    buf = []
    for l in linhas:
        s = l.strip()
        brk = (s == "" or s == "---" or s.startswith(("#", ">", "|"))
               or re.match(r"^-\s", s) or re.match(r"^\d+\.\s", s)
               or s.strip("*").strip() == PALAVRAS_NOVAS)
        if brk:
            if buf:
                saida.append(" ".join(buf).strip())
                buf = []
            saida.append(l)
        else:
            buf.append(s)
    if buf:
        saida.append(" ".join(buf).strip())
    return saida


def montar_livro_md():
    partes = []
    for nome, caminho in ordem_fontes():
        texto = "\n".join(_reflow(limpar_arquivo(caminho))).strip("\n")
        partes.append(texto)
    return "\n\n".join(partes).strip() + "\n"


# ================================================================ 4. DOCX
def config(doc):
    for s in doc.sections:
        s.top_margin = Cm(2.2); s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(2.4); s.right_margin = Cm(2.0)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")


def set_cab_rod(doc):
    sec = doc.sections[0]
    hdr = sec.header.paragraphs[0]
    hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = hdr.add_run(f"{TITULO}  ·  {AUTOR}")
    r.font.size = Pt(8); r.font.color.rgb = CINZA
    ftr = sec.footer.paragraphs[0]
    ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = ftr.add_run(f"{CURADORIA} — página ")
    r.font.size = Pt(8); r.font.color.rgb = CINZA
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    ftr._p.append(fld)


def add_heading_cor(doc, texto, nivel, cor, size):
    h = doc.add_heading("", level=nivel)
    run = h.add_run(texto)
    run.font.color.rgb = cor
    run.font.size = Pt(size)
    run.font.bold = True
    h.paragraph_format.space_before = Pt(14 if nivel == 1 else 10)
    h.paragraph_format.space_after = Pt(6)
    return h


def add_runs(p, texto, size=10.5, base_bold=False, base_italic=False, cor=None,
             state=None):
    return add_inline(p, texto, size=size, base_bold=base_bold, base_italic=base_italic,
                      cor=cor, state=state)


def add_par(doc, texto, size=10.5, italic=False, cor=None, espaco=6, alinhar=None):
    p = doc.add_paragraph()
    if alinhar:
        p.alignment = alinhar
    add_runs(p, texto, size=size, base_italic=italic, cor=cor)
    p.paragraph_format.space_after = Pt(espaco)
    return p


def caixa(doc, *, header=None, corpo=None, atribuicao=None, cor_borda=LILAS,
          fill="F5EEF9", size=10.5, central=False, header_cor=ROXO_H3):
    """Bloco de destaque: moldura 1x1 com borda esquerda e fundo suave."""
    corpo = corpo or []
    tb = doc.add_table(rows=1, cols=1)
    cell = tb.rows[0].cells[0]
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for lado in ("top", "bottom", "right"):
        el = OxmlElement(f"w:{lado}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:color"), "D9D9D9")
        borders.append(el)
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single"); left.set(qn("w:sz"), "24"); left.set(qn("w:color"), "%02X%02X%02X" % (cor_borda[0], cor_borda[1], cor_borda[2]))
    borders.append(left)
    tcPr.append(borders)

    first_p = True
    st = {"bold": False, "italic": False}
    if header:
        p = cell.paragraphs[0]
        first_p = False
        rr = p.add_run(header.upper())
        rr.bold = True; rr.font.size = Pt(8.5); rr.font.color.rgb = header_cor
        p.paragraph_format.space_after = Pt(3)
    for txt in corpo:
        p = cell.paragraphs[0] if first_p else cell.add_paragraph()
        first_p = False
        if central:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_runs(p, f"{txt.strip()}  ", size=size, state=st)
        p.paragraph_format.space_after = Pt(2)
    for a in (atribuicao or []):
        p = cell.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rr = p.add_run(f"— {a}")
        rr.font.size = Pt(8.5); rr.italic = True; rr.font.color.rgb = CINZA
        p.paragraph_format.space_after = Pt(2)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def add_toc(doc):
    settings = doc.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true")
    settings.append(uf)
    p = doc.add_paragraph()
    run = p.add_run("Sumário")
    run.bold = True; run.font.size = Pt(16); run.font.color.rgb = ROXO_H1
    add_par(doc, "(No Word: selecione tudo com Ctrl+A e pressione F9 — os números de "
                 "página e entradas serão montados a partir dos títulos do livro.)",
            size=8, italic=True, cor=CINZA, espaco=6)
    p = doc.add_paragraph()
    r1 = p.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin"); f1.set(qn("w:dirty"), "true"); r1._r.append(f1)
    r2 = p.add_run(); instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = ' TOC \\o "1-3" \\h \\z \\u '
    r2._r.append(instr)
    r3 = p.add_run(); f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "separate"); r3._r.append(f3)
    r4 = p.add_run("Sumário — atualize com Ctrl+A + F9 no Word"); r4.font.color.rgb = CINZA; r4.font.size = Pt(9)
    r5 = p.add_run(); f5 = OxmlElement("w:fldChar"); f5.set(qn("w:fldCharType"), "end"); r5._r.append(f5)
    doc.add_page_break()


def _tabela(doc, bloco):
    def celulas(linha):
        return [c.strip() for c in linha.strip().strip("|").split("|")]
    cab = celulas(bloco[0])
    corpo = [celulas(l) for l in bloco[2:]]
    ncols = len(cab)
    tb = doc.add_table(rows=1, cols=ncols)
    try:
        tb.style = "Table Grid"
    except KeyError:
        pass
    tb.autofit = True

    def preencher(cel, texto, negrito=False):
        cel.text = ""
        p = cel.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        add_inline(p, texto, size=9.5, base_bold=negrito)
    for j, txt in enumerate(cab):
        preencher(tb.rows[0].cells[j], txt, negrito=True)
    for linha in corpo:
        cells = tb.add_row().cells
        for j in range(ncols):
            preencher(cells[j], linha[j] if j < len(linha) else "")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def render_docx():
    doc = Document()
    config(doc)
    set_cab_rod(doc)

    # ---------------- CAPA
    for _ in range(7):
        doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(TITULO); r.font.size = Pt(27); r.bold = True; r.font.color.rgb = ROXO_H1
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(SUB_COVER); r.font.size = Pt(14); r.italic = True; r.font.color.rgb = ROXO_H3
    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(AUTOR); r.font.size = Pt(15); r.bold = True; r.font.color.rgb = CINZA
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("" + CURADORIA); r.font.size = Pt(11); r.font.color.rgb = CINZA
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(EDICAO); r.font.size = Pt(9.5); r.font.color.rgb = CINZA
    doc.add_page_break()

    # ---------------- NOTA DE REFERÊNCIA (a única, perene)
    add_heading_cor(doc, "Nota de referência", 1, ROXO_H1, 16)
    caixa(doc, header="Nota de referência", corpo=[NOTA_REFERENCIA],
          cor_borda=VERDE_NOTA, fill="EAF3EA", header_cor=VERDE_NOTA, size=10.5)
    doc.add_page_break()

    # ---------------- SUMÁRIO (campo TOC)
    add_toc(doc)

    # ---------------- CORPO
    for nome, caminho in ordem_fontes():
        linhas = limpar_arquivo(caminho)
        i = 0
        n = len(linhas)

        def _parada(s2):
            return (s2 == "" or s2 == "---"
                    or s2.startswith(("#", "|", ">"))
                    or re.match(r"^-\s", s2) or re.match(r"^\d+\.\s", s2))

        while i < n:
            s = linhas[i].strip()
            # ---- blockquote (caixa "Na voz do autor" / checkpoint / callout)
            if s.startswith(">"):
                bloco = []
                while i < n and linhas[i].strip().startswith(">"):
                    bloco.append(linhas[i].strip()[1:].strip()); i += 1
                info = classificar_bloco(bloco)
                if info["tipo"] == "voz":
                    caixa(doc, header="Na voz do autor", corpo=info["corpo"],
                          atribuicao=info["atribuicao"], cor_borda=LILAS,
                          fill="F5EEF9", header_cor=LILAS, size=10.5)
                elif info["tipo"] == "checkpoint":
                    caixa(doc, header=info["header"], corpo=info["corpo"],
                          cor_borda=VERDE_NOTA, fill="EAF3EA",
                          header_cor=VERDE_NOTA, size=10.5)
                elif info["tipo"] == "callout":
                    caixa(doc, corpo=info["corpo"], atribuicao=info["atribuicao"],
                          cor_borda=ROXO_H2, fill="F1ECF7", header_cor=ROXO_H2, size=10.5)
                continue
            # ---- tabela
            if s.startswith("|"):
                bl = []
                while i < n and linhas[i].strip().startswith("|"):
                    bl.append(linhas[i].strip()); i += 1
                eh_tabela = (len(bl) >= 2 and "-" in bl[1]
                             and re.match(r"^\|[\s:|-]+\|$", bl[1]))
                if eh_tabela:
                    _tabela(doc, bl)
                else:
                    for l in bl:
                        add_par(doc, l, size=9.5)
                continue
            # ---- régua horizontal
            if s == "---":
                i += 1
                continue
            # ---- títulos (H1..H4)
            mh = re.match(r"^(#{1,4})\s+(.*)$", s)
            if mh:
                nivel = len(mh.group(1))
                txt = mh.group(2).strip()
                txt = re.sub(r"[*_]{1,2}", "", txt).strip()   # título não carrega marcas md
                if nivel == 1 and txt.upper().startswith(("PARTE ", "FECHO")):
                    doc.add_page_break()
                cor = {1: ROXO_H1, 2: ROXO_H2, 3: ROXO_H3, 4: ROXO_H3}[nivel]
                sz = {1: 16, 2: 13, 3: 11.5, 4: 11}[nivel]
                add_heading_cor(doc, txt, nivel, cor, sz)
                i += 1
                continue
            # ---- mini-título "Palavras novas desta parte"
            if s.strip("*").strip() == PALAVRAS_NOVAS:
                p = doc.add_paragraph()
                r = p.add_run(PALAVRAS_NOVAS)
                r.bold = True; r.font.size = Pt(11); r.font.color.rgb = ROXO_H3
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
                i += 1
                continue
            # ---- item de lista (bullets/números), com continuação de linha
            if s.startswith("- ") or re.match(r"^\d+\.\s", s):
                eh_num = bool(re.match(r"^\d+\.\s", s))
                item = s[2:].strip() if s.startswith("- ") else re.sub(r"^\d+\.\s", "", s).strip()
                i += 1
                buf = [item]
                while i < n and linhas[i].strip() and not _parada(linhas[i].strip()):
                    buf.append(linhas[i].strip()); i += 1
                p = doc.add_paragraph(style="List Number" if eh_num else "List Bullet")
                add_inline(p, " ".join(buf).strip(), size=10.5)
                p.paragraph_format.space_after = Pt(2)
                continue
            # ---- parágrafo de prosa (reflow das quebras de linha suaves)
            if s:
                buf = [s]; i += 1
                while i < n and linhas[i].strip() and not _parada(linhas[i].strip()):
                    buf.append(linhas[i].strip()); i += 1
                add_par(doc, " ".join(buf).strip())
                continue
            i += 1

    # ---------------- RODAPÉ FINAL (créditos da obra)
    doc.add_page_break()
    add_heading_cor(doc, "Sobre esta edição", 1, ROXO_H1, 16)
    add_par(doc, "Fim do livro.", size=9, italic=True, cor=CINZA)
    add_par(doc, NOTA_REFERENCIA, size=9, cor=CINZA)
    add_par(doc, f"Autoria da matéria: {AUTOR}. {CURADORIA}. {EDICAO}.",
            size=9, cor=CINZA)
    doc.save(SAIDA_DOCX)
    print("OK ->", SAIDA_DOCX)


if __name__ == "__main__":
    md = montar_livro_md()
    with open(SAIDA_MD, "w", encoding="utf-8") as fh:
        fh.write(md)
    print("OK ->", SAIDA_MD, f"({len(md.splitlines())} linhas)")

    # ---- guarda de vazamento (regime de referência única): se qualquer código de
    # citação ou grade de fonte chegar ao produto final, o build FALHA com relatório.
    vazamento = [f"L{n+1}: {l.strip()[:120]}" for n, l in
                 enumerate(md.split("\n"))
                 if CODE_PAT.search(l) or "Rodapé de método" in l
                 or "Este arquivo é fonte de trabalho" in l]
    if vazamento:
        print("FALHA DE COMPILAÇÃO — aparato de citação vazou para o produto:")
        for v in vazamento:
            print("   ", v)
        raise SystemExit(1)

    render_docx()
    print("Compilação da Fase 3 concluída.")
