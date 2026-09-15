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

---

## 7. Tranche 2 — EXECUTADA na U88 (parte sem conflito)

Aplicadas as regras do despacho que **não divergem** das cadeias emitidas pelo
*driver*: `Relações` / `Relações centrais` → `Termos Relacionados` (71) ·
`Observação` → `Observações` (28) · `Blindagem*` → `Observações` (35) ·
`Etimologia` / `Grafia` / `Nomes` → `Etimologia e Grafias` (406).

| | |
|---|---|
| fichas afectadas | 495 |
| títulos renomeados | 556 |
| fusões (só as geradas pela renomeação) | 75 |
| **assinaturas** | **188 → 178** |
| corpo alterado | **0** |

### Regra de colisão — refinamento necessário
O despacho manda fundir quando a normalização gera dois H2 iguais. A Base
porém contém **122 secções duplicadas pré-existentes** (77 `Ampliação`,
24 `Fontes`, 18 `Atualização`, 3 `Reforço`) que não foram geradas por
nenhuma renomeação. Duas tentativas erradas ficam registadas para não se
repetirem:

1. **Fundir qualquer duplicado** → fundiu as duas `## Fontes` da RC‑089,
   concatenando duas tabelas de colunagens diferentes. O **T7 apanhou** 17
   fichas com `fontes` malformadas.
2. **Fundir só quando o título mudou** → falhou quando a *primeira* das duas
   secções era a renomeada (39 fichas ficaram com `Termos Relacionados`
   duplicado).

**Regra correcta, aplicada:** não fundir o que **já era** duplicado antes da
renomeação; fundir apenas as colisões que a renomeação cria. Contagem de
duplicados antes e depois: **122 → 122** (nenhum novo).

### Dependência pedagógica (U87) confirmada
Mais uma citação órfã, corrigida no mesmo commit: V4.18.03‑RC732 citava
«Blindagem clínica e científica máxima», secção-fronteira distintiva da
RC‑732, convertida por esta tranche em «Observações». O verbete passa a
registar a normalização em vez de perder o marco.

## 8. QUATRO CONFLITOS DO DESPACHO — submetidos a despacho, não executados

### (a) `Citação-chave` → `Escopo e evidência` é um erro de categoria
As 105 fichas com `Citação-chave` contêm **citações**, não escopo:
`> "Os 147 seres que terminaram compondo essa espécie..."` (RC‑011),
`> "O corpo Adhyatman de um Ser é a sua Consciência Primordial..."` (RC‑013).
`Escopo e evidência` é a secção de delimitação e evidência (169 fichas).
**Alvo coerente: `Citações-chave`** (652 fichas, emitida pelo *driver*).
Suspeita de gralha no despacho: `Citação-chave` e `Citações-chave` diferem
apenas pelo número.

### (b) A ordem canónica omite `Fontes` e `Citações-chave`
A lista de 7 posições do despacho não inclui duas das sete secções que o
*driver* emite, e que estão presentes em 746 e 652 fichas respectivamente.
Sem as suas posições, a tranche 4 não pode ser executada.

| secção | fichas | emitida pelo driver | posição no despacho |
|---|---|---|---|
| `Fontes` | 746 | **sim** | **ausente** |
| `Citações-chave` | 652 | **sim** | **ausente** |

### (c) Grafia diverge do *driver* → refragmentaria
| forma do despacho | existe na Base | forma do driver/legado | fichas |
|---|---|---|---|
| `Contexto e Origem` | **0** | `Contexto / Origem` | 665 |
| `Etimologia e Grafias` | 0 | `Etimologia / Grafias` | 402 |

`Etimologia e Grafias` foi adoptada (o *driver* não a emite, logo não há
divergência). `Contexto e Origem` **não foi aplicada**: as 147 fichas com
lote continuariam a emitir `Contexto / Origem`, pelo que renomear as 673
legadas **aumentaria** a fragmentação — o oposto do objectivo da A4.

