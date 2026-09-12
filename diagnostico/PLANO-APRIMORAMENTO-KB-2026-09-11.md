# Plano de Aprimoramento da KB — 11/09/2026

Consolidação da auditoria interna (frentes A→E), do censo de fichas e do parecer externo (com avaliação). Nada aqui executa sozinho: **cada onda exige chancela do Curador antes de começar e certidão de aceite ao terminar**.

## Regras do jogo (valem para todas as ondas)

1. **Paridade antes de trocar**: nenhum build novo aposenta o antigo sem diff byte-a-byte dos espelhos.
2. **Uma mudança estrutural por vez**, 1 commit por unidade (mesmo rito das levas).
3. **Só-stdlib** em tudo que for estrutural (sandbox apaga `pip` entre turnos).
4. **Nada apaga memória**: arquivar = tag/release + placa (marcado-em, sucedido-por, motivo).
5. **P7 segue pausado** até o aceite da Onda 0 (os portões novos passam a valer nas levas seguintes).

## Onda 0 — Fundação (só adiciona; risco zero)

| # | Item | Origem | Aceite |
|---|---|---|---|
| 0.1 | `test_suite.py`: 11 checks (5 do auditor + badge↔cadastro, ficha↔arquivo, **sem-fantasma**, Fontes bemformada, status-enum, `via` preenchido) | R6, C4, A, E3 | Roda < 30s, 0 falhas na base atual *exceto* as conhecidas (B061…), que viram lista de exceções lavrada |
| 0.2 | `loader.py` único (import; word/xlsx/índice passam a usá-lo; ast-scraping aposentado com paridade) | B2 | Espelhos idênticos byte-a-byte |
| 0.3 | `chancela/HOLD.csv` (833, 769, 859, 500, 795, 785, 193, 576, 800, 801, 812 + motivo + desde) + pergunta automática em V-sobre-HOLD | E4 | Simulação: retorno-teste com V no 833 dispara a pergunta |
| 0.4 | README vivo gerado do STATE-MIRROR (+ o atual vai para `docs/historico/` com placa) | R2 | README reflete 946/671/1898 sem edição manual |
| 0.5 | `ferramentas/legacy/` (6 `_*.py`) + placas de status em todos os scripts (`ATIVO-FLUXO-X`/`DORMENTE`/`LEGADO`) | B6, D3 | Nenhum script sem placa |
| 0.6 | Arquivar `backups/pacotes/` (tag `arquivo-migracao-2026-08-18`) + apagar duplicata GUIA `.txt` | D1, D2 | −10 MB na árvore, tag verificável |
| 0.7 | Ritos E3 codificados: assert de contagem em geração de template, parser rejeita linha em branco, commit nunca em cadeia `&&` (checklist no test-suite) | E3 | Falha simulada em cada rito é capturada |

## Onda 1 — Verdade-mestra (risco baixo→médio)

| # | Item | Origem | Aceite |
|---|---|---|---|
| 1.1 | Exportador `dados_termos.py` → `base/canonico.json` (tipos normalizados: listas, não strings `;`) + validador hand-rolled | F2, C7 | Round-trip `.py`→`.json`→`.py` idêntico |
| 1.2 | **Decisão Curador: JSON-primeiro × SQLite-primeiro** (parecer comparativo será apresentado; empate técnico, desempate por manutenção) | R1, F5 | Despacho lavrado |
| 1.3 | BIBLIO sai do `build_xlsx.py` para os dados canônicos (comentário "50 obras" morre aqui) | B3 | xlsx idêntico, BIBLIO com 102 entradas reconciliadas |
| 1.4 | Declarar hierarquia `t[6]` (navegação) × `RELACOES` (curatorial) + reconciliar 168 órfãos + auditar 9 duplicados + domar 279 tipos | C1 | 0 pares só-RELACOES; tipos hapax justificados ou fundidos |
| 1.5 | Campos `via` (P6-evidência/P7-conhecimento) e `confianca_fonte` (alta/média/baixa) — schema novo ou convenção interim em Observações | E5, R9 | 166 termos P7 marcados `via=P7-conhecimento` |
| 1.6 | **Despacho B061**: origem da sigla? + limpar 7 siglas-fantasma do cadastro e 28 das fichas (declarar vs. materializar) | C4 | 0 siglas-fantasma no cadastro |
| 1.7 | Builders passam a ler do canônico (F3), um por vez, com paridade | F3 | 3 espelhos idênticos |

