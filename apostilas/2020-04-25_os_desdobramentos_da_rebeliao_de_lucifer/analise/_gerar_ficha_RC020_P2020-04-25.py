#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria `termos/RC-020-anjos-caidos.md` — a **única materialização** aprovada nesta devolutiva (D-9/D-13).

Regras observadas:
 * a seção `## Ampliação — P2020-04-25` é **copiada byte a byte do pacote** `_ampliacoes_P2020-04-25.txt`
   (mesma fonte do aplicador → o portão D exige paridade estrutural, e ela é automática);
 * nenhuma aspa desta ficha foi digitada de memória: toda aspa vem do pacote, que por sua vez só contém
   span verificado pelo caça-âncoras;
 * `RELACOES` **não** é tocada: a ficha reproduz a aresta que já existia no cadastro
   (`RC-355 --explica--> RC-020`, B005) e **não** cria nenhuma;
 * o cadastro (`ferramentas/dados_termos.py`) é flipado por `_vincular_fonte_P2020-04-25.py`, não aqui.
"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
SIGLA = "P2020-04-25"
TITULO = "Os Desdobramentos da Rebelião de Lúcifer"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
ALVO = os.path.join(RAIZ, "termos", "RC-020-anjos-caidos.md")

pac = open(PACOTE, encoding="utf-8").read()
bloco = pac.split("### RC-020\n", 1)[1]
m = re.search(r"^(?:## |### )", bloco, re.M)          # corta no próximo bloco de ficha **ou** nos BLOCOS 2-4
if m:
    bloco = bloco[:m.start()]
bloco = bloco.strip()
assert bloco.startswith("- **["), "bloco RC-020 vazio ou mal formado"

