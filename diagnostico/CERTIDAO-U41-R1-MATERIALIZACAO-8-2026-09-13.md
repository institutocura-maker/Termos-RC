# Certidão U41 — Rota R1 do gap: os 8 «suspenso-B» materializados, com o V aplicado (13/09/2026)

**Despacho do Curador (13/09/2026):** entre as quatro rotas oferecidas no dossiê
`diagnostico/CENSO-GAP-FICHAS-2026-09-13.md` (U38), abrir pela **R1 · Piloto dos 8 suspenso-B** —
os únicos, entre os 25 chancelados-e-suspensos das levas P7m/n/o, que o censo classificou na
família **B · prosa citável na fonte declarada**.

## 1. O que foi feito

| Código | Termo | Leva do V | Ficha nova | Citações (fragmentos verbatim) |
|---|---|---|---|---|
| RC-027 | Astréia | P7m | `termos/RC-027-astreia.md` | 2 |
| RC-030 | Atlantes | P7m | `termos/RC-030-atlantes.md` | 3 |
| RC-050 | Demônios | P7m | `termos/RC-050-demonios.md` | 3 |
| RC-051 | Despina | P7m | `termos/RC-051-despina.md` | 4 |
| RC-090 | Projeto Planeta Azul | P7o | `termos/RC-090-projeto-planeta-azul.md` | 4 |
| RC-097 | Seres Extrafísicos | P7m | `termos/RC-097-seres-extrafisicos.md` | 5 |
| RC-100 | Seres Espirituais | P7n | `termos/RC-100-seres-espirituais.md` | 5 |
| RC-304 | Deucalião | P7m | `termos/RC-304-deucaliao.md` | 5 |

**31 fragmentos verbatim** no total, cada um conferido **byte a byte** contra a linha declarada do
`original.txt` da obra — a conferência é o portão B do motor e aborta a escrita ao primeiro
desvio. Dois erros meus de transcrição foram pegos por esse assert antes de qualquer arquivo
nascer: B031 L3182 (o fecho é `…multiplicação).`, não `…multiplicação.`) e a linha da citação de
P2024-11-09 (a sentença está na L85, não na L1).

**Cadastro:** 8 linhas viradas na região `TERMOS` de `ferramentas/dados_termos.py` —
`ficha=False → True` e status `P` (provisório) `→ verificado` (o V chancelado aplica-se agora que a
trava §7 «sem ficha → bloqueia» deixou de incidir). **`RELACOES` intocado — 1887 arestas, nenhuma
aberta, fechada ou reetiquetada.**

## 2. Achado de método — o hard-wrap é a doença, e R1 não a cura

Todos os livros do corpus são hard-wrapped: **B031 = 92 chars na maior linha** · B021 = 106 ·
B026 = 109 · B003 = 111 · B024 = 100 · B006 = 169. Em 7 dos 8 casos, **nenhuma sentença inteira
coube numa linha**; onde coube (B031 L3156, L674, L5259 de B021), a citação saiu completa.

A saída foi a que a própria política 2.3 da casa autoriza: «cada item traz **trecho literal
(começo da citação)** e aponta o bloco-fonte onde ela vive inteira». Cada fragmento entre «» é
verbatim intra-linha; quando a sentença foi partida, o seu início e o seu fecho aparecem como
itens distintos com as linhas indicadas, e a Observações de cada ficha lavra a fratura e a
reconferência pendente.

**Consequência para o Curador:** R1 fecha o capítulo dos 8 suspensos citáveis, mas **não dispensa
o refinamento R2** (reconstrução de parágrafos) — sem ele, o grosso da família D (104) e boa parte
da B continuará fora do padrão de citação da casa. As fontes orais (P###), que são uma linha única
de STT, admitem citação de sentença inteira, mas ao preço da degradação da transcrição.

## 3. Provas

- Suíte `ferramentas/test_suite.py`: **21 testes, 21 verdes** (rodada sola, sem pipe).
  - T13 frontmatter: **681 fichas** · T14 tabelas == cadastro: **0 divergentes** ·
    T15 `motor.fm_toml` == frontmatter das fichas: **681 conferidas · 0 divergentes**.
- `python3 ferramentas/verificar_verbetes.py`: **Base intacta: 946 termos · 681 fichas · 1887 relações**.
- Espelhos reconstruídos na ordem do rito: `build_indice` → `exportar_json` → `build_xlsx` →
  `build_word` → `build_readme` (946 termos · 681 fichas-resumo · 1887 relações · 102 obras).
- `chancela/HOLD.csv`: 8 desfechos lavrados (nada deletado). O campo `motivo` de **RC-090** estava
  partido por um `;` interno herdado das levas anteriores — recomposto com `,` para devolver a
  linha ao formato de 4 colunas; nenhuma outra linha foi tocada e os fins de linha originais
  (o arquivo está misto: 28 CRLF + 13 LF) foram preservados byte a byte.

## 4. Contas

- Status: **60⚪ · 228🟡 · 102🟠 · 556🟢** (8 🟡 → 🟢; os demais inalterados).
- Gap de fichas: **273 → 265** códigos sem ficha; os suspensos do HOLD caem de **25 para 17**
  (restam 11 da família D, 2 da E, 1 da F, mais os 3 que já vinham de outras levas).
- `ferramentas/u41_materializar_r1.py` fica versionado como o registro executável da unidade
  (`--dry` confere as citações sem escrever nada).

## 5. Próximo (sugestão ao Curador)

Restam **63 códigos na família B** (71 − 8), prontos para o mesmo procedimento; a fila está
ranqueada por ocorrências no `CENSO-GAP-FICHAS-2026-09-13.json`. As rotas **R2 (D)**, **R3 (E)** e
**R4 (A)** seguem intactas e independentes.
