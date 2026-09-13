# Certidão Onda 2.4 — notas de processo → `notas/fichas/` (12/09/2026)

**Despacho do Curador (12/09)**: opção `notas_rodape` (arquivo por ficha + uma linha de rastro na carta) e `verbatim_puro` — nenhuma palavra das notas foi alterada; conversão de "linha NN" em âncora **não** executada (as notas são memória do momento da revisão; o cabeçalho de cada arquivo declara isso).

## Execução (U15)
- **336 blocos `## Nota`** movidos de **253 fichas** para `notas/fichas/RC-###.md` (253 arquivos; reconciliação exata com o censo de 11/09: 336 = 336).
- Composição: 241 `Nota — MUTIRÃO REVISAR`, 38 `Nota de governança`, 16 `F043 T2`, 7 `F043 T3`, 6 `DESPACHO CURADORIA`, 3 `pedagógica` + 25 em títulos pontuais demais (336 no total) — todos verbatim.
- Na carta ficou **uma linha de rodapé**: `> Notas de processo: N bloco(s) arquivado(s) VERBATIM em notas/fichas/RC-###.md (migração 2.4 — 12/09/2026)…`.
- Gate de prova: reinserção direta dos blocos nas posições originais + remoção do rodapé **restaura cada arquivo byte a byte** (assert nos 253); frontmatter TOML dos pilotos intacto (gate separado).

## Verdes
- `grep '^## Nota' termos/` → **0** (porta do plano cumprida: zero nota no corpo das fichas; também zero no docx — espelho de leitura agora só mostra ouro).
- Suíte OK · JSON canônico 946/1887 válido · builds regenerados (docx mostra o rastro, sem `+++`).
- **verificador_verbetes ampliado** (patch declarado no código): o corpus do "todo verbatim confere" passou a incluir `notas/fichas/` — lastro que migrou continua fiscalizado. Sem o patch, 2 verbatim ancorados em notas teriam "sumido" para o verificador; com ele: `OK — todo verbatim confere byte a byte`.

## Ritos
1 unidade = 1 commit (`notas/fichas/` não-ignore — confirmado por `git check-ignore`); suite+verificador+builds antes do push; branch `arena/01a0960b-termos-rc`.
