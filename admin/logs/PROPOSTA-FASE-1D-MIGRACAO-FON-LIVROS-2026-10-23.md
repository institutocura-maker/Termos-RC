# Proposta — Fase 1D · migração física de FON-LIVROS

**Data:** 23/10/2026
**Estado:** proposta aprovada e executada no worktree; registrada para trilha de decisão.

## Escopo autorizado

```text
livros/ → fontes/livros/
```

A execução é limitada a 577 arquivos via `git mv`, preservação literal de fontes seladas e dos registros históricos, e quatro ajustes: rota `fonte.livros`, verificador auxiliar `.arena`, contrato `fontes/README.md` e o link de terceiros em `fontes/livros/README.md`.

A prova obrigatória é realizada antes da documentação: Fase 0 + averbação Fase 1B. A correção posterior do README é registrada em uma segunda averbação encadeada, sem regenerar o manifesto-base. Base, Termos, RAG, apostilas, ciclos, consolidações, recepção e `stash@{0}` ficam fora do patch.

## Portões

1. provar a linha Fase 1B antes e imediatamente após `git mv`;
2. corrigir somente a documentação autorizada;
3. validar a cadeia Fase 0 → Fase 1B → Fase 1D;
4. executar verificador auxiliar, builders, suíte, selftest e revisão de escopo;
5. apresentar o relatório/tree antes de publicação.
