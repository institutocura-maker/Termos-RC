# CERTIDÃO — U75 · R1 · LOTE 32
## A B049 (*Jesus e Nietzsche*) — RC‑372 «O Ser Humano Emancipado»

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 32 APROVADO (a B049) · VIA (a) mantida · verificação dupla de HEAD
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. A ficha

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑372 | O Ser Humano Emancipado | 10 |

**B049: 1 → 0.** Vigésima sexta obra liquidada. **10 fragmentos · 0 falhas** na conferência.

## 2. ⚠️ O Portão B recusou a primeira redação — e recusou com razão

Esta obra trouxe um artefato de ficheiro inédito: **7 886 das 8 959 linhas** trazem o carácter **TAB (U+0009)** onde o livro impresso tem ESPAÇO.

```
L65: 'O\tSer\tHumano\tEmancipado'
```

Redigi primeiro a citação na **forma impressa** (com espaços), por entender que a tabulação é aparelho de transcrição. **O Portão B recusou:** ele compara byte a byte.

**A recusa estava certa, e por três razões que se reforçam:**

1. **U50** — a normalização serve só para LOCALIZAR; o texto citado preserva os caracteres do ficheiro.
2. **U58** — normalizar o `original.txt` agora seria higienização no meio da esteira de extração. **Vedado.**
3. **A função do Portão** — é exactamente impedir que o motor decida sozinho o que «o livro queria dizer».

**Decisão executada:** a ficha cita os **bytes exactos** do ficheiro (com as tabulações), e **registra o artefato**, para que não se leia a tabulação como grafia do livro.

**Fica proposto para o Encerramento (frente 2 — higienização):** a normalização de TAB → ESPAÇO nesta obra, com reemissão da ficha. Não se fez agora, porque a esteira de extração não se interrompe para higienizar.

## 3. A obra **define** o termo — e a ficha a deixa defini‑lo

> «**Este** é o ser humano emancipado, **livre, aquele que pensa**, o que **não mais se encontra condicionado pelas “sombras da caverna”**, pelo mito da crença em um “deus estranho e tresloucado”, a quem todos devem temer sob pena de serem castigados. **É escravidão pura!**»

(L3731–L3734, no capítulo que o termo intitula)

## 4. O antecedente: a caverna de Platão — registrado como antecedente, não como equação

«a “caverna” é o mundo perceptível […] as “sombras” são as coisas as quais damos importância […] as “amarras” ou “grilhões” são os nossos **tabus e preconceitos**; o “instrumento” que quebra os “grilhões”, é a **reflexão**; e o “prisioneiro” que escapa, é o **filósofo**» (L3721–L3727); «**conhecer a si mesmo** é um ato de iluminação e de libertação, que passa sempre pela **educação do indivíduo**» (L3728–L3730).

A ficha registra o encadeamento e o «Este» que o retoma — **sem converter a sequência em identidade formal** que a fonte não enuncia nesses termos (disciplina da RC‑233, U68).

## 5. ⭐ A abstenção central: **não é o super‑homem**

> «**Mais que** o “homem de Schopenhauer” ou mesmo o “**super-homem de Nietzsche**”, penso que surgirá, ainda, um modelo de ser humano **esclarecido, equilibrado e, acima de tudo, emancipado** – que estabelecerá o único modo de se viver dignamente – em relação aos “grilhões” genéticos e psíquicos que “enjaulam” […] o precioso “eu” advindo da natureza humana»

(L3241–L3246)

O «**mais que**» é da fonte. A ficha **não funde** o ser humano emancipado com o «super-homem»/«além-homem» (Übermensch), que o mesmo capítulo descreve separadamente, com o «amor pelo destino» (L3742–L3757).

## 6. Alargamento (§6) e efeito na Base

Os blocos do censo eram «L43‑83», «L3712‑3757» e «L7917‑7919». A passagem que **distingue** o emancipado do super‑homem (L3241–L3243) ficava fora. **Décimo primeiro uso consecutivo do §6.**

- **V revogado mantido:** `"v_revogado": true`, sem `aplicar_V`; a ficha nasce 🟡. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slug ASCII.** Nenhuma aresta nova. O `diff` do cadastro é **1 linha**.
- **Verificação dupla de HEAD** aplicada. **Espelhos adiados** (768 vs Base 818).

| Indicador | Antes (U74) | Depois (U75) |
|---|---:|---:|
| **Fichas** | 817 | **818** |
| **GAP** | 129 | **128** |
| Família B v3 — restantes | 23 | **22** (2 activos + 20 congelados) |
| **B049 — restantes** | 1 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

**Activos restantes: RC‑377 (B043) · RC‑931 (B016).** — dois para o zero.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 818 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 818 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 818 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U75-R1-LOTE32-2026-09-13.json` · `termos/RC-372-ser-humano-emancipado.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`. Verificação dupla de HEAD: abertura e encerramento.*
