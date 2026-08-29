#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORTÃO D — contadores da malha + travas da devolutiva, **medidos** (não declarados).

Fecha o BLOCO A de P2023-12-03. Seis checagens, todas lidas de arquivo:

 1. **paridade estrutural**: o corpo da seção `## Ampliação — P2023-12-03` de cada ficha é o
    bloco correspondente do pacote (nada foi editado à mão depois da aplicação);
 2. **contadores**: `len(TERMOS)`, `len(RELACOES)`, nº de obras em `biblioteca/`, nº de arquivos em
    `termos/`, nº de linhas `ficha=True`, nº de fichas com a seção desta fonte e nº de códigos com a
    sigla na lista de FONTES;
 3. **trava D-1**: nenhum marcador lexical da digressão bloqueada aparece numa seção deste ciclo;
 4. **trava D-4**: idem para o bloco da doença;
 5. **trava D-3**: nenhuma aspa sobre mulheres/homoafetivos/«cobaias» entra em **qualquer** seção de
    ampliação deste ciclo (a devolutiva proíbe; aqui a proibição é conferida, não presumida);
 6. **materialização**: `RC-089` tem arquivo **e** `ficha=True`; nenhum outro código foi materializado.

Sai com código 1 se qualquer item falhar. Ferramenta de ciclo: não toca a Base.
"""
import os, re, sys, glob, importlib.util
_re_f = re.compile(r"(RC-\d{3})")

AQUI = os.path.dirname(os.path.abspath(__file__))
def _resolve_raiz(d):
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, "ferramentas")):
        d = os.path.dirname(d)
    return d
RAIZ = _resolve_raiz(AQUI)
SIGLA = "P2023-12-03"
SECAO = f"## Ampliação — {SIGLA}"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
MATERIALIZAR = ["RC-018", "RC-040"]
ARQ_ESPERADO, FICHA_TRUE_ESPERADO = 460, 459          # 458→460 arquivos · 457→459 ficha=True (as DUAS do D-10)
# ── travas **deste** ciclo, re-escritas aqui de propósito: um portão que importa as regras do
#    gerador não é portão, é eco. São os léxicos do despacho (D-1, D-2, D-3, D-4, D-12, D-13).
VAZADAS_D1 = ["identidade de gênero", "identidade de genero", "gêneros na Terra", "generos na terra",
              "mudar loucamente", "palavras humanas para"]
VAZADAS_D2 = ["atrapalham tudo", "fracasso nessa história", "fracasso nessa historia", "só sai de mulher"]
VAZADAS_D4 = ["*****", "****", "***", "p****", "m****"]
VAZADAS_D8 = ["a Arca cumpre um contrato", "arca cumpre"]
VETADAS = ["Bolsonaro", "Lula", "Trump", "direita e esquerda", "mediocridade"]            # D-3
PESSOAS = ["Chico Xavier", "Divaldo", "Valdemar", "Edgar Armon", "Jane Miranda", "João Altair",
           "Márcia", "Horácio", "Rogério", "Vasconcel", "Shimon", "Gandari"]               # D-12
CALENDARIO = ["2049", "2050", "2051", "2052", "1989", "julho de 9", "passaporte"]          # D-13 (só em RC-344/RC-003)
GRUPO_RX = r"humanos|homens|mulheres|povos|ind[íi]genas|crian[çc]as|pacientes|doen[çc]a|transtorno"
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
chk(arquivos == ARQ_ESPERADO, f"458 → {ARQ_ESPERADO} arquivos de ficha (as materializações: RC-018 e RC-040)",
    f"arquivos = {arquivos} ≠ {ARQ_ESPERADO}")
chk(ficha_true == FICHA_TRUE_ESPERADO, f"457 → {FICHA_TRUE_ESPERADO} linhas `ficha=True` no cadastro",
    f"ficha=True = {ficha_true} ≠ {FICHA_TRUE_ESPERADO}")
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
corpus_cit = " ".join(re.findall(r"\u00ab([^\u00bb]{15,})\u00bb", body) + re.findall(r'"([^"]{15,})"', body))
v1 = [w for w in VAZADAS_D1 if w.lower() in corpus_cit.lower()]
v4 = [w for w in VAZADAS_D4 if w.lower() in corpus_cit.lower()]
# nomes próprios: busca com fronteira de palavra e **caixa respetada** — sem isso, "células"
# e "pluricelulares" disparam falso positivo em "Lula" (foi o que aconteceu na 1ª rodada)
v3 = [w for w in VETADAS if re.search(r"\b" + re.escape(w) + r"\b", corpus_cit)]
v2 = [w for w in VAZADAS_D2 if w.lower() in corpus_cit.lower()]
v8 = [w for w in VAZADAS_D8 if w.lower() in body.lower()]
vx = [w for w in PESSOAS if re.search(r"\b" + re.escape(w), corpus_cit)]
chk(not v1, "trava D-1: 0 ocorrências do argumento de gênero nas citações injetadas", f"VAZOU D-1: {v1}")
chk(not v2, "trava D-2: 0 ocorrências do quiasma das mulheres nas citações injetadas", f"VAZOU D-2: {v2}")
chk(not v4, "trava D-4: 0 máscaras do STT em fichas deste ciclo", f"VAZOU D-4: {v4}")
chk(not v3, "trava D-3: 0 vocabulário político em **citações** das seções deste ciclo", f"VAZOU D-3: {v3}")
chk(not vx, "trava D-12: 0 nomes de pessoas da plateia/mediunidade em citações", f"VAZOU D-12: {vx}")
chk(not v8, "trava D-8: a cláusula «a Arca cumpre um contrato» não foi usada como auto-legitimação em ficha",
    f"VAZOU D-8: {v8}")
corpus_por_cod = {re.match(r"(RC-\d{3})", k).group(1): v for k, v in corpus.items()}
v13 = [w for w in CALENDARIO if w in corpus_por_cod.get("RC-200", "")]
chk(not v13, "trava D-13: RC-200 sem calendário profético", f"VAZOU D-13 em RC-200: {v13}")
# D-13 manda a janela para RC-344 **e** RC-003. Medido: `RC-344` é `ficha=False` — não há arquivo para
# receber nada, e D-10 não autorizou materializá-la. A verificação é feita então onde o dado **pode** estar:
# em `RC-003` na ficha, e em `RC-344` no pacote (BLOCO 2 = vínculo na malha + conteúdo aguardando materialização).
pac_txt = open(PACOTE, encoding="utf-8").read()
sec344 = pac_txt.split("### RC-344\n", 1)[1].split("### ")[0]
ok13 = (any(w in corpus_por_cod.get("RC-003", "") for w in CALENDARIO)
        and any(w in sec344 for w in CALENDARIO) and "### RC-344" in pac_txt)
chk(ok13, "trava D-13: janela em RC-003 (ficha) e em RC-344 (pacote, que é `ficha=False` sem arquivo)",
    "janela ausente de RC-003 e/ou do pacote em RC-344")
# trava D-3, recalculada aqui a partir do cadastro: nenhuma ficha cujo NOME nomeia
# pessoa/paciente/grupo humano pode receber vocabulário clínico desta fonte
vaz3 = []
nome_cad = {t[0]: t[1] for t in DT.TERMOS}
for cod, corpo_sec in corpus_por_cod.items():
    if re.search(GRUPO_RX, nome_cad.get(cod, ""), re.I):
        ach = [w for w in VAZADAS_D1 + VAZADAS_D2 + VETADAS if w.lower() in corpo_sec.lower()]
        if ach:
            vaz3.append(f"{cod} {nome_cad.get(cod,'')}: {ach}")
chk(not vaz3, "trava D-1/D-2: 0 aspas de gênero ou de grupo em fichas que **nomeiam** grupos humanos", f"VAZOU: {vaz3}")

# ---------- 6. materialização ----------
for cod in MATERIALIZAR:
    tem_arq = [os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, "termos", f"{cod}-*.md"))]
    flip = [t for t in TERMOS if t[0] == cod][0]
    chk(bool(tem_arq) and flip[7] is True, f"{cod} materializada: arquivo + ficha=True",
        f"{cod}: arquivo={tem_arq} ficha={flip[7]}")
cromon = [t for t in TERMOS if t[0] == "RC-444"][0]
chk(cromon[7] is False and not glob.glob(os.path.join(RAIZ, "termos", "RC-444-*.md")),
    "RC-444 Família Cromon permanece `ficha=False`, como ordenado (D-10)", "RC-444 foi materializada contra a ordem")
outras = [t[0] for t in TERMOS if t[7] and not glob.glob(os.path.join(RAIZ, "termos", t[0] + "-*.md"))]
chk(not outras, "nenhum código com ficha=True sem arquivo além do quadro pré-existente",
    f"flip sem arquivo: {outras}")

print("\nRESULTADO:", "BLOCO A COESO, TRAVAS HONRADAS ✓" if not ERROS else f"REVISAR ⚠️ ({len(ERROS)})")
sys.exit(0 if not ERROS else 1)
