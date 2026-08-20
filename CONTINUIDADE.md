# Continuidade — Base Terminológica RC

**Data de sincronização:** 2026-08-18 (ciclo P2025-11-29 — A Revelação de Ifá e o Destino dos Seres)  
**Estado canônico:** **767 termos (`RC-001–RC-767`), 1.531 relações, 377 termos com ficha e 378 fichas físicas** (377 canônicas + RC-004 como investigação). Fonte única: `ferramentas/dados_termos.py` · checksum `7a95c8dd5bdb9b981b55f43e9dd1e34229f155be548e232870b27d9e69d028ac`.

**Última atualização (2026-08-18) — Ciclo P2025-11-29 (A Revelação de Ifá e o Destino dos Seres) concluído com devolutiva do curador:**
- **1 código novo:** RC-767 **Os 256 Caminhos Profetizáveis de Orunmilá** (COS_PRO 2.5) — estrutura técnica da destinação dos seres (ancestralidade, protocolos, álbum memorial); correlacionado à Teia/Wyrd;
- **Compactação:** NT-IF02 (6 Etapas) e NT-IF03 (Ifismo) → absorvidos em RC-655; NT-IF04 (Divinosfera dos Orixás) → absorvido em RC-741;
- **RC-655/665/666 elevados a FONTE PRIMÁRIA definitiva** (Revelação de Ifá; Orunmilá = Moros de Orum; Obatalá = Javé) — o "missing link" prometido em P2024-09-28;
- **27 termos com fonte `P2025-11-29`** (24 ampliações + RC-767 + fichas novas RC-068/102/517) e **17 relações novas**;
- **Fichas:** RC-767/068/102/517 novas; 21 fichas ampliadas (incl. RC-001/666 Javé/Obatalá — fome de devoção; Krishna; Jesus; Islã; cuscuta);
- **Quarentena histórico-religiosa mantida:** Islã/Krishna/Maomé/Orixás = leituras do autor; "SUS da espiritualidade" = citação literária ilustrativa, não preceito;
- **Veto de STT confirmado:** Hainarok (= Ragnarök), Osamaro Ibier/Croma, 4.261 a.C., morrensor/moruself, imoléis, Vaius — Colecionar Incertezas até áudio;
- Base validada (`OK: 767 termos, 1531 relações`); índice/XLSX/DOCX regenerados; pacotes de reconstrução regenerados (hábito — manifesto dinâmico);
- Backup pré-ciclo: `reconstrucao/backups/dados_termos_pre-P2025-11-29_2026-08-18.py`.

> As seções históricas abaixo registram etapas intermediárias da reconstrução. Para contagens atuais, prevalece `ferramentas/dados_termos.py`.

**Correção de engenharia (2026-08-18) — gerador/restaurador de pacotes:** auditoria revelou que o gerador de pacotes embutia **1 byte `\n` extra** por arquivo (join com quebra de linha após conteúdo já terminado em `\n`; e marcador FIM-ARQ colado ao conteúdo quando o arquivo não termina em `\n`, ex.: `original.txt` do podcast irmãos Dias). Correções aplicadas: (1) `gerar_pacotes.py` agora **concatena o corpo sem join**, embutindo conteúdo byte a byte; (2) `restaurar_pacotes.py` localiza `===FIM-ARQ:` por **busca binária direta** (não mais regex de início de linha), aponta para `reconstrucao/pacotes/` (checkpoint mais recente) e aceita caminhos como argumentos. Teste de ida-e-volta: **386/386 arquivos 100% fiéis (pacote == manifesto == workspace)**.

> As seções históricas abaixo registram etapas intermediárias da reconstrução. Para contagens atuais, prevalece `ferramentas/dados_termos.py`.

## Estado restaurado inicial

- Tabela-mestra `TERMOS` inicialmente recuperada e depois ampliada para **727 registros**;
- grafo `RELACOES` atualmente com **1.218 relações**;
- bibliografia com 79 obras;
- builders de XLSX, índice Markdown, DOCX de leitura e apostilas;
- scripts e modelos incluídos no pacote;
- `indice-mestre.md` e `base-terminologica.xlsx` regenerados.

## Recuperação complementar das fichas

O `PACOTE-DE-FICHAS-2026-08-14.txt` restaurou **128 fichas detalhadas** em `termos/`:

- 127 correspondem aos termos marcados com `ficha=True` na tabela-mestra;
- 1 é a ficha adicional de investigação de `RC-004 — Elohim`.

Todas foram conferidas byte a byte. As curadorias posteriores acrescentaram 93 fichas, elevando o total físico para **221**. Não há fichas marcadas na tabela-mestra faltando.

## O que ainda não veio nos pacotes

- 42 extratos de livros `_B###_texto_extraido.txt`;
- documentos editoriais/pedagógicos integrais mencionados no Guia;
- arquivos-fonte da apostila “Faces de Javé”.

Esses itens não foram inventados nem reconstruídos por aproximação.

## Curadoria P2022-12-17 incorporada

A pré-curadoria da palestra de 17/12/2022 foi aprovada pelo curador e incorporada:

- 30 novos termos — `RC-566` a `RC-595`;
- 54 termos existentes reforçados com a fonte `P2022-12-17`;
- 82 relações novas;
- 30 fichas novas;
- 17 fichas existentes atualizadas;
- Base validada, sem códigos ou links quebrados.

## Reestruturação P2021-12-04 — C-01 a C-07

O primeiro bloco da palestra *Os Archeons de Ereon e os Seres Adhy* foi validado e incorporado sem criação de códigos novos:

- Ereon tornou-se grafia canônica de RC-496;
- Impérial/RC-497 foi deprecado como erro STT de Perpérion;
- Tempérion/RC-472 tornou-se canônico; Tempérium/RC-498 virou remissão histórica;
- Pashvnaj/RC-455 foi corrigido para espécie de 43 seres;
- Gênero Adhy/RC-411 foi firmado como 147 seres em cinco espécies;
- Seres LM/RC-456 foram aprofundados;
- 14 relações estruturais foram acrescentadas;
- 5 fichas estruturais novas foram criadas.

O Quadro 9 também foi incorporado:

- 24 termos novos — `RC-596` a `RC-619`;
- Paraíso Original mesclado a RC-204;
- Redes Psíquicas Coletivas mescladas a RC-188;
- Portal de Comunicação absorvido por RC-613;
- B079 Inquisição Espiritual registrado como obra anunciada;
- Colecionar Incertezas incorporado às convenções editoriais;
- apostila integral produzida com 667/667 unidades de cobertura.

## Devolutiva-01 — P2026-07-30

A primeira devolutiva da live *Estagiários do Kaos* foi incorporada parcialmente:

- correção canônica `Ealm` → **Elm**;
- dupla **Olm e Elm**, originária de Tempérion; enviada a Perpérion para observar a imponderabilidade e depois mergulhada no processo;
- En Ma/Emá/Emar mesclado em RC-476;
- Deva/Aurora ampliado em RC-475;
- 8 novos termos — RC-620 a RC-627;
- 25 relações novas;
- TÊNET fixado como grafia canônica;
- apostila em formato de entrevista produzida com cobertura integral; itens residuais permanecem no glossário para eventual curadoria posterior.

