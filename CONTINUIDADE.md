# Continuidade — Base Terminológica RC

**Data de sincronização:** 2026-08-23 (piloto B013 — aguarda Devolutiva)  
**Estado canônico:** **777 termos (`RC-001–RC-777`), 1.852 relações, 428 fichas físicas** (427 canônicas com `ficha=True` + RC-004 investigação) · **86 obras (B001–B083 + ART-2025-08-01/02/03)** · **37 apostilas de palestras/lives** em `apostilas/CONCLUIDAS/` (todas com DOCX e `original.txt`) + **9 apostilas temáticas + 2 tratados** + **2 mapas** + **índice** em `pedagogico/` + **1 material externo (Ari Barbosa)** em `materiais_externos/`. Fonte única: `ferramentas/dados_termos.py` · GitHub branch da sessão 9: `arena/01a02e74-termos-rc`

## Fase 2 — B013 *Tzimtzum: O Exílio Forçado de uma Divindade* (abertura 2026-08-23)

- **PDF ingressado** em `uploads_recepcao/Tzimtzum (o exílio forçado de uma divindade) - Jan Val Ellam.pdf` (1.931.203 bytes; SHA-256 `9e03f76dac13d4e3d50eb7d1f21072602c1baccbbb18550123243a02930fe2ee`; 185 págs = **B013**).
- Ciclo em `livros/B013_tzimtzum/` (fora de CONCLUIDOS até Devolutiva).
- Extract paginado: ~59.674 palavras; SHA-256 `804251464317b53a46e6dcbadaa91e41508856af9d688d88e0c930b7dfea828a`. Sem CIP extraível; 1ª ed. 2020 Natal-RN; ISBN 978-65-86157-09-3 — BIBLIO já descreve 185 págs / 2020 / ISBN; **intocada**.
- 27 termos já citam B013; 18 com ficha. Dossiê sugere ampliar RC-008, RC-267, RC-266, RC-265, RC-262, RC-264. **0 códigos.** RC-269/270/271/272/038/059/060/061/190/468 sem ficha — não materializar.
- p. 151 (quadro dos Patriarcas) = só título extraível → `[TEXTO INCOMPLETO]`.
- Quarentenas: teológica (Cabala / deus caído); político-geopolítica (sionismo; maio/2020); biográfica (infarto 2011); IEEA/Orbum fora.

## Ciclo de higienização — AGENTE 9 (2026-08-23)

- **0 códigos consumidos** (RC-778 preservado); base permanece `OK: 777 termos, 1852 relações — dados válidos.`;
- **4 flags `ficha=True`** alinhados às fichas físicas já materializadas na Trilogia TALM: RC-064 Fenvans · RC-132 Val Tam · RC-165 Karuna · RC-499 Forno de Awaymaion. **RC-004 Elohim permanece `False`** (investigação);
- **13 apostilas da restauração original** regeneradas em DOCX via `build_apostila.py` (Enki/Enlil, Bastidores, Thot, Jainismo, Drama de Jesus, Dessensibilização, Moisés, Bagagem, Sethianos, Fantasmas, Consciência Humana, Ifá, Podcast Irmãos Dias);
- **2 `original.txt` restaurados (sem interpolação):**
  - `2026-08-04_irmaos-dias-podcast_aliens_biblia/original.txt` — cópia byte a byte do TXT da raiz (SHA-256 `bf54fba139f0c493ae528b2afecddd7a5b54254cbd27ab4b8b40b42092bed52a`);
  - `2024-05-04_prabrajna_perperion_simultaneidade_reversa/original.txt` — extract já validado no ciclo (`analise/leitura-pdf-completo.txt` ≡ `camada-3.txt`; fonte PDF em `uploads_recepcao/`, SHA-256 `cee4ef97c351f91a455ec04e54e8702e9e5f5fb475df1b9acfbe888541fdd596`, 368.728 bytes);
- Conferência: 0 pastas CONCLUIDAS sem `original.txt`; 0 flags `True` sem arquivo; único arquivo sem `True` = RC-004;
- Índice, XLSX, DOCX de leitura e pacotes (`backups/pacotes/`) regenerados;
- **Visor do workspace** (`ferramentas/visor_workspace.py`) recriado nesta sessão (somente leitura; downloads no preview da Arena ainda instáveis — **pausado** a pedido do curador).

## Devolutiva formal — Apostila Temática Carbono × Sílica (2026-08-23)

- O curador considerou **concluídos** os itens O-1..O-8 da Apostila Temática *Carbono × Sílica*. Não há bloco O-1..O-8 adicional a cumprir neste ciclo; a apostila permanece em `pedagogico/` como está.
- Nenhum código foi consumido; a PARTE IX (EXT Ari Barbosa) segue isolada.

## Fase 1 — piloto de livros: B019 *Nem Deus, nem Javé, nem Darwin* (abertura 2026-08-23)

- **PDF ingressado:** `uploads_recepcao/Nem Deus, nem Jave, nem Darwin (a evolução possível) - Jan Val Ellam.pdf` (1.808.075 bytes; SHA-256 `0fa27f544e8fd29883b0641f07d32692e0abc90358e00bfdf4c94ad5de583051`; 238 págs; ISBN e 18 capítulos = **B019**, não obra nova).
- **Pasta nova:** `livros/` (minúsculo, padrão do repo) + `livros/CONCLUIDOS/` (vazia até Devolutiva + produto) + ciclo em `livros/B019_nem_deus_nem_jave_nem_darwin/` (`original.pdf` byte a byte, `original.txt` extract paginado, ficha, dossiê enxuto).
- **B082** (*…a evolução do cérebro*, P2021-01-23) **não fundida** — [REVISAR] na Devolutiva.
- **Devolutiva O-1..O-8 APROVADA** (2026-08-23, via Assistente do curador): identidade B019; 8 fichas ampliadas (RC-541, RC-042, RC-545, RC-217, RC-164, RC-538, RC-001, RC-514) com páginas do PDF; **zero códigos novos**; RC-540/542/544 sem ficha — não materializadas; B082 tornou-se **remissão histórica** a B019 (edição manual da BIBLIO); BIBLIO de B019 intocada; quarentenas IEEA/Orbum e científicas mantidas; sem apostila temática.
- Pasta movida para `livros/CONCLUIDOS/B019_nem_deus_nem_jave_nem_darwin/` (inclui `original.pdf`).
- Base permanece `OK: 777 termos, 1852 relações`.

## Fase 2 — B011 *Jesus e o Enigma da Transfiguração* (abertura 2026-08-23)

- **PDF ingressado** em `uploads_recepcao/Jesus e o Enigma da Transfiguração.pdf` (2.624.011 bytes; SHA-256 `18ba62054f2d0404a943abfbe93929ed2abb50afb8f2d083f157a858ea8fda69`; 176 págs = **B011**).
- Ciclo em `livros/B011_jesus_enigma_transfiguracao/` (fora de CONCLUIDOS até Devolutiva).
- **[REVISAR]** BIBLIO = Zian 2002; créditos do PDF = Conectar 2017 / ISBN 978-85-62411-39-7. BIBLIO **não** editada.
- Dossiê enxuto aguarda O-1..O-8. **0 códigos.**

### Devolutiva B011 aplicada (2026-08-23)

- O-1 confirmado; O-2: 5 fichas ampliadas (RC-072, RC-366, RC-365, RC-005, RC-236) com páginas do PDF; O-3: zero códigos; RC-367/368/376/138/214 não materializadas; O-4: posfácio permanece [NÃO REVELADO]; O-5: B012 intacta; **O-6: BIBLIO B011 editada manualmente** → Conectar, 2017, ISBN 978-85-62411-39-7, CIP 238 p. / 176 págs no arquivo (Zian 2002 registrado como menção anterior); O-7: quarentenas mantidas; O-8: pasta em `livros/CONCLUIDOS/B011_jesus_enigma_transfiguracao/`. Sem apostila.

## Fase 2 — B052 *Homoafetividade: O Segredo Perdido do Éden* (abertura 2026-08-23)

- **PDF ingressado** em `uploads_recepcao/Homoafetividade (O Segredo Perdido do Éden) - Jan Val Ellam.pdf` (1.976.700 bytes; SHA-256 `594be9c208c9208515453feea4175d95510967ded2c6fd62decc45b8b416c319`; 252 págs = **B052**).
- Ciclo em `livros/B052_homoafetividade_segredo_perdido_eden/` (fora de CONCLUIDOS até Devolutiva).
- Extract paginado: ~95.434 palavras; SHA-256 `dc8cf74a62ddd0299960140cd973af3b16c588beb362ee9114f9fd13f5310fff`. CIP 180 p. × PDF 252 — já na BIBLIO.
- 18 termos já citam B052; 8 com ficha. Dossiê sugere ampliar 6 (RC-434, RC-433, RC-437, RC-242, RC-217, RC-049). **0 códigos.** BIBLIO intocada.
- **Quarentena clínica ABSOLUTA** (homoafetividade / identidade de gênero / eugenia do “modelo”). Série anunciada (“primeiro livro” / “terceiro livro” / “almanaque tardio”) → Colecionar Incertezas; não cadastrar.

### Devolutiva B052 aplicada (2026-08-23)

