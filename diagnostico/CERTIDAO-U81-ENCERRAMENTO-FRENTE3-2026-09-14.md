# CERTIDÃO FINAL DA CAMPANHA R1
## Selo de encerramento da fase ativa da família B v3 · mapeamento das arestas pendentes de infraestrutura

**Data:** 14/09/2026 · **Despacho:** U81 — «Aprovação da Frente 2 e autorização da Frente 3»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0** · verificação dupla de HEAD
**Alcance:** 34 lotes (U42 → U77) · 820 fichas · 946 termos · 1 887 relações · 158 obras com texto

---

## 0. Abertura: a 5.ª regressão do git, contida pelo duplo cinturão

A checagem de **abertura** acusou divergência:

```
HEAD local : 0a640cf   (o commit BASE da branch — U40)
remoto     : 3ce9e07   (U80)
igual      : NÃO — ABORTAR
pendentes  : 245
```

**Operação abortada antes de qualquer escrita.** Diagnóstico, na ordem devida:

- **O disco estava íntegro.** Medido antes de tocar em nada: 946 termos · 1 887 relações · 820 fichas ·
  cadastro no ponto exacto da U80 (`RC-347 → ['B026']`) · certidão U80 presente · rastro presente na ficha.
- Quem regrediu foi a **ref do git**, como nas anteriores.
- O `SESSION-NOTES` reapareceu **trocado pelo ficheiro de OUTRA branch**
  (cabeçalho `arena/01a071c8-termos-rc`, 2 258 linhas, sem o bloco U80) — o mesmo modo de falha da U79.

Receita das U48/U61/U67/U79: salvaguarda de 4 679 ficheiros em `/tmp`, `git reset --mixed FETCH_HEAD`
(**nunca `--hard`**), e `git checkout HEAD -- .arena/SESSION-NOTES.md`. Estado reposto: **HEAD == remoto,
0 pendentes, 820 fichas**, histórico U78 → U79 → U80 intacto.

É a **quinta** ocorrência (U48, U61, U67, U79, U81). O duplo cinturão da U68 conteve-a sem dano — e é por
isso que a checagem de abertura existe.

## 1. O que se encerra

A **campanha R1** — rota de materialização ancorada pela obra (U57: «ancoragem pela obra que ocorre»),
um lote por fonte, sem interromper a esteira para higienizar (U58).

| dimensão | número |
|---|---|
| lotes emitidos | **34** (U42‑R1‑LOTE1 → U77‑R1‑LOTE34) |
| critério de ancoragem | censo v3 em 27 lotes · censo v2 em 5 · critério específico em 2 |
| fichas materializadas por lote | **139** |
| citações declaradas nos lotes | 747 |
| fichas na Base | **820** |
| termos · relações · obras declaradas | 946 · 1 887 · 102 |
| obras com texto no workspace | 158 (29 MB de `original.txt`) |

O **fim da fase ativa** é declarado com o poço seco: a U77 foi o lote final, sem sucessor possível sob o
critério vigente. O que se segue não é materialização — é manutenção e infraestrutura.

## 2. O selo: Portão B invicto, provado na íntegra

Não se certifica por amostra. Todas as citações de todas as 820 fichas foram reextraídas e confrontadas
com a **linha declarada** do `original.txt` da obra declarada:

```
CITAÇÕES COM APARELHO R1 (todas as 820 fichas) : 778
  confere na LINHA DECLARADA                   : 778
  confere noutra linha da mesma obra           :   0
  FALHAS                                       :   0
  fichas que contêm citações                   : 147
  obras distintas citadas                      :  38
```

**778 / 778, zero falhas.** Nenhuma citação foi encontrada em linha diversa da declarada — o aparelho
`— SIGLA p. N · original.txt LNNN` é exacto em todos os casos. Obras mais citadas: B031 (199), B001 (51),
B024 (50), B044 (46), B005 (39), B015 (35).

Prova complementar e independente: **32 dos 34 lotes são idempotentes** — reexecutados com
`--sobrescrever` numa cópia do repositório, todas as suas fichas saíram `idêntico (nada a reescrever)`,
isto é, o driver as reconstruiu byte a byte a partir da fonte e chegou ao mesmo ficheiro.

## 3. O que NÃO é R1: o corpus legado, medido com a mesma régua

681 das 820 fichas não têm lote: são gerações anteriores (piloto 2.1 e expansões). Muitas trazem citações
**sem o aparelho R1** — blocos `> «…»` sem a ancoragem `— SIGLA · LNNN`. Foram medidos com honestidade,
por janelas de 6 palavras sobre o corpus inteiro (tolerando o *hard-wrap*):

| medida | número |
|---|---|
| blocos de citação legados (sem aparelho) | **154** |
| localizáveis verbatim nalguma obra do corpus | **139** |
| **não localizáveis** em nenhuma das 158 obras | **15** (em 11 fichas) |
| localizáveis **fora** das fontes declaradas | **1** |

Os 15 não localizáveis concentram‑se em 11 fichas, quase todas ancoradas em palestras da série
P2023‑12‑25‑0N e P2018‑10‑06: RC‑778 · RC‑779 · RC‑834 · RC‑835 · RC‑862 · RC‑887 · RC‑942 · RC‑943 ·
RC‑944 · RC‑945 · RC‑946. **As fontes têm texto ingerido** — o que falta é o trecho: são transcrições
parciais ou versões diversas. Não são falsificações provadas; são **citações não verificáveis no estado
actual do arquivo**, e como tais ficam registradas.

