#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vincula a fonte P2023-10-14 na malha (ferramentas/dados_termos.py).

O que faz, e somente isto (espelho de `_vincular_fonte_P2021-05-15.py`):
 1. acrescenta 'P2023-10-14' à lista de FONTES de cada código que recebeu bloco no
    pacote de ampliações (`### RC-xxx`) — inclusive os `ficha=False` que ganham vínculo
    de malha sem arquivo (precedente: RC-385 com 'P2023-06-24');
 2. materializa os cinco códigos autorizados na Devolutiva (item 11):
    `ficha=False` → `ficha=True` — os arquivos `termos/RC-xxx-*.md` já existem quando
    este script roda (a criação dos arquivos vem antes, no mesmo bloco de aplicação).

**RELACOES NÃO É TOCADA** — teto de 1.856 arestas. Nenhum termo novo, nenhum código novo,
nenhum status alterado, nenhuma obra criada (B013 já existe; Devolutiva item 4).

Ficam **fora** da malha, por decisão do Curador e por checagem: RC-396 (Kvasir não é
pronunciado nesta fonte), RC-672 (a contagem «366» não ocorre na fonte) e RC-167 (conteúdo
de leitura apenas). Os três vivem no BLOCO 2 do pacote, não na tabela.
"""
import re, sys, os
from pathlib import Path

def _resolve_raiz(inicio):
    """Sobe até o diretório que contém `ferramentas/` — funciona antes e depois do
    engavetamento da pasta do ciclo em `apostilas/CONCLUIDAS/`."""
    d = os.path.abspath(inicio)
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d

RAIZ = Path(_resolve_raiz(Path(__file__).resolve().parent))
DADOS = RAIZ / "ferramentas" / "dados_termos.py"
AQUI = Path(__file__).resolve().parent
PACOTE = AQUI / "_ampliacoes_P2023-10-14.txt"
SIGLA = "P2023-10-14"
MATERIALIZAR = ["RC-322", "RC-425", "RC-432", "RC-381", "RC-191"]
EXCLUIDOS = ["RC-396", "RC-672", "RC-167"]

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
        nome = re.match(r'^\s*\("RC-\d{3}", "((?:[^"\\]|\\.)*)"', novo).group(1)
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
if avisos:
    print("fora da malha:", "; ".join(avisos))
falt = [c for c in alvos if c not in tocadas and not any(c in p for p in puladas)]
if falt:
    print("NÃO ENCONTRADOS NA MALHA:", falt)
    sys.exit(1)
if any("SEM ARQUIVO" in f for f in flipadas):
    print("ERRO: materialização sem arquivo — crie os .md antes de rodar")
    sys.exit(1)
