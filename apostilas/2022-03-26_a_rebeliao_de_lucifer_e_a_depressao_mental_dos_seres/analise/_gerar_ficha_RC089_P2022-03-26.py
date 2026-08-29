#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria `termos/RC-089-processador-val.md` — a **única materialização** aprovada nesta devolutiva (D-9).

Regras observadas (espelho do que foi feito com `RC-020` em P2020-04-25):

 * a seção `## Ampliação — P2022-03-26` é **copiada byte a byte do pacote** `_ampliacoes_P2022-03-26.txt`
   (mesma fonte do aplicador → a paridade estrutural exigida pelo portão D é automática);
 * nenhuma aspa desta ficha foi digitada de memória: toda aspa vem do pacote, e o pacote só contém span
   verificado pelo caça-âncoras;
 * `RELACOES` **não** é tocada: esta ficha reproduz o estado do cadastro e **não** abre aresta — o cadastro
   lista `RC-109; RC-018; RC-080; RC-141` em `relacionados` de RC-089 sem aresta correspondente, e a ficha
   declara isso em vez de fingir que resolveu;
 * o cadastro (`ferramentas/dados_termos.py`) é virado por `_vincular_fonte_P2022-03-26.py`, não aqui.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SIGLA = "P2022-03-26"
TITULO = "A Rebelião de Lúcifer e a Depressão Mental dos Seres"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
ALVO = os.path.join(RAIZ, "termos", "RC-089-processador-val.md")

pac = open(PACOTE, encoding="utf-8").read()
bloco = pac.split("### RC-089\n", 1)[1]
m = re.search(r"^(?:## |### )", bloco, re.M)          # corta no próximo bloco de ficha **ou** nos BLOCOS 2-4
if m:
    bloco = bloco[:m.start()]
bloco = bloco.strip()
assert bloco.startswith("- **["), "bloco RC-089 vazio ou mal formado"

sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                                             # noqa: E402
lin = [t for t in DT.TERMOS if t[0] == "RC-089"][0]
arestas = [r for r in DT.RELACOES if r[0] == "RC-089" or r[2] == "RC-089"]
rel_cadastro = [x.strip() for x in (lin[6] or "").split(";") if x.strip()]
fontes_cad = ", ".join(f"`{x}`" for x in (lin[5] or []))

