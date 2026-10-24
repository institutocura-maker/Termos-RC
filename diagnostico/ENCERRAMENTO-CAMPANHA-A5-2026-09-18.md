# ENCERRAMENTO E SELO DA CAMPANHA A5 — reanexação de citações legadas

**Unidade:** U102 · **Campanha:** A5 (reanexação das citações legadas pré-Portão B)
**Data:** 18/09/2026 · **Sessão:** `arena/01a0b65d-termos-rc`
**Despacho do Curador:** «Vamos arquivar e encerrar a campanha A5 e virar a página.»
**Estado:** CAMPANHA A5 **SELADA** · dívida remanescente transferida ao acervo documental (não extinta, não abandonada)

---

## 1. Selo final (números oficiais, verificados agora nesta unidade)

| Grandeza | Valor | Fonte da verificação |
|---|---|---|
| Termos na Base | **946** | `python3 ferramentas/dados_termos.py` → `OK: 946 termos, 1887 relações` |
| Fichas em `termos/` | **820** | `ls termos/*.md` + `[T13]` |
| Relações | **1887** | `dados_termos.py` · `verificar_verbetes.py` |
| Verbetes da Enciclopédia | **649** | `verificar_verbetes.py` (0 falhas) |
| Verbatim conferidos | **8 805** · falhas **0** | `verificar_verbetes.py` |
| Códigos conferidos | **8 247** · falhas **0** | `verificar_verbetes.py` |
| Testes de suíte | **21/21 OK** | `test_suite.py` · `EXIT=0` |
| Frontmatter × cadastro | **820/820** · divergentes **0** | `[T14]` / `[T15]` |
| Obras com texto ingerido | **164** | U100/U101 (corpus 159 → 164) |

**Base intacta: 946 termos · 820 fichas · 1887 relações.** Nenhum código novo, nenhuma
aresta alterada, `relacoes/` blindado, nenhuma ficha movida para fechar esta campanha.

## 2. O que a A5 entregou (linha do tempo, U85 → U101)

- **U85** · censo da dívida: 52 blocos pré-Portão B em 39 fichas → reancoragem exigiria reextração; A6 corrigida (RC-816) e encerrada.
- **U86** · quarentena epistemológica estendida a **478/478 fichas** com nota graduada; censo definitivo **658 blocos não-verbatim** (graus A/B/C); A7 arquivada; A8 selada por dados.
- **U87–U90** · A4 encerrada (471 → 102 assinaturas de layout, vocabulário de 12 títulos, ordem-mestre única).
- **U91** · infraestrutura + piloto: **72 citações reanexadas**, 17 verbetes reemitidos; Portão B 778/778 + 100.
- **U92** · faixa 90–99%: o fosso residual era ruído de transcrição (STT), não truncamento.
- **U93** · artefacto de curadoria: **212 instâncias** para decisão binária APROVAR_FONTE × MANTER_LEGADO.
- **U94** · aplicação da decisão do Curador: **59 reconstruções em 56 fichas**; 9 adiadas (vão) devolvidas; dois marcadores sumidos — `» … «` (hard-wrap) e `» […] «` (omissão aprovada).
- **U95** · **Orfanato A5**: 221 blocos sem vestígio no corpus — 186 paráfrases · 27 fonte-parcialmente-não-ingerida · 8 fonte-não-ingerida (dataset para triagem futura).
- **U96** · resgate das 9 adiadas (janela condicional no alinhador; refutação do diagnóstico de U94 sobre a causa).
- **U97** · refutação da normalização das fontes — arquivada; R2 permanece o caminho (vista derivada, nunca reescrita de `original.txt`).
- **U98** · manifesto de ingestão (U98-INGESTAO-PENDENTE-A5) + reanexação do RC-500.
- **U99** · B035 ingerida por lista autorizada (amostra contínua) · RC-194 permanece pendente (Portão B intocável) · comporta G instalada.
- **U100** · ingresso das 5 aulas de «Os Mistérios da Vida de Jesus» no corpus (159 → 164).
- **U101** · **11 citações reanexadas** das 5 aulas (7 fichas: RC-862, RC-887, RC-942, RC-943, RC-944, RC-945, RC-946; 19 trechos, 0 ausentes), com a doutrina dos dois marcadores preservada na reemissão de 3 verbetes.

## 3. Estado das arestas (fechamento do backlog A)

`A1 ✅ · A2 ✅ · A3 ✅ · A4 ✅ · A5 ✅ (SELADA AQUI — dívida transferida) · A6 ✅ · A7 ✅ · A8 ✅`

## 4. Dívida remanescente da A5 (transferida, não extinta)

A campanha **não matou** a totalidade da dívida legada — ela a **contornou com o
aparelho R1** onde havia fonte, e a **cercou** onde não havia. O remanescente fica
lavrado e localizável para campanha futura:

1. **Blocos não reancoráveis por edição** — a dívida de reextração documentada em
   `diagnostico/A5-CITACOES-PRE-PORTAO-B-2026-09-14.json` e tipificada no
   `diagnostico/U95-ORFANATO-A5.md` (221 blocos sem vestígio; 186 paráfrases).
2. **Manifesto de ingestão** — `diagnostico/U98-INGESTAO-PENDENTE-A5.md`: 35 blocos
   recuperáveis apenas com a chegada de obras ausentes do corpus (P2023-12-25-01..05,
   B051, ART-2026-08-18, B071, B072, B064…), matéria que depende de material do Curador.
3. **RC-194** — pendente por decisão expressa (Portão B intocável; B035 no corpus sem
   aparelhamento não pode ser citada automaticamente).
4. **Triagem semântica do Orfanato** — o dataset da U95 permanece como ponto de partida
   da próxima decisão editorial (paráfrase × ditado livre × reextração).

## 5. Rito de encerramento cumprido

- Documento de encerramento lavrado em `diagnostico/` (este arquivo), no padrão dos
  encerramentos anteriores (R1 selada em U82; Onda 1 selada; Onda 2 selada).
- Validações de partida e de fecho executadas na própria unidade: `dados_termos.py`,
  `test_suite.py` (21/21), `verificar_verbetes.py` (649 · 8 805 · 8 247 · 0 falhas).
- **Nenhum arquivo de dados foi alterado** por esta unidade — encerramento é registro,
  não mutação. Diff limitado ao documento presente.
- 1 unidade = 1 commit + push na branch da sessão; `--amend` nunca usado.

## 6. Viragem de página

Com o selo, a esteira de auditoria (R1 + A1–A8) fecha-se como frente concluída. A
próxima etapa anunciada pelo Curador é de **produção pedagógica**: um **livro de acesso**
para o estudante iniciante, construído a partir do índice da Enciclopédia
(`pedagogico/enciclopedia/INDICE-ENCICLOPEDIA-RC.md`), com linguagem acessível e
referência única/funding de legibilidade («todo o material baseia-se nos Livros e
Palestras de Jan Val Ellam», sem aparato de citação por ficha). A enciclopédia
permanece a obra de referência do pesquisador; o livro será a obra de entrada do
estudante — duas obras, duas naturezas, um só corpus.

**CAMPANHA A5 — SELADA.**
