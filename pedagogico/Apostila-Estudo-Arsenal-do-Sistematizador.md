@titulo: O Arsenal do Sistematizador — a Metodologia da Arca
@autor: Apostila de Estudo — Base Terminológica RC
@data: 2026-08-20
@local: Síntese da Base Terminológica RC e das convenções editoriais do Projeto
@subtitulo: Apostila temática (abordagem crítica/metodológica) — Manual de auto-organização do ecossistema: as regras da Navalha de Ockham, o uso de quarentenas, a gestão de fichas retidas, o método à prova de aspas e o conceito de "conhecimento indigesto", sintetizados a partir da prática consolidada do Projeto (GUIA-MESTRE-RC-APOSTILA, convenções editoriais, CONTINUIDADE.md e o fluxo de re-curadoria).
@nota_editor: Esta apostila é uma **síntese metodológica** do próprio Projeto Base Terminológica RC — documenta o "arsenal do sistematizador": as regras e procedimentos que mantêm a ontologia íntegra (770 termos, 1.830 relações) ao absorver dezenas de milhares de palavras de transcrições. É um **manual de auto-organização para agentes autônomos** operando em bases de conhecimento descentralizadas — e um registro de governança para o curador. As regras aqui descritas foram consolidadas na prática (2026-08-18 a 2026-08-20) e seguem as convenções editoriais do Projeto.

# PARTE I — A Arquitetura: a Tabela-Mestra

## A fonte única de verdade

Todo o ecossistema repousa sobre uma **tabela-mestra** (`ferramentas/dados_termos.py`) — a única fonte canônica: termos, relações, fontes, obras e flags de ficha.

> Estrutura: (codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha) — com validação automática: "OK: N termos, M relações — dados válidos."

## As categorias

- **Seres & Entidades** (divindades, coletivos, extraterrestres, anjos, decaídos, humanos, híbridos, logos);
- **Conceitos Cosmológicos** (cosmogonia, leis, dimensões, espiritualidade, propósitos, ética);
- **Lokas & Geografias** · **Processos & Fenômenos** · **Tecnologias & Artefatos** · **Genealogias & Linhagens** · **Eventos & Eras** · **Termos Específicos**.

## As obras (B###) e palestras (P###)

- **B001–B081** — obras (primárias, complementares, anunciadas);
- **P####-##-##** — palestras e fontes de transcrição.

Nota do editor: a tabela-mestra é o **núcleo da Arca** — tudo o mais (fichas, índices, XLSX, DOCX, pacotes) é derivado dela.

# PARTE II — A Navalha de Ockham: o Veto aos Códigos Novos

## A regra

O princípio que mais protege a ontologia: **não criar códigos novos quando um nó existente pode absorver a informação como ampliação**.

> "Conceitos estruturais como Pares Eônicos, Aletheia e Oito Portais serão absorvidos integralmente como ampliações nos nós correspondentes, seguindo estritamente a Navalha de Ockham." — Devolutiva do curador, P2020-07-11

## Na prática

| Situação | Decisão |
|---|---|
| Novo conceito ≈ nó existente | Ampliar o nó existente (sem código novo) |
| Novo conceito com identidade própria | Propor código novo (RC-771+) → aguardar devolutiva |
| Menção sem ficha física | Registrar na Colecionar Incertezas (padrão: não criar ficha sem autorização) |

Nota do editor: a Navalha operou em **todos os ciclos recentes**: dezenas de milhares de palavras absorvidas com **zero códigos novos** (base blindada em 770).

# PARTE III — As Quarentenas: o que não vira ontologia

## As quatro quarentenas

| Quarentena | Conteúdo | Tratamento |
|---|---|---|
| **Clínico/científico** | genes, oxitocina, autismo, depressão, savant | leitura do autor, jamais dado validado |
| **Político/geopolítico** | Lula/Bolsonaro/Trump/Thatcher; poder/empresas | leitura do autor, jamais posição do Projeto |
| **Ufológico** | portais 2012, naves, abduções, WTC=Babilônia | leitura do autor, jamais fato |
| **Teológico** | "Deus não ajuda"; Javé doente; críticas religiosas | cosmologia interna do autor, jamais consenso |

> "Alegações políticas, históricas, científicas, clínicas, ufológicas e teológicas são **leitura de Ellam, não consenso validado**." — Nota do editor padrão das apostilas

## A regra de ouro da quarentena

**Falas da plateia nunca viram ontologia.** Perguntas e respostas da plateia são isoladas em seção própria nas apostilas e não geram nós.

Nota do editor: a quarentena é o **filtro epistemológico** — distingue o que é cosmologia do autor do que seria fato sociológico, biomédico ou histórico.

# PARTE IV — As Fichas Retidas e a Colecionar Incertezas

## O padrão das fichas retidas