corpo = f"""# Processador Val — RC-089

| Campo | Valor |
|---|---|
| **Categoria Principal** | {lin[2].title()} |
| **Subcategoria** | {lin[3]} |
| **Status** | 🟡 {lin[4].capitalize()} |
| **Última atualização** | 2026-08-28 |

## Definição Sintética

Nas obras primárias, o **Processador Val** é o dispositivo que sustenta a **família Val** como coletivo — o análogo direto dos "Processadores Familiares" capelinos de `RC-446`, pelo qual cada estirpe armazena, transmite e coesa a mente do grupo. Esta ficha existia **só no cadastro** (`dados_termos.py`) desde a migração: não havia arquivo, e por isso não havia definição. Passa a tê-la, e a definição é a que a fonte oral de **26/03/2022** entrega: na palestra, o Processador é o **órgão remanescente** de um sistema colmeico em quarentena — o único que sobrou das famílias rebeldes, **fabricado por mistura genética** para absorvê-las, hospedado numa nave que virou cidade.

## Contexto / Origem

**Materialização (não é criação).** O código RC-089 vivia só no cadastro — linha `("{lin[0]}", "{lin[1]}", {lin[2]}, {lin[3]}…, {fontes_cad}, '{lin[6]}', False)` — sem arquivo em `termos/`. A **Devolutiva do Curador de 28/08/2026 (D-9)** autorizou a virada `ficha=False → ficha=True** a partir da fonte oral `P2022-03-26`, "uma vez que a palestra entrega a gênese técnica do objeto como mistura genética e sobrevivente". É a **única** materialização deste ciclo: `RC-444 Família Cromon` foi nominalmente mantida em `ficha=False`.

Com isso:

- a Base passa de **457 para 458 arquivos de ficha** e o cadastro de **456 para 457** linhas `ficha=True`;
- o cadastro continua em **777 termos** (teto curatorial; `RC-778` não consumido);
- as **1.856 relações permanecem intactas**: {len(arestas)} aresta(s) tocam RC-089 hoje — a rede deste termo é a que o cadastro já registrava, e nenhuma linha foi acrescentada a `RELACOES`;
- o cadastro lista em `relacionados` os códigos {", ".join(f"`{x}`" for x in rel_cadastro)}: **não há arestas correspondentes** para eles. Abrir essas arestas é decisão curatorial e continua pendente — a ficha declara a lacuna em vez de preenchê-la.

**Tensão a não escondar (D-10, sem harmonização):** `RC-446` registra que, na narrativa psicografada, *"Sophia, que nos engendrou, também criou todos os nossos 'Processadores'"* (B058, p. 68). A fala de 26/03/2022 dá **outra gênese** ao processador da família Vol: mistura genética feita **para absorver** as famílias rebeldes, depois de a revolta acontecer. As duas formulações coexistem na Base, cada uma com sua fonte e data; nenhuma é corrigida pela outra, e `RC-446` **não** foi editada por este ciclo.

**Origem do conteúdo da ampliação:** palestra `{SIGLA} — {TITULO}` (São Paulo, 26/03/2022), bloco U0034 (com apoio em U0008) do `original.txt` — transcrição automatizada, **não conferida com o áudio**. Cada aspa foi recortada byte a byte por `_gerar_ampliacoes_{SIGLA}.py` sobre o caça-âncoras `_aspas_{SIGLA}.py`; nada foi digitado de memória.

## Etimologia / Grafias

- **Canônico da Base:** *Processador Val* (família Val). ⚠️ A **família** aparece na fala de 2022 grafa pelo STT como `Vol` (6×), `vol` (4×), `voz` (2×), `V.` — o nome da família **não** é unificável a partir do TXT, e a forma canônica da Base permanece a das obras.
- **Na fonte oral (P2022-03-26):** o objeto é dito como *o processador da família Vol* e a nave que o hospeda como *Esferon* [REVISAR: nome novo, uma ocorrência] — ver o dicionário STT no apêndice da apostila do ciclo.
- **Vetado como grafia canônica** (devolutiva de 28/08/2026, D-4): nenhuma das degradações do STT promotione nome novo, e nenhuma máscara (`t*****`) transita para esta ficha.

## Ampliação — {SIGLA} ({TITULO})

{bloco}

## Fontes
| Obra (sigla) | Capítulo | Página | Tipo (citação/paráfrase) |
|---|---|---|---|
| {SIGLA} | {TITULO} (palestra) | — | transcrição automatizada; citação |
| B031 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B017 — Terra Atlantis: A Montagem Bíblica | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B018 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B039 — Terra Atlantis: A Era Sapiens | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| P2020-04-25 · P2026-04-02 | — | — | fontes orais já registradas no cadastro antes deste ciclo |

## Termos Relacionados
| Termo | Código | Tipo de relação |
|---|---|---|
| Processadores Familiares | RC-446 | análogo (aresta registrada na ficha RC-446; **não** há aresta em `RELACOES` para RC-089) |
| Família Val | RC-109 | listado no cadastro sem aresta |
| Biodemos | RC-036 | — (citação desta fala, não aresta) |

## Observações

A pergunta que `RC-446` deixava aberta — *"verificar nas obras primárias (ex.: B017/B018) a correspondência exata com os Processadores Familiares"* — **não** é respondida por esta ficha: a fala de 2022 não descreve um dispositivo capelino de coesão familiar neutra, e sim um **órgão de absorção** criado depois da revolta. Registrar a diferença é o serviço desta ficha; responder à pergunta de `RC-446` continua pendente e é decisão curatorial.
"""
open(ALVO, "w", encoding="utf-8").write(corpo)
print(f"ficha criada: {os.path.relpath(ALVO, RAIZ)} · {len(corpo):,} chars".replace(",", "."))
print(f"arestas em RELACOES tocando RC-089: {len(arestas)} (0 = nenhum grafo aberto por este ciclo)")
