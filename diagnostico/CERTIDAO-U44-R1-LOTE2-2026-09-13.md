# U44 — R1 · família B · lote 2 (8 novas fichas)

Safra: 2026-09-13 · despacho vigente: «seguir na família B» + presunção de V por fonte de livro (U43).

## Guardas E1–E5

Checadas antes de qualquer escrita. **0 impedimentos.**

## Conferência byte a byte

32 fragmentos verbatim intra-linha, conferidos contra o `original.txt` de cada obra declarada.

| Código | Nome | Ficha | Fragmentos | Fontes |
|---|---|---|---|---|
| RC-032 | Benem | `termos/RC-032-benem.md` | 6 | B018,B031 |
| RC-048 | Demiurgo | `termos/RC-048-demiurgo.md` | 3 | B031 |
| RC-073 | Keshava | `termos/RC-073-keshava.md` | 3 | B031 |
| RC-123 | Val Eno | `termos/RC-123-val-eno.md` | 5 | B031,B039 |
| RC-095 | Rogério de Almeida Freitas | `termos/RC-095-rogerio-de-almeida-freitas.md` | 5 | B031 |
| RC-438 | Tubal | `termos/RC-438-tubal.md` | 3 | B052 |
| RC-374 | Mordon | `termos/RC-374-mordon.md` | 3 | B043 |
| RC-211 | Kundalini | `termos/RC-211-kundalini.md` | 4 | B001,P2024-05-04 |

Total: **32 fragmentos** · 0 falhas de conferência.

## Efeito na Base

- **+8 fichas** (689 → 697) · **+8 🟢** (564 → 572) · **−8 🟡** (220 → 212).
- Gap de fichas: 257 → **249**. Família B: 55 → **47 restantes**.
- Nenhuma aresta criada em `relacoes/`; nenhum HOLD tocado.

## V presuntivo

Os 8 nascem 🟢 por **presunção de fonte de livro** (`aplicar_V: "presuncao-livro"`),
com nota de reversibilidade no corpo de cada ficha apontando ao despacho.
Cada um fica identificado na Base por `via = P6-evidência` + `confianca_fonte = alta`.

## Pendências deixadas registradas (não resolvidas nesta unidade)

1. **RC-095** — quarentena biográfica ativa (B031 L429+): dados pessoais existem na fonte e **não** foram transportados.
2. **RC-374** — a equiparação «druida da montanha» = «Venerável Mordon» (B043 L1458–L1461) está fraturada pelo hard-wrap; só citável após **R2**.
3. **RC-211** — B074/B075 usam Kundalini no sentido vital/prânico (com «Prana»/«Ki»), sentido diverso; registrado em Observações, fora das citações-chave.
4. Palestras sem ocorrência: **RC-073** (P2026-04-02) e **RC-438** (P2024-11-30).

## Adendo — uniformização do enunciado de arestas (24 fichas da R1)

Achado ao lavrar a RC-032: a linha «Arestas em `RELACOES`» contava **só as arestas do grafo**
(3, no caso) enquanto a tabela «Termos Relacionados» logo abaixo exibia 7 linhas — porque a tabela,
por exigência de T14, soma ao grafo o **espelho `t[6]` do cadastro**, nos dois polos. O enunciado
não estava errado, mas era **opaco**: lido de fora, parecia contradizer a tabela vizinha.

Nova redação, agora explícita:

> Arestas em `RELACOES`: 3 — a tabela abaixo soma a essas as do espelho do cadastro (7 no total).

Aplicada a **todas as 24 fichas já materializadas pela rota R1** — as 8 desta unidade (regeneradas
pelo driver) e as 16 do piloto U41 + lote 1 da U42 (remendadas linha a linha, com a contagem lida de
cada tabela, sem tocar em mais nada do corpo). O driver `ferramentas/materializar_lote.py` passa a
gerar a forma nova — as próximas 249 nascem já uniformes.

Nenhuma aresta foi criada, fechada ou reetiquetada; nenhum HOLD foi tocado.
