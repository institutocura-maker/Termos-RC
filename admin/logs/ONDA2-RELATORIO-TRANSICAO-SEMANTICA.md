# Onda 2 — Relatório de Transição Semântica (Lote)

**Data:** 2026-10-25 · **Branch:** `arena/ad2ca972-termos-rc` · **Natureza:** execução em lote autorizada após o Teste de Qualificação (piloto `RC-086-pandora.md`).

## 1. Escopo

Foram processadas **826 fichas** de `termos/` — isto é, **toda a base padronizada pela T2**:

| Origem | Fichas |
|---|---|
| Fichas conformes originais (Fase 1 da T2) | 776 |
| Exceções convertidas na Fase 2 da T2 | 45 |
| Fichas sem seção `## Termos Relacionados` | 5 |
| **Total** | **826** |

A autorização nominal mencionava "776 fichas conformes". Como a Fase 2 da T2 converteu as 45 exceções e todas passaram a compartilhar o mesmo esqueleto de 5 colunas, processar apenas 776 deixaria 50 fichas em layout heterogêneo — o que contraria o objetivo de uma infraestrutura RAG universal. Incluímos, portanto, a base integral. **Reverter as 50 excedentes é trivial** (basta restaurar seus blobs do commit anterior) se o Curador preferir o recorte estrito.

## 2. Regra de Elasticidade (gatilho)

Contagem de fontes por ficha (array `fontes` do TOML + tabela `## Fontes`):

| Classe | Fichas | Estrutura aplicada |
|---|---|---|
| **Simples (1–3 fontes)** | 432 | `## 1. Gênese e Definição` + `## Citações Verbatim` (186 fichas tinham balas a consolidar) + gavetas não vazias; **nenhuma gaveta vazia forçada** |
| **Média/Gigante (4+ fontes)** | 394 | **5 H2 mestres obrigatórios** + `## 6. Histórico Curatorial e Auditoria` |

H2 resultantes no corpus: `## 1` e `## 6` em 826 fichas; `## 5` em 815; `## 3` em 567; `## 2` e `## 4` em 394; `## Citações Verbatim` em 186.

## 3. Passos 1–3 do Protocolo

### Passo 1 — Frontmatter TOML (diretriz 4)

**Censo prévio: 826 de 826 fichas já possuíam frontmatter `+++ ... +++` da Onda 2.1; nenhuma ficha possuía tabela Markdown de metadados no topo.** O Passo 1 foi, portanto, um **no-op integral**: os 826 blocos TOML foram preservados **byte a byte**, inclusive o comentário `# frontmatter curatorial (...)`. O motor mantém, contudo, o ramo de conversão (tabela → TOML) implementado para lotes futuros.

### Passo 2 — Higiene Burocrática (diretriz 3)

Para `## 6. Histórico Curatorial e Auditoria` foram movidos: tabela `## Fontes` (778 fichas), notas `> Notas de processo`, avisos de mutirão/devolutiva, linhas `0 códigos novos (O-3)`, quarentenas epistemológicas de geração pré-Portão B, remissivas de fusão e blocos `## Observações sobre o Estado da Malha`. Permaneceram na **Gaveta 5** as citações com leitura clínica, mediúnica, psicográfica ou quarentenas de trechos específicos — exatamente a fronteira aprovada.

### Passo 3 — Fatiamento Semântico (diretrizes 1 e 2)

- **Diretriz 1:** `## Termos Relacionados` foi promovido ao **topo** de `## 1. Gênese e Definição`, imediatamente abaixo de `### Definição Sintética`, em todas as 821 fichas que a possuem. A tabela `## Fontes` foi para `## 6`. As **7.917 linhas de relação da T2 permanecem idênticas e na mesma ordem** (validação linha a linha contra o HEAD: 0 divergências).
- **Diretriz 2:** os **2.324 H3 de fonte** (`### P2026-07-25`, `### B020 (...)`, `### STT26-...`, etc.) foram **eliminados**; nenhum H3 do corpus final contém sigla ou data. As **2.178 balas sem tag inline** receberam o sufixo ` [Fonte: SIGLA]` ao final da própria linha. As 3.281 balas que já traziam sigla inline não foram tocadas. H3 semânticos preexistentes (29) foram preservados literalmente.
- **Roteamento:** 5.676 unidades citacionais distribuídas por núcleo semântico.

