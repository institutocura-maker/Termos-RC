# U98 — Manifesto de Ingestão Pendente (Fase 2, A5)

**Data:** 2026-09-15 · **Unidade:** U98 · **Estado:** a aguardar material do Curador.

## 1. O que se pediu e o que se encontrou

O despacho da Fase 2 indicou «35 órfãos identificados como recuperáveis por
simples ingestão». A verificação dos metadados e a busca no repositório
mostram que **a ingestão não depende de trabalho do agente, e sim de
material que aqui não está**:

| Situação | Registos |
|---|---|
| Totalmente recuperáveis com o que existe no repo | **2** |
| Parciais (misturam fonte existente com fonte inexistente) | 1 |
| **Sem fonte alguma no repositório** | **32** |

## 2. Obras cuja fonte NÃO EXISTE no repositório

Verificado por busca de ficheiros (`find`) em toda a árvore, excluindo `.git`:
nenhuma destas siglas corresponde a qualquer diretório ou ficheiro.

| Sigla | Blocos órfãos | Fichas afectadas |
|---|---|---|
| `P2023-12-25-03` | 9 | RC-142, RC-647, RC-942, RC-943, RC-945… |
| `P2023-12-25-01` | 7 | RC-001, RC-009, RC-329, RC-862, RC-942… |
| `B051` | 7 | RC-011, RC-012, RC-015, RC-310, RC-408… |
| `ART-2026-08-18` | 6 | RC-009, RC-086, RC-287, RC-514, RC-553… |
| `P2023-12-25-04` | 5 | RC-273, RC-887, RC-946 |
| `P2023-12-25-02` | 3 | RC-942, RC-944 |
| `B071` | 2 | RC-514, RC-516 |
| `B072` | 2 | RC-517, RC-530 |
| `P2023-12-25-05` | 2 | RC-943 |
| `B064` | 1 | RC-641 |
| **total** | **44** | 33 registos |

### Como desbloquear

Depositar o `original.txt` de cada obra em `uploads_recepcao/`, ou criar a
pasta `livros/CONCLUIDOS/<sigla>_<slug>/original.txt`. O carregador do corpus
lê apenas `livros/CONCLUIDOS`, `apostilas/CONCLUIDAS` e `ciclos`
(`ferramentas/censo_gap_v2.py`, `BASES`).

## 3. As duas excepções

### 3.1 `ART-2025-08-01` — não é obra em falta, é ALIAS

A apostila `2025-08-01_fornos_replicadores` está no corpus, mas o carregador
deriva a sigla do nome do diretório e produz `P2025-08-01`. O rótulo
`ART-2025-08-01` usado nas fichas não é reconhecido.

### 3.2 `B035` — existe, mas está BLOQUEADA por instrução vigente

Está em `livros/AMOSTRAS/B035_o_big_data_do_criador/original.txt` (30 011
bytes, 495 linhas). A ficha de ingresso da obra é explícita:

> «Pasta em `livros/AMOSTRAS/B035_o_big_data_do_criador/` — **não** promover
> a CONCLUIDOS. Obra completa continua pendente.»

A amostra tem 18 páginas (Intro + caps. 1–2). Ingerir `AMOSTRAS` no corpus
violaria essa instrução e faria citar texto incompleto como se fosse obra
acabada. **O agente não o fez.** Fica como decisão do Curador.

Se o Curador autorizar, 1 registo(s) passa(m) a ser
recuperável(eis) de imediato: `RC-194` L62.
O trecho do RC-194 L62 já foi verificado e confere **100%** byte a byte
contra `AMOSTRAS/B035.../original.txt` L284.

## 4. O que a U98 executou

Dos 35, só um era integralmente verificável com o corpus actual e sem
violar nenhuma instrução:

- **`RC-500` L45** — reanexado a `P2021-12-04` L4. O trecho declarava duas
  fontes fora do corpus, mas a própria ficha já citava `P2021-12-04`, que
  está no corpus e onde o texto confere a 100%.
- Achado de integridade: os dois fragmentos são **contíguos** na fonte
  (GAP = 0). O `[STT]` da ficha era inserção editorial, não omissão da
  fonte. Emitiu-se portanto um fragmento ÚNICO, sem `» […] «` — usar o
  marcador de omissão aqui seria afirmar uma falta que não existe.
