# Mapa de Dados — Base de Conhecimento e Terminológica das Revelações Cósmicas

**Levantamento:** 2026-10-26 · **Atualizado:** 2026-10-27 (achado §9.1 resolvido) · **Commit de referência:** `9c8b4d6` · **Branch:** `arena/ad2ca972-termos-rc`
**Método:** censo direto do working tree (6.065 arquivos versionados, 249,62 MB, excluindo `.git/` e `.arena/`) + leitura dos contratos de governança.
**Registro da regeneração:** `diagnostico/DIAGNOSTICO-T14-REGENERACAO-ESPELHOS-2026-10-27.md`.

> Documento de navegação. Complementa `docs/README.md` (mapa da documentação) e `APRESENTACAO-DO-SISTEMA.md` (arquitetura histórica de 11/09/2026, com rotas já migradas). Para números oficiais em vigor, ver §9 — os espelhos de estado estão defasados.

---

## 1. Visão geral em camadas

| # | Camada | Onde | Volume | Natureza |
|---|---|---|---|---|
| **L0** | Verdade-mestra (cadastro) | `ferramentas/dados_termos.py`, `base/` | 0,73 MB | Dados canônicos |
| **L1** | Conteúdo terminológico | `termos/` | 6,08 MB | **Conteúdo curatorial vivo** |
| **L2** | Espelhos de leitura | raiz (`*.md`, `.xlsx`, `.docx`) | 2,87 MB | **Gerados — não editar à mão** |
| **L3** | Fontes primárias | `fontes/` | 154,03 MB | **Intocáveis (verbatim/SHA-256)** |
| **L4** | Pipeline STT outubro | 6 diretórios `*_stt_*` | 45,26 MB | Derivados auditáveis |
| **L5** | RAG / pérolas | `rag/` | 0,40 MB | Recortes citacionais |
| **L6** | Derivados e evidência | `pedagogico/`, `ciclos/`, `consolidacoes/`, `notas/`, `diagnostico/` | 32,36 MB | Síntese e prova |
| **L7** | Governança e código | `admin/`, `chancela/`, `prompts/`, `docs/`, `ferramentas/`, `backups/`, `.arena/` | 8,04 MB | Decisões, ritos, scripts |

### Diagrama de fluxo

```
  [ Curador ] ──upload──> uploads_recepcao/          (caixa de entrada; hoje vazia)
                              │
                              ├─> fontes/livros/CONCLUIDOS/   44 obras · PDF + original.txt
                              ├─> fontes/apostilas/           82 cápsulas · 1.629 arquivos
                              └─> fontes/stt-lote-2026-10/   310 brutos STT (.md)
                                        │
                     normalizar_stt_lote_2026_10.py
                                        ↓
                          normalizados_stt_lote_2026-10/   309 derivados + 6 artefatos
                                        │
                      fase0_ingestao_stt_lote_2026_10.py
                                        ↓
                            ingestao_stt_lote_2026-10/      7 arquivos (Fase 0)
                                        │  309 registros · 11.326 sinais · 24 lotes
                      triagem_stt_lotes_2026_10.py
                                        ↓
                           triagem_stt_lote_2026-10/       24 dossiês STT26-01…24
                                        │  ⚠️ TODOS PENDENTES / AGUARDANDO DESPACHO
                            [ DESPACHO CURATORIAL ]  ←── fronteira atual
                                        ↓
                                    ciclos/            48 ciclo.toml (P*, OIDR26-*, STT26-*)
                                        │                    ↓
                                        │              rag/perolas/   299 pérolas
                                        ↓
  L0 dados_termos.py ──builds──> L2 espelhos (xlsx/docx/índices)
            │                          ↑
            └── base/canonico.json ────┘
                    946 termos · 1.887 relações · 104 obras
                            ↓
                       termos/*.md  (826 fichas · 5 gavetas H2 · 7.917 linhas de relação)
                            ↓
            pedagogico/ (659 verbetes) · notas/fichas/ (253 notas verbatim)
```

---

## 2. L0 — Verdade-mestra (cadastro canônico)

