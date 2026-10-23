# Relatório — Onda 2A da organização da raiz (diagnósticos históricos)

> **Estado:** executada e validada para aprovação curatorial; **sem commit**.
>
> **Escopo autorizado:** arquivos históricos/de baixo risco. Base, vocabulário, planilhas, glossário canônico e diretórios consolidados permaneceram intocados.

## Movimentos realizados

Os seis documentos abaixo foram deslocados da raiz para `diagnostico/` com `git mv`, preservando o histórico:

| Origem | Destino |
|---|---|
| `ANALISE-PROPOSTA-CONSOLIDACAO-E-22-GLOSSARIO-2026-09-03.md` | `diagnostico/ANALISE-PROPOSTA-CONSOLIDACAO-E-22-GLOSSARIO-2026-09-03.md` |
| `AVALIACAO-COBERTURA-PACTO-AESIR-VANIR-JURAMENTO-DA-SALIVA-2026-09-04.md` | `diagnostico/AVALIACAO-COBERTURA-PACTO-AESIR-VANIR-JURAMENTO-DA-SALIVA-2026-09-04.md` |
| `DIAGNOSTICO-BASELINE-KB-2026-09-03.md` | `diagnostico/DIAGNOSTICO-BASELINE-KB-2026-09-03.md` |
| `RELATORIO-BASE-TERMINOLOGICA.md` | `diagnostico/RELATORIO-BASE-TERMINOLOGICA.md` |
| `REVISAO-P2024-03-02-DIAGNOSTICO.md` | `diagnostico/REVISAO-P2024-03-02-DIAGNOSTICO.md` |
| `VERIFICACAO-DE-COBERTURA-2026-08-26.md` | `diagnostico/VERIFICACAO-DE-COBERTURA-2026-08-26.md` |

A raiz passa de 27 para **21 arquivos de projeto** (desconsiderados `.gitignore` e `.gitattributes`).

## Referências atualizadas

Foram atualizadas 9 ocorrências em quatro consumidores, sempre com caminho relativo ao arquivo consumidor:

- `APRESENTACAO-DO-SISTEMA.md`
- `INDICE-ARQUIVOS-RAIZ-2026-08-31.md`
- `admin/logs/DESPACHO-ESTEIRA-CONSOLIDACAO-2026-09-03.md`
- `livros/README.md`

## Exclusões deliberadas da onda 2A

Dois documentos inicialmente classificados como históricos permaneceram na raiz porque suas únicas referências externas estão dentro de diretórios consolidados, que a diretriz vigente protege contra modificação:

| Arquivo mantido na raiz | Referência protegida |
|---|---|
| `PARECER-GLOSSARIO-KRYS-AMON-2026-09-06.md` | `consolidacoes/F043_glossario-krys-amon/mapeamento.md` |
| `VERIFICACAO-DE-COBERTURA-LISTA-SIMPLES-2026-09-04.md` | `consolidacoes/TL01_lista-simples-rc/relatorio-trilha-leve.md` |

Também ficaram fora desta onda os índices, inventários, guia, planos, política de quarentena e diagnóstico do processo, por terem dependências operacionais maiores. Nenhum deles foi movido ou modificado.

## Validações

| Verificação | Resultado |
|---|---|
| Resolução relativa das 9 referências aos seis novos destinos | OK |
| `python3 ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` | OK |
| Escopo protegido (`base/`, `termos/`, `apostilas/`, `consolidacoes/`, `ciclos/`, ondas e normalizados/triagem STT) | OK — nenhum arquivo modificado |

A suíte emite somente `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; a execução terminou com `OK`.

## Situação para decisão

A onda 2A está pronta para commit e push após a validação do Curador. Nenhum commit foi criado nesta etapa.
