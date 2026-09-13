# Certidão U42 — Rota R1, lote 1 da família B (8 fichas) + achado de governança (13/09/2026)

**Despacho do Curador (13/09/2026):** concluído o piloto R1 (U41), «seguir na família B (63 restantes)».

## 1. O lote

Ranking por ocorrências no `CENSO-GAP-FICHAS-2026-09-13.json` — os 8 primeiros dos 63:

| # | Código | Termo | Occ | Ficha | Fragmentos verbatim |
|---|---|---|---|---|---|
| 1 | RC-108 | Universo Paralelo | 292 | `termos/RC-108-universo-paralelo.md` | 4 |
| 2 | RC-085 | Orbum | 233 | `termos/RC-085-orbum.md` | 3 |
| 3 | RC-065 | Frota Norte | 208 | `termos/RC-065-frota-norte.md` | 3 |
| 4 | RC-066 | Genos | 152 | `termos/RC-066-genos.md` | 3 |
| 5 | RC-540 | Molécula-mãe | 142 | `termos/RC-540-molecula-mae.md` | 2 |
| 6 | RC-077 | Lokas | 134 | `termos/RC-077-lokas.md` | 3 |
| 7 | RC-044 | Cultura Demo | 116 | `termos/RC-044-cultura-demo.md` | 6 |
| 8 | RC-392 | Reforma Íntima (Grupo Atlan) | 99 | `termos/RC-392-reforma-intima.md` | 4 |

**28 fragmentos verbatim**, todos conferidos byte a byte contra o `original.txt` da fonte
declarada — 0 falhas na primeira passada. Neste lote **7 dos 8 renderam ao menos uma sentença
completa intra-linha** (exceção: RC-044, cujas duas sentenças do verbete estão partidas em três
pedaços cada uma pelo hard-wrap de B031).

**Novo instrumento:** `ferramentas/materializar_lote.py` — driver genérico por lote (os dados
moram em `diagnostico/U42-R1-LOTE1-2026-09-13.json`), para não repetir 400 linhas a cada lote.

## 2. Achado de governança — parei e corrigi

Ao virar o cadastro, o script marcaria os 8 como `verificado` (🟢), copiando o gesto da U30/U41.
**Verifiquei antes de fechar: nenhum dos 8 consta de qualquer `chancela/P7-*.csv`** — nunca
passaram por leva. Ali o 🟢 era legítimo porque o **V do Curador já existia**, suspenso apenas pela
trava §7 «sem ficha → bloqueia»; aqui o V **não existe**, e marcá-los 🟢 seria **autocancela**.

**Correção executada:** as 8 fichas nascem **🟡 provisório** (`confianca_fonte = média`, pela regra
do loader), com `ficha=False → True`. O driver passou a exigir `aplicar_V: true` no lote para
promover a verificado, e cada ficha carrega a nota:

> **Status de nascença:** 🟡 **provisório** — este código nunca passou por leva de chancela
> (nenhuma planilha `chancela/P7-*.csv` o contém): a materialização da ficha foi despachada,
> o **V não**, e marcar 🟢 sem chancela seria autocancela. A ficha segue para a próxima leva de
> chancela, com as citações já extraídas e conferidas.

**Consequência para o Curador:** os 55 códigos restantes da família B **não têm V** (só os 17
suspensos do HOLD o têm). Se o senhor quiser que os lotes seguintes já nasçam 🟢, é preciso um
despacho que o autorize explicitamente (ou a chancela em leva, o que é o curso natural da casa).
Sem isso, todo lote nasce 🟡 e vai a leva depois.

## 3. Provas

- Suíte `ferramentas/test_suite.py`: **21 testes, 21 verdes**.
  - T13 frontmatter: **689 fichas** · T14 tabelas == cadastro: **0 divergentes** ·
    T15 `motor.fm_toml` == frontmatter: **689 conferidas · 0 divergentes**.
- `verificar_verbetes.py`: **Base intacta: 946 termos · 689 fichas · 1887 relações**.
- Builds na ordem do rito; `RELACOES` **intocado** (1887 — 0 arestas abertas, fechadas ou
  reetiquetadas).

## 4. Contas

- Status: **60⚪ · 228🟡 · 102🟠 · 556🟢** (inalterado — as 8 novas entram já no 🟡).
- Gap de fichas: **265 → 257**. Família B: **63 → 55**.

## 5. Próximo

Lote 2 da família B — próximos 8 do ranking: RC-032 Benem · RC-048 Demiurgo · RC-073 Keshava ·
RC-123 Val Eno · RC-095 Rogério de Almeida Freitas · RC-438 Tubal · RC-374 Mordon · RC-211
Kundalini.