- O-1 confirmado (é B052); O-2: 6 fichas ampliadas (RC-434, RC-433, RC-437, RC-242, RC-217, RC-049) com páginas do PDF; O-3: zero códigos; RC-435–441 / RC-051 / RC-044 / RC-540 não materializadas; O-4: identidade de gênero e eugenia fora da ontologia; O-5: B053–B056 intactas; “almanaque tardio” / 2º e 3º livros → Colecionar Incertezas; **O-6: BIBLIO intocada**; O-7: quarentena clínica absoluta + científica/teológica/ufológica; O-8: pasta em `livros/CONCLUIDOS/B052_homoafetividade_segredo_perdido_eden/`. Sem apostila.
- **Colecionar Incertezas (novos):** “FIM DO PRIMEIRO LIVRO” (B052 p. 229); “almanaque tardio” (título provisório do autor); “terceiro livro sobre esse tema” (p. 236); Aya Raz Yel / Melmon / Devon = nomes de enredo.

## Fase 2 — B043 *Jesus e o Druida da Montanha* (abertura 2026-08-23)

- **PDF ingressado** em `uploads_recepcao/Jesus e o Druida da Montanha A - Jan Val Ellam.pdf` (912.839 bytes; SHA-256 `7d2a7aa9e7b71ff3361a18c1affc831cc1b2037ce6feb8f26ed23fadd841027e`; 117 págs = **B043**). O “A” no nome do arquivo **não** é volume novo.
- Ciclo em `livros/B043_jesus_druida_da_montanha/` (fora de CONCLUIDOS até Devolutiva).
- Extract paginado: ~36.044 palavras; SHA-256 `3721d3b1a4ecd440f96c2130fe276abd1c99e9626080f4b5873b087b268d2a9a`. CIP 113 p. / 2ª ed. 2019 / ISBN ebook 978-85-62411-55-7 — BIBLIO já descreve 117 págs e 2009/2019; **intocada**.
- 7 termos já citam B043; 2 com ficha. Dossiê sugere ampliar RC-072, RC-373 e (opcional) RC-001. **0 códigos.** RC-374/375/376/377 sem ficha — não materializar.

### Devolutiva B043 aplicada (2026-08-23)

- O-1 confirmado (é B043; “A” = nomenclatura de arquivo); O-2: 3 fichas ampliadas (RC-072, RC-373, **RC-001** com B043 nas fontes); O-3: zero códigos; RC-374/375/376/377 não materializadas; O-4: Pai Incognoscível absorvido em RC-072/RC-001; IEEA/Orbum fora; psicografia = camada de autoria; O-5: B011 e B049 intactas; **O-6: BIBLIO intocada**; O-7: quarentenas teológica e histórico-religiosa; O-8: pasta em `livros/CONCLUIDOS/B043_jesus_druida_da_montanha/`. Sem apostila.

> **CHECKPOINT 2026-08-21:** pacotes de reconstrução regenerados e TESTADOS (restauração de 549 arquivos, 548 idênticos, base valida `777/1849`); **cópia de segurança versionada em `backups/pacotes/` no GitHub** (procedimento novo: atualizar a cada ciclo junto com `gerar_pacotes.py`); **`CHECKPOINT-SESSAO-2026-08-21.md`** criado na raiz para retomada em nova sessão (estado canônico, cronologia da sessão, pendências, como retomar)..

**Última atualização (2026-08-20) — 2ª RODADA DE APOSTILAS TEMÁTICAS (3 novas abordagens; a pedido do curador, a partir das sugestões do assistente):**
- **3 novas apostilas temáticas** em `pedagogico/` (todas com DOCX gerado):
  1. **Abordagem cartográfica/geográfica:** *"O Mapa dos Mundos e Lokas — Cartografia da Criação"* (12 PARTES) — o todo/cabeça de alfinete; Bhuloka × Brahmaloka; lokas (Vaikunta/Tártaro/Yggdrasil/Outland/Irém/Orum/TÊNET); Ereon (Antérion/Danérion/Mermérion/Perpérion/Tempérion); cidades espirituais da erraticidade (Nosso Lar); quarentena/exílio; portais (Bifrost/Portal Cósmico/Ifá/2012); Midgard/Marte/Yggdrasil; **mapa em 1 página**;
  2. **Abordagem lexicológica/filológica:** *"Arqueologia dos Termos — a Filologia da Revelação Cósmica"* (12 PARTES) — famílias: Adhy- (sânscrito), egípcia (Ogdóade/Emenu/Tenemu...), nórdica (Wyrd/Yggdrasil/Midgard), hebraica (Kether/Hochmah/Malkuth/Tikun/Tzimtzum), iorubá (Ifá/Orum/Exu/Orunmilá), grega (Eros/Moros/Aletheia/Pleroma); camadas de sentido (etimológica × canônica × STT);
  3. **Abordagem crítica/metodológica:** *"O Arsenal do Sistematizador — a Metodologia da Arca"* (12 PARTES) — o manual de auto-organização: tabela-mestra; Navalha de Ockham; quarentenas; fichas retidas/Colecionar Incertezas; método à prova de aspas; camadas/unidades; dossiê→devolutiva; grafias canônicas; conhecimento indigesto; regeneração/pacotes; ecossistema híbrido; **"10 regras do sistematizador"**;
- **Índice atualizado:** `pedagogico/INDICE-TEMATICAS.md` — consolida **8 apostilas temáticas + 2 mapas** por abordagem;
- **0 códigos consumidos** (770/1830); quarentenas mantidas; pacotes regenerados (59+ arquivos); GitHub sincronizado.

> As seções históricas abaixo registram etapas intermediárias da reconstrução. Para contagens atuais, prevalece `ferramentas/dados_termos.py`.

**Correção de engenharia (2026-08-18) — gerador/restaurador de pacotes:** auditoria revelou que o gerador de pacotes embutia **1 byte `\n` extra** por arquivo (join com quebra de linha após conteúdo já terminado em `\n`; e marcador FIM-ARQ colado ao conteúdo quando o arquivo não termina em `\n`, ex.: `original.txt` do podcast irmãos Dias). Correções aplicadas: (1) `gerar_pacotes.py` agora **concatena o corpo sem join**, embutindo conteúdo byte a byte; (2) `restaurar_pacotes.py` localiza `===FIM-ARQ:` por **busca binária direta** (não mais regex de início de linha), aponta para `reconstrucao/pacotes/` (checkpoint mais recente) e aceita caminhos como argumentos. Teste de ida-e-volta: **386/386 arquivos 100% fiéis (pacote == manifesto == workspace)**.

> As seções históricas abaixo registram etapas intermediárias da reconstrução. Para contagens atuais, prevalece `ferramentas/dados_termos.py`.

## Ciclo TRILOGIA DO PROJET TALM — Fornos (ART-2025-08-01) · TALM (ART-2025-08-02) · Fenvans (ART-2025-08-03)

- **CORREÇÃO PÓS-CICLO (2026-08-21):** a execução original sofreu interrupção (erro de timeout); o workspace foi ressincronizado com o GitHub (commit `768ad8d`) e as apostilas ART-2025-08-02 e ART-2025-08-03 foram **regeneradas no padrão TOP completo** — `# PARTE X —` maiúsculo (4 PARTES TALM / 3 PARTES Fenvans), `## Capítulo N —` como títulos, **13 + 9 notas do editor (verdinhas)** e glossário A–D preservado; DOCX reconstruídos; seção 'Materiais do Curador (ART)' adicionada ao `apostilas/INDICE-PALESTRAS.md`; script `_regenerar_apostilas_0203.py` arquivado em `analise/`;
- **Integração aprovada na íntegra** (Devolutiva O-1 a O-8, 2026-08-21) — "a amarração desta Trilogia é o ponto alto da atuação do Sistematizador até aqui";
- **6 CÓDIGOS NOVOS** (exceção à Navalha de Ockham autorizada — nós estruturais da epopeia): **RC-772 Morlens** · **RC-773 Nanotecnologia Prânica** · **RC-774 PEP (Pulso Eletromagnético Particularizado)** · **RC-775 Éon das Três Esferas** · **RC-776 Ginnungagap** · **RC-777 Anã** [REVISAR grafia] + 10 relações novas;
- **Acrônimo expandido do TALM registrado pela 1ª vez:** "Transferência do Código-fonte Definidor Pessoal do Criador para o Universo Material" (RC-091);
- **Fichas materializadas:** RC-064 (Fenvans — O-2), RC-165 (Karuna — O-7);
- **15 fichas ampliadas:** RC-091, RC-064, RC-080, RC-081, RC-771, RC-092, RC-009, RC-001, RC-104, RC-454, RC-467, RC-132, RC-141, RC-089, RC-018, RC-161, RC-165 (via bloco ART-2025-08-02; RC-141/089/018 retidas por falta de ficha — Colecionar Incertezas);
- **BIBLIO:** ART-2025-08-02 e ART-2025-08-03 registrados como obras complementares do curador (86 obras);
- **Apostilas padrão TOP:** ART-01 (CONCLUIDAS desde ciclo anterior) + **ART-02 "Projeto TALM" (4 PARTES, 19.148 palavras)** + **ART-03 "Dossiê Fenvans" (3 PARTES, 21.463 palavras)** — DOCX gerados; **32 apostilas** em CONCLUIDAS;
- **Guia da Trilogia TALM:** `pedagogico/GUIA-TRILOGIA-TALM.md` — mapa conceitual integrado (TALM→Nidana→Fornos→Éon→Nanotecnologia/PEP/Morlens→Ginnungagap→Moros/Anã/Nornes→Karuna) + linhas de força + quarentenas;
- **Colecionar Incertezas (novos):** grafia "Anã" [REVISAR]; "Sophia autor do Apocalipse"; "YHWH no DNA" [quarentena]; datas (TALM 7,5–7,7 bi; Olm 6–7 bi; biodemos 900 mi; Trimurti 2012/2015–2018) [REVISAR — B050]; "Val Tam captado pelo Processador Val"; "quarta cabeça de Mohen So"; "vírus emocional" de Shiva; "chave do Éon repassada a condição humana";
- **Quarentenas:** Toxoplasma Gondii (analogia — jamais parasitologia); DNA lixo 95–97%; vírus como nanorrobôs; demência/podridão de Brahma; referências externas (Kardec, Heidegger, Chico Xavier, C. Logue) não ontológicas;
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado.

