#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vincula a fonte P2021-05-15 na malha (ferramentas/dados_termos.py).

O que faz, e somente isto:
 1. acrescenta 'P2021-05-15' à lista de FONTES de cada código do pacote de ampliações
    (fichas ampliadas) e dos códigos `ficha=False` do Bloco 2 — precedente: RC-385,
    que carrega 'P2023-06-24' sem ter ficha;
 2. materializa RC-464: `ficha=False` → `ficha=True` (o arquivo `termos/RC-464-*.md`
    passou a existir; decisão do Curador, Devolutiva O-8).

**RELACOES NÃO É TOCADA** — teto de 1.856 arestas (Devolutiva O-8). Nenhum termo novo,
nenhum código novo, nenhum status alterado.
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DADOS = RAIZ / "ferramentas" / "dados_termos.py"
AQUI = Path(__file__).resolve().parent
PACOTE = AQUI / "_ampliacoes_P2021-05-15.txt"
SIGLA = "P2021-05-15"

# códigos com ficha ampliada: vêm do próprio pacote (### RC-xxx)
codigos = sorted(set(re.findall(r"^### (RC-\d{3})$", PACOTE.read_text(encoding="utf-8"), re.M)))
# Bloco 2 — termos sem ficha, mas com conteúdo textual nesta fonte (RC-089 fica fora:
# o pacote declara que a fonte não traz conteúdo próprio para ele).
SEM_FICHA = ["RC-186", "RC-401", "RC-035", "RC-093", "RC-031", "RC-075", "RC-017", "RC-018", "RC-189"]
alvos = sorted(set(codigos) | set(SEM_FICHA))

linhas = DADOS.read_text(encoding="utf-8").split("\n")
tocadas, puladas = [], []
# só a TABELA TERMOS: (code, nome, CAT[0], CAT[1], status, [fontes], rel, ficha)
# (as linhas de RELACOES não têm o padrão `CAT[0], CAT[1]`, ficam fora por construção)
LINHA_TERMOS = re.compile(r'^\s*\("(RC-\d{3})", .*, [A-Z_]+\[\d+\], [A-Z_]+\[\d+\], [A-Z]+,\s*\[')
for i, ln in enumerate(linhas):
    m = LINHA_TERMOS.match(ln)
    if not m or m.group(1) not in alvos:
        continue
    cod = m.group(1)
    novo = ln
    # a lista de FONTES é o primeiro [ … ] cujos itens são todos string citada
    # (o padrão `SER_EXT[0]` da categoria não entra — por isso o teste abaixo).
    ITEM = r"(?:\"[^\"]*\"|'[^']*')"
    LISTA = re.compile(r"\[((?:" + ITEM + r")(?:,\s*" + ITEM + r")*)\]")
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
    if cod == "RC-464":
        if novo.rstrip().endswith(", False),"):
            novo = novo[:novo.rindex("False")] + "True),"
        else:
            assert novo.rstrip().endswith(", True),"), novo[-40:]   # já materializada
    linhas[i] = novo

DADOS.write_text("\n".join(linhas), encoding="utf-8")
print(f"fontes vinculadas: {len(tocadas)} · {', '.join(tocadas[:8])} …")
if puladas:
    print("observações:", "; ".join(puladas))
esperados = set(alvos) - {c for c in tocadas if True}
falt = [c for c in alvos if c not in tocadas and not any(c in p for p in puladas)]
if falt:
    print("NÃO ENCONTRADOS NA MALHA:", falt)
    sys.exit(1)
