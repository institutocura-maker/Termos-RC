# CERTIDÃO — U49 · R1 · LOTE 6
## Os 8 códigos da B044 (*A Divina Colmeia*) — bloco único, sem V

**Data:** 13/09/2026 (dia curatorial da campanha R1; a unidade foi lavrada em continuidade imediata à U48)
**Rota:** R1 — materialização de códigos só-no-cadastro (`ficha=False`) com citação *verbatim* intra-linha conferida byte a byte (precedente U30)
**Despacho:** autorização do Curador de 13/09/2026 — lote 6 aprovado, com a recomendação expressa de «liquidar agrupamentos semânticos oriundos de uma mesma fonte de um único golpe»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. O que foi feito

Oito fichas materializadas, todas da **B044** (*A Divina Colmeia*, Jan Val Ellam), num bloco único — o poço inteiro que esta obra ainda devia à R1, segundo o censo v2.

| Cód. | Verbete | Frag. | Fonte | Observação |
|---|---|---:|---|---|
| RC-177 | Colmeia do Éden | 7 | B044 | título do **capítulo 2** |
| RC-180 | Fator Colmeia | 6 | B044 | título do **capítulo 15** |
| RC-181 | Pluribus Unum | 6 | B044 | título do **capítulo 13** |
| RC-182 | Unus Pluribum | 6 | B044 | título do **capítulo 14** |
| RC-183 | Cultura Demodhármica | 6 | B044 | nota explicativa + corpo |
| RC-184 | Trava-demo | 4 | B044 | ocorrência única (L2993) |
| RC-185 | Horda Colmeia | 5 | B044 | ocorrência única (L3412) |
| RC-187 | Insectoides | 6 | B044 | corpo (caps. 1 e 7) |
| | **8 fichas** | **46** | | |

**Com isto, a B044 está liquidada na R1: de 8 restantes para 0.**

---

## 2. Achado novo — a caixa alta espaçada dos títulos de capítulo

Ao localizar RC‑177, verificou-se que a expressão «Colmeia do Éden» só ocorre **duas vezes** na B044, ambas em posição estrutural (SUMÁRIO L46 e índice de Notas L5542). No corpo, o capítulo 2 existe, mas o seu título está grafado em **caixa alta espaçada**:

```
A  “ C O L M E I A  D O  É D E N ”          (B044 L727)
```

Essa grafia **derrota a busca normalizada** que o censo (v1 e v2) emprega para localizar as chaves — exactamente o mesmo tipo de artefato de medição que motivou a reclassificação v2 (agora com o hard‑wrap), só que numa variante nova: não é a frase que se parte, é a própria palavra.

Consequência prática, já aplicada neste lote: **quatro dos oito códigos (RC‑177, RC‑180, RC‑181, RC‑182) são títulos de capítulo** e, por isso, estavam sub-localizados no censo. Os seus títulos foram citados *verbatim*, com os espaços da edição preservados, e passaram pelo portão B byte a byte — o que valida a paridade inclusive sobre esse artefato.

Mapa de capítulos da B044, com as linhas (todos em caixa alta espaçada no corpo):

| # | Capítulo | Linha | | # | Capítulo | Linha |
|---|---|---:|---|---|---|---:|
| 1 | A “Abelha-Rainha” e os seus Súditos | 145 | | 9 | Ignorância Cultivada e Crescente | 3252 |
| 2 | **A “Colmeia do Éden”** | 727 | | 10 | Inesperada Liberdade | 3398 |
| 3 | A “Colmeia Universal” e Seus Dois “Grandes Favos” | 1225 | | 11 | Subordinação aos Fins | 3566 |
| 4 | Cego Guiando Cegos | 1643 | | 12 | “Mediocridade e Vexame” vistos como “Divinos” | 3731 |
| 5 | Três “Amalucados” e Quintilhões de “Apalermados” | 2026 | | 13 | **Pluribus Unum** | 3983 |
| 6 | “Projeto Talm” | 2249 | | 14 | **Unus Pluribum** | 4337 |
| 7 | O “Plano Colmeia” para o Universo Biológico | 2627 | | 15 | **O “Fator Colmeia” e o Cenário Final** | 4618 |
| 8 | Subserviência “Deslacrada” | 2978 | | | | |