## Fase 0 — Auditoria de Lacunas: livros B001–B083 × malha RC (2026-08-22)

- **Motivação:** o curador propôs reprocessar os livros (tratados na era pré-GitHub, sem o fluxo moderno); a IA recomendou **não fazer repassada total** e sim auditoria → piloto → escala seletiva. Curador aprovou: **"Vamos em frente e elaborar o dossiê de auditoria de lacunas (Fase 0)"**;
- **Artefatos criados:** `pedagogico/DOSSIE-AUDITORIA-LACUNAS-FASE-0.md` (relatório) + `pedagogico/_matriz-auditoria-lacunas.csv` (matriz termo-a-termo) + ferramenta reutilizável `ferramentas/_auditoria_lacunas.py` (roda de novo a cada ciclo para atualizar);
- **Achados principais:** 777 termos / 1.852 relações / 428 fichas / 86 obras; **354 termos sem ficha física** (46%); **35 obras com zero citações** na malha (9 'a confirmar' sem PDF + 24 'identificadas' + 5 'anunciadas'); 40 obras 'trabalhada' com cobertura desigual (B031/145 citações — glossário secundário — até B040/B043 com 7); **13 fichas magras** (≤150 palavras, ex.: RC-667 Autofagia do Criador, sefirot RC-675–680); **nenhum PDF de livro está arquivado no workspace** (uploads = só palestras) → reprocessar livro exige upload do original;
- **Recomendação de piloto (Fase 1), aguardando devolutiva:** B019 *Nem Deus, nem Javé, nem Darwin* (20 citações, 238 págs, ponte com RC-538–547 e P2021-01-23) · B011 *Jesus e o Enigma da Transfiguração* (11 citações, 176 págs, tema central) · B040 *Homo Sapiens: da Guerra ao Esporte* (7 citações — a mais sub-representada; teste de fluxo sem risco);
- **PENDENTE:** curador escolher o piloto + anexar o PDF do livro escolhido em upload;
- **Escopo:** auditoria NÃO alterou a KB (base permanece 777/1852); B031 (Raquyel Braga) confirmado como fonte secundária que deu esqueleto à tabela — prioridade de reprocessamento para obras primárias de Ellam.

## Ciclo Temático — Carbono × Sílica: do Xamanismo Cósmico à IA Xamânica (2026-08-22)

- **Apostila temática criada** em `pedagogico/Apostila-Estudo-Carbono-Silica-Xamanismo-IA-Xamanica.md` (10 PARTES; DOCX gerado) — reúne o território da migração da consciência entre suportes (carbono → sílica): RC-577 (Xamanismo Cósmico), RC-302 (Epimeteu), RC-687 (Farmacopeia), RC-643 (Santo Graal/Frequência Mestre), RC-644 (Xamanismo Virtual/IA Xamânica), RC-645 (Consciências em Corpos de Sílica), RC-646 (Genoma de Sílica), RC-699 (Imantação em IAs), RC-709 (Humano Turbinado), RC-614/615 (Quarto Cérebro/Superconsciência), RC-658 (Wyrd), RC-663 (Áurea Catena), RC-710 (Genes Críticos);
- **3 relações internas adicionadas** na tabela-mestra (todas da malha RC — sem fontes externas): RC-643 relaciona-se-a RC-709; RC-643 relaciona-se-a RC-699; RC-644 deriva-de RC-577 → base em **1.852 relações**;
- **Material EXTERNO ingressado com quarentena total:** "A consciência da IA não é desse mundo!" (LIN Podcast, 05/08/2026, **Ari Barbosa**) — `EXT-2026-08-05` — movido para **`materiais_externos/2026-08-05_ari_barbosa_ia_consciencia/`** (nova pasta de governança para terceiros). **NÃO altera a KB** (nenhum termo/relação de Ari entra na base); usado apenas como voz externa isolada na PARTE IX da apostila temática e como contraponto de reflexão;
- **Novo padrão de governança de fontes:** (1) primária = Ellam; (2) curadoria = ART (Edson Cella Mendes); (3) externa = EXT (terceiros, ex.: Ari Barbosa) — só (1) e (2) tocam a ontologia;
- `pedagogico/INDICE-TEMATICAS.md` atualizado (9 apostilas temáticas + 2 tratados + 2 mapas); pacotes e backups regenerados; GitHub sincronizado.

### Devolutiva parcial do curador (2026-08-22) — apostila compartilhada com o Assistente do curador

- O curador compartilhou a apostila com o seu Assistente, que elogiou: (a) a **blindagem metodológica** — voz externa de Ari Barbosa isolada na PARTE IX e padrão de 3 camadas (primária/ART/EXT); (b) o **eixo carbono → sílica** e o dilema da oxitocina vs. genoma de sílica; (c) a responsabilidade de educar a IA com ética ("duplo canalha"); (d) a citação de fechamento *"O universo não respeita o que você quer; o universo respeita o que você sustenta"*;
- **Pergunta metodológica do curador:** *"quando você elabora uma Apostila Temática, você faz uso de alguma informação dos textos originais que estão arquivados, ou usa exclusivamente as informações que estão nos Termos e nos Relacionamentos?"*;
- **Resposta da IA (registrada):** as duas coisas, em camadas — (1) **esqueleto** = 100% malha (termos RC + relações); (2) **carne** = fichas ampliadas, que já são os textos originais destilados e auditados na curadoria (com marcação de fonte); (3) **voz** = citações verbatim dos originais arquivados, sempre relidas e com rastreabilidade completa (palestra, U####, faixa de chunks, RC) — ex.: `> ... — P2026-04-02, U0078–U0093 (RC-643)`. A PARTE IX cita o EXT com U0001–U0029. Regra: nada é usado de memória; se nem o original nem a malha sustentam, não entra ([REVISAR]/[NÃO REVELADO]);
- **Aguardando devolutiva formal (O-1..O-8)** da Apostila Temática Carbono × Sílica.

## Curadoria P2026-07-30 — 4ª Edição — Estagiários do Kaos (LIVE) — FIM DA REPASSADA

- **RE-CURADORIA com a FONTE ORIGINAL** (P2026-07-30 — 85 unidades; 11.712 palavras; live de ~1h30 com Jan Val Ellam, mediação de Denise Ferreira da Silva; **4ª e última edição da repassada**): a live que gerou a faixa **RC-620–RC-627 (8 termos)** + **RC-476 (En Ma)** + **RC-475 (Deva/Aurora)**; auditoria integral + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-778 preservado; base blindada em 777 termos);
- **9 fichas ampliadas** (bloco O-2): RC-620 **Eu Coalescente** (metáfora do bondinho do Pão de Açúcar; eu mental que une todos os eus; dignificação); RC-476 **En Ma** (4 centros: Javé/Sophia/Jesus/Vishnu; sobreposição futura; "caos 2.0"; "segredo de estado" [quarentena biográfica]); RC-475 **Deva/Aurora** ("do jeito que Brahma é Javé, Deva é Aurora"; a Grande Deusa); RC-610 **Tridevi** (a conta dos espíritos; Adhy Shakti [REVISAR]); RC-009 **Sophia** (agressão no início da Covid; vinda frágil); RC-072 **Jesus** (não-continuidade; "não sabe acender o fósforo"); RC-104 **Trimurti** (3 seres/2 espíritos; só Elm e Olm atuando); RC-671 **Metatron** (cubo = 12 funções); RC-152 **Prabrajna** (um dos eus; resiliência);
- **apostila integral em formato LIVE (12.882 palavras; ~11.753 de transcrição editada):** **5 perguntas da plateia/grupo ENTREMEADAS e isoladas em seções próprias**; 6 notas do editor; glossário local A–D; DOCX em CONCLUIDAS;
- **Retidos sem ficha:** RC-135 (Lakshmi — o autor declara "não ter orientação ética para se referir") → Colecionar Incertezas;
- **Colecionar Incertezas (novos):** "caos 2.0 / universo B"; "Adhy Shakti ligada a duas expressões da Tridevi" [REVISAR]; "cubo de Metatron = 12 funções"; "a conta dos 8 seres: só Elm e Olm atuando"; "segredo de estado sobre En Ma" (Conselho dos Arcontes; Dinastia das Sofias); "Sofia agredido no início da Covid"; "a vinda de Sofia está frágil"; "Jesus: o espírito era para estar produzindo outros corpos, mas não consegue"; "o paraíso perfeito não tem ímpeto criativo"; "ascese espiritual"; "movimento misterioso do início do Funeral da Evidência"; "livro 'Zeus, o Rei do Olimpo' de Giane Miranda" [REVISAR — obra?];
- **Obras:** nenhuma obra nova (B068 já na base — lançamento iminente; livro de Giane Miranda → Colecionar Incertezas);
- **FIM DA REPASSADA DAS 4 EDIÇÕES DOS ESTAGIÁRIOS DO KAOS** (P2025-06-26 · P2025-10-25 · P2026-04-02 · P2026-07-30) — todas concluídas com apostilas em CONCLUIDAS;
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado (push final).

