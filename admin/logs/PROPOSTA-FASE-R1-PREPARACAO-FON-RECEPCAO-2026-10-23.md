# Proposta — Fase R1 · preparação de FON-RECEPÇÃO

**Data:** 23/10/2026
**Estado:** proposta para decisão curatorial; não executada.

## Premissa

FON-RECEPÇÃO é uma caixa de entrada de proveniência. Sua rota de runtime ainda
é `uploads_recepcao/`, registrada como `fonte.recepcao` em
`ferramentas/caminhos_acervo.py`. Embora o destino arquitetural
`fontes/recepcao/` exista no planejamento, ele não é autorização de uso nem de
movimento.

A linha de base verificada contém **330 arquivos**, **10.982.198 bytes** e
SHA-256 agregado
`a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b`.
O mapa integral de dependências está em
[`MAPA-PREPARACAO-FON-RECEPCAO-2026-10-23.csv`](MAPA-PREPARACAO-FON-RECEPCAO-2026-10-23.csv).

## Escopo proposto para R1

R1 prepara consumidores, sem mudar a rota atual e sem copiar fontes:

1. trocar a resolução física direta pela chamada
   `caminho_atual("fonte.recepcao")` nos cinco leitores/diagnósticos ativos:
   - `diagnostico/medir_processo.py`;
   - `ferramentas/aplicar_decisao_curador_a5.py`;
   - `ferramentas/normalizar_onda_incremental_dry_run.py`;
   - `ferramentas/normalizar_stt_dry_run.py`;
   - `ferramentas/normalizar_stt_lote_2026_10.py`.
2. substituir, em `ferramentas/fase0_ingestao_stt_lote_2026_10.py`, as
   referências de proveniência e a guarda que ainda codificam a rota por uma
   derivação a partir do mesmo mapa;
3. acrescentar testes de resolução do mapa e de não-escrita da recepção;
4. desenhar — sem executar — um verificador de cópia por item que compare
   caminho relativo, bytes e SHA-256 entre a origem e um destino curatorial
   previamente declarado.

A troca de consumidores permanece semanticamente neutra em R1: durante toda a
fase, `caminho_atual("fonte.recepcao")` continuará retornando
`uploads_recepcao/`.

## Exclusões expressas

- não criar `fontes/recepcao/` como destino de conteúdo;
- não usar `git mv`, `cp`, exclusão, normalização ou regravação sob
  `uploads_recepcao/`;
- não alterar os quatro scripts Python selados em `apostilas/`;
- não reescrever as 1.225 referências históricas/documentais inventariadas;
- não alterar FON-LIVROS, KB, Termos, RAG, apostilas, ciclos, consolidações ou
  a salvaguarda preservada `stash@{0}`.

## Critérios de saída de R1

1. `uploads_recepcao/` permanece byte a byte idêntica à linha de base e o
   verificador Fase 0 passa antes e depois;
2. os seis consumidores ativos usam apenas a chave arquitetural para obter a
   rota atual;
3. `git diff --check`, a suíte de integridade e o selftest passam;
4. relatório de escopo prova que não houve arquivo adicionado, removido ou
   modificado em `uploads_recepcao/`;
5. o Curador recebe uma taxonomia por item — permanecer, copiar para destino
   canônico, ou remover somente depois de cópia validada — antes de qualquer
   onda física.

## Onda física posterior (não autorizada)

Após R1 e decisão curatorial por item, uma possível fase R2 deverá executar
cópias byte a byte aos destinos aprovados, registrar manifestos de origem e
cópia, comparar cada SHA-256 e somente então solicitar autorização separada
para qualquer descarte na recepção. Um `git mv uploads_recepcao/ →
fontes/recepcao/` não satisfaz esse contrato e não é uma opção desta proposta.
