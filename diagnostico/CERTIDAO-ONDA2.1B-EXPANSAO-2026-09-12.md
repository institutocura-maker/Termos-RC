# Certidão Onda 2.1-B — EXPANSÃO do frontmatter TOML para as 661 (12/09/2026)

**Despacho do Curador**: "em frente com a expansão" — a decisão que estava em pausa desde o piloto foi assinada. As **671 fichas vivem agora 100% em TOML** (9 campos, valores SEMPRE do registro-mestre — G3.1).

## Execução (U18)
- **658 splices byte-provados**: envelope (`| Campo | Valor |`) removido da carta com prova de reinserção — reinserir o bloco restaura o arquivo byte a byte (gate G1.1 do piloto, reproduzido); `atualizado` resgatado do envelope antes da remoção (658/658 datas ISO, zero fallback).
- **3 lápides F045-MERGE** (RC-449, RC-872, RC-936): sem envelope na posição padrão — o envelope delas vive DENTRO do registro histórico que a própria remissiva de setembro declara "preservado". Receberam o TOML por prepend isolável (gate do piloto) e os envelopes-história **ficaram onde estão, como exceção sancionada** (removê-los violaria a declaração da lápide; T6 não enxerga ali envelope vivo). `atualizado` = data do git log (sem envelope vivo).
- Autópsia tomllib em todas as 661 + paridade campo a campo com o registro antes de escrever (gate do piloto, inclusive).

## Verdes
- **T13: 671 fichas com frontmatter** (o gate que esperava este momento) · T6 sem violação (nenhuma carta com envelope vivo) · T14 0 divergentes · suíte completa sem AVISO.
- Verificador: `OK — todo verbatim confere byte a byte · Base intacta: 946 termos · 671 fichas · 1887 relações`.
- JSON canônico válido (946/1887) · builds: docx sem `+++` e **sem envelope algum no espelho de leitura** (a carta agora é só ouro: conceito, citações, contexto — o triplo ponto arquitetônico do Curador em vigência integral), xlsx/README regenerados.

## Pendência lavrada (não executada — fora do escopo assinado)
`ferramentas/motor.py` (linhas ~719/~834) ainda **gera** fichas novas com envelope `| Campo | Valor |`. Enquanto P7 estiver pausado, nada é gerado; na reabertura do P7, o motor deve emitir o bloco `+++` (mesma função `fm_de` desta unidade vale como molde). Decisão e data de execução: do Curador. **— CUMPRIDA 13/09/2026 (U25):** despacho «retomar P7»; o motor agora gera o bloco `+++` (`fm_toml`, molde canônico + regra do loader importada); guarda T15 na suíte (671 fichas conferidas byte a byte, 0 divergentes); selftest 9/9. Registro: `diagnostico/P7-RETOMA-U25-2026-09-13.json`.

## Reversão
Um commit (esta unidade inteira) — `git revert` devolve envelopes a todas as 658 com o mesmo byte-prova ao contrário.
