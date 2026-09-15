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

---

## 5. ADENDO (mesmo dia) — a amostra da B035 é CONTÍNUA, e isso muda o quadro

O Curador esclareceu que, embora seja uma amostra, a B035 **é uma parte
contínua do livro a partir do início** — não são páginas salteadas. Verificou-se
no ficheiro e confirma-se:

```
===== [PÁGINA 1] =====   na linha   1
===== [PÁGINA 2] =====   na linha   4
...
===== [PÁGINA 18] =====  na linha 468
```

18 marcas, sequenciais de 1 a 18, sem uma única falha.

**Isto derruba a objecção técnica que motivou o bloqueio.** Numa amostra de
páginas salteadas, a chegada da obra completa *interpolaria* linhas pelo meio
e deslocaria toda a numeração: cada `B035 · original.txt LNNNN` passaria a
mentir. Sendo contínua a partir da página 1, as páginas 19 e seguintes
**acrescentam-se ao fim**. As linhas 1–495 ficam onde estão, hoje e depois de
a obra chegar. A numeração é estável.

Duas ressalvas locais, declaradas: há `[TEXTO INCOMPLETO]` nas linhas **74**
(p. 6) e **257** (p. 12), por runs de `\x00` no extract. A citação do RC-194
está na **L284** (p. 13) — região limpa, entre os dois buracos.

### 5.1 O que se fez

Ingeriu-se a B035 no corpus por **lista autorizada**
(`AMOSTRAS_AUTORIZADAS`, em `ferramentas/censo_gap_v2.py`), nunca por
diretório. O corpus passa de 158 para **159 obras**.

Não se ingeriu `livros/AMOSTRAS` inteiro por duas razões:

1. a instrução vigente das fichas de ingresso é «não promover a CONCLUIDOS».
   A lista mantém a pasta onde está e **não toca na BIBLIO**;
2. a **B061**, que ali está, **não é obra primária** — a sua ficha diz: «é
   glossário pré-repo elaborado pelo Curador com ajuda de IA». Cità-la como
   fonte de Ellam falsificaria a autoria. Fica fora por princípio, e não tem
   marcas de página (0).

A **B027** partilha a condição da B035 (14 marcas, PÁGINA 1 a 14, contínua).
Não foi ingerida porque nenhum órfão depende dela; basta uma linha na lista
quando o Curador o pedir.

### 5.2 O que NÃO se fez, e porquê

Posto ao Curador, decidiu-se **manter `materializar_lote.py` intocável**.
Consequência aceite:

- o Portão B (`caminho_da_obra`) não resolve a B035, pois só vasculha
  `CONCLUIDOS` / `CONCLUIDAS` / `ciclos`;
- logo **a RC-194 fica pendente**. Não se assina um aparelho de linha que a
  porta da casa não consegue verificar — seria a falsificação que a U86 e a
  U94 mandam evitar;
- a B035 continua no corpus como **achador** (U65): o censo localiza o texto,
  mas ele não é aparelhável.

### 5.3 A armadilha que se desactivou

Ter a B035 no corpus sem suporte do Portão B criava um risco: qualquer
execução automática futura que tentasse aparelhá-la rebentaria com
`FileNotFoundError`. Acrescentou-se por isso a **comporta G** em
`aplicar_decisao_curador_a5.py`: a obra tem de ser *aparelhável* antes de
receber citação. O texto localizável mas não aparelhável é recusado com
mensagem própria, em vez de derrubar a esteira.

Teste: `B031` aparelhável · `B035` **não** aparelhável · `B061` fora do corpus.

---

## 6. Adendo U100 — as 5 aulas de «Os Mistérios da Vida de Jesus» NÃO estavam ausentes

**Pista do Curador (recebida a 15/09/2026):** as palestras `P2023-12-25-01`…`-05` fazem parte do
curso «Os Mistérios da Vida de Jesus», processado em
`ciclos/P2023-12-25_F044_misterios-da-vida-de-jesus`, com os originais em `…/translado`.

**Achado — os ficheiros estavam no repositório desde sempre.** O carregador de corpus e o
`caminho_da_obra` procuram `<pasta>/original.txt`; o dossiê F044 guarda o texto em
`translado/0N-*.txt`, um ficheiro por aula, sem `original.txt` no topo. A obra era portanto
**invisível para a máquina** — não ausente do repositório.

**Correcção executada (sem tocar em nenhum ficheiro intocável):** criadas cinco pastas-obra
canónicas, uma por aula, cada uma com `original.txt` (cópia **byte a byte** do traslado,
sha256 conferido) e `ficha_ingresso.md`:

| Sigla | Aula | sha256 (16) | linhas |
|---|---|---|---|
| `P2023-12-25-01` | Adolescência e a Juventude de Jesus | `304c9d66260421af` | 6 |
| `P2023-12-25-02` | Os Anos de Pregação e a Promessa do Retorno | `2ddcfceff95fea53` | 18 |
| `P2023-12-25-03` | Dias Difíceis: Crucificação e Ressurreição | `d1d4171df8a0d5ec` | 29 |
| `P2023-12-25-04` | O Nascimento do Cristianismo | `b6d77e12ff8def73` | 35 |
| `P2023-12-25-05` | A Verdadeira Face de Maria Madalena | `cd246089b15e2d3a` | 20 |

Corpus passou de **159 para 164 obras**; as cinco siglas resolvem no **Portão B** — ao contrário
da B035 (U99), estas ficam **aparelháveis**.

### 6.1 O código estava despachado — a ficha de ingresso do ciclo ficou para trás

A ficha do ciclo dizia que os códigos «aguardam despacho do Curador». Estavam **despachados a
06/09/2026**, e o despacho está lavrado em `consolidacoes/F044_misterios-da-vida-de-jesus/ciclo.toml`:

```
[fontes_p2023_12_25]
decisao_curator = "2026-09-06 - P2023-12-25 (curso online lancado no Natal de 2023);
                   sufixo -01..-05 por aula"
```

O Curador reafirmou-o nesta sessão: **2023-12-25 é a data de LIBERAÇÃO do curso**, não a data de
cada aula. O sufixo `-0N` é **número de ordem**, não dia do mês — ficou registado em cada
`ficha_ingresso.md` para que ninguém o leia como data.

Os códigos constam ainda de `dados_termos.py` (base canónica de declaração) em 33 verbetes, e de
78 citações nas fichas. Não são provisórios: são a declaração oficial de fontes.

### 6.2 Saldo

Dos 17 registos órfãos que citam estas palestras, **11 verificam a 95–100 %** contra o traslado
e passam a ser aparelháveis; 6 ficam por síntese (cobertura < 80 %).

Pendências restantes desta lista: `B051` (7), `B071` (2), `B072` (2), `B064` (1),
`ART-2026-08-18` (6) — sem qualquer ficheiro no repositório.
