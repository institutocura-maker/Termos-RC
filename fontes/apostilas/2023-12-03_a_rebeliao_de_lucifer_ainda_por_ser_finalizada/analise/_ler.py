#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Leitor de ranges do bruto — `_ler.py INI FIM` (1-based, chars).

Existe para que a leitura integral seja feita em mordidas com endereço verdadeiro em vez de
tamanho cego: cada saída traz `Uxxxx·offset` no início de cada parágrafo lido, de modo que
qualquer aspa anotada aqui já nasce endereçada. Não altera nada do arquivo.
"""
import os, sys, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, "_aspas_P2023-12-03.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
RAW = ASP.RAW
LIN = ASP.LINHAS

ini = int(sys.argv[1]) - 1 if len(sys.argv) > 1 else 0
fim = int(sys.argv[2]) if len(sys.argv) > 2 else len(RAW)
ini = max(0, min(ini, len(RAW)))
fim = max(ini, min(fim, len(RAW)))
n = 0
for i, l in enumerate(LIN):
    a, b = sum(len(x) + 1 for x in LIN[:i]), sum(len(x) + 1 for x in LIN[:i]) + len(l)
    if b <= ini or a >= fim:
        continue
    s = l.strip()
    if not s:
        continue
    lo, hi = max(a, ini), min(b, fim)
    corpo = l[lo - a:hi - a].strip()
    if not corpo:
        continue
    n += 1
    print(f"───── U{i + 1:04d} · chars {lo + 1:,}–{hi:,} · {hi - lo:,} desta leitura".replace(",", "."))
    print(corpo)
print(f"───── (leitura {n} linha(s) de fala; janela pedida {ini + 1:,}–{fim:,} de {len(RAW):,})".replace(",", "."))
