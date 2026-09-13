#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO (U43+) — aplica o V a um lote de códigos e regenera o frontmatter.
"""Aplica a chancela (V) a códigos já materializados: `provisório` → `verificado`.

Despacho do Curador (13/09/2026): «pode aplicar_V em todos os termos» do lote 1
da família B e dos próximos, com a regra de **presunção de V por fonte de livro**
(`diagnostico/DESPACHO-V-POR-FONTE-DE-LIVRO-2026-09-13.md`).

O V é aplicado em duas escritas, nesta ordem:
  1. o cadastro (região `TERMOS`) — status `P` → `"verificado"`;
  2. o frontmatter de cada ficha — **regenerado por `motor.fm_toml`** contra o
     registro já virado (T13/T15), preservando o corpo da carta;
  3. a nota de status no corpo, trocada pela nota do V.
`RELACOES` nunca é tocado.

Uso
    python3 ferramentas/aplicar_v.py RC-085 RC-066 ... [--via "nota de origem do V"]
"""
from __future__ import annotations

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))

import motor as _m                                              # noqa: E402
import dados_termos as _d                                       # noqa: E402

CADASTRO = os.path.join(RAIZ, "ferramentas", "dados_termos.py")

NOTA_NASCENCA = re.compile(r"^- \*\*Status de nascença:\*\*.*$", re.M)


def nota_v(via: str) -> str:
    return ("- **V aplicado (U43, 13/09/2026):** despacho do Curador — «pode aplicar_V em todos os "
            "termos» deste lote e dos próximos, com a regra de **presunção de V por fonte de livro** "
            "(`diagnostico/DESPACHO-V-POR-FONTE-DE-LIVRO-2026-09-13.md`). O 🟢 é aqui **presuntivo**: "
            "vem do lastro em obra publicada (fonte `B###` declarada), não de revisão termo a termo — "
            "reversível a qualquer tempo. " + via)


def virar(codes: list[str]) -> None:
    linhas = open(CADASTRO, encoding="utf-8").read().split("\n")
    ini = next(i for i, l in enumerate(linhas) if l.strip() == "TERMOS = [")
    fim = next(i for i in range(ini, len(linhas)) if linhas[i].strip() == "]")
    for cod in codes:
        for i in range(ini, fim):
            l = linhas[i]
            if not l.lstrip().startswith(f'("{cod}"'):
                continue
            assert '"verificado"' not in l, f"{cod}: já é verificado"
            novo = l.replace(", P, [", ', "verificado", [', 1)
            assert novo != l, f"{cod}: esperava status P (provisório) — {l!r}"
            assert l.rstrip().endswith("True),"), f"{cod}: ficha não está True"
            linhas[i] = novo
            break
        else:
            raise AssertionError(f"{cod}: não achado na região TERMOS")
    open(CADASTRO, "w", encoding="utf-8").write("\n".join(linhas))


def main() -> int:
    argv = sys.argv[1:]
    via = ""
    if "--via" in argv:
        i = argv.index("--via")
        via = argv[i + 1] if i + 1 < len(argv) else ""
        argv = argv[:i] + argv[i + 2:]
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        sys.exit("uso: aplicar_v.py RC-### [RC-### ...] [--via texto]")
    hoje = "2026-09-13"
    virar(args)
    import importlib
    importlib.reload(_d)
    importlib.reload(_m)
    T = {t[0]: t for t in _d.TERMOS}
    for cod in args:
        t = T[cod]
        assert t[4] == "verificado", f"{cod}: status não virou"
        arq = next(p for p in os.listdir(os.path.join(RAIZ, "termos"))
                   if p.startswith(cod + "-"))
        p = os.path.join(RAIZ, "termos", arq)
        corpo = open(p, encoding="utf-8").read()
        assert corpo.startswith("+++\n"), f"{cod}: sem frontmatter"
        end = corpo.find("\n+++\n", 4)
        carta = corpo[end + 5:]
        carta = NOTA_NASCENCA.sub(nota_v(via), carta)
        if via and "V aplicado (U43" not in carta:
            carta = carta.rstrip() + "\n" + nota_v(via) + "\n"
        open(p, "w", encoding="utf-8").write(_m.fm_toml(t, hoje) + carta)
        print(f"  {cod}: V aplicado · {arq} · confiança {t and __import__('loader').confianca_de(t)}")
    print(f"\naplicar_v: {len(args)} código(s) chancelado(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
