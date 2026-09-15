#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REEMITIR VERBETES — U94 (a outra metade do mesmo commit)
========================================================

Doutrina da U87: «mudar uma ficha obriga a reemitir os verbetes que a citem
**no mesmo commit**». A U94 reescreveu 59 citações nas fichas; logo os verbetes
que as citavam passaram a mentir, e a suíte T5 fica vermelha até serem
reemitidos.

Por que não reusar `reemitir_verbetes_a5.py` (U92)
--------------------------------------------------
Aquele reemissor reconstrói o verbatim como `" … ".join(«fragmento»)` — uma
junta ÚNICA para todo o lote. Na U92 isso era correcto porque todas as juntas
eram quebra de hard-wrap. A U94 introduziu DOIS marcadores com significados
diferentes (despacho do Curador):

    » … «    quebra de hard-wrap da fonte — nenhuma palavra omitida
    » […] «  omissão APROVADA pelo Curador — há palavras da fonte em falta

Reemitir tudo com ` … ` apagaria essa distinção e o verbete passaria a afirmar
uma coisa falsa. Por isso este reemissor **não reconstrói**: copia o corpo que
a ficha já traz, marcadores incluídos. O verbete passa a dizer exactamente o
mesmo que a ficha, nem mais nem menos.

O que o verificador exige
-------------------------
Todo trecho entre «» de um verbete tem de ocorrer BYTE A BYTE no corpus de
fichas. Os marcadores ficam FORA dos pares «», pelo que não são verificados —
são prosa sinalizadora. Cada fragmento, esse sim, é cópia literal da ficha.

Como se acha o que mudou
------------------------
Por `git diff` contra o HEAD (que é pré-U94): para cada linha substituída,
extrai-se o texto legado (mapa) e o corpo novo (valor). Nada é inferido do
artefacto de curadoria — o Git é a testemunha.

