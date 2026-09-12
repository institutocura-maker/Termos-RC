# -*- coding: utf-8 -*-
"""
# STATUS: ATIVO-ENCICLOPEDIA (linha verbetes, outro fluxo)
Gera o DOCX de registro do Indice da Enciclopedia (ed. 2026.1).

Conversor minimo e auditavel de Markdown -> DOCX: titulos (1-4), paragrafos,
listas com marcadores, citacoes em bloco, tabelas (com linha de cabecalho em
negrito), linhas horizontais e enfase inline (**negrito**, *italico*, `code`).

Nao altera a Base, `termos/`, `relacoes/` nem `dados_termos.py` — apenas le o
markdown gerado por `build_indice_enciclopedia.py`.

Uso: python3 ferramentas/build_indice_enciclopedia_docx.py
Depende de: python-docx
"""
import os
import re
import sys
import glob

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

from docx import Document  # noqa: E402
from docx.shared import Pt, RGBColor  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402

import dados_termos as d  # noqa: E402

MD = os.path.join(RAIZ, "pedagogico", "enciclopedia", "INDICE-ENCICLOPEDIA-RC.md")
DOCX = os.path.join(RAIZ, "pedagogico", "enciclopedia", "INDICE-ENCICLOPEDIA-RC.docx")

NIVEL = {1: "Title", 2: "Heading 1", 3: "Heading 2", 4: "Heading 3", 5: "Heading 4", 6: "Heading 4"}


def emitir_inline(par, texto):
    """Escreve um trecho de paragrafo interpretando **negrito**, *italico*, `code`."""
    padrao = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
    for pedaco in padrao.split(texto):
        if not pedaco:
            continue
        if pedaco.startswith("**") and pedaco.endswith("**") and len(pedaco) > 4:
            par.add_run(pedaco[2:-2]).bold = True
        elif pedaco.startswith("*") and pedaco.endswith("*") and len(pedaco) > 2:
            par.add_run(pedaco[1:-1]).italic = True
        elif pedaco.startswith("`") and pedaco.endswith("`") and len(pedaco) > 2:
            r = par.add_run(pedaco[1:-1])
            r.font.name = "Consolas"
            r.font.size = Pt(9)
        else:
            par.add_run(pedaco)


def linhas_tabela(md, i):
    """Devolve (cabecalho, corpo, proximo_indice) se a linha i abre uma tabela."""
    if not md[i].lstrip().startswith("|"):
        return None
    bloco = []
    j = i
    while j < len(md) and md[j].lstrip().startswith("|"):
        bloco.append(md[j].strip())
        j += 1
    def celulas(linha):
        return [c.strip() for c in linha.strip().strip("|").split("|")]
    cab = celulas(bloco[0])
    corpo = [celulas(l) for l in bloco[2:]]  # pula a linha separadora |---|
    return cab, corpo, j


def main():
    assert os.path.exists(MD), f"indice nao encontrado: {MD}"
    md = open(MD, encoding="utf-8").read().split("\n")

    doc = Document()
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"
    estilo.font.size = Pt(10.5)

    i, n_tab, n_h, n_li = 0, 0, 0, 0
    while i < len(md):
        linha = md[i].rstrip()
        strip = linha.strip()

        if not strip:
            i += 1
            continue

        # tabela
        if strip.startswith("|"):
            res = linhas_tabela(md, i)
            if res:
                cab, corpo, i = res
                tab = doc.add_table(rows=1, cols=len(cab))
                tab.style = "Table Grid"
                for k, txt in enumerate(cab):
                    cel = tab.rows[0].cells[k]
                    cel.text = ""
                    p = cel.paragraphs[0]
                    r = p.add_run(re.sub(r"\*\*|\*|`", "", txt))
                    r.bold = True
                    r.font.size = Pt(9)
                for ln in corpo:
                    cells = tab.add_row().cells
                    for k, txt in enumerate(ln[:len(cab)]):
                        cells[k].text = ""
                        emitir_inline(cells[k].paragraphs[0], txt)
                        for r in cells[k].paragraphs[0].runs:
                            r.font.size = Pt(9)
                n_tab += 1
                doc.add_paragraph()
                continue

        # titulo
        m = re.match(r"^(#{1,6})\s+(.*)$", strip)
        if m:
            nv = len(m.group(1))
            p = doc.add_heading(re.sub(r"\*\*|\*|`", "", m.group(2)), level=min(nv, 4))
            n_h += 1
            i += 1
            continue

        # linha horizontal
        if re.match(r"^-{3,}$", strip):
            i += 1
            continue

        # citacao em bloco
        if strip.startswith(">"):
            par = doc.add_paragraph(style="Intense Quote")
            emitir_inline(par, strip.lstrip("> ").strip())
            i += 1
            continue

        # lista
        if strip.startswith("- "):
            par = doc.add_paragraph(style="List Bullet")
            emitir_inline(par, strip[2:])
            n_li += 1
            i += 1
            continue

        # paragrafo
        par = doc.add_paragraph()
        emitir_inline(par, strip)
        i += 1

    # rodape de registro
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run(
        "Documento de registro gerado por ferramentas/build_indice_enciclopedia_docx.py — "
        "edição 2026.1 — Base: %d termos · %d fichas · %d relações."
        % (len(d.TERMOS), sum(1 for t in d.TERMOS if t[7]), len(d.RELACOES))
    )
    r.italic = True
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.save(DOCX)
    print("titulos : %d" % n_h)
    print("tabelas : %d" % n_tab)
    print("itens   : %d" % n_li)
    print("OK -> %s (%d KB)" % (os.path.relpath(DOCX, RAIZ), os.path.getsize(DOCX) // 1024))
    print("Base intacta: %d termos · %d fichas · %d relacoes"
          % (len(d.TERMOS), sum(1 for t in d.TERMOS if t[7]), len(d.RELACOES)))


if __name__ == "__main__":
    main()
