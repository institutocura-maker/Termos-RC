#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INGRESSO + SEGMENTAÇÃO DE LEITURA do ciclo P2023-12-03.

Faz o que a esteira exige antes de qualquer leitura: (1) confere `original.txt` byte a byte contra o
arquivo recebido em `uploads_recepcao/` (tamanho, SHA-256 e terminadores de linha), (2) mede o bruto
(bytes, chars, linhas lógicas, linhas pesadas, palavras, períodos, pontuação degradada, nomes de
interlocutores) e grava em `analise/METADADOS-INGRESSO.json`, (3) corta a leitura em chunks
**endereçados** (`analise/leitura/chunk-NN.txt`) por fronteira de frase, nunca por tamanho cego, para
que toda âncora escrita depois tenha `Uxxxx` + offset verdadeiro.

Nada aqui decide conteúdo. Rodar de `analise/`.
"""
import os, re, json, glob, hashlib

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
RECEPCAO = os.path.join(RAIZ, "uploads_recepcao")
SIGLA = "P2023-12-03"
n8 = lambda x: f"{x:,}".replace(",", ".")   # padrão da casa: ponto de milhar
TITULO = "A Rebelião de Lúcifer ainda por ser Finalizada"
DATA = "2023-12-03"
ALVO_LINHA = 14000          # fatia-alvo das linhas pesadas (frase completa, nunca corte duro)

src = sorted(glob.glob(os.path.join(RECEPCAO, "2023-12-03*")))
assert len(src) == 1, f"esperava 1 arquivo de ingresso, achei {len(src)}"
src = src[0]
bruto_bytes = open(src, "rb").read()
orig_bytes = open(os.path.join(CICLO, "original.txt"), "rb").read()
assert bruto_bytes == orig_bytes, "⚠️ original.txt DIFERE do recebido — não se lê em cima de cópia duvidosa"

h = hashlib.sha256(orig_bytes).hexdigest()
raw_txt = orig_bytes.decode("utf-8")
crlf = orig_bytes.count(b"\r\n")
lf_soltos = orig_bytes.count(b"\n") - crlf
RAW = raw_txt.replace("\r\n", "\n")
LINHAS = RAW.split("\n")
nlin_txt = len([l for l in LINHAS if l.strip()])
chars = len(RAW)
chars_texto = sum(len(l.strip()) for l in LINHAS if l.strip())
palavras = len(" ".join(l.strip() for l in LINHAS if l.strip()).split())
periodos = len(re.findall(r"[.?!]+", RAW))

# --- linhas lógicas: endereço, tamanho, natureza ---------------------------------------------
med = []
off = 0
for i, l in enumerate(LINHAS):
    ini, fim = off, off + len(l)
    off = fim + 1
    s = l.strip()
    if not s:
        continue
    med.append(dict(u=f"U{i + 1:04d}", chars=len(s), ini=ini, fim=fim,
                    palavras=len(s.split()), periodos=len(re.findall(r"[.?!]+", s)),
                    natureza=("TÍTULO DO ARQUIVO" if i == 0 else
                              "MEGABLOCO DE FALA" if len(s) > 20000 else
                              "linha de fala" if len(s) > 400 else
                              "turno curto (interlocução)")))
pesadas = [m for m in med if m["chars"] > 400]
total_fala = sum(m["chars"] for m in med[1:])            # sem a linha-título
concentr = max(med, key=lambda m: m["chars"])
print(f"linhas lógicas com texto: {len(med)} · fala útil {total_fala:,} chars".replace(",", "."))
print(f"maior linha: {concentr['u']} com {n8(concentr['chars'])} chars = {100.0 * concentr['chars'] / total_fala:.1f}% da fala".replace(",", "."))
print("linhas >400 chars:", len(pesadas), "· turnos curtos:", len(med) - len(pesadas) - 1)

# --- degradação e nomes: medidos, não lembrados ----------------------------------------------
NOMES = ["Rogério", "Horácio", "Márcia", "Jan", "Thot", "Luzbell", "Lemion", "Sofia", "Javé",
         "Lúcifer", "Apocalipse", "entropia", "entrop", "algoritmo", "protocolo", "inteligência artificial",
         "Danão", "hibridaç", "hibridag", "2049", "Jane Miranda", "profec", "testemunh", "quartel"]
med_nomes = {}
for n in NOMES:
    hits = [(f"U{i + 1:04d}", m.start()) for i, l in enumerate(LINHAS) for m in re.finditer(re.escape(n), l, re.I)]
    if hits:
        med_nomes[n] = dict(n=len(hits), primeiros=sorted({u for u, _ in hits})[:6])
print("nomes/termos medidos:", {k: v["n"] for k, v in med_nomes.items()})

mascaras = len(re.findall(r"\*{3,}", RAW))
print("máscaras do STT (***):", mascaras, "· aspas retas no bruto:", RAW.count('"'))

# --- METADADOS-INGRESSO.json -------------------------------------------------------------------
meta = dict(
    sigla=SIGLA, titulo_arquivo=os.path.basename(src), data_fala="03/12/2023", dia_semana="domingo",
    bytes=len(orig_bytes), sha256=h, chars_normalizados=chars, chars_texto=chars_texto,
    terminadores_linha=dict(crlf=crlf, lf_soltos=lf_soltos),
    linhas_lógicas=len(LINHAS), linhas_com_texto=nlin_txt,
    palavras_fala=palavras, periodos=periodos,
    linhas_pesadas=len(pesadas), maior_linha=dict(u=concentr["u"], chars=concentr["chars"],
                                                  pct_fala=round(100.0 * concentr["chars"] / total_fala, 2)),
    turnos_curtos=len(med) - len(pesadas) - 1,
    mapa_linhas=[{k: m[k] for k in ("u", "chars", "ini", "fim", "palavras", "periodos", "natureza")} for m in med],
    nomes_e_termos=med_nomes, mascaras_stt=mascaras,
    integridade=dict(recebido_em="uploads_recepcao/", copiado_por="cp", conferido_por="cmp + sha256 (idênticos)",
                     original_modificado="NÃO — intocado por todo o ciclo"),
    observacao_palestra_preparatoria=("esta é a palestra anunciada por P2023-12-02 (Thot, 02/12/2023): "
                                      "`eu jamais iria fazer esta palestra de hoje se eu não tivesse decidido "
                                      "fazer a palestra de amanhã a pedidos` — o tema prometido era a Rebelião "
                                      "de Lúcifer envolvendo Thot; o autor abriu este TXT dizendo `Hoje nós vamos "
                                      "retomar um assunto` (U0003)"),
)
json.dump(meta, open(os.path.join(AQUI, "METADADOS-INGRESSO.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("METADADOS-INGRESSO.json escrito")

# --- chunks de leitura endereçados -------------------------------------------------------------
def fatiar(texto, base):
    """Corta em blocos de ~ALVO_LINHA em fronteira de frase; devolve (ini, fim) em coords do bruto."""
    i, out = 0, []
    while i < len(texto):
        fim = min(len(texto), i + ALVO_LINHA)
        if fim < len(texto):
            corte = max(texto.rfind(". ", i + 4000, fim), texto.rfind("? ", i + 4000, fim),
                        texto.rfind("! ", i + 4000, fim), texto.rfind(".\n", i + 4000, fim))
            if corte > 0:
                fim = corte + 1
        out.append((i, fim))
        i = fim
    return [(base + a, base + b) for a, b in out]


pedacos = []
for m in med:
    if m["u"] == "U0001":
        continue
    if m["chars"] <= ALVO_LINHA:
        pedacos.append((m["u"], m["ini"], m["fim"]))
    else:
        for a, b in fatiar(RAW[m["ini"]:m["fim"]], m["ini"]):
            pedacos.append((m["u"], a, b))
# agrupa os trechos em chunks por orçamento de tamanho (cada trecho entra uma única vez)
chunks, atual, atual_len = [], [], 0
for pc in pedacos:
    n = pc[2] - pc[1]
    if atual and atual_len + n > ALVO_LINHA:
        chunks.append(atual); atual, atual_len = [], 0
    atual.append(pc); atual_len += n
if atual:
    chunks.append(atual)

LE = os.path.join(AQUI, "leitura")
os.makedirs(LE, exist_ok=True)
for f in glob.glob(os.path.join(LE, "chunk-*.txt")):
    os.remove(f)
man = []
for i, ch in enumerate(chunks, 1):
    a, b = ch[0][1], ch[-1][2]
    us = sorted({u for u, _, _ in ch})
    corpo = RAW[a:b]
    cab = (f"CHUNK {i:02d} de {len(chunks):02d} — P2023-12-03 · endereços {'–'.join([us[0], us[-1]] if len(us)>1 else [us[0]])} "
           f"({', '.join(us)})\nbruto: caracteres {a + 1:,}–{b:,} de {n8(chars)} · {b - a:,} chars · "
           f"{len(corpo.split()):,} palavras · SHA-256 do arquivo inteiro `{h[:12]}…{h[-6:]}`\n"
           f"⚠️ Nada é reordenado nem resumido aqui: é o trecho do original.txt, byte a byte, com o endereço.\n"
           .replace(",", "."))
    open(os.path.join(LE, f"chunk-{i:02d}.txt"), "w", encoding="utf-8").write(cab + "\n" + corpo + "\n")
    man.append((i, us, a + 1, b, b - a))

with open(os.path.join(AQUI, "leitura-segmentada.txt"), "w", encoding="utf-8") as f:
    f.write(f"# SEGMENTAÇÃO DE LEITURA — {SIGLA} ({TITULO})\n\n")
    f.write("O bruto tem **uma linha que é 77% da fala** (U0004). Ler isso de uma vez produz leitura fatigada e ")
    f.write("âncora de memória — os dois males que a esteira combate. Por isso a fala foi cortada em ")
    f.write(f"**{len(chunks)} chunks** por fronteira de frase, cada um com `Uxxxx` e o intervalo de caracteres do ")
    f.write("bruto. A numeração abaixo é o índice do que existe em `analise/leitura/`.\n\n")
    f.write("| chunk | endereços | caracteres no bruto | tamanho |\n|---|---|---|---|\n")
    for i, us, a, b, n in man:
        f.write(f"| {i:02d} | {'–'.join([us[0], us[-1]]) if len(us) > 1 else us[0]} ({len(us)} linha(s)) | "
                f"{a:,}–{b:,} | {n:,} |\n".replace(",", "."))
    f.write("\n*Toda aspa dos arquivos de análise e do dossiê sairá do caça-âncoras "
            "`_aspas_P2023-12-03.py`, nunca desta segmentação.*\n")
# --- prova de cobertura: não é contagem de chars, é IGUALDADE DE TEXTO -------------------------
# Somar tamanhos enganaria (as linhas do bruto têm espaços à direita); o que vale é que o texto
# concatenado dos trechos, com espaços colapsados, seja exatamente o texto da fala.
planos = sorted(pc for ch in chunks for pc in ch)
assert len(planos) == len(pedacos), f"junção perdeu/duplicou trechos: {len(planos)} vs {len(pedacos)}"
assert sorted(pedos:=sorted(pedacos)) == sorted(p for p in planos), "conjunto de trechos divergiu da lista original"
assert all(a < b for _, a, b in planos), "trecho vazio na segmentação"
# (a prova de cima garante que todo trecho está presente exatamente uma vez; a de baixo, que a
# concatenação deles é a fala. Cobrir linha por linha seria ingênuo: a linha longa tem 6 trechos.)
texto_esperado = " ".join(" ".join(RAW[m["ini"]:m["fim"]].split()) for m in med[1:])
texto_chunks = " ".join(" ".join(RAW[a:b].split()) for _, a, b in planos)
assert texto_esperado == texto_chunks, "⚠️ os chunks NÃO reproduzem a fala: sobra ou falta texto"
print(f"✓ segmentação confere: {len(chunks)} chunks · {len(planos)} trechos · {len(texto_chunks):,} chars "
      f"de texto igual à fala útil".replace(",", "."))

with open(os.path.join(AQUI, "leitura-segmentada.txt"), "a", encoding="utf-8") as f:
    f.write("\n*A prova acima é de igualdade de texto (espaços colapsados) entre a fala útil e a união dos "
            "trechos — não de soma de tamanhos: assim um trecho duplicado ou perdido não passa.*\n")

# --- ficha de ingresso ------------------------------------------------------------------------
fi = f"""# Ficha de ingresso — {DATA} · {TITULO}

