# Despacho — rotas e chancela depois do censo v2 (13/09/2026)

Curador: despacho proferido em resposta ao relatório
`diagnostico/CENSO-RECLASSIFICADO-2026-09-13.md` (unidade U45).
Escrivão: agente da sessão `arena/01a09ca0-termos-rc`.

As três decisões abaixo **substituem** o despacho anterior
(`DESPACHO-V-POR-FONTE-DE-LIVRO-2026-09-13.md`) no que conflitarem com ele.

---

## 1. Poço da R1 = os 142 da família B da v2

> «O poço da R1 passa a ser absoluta e integralmente os 142 da família B da v2.
> Se o instrumento `v2` limpou o ruído e encontrou a prosa citável autêntica que
> estava oculta, é exatamente essa a base de dados real que a R1 deve processar.
> O mapa antigo está descartado.»

Consequências operacionais:

- A lista de trabalho da R1 passa a ser lida de
  `diagnostico/CENSO-RECLASSIFICADO-2026-09-13.json` (campo `fam_v2`), **não**
  do censo v1.
- O mapa antigo (`CENSO-GAP-FICHAS-2026-09-13.json`) fica no repositório como
  **memória do erro de medição** — não se apaga histórico — mas perde validade
  operacional para escolha de rota.
- A guarda E3 do driver, que consultava o censo v1 para barrar a família E,
  passa a consultar o censo v2 quando ele existir (feito em U46). Sem isso, a
  guarda voltaria a barrar RC-171, que o v2 provou ser família B.

## 2. E → R4 (compulsório); D e C → R3 (curadoria)

> «SIM para os 52 E: eles vão compulsoriamente para a R4 (declarar ausência,
> lápide, fusão). Se o `v2` limpou o texto e mesmo assim não achou a prosa no
> corpus, não há o que extrair. Para os 21 D e 17 C: eles vão para a R3
> (exceção/curadoria). Como exigem interpretação estrutural complexa ou estão
> fora da fonte declarada, retirá-los da esteira de automação cega da R1 é a
> medida de segurança necessária para evitar alucinações.»

Consequências operacionais:

| Família (v2) | Quantos | Rota | Situação até despacho próprio |
|---|---:|---|---|
| B | 142 | **R1** | materialização em lotes, como vem sendo feito |
| C | 17 | R3 | **fora da R1** — retificação de fontes, curadoria caso a caso |
| D | 21 | R3 | **fora da R1** — citação estrutural exige interpretação |
| E | 52 | R4 | **fora da R1** — declarar ausência / lápide / fusão |
| A | 6 | — | despacho taxonômico próprio |
| F | 11 | — | despacho taxonômico próprio |

Os códigos de cada grupo estão listados no §7 do relatório do censo v2.

## 3. V presuntivo REVOGADO a partir do lote 3

> «NÃO. Fica revogado para os lotes 3 em diante. A deriva de governança foi
> detectada e estancada. Como o instrumento anterior estava comprometido,
> estender a presunção de validação para os novos lotes comprometeria a base.
> Reiniciamos o rigor sobre a nova linha de base da `v2`.»

Consequências operacionais:

- Do lote 3 em diante, **nenhuma** ficha nasce 🟢. Nasce 🟡 provisório e segue
  para leva de chancela, com as citações já extraídas e conferidas.
- O lote passa a declarar `"v_revogado": true` e **não** declara `aplicar_V`;
  o driver registra a revogação no corpo de cada ficha, apontando a este
  despacho.
- As guardas E1–E5 só existem para sustentar a presunção de V: sem V, não se
  aplicam (o driver já as desliga).

### Sobre os 16 🟢 já lavrados por presunção (lotes 1 e 2)

**Não foram revertidos por este despacho** — o Curador revogou a presunção
«para os lotes 3 em diante», sem pedir a revisão do passado. Fica registrado,
para decisão futura, que:

- os 8 do lote 1 (U43) e os 8 do lote 2 (U44) receberam 🟢 por presunção;
- a presunção se apoiava em dois pilares — **fonte de livro declarada** e
  **citação verbatim conferida byte a byte** —, e nenhum dos dois dependia do
  censo; os 16 continuam de pé por esse motivo;
- cada um leva no corpo a nota de reversibilidade, de modo que eventual
  revisão é um ato simples e rastreável.

---

## Próximo passo autorizado

> «Pode avançar com a extração do Lote 3 (As 10 Eras da Criação) operando
> exclusivamente sobre os 142 códigos validados da Família B.»

Lote 3 = RC-156 · RC-157 · RC-158 · RC-159 · RC-168 · RC-169 · RC-170 ·
RC-171 · RC-172 · RC-173 (as 10 Eras da Criação, B024 §16), todos família B
na v2, todos com ficha a nascer 🟡.
