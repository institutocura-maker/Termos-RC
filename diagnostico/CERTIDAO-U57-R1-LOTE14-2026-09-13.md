# CERTIDÃO — U57 · R1 · LOTE 14
## Os 3 da B019 (*Nem Deus, nem Javé, nem Darwin*) + o inventário de desvios

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 14 APROVADO (a B019) · **inventário completo dos códigos com desvio entre fonte declarada e fonte sustentadora** determinado pelo Curador
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As três fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑539 | Arquitetos Universais (colectivo cocriador) | 4 |
| RC‑546 | Primado da Consciência Criativa (Goswami) | 5 |
| RC‑547 | Evolução Criativa (hipótese consciencial) | 5 |
| | **3 fichas** | **14** |

14 fragmentos verbatim intra-linha, **0 falhas** na primeira passada. **B019: 3 → 0** (quanto ao sustentável).

**RC‑347 fica para o lote natural da B026.** O poço atribuído à B019 tinha 4 códigos; RC‑347 declara B019, mas a evidência do censo é **toda da B026** (L194‑200, L59, L130‑131). É o **terceiro caso do mesmo padrão** — RC‑300 (→ B021), RC‑270 (→ B013), RC‑347 (→ B026) —, e foi exactamente ele que motivou o pedido do inventário.

## 2. Três abstenções, da mesma espécie das anteriores

- **RC‑539:** a obra não diz quantos são os Arquitetos Universais nem os nomeia; a ficha não o inventa. Registra só o que a fonte diz: que estão «comprometidos com a obtenção da tão esperada “Criatura Universal”».
- **RC‑547:** a fonte **arrola** a «Evolução Criativa» como a quarta hipótese entre quatro; **não a define** neste capítulo. A ficha dá-lhe o enquadramento da obra (a lista e o confronto com o Darwinismo) e não lhe atribui conteúdo doutrinário.
- **RC‑546:** a autoria da noção é atribuída «como aponta, por exemplo, o físico Amit Goswami» — **sem exclusividade**, tal como a obra a formula; e o livro de Goswami que a B019 cita («O Universo Autoconsciente») é registrado como **fonte externa citada pela obra, não adoptada pela ficha**.

**Duas posições sem etiqueta (RC‑539):** na SINOPSE a expressão vem entre aspas e com artigo («os “Arquitetos Universais”», L95); no corpo comparece nua, em enumeração (L5132). É variação da prosa do autor — pelo critério homologado na U56, não acciona a etiqueta de divergência.

## 3. O inventário de desvios — `INVENTARIO-DESVIOS-FONTE-DECLARADA-2026-09-13.md`

Levantado sobre **toda a família B do censo v3** (167 códigos), confrontando a bibliografia declarada no cadastro com as obras onde o censo verificou a ocorrência literal.

**Resultado: 28 códigos com desvio** (24 já materializados · 4 no poço).

| Perfil | Códigos | Descrição |
|---|---:|---|
| **C** | 1 | livro declarado, evidência só oral → congelado (RC‑296) |
| **D** | 27 | livro declarado sem ocorrência verificada |

**Obras mais vezes declaradas sem ocorrência:** B060 (7) · B018 (4) · B017 (3) · B042 (3) · B021, B026, B011, B019, B074, B075 (2 cada) · e 14 obras com 1.

**Ressalva que o documento faz questão de registar:** é um **mapa para verificação, não uma lista de erros**. O censo procura a chave normalizada do nome do verbete; uma obra que trate da matéria sob **outra forma de palavra** não é sinalizada — é o caso da própria RC‑296. Só a conferência humana, obra a obra, decide se a fonte declarada se mantém, se corrige ou se retira.

**Três usos no encerramento:** (1) higienizar o campo `fontes`; (2) ancorar os lotes do poço **sempre pela obra que ocorre**, nunca pela declarada; (3) rever a bibliografia das 24 fichas já materializadas (as fichas em si estão ancoradas correctamente).

**Nenhum campo do cadastro foi alterado por este documento.**

## 4. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 3 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 3. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 3 sinalizadores `ficha`.
- **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 787). Nenhum teste da suíte os fiscaliza.

| Indicador | Antes (U56) | Depois (U57) |
|---|---:|---:|
| **Fichas** | 784 | **787** |
| **GAP** | 162 | **159** |
| Família B v3 — restantes | 56 | **53** (33 activos + 20 congelados) |
| **B019 — sustentáveis** | 3 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B006 4 · B036 3 · B023 3 · B050 3 · B002 2 · B014 2 · B020 2 · B003 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 787 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 787 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 787 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/INVENTARIO-DESVIOS-FONTE-DECLARADA-2026-09-13.md` · `diagnostico/U57-R1-LOTE14-2026-09-13.json` · `termos/RC-539-arquitetos-universais-coletivo-cocriador.md` · `termos/RC-546-primado-da-consciencia-criativa-goswami.md` · `termos/RC-547-evolucao-criativa-hipotese-consciencial.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
