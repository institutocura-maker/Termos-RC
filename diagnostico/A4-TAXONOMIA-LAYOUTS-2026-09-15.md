# A4 · Taxonomia dos layouts — inventário, transformação e tranches restantes

**Lavrado em:** 15/09/2026 · **Unidade:** U87
**Despacho do Curador:** «Chegou a hora de enfrentarmos o desafio arquitetural
da A4» — unificação taxonómica dos layouts.

---

## 1. Inventário (medição de abertura)

| | |
|---|---|
| fichas | 820 |
| fichas **com lote** (layout emitido pelo *driver*) | 147 |
| fichas **sem lote** (layouts legados) | 673 |
| assinaturas brutas (sequências de H2 distintas) | **471** |
| títulos H2 distintos nas 673 sem lote | 325 |

As 147 fichas com lote emitem sempre as **7 secções canónicas** e mais nada
(excepto 5 com `6. Histórico Curatorial e Auditoria`). São, portanto,
intocáveis por A4: qualquer edição manual seria perdida na regeneração.

## 2. Anatomia da fragmentação

A fragmentação não vem de secções diferentes, mas de **193 variantes de três
secções** que embutem a obra no próprio título:

| família | títulos distintos | ocorrências |
|---|---|---|
| `Ampliação — <obra> (<título>)` | 155 | 2 071 |
| `Atualização — <obra> (<título>)` | 30 | 190 |
| `Reforço — <obra>` | 8 | 76 |

**Verificação prévia à escrita:** 62% das linhas de corpo das Ampliações
(2 929 de 4 750) contêm a sigla da obra, e cada bullet começa por
`[P2023-12-03 · …]`. A referência está **redundante no corpo** — o título
pode ser normalizado sem perda de informação.

## 3. Vocabulário canónico proposto (15 títulos)

**Núcleo canónico (as 7 que o *driver* emite):**
`Definição Sintética` · `Contexto / Origem` · `Escopo e evidência` ·
`Termos Relacionados` · `Fontes` · `Citações-chave` · `Observações`

**Secções canónicas opcionais (legado com conteúdo próprio):**
`Etimologia / Grafias` (402) · `Seres Associados` (322) · `Ampliação` (2 071) ·
`Atualização` (190) · `Reforço` (76) · `Blindagem epistemológica` (51) ·
`Observações sobre o Estado da Malha` (60) · `Estrutura interna` (29)

## 4. Tranche 1 — EXECUTADA na U87

**Regra:** `## Ampliação — <obra>` → `## Ampliação` + `### <obra>`; idem para
`Atualização` e `Reforço`. Fusão das repetições **consecutivas** (as
repetições são adjacentes na quase totalidade dos casos, pelo que **nenhuma
linha de corpo foi movida**). Correcção incidental do título defeituoso
`## ## Ampliação` (10 ocorrências).

| | |
|---|---|
| fichas afectadas | 523 |
| subtítulos `###` criados | 2 379 |
| H2 redundantes removidos por fusão | 1 542 |
| títulos variantes extintos | 193 → 3 |
| **assinaturas** | **471 → 188 (−60%)** |
| linhas de corpo movidas | **0** |
| fichas com lote afectadas | **0** |

A RC‑092, que tinha 32 H2 idênticos, passa a uma única `## Ampliação` com 28
subtítulos `### <obra>`.

**Salvaguardas verificadas:** nenhuma ficha com lote tocada · nenhum byte de
corpo alterado (conferido ficheiro a ficheiro contra o HEAD) · 97% dos
subtítulos conservam a sigla da obra.

## 5. Dependência descoberta — a camada pedagógica cita títulos de secção

O verificador (`verificar_verbetes.py`, teste T5) confirma que os verbetes da
enciclopédia citam **títulos de secção das fichas como verbatim**. A
transformação tornou 4 citações órfãs, em 3 verbetes:

| verbete | citação órfã | resolução |
|---|---|---|
| V3.16.03‑RC690 | `Ampliação — P2024-11-09` | → entrada «P2024-11-09» da secção «Ampliação» |
| V3.16.03‑RC690 | `Ampliação — P2025-03-15` | → entrada «P2025-03-15» da secção «Ampliação» |
| V4.18.03‑RC518 | `## ## Ampliação` | o defeito foi corrigido; registo actualizado |
| V5.22.01‑RC558 | `## ## Ampliação` | idem |

Duas destas citações **documentavam o próprio defeito** (`## ## Ampliação`)
que a tranche 1 corrigiu; os registos foram actualizados para o declarar
corrigido, preservando o histórico.

> **Doutrina:** qualquer futura normalização de títulos de secção deve
> reemitir os verbetes pedagógicos que os citem, no mesmo commit (Baliza 3
> da U80).

## 6. Tranches restantes

| tranche | conteúdo | assinaturas |
|---|---|---|
| — | partida | 471 |
| 1 | família Ampliação/Atualização/Reforço → H2 + H3 · **feita na U87** | **188** |
| 2 | variantes gráficas: `Citação-chave`→`Citações-chave` (105) · `Observação`→`Observações` (28) · `Relações`/`Relações centrais`→`Termos Relacionados` (71) · `Etimologia`→`Etimologia / Grafias` (3) · `Blindagem`→`Blindagem epistemológica` (24) | **177** |
| 3 | 66 títulos residuais (108 ocorrências), revisão individual — `Cautela editorial` (10) · `Quarentena Terminológica` (10) · `Glossário interno` (9) · `6. Histórico Curatorial e Auditoria` (6) · 62 com ≤3 | ~150 |
| 4 | **unificação da ORDEM** — decisão editorial: reordenar as secções de cada ficha pela ordem canónica. Move conteúdo; merece unidade própria e despacho expresso. | a decidir |

A tranche 2 deixa prever **colisões** (fichas que ganhariam dois H2 iguais,
por terem já `Termos Relacionados` e `Relações centrais`): exigem fusão
prévia e foram por isso deixadas fora desta unidade.

---

**A4 não está encerrada: 471 → 188 nesta unidade. Faltam as tranches 2, 3 e 4.**
