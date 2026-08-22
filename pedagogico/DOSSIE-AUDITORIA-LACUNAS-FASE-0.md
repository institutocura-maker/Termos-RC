# DOSSIE DE AUDITORIA DE LACUNAS — FASE 0

**Base Terminológica RC — Revelações Cósmicas de Jan Val Ellam**  
Gerado em 2026-08-22 pelo Agente RC (Arena) · Supervisão: curador Edson Cella Mendes  
Ferramenta reutilizável: `ferramentas/_auditoria_lacunas.py` · Matriz de apoio: `_matriz-auditoria-lacunas.csv`

> **Objetivo da Fase 0:** responder, com dados, *quais livros merecem reprocessamento* no fluxo moderno (camadas → unidades → chunks → leituras → dossiê → devolutiva → ampliações). Nenhuma decisão é tomada aqui: este dossiê **não altera a KB** e orienta a escolha do piloto (Fase 1).

## 1. Resumo executivo

- **Panorama:** 777 termos · 1852 relações · 428 fichas físicas · 86 obras na BIBLIO · 95 fontes distintas citadas na malha.

- **354 termos sem ficha física** (46% da malha) — vivem só na tabela-mestra; nenhuma ampliação, nenhuma citação rastreável.

- **40 obras marcadas como 'trabalhada'** (era pré-GitHub) — mas a representação na malha é **muito desigual**: de 145 citações (B031, glossário secundário) até **7** entre as primárias trabalhadas (B040, B043).

- **35 obras com ZERO citações** na malha — todas as 9 'a confirmar' (sem PDF) + 24 'identificadas' + 5 'anunciadas'.

- **13 fichas magras** (≤150 palavras) — esqueletos sem carne.

- **Lacuna infraestrutural:** nenhum PDF/TXT de livro está arquivado no workspace (os 28 uploads processados são de palestras). **Reprocessar livro exige o original** — o curador precisará anexar os PDFs na Fase 1.

- **Nota de governança:** B031 (glossário de Raquyel Braga) é a 2ª fonte mais citada (145 termos) — fonte **secundária** que deu o esqueleto da tabela; obras primárias de Ellam devem ser prioridade no reprocessamento.

## 2. Metodologia

- **Malha:** `ferramentas/dados_termos.py` (TERMOS: código, nome, categoria, subcategoria, status, fontes, relacionados, ficha).

- **Obras:** BIBLIO em `ferramentas/build_xlsx.py` (86 obras: B001–B083 + ART-2025-08-01/02/03), lida por regex (nunca editada).

- **Fichas:** arquivos em `termos/` (428). 'Magra' = ≤150 palavras.

- **Indicador de cobertura:** nº de termos que citam a obra no campo *fontes* (citação ≠ profundidade, mas é o melhor proxy disponível sem os textos).

- **Potencial de ampliação por obra:** nº de termos associados à obra **sem ficha física** (só a tabela-mestra tem o termo).

## 3. Panorama da BIBLIO

| Status | Qtd | Leitura para a auditoria |
|---|---|---|

| trabalhada | 40 | processadas na era pré-GitHub — candidatas a re-curadoria seletiva |

| identificada | 19 | mapeadas, sem processamento |

| a confirmar | 9 | aguardando PDF — não citadas |

| anunciada | 9 | futuras/em lançamento (B079–B083 etc.) |

| minerada | 4 | Enciclopédias/Glossários (B060/061/071/072/073) |

| curadoria | 3 | materiais ART — já no fluxo moderno |

| amostra recebida | 2 | parciais (B027, B035) |


## 4. Cobertura da malha por obra (ranking)

Contagem de termos que citam cada obra como fonte. Obras B### trabalhadas, ordenadas:

| Obra | Título | Citações | Termos-sf (potencial) |
|---|---|---|---|

| B031 | Painéis Emergentes da Revelação Cósmica | 145 | 111 |