## Curadoria P2024-05-04 — Simultaneidade Reversa

- 15 novos termos: RC-628 a RC-642;
- Simultaneidade Reversa consolidada como princípio central;
- 46 relações novas;
- Paraíso B mesclado em RC-612;
- apostila integral produzida a partir do PDF de 39 páginas;
- cobertura verificada de 1234/1234 unidades.

## Curadoria P2025-03-15 — Rebelião dos Elétrons

- fonte oficialmente marcada como **INCOMPLETA**: o TXT encerra no intervalo;
- 1.184/1.184 unidades disponíveis incorporadas à apostila — 100% do fragmento;
- 4 termos novos:
  - `RC-690 Colapso do Caos Organizado`;
  - `RC-691 Ishvara (Isuara — Retrato de Prabrajna Antes da Queda)`;
  - `RC-692 Kit Reencarnatório de Elétrons`;
  - `RC-693 Evolução da Informação, não das Espécies`;
- 84 termos existentes reforçados, totalizando 88 termos com a fonte;
- 38 relações tipadas acrescentadas;
- **Satchidananda** validado e absorvido na ficha de Ishvara;
- formas W/WD/AD/Erde da palestra fixadas como **Wyrd/Urd — RC-658**, sem reforçar RC-560;
- divergência causal de `RC-434 Homoafetividade` preservada, com ressalva científica e clínica;
- Base, índice, XLSX e DOCX regenerados;
- apostila DOCX do fragmento produzida, aguardando revisão do curador.

## Curadoria P2025-02-16 — Oitavo Dia da Criação

- original preservado, SHA-256 `a85a1526cf2e062f758c7eaeda42bef938105d1326a90abc8bf5fc0b0b89de10`;
- 22.025 palavras e 1.272 unidades analíticas;
- sequência completa, incluindo perguntas e encerramento;
- 8 termos novos: `RC-694–RC-701`;
- 116 termos existentes reforçados, totalizando 124 termos com a fonte;
- 93 relações tipadas acrescentadas;
- RC-664 ampliado e Reino Naga/Uraga absorvido;
- RC-577/687 ampliados com Xamanismo Naga e ressalvas;
- intervenções sobre MK-Ultra/V2K mantidas fora da ontologia;
- Base, índice, XLSX e DOCX regenerados;
- apostila integral produzida com 1.272/1.272 unidades.

## Curadoria P2025-02-15 — Camuflagem da Realidade

- original preservado, SHA-256 `8488bd1fab74d753e42901371a2e27122da06810da582d5963c8f1901d33b793`;
- 29.399 palavras e 1.833 unidades analíticas;
- 12 termos novos: `RC-702–RC-713`;
- 111 termos existentes reforçados, totalizando 123 termos com a fonte;
- 108 relações tipadas acrescentadas;
- itens em quarentena mantidos sem código;
- Camada 2 não usada como fala;
- Base, índice, XLSX e DOCX regenerados;
- apostila integral produzida com 1.833/1.833 unidades.

## Curadoria P2024-11-30 — Moros e os Arquivos do Destino Universal

- original preservado, SHA-256 `7796e58cdd7cec8d2b58e7b21e759c9b7db216e8216564689b2621371a883d46`;
- 34.936 palavras e 1.982 unidades analíticas;
- 7 termos novos: `RC-714–RC-720`;
- 192 termos existentes reforçados, totalizando 199 termos com a fonte;
- 86 relações tipadas acrescentadas;
- grande Hub de Moros ampliado;
- eBook avaliado e mantido fora da Base;
- itens em quarentena mantidos sem código;
- Base, índice, XLSX e DOCX regenerados;
- apostila integral produzida com 1.982/1.982 unidades.

## Curadoria P2024-11-09 — O Abismo da Consciência Cósmica

- original preservado, SHA-256 `46e3d73cb316ca6f3ba2dc445337e7b3260b148e7674039ab6bd6047431dd8fd`;
- 20.996 palavras e 1.271 unidades analíticas;
- sequência aparentemente completa, incluindo perguntas e encerramento;
- camada contextual ausente no arquivo recebido;
- Dossiê com 42 itens consolidado pelo curador;
- 7 termos novos: `RC-721–RC-727`;
- 117 termos existentes reforçados, totalizando 124 termos com a fonte;
- 72 relações tipadas acrescentadas;
- autismo/protodemência bloqueados como causalidade ou diagnóstico;
- terapias não locais e transferência 3D→2D registradas com ressalvas fortes;
- Daath, Epinoia/Pistis Sophia e Rede Neural Planetária mantidos em `[REVISAR]`;
- intervenções da plateia separadas e Camada 2 excluída como evidência;
- Base, índice, XLSX e DOCX regenerados;
- apostila integral produzida com 1.271/1.271 unidades;
- **apostila aprovada pelo curador em 16/08/2026**.

## Curadoria P2024-11-02 — Fantasmas do Passado Mitológico (CONCLUÍDA)

- original preservado, SHA-256 `a8ede85144c948712f094206cc0a40efd9c6dfeb4df8c43a5cd722b1cfd1d4ca`;
- 24.322 palavras na transcrição e 1.571 unidades analíticas;
- sequência aparentemente completa, com intervalo e perguntas;
- Dossiê de Pré-Curadoria concluído com 50 itens e 8 candidatos estruturais;
- riscos clínicos, científicos, históricos, políticos e fonéticos isolados;
- **concluída com sucesso na seção anterior (16/08/2026)**; devolutiva do curador incorporada;
- 8 termos novos: `RC-728–RC-735`:
  - RC-728 Fantasmas do Passado Mitológico;
  - RC-729 Jabutis Genéticos;
  - RC-730 Yggdrasil / Conglomerado dos Nove Mundos;
  - RC-731 Axis Mundi / Axismund;
  - RC-732 Invasão Ancestral do Genoma e do Psiquismo Humanos;
  - RC-733 Dominação Psíquica pela Devoção;
  - RC-734 Samudra Manthana / Batimento do Oceano de Leite;
  - RC-735 Abraço aos Fantasmas / Integridade sem Combate;
- 53 relações tipadas novas com fonte `P2024-11-02`;
- fichas criadas para os 8 termos (restauradas em 17/08/2026);
- Base, índice, XLSX e DOCX regenerados;
- apostila: Dossiê aprovado na seção anterior; produção integral 1.571/1.571 a confirmar nesta sessão (pasta com original/análises já no workspace).

## Curadoria P2024-09-29 — A Aristocracia Olimpiana e as Monarquias Terrestres

- devolutiva oficial do curador registrada em 2026-08-16;
- 6 termos novos: `RC-736–RC-741`:
  - RC-736 Aristocracia Olimpiana e Monarquias Terrestres;
  - RC-737 Projeto Amaterasu–Kami no Japão;
  - RC-738 Amaterasu (Teologia Comparada de Ellam);
  - RC-739 Susanoo (Teologia Comparada de Ellam);
  - RC-740 Kami (Projeto Japonês);
  - RC-741 Projeto Orunmilá–Olodus;
