# Relatório de cópia R3 — FON-APOSTILAS-CONCLUIDAS

**Data:** 24/10/2026
**Escopo autorizado:** cópia física byte a byte dos itens aprovados na R2, sem remoção ou alteração de origem.
**Resultado:** cópia concluída e prova de igualdade aprovada; a R4 permanece bloqueada até validação curatorial deste relatório.

## Cadeia de autorização

- Registro R2: `admin/logs/REGISTRO-DELIBERACAO-R2-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv`
  - SHA-256: `afc1a84250279ecfde45378e88a74e489b61b2dcef498caa5789b3c306133f6c`
  - 1.629 itens `APROVADO`, todos `RETIRAR_APOS_COPIA_VALIDADA`.
  - Destino declarado: `/fontes/apostilas/`, com caminho explícito por item.
- Manifesto desta cópia R3: `admin/logs/MANIFESTO-COPIA-R3-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv`
  - SHA-256: `1c71d0aced13820bf2899e696d861bc366eb7cf19aaf5f386cea19558293c158`
  - 1.629 pares origem/destino, com bytes e SHA-256 de ambas as pontas.

## Execução

1. Antes da escrita, as 1.629 origens foram relidas e confrontadas com bytes/SHA-256 da R2; o destino não continha nenhum dos arquivos a materializar.
2. Foram criados os 196 diretórios estruturais necessários sob `fontes/apostilas/`, preservando as 82 cápsulas imediatas e suas subpastas.
3. Cada arquivo foi copiado por `shutil.copyfile` para temporário no próprio diretório de destino, conferido por tamanho e SHA-256 e só então promovido ao nome final. Não houve normalização, edição, renomeação ou sobrescrita.
4. Nenhum arquivo em `apostilas/CONCLUIDAS/` foi removido, movido ou alterado.

## Prova de igualdade

| Conferência | Resultado |
|---|---:|
| Pares R2/R3 | **1.629 / 1.629** |
| Arquivos de origem | **1.629** |
| Arquivos de destino | **1.629** |
| Cápsulas imediatas preservadas | **82 / 82** |
| Bytes na origem | **41.323.152** |
| Bytes no destino | **41.323.152** |
| Pares com bytes idênticos | **1.629 / 1.629** |
| Pares com SHA-256 idêntico | **1.629 / 1.629** |
| SHA-256 agregado relativo à coleção, origem | `d0f6d344c5f0efd579cd99fb2581d1ba7ab02b67a9b1f7ee09bb59b841646c98` |
| SHA-256 agregado relativo à coleção, destino | `d0f6d344c5f0efd579cd99fb2581d1ba7ab02b67a9b1f7ee09bb59b841646c98` |

Uma validação independente, em segunda leitura do manifesto R3, recalculou SHA-256 da origem e do destino de cada par e confirmou a igualdade integral. A lista relativa de 1.629 arquivos e a lista das 82 cápsulas imediatas também coincidem exatamente; não há temporários de cópia remanescentes.

## Limite da R3

Esta fase é somente de materialização e prova. As cópias canônicas agora existem em `fontes/apostilas/`, mas as origens em `apostilas/CONCLUIDAS/` continuam íntegras. Não foram atualizados consumidores, manifestos de rota ou removidas origens. A R4 exige autorização curatorial expressa.

## Encerramento posterior da operação

A prova R3 foi validada pelo Curador e sucedida pela R4 em 24/10/2026. As 1.629 origens foram removidas exclusivamente após a prova desta cópia, e a rota canônica passou a ser `fontes/apostilas/`. Ver `admin/logs/RELATORIO-LIMPEZA-R4-FON-APOSTILAS-CONCLUIDAS-2026-10-24.md`. Esta seção não altera a evidência R3, que descreve o estado anterior à limpeza.
