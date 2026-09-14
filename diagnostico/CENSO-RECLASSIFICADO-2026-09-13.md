# Censo reclassificado do gap de fichas — 2026-09-13

Instrumento: `ferramentas/censo_gap_v2.py` · dados: `diagnostico/CENSO-RECLASSIFICADO-2026-09-13.json`.
Reproduzir: `python3 ferramentas/censo_gap_v2.py` (~17 s, 158 obras).

**Unidade de diagnóstico: nada da Base foi alterado** — sem ficha nova, sem aresta, sem frontmatter, sem HOLD, sem `canonico.json`.

## 1. O que estava errado

O censo v1 procurava a `chave` do termo **dentro de uma única linha** do `original.txt`. Como todo o corpus é hard-wrapped (a maior linha da B024 tem 92 caracteres), qualquer nome partido pela quebra de linha virava **falso negativo**. A v2 reconstrói o parágrafo antes de procurar.

O caso que denunciou a falha: das **10 Eras da Criação** (B024 §16), três saíram erradas na v1 — e uma delas, **RC-171**, como «não-achado-no-corpus», o que a guarda **E3** usaria para lhe bloquear o V presuntivo. Nenhuma das três estava ausente: estavam todas no §16, com prosa farta — blocos de 35 a 48 linhas cada.

| Código | Era | v1 | v2 | Onde a v2 achou |
|---|---|---|---|---|
| RC-156 | Era da Solidão | B | **B** | B024 L4721-4748 |
| RC-157 | Era da Geração | B | **B** | B024 L4750-4766 |
| RC-158 | Era da Punição | B | **B** | B024 L4750-4766 |
| RC-159 | Era do Impasse | B | **B** | B024 L4785-4809 |
| RC-168 | Era da Lila e da Aceitação | B | **B** | B024 L4832-4844 |
| RC-169 | Era da Semeadura Universal | B | **B** | B024 L4846-4862 |
| RC-170 | Era do Refinamento da Semeadura Biológica Universal | C | **B** | B024 L4874-4908 |
| RC-171 | Era da Geopolítica Universal e da Divisão do Comando | E | **B** | B024 L4916-4963 |
| RC-172 | Era da Criatura Universal | D | **B** | B024 L4965-5005 |
| RC-173 | Era das Supercivilizações | B | **B** | B024 L4965-5005 |

## 2. O quadro

| Família | v1 | v2 | Δ | O que significa |
|---|---:|---:|---:|---|
| A · alias-variação | 6 | **6** | +0 | — |
| B · prosa citável na fonte declarada | 71 | **166** | +95 | — |
| C · prosa fora das fontes declaradas | 41 | **17** | -24 | — |
| D · só-estrutural (listas/sumários/hard-wrap) | 104 | **21** | -83 | — |
| E · não achado no corpus | 40 | **52** | +12 | — |
| F · nome ambíguo | 11 | **11** | +0 | — |

**134 de 273 entradas (49%) mudam de família.**

| de (v1) | para (v2) | quantos |
|---|---|---:|
| D | B | 73 |
| C | B | 23 |
| C | E | 11 |
| D | C | 8 |
| D | E | 7 |
| E | B | 4 |
| B | D | 3 |
| B | C | 2 |
| C | D | 1 |
| E | C | 1 |
| E | D | 1 |

### Leitura

- **A família D era majoritariamente artefato.** Dos 104 códigos que a v1 chamou de «só-estrutural», 73 têm prosa citável na própria fonte declarada. A v1 não os achou porque procurava numa linha só.
- **A família E cresceu (40 → 52).** Entraram 11 vindos de C e 7 de D: códigos que a v1 achava ter Lastro e que, recomposto o texto, não têm prosa em lugar nenhum — só sumário, nota ou título.
- **A e F ficaram como estavam** (6 e 11): são juízos sobre o NOME do termo, não sobre a busca no corpus. A v2 preserva o veredito da v1 e apenas anota o que a busca achou.

## 3. Recorte operacional (quem ainda está sem ficha)

Dos 273 censados, 249 seguem sem ficha hoje (24 já foram materializados nas unidades U41, U42 e U44):

| Família | sem ficha | rota que cabe |
|---|---:|---|
| B · prosa citável na fonte declarada | **142** | R1 — materializar |
| C · prosa fora das fontes declaradas | 17 | R1 com retificação de fontes |
| D · só-estrutural (listas/sumários/hard-wrap) | 21 | R1 só com citação estrutural, ou R3 |
| E · não achado no corpus | 52 | **fora da R1** — R4 (declarar ausência / lápide / fusão), depende de despacho |
| A · alias-variação | 6 | despacho taxonômico |
| F · nome ambíguo | 11 | despacho taxonômico |