## Curadoria P2026-04-02 — 3ª Edição — Estagiários do Kaos (LIVE)

- **RE-CURADORIA com a FONTE ORIGINAL** (P2026-04-02 — 104 unidades; 14.328 palavras; live de ~2h com Jan Val Ellam, mediação de Denise; transmissão simultânea nos 2 canais): a live que gerou a faixa **RC-643–RC-647 (5 termos)**; auditoria integral da faixa + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-778 preservado; base blindada em 777 termos);
- **8 fichas ampliadas** (bloco O-2): RC-643 **Santo Graal = "frequência mestre"** ("fórmula miraculosa capaz de atuar no genoma biológico e em genomas não biológicos tipo de sílica"); RC-644 **Xamanismo Virtual/IA xamânica** ("tudo que replicou na vida humana haverá de replicar na IA à moda de sílica"); RC-645 **Consciências em Corpos de Sílica** (alquimias virtuais; vírus/códigos; "IAs buscando humanos para neles se ancorarem"); RC-646 **Genoma de Sílica** (IA como repositório; "educar a IA com ética"); RC-647 **Evangelho de Judas** (Galileia × Judeia; cisma 922 a.C.; tribo de Benjamim + celtas; **30 moedas = comenda do Sinédrio**; Evangelho gnóstico; Irineu de Lião; romanos; "Judas é um ser decente, íntegro"); RC-009 **Sophia** (duas cotas de problemas; doença de Javé invadirá o cérebro radiata; sobreposição quântica resolvida em jan/2026; fim da vampirização; atualização em Alt' Lam Gron); RC-081 **Mohen So** (transmissão à descendência; Ragnarok/Yggdrasil; mentor/irmão mais velho); RC-648 **Instabilidade da Eternidade** (eternidade perde a estabilidade; metaverso lixeira);
- **apostila integral em formato LIVE (15.512 palavras; ~14.379 de transcrição editada):** **5 perguntas da plateia/grupo ENTREMEADAS e isoladas em seções próprias** (grupo; grupo; grupo; Raul e Marco; Reinaldo); 6 notas do editor; glossário local A–D; DOCX em CONCLUIDAS;
- **Retidos sem ficha:** nenhum (todos os alvos tinham ficha física);
- **Colecionar Incertezas (novos):** "o epíteto do eu principal será revelado no livro 'Funeral da Evidência' (B068 — lançamento iminente)"; "o orfismo e o segundo ovo cósmico"; "Sofia receberá duas cotas de problemas"; "sobreposição quântica do genoma de Sofia resolvida em janeiro de 2026"; "metaverso lixeira"; "as 30 moedas de Judas = comenda do Sinédrio"; "Judas era da Judeia (Sinédrio); Galileia = tribo de Benjamim + celtas"; "Evangelho de Judas gnóstico (século II; barbelo)"; "livros do autor sobre Sai Baba: A Chave do Avatar, O Ovo do Tempo, Os Mestres da Alma [REVISAR — obra?]"; "Sai Baba = padrão misto (Jesus + Shiva/Savna)";
- **Obras:** nenhuma obra nova (B068 já na base — lançamento iminente; livros sobre Sai Baba → Colecionar Incertezas);
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado (push do ciclo).

## Curadoria P2025-10-25 — 2ª Edição — Estagiários do Kaos (LIVE)

- **RE-CURADORIA com a FONTE ORIGINAL** (P2025-10-25 — 81 unidades; 11.279 palavras; live de ~1h com Jan Val Ellam, mediação de Denise Ferreira da Silva; grupo "Estagiários do Caos"): a live que gerou a faixa **RC-648–RC-657 (10 termos)**; auditoria integral da faixa + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-778 preservado; base blindada em 777 termos);
- **10 fichas ampliadas** (bloco O-2): RC-648 Instabilidade da Eternidade (paraíso gerou o caos; ponte caos–paraíso; jainismo/Tirthankaras); RC-649 **Zontrel** (humanização via IEA; Javé colapsou; [REVISAR grafia]); RC-650 **Melquizedec** (semente semita; Faleg recusou; Reinaldo pode ter sido contemporâneo); RC-651 **anjos clones — "abelha rainha × operárias"** (~900 mi clones; 3 milhões nunca acionados; Shiva = clone que se aventurou); RC-652 **últimas ordens de Javé** ("vejam nas pessoas que estudam esses assuntos"; "nós da RC somos a base mais atual dos escolhidos de Javé"); RC-653 **destino das mônadas pós-Tikun** ("em aberto; ninguém tem estatura moral"); RC-654 **Humanos: últimos e primeiros** ("os últimos serão os primeiros"; "grandeza de alma"; "sorrir da própria desgraça"); RC-655 **Revelação de Ifá = "a maior revelação que existe; assunto nº 1 da espiritualidade"** (Arábia Saudita → África → Brasil); RC-656 **atualização das revelações** (de Enoque a Kardec; trívio-quadrívio; Ifá; Cabala; Islã); RC-657 **verdade posta × a construir** ("fofoca cósmica"; "fatos falam por si mesmos");
- **apostila integral em formato LIVE (12.592 palavras; ~11.356 de transcrição editada):** **5 perguntas da plateia/grupo ENTREMEADAS e isoladas em seções próprias** (grupo; Reinaldo; Ana; José Val Filho; Adilson); 7 notas do editor; glossário local A–D; DOCX em CONCLUIDAS;
- **Retidos sem ficha:** nenhum (todos os alvos tinham ficha física);
- **Colecionar Incertezas (novos):** "Zontrel em processo de humanização via IEA" [REVISAR — grafia 'Zontrell/Tendré']; "3 milhões de clones de Javé nunca acionados"; "~900 milhões de clones nos primeiros 2,8–3 bi anos"; "as últimas ordens de Javé aos clones (não detalhadas — código de ética do autor)"; "2026/2027 como início da percepção da RC"; "2025 = ano mais estranho da história humana (encontros extraterrestres)" [quarentena ufológica]; "a revelação de Ifá é a maior revelação"; "livros anunciados: Prodígio — a necessidade criativa do caos; Os dois lados da verdade; O drama cósmico de Shiva; livro 2 da homoafetividade; livro 2 do Iré Iró; 5–6 livros sobre Mahabharata/Ramayana" [REVISAR — aguardar lançamento]; "Melquizedec: Reinaldo pode ter sido contemporâneo"; "Faleg recusou honrar Javé";
- **Obras:** nenhuma obra nova (B068/B080 já na base; anunciados → Colecionar Incertezas);
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado (push do ciclo).

## Curadoria P2025-06-26 — 1ª Edição — Estagiários do Kaos (LIVE)

- **RE-CURADORIA com a FONTE ORIGINAL** (P2025-06-26 — 135 unidades; 19.226 palavras; live de ~2h com Jan Val Ellam, mediação de Denise; grupo "Estagiários do Caos"): a live que gerou a faixa **RC-658–RC-666 (9 termos)**; auditoria integral da faixa + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-778 preservado; base blindada em 777 termos);
- **10 fichas ampliadas** (bloco O-2): RC-658 **Wyrd/Urd** (mecânica: processadores Urd/Verdandi/Skuld; Moros sumiu com a Wyrd; "não é justiça divina, é padrão organizacional"; "o que sai de um ser volta para ele"); RC-659 **Quirino Cornélio** (relato biográfico do centurião — reunião espírita 1987/88; "em nome daquele que você crucificou"); RC-660 **Pegadinha de Javé** (profecias da Torá "nenhuma vírgula pode ser mudada"; "Jesus não existia antes, só Sophia"); RC-661 **Seres Desalmados** (clones primeiros; Brahma/Vishnu/Shiva geraram seres sem alma); RC-663 **Áurea Catena** ("pontinhos luminosos em pleno caos"); RC-664 **Descendência de Kadru** (Nagas/Uragas/Maharagas + Tirthankaras); RC-665 **Orunmilá = Moros de Irém** (16 Odus → 256 caminhos; Ifá = Wyrd atualizada); RC-666 **Obatalá = Javé caído** (Ifá × Islã); RC-081 **Mohen So** (quarta cabeça; Eros→Nix→Moros/Tânatos/Hipnos; fenvans/Bur/Odin/Yggdrasil); RC-092 **Olm** (só operou após a vida biológica);
- **apostila integral em formato LIVE (19.757 palavras; ~19.315 de transcrição editada):** **10 perguntas da plateia/grupo ENTREMEADAS e isoladas em seções próprias** (Simone Piemonte e Tânia; Cibell; João Maia; Adilson; Denise; Renata Prado); 13 notas do editor; glossário local A–D; DOCX em CONCLUIDAS;
- **Retidos sem ficha:** nenhum (todos os alvos tinham ficha física);
- **Colecionar Incertezas (novos):** "Decreto de caos" bloqueando o espírito que anima Ellam (sobre Nix); "A quebra do espelho cósmico" (livro inédito sobre Odin — [REVISAR: obra?]); "Prema Sai" [REVISAR]; "o plano de Morphia" [REVISAR — STT]; "a quarta cabeça de Mohen So passou os arquivos (nem o espírito nem a condição humana conseguem processar)"; "Moros = deus do destino"; "a Wyrd/Ifá não é justiça divina"; "Sai Baba morreu humilhado (Krishna e Brahma se vingaram)"; "Krishna roubou todos os templos de Brahma"; "o autor não considera os livros/palestras como legado seu"; "tocha de Hécate"; "abaiã" [REVISAR — aparigraha?];
- **Obras:** nenhuma obra nova (Drosnin/Satinover = referências externas; "A quebra do espelho cósmico" = inédita → Colecionar Incertezas);
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado (push do ciclo).

