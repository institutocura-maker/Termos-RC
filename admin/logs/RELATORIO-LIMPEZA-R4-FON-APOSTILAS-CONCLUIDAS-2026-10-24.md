# Relatório de limpeza R4 e reconfiguração — FON-APOSTILAS-CONCLUIDAS

**Data:** 24/10/2026
**Escopo autorizado:** remover somente as origens R2 com cópia R3 comprovada; reconfigurar rotas e contratos para a preservação modular canônica.
**Resultado:** concluído, sem remoção fora da matriz R2.

## Cadeia de prova

- R2: `admin/logs/REGISTRO-DELIBERACAO-R2-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv` — SHA-256 `afc1a84250279ecfde45378e88a74e489b61b2dcef498caa5789b3c306133f6c`; 1.629 decisões aprovadas para `RETIRAR_APOS_COPIA_VALIDADA`.
- R3: `admin/logs/MANIFESTO-COPIA-R3-FON-APOSTILAS-CONCLUIDAS-2026-10-24.csv` — SHA-256 `1c71d0aced13820bf2899e696d861bc366eb7cf19aaf5f386cea19558293c158`; 1.629 pares, 41.323.152 bytes.
- Imediatamente antes da remoção, uma nova leitura de cada par confirmou tamanho e SHA-256 idênticos em **1.629/1.629** pares.

## Limpeza física

- Removidos: **1.629 arquivos**, todos e somente os itens da R2.
- Removida após esvaziamento: `apostilas/CONCLUIDAS/` e suas subpastas.
- Preservado: `apostilas/` permanece com itens que não pertenciam à matriz R2.
- Rota canônica materializada: `fontes/apostilas/`, com **1.629 arquivos**, **82 cápsulas imediatas** e **196 diretórios estruturais**.

## Reconfiguração de contratos

- `ferramentas/caminhos_acervo.py` declara `fonte.apostilas_concluidas → fontes/apostilas` e realinha a evidência de palestras.
- Os consumidores de censo, materialização, motor, pacotes, diagnóstico, manifestos, U41 e a suíte passam a resolver a rota canônica; a suíte também vigia a inexistência de `apostilas/CONCLUIDAS/`.
- O verificador genérico passa a monitorar `FON-APOSTILAS-CONCLUIDAS` via a chave canônica no manifesto.
- Dois scripts internos receberam o único ajuste pós-cópia necessário para não resolverem a rota removida: `2023-12-03.../_gerar_camadas_P2023-12-03.py` e `2025-08-02.../_regenerar_apostilas_0203.py`. Seus hashes R3 e atuais estão averbados no manifesto; nenhum outro arquivo da cápsula divergiu da cópia R3.

## Linha de base e estado canônico

| Medida | Linha R2/R3 | Estado canônico pós-R4 |
|---|---:|---:|
| Arquivos | 1.629 | 1629 |
| Bytes | 41.323.152 | 41,323,141 |
| SHA-256 agregado | `d0f6d344c5f0efd579cd99fb2581d1ba7ab02b67a9b1f7ee09bb59b841646c98` | `1150bcc04c7be677311b769923036d2cc6274b9d4cd06bdacb0422dd8e3e2d68` |

A diferença pós-R4 decorre exclusivamente dos dois scripts de rota averbados acima; a linha R2/R3 continua preservada e auditável.

## Validações pós-limpeza

- `python3 ferramentas/verificar_migracao_fontes.py --colecao FON-APOSTILAS-CONCLUIDAS` — passou: 1.629 arquivos, 41.323.141 bytes e hash canônico preservado.
- Verificadores FON-RECEPÇÃO e FON-LIVROS (com três averbações) — passaram.
- `python3 ferramentas/test_suite.py` — **23/23** testes passaram.
- `python3 ferramentas/motor.py selftest` — **10/10** testes passaram.
- Compilação sintática de 213 scripts Python e `git diff --check` — passaram.
- A varredura dos scripts canônicos não encontrou resolução executável de `apostilas/CONCLUIDAS/`; as 21 menções remanescentes são documentação histórica interna.

## Limite de encerramento

A R4 não realizou commit. Após validações de integridade, a árvore fica pronta para `git add` explícito e revisão curatorial da mensagem de commit.
