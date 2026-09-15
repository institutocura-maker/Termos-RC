#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXTRACTOR DE FRAGMENTOS A5 — reanexação de citações legadas ao corpus
=====================================================================

O que este script resolve
-------------------------
A dívida **A5** não é «conhecimento perdido»: é «conhecimento presente numa
forma que o Portão B não reconhece». Os 658 blocos não-verbatim já estão
escritos nas fichas; o censo da U86 leu-os de lá. O que lhes falta é

  1. o **span exacto** na fonte (a transcrição legada trunca, elide, suaviza);
  2. o **aparelho de linha** R1 — `— SIGLA pg · original.txt LNNN`.

Este script produz (1) e (2) para os blocos que têm localização conhecida
(`ancora != null` no censo), e emite um **lote declarativo** para o aplicador
cirúrgico `reintegrar_citacoes.py`.

Porquê um lote declarativo
--------------------------
O `materializar_lote.py` NÃO serve: o seu `corpo()` regenera a ficha inteira a
partir de um molde de 7 secções e destruiria `Ampliação`/`Atualização`/
`Reforço`. A A5 precisa de cirurgia. Mas a cirurgia continua a ser **dados**:
o lote é a fonte da verdade, o aplicador é uma função pura dele.

O alinhamento
-------------
A fonte é *hard-wrapped*: uma sentença ocupa várias linhas físicas. E o
Portão B (`conferir()`) exige que cada fragmento entre «» caiba **dentro de
uma única linha física**. Logo o algoritmo é:

  1. localizar o bloco NA FICHA (o censo trunca o trecho com «…»; a ficha
     tem a linha completa — é ela que se repara);
  2. alinhar as palavras do trecho contra o parágrafo-fonte com
     `difflib.SequenceMatcher` (blocos de correspondência);
  3. agrupar as palavras correspondidas **por linha física de origem**, e
     para cada grupo recolher o SUBSTRING REAL da linha (o que garante, por
     construção, que `conferir()` passa);
  4. medir a cobertura: palavras do trecho cobertas por fragmentos verbatim.

O que não for coberto é EDIÇÃO LEGADA (elisão, suavização, paráfrase). O
extractor nunca a reinventa: simplesmente não a emite. O resultado é sempre
verbatim ou omisso — nunca aproximado.

Uso
---
    python3 ferramentas/extrair_fragmentos_a5.py --saida <lote.json> \
        [--faixa MIN MAX] [--cod RC-002 ...] [--verbose]

Sem `--faixa`, emite todos os blocos com localização.

