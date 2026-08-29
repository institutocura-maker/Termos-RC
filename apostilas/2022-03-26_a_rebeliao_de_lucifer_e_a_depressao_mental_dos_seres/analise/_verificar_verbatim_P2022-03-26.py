#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR VERBATIM DO CICLO P2022-03-26 — portões A e B.

A — **paridade de aspas**: todo `«…»` balanceado, sem aspa solta, sem trecho com < 8 chars
    entre aspas (marca de colagem truncada).
B — **fidelidade**: toda aspa com ≥ 25 chars de texto dentro de um arquivo de aparato
    (dossiê, camadas, notas, relatório, DECISAO, apostila) deve existir **case-sensitive** no
    `original.txt` com espaços colapsados. Não há exceção por afinidade: ou a aspa bate no
    bruto, ou o arquivo não é escrito.

Regra de casa deste ciclo em diante (herdada de P2020-04-25, R-2): aspas angulares são **só**
de citação verificável. Rótulo de bloco, nome de tema e grafia de dicionário saem de negrito ou
`backticks` — e por isso não passam por aqui.

Quando existir `DECISAO-DO-CURADOR.md`, o §1 (a devolutiva verbatim) entra como **2º corpus
declarado**: aspas que citam o Curador continuam auditadas, só que contra o texto em que foram
ditas — nunca afrouxando o teste contra a fonte oral.

A transcrição integral (PARTE I da apostila) **não** é coberta pelo portão A — ela é verbatim do
bruto e carrega as aspas retas do STT; ela é coberta por `_cobertura_apostila.py`.
"""
import os, re, sys, glob

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
BRUTO = " ".join(open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().split())

DEC = os.path.join(CICLO, "DECISAO-DO-CURADOR.md")
DEVOL = ""
if os.path.exists(DEC):
    _t = open(DEC, encoding="utf-8").read()
    if "## 1." in _t and "## 2." in _t:
        _t = _t.split("## 1.")[1].split("## 2.")[0]
        DEVOL = " ".join(re.sub(r"[>*`_#]", " ", _t).split()).casefold()

ARQS = [os.path.relpath(f, CICLO) for f in
        glob.glob(os.path.join(CICLO, "*.md")) + glob.glob(os.path.join(AQUI, "*.md")) +
        glob.glob(os.path.join(AQUI, "*.txt"))]
ARQS = [a for a in sorted(set(ARQS)) if not a.endswith(("leitura-segmentada.txt",)) and "/leitura/" not in a]

err_A, err_B = [], []
n_frag = n_dev = 0
for rel in ARQS:
    txt = open(os.path.join(CICLO, rel), encoding="utf-8").read()
    if rel.endswith((".md", ".txt")) and rel != "apostila.md" and txt.count("«") != txt.count("»"):
        err_A.append(f"{rel}: « = {txt.count('«')} vs » = {txt.count('»')}")
    for m in re.finditer(r"«([^»]{1,4000})»", txt, re.S):
        dentro = " ".join(m.group(1).split())
        if len(dentro) < 14 and " " in dentro and len(dentro.split()) > 3:
            err_A.append(f"{rel}: aspa curta demais (colar?): «{dentro}»")
        if len(dentro) >= 25 and "…" not in dentro:
            n_frag += 1
            cand = dentro.replace("…", "").strip()
            partes = [p.strip(" .,;") for p in re.split(r"[\"“”]", cand) if len(p.strip()) >= 25]
            for p in partes or [cand]:
                if p not in BRUTO:
                    if re.sub(r"[*`_]", "", p).strip().casefold() in DEVOL:
                        n_dev += 1
                        continue
                    err_B.append(f"{rel}: não encontrado no bruto → «{p[:110]}»")

print(f"arquivos testados: {len(ARQS)} · fragmentos longos testados: {n_frag} · aspas conferidas no 2º corpus (devolutiva): {n_dev}")
print(f"portão A (paridade de aspas): {len(err_A)} problema(s)")
for e in err_A[:12]:
    print("  ⚠️", e)
print(f"portão B (verbatim): {len(err_B)} divergência(s)")
for e in err_B[:15]:
    print("  ✗", e)
ok = not err_A and not err_B
print("\nRESULTADO:", "CITAÇÕES FIEL À FONTE ✓" if ok else "REVISAR ⚠️")
sys.exit(0 if ok else 1)
