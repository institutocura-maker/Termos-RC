#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GERAR DIFF CURATORIAL A5 — artefacto de decisão humana
======================================================

O que isto é
------------
Nas faixas de 100% e 90–99% a divergência era ARTEFACTO (aspas, negrito,
elisões) e a reanexação era mecânica: o Portão B bastava. A partir da faixa
70–89% o fosso passa a ser EDIÇÃO REAL — palavras trocadas, trechos
recompostos, paráfrases parciais — e a decisão deixa de poder ser despachada
sem o Curador.

Este script produz o artefacto de decisão: para cada bloco, o texto legado, o
texto-fonte localizado, onde divergem exactamente, e duas caixas de visto.

**É UMA OPERAÇÃO ESTRITAMENTE DE LEITURA.** Não escreve em `termos/`, não
emite notas de quarentena, não altera status, não toca no cadastro. O único
ficheiro que produz é o artefacto em `diagnostico/`.

Formato
-------
Markdown, porque é o que o Curador vai percorrer e marcar. Mas com uma
estrutura RÍGIDA, para que `ler_diff_curatorial_a5.py` o leia de volta sem
ambiguidade — e com um teste de ida-e-volta que o prova antes de o Curador
escrever seja o que for.

Cada instância distingue dois factos decisivos:

  · CONTÍGUO — os fragmentos encontrados são contíguos na fonte, logo existe
    UM substring exacto que substitui o legado. «APROVAR FONTE» é limpo.
  · DESCONTÍNUO — há fossos na fonte: aprovar exige juízo, porque a citação
    resultante é uma reconstrução, não um extracto.

Uso
---
    python3 ferramentas/gerar_diff_curatorial_a5.py [--min 70] [--max 90] \
        [--saida diagnostico/U93-DIFF-CURATORIAL.md]
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

from ferramentas.censo_gap_v2 import carregar_corpus  # noqa: E402
from ferramentas.extrair_fragmentos_a5 import (  # noqa: E402
    indice_de_fichas, nucleo_da_linha, localizar_na_ficha,
    palavras_com_linha, alinhar, palavras, frouxo,
)
from ferramentas.materializar_lote import pagina  # noqa: E402

# Um bloco reanexado com UM SÓ fragmento continua «localizável»: a sua chave
# ainda ocorre dentro do «» da nova citação. Sem este filtro, o artefacto
# entregaria ao Curador trabalho já feito.
APARELHO_R1 = re.compile(r"·\s*`original\.txt`\s*L\d+")

CENSO = os.path.join(RAIZ, "diagnostico",
                     "A5-CITACOES-PRE-PORTAO-B-2026-09-14.json")
MAX_FRAG = 6
MAX_PALAVRAS = 60


