# Certidão — Onda 2.1 · piloto frontmatter TOML (12/09/2026, Agente 25)

**Escopo:** 10 fichas-piloto (4 gigantes de 2.2 + 6 formas variadas) ganharam `+++` frontmatter TOML no topo; o envelope `| Campo | Valor |` saiu do corpo (G3.1–G3.3). `## Fontes` e demais seções = carta, intactas.

**Schema canônico do frontmatter (valores SEMPRE do registro — G3.1):** `codigo, nome, categoria, subcategoria, status, fontes[], via, confianca_fonte, atualizado` (o `atualizado` resgatado do envelope removido, com assert de concordância de status antes da mutação).

**Piloto:** RC-001 · RC-009 · RC-072 · RC-104 (corpos 51–107KB) · RC-167 · RC-454 · RC-499 · RC-592 · RC-611 · RC-714.

**Gates cumpridos (PACTO-ONDA2):**
- G1.1/G1.2: splice provou `original == título+envelope+corpo` e `novo == TOML+título+corpo` com corpo **verbatim contíguo** (byte a byte, sem normalização — G1.5);
- G3.2: nenhuma linha removida reaparece na ficha nem é citada em verbete (côtejo automático por ficheiro);
- Autópsia TOML pré-disco: `tomllib.loads` + igualdade 1:1 com a tupla do registro.

**Consumers (mesmo commit, G3.5):** `test_suite` T6 passou a aceitar o badge OU na tabela OU no TOML (xor estrito — duplicidade vira falha) e ganhou **T13** (frontmatter parseia + bate com registro + `atualizado` ISO); `build_word` faz strip do bloco `+++` (docx reconstruído e verificado: **sem vazamento**, títulos OK); **T8 corrigido no mesmo golpe**: a varredura sem-fantasma é da CARTA — com o envelope agora espelhando o registro, as siglas `P2023-12-25-0N` (série F044; o código de lançamento não é diretório) teriam virado "fantasmas" por construção do espelho, não por anomalia da prosa. O portão reagiu como projetado (foi ele quem pegou) — o fix é de escopo, não de relaxamento.

**Verde final:** validador 946/1887 · suite **19 OK** · verificador verbetes **649/8.540/8.250/0** · docx rebuild sem `+++` · xlsx/índice não leem corpo de ficha (inalterados, com razão).

**Em aberto (decisão do Curador, fim do plano 2.1):** EXPANDIR o frontmatter para as 661 fichas restantes (lote único mecânico, mesmos gates; ~1 commit) ou manter piloto + só aplicar nos 4 gigantes via 2.2. O formato-xor da suite convivendo com os dois estados permite esperar sem dívida.
