# Relatório — Fase 1E FON-LIVROS

**Data:** 23/10/2026
**Base publicada:** `2b20694c40904e097c433a4f05fb60dab90b15d0` (`2b20694 refactor: migra fontes de livros`)
**Natureza:** micro-onda documental pós-migração; sem movimento físico.

## Escopo executado

A Fase 1E normalizou seis referências de rota históricas no
`fontes/livros/README.md` para a localização canônica `fontes/livros/` e
corrigiu o link relativo à verificação de cobertura. Não houve alteração de
fontes primárias, nomes de arquivos, conteúdo de obras, rota de runtime ou
consumidores.

| Item | Antes | Depois |
|---|---:|---:|
| Arquivo alterado | `fontes/livros/README.md` | `fontes/livros/README.md` |
| Bytes | 16.943 | 17.012 |
| SHA-256 | `1c5da15827a451a47a6368f2d546c204a32366f1556360b97bc76699a9fe3559` | `be1c0ac599cf23454683309e183c6a77f20a7a7bc65148c2bfa9ddb23b794bf9` |
| Movimentações físicas de arquivos | 0 | 0 |

A averbação encadeada está em
`fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1E.json`. Ela declara
exclusivamente esse delta e não reescreve o manifesto imutável da Fase 0.

## Prova de integridade

A cadeia ordenada **Fase 0 → 1B → 1D → 1E** foi conferida pelo verificador
repetível. Resultado: **577 arquivos**, **100.540.402 bytes** e SHA-256
agregado final
`df1607e1328788008dc731b6f007d718e73cc5566c61825a24282edc1f3af3ff`, com três
averbações aplicadas. A validação JSON da averbação também passou.

A verificação direta contra a Fase 0, sem averbações, deliberadamente acusa
somente `README.md`; isso confirma que o delta documental está explicitamente
registrado, e não oculto no manifesto-base.

## Portões

| Portão | Resultado |
|---|---|
| `git diff --check` e índice | OK |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| Verificador FON-LIVROS com cadeia 1B, 1D e 1E | OK |
| Verificador FON-RECEPCAO contra Fase 0 | OK — 330 arquivos, 10.982.198 bytes |

Não existe gerador versionado que consuma `fontes/livros/README.md`: a busca
por sua rota encontrou somente registros de auditoria. Portanto nenhum builder
foi aplicável a esta micro-onda; arquivos gerados não foram tocados.

## Limites preservados

- `fontes/livros/` permanece no destino físico publicado na Fase 1D.
- A salvaguarda local `stash@{0}` não foi aplicada, removida ou alterada.
- A preparação de FON-RECEPÇÃO permanece documental; `uploads_recepcao/` não
  foi movida nem modificada.