**Recomendação registrada (não despachada):** o localizador do censo (`censo_gap_v2`) pode receber uma normalização que colapse `C\s+O\s+L\s+M\s+E\s+I\s+A` → `COLMEIA` antes de comparar, para que títulos em caixa espaçada passem a ser vistos. Fica como proposta ao Curador; **nada foi alterado no instrumento nesta unidade**.

---

## 3. Auditoria da extração

- **46 fragmentos** conferidos byte a byte contra `livros/CONCLUIDOS/B044_a_divina_colmeia/original.txt`; **0 falhas** no portão B.
- **4 erros meus de transcrição**, todos apanhados pelo portão antes de qualquer escrita:
  1. RC‑177 L775 — tomei a sentença recomposta de memória; a linha real começa em «submetidas à violência?», e o trecho procurado está partido entre L775 e L776 → desdobrado em dois fragmentos.
  2. RC‑185 L3417 e L3418 — deslocamento de duas linhas (L3417 é «” – mais especificamente os que fizeram») → renumerados para L3418/L3419.
  3. RC‑187 L611 — um «um» omitido («apresentam **um** comportamento “automatizado”»).
  
  **Lição aplicada a partir daqui:** em vez de iterar uma falha por vez, passou-se a pré-conferir **todos** os fragmentos do lote numa única passada antes de invocar o driver. É o mesmo tipo de prevenção que a U47 estabeleceu ao não confiar na contagem de linhas de memória.
- **V revogado** (despacho vigente, do lote 3 em diante): o lote declara `"v_revogado": true`, **sem** `aplicar_V`; as guardas E1–E5 ficaram desligadas; `ficha` passou `False → True`; **status preservado** — as 8 nascem 🟡 (provisório). **Nenhum 🟢 foi acrescentado**: 572 continuam 572.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada.

---

## 4. Efeito na Base

| Indicador | Antes (U48) | Depois (U49) |
|---|---:|---:|
| Termos no cadastro | 946 | 946 |
| **Fichas materializadas** | 746 | **754** |
| Relações | 1887 | 1887 |
| **GAP (`ficha=False`)** | 200 | **192** |
| Família B v2 — restantes | 93 | **85** |
| **B044 — restantes** | 8 | **0** |
| 🟢 verificado (fichas) | 572 | 572 (inalterado) |
| 🟡 provisório (fichas) | 72 | 80 (+8) |
| 🟠 em análise (fichas) | 102 | 102 |

Status do **cadastro** (946 termos, `dados_termos.TERMOS[t][4]`): 572 verificado · 212 provisório · 102 em análise · 60 candidato — **inalterado**. As 8 já eram provisórias como registro; a virada é só `ficha False→True`, sem promoção (V revogado).

Próximos poços da família B v2 (85 restantes), por obra declarada: **B001 8 · P2024‑11‑30 7 · B005 6 · B015 5 · B048 5 · P2021‑02‑28 5**, e os demais distribuídos. Fora da R1, por despacho: R3 (21 D + 17 C) e R4 (52 E, compulsório).

---

## 5. Verificação

```
python3 ferramentas/build_indice.py     -> 946 linhas
python3 ferramentas/exportar_json.py    -> 946 termos, 1887 relações, round-trip semântico limpo
python3 ferramentas/build_xlsx.py       -> 946 termos | 754 fichas-resumo | 1887 relações | 102 obras
python3 ferramentas/build_word.py       -> 946 | 1887 | 102 | 754
python3 ferramentas/build_readme.py     -> 946/754/1887/102

python3 ferramentas/test_suite.py       -> 21/21  EXIT=0
   [T13] 754 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter das fichas · 754 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte e todo codigo existe na Base.
                                             Base intacta: 946 termos · 754 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/U49-R1-LOTE6-2026-09-13.json` (lote) · `termos/RC-177…RC-187-*.md` (8 fichas) · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
