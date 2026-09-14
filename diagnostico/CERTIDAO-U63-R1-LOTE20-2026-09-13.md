# CERTIDÃO — U63 · R1 · LOTE 20
## Os 2 da B014 (*Sophia e o Logos Criadores*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 20 APROVADO (a B014) · 19 activos na contagem regressiva · **decisão de jurisprudência proferida**: a etiqueta da RC‑397 deve ser mantida
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑275 | Arte Demodhármica do Possível | 6 |
| RC‑278 | Olhar Adulto | 6 |
| | **2 fichas** | **12** |

**B014: 2 → 0.** Décima quarta obra liquidada. **12 fragmentos · 0 falhas** na primeira passada — o portão não precisou intervir.

## 2. Jurisprudência lavrada (decisão do Curador sobre a RC‑397)

O despacho confirma a etiqueta aplicada na U61 e fixa o fundamento, que ficou lavrado como **adendo §5** ao `DESPACHO-JURISPRUDENCIA-ETIQUETA-DIVERGENCIA-2026-09-13.md`:

> «Diferente da variação de caixa alta/baixa (que é estilo gráfico), a troca de posição da letra "h" e a ausência do plural configuram uma **mutação estrutural na ortografia da palavra**. Assim como no precedente "Terrenos × Terrestres", trata-se de um erro tipográfico de edição que altera o termo.»

O critério operativo desdobra-se agora em **dois testes cumulativos** (registrados no adendo):

1. **As letras da palavra são as mesmas?** Se não — troca, acréscimo, supressão ou **reordenação** —, é mutação ortográfica: **etiqueta-se**.
2. **A flexão (número, género) é a mesma?** Se divergir no próprio termo tal como a fonte o grafa, concorre para a mutação estrutural.

**Linha divisória:** *caixa, espaçamento, aspas e posição na página* = modo de imprimir (sem etiqueta); *ortografia e flexão do termo* = o termo mesmo (com etiqueta).

## 3. RC‑278 — a abstenção central: a obra declara uma **carência**, não uma faculdade

Esta foi a armadilha do lote. A expressão «olhar adulto» poderia ser lida como um atributo a descrever. **Não é o que a fonte diz.** A obra afirma:

- «**Não existe** “olhar adulto” sobre o que quer que seja, em termos dos conceitos religiosos que, enquanto humanidade, abraçamos» (L5078–L5079);
- «Sophia **não teve e ainda não tem** um “olhar adulto”, crítico e equilibrado» (L5137–L5142);
- «Um “olhar adulto” é algo **ainda por ser construído e conquistado**, tanto da parte dele como também da nossa» (L5143–L5144).

A ficha registra o termo **como aquilo que a fonte diz que falta**. Convertê-lo em capacidade definida inverteria o sentido da passagem.

## 4. RC‑275 — um condicional que não vira asserção, e um caso de aspas que submeto

**O raciocínio é condicional.** O autor não afirma que as estirpes do universo vizinho se alimentam da emoção religiosa: **argumenta que poderiam** («por que outras estirpes […] também não poderiam assim proceder?», L2811–L2812), e a percepção de que a fé dos terráqueos está «sendo usada como “fonte de alimentação”» vem introduzida por «**Em sendo verdadeira essa percepção**» (L2839). A ficha preserva o regime de dúvida.

**O caso das aspas (submetido ao Curador):** a expressão ocorre em três funções, e as **letras e palavras são as mesmas nas três**:

| Onde | Grafia | Alcance das aspas |
|---|---|---|
| Sumário (L53) | «A “Arte Demodhármica” do Possível» | só «Arte Demodhármica» |
| Título do capítulo (L2672, L10592) | «A “ARTE DEMODHÁRMICA” DO POSSÍVEL» | só «ARTE DEMODHÁRMICA» |
| Menção no corpo (L2821–L2823) | «“a arte demodhármica do possível”» | a expressão inteira |

**Não accionei a etiqueta**, por entender que se trata da marcação gráfica de uma cunhagem em três funções distintas — o mesmo raciocínio do precedente da RC‑330 («Saraswati» × «Saraswati‑Sindhu»), homologado sem etiqueta na U61. **Mas é um caso mais sutil que a mera caixa**, e por isso o submeto expressamente.

## 5. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 2. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 803).

| Indicador | Antes (U62) | Depois (U63) |
|---|---:|---:|
| **Fichas** | 801 | **803** |
| **GAP** | 145 | **143** |
| Família B v3 — restantes | 39 | **37** (17 activos + 20 congelados) |
| **B014 — restantes** | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo: **B020 2 · B003 2 · B026 2 · B034 2 ·** e os unitários (B033, B017, B018, B039, B013, B036, B052, B021).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 803 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 803 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 803 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U63-R1-LOTE20-2026-09-13.json` · `diagnostico/DESPACHO-JURISPRUDENCIA-ETIQUETA-DIVERGENCIA-2026-09-13.md` (adendo §5) · `termos/RC-275-arte-demodharmica-do-possivel.md` · `termos/RC-278-olhar-adulto.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
