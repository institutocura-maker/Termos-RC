# CERTIDÃO — U50 · DOIS ATOS
## (A) Normalização do localizador e novo censo v3 · (B) R1 · LOTE 7: os 8 da B001

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** autorização do Curador de 13/09/2026 — (1) normalização do localizador APROVADA, com a diretriz estrita de que o texto capturado permaneça *verbatim*; (2) re-rodar o censo e **reportar os números antes de processar** eventuais códigos recuperados de C, D ou E; (3) lote 7 APROVADO (os 8 da B001); (4) R3 (21 D + 17 C) e R4 (52 E) mantidos congelados
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

# ATO A — A normalização do localizador e o censo v3

## A.1 O que foi implementado

`ferramentas/censo_gap_v2.py` ganhou a função `colapsar_espacadas()` e a normalização `norm2()`:

```
um espaço entre letras  → remove   (C O L M E I A  → COLMEIA)
dois ou mais espaços    → um       (COLMEIA  DO    → COLMEIA DO)
```

`norm2` é usada **exclusivamente** no localizador (`buscar`, `tem_bloco` e o índice `norm2` de cada bloco recomposto). O campo `norm` — e, sobretudo, o `texto` de onde saem as citações — permanece intacto: **nada do que vai para as fichas passa pelo colapso**. A diretriz do Curador está cumprida por construção, não por cuidado.

Dois modos de chamada:

```
python3 ferramentas/censo_gap_v2.py                       # v3 (regra nova)
python3 ferramentas/censo_gap_v2.py --sem-espacadas \
        --saida=<base>                                    # v2, bit a bit
```

## A.2 Uma armadilha que quase passou

A primeira implementação aplicava o colapso ao **parágrafo já recomposto**. Não funciona: o compositor de blocos faz `re.sub(r"\s+", " ", texto)`, de modo que, ao chegar ao colapso, os dois espaços que separam palavras já tinham virado um — e `C O L M E I A  D O  É D E N` colapsava para `colmeiadoeden`, uma palavra só, que não casa com a chave.

**Correção:** o colapso passou a correr sobre o texto **bruto** (`bruto = "".join(partes)`, antes do `re.sub`), onde a distinção 1 espaço / 2 espaços ainda existe. Foi apanhado em teste, antes de qualquer censo ser rodado.

Com a correção, a RC‑177 ganhou o bloco **725‑757** (a abertura do capítulo 2 da B044) que a v2 não via; RC‑180, RC‑181 e RC‑182 ganharam, cada um, o bloco do seu título de capítulo.

## A.3 Prova de neutralidade

Rodou-se a v2 de novo, com `--sem-espacadas`, sobre os mesmos 273 códigos:

```
v2 arquivada  ×  v2 reproduzida  →  0 divergências em 273 códigos ✓
```

A refactoragem do instrumento é neutra: o que mudar daqui em diante vem da regra nova, não da reforma do código.

## A.4 Resultado do censo v3

| Família | v2 | v3 | Δ |
|---|---:|---:|---:|
| A · alias-variação | 6 | 6 | — |
| **B · prosa citável na fonte declarada** | 166 | **167** | +1 |
| C · prosa fora das fontes declaradas | 17 | 17 | — |
| **D · só-estrutural** | 21 | **20** | −1 |
| E · não achado no corpus | 52 | 52 | — |
| F · nome ambíguo | 11 | 11 | — |

**Exatamente 1 código muda de família em 273** — e nenhum se perde:

| Cód. | Verbete | v2 → v3 | Fonte | Onde apareceu |
|---|---|---|---|---|
| RC‑309 | Ordem dos Indecifráveis | **D → B** | B022 | título do cap. 9, em caixa alta espaçada (L5338) |

```
B022 L5338: O S  A D H Y T I A  E  A  “ O R D E M  D O S  I N D E C I F R Á V E I S ”
```

## A.5 Efeito nos poços — **reportado, não processado**

| Poço | v2 | v3 |
|---|---:|---:|
| **R1** (família B, sem ficha) | 85 | **86** |
| R3 (D + C) — congelado | 38 | **37** |
| R4 (E) — congelado | 52 | 52 |

**RC‑309 fica REPORTADA E INTOCADA.** O Curador pediu os números antes de qualquer processamento, e assim se faz: nenhuma ficha foi aberta para ela, nenhum fragmento extraído, nenhuma aresta tocada. Ela saiu do bloco congelado da R3 (era D) e entrou no poço da R1 — donde **aguarda despacho**: pode entrar num lote futuro da B022, ou em lote próprio, como o Curador decidir.

Artefatos: `diagnostico/CENSO-V3-ESPACADAS-2026-09-13.{json,md}`. O censo v2 (`CENSO-RECLASSIFICADO-2026-09-13.*`) **não foi sobrescrito** e continua a ser a referência do despacho vigente; a v3 é o instrumento auditado, à espera de chancela para virar referência.

