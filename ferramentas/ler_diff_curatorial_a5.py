#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LER DIFF CURATORIAL A5 — do visto do Curador ao lote de aplicação
=================================================================

A outra metade do artefacto. O Curador marca `diagnostico/U93-DIFF-CURATORIAL.md`;
este script lê os vistos e emite o **lote declarativo** que o
`reintegrar_citacoes.py` aplica.

Por que existe separado
-----------------------
A geração é só leitura; a leitura é só leitura também. Nenhuma das duas toca
em `termos/`. Só a aplicação final o fará, e só depois de o Curador ter
decidido — nunca antes.

O que valida
------------
  1. Todas as instâncias do artefacto são解析 parseáveis (o comentário
     `<!-- U93|… -->` é a âncora; se uma falhar, aborta).
  2. **No máximo um visto por instância.** Duas caixas marcadas é contradição
     e aborta: o Curador não pode querer simultaneamente substituir e manter.
  3. Caixas sem visto significam ADIAR — a instância fica fora do lote e
     permanece como está, sem penalidade.

Uso
---
    python3 ferramentas/ler_diff_curatorial_a5.py \
        [--artefacto diagnostico/U93-DIFF-CURATORIAL.md] \
        [--saida diagnostico/U93-A5-LOTE37-2026-09-15.json]

Se não houver nenhum visto marcado, emite-se um lote vazio e o script diz
quantas decisões estão por tomar — o que permite provar a ida-e-volta do
formato no próprio dia em que o artefacto nasce, antes de o Curador escrever
o que quer que seja.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from ferramentas.gerar_diff_curatorial_a5 import ID_RE  # noqa: E402

VISTO = re.compile(r"^- \[( |x|X)\] (APROVAR FONTE|MANTER LEGADO) — (\S+)\s*$")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artefacto", default=os.path.join(
        RAIZ, "diagnostico", "U93-DIFF-CURATORIAL.md"))
    ap.add_argument("--saida", default=os.path.join(
        RAIZ, "diagnostico", "U93-A5-LOTE37-2026-09-15.json"))
    a = ap.parse_args()

    linhas = open(a.artefacto, encoding="utf-8").read().split("\n")

    instancias: dict[str, dict] = {}
    ordem: list[str] = []
    for ln in linhas:
        m = ID_RE.search(ln)
        if not m:
            continue
        ident, cod, sigla, n, pct, contiguo, longo, arq, linha_ficha = m.groups()
        if ident in instancias:
            sys.exit(f"identificador repetido: {ident}")
        instancias[ident] = {
            "ident": ident, "cod": cod, "sigla": sigla, "linha": int(n),
            "pct": float(pct), "contiguo": contiguo == "sim",
            "longo": longo == "sim", "arquivo": arq,
            "linha_ficha": int(linha_ficha),
            "decisao": None,
        }
        ordem.append(ident)

    if not instancias:
        sys.exit("nenhuma instância encontrada — o artefacto está corrompido?")

    vistos = 0
    for ln in linhas:
        m = VISTO.match(ln)
        if not m:
            continue
        marca, acao, ident = m.group(1).lower(), m.group(2), m.group(3)
        if marca != "x":
            continue
        if ident not in instancias:
            sys.exit(f"visto para instância desconhecida: {ident}")
        d = "APROVAR_FONTE" if acao == "APROVAR FONTE" else "MANTER_LEGADO"
        if instancias[ident]["decisao"] not in (None, d):
            sys.exit(f"  CONTRADIÇÃO · {ident}: marcadas as duas caixas "
                     f"(«APROVAR FONTE» e «MANTER LEGADO») — abortar")
        instancias[ident]["decisao"] = d
        vistos += 1

    aprov = [i for i in ordem if instancias[i]["decisao"] == "APROVAR_FONTE"]
    manter = [i for i in ordem if instancias[i]["decisao"] == "MANTER_LEGADO"]
    adiar = [i for i in ordem if instancias[i]["decisao"] is None]

    print(f"instâncias lidas      : {len(instancias)}")
    print(f"  APROVAR FONTE       : {len(aprov)}")
    print(f"  MANTER LEGADO       : {len(manter)}")
    print(f"  por decidir (adiar) : {len(adiar)}")

    # ── o lote: só o que o Curador aprovou vira citação reanexada ───────────
    fichas = []
    for ident in aprov:
        i = instancias[ident]
        fichas.append({
            "cod": i["cod"], "sigla": i["sigla"], "linha": i["linha"],
            "linha_ficha": i["linha_ficha"], "arquivo": i["arquivo"],
            "pct": i["pct"], "contiguo": i["contiguo"], "ident": ident,
        })
    lote = {
        "unidade": "U93", "lote": "A5-3", "rota": "R1", "data": "2026-09-15",
        "aplicar_V": False,
        "origem": os.path.relpath(a.artefacto, RAIZ),
        "criterio": ("A5 — aplicação das decisões curatoriais do artefacto de "
                     "diff. Só entram as instâncias com «APROVAR FONTE»; as "
                     "«MANTER LEGADO» e as adiadas não sofrem nada."),
        "fichas": fichas,
    }
    json.dump(lote, open(a.saida, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\nlote escrito: {os.path.relpath(a.saida, RAIZ)} "
          f"({len(fichas)} fichas)")
    if not vistos:
        print("  (nenhum visto marcado — lote vazio; artefacto pronto a rever)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
