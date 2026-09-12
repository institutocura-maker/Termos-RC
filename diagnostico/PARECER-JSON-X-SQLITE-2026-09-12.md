# Parecer Comparativo — JSON × SQLite — Onda 1.2 (12/09/2026)

Despacho solicitado pelo plano: escolher o canônico pós-`dados_termos.py`. Premissas fixas (não-negociáveis): **só-stdlib**, **verdade revisável no git** (diff legível), escritor único (agente), ~1.000–10.000 linhas, git como log de transações.

## As duas candidaturas honestas

**A. JSON canônico** (`base/canonico.json` versionado; loader lê JSON; `.py` aposentado após paridade).
**B. SQLite-primeiro** (`base/schema.sql` + `base/data/*.csv` versionados; `rc.db` gitignored, construído localmente; loader lê o `.db`).

Nota decisiva: **B também precisa de texto canônico no git** (binário não é revisável) — ou seja, B = texto + binário derivado + disciplina de sincronia; A = só texto. A pergunta real: o binário derivado paga o seu custo?

## Placar por critério (1–5)

| Critério | A. JSON | B. SQLite |
|---|---|---|
| Zero-dependência (stdlib) | 5 (`json`) | 5 (`sqlite3`) |
| Diff revisável no git | 5 (o dado *é* o diff) | 2 (diff no sidecar, não no `.db` usado) |
| Validação declarativa | 2 (validador hand-rolled — manter!) | 5 (`UNIQUE`/`CHECK`/FK por construção) |
| Consultas ad-hoc | 3 (loops Python; OK até ~10k) | 5 (SQL de verdade) |
| Risco/curva de migração | 5 (mecânica: tupla→objeto) | 3 (schema + disciplina texto↔`.db`) |
| Reversibilidade | 5 (gera SQLite quando quiser) | 4 (dump sempre possível, mas há 2 fontes) |
| Busca full-text (FTS5) | 2 (grep/scripts) | 5 (nativo, testado na stdlib daqui) |
| Curador-legibilidade | 4 (abre e lê) | 1 (blob opaco sem ferramenta) |
| **Total** | **31** | **29** |

## Recomendação: A, com cláusula SQLite (híbrido disciplinado)

Recomendo **JSON canônico + SQLite derivado sob demanda**: o `canonico.json` é a verdade versionada; um `db_build.py` de ~30 linhas gera o `.db` (gitignored) quando — e só quando — consultas SQL/FTS forem necessárias (o item 3.2 do plano já prevê FTS5). Ganha-se: diff revisável (A), validação progressiva (validador now, constraints quando o `.db` existir), FTS5 sem pagar disciplina dual no dia a dia, e **migração reversível em qualquer ponto** (JSON→SQLite é função total; o inverso exige dump).

Contra-argumento registrado (honestidade): se a base passar a ter **escritores concorrentes** (2+ agentes simultâneos) ou **>50k linhas com joins frequentes**, B puro vence — o ponto de virada é objetivo e este parecer deve ser revisitado nele. Hoje: escritor único, 946 linhas, 0 joins em produção.

## O que cada despacho implica (Onda 1)

| Se A (recomendado) | Se B |
|---|---|
| 1.1 exportador `.py`→`.json` + validador; 1.7 loader lê JSON; `.py` vira gerado e aposenta | 1.1b `schema.sql` + importador + `db_build.py`; loader lê `.db`; `.py` aposenta igual |
| 1.3 BIBLIO→JSON; 1.5 `via`/`confianca_fonte` viram chaves | Idem, viram colunas |
| FTS5 (3.2) via `.db` derivado | FTS5 direto no `.db` de trabalho |
| Esforço: baixo–médio | Esforço: médio |

---

*Parecer lavrado pelo agente de engenharia em 12/09/2026. Devolver ao Assistente Auditor como revisor (item 7 do encaminhamento).*
