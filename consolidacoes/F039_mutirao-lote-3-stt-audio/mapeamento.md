# F039 · Mapeamento — Lote 3 (STT & Áudio), pré-governado em blocos

Conforme o plano aprovado no despacho F038/Q-E: **aprova-se a lógica do bloco, nunca a flag individual**.

## Revalidação do censo (1ª tarefa, obrigatória)

O censo-mestre de F037 contava **111 linhas** para L3. Contra o estado vivo das fichas (pós-L1/L2):

1. **111 → 86** por linha: 25 linhas morreram (flags adjudicadas em L1/L2, linhas reescritas, ou menções `«[REVISAR]`» meta dentro de notas de ciclos anteriores);
2. **86 → 79** por token com as guardas constitucionais (corte antes de `## Nota`, exclusão de backticks/aspetos, vocabulário de adjudicação ampliado: ENCERRADO/CHANCELA/FONTE/→);
3. **hóspedes: 0** — nenhum token vivo fora do censo (diferente do Lote 2, que pescou Olga);
4. Métrica de auditoria: **189 vivas no repo** — bate exatamente com o saldo oficial do L2. (O runner interno marca 190 por uma fronteira de backtick em RC-080; oficial: 189.)

Corpus de sondagem: 46 `original.txt` de `livros/` + apostilas — **regra estatística afinada neste lote**: a transcrição STT das apostilas NÃO vale como "par impresso" (é a mesma fala transcrita; contá-la é circular). Só `livros/` decide. O auto-censo inicial, que misturava os dois, produziu aberrações («com» 83.212×) — descartado e substituído por contagem por palavra na tabela abaixo.

## Blocos (79 flags · 55 fichas)

| Bloco | Flags | Chancela-padrão proposta | Exceções fecháveis (prova) |
|---|---|---|---|
| B1 nomes próprios | 1 | AGUARDA-ÁUDIO | anjo «Português» (RC-485 l.20): epíteto dito, não grafia — fica no bloco |
| B2 títulos de obras | 9 | AGUARDA-ÁUDIO | nenhuma: «O Sinal de Lemur» (RC-080) já é decisão do curador lavrada e suas flags eram meta (backtick); «Jesus Niet» (RC-072 l.224), «Ray Cursel» (RC-644 l.38) — 0× no impresso, áudio decide |
| B3 termos/vocábulos orais | 4 | AGUARDA-ÁUDIO | **×2 fecháveis por precedente** (ver abaixo) |
| B4 historicidade externa | 3 | **TENSÃO NÃO-RESOLVÍVEL INTRA-ARCA** (precedente Senequeribe, L2) | — |
| B5a números cósmicos | 48 | AGUARDA-ÁUDIO (número fica como falado; sem renomear nada) | 1 par lavrável (RC-425, ver D1); os demais são datas de palestra («2021/2023»), cuja contagem genérica no corpus não prova o caso — rejeitado como evidência pelo princípio L2 de releitura integral da linha |
| B5b quantidades locais | 14 | AGUARDA-ÁUDIO | — |

## As duas exceções com prova (propostas de ENCERRADO-PRECEDENTE)

1. **RC-425 l.26 — «quechava/quechada» = STT de «(o avatar) Keshava»**. Contagem soberana: *quechav* **0×** em livros (só 25× nas transcrições STT de apostilas, como era de esperar do artefato) × *keshava* **31×** impresso — e a própria ficha-mãe RC-081 tem «avatar keshava de vishnu» no título. Equivalência lavrada nos termos da D1 (Isar=Ishtar): grafia de fala registrada, código não renomeado.
2. **RC-836 l.20 — variação «Awayem» no forno de Awayen**. É a mesma matéria chancelada no L2 (RC-132/RC-771: Awayem sob FONTE AUSENTE DA ARCA — despacho Q-C). Proposta: encerrar por referência cruzada ao carimbo do L2 («a querência é de áudio e a obra-fonte não é possessa; grafia do bruto preservada»), sem novo despacho de conteúdo — o curador apenas confirma que o precedente alcança esta ficha.

## Forma do carimbo (uma nota por ficha, cobrindo todas as linhas do lote)

`[REVISAR] → AGUARDA-ÁUDIO 2026-09-06 · F039-L3: STT preservado como falado — ver nota` — e uma única secção final por ficha: «## Nota — MUTIRÃO REVISAR · Lote 3 — STT & Áudio (06/09/2026 · despacho Q-F039… bloco Bx)», listando as linhas carimbadas e as exceções fechadas com âncora verbatim. Fichas com mais de uma linha do lote (são 15) (RC-009, RC-024, RC-072, RC-102, RC-414, RC-530, RC-565, RC-759, RC-769, RC-777, RC-467, RC-489, RC-080…) recebem nota única multi-linha.

## Roster completo

`roster-l3.csv` (79 linhas: bloco · ficha · linha · contexto da flag · marca de fechável).