### (d) `Seres Associados` → `Termos Relacionados`: 393 fusões, todas com movimento
As 322 ocorrências de `Seres Associados` colidem **em 393 de 393 fichas**
(todas já têm `Termos Relacionados`), e o conteúdo é uma lista de seres com
código — `Yel Luzbel (RC-078); Len Mion (RC-074); Família Yel (RC-136)…`.
A fusão é defensável (seres associados são termos relacionados), mas apaga a
distinção seres/conceitos e constitui a maior operação com movimento de
conteúdo de toda a A4. Aguarda confirmação.

## 9. Estado de A4 após a U88

| tranche | assinaturas |
|---|---|
| partida | 471 |
| 1 · Ampliação/Atualização/Reforço → H2 + H3 (**U87**) | 188 |
| 2 · variantes gráficas, parte sem conflito (**U88**) | **178** |
| 2b · `Citação-chave` e `Seres Associados` | bloqueada por (a) e (d) |
| 3 · 76 títulos residuais (577 ocorrências) | bloqueada por (b) |
| 4 · unificação da ORDEM | bloqueada por (b) |

---

## 10. Tranches 3 e 4 — EXECUTADAS na U89 (com um conflito novo e bloqueante)

Despacho da U89 resolve os conflitos: (a) `Citação-chave` → **`Citações-chave`**
· (c) grafia do *driver* (`Contexto / Origem`) · (d) `Seres Associados` mantida
como **secção canónica separada** · (b) ordem mestre de 10 posições.

### 10.1 Tranche 3 — variantes inequívocas
`Citação-chave` e `Citações-chave (RC)` → `Citações-chave` (108) ·
`Observações Científicas*` → `Observações` (10) · `Glossário interno / …` →
`Glossário interno` (9). **128 renomeações · 66 fusões.**
Ficaram de fora, por serem dispositivos editoriais próprios e não variantes:
`Observações sobre o Estado da Malha` (60) · `Estrutura interna` (26) ·
`Cautela editorial` (10) · `Quarentena Terminológica` (10) ·
`6. Histórico Curatorial e Auditoria` (6) e 65 títulos com ≤3 ocorrências.

### 10.2 CONFLITO NOVO (e) — a ordem mestre contradiz a ordem do *driver*
A ordem mestre diverge da que o *driver* emite em **6 das 7 secções** comuns:

| secção | posição no driver | posição na ordem mestre |
|---|---|---|
| `Contexto / Origem` | 1 | 3 |
| `Escopo e evidência` | 2 | 1 |
| `Termos Relacionados` | 3 | 8 |
| `Fontes` | 4 | 10 |
| `Citações-chave` | 5 | 4 |
| `Observações` | 6 | 9 |

**Prova empírica:** a RC‑022 (ficha com lote) foi reordenada pela ordem mestre
numa cópia do repositório; ao correr `materializar_lote.py --sobrescrever`, o
*driver* **regenerou-a** — a idempotência perde-se. Reordenar as 147 fichas
com lote significaria reescrevê-las a cada execução, para sempre.

**Decisão tomada:** a tranche 4 foi aplicada **apenas às 673 fichas sem lote**
(637 efectivamente reordenadas). As 147 com lote conservam a ordem do
*driver*. Submete-se ao Curador: a unificação plena exige alterar a ordem
emitida pelo *driver* (com regeneração das 147), ou aceitar a dualidade.

### 10.3 Tranche 4 — ordenação
Ordem mestre aplicada com ordenação **estável**; as secções fora do
vocabulário canónico vão para o fim, conservando a ordem relativa que tinham
(196 secções). Nenhuma linha de corpo foi alterada: conferido secção a
secção contra o HEAD, **0 fichas com conteúdo alterado**.

### 10.4 Estado de A4 após a U89

| tranche | assinaturas |
|---|---|
| partida | 471 |
| 1 · Ampliação/Atualização/Reforço → H2 + H3 (U87) | 188 |
| 2 · variantes gráficas sem conflito (U88) | 178 |
| 3 + 4 · residuais e ordenação (U89) | **150** |

| pendente | |
|---|---|
| 147 fichas com lote | bloqueadas pelo conflito (e) — exigem decisão sobre o *driver* |
| 70 títulos / 196 ocorrências fora do vocabulário | dispositivos editoriais próprios; mantidos por decisão editorial |
| 122 secções duplicadas pré-existentes | fora do escopo; intactas |