- 23 relações tipadas novas com fonte `P2024-09-29`;
- fichas dos 6 termos restauradas em 17/08/2026;
- correspondências mitológicas registradas somente como **Teologia Comparada de Ellam**;
- genealogia imperial japonesa e leituras geopolíticas mantidas fora da ontologia (quarentena);
- Base, índice, XLSX e DOCX regenerados.

## Curadoria P2024-08-03 — A Falência dos Deuses e a Destinação do Lobo

- devolutiva oficial do curador registrada em 2026-08-16;
- 13 relações tipadas novas com fonte `P2024-08-03`; termos RC-742/743/744 criados (também citados por outras fontes);
- RC-742 Falência dos Deuses; RC-743 Destinação do Lobo; RC-744 Pendências Existenciais em Realidades Paralelas;
- divergências fonéticas mantidas em `[REVISAR]` (ex.: Pularra/Prara/Pharara — sem conversão em relação canônica);
- lacuna de fala preservada como `[frase truncada]` (não preenchida com Wyrd/Urd nem outro nome);
- Base, índice, XLSX e DOCX regenerados.

## Curadoria P2024-07-14 — Consciências Espirituais Dignificadas

- devolutiva oficial do curador registrada em 2026-08-16;
- 27 relações tipadas novas com fonte `P2024-07-14`;
- RC-745 Colegiados Espirituais Humanizados criado;
- correspondências Teologia Comparada registradas (ex.: Hochmah/Sophia, Kether/Javé/Brahma);
- Base, índice, XLSX e DOCX regenerados.

## Curadoria P2024-07-13 — Reintegração Cósmica — Tempos de Ruptura

- devolutiva oficial do curador registrada em 2026-08-16;
- 20 relações tipadas novas com fonte `P2024-07-13`;
- RC-742/743/744 também citados por esta fonte;
- Base, índice, XLSX e DOCX regenerados.


## Decisão estratégica (2026-08-17) — Cenário Base-first

O curador decidiu **adiar a produção de apostilas** e priorizar o **enriquecimento da Base Terminológica** (termos + fichas + relações) a partir das palestras.

- Apostila integral (DOCX): **adiada**; produzida futuramente a pedido explícito.
- **Camadas 0–3 e segmentação U#### MANTIDAS** no fluxo — matéria-prima editorial reaproveitável para apostilas futuras.
- Leitura 2x + dossiê enxuto + devolutiva do curador: **inalterados** (qualidade inegociável).
- Entregável padrão do ciclo: relatório de enriquecimento (termos novos, relações, quarentenas, blindagens).
- Palestra **P2024-03-02 — O Drama Espiritual de Jesus**: registrada pelo curador como a última que ficou **interrompida pela metade** (não consta no índice de 17/08/2026); status a verificar quando houver material.

## Curadoria P2024-03-03 — A dessensibilização da Humanidade

- original preservado, SHA-256 `2d5ed19a1aaaf4a837231ec6835a62a2eb5358c38241a12edcb6c8ae18ebba64`;
- 83.594 bytes · ~14.051 palavras na transcrição · Sumário de 7 seções;
- devolutiva do curador (17/08/2026): compactação — **3 códigos novos + 7 absorções/mesclas + 20 ampliações**;
- 3 termos novos: `RC-746–RC-748`:
  - RC-746 Dessensibilização da Condição Humana (eixo estrutural);
  - RC-747 Vergonha de Existir;
  - RC-748 Genótipo da Gentileza (GG) — com ressalva: cronologia interna de Ellam;
- absorções: Usufruto→RC-746/049; Incômodo Luciferiano→RC-078/142/002; Insensibilidade Demo→RC-049/001; Contentamento Permanente→RC-746; Alimentação dos Deuses→RC-001; Dessensibilização dos Elétrons→RC-378/692; Frase→RC-705;
- 20 termos existentes ampliados com a fonte `P2024-03-03` (RC-529, RC-009, RC-434, RC-699, RC-705 etc.);
- 11 relações tipadas novas com fonte `P2024-03-03`;
- quarentenas confirmadas (clínico, genético, político, IA, STT duvidoso); plateia separada;
- fichas RC-746/747/748 criadas; Base, índice, XLSX e DOCX regenerados;
- apostila: **adiada** (Cenário Base-first).

## Curadoria P2024-04-13 — Moisés, as Doze Tribos e os Desígnios de Javé

- original preservado, SHA-256 `f3f35738828c2cbb1ba5596a1601afeab4f3b81498bb54d353bdb93d1ea511a8`;
- 128.662 bytes · ~21.825 palavras na transcrição · SUGESTÃO DE ÍNDICE (9 seções, 36 subseções);
- devolutiva do curador (17/08/2026): compactação severa — **2 códigos novos + 2 absorções + 33 ampliações**;
- 2 termos novos: `RC-749–RC-750`:
  - RC-749 Vício Devocional (mecanismo cármico/ético);
  - RC-750 Moisés e o Êxodo (leitura RC) — com ressalva: quarentena histórico-religiosa rígida;
- absorções: Desígnios de Javé→RC-001/RC-271; Big Data do Criador→RC-194/RC-019;
- 33 termos existentes ampliados com a fonte `P2024-04-13` (RC-001, RC-019, RC-024, RC-529, RC-580, RC-611, RC-631, RC-565, RC-683 etc.);
- 10 relações tipadas novas com fonte `P2024-04-13` (ontologia de "instrumentos");
- STT resolvidos: Rockma/Rockman→Hochmah (RC-565); "comar candã"→Kumari Kandam (RC-329);
- quarentenas confirmadas (histórico-religioso, neurobiológico, geopolítico, Sitchin/Nibiru); plateia separada;
- fichas RC-749/750 criadas; Base, índice, XLSX e DOCX regenerados;
- apostila: **adiada** (Cenário Base-first).

## Curadoria P2024-04-14 — Bagagem Intransferível — Pendências e Tendências Espirituais

- original preservado, SHA-256 `bd3963941482b93c4b68683108c48152d0734e5cf14d2f92595d11b91959119c`;
- 128.723 bytes · ~21.710 palavras na transcrição · SUGESTÃO DE ÍNDICE (11 seções, 33 subseções);
- devolutiva do curador (17/08/2026): compactação extrema — **2 códigos novos + 6 absorções + 22 ampliações**;
- 2 termos novos: `RC-751–RC-752`:
  - RC-751 Bagagem Espiritual Intransferível (termo guarda-chuva);
  - RC-752 Agenda Espiritual (expressão prática/encomenda);
- absorções: Pendências/Tendências→RC-751; Campos Morfogenéticos→RC-381 (ressalva Sheldrake); Maestria→RC-553/552; Mente Bicameral→citação; Conectomas→RC-548; Programa Encarnatório→RC-752;
- 22 termos existentes ampliados com a fonte `P2024-04-14` (RC-081/282 Mohen So "legista de Brahma", RC-063/332 Favor Divino, RC-548, RC-553, RC-381, RC-623 etc.);
- 7 relações tipadas novas com fonte `P2024-04-14`;
- STT confirmados (Moren Sor→Mohen So; Carta→Karma; Funes→Phanes);
- quarentenas confirmadas (Sheldrake, clínico, simulação, Jaynes); plateia separada (7);
- fichas RC-751/752 criadas; Base, índice, XLSX e DOCX regenerados;
- apostila: **adiada** (Cenário Base-first).