| Caminho | Conteúdo | Chave |
|---|---|---|
| `ferramentas/dados_termos.py` | **Fonte única de verdade**: 946 termos como tuplas Python `(codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha)` | 352 KB |
| `base/canonico.json` | Espelho canônico `canonico-1.1`: **946 termos + 1.887 relações**, gerado de `dados_termos.py` | 634 KB |
| `base/biblio.json` | **Bibliografia canônica**: 104 obras (códigos `B###` + especiais `ART-`/`PER-`/`EXT-`) | 99 KB |
| `INVENTARIO-APOSTILAS.json` | 81 apostilas catalogadas | 13 KB |
| `INDICE-PALESTRAS.md` (raiz) | Índice operacional das palestras | 48 KB |

**Estado real dos 946 termos** (lido de `dados_termos.py`): `572 verificado · 212 provisório · 102 em análise · 60 candidato`. **826 têm ficha (`ficha=True`); 120 não têm** — este é o *gap de fichas* histórico, censado em `diagnostico/CENSO-GAP-FICHAS-2026-09-13.*`.

> ⚠️ `dados_termos.py` é código + dados misturados, escrito por regex — a principal fragilidade arquitetural apontada em `APRESENTACAO-DO-SISTEMA.md` §9.1. Os builds leem `base/canonico.json`, mas o registro `.py` continua mestre.

---

## 3. L1 — Conteúdo terminológico (`termos/`)

- **826 fichas** `RC-001…RC-946` em Markdown (~6 MB).
- Após a Onda 2, cada ficha tem **frontmatter TOML `+++`** (comentário `# frontmatter curatorial` preservado) e o esqueleto H2 de **5 gavetas semânticas + `## 6. Histórico Curatorial e Auditoria`**:

| H2 | Fichas | Conteúdo |
|---|---:|---|
| `## 1. Gênese e Definição` | 826 | Definição sintética + **tabela `Termos Relacionados` no topo** + etimologia/contexto |
| `## 2. Natureza e Atributos` | 404 | Atributos, biologia, estruturas |
| `## 3. Hierarquia e Geopolítica` | 569 | Poder, cargos, alianças |
| `## 4. Histórico e Eventos Cósmicos` | 407 | Eventos e cronologias |
| `## 5. Lentes Curatoriais e Quarentenas` | 815 | Leituras fenomenológicas, quarentenas |
| `## 6. Histórico Curatorial e Auditoria` | 826 | Tabela `Fontes`, notas de processo, devolutivas |
| `## Citações Verbatim` | 186 | Consolidado das **fichas simples** (1–3 fontes) |

- **7.917 linhas de relação** no padrão de 5 colunas `| Termo | Código | Relação | Direção | Notas |` — intactas após T2 + Onda 2.
- **2.178 sufixos `[Fonte: SIGLA]`** e **0 H3 com sigla/data**.
- Governança da frente: `admin/logs/ONDA2-RELATORIO-TRANSICAO-SEMANTICA.md`, `ONDA2-AUDITORIA-ROTEAMENTO.csv`, `ONDA2-FILA-REVISAO.csv`, `ONDA2-RECLASSIFICACAO-384.csv`, `T2-MAPEAMENTO-RELACOES.csv` (998 linhas `APROVADO`).
- Padrões editoriais: `01-ficha-modelo.md`, `02-vocabulario-controlado.md`, `convencoes-editoriais-rc.md`.

---

## 4. L2 — Espelhos gerados (**nunca editar à mão**)

| Arquivo | Gerador | Tamanho |
|---|---|---|
| `README.md` | `ferramentas/build_readme.py` | 7 KB |
| `indice-mestre.md` | `ferramentas/build_indice.py` | 242 KB |
| `base-terminologica.xlsx` | `ferramentas/build_xlsx.py` | 311 KB |
| `base-terminologica-leitura.docx` | `ferramentas/build_word.py` | 2,11 MB |
| `GLOSSARIO-CANONICO-2026-08-31.md` | — (canônico datado) | 51 KB |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | — | 30 KB |

Rebuilds são **totais**; o portão de integridade é `ferramentas/verificar_verbetes.py` (verbatim byte a byte + existência de códigos) e `ferramentas/test_suite.py`.

---

## 5. L3 — Fontes primárias (`fontes/`, 154 MB — **zona intocável**)

