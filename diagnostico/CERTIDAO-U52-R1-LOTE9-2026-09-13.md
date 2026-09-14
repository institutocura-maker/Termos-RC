# CERTIDÃO — U52 · R1 · LOTE 9
## O lote natural da B022 (*Inquisição Trimurtiana – Tempo de Apostasia*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 9 APROVADO como **lote natural da fonte B022** — «duplamente estratégico: liquida mais uma fonte de um único golpe e captura adequadamente a RC-309, recém-promovida ao poço da R1 graças à v3 do censo»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. | Natureza |
|---|---|---:|---|
| RC‑309 | Ordem dos Indecifráveis | 9 | capítulo 9 da B022 |
| RC‑313 | Tempo de Apostasia | 7 | **subtítulo da própria obra** |
| | **2 fichas** | **16** | |

16 fragmentos verbatim intra-linha conferidos byte a byte, **0 falhas** na primeira passada (pré-conferência em bloco único, como nas U49–U51).

## 2. RC‑309 — o ciclo da v3 fecha-se aqui

Este é o código que a **regra nova do localizador** (caixa alta espaçada) resgatou de D para B na U50, e que o Curador mandou **reportar antes de processar**. Fica agora materializado:

```
B022 L5338: O S  A D H Y T I A  E  A  “ O R D E M  D O S  I N D E C I F R Á V E I S ”
```

O ciclo completo, em três unidades: **U50** achou (D → B) · **U51** homologou a regra e a guarda E3 e manteve o código no poço, intocado · **U52** materializou. Nenhum atalho: foi reportado antes de processado, exactamente como despachado.

**Rigor que a ficha guarda:** a expressão no plural só ocorre no SUMÁRIO (L29) e no título do capítulo (L5338). No corpo, o termo comparece no **singular** — «o Indecifrável» — e os **Adhytia** são apresentados à parte (L5584–L5585). **A ficha não afirma que a «Ordem dos Indecifráveis» seja o conjunto dos Adhytia nem do «Indecifrável»**: essa relação não está escrita na fonte e não foi inferida. O que a ficha traz é a auto-definição do ser («cuidei de a tudo “esconder” e, por isto, sou o “Indecifrável” dentre todos vós») e a interpelação de Brahma («Ó Indecifrável, tu és a temida certeza obscura que sempre a nossa ciência apontou como sendo passível de existir»).

## 3. RC‑313 — o verbete é o subtítulo do livro

A B022 intitula-se *Inquisição Trimurtiana* **– Tempo de Apostasia** (folha de rosto, L5–L6). A ficha apoia-se na descrição que o **próprio catálogo editorial da obra** faz do livro (L7158–L7164):

> «Narrativa de um impensável debate entre os Senhores da Trimurti — Brahma, Vishnu e Shiva — em torno da falência da política por eles praticada desde o início dos tempos da criação universal, cujo final aponta para a mais singular ocorrência já acontecida entre os seres que residem nesse ambiente paralelo (…)»

Apresentada como o que é — **descrição editorial/autoral** —, não como definição doutrinária.

**Divergência de pontuação dentro da própria obra**, preservada sem normalização: o catálogo grafa «Inquisição Trimurtiana **–** Tempo de Apostasia» (L7158, travessão) e a ficha de créditos grafa «Inquisição Trimurtiana **-** Tempo de Apostasia» (L7270 e L7283, hífen). As duas formas estão citadas.

## 4. RC‑300 fica para o lote natural da B021

O poço que o censo atribui à B022 tinha **3 códigos**; sustentam-se na B022 só **2**:

| Cód. | Verbete | Situação |
|---|---|---|
| RC‑309 | Ordem dos Indecifráveis | B022 · **materializada** |
| RC‑313 | Tempo de Apostasia | B022 · **materializada** |
| **RC‑300** | Dissolução da Tríade (2015–2017) | **a família B assenta-se na B021** (L5365‑5408); a expressão não ocorre na B022 |

**RC‑300 não foi processada neste lote.** O critério do Curador é liquidar blocos de fonte única de um só golpe: trazê-la aqui seria misturar fontes e citar a B021 dentro de um lote da B022. Fica proposta para o **lote natural da B021**, onde terá sustentação própria. Assinalo a decisão para o Curador ratificar ou emendar.

## 5. Espelhos .xlsx e .docx — PULADOS POR DESPACHO

O Curador observou o custo de reconstruir os dois espelhos a cada rodada e autorizou adiá-los para o fim da sessão. Foram, portanto, executados apenas:

```
build_indice.py     ✓ 946 linhas
exportar_json.py    ✓ 946 termos · 1887 relações · round-trip limpo  (T12 depende dele)
build_readme.py     ✓ 946/770/1887/102
build_xlsx.py       — PULADO
build_word.py       — PULADO
```

**DÍVIDA REGISTRADA:** `base-terminologica.xlsx` e `base-terminologica-leitura.docx` estão congelados em **768 fichas**, enquanto a Base já tem **770**. Verifiquei antes que **nenhum teste da suíte fiscaliza esses dois arquivos** (T10 HOLD · T11 parser · T12 canônico · T13 frontmatter · T14 tabelas · T15 fm_toml), de modo que adiá-los não enfraquece a verificação. **Falta reconstruí-los no encerramento da sessão.**

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada.
- O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.

| Indicador | Antes (U51) | Depois (U52) |
|---|---:|---:|
| **Fichas** | 768 | **770** |
| **GAP** | 178 | **176** |
| Família B v3 — restantes | 72 | **70** |
| B022 — sustentáveis na B022 | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Próximos poços: **P2024‑11‑30 6 · B015 5 · B048 5 · P2021‑02‑28 5 · B052 4 · B019 4 · B006 4 · B036 3**.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 770 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 770 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 770 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U52-R1-LOTE9-2026-09-13.json` · `termos/RC-309-ordem-dos-indecifraveis.md` · `termos/RC-313-tempo-de-apostasia.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