Uso:  python3 ferramentas/reemitir_verbetes_u94.py [--aplicar]
"""

import os
import re
import sys
import json
import difflib
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERBETES = os.path.join(RAIZ, "pedagogico", "enciclopedia", "verbetes")
TERMOS = os.path.join(RAIZ, "termos")
CIT = re.compile(r"«([^»]+)»")
MARCA_WRAP = "» … «"
MARCA_FOSSO = "» […] «"


def norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def chave(s: str) -> str:
    """Normalização para casar citações: ignora caixa, acentos, espaços e a
    ênfase markdown (**negrito**), que o texto legado trazia e a fonte não."""
    return norm(s).replace("*", "").replace('"', "")


def _git(*args: str) -> str:
    return subprocess.run(("git", "-C", RAIZ) + args,
                          capture_output=True, text=True,
                          check=True).stdout


def corpo_da_ficha(linha: str) -> str:
    """Extrai o corpo citado de uma linha R1, sem o aparelho final."""
    i = linha.find("`original.txt`")
    if i >= 0:
        j = linha.rfind(" — ", 0, i)
        if j > 0:
            linha = linha[:j]
    return linha.strip()


def texto_legado(linha: str) -> str:
    """Extrai o texto citável de uma linha legada (pré-U94)."""
    s = linha.strip()
    if s.startswith("> "):
        s = s[2:]
    i = s.find("`original.txt`")
    if i >= 0:
        j = s.rfind(" — ", 0, i)
        if j > 0:
            s = s[:j]
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
    return s.replace("**", "").replace("*", "").strip()


def main() -> int:
    aplicar = "--aplicar" in sys.argv

    # ── 1. o mapa: texto legado -> corpo novo (com os DOIS marcadores) ───────
    mudados = [p for p in _git("diff", "--name-only", "--", "termos/").split("\n")
               if p.strip()]
    mapa: dict[str, str] = {}
    for rel in mudados:
        path = os.path.join(RAIZ, rel)
        antigo = _git("show", f"HEAD:{rel}").split("\n")
        novo = open(path, encoding="utf-8").read().split("\n")
        sm = difflib.SequenceMatcher(None, antigo, novo, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "replace":
                continue
            # só nos interessam substituições linha a linha (1 por 1)
            if i2 - i1 != 1 or j2 - j1 != 1:
                sys.exit(f"  !! {rel}: bloco substituído de tamanho "
                         f"{i2-i1}x{j2-j1} — foge ao padrão 1:1")
            a, b = antigo[i1], novo[j1]
            if "`original.txt`" not in b:
                continue        # a linha nova não traz aparelho R1: foge à U94
            velho = texto_legado(a)
            corpo = corpo_da_ficha(b[2:] if b.startswith("> ") else b)
            if not velho or not corpo:
                sys.exit(f"  !! {rel} L{j1+1}: não extrai velho/corpo")
            # A chave guarda uma LISTA: duas fichas distintas podem citar o
            # mesmo trecho, e o desempate é feito depois pelo código do verbete.
            mapa.setdefault(chave(velho), []).append(
                (os.path.basename(rel)[:6].replace("-", ""), corpo))
    print(f"  mapa: {len(mapa)} citações reconstruídas lidas do git diff")

    # ── 2. o corpus de fichas, para saber que citações ficaram obsoletas ─────
    corpus = ""
    for p in sorted(os.listdir(TERMOS)):
        if p.endswith(".md"):
            corpus += open(os.path.join(TERMOS, p), encoding="utf-8").read()
    notas = os.path.join(RAIZ, "notas", "fichas")
    if os.path.isdir(notas):
        for p in sorted(os.listdir(notas)):
            if p.endswith(".md"):
                corpus += open(os.path.join(notas, p), encoding="utf-8").read()

    # ── 3. as citações dos verbetes que já não ocorrem no corpus ─────────────
    arquivos = sorted(g for g in _git("ls-files", "pedagogico/enciclopedia/verbetes")
                      .split("\n")
                      if g.endswith(".md")
                      and os.path.basename(g).lower() != "readme.md")
    arquivos = [os.path.join(RAIZ, a) for a in arquivos]
    assert arquivos, f"nenhum verbete em {VERBETES}"

    vistos: dict[tuple[str, str], int] = {}
    for arq in arquivos:
        txt = open(arq, encoding="utf-8").read()
        for cit in CIT.findall(txt):
            if cit not in corpus:
                vistos[(arq, cit)] = txt.count(f"«{cit}»")
    print(f"  verbetes: {len(arquivos)} · citações obsoletas: {len(vistos)} "
          f"· ocorrências: {sum(vistos.values())}")

    # ── 4. casar com o mapa ──────────────────────────────────────────────────
    planos: dict[str, list[tuple[str, str]]] = {}
    orfaos = []
    for arq, cit in vistos:
        base = os.path.basename(arq)
        m = re.search(r"RC\d{3}", base)
        dono = m.group(0) if m else None
        cands = list(mapa.get(chave(cit), ()))
        if not cands:                       # o verbete pode citar truncado
            for k, v in mapa.items():
                if chave(cit) in k or k in chave(cit):
                    cands.extend(v)
        if dono:
            afinados = [c for c in cands if c[0].startswith(dono)]
            if afinados:
                cands = afinados
        if len(cands) != 1:
            orfaos.append((base, cit, len(cands)))
            continue
        planos.setdefault(arq, []).append((cit, cands[0][1]))

    if orfaos:
        print(f"\n  !! {len(orfaos)} citações SEM correspondência no lote:")
        for a, c, n in orfaos[:12]:
            print(f"     {a}: {c[:90]} ({n} candidatos)")
        return 1

    # ── 5. escrever ──────────────────────────────────────────────────────────
    n_sub = 0
    for arq, trocas in sorted(planos.items()):
        txt = open(arq, encoding="utf-8").read()
        for cit, corpo in trocas:
            velho = f"«{cit}»"
            if velho not in txt:
                print(f"  !! {os.path.basename(arq)}: «{cit[:60]}» não achado")
                return 1
            n_sub += txt.count(velho)
            txt = txt.replace(velho, corpo)
        if aplicar:
            open(arq, "w", encoding="utf-8").write(txt)
    print(f"  {len(planos)} verbetes · {n_sub} ocorrências reemitidas")

    if not aplicar:
        print("  --aplicar NÃO passado: nada escrito.")
        return 0

    saida = os.path.join(RAIZ, "diagnostico",
                         "U94-VERBETES-REEMITIDOS-2026-09-15.json")
    json.dump({"unidade": "U94", "verbetes": len(planos),
               "ocorrencias": n_sub,
               "ficheiros": sorted(os.path.relpath(a, RAIZ) for a in planos)},
              open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  lote: {os.path.relpath(saida, RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