| Subárvore | Conteúdo | Volume |
|---|---|---|
| `fontes/livros/CONCLUIDOS/B0NN_*/` | **44 obras** com `original.pdf` (48 PDFs, 83,7 MB no total) + `original.txt` e camadas de análise | 98 MB |
| `fontes/livros/AMOSTRAS/` | 4 amostras | 2,55 MB |
| `fontes/apostilas/<AAAA-MM-DD_slug>/` | **82 cápsulas** (81 com `original.txt`), com análise/leitura/índices | ~30 MB |
| `fontes/stt-lote-2026-10/` | **310 brutos STT** do lote de outubro (`.md`, com frontmatter/URL preservados) | 10,21 MB |
| `fontes/externas/` | Materiais de terceiros (glossário Krys Amon, Ari Barbosa) | 0,15 MB |
| `fontes/docx_originais/`, `fontes/pilotos_historicos/` | DOCX bruto e 6 pilotos históricos | 0,69 MB |
| `fontes/manifestos/MANIFESTO-FONTES-FASE-0.json` | Inventário SHA-256 de fontes e evidências (IDs estáveis, destinos propostos) | 1,12 MB |
| `fontes/README.md` | **Contrato de arquitetura de fontes** e estado da migração Fase 0 | — |

Migrações já executadas (23–24/10/2026): `FON-EXTERNAS`, `FON-LIVROS`, `FON-RECEPÇÃO` (R2/R3/R4) e `FON-APOSTILAS-CONCLUIDAS` (82 cápsulas, 1.629 arquivos). Registros em `admin/logs/RELATORIO-*FON-*`.

> ⚠️ `.gitattributes` protege CRLF e espaços finais dos derivados STT e dos `original.txt` dos ciclos — **são proveniência, não estilo**.

---

## 6. L4 — Pipeline STT do lote de outubro (a próxima frente)

| Estágio | Diretório | Arquivos | Estado |
|---|---|---:|---|
| 0. Recepção | `uploads_recepcao/` | 2 | Vazio por desenho: só `README.md` + `.gitkeep` (caixa de entrada futura) |
| 1. Bruto canônico | `fontes/stt-lote-2026-10/` | 310 | Destino imutável pós-R4 |
| 2. Normalização | `normalizados_stt_lote_2026-10/` | 315 | 309 derivados + manifestos SHA-256, `rastreio-antes-depois.jsonl`, `preservados-d3.jsonl`; **1.306 substituições auditadas** (regras STT-A/D1/D2/C01); 0 fontes alteradas |
| 3. Ingestão Fase 0 | `ingestao_stt_lote_2026-10/` | 7 | `registro-mestre.jsonl`, `mapa-linhas.jsonl`, `indice-termos-base.jsonl`, `mapa-tematico.jsonl`, `lotes-planejados.json`, `resumo-triagem.json`. **309 registros · 245:56:52 · 11.326 sinais exatos · 24 lotes · 0 mutações na Base** |
| 4. Triagem curatorial | `triagem_stt_lote_2026-10/STT26-01…24/` | 145 | 24 dossiês (DOSSIE, candidatos-cotejo, ocorrências, resumo, DESPACHO-TEMPLATE). **Todos com `resultado: PENDENTE`, `autorizacao_para_abrir_ciclo: false`** — 25 candidatos de cotejo por lote (teto) |
| 5. Ciclos do Motor | `ciclos/` | 284 | 53 pastas / 48 `ciclo.toml`. Inclui os 6 eixos `STT26-*` (já pousados) e os 4 `OIDR26-01…04` (100 pérolas aprovadas, encerrados) |
| 6. RAG | `rag/` | 328 | 299 pérolas + 29 manifestos |

**Pilotos/dry-runs preservados** (não são runtime):
- `normalizados_stt_dry_run/` — 6 cópias, só as 8 regras `AUTOMÁTICA` (52 substituições).
- `onda_incremental_dry_run/` — 62 arquivos; 6 derivados, mapeamento de eixos, triagem curatorial, `ENCERRAMENTO-CURATORIAL-ONDA-INCREMENTAL.*` (4 lotes OIDR26, 100 pérolas, 0 termos/0 relações novos).

**Ferramentas do pipeline** (em `ferramentas/`): `normalizar_stt_lote_2026_10.py`, `fase0_ingestao_stt_lote_2026_10.py` (`--buscar`, `--force`), `triagem_stt_lotes_2026_10.py` (`--proximo`), `abrir_ciclo_eixo_stt_2026_10.py`, `consolidar_despacho_eixo_stt_2026_10.py`, `auditar_onda_stt_2026_10.py`, `pousar_oidr26_0*.py`, `motor.py`.

