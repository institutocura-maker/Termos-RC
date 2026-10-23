# Relatório — Fase 0 da arquitetura Fontes / KB

> **Estado:** executada e validada para decisão curatorial; **sem commit**.
>
> **Regra cumprida:** esta fase não moveu, copiou, renomeou ou reescreveu qualquer fonte, ficha, cadastro, evidência de ciclo ou diretório consolidado.

## Entregas

### Mapa de caminhos

`ferramentas/caminhos_acervo.py` estabelece as chaves estáveis da arquitetura e declara, separadamente:

- o caminho físico atual, único caminho de runtime durante a Fase 0;
- o destino futuro planejado, que não é caminho de runtime e não autoriza migração.

As dez chaves atuais existem no disco: livros, recepção, fontes externas, três camadas de evidência, base, termos, RAG e registro executável.

### Manifestos imutáveis de pré-migração

`ferramentas/gerar_manifestos_acervo.py` gera e valida inventários determinísticos com SHA-256 por arquivo e hash agregado por coleção.

| Manifesto | Coleções | Arquivos | Bytes | Cobertura |
|---|---:|---:|---:|---|
| `fontes/manifestos/MANIFESTO-FONTES-FASE-0.json` | 6 | 2.947 | 173.642.156 | livros, recepção, fontes externas e três camadas de evidência |
| `kb/manifestos/MANIFESTO-KB-FASE-0.json` | 4 | 1.157 | 7.359.603 | cadastro, fichas, RAG e registro executável |

A validação recalculou todas as hashes e confirmou igualdade byte a byte com os dois manifestos.

### Contratos documentais

- `fontes/README.md` declara a taxonomia futura e diferencia tipo editorial de canal de origem: YouTube é canal, não sinônimo de palestra.
- `kb/README.md` delimita a futura camada KB e preserva explicitamente `base/`, `termos/` e `rag/` como rotas canônicas atuais.
- `docs/planos/PLANO-FONTES-KB-FASE-0-2026-10-23.md` define os portões, as ondas futuras e os itens fora de escopo.
- `docs/README.md` recebeu links para as duas camadas de Fase 0 e para o plano.

## Arquitetura declarada, sem migração física

```text
fontes/
├── recepcao/          ← destino futuro de uploads_recepcao/
├── livros/            ← destino futuro de livros/
├── palestras/         ← classificação editorial futura
├── online/youtube/    ← classificação por canal futura
└── externas/          ← destino futuro de materiais_externos/

kb/
├── base/              ← destino futuro de base/
├── termos/            ← destino futuro de termos/
└── rag/               ← destino futuro de rag/
```

As subpastas acima são apenas topologia planejada; não foram criadas com cópias vazias ou dados duplicados. Isso evita que ferramentas interpretem um caminho planejado como caminho ativo.

`apostilas/`, `ciclos/` e `consolidacoes/` ficaram deliberadamente fora de `fontes/`: preservam transformação, despacho, âncoras e proveniência, e não devem ser reduzidos a “fontes”.

## Segurança e piloto futuro

A Fase 0 oferece **prova verificável de não alteração** e base de comparação para qualquer onda seguinte. Ainda não redireciona os consumidores ativos; esse é um portão posterior, justamente para não alterar o Motor antes de uma migração aprovada.

O piloto físico potencial continua sendo `materiais_externos/`, por não possuir consumidor Python direto na auditoria inicial. Mesmo esse piloto exige levantamento próprio de suas referências textuais e das referências eventualmente preservadas em acervo consolidado antes de qualquer `git mv`.

## Validações executadas

| Verificação | Resultado |
|---|---|
| `py_compile` de `caminhos_acervo.py` e `gerar_manifestos_acervo.py` | OK |
| Existência das 10 rotas físicas declaradas | OK |
| Geração dos manifestos | OK |
| `gerar_manifestos_acervo.py --validar` | OK — igualdade byte a byte |
| Links locais em `docs/README.md` | OK |
| `python3 ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` / escopo protegido | OK |

A suíte emite apenas `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; encerrou com `OK`.

## Situação para decisão

A Fase 0 está pronta para commit e push após validação curatorial. Qualquer Fase 1 deve ser objeto de novo despacho, escolher uma única coleção-piloto e cumprir os manifestos/hashes antes e depois do movimento.
