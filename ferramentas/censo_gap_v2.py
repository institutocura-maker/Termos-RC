#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CENSO DO GAP DE FICHAS — v2 (reclassificação sobre o texto recomposto)
=====================================================================

Por que esta v2 existe
----------------------
A v1 (`diagnostico/CENSO-GAP-FICHAS-2026-09-13.json`, 13/09/2026) procurava a
`chave` do termo **dentro de uma única linha** do `original.txt`. Todo o corpus
é hard-wrapped (B024, p.ex., tem 92 chars na maior linha), de modo que qualquer
nome partido pela quebra de linha virava **falso negativo**: códigos com prosa
farta na própria fonte declarada foram parar em «E.não-achado-no-corpus» ou em
«D.só-estrutural». Amostra do estrago, já medida: das 10 Eras da Criação de
B024 §16, três (RC-170/171/172) saíram erradas — uma delas, RC-171, como
«não-achado-no-corpus», o que a guarda E3 usaria para LHE BLOQUEAR o V.

O que a v2 faz de diferente
---------------------------
Reconstrói o parágrafo antes de procurar:
  * linhas consecutivas (sem linha em branco entre elas) viram um BLOCO;
  * o marcador «===== [PÁGINA n] =====» é SUPRIMIDO e não corta o bloco
    (sensibilidade primeiro: era isso que faltava à v1);
  * hífen de translineação (linha finda em «-» e a seguinte começa minúscula)
    é recomposto sem espaço;
  * a busca usa a `chave` normalizada da v1 (sem acentos, caixa baixa, espaços
    colapsados) — muda só a UNIDADE DE BUSCA: parágrafo, não linha.

Prosa × estrutural
------------------
PROSA = bloco com >= MIN_PROSA caracteres E pelo menos MIN_TERMO terminadores
de sentença. Terminador REAL = `[.!?]` seguido de espaço ou fim de bloco e
**não** precedido de dígito — assim o «1.» de sumário/lista fica de fora.

Dois critérios foram testados e ABANDONADOS, e ficam registrados aqui:
  * «tem pontuação» — o SUMÁRIO da B049 (L43-83) passava, e não é prosa;
  * «mediana do comprimento das linhas» — rebaixava prosa autêntica, porque o
    hard-wrap quebra palavras no meio («Projeto» / «Talm») e encurta as linhas.

Classificação v2 (mesmas letras da v1, critério explícito):
  B.prosa-citável-na-fonte-declarada  — achado em PROSA de fonte declarada
  C.prosa-fora-das-fontes-declaradas  — prosa só em obra NÃO declarada
  D.só-estrutural(listas/sumários)    — achado, mas só em bloco estrutural
  E.não-achado-no-corpus              — não achado em lugar nenhum do corpus
  A.alias-variação / F.nome-ambíguo   — juízos de NOME, não de busca: a v2
                                        preserva o veredito da v1 e apenas
                                        anota o que a busca recombinada achou.

Esta unidade é DIAGNÓSTICO: não escreve em `ferramentas/dados_termos.py`,
não cria ficha, não mexe em `relacoes/`, não toca em HOLD.

Uso:
    python3 ferramentas/censo_gap_v2.py
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
import time
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENSO_V1 = os.path.join(RAIZ, "diagnostico", "CENSO-GAP-FICHAS-2026-09-13.json")
SAIDA_JSON = os.path.join(RAIZ, "diagnostico", "CENSO-RECLASSIFICADO-2026-09-13.json")
SAIDA_MD = os.path.join(RAIZ, "diagnostico", "CENSO-RECLASSIFICADO-2026-09-13.md")

BASES = ("livros/CONCLUIDOS", "apostilas/CONCLUIDAS", "ciclos")

