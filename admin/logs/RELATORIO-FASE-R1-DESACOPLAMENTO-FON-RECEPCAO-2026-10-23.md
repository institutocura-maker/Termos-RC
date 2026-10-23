# Relatório — Fase R1 · desacoplamento de FON-RECEPÇÃO

**Data:** 23/10/2026
**Base:** `3c018eb docs: consolida fase 1E e preparação de recepção`
**Natureza:** preparação de consumidores; sem movimento, cópia ou alteração de fontes.

## Escopo executado

A R1 eliminou a resolução física direta de `uploads_recepcao/` dos seis consumidores ativos mapeados na preparação. Todos agora obtêm a rota por `caminho_atual("fonte.recepcao")`, cuja resolução atual continua sendo `uploads_recepcao/`.

| Consumidor | Papel da rota mapeada |
|---|---|
| `diagnostico/medir_processo.py` | censo de itens recebidos |
| `ferramentas/aplicar_decisao_curador_a5.py` | arquivo de decisão recebido |
| `ferramentas/normalizar_onda_incremental_dry_run.py` | fontes do piloto STT |
| `ferramentas/normalizar_stt_dry_run.py` | fontes do dry-run STT |
| `ferramentas/normalizar_stt_lote_2026_10.py` | lote bruto STT |
| `ferramentas/fase0_ingestao_stt_lote_2026_10.py` | proveniência declarada e guarda de saída |

Não foram alteradas referências históricas em fontes, apostilas, relatórios ou derivados. O valor atual do mapa também não foi trocado: R1 prepara a futura decisão sem antecipá-la.

## Testes novos

A suíte ganhou os portões T16 e T17:

- **T16:** carrega os seis consumidores sem executar seus pontos de entrada e confirma que cada rota resolve para a mesma coleção `fonte.recepcao`;
- **T17:** registra tamanho e SHA-256 de cada arquivo da recepção antes e depois desses carregamentos, reprovando qualquer escrita por efeito de importação.

## Portões

| Portão | Resultado |
|---|---|
| Compilação dos sete módulos alterados | OK |
| `git diff --check` | OK |
| `python3 ferramentas/test_suite.py` | OK — 23 testes, incluindo T16/T17 |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| Verificador FON-RECEPÇÃO | OK — 330 arquivos, 10.982.198 bytes |
| SHA-256 agregado FON-RECEPÇÃO | `a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b` |
| Diff em `uploads_recepcao/` e `fontes/recepcao/` | nenhum |

A verificação encadeada de FON-LIVROS também permaneceu verde: 577 arquivos, 100.540.402 bytes e SHA-256 agregado `df1607e1328788008dc731b6f007d718e73cc5566c61825a24282edc1f3af3ff`.

## Salvaguarda em paralelo

A análise segura da salvaguarda atual está registrada em
[`RECONCILIACAO-SALVAGUARDA-R1-2026-10-23.md`](RECONCILIACAO-SALVAGUARDA-R1-2026-10-23.md). Nenhum conteúdo dela foi aplicado à R1.

## Limites preservados

- `uploads_recepcao/` não foi movida, copiada, removida nem regravada;
- `fontes/recepcao/` não recebeu conteúdo;
- a salvaguarda `stash@{0}` não foi aplicada, removida ou limpa;
- R2 permanece apenas como proposta curatorial, dependente de decisão por item.
