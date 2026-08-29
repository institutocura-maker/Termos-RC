#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vincula a fonte P2022-03-26 na malha (`ferramentas/dados_termos.py`).

Espelho de `_vincular_fonte_P2020-04-25.py` (que é espelho do de P2023-10-14), com as diferenças deste ciclo:

 1. acrescenta `'P2022-03-26'` à lista de FONTES de **todo** código que recebeu bloco no pacote
    (`### RC-xxx`), inclusive os `ficha=False` — o vínculo de malha existe sem arquivo
    (precedentes: RC-385/P2023-06-24, RC-272/P2023-10-14);
 2. materializa **o único código autorizado** pela devolutiva (D-9): `RC-089` —
    `ficha=False` → `ficha=True`; o arquivo `termos/RC-089-processador-val.md` é criado **antes**,
    por `_gerar_ficha_RC089_P2022-03-26.py`, e este script recusa o flip se ele não existir.

**`RELACOES` NÃO É TOCADA** — teto de 1.856 arestas (D-8: «+0 códigos, +0 relações, +0 obras»).
Nenhum termo novo, nenhum status alterado, nenhuma obra criada. A devolutiva aprovou a tabela de vínculos
inteira e não autorizou exclusão nominal de nenhum, então `EXCLUIDOS` está vazio **por leitura da decisão**,
não por esquecimento. `RC-444 Família Cromon` segue `ficha=False` por ordem expressa (D-9).
"""
import re, sys, os
from pathlib import Path

def _resolve_raiz(inicio):
    d = os.path.abspath(inicio)
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d

RAIZ = Path(_resolve_raiz(Path(__file__).resolve().parent))
DADOS = RAIZ / "ferramentas" / "dados_termos.py"
AQUI = Path(__file__).resolve().parent
PACOTE = AQUI / "_ampliacoes_P2022-03-26.txt"
SIGLA = "P2022-03-26"
MATERIALIZAR = ["RC-089"]
EXCLUIDOS = []

codigos = sorted(set(re.findall(r"^### (RC-\d{3})$", PACOTE.read_text(encoding="utf-8"), re.M)))
alvos = sorted(set(codigos) | set(MATERIALIZAR))
print(f"códigos no pacote: {len(codigos)} · alvos na malha: {len(alvos)}")

LINHA_TERMOS = re.compile(r'^\s*\("(RC-\d{3})", .*, [A-Z_]+\[\d+\], [A-Z_]+\[\d+\], [A-Z]+,\s*\[')
ITEM = r"(?:\"[^\"]*\"|'[^']*')"
LISTA = re.compile(r"\[(" + ITEM + r"(?:,\s*" + ITEM + r")*)\]")

linhas = DADOS.read_text(encoding="utf-8").split("\n")
tocadas, puladas, flipadas, avisos = [], [], [], []
for i, ln in enumerate(linhas):
    m = LINHA_TERMOS.match(ln)
    if not m:
        continue
    cod = m.group(1)
    if cod in EXCLUIDOS and cod not in alvos:
        avisos.append(f"{cod} excluído por decisão — linha intocada")
        continue
    if cod not in alvos:
        continue
    novo = ln
    if f'"{SIGLA}"' not in novo and f"'{SIGLA}'" not in novo:
        fm = LISTA.search(novo)
        if fm:
            atual = fm.group(1)
            aspa = "'" if atual.count("'") >= atual.count('"') else '"'
            extra = f", {aspa}{SIGLA}{aspa}" if atual.strip() else f"{aspa}{SIGLA}{aspa}"
            novo = novo[:fm.start(1)] + atual + extra + novo[fm.end(1):]
            tocadas.append(cod)
        else:
            puladas.append(cod + " (sem lista de fontes)")
    else:
        puladas.append(cod + " (fonte já presente)")
    if cod in MATERIALIZAR:
        arq = list((RAIZ / "termos").glob(f"{cod}-*.md"))
        if not arq:
            flipadas.append(f"{cod} SEM ARQUIVO — ficha não flipada")
            novo = ln
        elif novo.rstrip().endswith(", False),"):
            novo = novo[:novo.rindex("False")] + "True),"
            flipadas.append(cod)
        else:
            assert novo.rstrip().endswith(", True),"), novo[-40:]
            flipadas.append(cod + " (já materializada)")
    linhas[i] = novo

DADOS.write_text("\n".join(linhas), encoding="utf-8")
print(f"fontes vinculadas: {len(tocadas)}")
print("materializações:", ", ".join(flipadas) if flipadas else "—")
if puladas:
    print("observações:", "; ".join(puladas))
falt = [c for c in alvos if c not in tocadas and not any(c in p for p in puladas)]
if falt:
    print("NÃO ENCONTRADOS NA MALHA:", falt)
    sys.exit(1)
if any("SEM ARQUIVO" in f for f in flipadas):
    print("ERRO: materialização sem arquivo — crie os .md antes de rodar")
    sys.exit(1)
