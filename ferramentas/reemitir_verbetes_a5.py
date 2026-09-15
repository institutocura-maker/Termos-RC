#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REEMITIR VERBETES A5 — a outra metade do mesmo commit
=====================================================

Por que este script existe
--------------------------
Doutrina da U87 (confirmada na U88, V4.18.03-RC732): «normalizar títulos de
secção obriga a reemitir os verbetes da enciclopédia que os citem **no mesmo
commit**». A mesma baliza vale para o texto das citações: o verificador
`verificar_verbetes.py` exige que todo trecho entre «» de um verbete ocorra
BYTE A BYTE no corpus de fichas. Quando a U91 reanexa uma citação legada, o
texto muda — e os verbetes que a citavam passam a não conferir.

Logo: **reanexar sem reemitir é deixar a suíte vermelha.** Esta é a outra
metade da unidade, e corre no mesmo commit.

O que muda no verbete
---------------------
A fonte é *hard-wrapped* e o Portão B só aceita fragmentos INTRA-LINHA. Uma
citação que na ficha era um período contínuo passa a sér emitida como N
fragmentos. O verbete acompanha:

    «f1» … «f2» … «f3»

Cada fragmento entre «» continua a ocorrer byte a byte na ficha (cada um
dentro do seu par de «»), pelo que o verificador passa; e as reticências
sinalizam ao leitor que a sentença foi partida pela quebra de linha da fonte —
o mesmo que `» … «` significa dentro da ficha.

Nada do conteúdo do verbete se perde: os mesmos N fragmentos, na mesma ordem,
cobrem exactamente o mesmo período que o verbete já citava.

Uso
---
    python3 ferramentas/reemitir_verbetes_a5.py <lote.json> [--aplicar]

Sem `--aplicar`, nada é escrito.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERBETES = os.path.join(RAIZ, "pedagogico", "enciclopedia", "verbetes")
TERMOS = os.path.join(RAIZ, "termos")
CIT = re.compile(r"«([^»]+)»")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def main() -> int:
    if len(sys.argv) < 2:
        sys.exit("uso: reemitir_verbetes_a5.py <lote.json> [--aplicar]")
    aplicar = "--aplicar" in sys.argv
    lote = json.load(open(sys.argv[1], encoding="utf-8"))

    corpus = ""
    for p in sorted(glob.glob(os.path.join(TERMOS, "*.md"))):
        corpus += open(p, encoding="utf-8").read()
    for p in sorted(glob.glob(os.path.join(RAIZ, "notas", "fichas", "*.md"))):
        corpus += open(p, encoding="utf-8").read()

    # mapa: texto legado normalizado -> fragmentos novos
    mapa = {}
    for f in lote["fichas"]:
        frags = [t for _l, t in f["fragmentos"]]
        for t in frags:
            assert "»" not in t and "«" not in t, (
                f"{f['cod']}: fragmento contém «» — quebraria o verificador")
        mapa[norm(f["trecho_atual"])] = frags

    arquivos = sorted(g for g in glob.glob(os.path.join(VERBETES, "**", "*.md"),
                                           recursive=True)
                      if os.path.basename(g).lower() != "readme.md")
    assert arquivos, f"nenhum verbete em {VERBETES}"

    # Deduzplicar por (verbete, citação): a mesma citação costuma ocorrer duas
    # vezes no verbete — no corpo e no blockquote de fecho — e a segunda já não
    # seria encontrada depois de a primeira ter substituído TODAS as ocorrências.
    vistos: dict[tuple[str, str], int] = {}
    for arq in arquivos:
        txt = open(arq, encoding="utf-8").read()
        for cit in CIT.findall(txt):
            if cit not in corpus:
                vistos[(arq, cit)] = txt.count(f"«{cit}»")
    falhas = list(vistos)
    print(f"verbetes: {len(arquivos)} · citações DISTINTAS a corrigir: "
          f"{len(falhas)} · ocorrências: {sum(vistos.values())}")

    planos: dict[str, list[tuple[str, str]]] = {}
    orfaos = []
    for arq, cit in falhas:
        frags = mapa.get(norm(cit))
        if frags is None:
            # o verbete pode citar uma versão TRUNCADA do trecho legado
            cand = [k for k in mapa if norm(cit) in k or k in norm(cit)]
            if len(cand) == 1:
                frags = mapa[cand[0]]
            else:
                orfaos.append((os.path.basename(arq), cit, len(cand)))
                continue
        novo = " … ".join(f"«{t}»" for t in frags)
        planos.setdefault(arq, []).append((cit, novo))

    if orfaos:
        print(f"\n!! {len(orfaos)} citações SEM correspondência no lote:")
        for a, c, n in orfaos[:10]:
            print(f"   {a}: {c[:100]} ({n} candidatos)")
        return 1

    n_sub = 0
    for arq, trocas in sorted(planos.items()):
        txt = open(arq, encoding="utf-8").read()
        for cit, novo in trocas:
            velho = f"«{cit}»"
            if velho not in txt:
                print(f"  !! {os.path.basename(arq)}: «{cit[:60]}» não achado")
                return 1
            k = txt.count(velho)
            txt = txt.replace(velho, novo)
            n_sub += k
        planos[arq] = [(c, n) for c, n in trocas]
        if aplicar:
            open(arq, "w", encoding="utf-8").write(txt)
        print(f"  {os.path.basename(arq):58s} "
              f"{len(trocas)} citação(ões) reemitida(s)")

    print(f"\n  {len(planos)} verbetes · {n_sub} ocorrências substituídas")
    if not aplicar:
        print("  --aplicar NÃO passado: nada escrito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
