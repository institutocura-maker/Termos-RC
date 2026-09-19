#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portão B do LIVRO (Fase 1) — verificador interno de trabalho.

Cada caixa «Na voz do autor» traz, na linha seguinte, «— *Título* (SIGLA)».
Este verificador:
  1. extrai, de cada capítulo em pedagogico/livro/capitulos/, os trechos entre «»;
  2. para cada trecho, identifica a SIGLA declarada na linha «— … (SIGLA)»;
  3. colapsa APENAS espaços/quebras de linha (hard-wrap) — sem tocar em
     caixa, acentos ou aspas;
  4. confere se o trecho colapsado é substring byte a byte do original.txt
     colapsado da obra declarada; se não for, vasculha todo o corpus e
     reporta onde estaria.

Não escreve nada em termos/ nem em ferramentas/. Uso:
    python3 .arena/verifica_livro_portao_b.py
"""
from __future__ import annotations

import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPS = os.path.join(RAIZ, "pedagogico", "livro", "capitulos")

SIGLA_RE = re.compile(r"—\s+\*.*\*\s+\(([^)]+)\)")
# ex.: B031, P2024-11-30, P2023-12-03, P2012-02-19
# exceções tratadas à mão: «dedicatória» e citações do glossário B031 (cap. 04)


def colapsar(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def limpa_box(bloco: str) -> str:
    """Remove marcadores de blockquote e quebras de linha, preservando o resto."""
    sem_marcador = re.sub(r"(?m)^\s*>\s?", "", bloco)
    return colapsar(sem_marcador)


def corpus() -> dict[str, str]:
    """sigla -> texto colapsado do original.txt."""
    out: dict[str, str] = {}
    for base in ("livros/CONCLUIDOS", "apostilas/CONCLUIDAS", "ciclos"):
        for dd in glob.glob(os.path.join(RAIZ, base, "*")):
            p = os.path.join(dd, "original.txt")
            if not os.path.exists(p):
                continue
            dname = os.path.basename(dd)
            sigla = dname.split("_")[0]
            if base == "livros/CONCLUIDOS":
                pass  # B031
            elif base == "ciclos":
                pass  # P2012-02-19 (já com P)
            else:  # apostilas: diretório 2017-05-14_... → P2017-05-14
                if sigla.startswith("P"):
                    pass
                else:
                    sigla = "P" + sigla
            with open(p, encoding="utf-8", errors="replace") as fh:
                out[sigla] = colapsar(fh.read())
    return out


def main() -> int:
    CORPUS = corpus()
    falhas = 0
    total = 0
    for cap in sorted(glob.glob(os.path.join(CAPS, "*.md"))):
        nome = os.path.basename(cap)
        if nome == "README.md":
            continue  # não é capítulo: cita trechos de forma documental, não é box verbatim
        with open(cap, encoding="utf-8") as fh:
            texto = fh.read()
        linhas = texto.split("\n")
        # acha blocos: linha de abertura do box, depois o trecho «...», depois a linha — (SIGLA)
        i = 0
        while i < len(linhas):
            if "«" not in linhas[i]:
                i += 1
                continue
            # acha o fecho do trecho (pode atravessar linhas)
            j = i
            while j < len(linhas) and "»" not in linhas[j]:
                j += 1
            if j >= len(linhas):
                i += 1
                continue
            bloco = "\n".join(linhas[i:j + 1])
            m = re.search(r"«(.*?)»", bloco, re.S)
            if not m:
                i = j + 1
                continue
            trecho = limpa_box(m.group(1))
            # procura a sigla nas linhas seguintes ao bloco
            sigla = None
            k = j + 1
            while k < min(j + 4, len(linhas)):
                sm = SIGLA_RE.search(linhas[k])
                if sm:
                    sigla = sm.group(1).strip()
                    break
                k += 1
            total += 1
            if sigla is None:
                # atribuições por nome (sem sigla) — cap. 04:
                contexto = "\n".join(linhas[j + 1:min(j + 4, len(linhas))])
                if "dedicatória" in contexto or "prefácio" in contexto:
                    sigla = "B031"
                else:
                    print(f"[SEM-SIGLA] {nome}: {trecho[:60]!r}")
                    falhas += 1
                    i = j + 1
                    continue
            fonte = CORPUS.get(sigla)
            if fonte is None:
                print(f"[OBRA-AUSENTE] {nome} ({sigla}): {trecho[:60]!r}")
                falhas += 1
                i = j + 1
                continue
            if trecho in fonte:
                print(f"[OK]  {nome} ({sigla})")
            else:
                # onde estaria no corpus?
                onde = [s for s, t in CORPUS.items() if trecho in t]
                print(f"[FALHA] {nome} ({sigla}): {trecho!r}")
                if onde:
                    print(f"       ... encontrado em: {onde}")
                else:
                    print("       ... não encontrado em obra alguma do corpus")
                falhas += 1
            i = j + 1
    print("\n===== RESULTADO =====")
    print(f"caixas conferidas: {total} · falhas: {falhas}")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
