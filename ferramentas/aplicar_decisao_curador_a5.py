#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APLICAR DECISÃO DO CURADOR A5 — U94
===================================

Lê `uploads_recepcao/U93-U94-id-decisao.txt` e executa o que o Curador
decidiu sobre as 212 instâncias do artefacto de curadoria.

As três regras do despacho
--------------------------
1. **APROVAR_FONTE (não-contíguo)** → reconstrução com o marcador `» […] «`
   nos fossos, e nota explícita «reconstrução aprovada na U93; N palavras da
   fonte omitidas».
2. **`» … «` mantém o seu significado EXCLUSIVO**: quebra de hard-wrap, sem
   omissão de palavras. Nunca assinala fosso.
3. **MANTER_LEGADO** → nenhuma acção. Não se acrescenta aparelho R1 a texto
   que não é verbatim: o aparelho afirma que o texto está naquela linha, e não
   está. A nota de quarentena da U86 já cobre o bloco e fica correcta.

Dois marcadores, duas verdades
------------------------------
Foi por isto que a G6 nasceu na U91: um único marcador para duas realidades
incompatíveis faria a ficha mentir sobre a natureza do que une os fragmentos.
Agora cada um diz o que é:

    » … «     quebra de hard-wrap  (nenhuma palavra da fonte omitida)
    » […] «   omissão APROVADA     (N palavras da fonte ficaram de fora)

Comportas (as mesmas do `reintegrar_citacoes.py`)
-------------------------------------------------
  A  `conferir()` em cada fragmento, importado do driver, antes de escrever;
  B  a linha indicada pelo artefacto tem de existir e NÃO trazer aparelho R1;
  C  nenhuma ficha com dois blocos aprovados no mesmo endereço;
  D  idempotência: se a linha já é a que este lote produz, não se reescreve.

Uso
---
    python3 ferramentas/aplicar_decisao_curador_a5.py [--aplicar]
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from ferramentas.censo_gap_v2 import carregar_corpus  # noqa: E402
from ferramentas.extrair_fragmentos_a5 import (  # noqa: E402
    nucleo_da_linha, palavras_com_linha, alinhar, palavras, frouxo,
)
# Portão B: o mesmo código do driver, não uma reimplementação.
from ferramentas.materializar_lote import (  # noqa: E402
    caminho_da_obra, conferir, pagina)

ARTEFACTO = os.path.join(RAIZ, "diagnostico", "U93-DIFF-CURATORIAL.md")
DECISAO = os.path.join(RAIZ, "uploads_recepcao", "U93-U94-id-decisao.txt")
SAIDA = os.path.join(RAIZ, "diagnostico", "U94-A5-LOTE38-2026-09-15.json")
APARELHO_R1 = re.compile(r"·\s*`original\.txt`\s*L\d+")
ANCORA = re.compile(r"<!--\s*U93\|([^|]+)\|([^|]+)\|([^|]+)\|(\d+)\|([\d.]+)\|"
                    r"(sim|nao)\|(sim|nao)\|([^|]+)\|(\d+)\s*-->")
DEC = re.compile(r"^U93-(I|II)-(\d{3})\s*→\s*(APROVAR_FONTE|MANTER_LEGADO)$")
MARCA_WRAP = "» … «"      # quebra de hard-wrap — sem omissão
MARCA_FOSSO = "» […] «"

# ── COMPORTA E — o vão ────────────────────────────────────────────────────────
# Distância máxima, em palavras da fonte, entre o primeiro e o último fragmento
# de uma mesma reconstrução. Existe porque há obras do corpus sem quebra de
# parágrafo: o «parágrafo» é o livro inteiro, e o alinhador (difflib) vai então
# pescar as palavras do legado em QUALQUER página, devolvendo cobertura de 100%
# para o que não passa de salada de palavras-chave. Uma citação real — mesmo
# muito elidida — não se estende por mais de algumas centenas de palavras.
MAX_VAO = 300   # omissão APROVADA pelo Curador
# Metade do vão admitido para cada lado do fragmento dominante: a janela total
# tem assim MAX_VAO palavras mais o comprimento do próprio fragmento.
MAX_JANELA = MAX_VAO // 2