**Sigla:** `{SIGLA}` · **Recebido em:** `uploads_recepcao/{os.path.basename(src)}` · **Cópia:** `cp` + `cmp`
(idênticos) + SHA-256 conferido nos dois lados: `{h[:12]}…{h[-6:]}` · **`original.txt` intocado o ciclo inteiro.**

## O que o arquivo é (medido, não declarado)

| grandeza | valor |
|---|---|
| bytes | {n8(len(orig_bytes))} |
| caracteres (normalizados LF) | {n8(chars)} |
| linhas lógicas | {len(LINHAS)} · com texto: {n8(nlin_txt)} |
| palavras de fala | {n8(palavras)} |
| períodos (`[.?!]+`) | {n8(periodos)} |
| terminadores | CRLF: {crlf} · LF soltos: {lf_soltos} |
| linhas pesadas (>400 chars) | {n8(len(pesadas))} |
| concentração | {concentr['u']} = {n8(concentr['chars'])} chars (**{100.0 * concentr['chars'] / total_fala:.1f}% da fala**) |
| turnos curtos (interlocução) | {len(med) - len(pesadas) - 1} |
| máscaras do STT (`***`) | {mascaras} |
| aspas retas no bruto | {RAW.count(chr(34))} |

## Estrutura da fala (endereços do bruto)