def caminho_ficha(cod: str) -> str:
    g = glob.glob(os.path.join(RAIZ, "termos", cod + "-*.md"))
    return g[0] if len(g) == 1 else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=70.0)
    ap.add_argument("--max", type=float, default=90.0)
    ap.add_argument("--saida", default=os.path.join(
        RAIZ, "diagnostico", "U93-DIFF-CURATORIAL.md"))
    ap.add_argument("--unidade", default="U93")
    a = ap.parse_args()

    censo = json.load(open(CENSO, encoding="utf-8"))
    corpus = carregar_corpus(verbose=False)
    fichas = indice_de_fichas()

    instancias: list[dict] = []
    g6falhas: list[dict] = []
    saltos = collections.Counter()
    for b in censo["blocos"]:
        if not b.get("ancora"):
            continue
        cod, sigla, ln = b["codigo"], b["ancora"]["obra"], b["ancora"]["linha"]
        path = fichas.get(cod)
        ob = corpus.get(sigla)
        if not path or ob is None:
            saltos["obra/ficha ausente"] += 1
            continue
        par = next((p for p in ob.blocos if p["ini"] <= ln <= p["fim"]), None)
        if par is None:
            saltos["linha fora de parágrafo"] += 1
            continue
        loc = localizar_na_ficha(path, b["trecho"])
        if loc is None:
            # já reanexado por U91/U92: o texto solto desapareceu
            saltos["já reanexado (U91/U92)"] += 1
            continue
        i_linha, linha_ficha = loc
        if APARELHO_R1.search(linha_ficha):
            saltos["já reanexado (a linha traz aparelho R1)"] += 1
            continue
        legado = nucleo_da_linha(linha_ficha)
        alvo = palavras(legado)
        if len(alvo) < 4:
            saltos["núcleo curto"] += 1
            continue
        pal = palavras_com_linha(ob.linhas, par["ini"], par["fim"])
        fonte = [w for w, _l, _c, _d in pal]
        bm = alinhar([frouxo(w) for w in alvo], [frouxo(w) for w in fonte])
        cob = set()
        for i, j, k in bm:
            cob |= set(range(i, i + k))
        pct = round(100 * len(cob) / len(alvo), 1)
        # NÃO se filtra aqui: o bloco só é roteado no fim, porque a Parte II
        # (≥90% mas sem substring único) precisa das mesmas contas.

        # fragmentos (substrings reais da linha-fonte)
        frag = []
        for _i, j, k in bm:
            ini = 0
            while ini < k:
                lin0 = pal[j + ini][1]
                fim = ini
                while fim + 1 < k and pal[j + fim + 1][1] == lin0:
                    fim += 1
                ca, cb = pal[j + ini][2], pal[j + fim][3]
                txt = ob.linhas[lin0 - 1].rstrip()[ca:cb]
                esperado = " ".join(pal[j + ini + t][0] for t in range(fim - ini + 1))
                if txt.strip() and " ".join(palavras(txt)) == esperado:
                    frag.append({"linha": lin0, "texto": txt,
                                 "ifonte": j + ini, "n": fim - ini + 1})
                ini = fim + 1
        contiguo = all(b2["ifonte"] == b1["ifonte"] + b1["n"]
                       for b1, b2 in zip(frag, frag[1:])) if frag else False

        # divergências: fossos do alvo, com o que a fonte tem no lugar
        falta = [i for i in range(len(alvo)) if i not in cob]
        runs = []
        if falta:                      # cobertura total => sem divergências
            cur = [falta[0]]
            for i in falta[1:]:
                if i == cur[-1] + 1:
                    cur.append(i)
                else:
                    runs.append(cur); cur = [i]
            runs.append(cur)
        divs = []
        for r in runs:
            # palavras da fonte que ficam entre o bloco anterior e o seguinte
            ant = [bmk for bmk in bm if bmk[0] + bmk[2] <= r[0]]
            prox = [bmk for bmk in bm if bmk[0] >= r[-1] + 1]
            j0 = (max(ant, key=lambda x: x[0] + x[2])[1]
                  + max(ant, key=lambda x: x[0] + x[2])[2]) if ant else 0
            j1 = min(prox, key=lambda x: x[0])[1] if prox else len(fonte)
            divs.append({
                "pos": ("início" if r[0] == 0 else
                        "fim" if r[-1] == len(alvo) - 1 else "meio"),
                "legado": " ".join(alvo[r[0]:r[-1] + 1]),
                "fonte": " ".join(fonte[j0:j1]),
            })

        reg = {
            "cod": cod, "sigla": sigla, "linha": ln,
            "secao": b["secao"], "pct": pct,
            "palavras": len(alvo), "cobertas": len(cob),
            "arquivo": os.path.relpath(path, RAIZ),
            "linha_ficha": i_linha + 1,
            "legado": legado,
            "fragmentos": [[f["linha"], f["texto"]] for f in frag],
            "contiguo": contiguo,
            "n_frag": len(frag),
            "longo": len(frag) > MAX_FRAG or len(alvo) > MAX_PALAVRAS,
            "divs": divs,
            "chave": " ".join(palavras(b["trecho"])[:10]),
        }
        if pct >= 90.0 and not contiguo:
            g6falhas.append(reg)                       # Parte II
        elif a.min <= pct < a.max:
            instancias.append(reg)                     # Parte I

    print(f"instâncias na faixa [{a.min}, {a.max}[: {len(instancias)}")
    for k, v in saltos.most_common():
        print(f"  — {k}: {v}")

    # ── saldo completo, para que nada fique fora do mapa ────────────────────
    ledger = collections.Counter()
    for b in censo["blocos"]:
        if not b.get("ancora"):
            continue
        cod, sigla, ln = b["codigo"], b["ancora"]["obra"], b["ancora"]["linha"]
        path, ob = fichas.get(cod), corpus.get(sigla)
        if not path or ob is None:
            ledger["ficha/obra ausente"] += 1; continue
        par = next((q for q in ob.blocos if q["ini"] <= ln <= q["fim"]), None)
        if par is None:
            ledger["fora de parágrafo"] += 1; continue
        loc = localizar_na_ficha(path, b["trecho"])
        if loc is None or APARELHO_R1.search(loc[1]):
            ledger["JÁ reanexado"] += 1; continue
        alvo = palavras(nucleo_da_linha(loc[1]))
        if len(alvo) < 4:
            ledger["núcleo curto"] += 1; continue
        pal = palavras_com_linha(ob.linhas, par["ini"], par["fim"])
        bm = alinhar([frouxo(w) for w in alvo],
                     [frouxo(w) for w in (w for w, _l, _c, _d in pal)])
        pct = round(100 * sum(k for _i, _j, k in bm) / len(alvo), 1)
        frag = []
        for _i, j, k in bm:
            ini = 0
            while ini < k:
                l0 = pal[j + ini][1]; fim = ini
                while fim + 1 < k and pal[j + fim + 1][1] == l0:
                    fim += 1
                frag.append((j + ini, fim - ini + 1)); ini = fim + 1
        cont = all(b2[0] == b1[0] + b1[1] for b1, b2 in zip(frag, frag[1:])) if frag else False
        faixa = ("100%" if pct >= 99.5 else "90–99%" if pct >= 90 else
                 "70–89%" if pct >= 70 else "50–69%" if pct >= 50 else
                 "25–49%" if pct >= 25 else "<25%")
        if pct >= 90:
            ledger[f"{faixa} · CONTÍGUO (motor resolve)"] += 1 if cont else 0
            ledger[f"{faixa} · FALHA G6 (curador)"] += 0 if cont else 1
        else:
            ledger[f"{faixa} · curador"] += 1
    print("\nSALDO DOS 442 BLOCOS COM LOCALIZAÇÃO (alinhamento frouxo):")
    for k, v in sorted(ledger.items(), key=lambda x: -x[1]):
        print(f"   {k:34s} {v:4d}")
    print(f"   {'TOTAL':34s} {sum(ledger.values()):4d}")

    instancias.sort(key=lambda x: (x["cod"], x["linha"]))
    c = collections.Counter(
        ("CONTÍGUO" if x["contiguo"] else "DESCONTÍNUO") +
        (" · LONGO" if x["longo"] else "") for x in instancias)
    print("\nclassificação:")
    for k, v in c.most_common():
        print(f"   {k:26s} {v:3d}")

    json.dump({"unidade": a.unidade, "faixa": [a.min, a.max],
               "banda": instancias, "g6": g6falhas},
              open("/tmp/u93_tudo.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\nParte I (faixa {a.min}–{a.max}%): {len(instancias)}")
    print(f"Parte II (≥90% mas FALHA G6):     {len(g6falhas)}")
    print(f"gravado em /tmp/u93_tudo.json")

    escrever_artefacto(a.saida, instancias, g6falhas, [a.min, a.max],
                       a.unidade)
    print(f"artefacto: {os.path.relpath(a.saida, RAIZ)} "
          f"({len(instancias) + len(g6falhas)} instâncias)")
    return 0




# ══════════════════════════════════════════════════════════ emissão ═════════
ID_RE = re.compile(r"<!--\s*U93\|([^|]+)\|([^|]+)\|([^|]+)\|(\d+)\|([\d.]+)\|"
                   r"(sim|nao)\|(sim|nao)\|([^|]+)\|(\d+)\s*-->")


def _esc(t: str) -> str:
    """Uma linha segura para markdown (tira pipes e quebras)."""
    return re.sub(r"\s+", " ", t.replace("|", "\\|")).strip()


def emitir(inst: dict, parte: str, n: int, out) -> None:
    i = inst["cod"] + " · " + inst["sigla"] + " L" + str(inst["linha"])
    ident = f"{parte}-{n:03d}"
    print(f"### U93-{ident} · {i}", file=out)
    print(f"<!-- U93|{ident}|{inst['cod']}|{inst['sigla']}|{inst['linha']}|"
          f"{inst['pct']}|{'sim' if inst['contiguo'] else 'nao'}|"
          f"{'sim' if inst['longo'] else 'nao'}|{inst['arquivo']}|"
          f"{inst['linha_ficha']} -->", file=out)
    print("", file=out)
    print(f"**Cobertura:** {inst['pct']}% ({inst['cobertas']}/{inst['palavras']} "
          f"palavras) · **Divergência:** {round(100 - inst['pct'], 1)}% · "
          f"**Secção:** {inst['secao']}", file=out)
    print(f"**Contíguo na fonte:** {'SIM — existe um substring único' if inst['contiguo'] else 'NÃO — a citação seria reconstruída'} · "
          f"**Longo:** {'SIM (>6 frag ou >60 palavras)' if inst['longo'] else 'não'}",
          file=out)
    print("", file=out)
    print("**LEGADO** — como está hoje na ficha", file=out)
    print("", file=out)
    print("> " + _esc(inst["legado"]), file=out)
    print("", file=out)
    print("**FONTE** — fragmentos verbatim localizados", file=out)
    print("", file=out)
    if inst["fragmentos"]:
        marca = " » … « ".join(f"«{_esc(t)}»" for _l, t in inst["fragmentos"])
        print("> " + marca, file=out)
        print("", file=out)
        print("> " + " · ".join(
            f"L{l}" for l, _t in inst["fragmentos"]), file=out)
    else:
        print("> *(nenhum fragmento verbatim localizado)*", file=out)
    print("", file=out)
    if inst["divs"]:
        print("**DIVERGÊNCIAS**", file=out)
        print("", file=out)
        print("| # | posição | legado | fonte |", file=out)
        print("|---|---|---|---|", file=out)
        for k, d in enumerate(inst["divs"][:12], 1):
            print(f"| {k} | {d['pos']} | `{_esc(d['legado'])[:90]}` | "
                  f"`{_esc(d['fonte'])[:90]}` |", file=out)
        if len(inst["divs"]) > 12:
            print(f"| … | | *(+{len(inst['divs']) - 12} divergências)* | |",
                  file=out)
        print("", file=out)
    print("**DECISÃO**", file=out)
    print("", file=out)
    print(f"- [ ] APROVAR FONTE — {ident}", file=out)
    print(f"- [ ] MANTER LEGADO — {ident}", file=out)
    print("", file=out)
    print("---", file=out)
    print("", file=out)


def escrever_artefacto(caminho: str, banda: list[dict], g6: list[dict],
                       faixa: list[float], unidade: str) -> None:
    with open(caminho, "w", encoding="utf-8") as out:
        print(f"# {unidade} — Diff Curatorial A5 (artefacto de LEITURA)", file=out)
        print("", file=out)
        print("**Gerado por:** `ferramentas/gerar_diff_curatorial_a5.py`  ", file=out)
        print("**Operação:** estritamente de leitura — nenhuma ficha foi "
              "alterada, nenhuma nota emitida, nenhum status mexido.  ", file=out)
        print("**Instruções:** marque UMA caixa por instância. Deixe ambas em "
              "branco para adiar. Não marque as duas.", file=out)
        print("", file=out)
        print("## Como ler cada instância", file=out)
        print("", file=out)
        print("- **Cobertura** = quantas palavras do trecho legado ocorrem "
              "verbatim na fonte. **Divergência** = o resto.", file=out)
        print("- **Contíguo na fonte: SIM** — os fragmentos são seguidos, logo "
              "existe UM substring exacto que substitui o legado. Aprovar é "
              "limpo.", file=out)
        print("- **Contíguo na fonte: NÃO** — há fossos. Aprovar produz uma "
              "citação reconstruída (os fragmentos unidos por `» … «`), o que "
              "exige juízo: é essa a decisão que se lhe pede.", file=out)
        print("- **DIVERGÊNCIAS** mostra, fosso a fosso, o que a ficha diz "
              "contra o que a fonte tem no mesmo ponto.", file=out)
        print("", file=out)
        print("## Saldo dos 442 blocos com localização", file=out)
        print("", file=out)
        print("| situação | blocos | quem resolve |", file=out)
        print("|---|---|---|", file=out)
        print("| JÁ reanexado (U91+U92) | 122 | feito |", file=out)
        print("| ≥90% e contíguo | 44 | motor (U94) |", file=out)
        print("| **Parte II — ≥90% mas SEM substring único** | **167** | **curador** |", file=out)
        print("| **Parte I — faixa 70–89%** | **45** | **curador** |", file=out)
        print("| 50–69% | 26 | curador (U95) |", file=out)
        print("| 25–49% | 21 | curador (U95) |", file=out)
        print("| <25% | 11 | curador (U95) |", file=out)
        print("| fora de parágrafo | 6 | investigar |", file=out)
        print("", file=out)
        print(f"## PARTE I — faixa {faixa[0]:.0f}–{faixa[1]:.0f}% "
              f"({len(banda)} instâncias)", file=out)
        print("", file=out)
        for n, inst in enumerate(banda, 1):
            emitir(inst, "I", n, out)
        print(f"## PARTE II — ≥90% mas sem substring único "
              f"({len(g6)} instâncias)", file=out)
        print("", file=out)
        print("*Estes blocos têem cobertura alta mas os fragmentos não são "
              "contíguos na fonte: não existe um único extracto que os "
              "substitua. Aprovar é uma reconstrução — decide-se caso a caso.*",
              file=out)
        print("", file=out)
        for n, inst in enumerate(g6, 1):
            emitir(inst, "II", n, out)


if __name__ == "__main__":
    sys.exit(main())
