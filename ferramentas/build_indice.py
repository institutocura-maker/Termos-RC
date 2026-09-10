#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera indice-mestre.md a partir da tabela-mestra ferramentas/dados_termos.py.
Execute a partir de rc-terminologia/ :  python3 ferramentas/build_indice.py
"""
import glob as _glob
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from dados_termos import TERMOS

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "indice-mestre.md")
STATUS_EMOJI = {"candidato": "⚪", "provisório": "🟡", "em análise": "🟠", "verificado": "🟢"}

def slug(nome):
    s = nome.lower().replace("(", "").replace(")", "").replace("/", " ").replace("\\", " ")
    s = s.replace("á", "a").replace("ã", "a").replace("â", "a").replace("à", "a").replace("é", "e").replace("ê", "e")
    s = s.replace("í", "i").replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("ú", "u").replace("ç", "c")
    s = s.replace("´", "").replace("'", "").replace(":", "").replace("!", "").replace("—", "-").replace("–", "-")
    s = s.replace("ª", "a").replace("º", "o")
    s = s.replace(",", "").replace(";", "").replace(".", "").replace("=", "")
    s = " ".join(s.split())
    return s.replace(" ", "-")

TERMOS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "termos")
def ficha_link(cod, nome):
    # 10/09/2026: resolve o ARQUIVO REAL (o slug derivado errava 101/652 links).
    cand = sorted(_glob.glob(os.path.join(TERMOS_DIR, f"{cod}-*.md")))
    if len(cand) == 1:
        return f"[✔](termos/{os.path.basename(cand[0])})"
    return f"[✔](termos/{cod}-{slug(nome)}.md)"

lines = []
lines.append("# Índice Mestre — RC")
lines.append("")
lines.append("> Tabela com **todos** os termos do projeto. Termos com ficha completa têm link em `termos/`.")
lines.append("> Status: ⚪ candidato · 🟡 provisório (fonte publicada, aguardando revisão) · 🟠 em análise · 🟢 verificado.")
lines.append("> Gerado por `ferramentas/build_indice.py` a partir de `ferramentas/dados_termos.py` — **não editar à mão**.")
lines.append("")
lines.append("| Código | Termo | Categoria | Subcategoria | Status | Fontes | Relacionados | Ficha |")
lines.append("|---|---|---|---|---|---|---|---|")

# ordenar por categoria (grande grupo) e depois código
for cod, nome, cat, sub, status, fontes, rel, ficha in sorted(TERMOS, key=lambda t: t[0]):
    link = ficha_link(cod, nome) if ficha else "—"
    lines.append(f"| {cod} | {nome} | {cat} | {sub} | {STATUS_EMOJI[status]} | {', '.join(fontes) if fontes else '—'} | {rel} | {link} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## Como cresce este índice")
lines.append("")
lines.append("1. Cada PDF processado gera **candidatos** (⚪) e/ou **provisórios** (🟡) no `dados_termos.py`;")
lines.append("2. Termos centrais ganham **ficha completa** em `termos/` e o campo Ficha passa a `✔`;")
lines.append("3. Após revisão cruzada com as obras primárias de Ellam, o status evolui para 🟠 e depois 🟢;")
lines.append("4. Regenere a planilha e este índice com: `python3 ferramentas/build_xlsx.py && python3 ferramentas/build_indice.py`.")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"OK -> {OUT} ({len(TERMOS)} linhas)")