## Curadoria P2025-06-14 — A Consciência Humana e a Chave da Decifração Universal

- original preservado, SHA-256 `a61bbb23af283187de72fa7bcc9d2cc2c3dbdd63106df071740831087e542995`;
- 182.960 bytes · ~31.403 palavras na transcrição (**maior do conjunto**) · Florianópolis-SC;
- devolutiva do curador (17/08/2026): compactação rigorosa + quarentena científica — **3 códigos novos + 4 absorções + 27 ampliações**;
- 3 termos novos: `RC-753–RC-755`:
  - RC-753 Estrangulamento Cognitivo / Neural;
  - RC-754 Chave da Decifração Universal;
  - RC-755 Escola da Decifração da Realidade (Método Druídico);
- absorções: Redução Objetiva Orquestrada e Microtúbulos→quarentena científica (citação em RC-753/166); Vrittis/Chittas/Nirodha→RC-552/553; Brain Rot→RC-746;
- 27 termos existentes ampliados com a fonte `P2025-06-14` (RC-658 Wyrd/Ifá, RC-691 Ishvara, RC-665/666 Orunmilá/Obatalá, RC-712, RC-708, RC-200 etc.);
- 12 relações tipadas novas com fonte `P2025-06-14`;
- **ressalva reflexiva:** ficha RC-200 criada (não existia) com a contradição retórica "justiça divina não existe" registrada em Colecionar Incertezas;
- quarentenas confirmadas (física quântica/Penrose-Hameroff/Zizzi, brain rot como sintoma, político, psicotrônica); plateia separada (12);
- fichas RC-753/754/755 (+ RC-200) criadas; Base, índice, XLSX e DOCX regenerados;
- apostila: **adiada** (Cenário Base-first).

## Processamento P2026-08-04 — Podcast Irmãos Dias #272 (O QUE NÃO TE CONTARAM SOBRE ALIENÍGENAS E A BÍBLIA)

