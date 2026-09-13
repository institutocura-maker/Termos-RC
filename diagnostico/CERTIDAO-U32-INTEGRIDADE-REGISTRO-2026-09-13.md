# Certidão U32 — reparo de integridade do registro-mestre (13/09/2026)

**Como se achou**: ao gerar a proposta da leva P7m (tema 1.5), o campo `DECISÃO` da linha de RC-479
saiu deslocado — a planilha estourou 11 colunas. Investigo: o cadastro carregava em `fontes` a
string `'P2026-08-04; RC-286; RC-072'` — um **fragmento de rel colado na fonte**, herança de eras
anteriores ao frontmatter. Censo integral: **9 termos** com o mesmo padrão — RC-005, RC-074, RC-274,
RC-475, RC-479, RC-494, RC-564, RC-580, RC-718 (todos com `P<sigla de data>; RC-x[; RC-y]`).

**Reparo executado (cirúrgico, região TERMOS apenas — as linhas RELACOES têm o mesmo prefixo
`("RC-…` e ficaram intocadas; lição lavrada)**:
1. `fontes` limpas: fica só a sigla da obra (ex.: `P2026-08-04`).
2. As referências órfãs voltam ao espelho `t[6]` onde faltavam (M3 já promovera a maioria):
   RC-074 ← RC-286; RC-479 ← RC-286 + RC-072.
3. Propagação pelo mecanismo M3 visto dos dois polos: a tabela de RC-286 recebeu a linha
   «Belial (arconte; 'Satã' do livro de Jó) | RC-479 | associado» (T14 a exigiu — o espelho é
   simétrico nos polos).
4. Frontmatter das 9 fichas regerado pelo molde `fm_toml` (paridade T13/T15).

**Provas**: verificador 946·673·1887; suíte sola 21/21 (T14: 0 divergentes; T15: 673/0);
`RELACOES` intocado (1887 — nenhuma aresta criada/reetiquetada); builds regenerados.
Os orfãos agora restaurados ao espelho eram NAVEGAÇÃO (t[6]) — sem efeito em arestas.
