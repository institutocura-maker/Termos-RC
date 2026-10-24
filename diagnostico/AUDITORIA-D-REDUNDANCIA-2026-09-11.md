# Auditoria Interna — Frente D: Redundância — 11/09/2026

Leitura pura. Pergunta: o que é peso morto, o que é memória viva, e o que quebra se mover?

## D1. `backups/pacotes/` (10 MB): o fóssil mais caro do repo

4 TXTs congelados em 18/08/2026 (era migração-de-chats): apostilas 2,8 MB · fichas 1,7 MB · **originais 5,2 MB** · regeneração 631 KB. O de 5,2 MB é o **maior blob de todo o histórico git**. Função original: transportar estado entre chats sem git — **função extinta** desde a adoção do GitHub (o git faz isso melhor). Proposta: etiquetar uma release/tag `arquivo-migracao-2026-08-18`, remover da árvore (Onda 0). Os 13 `REGISTRO-LIMPEZA-*.json` (4 KB cada) são certidões — manter, ocupam nada.

## D2. Raiz: 45 docs, 38 interligados — mover exige reescrita de links

Inventário de citações cruzadas (nome-de-arquivo mencionado no corpo): 38 dos 45 docs citam outros (hubs: `INDICE-ARQUIVOS-RAIZ`→27, `PROMPT-PROXIMA-SESSAO`→16, `CONTINUIDADE`→14). A recomendação do auditor (mover para `docs/historico/`) está correta **desde que** acompanhada de reescrita mecânica dos links (mapa origem→destino aplicado por script + conferência). Sem isso, move-se o caos com ~150 referências quebradas.

Classificação proposta:

| Classe | Docs | Destino |
|---|---|---|
| VIVO (7) | `../admin/logs/STATE-MIRROR.md`, `01-ficha-modelo.md`, `02-vocabulario-controlado.md`, `convencoes-editoriais-rc.md`, `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`, `APRESENTACAO-DO-SISTEMA.md`, README vivo (a gerar) | Ficam na raiz |
| HISTÓRICO já marcado (5) | `README.md` (atual), `../prompts/PROMPT-INICIAL-DO-AGENTE.md`, `PACOTE-…`, `PLANO-MIGRACAO-…`, `../admin/logs/STATUS-RESTAURACAO.md` | Movem com placa |
| DIÁRIO congelado (1) | `../admin/logs/CONTINUIDADE.md` (1.681 linhas de `🔔 CICLO … FECHADO`, parado ~02/09, sucedido por STATE-MIRROR+git) | Congelar com placa "encerrado em …; sucedido por …" (não apagar: é a certidão da era dos ciclos) |
| DUPLICATA byte-idêntica (1 par) | `GUIA-MESTRE-RC-APOSTILA-v1.1.md` = `.txt` (29.426 bytes, `diff` limpo) | Apagar um (manter `.md`) |
| SÉRIES temporais (13) | `PROMPT-CONTINUIDADE`×4, `PROMPT-COMPLETO`×2, `STATUS-HANDOFF`×4, `VERIFICACAO-DE-COBERTURA`×2, +3 correlatos | `docs/historico/prompts/` e `docs/historico/handoffs/`, com índice |
| GERADOS na raiz (3) | `indice-mestre.md`, `base-terminologica.xlsx`, `base-terminologica-leitura.docx` | Decisão pendente (R4): raiz ou `espelhos/`? |
| DEMAIS despachos/diagnósticos (~15) | `DESPACHO-*`, `DIAGNOSTICO-*`, `AVALIACAO-*`, `PLANO-*`, etc. | `docs/historico/` com índice por data |

## D3. `_*.py`: 6 arquivos, ~91 KB, uso único e histórico

`_ampliar_fichas_*`×2, `_desduplicar_F045*`×2, `_materializar_ancoras_F045`, `_auditoria_lacunas` — todos de ciclos passados, nenhum importado por nada. Consenso com o auditor: `ferramentas/legacy/` + README de uma linha cada (Onda 0).

## D4. Falsos-positivos de redundância (verificado, manter como está)

- `apostilas/CONCLUIDAS` × `ciclos/`: overlap de **4 datas em 80+36** — são fluxos complementares (produto × processo), não duplicatas.
- `INVENTARIO-APOSTILAS.json` × `INVENTARIO-COMPACTO-*.md` × `INDICE-PALESTRAS.md`: mandatos distintos (máquina × humano × diário de ciclos); o terceiro está com conteúdo congelado em 28/08 mas é certidão, não lixo.
- `consolidacoes/` (1,9 MB), `pedagogico/top-down/` (2,4 MB), `rag/` (196 KB): outros fluxos/linhas — fora do escopo desta frente.

## D5. Prática existente a generalizar: a placa "ARQUIVO HISTÓRICO"

5 docs já carregam o carimbo `⚠️ ARQUIVO HISTÓRICO (marcado na revisão de …)` com apontamento do sucessor ("prevalece X"). É um padrão são e barato. Proposta: estender a placa a tudo que for congelado (D2), com 3 campos obrigatórios: **marcado-em, sucedido-por, motivo**. Congelar com placa ≠ apagar: preserva a memória sem poluir a navegação.

## Síntese da Frente D

Peso morto real: **10 MB de pacotes extintos + 1 duplicata + 6 legados** (todos Onda 0, zero risco). Memória mal-organizada (não morta): **~35 docs de raiz** que precisam de classificação + reescrita de links, nunca de apagamento sumário. Recomendação central: **arquivar pacotes/legados/duplicata já; mover a raiz com mapa de links e placas, nunca no escuro**.
