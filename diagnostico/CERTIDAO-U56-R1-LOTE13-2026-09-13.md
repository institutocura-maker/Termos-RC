# CERTIDÃO — U56 · R1 · LOTE 13
## O bloco de fonte única da B052 (*Homoafetividade: o Segredo Perdido do Éden*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 13 APROVADO (a B052) · **segregação livro a livro mantida** («não misture fontes no mesmo lote») · jurisprudência da etiqueta de divergência **homologada** · critério do poço congelado **cristalizado**
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As três fichas

| Cód. | Verbete | Frag. | Posição na obra |
|---|---|---:|---|
| RC‑435 | O Segredo Perdido do Éden | 6 | **subtítulo do próprio livro** |
| RC‑439 | Os Magos do Norte | 5 | capítulo 8 |
| RC‑440 | A Sina dos Portadores | 4 | capítulo 11 |
| | **3 fichas** | **15** | |

**B052: 3 → 0** (quanto ao sustentável). Sétima obra liquidada pela via expressa, e a primeira em que o lote rende menos de 5 fichas — efeito esperado do esgotamento dos blocos maiores.

## 2. RC‑435 — divergência tipográfica no **próprio título da obra**

A B052 grafa o seu título de **duas maneiras**:

| Posição | Linha | Grafia |
|---|---|---|
| CRÉDITOS | B052 L9444 | «Homoafetividade**:** O Segredo Perdido do Éden» (dois‑pontos pegado à palavra; caixa de título) |
| Registro CIP | B052 L9456 | «Homoafetividade **:** o segredo perdido do Éden» (dois‑pontos com espaço antes; caixa baixa) |

Divergem a **pontuação** e a **caixa**. **Etiquetada** com `[⚠️ DIVERGÊNCIA INTERNA DA FONTE]`, por aplicação directa da regra homologada neste despacho: pontuação diferente é contradição **tipográfica estrutural**, não convenção de formatação.

**Caso‑limite não etiquetado:** na fala de Maneton, a expressão surge como «um segredo perdido **do jardim** do Éden» (L6865) — artigo indefinido e locução acrescentada. Não se etiquetou: é **variante da prosa da personagem**, não grafia do termo. Fica registrado no despacho de jurisprudência como caso‑limite.

## 3. Convenção gráfica — o critério homologado em acção

Nesta obra **os títulos dos capítulos só comparecem no SUMÁRIO**; no corpo, a expressão ocorre como linguagem corrente, em minúscula (L4610, L5206, L7286 «dos magos do norte»; L6253 «sina dos portadores da peste», entre aspas). As duas posições vão *verbatim* e **sem etiqueta** — exactamente o critério homologado pelo Curador neste despacho.

## 4. RC‑270 fica para o lote natural da B013

O poço que o censo atribui à B052 tinha 4 códigos; **3 se sustentam nela**:

| Cód. | Verbete | Situação |
|---|---|---|
| RC‑435 · RC‑439 · RC‑440 | — | B052 ✓ **materializadas** |
| **RC‑270** | Linhagem dos Patriarcas Hebreus | **a evidência do censo é toda da B013** (L100‑129, L905‑945, L31‑65) |

É o **segundo caso do mesmo padrão** — o primeiro foi RC‑300, ancorada na B021 pela U52 e resgatada na U54. RC‑270 fica proposta para o **lote natural da B013**, sem misturar fontes.

## 5. Jurisprudência da etiqueta — despacho lavrado

`diagnostico/DESPACHO-JURISPRUDENCIA-ETIQUETA-DIVERGENCIA-2026-09-13.md` consolida a regra com os casos já lavrados:

- **acciona** a etiqueta: RC‑362 (Terrenos × TERRESTRES), RC‑313 (travessão × hífen), RC‑300 (2015 × 2015‑2017), RC‑435 ("**:**" × " **:**");
- **não acciona**: B005 (caixa alta espaçada × caixa normal), B015 (Endrelnianos × endrelnianos), B048 (caixa alta × caixa normal), B052 (sumário × corpo em minúscula);
- **critério operativo**: a pergunta é «a diferença altera o **termo**, ou apenas o **modo de o imprimir**?»; e, em caso de dúvida, **etiqueta‑se e diz‑se porquê**.

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 3 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 3. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 3 sinalizadores `ficha`.
- **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 784). Nenhum teste da suíte os fiscaliza.

| Indicador | Antes (U55) | Depois (U56) |
|---|---:|---:|
| **Fichas** | 781 | **784** |
| **GAP** | 165 | **162** |
| Família B v3 — restantes | 59 | **56** (36 activos + 20 congelados) |
| **B052 — sustentáveis** | 3 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B019 4 · B006 4 · B036 3 · B023 3 · B050 3 · B002 2 · B014 2 · B020 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 784 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 784 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 784 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/DESPACHO-JURISPRUDENCIA-ETIQUETA-DIVERGENCIA-2026-09-13.md` · `diagnostico/U56-R1-LOTE13-2026-09-13.json` · `termos/RC-435-o-segredo-perdido-do-eden.md` · `termos/RC-439-os-magos-do-norte.md` · `termos/RC-440-a-sina-dos-portadores.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
