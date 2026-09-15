# CERTIDÃO — U80 · ENCERRAMENTO · FRENTE 2
## Higienização do campo `fontes` (regime substitutivo) e reemissão das fichas afectadas

**Data:** 14/09/2026 · **Despacho:** U80 — «Frente 2, Regime Substitutivo, 3 Balizas»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0** · verificação dupla de HEAD
**Escopo:** 28 candidatos do inventário U57 → **12 siglas expurgadas em 10 códigos** · **10 fichas reemitidas no mesmo commit**

---

## 0. Abertura: HEAD limpo

```
HEAD local : f4b6d50   (U79)
remoto     : f4b6d50
igual      : SIM
pendentes  : 0
```

Nenhuma regressão do git nesta unidade (a 4.ª, da U79, não se repetiu).

## 1. Primeira conclusão: o inventário U57 **não é fiável**

O `INVENTARIO-DESVIOS-FONTE-DECLARADA-2026-09-13.md` declara «sem ocorrência» para vários pares que
**têm** ocorrência provada. Falsos «zero» confirmados:

| par declarado «sem ocorrência» | realidade medida |
|---|---|
| B060 / «Astréia» | ocorre (L29, L31) |
| B017 + B018 / «Benem» | 29 e 31 ocorrências |
| B042 + B057 / «Orbum» | ocorre |
| B075 / «Kundalini» | ocorre |
| B026 / «planeta azul» | 23 ocorrências |
| B052 / «linhagem» | 75 ocorrências |
| B042 + B011 / «o Mais Alto» | ocorre |
| B022 + P2024-11-30 / «Tríade» | ocorre |
| P2024-11-03 / «Kundaline» | ocorre |
| B019 / «Criatura Universal» | ocorre |

**Causa:** o censo v3 (`CENSO-V3-ESPACADAS`) guarda apenas **3 blocos por código** — serve para *achar*,
não para *provar ausência* (U65: «censo é achador, não cerca»).

**Consequência metodológica, adoptada nesta unidade:** o inventário passa a valer como **mapa de
candidatos**, nunca como lista de erros. Cada decisão exigiu varredura própria, por dois métodos
independentes — varrimento **linha a linha** e varrimento sobre **blocos recompostos**
(`censo_gap_v2.tem_bloco`, que resolve o *hard-wrap*). Os dois métodos concordaram em todos os zeros
aqui certificados.

## 2. O método de verificação: quatro camadas

Uma sigla só é expurgada se falhar **simultaneamente** nas quatro:

1. **Chave literal** — nenhuma ocorrência da chave na obra, em **blocos recompostos** (não em linhas soltas).
2. **Citação** — nenhuma citação daquela ficha naquela obra (varridos todos os lotes `U*-R1-LOTE*.json`).
3. **Matéria** — nenhuma ocorrência distintiva da matéria: nem a chave, nem variante gráfica (hífen,
   acento, grafia alternativa), nem epíteto, nem forma parcial do nome. A co-ocorrência simples foi
   **abandonada** por gerar falsos positivos em blocos gigantes; adoptou-se **proximidade ≤ 6 palavras**
   mais a regra decisiva «se a ficha cita a obra, há evidência», com leitura manual do trecho.
4. **Aresta** — nenhuma aresta em `RELACOES` com aquela fonte (ver § 3).

## 3. A regra nova que esta Frente produziu: **aresta é evidência**

> Se existe `(a, t, cod, f)` em `RELACOES`, então **f é evidência de `cod`** — a aresta é um acto de
> registro ancorado numa leitura. Nunca expurgar uma fonte que sustente uma aresta.

Seis expurgos originalmente planeados **caíram** por esta regra, e um sétimo (RC‑184 −B020) caiu pela
aresta `RC-285 rompe RC-184 B020`. O expurgo passou a ser precedido de um `assert` de **0 conflitos**
antes de tocar no cadastro.

## 4. As três balizas do despacho U80, aplicadas

**Baliza 1 — só se expurga quem tem ZERO evidência; a pluralidade legítima fica intacta.**
Aplicada. Ficaram mantidas, contrariando o inventário U57: B060 × RC‑027 · B017/B018 × RC‑032 ·
B017/B018 × RC‑065 · B018/B039 × RC‑123 · B060 × RC‑112/116/129 · B011/B060 × RC‑138 ·
B024/B006 + P2025‑03‑15 + P2025‑02‑16 × RC‑100 · B019 × RC‑172 · B001 × RC‑209 ·
B075 e P2024‑11‑03 × RC‑211 · B026 × RC‑090 · B036 × RC‑270 · B021 × RC‑300.
Dentro dos 10 códigos mexidos, também ficaram: **B023 × RC‑082** (aresta `RC-323 envolve RC-082 B023`),
**P2025‑03‑15 e P2025‑02‑16 × RC‑100** (arestas RC‑692/RC‑699),
**P2026‑04‑02 × RC‑138** (arestas RC‑647/RC‑365).
**RC‑296 não foi tocada** — série P congelada (U53/U54).

