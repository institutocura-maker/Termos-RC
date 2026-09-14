# CERTIDÃO — U58 · R1 · LOTE 15
## Os 4 da B006 (*Nos Bastidores da Luz I*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 15 APROVADO (a B006) · **diretriz de reta final:** «não antecipar a higienização do campo fontes; manter a esteira de extração rodando; concluir a materialização bruta antes das transformações globais de metadados»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As quatro fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑389 | Casa de Lucas (origem do Grupo Atlan) | 5 |
| RC‑391 | Mesmice Espiritual | 6 |
| RC‑393 | Enéas (espírito comunicante) | 5 |
| RC‑394 | Mandreya Ramataiana (espírito comunicante) | 5 |
| | **4 fichas** | **21** |

21 fragmentos verbatim intra-linha, **0 falhas** na primeira passada. Os 4 são **exclusivos** da B006. **B006: 4 → 0.** Nona obra liquidada.

## 2. Uma fonte de natureza diferente — e o cuidado que isso pediu

A B006 é **obra mediúnica** («ditada por Diversos Espíritos», folha de rosto), com «APRESENTAÇÃO», «PREFÁCIO», «ESCLARECIMENTO», uma secção **«PERSONAGENS»** (que apresenta as entidades comunicantes) e capítulos em forma **PERGUNTA / RESPOSTA**. Não tem sumário.

Daí três cautelas, todas da mesma família das anteriores:

- **RC‑389:** a obra relata a mudança de denominação do grupo para **Atlan** e a rotina das reuniões. **Não** se afirma que a Casa de Lucas fosse instituição formal extinta, nem se lhe atribui fundação, endereço ou data: nada disso consta da passagem.
- **RC‑393 e RC‑394:** as duas fichas **descrevem, não endossam**. A obra apresenta Enéas e Mandreya como «amigos espirituais» e relata o que «ele mesmo disse» e o que «outros amigos espirituais informaram». A ficha conserva **esse regime de atribuição** — e, no caso de Mandreya, conserva-o até no **condicional da fonte**: a identificação do Conselho com o do Apocalipse é formulada pela obra como «seria o mesmo referido no livro do Apocalipse», e assim fica, sem ser promovida a afirmação do cadastro.
- **RC‑391:** o termo ocorre em mais de um ponto (título de capítulo, L1010; «a perigosa mesmice do jogo das sensações terrenas», L408; «a “mesmice terrestre”», L2009). A ficha cita as três posições e **não** as trata como definições equivalentes — apenas como ocorrências do mesmo termo.

## 3. Os artefatos desta edição, preservados sem correcção

A edição digital da B006 tem defeitos próprios que nenhuma outra obra da campanha apresentou com esta densidade, e **nenhum foi normalizado**:

| Artefato | Exemplo |
|---|---|
| Palavras partidas ao meio pelo *hard-wrap* | «Centro Espí rita» (L73), «transcr itas», «espirit ualidade», «div ersos», «dois mi l anos» |
| Dois espaços em lugar de um | depois de ponto final («MANDREYA RAMATAIANA.  Ser»), em redor de travessões («se apresentava -  ou se apresenta -  os»), no meio de frases («muito  pouco») |
| Falta de acentuação | «incomodo» por «incômodo» |

O Portão de Paridade Verbatim é absoluto: onde a fonte escreve «Espí rita», escreve‑se «Espí rita».

## 4. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 4 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 4. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 4 sinalizadores `ficha`.
- **Higienização NÃO antecipada**, por diretriz expressa: o campo `fontes` permanece intocado; o inventário da U57 segue como mapa para o encerramento.
- **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 791). Nenhum teste da suíte os fiscaliza.

| Indicador | Antes (U57) | Depois (U58) |
|---|---:|---:|
| **Fichas** | 787 | **791** |
| **GAP** | 159 | **155** |
| Família B v3 — restantes | 53 | **49** (29 activos + 20 congelados) |
| **B006 — restantes** | 4 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B036 3 · B023 3 · B050 3 · B002 2 · B014 2 · B020 2 · B003 2 · B026 2 · B034 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 791 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 791 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 791 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U58-R1-LOTE15-2026-09-13.json` · `termos/RC-389-casa-de-lucas-origem-do-grupo-atlan.md` · `termos/RC-391-mesmice-espiritual.md` · `termos/RC-393-eneas-espirito-comunicante.md` · `termos/RC-394-mandreya-ramataiana-espirito-comunicante.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
