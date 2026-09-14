# CERTIDÃO — U59 · R1 · LOTE 16
## Os 2 da B036 (*Memórias de Javé*)

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 16 APROVADO (a B036) · segregação obra a obra mantida «independentemente do tamanho do lote»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As duas fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑423 | Advogado de Acusação (Ellam × Javé) | 6 |
| RC‑427 | Criatura‑teste (estágio avançado) | 5 |
| | **2 fichas** | **11** |

11 fragmentos verbatim intra-linha, **0 falhas** na primeira passada. Ambos exclusivos da B036. **B036: 2 → 0** (quanto ao sustentável).

**RC‑270 permanece ancorada na B013** — caso já registrado na U57 (inventário de desvios), aqui apenas reafirmado: a evidência do censo para esse código é toda da B013.

## 2. O discurso é de Javé — não do cadastro

A B036 (*Memórias de Javé*) é escrita **na primeira pessoa do Criador**, dirigindo-se ao humano que lhe serve de instrumento. As duas designações deste lote são **palavras da personagem**, e as fichas as registram como tal:

- «Espero poder continuar a me expressar através deste **advogado de acusação** de um julgamento inexistente, mas que ele pensa existir em torno de mim e da minha Obra. Para minha desdita, fui eu mesmo que o contratei, só que não era para esta função.» (L258–L261)
- «agora me obrigo a despertar a todos os que de mim surgiram, e você é a minha **criatura‑teste** deste processo.» (L297–L298)

Nenhuma das duas é adoptada como conceito do cadastro, nem recebe estatuto doutrinário.

## 3. Duas abstenções de fronteira

- **RC‑423:** o cadastro registra o verbete com a fórmula «Ellam × Javé»; a obra, nesta passagem, diz apenas «este advogado de acusação», **sem nomear ninguém**. A ficha **não** introduz o nome próprio que a fonte não escreve.
- **RC‑427:** o cadastro qualifica o verbete como «estágio avançado»; a obra diz «minha criatura‑teste deste processo» (L298) e **não gradua o estágio**. A ficha não transporta o qualificativo para dentro da citação nem o apresenta como sendo da fonte.

É o mesmo tipo de fronteira das unidades anteriores: o que o cadastro sabe, a ficha não empresta à fonte; o que a fonte não diz, a ficha não lhe atribui.

## 4. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 2 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- **Slugs ASCII** nas 2 (`advogado-de-acusacao-ellam-x-jave`, com «x» no lugar do sinal de multiplicação). Nenhuma aresta nova; nenhuma memória deletada. O `diff` do registro-mestre são só os 2 sinalizadores `ficha`.
- **Higienização NÃO antecipada**, por diretriz vigente. **Espelhos .xlsx/.docx continuam adiados** (congelados em 768; Base em 793).

| Indicador | Antes (U58) | Depois (U59) |
|---|---:|---:|
| **Fichas** | 791 | **793** |
| **GAP** | 155 | **153** |
| Família B v3 — restantes | 49 | **47** (27 activos + 20 congelados) |
| **B036 — sustentáveis** | 2 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Poço activo por obra: **B023 3 · B050 3 · B002 2 · B014 2 · B020 2 · B003 2 · B026 2 · B034 2 ·** demais 1 cada.

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 793 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 793 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 793 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U59-R1-LOTE16-2026-09-13.json` · `termos/RC-423-advogado-de-acusacao-ellam-x-jave.md` · `termos/RC-427-criatura-teste-estagio-avancado.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