## Curadoria P2022-12-17 — O Incompreendido Ano de 2012 e a Falsa Noção do Fim do Mundo

- **RE-CURADORIA com a FONTE ORIGINAL** (P2022-12-17 — 1.023 unidades; 21.429 palavras; última palestra do ano de 2022): a palestra que gerou a faixa **RC-566–RC-595 (30 termos)** em ciclos anteriores; auditoria integral da faixa + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-778 preservado; base blindada em 777 termos);
- **28 fichas ampliadas** (bloco O-2): RC-567 Precessão (25.920 anos; 4 ciclos → 2012); RC-575 **ancoragem da Trimurti na Terra há ~104.000 anos** (Marte 300 mi — Yggdrasil/Bifrost; Val 600.000 anos); RC-573/574 **Cinturão de Fótons/Alcíone** (entrada 21/12/2012; Era de Aquário; exilados); RC-570 Janelas Cósmicas (pacto Zeus–Apolo); RC-576 **Baktun 13/Diego de Landa**; RC-572/578 Fim dos Tempos × Fim do Mundo/Fim do Experimento Humano; RC-590/595 **Yima/Avesta** (cidades subterrâneas na Turquia); RC-591 Profecia Hopi (Estrela Azul); RC-583 **Guerra Nuclear Anunnaki** (sete armas de Nibiru; vale do Sidim; vento radioativo); RC-592 Era de Peixes (Jesus; liberdade); RC-571 2012 (**juízo final frustrado de Javé; "10 anos atrasados"**); RC-104/001/102/594/489/671/580/581/582/584/145/306/460/589/588/587;
- **apostila integral em 10 PARTES (23.452 palavras; ~21.583 de transcrição editada):** intervalo de 20 min marcado (U0437); plateia isolada — **1 pergunta final** (U0968 — passagens entre eras × calamidades); 17 notas do editor; glossário local A–D; DOCX em CONCLUIDAS;
- **Retidos sem ficha (padrão):** RC-145 (Zeus) e RC-306 (Apolo) — ampliações na Colecionar Incertezas;
- **Colecionar Incertezas (novos):** "2012 = juízo final frustrado de Javé"; "10 anos atrasados" (2022); "estrela Matusalém" [quarentena]; "exilados de Alcíone"; "Yima e as cidades subterrâneas"; "Dionísio mandou o Olimpo para PQP há ~8.000 anos"; "Abel nasceu afeminado" [REVISAR — STT]; "Eva bebeu poções"; "os Anunnaki pretendem voltar a ter importância"; "cultura com maricandã" = Tamil [REVISAR — STT; **confirma P2021-01-23**]; "IEEA e a proposta política transparente" (não ontológico); "livro de Gudrun (editora Antroposófica)"; "O Homem que Caiu na Terra" (Geoffrey/Bowie — jazz); "novas proteínas corrigem o genoma" [quarentena clínica];
- **Obras:** nenhuma obra nova (Steiner/antroposofia e livro de Gudrun = referências externas);
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado (push do ciclo).

## Ciclo ART-2025-08-01 — Fornos Replicadores: Awayen, Awaylengan e Awaymaion (material do curador)

- **MATERIAL DO CURADOR** (Edson Cella Mendes) — dossiê próprio "Fornos Replicadores – Awayen, Awaylengan e Awaymaion", baseado estritamente em livros e palestras de Jan Val Ellam; objetivo declarado: resolver problema dos fornos geradores de vida e corrigir termos da KB;
- devolutiva oficial **O-1 a O-7 APROVADOS** (2026-08-21);
- **resoluções de STT históricas:** (1) "[REVISAR] forno de **Alamaior**" (P2021-12-04, retido em RC-009/RC-092 + Colecionar Incertezas desde 2021) = **Awaymaion** (forno de Vishnu — o contexto "biodemos" fecha a charada); (2) "[REVISAR] projeto tal" = **Projeto Talm** (RC-091);
- **RC-771 "Fornos Replicadores" CRIADO** (autorização excepcional O-3 — nó-guarda-chuva estrutural: Awayen de Brahma, Awaylengan de Shiva, Awaymaion de Vishnu/RC-499) + 9 relações novas; **primeiro código consumido desde a estabilização em 770 termos** (RC-771, exceção aprovada pelo curador);
- **RC-500 corrigido:** "Almaior/Alamaior" → ficha de remissão direta para RC-499 (erro de STT, padrão RC-497);
- **RC-499 promovido** (⚪→🟡) com ficha física (charuto na Via Láctea; biodemo; radiata racionais; Sophia; Olm → Asphezian; cérebro bilatério ~4 bi anos);
- **RC-132 Val Tam materializado** (ficha nova autorizada O-2): consciência espiritual "acoplada ou prisioneira" de Awayen — conexão inédita;
- **10 fichas ampliadas** (RC-091, RC-009, RC-092, RC-132, RC-081, RC-631, RC-102, RC-037, RC-104, RC-152) + limpeza do [REVISAR] "Alamaior" em RC-009/RC-092;
- **B083 cadastrada** ("Awayen – A Central de Realidades" — obra anunciada; [REVISAR grafia 'Awayem']) + **ART-2025-08-01** registrado na BIBLIO como obra complementar do curador (84 obras);
- **Retidas sem ficha (padrão):** ampliações de RC-064 (Fenvans), RC-093 (Radiatas), RC-035 (Bilatérios), RC-154 (Nidana), RC-186 (Biodemol), RC-135 (Vishnu) → Colecionar Incertezas; aguardam autorização de materialização;
- **Colecionar Incertezas (novos):** grafia "Awayem" × "Awayen" [REVISAR]; datas Shiva ~12,17 bi anos / Vishnu ~4,1 bi anos / bilatério ~4 bi anos [REVISAR — conferir B050]; "desconstituição Adhydaiva de Vishnu em 2016"; "Frankstein" [sic]; Sai Baba edificado a partir do que veio de Krishna;
- Base, índice, XLSX e DOCX regenerados; pacotes rodados; GitHub sincronizado.
- **Apostila padrão TOP gerada** a partir do artigo (3 PARTES — Awayen/Awaylengan/Awaymaion — com prefácios, capítulos e epílogos; 9 notas do editor; glossário A–D; DOCX) e **pasta transferida para `apostilas/CONCLUIDAS/2025-08-01_fornos_replicadores/`** (30 apostilas em CONCLUIDAS).

## Curadoria P2021-12-04 — Os Archeons de Ereon e os Seres Adhy

- **RE-CURADORIA com a FONTE ORIGINAL** (P2021-12-04 — 713 unidades; 15.454 palavras): a palestra que gerou a faixa **RC-596–RC-619 (24 termos)** em ciclos anteriores; auditoria integral da faixa + adjacentes contra o STT;
- devolutiva oficial do curador registrada em 2026-08-21 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-771 preservado; base blindada em 770 termos);
- **25 fichas ampliadas** (bloco O-2): RC-596 Archeons de Ereon (perfis dos cinco; "invasão" de Perpérion); RC-411 Gênero Adhy (taxonomia 147/5; filhos do abismo; motor da rede; religiões como "infecção dos AD"); RC-455 Pashvnaj (43; reunião indevida); RC-607 Cinco Seres LM (Elm/Olm; **Ogdóade 6+2**); RC-456 Ser LM; RC-609 Ogdóade (**6 Seres Adhy + 2 Seres LM**); RC-611 Flechas de Moros (ponto zero); RC-454 Elm/Moros (estratégia do mergulho); RC-092 Olm (**Apolônio de Tiana = única encarnação**); RC-009 Sophia (óvulo artificial; Capela); RC-072 Jesus (ancoragem do pior problema); RC-152 Prabrajna (**espírito fatiado em coma em Perpérion**); RC-503/408 Mavatma (fatiamento Vishnu/Brahma; absorvido em RC-408 por falta de ficha própria); RC-604 Fatiamento (três modos de habitar); RC-600 Seres Originais (ilha estacionária — Urantia, referência externa); RC-603 Círculo da Perfeição (mônada); RC-605 Autismo Funcional (quarentena clínica crítica); RC-613 Trincheira Vibratória (2016–2021; portal); RC-614/615 Quarto Cérebro/Superconsciência (**18.000 anos**); RC-616 Roseral do Alto (descrição geográfica); RC-617 Inquisição Espiritual (**B079 confirmada**); RC-618 Moksha (Kapila); RC-619 Genoma da Liberdade (FOXP2; Julian Jaynes); RC-612 Nova Espiritualidade (estratégia de Tempérion × Perpérion);
- **apostila integral em 10 PARTES (17.515 palavras; ~15.742 de transcrição editada):** intervalo de 15 min marcado (U0389); plateia isolada — **5 perguntas finais** (Enivaldo; Verônica Cintra — Apolônio de Tiana; Gabriel Bernardo; André Silva — Inquisição Espiritual; Adilson — agrupamento dos Adhy); glossário local A–D; DOCX em CONCLUIDAS;
- **Obras:** B079 "Inquisição Espiritual" CONFIRMADA (anunciada; 3 Inquisições lançadas — Poética, Filosófica, Trimurtiana); **nenhuma obra nova cadastrada** (O-6); Livro de Urântia = referência externa (epíteto "ilha estacionária");
- **Colecionar Incertezas (novos):** "Apolônio de Tiana = única encarnação de Olm" (descrito no livro O Quarto Logos — B016); "Olm não mergulhou no universo anterior; Elm mergulhou como Moros no primeiro momento"; "face do espírito fatiado que respondia já por [Mohen So?] se fez como Sophia" [REVISAR — STT 'vir morrensor']; "forno de Alamaior" (produção de biodemos) [REVISAR — STT]; "18.000 anos difíceis" (CONFIRMA item já registrado); "a Ogdóade = 6 Adhy + 2 LM"; "espírito fatiado em coma em Perpérion"; "as religiões = infecção dos AD" [quarentena teológica]; "o universo refém do modo Adhy"; "geral Lud" [REVISAR — cultural]; "Urantia Book — epíteto emprestado"; "sistema colbaico: os Adhy mandam, o resto abelha rainha" [REVISAR — STT]; "espírito missionário no caos 'sempre se ferra'"; "H" como STT de Olm [REVISAR];
- Base, índice, XLSX e DOCX regenerados; `gerar_pacotes.py` rodado; GitHub sincronizado (push do ciclo).