## 4. Mapa formal das arestas pendentes de infraestrutura

Requisitos para o futuro. Nenhum bloqueia o selo; todos são dívida declarada.

### A1 — `U42-R1-LOTE1` não reexecutável (8 fichas)
**Sintoma:** `AssertionError: RC-108: status 'verificado' incompatível com aplicar_V=False`.
**Causa:** o lote não possui a chave `aplicar_V` (nem no lote, nem por ficha); os seus 8 códigos
(RC‑108, RC‑085, RC‑065, RC‑066, RC‑540, RC‑077, RC‑044, RC‑392) estão hoje todos `verificado` no
cadastro, promovidos por despachos posteriores.
**Reparo:** no **JSON do lote**, nunca no driver. Nenhuma asserção foi afrouxada.

### A2 — `U44-R1-LOTE2` não reexecutável (8 fichas)
**Sintoma:** `KeyError: 'fam'`.
**Causa:** o lote traz `aplicar_V` mas as suas 8 fichas (RC‑032, RC‑048, RC‑073, RC‑123, RC‑095,
RC‑438, RC‑374, RC‑211) não têm a chave `fam`, introduzida nos lotes seguintes.
**Reparo:** no **JSON do lote**.

> A1 e A2 cobrem 16 das 139 fichas com lote. As restantes **123** são plenamente regeneráveis.

### A3 — 8 fichas com citações mas sem lote (29 citações)
RC‑027 · RC‑030 · RC‑050 · RC‑051 · RC‑090 · RC‑097 · RC‑100 · RC‑304. Têm citações verificadas
(integram as 778), mas **nenhum lote as pode regenerar**. A RC‑100 foi corrigida à mão na U80;
as outras sete aguardam lote próprio.

### A4 — Unificação de layouts
As 820 fichas apresentam **471 combinações distintas** de secções. Distribuição:

| arquétipo | fichas |
|---|---|
| canónico R1 (Definição Sintética · Contexto/Origem · **Escopo e evidência** · Termos Relacionados · Fontes · Citações‑chave · Observações) | **144** |
| com «Escopo e evidência» (qualquer variante) | **169** |
| layout pré‑R1 com «Etimologia / Grafias» | 75 |
| demais variantes | resto |

**Requisito:** convergir para o arquétipo canónico. O frontmatter de **todas** as 820 está em sincronia
com o cadastro (T15: 0 divergentes), pelo que a unificação é cosmética‑estrutural, não substantiva.

### A5 — 15 blocos de citação legados não localizáveis (11 fichas)
Ver § 3. **Requisito:** reingestão das transcrições integrais (séries P2023‑12‑25‑0N, P2018‑10‑06) e
reancoragem pelo aparelho R1.

### A6 — 1 citação localizável fora das fontes declaradas
Um bloco legado cujo texto ocorre numa obra **não listada** no `fontes` da ficha.
**Requisito:** corrigir a atribuição na respectiva ficha.

### A7 — Dívidas conhecidas, fora do escopo desta certidão
- **RC‑296** — série P congelada (U53/U54), não tocada.
- **RC‑118** — sem lote, não regenerável.
- **B049** — normalizada na U79 (0 TABs); persiste o segundo artefato, **espaços intra‑palavra**
  (ex.: L106 «Reflex ão Neces s á ria»), não tocado por exigir confronto com o impresso.
- **Censo v3** guarda só 3 blocos por código: serve para achar, nunca para provar ausência (U65).

## 5. Invariantes que ficam garantidas

| verificação | resultado |
|---|---|
| suíte | **21/21 · EXIT=0** |
| T13 · fichas com frontmatter | **820** |
| T14 · tabelas == cadastro | **0 divergentes** |
| T15 · `motor.fm_toml` == frontmatter | **820 conferidas · 0 divergentes** |
| verificador | **946 termos · 820 fichas · 1 887 relações** · todo verbatim confere byte a byte |
| Portão B (varrimento integral) | **778/778 na linha declarada · 0 falhas** |
| idempotência dos lotes | **32/34** (as 123 fichas restantes, regeneráveis byte a byte) |
| paridade ficha ↔ cadastro | **820/820** frontmatter |
| rastro da higienização (U80) | **10/10** fichas · **10/10** no `.docx` |

## 6. Encerramento

Declara‑se **encerrada a fase ativa da campanha R1** e **selada a família B v3** com 820 fichas e o
**Portão B invicto**: toda citação com aparelho R1 confere byte a byte contra o `original.txt` da obra
declarada, na linha declarada, sem uma única falha em 778 verificações.

O que fica não é trabalho a meio, é **dívida mapeada**: 2 lotes por reparar no JSON, 8 fichas por
lotear, 471 layouts por unificar, 15 citações por reancorar, 1 atribuição por corrigir. Nenhuma dessas
arestas é conteúdo em falta — nenhuma põe em causa uma única linha do que está certificado.

```
┌──────────────────────────────────────────────────────────────┐
│  CAMPANHA R1 · SELADA EM 14/09/2026                          │
│  820 fichas · 946 termos · 1 887 relações · 158 obras         │
│  778/778 citações conferidas byte a byte · 0 falhas           │
│  Frentes: 1 ✅ · 1.5 ✅ · 2 ✅ · 3 ✅                          │
└──────────────────────────────────────────────────────────────┘
```
