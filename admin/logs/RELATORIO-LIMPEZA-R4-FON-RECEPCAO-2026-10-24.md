# Relatório de limpeza R4 e reconfiguração — FON-RECEPÇÃO

**Data:** 24/10/2026
**Escopo autorizado:** limpeza exclusivamente das origens com decisão `RETIRAR_APOS_COPIA_VALIDADA`, após prova R3 aprovada.
**Resultado:** concluído sem alteração de conteúdo e sem remoção dos dois itens estruturais da caixa de entrada.

## Cadeia de autorização e pré-condições

- Matriz R2: `admin/logs/REGISTRO-DELIBERACAO-R2-FON-RECEPCAO-2026-10-24.csv` — SHA-256 `9122595742bf23867318873c690d568c45775841082838d57ee9599b331c77e4`; 330 decisões aprovadas, 328 para retirada após cópia e 2 para manutenção.
- Manifesto R3: `admin/logs/MANIFESTO-COPIA-R3-FON-RECEPCAO-2026-10-24.csv` — SHA-256 `49265cc73f16954b377c380d7c259f3560a3965b830aeee443e6af59543dec28`; 328 pares e 10.963.118 bytes.
- Antes de qualquer `unlink`, cada um dos 328 pares foi relido: existência de ambas as pontas, tamanho da origem, SHA-256 da origem contra R2 e igualdade byte a byte com o destino. O lote inteiro passou no preflight.

## Limpeza executada

- Removidos de `uploads_recepcao/`: **328 arquivos**, todos e somente os declarados para retirada.
- Não removidos: `uploads_recepcao/README.md` e `uploads_recepcao/.gitkeep` (**2 arquivos, 19.080 bytes**).
- O subdiretório vazio `uploads_recepcao/stt-lote-2026-10/` foi eliminado depois da remoção de seu último arquivo; nenhum conteúdo adicional foi tocado.
- Leitura independente posterior à limpeza: 328/328 destinos presentes com bytes e SHA-256 idênticos aos da matriz R2; as 328 origens não existem mais.

## Inventário canônico pós-R3/R4

| Rota canônica | Itens declarados | Bytes |
|---|---:|---:|
| `admin/logs/` | 10 | 43.315 |
| `admin/documentos/` | 1 | 24.081 |
| `fontes/docx_originais/` | 1 | 57.450 |
| `fontes/pilotos_historicos/` | 6 | 626.715 |
| `fontes/stt-lote-2026-10/` | 310 | 10.211.557 |
| `uploads_recepcao//` | 2 | 19.080 |

- O inventário distribuído de FON-RECEPÇÃO contém **330 arquivos**. **10.982.198 bytes** e SHA-256 agregado `a9f253187a50e3a6e31d1e04054739f534592cefb02c1cbf64f753523efe9ccb`.
- O campo `linha_base_origem_fase_0` conserva a linha histórica: 330 arquivos, 10.982.198 bytes e SHA-256 agregado `a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b` para a antiga coleção única em recepção.

## Reconfiguração de contratos

- `fontes/manifestos/MANIFESTO-FONTES-FASE-0.json` passou FON-RECEPÇÃO para `modo_verificacao: distribuida_por_arquivo`; cada item declarado aponta à sua rota canônica relativa à raiz.
- `ferramentas/verificar_migracao_fontes.py` verifica esse modo por arquivo declarado e não trata os demais arquivos adjacentes de `admin/logs/` ou `admin/documentos/` como extras da coleção.
- `ferramentas/caminhos_acervo.py` e os consumidores de ingestão/normalização usam as seis chaves canônicas; os testes T16/T17 vigiam a resolução delas.

## Validações pós-limpeza

- `python3 ferramentas/verificar_migracao_fontes.py --colecao FON-RECEPCAO` — passou: 330 arquivos, 10.982.198 bytes e hash agregado preservado.
- Verificador FON-LIVROS com as três averbações — passou: 577 arquivos, 100.540.402 bytes e hash agregado preservado.
- `python3 ferramentas/test_suite.py` — **23/23** testes passaram.
- `python3 ferramentas/motor.py selftest` — **10/10** testes passaram.
- `git diff --check`, validação JSON e compilação Python dos arquivos alterados — passaram.

## Limite de encerramento

A R4 realizou limpeza física e reconfiguração de contratos somente. Não houve commit nesta etapa; a árvore fica preparada para revisão curatorial e stage explícito por allowlist.
