#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: PRODUÇÃO — campanha do livro "O Universo e seu Criador" (Fase 3 · Compilação)
"""Verificador de compilação da Fase 3.

Confere os produtos finais da compilação (`livro.md` + DOCX) contra o contrato
(`README-contrato.md`, cláusulas 2 e 7) e o plano (§5 · Fase 3):

   1. produtos existem e abrem;
   2. árvore integral — 48 peças na ordem canônica (Abertura, 3 Partes, Fecho);
   3. regime de referência única — ZERO código RC-### / B### / P####-MM-DD no DOCX;
       ZERO selo de estágio (✔/✓) e ZERO rodapé de método / cabeçalho interno;
   4. 64 caixas "Na voz do autor" presentes (as caixas verbatim não são reabertas);
   5. a nota de referência única presente;
   6. capa: título "O Universo e seu Criador", autor "Jan Val Ellam",
       curadoria "Instituto Cura".

Uso:  python3 .arena/verifica_livro_compilacao.py
Saída: OK/falhas (exit code != 0 se falhar).
"""
import os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_LIVRO = os.path.join(RAIZ, "pedagogico", "livro")
MD = os.path.join(DIR_LIVRO, "livro.md")
DOCX = os.path.join(DIR_LIVRO, "O-Universo-e-seu-Criador.docx")

CODE_PAT = re.compile(r"(?:RC-\d{1,3}|B\d{3}|P\d{4}-\d{2}-\d{2}|F\d{3})")

falhas = []


def confere(cond, rotulo, extra=""):
    if not cond:
        falhas.append(f"[X] {rotulo} {extra}")


# ---------------------------------------------------------------- 1. existência
confere(os.path.isfile(MD), "livro.md existe", MD)
confere(os.path.isfile(DOCX), "DOCX existe", DOCX)
if not (os.path.isfile(MD) and os.path.isfile(DOCX)):
    print("\n".join(falhas) or "produtos ausentes")
    sys.exit(1)

# ---------------------------------------------------------------- 2. árvore no livro.md
md = open(MD, encoding="utf-8").read()
h1 = [l for l in md.split("\n") if l.startswith("# ")]
confere(len(h1) == 49, "livro.md tem 49 títulos H1", f"(achei {len(h1)})")
ordem = [h[2:].strip() for h in h1]
confere(ordem[0].startswith("ABERTURA"), "abre na Abertura")
confere(ordem[1].startswith("PARTE I"), "Parte I presente")
confere(ordem[10].startswith("PARTE II"), "Parte II presente")
confere(ordem[25].startswith("PARTE III"), "Parte III presente")
confere(ordem[-6].startswith("F.1"), "Fecho F.1 presente", ordem[-6])
confere(ordem[-1].startswith("F.6"), "Fecho F.6 presente", ordem[-1])
cap_num = [x for x in ordem if re.match(r"^\d+\.\s", x)]
confere(len(cap_num) == 38, "38 capítulos numerados", f"(achei {len(cap_num)})")

# ---------------------------------------------------------------- 3. DOCX via python-docx
from docx import Document
from docx.oxml.ns import qn

doc = Document(DOCX)


def all_text(parent):
    from docx.text.paragraph import Paragraph
    body = []
    for ch in parent.element.body.iterchildren():
        if ch.tag == qn('w:p'):
            body.append(Paragraph(ch, parent).text)
        elif ch.tag == qn('w:tbl'):
            for cell in ch.iter(qn('w:tc')):
                body.append("".join(t.text or "" for t in cell.iter(qn('w:t'))))
    return "\n".join(body)


full = all_text(doc)
confere(not CODE_PAT.search(full), "DOCX sem códigos de citação (RC-/B###/P####-MM-DD)")
confere(not re.search(r"[✔✓]", full), "DOCX sem selos de estágio (✔/✓)")
confere("Rodapé de método" not in full, "DOCX sem rodapé de método")
confere("Este arquivo é fonte de trabalho" not in full, "DOCX sem cabeçalho interno")
confere("fonte de trabalho" not in full, "DOCX sem 'fonte de trabalho'")
confere(full.count("**") == 0, "DOCX sem marcas md literais (**)")
confere("Todo o conteúdo deste livro provém dos Livros e Palestras de Jan Val Ellam" in full,
        "nota de referência única presente")

voz = sum(1 for t in doc.tables if "NA VOZ DO AUTOR" in
          " ".join(c.text for r in t.rows for c in r.cells))
confere(voz == 64, "64 caixas 'Na voz do autor'", f"(achei {voz})")

ps = [p.text for p in doc.paragraphs]
confere("O Universo e seu Criador" in ps[:20], "capa: título")
confere("Jan Val Ellam" in ps[:20], "capa: autor")
confere("Curadoria editorial: Instituto Cura" in ps[:20], "capa: curadoria")

# ---------------------------------------------------------------- relatório
if falhas:
    print("FALHAS DA COMPILAÇÃO:")
    for f in falhas:
        print("  ", f)
    sys.exit(1)
print("OK — compilação íntegra: árvore 48 peças · 64 caixas · regime de referência única · capa correta.")
