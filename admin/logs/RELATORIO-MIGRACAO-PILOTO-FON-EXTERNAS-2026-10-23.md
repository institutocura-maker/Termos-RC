# Relatório — migração piloto FON-EXTERNAS

> **Estado:** executada e validada para decisão curatorial; **sem commit**.
>
> **Despacho aplicado:** após auditoria de bloqueio, o Curador autorizou atualização limitada e auditável do registro consolidado F043 para liberar este piloto físico.

## Movimento realizado

```text
materiais_externos/  →  fontes/externas/
```

A coleção `FON-EXTERNAS` foi movida com `git mv`. Os 15 arquivos dos ingressos `EXT-2024-01-04` e `EXT-2026-08-05` foram preservados literalmente: Git detecta os 15 como renomeações de 100%.

| Propriedade | Resultado |
|---|---|
| Arquivos | 15 |
| Bytes | 146.373 |
| SHA-256 agregado pré/pós-migração | `144847a396d9600288831044e41a3e612ea0cb398523ceb9793737358c2f6488` |
| Verificador | `ferramentas/verificar_migracao_fontes.py --piloto externas` |
| Resultado do verificador | OK — igualdade de caminho relativo, bytes, SHA-256 individual e hash agregado |

O manifesto Fase 0 permanece imutável como prova do estado anterior. A nova verificação lê esse manifesto e compara o destino `fontes/externas/`, sem reemitir nem alterar a linha de base.

## Referências e averbamento

- `ferramentas/caminhos_acervo.py` passa a declarar `fontes/externas/` como rota atual de `fonte.externas`; não há destino pendente para essa chave.
- Documentação operacional e de navegação foi atualizada para a nova rota.
- `consolidacoes/F043_glossario-krys-amon/DECISAO-DO-CURADOR.md` recebeu o único averbamento em acervo consolidado: referências de localização passam a apontar para `../../fontes/externas/`, com registro expresso do caminho anterior, hash de prova e escopo estritamente topológico.
- O conteúdo das fontes migradas **não** foi reescrito, mesmo quando contém referências históricas ao nome anterior.
- Ocorrências do nome legado persistem apenas em manifesto pré-migração, backups, relatórios históricos, fontes seladas, uso semântico do termo ou no averbamento autorizado; nenhuma rota operacional ativa usa o diretório removido.

`livros/README.md` foi atualizado apenas como consumidor documental para indicar a rota atual de fontes externas. Nenhum livro, bruto ou corpus foi alterado.

## Escopo preservado

Não foram modificados `base/`, `termos/`, `rag/`, `apostilas/`, `ciclos/`, `uploads_recepcao/`, ondas STT ou arquivos de livros. A única alteração em `consolidacoes/` é o averbamento F043 explicitamente autorizado.

## Validações

| Verificação | Resultado |
|---|---|
| `py_compile` dos caminhos e verificador do piloto | OK |
| Prova FON-EXTERNAS contra manifesto Fase 0 | OK |
| Remoção da rota física legada / resolução da rota atual | OK |
| Classificação das referências legadas | OK — nenhuma rota ativa legada |
| `python3 ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `python3 ferramentas/build_indice.py` | OK — 946 linhas |
| `python3 ferramentas/test_suite.py` | OK — 21 testes |
| `python3 ferramentas/motor.py selftest` | OK — 10/10 |
| `git diff --check` | OK |

A suíte emite apenas `ResourceWarning` herdados por arquivos abertos sem fechamento explícito; encerrou com `OK`.

## Conclusão

O piloto demonstra que a arquitetura `fontes/` pode receber coleção física com segurança **quando** há manifesto prévio, verificador pós-migração, consumidor ativo reendereçado e despacho para qualquer referência consolidada. Isso não autoriza automaticamente a migração de coleções maiores ou da KB; cada uma exige auditoria e portões próprios.