---

## 11. Tranches 3b e 4b — EXECUTADAS na U90 (unificação concluída)

**Decisões do Curador:** (e-1) **adoptar a ordem do *driver* como ordem
mestre** — unificação total sem tocar no código; (e-2) os 70 títulos
editoriais **descem a H3 sob a secção-mãe**, sem perder o rótulo.

### 11.1 Nova ordem mestre (a do driver, mais as 5 secções extra)

1. `Definição Sintética` · 2. `Etimologia e Grafias` · 3. `Contexto / Origem` ·
4. `Escopo e evidência` · 5. `Termos Relacionados` · 6. `Seres Associados` ·
7. `Fontes` · 8. `Citações-chave` · 9. `Ampliação` · 10. `Atualização` ·
11. `Reforço` · 12. `Observações`

As 7 secções que o *driver* emite ocupam as posições 0, 2, 3, 4, 6, 7 e 11 —
**estritamente crescentes**, pelo que a ordem do driver fica integralmente
preservada. Consequência: as 147 fichas com lote **já estavam** nesta ordem, e
a reordenação é-lhes uma operação nula.

### 11.2 Resultado

| | |
|---|---|
| fichas afectadas | 673 (as 147 com lote intactas) |
| títulos editoriais → H3 | 191 |
| secções-mãe criadas | 103 |
| **assinaturas** | **150 → 102** |
| fichas fora da ordem mestre | **0** |
| H2 fora do vocabulário | **1** (`6. Histórico Curatorial e Auditoria`, nas 5 fichas com lote) |
| duplicados H2 | 122 (os pré-existentes, intactos) |
| conteúdo alterado | **0** |

### 11.3 Mapa editorial → secção-mãe (para auditoria)