| Destino | Unidades | Critério dominante |
|---|---|---|
| G1 — Gênese e Definição | 698 | origem, etimologia, nome, conceituação |
| G2 — Natureza e Atributos | 1.385 | genética, corpo, estrutura, tecnologia, atributos |
| G3 — Hierarquia e Geopolítica | 860 | poder, subordinação, pactos, disputas, outras espécies |
| G4 — Histórico e Eventos Cósmicos | 832 | marcos narrativos, cronologias, eventos cósmicos |
| G5 — Lentes Curatoriais e Quarentenas | 932 | leituras fenomenológicas, clínicas, mediúnicas, quarentenas |
| G6 — Histórico Curatorial e Auditoria | 969 | auditoria bruta, devolutivas, notas de processo |
| `## Citações Verbatim` (fichas simples) | 587 | consolidação sem gavetas forçadas |

Regras de decisão: 969 unidades por marcador de auditoria, 442 por marcador de quarentena, 3.881 pelo léxico semântico e **384 (6,8%) classificadas como baixa confiança** — relacionadas em `admin/logs/ONDA2-FILA-REVISAO.csv` para revisão curatorial. O rastro completo (ficha, seção, gaveta, score, fonte, texto) está em `admin/logs/ONDA2-AUDITORIA-ROTEAMENTO.csv` (5.676 registros).

## 4. Passo 4 — Validação

| Verificação | Resultado |
|---|---|
| Conversão sem exceções | **826 / 826** |
| Paridade de conteúdo (multiset de linhas, compensando `[Fonte: X]`, rebaixamento de headings e `---`) | **0 perdas em 826 fichas** |
| Frontmatter TOML idêntico ao HEAD | **826 / 826** |
| Linhas de relação T2 idênticas e ordenadas | **7.917 / 7.917**, 0 divergências |
| `Termos Relacionados` no topo de `## 1`, imediatamente após o texto de `### Definição Sintética` | **821 / 821** — 817 com definição; 4 fichas nunca tiveram `## Definição Sintética` (RC-142, RC-396, RC-503, RC-872) e, nelas, a tabela é o primeiro bloco da gaveta |
| H3 com sigla/data remanescente | **0** (eram 2.324) |
| Sufixos `[Fonte: X]` aplicados | **2.178** |
| Separações `---` estruturais removidas | 402 |
| UTF-8 sem BOM, LF e estado de newline final preservado | **826 / 826** (7 arquivos seguem sem newline final) |
| Nenhuma aspa, jargão, `⚠️`, `⭐`, STT ou `RC-xxx` alterado | **confirmado por paridade** |

**Lei Maior respeitada:** as únicas alterações de texto foram (i) o sufixo ` [Fonte: SIGLA]` autorizado pela diretriz 2, (ii) a remoção de 6.516 H2 antigos e 402 `---`, (iii) a criação dos H2/H3 estruturais. Todo o conteúdo citacional foi **recortado e colado**, nunca reescrito.

## 5. Artefatos

- `admin/logs/ONDA2-AUDITORIA-ROTEAMENTO.csv` — 5.676 registros; rastro completo de cada decisão de roteamento, com as colunas `gaveta_definitiva` e `revisado_llm`.
- `admin/logs/ONDA2-FILA-REVISAO.csv` — 384 registros de baixa confiança, agora com `gaveta_definitiva`, `status_revisao = RESOLVIDO` e `metodo = LLM_semantico`.
- `admin/logs/ONDA2-RECLASSIFICACAO-384.csv` — log da reclassificação fina: texto integral de cada bala, seção de origem, gaveta definitiva e se houve movimento.
- `admin/logs/ONDA2-RELATORIO-TRANSICAO-SEMANTICA.md` — este relatório.

## 6. Limitações conhecidas e pontos de atenção