**Fronteira atual:** `ingestao_stt_lote_2026-10/README.md` — *"Cada lote permanece em `AGUARDANDO-DESPACHO-CURATORIAL`. Somente um despacho consolidado poderá selecionar candidatos e abrir um `ciclo.toml` para o `motor.py`."*

---

## 7. L5/L6 — RAG, derivados e evidência

| Caminho | Volume | Papel |
|---|---|---|
| `rag/perolas/PER-*.md` | 299 | Pérolas com frontmatter: `id`, `ciclo`, `unidade U0004`, `chars`, `sha256_fonte`, `termo RC-###`, `status`, glosa |
| `rag/MANIFESTO-*.json` | 29 | Manifestos por ciclo/eixo |
| `pedagogico/enciclopedia/` | 660 | **659 verbetes** em `V1…V5` (V3 263 · V4 157 · V2 121 · V5 75 · V1 33) + 4 modelos + 4 da seção V.24 + índice |
| `pedagogico/top-down/`, `livro/`, raiz | 113 | 10 apostilas top-down, proposta pedagógica, making-of, livro, mapa de abstração |
| `ciclos/` | 284 | 48 `ciclo.toml` + dossiês RAG, ancorários, relatórios, `POUSO-CONFIRMADO-*`, `original.txt` selados |
| `consolidacoes/` | 110 | 20 frentes `F022…F044`, esteira de apostilas, `29-PERSONAGENS`, `TL01_lista-simples-rc` |
| `notas/fichas/RC-*.md` | 253 | **Notas de processo migradas VERBATIM** (PACTO G2.4 — não editar, não reescrever) |
| `diagnostico/` | 183 | Censos, certidões (`CERTIDAO-*`), auditorias A–E, dossiês A5/B061/U41/U42, tabela e despacho de normalização STT, `PLANO-APRIMORAMENTO-KB` |

---

## 8. L7 — Governança, decisões e código

| Caminho | Volume | Papel |
|---|---|---|
| `admin/logs/` | 66 | `STATE-MIRROR.md`, handoffs, despachos, certidões R1–R4 de fontes, relatórios das ondas T2/Onda 2 |
| `admin/documentos/` | 2 | Propostas de fase + parecer de auditoria (`.docx`) |
| `chancela/` | 31 CSV | **Trilha de decisões**: `HOLD.csv` (40 códigos bloqueados) + 15 pares `P7-*`/`*_retorno` |
| `prompts/` | 10 | Prompts completos, iniciais e de continuidade de sessão |
| `docs/` | 7 | `README.md` (regras de localização), `historico/` (4), `planos/` (2: corpus IA local, Fontes/KB Fase 0) |
| `ferramentas/` | 63 | **54 scripts `.py`** (builders, motor, validadores, pipeline STT) + `legacy/` (6) + `RITO-COMMIT.md`, `test_baseline.json` |
| `backups/` | 20 | 18 `REGISTRO-LIMPEZA-*.json` + manifesto de pacotes |
| `.arena/` | 3 | `SESSION-NOTES.md` (486 KB — diário de bordo local) + 2 verificadores. **Não é canônico e não sobrevive ao clone** |
| Raiz (políticas) | — | `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md` (vigente), `PLANO-MIGRACAO-DE-CHAT.md`, `PARECER-GLOSSARIO-KRYS-AMON-*`, `VERIFICACAO-DE-COBERTURA-*` |

**Regras de admissão** (`docs/README.md`): raiz = interfaces estáveis/canônicos/espelhos; `docs/planos/` = estratégia; `docs/historico/` = documentação datada; `diagnostico/` = auditorias e certidões; `admin/logs/` = trilha operacional. **Zonas preservadas** (não mover sem despacho): `base/`, `termos/`, `fontes/apostilas/`, `consolidacoes/`, `ciclos/` e derivados de ondas.

**Zonas planejadas, ainda sem dados** (Fase 0 — `kb/README.md`, `fontes/README.md`): `kb/base|termos|rag/`, `fontes/recepcao/`, `fontes/palestras/`, `fontes/online/youtube/`. Os manifestos `MANIFESTO-KB-FASE-0.json` (238 KB) e `MANIFESTO-FONTES-FASE-0.json` (1,12 MB) registram os hashes de pré-migração. **`kb/` não deve ser usada como caminho de runtime até despacho de migração.**

