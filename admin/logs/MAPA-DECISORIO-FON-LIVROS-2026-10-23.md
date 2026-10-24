# Mapa decisório — Fase 1C · FON-LIVROS

**Data:** 23/10/2026
**Base auditada:** commit `5a9b68b7231086d0e8dfd797c16a6167ae02e3dc`.
**Escopo:** decisão preparatória; não move, renomeia ou edita o corpus de livros.

## Método

Cada ocorrência literal de `livros/` no HEAD foi registrada com arquivo, linha, contexto, tipo, classe e decisão preliminar no CSV anexo. A classificação não substitui autorização curatorial: ela separa preservação, revisão documental e itens que exigem despacho específico.

- Ocorrências mapeadas: **380**.
- Arquivos distintos: **236**.
- Inventário: [`MAPA-DECISORIO-FON-LIVROS-2026-10-23.csv`](MAPA-DECISORIO-FON-LIVROS-2026-10-23.csv), SHA-256 `de79bcd364dfcd604615a87dc3dd16c5a6416524ce535f1418b184467591030b`.

## Decisão preliminar por classe

| Classe | Ocorrências |
|---|---:|
| documentacao_operacional | 20 |
| evidencia_consolidada | 33 |
| ficha_canonica | 1 |
| fonte_interna_selada | 159 |
| registro_consolidado | 16 |
| registro_historico_ou_de_proveniencia | 151 |

## Disposição para uma futura onda física

| Disposição | Ocorrências | Arquivos | Regra |
|---|---:|---:|---|
| AUTORIZACAO_CURATORIAL_SE_ALTERAR | 50 | 36 | Consolidado, evidência ou ficha canônica; só averbamento contextual autorizado. |
| PRESERVAR_E_CLASSIFICAR_NA_ONDA | 151 | 45 | Registro histórico/proveniência; não substituir em massa. |
| PRESERVAR_LITERAL | 159 | 147 | Fonte selada; manter blob e menções internas literalmente. |
| REVISAR_NA_ONDA_FISICA | 20 | 8 | Documentação operacional; revisar manualmente após despacho de movimento. |

## Gate de decisão

### Pronto
- Runtime: pronto. Os quatro consumidores ativos já resolvem `fonte.livros` pelo mapa central.
- Integridade: pronta. O verificador genérico valida os 577 arquivos contra a linha de base Fase 0 + a averbação documentada de `README.md`.
- Proveniência: pronta para ser conferida imediatamente antes e depois de um eventual `git mv`.

### Ainda bloqueado para movimento físico
- Não há autorização para reescrever as 159 ocorrências internas seladas.
- Há 36 arquivos em apostilas, consolidações ou fichas canônicas com referências candidatas a despacho contextual.
- Há 20 ocorrências de documentação operacional a revisar manualmente, nunca por substituição cega.

### Recomendação
Abrir uma proposta Fase 1D de movimento físico somente se o Curador autorizar simultaneamente: (a) preservar literalmente fontes seladas e relatórios; (b) tratar a averbação de `livros/README.md` como baseline aceito; e (c) receber a lista abaixo como candidatos de despacho, sem autorização implícita para todos.

## Candidatos que exigem despacho se houver necessidade de alteração

- `apostilas/CONCLUIDAS/2020-04-25_os_desdobramentos_da_rebeliao_de_lucifer/analise/RELATORIO-DE-CICLO.md`
- `apostilas/CONCLUIDAS/2020-04-25_os_desdobramentos_da_rebeliao_de_lucifer/analise/_portao_d_contadores.py`
- `apostilas/CONCLUIDAS/2020-04-25_os_desdobramentos_da_rebeliao_de_lucifer/ficha_ingresso.md`
- `apostilas/CONCLUIDAS/2021-05-15_etnias_hiperboreas_e_os_anunnakis/analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/DECISAO-DO-CURADOR.md`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/analise/RELATORIO-DE-CICLO.md`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/analise/_gerar_apostila_P2022-03-26.py`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/analise/_gerar_dossie_P2022-03-26.py`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/analise/_portao_d_contadores.py`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/apostila.md`
- `apostilas/CONCLUIDAS/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/ficha_ingresso.md`
- `apostilas/CONCLUIDAS/2023-10-14_a_esquecida_honra_dos_anunnaki/analise/_portao_d_contadores.py`
- `apostilas/CONCLUIDAS/2023-12-03_a_rebeliao_de_lucifer_ainda_por_ser_finalizada/analise/RELATORIO-DE-CICLO.md`
- `apostilas/CONCLUIDAS/2023-12-03_a_rebeliao_de_lucifer_ainda_por_ser_finalizada/analise/_gerar_apostila_P2023-12-03.py`
- `apostilas/CONCLUIDAS/2023-12-03_a_rebeliao_de_lucifer_ainda_por_ser_finalizada/analise/_portao_d_contadores_P2023-12-03.py`
- `apostilas/CONCLUIDAS/2023-12-03_a_rebeliao_de_lucifer_ainda_por_ser_finalizada/apostila.md`
- `apostilas/CONCLUIDAS/2025-06-26_estagiarios_kaos_1ed/analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`
- `apostilas/CONCLUIDAS/2025-06-26_estagiarios_kaos_1ed/apostila.md`
- `consolidacoes/AVALIACAO-PRIORIDADE-ESTEIRA-APOSTILAS-2026-09-03.md`
- `consolidacoes/F022_22-glossario/ciclo.toml`
- `consolidacoes/F022_22-glossario/cotejo.md`
- `consolidacoes/F030_colegio-druidico/DECISAO-DO-CURADOR.md`
- `consolidacoes/F030_colegio-druidico/ciclo.toml`
- `consolidacoes/F030_colegio-druidico/devolutiva.md`
- `consolidacoes/F035_fornos-replicadores-refatorado/divergencias.md`
- `consolidacoes/F035_fornos-replicadores-refatorado/mapeamento.md`
- `consolidacoes/F036_projeto-talm-livro/mapeamento.md`
- `consolidacoes/F039_mutirao-lote-3-stt-audio/DECISAO-DO-CURADOR.md`
- `consolidacoes/F039_mutirao-lote-3-stt-audio/ciclo.toml`
- `consolidacoes/F039_mutirao-lote-3-stt-audio/devolutiva.md`
- `consolidacoes/F039_mutirao-lote-3-stt-audio/mapeamento.md`
- `consolidacoes/F040_mutirao-lote-4-tensao-corpus/ciclo.toml`
- `consolidacoes/F041_mutirao-lote-5-outros/ENCERRAMENTO-DO-MUTIRAO.md`
- `consolidacoes/F041_mutirao-lote-5-outros/ciclo.toml`
- `termos/RC-002-rebeliao-de-lucifer.md`

A lista é de candidatos: referências semânticas podem permanecer como prova histórica. Qualquer averbamento futuro deverá citar arquivo, linha, justificativa e hash de prova.