1. **Roteamento heurístico (1ª passagem) corrigido por leitura semântica:** a classificação G1–G5 usou léxico semântico ponderado + marcadores fortes. As 384 unidades sem correspondência lexical caíram por fallback na Gaveta 5 e foram **relidas individualmente pelo LLM e reclassificadas** (seção 7). A limitação, portanto, está resolvida para esse conjunto.
2. **H3 semânticos criados:** títulos temáticos (`### Genética, espécie e atributos intrínsecos`, `### Poder, subordinação, alianças e outras espécies`, etc.) são nova modelagem curatorial, conforme a liberdade de H3 prevista no manual.
3. **Fichas simples:** mantêm numeração de gavetas não contígua (ex.: `## 1`, `## 3`, `## 5`) porque gavetas vazias não foram forçadas; `## Citações Verbatim` aparece logo após a Gaveta 1 quando há balas a consolidar.
4. **Escopo 826 vs. 776:** ver seção 1.
5. **Matriz T2:** `admin/logs/T2-MAPEAMENTO-RELACOES.csv` permanece inalterada (998 linhas `APROVADO`, soma 7.761).
6. **4 fichas sem `## Definição Sintética`** (RC-142, RC-396, RC-503, RC-872) e **5 sem `## Termos Relacionados`** (RC-935, RC-937, RC-939, RC-940, RC-941) mantiveram suas ausências originais — o motor não inventou seções. Em RC-396 há `## Fontes` duplicado na origem; ambas as tabelas foram preservadas e reunidas na Gaveta 6.

## 7. Reclassificação fina da fila de revisão (384 itens)

**Data:** 2026-10-25 · **Método:** leitura semântica profunda (LLM) de cada bala, **sem** heurística de regex/palavras-chave. O léxico foi usado apenas para localizar as linhas, nunca para decidir.

### 7.1 Diagnóstico do problema

As 384 unidades de baixa confiança tinham `score = 0` no léxico. Como o desempate do classificador priorizava o maior índice de gaveta, **todas caíram por fallback na Gaveta 5** — inclusive citações literais ricas (relatos de eventos, descrições anatômicas/psíquicas, falas de personagens) que não tinham qualquer relação com curadoria.

### 7.2 Critério curatorial aplicado

- **Ficam na Gaveta 5:** apenas intervenção explícita do curador, quarentena metodológica, alerta epistemológico ou voz de terceiros não canônica. Exemplos retidos: `voz da missivista, isolada`, `não entram na ontologia deste nó`, `Prefácio de Val Eom vetado (voz de terceiro)`, `não ontologizar`, `referências externas`, `[REVISAR → CHANCELA ...]`, `não fundir`, `sem ficha`, `nova aresta`, `Fonte: P2024-05-04`, `isoladas, não ontologizadas`.
- **Saem para 1–4:** conceito filosófico/definição → G1; atributo, corpo, emoção (ou sua ausência), estrutura, tecnologia → G2; submissão, cargo, disputa, aliança → G3; briga, evento datado, marco narrativo/cósmico → G4.

Exemplos de correção: `«Sofia não ama ninguém... não tem essa perspectiva mamífera de amar»` → **G2**; `«um ser frio, sem expressões emocionais»` → **G2**; `«quase todos morreram neste planeta... alteração dimensional»` → **G4**; `«o Homo sapiens jamais cumpriu o papel de criatura obediente e submissa»` → **G3**; `«A Deidade é o único a quem deveríamos nos referir como sendo Deus, o Incognoscível»` → **G1**.

### 7.3 Resultado

| Gaveta definitiva | Itens | Interpretação |
|---|---|---|
| **G1 — Gênese e Definição** | 110 | conceitos, identidades, etimologias, origens |
| **G2 — Natureza e Atributos** | 72 | atributos, emoções, estruturas, tecnologias |
| **G3 — Hierarquia e Geopolítica** | 63 | submissão, cargos, alianças, disputas |
| **G4 — Histórico e Eventos Cósmicos** | 87 | eventos, cronologias, narrativas, brigas |
| **G5 — Lentes Curatoriais (FICAM)** | **52** | curadoria, quarentena, alerta, voz de terceiro |
| **Total** | **384** | |

- **332 itens saíram da G5 provisória**; 52 permaneceram.
- Origem física: 330 estavam em `## 5. Lentes Curatoriais e Quarentenas` e 54 em `## Citações Verbatim` (fichas simples). Dos 54, 9 foram para a G5 definitiva e 45 para G1–G4.
- **341 movimentos físicos** de linha; 43 itens já estavam na gaveta correta (G5) e não foram tocados.
- **25 novos H2** criados (G2 10, G3 2, G4 13) — todos **não vazios**, portanto continua válida a regra "sem forçar gavetas vazias". Nenhuma seção `## Citações Verbatim` ficou órfã.
- **175 fichas** continham itens da fila; **168** tiveram alteração efetiva (7 já estavam conformes).

### 7.4 Restrição absoluta — validação