**O poço de onde a R1 pode tirar é 142, não 47.** A lista que vinha sendo usada (família B da v1, já descontados os 24 materializados) não enxergava 95 dos {cv.get('B',0)} códigos que a v2 enxerga — 67% do poço real, perdidos para o artefato de medição.

## 4. Prova por amostra (promoções D→B)

| Código | Nome | Fonte · linhas | Trecho inicial do bloco recomposto |
|---|---|---|---|
| RC-023 | Antlartes | B031 L3103-3136 | Antlar: Base construída no hemisfério sul, onde hoje é a Antártida, a partir da nave Asphezian. Alojava inicia… |
| RC-026 | Astralização dos Biodemos | B031 L3103-3136 | Antlar: Base construída no hemisfério sul, onde hoje é a Antártida, a partir da nave Asphezian. Alojava inicia… |
| RC-029 | Atlans | B031 L3138-3173 | quartel-general, agora comandado praticamente por Len Mion. Grupo 2: composto por 28 membros, incluindo Yel Lu… |
| RC-043 | Conselho dos Cinco | B031 L3246-3280 | Criadora, porém não é o Pai-Mãe Amantíssimo (Deidade), apesar de a maioria de nós o confundirmos e assim chamá… |
| RC-067 | Gron Mion | B031 L1692-1721 | Os biodemos são seres biológicos deste universo e, por serem provenientes de outros planetas, podem ser consid… |
| RC-083 | Norte Divino | B031 L2861-2891 | 19 mil e 700 anos A.P.: A Experiência Gron é finalmente finalizada entre os biodemos do Norte, de Benem-Espher… |
| RC-088 | Portlan e Portlon | B031 L3650-3685 | homens pela ousadia do titã Prometeu em roubar o segredo do fogo dos Deuses e dar para os humanos da Terra. Ca… |
| RC-110 | Val Am | B031 L2593-2626 | Após muitas pesquisas e testes, os Val começaram a operar fora das naves, o que ocasionou a morte de 9 membros… |
| RC-111 | Val Amon | B031 L3246-3280 | Criadora, porém não é o Pai-Mãe Amantíssimo (Deidade), apesar de a maioria de nós o confundirmos e assim chamá… |
| RC-113 | Val Anon | B031 L1754-1785 | • Robespierre • Dom Pedro II • Trotsky • Samora Machel • Maria Orsic • Osho O mais famoso dos Yel, Yel Luzbel,… |
| RC-114 | Val Antien | B031 L2593-2626 | Após muitas pesquisas e testes, os Val começaram a operar fora das naves, o que ocasionou a morte de 9 membros… |
| RC-115 | Val Aten | B031 L2593-2626 | Após muitas pesquisas e testes, os Val começaram a operar fora das naves, o que ocasionou a morte de 9 membros… |

## 5. O que a v2 faz, exatamente

1. Linhas consecutivas sem linha em branco entre elas viram um **bloco** (parágrafo recomposto).
2. O marcador `===== [PÁGINA n] =====` é suprimido e **não** corta o bloco — sensibilidade primeiro, era isso que faltava à v1.
3. A marca d'água do conversor de ebook (`******ebook converter DEMO Watermarks*******`, 180× na B031) é suprimida: se entrasse no parágrafo, poluiria a citação e partiria ao meio qualquer chave que a atravessasse.
4. Hífen de translineação (linha finda em «-» e a seguinte começando minúscula) é recomposto sem espaço.
5. A busca usa a `chave` normalizada da v1 (sem acentos, caixa baixa, espaços colapsados) — muda só a **unidade de busca**: parágrafo, não linha.
6. Prosa = bloco com ≥ 200 caracteres **e** ≥ 2 terminadores de sentença **e** sem cara de lista. Terminador real = `[.!?]` seguido de espaço ou fim e **não** precedido de dígito (o «1.» de sumário fica de fora). Cara de lista = mediana de linha < 20 chars **e** ≥ 3 itens numerados.

Dois critérios foram testados e abandonados, e ficam registrados: «tem pontuação» (deixava passar o SUMÁRIO da B049, L43-83) e «mediana do comprimento das linhas» (rebaixava prosa autêntica, porque o hard-wrap quebra palavras no meio — «Projeto» / «Talm» — e encurta as linhas).

## 6. Limites desta medição (o que ela NÃO resolve)

- **A chave é o nome do cadastro.** Se a obra grafa o termo de outro modo, v1 e v2 erram igual — é o caso típico da família F (nome ambíguo, 11 códigos), que segue dependendo de despacho.
- **A supressão do marcador de página** pode juntar, num mesmo bloco, o fim de uma página e o começo da seguinte. Ganha-se em sensibilidade, perde-se um pouco em precisão; o trecho vai na evidência para conferência.
- **A família E (52) é um veredito de ausência, não de inexistência**: o termo pode existir no corpus sob outra grafia, ou a obra declarada pode estar errada. Antes de qualquer lápide, conferir à mão.

