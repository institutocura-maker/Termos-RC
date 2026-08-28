#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTÃO C — verifica o que foi INJETADO NAS FICHAS contra o byte da fonte.

O pacote `_ampliacoes_P2020-04-25.txt` já passou pelo portão A (paridade) e pelo
portão B (verbatim) do `_verificar_verbatim_P2020-04-25.py`, e o próprio gerador do
pacote aborta se uma âncora cair em span bloqueado (D-1/D-4) ou contiver aspa vedada
(D-3). Este script fecha o círculo: relê as fichas ampliadas de `termos/`, extrai a
seção `## Ampliação — P2020-04-25` de cada uma e confere, citação por citação, que o
texto injetado continua sendo o texto da fonte — nem mais, nem menos.

Tokenização igual à do verificador do ciclo: pontuação e marcação markdown fora;
endereços `(U00xx)` ignorados; `[…]` são comentários meus e saem da aspa.
"""
import re, os, glob

AQUI = os.path.dirname(os.path.abspath(__file__))
import sys
if str(AQUI) not in sys.path: sys.path.insert(0, AQUI)
def _resolve_raiz(inicio):
    """Sobe até o diretório que contém `ferramentas/` — funciona antes e depois do
    engavetamento da pasta do ciclo em `apostilas/CONCLUIDAS/`."""
    d = os.path.abspath(inicio)
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d

RAIZ = _resolve_raiz(AQUI)
CICLO = AQUI.rsplit("/analise", 1)[0]
SECAO = "## Ampliação — P2020-04-25"


def tk(s):
    s = re.sub(r"[*_`]", " ", s)
    s = re.sub(r"\([^)]*U\d{4}\)", " ", s)          # endereço de fonte não é fala
    s = re.sub(r"\[[^\]]*\]", " ", s)               # colchetes editoriais
    return re.sub(r"\s+", " ", re.sub(r"[^0-9a-zA-ZÀ-ÿ]+", " ", s.replace("…", " "))).strip().lower()


src = " " + tk(open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n")) + " "
n_arq = n_cit = n_bad = 0
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    t = open(f, encoding="utf-8").read()
    i = t.find(SECAO)
    if i < 0:
        continue
    n_arq += 1
    j = t.find("\n## ", i + 10)
    sec = t[i:j if j > 0 else len(t)]
    for q in re.findall(r'"([^"]+)"', sec):
        q = q.replace("«", " ").replace("»", " ")
        if len(tk(q)) < 40:
            continue
        n_cit += 1
        if tk(q) not in src:
            n_bad += 1
            print("✗", os.path.basename(f), q[:80])
print(f"\nPORTÃO C — fichas com ampliação: {n_arq} · citações verificadas: {n_cit} · divergentes: {n_bad}")
print("RESULTADO:", "FICHA A FICHA, TUDO FIEL À FONTE ✓" if n_bad == 0 else "REVISAR ⚠️")
raise SystemExit(0 if n_bad == 0 else 1)
