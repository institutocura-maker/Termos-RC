# CERTIDÃO — U71 · R1 · LOTE 28
## A B013 (*Tzimtzum*) — RC‑270 «Linhagem dos Patriarcas Hebreus»

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 28 APROVADO (a B013) · VIA (a) mantida · verificação dupla de HEAD
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. A ficha

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑270 | Linhagem dos Patriarcas Hebreus | 9 |

**B013: 1 → 0.** Vigésima segunda obra liquidada. **9 fragmentos · 0 falhas** na primeira passada.

## 2. O verbete é um **anexo** — e a obra não traz o seu corpo em texto extraível

O termo não é um conceito solto: é o título de um **anexo**, anunciado duas vezes no corpo pela fórmula «(Ver, em anexo, “A Linhagem dos Patriarcas Hebreus”)» (L108–L110, L920–L923), listado no sumário entre o «Posfácio» (L58) e as «Notas Explicativas e Referências Bibliográficas» (L60), e com título próprio em caixa alta (L7001).

**Mas o texto extraído do anexo contém apenas o seu título.** Pelo aparelho de paginação da transcrição, a página que o encabeça cede só o cabeçalho, e a página seguinte já abre «NOTAS EXPLICATIVAS E REFERÊNCIAS BIBLIOGRÁFICAS» (L7004) — o desenvolvimento da linhagem **não comparece em texto extraível** (era, ao que tudo indica, quadro, imagem ou matéria não corrida).

**Regime de carência (critério U63), aplicado agora à própria fonte e não a um conceito:** a ficha **não inventa a genealogia, não a importa de outra obra, e não supre a lacuna** — registra a carência. E assinala a consequência: o que se pode afirmar sobre o **conteúdo** do anexo vem do **corpo do livro**, não do anexo mesmo.

## 3. O que o corpo diz que o anexo cobre

A descendência de Noé:

- «**Gomer**, ancestral do “DNA ariano”, era também neto de Noé, só que de uma **outra linhagem** do seu sangue. **Abraão** era da descendência de **Sem**, outro filho de Noé» (L912–L914);
- «após ter se decepcionado com os arianos e, depois, com os judeus, esse mesmo Ser pactuou com **Maomé**, árabe de origem, e que também representava um **outro ramo da descendência de Abraão**» (L915–L917);

donde a conclusão do autor:

> «ter se apresentado aos antigos hebreus como “**Javé**”, aos arianos como “**Brahma**” e aos árabes como “**Alá**”, todo esse contexto de pactos se encontrava **no âmbito da descendência de Noé**!» (L918–L920)

## 4. Outras abstenções

- **A moldura dos pactos é afirmação do autor sobre a perspectiva da personagem**, não facto do cadastro: «para Javé, ele não estava fazendo nada de errado, pois que o “pacto” feito por ele com Noé […] dava “legalidade moral” à opção feita no pretérito» (L910–L912). E a ressalva: «Óbvio que a ortodoxia judaica não aceita esse aspecto da história» (L909).
- **Ancoragem (U57):** RC‑270 declara B013, B036 e B052; a evidência ocorre **na B013**, e é nela que a ficha se sustenta. Nenhum conteúdo de B036 ou B052 foi importado.
- **Convenção gráfica, sem etiqueta:** caixa normal no sumário e no corpo (L59, L109) × caixa alta no título do anexo (L7001); e o título partido pelo hard-wrap no segundo anúncio (L921–L922).
- **Aparelho de transcrição:** os marcadores «===== [PÁGINA NNN] =====» **não são citados como conteúdo** (critério U61); apenas invocados na observação sobre a carência, como meio pelo qual se apurou a extensão do anexo.

## 5. Alargamento (§6)

Os blocos do censo eram «L31‑65», «L100‑129» e «L905‑945». O **título do anexo** (L7001) ficava fora deles e foi alcançado por leitura estendida na mesma obra, por ser a ocorrência canónica do termo. Sétimo uso consecutivo do §6.

## 6. Governança e efeito na Base

- **V revogado mantido:** `"v_revogado": true`, sem `aplicar_V`; a ficha nasce 🟡 provisório, `ficha False→True`. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slug ASCII.** Nenhuma aresta nova. O `diff` do registro-mestre é **1 linha**, só o sinalizador `ficha`.
- **Verificação dupla de HEAD** aplicada: abertura e encerramento.
- **Higienização NÃO antecipada.** **Espelhos .xlsx/.docx adiados** (768 vs Base 814).

| Indicador | Antes (U70) | Depois (U71) |
|---|---:|---:|
| **Fichas** | 813 | **814** |
| **GAP** | 133 | **132** |
| Família B v3 — restantes | 27 | **26** (6 activos + 20 congelados) |
| **B013 — restantes** | 1 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Activos restantes: **RC‑347** (B026) · RC‑352 (B025) · RC‑368 (B011) · RC‑372 (B049) · RC‑377 (B043) · RC‑931 (B016).

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 814 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 814 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 814 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U71-R1-LOTE28-2026-09-13.json` · `termos/RC-270-linhagem-dos-patriarcas-hebreus.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`. Verificação dupla de HEAD: abertura e encerramento.*