Este módulo é DIAGNÓSTICO: não escreve em `termos/`.
"""
from __future__ import annotations

import argparse
import collections
import difflib
import glob
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from ferramentas.censo_gap_v2 import (  # noqa: E402
    MARCA_PAGINA, MARCA_AGUA, carregar_corpus,
)
# O Portão B é IMPORTADO DO DRIVER: o mesmo código, não uma reimplementação.
from ferramentas.materializar_lote import conferir, pagina  # noqa: E402

CENSO = os.path.join(RAIZ, "diagnostico", "A5-CITACOES-PRE-PORTAO-B-2026-09-14.json")
TERMOS = os.path.join(RAIZ, "termos")

ABRE = "\"«“'‘*"
FECHA = "\"»”'’*"

# ── comportas de qualidade do PILOTO (U91) ─────────────────────────────────
# G1 cobertura 100%  — nada do que a ficha diz se perde
# G2 citação, não capítulo — o bloco tem de caber num blockquote legível
# G3 nenhum fragmento é só pontuação/símbolo (o «◆ ◆ ◆» separador de verbetes)
# G4 nenhum fragmento traz marca de censura/elisão da transcrição
# G5 o Portão B (`conferir`) aceita cada fragmento na sua linha
MAX_FRAG = 6
MAX_PALAVRAS = 60
SO_SIMBOLO = re.compile(r"^[\s\W\d_\u25c6\u25aa\u2022*=—–-]+$", re.U)
CENSURA = re.compile(r"\*{3,}|\[\s*\]|\[\.\.\.\]")
# aparelho do tipo:  …generalizada." — B031, verbete "Rebelião de Lúcifer
APARELHO = re.compile(r"\s*[—–-]\s*(?:`?)(B\d{3}|P\d{4}-\d{2}-\d{2}[a-z]?)\b.*$",
                      re.S | re.I)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def palavras(s: str) -> list[str]:
    return norm(s).split()


# ── ALINHAMENTO FROUXO (U92) ───────────────────────────────────────────────
# Descoberto ao medir a faixa 90–99%: o fosso NÃO é truncamento nos limites
# (só 16 dos 161 blocos falham no início ou no fim) — é RUÍDO DE TRANSCRIÇÃO
# NO MEIO da sentença. Contagem: 91 fossos são aspas divergentes («'x'» na
# ficha contra «"x"» na fonte), 91 são artefactos («**negrito**», «[…]») e
# 149 têem 1–2 palavras. Apenas 2 blocos têem edição real de prosa.
# Logo: alinha-se com um normalizador que DESPREZA esses artefactos, mas
# EMITE-SE sempre o substring real da fonte — o Portão B continua a exigir
# byte a byte, e o que a ficha ganha é a pontuação da FONTE, não a do
# transcriptor. Nada do conteúdo se perde: o artefacto nunca foi texto-fonte.
LIXO = re.compile(r"[*_`\[\]'\"“”‘’…]")


def frouxo(w: str) -> str:
    """Chave de ALINHAMENTO: ignora pontuação editorial. Nunca usada na emissão."""
    return LIXO.sub("", w).strip(" .,;:!?()").lower()


# ══════════════════════════════════════════════════════════ 1. ler da ficha ──
def indice_de_fichas() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in glob.glob(os.path.join(TERMOS, "*.md")):
        b = os.path.basename(p).split("-")
        out["-".join(b[:2])] = p
    return out


def nucleo_da_linha(linha: str) -> str:
    """Duma linha de ficha, extrai o TRECHO CITADO (sem `>`, sem aspas, sem aparelho)."""
    t = linha.strip()
    if t.startswith(">"):
        t = t[1:].strip()
    t = t.strip(ABRE)
    m = APARELHO.search(t)
    if m:
        t = t[: m.start()]
    t = t.strip()
    t = t.strip(FECHA).strip()
    return t


def localizar_na_ficha(path: str, censo_trecho: str) -> tuple[int, str] | None:
    """
    Acha a linha da ficha que contém o bloco. O censo trunca o trecho com «…»,
    por isso procura-se o PREFIXO (10 palavras) e não o trecho inteiro.
    """
    alvo = palavras(censo_trecho)
    if len(alvo) < 4:
        return None
    chave = " ".join(alvo[:10])
    linhas = open(path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(linhas):
        if chave in norm(ln):
            return i, ln
    # tolerância: 6 palavras
    chave6 = " ".join(alvo[:6])
    for i, ln in enumerate(linhas):
        if chave6 in norm(ln):
            return i, ln
    return None


# ═══════════════════════════════════════════════════ 2. palavras com linha ──
def palavras_com_linha(linhas: list[str], ini: int, fim: int) -> list[tuple[str, int, int, int]]:
    """
    Palavras normalizadas do parágrafo [ini,fim] (1-based, inclusivo), cada uma
    com (palavra, nº da linha, offset inicial, offset final) DENTRO DA LINHA.
    Marcas de página e marcas d'água são suprimidas (como no censo v2).
    """
    out: list[tuple[str, int, int, int]] = []
    for n in range(ini, min(fim, len(linhas)) + 1):
        bruta = linhas[n - 1].rstrip()
        if not bruta.strip():
            continue
        if MARCA_PAGINA.match(bruta) or MARCA_AGUA.match(bruta):
            continue
        for m in re.finditer(r"\S+", bruta):
            w = norm(m.group(0))
            if not w:
                continue
            out.append((w, n, m.start(), m.end()))
    return out


# ══════════════════════════════════════════════════════ 3. alinhamento ──────
def alinhar(alvo: list[str], fonte: list[str]) -> list[tuple[int, int, int]]:
    """Blocos de correspondência (i_alvo, j_fonte, tamanho) via SequenceMatcher."""
    sm = difflib.SequenceMatcher(None, alvo, fonte, autojunk=False)
    return [(i, j, k) for i, j, k in sm.get_matching_blocks() if k > 0]


def fragmentar(blocos: list[tuple[int, int, int]],
               pal_fonte: list[tuple[str, int, int, int]],
               linhas: list[str]) -> list[dict]:
    """
    Converte blocos de correspondência em FRAGMENTOS intra-linha: palavras
    consecutivas na MESMA linha física viram um fragmento cujo texto é o
    substring REAL da linha — logo `conferir()` passa por construção.
    """
    frag: list[dict] = []
    for _i, j, k in blocos:
        # percorre as k palavras da fonte; corta quando a linha muda
        ini = 0
        while ini < k:
            lin0 = pal_fonte[j + ini][1]
            fim = ini
            while fim + 1 < k and pal_fonte[j + fim + 1][1] == lin0:
                fim += 1
            a, b = pal_fonte[j + ini][2], pal_fonte[j + fim][3]
            texto = linhas[lin0 - 1].rstrip()[a:b]
            # o substring pode estar partido por marca d'água/página: só aceita
            # se o texto normalizado bater com as palavras esperadas
            esperado = " ".join(pal_fonte[j + ini + t][0] for t in range(fim - ini + 1))
            if norm(texto) == esperado and texto.strip():
                frag.append({"linha": lin0, "texto": texto,
                             "ifonte": j + ini, "n": fim - ini + 1})
            ini = fim + 1
    # funde fragmentos adjacentes da MESMA linha (ex.: vírgula ÷ palavra)
    unidos: list[dict] = []
    for f in frag:
        if (unidos and unidos[-1]["linha"] == f["linha"]
                and pal_fonte is not None):
            continue
        unidos.append(f)
    return frag


def contiguo(frag: list[dict]) -> bool:
    """Dois fragmentos consecutivos têem de ser contíguos NA FONTE (hard-wrap)."""
    for a, b in zip(frag, frag[1:]):
        if b["ifonte"] != a["ifonte"] + a["n"]:
            return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", required=True)
    ap.add_argument("--faixa", nargs=2, type=float, default=None,
                    metavar=("MIN", "MAX"))
    ap.add_argument("--cod", nargs="*", default=None)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--frouxo", action="store_true",
                    help="alinhar com o normalizador frouxo (ignora pontuação "
                         "editorial); a emissão continua byte a byte")
    a = ap.parse_args()

    censo = json.load(open(CENSO, encoding="utf-8"))
    blocos = [b for b in censo["blocos"] if b.get("ancora")]
    if a.cod:
        blocos = [b for b in blocos if b["codigo"] in set(a.cod)]
    print(f"blocos com localização: {len(blocos)}")

    corpus = carregar_corpus(verbose=False)
    fichas = indice_de_fichas()

    saida: list[dict] = []
    motivos = collections.Counter()
    for b in blocos:
        cod, o, ln = b["codigo"], b["ancora"]["obra"], b["ancora"]["linha"]
        path = fichas.get(cod)
        ob = corpus.get(o)
        if not path or ob is None:
            motivos["ficha/obra ausente"] += 1
            continue
        par = next((p for p in ob.blocos if p["ini"] <= ln <= p["fim"]), None)
        if par is None:
            motivos["linha fora de parágrafo"] += 1
            continue
        loc = localizar_na_ficha(path, b["trecho"])
        if loc is None:
            motivos["bloco não localizado na ficha"] += 1
            continue
        _n, linha_ficha = loc
        nucleo = nucleo_da_linha(linha_ficha)
        alvo = palavras(nucleo)
        if len(alvo) < 4:
            motivos["núcleo curto"] += 1
            continue
        pal_fonte = palavras_com_linha(ob.linhas, par["ini"], par["fim"])
        fonte = [w for w, _l, _a, _b in pal_fonte]
        chave = frouxo if a.frouxo else (lambda w: w)
        blocosm = alinhar([chave(w) for w in alvo], [chave(w) for w in fonte])
        frag = fragmentar(blocosm, pal_fonte, ob.linhas)
        cobertas = sum(k for _i, _j, k in blocosm)
        pct = round(100 * cobertas / len(alvo), 1)

        if a.faixa and not (a.faixa[0] <= pct <= a.faixa[1]):
            motivos["fora da faixa"] += 1
            continue
        if not frag:
            motivos["G1 sem fragmento verbatim"] += 1
            continue
        if pct < 99.5:
            motivos["G1 cobertura < 100%"] += 1
            continue
        if len(frag) > MAX_FRAG or len(alvo) > MAX_PALAVRAS:
            motivos["G2 citação longa (> 6 frag ou > 60 palavras)"] += 1
            continue
        if any(SO_SIMBOLO.match(f["texto"]) for f in frag):
            motivos["G3 fragmento só símbolo"] += 1
            continue
        if any(CENSURA.search(f["texto"]) for f in frag):
            motivos["G4 censura/elisão na transcrição"] += 1
            continue
        try:
            for f in frag:
                conferir(o, f["linha"], [f["texto"]])
        except AssertionError:
            motivos["G5 Portão B recusou"] += 1
            continue
        # G6 — CONTIGUIDADE. Na casa, «» … «» marca QUEBRA DE HARD-WRAP:
        # «quando uma sentença foi partida, o seu início e o seu fecho
        # aparecem como fragmentos distintos». Se entre dois fragmentos a
        # fonte tem palavras que a ficha não trazia (ou que o alinhamento não
        # emparelhou — p.ex. «à» na ficha contra «a» na fonte), então o
        # marcador estaria a encobrir uma OMISSÃO e não uma quebra: é mentira
        # estrutural, e o bloco sai do piloto para juízo curatorial.
        if not contiguo(frag):
            motivos["G6 fragmentos não contíguos na fonte"] += 1
            continue

        # secção REAL, lida da ficha: o censo da U86 registou «Citação-chave»
        # no singular, rótulo que a A4 (U89) unificou em «Citações-chave».
        linhas_f = open(path, encoding="utf-8").read().split("\n")
        sec_real = next((linhas_f[j] for j in range(_n, -1, -1)
                         if linhas_f[j].startswith("## ")), "?")
        saida.append({
            "cod": cod,
            "secao": sec_real,
            "secao_censo_u86": b["secao"],
            "sigla": o,
            "linha": min(f["linha"] for f in frag),
            "chave": " ".join(palavras(b["trecho"])[:10]),
            "trecho_atual": nucleo,
            "palavras": len(alvo),
            "cobertura": pct,
            "alinhamento": "frouxo" if a.frouxo else "estrito",
            "cobertas": cobertas,
            "fragmentos": [[f["linha"], f["texto"]] for f in frag],
            "nota": ("reanexado à fonte na U91 (A5); o trecho legado era fiel ao "
                     "sentido mas não trazia aparelho de linha nem era verificável "
                     "byte a byte"),
        })

    print(f"extraídos (aprovados nas comportas G1–G5): {len(saida)}")
    for k, v in motivos.most_common():
        print(f"  — {k}: {v}")

    bandas = collections.Counter()
    for s in saida:
        p = s["cobertura"]
        bandas["100%" if p >= 99.5 else "90–99%" if p >= 90 else
               "70–89%" if p >= 70 else "50–69%" if p >= 50 else "<50%"] += 1
    print("\ncobertura dos extraídos:")
    for k in ["100%", "90–99%", "70–89%", "50–69%", "<50%"]:
        if bandas.get(k):
            print(f"   {k:8s} {bandas[k]:4d}")

    lote = {
        "unidade": "U91",
        "lote": "A5-1",
        "rota": "R1",
        "data": "2026-09-15",
        "aplicar_V": False,
        "criterio": (
            "A5/{} — reanexação dos blocos legados com localização conhecida no ".format(
                "U92" if a.frouxo else "U91") + 
            "corpus. Comportas: G1 cobertura 100% (nada do que a ficha diz se "
            "perde) · G2 <= 6 fragmentos e <= 60 palavras (é citação, não "
            "capítulo) · G3 nenhum fragmento só de símbolos · G4 nenhuma marca "
            "de censura/elisão · G5 Portão B (`conferir`, importado do driver) "
            "aceita cada fragmento na sua linha. Os 25 blocos reprovados por "
            "G2 ficam para unidade própria: não se trunca citação para caber "
            "no blockquote, porque truncar seria suprimir conteúdo da ficha."
            + (" ALINHAMENTO FROUXO: a chave de alinhamento despreza pontuação "
               "editorial (aspas divergentes, **negrito**, […]) porque se mediu "
               "que 159 dos 161 blocos desta faixa divergem por ARTEFACTO e não "
               "por conteúdo; a emissão, porém, é sempre o substring real da "
               "linha-fonte, conferido byte a byte." if a.frouxo else "")),
        "nota_hardwrap": (
            "**Fratura de hard-wrap:** a edição digital das fontes quebra as "
            "sentenças em linhas curtas. Cada fragmento entre «» é verbatim "
            "**intra-linha**, conferido byte a byte contra o `original.txt` da "
            "obra declarada; quando uma sentença foi partida, o seu início e o "
            "seu fecho aparecem como fragmentos distintos, unidos por » … «."),
        "fichas": saida,
    }
    json.dump(lote, open(a.saida, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\nescrito: {a.saida}")

    if a.verbose:
        for s in saida[:8]:
            print(f"\n── {s['cod']} · {s['sigla']} L{s['linha']} · "
                  f"{s['palavras']}p · cobertura {s['cobertura']}% · "
                  f"{len(s['fragmentos'])} frag")
            print(f"   antes : {s['trecho_atual'][:150]}")
            for l, t in s["fragmentos"][:5]:
                print(f"   L{l:<6d} «{t[:90]}»")
    return 0


if __name__ == "__main__":
    sys.exit(main())
