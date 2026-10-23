# Mapa da documentação — Termos-RC

> Ponto de orientação para documentos humanos do repositório. Para números e estado operacional vigentes, prevalecem `../README.md` e `../admin/logs/STATE-MIRROR.md`.

## Começar por aqui

1. [`../README.md`](../README.md) — visão geral, números oficiais e comandos de validação.
2. [`../admin/logs/STATE-MIRROR.md`](../admin/logs/STATE-MIRROR.md) — estado operacional entre sessões.
3. [`../prompts/`](../prompts/) — instruções e bootstrap da próxima sessão.
4. [`../admin/logs/`](../admin/logs/) — despachos, handoffs, checkpoints e registros operacionais.

## Mapa de responsabilidades

| Local | Papel | Exemplos |
|---|---|---|
| **Raiz** | interfaces estáveis, padrões canônicos e espelhos gerados | `README.md`, `indice-mestre.md`, planilhas da Base, ficha-modelo, vocabulário, convenções, glossário, apresentação, guia e índices operacionais |
| [`historico/`](historico/) | documentação datada mantida como referência, não como estado corrente | índice de handoff de 2026-08-31, inventário compacto e preparação temática P2020-04-25 |
| [`planos/`](planos/) | planos estratégicos e de evolução | plano do corpus de treinamento da IA Local |
| [`../diagnostico/`](../diagnostico/) | diagnósticos, auditorias, avaliações, relatórios, verificações e certidões | diagnóstico do processo, auditorias e baseline da KB |
| [`../prompts/`](../prompts/) | instruções de sistema e continuidade de sessão | prompts completos, iniciais e de continuidade |
| [`../admin/logs/`](../admin/logs/) | trilha operacional e curatorial | `STATE-MIRROR`, despachos, handoffs e relatórios de organização |

## Regra de admissão

- Um documento novo **não** deve nascer na raiz apenas por conveniência.
- Plano estratégico vai para `docs/planos/`; documentação datada sem função operacional corrente vai para `docs/historico/`; diagnóstico, auditoria, avaliação, relatório e verificação vão para `diagnostico/`.
- A raiz é reservada a entradas estáveis, documentação canônica e artefatos gerados de leitura humana.
- `README.md` e `indice-mestre.md` são gerados: seus geradores, em `../ferramentas/`, são a única via de edição.

## Zonas preservadas

Não mover nem reescrever conteúdo em `base/`, `termos/`, `apostilas/CONCLUIDAS/`, `consolidacoes/`, `ciclos/` e diretórios de ondas/derivados sem despacho específico. Documentos ainda citados nessas zonas podem permanecer na raiz como **compatibilidade bloqueada**; a organização não deve reescrever a evidência histórica para obter uma árvore visualmente menor.
