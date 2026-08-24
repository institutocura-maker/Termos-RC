#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica ampliações B042 lendo o arquivo de texto puro.

RAIZ = AQUI.parents[2] — rodar ANTES de mover a pasta para CONCLUIDOS/.
"""
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
TERMOS = RAIZ / "termos"
FONTE = AQUI / "_ampliacoes_B042.txt"

texto = FONTE.read_text(encoding="utf-8")
aplicadas = 0
sem_ficha = []
for bloco in texto.split("### "):
    bloco = bloco.strip()
    if not bloco:
        continue
    linha1, _, conteudo = bloco.partition("\n")
    if not linha1.startswith("RC-"):
        continue
    cod = linha1.strip()
    conteudo = conteudo.strip()
    alvo = next((f for f in TERMOS.glob(f"{cod}-*.md")), None)
    if not alvo:
        sem_ficha.append(cod)
        continue
    txt = alvo.read_text(encoding="utf-8")
    if "## Ampliação — B042" in txt:
        print("!! já ampliada:", cod)
        continue
    secao = (
        "\n## Ampliação — B042 (Crônicas de um Novo Tempo)\n\n"
        f"{conteudo}\n"
    )
    if "## Fontes" in txt:
        txt = txt.replace("## Fontes", secao + "\n## Fontes", 1)
    else:
        txt = txt.rstrip() + "\n" + secao + "\n---\n"
    alvo.write_text(txt, encoding="utf-8")
    aplicadas += 1
    print("ok", alvo.name)
print("fichas ampliadas:", aplicadas)
if sem_ficha:
    print("sem ficha:", ", ".join(sem_ficha))
