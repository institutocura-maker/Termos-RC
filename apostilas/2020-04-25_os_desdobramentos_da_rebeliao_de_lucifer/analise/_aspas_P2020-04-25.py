#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAÇA-ÂNCORAS de P2020-04-25 — nenhuma aspa digitada à mão.

Este módulo é a ÚNICA forma autorizada de obter uma citação desta fonte neste ciclo:
a âncora é dada em forma *frouxa* (sequência de palavras, sem rigor de acento, caixa ou
espaço), o texto real é localizado no `original.txt` e **devolvido byte a byte**, estendido
até fronteiras de frase. Se a âncora bate 0 ou >1 vez, o script aborta — é assim que o
ciclo se protege da memória de quem escreve (lição R-1…R-5b do ciclo P2023-10-14).

Uso:  from _aspas_P2020-04-25 import span, uaddr
      txt = span("Nós, os seres humanos", "o abismo para Javé")   # → aspa exata
"""
import os, re, sys, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
FONTE = os.path.join(CICLO, "original.txt")

RAW = open(FONTE, encoding="utf-8").read().replace("\r\n", "\n")
LINHAS = RAW.split("\n")
OFF = [0]
for _l in LINHAS:
    OFF.append(OFF[-1] + len(_l) + 1)

# --- texto normalizado (sem acento, minúsculo, espaço colapsado) com mapa p/ offsets reais ---
_norm_chars = []
_map = []
for i, ch in enumerate(RAW):
    if ch.isspace():
        _norm_chars.append(" ")
        _map.append(i)
        continue
    d = unicodedata.normalize("NFD", ch)
    base = "".join(c for c in d if not unicodedata.combining(c)).lower()
    for c in base or ch.lower():
        _norm_chars.append(c)
        _map.append(i)
# colapsa espaços duplicados mantendo o mapa (primeiro índice de cada corrida)
NORM = []
MAP = []
for c, i in zip(_norm_chars, _map):
    if c == " " and NORM and NORM[-1] == " ":
        continue
    NORM.append(c)
    MAP.append(i)
NORM = "".join(NORM)


def _re_norm(txt):
    out = []
    for ch in txt:
        if ch.isspace():
            out.append(r"\s+")
            continue
        d = unicodedata.normalize("NFD", ch)
        base = "".join(c for c in d if not unicodedata.combining(c)).lower()
        out.append(re.escape(base) if base else re.escape(ch.lower()))
    return "".join(out)


def uaddr(pos):
    """Endereço Uxxxx (1-based) do offset `pos` no bruto."""
    import bisect
    return f"U{bisect.bisect_right(OFF, pos):04d}"


def locate(loose, fim=None, modo="frase"):
    """Localiza a âncora frouxa e devolve (ini, fim_abs, texto_exato). Aborta se ambíguo."""
    ini = [m.start() for m in re.finditer(_re_norm(loose), NORM)]
    if len(ini) != 1:
        raise SystemExit(f"ÂNCORA '{loose[:48]}' → {len(ini)} ocorrência(s); deve ser exatamente 1")
    a = MAP[ini[0]]
    if fim:
        j = [m.start() for m in re.finditer(_re_norm(fim), NORM[ini[0]:])]
        if len(j) != 1:
            raise SystemExit(f"FIM '{fim[:48]}' após '{loose[:24]}' → {len(j)} ocorrência(s)")
        b = MAP[ini[0] + j[0]] + 0
        b = MAP[ini[0] + j[0]]
        # estende até o fim da frase que contém o termo final
        b = _fim_frase(b, fim)
    else:
        b = _fim_frase(a, loose)
    if modo == "frase":
        a = _ini_frase(a)
    return a, b, RAW[a:b].strip()


def _ini_frase(p):
    k = p
    for sep in (". ", "? ", "! ", ".\n", "?\n", "!\n"):
        q = RAW.rfind(sep, 0, p)
        if q != -1:
            k = max(k, q + len(sep))
    return k


def _fim_frase(p, anchor):
    q = p
    for w in anchor.split():
        q = RAW.lower().find(w[:6].lower(), q)
        if q == -1:
            q = p
            break
        q += len(w)
    best = q
    for sep in (". ", "? ", "! "):
        r = RAW.find(sep, q)
        if r != -1 and (best == q or r < best):
            best = r + 1
    return best


def span(loose, fim=None):
    return locate(loose, fim)[2]


if __name__ == "__main__":
    alvos = [a.split("\t") for a in sys.argv[1:]] or []
    for alvo in alvos:
        ini = alvo[0]
        fim = alvo[1] if len(alvo) > 1 else None
        a, b, txt = locate(ini, fim)
        print(f"### {uaddr(a)} · chars {a}–{b} · {b-a}c\n{txt}\n")