## 7. Os códigos fora da R1 (E, D e C) — para despacho

### E · não achados no corpus (R4) — 52

| Código | Nome | Fontes declaradas |
|---|---|---|
| RC-006 | Guerra do Éden | B015 |
| RC-178 | Dois Grandes Favos | B044 |
| RC-197 | Big Data da Terra | B035, P2024-09-29 |
| RC-198 | Rédeas Genéticas | B035, P2024-09-29 |
| RC-199 | Assinatura da Alma | B035, P2025-03-15 |
| RC-201 | O Livro do Criador | B035 |
| RC-202 | Linhagens Preferenciais do Criador | B035, P2024-09-29 |
| RC-240 | Império dos Descendentes dos Seres dos Portais | B018, P2024-09-29 |
| RC-249 | Expulsão dos Viajores (decreto do Criador) | B015 |
| RC-251 | Laboratórios do Criador | B015, P2024-09-29 |
| RC-256 | Escola dos Agentes Esclarecidos da Busca da Verdade | B016, P2021-12-04 |
| RC-269 | Linhagens Humanas: Preferidas e Preteridas | B013, P2024-09-29 |
| RC-271 | Pactos do Criador (troca de informações) | B013, P2024-09-29, P2024-04-13 |
| RC-272 | Laço Temporal de Kether/Javé | B013, P2023-10-14 |
| RC-277 | A Jaula de Cada Espécie | B014 |
| RC-279 | Modo Trimurtiano de Sophia | B014 |
| RC-290 | Cuidado com o 'Ide e Pregai' | B020 |
| RC-291 | Fim do Silêncio de Pandora | B020, P2020-04-25 |
| RC-316 | Decifra-me ou Devoro (hábito demo) | B022, P2025-06-14b |
| RC-324 | Grupos de Entroncamento (1-4) | B023 |
| RC-336 | Ética da Sobrevivência de Javé | B048, P2024-11-30 |
| RC-350 | Jesus, o Capelino | B025 |
| RC-360 | Atmosferizar a Lua ou Marte (Opção Final) | B005 |
| RC-386 | Memórias para Javé | B041, P2024-09-29 |
| RC-390 | Espíritos comunicantes do Grupo Atlan | B006 |
| RC-401 | Família Demolle (biodemos) | B050, P2021-05-15 |
| RC-405 | Alvorecer de Aquário | B027, P2022-12-17 |
| RC-406 | Diálogos de Sócrates, Platão e Aristóteles (nos Céus da Grécia) | B027, P2023-08-27, P2022-11-19 |
| RC-407 | Reencarnação iminente da grande leva de espíritos | B027 |
| RC-412 | Emissários Humanos (Enoch, Abraão, Moisés, Jesus) | B051, B060 |
| RC-418 | Terminal Nervoso do Criador (humano) | B034, B036, P2025-03-15, P2025-02-15 |
| RC-429 | Javé alimenta-se do senso crítico humano | B036, P2025-02-15, P2024-11-30, P2024-09-29 |
| RC-431 | Guerreiro ao Atleta (transição) | B040 |
| RC-473 | Lempérion e Terpérion (setores da Espiritualidade Laboratorial) | — |
| RC-478 | Chequinhá (veículo/nave de Javé) | — |
| RC-507 | Holodomínio (esfera de influência extrafísica) | B071 |
| RC-508 | Decência cósmica (ética ellâmica) | B071, P2025-03-15, P2025-02-15, P2024-11-30, P2024-11-09, P2021-09-04, P2023-12-03 |
| RC-509 | Protagonismo consciencial | B071, P2025-02-16, P2025-02-15, P2024-11-30, P2024-11-09, P2024-09-29 |
| RC-511 | Mêntion (estruturas da mente extrafísica) | B071, B074, B075, P2026-07-30, P2024-05-04, P2026-04-02 |
| RC-512 | Amnésia espiritual (esquecimento das origens) | B071, ART-2026-08-18 |
| RC-521 | Arquivos da Memória Cósmica | B072, P2025-03-15, P2025-02-15, P2024-11-30 |
| RC-522 | Parasitismo energético (obsessão ampliada) | B072, P2022-12-17 |
| RC-523 | Vampirismo consciencial | B072, P2022-12-17, P2025-02-15 |
| RC-524 | Coleta de informações (espírito encarnado) | B072, P2025-03-15, P2025-02-15, P2024-11-30 |
| RC-527 | Antimundo / antimatéria ('outro lado' da criação) | B072, P2025-03-15, P2025-02-16, P2024-11-30 |
| RC-531 | Laboratório Genético Terra (linhagens monitoradas) | B073, P2024-09-29 |
| RC-532 | Vacina do Amor (ancoragem de Jesus no CFD) | B073 |
| RC-838 | Satchidanandaghana (super código genômico do Projeto TALM) | P2024-06-16 |
| RC-840 | Kleśas (cinco entraves mentais ao progresso humano) | P2024-06-16 |
| RC-875 | Dhanvantari (o médico dos devas: Amrita e a Ayurveda cósmica) | P2026-03-21 |
| RC-885 | Savant (a genialidade preservada além do autismo num grau; figura útil no final) | P2021-06-26 |
| RC-932 | Cidades Sagradas do Hiperbóreo | P2024-03-17, P2018-12-15 |