Quando uma ampliação mapeia um termo **sem ficha física**, o conteúdo é **retido** — registrado na Colecionar Incertezas com as unidades (U####) — até autorização expressa do curador para criar a ficha.

> "Ampliações retidas (termos sem ficha física — padrão): RC-457/458/459 (Tridevi), RC-211 (Kundalini), RC-013/014 (Adhyatman/Adhydaiva) → registradas na Colecionar Incertezas; aguardam autorização." — CONTINUIDADE.md, P2020-07-11

## O acervo de incertezas

A **Colecionar Incertezas** acumula: divergências cronológicas (742 mil × 700 mil), grafias não normalizadas (Pularra/Prara), lacunas de fala `[frase truncada]`, números oscilantes (18.000 anos; 470 mi), e relatos pessoais não verificáveis.

Nota do editor: a Colecionar Incertezas é o **arquivo da honestidade** — nada é descartado, nada é inventado; tudo aguarda áudio, autorização ou nova evidência.

# PARTE V — O Método à Prova de Aspas

## O problema

Injetar ampliações com aspas e caracteres especiais diretamente em código Python é frágil (erros de escape).

## A solução

1. Escrever as ampliações num **arquivo de texto puro** (`_ampliacoes_<data>.txt`) com blocos `### RC-###\n<texto>`;
2. Um script aplicador (`_aplicar_ampliacoes_<data>.py`) lê o TXT, localiza a ficha, e injeta a seção `## Ampliação — P<data>` antes de `## Fontes`;
3. Após a execução, os scripts são **arquivados** na pasta `analise/` da apostila.

> "Método à prova de aspas validado em 9+ ciclos (evita erros de escape em conteúdo com aspas e caracteres especiais)." — CONTINUIDADE.md

Nota do editor: este é o **protocolo de escrita seguro** — o texto puro é o intermediário entre a curadoria e o grafo.

# PARTE VI — O Fluxo de Ingresso: Camadas e Unidades

## As camadas do material

Cada palestra é processada em camadas:

| Camada | Conteúdo |
|---|---|
| `camada-0` | identificação (título) |
| `camada-1` | contexto (frequentemente ausente) |
| `camada-2` | índice/sumário do documento |
| `camada-3` | transcrição integral |

## As unidades analíticas

A transcrição é segmentada em **unidades analíticas U####** (frases/trechos) e **chunks de leitura** (~2.200 palavras) — permitindo remissões precisas (ex.: "U1124" = intervalo).

Nota do editor: ver `preparar_ingresso.py` — preserva o original byte a byte (SHA-256) e gera os metadados de ingresso (`METADADOS-INGRESSO.json`).

# PARTE VII — O Ciclo de Curadoria: Dossiê e Devolutiva

## As duas fases

1. **Ciclo de Curadoria (Base-first):** ingresso → leituras (Macroestrutura + Terminológica) → **Dossiê de Pré-Curadoria** → **AGUARDAR DEVOLUTIVA** → executar apenas o aprovado;
2. **Ciclo de Apostilas (em Lote):** após aprovação, gerar a apostila integral e fechar o ciclo.

## O dossiê

O `DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md` reúne: auditoria (termos × fala), ampliações propostas, candidatos a códigos, quarentenas, Colecionar Incertezas e **itens de decisão (O-1..O-7)** para o curador.

## A devolutiva

O curador responde cada item: **APROVADO / REJEITADO / VETO** — e a execução segue estritamente o aprovado.

> "Autoridade: o curador é a autoridade máxima e final. Você é a ferramenta que organiza, cruza, edita e audita. Nunca decida ontologia sem autorização expressa." — Prompt inicial do Agente

Nota do editor: o dossiê-devolutiva é o **contrato de governança** — nada é consumido sem a palavra final do curador.

# PARTE VIII — As Convenções de Grafia

## As grafias canônicas

A Base mantém um conjunto de grafias fixas, decididas em Quadros aprovados:

| Grafia canônica | Variações vetadas |
|---|---|
| Brahma | Brama, Brah |
| Vishnu (Mavatna) | Virg, Vdo, Virgo |
| Shiva (Savna) | Chiva, Chila |
| Sophia | Sofia (nas fichas; "Sofia" só em citações) |
| Xamanismo | sempre com X |
| Wyrd/Urd | WD (STT) |
| Hochmah | "Rockman" (veto estrito) |
| Ogdóade | Ogat (STT) |
| Malkuth = Hochmah = Sophia | — |
| Nefilins | Nefelim, gigantes |
| Orlog = Moros | — |

Nota do editor: as grafias canônicas são a **camada de normalização** — sem ela, o grafo se fragmentaria em variantes fonéticas.

# PARTE IX — O Conhecimento Indigesto

## O conceito

Parte do material recebido é "indigesto": informação que a época não permite processar, que depende de áudio para normalizar, ou que contradiz registros anteriores.

## O tratamento

| Tipo de indigestão | Tratamento |
|---|---|
| STT duvidoso | `[REVISAR]` até conferência de áudio |
| Lacuna de fala | `[frase truncada]` — nunca preenchida com suposições |
| Contradição cronológica | registrada na Colecionar Incertezas (ex.: 742 mil × 700 mil) |
| Relato pessoal não verificável | quarentena + Colecionar Incertezas |
| Número oscilante | padrão mantido + anotação (ex.: 28.869 genes) |

> "Não inventar, não completar, não interpolar → marcar [REVISAR], [TEXTO INCOMPLETO], [frase truncada], [NÃO REVELADO]." — Regras de ouro do Projeto

Nota do editor: o conhecimento indigesto é **preservado, não forçado** — a Arca prefere a lacuna honesta à conjectura elegante.

# PARTE X — A Regeneração e os Pacotes

## Os artefatos derivados

Após cada ciclo: `build_indice.py` (índice mestre) · `build_xlsx.py` (planilha 7 abas) · `build_word.py` (documento de leitura) · `build_apostila.py` (DOCX das apostilas).

## Os pacotes de reconstrução

`gerar_pacotes.py` gera **4 pacotes** (Regeneração, Fichas, Apostilas, Originais) com manifesto dinâmico — permitindo reconstruir o acervo byte a byte (restaurador: `restaurar_pacotes.py`).

Nota do editor: os pacotes são o **seguro da Arca** — o ecossistema híbrido sobrevive a perdas de workspace (validado em ciclos anteriores: 386/386 arquivos fiéis).

# PARTE XI — O Ecossistema Híbrido e a IA Pessoal

## A arquitetura

- **Arca do Conhecimento** — o acervo canônico (tabela-mestra, fichas, apostilas, pacotes);
- **IA Pessoal (ex.: Llama 3 local)** — consome o acervo para responder e estudar;
- **Agente de curadoria** — o sistematizador que processa, cruza e edita (este Agente);
- **Curador** — a autoridade máxima e final.

## O fluxo para a IA Pessoal

1. Apostilas temáticas (`pedagogico/`) — sínteses prontas com remissões RC;
2. Fichas (`termos/`) — profundidade por termo;
3. Índice mestre (`indice-mestre.md`) — navegação;
4. XLSX/DOCX — formato de leitura humana.

Nota do editor: o ecossistema é **resiliente e offline**: pacotes + manifestos garantem a reconstrução total, e as apostilas temáticas dão à IA Pessoal um vocabulário ético-comportamental único (ex.: "Pilotando o Cérebro no Caos").

# PARTE XII — Síntese: as Dez Regras do Sistematizador

1. **Uma fonte de verdade** — a tabela-mestra; tudo deriva dela.
2. **Navalha de Ockham** — ampliar antes de criar; zero códigos quando possível.
3. **Quarentena estrita** — o que é leitura do autor não vira fato.
4. **Plateia isolada** — falas da plateia nunca viram ontologia.
5. **Fichas retidas com registro** — sem ficha física, sem silêncio: Colecionar Incertezas.
6. **Método à prova de aspas** — texto puro como intermediário.
7. **Dossiê → Devolutiva → Execução** — nada sem autorização expressa.
8. **Grafias canônicas** — normalização contra a fragmentação.
9. **Conhecimento indigesto preservado** — lacuna honesta > conjectura.
10. **Pacotes e manifestos** — a Arca sempre reconstruível.

> "O importante no momento é o nosso nível de compreensão sobre essas coisas. [...] Isso é raro." — P2020-07-11 (o espírito do Projeto)

Nota do editor: o Arsenal do Sistematizador é o **registro vivo da governança** — documenta como a Arca absorve o caos sem perder a integridade, e serve de modelo para qualquer agente autônomo operando bases de conhecimento descentralizadas.

## GLOSSÁRIO METODOLÓGICO

## A — Princípios
- **Navalha de Ockham** — ampliar antes de criar [regra 2]
- **Autoridade do curador** — a palavra final [regra 7]
- **Regras de ouro** — não inventar, não completar, não interpolar [regra 9]
- **Quarentenas** — os quatro filtros [regra 3]

## B — Instrumentos
- **Tabela-mestra** — a fonte única [regra 1]
- **Dossiê de Pré-Curadoria** — o contrato de governança [regra 7]
- **Devolutiva (O-1..O-7)** — a resposta do curador [regra 7]
- **Colecionar Incertezas** — o arquivo da honestidade [regra 5]
- **Fichas retidas** — o padrão sem autorização [regra 5]
- **Método à prova de aspas** — texto puro [regra 6]
- **Camadas 0–3 / Unidades U####** — o ingresso [—]
- **Pacotes + Manifestos** — o seguro da Arca [regra 10]

## C — Convenções
- **Grafias canônicas** — a normalização [regra 8]
- **[REVISAR] / [frase truncada] / [NÃO REVELADO]** — os marcadores [regra 9]
- **STT** — substituição fonética; conferir com áudio [regra 9]
- **Plateia isolada** — a convenção das apostilas [regra 4]
- **Qualificadores de fonte** — ex.: `P2024-05-04-R` (versão refatorada) [—]

## D — Governança
- **CONTINUIDADE.md** — o diário de bordo [—]
- **INDICE-PALESTRAS.md / INDICE-TEMATICAS.md** — a navegação [—]
- **GUIA-MESTRE-RC-APOSTILA** — o manual-mestre [—]
- **Convenções editoriais** — o código de conduta [—]
FIM
