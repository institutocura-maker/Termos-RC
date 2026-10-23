# Auditoria e preparação — FON-RECEPÇÃO

**Data:** 23/10/2026
**Base auditada:** `2b20694c40904e097c433a4f05fb60dab90b15d0`
**Estado:** preparação sem movimento físico; a rota de runtime continua `uploads_recepcao/`.

## Linha de base

| Campo | Valor |
|---|---|
| Arquivos | 330 |
| Bytes | 10982198 |
| SHA-256 agregado Fase 0 | `a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b` |
| Rota atual | `uploads_recepcao/` |
| Destino apenas planejado | `fontes/recepcao/` |

O verificador genérico confirmou a coleção integralmente contra a Fase 0.

## Mapa de referências

- Busca literal por `uploads_recepcao`: **1225** ocorrências em **350 arquivos**.
- Inventário por linha: [`MAPA-PREPARACAO-FON-RECEPCAO-2026-10-23.csv`](MAPA-PREPARACAO-FON-RECEPCAO-2026-10-23.csv), SHA-256 `c910388ed271e48dda631751f279d5f58dcfe362f04ebc7f972e3991989f8075`.

| Classe | Ocorrências |
|---|---:|
| artefato_derivado_de_ingestao | 327 |
| consumidor_python_ativo | 29 |
| documentacao_ou_outro | 6 |
| evidencia_ou_fonte_selada | 362 |
| infraestrutura_de_mapa | 1 |
| proveniência_em_executor_ativo | 5 |
| recepcao_interna | 28 |
| registro_ou_documentacao | 455 |
| script_historico_ou_selado | 12 |

## Consumidores executáveis a preparar antes de qualquer mudança de rota

**Leitura direta / diagnóstico da caixa de entrada (5):**
- `diagnostico/medir_processo.py`
- `ferramentas/aplicar_decisao_curador_a5.py`
- `ferramentas/normalizar_onda_incremental_dry_run.py`
- `ferramentas/normalizar_stt_dry_run.py`
- `ferramentas/normalizar_stt_lote_2026_10.py`

**Proveniência/guarda de saída em executor ativo (1):**
- `ferramentas/fase0_ingestao_stt_lote_2026_10.py`

`ferramentas/caminhos_acervo.py` já centraliza `fonte.recepcao` na rota atual e não foi alterado. Os quatro scripts Python selados em apostilas, assim como registros e fontes históricas, não devem ser reescritos.

## Contrato de recepção

FON-RECEPÇÃO não é equivalente a uma coleção de livros. Ela é caixa de entrada/proveniência: o contrato exige cópia byte a byte e SHA-256 aos destinos canônicos antes de qualquer remoção. Portanto, uma futura onda **não deve começar por `git mv uploads_recepcao/ fontes/recepcao/`**.

A migração física só poderá ser proposta depois de definir, por item, se o arquivo: (a) permanece na recepção; (b) é copiado ao destino canônico com prova de hash; ou (c) pode sair da recepção após a cópia validada. Apostilas, ciclos e consolidações nunca são destino automático da caixa de entrada.

## Próximo passo recomendado

Abrir uma Fase R1 sem migração física: adaptar os cinco leitores e o registrador de proveniência ao mapa central, criar um verificador de cópia/identidade por item e executar testes. Só então apresentar uma taxonomia de destinos para decisão curatorial.