| B060 | Personagens e Terminologias da Revelação Cósmica | 67 | 30 |

| B024 | A Epopeia dos Agentes da Vida Universal | 49 | 29 |

| B044 | A Divina Colmeia | 40 | 21 |

| B001 | O Drama Cósmico de Javé | 31 | 13 |

| B021 | Tempos Difíceis no Olimpo | 29 | 13 |

| B013 | Tzimtzum | 27 | 9 |

| B023 | O Dharma e as Castas Hindus | 27 | 12 |

| B022 | Inquisição Trimurtiana | 26 | 14 |

| B016 | O Quarto Logos | 25 | 10 |

| B002 | O Drama Espiritual de Javé | 24 | 11 |

| B020 | O Sorriso de Pandora | 24 | 11 |

| B014 | Sophia e o Logos Criadores | 23 | 10 |

| B017 | Terra Atlantis I: O Sinal de Land's End | 23 | 14 |

| B005 | Fator Extraterrestre | 22 | 10 |

| B015 | O Guardião do Éden | 22 | 12 |

| B036 | As Memórias de Javé | 22 | 10 |

| B003 | Reintegração Cósmica | 21 | 10 |

| B018 | Terra Atlantis II: A Frota Norte | 21 | 14 |

| B051 | Diagrama Geral de Ligações entre Termos | 21 | 13 |

| B057 | Os Livros de Yel Luzbel 1: A Revolta do Anjo Decaído | 21 | 9 |

| B058 | Os Livros de Yel Luzbel 2: O Início da Revolta Capel | 21 | 12 |

| B019 | Nem Deus, nem Javé, nem Darwin | 20 | 11 |

| B041 | A Rebelião dos Elétrons e o Código de Vida do Criado | 20 | 11 |

| B048 | Favor Divino | 20 | 9 |

| B052 | Homoafetividade | 18 | 10 |

| B039 | Terra Atlantis III: A Era Sapiens | 17 | 12 |

| B042 | Crônicas de um Novo Tempo | 17 | 8 |

| B033 | O Drama Terreno de Javé | 16 | 6 |

| B050 | Guia das Eras Universais (Mapa) | 16 | 10 |

| B025 | Caminhos Espirituais | 15 | 6 |

| B074 | Mentalma I: A Consciência Esclarecida e a Gestão dos | 15 | 7 |

| B026 | Carma e Compromisso | 14 | 6 |

| B075 | Mentalma II: Gestão Psíquica e Memórias Complexas | 14 | 7 |

| B006 | Nos Bastidores da Luz I | 13 | 11 |

| B034 | Cartas a Javé | 13 | 5 |

| B011 | Jesus e o Enigma da Transfiguração | 11 | 5 |

| B049 | Jesus e Nietzsche | 9 | 3 |

| B040 | Homo Sapiens: da Guerra ao Esporte | 7 | 4 |

| B043 | Jesus e o Druida da Montanha | 7 | 4 |


*'Termos-sf' = termos que citam a obra e não têm ficha física (candidatos a ampliação se a obra for reprocessada).*

## 5. Obras trabalhadas SUB-REPRESENTADAS (≤20 citações)

Candidatas naturais ao reprocessamento (a priorizar por centralidade temática):

| Obra | Título | Citações | Termos-sf |
|---|---|---|---|

| B040 | Homo Sapiens: da Guerra ao Esporte | 7 | 4 |

| B043 | Jesus e o Druida da Montanha | 7 | 4 |

| B049 | Jesus e Nietzsche | 9 | 3 |

| B011 | Jesus e o Enigma da Transfiguração | 11 | 5 |

| B006 | Nos Bastidores da Luz I | 13 | 11 |

| B034 | Cartas a Javé | 13 | 5 |

| B026 | Carma e Compromisso | 14 | 6 |

| B075 | Mentalma II: Gestão Psíquica e Memórias Complexas | 14 | 7 |