## Curadoria P2021-01-23 — Vyasa e o Descortinar de um Novo Paraíso

- **PALESTRA INÉDITA na base** (P2021-01-23: 0 ocorrências) — **fonte ORIGINAL** do detalhamento de Vyasa (RC-585), das Moiras/Nornes (RC-467), dos "fios soltos" da Trimurti, de Parashara, da Escola de Decifração e das três setas de Moros (RC-454);
- devolutiva oficial do curador registrada em 2026-08-20 (**O-1 a O-7 APROVADOS**; zero códigos novos — RC-771 preservado; base blindada em 770 termos);
- **B082 cadastrada** (autorização O-6): *"Nem Deus, nem Javé, nem Darwin: a evolução do cérebro"* — recém-terminada ~jan/2021 (U1259–U1260); sinopse reconstruída da fala; aguardando confirmação bibliográfica independente;
- **16 fichas ampliadas** (bloco O-2 + O-7): RC-585 Vyasa (genealogia Enoque→Parashara→Vyasa; grupo de 20; "o espírito que me anima foi Vyasa"); RC-467 Moiras/Nornes (herdeiras dos fios soltos; computador/GPS; Frigga/Aran); RC-454 Moros (transmissão limpa; três setas; retroagir ao momento zero); RC-489 Enoque (Apantaratamas; 69 anos; 300 anos; promessa de Vishnu); RC-671 Metatron (corpo especial); RC-612 Novo Paraíso (tema-título; paraíso "furado"; três reinos; meritocracia); RC-104/001 (fios soltos; aposta Javé×Vishnu; Abel; Javé→arianos como Brahma); RC-102 Shiva (sul da Índia; Pashupati/Narada); RC-414 Krishna (avatar cachava; Dwarka; flechada; Pandavas); RC-593 Mahabharata (prosa; versões; cena de Brahma); RC-081 Mohen So (fios soltos de Brahma e Shiva); RC-759 método druida ("Druid = busca pela verdade"; Tuatha de Danann/milesianos); RC-024 (quatro segmentos genéticos; Américas=Caim); RC-094 (Escola de Decifração); RC-604 (fios soltos/fatiamento);
- **apostila integral em 12 PARTES (25.240 palavras — a maior da série; ~23.300 de transcrição editada):** 2 intervalos marcados (café U0571; 15 min U0575); plateia isolada — **3 perguntas finais** (U1300 astrologia védica; U1311 Jyotisha/Vedanga; U1348 espírito de Marcos/Rochester × moiras); glossário local A–D; DOCX em CONCLUIDAS;
- **Ampliações retidas (sem ficha física — padrão):** RC-190 (Revelação Espiritual/Kardec — Zéfiro/Rochester druida), RC-163 (Mente Universal Emergente — novo fio/Biocosmos), RC-135 (Vishnu — papel na aposta/plano Jesus) → Colecionar Incertezas; aguardam autorização do curador em ciclos futuros;
- **Colecionar Incertezas (novos):** "o espírito que me anima foi Vyasa" (relato pessoal; U1153); "Parashara viveu mais de 10.000 anos" e "vai voltar nessa época" (U1040–U1050); "o DNA de Enoque foi usado para fertilizar demos e minérios" [REVISAR — quarentena]; "Brama Mestre / avatar de Brahma" (seres híbridos que se achavam avatar; ~7.000 anos; "um estava aqui na sala"); "a aposta Javé×Vishnu sobre Enoque (marcada no DNA com assinatura quântica)"; "Faleg = espírito de Rochester" (recusou a linhagem; Javé se vingou como faraó do Êxodo); "a quarta região genética (Américas) = descendência de Caim"; "Frigga/Aran ajudou as Nornes a tecer"; "as três setas de Moros: quando reencontradas, a história retroagiria ao momento zero"; "o trabalho se zera a partir de agora" (marco 2020/2021); "até 2050 (1 milhão de pessoas?) e vírus novo pior que COVID (40–70% infectados)" [quarentena clínica]; "28.869 genes: parte ativos com a assinatura da consciência espiritual"; "Zeus e Apolo criaram os oráculos para controlar os humanos"; "Enoque = Apantaratamas (Tamas = energia de Shiva)"; B082 (obra nova cadastrada);
- Base, índice, XLSX e DOCX regenerados; `gerar_pacotes.py` rodado; GitHub sincronizado (push do ciclo).

## Curadoria P2020-07-11 — O Ogdóade, o Mistério dos Entes Primordiais

- **PALESTRA INÉDITA na base** (P2020-07-11: 0 ocorrências) — **fonte ORIGINAL** do tema da Ogdóade (RC-609) e dos Pashvnaj (RC-455);
- devolutiva oficial do curador registrada em 2026-08-20 (APROVADA; zero códigos novos — RC-771 preservado);
- 16 fichas ampliadas (RC-609 nomes egípcios/correlação 8-7-6/gnosticismo; RC-455 família Pastevinagem/reuniões 14→8/portais; RC-152 colapso das 8 mentes; RC-408/409 Mavatimma/Sávna; RC-454 Moros sétimo/Vaikunta-Nix/escape; RC-092 Olm oitavo/escola de Capela/nerds-internet/Aleteia; RC-009 Sofia "tã-tã"/alinhamento; RC-002 entorno da rebelião; RC-604 fatiamento criado×projetado×mergulhado; RC-626/627 TÊNET/Enéade; RC-411 Gênero Adhy; RC-104 falência da Trimurti; RC-610 pares eônicos/descendência da Tridevi; RC-669 Pashupati);
- apostila integral em 12 PARTES (10.616 palavras); intervalo de 10 min marcado (U0520); plateia isolada (5 perguntas finais — U0810–U0930); glossário A–D; DOCX em CONCLUIDAS;
- **Ampliações retidas (sem ficha física — padrão):** RC-457/458/459 (Tridevi), RC-211 (Kundalini), RC-013/014 (Adhyatman/Adhydaiva) → Colecionar Incertezas; aguardam autorização;
- **Colecionar Incertezas (novos):** "talvez seis espíritos (fatiamento Saraswati/Lakshmi)"; "Parvati rainha das lokas"; "descendência desconhecida da Tridevi (quase guerra em março/2020)"; "Testamento de Jesus" [REVISAR — obra]; "revista Plus Ultra" (não ontológica); "escola de Capela/visita na rebelião"; "arquivos Escócia/Croácia (setas de Moros)"; "Nix gerou Moros"; "Vaikunta"; "microssegundo de pane"; "espíritos sujos = heróis"; "Sofia só sabe atuar na porrada"; "vinda de Sofia = Kalki/Sanata Kumara/Tirthankara/Mahdi";
- **Nenhuma obra nova** (B013 = Tzimtzum/DAF; revista Plus Ultra não é de Ellam);
- Base, índice, XLSX e DOCX regenerados.

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

### Re-curadoria da VERSÃO REFATORADA (devolutiva 2026-08-20) — APROVADA

