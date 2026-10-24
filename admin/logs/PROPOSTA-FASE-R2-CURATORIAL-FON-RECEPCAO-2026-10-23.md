# Proposta — Fase R2 curatorial de FON-RECEPÇÃO

**Data:** 23/10/2026
**Estado:** proposta para deliberação curatorial; não executada.
**Pré-requisito cumprido:** Fase R1 desacoplou os consumidores ativos sem trocar a rota nem tocar os arquivos recebidos.

## Base imutável

A decisão R2 parte do manifesto Fase 0 e só poderá usar a seguinte linha de base:

| Campo | Valor |
|---|---|
| Coleção | FON-RECEPÇÃO |
| Itens | 330 |
| Bytes | 10.982.198 |
| SHA-256 agregado | `a780ac57fed45d40507363910ad9f1b33391fc154cad6ad86232f5d42efcd81b` |
| Rota atual | `uploads_recepcao/` |

## Lotes de deliberação

R2 não presume que todos os itens têm o mesmo destino. A decisão deve ser registrada por arquivo, a partir destes grupos operacionais:

| Grupo | Itens | Papel atual | Decisão que o Curador deve registrar |
|---|---:|---|---|
| `stt-lote-2026-10/` | 310 | lote bruto STT, incluindo seu README | manter, copiar a destino canônico aprovado, ou retirar somente após cópia validada |
| seis Markdown do piloto na raiz | 6 | fontes delimitadas de dry-runs históricos | manter como proveniência ou copiar a destino explicitamente aprovado |
| documentos DOCX na raiz | 2 | materiais recebidos sem destino canônico automático | decidir classificação e destino individual |
| `U93-U94-id-decisao.txt` | 1 | decisão de curadoria recebida | reter como evidência, com destino documental a aprovar |
| registros `REGISTRO-LIMPEZA-*.json` | 9 | registros operacionais de recepção | reter como evidência ou copiar ao arquivo documental aprovado |
| `README.md` e `.gitkeep` | 2 | contrato e suporte da caixa de entrada | manter com a caixa de entrada até nova decisão estrutural |

## Instrumento de decisão obrigatório

Antes de qualquer cópia, criar e preencher um registro curatorial por item com as colunas mínimas:

```text
caminho_origem;sha256_origem;bytes_origem;decisao;destino_canonico;justificativa_curatorial;aprovado_em;validador
```

Valores permitidos em `decisao`:

- `MANTER_EM_RECEPCAO`;
- `COPIAR_PARA_DESTINO_CANONICO`;
- `RETIRAR_APOS_COPIA_VALIDADA`.

Os dois últimos exigem `destino_canonico` explícito e decisão curatorial nominal. Nenhuma inferência por extensão, nome de arquivo, lote ou local histórico é suficiente.

## Execução futura, somente após aprovação

Uma eventual onda física R3 deverá, para cada item aprovado:

1. copiar byte a byte sem normalizar ou renomear silenciosamente;
2. registrar origem, destino, bytes e SHA-256 de ambos;
3. exigir igualdade de hashes antes de marcar a cópia como válida;
4. preservar a origem até que a remoção tenha autorização curatorial separada;
5. atualizar consumidores somente por `fonte.recepcao`, jamais por substituição global de texto;
6. executar o verificador Fase 0, a suíte, selftest e uma revisão de escopo.

## Exclusões desta proposta

- nenhum `git mv uploads_recepcao/ fontes/recepcao/`;
- nenhuma criação de conteúdo em `fontes/recepcao/`;
- nenhuma cópia, remoção, alteração de bytes ou normalização em `uploads_recepcao/`;
- nenhuma aplicação ou limpeza da salvaguarda `stash@{0}`;
- nenhuma alteração de fontes seladas, apostilas, ciclos, termos, RAG ou KB.

## Decisão solicitada ao Curador

Aprovar o instrumento de decisão e a ordem dos grupos acima, ou indicar destinos canônicos e prioridades diferentes. A R2 permanece deliberativa; a execução física exige autorização nova e específica.
