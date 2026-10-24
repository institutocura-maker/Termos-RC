# KB — arquitetura em Fase 0

> Esta pasta descreve a futura camada física da Base de Conhecimento. **Nenhum dado canônico foi movido nesta fase**; os caminhos atuais continuam sendo a única rota de runtime autorizada.

## Topologia planejada

```text
kb/
├── base/       # cadastro canônico; hoje: base/
├── termos/     # fichas terminológicas; hoje: termos/
└── rag/        # artefatos derivados de recuperação; hoje: rag/
```

O registro executável `ferramentas/dados_termos.py` permanece em `ferramentas/`: ele é parte do Motor, não um arquivo a ser deslocado junto da camada de dados sem uma migração específica do runtime.

## Regras de segurança

- `base/`, `termos/` e `rag/` continuam autoritativos enquanto a Fase 0 vigorar.
- Não usar `kb/` como caminho de entrada para builders, Motor ou scripts até existir despacho de migração e adaptação integral dos consumidores ativos.
- Os hashes de pré-migração estão em [`manifestos/MANIFESTO-KB-FASE-0.json`](manifestos/MANIFESTO-KB-FASE-0.json).
