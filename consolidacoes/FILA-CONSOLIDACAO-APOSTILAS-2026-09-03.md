# FILA PRIORIZADA — Esteira de Consolidação sobre as Apostilas Refatoradas

**Data:** 03/09/2026 · **Branch:** `arena/01a06429-termos-rc` · **Documento de planejamento** (não altera a base)

> Objetivo: aplicar a mesma **Esteira de Consolidação** usada no piloto **F022 (22-GLOSSÁRIO)** sobre os
> documentos refatorados de `apostilas/CONCLUIDAS/*/apostila.md` — cada um é uma **recompilação revisada**
> de uma palestra/obra Ellam (v3.1-MP, normalizada, RAG-optimal). A esteira: **levantamento (mapeamento) →
> devolutiva → merges/elevação → documentação**, sem fabricar conteúdo não ancorado.

---

## 1. Contexto e volume

- **81 apostilas concluídas**, cada uma com `original.txt` (fonte bruta, byte a byte) + `apostila.md` (versão refatorada/normalizada) + ocasionalmente `analise/`, `ficha_ingresso.md`, `apostila.docx`.
- **Formato v3.1 estruturado** (`@metadata`, `@tese`, `@datas`, `@glossario`, `@autoridade_leitura`) — o mais favorável à consolidação — presente em pelo menos 4: `2018-05-20`, `2019-04-14`, `2019-08-25`, `2023-12-17`. As demais têm formatos mais antigos/heterogêneos.
- **Datas variam de 2017 a 2026.** Vários documentos correspondem a palestras cujos termos já foram ampliados na base (códigos RC-001..926) em ciclos anteriores; outros podem conter **termos/grafias ainda não registrados** → fonte de confirmação e de eventuais lacunas.

---

## 2. Critérios de priorização

A ordem da fila combina 4 critérios:

| Critério | Peso | Justificativa |
|---|---|---|
| **Estrutura v3.1** (mais parseável) | alta | mapeamento mais confiável e barato |
| **Riqueza em personagens** (casa com B060) | alta | permite elevação segura de status |
| **Relevância temática central** (Trimurti, Sophia, Jesus, Arcontes, Pandora, Fornos/Talm, Lúcifer) | média | núcleo da KB |
| **Proximidade temporal recente** (2023–2026, já consolidadas editorialmente) | média | texto mais revisado, menos erros de STT |

Prioriza-se começar por apostilas **v3.1** e por temas centrais, deixando por último as mais periféricas/heterogêneas.

---

## 3. FILA (ordem recomendada de processamento)

### Lote 1 — Apostilas v3.1 estruturadas (piloto estendido)
| # | Data | Tema | Por que aqui |
|---|---|---|---|
| 1 | 2019-08-25 | Os Três Fornos Replicadores do Projeto Talm | v3.1; núcleo Fornos/Talm; ~30 RC; já gerou RC-836/837 |
| 2 | 2018-05-20 | De Pandora a Eva e o Culto a Lilith | v3.1; Pandora/Lilith; personagens (B060) |
| 3 | 2019-04-14 | Javé versus Pandora: A Prole sem Face | v3.1; Pandora/Javé |
| 4 | 2023-12-17 | Lúcifer e a Rebelião dos Elétrons | v3.1; Lúcifer/elétrons; núcleo da Rebelião |

### Lote 2 — Tema central / recentes (2023–2026)
| # | Data | Tema |
|---|---|---|
| 5 | 2024-11-30 | Morus e os Arquivos do Destino Universal |
| 6 | 2023-09-09 | O Colapso da Trimurte e suas Consequências |
| 7 | 2023-06-24 | O Buraco Negro Mental e o Estacionamento Coletivo |
| 8 | 2024-08-03 | Falência dos Deuses / Destinação do Lobo |
| 9 | 2024-05-04 | Prabrajna, Perpérion, Simultaneidade Reversa |
| 10 | 2022-12-17 | Ano 2012 — Falsa Noção de Fim do Mundo |

