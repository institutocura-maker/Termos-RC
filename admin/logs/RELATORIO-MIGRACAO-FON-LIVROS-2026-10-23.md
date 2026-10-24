# Relatório — execução Fase 1D · FON-LIVROS

**Data:** 23/10/2026
**Estado:** migração física aprovada e concluída; pronta para consolidação/publicação.

## Movimento e prova literal

```text
livros/ → fontes/livros/
```

Antes de qualquer ajuste documental, `git mv` deslocou **577 arquivos**, reconhecidos em **100%**, com **100.540.340 bytes** e hash agregado Fase 1B preservado:

```text
06098a1590654708a6e0145502cf0147066e2048b16ed8b8a0dcd15d612c66d5
```

A raiz `livros/` foi removida e `fontes/livros/` tornou-se a rota física de `fonte.livros`.

## Alterações pontuais autorizadas

- `ferramentas/caminhos_acervo.py`: rota de runtime para `fontes/livros/`;
- `.arena/verifica_livro_portao_b.py`: resolução via mapa central, sem literal de livros;
- `fontes/README.md`: estado da migração atualizado;
- `fontes/livros/README.md`: somente `../fontes/externas/` → `../externas/`.

A mudança de sete bytes no README foi registrada em `fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1D.json`. O verificador aceita a cadeia Fase 0 → Fase 1B → Fase 1D e confirma o estado final:

```text
577 arquivos
100.540.333 bytes
816ea75b329eab074103de639bd12c0d98a44d72b46ee93e6db7373fe11128c6
```

## Validações

| Portão | Resultado |
|---|---|
| FON-LIVROS Fase 1B, pré/pós `git mv` | OK |
| FON-LIVROS com Fase 1B + Fase 1D | OK |
| FON-EXTERNAS | OK |
| Verificador auxiliar `.arena` | 64 caixas, 0 falhas |
| Consumidores mapeados | OK |
| `test_suite.py` | 21/21 |
| `motor.py selftest` | 10/10 |
| Builders | OK |
| `git diff --check` | OK |

As 159 referências internas seladas, 151 históricas e 50 de apostilas/consolidações/ficha canônica foram preservadas. Base, Termos, RAG, apostilas, ciclos, consolidações, recepção e stash não fazem parte do patch.

## Nota documental

Seis menções históricas adicionais a `livros/` e um link `../diagnostico/` em `fontes/livros/README.md` não foram alterados: a autorização delimitava somente o link de terceiros. Não são consumidores de runtime e ficam para eventual micro-onda documental explícita.
