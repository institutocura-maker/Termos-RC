# CERTIDÃO — U55 · R1 · LOTE 12
## O bloco de fonte única da B048 (*Favor Divino*) + RC‑296 no inventário congelado

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 12 APROVADO (os 5 da B048) · **RC‑296: via (a) — MANTER CONGELADA**, com transferência ao inventário da série P
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As cinco fichas

| Cód. | Verbete | Frag. | Cap. |
|---|---|---:|---|
| RC‑337 | Humanos: uma simples Experiência Biológica | 6 | 1 |
| RC‑338 | O Reconhecimento que nunca veio | 6 | 10 |
| RC‑339 | A Difícil Cobrança sobre os Humanos | 6 | 9 |
| RC‑340 | Atores de uma Peça Incompreensível | 6 | 7 |
| RC‑341 | Ferramentas do Favor Divino | 6 | 3 |
| | **5 fichas** | **30** | |

**B048: 5 → 0.** Sexta obra liquidada de um só golpe.

## 2. O portão B barrou três fragmentos — e nada foi escrito

Na primeira passada, a RC‑337 veio com **3 fragmentos deslocados de uma linha** (eu os transcrevera em L106–L108; estão em **L105–L107**). O `materializar_lote.py` levantou o **Portão B** e abortou:

```
AssertionError: PORTÃO B · B048 L106: trecho NÃO confere byte a byte
  trecho : 'aspecto que dá sustentação ao porquê das “coisas serem com elas são”, em'
  linha  : 'especial para o lado dos humanos da Terra — existem “humanos” que não'
```

Corrigidos os três, nova conferência: **30 fragmentos · 0 falhas**, e só então as 5 fichas foram materializadas. É a quinta vez que o mecanismo pega um erro meu de transcrição antes da escrita (U47, U49, U51, U52 confirmam a regra: **conferir numa passada única, antes de invocar o driver, e nunca confiar na memória da leitura**).

## 3. Convenção gráfica × divergência do termo — uma distinção que propus e apliquei

Nesta obra **todos os cinco** verbetes são títulos de capítulo que a fonte grafa em **duas posições**:

| Posição | Exemplo (RC‑337) |
|---|---|
| SUMÁRIO (L37) | «Humanos: uma simples Experiência Biológica» |
| Corpo (L103) | «HUMANOS: UMA SIMPLES EXPERIÊNCIA BIOLÓGICA» |

As duas posições estão citadas *verbatim* em cada ficha, sem normalização. **Não lhes pus, porém, a etiqueta `[⚠️ DIVERGÊNCIA INTERNA DA FONTE]`**, e é esta a distinção que submeto ao Curador:

- as **palavras** são as mesmas; o que muda é a **caixa** — é uma **convenção gráfica da obra** (SUMÁRIO em caixa normal, títulos de capítulo em caixa alta no corpo), sistemática nos 5 casos;
- a etiqueta ⚠️ foi reservada, até aqui, para os casos em que **o próprio termo diverge**: Terrenos × TERRESTRES (RC‑362, U51), travessão × hífen (RC‑313, U52), 2015 × 2015‑2017 (RC‑300, U54).

Tagar os 5 por diferença de caixa diluiria o sinal da etiqueta. Se o Curador preferir a regra inversa (etiquetar toda e qualquer diferença gráfica entre posições), o critério fica desde já registrado para revisão.

## 4. RC‑296 transferida ao inventário congelado

Cumprida a via (a): a **RC‑296** integra agora o inventário da série P (adendo ao `DESPACHO-CONGELAMENTO-SERIE-P-2026-09-13.md`).

Ficou consignado que **o critério de pertença ao poço congelado não é «declara fonte P», mas «a evidência literal é oral»** — o que mantém intacta a salvaguarda dos códigos mistos (RC‑337 e RC‑341, deste lote, declaram palestras e foram processados, porque se sustentam na B048).

E ficou escrito, para constar: **nenhuma excepção consciente ao Portão de Paridade foi aberta.** Não há nesta base ficha alguma materializada por aproximação de matéria.

| Poço da R1 (família B v3, após o lote 12) | Códigos |
|---|---:|
| **Activo — livros** | **39** |
| **Congelado — evidência oral** | **20** (19 + RC‑296) |

## 5. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 5 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nos 5, conforme a obrigatoriedade estabelecida na U54.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada. O `diff` do registro-mestre são só os 5 sinalizadores `ficha`.
- **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 781). Nenhum teste da suíte os fiscaliza.

| Indicador | Antes (U54) | Depois (U55) |
|---|---:|---:|
| **Fichas** | 776 | **781** |
| **GAP** | 170 | **165** |
| Família B v3 — restantes | 64 | **59** (39 activos + 20 congelados) |
| **B048 — restantes** | 5 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B052 4 · B019 4 · B006 4 · B036 3 · B023 3 · B050 3 · B002 2 · B014 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 781 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 781 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 781 fichas · 1887 relacoes
```

**Artefatos:** adendo ao `diagnostico/DESPACHO-CONGELAMENTO-SERIE-P-2026-09-13.md` · `diagnostico/U55-R1-LOTE12-2026-09-13.json` · `termos/RC-337-humanos-uma-simples-experiencia-biologica.md` · `termos/RC-338-o-reconhecimento-que-nunca-veio.md` · `termos/RC-339-a-dificil-cobranca-sobre-os-humanos.md` · `termos/RC-340-atores-de-uma-peca-incompreensivel.md` · `termos/RC-341-ferramentas-do-favor-divino.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