---

# ATO B — R1 · LOTE 7: os 8 da B001 (*O Drama Cósmico de Javé*)

## B.1 As oito fichas

| Cód. | Verbete | Frag. | Fonte |
|---|---|---:|---|
| RC‑205 | Pai Supremo (Amantíssimo) | 7 | B001 |
| RC‑206 | Divindades Excelsas | 5 | B001 |
| RC‑208 | Criador de Padrões Dependentes | 6 | B001 |
| RC‑209 | Vida de Padrão Dependente | 6 | **B002** (+ B001) |
| RC‑212 | O Grande Dia do Senhor Javé | 8 | B001 |
| RC‑213 | Centro de Comando Paralelo | 7 | B001 |
| RC‑214 | Agente do Mais Alto | 7 | B001 |
| RC‑215 | Emissários da Espiritualidade Maior | 8 | B001 |
| | **8 fichas** | **54** | |

**B001: 8 restantes → 0.** Terceira obra liquidada de um só golpe (B031 na U48, B044 na U49, B001 agora).

## B.2 Achados da B001 — novos artefatos de diagramação

1. **O título do capítulo mora no rodapé**, partido em duas ou três linhas, seguido da numeração («Capítulo 16», L8593); o cabeçalho de cada página o repete inteiro. Exemplo (RC‑215):
   ```
   L4208: Emissários da Espiritualidade Maior     ← cabeçalho
   L4229: Emissários da / L4230: Espiritualidade / L4231: Maior.   ← rodapé
   L4232: Capítulo 8
   ```
   **Nenhuma ficha afirma a numeração do capítulo**: o livro não traz sumário numerado, e a posição do título no rodapé não autoriza inferi-la. As três posições são citadas *verbatim*.
2. **Espaços internos em palavras** — «T erra», «V al Ellam», «P ararelo» — e **espaço antes da pontuação** — «Deidade , esta». Nada foi normalizado.
3. **Divergência de grafia dentro da própria obra** (RC‑213): o cabeçalho grafa «Centro de Comando **P ararelo**» (L8232) e o rodapé grafa «Centro de Comando **Paralelo**» (L8255–L8256). Ambas citadas; nenhuma corrigida — aplicação directa do despacho de paridade absoluta de 13/09/2026 (U48).
4. **RC‑209 — a expressão exacta não existe na B001.** A família B assentou-se na **B002**, também declarada no cadastro, onde o termo é definido de propósito («Por que “vida de padrão dependente”? …», L5366–L5374). A ficha cita a B002 e, da B001, a formulação vizinha («criações de padrões dependentes» que era «a especialidade do Senhor Javé», L9302) — **sem fundir as duas formulações nem dar à B001 o que ela não diz**.

## B.3 Método e governança

- **54 fragmentos, 0 falhas, na primeira passada.** A pré-conferência em bloco único (estabelecida na U49) voltou a pagar: os fragmentos foram todos verificados antes de invocar o driver.
- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 8 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada.
- O `diff` do registro-mestre são só os 8 sinalizadores `ficha`.

## B.4 Efeito na Base

| Indicador | Antes (U49) | Depois (U50) |
|---|---:|---:|
| Termos | 946 | 946 |
| **Fichas** | 754 | **762** |
| Relações | 1887 | 1887 |
| **GAP** | 192 | **184** |
| Família B v3 — restantes | 86 | **78** |
| **B001 — restantes** | 8 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Próximos poços da família B (78 restantes), por obra declarada: **P2024‑11‑30 6 · B005 6 · B015 5 · B048 5 · P2021‑02‑28 5 · B052 4 · B019 4**, e os demais distribuídos.

---

# VERIFICAÇÃO (os dois atos)

```
python3 ferramentas/build_indice.py     -> 946 linhas
python3 ferramentas/exportar_json.py    -> 946 termos, 1887 relações, round-trip limpo
python3 ferramentas/build_xlsx.py       -> 946 | 762 | 1887 | 102
python3 ferramentas/build_word.py       -> 946 | 1887 | 102 | 762
python3 ferramentas/build_readme.py     -> 946/762/1887/102

python3 ferramentas/test_suite.py       -> 21/21  EXIT=0
   [T13] 762 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 762 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                             Base intacta: 946 · 762 fichas · 1887 relacoes
```

**Artefatos:** `ferramentas/censo_gap_v2.py` (alterado) · `diagnostico/CENSO-V3-ESPACADAS-2026-09-13.{json,md}` · `diagnostico/U50-R1-LOTE7-2026-09-13.json` · `termos/RC-205…RC-215-*.md` (8 fichas) · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
