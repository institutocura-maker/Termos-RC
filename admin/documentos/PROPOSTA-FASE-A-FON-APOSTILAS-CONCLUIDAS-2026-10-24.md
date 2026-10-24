# Proposta — Fase A de inventário para FON-APOSTILAS-CONCLUÍDAS

**Data:** 24/10/2026
**Estado:** proposta de preparação; não autoriza cópia, movimento, remoção, renomeação ou alteração de conteúdo.

## Pedido curatorial

O acervo de `apostilas/CONCLUIDAS/` concentra grande parte do material já processado e deve receber atenção para uma futura organização sob `fontes/`. Esta proposta delimita o levantamento necessário antes de qualquer intervenção física.

## Linha de base levantada

| Medida | Resultado |
|---|---:|
| Pastas imediatas de apostilas concluídas | 82 |
| Arquivos totais | 1,629 |
| Bytes totais | 41,323,152 |
| Candidatos brutos nomeados `original.txt` ou `original.pdf` | 82 |
| Bytes dos candidatos brutos | 10,184,996 |
| Pastas com candidato bruto | 81 |
| Pastas sem `original.txt`/`original.pdf` | 1 |

Os totais usam separador de milhares internacional no inventário de máquina; nesta proposta, correspondem a 1629 arquivos e 41323152 bytes.

O inventário file-level está em [`../logs/INVENTARIO-PRE-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv`](../logs/INVENTARIO-PRE-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv):

- SHA-256 do CSV: `3ca53e15e497b1ed01028aa4c3779a65daa0871ca6618631304ef498914a0b36`;
- hash agregado dos 82 candidatos brutos: `81042108ea7a7b8cbd38aff72f20095ffe9f7557d4b458170e774cabda4e9b3f`;
- cada linha está em `AGUARDA_DELIBERACAO_CURATORIAL`, sem destino proposto.

A única pasta sem um arquivo com esses dois nomes é `2026-02-28_os_desafios_da_transicao_planetaria_aprofundamento`. A pasta `2024-05-04_prabrajna_perperion_simultaneidade_reversa` é a única com dois candidatos (`original.txt` e `original.pdf`). Ambas exigem decisão explícita, sem suposições.

## Por que não mover a árvore inteira agora

`apostilas/CONCLUIDAS/` não é um repositório homogêneo de fontes. Seus 1629 arquivos incluem 907 `.txt`, 415 `.md`, 158 scripts Python, 71 JSON, 72 DOCX, 1 PDF e 5 PNG. Além dos 82 possíveis brutos, há **1547 artefatos de transformação, análise, auditoria e apresentação**. Movê-los em bloco para `fontes/` misturaria fonte primária e produto editorial, contrariando a separação que hoje protege proveniência e referências históricas.

## Rota a deliberar

A recomendação preliminar é avaliar uma coleção **FON-APOSTILAS-CONCLUIDAS** cujo escopo inicial seja apenas o bruto de cada apostila, com candidata de destino estrutural:

```text
fontes/palestras/concluidas/<pasta-da-apostila>/original.txt|original.pdf
```

Ela é apenas uma proposta de topologia; **não é rota atual, oficial ou autorizada**. A decisão também deve escolher, por item ou por regra expressa, entre:

1. manter a cópia atual em `apostilas/CONCLUIDAS/` e criar cópia canônica em `fontes/`;
2. mover o bruto após validação e atualizar todos os consumidores/referências;
3. manter o item na apostila por razão histórica/técnica;
4. tratar separadamente os itens sem bruto nomeado ou com dois brutos.

## Roteiro seguro proposto

1. **Fase A1 — inventário e classificação:** revisar as 82 linhas do CSV e a pasta sem candidato; identificar dependências de runtime e referências textuais.
2. **Fase A2 — matriz curatorial:** receber decisão explícita para cada item, sem inferir destino a partir de extensão, data ou pasta.
3. **Fase A3 — cópia controlada:** para os itens autorizados, copiar byte a byte, registrar bytes/SHA-256 de ambas as pontas e não remover origem.
4. **Fase A4 — corte:** somente após prova validada, atualizar contratos/consumidores e remover exclusivamente as origens que tenham autorização expressa.
5. **Fase A5 — encerramento:** verificar a coleção distribuída, a integridade das apostilas e produzir relatório para aprovação.

## Limite desta fase

Esta proposta e seu CSV são exclusivamente de leitura/inventário. Nenhum arquivo de `apostilas/CONCLUIDAS/` foi copiado, movido, removido ou reescrito.
