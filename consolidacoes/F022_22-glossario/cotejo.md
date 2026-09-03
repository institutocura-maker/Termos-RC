# COTEJO — F022 · 22-GLOSSÁRIO (fase de cotejo com obras de referência)

**Data:** 03/09/2026 · **Branch:** `arena/01a06429-termos-rc`
**Obras de referência (validadas por equipe avançada da RC + Ellam):**
- **B031** — Painéis Emergentes da Revelação Cósmica (referência p/ a maioria dos termos)
- **B060** — Personagens e Terminologias (referência p/ personagens)
- **B050** — Guia das Eras Universais · Mapa (referência p/ períodos/datas/eras)

As três obras estão em `livros/CONCLUIDOS/B031|B060|B050_*/original.txt`.

---

## 1. Dimensão do cotejo

| Fonte | termos que a citam | com ficha |
|---|---|---|
| B031 | 147 | 64 |
| B060 | 71 | 50 |
| B050 | 17 | 12 |
| **≥1 das três (união)** | **198** | **101** |
| Eleváveis (provisório + ficha + cita obra revisada) | **97** | — |

---

## 2. Triagem das duplicatas D5–D9

| # | Par | Veredito (cotejo) | Recomendação |
|---|---|---|---|
| D5 | Favor Divino RC-063 × RC-332 | **NÃO é duplicata.** A ficha RC-332 declara explicitamente: RC-063 = *título/obra* (B048 «Favor Divino»); RC-332 = *conceito* («favor divino invertido»). Pares complementares deliberados. | **Manter ambos.** Sem merge. (Documentado na ficha RC-332.) |
| D6 | Choque de Realidade RC-867 × RC-898 | RC-867 (cand., sem ficha) está na **fila aberta de materialização** (P2022-11-26, "donos da verdade"); RC-898 (prov., com ficha e verbatim P2024-02-04) é o termo **materializado**. Mesmo referente. | **Merge**: `RC-867 --variação--> RC-898`. Preservar a faceta "donos da verdade" como nota/observação. |
| D7 | Criaturas-ferramenta RC-164 × RC-449 | RC-449 ficha declara-se **"sinônimo funcional de RC-164"** (mesma fonte P2021-03-27); há relações compartilhadas (RC-764, RC-148 ligam a ambos). RC-164 tem fontes canônicas B024/B035/B019; RC-449 agrega B057/B058. | **Merge com consolidação**: manter RC-164 canônico; `RC-449 --variação--> RC-164`; conteúdo único de RC-449 (B057/B058) preservado por relação/ficha (sem apagar). |
| D8 | Fenômenos Denunciadores do Fim RC-203 × RC-314 | RC-203 (cand., sem ficha) = título no sumário de B035; RC-314 (prov., ficha) = termo materializado de B022 (cap. 4). RC-690 relaciona-se com **ambos** → mesmo referente. | **Merge**: `RC-203 --variação--> RC-314`. |
| D9 | Val dos Corpos Perdidos RC-133 × RC-493 | RC-133 (prov., B031) = agrupador canônico; RC-493 (cand., B061) = "Os 9 Val", mesma referência aos Val dimensionados (a fonte de referência é B031). | **Merge**: `RC-493 --variação--> RC-133`. |

> Todos os merges seguem o padrão já aplicado em D1–D3 (relação `variação` sobre código imutável, sem apagar). D5 fica **sem merge** (par deliberado).

---

## 3. Elevação de STATUS — proposta

**Premissa aprovada:** o conteúdo das obras B031/B060/B050 foi **revisado por equipe avançada da RC e pelo próprio Ellam** → passa a funcionar como **fonte primária curada** para os termos que as citam.

**Conjunto elegível:** termos com `status=provisório` + `ficha=True` + que citam **≥1** das obras revisadas = **97 termos**.

| Eixo | Subgrupo | nº |
|---|---|---|
| provisório + ficha + cita obra revisada | total | **97** |
| …dos quais também citam ≥1 palestra | corroboração cruzada | 91 |
| …dos quais citam ≥2 obras revisadas | corroboração forte | 22 |

**Proposta de regra de elevação (à escolha do curador):**
- **Opção A (conservadora, recomendada):** elevar os 97 a `em análise` — sinaliza "base sólida em fonte primária curada, aguardando a auditoria fina página-a-página que precede `verificado`". Compatível com a definição vigente de `em análise` = "ficha redigida a partir dos PDFs".
- **Opção B (máxima):** elevar a `verificado` os que citam **≥2** obras revisadas **ou** obra revisada + palestra **com referência página a página** nas fichas (subconjunto a confirmar caso a caso) → `em análise` os demais.
- **Opção C:** não elevar agora; só registrar a "banca de referência" como metadado de confiança.

> Recomendação do piloto: **Opção A** como passo seguro e auditável nesta rodada (eleva 97 provisórios → em análise), deixando `verificado` para uma auditoria página-a-página dedicada. O que não deve ocorrer é manter `candidato/provisório` para termos já ancorados em obra revisada sem sinal de consolidação.

---

## 4. Ações pendentes de confirmação do curador

| # | Decisão | Opções |
|---|---|---|
| Q-M1 | Aplicar merges D6, D7, D8, D9 (relações `variação`) + manter D5? | Sim (recomendado) / parcial / não |
| Q-M2 | D7 (RC-449→RC-164): além da relação, consolidar o conteúdo B057/B058 de RC-449 na ficha RC-164? | Sim / só a relação |
| Q-E1 | Regra de elevação a adotar | Opção A / B / C |
| Q-E2 | Se B ou C: detalhar critério (a definir) | — |

*Este arquivo não altera a base; documenta o cotejo para a devolutiva.*