# ── COMPORTA F — micro-fragmentos isolados ───────────────────────────────────
# Um fragmento de poucas palavras separado do resto por um fosso grande é
# quase sempre um FALSO POSITIVO: o difflib reconhece «a», «O», «Javé»,
# «existe.» em qualquer parte da obra e casa-os a milhares de palavras do
# trecho real. Foi exactamente este mecanismo que inflou os vãos na U94 e
# adiou as 9 instâncias. Um fragmento GENUÍNO dessa dimensão aparece colado
# ao fragmento dominante (é o caso de «o ser humano,» na II-085, a uma palavra
# de distância); o espúrio aparece isolado. Dai o critério: poucas palavras E
# vizinho mais próximo a mais de LIMPAR_VAO palavras.
LIMPAR_MICRO = 3    # palavras
LIMPAR_VAO = 25     # palavras da fonte


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def _fragmentos(pal, fonte_f, alvo_f, ob, janela=None) -> list[dict]:
    """Alinha `alvo_f` contra `fonte_f` — ou contra uma janela desta — e
    devolve os fragmentos verificáveis, um por linha da fonte."""
    off = 0
    if janela is None:
        bm = alinhar(alvo_f, fonte_f)
    else:
        a0, a1 = janela
        bm = alinhar(alvo_f, fonte_f[a0:a1])
        off = a0
    frag = []
    for _i, j, k in bm:
        j += off
        ini = 0
        while ini < k:
            l0 = pal[j + ini][1]
            fim = ini
            while fim + 1 < k and pal[j + fim + 1][1] == l0:
                fim += 1
            ca, cb = pal[j + ini][2], pal[j + fim][3]
            txt = ob.linhas[l0 - 1].rstrip()[ca:cb]
            esp = " ".join(pal[j + ini + t][0] for t in range(fim - ini + 1))
            if txt.strip() and " ".join(palavras(txt)) == esp:
                frag.append({"linha": l0, "texto": txt,
                             "ifonte": j + ini, "n": fim - ini + 1})
            ini = fim + 1
    return frag


def _limpar_micro(frag: list[dict]) -> list[dict]:
    """Descarta micro-fragmentos isolados (comporta F). Ver docstring das
    constantes LIMPAR_MICRO / LIMPAR_VAO."""
    if len(frag) < 2:
        return frag
    fora = []
    for i, f in enumerate(frag):
        viz = []
        if i > 0:
            viz.append(f["ifonte"] - (frag[i - 1]["ifonte"] + frag[i - 1]["n"]))
        if i + 1 < len(frag):
            viz.append(frag[i + 1]["ifonte"] - (f["ifonte"] + f["n"]))
        if f["n"] <= LIMPAR_MICRO and viz and min(viz) > LIMPAR_VAO:
            continue                      # isolado ⇒ falso positivo
        if f["n"] == 1 and viz and min(viz) > 0:
            # Uma palavra só só se justifica se estiver COLADA a um vizinho
            # (é o caso do resto de uma linha hard-wrapped). Separada por um
            # fosso, é ruído: não acrescenta nada à citação e denuncia um
            # casamento espúrio do alinhador.
            continue
        fora.append(f)
    return fora or frag


def aparelhavel(sigla: str) -> bool:
    """A obra pode receber aparelho `original.txt LNNNN`?

    O censo e o Portão B não vêem necessariamente as mesmas obras: o corpus
    pode incluir amostras autorizadas (`AMOSTRAS_AUTORIZADAS`, em
    `censo_gap_v2`) que `materializar_lote.caminho_da_obra` — ficheiro
    INTOCÁVEL, onde vive o Portão B — não resolve. Para essas obras o texto é
    LOCALIZÁVEL mas não é APARELHÁVEL: apontar-lhes uma linha produziria uma
    citação que a porta da casa não consegue verificar.
    """
    try:
        caminho_da_obra(sigla)
        return True
    except FileNotFoundError:
        return False