| título editorial | ocorrências | secção-mãe |
|---|---:|---|
| Observações sobre o Estado da Malha | 60 | `Observações` |
| Estrutura interna | 26 | `Definição Sintética` |
| Cautela editorial | 10 | `Observações` |
| Quarentena Terminológica | 10 | `Observações` |
| Glossário interno | 9 | `Etimologia e Grafias` |
| 6. Histórico Curatorial e Auditoria | 6 | `Observações` |
| Interpretação secundária (ART-2026-08-18) | 3 | `Observações` |
| Remissão | 3 | `Termos Relacionados` |
| Absorções | 3 | `Etimologia e Grafias` |
| Contexto biográfico — NATIVO/EXTERNO (não é doutrina RC) | 3 | `Contexto / Origem` |
| Leitura interpretativa — [NÃO ANCORADA / QUARENTENA] | 3 | `Observações` |
| Registro histórico (título original) | 2 | `Observações` |
| Distinção Adhyagia × Adhyagya | 1 | `Definição Sintética` |
| Colecionar Incertezas | 1 | `Contexto / Origem` |
| As 10 Eras | 1 | `Definição Sintética` |
| Absorção de RC-449 — F045 · 07/09/2026 | 1 | `Etimologia e Grafias` |
| Ressalva reflexiva (registrada em 2026-08-17, a pedido do curador) | 1 | `Observações` |
| Higiene ontológica — P2024-11-30 e eBook de IA | 1 | `Observações` |
| Absorção de RC-203 (F045 · 07/09/2026) | 1 | `Etimologia e Grafias` |
| Colecionar Incertezas — "quachadas/quechada" = Keshava? (pista do curador, 2026-08-18) | 1 | `Observações` |
| Distinção ratificada — P2025-03-15 | 1 | `Definição Sintética` |
| Divergência preservada — P2025-03-15 | 1 | `Observações` |
| Correção canônica — Devolutiva-01 / P2026-07-30 | 1 | `Observações` |
| Grande Hub de Moros — P2024-11-30 | 1 | `Contexto / Origem` |
| Súdices — F032 aplicação (05/09/2026, C-ii) | 1 | `Contexto / Origem` |
| Observação do curador — HIPÓTESE DE LEITURA (2026-08-18) | 1 | `Observações` |
| Absorção de RC-872 — F045 · 10/09/2026 | 1 | `Etimologia e Grafias` |
| Fusão WD → Wyrd (decisão do curador, 2026-08-18) | 1 | `Observações` |
| Subtermos absorvidos | 1 | `Etimologia e Grafias` |
| Eventos e atuações atribuídos | 1 | `Contexto / Origem` |
| Kadru na Terra | 1 | `Contexto / Origem` |
| Itens travados em revisão | 1 | `Observações` |
| Distinção Ontológica | 1 | `Definição Sintética` |
| Validação da Grafia Canônica | 1 | `Etimologia e Grafias` |
| Satchidananda | 1 | `Contexto / Origem` |
| Conselho das Nagas | 1 | `Contexto / Origem` |
| Estrutura interna absorvida | 1 | `Definição Sintética` |
| Samskaras e Vasanas | 1 | `Contexto / Origem` |
| Satyagraha e Abhaya | 1 | `Contexto / Origem` |
| Processo descrito | 1 | `Contexto / Origem` |
| Absorção | 1 | `Etimologia e Grafias` |
| Ressalva Científica | 1 | `Observações` |
| Distinções internas | 1 | `Definição Sintética` |
| Escopo rigoroso | 1 | `Definição Sintética` |
| Ressalva Biomédica | 1 | `Observações` |
| Estrutura | 1 | `Definição Sintética` |
| Escalas descritas | 1 | `Contexto / Origem` |
| Fixação da sigla | 1 | `Definição Sintética` |
| Ressalva de escopo | 1 | `Observações` |
| Primeiro caso descrito | 1 | `Contexto / Origem` |
| Risco de Krishna | 1 | `Observações` |
| Sequência apresentada | 1 | `Contexto / Origem` |
| As três faíscas | 1 | `Definição Sintética` |
| Formulação oral absorvida | 1 | `Definição Sintética` |
| Selo temporal — P2025-07-18 — divergência Pandora / Eva–Adão | 1 | `Observações` |
| Origem da imagem | 1 | `Contexto / Origem` |
| Instâncias internas de glossário | 1 | `Etimologia e Grafias` |
| Escopo autorizado | 1 | `Definição Sintética` |
| Exclusão clínica vinculante | 1 | `Observações` |
| Qualificadores internos absorvidos | 1 | `Etimologia e Grafias` |
| Elementos preservados | 1 | `Definição Sintética` |
| Pontos não harmonizados | 1 | `Observações` |
| Princípios | 1 | `Definição Sintética` |
| Variante e escopo | 1 | `Definição Sintética` |
| Limites obrigatórios | 1 | `Observações` |
| As cinco lentes (estrutura interna) | 1 | `Definição Sintética` |
| Estrutura interna (as "badaladas") | 1 | `Definição Sintética` |
| Estrutura interna (3 elementos definidores) | 1 | `Definição Sintética` |
| Absorção de RC-936 — F045 · 07/09/2026 | 1 | `Etimologia e Grafias` |
| Grafias (decisão canônica 03/09/2026) | 1 | `Etimologia e Grafias` |

Distribuição: {'Observações': 110, 'Definição Sintética': 44, 'Contexto / Origem': 17, 'Termos Relacionados': 3, 'Etimologia e Grafias': 22}

### 11.4 Salvaguardas — três erros meus, todos apanhados pelos testes
1. Fundir duplicados **pré-existentes** (as duas `## Fontes` da RC‑089) →
   tabelas de 5 e 4 colunas concatenadas; o **T7** detectou 17 fichas.
2. Asserção mal formulada («nenhuma secção nova») disparou na RC‑010, que
   ganha uma `Observações` legítima (0 → 1). Corrigida para «nenhum
   **duplicado** novo».
3. Um editorial pode criar a secção-mãe **antes** de a ficha ter a sua
   própria; a secção real funde-se então no *placeholder*, mas nunca num
   duplicado pré-existente.

### 11.5 Estado final de A4

`471 → 188 (U87) → 178 (U88) → 150 (U89) → 102 (U90)`

A4 está **ENCERRADA** no seu objecto taxonómico: vocabulário canónico de 12
títulos, ordem mestre única, zero fichas fora dela. Permanece apenas
`6. Histórico Curatorial e Auditoria` (5 fichas com lote), que depende de
decisão sobre o *driver*.