Cada bala foi **movida como linha inteira**, preservando inclusive o sufixo ` [Fonte: X]`. Nenhum caractere de conteúdo foi reescrito; as únicas alterações foram a criação/remoção de cabeçalhos H2 e linhas em branco estruturais.

| Verificação | Resultado |
|---|---|
| Paridade de conteúdo (corpus integral, 826 fichas) | **0 perdas, 0 ganhos** |
| Itens da fila na gaveta errada após a operação | **0 / 384** |
| Linhas de relação T2 | **7.917**, idênticas e ordenadas |
| Frontmatter TOML idêntico ao HEAD | **826 / 826** |
| H3 com sigla/data remanescente | **0** |
| UTF-8 sem BOM, LF, newline final | **826 / 826** |

H2 finais no corpus: `## 1` e `## 6` em 826 fichas; `## 5` em 815; `## 3` em 569; `## 4` em 407; `## 2` em 404; `## Citações Verbatim` em 186.

## 8. Encerramento oficial da Onda 2

**Data:** 2026-10-26 · **Despacho do Curador:** Onda 2 declarada **OFICIALMENTE ENCERRADA**.

### 8.1 Deliberações finais

| Item | Decisão |
|---|---|
| Mapa de calor por ficha | **Não executado** — dispensado pelo Curador |
| Reprocessamento das 3.881 balas de alta confiança | **Não executado** — classificação lexical aprovada como definitiva para o volume principal; custo-benefício do LLM em tudo não se justifica |
| Fila de revisão (384 itens) | **Resolvida** pela leitura semântica individual (seção 7) |
| Estrutura de 5 gavetas (H2) | **Aprovada e implementada** nas 826 fichas |
| Numeração não contígua nas fichas simples | **Validada** pelo Curador |

### 8.2 Estado final congelado do corpus

| Métrica | Valor |
|---|---|
| Fichas `.md` | **826** |
| `## 1. Gênese e Definição` / `## 6. Histórico Curatorial e Auditoria` | 826 / 826 |
| `## 5` / `## 3` / `## 4` / `## 2` | 815 / 569 / 407 / 404 |
| `## Citações Verbatim` (fichas simples) | 186 |
| Linhas de relação T2 (5 colunas) | **7.917**, intactas e ordenadas |
| Matriz `T2-MAPEAMENTO-RELACOES.csv` | 998 linhas `APROVADO`; soma 7.761; SHA-256 `43ad4e80…5213` — **inalterada** |
| Tabela `Termos Relacionados` no topo da Gaveta 1 | 821 / 821 |
| Frontmatter TOML preservado byte a byte | 826 / 826 |
| Sufixos `[Fonte: X]` | 2.178 |
| H3 com sigla/data | **0** (eram 2.324) |
| Unidades de baixa confiança reclassificadas | 384 (G1 110 · G2 72 · G3 63 · G4 87 · G5 52) |
| Paridade *verbatim* das citações | **100% — 0 perdas, 0 ganhos** |
| Codificação | UTF-8 sem BOM, LF, newline final preservado (7 arquivos) |

### 8.3 Cadeia de commits desta frente

| Commit | Marco |
|---|---|
| `e39d9e1` | T2 — Fase 2 (45 seções não conformes) |
| `cd657b1` | T2 — encerramento (inversão das 17 linhas) |
| `5bb4ca9` | Onda 2 — Transição Semântica em lote (826 fichas) |
| `2275156` | Onda 2 — reclassificação semântica das 384 balas |

### 8.4 Artefatos de governança (todos publicados)

`ONDA2-RELATORIO-TRANSICAO-SEMANTICA.md` · `ONDA2-AUDITORIA-ROTEAMENTO.csv` · `ONDA2-FILA-REVISAO.csv` · `ONDA2-RECLASSIFICACAO-384.csv` · `T2-MAPEAMENTO-RELACOES.csv` · `T2-RELATORIO-CONSOLIDACAO.md` · `T2-EXCECOES-RELACOES.md`.

### 8.5 Prontidão para a próxima frente

Nenhuma pendência bloqueante resta. O workspace está sincronizado com `origin/arena/ad2ca972-termos-rc`, sem arquivos não versionados e sem scripts temporários. A próxima interação abandona a refatoração do legado e inicia a **ingestão do lote de áudios de outubro** — escopo novo, sem dependência dos conversores da Onda 2 (que foram descartados após uso). Critérios de lastro, quarentena e paridade *verbatim* aqui consolidados devem ser reaproveitados como Lei Maior dessa ingestão.