# ── AMOSTRAS AUTORIZADAS PARA CITAÇÃO ────────────────────────────────────────
# (sigla, pasta). Só entram as amostras CUJAS PÁGINAS SÃO CONTÍNUAS A PARTIR DA
# PÁGINA 1: quando a obra completa chegar, as páginas seguintes são ACRESCENTADAS
# AO FIM, pelo que a numeração de linhas já citada não se desloca. Numa amostra
# de páginas salteadas, a interpolação das páginas em falta deslocaria tudo e
# cada `original.txt LNNNN` passaria a mentir.
#
# NÃO se ingere `livros/AMOSTRAS` inteiro por duas razões:
#   1. a instrução vigente das fichas de ingresso é «não promover a CONCLUIDOS»;
#      a lista mantém a pasta onde está e não toca na BIBLIO, mas torna o texto
#      verificável pelo Portão B;
#   2. a B061, que lá está, NÃO É OBRA PRIMÁRIA — é glossário pré-repo escrito
#      pelo Curador com ajuda de IA. Cità-la como fonte de Ellam falsificaria a
#      autoria. Fica fora por princípio.
AMOSTRAS_AUTORIZADAS = (
    ("B035", "livros/AMOSTRAS/B035_o_big_data_do_criador"),
)
MARCA_PAGINA = re.compile(r"^\s*=+\s*\[?PÁGINA", re.I)
# Marca d'água do conversor de ebook: ocorre 180× no meio do texto de B031 e,
# se não for suprimida, ENTRA DENTRO do parágrafo recomposto — poluiria a
# citação e partiria ao meio qualquer chave que a atravessasse.
MARCA_AGUA = re.compile(r"^\*+\s*ebook converter DEMO Watermarks\s*\*+$", re.I)
MIN_PROSA = 200           # chars mínimos para um bloco valer como prosa
MIN_TERMO = 2             # terminadores de sentença exigidos
TERMINADOR = re.compile(r'(?<![0-9])[.!?]["”’]?(?=\s|$)')
# Cara de SUMÁRIO/LISTA: linhas curtas (mediana < 20 chars) E pelo menos três
# itens numerados. O SUMÁRIO da B049 (L43-83) tem pontuação suficiente para
# passar por prosa no teste dos terminadores — este é o teste que o barra.
MIN_MED_LISTA = 20
MIN_ITENS = 3
ITEM_NUM = re.compile(r'(?:^|\s)\d{1,3}[.)]\s')


# ──────────────────────────────────────────────────────────── normalização
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).strip().lower()


# ── caixa alta espaçada ─────────────────────────────────────────────────────
# A B044 (e outras) grafam os títulos de capítulo em CAIXA ALTA ESPAÇADA: um
# espaço entre letras, DOIS entre palavras — forma que a busca normalizada não
# alcança (achado da U49: quatro dos oito códigos do lote 6 eram títulos). O
# colapso é legítimo NO LOCALIZADOR. O texto capturado para a ficha permanece
# rigorosamente verbatim, com os espaços da edição (despacho do Curador, U50).
ESPACADA = re.compile(
    r"(?<![\wÀ-ÿ])(?:[A-ZÀ-Ý][ \t]+){1,}[A-ZÀ-Ý](?![\wÀ-ÿ])")

USAR_ESPACADAS = True      # `--sem-espacadas` reproduz o censo v2


def colapsar_espacadas(s: str) -> str:
    def troca(m: re.Match) -> str:
        t = m.group(0)
        # 1 espaço = separador de LETRA (some); 2+ espaços = separador de PALAVRA
        t = re.sub(r"(?<=[A-ZÀ-Ý]) (?=[A-ZÀ-Ý])", "", t)
        return re.sub(r"\s{2,}", " ", t)
    return ESPACADA.sub(troca, s)


def norm2(s: str) -> str:
    """`norm` + colapso de caixa alta espaçada. Só para LOCALIZAR; nunca para citar."""
    return norm(colapsar_espacadas(s)) if USAR_ESPACADAS else norm(s)


def mediana_de(vals: list[int]) -> int:
    if not vals:
        return 0
    v = sorted(vals)
    m = len(v) // 2
    return v[m] if len(v) % 2 else (v[m - 1] + v[m]) // 2


