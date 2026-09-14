# CERTIDÃO — U54 · R1 · LOTE 11
## O lote natural da B021 — e a exceção que não se sustenta na fonte

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 11 = lote natural da B021 (*Tempos Difíceis no Olimpo*), com prioridade à liquidação de dívidas técnicas: processar os códigos nativos e **resgatar a RC‑300**, ancorada nesta fonte desde a U52
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. O que o lote materializou

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑300 | Dissolução da Tríade (2015–2017) | 7 |

**1 ficha · 7 fragmentos verbatim intra-linha · 0 falhas** (conferência do driver e conferência independente, ambas limpas).

A RC‑300 estava ancorada na B021 desde a U52, quando a excluí do lote da B022 por não ter sustentação naquela obra. O censo atribui-lhe família B **por esta passagem**, e aqui ela se cumpre.

## 2. Divergência interna da fonte — terceira ocorrência do padrão

A obra grafa o mesmo acontecimento de **dois modos**:

| Formulação | Linha | Trecho |
|---|---|---|
| Pontual | B021 L5384 | «Somente quando a Tríade **implodiu no ano de 2015**, é que a percepção da…» |
| Intervalar | B021 L5408–L5411 | «a dissolução da Tríade, levada a efeito **entre os anos terrestres de 2015 e 2017**, que Caos, Eros e Tártar assumiram a falência da…» |

O cadastro registra o intervalo (2015–2017), que é o do verbete. **As duas formulações estão citadas *verbatim*; nenhuma foi normalizada.** É a terceira aplicação do mesmo critério, depois de Terrenos × TERRESTRES (RC‑362, U51) e travessão × hífen (RC‑313, U52) — o padrão está consolidado.

**Quem é a Tríade** a fonte o diz expressamente — «Caos, Eros e Tártar» (L5411) —; a ficha não o deduz de mitologia comparada.

## 3. ⚠️ ACHADO — RC‑296 não se sustenta na B021

O poço que o censo atribui à B021 tinha 2 códigos. Só **1** se sustenta:

| Cód. | Verbete | Situação |
|---|---|---|
| RC‑300 | Dissolução da Tríade (2015–2017) | B021 L5365‑5408 ✓ **materializada** |
| **RC‑296** | Pitonisas e Oráculos (Apolo/Delfos) | **a evidência do censo é uma PALESTRA** — P2023‑05‑21 L3‑37 |

**O que verifiquei, por três vias:**

1. **Localizador (chave «pitonisas e oraculos» na B021): 0 blocos.** A expressão do cadastro não ocorre como tal em nenhuma linha do livro.
2. **Busca solta:** os componentes *ocorrem* — «pitonisa» (L4614, L5097, L5099, L5104), «oráculo» (L3320, L3618, L4614, L5020, L5025, L5028, L5031, L5046), «Delfos» (L1908, L1919, L5100, L5103), «Apolo» (71 vezes). Há mesmo uma passagem excelente sobre a matéria (L5095–L5112: o método de controlar a humanidade «por meio das pitonisas, dos oráculos», a origem do nome em Píton e nos jogos píticos de Delfos).
3. **Evidência do censo v3 para RC‑296:** `P2023-05-21 L3-37` — ou seja, a família B deste código foi decidida **por uma palestra**, não pela B021.

**Consequência:** a RC‑296 cai sob o despacho de congelamento da série P — a sua única sustentação censitária é oral, e a B021 não a carrega sob a forma do nome.

**Não materializei a ficha.** Sob o Portão de Paridade Verbatim e pelo precedente da U53 (onde recusei inferir «Mundo das Águas = Terra» sem âncora explícita), um código cujo **nome** não ocorre na fonte não deve ser materializado por aproximação de matéria.

**Submeto ao Curador duas vias:**

- **(a) Manter congelada** — RC‑296 aguarda o protocolo da série P, quando a evidência oral (P2023‑05‑21 L3‑37) poderá ser citada com regra própria. **É o que resulta dos despachos vigentes, e foi o que fiz.**
- **(b) Autorizar por despacho expresso a materialização pela B021**, com a ficha declarando que o nome do verbete não ocorre literalmente na obra, e ancorando-se em L5097 («por meio das pitonisas, dos oráculos e outros possíveis de serem impostos aos desavisados humanos»), L5099 («Por que a denominação “pitonisa”?») e L5100–L5107 (Delfos, Píton, Apolo).

Se (b) for a escolha, fica desde já registrado que se trata de **excepção consciente ao Portão de Paridade**, e não de precedente automático para os demais códigos.

## 4. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; a ficha nasce 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slug ASCII:** `dissolucao-da-triade-2015-2017` — conforme a obrigatoriedade agora estabelecida para todas as fichas da R1.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada. O `diff` do registro-mestre é só o sinalizador `ficha` da RC‑300.
- **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 776). Nenhum teste da suíte os fiscaliza.

| Indicador | Antes (U53) | Depois (U54) |
|---|---:|---:|
| **Fichas** | 775 | **776** |
| **GAP** | 171 | **170** |
| Família B v3 — restantes | 65 | **64** (45 activos + 19 congelados) |
| B021 — sustentáveis na B021 | 1 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B048 5 · B052 4 · B019 4 · B006 4 · B036 3 · B023 3 · B050 3 · B002 2 · B014 2 · B020 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 776 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 776 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 776 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U54-R1-LOTE11-2026-09-13.json` · `termos/RC-300-dissolucao-da-triade-2015-2017.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
