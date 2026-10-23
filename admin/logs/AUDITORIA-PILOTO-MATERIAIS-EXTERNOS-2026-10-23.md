# Auditoria do piloto físico — `materiais_externos/`

> **Resultado:** **NÃO APTO para migração física nesta etapa**, sob a regra vigente de não modificar acervo consolidado.
>
> Esta auditoria não moveu nem reescreveu nenhum arquivo.

## Escopo auditado

| Campo | Resultado |
|---|---:|
| Coleção | `FON-EXTERNAS` |
| Caminho atual | `materiais_externos/` |
| Destino planejado | `fontes/externas/` |
| Arquivos | 15 |
| Bytes de arquivos | 146.373 |
| SHA-256 agregado da coleção | `144847a396d9600288831044e41a3e612ea0cb398523ceb9793737358c2f6488` |
| Consumidores Python diretos | 0 |

A coleção contém dois ingressos de material externo, com bruto, ficha de ingresso e análise: glossário Krys Amon (`EXT-2024-01-04`) e material Ari Barbosa (`EXT-2026-08-05`).

## Resultado da varredura de referências

Não há consumidor Python direto do caminho `materiais_externos/`, mas há referências documentais e históricas ativas. A referência bloqueante está em:

```text
consolidacoes/F043_glossario-krys-amon/DECISAO-DO-CURADOR.md
```

O registro consolidado declara explicitamente a canificação da fonte no caminho físico atual:

```text
materiais_externos/2024-01-04_glossario-krys-amon/
```

Atualizar esse caminho exigiria editar uma decisão curatorial em `consolidacoes/`, diretório que a política de organização atual preserva como acervo selado. Deixá-lo inalterado após mover a coleção tornaria a referência histórica factualmente desatualizada.

## Deliberação técnica

Embora o piloto seja pequeno e não tenha dependências Python, ele falha no portão de proveniência histórica. Portanto, **não será feito `git mv materiais_externos/ fontes/externas/`** sem novo despacho.

Git preservaria o histórico dos arquivos, e o manifesto provaria igualdade byte a byte, mas isso não elimina a referência de localização gravada no ato curatorial consolidado. Integridade de conteúdo não substitui integridade de trilha documental.

## Opções para o próximo despacho

1. **Recomendado — Fase 1A sem migração física:** integrar gradualmente o mapa `ferramentas/caminhos_acervo.py` aos consumidores ativos e criar um verificador de rotas legadas, mantendo todos os caminhos físicos atuais.
2. **Exceção curatorial explícita:** liberar somente a atualização de caminhos nos registros consolidados diretamente afetados, com relatório de antes/depois. Só então o piloto poderia ser reavaliado.
3. **Compatibilidade física transitória:** mover a coleção e manter um redirecionador no caminho antigo. Não recomendado como primeira escolha: pode confundir leitores, não resolve todos os usos de caminho e prolonga a duplicidade estrutural.

## Desfecho posterior à auditoria

Em 23/10/2026, o Curador selecionou explicitamente a opção de **liberar atualização limitada do registro consolidado F043**. A barreira documental foi então averbada no próprio registro, preservando o hash pré-migração e delimitando a mudança exclusivamente à localização física. A migração piloto passou a ser executável e é documentada no relatório de migração correspondente.

## Garantias preservadas

- Manifesto Fase 0 permanece imutável como linha de base; a igualdade de `FON-EXTERNAS` passou a ser verificada contra o destino migrado.
- Base, termos, RAG, apostilas e ciclos não receberam mutação.
- A exceção curatorial é limitada ao caminho de `FON-EXTERNAS` no registro consolidado F043; não libera reescrita genérica de acervo consolidado.