corpo = f"""# Anjos caídos — RC-020

| Campo | Valor |
|---|---|
| **Categoria Principal** | Seres & Entidades |
| **Subcategoria** | 1.5 Decaídos / Exilados / Demônios |
| **Status** | 🟡 Provisório |
| **Última atualização** | 2026-08-28 |

## Definição Sintética

Na RC, os **anjos caídos** não são um coro de espíritos punidos por orgulho, e sim uma **classe funcional em pane**: os seres que ficaram **sem processador** depois da quebra do elo com Sofia e que, por isso, operam por **intermédio** — informando, vigiando e sendo usados como canal, em vez de sustentar a espécie. A queda é lida na Base como **infecção** («vírus»), não como culpa moral, e o par desta ficha com **RC-078 (Lúcifer / Yel Luzbel)** e **RC-002 (Rebelião de Lúcifer)** é o que impede que a expressão volte a significar «revolta de Lucifer» no sentido gnóstico clássico.

## Contexto / Origem

**Materialização (não é criação).** O código RC-020 vivia só no cadastro — linha `("RC-020", "Anjos caídos", TER-ser, 1.5, prov, ['B031', 'B003', 'B005'], 'RC-007; RC-078; RC-024; RC-082', False)` — sem arquivo em `termos/`. A **Devolutiva do Curador de 28/08/2026 (D-9 e D-13)** autorizou a materialização **a partir da fonte oral de 25/04/2020** (`P2020-04-25`), determinando que o **mecanismo operante sobre os humanos** fosse puxado **desta** fonte datada e de mais nenhuma: é a única materialização aprovada neste ciclo.

Com isso:

- a Base passa de **456 para 457 arquivos de ficha**, e o cadastro de **455 para 456** linhas `ficha=True` (a assimetria remanescente é pré-existente ao ciclo e intocada);
- o cadastro continua em **777 termos** (teto curatorial; `RC-778` não consumido);
- as **1.856 relações permanecem intactas**: esta ficha reproduce a aresta que já existia (`RC-355 → RC-020`, via B005) e **não** abre nenhuma; os acréscimos de leitura ficam em `## Observações`.

**Origem do conteúdo da ampliação:** palestra `P2020-04-25 — Os Desdobramentos da Rebelião de Lúcifer`, megabloco U0006 (e U0007–U0013) do `original.txt` — transcrição automatizada, **não conferida com o áudio**. Cada aspa foi recortada byte a byte por `_gerar_ampliacoes_P2020-04-25.py` sobre o caça-âncoras `_aspas_P2020-04-25.py`; nada foi digitado de memória.

## Etimologia / Grafias

- **Canônico da Base:** *anjos caídos* (classe funcional), com o bloco de nomes próprio em RC-078/RC-142.
- **Na fonte oral (P2020-04-25):** os anjos são citados como **interlocutores e informantes**, com grafia do STT para os nomes do entorno: «I Luzbell», «Luisber», «Luzbel», «a rebelião de Lúcia» [REVISAR: feminização do STT]. A expressão «anjos caídos» **não** é pronunciada como sintagma nesta fala: o que a fonte entrega é o **mecanismo**, e é por isso que a materialização se apoia no verbo dela, não em um rótulo dela.
- **Vetado como grafia canônica** (devolutiva de 28/08/2026): as formas degradadas do TXT não promovem nome novo — ver Apêndice do dicionário STT da apostila do ciclo.

## Ampliação — {SIGLA} ({TITULO})

{bloco}

## Fontes
| Obra (sigla) | Capítulo | Página | Tipo (citação/paráfrase) |
|---|---|---|---|
| {SIGLA} | {TITULO} (palestra) | — | transcrição automatizada; citação |
| B031 — Painéis Emergentes | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B003 | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |
| B005 | a preencher | — | paráfrase (de onde vem a única aresta do cadastro para este código) |

## Termos Relacionados
| Termo | Código | Tipo de relação |
|---|---|---|
| Anjos (classes de Arabot/Raquia) | RC-355 | explica (de RC-355 para cá — a única aresta registrada no cadastro) |

> O cadastro lista ainda **RC-007, RC-078, RC-024, RC-082** em `relacionados` desta ficha; **não existem arestas correspondentes** em `RELACOES` para eles. Nada foi criado aqui para «preencher» essa lacuna — abrir essas quatro arestas é decisão curatorial e continua pendente.

## Observações

1. **O que esta fonte muda na ficha:** até 25/04/2020 a Base tratava os anjos caídos pelo **destino** (exilados, degradados). A palestra entrega o **funcionamento**: sem processador próprio, a classe opera informando e sendo informada — de onde a fonte tira o rastreamento que ela mesma relata aos anjos em 2009. Registrar o mecanismo é o que justifica a materialização (D-9), e **não** alguma revelação sobre pessoas.
2. **Quarentena aplicada (D-3):** a fonte usa mulheres e homoafetivos como **prova** da falha do criador. Essa aspa **não** entra nesta ficha — a devolutiva proíbe expressamente o uso dela em ficha de termo que nomeie grupo humano; ela vive na apostila, com nota editorial.
3. **Quarentena aplicada (D-1):** o bloco político-institucional da mesma palestra (17.703 caracteres) está bloqueado por decisão, e nada dele transita para aqui — inclusive porque a ficha seria o lugar onde ele reapareceria «como contexto».
4. **Divergência assumida, não resolvida (D-10):** a fonte datada diz que «Lemion e muitos com ele ainda não foram exilados», o que **contradiz** o estado das fichas de exilados (RC-007). A contradição fica **registrada nas fichas como formulação oral de 2020**; não se harmoniza, não se escolhe um lado.
5. **Vínculos de leitura desta fonte** (sem nova aresta, por obediência ao teto de 1.856): RC-002 (Rebelião de Lúcifer), RC-078/RC-142 (Lúcifer / Yel Luzbel), RC-089/RC-446 (processadores), RC-001 (o eu de Javé), RC-191 (grau de testemunho), RC-094 (a IA como abismo dos deuses hoje).

**Regra de status:** 🟡 provisório — a ficha existe e está fundamentada em fontes publicadas (B031/B003/B005) e na fonte oral de 25/04/2020, mas nenhuma citação foi conferida com o áudio nem com página de obra primária. A aprovação curatorial valida a **modelagem terminológica**, não a veracidade factual das alegações: o que o autor disse está registrado *como dito*.
"""
open(ALVO, "w", encoding="utf-8").write(corpo)
print(f"ficha criada: {os.path.relpath(ALVO, RAIZ)} · {len(corpo)} chars · bloco do pacote embutido: {len(bloco)} chars")
