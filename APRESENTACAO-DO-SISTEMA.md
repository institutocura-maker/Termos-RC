# Apresentação do Sistema — Base Terminológica RC

**Documento de contexto para auditoria externa de arquitetura.**
Data: 11/09/2026 · Repositório: `institutocura-maker/Termos-RC` · Branch de trabalho: `arena/01a08907-termos-rc`
Autor do documento: agente de engenharia/curadoria (com revisão do Curador) — **não é peça de marketing**: contém as preocupações conhecidas (§9).

---

## 1. O que é este sistema

A **Base Terminológica RC** é uma base de conhecimento curada sobre a obra autoral de Rogério Ellam ("Revelação Cósmica" / RC): ~44 livros catalogados (siglas `B001`–`B089`) e ~116 palestras transcritas (siglas `PAAAA-MM-DD`, STT + revisão). Sobre esse corpus, o sistema constrói:

- um **cadastro terminológico** de 946 termos (códigos imutáveis `RC-001`…`RC-946`), com status de validação;
- **671 fichas terminológicas** em Markdown (definição, contexto, etimologia, fontes com página/capítulo, citações verbatim, relações, quarentenas editoriais);
- **~660 verbetes enciclopédicos** derivados das fichas (camada pedagógica);
- **espelhos de leitura**: planilha `.xlsx`, documento `.docx`, índice-mestre `.md` — todos **gerados**, nunca editados à mão;
- apostilas, tratados e mapas de conexões (camada de produtos).

Escala atual (11/09/2026): **946 termos · 671 fichas · 1898 relações · 102 obras** · status **60 ⚪ / 241 🟡 / 166 🟠 / 479 🟢** · repo ≈ 389 MB · 129 commits.

## 2. Como a arquitetura chegou aqui (histórico honesto)

1. **Fase chats-avulsos (até ~ago/2026):** trabalho em workspaces isolados por sessão de chat, com pacotes de migração manuais (ver `PACOTE-MIGRACAO-*.md`, `PROMPT-CONTINUIDADE-*.md`, `STATUS-HANDOFF-*.md`). Continuidade frágil.
2. **Fase GitHub (a partir de ~30/08/2026):** adoção do repositório como memória persistente. Os processos foram se adequando de forma orgânica: convenções de commit (1 commit por leva de chancela), `STATE-MIRROR.md` como resumo de estado, trilha de auditoria em `chancela/`.
3. **Fase atual:** volume grande e crescente; o Curador suspeita que decisões pragmáticas do início (sobretudo o §4) podem não ser as adequadas para o futuro. Daí esta auditoria.

## 3. Mapa do repositório

| Caminho | Conteúdo | Tamanho aprox. |
|---|---|---|
| `ferramentas/dados_termos.py` | **Tabela-mestra**: os 946 termos como tuplas Python — a "fonte única de verdade" (§4) | 336 KB · 3.178 linhas |
| `termos/RC-*.md` | 671 fichas terminológicas (conteúdo curatorial rico) | 5,3 MB |
| `livros/CONCLUIDOS/` | 44 obras-fonte processadas (`original.txt` + camadas de análise) | 98 MB |
| `apostilas/CONCLUIDAS/` | 81 palestras processadas (transcrição + camadas) | 44 MB |
| `ciclos/` | 38 ciclos de processamento de palestras (`ciclo.toml` + manifestos) | — |
| `pedagogico/enciclopedia/verbetes/` | ~660 verbetes derivados | (9 MB no `pedagogico/` total) |
| `ferramentas/build_*.py` | Geradores dos espelhos (xlsx, docx, índices) + `motor.py` (esteira de validação) + `verificar_verbetes.py` | — |
| `base-terminologica.xlsx` / `base-terminologica-leitura.docx` / `indice-mestre.md` | Espelhos gerados (leitura humana) | 292 KB / 1,7 MB / 228 KB |
| `chancela/` | 20 planilhas CSV: templates + retornos de chancela (trilha de auditoria das decisões) | — |
| `STATE-MIRROR.md` | Resumo de estado em 42 linhas (números oficiais + pendências) | — |
| `RELATORIO-BASE-TERMINOLOGICA.md` / `GLOSSARIO-CANONICO-2026-08-31.md` | Relatório analítico (672 l.) + glossário canônico (702 l.) | — |
| `01-ficha-modelo.md`, `02-vocabulario-controlado.md`, `convencoes-editoriais-rc.md` | Padrões editoriais | — |
| `uploads_recepcao/` | Caixa de entrada de arquivos do Curador (uso transitório; raiz preservada como histórico) | — |
| `backups/`, `consolidacoes/`, `materiais_externos/`, `rag/`, `diagnostico/` | Áreas auxiliares/históricas | — |
| `*.md` na raiz (~40 docs) | Despachos, diagnósticos, handoffs, planos — memória operacional acumulada | — |

## 4. O coração (e a principal preocupação): `ferramentas/dados_termos.py`

Cada termo é uma tupla:

```python
(codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha)
# status: candidato | provisório | em análise | verificado
# fontes: siglas B### (lista) · relacionados: códigos RC-### · ficha: True/False
```

- **Papel real:** funciona como **banco de dados** — todos os builds (`build_xlsx.py` ~99 KB, `build_word.py`, `build_indice.py`) e verificações o importam como verdade-mestra.
- **Como é alterado:** edições via scripts Python (regex sobre o próprio arquivo) + commits; nunca editado à mão em produção.
- **Regras declaradas no cabeçalho:** códigos imutáveis; nomes podem mudar; grafia preferida mora neste arquivo.
- **A preocupação do Curador (§9.1):** um arquivo `.py` em crescimento como BD mistura código e dados, sem schema validado, sem consultas, sem integridade referencial automática. É o ponto nº 1 da auditoria.