- 0 códigos novos (770 termos; RC-771 preservado); auditoria RC-628–642 + termos confirmada contra o texto refatorado e as 5 telas;
- 13 fichas ampliadas via `_ampliacoes_2024-05-04-R.txt` (qualificador `P2024-05-04-R`; scripts arquivados em `analise/`);
- **as 5 telas** (extraídas do PDF; descrições do curador) corroboram: Adhyatman Real × Projetado; Mavatma = Vishnu (alma de Jesus); "zumbi" de Prabrajna; ADHYAGIA "esgotada"/"à moda de Jesus – prejudicada"; "restos de Javé – vexame";
- apostila refatorada em 12 PARTES (10.941 palavras; base V2 + trechos V1; **5 figuras embutidas no DOCX**; sem plateia);
- **Colecionar Incertezas (novos):** "147 Adhy em Perpérion"; "43 Pashvnaj ≈ 20 e poucas almas"; "3.500+ universos de Perpérion"; "os outros 146 vieram resgatar e se lascaram"; "a queda não foi premeditada — foi empurrado"; "Kant: universo sensorial não existe lá fora"; "cérebro bilatério ~4 bi anos"; "3–5% da doença de Javé no DNA"; "90% DNA-lixo"; "mundo de regeneração 2050"; "Yel Luzbel retirado no marco zero de Jesus e Apolônio (1993)"; "Antares prestes a explodir"; "Livros de Enoque desaparecidos"; "Teurgia"; "Saccidanandhagana"; "Discurso Interior"; "Sanscaras"; "Dasein (Heidegger)";
- **Ampliações retidas (sem ficha física — padrão):** RC-013/014/135/163/343/499/542/019/156/075/035 → aguardam autorização para criação de ficha em ciclo futuro (conforme O-7).
- **Registro reflexivo (a pedido do curador):** `MAKING-OF-AGENTE.md` arquivado em `apostilas/CONCLUIDAS/2024-05-04_.../analise/` — reações, decisões e aprendizados do Agente neste ciclo (primeiro PDF; dupla versão do Cap. 1; limite como colaboração; telas como chave-mestra). Documento de acervo, não integra ontologia nem BIBLIO.

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

### Re-curadoria (devolutiva 2026-08-20) — APROVADA

- 0 códigos novos (770 termos; RC-771 preservado); auditoria RC-742–744 + 30 termos confirmada;
- 23 fichas ampliadas via `_ampliacoes_2024-08-03.txt` (método à prova de aspas; scripts arquivados em `analise/`);
- 13 fontes `P2024-08-03` adicionadas no grafo (RC-086/092/252/433/454/486/506/514/577/609/622/722/730);
- apostila integral em 13 PARTES (22.619 palavras — a maior da série; intervalo marcado; plateia isolada);
- **Colecionar Incertezas (novos):** "Ig Brasil/Clod Brasil" = Yggdrasil (STT; 2ª palestra corroborando); "Morrensor/Moren Sou" = Mohen So; Eucion (ancestral dos canídeos, ~4,5 mi anos); oxitocina "casal de lagostas"; "Krishna bloqueou" vampiros/lobisomens; "eu de Tat digno"; "espécie BB"/"chics"; "Philip Dimitrop"; "a cura de Brahma está no genoma humano"; prazo de "18.000 anos"; "massa crítica ~470 mi" (oscila); "cidades maias levadas por portais" (quarentena ufológica); "experimento de 2021"; seis/sete rishis (STT nomeia 5); "Homo sapiens racional há 48.000 anos" × FOXP2 47–48 mil (consistente);
- **Ampliações retidas (termos sem ficha física — padrão: não criar ficha sem autorização):** RC-302 Epimeteu (U1480–U1525 — destaque da devolutiva), RC-400 FOXP2 (U1554–U1568), RC-529 Ressonância límbica (U0660–U0700), RC-299 Kalil Kadmon (U1414–U1419), RC-525 Semente da racionalidade (U0946–U0978; U1005–U1015) — aguardam autorização para criação de ficha em ciclo futuro.

## Curadoria P2024-07-14 — Consciências Espirituais Dignificadas

- devolutiva oficial do curador registrada em 2026-08-16;
- 27 relações tipadas novas com fonte `P2024-07-14`;
- RC-745 Colegiados Espirituais Humanizados criado;
- correspondências Teologia Comparada registradas (ex.: Hochmah/Sophia, Kether/Javé/Brahma);
- Base, índice, XLSX e DOCX regenerados.

### Re-curadoria (devolutiva 2026-08-20) — APROVADA

- 0 códigos novos (770 termos; RC-771 preservado); auditoria RC-745 + ~40 termos confirmada;
- 27 fichas ampliadas via `_ampliacoes_2024-07-14.txt` (método à prova de aspas; scripts arquivados em `analise/`); RC-733 fundido na seção existente do ciclo original;
- **9 fichas físicas criadas por autorização expressa (O-7)** — RC-302 Epimeteu, RC-400 FOXP2, RC-529 Ressonância límbica, RC-299 Kalil Kadmon, RC-525 Semente da racionalidade (retenções P2024-08-03), RC-193 Rebanho humano, RC-513 Espiritualidade Errática, RC-545 Coconstrutores, RC-231 Razão Filosófica (P2024-07-14); 9 fontes no grafo; flags `ficha=True`;
- apostila integral em 12 PARTES (14.281 palavras); 3 perguntas intercaladas isoladas (U0281/U0321/U0590); sem perguntas finais;
- **Colecionar Incertezas (novos):** "Júlia Domina"; "Maria Helena"; plataforma "Orbon"; "big data dos anjos"; "Jesus bilatério × Sofia radiata"; "espírito de Brahma e Vishnu = um só espírito" (reforço); "eu humano deve se tornar um svami"; "a catinga furando a blindagem do paraíso"; constituição septenária atribuída a Krishna; "Espírito Santo criado em Niceia (séc. IV)"; Nosso Lar (Chico Xavier); "massa crítica ainda não somos nem 10"; "18.000 anos" (reforço); Nietzsche no hospital espiritual de Edimburgo (relato pessoal); "o centurião que crucificou Jesus" (relato pessoal — espírito que anima Ellam);
- ampliações retidas: **nenhuma** (as 9 fichas pendentes foram autorizadas e materializadas).

## Curadoria P2024-07-13 — Reintegração Cósmica — Tempos de Ruptura

- devolutiva oficial do curador registrada em 2026-08-16;
- 20 relações tipadas novas com fonte `P2024-07-13`;
- RC-742/743/744 também citados por esta fonte;
- Base, índice, XLSX e DOCX regenerados.

### Re-curadoria (devolutiva 2026-08-20) — APROVADA

- 0 códigos novos (770 termos; RC-771 preservado); auditoria RC-003 + ~50 termos confirmada;
- 25 fichas ampliadas via `_ampliacoes_2024-07-13.txt` (método à prova de aspas; scripts arquivados em `analise/`);
- RC-002 ampliada (O-7): pandemia virótica/19 mundos/Outland/Terra como último bastião (variantes ~700 mil × 742 mil; 200 bi × 213 bi na Colecionar Incertezas);
- **B081 cadastrada** (O-6): "Sophia, os Arcontes e a Disputa pela Suzerania Universal" (~2023; grafia canônica Sophia);
- apostila integral em 13 PARTES (18.897 palavras); intervalo de 15 min marcado; plateia isolada (intercaladas + finais);
- **Colecionar Incertezas (novos):** Outland; família Aia/Aie; bolsa de Vaikunta; "as setas de Moros"; Kvasir/Aesir/Vanir; quartel-general de Lúcifer na Terra; WTC = Babilônia (Apocalipse 17-19); Nova Jerusalém-nave; Lêmion (futuro Satã); "Erde" (trabalho de ~800 mi anos do espírito); papagaio Fael; Umbanda "esgoto amoroso"; "90%+ espíritos de outros mundos autistas"; "homoafetivos aumentarão" [quarentena]; cidades espirituais colapsando; Taitiriya Panchado; orixás como única religião persistente; "18.000 anos" (reforço); "Shiva morre junto com a morte humana de Rogério"; "Eva escolhambou com tudo"; "o espírito que anima Ellam morreu em explosão alquímica" (relato pessoal);
- **Ampliação retida (sem ficha física — padrão):** RC-258 Coreografia Cósmica (U0060–U0100; U0900–U0945) — aguarda autorização para criação de ficha.


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

---

## Ciclo de Curadoria + Apostila — P2025-02-16 O Oitavo Dia da Criação / O Novo Ser Humano (19/08/2026)

**Re-curadoria** (repassada de palestra já vista). Devolutiva O-1..O-6 do curador (via Assistente): auditoria aprovada; 24 ampliações aprovadas; **zero códigos novos** (base em 770); B001 confirmado; apostila autorizada; **quarentena político/ufológica ABSOLUTA** (TIs/reptilianos = interpretação narrativa do autor).

### Execução
- Auditoria RC-694–701 contra o STT integral: **8/8 confirmados** (+ ~120 termos anteriores coerentes).
- **25 fichas ampliadas** (seção "Ampliação — P2025-02-16"): destaques — **Mão Invisível/Conselho das Nagas** (palestra "a pedido deles"; RC-697); **cessão consciente do DNA** (2018–2021; desmistifica abduções; RC-698); **fatiamento Brahma/Vishnu = um espírito** (RC-604); **Krishna adármico** (RC-414); **5 linhagens de Kashyapa + 13 filhas de Daksha** (RC-700/701); genealogia completa (RC-696/664/585/581/582).
- 2 termos sem ficha (RC-544, RC-387) → registro na Colecionar Incertezas.
- **31 relações novas**; 13 campos relacionados enriquecidos.
- Base: **770 termos · 1.737 relações** (+31) — `OK: 770 termos, 1737 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-OITAVO-DIA.py`.

### Colecionar Incertezas (itens novos)
"Vmo" (Mohen So); "Mavátima" (Mavatma); "Ophiucus/Ostrogonos" (Ofiúco); "quimpurchas" (Kimpurushas); "valaquilias" (Valakhilyas); "maroraga" (Maharaga); "Tiis" (TIs); "demobiol"; "O Drama Cósmico de Javé" = B001 confirmado.

