#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR DE COBERTURA DA APOSTILA — P2021-05-15.

Prova duas coisas, e só estas, porque são as que a esteira exige:

 1. **Fidelidade:** todo parágrafo de transcrição da apostila é substring do
    `original.txt` (ou é o marcador declarado de bloqueio). Ou seja: nada foi
    reescrito, resumido ou "melhorado".
 2. **Cobertura:** a união dos parágrafos cobre o texto falado inteiro, com a
    única lacuna autorizada (o trecho de vida pessoal bloqueado pelo Curador).

Roda de `analise/` e imprime o veredito. Saída 0 = ok.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
src = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n")
apos = open(os.path.join(CICLO, "apostila.md"), encoding="utf-8").read()

S = " ".join(src.split())
MARCADOR = "[TRECHO BLOQUEADO POR DECISÃO DO CURADOR"

# a transcrição vai de "# PARTE I" até "# PARTE II"
ini = apos.index("# PARTE I —")
fim = apos.index("# PARTE II —")
corpo = apos[ini:fim]

paragrafos, cabeçalhos = [], []
for l in corpo.split("\n"):
    s = l.strip()
    if not s:
        continue
    if s.startswith("#"):
        cabeçalhos.append(s)
    elif s.startswith("*Nota editorial:*"):
        continue                                   # aparato, não transcrição
    else:
        paragrafos.append(s)

fora = [p for p in paragrafos if " ".join(p.split()) not in S and MARCADOR not in p]
print(f"parágrafos de transcrição: {len(paragrafos)} · cabeçalhos de bloco: {len(cabeçalhos)}")
print(f"parágrafos NÃO encontrados na fonte: {len(fora)}")
for p in fora[:5]:
    print("  ✗", p[:150])

# cobertura: o texto reconstruído dos parágrafos TEM de ser o da fonte, com o
# bloqueio aplicado no mesmo lugar. Nada mais, nada menos.
blobs = [" ".join(p.split()) for p in paragrafos]
rec = " ".join(blobs)
rec = re.sub(re.escape(MARCADOR) + r"[^\]]*\]", " ", rec)   # o marcador não é fala
ini_falado = S.index("Olá, pessoal.")
falado = S[ini_falado:]
a, b = src.find("Que coisa boa. Só assim eu paro."), src.find("só fiz me ferrar.") + len("só fiz me ferrar.")
n_bloqueio = 1 if a >= 0 else 0
if a >= 0 and b > a:
    bruto = " ".join(src[:a].split())
    cortado = " ".join(src[b:].split())
    falado_esperado = " ".join((bruto + " " + cortado).split())
    # recomeça do ponto de "Olá" e ignora o cabeçalho/tail do arquivo
    falado_esperado = falado_esperado[falado_esperado.index("Olá, pessoal."):]
    rec_aj = rec if rec.startswith("Olá") else rec
else:
    falado_esperado = falado
    rec_aj = rec
igual = " ".join(rec_aj.split()) == " ".join(falado_esperado.split())
print(f"\ntexto reconstruído == fonte (com o bloqueio aplicado): {igual}")
if not igual:
    import difflib
    r = difflib.SequenceMatcher(None, rec_aj, falado_esperado)
    print(f"similaridade: {100 * r.ratio():.3f}%")
    for tag, i1, i2, j1, j2 in r.get_opcodes():
        if tag != "equal":
            print(f"  {tag}: apostila[{i1}:{i2}]={rec_aj[i1:i2][:90]!r}  fonte[{j1}:{j2}]={falado_esperado[j1:j2][:90]!r}")
    sys.exit(1)
print(f"cobertura: 100% do texto falado, com {n_bloqueio} lacuna autorizada pelo Curador "
      f"({len(' '.join(src[a:b].split())) if a >= 0 else 0} chars não transcritos, declarados no local)")

ok = not fora and igual
print("\nRESULTADO:", "TRANSCRIÇÃO ÍNTEGRA E FIEL ✓" if ok else "REVISAR ⚠️")
sys.exit(0 if ok else 1)