## 5. As fichas (`termos/RC-*.md`) — onde mora o conteúdo

Markdown padronizado (`01-ficha-modelo.md`): definição sintética, contexto/origem, etimologia/grafias, tabela de fontes (obra/capítulo/página), citações-chave **verbatim** (preservadas byte a byte, inclusive erros de STT), termos relacionados, seres associados, observações, quarentenas terminológicas (vetos de grafia/uso, ex.: "Hochmah, nunca Rockma").

Observação arquitetural: o **status existe em dois lugares** — no cadastro (`dados_termos.py`) e no badge da ficha (`| **Status** | 🟢 … |`) — sincronizados por script a cada leva.

## 6. Pipeline de builds e verificações

```
dados_termos.py + termos/*.md  →  build_xlsx.py / build_word.py / build_indice.py
                                →  .xlsx + .docx + indice-mestre.md (regenerados por inteiro)
verificar_verbetes.py           →  confere verbatim byte-a-byte + existência de códigos
```

- Rebuilds são **totais** (não incrementais) e rodam a cada leva aplicada.
- O verificador é o portão de integridade: qualquer divergência verbatim ou código inexistente falha a leva.

## 7. Processo de curadoria (como os dados evoluem)

- **Chancela por levas:** o Curador aprova conjuntos de termos por planilha CSV (`;`, UTF-8-SIG) em `chancela/`: colunas de contexto + `DECISÃO (V/X/?)`. 1 leva = 1 commit. Histórico: P6 (35 levas, 291 chancelas) + P7 em curso (10 levas, 155 chancelas).
- **Travas automáticas por leva:** sem ficha → bloqueia; `[REVISAR]` aberto → bloqueia; status-fonte ≠ 🟠 → bloqueia; auditoria spot (~5%) confere citações nas fontes.
- **Despachos curatoriais:** decisões de grafia/escopo registradas nas fichas e no relatório (ex.: renames Chiva→Shiva, Sofia→Sophia, Anunnakis→Anunnaki invariável; retenções documentadas de termos excluídos).
- **Quarentenas:** sistema de vetos editoriais entre ecossistemas (`POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`).

## 8. Pontos que consideramos saudáveis (a preservar)

1. Fonte única de verdade explícita + espelhos 100% gerados (nunca editados à mão).
2. Verificador verbatim byte-a-byte como portão de integridade.
3. Trilha de auditoria completa das decisões (CSVs + 1 commit por leva + notas nas fichas).
4. Códigos imutáveis; grafias canônicas versionadas.
5. Separação conteúdo-fonte (livros/apostilas, intocáveis) × conteúdo derivado (fichas/verbetes/produtos).

## 9. Preocupações conhecidas (para o auditor investigar — sem ordem de prioridade)

1. **`dados_termos.py` como banco de dados:** mistura código+dados; sem schema/migração/validação de tipos; escrita por regex; risco de corrupção silenciosa; consultas só via Python ad-hoc. Pergunta central: migrar para SQLite/JSON-schema/ORM? Com que estratégia de transição sem quebrar os builds?
2. **Duplicação de status** cadastro↔ficha (§5): sincronia por convenção+script, não por construção.
3. **Rebuilds totais** a cada leva: tempo e risco crescem com a base (hoje ~1 min; e com 3.000 termos?).
4. **Binários versionados:** `.xlsx`/`.docx` (até 1,7 MB) commitados a cada leva — inchaço do histórico git.
5. **Raiz com ~40 documentos** acumulados: memória valiosa, mas sem índice curatorial claro (há `INDICE-ARQUIVOS-RAIZ-2026-08-31.md`, possivelmente desatualizado).
6. **Scripts legados** `_*.py` em `ferramentas/` (uso único, históricos): manter, arquivar ou remover?
7. **Ausência de testes automatizados:** a validação é o verificador + asserts em scripts avulsos; sem suite de regressão.
8. **`backups/` e áreas históricas:** política de retenção indefinida.
9. **STT como fonte primária** de muitas fichas: convenção "verbatim preservado" é proposital, mas o auditor deve opinar se o lastro é suficiente.
10. **Acoplamento dos builds ao formato interno** das fichas (parsing de Markdown por regex): fragilidade diante de variações editoriais.

## 10. Escopo pedido ao auditor

- **Auditar:** arquitetura de dados e de código (§4–§7), riscos de integridade/escala, priorização das recomendações (quick wins × reformas estruturais), com atenção especial ao §9.1.
- **Não auditar:** conteúdo doutrinário/religioso (a curadoria de mérito é do Curador); ortografia das fichas; escolhas editoriais já despachadas.
- **Entregável esperado:** parecer escrito com achados (fortes a preservar + frágeis a corrigir), riscos ordenados por severidade e roteiro de migração faseado, se aplicável.

## 11. Roteiro de leitura sugerido (2–3 horas)

1. Este documento → 2. `STATE-MIRROR.md` → 3. cabeçalho + 20 linhas de `ferramentas/dados_termos.py` → 4. uma ficha exemplar (`termos/RC-565-*.md`, `termos/RC-024-*.md`) → 5. `ferramentas/build_xlsx.py` (skim) + `verificar_verbetes.py` (íntegra, 3,8 KB) → 6. `chancela/P7-8.2-hebraico_retorno.csv` (exemplo de decisão) → 7. `RELATORIO-BASE-TERMINOLOGICA.md` (skim) → 8. `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`.

---

*Dúvidas de contexto histórico podem ser dirigidas ao agente de engenharia via Curador. Bom trabalho — e seja bem-vindo à Arca.* 🛶
