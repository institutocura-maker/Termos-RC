#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITORIA VERBATIM v2 — P2021-05-15.

Dois portões, ambos obrigatórios:

A) PARIDADE: toda linha de todo derivado do ciclo deve ter número PAR de aspas duplas.
   Uma aspas solta = texto meu sendo lido como citação (risco de "citação inventada"
   por pareamento espúrio) ou aspas não fechada. Corrigir antes de olhar o portão B.

B) VERBATIM: cada trecho entre aspas duplas com >= 40 caracteres deve existir
   palavra a palavra em `original.txt`, depois de (i) descartar inserções editoriais
   [REVISAR]/[STT…], (ii) tratar `…` como corte permitido (cada segmento é testado)
   e (iii) normalizar espaço/pontuação/caixa. Citações em «» são rótulos desteira e
   não são testadas.

Zero divergências no B + zero linhas ímpares no A == as citações são fiéis à fonte.
Ferramenta de ciclo (não toca a Base); reaproveitada na aplicação e na apostila.
"""
import re, sys, os

RAIZ = os.path.dirname(os.path.abspath(__file__))            # .../analise
CICLO = os.path.dirname(RAIZ)                                 # .../apostilas/<slug>
FONTE = os.path.join(CICLO, "original.txt")

def toks(s):
    s = re.sub(r"\[[^\]]*\]", " ", s).replace("…", " ")
    s = re.sub(r"[^0-9a-zA-ZÀ-ÿ%]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()

def main():
    src = toks(open(FONTE, encoding="utf-8").read().replace("\r\n", "\n"))
    alvos = sorted(p for p in os.listdir(RAIZ)
                   if p.endswith((".md", ".txt")) and not p.startswith("_"))
    paridade = 0
    verbatim = 0
    testados = 0
    for nome in alvos:
        txt = open(os.path.join(RAIZ, nome), encoding="utf-8").read()
        # --- portão A
        for i, lin in enumerate(txt.split("\n"), 1):
            if lin.count('"') % 2:
                paridade += 1
                print(f"✗ [A PARIDADE] {nome}:{i}  nº ímpar de aspas → {lin[:110]}")
        # --- portão B: pareia aspas por linha (a linha é íntegra, portanto o pareamento é determinístico)
        for lin in txt.split("\n"):
            partes = lin.split('"')
            for q in [partes[i] for i in range(1, len(partes) - 1, 2)]:   # pareamento posicional (A garante paridade)
                if q.strip().startswith("|"):
                    continue
                for seg in [x for x in re.split(r"…", q) if len(toks(x)) > 30]:
                    t = toks(seg)
                    if not t:
                        continue
                    testados += 1
                    if t not in src:
                        verbatim += 1
                        w = t.split(" ")[:4]
                        idx = src.find(" ".join(w))
                        hint = " → fonte: " + " ".join(src[idx:idx + 14].split(" ")[:12]) if idx >= 0 else " (início não localizado na fonte)"
                        print(f"✗ [B VERBATIM] {nome}: {seg[:95]}{hint}")
    print(f"\n=== AUDITORIA VERBATIM v2 — {os.path.basename(CICLO)} ===")
    print(f"arquivos: {len(alvos)} · fragmentos longos testados: {testados}")
    print(f"portão A (paridade de aspas): {paridade} problema(s)")
    print(f"portão B (verbatim): {verbatim} divergência(s)")
    print("RESULTADO:", "CITAÇÕES FIEL À FONTE ✓" if paridade == 0 and verbatim == 0 else "REVISAR ⚠️")
    return 1 if (paridade or verbatim) else 0

if __name__ == "__main__":
    sys.exit(main())