| linha | chars | o que é |
|---|---|---|
""" + "\n".join(f"| {m['u']} | {n8(m['chars'])} | {m['natureza']} |".replace(",", ".") for m in med) + f"""

## Contexto que o senhor já conhece

Esta palestra é a que **{ 'P2023-12-02' } (Thot, 02/12/2023) anunciou como `a palestra de amanhã, a pedidos`** —
o tema prometido era a Rebelião de Lúcifer envolvendo Thot (ver `apostilas/CONCLUIDAS/2023-12-02_thot_enigmatico_hermes_trimegisto/analise/camada-1.txt` l.2
e o `METADADOS-INGRESSO.json` daquele ciclo, campo `observacao_palestra_preparatoria`). Fecha-se assim o **terceiro
ponto do eixo** que a Arca vem trabalhando: **P2020-04-25** (56 fichas) → **P2022-03-26** (75 fichas) → **esta**,
com **0 ocorrências da sigla na malha** antes do ciclo: fonte inédita, não reprocessada.

## Dias e nomes que aparecem (medidos; sem juízo de mérito)

""" + "\n".join(f"- `{k}` — {v['n']}× em {', '.join(v['primeiros'][:5])}" for k, v in med_nomes.items()) + f"""

## Agenda do ciclo (rito Base-first)

1. **Etapa 1 (esta ficha + camadas 0–3 + dossiê):** leitura integral em {len(chunks)} chunks endereçados, sem
   tocar a Base, e devolutiva **D-1…D-n** ao Curador;
2. **nada é aplicado antes da resposta dele** — 0 códigos, 0 relações, 0 obras; teto 777 e `RC-778` intocáveis;
3. BLOCO A (malha + fichas) e BLOCO B (apostila + DOCX + engavetamento) em **commits separados**, cada um com os
   portões A · B · C · D · E verdes e o regime de moldura de P2022-03-26 (trânsito, não corte).
"""
open(os.path.join(CICLO, "ficha_ingresso.md"), "w", encoding="utf-8").write(fi)
print("ficha_ingresso.md escrito:", len(fi), "chars")
