# U46 — R1 · lote 3 · as 10 Eras da Criação

Safra 2026-09-13 · despacho vigente: `diagnostico/DESPACHO-ROTAS-POS-V2-2026-09-13.md`
(poço = família B do censo v2 · V presuntivo **revogado** do lote 3 em diante).

## As 10 fichas

| Código | Era | Ficha | Fragmentos |
|---|---|---|---:|
| RC-156 | Era da Solidão | `termos/RC-156-era-da-solidao.md` | 5 |
| RC-157 | Era da Geração | `termos/RC-157-era-da-geracao.md` | 5 |
| RC-158 | Era da Punição | `termos/RC-158-era-da-punicao.md` | 5 |
| RC-159 | Era do Impasse | `termos/RC-159-era-do-impasse.md` | 5 |
| RC-168 | Era da Lila e da Aceitação | `termos/RC-168-era-da-lila-e-da-aceitacao.md` | 5 |
| RC-169 | Era da Semeadura Universal | `termos/RC-169-era-da-semeadura-universal.md` | 5 |
| RC-170 | Era do Refinamento da Semeadura Biológica Universal | `termos/RC-170-era-do-refinamento-da-semeadura-biologica-universal.md` | 6 |
| RC-171 | Era da Geopolítica Universal e da Divisão do Comando | `termos/RC-171-era-da-geopolitica-universal-e-da-divisao-do-comando.md` | 5 |
| RC-172 | Era da Criatura Universal | `termos/RC-172-era-da-criatura-universal.md` | 4 |
| RC-173 | Era das Supercivilizações | `termos/RC-173-era-das-supercivilizacoes.md` | 5 |

**50 fragmentos** verbatim intra-linha, conferidos byte a byte contra o `original.txt` da B024 — **0 falhas**.

Todas as dez vêm do §16 de **B024** (*Epopeia — Agentes da Vida Universal*), L4737–L5016,
sob o guarda-chuva **RC-155 «Eras da Criação (10 eras)»**, que já possui ficha.

## Chancela — V revogado

Nenhuma das dez nasce 🟢. O despacho revogou a presunção de V por fonte de livro
para os lotes 3 em diante; o lote declara `"v_revogado": true` e **não** declara `aplicar_V`.
Resultado: `ficha False→True` e **status preservado** (`provisório`), com a nota de
revogação apontando ao despacho no corpo de cada ficha. As guardas E1–E5, que só existem
para sustentar a presunção de V, não se aplicam e o driver as desliga.

## Efeito na Base

- **+10 fichas** (697 → 707).
- **Status inalterado**: as dez já eram `provisório` — 572🟢 · 212🟡 · 102🟠 · 60⚪.
- Gap de fichas: 249 → **239**. Poço da família B (censo v2): 142 → **132 restantes**.
- Nenhuma aresta criada em `relacoes/` (1887) · nenhum HOLD tocado.

## Correções de governança aplicadas nesta unidade

1. **A guarda E3 passa a ler o censo v2.** Consultava o v1 e barraria códigos classificados
   como «E.não-achado-no-corpus» — foi o que por pouco aconteceu com a RC-171, cujo título o
   hard-wrap partiu entre L4962 e L4963. Com o v2, a guarda lê família B e não barra nada.
2. **Nota de revogação** no corpo de cada ficha, para que nenhum 🟡 futuro pareça
   esquecimento: cada uma declara que a presunção foi revogada pelo Curador, com o caminho
   do despacho.

## O erro corrigido, registrado nas próprias fichas

Três das dez eras haviam sido mal classificadas pelo censo v1; a correção consta das
Observações de cada ficha, para que o leitor saiba por que a entrada existe:

| Código | v1 | v2 | Causa do erro |
|---|---|---|---|
| RC-170 | C.prosa-fora-das-fontes-declaradas | B | título §16.7 partido em L4906–L4907 |
| RC-171 | **E.não-achado-no-corpus** (occ=0) | B | título §16.8 partido em L4962–L4963 |
| RC-172 | D.só-estrutural | B | prosa de L4996–L5002 lida como estrutural |

## Verificação

Suíte 21/21 (T13 707 · T14 0 divergentes · T15 707/0) · verificador 946/707/1887 ·
5 builds na ordem (indice → exportar_json → xlsx → word → readme).