### Lote 3 — Personagens / Pandora (B060)
| # | Data | Tema |
|---|---|---|
| 11 | 2023-12-02 | Thot Enigmático / Hermes Trismegisto |
| 12 | 2024-11-03 | Apolônio de Tiana e o Quarto Logos |
| 13 | 2023-08-05 | O Velho Sonho de Ares |
| 14 | 2017-05-14 | O Desvio de Rota de Pandora e o Quarto Logos |
| 15 | 2018-02-24 | Pandora e a Estratégia dos Avatares (fonte de RC-797/800/801) |

### Lote 4 — Demais apostilas (2018–2026, heterogêneas) — 60+ itens
Ordem cronológica preferencial dentro do tema (Sophia → Jesus → Arcontes → conceitos → "Estagiários do Kaos" → "Irmãos Dias" podcast). Lista completa disponível em `apostilas/CONCLUIDAS/` (81 pastas, datas de 2017-05-14 a 2026-08-04).

---

## 4. Regras aplicadas por documento (padrão F022)

1. **Carregar fonte** em `consolidacoes/F###_<slug>/` (cópia da `apostila.md` como `fonte.txt`), registrar sigla `F###`, SHA e metadata.
2. **Mapear** termos/entidades do texto → códigos RC (com matcher assistido + curadoria).
3. **Anti-duplicação** antes de qualquer código novo.
4. **Registrar divergências** no Divergence Ledger; nada auto-resolvido sem cotejo.
5. **Elevação de STATUS** só nos casos seguros (termo já ancorado em obra revisada e confirmado; sem pseudoconfirmação). Como as apostilas derivam do MESMO corpus, servem mais como **auditoria/confirmação de leitura** que como corroboração independente — o mesmo cuidado do F022.
6. **Devolutiva ao curador** antes de aplicar alterações na base em cada documento (ou lote).

---

## 5. Governança — decisões solicitadas antes do processamento em massa

| # | Pergunta | Recomendação |
|---|---|---|
| G1 | **Fonte para elevação:** as apostilas são fontes P (palestras), não B031/B060/B050. Posso usar a presença numérica/consistente de um termo na apostila apenas como **auditoria**, e elevar status **somente** quando houver obra primária revisada (B031/B060/B050) ou revisão do curador? | Sim (não elevar só por apostila) |
| G2 | **Escopo por rodada:** processar a fila **documento a documento** (com devolutiva a cada um) ou **em lotes** (ex.: Lote 1 inteiro → uma devolutiva)? | Lote a lote (mais eficiente) |
| G3 | **Criação de termos novos:** nas apostilas há itens que podem não estar na base. Mantém-se a política de **não criar código novo sem necessidade e sem fonte primária** (tratar como variação/duplicata quando for o caso)? | Sim |
| G4 | **Prioridade imediata:** começar pelo **Lote 1** (v3.1) agora? | Sim |

> Este documento é um **plano**; não altera a base. O processamento efetivo de cada lote gera estrutura em
> `consolidacoes/` e segue o fluxo levantamento → devolutiva → aplicação.

---

## 6. Decisões do curador (03/09/2026)

| # | Pergunta | Decisão |
|---|---|---|
| G1 | Fonte para elevação de STATUS | **Apostila = auditoria.** Não elevar status só por apostila. Elevar apenas termos já ancorados em obra primária revisada (B031/B060/B050) ou que ganhem citação primária P (palestra, página a página) — sempre com revisão do curador. |
| G2 | Escopo por rodada | **Em lotes** — devolutiva conjunta por lote. |
| G3 | Criação de termos novos | **Não criar código novo sem necessidade/fonte primária.** Itens novos tratados como variação/duplicata/sem-código quando for o caso. |
| G4 | Iniciar Lote 1 | **Sim — iniciar o Lote 1 (apostilas v3.1)** nesta sessão. |