- original preservado, SHA-256 `bf54fba139f0c493ae528b2afecddd7a5b54254cbd27ab4b8b40b42092bed52a`;
- 96.514 bytes · ~15.978 palavras · formato **podcast/entrevista** (Irmãos Dias Podcast #272);
- devolutiva do curador (17/08/2026): **compactação absoluta — ZERO códigos novos** (material retrospectivo de esclarecimento);
- **24 ampliações** com a fonte `P2026-08-04` (RC-072 Jesus/Sophia, RC-489/672 Enoque, RC-488 Nefilins, RC-474/479 Arcontes/Belial, RC-273 Niceia, RC-096 Septuaginta, RC-005 Segundo Advento, RC-746/702 Pós-Verdade, RC-001 Javé etc.);
- **12 relações novas** (sinapses) — sem duplicatas;
- 14 fichas físicas atualizadas com a fonte;
- quarentenas aplicadas: ufológica/histórica (Roswell, MJ-12, JFK), política (Iluminismo Sombrio), teológica (Deus Pai séc. IV), clínica; falas dos apresentadores bloqueadas;
- divergência "366 manuscritos" × "363 livros" mantida em Colecionar Incertezas;
- Base, índice, XLSX e DOCX regenerados (755 termos, 1.406 relações);
- **Mapa do Buraco Negro Javé: SEGURADO** (a pedido do curador).

## Curadoria P2024-03-02 — O Drama Espiritual de Jesus

- original preservado, SHA-256 `fd1f08a18bbdda42ee60cdf100b313983211685b1615c0b7488e75140159c28b`;
- 111.154 bytes · ~18.793 palavras · ÍNDICE (9 seções, 27 subseções);
- palestra que causou timeout no fluxo anterior; arquivo termina de forma abrupta ("Amanhã eu vou") — **interrupção natural, não interpolada**; núcleo temático validado;
- devolutiva do curador (17/08/2026): compactação máxima — **1 código novo + 3 absorções/quarentenas + 25 ampliações**;
- 1 termo novo: `RC-756` Ganesha (exceção à metamorfose; cabeça de elefante; elefantes racionais);
- absorções: Drama de Jesus→RC-072 (cruzado com RC-604/RC-152); Aretalogia→quarentena/glossário (RC-414/RC-001); Adhybuta→RC-414;
- 25 termos existentes ampliados com a fonte `P2024-03-02` (RC-072 recusa da violência; RC-009 inseminação de Maria; RC-604 Fatiamento; RC-152/503; RC-414 Krishna; RC-396/730/395 Kvaser/Yggdrasil/Ragnarok etc.);
- 4 relações tipadas novas com fonte `P2024-03-02` (RC-756 ↔ Shiva/Parvathi/Fatiamento/Krishna);
- quarentenas confirmadas (JJ Benítez sem endosso; eutanásia como Teologia Comparada; cronologias de Krishna/Ragnarok em Colecionar Incertezas); plateia separada (12);
- ficha RC-756 criada; Base, índice, XLSX e DOCX regenerados (756 termos, 1.410 relações);
- apostila: **adiada** (Cenário Base-first).


## Retomada gradual de apostilas (decisão do curador, 2026-08-17)

Após o ciclo de enriquecimento Base-first (727→756 termos; 1.218→1.410 relações), o curador solicitou a **retomada da produção de apostilas** para as palestras/podcast processados nesta seção:

1. P2024-03-03 — A dessensibilização da Humanidade (RC-746–748);
2. P2024-03-02 — O Drama Espiritual de Jesus (RC-756);
3. P2024-04-13 — Moisés, as Doze Tribos e os Desígnios de Javé (RC-749–750);
4. P2024-04-14 — Bagagem Intransferível (RC-751–752);
5. P2025-06-14 — A Consciência Humana e a Chave da Decifração Universal (RC-753–755);
6. P2026-08-04 — Podcast Irmãos Dias #272 (0 códigos).

**Estratégia:** produção **incremental com piloto** — elaborar 1 apostila integral (transcrição editada ~100%, notas editoriais, glossário local com remissões RC), validar o formato com o curador e escalar uma a uma. Qualidade > velocidade (princípio inegociável).

**STATUS (2026-08-18):** ✅ Piloto (P2024-03-03 — Dessensibilização) **APROVADO** pelo curador; **6 apostilas produzidas** (todas as processadas na seção) e **arquivadas em `apostilas/CONCLUIDAS/`**;
- P2024-03-03 — A Dessensibilização da Humanidade (11 PARTES, 58 notas) — piloto aprovado;
- P2024-03-02 — O Drama Espiritual de Jesus (11 PARTES, 39 notas);
- P2024-04-13 — Moisés, as Doze Tribos e os Desígnios de Javé (9 PARTES, 34 notas);
- P2024-04-14 — Bagagem Intransferível (8 PARTES, 26 notas);
- P2025-06-14 — A Consciência Humana e a Chave da Decifração Universal (9 PARTES, 28 notas);
- P2026-08-04 — Podcast Irmãos Dias #272 (10 PARTES, 32 notas).

Cada uma em `apostilas/SLUG/Apostila - [Título].docx` (formato TOP: capa, nota do editor, TOC, PARTES roxas, citações, notas verdes, glossário A-D com remissões RC).

**Matéria-prima disponível por palestra:** `original.txt` + camadas 0–3 + leitura segmentada + dossiê + fichas + cruzamento com a Base. Builder: `ferramentas/build_apostila.py`.

## Revisão de grafias e fusão WD→Wyrd (2026-08-18)

- **Correções de grafia** na fonte canônica: `Brama`→`Brahma` (RC-505) e `Sofia`→`Sophia` (RC-474) + comentários e fichas (RC-579); `ayahuasca`→`Ayahuasca` (ficha RC-577). Verificados e já corretos: Hochmah (RC-565), Kapila (fichas), Xamanismo (RC-577/644), Vaishnava (novo).
- **Novo termo RC-757 — Vaishnavismo (vixenuísmo):** tradição hindu de adoração a Vishnu/Krishna (fato histórico-religioso) + leitura de Ellam sobre a distorção dos puranas (P2024-03-02). Ficha criada.
- **FUSÃO WD → WYRD (decisão do curador, confirmada pelo vídeo da palestra):** RC-560 (WD) **fundido em RC-658 (Wyrd/Urd)** — fontes (P2024-02-25, P2024-05-04) e relações (RC-559, RC-217, RC-628) absorvidas; RC-560 permanece como **remissão histórica** (`RC-560 —variação→ RC-658`). Revoga a orientação anterior de "não fundir sem decisão específica".
- Base regenerada: 757 termos, 1.415 relações; ficha↔Base 100%.


**DECISÃO DO CURADOR (2026-08-18) — reorganização do acervo e retomada do fluxo Base-first:**

- Criada a subpasta **`apostilas/CONCLUIDAS/`** — reúne todas as pastas de palestras/podcast **com apostila DOCX concluída** (as 6 desta seção). Cada pasta mantém `original.txt` + camadas + apostila.md + Apostila DOCX;
- **Fluxo padrão retomado:** novas palestras são processadas **somente para alimentar a Base Terminológica** (termos, relações, fichas), com a matéria-prima (original, camadas, dossiê) preservada na pasta `apostilas/YYYY-MM-DD_slug/`;
- **Apostilas:** geradas **apenas se, no futuro, for possível** — a partir do material preservado (mesmo pipeline: `apostila.md` + `build_apostila.py` → `apostilas/CONCLUIDAS/`);
- A **P2024-11-02 (Fantasmas do Passado Mitológico) foi CONCLUÍDA** em 2026-08-18: apostila integral produzida e arquivada em `apostilas/CONCLUIDAS/` — com isso, todas as palestras com material completo da seção estão com apostila.


## Pacotes de Reconstrução/Migração (gerados em 2026-08-18)

Para migração entre chats ou reconstrução após eventualidade, anexar os TXT de
`reconstrucao/pacotes/` (a plataforma aceita TXT; não aceita ZIP/MD):

| Pacote | Conteúdo | Tamanho |
|---|---|---|
| `PACOTE-DE-REGENERACAO-2026-08-18.txt` | núcleo canônico (dados_termos.py, builders, docs, guia texto, restaurador, gerador) | ~472 KB |
| `PACOTE-DE-FICHAS-2026-08-18.txt` | 335 fichas detalhadas (termos/) | ~812 KB |
| `PACOTE-DE-APOSTILAS-2026-08-18.txt` | apostila.md + ficha_ingresso.md das 7 CONCLUIDAS (regenera DOCX via build_apostila.py) | ~223 KB |
| `PACOTE-DE-ORIGINAIS-2026-08-18.txt` | original.txt das 7 CONCLUIDAS (fonte primária) | ~858 KB |
| `MANIFESTO-PACOTES-2026-08-18.txt` | estado canônico + SHA-256 de cada pacote + regra de restauração | — |

**Formato:** `===ARQ: caminho===` / `===FIM-ARQ: caminho===` (byte a byte).
**Restaurador:** `ferramentas/restaurar_pacotes.py` (v3, binário).
**Teste de integridade (2026-08-18):** 372/372 arquivos conferidos byte a byte — OK.
**Gerador:** `ferramentas/gerar_pacotes.py` (regenera os pacotes a qualquer momento).
**Observação:** XLSX/DOCX/PDF são binários e NÃO são embutidos — são regeneráveis pelos builders (índice/XLSX/DOCX) ou não canônicos (PDFs). O `GUIA-MESTRE-RC-APOSTILA.pdf` original deve ser anexado junto, se disponível (a versão texto já está no pacote de regeneração).

**HÁBITO OBRIGATÓRIO (decisão do curador, 2026-08-18):** rodar `python3 ferramentas/gerar_pacotes.py` **ao final de cada ciclo de palestra/material processado**, para atualizar o seguro com os termos, fichas e apostilas novos. O gerador embute o estado canônico mais recente e o manifesto SHA-256; o teste de integridade (byte a byte) deve ser executado após a geração.

## Processamento ART-2026-08-18 — O Quarto Cérebro de Pandora (Denise F. Silva, aluna avançada)

- **Fonte nova:** `ART-2026-08-18` (artigo de aluna avançada — fonte secundária **MUITO confiável**, com demarcação de autoria);
- 1 termo novo: `RC-758` Quarto Cérebro (enraizado em O Quarto Logos, caps. 6–9);
- 11 ampliações (RC-086, RC-287, RC-514, RC-092, RC-009, RC-166, RC-554, RC-512, RC-545, RC-553, RC-724);
- 7 relações novas; 4 absorções com demarcação ("Na leitura/interpretação do artigo ART-2026-08-18 (Denise F. Silva)...");
- fichas criadas: RC-758 + RC-086/287/514 (com seção "Interpretação secundária"); 4 fichas atualizadas;
- **quarentena de autoria:** linguagem iniciática não ontologizada; STT corrigido;
- Base regenerada: 758 termos, 1.422 relações.


## Apostilas Temáticas — "Super-Nó Semântico" (decisão estratégica, 2026-08-18)

**Aprovado pelo curador + Assistente** como a "Pedra de Roseta" do ecossistema — o elo entre banco de dados estático e tutor cognitivo ativo.

### O que é
Apostilas de estudo **temáticas** (não transcrições de palestra): narrativa integrada sobre um "buraco negro" da Base (ex.: RC-001 Javé), amarrando dezenas de termos e relações em um único documento com fio condutor, glossários temáticos e remissões RC-###.

### Por que é o auge do ecossistema
1. **Treinamento da IA (Llama 3 / RAG):** reduz "hops" de busca — a IA lê ~103 termos já amarrados em um bloco; a narrativa faz o trabalho lógico (ex.: Demência do Criador → Vício Devocional), reduzindo processamento e alucinação;
2. **Pedagogia humana (anamnese):** traduz o material fragmentado/espiralado de Ellam em linha do tempo linear e referenciada; o "fio condutor" em uma frase é pílula pedagógica de desconstrução metódica do dogma;
3. **Primeira implementação:** `pedagogico/Apostila-Estudo-Jave-Buraco-Negro.md` → DOCX "Javé: O Buraco Negro da Revelação Cósmica" (12 PARTES, ~103 termos, 34 fontes).

### Estratégia futura
- **Manter a opção em mente** — será usada em **futuro próximo, quando mais palestras estiverem agregadas à KB**;
- Novos candidatos naturais: Sophia (RC-009), Moros (RC-454), Jesus (RC-072), Pandora (RC-086);
- As apostilas temáticas de `pedagogico/` são **regeneráveis** e já incluídas no `PACOTE-DE-APOSTILAS` dos pacotes de reconstrução.

## Curadoria P2024-02-03 — O Jainismo e o Druidismo Ancestrais

- original preservado, SHA-256 `8b8ae3bab6fba86a82766925bb1f4c2d455a6fe663eb377dd546a7f22b2c356f`;
- 139.510 bytes · ~23.053 palavras · índice estruturado (9 seções);
- devolutiva do curador (18/08/2026): compactação brutal — **2 códigos novos + 3 absorções + 17 ampliações** (Base detectou 111 termos pré-existentes — recorde);
- 2 termos novos: `RC-759` Jainismo (antigo Druidismo) e `RC-760` Vrittis e Cittas;
- absorções: Tirthankaras→RC-397; Karma-substância/Nirjara→RC-559/658; Tuatha/Relíquias→RC-398;
- 17 termos existentes ampliados (RC-755 Método Druídico, RC-618 Moksha, RC-398, RC-559, RC-658 etc.);
- 11 relações tipadas novas (conexão Tirthankaras/Jainismo/Método Druídico);
- quarentenas confirmadas (Mohenjo-Daro nuclear, cittas=transtornos como metáfora, Kardec druida, cronologia jainista); plateia separada (12);
- fichas RC-759/760 criadas; Base, índice, XLSX e DOCX regenerados (760 termos, 1.433 relações);
- apostila: **adiada** (Cenário Base-first).

## Prioridade de retomada

### 1. P2024-11-02 — produção da apostila integral

O Dossiê foi aprovado e os termos (RC-728–735) incorporados na seção anterior. Produzir a apostila integral de 1.571/1.571 unidades a partir do material já presente em `apostilas/2024-11-02_fantasmas_passado_mitologico/`, com locutores separados e intervenções da plateia isoladas.

### 2. Próximas palestras (fora do índice de apostilas concluídas)

As palestras conhecidas do Guia (Setianos Emancipados, Jesus e a Dinastia das Sophias) aguardam material-fonte.

### 3. Recuperação do retorno do intervalo de P2025-03-15

A apostila disponível foi aprovada. Se o restante da gravação/transcrição for localizado, preservar o novo original e executar pré-curadoria complementar antes de declarar a palestra integral.

### 4. Faces de Javé

Recuperar o `apostila.md` já corrigido e rodar `build_apostila.py`. A grafia canônica é **Hochmah — RC-565**, não “Rockman/Rochman”.

## Alertas canônicos

- Não editar diretamente a planilha XLSX.
- Não alterar códigos RC já atribuídos.
- Não promover candidatos sem curadoria.
- Fontes B071–B073 são compilações de IA: servem apenas para mineração, não para citação.
- B061 é fonte secundária de transcrições automáticas: usar como pista, não como fonte primária.
- Preservar divergências documentadas, em vez de escolher arbitrariamente uma data ou versão.


**Correção de engenharia (2026-08-18, 2ª) — MANIFESTO-PACOTES dinâmico:** auditoria técnica revelou que o `MANIFESTO-PACOTES-2026-08-18.txt` externo exibia estado canônico **HARDCODED** (757 termos / 1.415 relações / próximo RC-758 / "P2024-11-02 CONCLUÍDA") — congelado num checkpoint antigo, enquanto a Base já estava em 765 termos. Causa raiz: `gerar_pacotes.py` tinha as contagens fixas no código-fonte do manifesto. **Correção:** o gerador agora **computa dinamicamente** o estado canônico (termos, relações, fichas, próximo código, apostilas) a partir de `dados_termos.py` e do diretório `termos/`. Pacotes regenerados e verificados: **409/409 arquivos fiéis (pacote == manifesto interno == workspace)**; novo manifesto correto (765 termos / 1.492 relações / próximo RC-766 / 7 apostilas).

---

## Auditoria Apostila(7) — restauração + regeneração de artefatos (2026-08-19)

- **Restauração (Fonte A — GitHub):** token do curador via variável de ambiente (nunca em arquivo); clone `institutocura-maker/Termos-RC` (commit `954d309`, branch `main`) → materializado em `/home/user/rc-terminologia` (729 arquivos; sem `.git`, sem `reconstrucao/` — por design do espelhamento).
- **Validação:** `OK: 767 termos, 1531 relações — dados válidos.` · SHA-256 `dados_termos.py` = `7a95c8dd…d69d028ac` (idêntico ao Guia v1.1). Nenhum código consumido (próximo: **RC-768**).
- **Artefatos regenerados (conferência autorizada pelo curador):**
  - `indice-mestre.md` — 767 linhas; SHA-256 `652519f1…` **byte-idêntico** ao checkpoint 08-18;
  - `base-terminologica.xlsx` — 7 abas (Índice 767 · Fichas 377 · Relações 1531 · Bibliografia 79 · Categorias 40+1 · Status · Como usar);
  - `base-terminologica-leitura.docx` — 767 termos / 1531 relações / 79 obras / 378 fichas; **cobertura 767/767 códigos** (parágrafos + tabelas).
- **Determinismo dos builders:** prova com 2ª geração → diff interno dos ZIPs: única diferença `docProps/core.xml` (timestamp). DOCX idêntico inclusive no core.xml. Builders inalterados desde o checkpoint (`7c95fdf`). Diferença vs 18/08 é só metadado de data (XLSX: created/modified; DOCX: linha "Gerado em 19/08/2026" por design, `build_word.py` L204).
- **Spot-check de grafias canônicas (XLSX + DOCX):** Brahma RC-037 · Tikun RC-514 · Sophia RC-009 · Nefilins RC-488 · Ialdabaoth RC-482 · Olm RC-092 · Elm RC-454 · Adhy RC-011 (ser) / RC-310 (Adhy que caiu) · Javé RC-001 · Vishnu RC-135 · Xamanismo RC-577 · Wyrd/Urd RC-658 (RC-560 remissão) · Hochmah RC-565 · Vaishnavismo RC-757 · Kapila (ocorre em B076/B078) — **todos OK, sem divergências**.
- **Sem edições de dados.** Base inalterada; pacotes regenerados abaixo (hábito obrigatório).

---

## Ciclo de Curadoria P2026-07-25 — Jesus e a Dinastia das Sophias (19/08/2026)

**Primeira palestra do ciclo Apostila(7) — "prova de fogo".** Material-fonte fornecido pelo curador (TXT "2026-25-07"); dossiê e devolutiva completos no mesmo dia.

### Devolutiva do curador (via Assistente, 19/08/2026) — integral
- **D-1:** fonte canônica **P2026-07-25** (data declarada na fala: "hoje, dia 25 de julho do ano 2026"); índices corrigidos (P2025-07-25 → P2026-07-25).
- **D-2:** aprovados **RC-768** (Princípio da Externalização), **RC-769** (Corpos Fenvã), **RC-770** (Hipóstase dos Arcontes); rejeitados com absorção: Cisne Negro → RC-192 (+nota RC-702); Evangelho de Bartolomeu/500 Passos → RC-072 (cruzando RC-647); Hades/Reides → RC-286 (cruzando RC-074).
- **D-3:** "Wert" é desvio fonético — unificado exclusivamente como **Wyrd (RC-658)**.
- **D-4:** 10 subordinados absorvidos (Navalha de Ockham) — sem códigos novos.
- **D-5:** **B080 Perversa Gratidão** cadastrada na BIBLIO (edição manual, sem tocar em outras entradas).
- **D-6:** bloco de ~40 ampliações aprovado integralmente.
- **D-7:** quarentenas estritas (clínico/científico/geopolítico/ufológico/teológico/STT).
- **D-8:** plateia isolada (7 perguntas finais) — sem ontologia.

### Execução
- Base: **770 termos · 1.604 relações** (+3 termos, +73 relações) — `OK: 770 termos, 1604 relações — dados válidos.`
- Fichas: **14 criadas** (RC-768/769/770 + RC-286 Tártaro, RC-494 Dinastia das Sophias, RC-495 Arabot-Ráquia/Shekinah/Merkabah, RC-482 Ialdabaoth, RC-479 Belial, RC-565 Hochmah, RC-530 Pistis Sophia, RC-485 Classes de anjos, RC-477 Ensá, RC-480 Indra, RC-518 Genoma Derivado) e **40 ampliadas** (seção "Ampliação — P2026-07-25").
- Artefatos regenerados: índice (770), XLSX (7 abas; 80 obras), DOCX (770/1604/80/392).
- Backup pré-ciclo: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-768-770.py` (`7a95c8dd…`).
- Próximo código disponível: **RC-771**.
- **Pendência:** apostila integral (Ciclo de Apostilas em Lote) — aguardando acúmulo/gatilho do curador.

---

## Ciclo de Apostilas — P2026-07-25 Jesus e a Dinastia das Sophias (19/08/2026)

**Primeira apostila integral desta sessão (Apostila(7)).** Autorizada pelo curador ("vamos em frente com a geração da Apostila MD + DOCX e concluí-la").

- `apostila.md` — transcrição editada integral no formato TOP: capa (metadados @), Nota do editor, **12 PARTES** temáticas + seção de perguntas da plateia isolada (PARTE XII) + **Glossário local A–D** com remissões RC (18.855 palavras; 458 parágrafos no DOCX).
- Cobertura: 100% da macroestrutura real (16 blocos → 12 PARTES); citações literais editadas (grafias canônicas com nota na 1ª ocorrência; [REVISAR] preservados nos STTs duvidosos; marcadores orais/humor/digressões preservados).
- DOCX gerado via `build_apostila.py` (identidade visual roxa padrão, TOC Word com updateFields).
- Pasta renomeada para a data canônica **`2026-07-25_jesus_dinastia_sophias_arcontes`** e movida para `apostilas/CONCLUIDAS/` (D-1: data 2026).
- Índices sincronizados (raiz + `apostilas/INDICE-PALESTRAS.md`).
- **Total: 14 apostilas concluídas** em `apostilas/CONCLUIDAS/`.
- Próximos passos (orientação do curador): processar mais palestras → atualizar a base → gerar apostilas **em lote**.

---

## APROVAÇÃO OFICIAL (19/08/2026) — P2026-07-25 e Fluxo completo

**Curador:** "Podemos considerar a Apostila APROVADA!!! ... bem como todo o Fluxo que realizamos até aqui. PARABÉNS!!!"

- Apostila P2026-07-25 (MD + DOCX) **APROVADA**;
- Fluxo integral (Base-first → Devolutiva → Base → Apostila → pacotes → GitHub) **validado pelo curador**;
- Registros: `DECISAO-DO-CURADOR.md` e `RELATORIO-DE-CICLO.md` na pasta da palestra em `apostilas/CONCLUIDAS/2026-07-25_jesus_dinastia_sophias_arcontes/analise/`;
- Estado canônico: **770 termos · 1.604 relações · RC-771 livre · 392 fichas · 80 obras · 14 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2024-02-25 As Faces de Javé / O Senhor Parameshthi (19/08/2026)

**Re-curadoria** (TXT recuperado — estava "material-fonte ausente"). Devolutiva F-1..F-7 do curador (via Assistente): auditoria aprovada; 8 fichas criadas; bloco de ampliações aprovado; **zero códigos novos** (Navalha de Ockham — base congelada em 770); quarentenas confirmadas; apostila autorizada.

### Execução
- Auditoria RC-556–RC-565 contra o STT original: **todos confirmados** (a sessão anterior acertou o núcleo).
- **8 fichas físicas criadas:** RC-556 (Senhor Parameshthi), RC-557 (Conectoma), RC-558 (Sensação de eu), RC-560 (WD→remissão Wyrd), RC-561 (Faces de Javé), RC-562 (Baralho genético), RC-563 (Travas e lacres), RC-564 (Fios soltos).
- **19 fichas ampliadas** (seção "Ampliação — P2024-02-25"): RC-001, RC-009, RC-072, RC-074, RC-104, RC-166, RC-192, RC-414, RC-437, RC-454, RC-518, RC-533(?), RC-559, RC-585, RC-614, RC-658, RC-684, RC-702, RC-722, RC-732 (19 confirmadas).
- **29 relações novas** com fonte P2024-02-25; 13 campos "relacionados" enriquecidos.
- Base: **770 termos · 1.633 relações** (+29) — `OK: 770 termos, 1633 relações — dados válidos.` · RC-771 preservado.
- Artefatos regenerados: índice (770), XLSX (80 obras), DOCX (770/1633/80/**400 fichas**).
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-FACES-JAVE.py`.

### Colecionar Incertezas — KESHAVA (rubrica FECHADA)
- **STT "avatares quechava/quechadas" (P2024-02-25) = avatares Keshava** — evidência que confirma a pista do curador ("quachadas/quechada" = Keshava). Veto estrito mantido: nenhuma grafia fonética virou termo; nós oficiais RC-073 (Keshava) e RC-425 (Krishna como pretenso Keshava) mantidos. *Rubrica encerrada como confirmada.*

### Apostila (15ª do acervo)
- `apostila.md` (10.434 palavras; 12 PARTES + glossário A–D; **sem seção de plateia** — autor encerrou sem perguntas); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2024-02-25_faces_jave_parameshthi/`.
- Índices sincronizados (raiz + apostilas/).

**Estado:** 770 termos · 1.633 relações · RC-771 livre · 400 fichas · 80 obras · **15 apostilas concluídas**.

---

## Correção de engenharia (2026-08-19, 3ª) — sincronização GitHub: duplicata órfã removida

**Problema (apontado pelo curador):** no GitHub havia `apostilas/2025-07-25_jesus_dinastia_sophias_arcontes/` (estado da curadoria, antes da renomeação canônica para `2026-07-25` + CONCLUIDAS) além da pasta canônica em `CONCLUIDAS/` — duplicata órfã.

**Causa raiz:** o método de sincronização `cp -a /home/user/rc-terminologia/. <clone>` **não remove** do working tree do clone os arquivos que deixaram de existir no workspace; o `git add -A` então não registrava remoções, e arquivos/pastas antigos permaneciam no repo.

**Correção aplicada:** `git rm -r apostilas/2025-07-25_jesus_dinastia_sophias_arcontes` → commit `6a67b77` → push. Auditoria completa (git ls-files × workspace): nenhuma outra órfã real (os "ORFAO" de `termos/RC-572/657/706` e `.docx` eram falsos positivos de escaping de nomes com caracteres especiais).

**Procedimento novo de sincronização (a partir de agora):**
```bash
cd /tmp && rm -rf Termos-RC && git clone https://x-access-token:${GH_TOKEN}@github.com/institutocura-maker/Termos-RC.git
cd Termos-RC
find . -mindepth 1 ! -name '.git' -exec rm -rf {} +     # LIMPAR working tree (novo passo)
cp -a /home/user/rc-terminologia/. .
rm -rf reconstrucao base-terminologica.xlsx base-terminologica-leitura.docx __pycache__
git checkout HEAD -- .gitignore
git add -A && git commit -m "..." && git push origin main
```
Com o working tree limpo antes do `cp`, o `git add -A` detecta corretamente remoções e renomeações.

---

## Ciclo de Curadoria + Apostila — P2025-05-31 O Mistério da Árvore da Vida e a Urdidura de Metatron (19/08/2026)

**Re-curadoria** (TXT recuperado). Devolutiva M-1..M-6 do curador (via Assistente): auditoria aprovada; bloco de ampliações aprovado; **zero códigos novos** (base congelada em 770); absorções Orlog/Norns aprovadas; apostila autorizada; quarentenas confirmadas ("a Arca mapeia a estrutura da Revelação, não o noticiário").

### Execução
- Auditoria RC-671–RC-689 contra o STT: **19/19 confirmados** (a sessão anterior acertou integralmente — base "madura").
- **7 fichas materializadas:** RC-467 (Moiras/Nornes/Parcas — Urd/Verdandi/Skuld), RC-262 (Daath), RC-266 (Zohar/Shimon bar Yochai), RC-267 (Isaac Luria), RC-005 (Segundo Advento), RC-329 (Kumari Kandan), RC-490 (Caim).
- **29 fichas ampliadas** (seção "Ampliação — P2025-05-31"): destaques — **Malkuth = Hochmah/Sophia** (consolidação canônica); **Otz Chim = planilha de Enoque**; **Enoque "se suicidou" dentro de Metatron** [REVISAR]; **Orlog = Moros** (RC-454); **Norns → RC-467**; Wyrd como computador quântico (RC-658); inseminação de Maria (B004); transfiguração (RC-366); Corpos Átmico/Búdico/Manásico (RC-623–625); Trishna/Avidya (RC-712); Igigi (RC-580).
- **41 relações novas** com fonte P2025-05-31; 13 campos relacionados enriquecidos.
- Base: **770 termos · 1.674 relações** (+41) — `OK: 770 termos, 1674 relações — dados válidos.` · RC-771 preservado.
- Artefatos regenerados: índice (770), XLSX (80 obras), DOCX (770/1674/80/**407 fichas**).
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-ARVORE-VIDA.py`.

### Colecionar Incertezas (itens novos)
"Vatireca" [STT]; "Lammur" (Marte); "Ig Brasil" (reino do Ragnarok); "Anahata/Pashupati"; "Enoque se suicidou dentro de Metatron" [REVISAR]; "25.869 × 28.869 genes"; "Hochmah filho de Chokhmah"; "Sóclov" (Sokolov); "Vasir" (urdidura de Moros).

### Apostila (16ª do acervo)
- `apostila.md` (13.979 palavras; 12 PARTES + glossário A–D; **PARTE XI — Perguntas da Plateia isolada** com 8 intervenções nomeadas e mediador Guilherme Veríssimo); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2025-05-31_arvore_da_vida_urdidura_metatron/`.
- Índices sincronizados (raiz + apostilas/).

**Estado:** 770 termos · 1.674 relações · RC-771 livre · 407 fichas · 80 obras · **16 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2025-03-15 A Rebelião dos Elétrons e a era do Colapso do Caos Organizado (19/08/2026)

**Re-curadoria** (TXT completo recuperado — antes "fonte oficialmente incompleta"). Devolutiva R-1..R-6 do curador (via Assistente): auditoria aprovada; 24 ampliações aprovadas; **zero códigos novos** (base em 770); B063 confirmado; apostila autorizada; **quarentena clínica ABSOLUTA** (homoafetividade/gênero = cosmologia filosófica do autor, jamais fato).

### Execução
- Auditoria RC-690–693 + RC-378 contra o STT integral: **5/5 confirmados** (+ ~60 ampliações anteriores do fragmento coerentes).
- **27 fichas ampliadas** (seção "Ampliação — P2025-03-15"): destaques — **Ishvara = "retrato de Prabrajna"** (RC-691); **mecânica da assinatura quântica/kit reencarnatório** (RC-692); **Wyrd gerada FORA da geopolítica da Trimurti + oposição de Krishna** (RC-658/RC-559); "cansaço da matéria" (RC-378); Schopenhauer/B063 (RC-161); Paraíso B (RC-612); oxitocina/IA (RC-646).
- 4 termos sem ficha física (RC-406, RC-529, RC-542, RC-191) → ampliação registrada na Colecionar Incertezas (sem ficha criada, conforme "nenhuma nova ficha").
- **32 relações novas**; 15 campos relacionados enriquecidos.
- Base: **770 termos · 1.706 relações** (+32) — `OK: 770 termos, 1706 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-REBELIAO-ELETRONS.py`.

### Colecionar Incertezas (itens novos)
"Acabou em fevereiro desse ano [2025]" [REVISAR]; "Vatireca" [STT]; "25.869 × 28.869 genes"; experimentos militares/Polo Sul (não verificáveis); "Sha Howard"→Schopenhauer (B063 confirmado); "10 milhões de IAs".

### Apostila (17ª do acervo)
- `apostila.md` (10.713 palavras; 12 PARTES + glossário A–D; nota editorial com **quarentena clínica absoluta** explícita; seção de perguntas finais marcada como [TEXTO INCOMPLETO] — material recebido cobre até o intervalo); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2025-03-15_rebeliao_eletrons_caos_organizado/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.706 relações · RC-771 livre · 407 fichas · 80 obras · **17 apostilas concluídas**.
