# CERTIDÃO — U64 · R1 · LOTE 21
## Os 2 da B020 (*O Sorriso de Pandora*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 21 APROVADO (a B020) · 17 activos na contagem · **decisão sobre as aspas da RC‑275: abstenção CORRETA**, registrada como §5.1 da jurisprudência
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑288 | Os Anais de uma Cultura Perdida | 6 |
| RC‑289 | O Vício de Epimeteu | 8 |
| | **2 fichas** | **14** |

**B020: 2 → 0.** Décima quinta obra liquidada. **14 fragmentos · 0 falhas** na primeira passada.

## 2. A obra fala pela boca de Pandora

Como na B036 (U59), **o discurso é de uma personagem, não do cadastro**: a B020 é narrada na primeira pessoa por **Pandora**, que se declara de «condição demoníaca» (L658) e «criada só muito recentemente, há cerca de 74 mil anos» (L667). A «cultura perdida» do verbete é, no texto, a cultura da própria estirpe da narradora, vista de dentro.

A edição traz artefatos que **não foram normalizados**: palavras partidas ao meio («fa ctos», «semea r corpos», «basta nte»), hífenes soltos («abelha- rainha», «produto -cobaia») e **mistura de aspas curvas e rectas** na mesma obra (curvas em L671 e L1980; **rectas** em L2098 — preservadas como estão).

## 3. RC‑289 — a abstenção central: a fonte **não** identifica o vício à fixação pelo barro

O capítulo 5 abre assim:

> A humanidade jamais poderá compreender um dos seus progenitores, no caso, Epimeteu. Ele era uma **“figura estranha”** até mesmo para os seus próprios pares titãs. Epimeteu e Prometeu […] tinham uma **fixação pelo barro**…

E só mais adiante a obra emprega a palavra «vício»:

> **Para os humanos**, Epimeteu **seria** um drogado, com **vício extremado na absorção de poções**… (L2097–L2098)

> Sobrava somente a questão do vício, mas isso era problema de cada um. (L2103)

> A sua vida era dedicada à **alquimia** de tudo o que com ele interagia. (L2105)

**Fixação × vício são duas coisas distintas no texto**, e a ficha **não as funde**. O cadastro as aproximaria por vizinhança de capítulo; a Extração R1 registra cada uma com a palavra que a fonte lhe dá.

**O enquadramento foi preservado:** a caracterização como «drogado» é **o modo como os humanos o veriam** — «Para os humanos […] **seria**» —, não a ontologia que a narradora lhe atribui.

## 4. ⚠️ Alargamento do alcance da leitura — registrado para auditoria

O bloco de evidência do censo v3 para a RC‑289 era «B020 L86‑115 e L1976‑1984», que contém apenas o índice e a **abertura** do capítulo — e **a abertura não nomeia o vício**. Para que a ficha dissesse o que a fonte diz, a leitura foi estendida **dentro do mesmo capítulo** (capítulo 5 = L1977–L2328), de onde provêm L2097–L2105.

Todos os fragmentos continuam verbatim intra-linha e conferidos byte a byte pelo Portão B. **Fica o alargamento registrado**, por ser a primeira vez na campanha que a ficha vai além do bloco indicado pelo censo. O censo é achador de ocorrências; não é cerca.

O vício **reaparece fora do capítulo**, já no 6 («e isso, junto com o seu vício, o desgastou a tal ponto que ele desfaleceu», L2348–L2350). **Não foi citado** entre os fragmentos, por estar fora do capítulo que dá título ao termo; ficou registrado nas observações da ficha.

## 5. Jurisprudência — §5.1, o caso das aspas (homologado)

A decisão do Curador sobre a RC‑275 ficou lavrada como **§5.1** do despacho da U56, com o fundamento de que a variação do alcance das aspas «recai perfeitamente na coluna *Modo de imprimir*», pois «não há mutação nas letras, na ordem das palavras ou no sentido estrutural do termo», e de que «manter a isenção da etiqueta neste caso **preserva o "peso" do alerta** para quando houver falhas reais de ortografia ou contradições semânticas».

**Regra extraída:** *aspas* — inclusive a variação do seu **alcance** — integram a coluna «modo de imprimir».

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 2. Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 805).

| Indicador | Antes (U63) | Depois (U64) |
|---|---:|---:|
| **Fichas** | 803 | **805** |
| **GAP** | 143 | **141** |
| Família B v3 — restantes | 37 | **35** (15 activos + 20 congelados) |
| **B020 — restantes** | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo: **B003 2 · B026 2 · B034 2 ·** e os unitários (B033, B017, B018, B039, B013, B036, B052, B021, B019).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 805 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 805 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 805 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U64-R1-LOTE21-2026-09-13.json` · `diagnostico/DESPACHO-JURISPRUDENCIA-ETIQUETA-DIVERGENCIA-2026-09-13.md` (§5.1) · `termos/RC-288-os-anais-de-uma-cultura-perdida.md` · `termos/RC-289-o-vicio-de-epimeteu.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
