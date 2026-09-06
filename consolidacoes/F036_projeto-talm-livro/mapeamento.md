# F036 — «Projeto TALM – O Livro» · Mapeamento

Fonte canônica: `consolidacoes/F036_projeto-talm-livro/fonte.txt` · SHA-256 `b9ad623e3b6fd27e9057c1cf04c63a4f085b9fb802b12fae1c4193eae8f7857e` · 121.388 B · 338 linhas.
Bruto de recepção (nome EXATO, com travessão «–»): `uploads_recepcao/14 - Projeto TALM – O Livro.txt` (recebido via commit `f88f554`; ff-only sobre `fda60c2`).

## §1 · Estrutura

Prefácio «O Prefácio do Arquiteto Cósmico» + Parte I (Caps. 1–3: Design Inteligente/Vácuo do Acaso; Drama do Criador; Nidana) + Parte II (Caps. 4–6: Semeadura e Fornos; DNA Humano; Rebelião dos Elétrons) + Parte III (Caps. 7–9: Humanidade Artífice; Desafios da Consciência; Liberdade de Pensamento) + Parte IV (Caps. 10–11: Quarto Logos e Reintegração; Nidana→Saccidanandhagana) + Conclusão + Anexo: Glossário Temático (≈12 verbetes, encerrando o arquivo — sem resíduo de compilador, mais limpo que o F034).

## §2 · Diagnóstico central — documento-FONTE do cluster P2025-08-02

- `apostilas/CONCLUIDAS/2025-08-02_projeto_talm/analise/METADADOS-INGRESSO.json`: natureza = «MATERIAL DO CURADOR (ART-2025-08-02) — sistematização própria baseada estritamente em livros e palestras de Jan Val Ellam» · autor = **Edson Cella Mendes (o curador)** — o mesmo da série «refatorada» (cf. P2024-05-04: «pdf refatorado… documento de Edson Cella Mendes»).
- **Diff doc × `original.txt` da apostila = 6 linhas, todas o cabeçalho**: o original traz «2025-08-02 - Projeto TALM / Autor: … / Fonte: …» onde o doc traz o título «Projeto TALM – O Livro». O CORPO É BYTE-A-BYTE O MESMO TEXTO. O doc não é reciclagem de terceiro grau (F034): é a fonte (F035-sibling) com o wrapper trocado.
- Estatística de linha: **250/250 (100%)** linhas ≥80c verbatim no corpus; **250/250 vs `original.txt`**; **203/250 (81%) vs `apostila.md`** — as 47 linhas ausentes são todas o andaime pedagógico de abertura de capítulo («Capítulo N: … Descreveremos/Exploraremos/Analisaremos…»), condensado em prosa própria pela editoração de 2025: supressão de formato, não de conteúdo (§5).
- Auditoria de aspas: **393/393 (100%)** citações ≥8 palavras em linha verbatim no corpus — o melhor índice da série (o material do curador usa aspas para marcar os próprios empréstimos de Ellam, e os empréstimos batem).
- Numerais: único «sem par» aparente são os números de capítulo (1–11, 9.1–9.3); «7,5 a 7,7 bi», «95% a 97%», «3% a 5%», «~4 bi», «2016/2017/2018» todos ancorados (F033/F034/F035-eras).

## §3 · Cotejo B050 (o ganho de verificação do ciclo — lista «Datas a conferir» do DOSSIE l. 86)

O DOSSIE-UTILIDADE do próprio cluster lista, em «C. Incertezas do texto»: *«Datas [REVISAR — conferir B050]: TALM ~7,5–7,7 bi; Olm 6–7 bi; biodemos ~900 mi; Trimúrti presa 2012; desfeita 2015–2018; Sophia em Alt' Lam Gron 2017/2018; «Sophia autor do Apocalipse»»*. Verificação feita contra `livros/CONCLUIDOS/B050_guia_das_eras_universais_mapa/original.txt`:

