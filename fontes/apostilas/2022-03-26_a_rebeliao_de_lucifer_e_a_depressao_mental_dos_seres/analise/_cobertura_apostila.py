#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR DE COBERTURA, MOLDURAS E TRÂNSITO — ciclo P2022-03-26.

Este ciclo **não corta nada** (D-1: «transcreva integralmente na apostila com forte nota editorial de
moldura»), então o auditor não procura ausência: ele procura **presença** e **vizinhança**. Provas:

 1. **Fidelidade:** todo parágrafo de transcrição da apostila é substring do `original.txt`
    (espaços normalizados) — nada foi reescrito, resumido nem «melhorado».
 2. **Cobertura:** a concatenação dos parágrafos reproduz **exatamente** o texto falado integral
    (U0003–U0050) — 100,00%, sem span suprimido.
 3. **Ordem (D-13):** os endereços `Uxxxx` dos blocos são monotonicamente crescentes — a apostila não
    reorganizou nada tematicamente.
 4. **Molduras (D-1, D-2, D-3):** os três spans sensíveis estão **presentes** na transcrição e o bloco
    que os contém vem precedido de nota editorial que os nomeia.
 5. **Trava de trânsito (D-1/D-2/D-3/D-4):** os termos desses mesmos spans **não** aparecem em nenhuma
    seção `## Ampliação — P2022-03-26` das fichas de `termos/`, e as máscaras do STT não transitam.
 6. **Glossário:** cada `RC-###` citado na apostila existe na Base (o `build_apostila.py` também confere;
    aqui a conferência é a montante, para que a falha apareça antes do DOCX).