# ─────────────────────────────────────────────────────────────────── índice
class Obra:
    """Uma obra decomposta em blocos (parágrafos recompostos)."""

    __slots__ = ("sigla", "linhas", "blocos")

    def __init__(self, sigla: str, linhas: list[str]):
        self.sigla = sigla
        self.linhas = linhas
        self.blocos: list[dict] = []
        self._recompor()

    def _recompor(self) -> None:
        cur: list[str] = []
        ini = 1
        for i, linha in enumerate(self.linhas, start=1):
            bruta = linha.rstrip()
            if not bruta.strip():
                self._fechar(cur, ini, i - 1)
                cur, ini = [], i + 1
                continue
            if MARCA_PAGINA.match(bruta) or MARCA_AGUA.match(bruta):
                continue                       # suprimido, NÃO corta o bloco
            cur.append(bruta)
        self._fechar(cur, ini, len(self.linhas))

    def _fechar(self, cur: list[str], ini: int, fim: int) -> None:
        brutas = [x.strip() for x in cur if x.strip()]
        if not brutas:
            return
        plano = re.sub(r"\s+", " ", " ".join(brutas)).strip()
        termos = len(TERMINADOR.findall(plano))
        mediana = mediana_de([len(x) for x in brutas])
        partes = []
        for j, ln in enumerate(cur):
            if (ln.endswith("-") and j + 1 < len(cur)
                    and cur[j + 1][:1].islower()):
                partes.append(ln[:-1])         # translineação: sem espaço
            else:
                partes.append(ln + " ")
        # bruto = ANTES de colapsar os espaços: é aí que ainda se distingue
        # 1 espaço (separador de letra) de 2+ (separador de palavra) na caixa
        # alta espaçada. Só o localizador usa o bruto; `texto` segue verbatim
        # para métrica e exibição.
        bruto = "".join(partes)
        texto = re.sub(r"\s+", " ", bruto).strip()
        if not texto:
            return
        lista = (mediana < MIN_MED_LISTA
                 and len(ITEM_NUM.findall(plano)) >= MIN_ITENS)
        self.blocos.append({
            "ini": ini,
            "fim": fim,
            "texto": texto,
            "norm": norm(texto),
            "norm2": norm2(bruto),
            "nlin": len(brutas),
            "mediana_linha": mediana,
            "terminadores": termos,
            "cara_de_lista": lista,
            "prosa": (len(texto) >= MIN_PROSA and termos >= MIN_TERMO
                      and not lista),
        })


def carregar_corpus(verbose: bool = True) -> dict[str, Obra]:
    obras: dict[str, Obra] = {}
    for base in BASES:
        d0 = os.path.join(RAIZ, base)
        if not os.path.isdir(d0):
            continue
        for dd in sorted(os.listdir(d0)):
            sigla = dd.split("_")[0]
            if sigla[:1].isdigit():
                sigla = "P" + sigla
            p = os.path.join(d0, dd, "original.txt")
            if not os.path.exists(p) or sigla in obras:
                continue
            with io.open(p, encoding="utf-8", errors="replace") as fh:
                obras[sigla] = Obra(sigla, fh.read().split("\n"))
    for sigla, rel in AMOSTRAS_AUTORIZADAS:
        p = os.path.join(RAIZ, rel, "original.txt")
        if not os.path.exists(p) or sigla in obras:
            continue
        with io.open(p, encoding="utf-8", errors="replace") as fh:
            obras[sigla] = Obra(sigla, fh.read().split("\n"))

    if verbose:
        nbl = sum(len(o.blocos) for o in obras.values())
        print(f"corpus: {len(obras)} obras · {nbl:,} blocos recompostos",
              flush=True)
    return obras


# ──────────────────────────────────────────────────────────────────── busca
def buscar(obra: Obra, chave: str, modo: str) -> list[dict]:
    """modo='linha' reproduz a v1; modo='bloco' é a v2 (parágrafo recomposto)."""
    achados: list[dict] = []
    if modo == "linha":
        for i, ln in enumerate(obra.linhas, start=1):
            if chave in norm2(ln):
                achados.append({"linha": i, "texto": ln.strip()[:240],
                                "prosa": False})
        return achados
    for b in obra.blocos:
        if chave in b["norm2"]:
            achados.append({
                "linha": b["ini"],
                "linhas": f'{b["ini"]}-{b["fim"]}',
                "texto": b["texto"][:240],
                "prosa": b["prosa"],
                "nlin": b["nlin"],
                "mediana_linha": b["mediana_linha"],
                "terminadores": b["terminadores"],
                "cara_de_lista": b["cara_de_lista"],
            })
    return achados


