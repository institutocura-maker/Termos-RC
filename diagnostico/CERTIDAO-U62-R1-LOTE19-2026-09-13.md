# CERTIDÃO — U62 · R1 · LOTE 19
## Os 2 da B002 (*O Drama Espiritual de Javé*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** via expressa, cadência de esgotamento «obra a obra» mantida · questão da etiqueta da RC‑397 submetida ao Curador e pendente
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑221 | Sustentação Espiritual do Universo | 6 |
| RC‑222 | Filhos das Estrelas | 6 |
| | **2 fichas** | **12** |

**B002: 2 → 0.** Décima terceira obra liquidada.

## 2. O portão pegou o sétimo deslocamento meu

«fazem por pura obrigação,» eu lera em **L4287**; está em **L4288**. O conferidor independente acusou antes de o driver ser invocado; corrigido, **12 fragmentos · 0 falhas**. Sétima vez que o mecanismo segura um erro de transcrição antes da escrita (U47, U49, U51, U52, U55, U60, U62).

## 3. A armadilha: uma epígrafe citada que não é doutrina do autor

O capítulo 9 da B002 abre assim:

> O que quer que tenha chegado a ser e o que quer que virá a ser, também toda a forma e tudo o que é sem forma – todas as coisas neste mundo (universo) **são permeadas pelo Supremo Atman**.

A atribuição vem logo abaixo, em **caixa alta espaçada e partida pelo hard-wrap**: L4267 « —  S» · L4268 «HIVA» · L4269 « S» · L4270 «AMHITA» · L4271 « ¹.» — isto é, «**— SHIVA SAMHITA¹**», com nota de rodapé.

É **citação de fonte externa, não adopção pelo autor** — o mesmo caso de Goswami na RC‑546 (U57). A ficha registra a epígrafe **como epígrafe** e a exposição do autor **como exposição**, e **não funde as duas coisas**:

| | Epígrafe (L4264–L4266) | Exposição do autor (L4278–L4288) |
|---|---|---|
| Conteúdo | tudo é permeado pelo Supremo Atman | Javé, ao criar materialmente, precisava de «uma componente espiritual correspondente», e «o Mais Alto viu-se obrigado a fornecê-la» |
| Natureza | citação do Shiva Samhita, com nota | tese do autor |
| Registro | vai verbatim, **marcada como citação** | vai verbatim, **como tese** |

## 4. «Filhos das Estrelas» — a fonte dá a razão do nome

A obra não usa a expressão como metáfora; **justifica-a literalmente**:

> […] todos os que existem no âmbito deste universo […] são referidos como sendo «filhos das estrelas». Isto porque seus espíritos, para poderem residir em qualquer quadrante universal, necessitam do concurso de algum tipo de corpo […] e esses corpos somente poderão existir com a contribuição essencial dos elementos químicos **produzidos pelas fornalhas estelares do universo**.

**O que a ficha não faz:** não estreita a designação à humanidade — na obra ela abrange «todos os que existem no âmbito deste universo» (L5337–L5339) e «todas as espécies» (L5691). E **não lhe atribui origem extraterrestre no sentido de «vindos de outros mundos»**: a razão dada é a composição química dos corpos, forjada nas estrelas. A «síndrome de estrangeiro» (L4296–L4298) pertence ao capítulo 9 e **não é invocada** como definição.

## 5. Três grafias, nenhuma etiqueta

| Onde | Grafia |
|---|---|
| Sumário (L33) | «Os Filhos das Estrelas» |
| Título do capítulo (L5327) | «OS FILHOS DAS ESTRELAS» |
| Corpo (L5321, L5339, L5691, L5706) | «filhos das estrelas» |

Três **convenções de caixa** para o mesmo termo, sem alteração de letras — portanto **sem** a etiqueta de divergência (critérios homologados na U55 e na U56). O mesmo vale para «A Sustentação Espiritual do Universo» (L29) × «A SUSTENTAÇÃO ESPIRITUAL DO UNIVERSO» (L4263).

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 2. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 801).

| Indicador | Antes (U61) | Depois (U62) |
|---|---:|---:|
| **Fichas** | 799 | **801** |
| **GAP** | 147 | **145** |
| Família B v3 — restantes | 41 | **39** (19 activos + 20 congelados) |
| **B002 — restantes** | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo: **B014 2 · B020 2 · B003 2 · B026 2 · B034 2 ·** e os unitários (B033, B017, B018, B039, B013, B036, B052).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 801 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 801 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 801 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U62-R1-LOTE19-2026-09-13.json` · `termos/RC-221-sustentacao-espiritual-do-universo.md` · `termos/RC-222-filhos-das-estrelas.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