| B025 | Caminhos Espirituais | 15 | 6 |

| B074 | Mentalma I: A Consciência Esclarecida e a Gestão dos | 15 | 7 |

| B033 | O Drama Terreno de Javé | 16 | 6 |

| B050 | Guia das Eras Universais (Mapa) | 16 | 10 |

| B039 | Terra Atlantis III: A Era Sapiens | 17 | 12 |

| B042 | Crônicas de um Novo Tempo | 17 | 8 |

| B052 | Homoafetividade | 18 | 10 |

| B019 | Nem Deus, nem Javé, nem Darwin | 20 | 11 |

| B041 | A Rebelião dos Elétrons e o Código de Vida do Criado | 20 | 11 |

| B048 | Favor Divino | 20 | 9 |


## 6. Obras com ZERO citações (sem PDF ou não processadas)

| Obra | Título | Status |
|---|---|---|

| B004 | A Sétima Trombeta do Apocalipse | a confirmar |

| B007 | Nos Bastidores da Luz 2 | a confirmar |

| B008 | Nos Bastidores da Luz 3 | a confirmar |

| B009 | Muito Além do Horizonte | a confirmar |

| B010 | O Testamento de Jesus | a confirmar |

| B012 | Recado Cósmico | a confirmar |

| B028 | O Sorriso do Mestre | a confirmar |

| B029 | Inquisição Poética | a confirmar |

| B030 | A Teia do Tempo | a confirmar |

| B032 | Queda e Ascensão Espiritual (trilogia) | identificada |

| B037 | Inquisição Filosófica | identificada |

| B038 | Frota Norte | identificada |

| B045 | Projeto Talm: a Gênese da Vida Superior | anunciada |

| B046 | Xadrez Cósmico (livro) | anunciada |

| B047 | Dramas de Shiva (trilogia anunciada) | anunciada |

| B053 | O Sentido Gradual das Leis Morais | anunciada |

| B054 | Sophia e o Pêndulo Cósmico | anunciada |

| B055 | O Incompreendido Norte Divino | anunciada |

| B056 | O Desvio de Rota de Pandora e o Quarto Logos Universal | anunciada |

| B062 | Ignorância santificada | identificada |

| B063 | Reflexões Quase Filosóficas: Schopenhauer e o Sofrimento | identificada |

| B065 | O abismo da consciência cósmica | identificada |

| B066 | O Manual da Busca Filosófica do Sentido da Vida | identificada |

| B067 | Prodigium: a Necessidade Criativa do Khaos | identificada |

| B068 | O Funeral da Evidência | identificada |

| B069 | Shiva e a Esquecida Origem do Yoga | identificada |

| B070 | A Escola da Decifração da Realidade: O Método Dru'uid An | identificada |

| B076 | Mentalma III: Autoconhecimento e Emancipação | identificada |

| B077 | Mentalma IV: Consciência Pessoal e Soberania Espiritual | identificada |

| B078 | Mentalma V: Autorrealização | identificada |

| B079 | Inquisição Espiritual | anunciada |

| B080 | Perversa Gratidão | identificada |

| B081 | Sophia, os Arcontes e a Disputa pela Suzerania Universal | identificada |

| B082 | Nem Deus, nem Javé, nem Darwin: a evolução do cérebro | identificada |

| B083 | Awayen – A Central de Realidades | anunciada |


**Total: 35 obras.** Nenhuma delas pode ser reprocessada sem o PDF original (anexar em upload na Fase 1).

## 7. Termos sem ficha física (354)

**354 termos** têm entrada na tabela-mestra (nome, categoria, fontes, relações) mas **não têm ficha em `termos/`** — não há ampliação, contexto ou citação rastreável. Distribuição por categoria:

| Categoria principal | Termos sem ficha |
|---|---|

| Seres & Entidades | 120 |

| Conceitos Cosmológicos | 96 |

| Eventos & Eras | 37 |

