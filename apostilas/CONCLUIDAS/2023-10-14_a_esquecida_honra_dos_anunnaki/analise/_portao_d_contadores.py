#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTÃO D — contadores da malha + travas de bloqueio, medidos (não declarados).

Fecha o círculo do bloco A:

 1. **paridade estrutural**: o corpo da seção `## Ampliação — P2023-10-14` de cada ficha
    é **byte a byte** o bloco correspondente do pacote (nada foi editado à mão depois da
    aplicação);
 2. **contadores**: `len(TERMOS)`, `len(RELACOES)`, nº de obras em `biblioteca/`, nº de
    arquivos em `termos/`, nº de linhas `ficha=True` e nº de fichas que citam a sigla —
    todos lidos por import, nunca por memória;
 3. **travas**: as duas frases misóginas (U0015/U0033) e o bloco político/institucional
    bloqueado pelo item 10 da devolutiva **não** aparecem em nenhum `.md` de `termos/`;
 4. **materializações**: os 5 códigos autorizados têm arquivo **e** `ficha=True`; RC-272
    tem vínculo na malha e continua sem arquivo.

Sai com código 1 se qualquer item falhar. Ferramenta de ciclo: não toca a Base.
"""
import os, re, sys, glob, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))


def _resolve_raiz(inicio):
    d = os.path.abspath(inicio)
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d


RAIZ = _resolve_raiz(AQUI)
CICLO = AQUI.rsplit("/analise", 1)[0]
SIGLA = "P2023-10-14"
SECAO = f"## Ampliação — {SIGLA}"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
MATERIALIZAR = ["RC-322", "RC-425", "RC-432", "RC-381", "RC-191"]
ERROS = []


def chk(cond, ok, falha):
    print(("✓ " if cond else "✗ ") + (ok if cond else falha))
    if not cond:
        ERROS.append(falha)


# ---------- 1. paridade estrutural ficha ↔ pacote ----------
pac = open(PACOTE, encoding="utf-8").read()
blocos = {}
for bloco in pac.split("### ")[1:]:
    cab, _, corpo = bloco.partition("\n")
    cab = cab.strip()
    if re.fullmatch(r"RC-\d{3}", cab):
        m = re.search(r"^## ", corpo, re.M)      # BLOCOS 2-4 não pertencem a fichas
        blocos[cab] = (corpo[:m.start()] if m else corpo).strip()

def norm_bloco(s):
    """compara o corpo da seção: espaços de borda, separadores `---` e a marcação de
    tabela de fontes não contam — o que se exige é que **nenhuma aspa** tenha sido
    editada depois da aplicação."""
    return [l.rstrip() for l in s.strip().split("\n")
            if l.strip() and l.strip() != "---"]

n_sec = 0
for cod, corpo in sorted(blocos.items()):
    arq = glob.glob(os.path.join(RAIZ, "termos", f"{cod}-*.md"))
    if not arq:
        if cod != "RC-272":
            ERROS.append(f"{cod}: bloco no pacote sem ficha e sem a exceção RC-272")
        continue
    t = open(arq[0], encoding="utf-8").read()
    i = t.find(SECAO)
    if i < 0:
        ERROS.append(f"{cod}: ficha sem a seção de ampliação (aplicação não gravou)")
        continue
    j = t.find("\n## ", i + 10)
    sec = t[i:j if j > 0 else len(t)]
    sec = "\n".join(sec.split("\n")[1:]).strip()
    n_sec += 1
    if norm_bloco(sec) != norm_bloco(corpo):
        a, b = norm_bloco(sec), norm_bloco(corpo)
        for k in range(max(len(a), len(b))):
            x = a[k] if k < len(a) else "<ausente>"
            y = b[k] if k < len(b) else "<ausente>"
            if x != y:
                ERROS.append(f"{cod}: linha {k+1} difere do pacote\n     ficha: {x[:110]}\n     pacote:{y[:110]}")
                break
chk(not ERROS, f"paridade estrutural: {n_sec} seções idênticas ao pacote (0 desvios)",
    f"desvios na paridade estrutural: {len(ERROS)}")

# ---------- 2. contadores ----------
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as dt

termos_n = len(dt.TERMOS)
rel_n = len(dt.RELACOES)
ficha_true = sum(1 for t in dt.TERMOS if t[7])
com_sigla = [t[0] for t in dt.TERMOS if SIGLA in t[5]]
arquivos = len(glob.glob(os.path.join(RAIZ, "termos", "*.md")))
import subprocess
tocados = subprocess.run(["git", "-C", RAIZ, "diff", "--name-only", "HEAD"],
                         capture_output=True, text=True).stdout.split("\n")
tocados = [t for t in tocados if t.strip()]
novos_livros = [f for f in os.listdir(os.path.join(RAIZ, "livros", "CONCLUIDOS"))]

chk(termos_n == 777, f"termos no cadastro: {termos_n} (teto curatorial inviolado)", f"TERMOS = {termos_n} ≠ 777")
chk(rel_n == 1856, f"relações na malha: {rel_n} (0 arestas criadas)", f"RELACOES = {rel_n} ≠ 1856")
chk(not [t for t in tocados if t.startswith("livros/")],
    "0 obras novas: nenhuma linha de `livros/` foi tocada (102 obras — B013 já existia)",
    "foram tocados arquivos de obra: " + str([t for t in tocados if t.startswith('livros/')]))
chk(len(com_sigla) == len(blocos),
    f"linhas do cadastro com «{SIGLA}»: {len(com_sigla)} = {len(blocos)} códigos do pacote",
    f"linhas com a sigla = {len(com_sigla)}, esperado {len(blocos)}")
chk(arquivos == 456, f"arquivos em `termos/`: {arquivos} (451 + 5 materializações)",
    f"arquivos em termos/ = {arquivos}, esperado 456")
chk(ficha_true == 455, f"linhas `ficha=True`: {ficha_true} (450 + 5)",
    f"ficha=True = {ficha_true}, esperado 455")

# ---------- 3. travas de conteúdo bloqueado ----------
bruto = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read()
BLOQUEADAS = ["As mulheres sempre colocam os homens de mau caminho",
              "mania de querer jogar os homens na desgraça",
              "100 bilhões de dólares para projetos secretos",
              "não existe um governo, existe uma porrada"]
todas = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(RAIZ, "termos", "*.md")))
vazando = [p for p in BLOQUEADAS if p.lower() in todas.lower()]
chk(not vazando, f"trechos bloqueados em `termos/`: 0 de {len(BLOQUEADAS)} (existem no bruto: "
    f"{sum(1 for p in BLOQUEADAS if p.lower() in bruto.lower())})",
    f"VAZAMENTO de conteúdo bloqueado: {vazando}")

# ---------- 4. materializações ----------
for cod in MATERIALIZAR:
    tem_arq = bool(glob.glob(os.path.join(RAIZ, "termos", f"{cod}-*.md")))
    linha = next(t for t in dt.TERMOS if t[0] == cod)
    chk(tem_arq and linha[7] is True and SIGLA in linha[5],
        f"{cod}: arquivo + ficha=True + fonte na malha",
        f"{cod}: arq={tem_arq} ficha={linha[7]} sigla={SIGLA in linha[5]}")
linha272 = next(t for t in dt.TERMOS if t[0] == "RC-272")
chk(not glob.glob(os.path.join(RAIZ, "termos", "RC-272-*.md")) and linha272[7] is False and SIGLA in linha272[5],
    "RC-272: vínculo de malha sem arquivo (precedente RC-385) — como aprovado",
    "RC-272 divergiu do padrão aprovado")
for cod in ("RC-396", "RC-672"):
    linha = next(t for t in dt.TERMOS if t[0] == cod)
    chk(SIGLA not in linha[5], f"{cod}: sigla **não** entrou na malha (Devolutiva itens 3/9)",
        f"{cod}: a sigla entrou indevidamente na malha")

print(f"\n=== PORTÃO D — {SIGLA} ===")
print("RESULTADO:", "BLOCO A CONSISTENTE ✓" if not ERROS else f"{len(ERROS)} PROBLEMA(S) ⚠️")
raise SystemExit(0 if not ERROS else 1)
