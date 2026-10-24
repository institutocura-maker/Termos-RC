# Relatório de cópia — Fase R3 FON-RECEPÇÃO

**Data:** 24/10/2026
**Estado:** cópia byte a byte concluída; remoção da origem não autorizada.

## Escopo autorizado e executado

A matriz R2 aprovou os 330 itens: 2 itens de suporte permanecem em `uploads_recepcao/` e 328 itens receberam `RETIRAR_APOS_COPIA_VALIDADA`. Foram criadas cópias nos destinos curatoriais, preservando nome e bytes de cada arquivo. Nenhum arquivo da origem foi movido, removido, normalizado ou regravado.

| Destino canônico | Itens copiados |
|---|---:|
| `admin/logs/` | 10 |
| `admin/documentos/` | 1 |
| `fontes/docx_originais/` | 1 |
| `fontes/pilotos_historicos/` | 6 |
| `fontes/stt-lote-2026-10/` | 310 |
| **Total** | **328** |

Os itens mantidos em recepção são `uploads_recepcao/README.md` e `uploads_recepcao/.gitkeep`.

## Prova de igualdade

O manifesto de cópia está em [`MANIFESTO-COPIA-R3-FON-RECEPCAO-2026-10-24.csv`](MANIFESTO-COPIA-R3-FON-RECEPCAO-2026-10-24.csv), SHA-256 `49265cc73f16954b377c380d7c259f3560a3965b830aeee443e6af59543dec28`. Ele contém, por cópia, origem, destino, bytes e SHA-256 dos dois lados.

Uma segunda leitura independente do manifesto confirmou:

- **328/328** pares com bytes idênticos;
- **328/328** pares com SHA-256 idêntico;
- **10.963.118 bytes** copiados e verificados;
- nenhum arquivo preexistente divergente foi sobrescrito.

## Prova de preservação da origem

O verificador Fase 0 passou antes e depois da cópia:

- 330 arquivos;
- 10.982.198 bytes;
- SHA-256 agregado `a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b`.

## Próxima decisão solicitada

Validar a prova de igualdade. Somente após autorização curatorial nova e expressa poderá ocorrer a limpeza das 328 origens copiadas. A presente R3 não confere autorização de remoção.

## Encerramento posterior da operação

Após a validação curatorial desta prova, a R4 foi autorizada e executada em 24/10/2026. As 328 origens comprovadas foram removidas e os contratos passaram a usar as rotas canônicas distribuídas. Ver `admin/logs/RELATORIO-LIMPEZA-R4-FON-RECEPCAO-2026-10-24.md`. Esta seção não altera a evidência R3: ela registra o estado anterior à limpeza.
