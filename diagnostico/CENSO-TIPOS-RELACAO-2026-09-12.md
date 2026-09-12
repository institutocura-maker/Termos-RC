# Censo de tipos de relação — proposta de doma — Onda 1.4 (12/09/2026)

**279 tipos** em 1889 lançamentos. Top-10 + cauda hapax (≤2 usos).

## Top-15

| Tipo | Usos |
|---|---|
| relaciona-se-a | 888 |
| é-um | 117 |
| envolve | 102 |
| variação | 78 |
| inclui | 64 |
| associado-a | 40 |
| usa | 30 |
| parte-de | 24 |
| opõe-se-a | 17 |
| ocorre-em | 16 |
| aplica-se-a | 14 |
| distingue-se-de | 13 |
| sinônimo | 11 |
| manifesta-se-em | 9 |
| realiza | 9 |

Hapax (≤2 usos): **223 tipos** — rotulação livre, não vocabulário controlado.

## Clusters candidatos a fusão (mesmo radical, flexão distinta)

Proposta do agente — **nada fundido sem despacho**. Cada grupo: manter todos, eleger 1 canônico, ou reescrever.

- `alimenta`: alimenta (2x), alimenta-se-de (1x)
- `aplica`: aplica-a (1x), aplica-se-a (14x)
- `armazenada`: armazenada-em (1x), armazenadas-em (2x)
- `atua`: atua-em (7x), atua-por (1x)
- `conecta`: conecta (1x), conecta-se-por (2x)
- `criada`: criada-por (1x), criadas-por (1x)
- `criado`: criado-por (4x), criados-por (1x)
- `cumpre`: cumpre (2x), cumpre-se-em (1x)
- `explicado`: explicado-por (1x), explicados-por (1x)
- `inicia`: inicia (4x), inicia-em (1x)
- `opera`: opera-em (1x), opera-por (1x)
- `organiza`: organiza (3x), organiza-se-em (2x)
- `origem`: origem-de (1x), origem-em (8x)
- `origina`: origina (1x), origina-de (1x), origina-em (5x)
- `propõe`: propõe (2x), propõe-a (1x)
- `responde`: responde-a (1x), responde-por (2x)
- `resulta`: resulta-de (2x), resulta-em (7x)
- `risco`: risco-de (1x), risco-para (1x)
- `sucede`: sucede (7x), sucede-por (1x)
- `transfere`: transfere (1x), transfere-para (3x)
- `transportado`: transportado-por (1x), transportados-por (1x)

## Recomendação do agente
Declarar o campo `tipo` como **rótulo livre** (prosa curta, não enum) + fundir só os clusters acima com canônico óbvio (ex.: criada-por/criados-por/criadas-por → criados-por? ou forma neutra?). Vocabulário controlado de ~20 tipos seria projeto curatorial à parte (Onda 2+), não manutenção.