# Relatório — Onda 3 da organização (contrato de navegação)

> **Estado:** executada e validada para decisão curatorial; **sem commit**.
>
> **Escopo autorizado:** concluir a fronteira entre raiz e documentação histórica, criar um mapa permanente da documentação e não mover documentos cujo redirecionamento exigiria reescrever acervo consolidado.

## Movimentos preservando histórico

| Origem | Destino | Função |
|---|---|---|
| `INDICE-ARQUIVOS-RAIZ-2026-08-31.md` | `docs/historico/INDICE-ARQUIVOS-RAIZ-2026-08-31.md` | índice histórico de handoff e compatibilidade |
| `INVENTARIO-COMPACTO-2026-08-31.md` | `docs/historico/INVENTARIO-COMPACTO-2026-08-31.md` | snapshot legível e datado do inventário de apostilas |

Os dois movimentos foram realizados com `git mv`. A raiz passa de 18 para **16 arquivos de projeto** (sem contar `.gitignore` e `.gitattributes`).

## Contrato de navegação criado

Foi criado `docs/README.md`, apontado pelo README principal, com:

- ponto de partida para documentação humana;
- responsabilidades da raiz, `docs/historico/`, `docs/planos/`, `diagnostico/`, `prompts/` e `admin/logs/`;
- regra de admissão para que documento novo não seja criado na raiz por conveniência;
- zonas canônicas/consolidadas que não devem ser movidas ou reescritas sem despacho.

`ferramentas/build_readme.py` foi ajustado para publicar o link para `docs/README.md`; `README.md` foi regenerado somente por esse gerador.

O índice datado, agora em `docs/historico/`, foi ajustado para declarar sua condição de ponte histórica e apontar ao mapa atual em `docs/README.md`.

## Referências e limites

A verificação percorreu **15 referências** aos dois snapshots movidos; todas resolvem relativamente ao arquivo consumidor. Foram atualizados os consumidores fora das zonas protegidas, inclusive apresentação, índice de palestras, handoff, prompt e relatórios de organização anteriores.

Nenhum arquivo de `base/`, `termos/`, `apostilas/`, `consolidacoes/`, `ciclos/`, ondas ou derivados STT foi modificado.

Permanecem deliberadamente na raiz como **compatibilidade bloqueada**:

- `PLANO-MIGRACAO-DE-CHAT.md` — citado em `apostilas/CONCLUIDAS/`;
- `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md` — citada em `consolidacoes/`;
- `PARECER-GLOSSARIO-KRYS-AMON-2026-09-06.md` — citado em `consolidacoes/`;
- `VERIFICACAO-DE-COBERTURA-LISTA-SIMPLES-2026-09-04.md` — citada em `consolidacoes/`.

Também permanecem por função operacional `INDICE-PALESTRAS.md`, `INVENTARIO-APOSTILAS.json` e `GUIA-MESTRE-RC-APOSTILA-v1.1.md`.

## Validações

| Verificação | Resultado |
|---|---|
| Resolução relativa das 15 referências migradas | OK |
| Links locais em `docs/README.md` | OK |
| `python3 ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` e `git diff --cached --check` | OK |
| Escopo canônico e consolidado | OK — nenhuma modificação |

A suíte emite apenas `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; encerrou com `OK`.

## Situação para decisão

A Onda 3 está pronta para commit e push após a validação do Curador. A organização da raiz atinge um ponto de estabilização: qualquer nova migração dos quatro documentos de compatibilidade bloqueada exige despacho que permita atualizar as referências mantidas em acervo consolidado.