## Onda 2 — Fichas (risco médio; o grueso curatorial)

| # | Item | Origem | Aceite |
|---|---|---|---|
| 2.1 | Frontmatter TOML piloto (10 fichas: metadados no TOML, prosa no corpo) + decisão de expandir | B8-alternativa, R8 | Validador lê TOML; fichas-piloto intactas em leitura |
| 2.2 | Consolidação dos 4 dossiês gigantes (001/009/072/104): fusão dos blocos repetidos (A1), ordenação cronológica, `Definição Sintética` re-sintetizada | A1, A2 | 4 fichas com blocos únicos/ordenados + síntese que sintetiza |
| 2.3 | Política `Citações-chave`: índice curado nas 🟢 (opção b), seção some do modelo das demais (opção a); fila das 163 🟢 sem seção | A3, A5 | Critério "lastro visível" incorporado ao 🟢 futuro (sem retroatividade) |
| 2.4 | 336 notas de processo → `notas/` (por ficha) ou rodapé padronizado; referências a nº de linha convertidas em âncoras | A-frente, §5-doc | 0 `## Nota — MUTIRÃO` no corpo das fichas |
| 2.5 | Tabela `Termos Relacionados` gerada do cadastro (após auditar as 421 só-na-tabela) | A4 | 0 divergências tabela×cadastro |
| 2.6 | Despachos pontuais: 4 pares de títulos duplicados (C6), 2 pastas P ausentes (P2023-12-25, P2026-02-28) | C6, C4 | 4+2 decisões lavradas |

## Onda 3 — Escala e distribuição (aditivo; risco baixo)

| # | Item | Origem | Aceite |
|---|---|---|---|
| 3.1 | Releases por fase + GitHub Action (test-suite pós-push como alarme) → *então* `gitignore` nos binários | R4, D-futuro | Espelhos baixáveis na Release; `.git` para de crescer por leva |
| 3.2 | Busca full-text FTS5 (stdlib, já testado) sobre 671 fichas + 659 verbetes | D-futuro | `busca.py "termo"` retorna ranqueado < 2s |
| 3.3 | Grafo D3.js das relações (HTML estático gerado) | D-futuro | 1 HTML navegável_clusters/termos-ponte visíveis |
| 3.4 | Builds incrementais **se** rebuild > 3 min (gatilho, não antes) | R5 | Medição registrada; implemento só se disparar |
| 3.5 | Prep YouTube: despacho sigla V/Y + pipeline (transcrição→pré-filtro→lotes→CSV) + política de armazenamento externo (repo só guarda transcrição+metadados+link) | C-YouTube | 1 lote-piloto de 3 vídeos processado de ponta a ponta |
| 3.6 | Mudança da raiz para `docs/historico/` com mapa de links + placas (D2) | R7, D2 | 0 links quebrados (verificado por script) |

## Dependências (ordem de execução)

```
0.1 test-suite ─┬─→ 0.2 loader ─→ 1.1 exportador ─→ 1.2 decisão ─→ 1.7 builds-no-canônico
                ├─→ 0.3 HOLD ─→ (P7 retoma)
                ├─→ 0.7 ritos ─→ (E3 codificado)
                └─→ 1.4/1.6/2.5 (portões usam o suite)
0.4/0.5/0.6 ─→ 3.6 (raiz por último, com tudo placado)
1.5 ─→ 3.5 (via/confiança alimentam o pipeline de vídeos)
```

## Despachos pendentes do Curador (decisões só suas, reunidas)

1. **B061**: origem da sigla? (C4 — bloqueia 1.6)
2. **JSON × SQLite** (1.2 — parecer comparativo a apresentar)
3. **Sigla V/Y** para vídeos (3.5)
4. **Canal dos espelhos**: Release/Actions antes do gitignore? (3.1)
5. **4 pares de títulos** + 2 pastas P (2.6 — barato, pode sair antes)
6. **Critério 🟢 futuro** com "lastro visível" (2.3)
7. **Chancela da Onda 0** para começar (este plano)

---

*Plano lavrado em 11/09/2026. Pilares: paridade, stdlib, memória preservada, P7 retomado sob portões novos. Revisão externa: devolver ao Assistente Auditor como revisor.*
