#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR DE COBERTURA, MOLDURAS E TRÂNSITO — ciclo P2023-12-03.

Este ciclo **não corta nada** (D-1…D-4: «transcrição integral com nota editorial de moldura», e D-4 proíbe
explicitamente a purificação silenciosa), então o auditor não procura ausência: procura **presença**,
**vizinhança** e **contiguidade**. Provas:

 1. **Fidelidade:** todo parágrafo de transcrição da apostila é substring do `original.txt` (espaços
    normalizados) — nada foi reescrito, resumido nem «melhorado».
 2. **Cobertura:** a concatenação dos parágrafos reproduz **exatamente** a fala integral (U0003–U0038) —
    100,00%, sem span suprimido. Cobertura se prova por igualdade de texto, não por soma de tamanhos.
 3. **Ordem (D-13 do ciclo de 2022, mantida):** os endereços `Uxxxx` dos blocos são monotonicamente crescentes.
 4. **Molduras (D-1, D-2, D-3, D-4):** os quatro spans sensíveis estão **presentes** na transcrição e o bloco
    que os contém traz a nota que os nomeia. Não basta a nota existir em algum lugar da apostila.
 4-bis. **Contiguidade (D-2):** as duas frases do quiasma caem **no mesmo bloco** — apartá-las era o único jeito
    de a moldura virar censura; a prova é estrutural, não de boa intenção.
 5. **Trava de trânsito (D-1/D-2/D-3/D-4/D-12):** os termos desses spans **não** aparecem em nenhuma seção
    `## Ampliação — P2023-12-03` das fichas de `termos/`. A devolutiva proíbe; aqui a proibição é **conferida**.
 6. **Glossário:** cada `RC-###` citado no GLOSSÁRIO LOCAL existe na Base (montante do DOCX, para a falha
    aparecer antes do Word).

