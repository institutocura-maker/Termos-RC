# Relatório de abertura R2 curatorial — FON-APOSTILAS-CONCLUIDAS

**Data:** 24/10/2026
**Fase:** R2 — deliberação e linha de base; sem cópia física.

## Decisão homologada

| Campo | Valor |
|---|---|
| Regra | Migração Modular Integral |
| Escopo | 1.629 arquivos em 82 pastas de `apostilas/CONCLUIDAS/` |
| Situação | 1.629 `APROVADO`; 0 pendentes |
| Decisão por item | `RETIRAR_APOS_COPIA_VALIDADA` |
| Destino canônico | `/fontes/apostilas/` |
| Estrutura | réplica literal da estrutura relativa de cada cápsula |
| Justificativa | fonte, scripts, metadados e produto final permanecem inseparáveis no mesmo módulo |

## Linha de base R2

- Arquivos: **1629**
- Pastas modulares imediatas: **82**
- Bytes: **41,323,152**
- SHA-256 agregado: `d0f6d344c5f0efd579cd99fb2581d1ba7ab02b67a9b1f7ee09bb59b841646c98`
- Registro decisório: `admin/logs/REGISTRO-DELIBERACAO-R2-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv`
- SHA-256 do registro: `afc1a84250279ecfde45378e88a74e489b61b2dcef498caa5789b3c306133f6c`

O agregado é calculado sobre linhas ordenadas por caminho relativo a `apostilas/CONCLUIDAS/`, no formato `caminho\0bytes\0sha256\n`.

## Conferências

- Cada uma das 1629 origens foi relida para obter bytes e SHA-256.
- Cada linha R2 possui um destino individual explícito sob `fontes/apostilas/`; não há colisões de destino.
- Os destinos finais ainda não existem como arquivos. `fontes/apostilas/` foi criado vazio para receber uma eventual R3.
- O inventário preliminar de 82 brutos foi atualizado de `AGUARDA_DELIBERACAO_CURATORIAL` para `APROVADO`; ele é subconjunto da decisão modular de 1.629 arquivos.

## Limite da R2

Esta R2 **não copiou, moveu, renomeou, alterou nem removeu** arquivo algum de `apostilas/CONCLUIDAS/`. A R3 só poderá iniciar após validação curatorial deste registro; deverá copiar byte a byte, provar tamanho e SHA-256 em ambas as pontas e preservar integralmente as origens até novo despacho de limpeza.

## Estado posterior da operação

Após validação curatorial da R2, a cópia R3 foi executada em 24/10/2026 e comprovou 1.629/1.629 pares idênticos. Ver `admin/logs/RELATORIO-COPIA-R3-FON-APOSTILAS-CONCLUIDAS-2026-10-24.md`. Esta seção não altera a declaração R2, que representa o estado anterior à cópia.

## Encerramento posterior da operação

A R3 foi validada e a R4 executou a remoção autorizada das 1.629 origens em 24/10/2026. Ver `admin/logs/RELATORIO-LIMPEZA-R4-FON-APOSTILAS-CONCLUIDAS-2026-10-24.md`. Esta nota não modifica a linha de base R2.
