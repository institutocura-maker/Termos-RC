# CERTIDÃO — U67 · R1 · LOTE 24
## A B033 (*O Drama Terreno de Javé*) — RC‑227 «Opção Terra»

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 24 APROVADO (a B033) · **VIA (a) confirmada: 1 obra = 1 lote** · 11 activos na fila nominal
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 0. Incidente de abertura — a checagem pegou a terceira regressão

Ao abrir o turno, a checagem que propus na U61 acusou de imediato:

```
HEAD: 0a640cf   remoto: fd51d3f   igual: NÃO — regressão   pendentes: 208
```

**Terceira ocorrência** do mesmo fenómeno (U48, U61, U67): o sandbox perde os objetos do git entre turnos. **A detecção foi imediata e anterior a qualquer trabalho** — foi exactamente para isso que a checagem foi instituída.

**Nada se perdeu:** o disco tinha as 809 fichas e todos os artefatos; o remoto tinha o HEAD `fd51d3f` com as 809 fichas. Correcção pelo procedimento homologado (fetch → `reset --mixed FETCH_HEAD`, **nunca `--hard`** → restauração do `SESSION-NOTES` pelo HEAD, que reaparecera com o conteúdo de outra branch). Estado recomposto e verificado: **0 pendentes, 809/809 fichas, suíte 21/21**.

## 1. A ficha

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑227 | Opção Terra: Estratégia Necessária | 7 |

**B033: 1 → 0.** Décima oitava obra liquidada. **7 fragmentos · 0 falhas** na primeira passada.

## 2. Três atribuições — e por que **não** etiquetei

A fonte atribui a «opção Terra» de três modos:

| Linha | Atribuição |
|---|---|
| L4260–L4261 | Brahma «tomou como sendo sua a “opção Terra” **quando, na verdade, “outras vontades” foram quem fizeram convergir**» |
| L6812–L6813 | «feita pelo Senhor Javé — **seguramente influenciado** pelo Cristo Cósmico e também por Shiva» |
| L6664 | «**parece** ser mais um “acaso”, filho de uma outra série de “acasos”» |

**Decidi não accionar a etiqueta, com fundamento, e submeto a leitura ao Curador:**

1. A primeira não é um conflito entre passagens — é uma **correcção dentro da mesma sentença** («tomou como sendo sua […] quando, na verdade…»).
2. A terceira vem com a moldura que a compõe: «**na lógica humana**, não se observa nenhum padrão de inexorabilidade» (L6665–L6666). O acaso é **aparência para nós**, não facto cósmico.
3. Todo o capítulo é escrito sob reserva explícita do autor: «parece», «pelo que deduzo» (L6697), «Desconfio que» (L6707), «Penso saber que» (L6711), «é o que julgo compreender» (L6817), «conforme penso» (L6841).

O que varia é o **grau de certeza do raciocínio do autor**, não a grafia nem a semântica do termo. Pela matriz homologada, isso não acciona o alerta — cujo peso se reserva à ortografia e à contradição semântica.

**A abstenção decorrente: a ficha NÃO resolve a autoria.** O cadastro tenderia a cravar um responsável; a R1 registra as três formulações, cada uma com a sua linha, sem eleger nenhuma.

## 3. O que a fonte **afirma**

Ao contrário da autoria, a consequência é enunciada sem reserva: «a opção pelo planeta Terra, para que este fosse o palco dos acontecimentos que importariam a todo o cosmos, foi, portanto, um fator decorrente da **morte do primeiro anjo-clone acidentalmente ocorrida nesta galáxia**» (L6647–L6657).

Registrada como **consequência declarada**, não como causa confirmada.

## 4. Alargamento (§6)

Os blocos do censo eram «L4255‑4272, L6639‑6669, L6696‑6739». O **sumário** (L36) e o **título do capítulo** (L6383) estavam fora e foram alcançados por leitura estendida, por serem as ocorrências canónicas do termo.

## 5. O poço revelou a sua composição final

Com a B033 fechada, o poço tem **30 códigos: 10 activos + 20 congelados** — e os 20 congelados são **exactamente** os de evidência só-em-palestras (RC‑839, RC‑857, RC‑861, RC‑864, RC‑866…RC‑933), isto é, a série P integralmente caracterizada:

| Activo | Obra |
|---|---|
| RC‑233 Marca Val | B017 |
| RC‑234 Cidades Voadoras | B018 |
| RC‑235 Teurgistas | B039 |
| RC‑270 Linhagem dos Patriarcas Hebreus | **B013** |
| RC‑347 Projeto Terra | **B026** |
| RC‑352 A Segunda Grande Vinda | B025 |
| RC‑368 Assessoria Cósmica | B011 |
| RC‑372 O Ser Humano Emancipado | B049 |
| RC‑377 Brendiver e Dolman | B043 |
| RC‑931 Nuctemeron | B016 |

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; a ficha nasce 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slug ASCII.** Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre é **1 linha**, só o sinalizador `ficha`.
- **Higienização NÃO antecipada** (EL antes de Transform). **Espelhos .xlsx/.docx adiados** (congelados em 768; Base em 810).

| Indicador | Antes (U66) | Depois (U67) |
|---|---:|---:|
| **Fichas** | 809 | **810** |
| **GAP** | 137 | **136** |
| Família B v3 — restantes | 31 | **30** (10 activos + 20 congelados) |
| **B033 — restantes** | 1 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 810 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 810 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 810 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U67-R1-LOTE24-2026-09-13.json` · `termos/RC-227-opcao-terra-estrategia-necessaria.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