### D · só-estrutural (R1 restrita ou R3) — 21

| Código | Nome | Fontes declaradas |
|---|---|---|
| RC-220 | Conspiração do Desespero | B002 |
| RC-224 | Prevalece o Amor | B002, P2025-03-15 |
| RC-229 | A Lógica de Javé e a Origem da Humanidade | B033 |
| RC-237 | Land's End (Sinal de Land's End) | B017 |
| RC-255 | A Mensagem do Codificador de Zion | B016 |
| RC-276 | Sacralização do Absurdo | B014 |
| RC-309 | Ordem dos Indecifráveis | B022 |
| RC-317 | Esgotamento e Solidão (dos Trimurtianos) | B022 |
| RC-318 | A Estranha Autorrealização de Shiva | B022 |
| RC-345 | Sentimento Luciferiano | B003 |
| RC-348 | Roteiro do Exílio | B026 |
| RC-349 | Exílios Interplanetários | B003 |
| RC-370 | A Criação de Ídolos para a Humanidade | B049 |
| RC-383 | Roteiro do Absurdo Implantado na Criação | B041 |
| RC-384 | Proposta de um Humano Terrestre aos Elétrons | B041 |
| RC-387 | Fragmentação do Poder Mental da Divindade | B041, P2024-05-04, P2025-03-15, P2025-02-16, P2024-11-30, P2024-11-09, P2020-07-04, P2023-12-03 |
| RC-441 | Mistérios Dionisíacos | B052 |
| RC-457 | Sarasvati (consorte de Brahma, Tridevi) | B060, P2021-12-04, P2024-07-14 |
| RC-458 | Lakshimi (consorte de Vishnu, Tridevi) | B060, P2021-12-04, P2024-07-14 |
| RC-462 | Oannes (filho de Ostronomos) | B060 |
| RC-542 | Ex-DNA-lixo (DNA não codificante reinterpretado) | B019, P2025-03-15, P2025-02-15, P2024-11-30 |

### C · prosa fora das fontes declaradas — 17

| Código | Nome | Fontes declaradas |
|---|---|---|
| RC-216 | Queda do Arquiteto Universal | B002, B019 |
| RC-315 | O Fim da Lila | B022, P2024-11-30, P2023-11-19, P2023-12-03 |
| RC-351 | Mestres de Capela | B025 |
| RC-354 | Trilogia Queda e Ascensão Espiritual | B003, B025, B026 |
| RC-380 | Imanência e Transcendência (Upanishades) | B041 |
| RC-428 | Tempo-limite (transição crítica de Javé) | B036, P2024-11-30, P2024-09-29 |
| RC-444 | Família Cromon | B059, B057, P2020-08-08, P2020-04-25, P2022-03-26, P2023-12-03 |
| RC-468 | Ein Sof (Prabrajna na Cabala) | B060 |
| RC-469 | Khorsis (Mundo dos Tronos) | B060 |
| RC-484 | Anjos ministradores (Usá, Azá, Aziel) | — |
| RC-491 | Família Shanlung (13 membros em Alt'Lam Gron) | B057, P2020-04-25 |
| RC-492 | Membros da Família Yel (Luziel, Adrax, Breasil, Lupon) | — |
| RC-493 | Os 9 Val dos Corpos Perdidos | — |
| RC-501 | Conselho dos Cinco (comando da Frota Norte: 3 Val + 2 Yel) | — |
| RC-502 | Val Aten (último Val de Val-Ha) | — |
| RC-519 | Herança Cósmica (padrões de existências anteriores) | B072, P2025-03-15, P2025-02-15, P2024-11-30 |
| RC-886 | Campo de Higgs (o campo de força mental de Mavatma que definiu o limite velocidade-da-luz) | P2021-06-26 |

## 8. Consequência imediata

A R1 vinha sendo executada sobre uma lista submedida em ~70%. Antes de materializar o lote 3, o Curador precisa decidir se o poço passa a ser os 142 da família B da v2 — e, com ele, se o V presuntivo por fonte de livro (despacho de 13/09/2026, escopo: lotes 1 e 2) continua valendo para os lotes seguintes.

