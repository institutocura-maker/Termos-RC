# Relatório de refatoração da raiz — 23/10/2026

> **Estado:** concluído para validação curatorial; **sem commit** e sem alteração da Base, do vocabulário, das planilhas, do glossário canônico ou dos diretórios consolidados de processamento.

## 1. Escopo executado

Foram criados os três destinos aprovados:

```text
admin/
├── logs/       # 13 registros operacionais migrados + este relatório
└── scripts/    # reserva versionada (.gitkeep); não havia .py/.sh solto na raiz
prompts/        # 10 prompts e instruções de sistema migrados
```

Os 23 documentos foram deslocados com `git mv`, preservando a detecção de renomeação e, portanto, o histórico de cada arquivo.

### Prompts movidos para `prompts/` (10)

1. `PROMPT-COMPLETO-2026-08-31-ESTEIRA-LEVE.md`
2. `PROMPT-COMPLETO-2026-08-31.md`
3. `PROMPT-CONTINUIDADE-2026-09-01.md`
4. `PROMPT-CONTINUIDADE-2026-09-02.md`
5. `PROMPT-CONTINUIDADE-2026-09-06-F044.md`
6. `PROMPT-CONTINUIDADE-2026-09-07-PEDAGOGIA-TOP-DOWN.md`
7. `PROMPT-CONTINUIDADE-2026-09-13-FIM-DE-LEVAS.md`
8. `PROMPT-INICIAL-DO-AGENTE.md`
9. `PROMPT-NOVO-CHAT-2026-09-07.md`
10. `PROMPT-PROXIMA-SESSAO.md`

### Registros movidos para `admin/logs/` (13)

1. `CHECKPOINT-SESSAO-2026-08-21.md`
2. `CONTINUIDADE.md`
3. `DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md`
4. `DESPACHO-ESTEIRA-CONSOLIDACAO-2026-09-03.md`
5. `HANDOFF-ONDA1-2026-09-12.md`
6. `PACOTE-MIGRACAO-CHAT-2026-08-18.md`
7. `REGISTRO-ANOMALIA-REBASE-2026-08-31.md`
8. `STATE-MIRROR.md`
9. `STATUS-HANDOFF-2026-08-31.md`
10. `STATUS-HANDOFF-2026-09-01.md`
11. `STATUS-HANDOFF-2026-09-02.md`
12. `STATUS-HANDOFF-2026-09-09.md`
13. `STATUS-RESTAURACAO.md`

## 2. Referências e geradores atualizados

As referências ativas afetadas foram recalculadas relativamente ao arquivo que as consome, incluindo documentação de raiz, diagnósticos, material pedagógico, `.arena/`, os próprios prompts/logs e scripts de apoio.

Atualizações de comportamento verificadas:

- `ferramentas/build_readme.py` lê `admin/logs/STATE-MIRROR.md`, anuncia esse caminho na navegação e, ao transportar a narrativa de fase para o README na raiz, normaliza rotas relativas de `prompts/` e `admin/logs/` para o novo contexto.
- `ferramentas/gerar_pacotes.py` inclui `admin/logs/CONTINUIDADE.md` e `prompts/PROMPT-INICIAL-DO-AGENTE.md` no grupo regenerável.
- `diagnostico/medir_processo.py` mede os novos destinos a partir da raiz do repositório.
- `ferramentas/motor.py` passa a gravar em novos `ciclo.toml` a referência `../../admin/logs/DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md`, correta a partir de `ciclos/<sigla>/`.
- `README.md` foi regenerado exclusivamente por `python3 ferramentas/build_readme.py`.
- `indice-mestre.md` foi regenerado exclusivamente por `python3 ferramentas/build_indice.py`; o conteúdo já estava atual e não produziu delta textual.

A varredura de links Markdown não encontrou nenhum link ainda apontando diretamente para os nomes antigos na raiz.

### Preservação deliberada de acervo consolidado

Há 12 menções textuais históricas, sem link Markdown direto, a `CONTINUIDADE.md` ou `PROMPT-PROXIMA-SESSAO.md` dentro de `apostilas/CONCLUIDAS/`. Elas **não foram reescritas** para respeitar a determinação de não modificar diretórios consolidados de processamento. Não há arquivo movido referenciado por link Markdown antigo nesse acervo. Caso se deseje converter também essas citações históricas em caminhos atuais, isso exige despacho específico que libere a modificação do diretório consolidado.

## 3. Validações executadas

| Verificação | Resultado |
|---|---|
| Compilação (`py_compile`) de `build_readme.py`, `build_indice.py`, `gerar_pacotes.py`, `motor.py` e `medir_processo.py` | OK |
| Resolução das entradas migradas em `gerar_pacotes.py` e métricas em `medir_processo.py` | OK |
| `python3 ferramentas/build_readme.py` | OK — `README.md` gerado (`946/820/1887/104`) |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` | OK |
| Escopo protegido (`base/`, `termos/`, `ciclos/`, `onda_incremental_dry_run/`, normalizados/triagem STT) | OK — nenhum arquivo modificado |

A suíte emite `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; não são falhas e a execução terminou com `OK`.

## 4. Situação para aprovação

- Raiz livre dos 10 prompts e 13 registros selecionados.
- Nova árvore administrativa criada e preenchida.
- Índices tratados somente por seus geradores.
- Dados canônicos e diretórios consolidados preservados.
- Worktree propositalmente permanece **sem commit**, aguardando validação do Curador sobre tree, diff e esta ressalva de preservação histórica.