Roda de `analise/`. Saída 0 = ok.
"""
import os, re, sys, glob, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = os.path.dirname(AQUI)
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)   # sobe até a raiz: o ciclo funciona em `apostilas/<ciclo>/` e em
RAIZ = _d                     # `apostilas/CONCLUIDAS/<ciclo>/` sem nada mudar (engavetamento por git mv)
SIGLA = "P2022-03-26"

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ger", os.path.join(AQUI, f"_gerar_apostila_{SIGLA}.py"))
ger = importlib.util.module_from_spec(spec)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(ger)
NOTAS, QD = ger.NOTAS, ger.QD

src = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n")
apos = open(os.path.join(CICLO, "apostila.md"), encoding="utf-8").read()
S = " ".join(src.split())

# --- fatia da transcrição ---------------------------------------------------------------------
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
    elif s.startswith("*Nota editorial:*") or s.startswith("> "):
        continue        # `> ` = apparatus de leitura, não transcrição (D-13: nada de fala é substituído por comentário)
    else:
        paragrafos.append(s)

fora = [p for p in paragrafos if " ".join(p.split()) not in S]
print(f"parágrafos de transcrição: {len(paragrafos)} · cabeçalhos de bloco: {len(cabecalhos)}")
print(f"1) parágrafos NÃO encontrados na fonte: {len(fora)}")
for p in fora[:5]:
    print("   ✗", p[:150])

linhas = src.split("\n")
esperado = " ".join(" ".join(l.strip() for l in linhas[2:] if l.strip()).split())
rec = " ".join(" ".join(p.split()) for p in paragrafos)
igual = rec == esperado
print(f"2) texto reconstruído == fala integral (U0003–U0050): {igual} · {100.0 * len(rec) / len(esperado):.2f}% "
      f"de {len(esperado):,} caracteres".replace(",", "."))
if not igual:
    import difflib
    r = difflib.SequenceMatcher(None, rec, esperado)
    print(f"   similaridade: {100 * r.ratio():.3f}%")
    for tag, i1, i2, j1, j2 in r.get_opcodes()[:6]:
        if tag != "equal":
            print(f"   {tag}: apostila[{i1}:{i2}]={rec[i1:i2][:70]!r}  fonte[{j1}:{j2}]={esperado[j1:j2][:70]!r}")

# --- 3) ordem ---------------------------------------------------------------------------------
ends = re.findall(r"\((U\d{4}),", corpo)
ordem_ok = ends == sorted(ends)
print(f"3) endereços monotônicos (D-13, ordem cronológica): {ordem_ok} · {len(ends)} blocos, "
      f"{ends[0] if ends else '—'} → {ends[-1] if ends else '—'}")

# --- 4) molduras: presença + vizinhança --------------------------------------------------------
# A prova é estrutural: o span sensível tem de cair num bloco da transcrição, e o **mesmo bloco**
# tem de trazer a nota que o nomeia. Não basta a nota existir em algum lugar da apostila.
MOLDURAS = [("revolver_alto_engano", "D-1", "U0009"), ("narrativas_pos_facto", "D-2", "U0005"),
            ("autistas_dementes", "D-3", "U0005")]
secoes, atual = [], None
for l in corpo.split("\n"):
    t = l.strip()
    if t.startswith("## Bloco"):
        atual = [t, []]; secoes.append(atual)
    elif atual is not None and t:
        atual[1].append(t)
blocos = [(h, " ".join(" ".join(b).split())) for h, b in secoes]
print("4) molduras (presentes na transcrição e emolduradas dentro do MESMO bloco):")
mold_ok = True
for chave, item, end_esperado in MOLDURAS:
    a = QD[chave][0]
    t = re.sub(r"\s+", " ", QD[chave][2])
    u = ger.ASP.uaddr(a)
    if u != end_esperado:
        print(f"   ✗ {chave}: endereço medido {u} ≠ declarado {end_esperado}")
        mold_ok = False
    alvos = [(h, b) for h, b in blocos if t in b]
    if not alvos:
        print(f"   ✗ {chave}: span sensível AUSENTE da transcrição (o veto de corte foi violado ao contrário)")
        mold_ok = False
        continue
    rot, txt = alvos[0]
    nb = re.search(r"Bloco \d+", rot).group(0)
    emold = f"MOLDURA ({item})" in txt or f"({item})" in txt
    print(f"   · {item}: «{t[:46]}…» em {u} · bloco {nb} · moldura no mesmo bloco: "
          f"{'sim' if emold else 'NAO'}")
    if not emold:
        mold_ok = False
print(f"   notas editoriais definidas: {len(NOTAS)} · emitidas no corpo: {apos.count('*Nota editorial:*')}")

# --- 5) trânsito --------------------------------------------------------------------------------
# A devolutiva (verbatim em `DECISAO-DO-CURADOR.md` §1) dá dois regimes diferentes, e o auditor
# confere os dois separadamente:
#   (i) **proibição incondicional** — o span do suicídio, os nomes públicos e as máscaras do STT não
#       entram em **nenhuma** ficha;
#  (ii) **proibição com escopo** — a taxonomia clínica não entra em ficha **cujo termo nomeie pessoa,
#       paciente ou grupo humano** (as «aspas» de «autistas do paraíso» sobre RC-020/RC-049/RC-605 são
#       sobre classes de seres, e por isso ficaram — mesmo critério do gerador do pacote e do portão D).
corpus = "\n".join(open(f, encoding="utf-8").read() for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))))
secoes = {}
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    t = open(f, encoding="utf-8").read()
    if f"## Ampliação — {SIGLA}" in t:
        secoes[os.path.basename(f)] = t.split(f"## Ampliação — {SIGLA}")[1]
so = "\n".join(secoes.values())
NOMES = ["Lula", "Bolsonaro", "Dilma", "Temer", "Fernando Henrique", "Hillary", "Trump", "Collor", "Itamar"]
INCOND = [(w, r"\b" + w + r"\b") for w in NOMES] + [
    ("revólver", r"rev[oó]lver"), ("se desativaram", r"se\s+desativaram"), ("vida vergonhosa", r"vida\s+vergonhosa"),
    ("fundo do poço", r"fundo\s+do\s+po[çc]o"), ("máscara STT t*****", r"t\*{5}"), ("máscara STT m****", r"m\*{4}")]
GRUPO_RX = r"(pessoa|pessoas|gente|humano|humanos|homem|mulher|crian|indiv[íi]duo|paciente|doente|grupo|" \
           r"autist|esquiz|deprim|transgener|mulher|homem)"
vaz_i = []
for rotulo_, rx in INCOND:
    hits = [k for k, txt in secoes.items() if re.search(rx, txt, re.I)]
    if hits:
        vaz_i.append((rotulo_, hits[:3]))
print(f"5) trânsito para as fichas — (i) incondicional: {len(so):,} caracteres lidos · vazamentos: {len(vaz_i)}"
      .replace(",", "."))
for r_, h in vaz_i:
    print("   ✗", r_, h)
clin = ["demente", "autista", "esquizofr[êe]nic", "idiotia", "babaca"]
fichas_nome = {}
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    txt = open(f, encoding="utf-8").read()
    m = re.search(r"^#\s*(?:RC-\d{3}\s*[—-]\s*)?(.+)$", txt, re.M)
    fichas_nome[os.path.basename(f)] = (m.group(1).strip() if m else os.path.basename(f))
vaz_c = [(w, [k for k, txt in secoes.items() if re.search(w, txt, re.I) and re.search(GRUPO_RX, fichas_nome.get(k, ""), re.I)])
         for w in clin]
vaz_c = [(w, h) for w, h in vaz_c if h]
print(f"   (ii) taxonomia clínica × fichas que nomeiam gente: vazamentos: {len(vaz_c)} {vaz_c[:3]}")
ref = []
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    for l in open(f, encoding="utf-8").read().split("\n"):
        for w in NOMES:
            if re.search(r"\b" + w + r"\b", l):
                ref.append(f"{os.path.basename(f)}:{w}")
print("   (referência) nomes públicos em qualquer linha de toda a Base: " + str(len(ref)) +
      (" — " + "; ".join(ref[:3]) + " (histórico de outro ciclo, linha de *quarentena declarada*, não conteúdo)"
       if ref else ""))

# --- 6) remissões do glossário ----------------------------------------------------------------
gl = apos[apos.index("## GLOSSÁRIO LOCAL"):]
rcs = sorted(set(re.findall(r"RC-\d{3}", gl)))
base = set()
p = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
tt = open(p, encoding="utf-8").read()
base = set(re.findall(r'"(RC-\d{3})"', tt))
faltando = [r for r in rcs if r not in base]
print(f"6) remissões RC-### no GLOSSÁRIO: {len(rcs)} · inexistentes na Base: {len(faltando)} {faltando[:6]}")

ok = (not fora) and igual and ordem_ok and mold_ok and not vaz_i and not vaz_c and not faltando
print("\nRESULTADO:", "TRANSCRIÇÃO ÍNTEGRA · MOLDURAS NO LUGAR · TRÂNSITO VEDADO · GLOSSÁRIO ENDEREÇADO ✓"
      if ok else "REVISAR ⚠️")
sys.exit(0 if ok else 1)
