# onda_incremental_dry_run

**Iniciada em:** 2026-10-22
**Estado:** normalização concluída; aguardando o mapeamento dos eixos temáticos.

Esta é uma área de processamento exclusivamente derivada dos seis brutos do
piloto STT. Ela é fisicamente separada de `normalizados_stt_dry_run/` e não
altera nenhuma fonte em `uploads_recepcao/`.

## Produtos

| Caminho | Conteúdo |
|---|---|
| `INVENTARIO-FONTES.md` | inventário humano dos seis brutos, IDs e hashes confirmados |
| `manifesto-fontes.json` | proveniência estruturada das fontes de entrada |
| `derivados_normalizados/` | as seis cópias normalizadas; não são brutos |
| `manifesto-derivados.json` | hashes de saída, hash de origem e quantidade de trocas por derivado |
| `rastreio-antes-depois.jsonl` | cada substituição com regra, posição e contexto da fonte |
| `RELATORIO-NORMALIZACAO.md` | confirmação humana, censo e limites do processamento |

## Regras executadas

Somente as oito regras `AUTOMÁTICA` da seção 2.1 de
`diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md` foram aplicadas ao corpo Markdown. Frontmatter YAML e URLs
foram mantidos byte a byte; regras contextuais, itens em revisão e formas
preservadas ficaram fora desta execução.

| Regra | DE | PARA | Trocas | Âncora canônica |
|---|---|---|---:|---|
| `STT-A01` | `anunaki` | **Anunnaki** | 6 | RC-024 — Anunnaki |
| `STT-A02` | `trimurte` / `trimurto` | **Trimurti** | 9 | RC-104 — Trimurti |
| `STT-A03` | `vismo` / `visma` / `vizno` | **Vishnu** | 20 | RC-135 — Vishnu (Mavatna) |
| `STT-A04` | `pachupati` / `pachupato` | **Pashupati** | 4 | RC-669 — Pashupati |
| `STT-A05` | `tikkun` | **Tikun** | 4 | RC-514 — Tikun Cósmico |
| `STT-A06` | `mohensof` / `mohenso` | **Mohen So** | 5 | RC-081 — Mohen So |
| `STT-A07` | `tirtankaras` | **Tirthankaras** | 1 | RC-397 — Tirthankaras |
| `STT-A08` | `tote` / `toth` | **Thoth** | 3 | RC-463/RC-534 — Thoth |

**Total:** 52 substituições, em 6 derivados.
**Idempotência:** verificada.
**Alterações nos brutos:** 0.