| item da lista | resultado no B050 / corpus | estado |
|---|---|---|
| TALM ~7,5–7,7 bi | **B050 l. 82**: «[ 7,700,000,000 a.p.] (trilha A, y=1724) "Início" do projeto Talm. (7,7 bilhões a.p.)» — converge com a faixa da curadoria 2025 (apostila-02 l. 50) | ✅ CONFERIDO (com aspas de «início» que o mapa impõe) |
| Mohen So/Fenvans ~7,8 bi (corolário F034) | **B050 l. 81**: «[ 7,800,000,000 a.p.] Surge Mohen So, criador dos Fenvans.» | ✅ corrobora a âncora do F034 (RC-064) |
| Nidana «molécula-mãe» ~4 bi | **B050 l. 94**: «[ 3,800,000,000 a.p.] Surge a água no planeta Terra. / Surge o Nidana ("molécula-mãe). / Primeiras moléculas que já / possuiam câncer.» | ✅ compatível (≈4 bi); nota: o mapa crava 3,8 e a grafia «molécula-mãe)» sem fecha-parênteses é do original |
| biodemos ~900 mi | B050 silencioso; âncora primária de palestra: P2022-03-26 «essa historia comecou ha cerca de 900 milhoes de anos atras» + P2020-04-25 («natureza dos biodemos: casulos, assexuacao por familia, 900 milhoes de anos») + **B057 p. 21 nas fichas RC-009/RC-442** («900 milhões a 230 milhões») | ✅ fechável por fonte diversa |
| Olm 6–7 bi | **B050 SILENCIOSO** (nenhuma linha Olm/Quarto Logos); persiste a tensão de molduras: curadoria 2025 ×3 «surgiu de Awaymaion há 6–7 bi» vs aula P2020-07-11 «o oitavo: ficou fora 5–6 bilhões de anos; só quando estava estabelecida a estratégia… mergulhou» (+ RC-092 l. 56: P2025-06-26 «só mergulhou quando a vida biológica surgiu») | ⚠ NÃO ENCERRÁVEL — flag da ficha RC-092 l. 51 mantém-se |
| Trimúrti presa 2012 · desfeita 2015–2018 · Sophia 2017/2018 | datas EC (era comum) — fora da jurisdição do mapa das eras (tempo profundo); já ancoradas no próprio material ART (l. 50 «desfeita entre 2015 e 2018»… ll. 708/976) | ✅ conferidas por inadstrição de alçada + âncora de curadoria |
| «Sophia autor do Apocalipse» | regido pelo despacho F034-Q-C: **REVISAR MANTIDO** | ⏸ não é matéria do F036 |
| (extra) RC-091 l. 65 `[REVISAR]` de cronologia interna do B024 (~8,1 bi cap. 16 × ~7,5 bi cap. 12) | o B050 oferece **um terceiro ponto convergente: 7,7 bi** («início» com aspas), não resolve a discrepância interna do livro | ⚠ averbar os três pontos; encerrar ou não é decisão do curador |

## §4 · Anti-duplicação

Conteúdo integralmente internalizado pelo ART-2025-08-02 (INDICE: «o programa: acrônimo expandido; nidana→saccidanandhagana; semeadura; DNA; Rebelião dos Elétrons; reintegração (RC-091 e ~15 ampliações; 6 códigos novos RC-771…777)» — e glossário do doc reproduz verbetes já fichados: RC-080/091/092/132/154/165/186/442/454/658/771…). **Termos novos: 0 · Relações novas: 0.** Guarda B060 («nome ??»): inatacável (nenhum nome novo; «Codificador de Zion» = sinônimo Zian↔Zion já assentado na F030-era).

## §5 · As 47 linhas suprimidas pela apostila

Todas de um só gênero: as aberturas «• Capítulo N: … Este capítulo desvendará / Descreveremos / Exploraremos…». A editoração de 2025 substituiu o estilo-índice («o que este capítulo fará») por prosa afirmativa — escolha de formato, zero perda doutrinária (cada afirmação substantiva dessas linhas tem par correspondente na prosa curada). Averbo para que a próxima reciclagem não leia a supressão como censura de conteúdo.

## §6 · Nota filológica (ledger)

- O corpo do doc bate 100% com o original.txt, mas o doc NÃO é byte-idêntico ao original (header substituído; 338 vs 342 linhas; 121.388 vs 121.514 B) — distinção que separa F036 de F035 (lá: 0 de diferença).
- Aspas do material: em 2 casos o original.txt fecha parênteses sem abrir e vice-versa (l. 94 do B050 reproduzida acima é do próprio livro, não do doc) — nenhum impacto.
- O doc não contém «Briefing Documento» (ausência que o torna mais limpo que o irmão F034).
