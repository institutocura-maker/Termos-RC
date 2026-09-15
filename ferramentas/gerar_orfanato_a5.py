#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERAR ORFANATO A5 — contenção segura dos blocos sem localização
===============================================================

O que é um órfão
----------------
Dos 658 blocos não-verbatim, 439 têem âncora conhecida no corpus e 219 não
deixam **nenhum vestígio**: nenhuma janela de 5 palavras consecutivas ocorre
em obra alguma das 158 ingeridas. São paráfrases, ou vêm de fonte ainda não
ingerida. Para estes não há reanexação possível hoje — e não há nada que um
modelo, por melhor que seja, possa extrair: o texto simplesmente não está cá.

Por que um ARTEFACTO e não uma ficha
------------------------------------
O despacho equacionou criar `RC-000-QUARENTENA-A5.md`. Rejeitou-se, e o
artefacto é melhor por três razões:

  1. Um termo fora do cadastro quebraria os números do selo (946/820/1887),
     o `build_indice` e o T14 — e criaria um código que nenhuma relação
     conhece.
  2. A contenção JÁ ESTÁ FEITA: a U86 lavrou a nota de quarentena em
     478/478 fichas, e o bloco fica no seu lugar, com o seu aviso. Nada
     precisa de ser movido para estar contido.
  3. Um artefacto em `diagnostico/` é directamente o *dataset* para a
     triagem semântica futura — ficha, secção, trecho, fontes declaradas —
     **tocando zero fichas**.

O que este script acrescenta ao censo
-------------------------------------
O censo diz apenas «sem âncora». Este script pergunta **porquê**, que é o que
determina se algum dia será recuperável:

  · **fonte não ingerida** — o bloco declara uma obra que NÃO existe no
    corpus (158 obras). Recuperável: basta ingerir a obra.
  · **paráfrase** — todas as fontes declaradas estão no corpus e mesmo assim
    o texto não ocorre. Não é extracto: é redacção do transcriptor. Só a
    curadoria resolve, e talvez nem ela.

**OPERAÇÃO ESTRITAMENTE DE LEITURA.** Não escreve em `termos/`, não emite
notas, não altera status.

Uso
---
    python3 ferramentas/gerar_orfanato_a5.py \
        [--saida-md diagnostico/U95-ORFANATO-A5.md] \
        [--saida-json diagnostico/U95-ORFANATO-A5.json]
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from ferramentas.censo_gap_v2 import carregar_corpus, BASES  # noqa: E402

CENSO = os.path.join(RAIZ, "diagnostico",
                     "A5-CITACOES-PRE-PORTAO-B-2026-09-14.json")
APARELHO_R1 = re.compile(r"·\s*`original\.txt`\s*L\d+")


def norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def indice_de_fichas() -> dict[str, str]:
    out = {}
    for p in glob.glob(os.path.join(RAIZ, "termos", "*.md")):
        b = os.path.basename(p).split("-")
        out["-".join(b[:2])] = p
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida-md", default=os.path.join(
        RAIZ, "diagnostico", "U95-ORFANATO-A5.md"))
    ap.add_argument("--saida-json", default=os.path.join(
        RAIZ, "diagnostico", "U95-ORFANATO-A5.json"))
    a = ap.parse_args()

    censo = json.load(open(CENSO, encoding="utf-8"))
    corpus = carregar_corpus(verbose=False)
    fichas = indice_de_fichas()

    orfaos = [b for b in censo["blocos"] if not b.get("ancora")]
    print(f"blocos sem localização no censo: {len(orfaos)}")

    registos = []
    for b in orfaos:
        cod = b["codigo"]
        path = fichas.get(cod)
        if not path:
            continue
        # localizar o bloco na ficha, para lhe dar endereço e secção real
        chave = " ".join(norm(b["trecho"]).split()[:10])
        linhas = open(path, encoding="utf-8").read().split("\n")
        hit = None
        for i, ln in enumerate(linhas):
            if chave and chave in norm(ln):
                hit = i
                break
        secao = "?"
        if hit is not None:
            secao = next((linhas[j][3:] for j in range(hit, -1, -1)
                          if linhas[j].startswith("## ")), "?")
        fontes = b.get("fontes_declaradas") or []
        tem = [f for f in fontes if f in corpus]
        falta = [f for f in fontes if f not in corpus]
        if falta:
            veredito = ("FONTE NÃO INGERIDA" if len(falta) == len(fontes)
                        else "FONTE PARCIALMENTE NÃO INGERIDA")
        else:
            veredito = "PARÁFRASE"
        registos.append({
            "cod": cod,
            "secao": secao,
            "arquivo": os.path.relpath(path, RAIZ),
            "linha_ficha": (hit + 1) if hit is not None else None,
            "palavras": b["palavras"],
            "trecho": b["trecho"],
            "fontes_declaradas": fontes,
            "fontes_no_corpus": tem,
            "fontes_fora_do_corpus": falta,
            "veredito": veredito,
            "marcas": ("«»" if b.get("guil") else
                       "aspas" if b.get("asp") else "sem marca"),
            "ja_reanexado": bool(hit is not None
                                 and APARELHO_R1.search(linhas[hit])),
        })

    vivos = [r for r in registos if not r["ja_reanexado"]]
    print(f"  · já reanexados (a linha traz aparelho R1): "
          f"{len(registos) - len(vivos)}")
    print(f"  · ÓRFÃOS VIVOS: {len(vivos)}")

    c = collections.Counter(r["veredito"] for r in vivos)
    print("\nveredito:")
    for k, v in c.most_common():
        print(f"   {k:34s} {v:4d}")
    print(f"\ndistribuição por secção:")
    for k, v in collections.Counter(r["secao"] for r in vivos).most_common(8):
        print(f"   {k[:44]:44s} {v:4d}")
    print(f"\nsem marca de citação (paráfrase assumida): "
          f"{sum(1 for r in vivos if r['marcas'] == 'sem marca')}")
    print(f"com «» (promessa explícita de verbatim): "
          f"{sum(1 for r in vivos if r['marcas'] == '«»')}")

    faltantes = collections.Counter()
    for r in vivos:
        for f in r["fontes_fora_do_corpus"]:
            faltantes[f] += 1
    if faltantes:
        print(f"\nobras declaradas mas AUSENTES do corpus (top 15):")
        for k, v in faltantes.most_common(15):
            print(f"   {k:16s} {v:4d} bloco(s)")

    vivos.sort(key=lambda r: (r["cod"], r["linha_ficha"] or 0))
    json.dump({"unidade": "U95", "gerado_por": "gerar_orfanato_a5.py",
               "corpus": len(corpus), "orfãos": len(vivos),
               "registos": vivos},
              open(a.saida_json, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    with open(a.saida_md, "w", encoding="utf-8") as out:
        print("# U95 — Orfanato A5: os blocos sem vestígio no corpus", file=out)
        print("", file=out)
        print("**Gerado por:** `ferramentas/gerar_orfanato_a5.py`  ", file=out)
        print("**Operação:** estritamente de leitura — zero fichas tocadas, "
              "nenhuma nota emitida.", file=out)
        print("", file=out)
        print(f"**{len(vivos)} blocos** não deixam nenhuma janela de 5 palavras "
              f"consecutivas em obra alguma das {len(corpus)} ingeridas. Não são "
              "recuperáveis por reanexação: o texto não está cá.", file=out)
        print("", file=out)
        print("## Por que um artefacto e não uma ficha de quarentena", file=out)
        print("", file=out)
        print("1. Um termo fora do cadastro quebraria os números do selo "
              "(946/820/1887), o `build_indice` e o T14.", file=out)
        print("2. A contenção já está feita: a U86 lavrou a nota de quarentena "
              "em 478/478 fichas, e cada bloco fica no seu lugar com o seu "
              "aviso. Nada precisa de ser movido para estar contido.", file=out)
        print("3. Este ficheiro é directamente o *dataset* para a triagem "
              "semântica futura.", file=out)
        print("", file=out)
        print("## Veredito", file=out)
        print("", file=out)
        print("| veredito | blocos | o que significa |", file=out)
        print("|---|---|---|", file=out)
        for k, v in c.most_common():
            desc = ("o bloco declara obras que o corpus não tem — recuperável "
                    "ao ingerir a obra" if "NÃO INGERIDA" in k else
                    "todas as fontes declaradas estão no corpus e o texto "
                    "mesmo assim não ocorre: é redacção, não extracto")
            print(f"| {k} | {v} | {desc} |", file=out)
        print("", file=out)
        if faltantes:
            print("## Obras declaradas mas ausentes do corpus", file=out)
            print("", file=out)
            print("| obra | blocos que a declaram |", file=out)
            print("|---|---|", file=out)
            for k, v in faltantes.most_common(20):
                print(f"| {k} | {v} |", file=out)
            print("", file=out)
        print("## Registo", file=out)
        print("", file=out)
        for n, r in enumerate(vivos, 1):
            print(f"### O{n:03d} · {r['cod']} · {r['secao']}", file=out)
            print(f"<!-- U95|O{n:03d}|{r['cod']}|{r['arquivo']}|"
                  f"{r['linha_ficha'] or 0}|{r['veredito']} -->", file=out)
            print("", file=out)
            print(f"**Veredito:** {r['veredito']} · **Palavras:** "
                  f"{r['palavras']} · **Marca:** {r['marcas']}  ", file=out)
            print(f"**Endereço:** `{r['arquivo']}`"
                  + (f" L{r['linha_ficha']}" if r["linha_ficha"] else "")
                  + "  ", file=out)
            print(f"**Fontes no corpus:** {', '.join(r['fontes_no_corpus']) or '—'}  ",
                  file=out)
            print(f"**Fontes AUSENTES:** {', '.join(r['fontes_fora_do_corpus']) or '—'}",
                  file=out)
            print("", file=out)
            print("> " + re.sub(r"\s+", " ", r["trecho"]).strip(), file=out)
            print("", file=out)

    print(f"\nartefactos: {os.path.relpath(a.saida_md, RAIZ)} · "
          f"{os.path.relpath(a.saida_json, RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