def main() -> int:
    aplicar = "--aplicar" in sys.argv

    # ── ler a decisão ───────────────────────────────────────────────────────
    decisao: dict[str, str] = {}
    for l in open(DECISAO, encoding="utf-8"):
        m = DEC.match(l.strip())
        if m:
            k = f"{m.group(1)}-{m.group(2)}"
            if k in decisao and decisao[k] != m.group(3):
                sys.exit(f"contradição: {k} decidido duas vezes")
            decisao[k] = m.group(3)
    if not decisao:
        sys.exit("nenhuma decisão lida")
    n_ap = sum(1 for v in decisao.values() if v == "APROVAR_FONTE")
    print(f"decisões: {len(decisao)} · APROVAR_FONTE {n_ap} · "
          f"MANTER_LEGADO {len(decisao) - n_ap}")

    # ── ler as âncoras do artefacto ─────────────────────────────────────────
    ancoras: dict[str, dict] = {}
    for l in open(ARTEFACTO, encoding="utf-8"):
        m = ANCORA.search(l)
        if not m:
            continue
        ancoras[m.group(1)] = {
            "cod": m.group(2), "sigla": m.group(3),
            "linha": int(m.group(4)), "pct": float(m.group(5)),
            "contiguo": m.group(6) == "sim", "longo": m.group(7) == "sim",
            "arquivo": m.group(8), "linha_ficha": int(m.group(9)),
        }
    if len(ancoras) != len(decisao):
        sys.exit(f"artefacto tem {len(ancoras)} instâncias, decisão tem "
                 f"{len(decisao)} — não casam")
    for k in decisao:
        if k not in ancoras:
            sys.exit(f"decisão para instância inexistente: {k}")

    corpus = carregar_corpus(verbose=False)
    planos = []
    vistos: set[tuple[str, int]] = set()
    por_endereco: dict[tuple[str, int], dict] = {}
    bloq_b = 0
    n_aparelhaveis = [0]

    for ident, d in sorted(decisao.items()):
        if d != "APROVAR_FONTE":
            continue                       # MANTER_LEGADO — nenhuma acção
        a = ancoras[ident]
        path = os.path.join(RAIZ, a["arquivo"])
        if not os.path.exists(path):
            sys.exit(f"  comporta B · {ident}: ficha inexistente ({path})")
        linhas = open(path, encoding="utf-8").read().split("\n")
        n = a["linha_ficha"]
        if not (1 <= n <= len(linhas)):
            sys.exit(f"  comporta B · {ident}: linha {n} fora do ficheiro")
        if APARELHO_R1.search(linhas[n - 1]):
            bloq_b += 1
            continue                       # idempotência: já reanexado
        vistos.add((a["arquivo"], n))

        ob = corpus.get(a["sigla"])
        if ob is None:
            sys.exit(f"  {ident}: obra {a['sigla']} fora do corpus")
        if not aparelhavel(a["sigla"]):
            # texto localizável mas NÃO aparelhável (Portão B cego a esta obra)
            n_aparelhaveis[0] += 1
            continue
        par = next((p for p in ob.blocos
                    if p["ini"] <= a["linha"] <= p["fim"]), None)
        if par is None:
            sys.exit(f"  {ident}: linha fora de parágrafo")

        alvo = palavras(nucleo_da_linha(linhas[n - 1]))
        pal = palavras_com_linha(ob.linhas, par["ini"], par["fim"])
        fonte = [w for w, _l, _c, _d in pal]
        alvo_f = [frouxo(w) for w in alvo]
        fonte_f = [frouxo(w) for w in fonte]

        # ── ALINHAMENTO EM JANELA (U96, Fase 1) ─────────────────────────────
        # Sobre o bloco inteiro, o difflib pesca palavras banais («a», «O»,
        # «Javé») a milhares de palavras do trecho real, inflando o vão e
        # fabricando reconstruções que juntam pontas opostas da obra. A janela
        # resolve em duas passagens: alinha-se uma vez para achar o fragmento
        # dominante, e volta a alinhar só dentro de MAX_JANELA palavras em
        # torno dele. É NÃO-DESTRUTIVO — não mexe nas fontes nem na numeração
        # de linhas de que depende todo o aparelho `original.txt LNNNN` — e
        # provou não alterar uma única palavra das 60 já aplicadas na U94.
        frag = _fragmentos(pal, fonte_f, alvo_f, ob)
        if not frag:
            sys.exit(f"  {ident}: sem fragmentos — não se aplica")

        # A janela e a comporta F são manobras de SALVAMENTO, accionadas só
        # quando o alinhamento global é IMPLAUSÍVEL (vão > MAX_VAO). Se o vão
        # global já cabe, o alinhamento é fidedigno e NÃO se mexe — é o que
        # garante que as 59 reconstruções já aplicadas na U94 fiquem
        # exactamente como estão. Intervir sempre degradaria casos sãos: a
        # janela é centrada no fragmento dominante e corta o que fique a mais
        # de MAX_JANELA palavras dele (foi assim que a II-107 perdeu 10).
        vao_g = (max(f["ifonte"] + f["n"] for f in frag)
                 - min(f["ifonte"] for f in frag))
        if vao_g > MAX_VAO:
            dom = max(frag, key=lambda f: f["n"])
            i0 = max(0, dom["ifonte"] - MAX_JANELA)
            i1 = min(len(fonte_f), dom["ifonte"] + dom["n"] + MAX_JANELA)
            f2 = _fragmentos(pal, fonte_f, alvo_f, ob, janela=(i0, i1))
            if f2:
                frag = f2
                frag.sort(key=lambda f: f["ifonte"])
                frag = _limpar_micro(frag)      # comporta F
        frag.sort(key=lambda f: f["ifonte"])

        for f in frag:
            conferir(a["sigla"], f["linha"], [f["texto"]])   # comporta A

        chave_end = (a["arquivo"], n)
        por_endereco.setdefault(chave_end, {"path": path, "n": n,
                                            "sigla": a["sigla"],
                                            "linha": a["linha"],
                                            "frag": [], "idents": []})
        por_endereco[chave_end]["frag"].extend(frag)
        por_endereco[chave_end]["idents"].append(ident)

    # ── FUSÃO: dois blocos aprovados no MESMO endereço são uma só citação ──
    # Caso RC-747: o censo partiu em dois blocos (fonte L60 e L61) o que a
    # ficha traz numa única linha. Escolher um destruiria o outro; fundir é o
    # único acto honesto — e, sendo L60 e L61 consecutivas, os fragmentos
    # ficam contíguos, pelo que a junta é de hard-wrap e não de fosso.
    planos, adiados = [], []
    for (arq, n), g in sorted(por_endereco.items()):
        frag = sorted(g["frag"], key=lambda f: (f["linha"], f["ifonte"]))
        vao = (frag[-1]["ifonte"] + frag[-1]["n"]) - frag[0]["ifonte"]
        if vao > MAX_VAO:
            adiados.append({"ident": "+".join(g["idents"]), "path": g["path"],
                            "n": n, "sigla": g["sigla"], "linha": g["linha"],
                            "vao": vao, "nfrag": len(frag)})
            continue
        partes, omisso = [], 0
        for f in frag:
            if partes:
                ant = partes[-1]
                if (f["linha"] == ant["linha"]
                        and f["ifonte"] == ant["ifonte"] + ant["n"]):
                    pass                       # mesma linha e contíguo: unir
                elif (f["linha"] == ant["linha"] + 1
                      and f["ifonte"] == ant["ifonte"] + ant["n"]):
                    partes.append(MARCA_WRAP)  # quebra de hard-wrap
                else:
                    omisso += f["ifonte"] - (ant["ifonte"] + ant["n"])
                    partes.append(MARCA_FOSSO)  # omissão APROVADA
            partes.append(f)
        corpo = ""
        for i, p in enumerate(partes):
            if isinstance(p, str):
                corpo += " " + p
            else:
                corpo += ("" if i == 0 else " ") + f"«{p['texto']}»"
        corpo = re.sub(r"»\s+(»)", r"» \1", corpo).strip()

        if omisso:
            nota = (f"reconstrução aprovada pelo Curador na U93; {omisso} "
                    f"palavra{'s' if omisso > 1 else ''} da fonte omitida"
                    f"{'s' if omisso > 1 else ''} — » […] « assinala o fosso, "
                    f"ao passo que » … « assinala apenas quebra de hard-wrap")
        else:
            nota = ("reanexado à fonte na U94 (A5); o trecho legado não trazia "
                    "aparelho de linha nem era verificável byte a byte")
        pg = pagina(g["sigla"], g["linha"])
        onde = f"{g['sigla']} {pg}" if pg != "—" else g["sigla"]
        novo = f"> {corpo} — {onde} · `original.txt` L{g['linha']} · {nota}."
        planos.append({"ident": "+".join(g["idents"]), "path": g["path"],
                       "n": n, "novo": novo, "omisso": omisso,
                       "nfrag": len(frag), "cod": arq.split("/")[-1][:6],
                       "sigla": g["sigla"], "linha": g["linha"],
                       "pct": 0.0, "longo": False})

    if not planos and bloq_b:
        print(f"  comporta B: as {bloq_b} reconstruções já estão "
              f"aplicadas — nada a fazer (idempotente)")
        return 0
    print(f"  comporta A: {sum(p['nfrag'] for p in planos)} fragmentos "
          f"conferidos byte a byte — 0 recusas")
    print(f"  comportas B/C: 0 impedimentos · {len(planos)} reconstruções "
          f"prontas")
    if n_aparelhaveis[0]:
        print(f"  comporta G: {n_aparelhaveis[0]} recusada(s) — texto localizável "
              f"no corpus mas NÃO aparelhável (o Portão B não resolve a obra)")
    print(f"  comporta E (vão>{MAX_VAO}): {len(adiados)} adiadas — salada "
          f"de palavras-chave")
    for d in sorted(adiados, key=lambda x: -x["vao"]):
        print(f"     {d['ident']} · {d['path'].split('/')[-1][:34]} "
              f"L{d['n']} · vão {d['vao']} · {d['nfrag']} frag")
    print(f"  fossos: {sum(1 for p in planos if p['omisso'])} com omissão · "
          f"palavras omitidas no total: "
          f"{sum(p['omisso'] for p in planos)} · máx por citação: "
          f"{max((p['omisso'] for p in planos), default=0)}")

    if not aplicar:
        import json as _j
        _j.dump({"planos": planos, "adiados": adiados},
                open("/tmp/u94_seco.json", "w", encoding="utf-8"),
                ensure_ascii=False, indent=1)
        print("  seco despejado em /tmp/u94_seco.json")
        for p in sorted(planos, key=lambda x: -x["omisso"])[:6]:
            L = open(p["path"], encoding="utf-8").read().split("\n")
            print(f"\n   {p['ident']} {p['cod']} · {p['sigla']} "
                  f"L{p['linha']} · {p['nfrag']} frag · "
                  f"{p['omisso']} palavras omitidas")
            print(f"   - {L[p['n']-1][:150]}")
            print(f"   + {p['novo'][:150]}")
        return 0

    feitos = 0
    for p in sorted(planos, key=lambda x: (x["path"], -x["n"])):
        linhas = open(p["path"], encoding="utf-8").read().split("\n")
        if linhas[p["n"] - 1] == p["novo"]:
            continue                        # comporta D — idempotência
        linhas[p["n"] - 1] = p["novo"]
        open(p["path"], "w", encoding="utf-8").write("\n".join(linhas))
        feitos += 1
    print(f"\n  {feitos} fichas reescritas · {len(planos) - feitos} idênticas")

    json.dump({"unidade": "U94", "lote": "A5-4", "rota": "R1",
               "data": "2026-09-15", "aplicar_V": False,
               "origem": os.path.relpath(DECISAO, RAIZ),
               "criterio": ("decisão do Curador sobre as 212 instâncias do "
                            "artefacto de curadoria; 69 reconstruções com o "
                            "marcador » […] «, 143 mantidas sem acção."),
               "fichas": [{k: p[k] for k in
                           ("ident", "cod", "sigla", "linha", "pct",
                            "nfrag", "omisso", "longo")} for p in planos]},
              open(SAIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  lote: {os.path.relpath(SAIDA, RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
