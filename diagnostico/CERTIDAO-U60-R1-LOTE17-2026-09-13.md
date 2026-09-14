# CERTIDÃO — U60 · R1 · LOTE 17
## Os 3 da B023 (*O Dharma e as Castas Hindus*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 17 APROVADO (a B023) · postulado central da Extração R1 adoptado: *«o que o cadastro sabe, a ficha não empresta à fonte; o que a fonte não diz, a ficha não lhe atribui»* · roteiro de encerramento homologado (3 frentes, accionadas quando o poço chegar a zero)
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As três fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑326 | Povos Escolhidos (ariano, judeu, árabe) | 6 |
| RC‑327 | Homo hierarchicus | 6 |
| RC‑330 | Civilização Saraswati | 6 |
| | **3 fichas** | **18** |

**B023: 3 → 0.** Décima primeira obra liquidada.

## 2. O portão B pegou mais um deslocamento meu

Na primeira passada, um fragmento da RC‑330 veio com a linha trocada: eu lera «Saraswati‑Sindhu, hoje perdida nas brumas do tempo; e» em **L1940**, quando está em **L1941**. O conferidor independente acusou a falha antes de o driver ser invocado; corrigido, **18 fragmentos · 0 falhas**. Sexta vez que o mecanismo segura um erro de transcrição antes da escrita (U47, U49, U51, U52, U55, U60).

## 3. O postulado central, aplicado três vezes

O despacho da U59 erigiu em postulado a máxima desta campanha. Neste lote ela foi aplicada em três registos diferentes:

| Ficha | O cadastro sabe | A fonte diz | A ficha fez |
|---|---|---|---|
| RC‑327 | o termo «Homo hierarchicus» | «passei a chamá-lo de “Homo hierarchicus”» | registrou-a como **cunhagem do autor**, declarada como tal |
| RC‑326 | a eleição de três povos | «como já o disse, escolheu os arianos… depois, elegeu os judeus… optou pelos árabes» | registrou-a como **tese do autor**, em primeira pessoa |
| RC‑330 | «Civilização Saraswati» | «civilização Saraswati» **e** «civilização Saraswati‑Sindhu» | citou **as duas** formulações, sem preferir nenhuma |

Nos três casos: **nenhuma adopção como afirmação do cadastro, nenhuma conferência contra fonte externa, nenhuma promoção de categoria**.

## 4. Duas formulações do mesmo nome, sem etiqueta (RC‑330)

A obra grafa «civilização **Saraswati**» (L1900) e «civilização **Saraswati‑Sindhu**» (L1923, L1941). **Não etiquetei**, e digo porquê: não são contraditórias — a segunda é a forma alongada, e a própria obra a explica de imediato («o lendário rio Saraswati, do vale do rio **Indo**», L1920–L1922). Pelo critério homologado na U56, é variação de designação, não contradição tipográfica estrutural. **Se o Curador preferir o critério inverso, fica registrado para revisão.**

## 5. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 3 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 3. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 3 sinalizadores `ficha`.
- **Higienização NÃO antecipada**, por diretriz vigente (EL antes de Transform). **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 796).

| Indicador | Antes (U59) | Depois (U60) |
|---|---:|---:|
| **Fichas** | 793 | **796** |
| **GAP** | 153 | **150** |
| Família B v3 — restantes | 47 | **44** (24 activos + 20 congelados) |
| **B023 — restantes** | 3 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B050 3 · B002 2 · B014 2 · B020 2 · B003 2 · B026 2 · B034 2 ·** e os unitários (B033, B017, B018…).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 796 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 796 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 796 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U60-R1-LOTE17-2026-09-13.json` · `termos/RC-326-povos-escolhidos-ariano-judeu-arabe.md` · `termos/RC-327-homo-hierarchicus.md` · `termos/RC-330-civilizacao-saraswati.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