def tem_bloco(obra: Obra, chave: str) -> bool:
    return any(chave in b["norm2"] for b in obra.blocos)


# ───────────────────────────────────────────────────────────────── relatório
LETRAS = ("A", "B", "C", "D", "E", "F")
NOME_FAM = {
    "A": "alias-variação",
    "B": "prosa citável na fonte declarada",
    "C": "prosa fora das fontes declaradas",
    "D": "só-estrutural (listas/sumários/hard-wrap)",
    "E": "não achado no corpus",
    "F": "nome ambíguo",
}


def _f(x: dict, campo: str) -> str:
    return x[campo].split(".")[0]


def relatorio(saida: list[dict]) -> str:
    from collections import Counter
    c1 = Counter(_f(x, "fam_v1") for x in saida)
    c2 = Counter(_f(x, "fam_v2") for x in saida)
    mudou = [x for x in saida if x["mudou"]]
    L = []
    A = L.append

    A("# Censo reclassificado do gap de fichas — 2026-09-13")
    A("")
    A("Instrumento: `ferramentas/censo_gap_v2.py` · dados: "
      f"`{os.path.relpath(SAIDA_JSON, RAIZ)}`.")
    A("Reproduzir: `python3 ferramentas/censo_gap_v2.py` (~20 s, 158 obras) · "
      "a v2, bit a bit: `python3 ferramentas/censo_gap_v2.py --sem-espacadas "
      "--saida=<base>`.")
    A("")
    if USAR_ESPACADAS:
        A("**Regra v3 — caixa alta espaçada (U50, despacho do Curador):** o "
          "localizador colapsa as sequências de letras separadas por espaço "
          "(um espaço = separador de letra, dois = separador de palavra), "
          "porque a B044, a B022 e outras grafam os títulos de capítulo em "
          "caixa alta espaçada — forma que a busca normalizada não alcança. "
          "**O colapso vale só para localizar:** o texto capturado para as "
          "fichas permanece verbatim, com os espaços da edição.")
        A("")
    else:
        A("**Modo `--sem-espacadas`:** reproz a v2 — o colapso da caixa alta "
          "espaçada fica desligado.")
        A("")
    A("**Unidade de diagnóstico: nada da Base foi alterado** — sem ficha nova, "
      "sem aresta, sem frontmatter, sem HOLD, sem `canonico.json`.")
    A("")
    A("## 1. O que estava errado")
    A("")
    A("O censo v1 procurava a `chave` do termo **dentro de uma única linha** do "
      "`original.txt`. Como todo o corpus é hard-wrapped (a maior linha da B024 "
      "tem 92 caracteres), qualquer nome partido pela quebra de linha virava "
      "**falso negativo**. A v2 reconstrói o parágrafo antes de procurar.")
    A("")
    A("O caso que denunciou a falha: das **10 Eras da Criação** (B024 §16), "
      "três saíram erradas na v1 — e uma delas, **RC-171**, como "
      "«não-achado-no-corpus», o que a guarda **E3** usaria para lhe bloquear "
      "o V presuntivo. Nenhuma das três estava ausente: estavam todas no §16, "
      "com prosa farta — blocos de 35 a 48 linhas cada.")
    A("")
    A("| Código | Era | v1 | v2 | Onde a v2 achou |")
    A("|---|---|---|---|---|")
    for x in saida:
        if x["cod"] in ("RC-156", "RC-157", "RC-158", "RC-159", "RC-168",
                        "RC-169", "RC-170", "RC-171", "RC-172", "RC-173"):
            ev = x["evidencia"][0]
            A(f"| {x['cod']} | {x['nome']} | {_f(x,'fam_v1')} | "
              f"**{_f(x,'fam_v2')}** | {ev['obra']} L{ev.get('linhas')} |")
    A("")
    A("## 2. O quadro")
    A("")
    A("| Família | v1 | v2 | Δ | O que significa |")
    A("|---|---:|---:|---:|---|")
    for f in LETRAS:
        A(f"| {f} · {NOME_FAM[f]} | {c1.get(f,0)} | **{c2.get(f,0)}** | "
          f"{c2.get(f,0)-c1.get(f,0):+d} | — |")
    A("")
    A(f"**{len(mudou)} de {len(saida)} entradas ({len(mudou)*100//len(saida)}%) "
      "mudam de família.**")
    A("")
    A("| de (v1) | para (v2) | quantos |")
    A("|---|---|---:|")
    mx = Counter((_f(x, "fam_v1"), _f(x, "fam_v2")) for x in mudou)
    for (a, b), n in sorted(mx.items(), key=lambda kv: (-kv[1], kv[0])):
        A(f"| {a} | {b} | {n} |")
    A("")
    A("### Leitura")
    A("")
    A(f"- **A família D era majoritariamente artefato.** Dos {c1.get('D',0)} "
      f"códigos que a v1 chamou de «só-estrutural», "
      f"{mx.get(('D','B'),0)} têm prosa citável na própria fonte declarada. "
      "A v1 não os achou porque procurava numa linha só.")
    A(f"- **A família E cresceu ({c1.get('E',0)} → {c2.get('E',0)}).** "
      f"Entraram {mx.get(('C','E'),0)} vindos de C e {mx.get(('D','E'),0)} de D: "
      "códigos que a v1 achava ter Lastro e que, recomposto o texto, não têm "
      "prosa em lugar nenhum — só sumário, nota ou título.")
    A(f"- **A e F ficaram como estavam** ({c1.get('A',0)} e {c1.get('F',0)}): "
      "são juízos sobre o NOME do termo, não sobre a busca no corpus. A v2 "
      "preserva o veredito da v1 e apenas anota o que a busca achou.")
    A("")
    A("## 3. Recorte operacional (quem ainda está sem ficha)")
    A("")
    vivos = [x for x in saida if x.get("sem_ficha")]
    cv = Counter(_f(x, "fam_v2") for x in vivos)
    A(f"Dos {len(saida)} censados, {len(vivos)} seguem sem ficha hoje "
      "(24 já foram materializados nas unidades U41, U42 e U44):")
    A("")
    A("| Família | sem ficha | rota que cabe |")
    A("|---|---:|---|")
    A(f"| B · {NOME_FAM['B']} | **{cv.get('B',0)}** | R1 — materializar |")
    A(f"| C · {NOME_FAM['C']} | {cv.get('C',0)} | R1 com retificação de fontes |")
    A(f"| D · {NOME_FAM['D']} | {cv.get('D',0)} | R1 só com citação estrutural, "
      "ou R3 |")
    A(f"| E · {NOME_FAM['E']} | {cv.get('E',0)} | **fora da R1** — R4 "
      "(declarar ausência / lápide / fusão), depende de despacho |")
    A(f"| A · {NOME_FAM['A']} | {cv.get('A',0)} | despacho taxonômico |")
    A(f"| F · {NOME_FAM['F']} | {cv.get('F',0)} | despacho taxonômico |")
    A("")
    A(f"**O poço de onde a R1 pode tirar é {cv.get('B',0)}, não 47.** A lista "
      "que vinha sendo usada (família B da v1, já descontados os 24 "
      "materializados) não enxergava 95 dos {cv.get('B',0)} códigos que a v2 "
      "enxerga — 67% do poço real, perdidos para o artefato de medição.")
    A("")
    A("## 4. Prova por amostra (promoções D→B)")
    A("")
    A("| Código | Nome | Fonte · linhas | Trecho inicial do bloco recomposto |")
    A("|---|---|---|---|")
    am = [x for x in saida if _f(x, "fam_v1") == "D" and _f(x, "fam_v2") == "B"]
    for x in am[:12]:
        ev = x["evidencia"][0]
        txt = ev["texto"][:110].replace("|", "\\|")
        A(f"| {x['cod']} | {x['nome'][:34]} | {ev['obra']} "
          f"L{ev.get('linhas')} | {txt}… |")
    A("")
    A("## 5. O que a v2 faz, exatamente")
    A("")
    A("1. Linhas consecutivas sem linha em branco entre elas viram um **bloco** "
      "(parágrafo recomposto).")
    A("2. O marcador `===== [PÁGINA n] =====` é suprimido e **não** corta o "
      "bloco — sensibilidade primeiro, era isso que faltava à v1.")
    A("3. A marca d'água do conversor de ebook (`******ebook converter DEMO "
      "Watermarks*******`, 180× na B031) é suprimida: se entrasse no parágrafo, "
      "poluiria a citação e partiria ao meio qualquer chave que a atravessasse.")
    A("4. Hífen de translineação (linha finda em «-» e a seguinte começando "
      "minúscula) é recomposto sem espaço.")
    A("5. A busca usa a `chave` normalizada da v1 (sem acentos, caixa baixa, "
      "espaços colapsados) — muda só a **unidade de busca**: parágrafo, não linha.")
    A("6. Prosa = bloco com ≥ 200 caracteres **e** ≥ 2 terminadores de sentença "
      "**e** sem cara de lista. Terminador real = `[.!?]` seguido de espaço ou "
      "fim e **não** precedido de dígito (o «1.» de sumário fica de fora). Cara "
      "de lista = mediana de linha < 20 chars **e** ≥ 3 itens numerados.")
    A("")
    A("Dois critérios foram testados e abandonados, e ficam registrados: «tem "
      "pontuação» (deixava passar o SUMÁRIO da B049, L43-83) e «mediana do "
      "comprimento das linhas» (rebaixava prosa autêntica, porque o hard-wrap "
      "quebra palavras no meio — «Projeto» / «Talm» — e encurta as linhas).")
    A("")
    A("## 6. Limites desta medição (o que ela NÃO resolve)")
    A("")
    A("- **A chave é o nome do cadastro.** Se a obra grafa o termo de outro "
      "modo, v1 e v2 erram igual — é o caso típico da família F (nome ambíguo, "
      f"{c2.get('F',0)} códigos), que segue dependendo de despacho.")
    A("- **A supressão do marcador de página** pode juntar, num mesmo bloco, o "
      "fim de uma página e o começo da seguinte. Ganha-se em sensibilidade, "
      "perde-se um pouco em precisão; o trecho vai na evidência para conferência.")
    A(f"- **A família E ({c2.get('E',0)}) é um veredito de ausência, não de "
      "inexistência**: o termo pode existir no corpus sob outra grafia, ou a "
      "obra declarada pode estar errada. Antes de qualquer lápide, conferir à mão.")
    A("")
    A("## 7. Os códigos fora da R1 (E, D e C) — para despacho")
    A("")
    for letra, titulo in (("E", "E · não achados no corpus (R4)"),
                          ("D", "D · só-estrutural (R1 restrita ou R3)"),
                          ("C", "C · prosa fora das fontes declaradas")):
        lst = [x for x in vivos if _f(x, "fam_v2") == letra]
        A(f"### {titulo} — {len(lst)}")
        A("")
        A("| Código | Nome | Fontes declaradas |")
        A("|---|---|---|")
        for x in sorted(lst, key=lambda y: y["cod"]):
            A(f"| {x['cod']} | {x['nome']} | {', '.join(x['fontes']) or '—'} |")
        A("")
    A("## 8. Consequência imediata")
    A("")
    A("A R1 vinha sendo executada sobre uma lista submedida em ~70%. Antes de "
      "materializar o lote 3, o Curador precisa decidir se o poço passa a ser "
      f"os {cv.get('B',0)} da família B da v2 — e, com ele, se o V presuntivo "
      "por fonte de livro (despacho de 13/09/2026, escopo: lotes 1 e 2) continua "
      "valendo para os lotes seguintes.")
    A("")
    return "\n".join(L) + "\n"


