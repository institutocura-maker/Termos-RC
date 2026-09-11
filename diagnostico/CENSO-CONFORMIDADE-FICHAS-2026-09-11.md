# Censo de Conformidade das Fichas — 11/09/2026

Leitura pura (nenhum arquivo alterado). Universo: **671 fichas** em `termos/RC-*.md`. Modelo: `01-ficha-modelo.md`.

## 1. Sumário executivo

- Fichas sem badge `| **Status** |` única: **1** RC-396)
- Divergências badge↔cadastro: **0** (sincronia perfeita)
- Tabelas `## Fontes` malformadas/vazias/ausentes: **184** (27.4%)
- `[REVISAR]` abertos (reais): **18** ocorrências
- Blocos `Ampliação/Atualização/Reforço`: **2323** no total (média 3.5/ficha)
- Notas de processo (`## Nota`): **336** no total

## 2. Seções do modelo ausentes (nº de fichas)

| Seção | Ausente em | % |
|---|---|---|
| Definição Sintética | 4 | 0.6% |
| Contexto / Origem | 155 | 23.1% |
| Etimologia / Grafias | 269 | 40.1% |
| Fontes | 74 | 11.0% |
| Citações-chave | 313 | 46.6% |
| Termos Relacionados | 127 | 18.9% |
| Seres Associados | 349 | 52.0% |
| Observações | 267 | 39.8% |

## 3. Top-15 dossiês (por nº de blocos)

| Código | Título | Blocos | Notas | Linhas | Status |
|---|---|---|---|---|---|
| RC-001 | Javé | 67 | 1 | 497 | verificado |
| RC-009 | Sophia (Cristo Cósmico) | 65 | 5 | 496 | verificado |
| RC-072 | Jesus | 59 | 2 | 455 | verificado |
| RC-104 | Trimurti | 51 | 5 | 349 | verificado |
| RC-092 | Quarto Logos (Olm / Codificador de Zian) | 37 | 4 | 280 | verificado |
| RC-454 | Elm (Moros — ser LM de Tempérion) | 28 | 4 | 308 | em análise |
| RC-102 | Shiva (Savna) | 27 | 5 | 237 | verificado |
| RC-005 | Segundo Advento do Cristo (Volta de Jesus) | 26 | 1 | 194 | em análise |
| RC-037 | Brahma (Brajna) | 26 | 2 | 225 | verificado |
| RC-727 | DNA Insubmisso / Linhagem Pandora–Eva–Noreia | 26 | 2 | 185 | em análise |
| RC-414 | Krishna (avatar de Vishnu/Shiva) | 25 | 3 | 215 | verificado |
| RC-395 | Ragnarok em Marte | 22 | 1 | 163 | verificado |
| RC-002 | Rebelião de Lúcifer | 20 | 4 | 205 | verificado |
| RC-086 | Pandora | 20 | 1 | 199 | em análise |
| RC-565 | Hochmah (2ª Sefirah — Sabedoria; = Sophia) | 20 | 2 | 191 | verificado |

## 4. Fichas com `[REVISAR]` aberto

| Código | Ocorrências | Status |
|---|---|---|
| RC-091 | 4 | verificado |
| RC-036 | 3 | verificado |
| RC-777 | 3 | verificado |
| RC-102 | 2 | verificado |
| RC-120 | 2 | provisório |
| RC-281 | 2 | em análise |
| RC-012 | 1 | em análise |
| RC-425 | 1 | verificado |

## 5. Leitura crítica (conclusão do censo)

1. **O modelo v2 não descreve o uso real**: 46,6% das fichas não têm `Citações-chave`; 52,0% não têm `Seres Associados`; 40,0% não têm `Etimologia`. O formato de facto é *dossiê-acumulativo*, não *ficha-síntese**.
2. **27,4% das tabelas de Fontes não são confiáveis** (malformadas, vazias ou ausentes) — confirma a necessidade do parser com fallback.
3. **Concentração**: as 4 maiores fichas (001/009/072/104) somam 232 blocos (10% do total de 2.323).
4. **336 notas de processo** embutidas nas fichas (metadados operacionais misturados ao conteúdo).
5. Ponto positivo: **sincronia badge↔cadastro em 100%** e só 1 ficha sem badge única.