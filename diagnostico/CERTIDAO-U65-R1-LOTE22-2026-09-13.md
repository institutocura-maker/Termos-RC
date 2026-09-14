# CERTIDÃO — U65 · R1 · LOTE 22
## Os 2 da B003 (*Reintegração Cósmica*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 22 APROVADO (a B003) · **diretriz arquitetural: o Censo é ACHADOR, não CERCA** (homologada e registrada como §6 do despacho do censo)
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑343 | Portal Cósmico (destinação do Planeta Azul) | 6 |
| RC‑353 | Ilha Cósmica (mundos rebelados) | 6 |
| | **2 fichas** | **12** |

**B003: 2 → 0.** Décima sexta obra liquidada. **12 fragmentos · 0 falhas** na primeira passada.

## 2. RC‑343 — o portal **não foi construído**

A abstenção central desta ficha. A obra apresenta o portal sempre como **projeto truncado**:

- «nele **seria** construído um Portal cósmico» (L41–L42);
- «que na Terra **estava para ser** edificado» (L629);
- «o objetivo era a **edificação** do portal» (L4364–L4365).

E a própria abertura registra a frustração: «uma **dr amática ocorrência truncou a destinação** do Planeta Azul e de outros mundos irmãos. Resultado: uma **quaren tena**» (L44–L45). O verbete fica registrado **como destinação frustrada**, não como estrutura existente.

**A cautela do mecanismo foi preservada:** as naves «encontrariam, **provavelmente**, o que […] a física relativista e a física quântica de vanguarda **chamam de** buracos de verme» (L638–L641). A obra **toma o vocabulário da física contemporânea por aproximação** — não afirma que o portal fosse um buraco de verme. O «provavelmente» e o «chamam de» ficam na ficha.

## 3. RC‑353 — «uma espécie de» e o alargamento que encontrou a definição

**A obra não dá a designação como categoria, mas como comparação:**

> «A partir de então, o conjunto dos mundos rebelados passou a ser **uma espécie de** ilha cósmica entregue às próprias condições de capacidade tecnológico‑científica e nível moral dos seres ali congregados por força da rebelião.» (L973–L976)

Não é um lugar geométrico; é uma **condição de isolamento decretada** — a quarentena que «isolava pelo tempo que fosse necessário os mundos rebeldes do intercâmbio cósmico» (L969–L971).

⚠️ **Alargamento registrado (ao amparo do §6):** os blocos que o censo indicava (L304‑316, L87‑91, L325‑328) trazem apenas **aplicações** da expressão — a **definição** está em L973‑976, e a perda de comunicação entre os mundos em L994‑996. Ambas foram alcançadas por leitura estendida dentro da mesma obra.

## 4. A obra reitera passagens com variantes — e o termo não muda

| | Formulação |
|---|---|
| L87–L91 | «a **convicção** de que o todo **não pode** se resumir ao que **é** observado na **ilha cósmica**, **leva** as mentes de vanguarda […] na **busca** da verdade» |
| L325–L328 | «a **profunda e inabalável convicção** de que o todo **não podia** se resumir **apenas** no que **pudesse ser** observado na **ilha cósmica**, **levaram** as mentes de vanguarda […] na **interminável busca** da verdade» |

**Sem etiqueta:** a mutação está **na frase, não no termo** — «ilha cósmica» é idêntica nas duas. Pela matriz homologada, reiteração de redação é modo de imprimir.

## 5. Diretriz arquitetural — §6, «o Censo é ACHADOR, não CERCA»

Ficou lavrada no despacho do censo, com as duas condições cumulativas:

1. **Limite:** o alargamento vale **dentro da obra e do verbete** — nunca para mudar de obra nem para importar conteúdo de outro código.
2. **Portão:** todo fragmento colhido por alargamento passa pelo **Portão de Paridade Verbatim**, como os do bloco original.

E a regra de transparência: sempre que uma ficha colher fora dos blocos, o facto é registrado na ficha, no espelho e na certidão, com as linhas alcançadas.

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 2. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 807).

| Indicador | Antes (U64) | Depois (U65) |
|---|---:|---:|
| **Fichas** | 805 | **807** |
| **GAP** | 141 | **139** |
| Família B v3 — restantes | 35 | **33** (13 activos + 20 congelados) |
| **B003 — restantes** | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo: **B034 2 ·** e os unitários (B033, B017, B018, B039, B013, B036, B052, B021, B026, B019, B025).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 807 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 807 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 807 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U65-R1-LOTE22-2026-09-13.json` · `diagnostico/DESPACHO-CENSO-V3-HOMOLOGADO-2026-09-13.md` (§6) · `termos/RC-343-portal-cosmico-destinacao-planeta-azul.md` · `termos/RC-353-ilha-cosmica-mundos-rebelados.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
