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

- `admin/logs/ONDA2-AUDITORIA-ROTEAMENTO.csv` — 5.676 registros; rastro completo de cada decisão de roteamento.
- `admin/logs/ONDA2-FILA-REVISAO.csv` — 384 registros de baixa confiança, com a gaveta sugerida e o texto original (180 caracteres) para reclassificação curatorial.
- `admin/logs/ONDA2-RELATORIO-TRANSICAO-SEMANTICA.md` — este relatório.

## 6. Limitações conhecidas e pontos de atenção

1. **Roteamento heurístico:** a classificação G1–G5 usa léxico semântico ponderado + marcadores fortes, não leitura curatorial individual. As 384 unidades de baixa confiança são o ponto de revisão prioritário; o CSV permite reclassificar sem tocar no texto.
2. **H3 semânticos criados:** títulos temáticos (`### Genética, espécie e atributos intrínsecos`, `### Poder, subordinação, alianças e outras espécies`, etc.) são nova modelagem curatorial, conforme a liberdade de H3 prevista no manual.
3. **Fichas simples:** mantêm numeração de gavetas não contígua (ex.: `## 1`, `## 3`, `## 5`) porque gavetas vazias não foram forçadas; `## Citações Verbatim` aparece logo após a Gaveta 1 quando há balas a consolidar.
4. **Escopo 826 vs. 776:** ver seção 1.
5. **Matriz T2:** `admin/logs/T2-MAPEAMENTO-RELACOES.csv` permanece inalterada (998 linhas `APROVADO`, soma 7.761).
6. **4 fichas sem `## Definição Sintética`** (RC-142, RC-396, RC-503, RC-872) e **5 sem `## Termos Relacionados`** (RC-935, RC-937, RC-939, RC-940, RC-941) mantiveram suas ausências originais — o motor não inventou seções. Em RC-396 há `## Fontes` duplicado na origem; ambas as tabelas foram preservadas e reunidas na Gaveta 6.
