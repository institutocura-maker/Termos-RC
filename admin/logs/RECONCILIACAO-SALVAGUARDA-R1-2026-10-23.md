# Reconciliação segura da salvaguarda — R1

**Data:** 23/10/2026
**Método:** leitura de `base × stash × HEAD`; nenhuma aplicação, `pop`, remoção
ou limpeza da salvaguarda foi executada.

## Identidades analisadas

| Papel | Git object |
|---|---|
| Base da salvaguarda | `41cfedbcbd3ee632e7e582fffc28926a912d0fac` |
| Conteúdo rastreado da salvaguarda | `363059facc2f5f4f5b5a19281912bb92d2a30e41` |
| HEAD R1 | `3c018ebe73345587aced7f20a6d8fcefbc0909c5` |

A salvaguarda atual é `stash@{0}` com a identificação
`arena-salvaguarda-checkout-reaberto-2026-10-23-r1`. Ela permanece preservada.

## Resultado — arquivos rastreados

Foram comparados **90** arquivos modificados na salvaguarda contra
sua base. Destes, **55** já têm no HEAD o mesmo
conteúdo da salvaguarda e não devem ser reaplicados.

| Classificação | Quantidade | Ação |
|---|---:|---|
| `CONVERGENTE_JA_EM_HEAD` | 55 | não aplicar |
| `CONFLITO_DE_TRES_VIAS` | 34 | decidir por arquivo |
| `MESCLA_AUTOMATICA` | 1 | validar antes de qualquer aplicação |
| `FALHA_TECNICA_A_REVISAR` | 0 | decidir por arquivo |

Os **35** itens que ainda requerem tratamento estão em `ferramentas/` (2), `termos/` (33). O inventário detalhado está em
[`RECONCILIACAO-SALVAGUARDA-R1-2026-10-23.csv`](RECONCILIACAO-SALVAGUARDA-R1-2026-10-23.csv), SHA-256 `c7afacc4e9dffd546636e7649af1a852e09f30784a94adde575561a693a110ce`.

## Conteúdo não rastreado preservado

A terceira árvore da stash contém **1089** entradas originalmente não
rastreadas. Elas foram apenas inventariadas, sem materialização no worktree:

| Classificação | Quantidade | Ação |
|---|---:|---|
| `JA_RASTREADO_EM_HEAD_IDENTICO` | 1079 | não aplicar |
| `COLIDE_COM_HEAD_DIVERGENTE` | 8 | decidir por arquivo |
| `EXCLUSIVO_NA_SALVAGUARDA` | 2 | inventariar antes de qualquer aplicação |

## Conclusão operacional

A R1 segue independente da salvaguarda: não absorveu nenhuma dessas mudanças e
não alterou fontes em recepção. Antes de qualquer tentativa de recuperar a
salvaguarda, deve haver decisão explícita item a item para os conflitos e para
qualquer conteúdo exclusivo. `git stash apply` ou `git stash pop` permanecem
fora de escopo.
