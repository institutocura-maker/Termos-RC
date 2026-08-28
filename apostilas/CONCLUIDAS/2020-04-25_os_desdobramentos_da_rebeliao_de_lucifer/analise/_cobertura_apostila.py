#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR DE COBERTURA DA APOSTILA — P2023-10-14.

Prova três coisas, e só estas, porque são as que a esteira exige (P2020-04-25):

 1. **Fidelidade:** todo parágrafo de transcrição da apostila é substring do
    `original.txt` (normalizado em espaços) — nada foi reescrito, resumido ou «melhorado».
 2. **Cobertura:** a união dos parágrafos reproduz exatamente o texto falado **com os
    spans bloqueados removidos** (lista lida do próprio gerador, `BLOQUEIOS`, para que
    haja uma única fonte de verdade do que foi cortado).
 3. **Trava D-1/D-4:** nenhum span bloqueado aparece na apostila **nem** em `termos/`; e as aspas vedadas
    por **D-3** (mulheres/homoafetivos/«cobaias») não podem aparecer em **nenhuma** seção de ampliação
    deste ciclo nas fichas — aqui a proibição é conferida no material aplicado, não presumida.

Roda de `analise/`. Saída 0 = ok.
"""
import os, re, sys, glob, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))

spec = importlib.util.spec_from_file_location("ger", os.path.join(AQUI, "_gerar_apostila_P2020-04-25.py"))
ger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ger)
BLOQUEIOS = ger.BLOQUEIOS
MARCADOR = ger.MARCADOR

src = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n")
apos = open(os.path.join(CICLO, "apostila.md"), encoding="utf-8").read()

# --- fonte esperada: a partir de U0003, com cada span bloqueado suprimido ---
linhas = src.split("\n")
esperada = []
cortados = 0
n_corte = 0
for i in range(2, len(linhas)):
    s = linhas[i].strip()
    if not s:
        continue
    for ini, fita, motivo, addr in BLOQUEIOS:
        if addr != f"U{i + 1:04d}":
            continue
        a = s.find(ini)
        assert a >= 0, f"âncora de bloqueio ausente em {addr}: {ini[:50]}"
        b = s.find(fita, a) + len(fita) if fita else a + len(ini)
        cortados += b - a
        n_corte += 1
        s = (s[:a] + " " + s[b:]).strip()
    esperada.append(s)
esperado = " ".join(" ".join(" ".join(esperada).split()).split())

# --- apostila: parágrafos de transcrição ---
ini_a = apos.index("# PARTE I —")
fim_a = apos.index("# PARTE II —")
corpo = apos[ini_a:fim_a]
paragrafos, cabecalhos = [], []
for l in corpo.split("\n"):
    s = l.strip()
    if not s:
        continue
    if s.startswith("#"):
        cabecalhos.append(s)
    elif s.startswith("*Nota editorial:*"):
        continue
    else:
        paragrafos.append(s)

S = " ".join(src.split())
fora = [p for p in paragrafos if " ".join(p.split()) not in S and MARCADOR[:24] not in p]
print(f"parágrafos de transcrição: {len(paragrafos)} · cabeçalhos de bloco: {len(cabecalhos)}")
print(f"parágrafos NÃO encontrados na fonte: {len(fora)}")
for p in fora[:5]:
    print("  ✗", p[:150])

rec = " ".join(" ".join(p.split()) for p in paragrafos)
rec = re.sub(re.escape(MARCADOR[:24]) + r"[^\]]*\]", " ", rec)      # o marcador não é fala
rec = " ".join(rec.split())
igual = rec == esperado
print(f"\ncaracteres suprimidos por bloqueio: {cortados} em {n_corte} span(s) · "
      f"cobertura: {100.0 * len(rec) / (len(rec) + cortados):.2f}% do texto falado")
print(f"texto reconstruído == fonte com os bloqueios aplicados: {igual}")
if not igual:
    import difflib
    r = difflib.SequenceMatcher(None, rec, esperado)
    print(f"similaridade: {100 * r.ratio():.3f}%")
    for tag, i1, i2, j1, j2 in r.get_opcodes()[:8]:
        if tag != "equal":
            print(f"  {tag}: apostila[{i1}:{i2}]={rec[i1:i2][:80]!r}  fonte[{j1}:{j2}]={esperado[j1:j2][:80]!r}")

# --- trava do item 10: nada do que foi cortado reaparece em apostila ou fichas ---
vaz = []
for ini, fita, motivo, addr in BLOQUEIOS:
    for alvo, texto in (("apostila.md", apos),):
        if ini in texto:
            vaz.append(f"{addr}:{alvo}:âncora inicial")
    if fita and fita in apos:
        vaz.append(f"{addr}:apostila.md:âncora final")
corpus_fichas = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(RAIZ, "termos", "*.md")))
for ini, fita, motivo, addr in BLOQUEIOS:
    for trecho in (ini, fita):
        if trecho and trecho in corpus_fichas:
            vaz.append(f"{addr}:termos/:{trecho[:40]}")
print(f"\nvazamento de conteúdo bloqueado (apostila + fichas): {len(vaz)}")
for v in vaz:
    print("  ✗", v)

ok = not fora and igual and not vaz and n_corte == len(BLOQUEIOS)
print("\nRESULTADO:", "TRANSCRIÇÃO ÍNTEGRA, FIEL E BLOQUEIOS HONRADOS ✓" if ok else "REVISAR ⚠️")
sys.exit(0 if ok else 1)
