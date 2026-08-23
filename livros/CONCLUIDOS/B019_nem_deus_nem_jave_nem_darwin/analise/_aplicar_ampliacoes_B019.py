#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica ampliações B019 lendo o arquivo de texto puro."""
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
TERMOS = RAIZ / "termos"
FONTE = AQUI / "_ampliacoes_B019.txt"

texto = FONTE.read_text(encoding="utf-8")
blocos = texto.split("### ")
aplicadas = 0
sem_ficha = []
for bloco in blocos:
    bloco = bloco.strip()
    if not bloco:
        continue
    linha1, _, conteudo = bloco.partition("\n")
    if not linha1.startswith("RC-"):
        continue
    cod = linha1.strip()
    conteudo = conteudo.strip()
    if not conteudo:
        continue
    alvo = next((f for f in TERMOS.glob(f"{cod}-*.md")), None)
    if not alvo:
        sem_ficha.append(cod)
        continue
    txt = alvo.read_text(encoding="utf-8")
    if "## Ampliação — B019" in txt:
        print(f"!! já ampliada: {cod}")
        continue
    secao = f"\n## Ampliação — B019 (Nem Deus, nem Javé, nem Darwin)\n\n{conteudo}\n"
    if "## Fontes" in txt:
        txt = txt.replace("## Fontes", secao + "\n## Fontes", 1)
    else:
        txt = txt.rstrip() + "\n" + secao + "\n---\n"
    alvo.write_text(txt, encoding="utf-8")
    aplicadas += 1
    print("ok", alvo.name)

print(f"fichas ampliadas: {aplicadas}")
if sem_ficha:
    print("sem ficha física (não materializar):", ", ".join(sem_ficha))