**Baliza 2 — palestra como fonte exclusiva, confirmada.**
Aplicada. **Nenhum dos 10 verbetes ficou só com palestra**: todos conservam pelo menos uma obra
(B031, B044, B001, B026, B011, B021, B024, B006, B018, B023, B042, B057, B060, B075). Logo,
**nenhum verbete mudou de natureza** nesta Frente, e nenhum erro de cadastro precisou de ir para
observações por esse motivo. As palestras mantidas (P2025‑03‑15, P2025‑02‑16, P2025‑02‑15,
P2024‑11‑09, P2026‑04‑02, P2024‑05‑04 e P2024‑11‑03 em RC‑211) têm evidência própria.

**Baliza 3 — reemissão dentro da Frente 2 (Princípio da Atomicidade).**
Cumprida: metadado e `.md` no mesmo commit. Ver § 6.

## 5. Os 12 expurgos, e a auditoria que os sustenta

| código | termo | sigla expurgada | estado final |
|---|---|---|---|
| RC‑077 | Lokas | B060 — *Personagens e Terminologias da Revelação Cósmica* | B031, B021 |
| RC‑082 | Nephilins | B017 — *Terra Atlantis I* | B031, B018, B023 |
| RC‑085 | Orbum | P2020‑08‑08 — *Sophia e o alinhamento interdimensional do moscoviano* | B031, B042, B057 |
| RC‑100 | Seres Espirituais | P2024‑11‑30 — *Morus — arquivos, destino universal* | B031, B024, B006, P2025‑03‑15, P2025‑02‑16, P2025‑02‑15, P2024‑11‑09 |
| RC‑138 | Yel Am / Yel Liam | P2025‑10‑25 — *Estagiários do Kaos (2ª ed.)* | B031, B011, B060, P2026‑04‑02 |
| RC‑177 | Colmeia do Éden | B015 — *O Guardião do Éden* | B044 |
| RC‑208 | Criador de Padrões Dependentes | P2024‑05‑04 — *Prabrajna, Perperion, simultaneidade reversa* | B001, B002 |
| RC‑209 | Vida de Padrão Dependente | P2024‑05‑04 — *idem* | B001, B002 |
| RC‑211 | Kundalini | B074 — *Mentalma I* · P2023‑07‑05 — *O despertar dos potenciais da consciência pessoal* | B001, B075, P2024‑05‑04, P2024‑11‑03 |
| RC‑347 | Projeto Terra | B019 — *Nem Deus, nem Javé, nem Darwin* · P2024‑11‑30 — *Morus* | B026 |

**Auditoria final, reproduzível, executada sobre o corpus carregado (158 obras · 14 600 blocos):**

```
código   sigla         chave na obra   citação  aresta  veredicto
------------------------------------------------------------------------------
RC-077   B060                      0     False   False  EXPURGO VÁLIDO
RC-082   B017                      0     False   False  EXPURGO VÁLIDO
RC-085   P2020-08-08               0     False   False  EXPURGO VÁLIDO
RC-100   P2024-11-30               0     False   False  EXPURGO VÁLIDO
RC-138   P2025-10-25               0     False   False  EXPURGO VÁLIDO
RC-177   B015                      0     False   False  EXPURGO VÁLIDO
RC-208   P2024-05-04               0     False   False  EXPURGO VÁLIDO
RC-209   P2024-05-04               0     False   False  EXPURGO VÁLIDO
RC-211   B074                      0     False   False  EXPURGO VÁLIDO
RC-211   P2023-07-05               0     False   False  EXPURGO VÁLIDO
RC-347   B019                      0     False   False  EXPURGO VÁLIDO
RC-347   P2024-11-30               0     False   False  EXPURGO VÁLIDO
```

**12/12 válidos.** Verificação suplementar de integridade: para os 10 códigos,
`estado anterior − expurgadas == estado final` (asserção exacta, sem sobras).

**Nota de método sobre arquivo:** todas as 12 siglas tinham **texto presente** no corpus — nenhum
expurgo se apoiou na ausência do ficheiro. (As palestras vivem sob `apostilas/CONCLUIDAS/` e
`ciclos/`, com pastas iniciadas por data; `censo_gap_v2` prefixa `P`.)

## 6. Reemissão das fichas (Baliza 3)

**6 por lote**, com prova de reproducibilidade — `materializar_lote.py --sobrescrever` sobre os
lotes 4, 5, 6, 7 e 29: **todas as fichas do lote saíram `idêntico (nada a reescrever)`, e as 6 alvo
foram regeradas**. RC‑082 · RC‑138 · RC‑177 · RC‑208 · RC‑209 · RC‑347.