---

## 9. Achados de governança deste censo

1. ~~**Espelhos de estado defasados.**~~ **RESOLVIDO em 27/10/2026** (regeneração autorizada pelo Curador). O censo original apontava `README.md` com *820 fichas* e `STATE-MIRROR.md` com *689 fichas / 102 obras*. A causa raiz era `base/canonico.json` desatualizado em relação ao mestre: 6 flags `ficha` e 274 siglas `STT26-*`/`OIDR26-*` ausentes. A cadeia completa foi reexecutada — `exportar_json.py` → `build_readme` / `build_indice` / `build_xlsx` / `build_word` — e todos os espelhos agora leem **946 termos · 826 fichas · 1887 relações · 104 obras**. Ver `admin/logs/STATE-MIRROR.md` §8. Nenhuma ficha, fonte ou relação foi alterada.
2. **Rotas históricas em documentos antigos.** `APRESENTACAO-DO-SISTEMA.md` (11/09/2026) ainda cita `livros/CONCLUIDOS/` e `apostilas/CONCLUIDAS/`, ambas migradas para `fontes/` em 23–24/10/2026. O documento é arquitetura histórica, não mapa de runtime.
3. **Gap de fichas:** 120 termos cadastrados sem ficha (`946 − 826`). Censo detalhado em `diagnostico/CENSO-GAP-FICHAS-2026-09-13.*`.
4. **Fronteira de ingestão travada:** os 24 lotes `STT26-01…24` estão com despacho `PENDENTE`. Nenhum ciclo novo pode ser aberto sem decisão curatorial consolidada.
5. **Verdade-mestra duplicada:** `dados_termos.py` (mestre) × `base/canonico.json` (espelho) × badges nas fichas — sincronia por convenção+script, não por construção.

---

## 10. Onde procurar — guia rápido

| Pergunta | Caminho |
|---|---|
| Qual o status/categoria de um termo? | `ferramentas/dados_termos.py` · `base/canonico.json` |
| Onde está o conteúdo de um termo? | `termos/RC-NNN-*.md` (gavetas H2) |
| Onde estão as relações entre termos? | Tabela `### Termos Relacionados` dentro da ficha (7.917 linhas) · `base/canonico.json` (1.887 arestas) · `admin/logs/T2-MAPEAMENTO-RELACOES.csv` (De-Para) |
| Qual a bibliografia de uma sigla `B0NN`? | `base/biblio.json` (104 obras) |
| Onde está o PDF/TXT original de um livro? | `fontes/livros/CONCLUIDOS/B0NN_*/original.pdf|original.txt` |
| Onde está a transcrição de uma palestra? | `fontes/apostilas/<AAAA-MM-DD_slug>/original.txt` (81) · `ciclos/<sigla>/original.txt` |
| Onde está o verbatim de uma citação? | Na própria ficha (tag `[Fonte: X]`) · `rag/perolas/` (299) · `notas/fichas/` (253) |
| Onde está a decisão curatorial que autorizou X? | `chancela/` (levas P7 + HOLD) · `admin/logs/` (despachos) · `consolidacoes/F0NN/` · `diagnostico/CERTIDAO-*` |
| Qual o estado operacional entre sessões? | `admin/logs/STATE-MIRROR.md` + `README.md` (⚠️ ver §9) · `prompts/PROMPT-PROXIMA-SESSAO.md` |
| Onde estão os scripts e o rito de commit? | `ferramentas/` · `ferramentas/RITO-COMMIT.md` · `ferramentas/test_suite.py` |
| Onde está o plano de treinamento da IA local? | `docs/planos/PLANO-CORPUS-TREINAMENTO-IA-LOCAL.md` |
| Onde está a regra de quarentena entre ecossistemas? | `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md` |
| **Por onde começo o lote de áudios de outubro?** | `fontes/stt-lote-2026-10/` → `normalizados_stt_lote_2026-10/` → `ingestao_stt_lote_2026-10/` → `triagem_stt_lote_2026-10/` → (despacho) → `ciclos/` → `rag/perolas/` |

---

*Mapa gerado por censo direto em `9c8b4d6`. Nenhum arquivo de dados foi alterado para produzir este documento.*
