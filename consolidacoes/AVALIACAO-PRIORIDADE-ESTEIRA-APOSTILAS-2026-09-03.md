# AVALIAÇÃO — Prioridade da Esteira de Apostilas vs. Outros Arquivos para Consolidação da KB

**Data:** 03/09/2026 · **Pedido:** avaliar a importância do processo de consolidação sobre apostilas, considerando pausá-lo para priorizar arquivos ainda não processados de maior consolidação. **Branch:** `arena/01a06429-termos-rc`.

---

## 1. Resumo executivo
**Recomendo PAUSAR (depriorizar) a esteira de apostilas** e redirecionar o esforço para **fichas em falta, elevação de STATUS via cotejo de obras primárias (livros B) e duplicatas**. A evidência abaixo mostra que as apostilas têm **baixo valor marginal incremental**: elas já foram a *fonte de origem* dos códigos, então reprocessá-las gera quase só auditoria, sem termos novos e sem elevação de status.

---

## 2. Por que a esteira de apostilas é de baixo valor marginal (evidência do Lote 1)
- **As 4 apostilas do Lote 1 já estão 100% integradas**: todos os conceitos que declaram "criar" (RC-813..818, 819..825, 826..833, 836/837) **existem** na base e já citam a fonte P.
- **Natureza das apostilas:** são `v3.1-MP` = *produtos de treinamento* (normalizadas e "RAG-optimal") **derivadas do mesmo corpus já minerado**. Não são obra primária nova.
- **Consequência (decisões G1/G3):** como são fontes **P (palestras)**, **não podem elevar STATUS** (só obra B primária + curadoria o faz) e **não trazem termos novos**. O ganho restante é: checagem de consistência ficha↔cadastro (V-1) e detecção de ruído editorial — **auditivo, não de crescimento**.
- Logo, as **81 apostilas** (77 restantes) renderiam, no melhor caso, **auditoria de consistência**, com custo alto (1 apostila = ~1 levantamento) e **retorno baixo**.

---

## 3. Oportunidades de MAIOR consolidação (fundamentadas em dados da base)

### A) Termos registrados SEM ficha markdown (~271 substantivos)
Dos **929 termos**, apenas **623 têm ficha**; **306 não têm arquivo de ficha**, e ~271 deles **não são aliases** (não participam de relação `sinônimo`/`variação`). Entre eles há termos centrais: RC-006 Guerra do Éden, RC-011 Adhy, RC-030 Atlantes, RC-034 Big Bang, RC-162 Elétrons, RC-289 O Vício de Epimeteu, RC-300 Dissolução da Tríade, RC-301 Prometeu, RC-302 Epimeteu, RC-305 Têmis, RC-414 Krishna etc.
> **Ação candidata:** confirmar se a ausência de ficha é *design* (termos-só-índice) ou *lacuna*; se lacuna, criar fichas é o maior salto de completude da KB.

### B) Elevação de STATUS via cotejo de obras primárias (livros B) — F022 provou o método
O piloto F022 elevou **22 → `verificado`** e **75 → `em análise`** usando B031/B060/B050. Há hoje na base:
- **149 termos citam B031**, **74 citam B060**, **17 citam B050**.
- **100 `provisório` + 4 `candidato`** já citam B031/B060/B050 e **ainda não foram elevados** (o cotejo do F022 foi escopado; não cobriu a KB inteira).
> **Ação candidata:** uma passada de **cotejo global** sobre esses ~104+ termos, confirmando citação página a página, elevaria um bloco grande de `provisório`/`candidato` → `em análise`/`verificado`. Isto é o que mais **qualifica** a KB (status é o selo de confiança).

### C) Obras (livros B) ainda pouco mineradas / recentes
Das ~47 obras em `livros/CONCLUIDOS/`, só B031 (149), B060 (74), B050 (17) têm cobertura alta. Há obras de peso pouco citadas e **trilogias novas ainda não cotejadas**: **B087/B088/B089 (Trilogia Pandora: Zeus/Titas, Coquetel de Poções, Anunnaki)**, B037 (Inquisição Filosófica/Divina Colmeia), B057/B058 (Revolta do Anjo Caído / Revolta Capelina), B041 (Rebelião dos Elétrons), B044 (A Divina Colmeia), B052 (Homoafetividade), B074/075 (Mentalma).
> **Ação candidata:** cotejar essas obras (fonte primária de conteúdo) eleva status **e** pode revelar termos/afirmações ainda não ancorados.

### D) Duplicatas residuais
O F022 evidenciou D1–D9. O grafo (1884 relações) pode conter outros pares `sinônimo`/`variação` não mergeados. Uma varredura de duplicatas consolida o grafo (reduz nós espúrios).

---

## 4. Comparação de retorno por tipo de trabalho

| Tipo de trabalho | Termos novos? | Eleva status? | Completa KB? | Retorno/$$ |
|---|---|---|---|---|
| **Esteira de apostilas** (P) | quase nunca | não (é P) | baixo | **baixo** |
| **Fichas em falta (A)** | — | parcial | **alto** | alto |
| **Cotejo obras B p/ status (B)** | às vezes | **sim** | alto | **alto** |
| **Cotejo obras B pouco mineradas (C)** | sim | sim | alto | **muito alto** |
| **Merge duplicatas (D)** | — | — | médio | médio |

---

## 5. Recomendação
1. **Pausar a esteira de apostilas** (mantendo-a documentada e retomável; não é descartada).
2. **Prioridade 1 — Cotejo de obras primárias B ainda pouco mineradas/recentes** (B087–089 Trilogia Pandora, B037, B057/058, B041, B044, B052) — maior potencial de novo conteúdo + elevação.
3. **Prioridade 2 — Passada de elevação de STATUS** sobre os ~104 `provisório`/`candidato` que já citam B031/B060/B050 (cotejo global).
4. **Prioridade 3 — Fichas em falta** (~271 substantivas; confirmar design vs lacuna).
5. **Prioridade 4 — Varredura de duplicatas** residuais.

> Os arquivos "ainda não processados" de maior valor são, portanto, **as obras B primárias com pouca/nenhuma mineração** e o **fecho das fichas**, e não as apostilas (que já foram a semente dos códigos).