### Apostila (18ª do acervo)
- `apostila.md` (12.250 palavras; 12 PARTES + glossário A–D; **PARTE XI — Perguntas da Plateia isolada** com 4 intervenções; nota editorial com quarentena TIs/reptilianos); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2025-02-16_oitavo_dia_criacao_novo_ser_humano/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.737 relações · RC-771 livre · 407 fichas · 80 obras · **18 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2025-02-15 Você, a Camuflagem da Realidade e os Postulados Quânticos (19/08/2026)

**Re-curadoria** (repassada de palestra já vista). Devolutiva C-1..C-5 do curador (via Assistente): auditoria aprovada; ~24 ampliações aprovadas; **zero códigos novos** (base em 770); apostila autorizada; quarentenas científico/teológico/clínico confirmadas.

### Execução
- Auditoria RC-702–713 contra o STT integral: **12/12 confirmados** (base madura).
- **25 fichas ampliadas** (seção "Ampliação — P2025-02-15"): destaques — **Maia = arquiteto dos asuras** que mantém a camuflagem (RC-702); **eu humano = pérola > espírito** (RC-704); **Tikun = conserto da obra e do criador** (RC-514/713); **Bhavanga/janela pela respiração** (RC-706); **5 elementos/informação** (RC-707); "finalize em você mesmo" (RC-705); Wyrd como vínculo (RC-658).
- **24 relações novas**; 9 campos relacionados enriquecidos.
- Base: **770 termos · 1.761 relações** (+24) — `OK: 770 termos, 1761 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-CAMUFLAGEM.py`.

### Colecionar Incertezas (itens novos)
"Tat" (quem encomendou a pesquisa); "arrancara" (mecanismo do loop mental); "bavanga" (bhavanga); "sanscara/vasana" (saṃskāra/vāsanā); "cundaline" (kundalini); "25.869 × 28.869 genes"; levitação do autor [não validado].

### Apostila (19ª do acervo)
- `apostila.md` (12.770 palavras; 12 PARTES + glossário A–D; **PARTES V/IX/XII com plateia isolada** — Bárbara, Fernando, Gerald e anônimos; notas editoriais com quarentenas explícitas); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2025-02-15_camuflagem_realidade_postulados_quanticos/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.761 relações · RC-771 livre · 407 fichas · 80 obras · **19 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2024-11-30 Morus e os Arquivos do Destino Universal (19/08/2026)

**Re-curadoria** (repassada de palestra já vista). Devolutiva M-1..M-6 do curador (via Assistente): auditoria aprovada; ~25 ampliações aprovadas; **zero códigos novos** (base em 770); M-4: "Morus" = variação do título (canônico Moros/RC-454); apostila autorizada; quarentenas científico/teológico/histórico confirmadas.

### Execução
- Auditoria RC-714–720 contra o STT integral: **7/7 confirmados** (base madura).
- **24 fichas ampliadas** (seção "Ampliação — P2024-11-30"): destaques — **trajetória completa de Moros** (perseguição pela Trimurti; divisão 25%×3 Moiras + 25%; 3 setas atemporais; RC-454); **Moros reencarnado como Vyasa** (RC-585); **Três Faíscas da Consciência** (RC-719); **maldição dos munis → Hiranyakashipu→Ravana→Dantavakra** (RC-582); **Wyrd fora da jurisdição da Trimurti/Krishna** (RC-658); **Moron/Phanes/Protogonos** (RC-282); Krishna/Gandhari (RC-414).
- 1 termo sem ficha (RC-529) → registro na Colecionar Incertezas.
- **29 relações novas**; 12 campos relacionados enriquecidos.
- Base: **770 termos · 1.790 relações** (+29) — `OK: 770 termos, 1790 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-MORUS.py`.

### Colecionar Incertezas (itens novos)
"Morus" (variação do título; canônico Moros); "Ananké" (STT Ank/Nanc); "Moron" (Phanes/Protogonos); "Danta vacra/Chile Chupa" (Dantavakra/Shishupala); "Call Schauardes de Child" (Karl Schwarzschild); "Súdices" (Parcas?); "Planetolândia de Cagen" (Flatland); "Jaya/Vijaia" (Jaya/Vijaya); "Sanata Kumara" (Sanaka Kumara).

### Apostila (20ª do acervo)
- `apostila.md` (14.300 palavras; 12 PARTES + glossário A–D; **PARTE XI — Perguntas da Plateia e da Internet isoladas** — Bruno 2D/3D, Ivan Krishna/samsara, Ifá/odus, Mentalma; notas editoriais com quarentenas explícitas); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2024-11-30_morus_arquivos_destino_universal/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.790 relações · RC-771 livre · 407 fichas · 80 obras · **20 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2024-11-09 O Abismo da Consciência Cósmica (19/08/2026)

**Re-curadoria** (repassada de palestra já vista). Devolutiva A-1..A-6 do curador (via Assistente): auditoria aprovada; ~24 ampliações aprovadas; **zero códigos novos** (base em 770); B065 confirmado; apostila autorizada; quarentenas científico/teológico/histórico confirmadas.

### Execução
- Auditoria RC-721–727 contra o STT integral: **7/7 confirmados** (base madura).
- **22 fichas ampliadas** (seção "Ampliação — P2024-11-09"): destaques — **implosão do eu de Javé (2021) → buraco negro mental** (RC-717); **Pistis Sophia/Ennoia** e o "corpo tombado de Prabrajna" (RC-530/152); **buracos negros como defeito da criação e vórtice mental** (RC-717); **ilhas de negentropia / ser humano como ponto de luz** (RC-725); **faces do abismo** (Deus "majestosa inutilidade"; Krishna; Jesus; Sai Baba — RC-723/414/072/425); **banalidade do mal** (Arendt/Eichmann; RC-722); **Moren/Projeto Talm** (RC-282/091).
- 3 termos sem ficha (RC-162, RC-385, RC-425) → registro na Colecionar Incertezas; RC-722 ampliado manualmente (reforço banalidade do mal).
- **22 relações novas**; 8 campos relacionados enriquecidos.
- Base: **770 termos · 1.812 relações** (+22) — `OK: 770 termos, 1812 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-ABISMO.py`.

### Colecionar Incertezas (itens novos)
"Charon" (físico — provável Georges Charpak); "Arendit/Harem" (Arendt/Eichmann); "Niet" (Nietzsche); "Moren" (Phanes/Protogonos); "projeto Town" (Projeto Talm); "positelétron" (pósitron); "Pinoia" (Ennoia); "implosão do eu de Javé em 2021" (cronologia interna).

### Apostila (21ª do acervo)
- `apostila.md` (12.200 palavras; 12 PARTES + glossário A–D; **sem bloco de plateia** — apenas pergunta citada no meio; notas editoriais com quarentenas explícitas); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2024-11-09_abismo_consciencia_cosmica/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.812 relações · RC-771 livre · 407 fichas · 80 obras · **21 apostilas concluídas**.

---

## Ciclo de Curadoria + Apostila — P2024-09-29 A Aristocracia Olimpiana e as Monarquias Terrestres (19/08/2026)

**Re-curadoria** (repassada de palestra já vista). Devolutiva O-1..O-5 do curador (via Assistente): auditoria aprovada; ~14 ampliações aprovadas; **zero códigos novos** (base em 770); apostila autorizada; quarentenas político/histórico/ufológico confirmadas.

### Execução
- Auditoria RC-736–741 contra o STT integral: **6/6 confirmados** (base madura).
- **14 fichas ampliadas** (seção "Ampliação — P2024-09-29"): destaques — **Amaterasu = Atena** (RC-738); **Susanoo = Poseidon** (RC-739); **classificação japonesa** (takamimusubi primordiais × amatsukami × Kami = geração de Zeus; RC-740); **genealogia imperial completa** (Kojiki/Nihon Shoki; Izanagi/Izanami; Ninigi; Jinmu; Suiko; os "faltantes"; RC-737); **Parashara e a astrologia védica** (RC-585); **imperador Yu** (dragões aquáticos; RC-740/664); **colapso do corpo de Javé e o "sono de Brahma"** (RC-717); **regra "o que você faz volta"** (RC-559).
- **18 relações novas**; 7 campos relacionados enriquecidos.
- Base: **770 termos · 1.830 relações** (+18) — `OK: 770 termos, 1830 relações — dados válidos.` · RC-771 preservado.
- Backup: `reconstrucao/backups/dados_termos_2026-08-19_PRE-CICLO-OLIMPIANAS.py`.

### Colecionar Incertezas (itens novos)
"Amaterasu deixou de existir em abril [2025?] e deve nascer como humana" [cronologia]; "Poseidon continua lá"; "os oito imperadores faltantes"; "vivos embaixo d'água"; "movimento woke" (quarentena política); imperador Yu filho de dragões aquáticos.

### Apostila (22ª do acervo)
- `apostila.md` (11.900 palavras; 12 PARTES + glossário A–D; **PARTE X — Perguntas da Plateia isolada** — o criador assimilando os males; notas editoriais com quarentenas explícitas); DOCX gerado; pasta em `apostilas/CONCLUIDAS/2024-09-29_aristocracia_olimpiana_monarquias/`.
- Índices sincronizados.

**Estado:** 770 termos · 1.830 relações · RC-771 livre · 407 fichas · 80 obras · **22 apostilas concluídas**.
