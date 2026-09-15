# U97 — Refutação da normalização das fontes (Fase 1, A5)

**Data:** 2026-09-15 · **Unidade:** U97 · **Natureza:** artefacto de leitura —
não altera nenhuma ficha, nenhuma fonte e nenhum verbete.

## 1. A instrução recebida

O despacho complementar à Fase 1 determinou a normalização das 9 obras-fonte
correspondentes às instâncias adiadas na U94 (`RC-708`, `RC-474`, `RC-266`,
`RC-821`, `RC-768`, `RC-575`, `RC-490`, `RC-837`, `RC-193`), com injecção de
quebras de parágrafo (`\n\n`) por heurística — pontuação final seguida de
maiúscula, espaçamentos maiores, quebras de secção nativas —, a fim de fazer o
vão cair abaixo de 300 palavras.

**Premissa declarada:** «essas obras-fonte carecem de quebras de parágrafo
estruturais (o texto lê-se como um bloco único massivo)».

## 2. A premissa é falsa

Medição directa das 9 obras (`ferramentas/censo_gap_v2.py`, blocos = trechos
entre linhas em branco):

| instância | sigla | linhas | linhas em branco | blocos | bloco da âncora |
|---|---|---|---|---|---|
| II-085 | P2025-02-15 | 170 | 16 | **14** | 29 399 palavras / 65 linhas |
| II-059 | P2023-12-02 | 114 | 11 | **11** | 17 880 / 61 |
| II-023 | P2025-05-31 | 145 | 23 | **19** | 28 387 / 43 |
| II-148 | P2019-04-14 | 64 | 3 | **2** | 23 261 / 60 |
| II-111 | P2026-07-25 | 310 | 9 | **4** | 17 474 / 33 |
| II-077 | P2022-12-17 | 10 | 2 | **3** | 21 429 / 6 |
| II-064 | P2025-05-31 | 145 | 23 | **19** | 28 387 / 43 |
| II-166 | P2019-08-25 | 168 | 5 | **3** | 8 251 / 50 |
| II-018 | P2024-07-14 | 107 | 14 | **13** | 15 396 / 14 |

Todas têm linhas em branco e mais de um bloco. **Nenhuma é um bloco único.**

Verificou-se ainda a hipótese de terminadores trocados: **CR solitário = 0 em
158 obras**. Os ficheiros usam CRLF de forma consistente.

## 3. A causa real: linhas gigantescas

| sigla | linhas | maior linha (caracteres) |
|---|---|---|
| P2022-12-17 | 10 | **112 921** |
| P2025-05-31 | 145 | **76 107** |
| P2024-07-14 | 107 | **44 059** |
| P2026-07-25 | 310 | **43 565** |
| P2025-02-15 | 170 | **34 076** |
| P2023-12-02 | 114 | **31 572** |
| P2019-04-14 | 64 | **30 869** |
| P2019-08-25 | 168 | **13 597** |

São transcrições não *hard-wrapped*: a unidade de composição é a linha, não o
parágrafo. Uma única linha transporta uma secção inteira, pelo que o bloco
(ainda que delimitado por linhas em branco legítimas) se torna um contentor de
dezenas de milhar de palavras.

Dentro desse contentor, o alinhador (`difflib`) casa palavras banais — «a»,
«O», «Javé», «existe.» — a milhares de palavras do trecho real. Verificou-se em
7 dos 9 casos o mesmo padrão: um fragmento longo com toda a substância,
**colado** às palavras em falta, mais 1 a 3 fragmentos de uma ou duas palavras
pescados longe.

Exemplo decisivo (II-085, `RC-708`, vão 26 771):

> Fonte L164: «…Mas compreenda, **o ser humano, ele** »»»**é não local. Ele não
> precisa estar no lugar para atuar naquele lugar.**««« Ele pode estar aqui…»

O alinhador fora buscar «o ser humano» à L104, sessenta linhas antes, quando as
mesmas palavras estão imediatamente antes do fragmento dominante.

## 4. O que a normalização produziria: um falso passe

Simulou-se a heurística indicada (quebra após pontuação final + maiúscula,
parágrafos de ~600 caracteres). **Nada foi escrito** — a simulação construiu
uma cópia em memória.

| instância | vão antes | vão depois | palavras do alvo | palavras retidas |
|---|---|---|---|---|
| II-085 | 26 771 | **97** | 16 | **6** |
| II-059 | 17 426 | **79** | 27 | **4** |
| II-023 | 16 187 | **47** | 18 | **4** |
| II-148 | 15 757 | **11** | 37 | **4** |
| II-111 | 2 525 | **115** | 23 | **6** |
| II-077 | 1 963 | **107** | 16 | **4** |
| II-064 | 1 608 | **25** | 17 | **3** |
| II-166 | 937 | **24** | 25 | 24 |
| II-018 | 884 | **40** | 21 | **4** |

As 9 passariam no limiar de 300 — com vãos de 11 a 115. Mas reteriam **4 a 6
palavras das 16 a 37 originais**.

**O vão não cai porque o texto melhore: cai porque os fragmentos distantes
deixam de ser encontrados.** Ao dividir a linha em 290 blocos, passam a viver
noutro bloco, e o localizador só procura dentro do bloco que contém a âncora.
Uma métrica que desce por lhe terem encolhido o contentor não mede proximidade
nenhuma — mede o tamanho do contentor.

## 5. O custo colateral

A base contém **974 citações** com aparelho `original.txt LNNNN`, distribuídas
por 71 obras. **25** apontam às 9 obras visadas:

| sigla | citações | linhas distintas |
|---|---|---|
| P2026-07-25 | 6 | 4 |
| P2024-07-14 | 4 | 3 |
| P2025-05-31 | 4 | 3 |
| P2019-04-14 | 3 | 2 |
| P2023-12-02 | 3 | 3 |
| P2022-12-17 | 2 | 1 |
| P2025-02-15 | 2 | 2 |
| P2019-08-25 | 1 | 1 |
| **total** | **25** | |

Inserir quebras em `original.txt` desloca a numeração de todas as linhas
seguintes. Cada uma destas 25 citações passaria a apontar para a linha errada —
uma falsificação silenciosa do rastreio, precisamente o que a doutrina da U86/U94
manda evitar.

## 6. O que foi feito em vez disso (U96)

Engenharia no **alinhador**, não nas fontes:

- **Janela de salvamento condicional** — só quando o vão global excede
  `MAX_VAO` se volta a alinhar dentro de `MAX_JANELA` palavras em torno do
  fragmento dominante. Por ser condicional, as 59 reconstruções aplicadas na
  U94 ficam textualmente idênticas (verificado texto a texto).
- **Comporta F** — descarta micro-fragmentos (≤3 palavras) isolados por mais de
  `LIMPAR_VAO` palavras da fonte, e qualquer fragmento de uma palavra não
  colado a um vizinho.

Resultado: as 9 aplicadas, vãos de **4 a 257**, 13 fragmentos conferidos byte a
byte, 0 recusas, 4 palavras omitidas no total, T5 verde, idempotente.

## 7. Desfecho

A normalização heurística das fontes fica **arquivada como refutada**, com esta
medição por justificação. Não se executa.

A reconstrução de parágrafos continua a ser o caminho de longo prazo — a própria
base já o prevê no texto-padrão das fichas: «A sentença íntegra só será citável
após o refinamento **R2** (reconstrução de parágrafos)». Quando R2 se fizer,
deverá produzir uma **vista segmentada derivada**, nunca uma reescrita de
`original.txt`, para não deslocar a numeração de que o aparelho R1 depende.
