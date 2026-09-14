# CERTIDÃO — U68 · R1 · LOTE 25
## A B017 (*Terra Atlantis: O Sinal de Land's End*) — RC‑233 «Marca Val»

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 25 APROVADO (a B017) · VIA (a) mantida · **nova diretriz de governança: verificação de integridade do HEAD também no encerramento, antes do push** (duplo cinturão)
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. A ficha

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑233 | Marca Val (A Estratégia do Possível) | 7 |

**B017: 1 → 0.** Décima nona obra liquidada. **7 fragmentos · 0 falhas** na primeira passada.

## 2. A explicação estava no **fecho** do capítulo, não na abertura

Os blocos que o censo indicava eram o índice (L55‑88) e a **abertura** do capítulo 7 (L2817‑2846). A abertura narra a descoberta genética sobre os nephelim — e **não explica o título**. A explicação está no fecho (L3350–L3374, sendo o capítulo 7 = L2818–L3425):

> «**Val El** introduziu a “lógica do possível” entre os Val, e com isso a capacidade crítica pessoal foi crescendo ao nosso psiquismo, facto que implica em ressaltar que muitas das estratégias planeadas e executadas até aos tempos atuais nasceram sob esse prisma.» (L3362–L3365)

> «É como se, a cada degrau que fosse galgado de **uma escada infinita**, um novo horizonte de possibilidades pudesse ser agora percebido, analisado e diagnosticado. Sobre essa base, **a estratégia do “possível” ou da “lógica do possível”**, de ser posta em prática para aquele nível, seria então trabalhada como sendo o objetivo de todos.» (L3371–L3374)

É o **quarto uso consecutivo** do §6 (o censo é ACHADOR, não CERCA) e o segundo em que a definição só aparece fora do bloco indicado.

## 3. A abstenção central: a obra **não** profere a frase equacional

Não há, em parte alguma do livro, uma sentença que diga «a marca dos Val é a lógica do possível». O que existe é o **título do capítulo** (L72, L2819‑L2820) e o seu **desenvolvimento**, que culmina na «lógica do possível» introduzida por Val El.

A ficha registra o nexo **como nexo estabelecido pelo desenvolvimento do próprio capítulo**, e não como identidade enunciada pela fonte — o mesmo cuidado aplicado à RC‑227 na U67.

## 4. O que a «lógica do possível» **substituiu**

O capítulo define-se por contraste:

| Antes | Depois |
|---|---|
| «**aceitação acrítica**, associada à impressão psíquica de que “a realidade percebida era a verdade a ser assumida”» (L3350‑L3351) | a «lógica do possível», que faz crescer «a capacidade crítica pessoal» (L3362‑L3363) |
| «não exist[ia] um senso crítico, uma lógica que observe a realidade e com ela interaja sem que isso limite a perceção do todo» (L3352‑L3354) | a percepção de que a realidade «não era uma **obra acabada**», cabendo a cada ser racional «a produção do **esclarecimento possível** da realidade» (L3355‑L3361) |

## 5. A voz é de um Val

«Assim vivemos, os Val, até estes dias em que daqui me comunico com os que hoje habitam a Terra» (L3375–L3376). A obra acrescenta que essa lógica «terminou por ser uma das componentes que influenciou […] os humanos da Terra» (L3377–L3379) — **testemunho da personagem**, registrado como tal (critério da B036, U59).

## 6. Nota de governança da abertura

A checagem de abertura acusou «igual: NÃO», mas era **falso alarme**: o `fetch` falhara por um soluço de rede e eu o havia suprimido com `2>/dev/null`, deixando o `FETCH_HEAD` inexistente. **Correcção de método: não mais suprimo os erros do fetch**, para distinguir uma falha de rede de uma regressão real. Refeita a checagem: HEAD == remoto == `b11cc01`, 0 pendentes, 810/810 fichas.

## 7. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; a ficha nasce 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slug ASCII.** Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre é **1 linha**, só o sinalizador `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 811).

| Indicador | Antes (U67) | Depois (U68) |
|---|---:|---:|
| **Fichas** | 810 | **811** |
| **GAP** | 136 | **135** |
| Família B v3 — restantes | 30 | **29** (9 activos + 20 congelados) |
| **B017 — restantes** | 1 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Activos restantes: **RC‑234** (B018) · RC‑235 (B039) · RC‑270 (B013) · RC‑347 (B026) · RC‑352 (B025) · RC‑368 (B011) · RC‑372 (B049) · RC‑377 (B043) · RC‑931 (B016).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 811 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 811 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 811 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U68-R1-LOTE25-2026-09-13.json` · `termos/RC-233-marca-val-a-estrategia-do-possivel.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`. Verificação dupla de HEAD: abertura e encerramento.*