# ───────────────────────────────────────────────────────────────────── main
def main() -> int:
    global SAIDA_JSON, SAIDA_MD, USAR_ESPACADAS
    args = sys.argv[1:]
    if "--sem-espacadas" in args:
        USAR_ESPACADAS = False                 # censo v2, bit a bit
    else:
        SAIDA_JSON = os.path.join(RAIZ, "diagnostico",
                                  "CENSO-V3-ESPACADAS-2026-09-13.json")
        SAIDA_MD = os.path.join(RAIZ, "diagnostico",
                                "CENSO-V3-ESPACADAS-2026-09-13.md")
    for a in args:
        if a.startswith("--saida="):
            base = a.split("=", 1)[1]
            SAIDA_JSON = os.path.join(RAIZ, "diagnostico", base + ".json")
            SAIDA_MD = os.path.join(RAIZ, "diagnostico", base + ".md")
    t0 = time.time()
    v1 = json.load(io.open(CENSO_V1, encoding="utf-8"))
    obras = carregar_corpus()
    print(f"entradas da v1: {len(v1)}", flush=True)

    saida = []
    for n, e in enumerate(v1, 1):
        chave = e["chave"]
        declaradas = [s for s in (e["fontes"] or []) if s in obras]

        # 1. fonte declarada, busca por LINHA (o método da v1, replicado)
        occ_v1 = sum(len(buscar(obras[s], chave, "linha")) for s in declaradas)

        # 2. fonte declarada, busca por BLOCO recomposto
        ev_dec, prosa_dec = [], False
        for s in declaradas:
            for a in buscar(obras[s], chave, "bloco"):
                ev_dec.append({"obra": s, **a})
                prosa_dec = prosa_dec or a["prosa"]
        ev_dec.sort(key=lambda a: not a["prosa"])   # prosa primeiro na evidência

        # 3. se não há prosa na declarada, procura no corpus inteiro
        ev_fora, prosa_fora, onde_fora = [], False, []
        outras = [s for s in sorted(obras) if s not in declaradas]
        if not prosa_dec:
            for s in outras:
                for a in buscar(obras[s], chave, "bloco"):
                    if a["prosa"]:
                        ev_fora.append({"obra": s, **a})
                        prosa_fora = True
                        if s not in onde_fora:
                            onde_fora.append(s)

        if e["fam"].startswith(("A.", "F.")):
            fam_v2 = e["fam"]                  # juízo de nome: preserva a v1
        elif prosa_dec:
            fam_v2 = "B.prosa-citável-na-fonte-declarada"
        elif prosa_fora:
            fam_v2 = "C.prosa-fora-das-fontes-declaradas"
        else:
            achou = bool(ev_dec) or any(tem_bloco(obras[s], chave)
                                        for s in outras)
            fam_v2 = ("D.só-estrutural(listas/sumários/hard-wrap)" if achou
                      else "E.não-achado-no-corpus")

        saida.append({
            "cod": e["cod"], "nome": e["nome"], "sub": e["sub"],
            "status": e["status"], "fontes": e["fontes"],
            "chave": chave, "alias_v1": e.get("alias", ""),
            "fam_v1": e["fam"], "fam_v2": fam_v2,
            "mudou": e["fam"] != fam_v2,
            "occ_v1_declarada": e.get("occ", 0), "occ_v1_replicada": occ_v1,
            "occ_bloco_declarada": len(ev_dec), "prosa_declarada": prosa_dec,
            "obras_com_prosa_fora": onde_fora,
            "evidencia": (ev_dec or ev_fora)[:3],   # prosa primeiro (ordem posta)
        })
        if n % 50 == 0:
            print(f"  … {n}/{len(v1)} ({time.time() - t0:.0f}s)", flush=True)

    # quem AINDA está sem ficha — a v1 foi lavrada quando eram 273; as unidades
    # U41, U42 e U44 materializaram 24 desde então (leitura, nunca escrita)
    import contextlib
    sem: set[str] = set()
    with contextlib.redirect_stdout(io.StringIO()):
        sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
        try:
            import dados_termos as _d
            sem = {t[0] for t in _d.TERMOS if not t[7]}
        except Exception:                                  # pragma: no cover
            pass
    for x in saida:
        x["sem_ficha"] = x["cod"] in sem

    json.dump(saida, io.open(SAIDA_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    io.open(SAIDA_MD, "w", encoding="utf-8").write(relatorio(saida))
    print(f"JSON -> {os.path.relpath(SAIDA_JSON, RAIZ)} · "
          f"{sum(1 for x in saida if x['mudou'])} de {len(saida)} mudaram "
          f"({time.time() - t0:.0f}s)", flush=True)
    print(f"MD   -> {os.path.relpath(SAIDA_MD, RAIZ)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
