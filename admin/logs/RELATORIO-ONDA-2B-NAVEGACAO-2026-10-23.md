# Relatório — Onda 2B da organização da raiz (navegação e documentação)

> **Estado:** executada e validada para decisão curatorial; **sem commit**.
>
> **Autorização aplicada:** onda semântica integralmente aprovada: diagnóstico de processo para `diagnostico/`, preparação temática datada para `docs/historico/`, plano de corpus para `docs/planos/`, e atualização do índice de ponteiros.

## Movimentos realizados

| Origem | Destino | Papel após a migração |
|---|---|---|
| `DIAGNOSTICO-DO-PROCESSO-2026-08-29.md` | `diagnostico/DIAGNOSTICO-DO-PROCESSO-2026-08-29.md` | diagnóstico técnico do rito e da sua reforma |
| `PREPARACAO-DE-TEMA-2020-04-25-YEL-LUZBEL.md` | `docs/historico/PREPARACAO-DE-TEMA-2020-04-25-YEL-LUZBEL.md` | preparação datada de fonte específica, preservada como histórico |
| `PLANO-CORPUS-TREINAMENTO-IA-LOCAL.md` | `docs/planos/PLANO-CORPUS-TREINAMENTO-IA-LOCAL.md` | plano estratégico, fora da interface da raiz |

Os três movimentos foram feitos por `git mv`; a raiz passa de 21 para **18 arquivos de projeto** (sem contar `.gitignore` e `.gitattributes`).

## Índice de ponteiros requalificado

`../../docs/historico/INDICE-ARQUIVOS-RAIZ-2026-08-31.md` foi preservado na raiz como ponte de compatibilidade, mas agora declara explicitamente que:

- é um **índice histórico de handoff**, e não inventário literal da raiz;
- as contagens, tamanhos, HEADs e recomendações datadas permanecem como registro histórico;
- a navegação atual separa interfaces de raiz, `prompts/`, `admin/logs/`, `diagnostico/`, `docs/historico/` e `docs/planos/`;
- estado presente deve ser consultado em `README.md` e `admin/logs/STATE-MIRROR.md`.

As entradas históricas do próprio índice foram atualizadas para os novos caminhos.

## Referências atualizadas

Foram verificadas **12 ocorrências** relativas aos três documentos movidos. Os consumidores abaixo foram atualizados quando a mudança de diretório alterava o caminho relativo; `diagnostico/medir_processo.py` foi conferido como já correto por passar a compartilhar o diretório do diagnóstico:

- `../../docs/historico/INDICE-ARQUIVOS-RAIZ-2026-08-31.md`;
- `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`;
- `admin/logs/CONTINUIDADE.md`;
- `admin/logs/DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md`;
- `admin/logs/STATUS-HANDOFF-2026-09-02.md`;
- `diagnostico/medir_processo.py`;
- `prompts/PROMPT-CONTINUIDADE-2026-09-02.md`;
- `prompts/PROMPT-PROXIMA-SESSAO.md`;
- o próprio plano, cuja referência ao diagnóstico foi recalculada a partir de `docs/planos/`.

## Escopo preservado e itens adiados

Não foram alterados Base, vocabulário, planilhas, glossário canônico ou diretórios consolidados (`apostilas/`, `consolidacoes/`, `ciclos/`, ondas e derivados STT).

Continuam na raiz por dependência operacional ou por referências em acervo consolidado:

- `INDICE-PALESTRAS.md`, inventários e `GUIA-MESTRE-RC-APOSTILA-v1.1.md`;
- `PLANO-MIGRACAO-DE-CHAT.md` e `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`;
- `PARECER-GLOSSARIO-KRYS-AMON-2026-09-06.md` e `VERIFICACAO-DE-COBERTURA-LISTA-SIMPLES-2026-09-04.md`.

## Validações

| Verificação | Resultado |
|---|---|
| Resolução relativa das 12 referências migradas | OK |
| `python3 ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` e `git diff --cached --check` | OK |
| Escopo canônico e consolidado | OK — nenhuma modificação |

A suíte emite apenas `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; encerrou com `OK`.

## Situação para decisão

A Onda 2B está pronta para commit e push após a validação do Curador. Nenhum commit foi criado nesta etapa.