**4 à mão**, por não haver lote reexecutável: RC‑077 · RC‑085 · RC‑100 · RC‑211. O patch altera
exactamente duas linhas, ambas **geradas a partir do cadastro** — o frontmatter por `motor.fm_toml`
(garante a paridade T15) e a linha «Fontes declaradas no cadastro» pelo mesmo formatador do driver
(`', '.join(termo[5])`) — mais a nota de rastro.

**Rastro da higienização:** as 10 fichas receberam, nas **Observações**, o registro do que foi
expurgado, com a declaração original preservada textualmente. Onde houve lote, a nota foi escrita no
`obs` do lote (fonte de verdade) e a ficha regerada pelo driver; onde não houve, foi inserida
directamente. Verificado: **10/10 com rastro**, e o rastro consta do `.docx` de leitura (10/10).

**Por que dois lotes não são reexecutáveis (dois erros de driver, nenhum corrigido no driver):**

- `U42-R1-LOTE1` → `AssertionError: RC-108: status 'verificado' incompatível com aplicar_V=False`.
  O lote 1 traz `aplicar_V` que o cadastro de hoje já não sustenta (RC‑108 foi promovido por despacho
  posterior). **O dessincronizado é o JSON do lote, não o driver.**
- `U44-R1-LOTE2` → `KeyError: 'fam'` — formato antigo de lote, sem a chave hoje exigida.
  **Corrigir o JSON, nunca o driver.**

Nenhuma asserção do `materializar_lote.py` foi afrouxada (o reparo da U77 aguarda homologação).

## 7. Dois erros meus nesta unidade, ambos detectados e corrigidos

1. **Matcher de fecho de array:** ao inserir as notas no JSON, procurei o fecho `   ]` — mas quando
   outra chave se segue, o fecho é `   ],`. A nota da RC‑138 foi parar ao array `historico`.
   Corrigido para `^\s*\],?$`; verificado depois por código (nota é o **último** elemento de `obs`,
   `historico` intacto).
2. **Restauro por iteração:** processei RC‑208 e RC‑209 em iterações separadas, cada uma começando por
   `git checkout HEAD` — o segundo restauro apagou a nota do primeiro. Corrigido agrupando as fichas
   **por ficheiro**, com um único restauro por ficheiro.

Prova final de que o delta dos 5 JSONs de lote é **só a nota**: carregados o HEAD e a versão nova,
removida a nota, `ant == nov` para os cinco (e validada a colocação, não apenas a presença).

Ruído evitado: a reescrita por `json.dump(indent=1)` explodia ~900 linhas de formatação; as notas
foram reinseridas **no estilo original** de cada ficheiro — delta final de **3 linhas por nota**.

## 8. Invariantes ao encerrar

| verificação | resultado |
|---|---|
| suíte | **21/21 · EXIT=0** |
| T13 · fichas com frontmatter | **820** |
| T14 · tabelas == cadastro | **0 divergentes** |
| T15 · `motor.fm_toml` == frontmatter | **820 conferidas · 0 divergentes** |
| verificador de verbetes | **946 termos · 820 fichas · 1887 relações** · todo verbatim confere byte a byte |
| canónico | 946 termos · 1887 relações |
| espelhos reconstruídos | xlsx **820/820** (7 abas) · docx **820** fichas |
| paridade ficha ↔ cadastro | **820/820** frontmatter · **149/149** bullets em sincronia · **0** divergências |
| rastro nas 10 fichas | **10/10** |

## 9. Observações e dívidas para a Frente 3

1. **Heterogeneidade do corpus:** as 820 fichas apresentam **471 layouts distintos** de secções; só
   **169** possuem a secção «Escopo e evidência» (das quais 144 no layout canónico R1). As restantes
   são de gerações anteriores, muitas com a tabela `## Fontes` ainda em «a identificar». Condição
   **pré-existente**, não criada por esta Frente; o frontmatter de todas está em sincronia com o
   cadastro, pelo que não há falsa declaração em jogo. Fica o registro para a certidão final.
2. **Dois lotes não reexecutáveis** (U42‑LOTE1, U44‑LOTE2) — os seus JSONs estão dessincronizados do
   cadastro de 14/09. A sanar quando forem reprocessados; nunca pelo driver.
3. **RC‑100** não tem lote (dívida conhecida, da mesma natureza da RC‑118): foi aqui corrigida à mão,
   com frontmatter gerado pelo motor. Continua não regenerável por lote.
4. **Co-ocorrência simples não serve como prova de matéria** — gerou falsos positivos em blocos
   gigantes (B024, B006, B019, B042, B022, B036, B052). O critério adoptado (proximidade ≤ 6 palavras
   + leitura manual + a regra «ficha que cita, tem evidência») deve ser o padrão daqui em diante.
5. **Censo v3 guarda só 3 blocos por código** — não serve para provar ausência (reforço da U65).

---

**Frentes:** 1 ✅ U78 · 1.5 ✅ U79 · **2 ✅ U80** · 3 ⏳ (certidão final da campanha R1)