Roda de `analise/`. Saída 0 = ok. Ferramenta de ciclo: não toca a Base.
"""
import os, re, sys, glob, importlib.util, io, contextlib

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = os.path.dirname(AQUI)
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SIGLA = "P2023-12-03"

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ger", os.path.join(AQUI, f"_gerar_apostila_{SIGLA}.py"))
ger = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(ger)
NOTAS, QD = ger.NOTAS, ger.QD

src = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n")
apos = open(os.path.join(CICLO, "apostila.md"), encoding="utf-8").read()
S = " ".join(src.split())

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
        continue
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
print(f"2) texto reconstruído == fala integral (U0003–U0038): {igual} · {100.0 * len(rec) / len(esperado):.2f}% "
      f"de {len(esperado):,} caracteres".replace(",", "."))
if not igual:
    import difflib
    r = difflib.SequenceMatcher(None, rec, esperado)
    print(f"   similaridade: {100 * r.ratio():.3f}%")
    for tag, i1, i2, j1, j2 in r.get_opcodes()[:6]:
        if tag != "equal":
            print(f"   {tag}: apostila[{i1}:{i2}]={rec[i1:i2][:70]!r}  fonte[{j1}:{j2}]={esperado[j1:j2][:70]!r}")

ends = re.findall(r"\((U\d{4}),", corpo)
ordem_ok = ends == sorted(ends)
print(f"3) endereços monotônicos (ordem da fonte, sem reorganização): {ordem_ok} · {len(ends)} blocos, "
      f"{ends[0] if ends else '—'} → {ends[-1] if ends else '—'}")

# --- 4) molduras -------------------------------------------------------------------------------
MOLDURAS = [("d1_humanidade", "D-1", "U0004"), ("d2_quiasma", "D-2", "U0004"),
            ("d3_politica", "D-3", "U0023"), ("d4_masculina", "D-4", "U0004")]
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
    emold = f"MOLDURA ({item})" in txt
    print(f"   · {item}: «{t[:46]}…» em {u} · bloco {nb} · moldura no mesmo bloco: {'sim' if emold else 'NAO'}")
    if not emold:
        mold_ok = False
print(f"   notas editoriais definidas: {len(NOTAS)} · emitidas no corpo: {apos.count('*Nota editorial:*')}")

# --- 4-bis) contiguidade do quiasma (D-2) ------------------------------------------------------
def bloco_de(sub):
    for i, (h, b) in enumerate(blocos):
        if sub in b:
            return i, re.search(r"Bloco \d+", h).group(0)
    return None, None
i1, r1 = bloco_de("As mulheres atrapalham tudo")
i2, r2 = bloco_de("foi o DNAzinho de Maria em Jesus")
contiguo = i1 is not None and i1 == i2
print(f"4-bis) D-2: as duas frases do quiasma no MESMO bloco: {contiguo} · {r1} × {r2} "
      "(apartá-las transformaria a reversão em ofensa — ordem expressa do despacho)")
if not contiguo:
    mold_ok = False

# --- 5) trânsito -------------------------------------------------------------------------------
secoes_f = {}
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    t = open(f, encoding="utf-8").read()
    if f"## Ampliação — {SIGLA}" in t:
        # recorte **só** da seção deste ciclo: do título até o próximo `## `. Sem isso o auditor leria o
        # corpo inteiro da ficha e acusaria de vazamento o texto que já estava lá de outros ciclos
        # (foi o que aconteceu na 1ª rodada: o nome civil no título de `RC-071` e uma observação de
        # `RC-378` sobre identidade de gênero, ambos pré-existentes e fora desta ampliação).
        i = t.find(f"## Ampliação — {SIGLA}")
        j = t.find("\n## ", i + 10)
        secoes_f[os.path.basename(f)] = t[i:j if j > 0 else len(t)]
so = "\n".join(secoes_f.values())
NOMES = ["Chico Xavier", "Divaldo", "Valdemar", "Edgar Armon", "Jane Miranda", "João Altair", "Vasconcel",
         "Rogério", "Márcia", "Horácio", "Shimon", "Gandari"]
INCOND = [(f"nome: {n}", r"\b" + re.escape(n)) for n in NOMES] + [
    ("gênero: identidade de gênero", r"identidade de g\w*nero"),
    ("gênero: conta dos gêneros terrenos", r"mudar loucamente|palavras humanas para"),
    ("quiasma: atrapalham tudo", r"atrapalham tudo"),
    ("quiasma: homens são fracasso", r"fracasso nessa hist"),
    ("máscara STT p****", r"p\*{4}"), ("máscara STT e******", r"e\*{6}"), ("máscara STT b******", r"b\*{6}"),
    ("máscara STT genérica", r"[A-Za-zÀ-ÿ]\*{3,}"),
    ("política: direita/esquerda", r"direita e esquerda|toda porcaria junto"),
]
vaz_i = []
for rotulo_, rx in INCOND:
    hits = [k for k, txt in secoes_f.items() if re.search(rx, txt, re.I)]
    if hits:
        vaz_i.append((rotulo_, hits[:3]))
print(f"5) trânsito para as fichas — (i) incondicional: {len(so):,} caracteres lidos em {len(secoes_f)} seções · "
      f"vazamentos: {len(vaz_i)}".replace(",", "."))
for r_, h in vaz_i:
    print("   ✗", r_, h)

GRUPO_RX = r"(humanos|homens|mulheres|povos|ind[íi]genas|crian[çc]as|paciente|doente|transtorno|pessoa|gente|idiv[íi]duo)"
fichas_nome = {}
for f in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
    txt = open(f, encoding="utf-8").read()
    m = re.search(r"^#\s*(?:RC-\d{3}\s*[—-]\s*)?(.+)$", txt, re.M)
    fichas_nome[os.path.basename(f)] = (m.group(1).strip() if m else os.path.basename(f))
sens = [r"identidade de g\w*nero", r"atrapalham tudo", r"fracasso nessa hist",
        r"direita e esquerda", r"mudar loucamente"]
vaz_c = [(w, [k for k, txt in secoes_f.items()
              if re.search(w, txt, re.I) and re.search(GRUPO_RX, fichas_nome.get(k, ""), re.I)]) for w in sens]
vaz_c = [(w, h) for w, h in vaz_c if h]
print(f"   (ii) léxico sensível × fichas que nomeiam gente: vazamentos: {len(vaz_c)} {vaz_c[:3]}")

# --- 6) remissões do glossário ------------------------------------------------------------------
gl = apos[apos.index("## GLOSSÁRIO LOCAL"):]
rcs = sorted(set(re.findall(r"RC-\d{3}", gl)))
base = set(re.findall(r'"(RC-\d{3})"', open(os.path.join(RAIZ, "ferramentas", "dados_termos.py"),
                                            encoding="utf-8").read()))
faltando = [r for r in rcs if r not in base]
print(f"6) remissões RC-### no GLOSSÁRIO: {len(rcs)} · inexistentes na Base: {len(faltando)} {faltando[:6]}")
sem_arq = [r for r in rcs if r in base and not glob.glob(os.path.join(RAIZ, "termos", f"{r}-*.md"))]
print(f"   (referência) remissões a código existente mas **sem arquivo**: {len(sem_arq)} — "
      + ("; ".join(sem_arq[:8]) if sem_arq else "nenhuma") +
      (" · são `ficha=False` e o despacho não autorizou materializá-las, então a remissão é à malha" if sem_arq else ""))

ok = (not fora) and igual and ordem_ok and mold_ok and not vaz_i and not vaz_c and not faltando
print("\nRESULTADO:", "TRANSCRIÇÃO ÍNTEGRA · MOLDURAS NO LUGAR · QUIASMA ÍNTEGRO · TRÂNSITO VEDADO · GLOSSÁRIO "
      "ENDEREÇADO ✓" if ok else "REVISAR ⚠️")
sys.exit(0 if ok else 1)
