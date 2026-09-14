# CERTIDÃO — U61 · R1 · LOTE 18
## Os 3 da B050 (*Guia das Eras Universais · Mapa*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 18 APROVADO (a B050) · cadência de esgotamento «obra a obra» mantida com 24 activos em fila · jurisprudência da etiqueta (U56) reafirmada pelo Curador na RC‑330
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As três fichas

| Cód. | Verbete | Frag. | Etiqueta |
|---|---|---:|---|
| RC‑397 | Tirthankaras (Rishabh Dev, Jina Mahavira) | 3 | **[⚠️ DIVERGÊNCIA INTERNA DA FONTE]** |
| RC‑399 | Dwarka (submersa) | 2 | — |
| RC‑402 | Halos de Poder (demos) | 2 | — |
| | **3 fichas** | **7** | |

**B050: 3 → 0.** Décima segunda obra liquidada.

## 2. Primeiro achado — a B050 **não é um livro**

Ao abrir a fonte, o `original.txt` declara de imediato:

> `[NOTA METODOLÓGICA]` O original.pdf é um **INFOGRÁFICO de 1 página** (A0, 3436×2450 pt, Adobe Illustrator 26.1, 30/05/2023) — não há fluxo de texto corrido. Este arquivo é a **TRANSCRIÇÃO ESTRUTURAL FIEL do conteúdo textual vetorial do artefato** (298 spans), extraído com pypdf/PyMuPDF (**sem OCR, sem interpolação**).

A obra é a *Linha do Tempo da Revelação Cósmica*: **quatro trilhas verticais** (A = universo demo/antimaterial; A2 = famílias biodemo; B = Terra/humanidade; C = pré-história e mito; D = recorte histórico), com **143 eventos datados** (L63–L205).

**Consequência para o Portão de Paridade:** cada entrada tem a forma

```
[DATA a.p.] (trilha X, y=NNN) <legenda> (DATA por extenso)
```

Ora a secção 4 do próprio ficheiro declara: «trilha e posição y **conforme o artefato**» (L58). Isto é, **a data entre colchetes e as coordenadas são aparelho da transcrição, não texto impresso no infográfico**. As citações tomam portanto o **núcleo semântico da legenda**, sem o aparelho — cada fragmento é, ainda assim, verbatim intra-linha do `original.txt`, conferido byte a byte. A barra «/» dentro das linhas marca uma quebra de linha interna ao span.

Registro o ponto ao Curador: **nunca antes a campanha citara uma fonte que não fosse texto corrido**, e a distinção «texto impresso × aparelho da transcrição» passa a ser matéria do Portão.

## 3. Segundo achado — uma divergência que **acciona** a etiqueta

A obra grafa o termo de dois modos, em duas entradas do mesmo artefato:

| Linha | Entrada | Grafia |
|---|---|---|
| L170 | «Rishabh Dev, primeiro dos / **Tirthankaras**. Fundou o Jainadharma.» | **Tirthankaras** |
| L186 | «Jina Mahavira. 24°A **Thirtankara**. (2600 a.p.)» | **Thirtankara** |

**Accionei a etiqueta.** O fundamento é a pergunta operativa da jurisprudência U56 — «a diferença altera o **TERMO**, ou apenas o modo de o imprimir?» —, e a resposta é a primeira: não se trata de convenção de caixa (alta × baixa) nem de espaçamento gráfico, mas de **outra ordem de letras** (Thir‑ × Tir‑) na grafia do próprio nome. Ambas as posições vão verbatim, sem conciliação e sem correcção. **Submeto o enquadramento ao Curador.**

**Duas cautelas registradas na ficha:** (i) a grafia anómala «24°A», com o «A» solto após o ordinal, e a própria «Thirtankara» provêm da camada vectorial extraída sem OCR nem interpolação — constam do ficheiro canónico tal como o artefato as traz; se o defeito é do infográfico ou da extração, **isso não se decide aqui**; (ii) não accionei etiqueta para «Halos de **P**oder» (cadastro) × «Halos de **p**oder» (legenda, RC‑402): é caixa, não termo.

## 4. O postulado central, numa fonte que quase nada diz

As legendas de um infográfico são marcos cronológicos, não exposições. O postulado foi aplicado com mais rigor aqui do que em qualquer lote anterior:

| Ficha | O que a fonte diz | O que a ficha **não** lhe atribuiu |
|---|---|---|
| RC‑399 | «Dwarka submersa.» — é a **íntegra** da entrada | localização, causa, agente ou consequência; a vizinhança cronológica (L157, L159) é contexto, não definição |
| RC‑402 | «Halos de poder usados para estabilizar a forma física dos demos.» | o que são, de que são feitos, quem os fez, como operam; e **nenhuma relação de causa** com «Abertura de portais…» (L83), contemporânea na mesma data, porque a fonte não a enuncia |
| RC‑397 | dois nomes e duas datas | o que seja um tirthankara — **a fonte não define o termo** |

## 5. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 3 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 3 (o «°» de «24°A» fica na citação, não no slug). Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 3 sinalizadores `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 799).

| Indicador | Antes (U60) | Depois (U61) |
|---|---:|---:|
| **Fichas** | 796 | **799** |
| **GAP** | 150 | **147** |
| Família B v3 — restantes | 44 | **41** (21 activos + 20 congelados) |
| **B050 — restantes** | 3 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo: **B002 2 · B014 2 · B020 2 · B003 2 · B026 2 · B034 2 ·** e os unitários (B033, B017, B018, B039, B013, B036).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 799 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 799 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 799 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U61-R1-LOTE18-2026-09-13.json` · `termos/RC-397-tirthankaras-rishabh-dev-jina-mahavira.md` · `termos/RC-399-dwarka-submersa.md` · `termos/RC-402-halos-de-poder-demos.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