| Lokas & Geografias | 32 |

| Termos Específicos | 22 |

| Tecnologias & Artefatos | 16 |

| Genealogias & Linhagens | 16 |

| Processos & Fenômenos | 15 |


Lista completa: ver `_matriz-auditoria-lacunas.csv` (coluna 'sem_ficha'). Exemplos de termos órfãos já sinalizados na Colecionar Incertezas: RC-013/014 (Adhyatman/Adhydaiva), RC-135 (Vishnu/Lakshmi), RC-163 (Mente Universal Emergente), RC-190 (Kardec), RC-211 (Kundalini), RC-343, RC-542, RC-457/458/459 (Tridevi) etc.

## 8. Fichas magras (≤150 palavras)

**13 fichas** são esqueleto sem carne — cabeçalho + definição sintética, sem ampliação:

| Palavras | Ficha |
|---|---|

| 73 | RC-667-autofagia-do-criador |

| 109 | RC-688-yajna-ritual-de-sacrificio-fogo |

| 110 | RC-675-binah |

| 110 | RC-676-chesed |

| 110 | RC-677-geburah |

| 110 | RC-679-netzach |

| 110 | RC-680-hod |

| 114 | RC-678-tiferet-tiphareth |

| 114 | RC-683-tora-pentateuco |

| 116 | RC-668-som-da-flauta-som-da-falta |

| 117 | RC-670-yoga-ancestral-origem-cosmica |

| 117 | RC-681-yesod |

| 118 | RC-689-sangue-como-copia-da-seiva |

## 9. Lacuna infraestrutural (crítica para a Fase 1)

- **Nenhum PDF/TXT de livro está no workspace.** `uploads/processados/` contém 28 arquivos, todos de palestras/materiais do projeto.

- Sem o original não há camada 0, chunks nem citações verbatim — o reprocessamento de livros **depende de upload** pelo curador.

- Obras com PDF já 'trabalhadas' na era antiga (40) precisam ser **re-anexadas** para o fluxo moderno; as 'a confirmar' (9) precisam do PDF pela 1ª vez.

## 10. Recomendação de priorização (proposta, aguarda devolutiva)

**Critérios:** (1) centralidade na Revelação; (2) sub-representação atual (poucas citações + termos-sf); (3) disponibilidade prática do PDF; (4) Navalha de Ockham — reprocessar para **ampliar/auditar/rastrear**, não para criar códigos.

- **Piloto (Fase 1) — candidatos com melhor custo-benefício:**

  - **B019 *Nem Deus, nem Javé, nem Darwin*** (20 citações; 18 capítulos; 2021) — ponte direta com a malha recente (RC-538–547 criados no seu ciclo; palestra P2021-01-23 já curada); PDF 238 págs; tema evolucionário de alto rendimento.

  - **B011 *Jesus e o Enigma da Transfiguração*** (11 citações; 176 págs; 2002) — obra primária antiga, tema central (Jesus), sub-representada; PDF já existiu no projeto.

  - **B040 *Homo Sapiens: da Guerra ao Esporte*** (7 citações) — a mais sub-representada das 'trabalhada'; tema periférico, bom para testar o fluxo sem risco de contaminar o núcleo.

- **Fase 2 (escala seletiva):** reprocessar, um ciclo por vez, as obras da seção 5 (≤20 citações) em ordem de centralidade, mais B013 (Tzimtzum) e B014 (Sophia e o Logos) como **auditoria de grafias canônicas** (livros centrais que definem vocabulário).

- **Fichas magras (seção 8):** candidatas a ampliação sempre que o livro/palestra-fonte entrar em ciclo — sem ciclo, permanecem.


---

*Fim do dossiê — Fase 0. Próximo passo: devolutiva do curador (escolha do piloto + anexo do PDF). Este dossiê não altera a Base Terminológica (777 termos / 1.852 relações permanecem intactos).*
