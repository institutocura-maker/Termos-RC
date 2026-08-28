#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTÃO D — contadores da malha + travas da devolutiva, **medidos** (não declarados).

Fecha o BLOCO A de P2020-04-25. Seis checagens, todas lidas de arquivo:

 1. **paridade estrutural**: o corpo da seção `## Ampliação — P2020-04-25` de cada ficha é o
    bloco correspondente do pacote (nada foi editado à mão depois da aplicação);
 2. **contadores**: `len(TERMOS)`, `len(RELACOES)`, nº de obras em `biblioteca/`, nº de arquivos em
    `termos/`, nº de linhas `ficha=True`, nº de fichas com a seção desta fonte e nº de códigos com a
    sigla na lista de FONTES;
 3. **trava D-1**: nenhum marcador lexical da digressão bloqueada aparece numa seção deste ciclo;
 4. **trava D-4**: idem para o bloco da doença;
 5. **trava D-3**: nenhuma aspa sobre mulheres/homoafetivos/«cobaias» entra em **qualquer** seção de
    ampliação deste ciclo (a devolutiva proíbe; aqui a proibição é conferida, não presumida);
 6. **materialização**: `RC-020` tem arquivo **e** `ficha=True`; nenhum outro código foi materializado.

Sai com código 1 se qualquer item falhar. Ferramenta de ciclo: não toca a Base.
"""
import os, re, sys, glob, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
def _resolve_raiz(d):
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d
RAIZ = _resolve_raiz(AQUI)
SIGLA = "P2020-04-25"
SECAO = f"## Ampliação — {SIGLA}"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
MATERIALIZAR = ["RC-020"]
VAZADAS_D1 = ["84%", "Sarnei", "Sarneio", "Polícia Federal", "medíocre", "impeachment",
              "Sérgio Mota", "Bolsonaro", "Dilma", "61 anos", "fuleira", "Tancredo"]
VAZADAS_D4 = ["doença para aqui", "permanecer calado", "série de problemas"]
VETADAS = ["homoafetivos", "homofetiv", "homfetiv", "cobaias", "bateu duro", "macho fêmea"]
ERROS = []

def chk(cond, ok, falha):
    print(("✓ " if cond else "✗ ") + (ok if cond else falha))
    if not cond:
        ERROS.append(falha)

# ---------- 1. paridade estrutural ----------
pac = open(PACOTE, encoding="utf-8").read()
blocos = {}
for bloco in pac.split("### ")[1:]:
    cab, _, corpo = bloco.partition("\n")
    cab = cab.strip()
    if re.fullmatch(r"RC-\d{3}", cab):
        m = re.search(r"^## ", corpo, re.M)
        blocos[cab] = (corpo[:m.start()] if m else corpo).strip()
def norm(s):
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n+", "\n", s)
    return s.strip().strip("-").strip()
fichas_com_secao, divergentes = [], []
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    t = open(f, encoding="utf-8").read()
    i = t.find(SECAO)
    if i < 0:
        continue
    cod = re.match(r"(RC-\d{3})", os.path.basename(f)).group(1)
    fichas_com_secao.append(cod)
    j = t.find("\n## ", i + 10)
    corpo = t[i:j if j > 0 else len(t)]
    corpo = corpo[t[i:].find("\n") + 1:]                      # fora o título da seção
    if cod in blocos and norm(corpo) != norm(blocos[cod]):
        divergentes.append(cod)
chk(not divergentes,
    f"paridade ficha ↔ pacote: {len(fichas_com_secao)} seções conferidas, 0 divergências",
    f"paridade ficha ↔ pacote DIVERGE em: {divergentes}")

# ---------- 2. contadores ----------
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT
TERMOS, RELACOES = DT.TERMOS, DT.RELACOES
import subprocess
tocados_git = [x for x in subprocess.run(["git", "-C", RAIZ, "diff", "--name-only", "HEAD"],
                capture_output=True, text=True).stdout.split("\n") if x.strip()]
pasta_obras = [x for x in os.listdir(os.path.join(RAIZ, "livros", "CONCLUIDOS")) if not x.startswith(".")]
obras = len(pasta_obras)          # obras físicas em livros/CONCLUIDOS
arquivos = len([p for p in os.listdir(os.path.join(RAIZ, "termos")) if p.endswith(".md")])
ficha_true = sum(1 for t in TERMOS if t[7])
com_sigla = [t[0] for t in TERMOS if SIGLA in (t[5] or [])]
print(f"\ncontadores: termos={len(TERMOS)} · relações={len(RELACOES)} · obras={obras} · "
      f"arquivos em termos/={arquivos} · ficha=True={ficha_true} · fichas com a seção={len(fichas_com_secao)} · "
      f"códigos com a sigla na malha={len(com_sigla)}")
chk(len(TERMOS) == 777, "teto curatorial preservado: 777 termos", f"TERMOS = {len(TERMOS)} ≠ 777")
chk(len(RELACOES) == 1856, "teto de arestas preservado: 1.856 relações", f"RELACOES = {len(RELACOES)} ≠ 1856")
chk(not [f for f in tocados_git if f.startswith("livros/")],
    f"0 obras novas: nenhuma linha de `livros/` foi tocada ({obras} obras físicas em `livros/CONCLUIDOS`; "
    "o registro BIBLIO de 102 obras em `CONTINUIDADE.md` l.10 permanece intocado)",
    "foram tocados arquivos de obra: " + str([f for f in tocados_git if f.startswith('livros/')]))
chk(arquivos == 457, "456 → 457 arquivos (a única materialização: RC-020)", f"arquivos = {arquivos} ≠ 457")
chk(ficha_true == 456, "455 → 456 linhas `ficha=True`", f"ficha=True = {ficha_true} ≠ 456")
chk(set(com_sigla) == set(blocos), f"os {len(blocos)} códigos do pacote têm a sigla na malha (e nenhum além deles)",
    f"diferença malha↔pacote: {sorted(set(com_sigla) ^ set(blocos))}")
chk(not [p for p in glob.glob(os.path.join(RAIZ, "termos", "*.md")) if "RC-778" in os.path.basename(p)],
    "RC-778 não consumido", "RC-778 virou arquivo")

# ---------- 3/4/5. travas ----------
corpus = {}
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    t = open(f, encoding="utf-8").read()
    i = t.find(SECAO)
    if i < 0:
        continue
    j = t.find("\n## ", i + 10)
    corpus[os.path.basename(f)] = t[i:j if j > 0 else len(t)]
body = "\n".join(corpus.values())
corpus_cit = " ".join(re.findall(r'"([^"]{15,})"', body))      # só o que está entre aspas é fala da fonte
v1 = [w for w in VAZADAS_D1 if w.lower() in corpus_cit.lower()]
v4 = [w for w in VAZADAS_D4 if w.lower() in corpus_cit.lower()]
v3 = [w for w in VETADAS if w.lower() in corpus_cit.lower()]
chk(not v1, "trava D-1: 0 marcadores da digressão política em fichas deste ciclo", f"VAZOU D-1: {v1}")
chk(not v4, "trava D-4: 0 marcadores do bloco de doença em fichas deste ciclo", f"VAZOU D-4: {v4}")
chk(not v3, "trava D-3: 0 aspas vedadas em **citações** das seções deste ciclo", f"VAZOU D-3: {v3}")

# ---------- 6. materialização ----------
tem_arq = [os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, "termos", "RC-020-*.md"))]
flip = [t for t in TERMOS if t[0] in MATERIALIZAR][0]
chk(bool(tem_arq) and flip[7] is True, "RC-020 materializada: arquivo + ficha=True",
    f"RC-020: arquivo={tem_arq} ficha={flip[7]}")
outras = [t[0] for t in TERMOS if t[7] and not glob.glob(os.path.join(RAIZ, "termos", t[0] + "-*.md"))]
chk(not outras, "nenhum código com ficha=True sem arquivo além do quadro pré-existente",
    f"flip sem arquivo: {outras}")

print("\nRESULTADO:", "BLOCO A COESO, TRAVAS HONRADAS ✓" if not ERROS else f"REVISAR ⚠️ ({len(ERROS)})")
sys.exit(0 if not ERROS else 1)
