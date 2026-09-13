# Mesa 2.5 — tabela `Termos Relacionados` gerada do cadastro (diagnóstico · 12/09/2026)

## O censo honesto (re-rodado hoje; A4 de 11/09 media com uma régua só)
Superfícies medidas: **RELACOES** (arestas tipadas, 1.887 · 1.531 pares) · **espelho t[6]** do cadastro (associações sem tipo · 3.599 pares, só 1.063 recíprocos) · **tabelas das 671 fichas** (~3.215 linhas, 3.041 pares únicos).

| Medida | Nº | Destino na geração |
|---|---|---|
| Par tabela×espelho alinhado (sem aresta tipada) | 904 | linha preservada (o censo A3-era as contava como "só-na-tabela" por olhar só RELACOES) |
| Par só-na-tabela **órfão** (nem aresta nem espelho) | **233** | **a mesa abaixo** — todas têm rótulo editorial real |
| Aresta de cadastro sem linha em NENHUM dos dois polos | 590 | ganham linha na tabela do polo correspondente (nem têm tipo a perder) |
| Divergência de rótulo (par ok, tipo tabela≠tipo aresta) | 216 | resolvida pela hierarquia de rótulos da regra de geração (C4: rótulo livre documenta) |
| Fichas com arestas/espelho mas **sem seção** de tabela | 245 | seção criada na posição canônica (`antes de Seres Associados/Fontes/rodapé`) |

## Regra de geração (função determinística do cadastro; tabelas deixam de ser fonte, viram espelho)
Para a ficha X, o conjunto de linhas é: `t6[X]` ∪ `{Y : X ∈ t6[Y]}` ∪ `{polos de arestas em RELACOES envolvendo X}` — ordenado por código. Coluna *Termo* = nome do cadastro (nunca o apelido da tabela). Coluna *Tipo*: `tipo da aresta se X é sujeito` → `"← tipo" se X é objeto` → `rótulo da tabela atual se o par já tinha linha` → `associado`. Gate de 0 divergências: **suíte ganha T14** — `tabela == f(cadastro)` para as 671; verificador atualiza o parser do `## Termos Relacionados` se precisar (é seção canônica, nome intocado — G2.3).

## As 233 órfãs (lista nominal — curadoria a mesa)
Aparecem na tabela de pelo menos uma ponta sem nenhuma âncora no cadastro; 100% rotuladas. Distribuição dos rótulos: `relaciona-se-a` 59 (+ variantes com glosa), `contexto` 21, `é-um` 4, `protagoniza` 4, `desdobramento` 4, `origem` 3, `gera (cadeia)` 2, `associado-a (família Adhy)` 2, `produz` 2 + cauda longa. Amostra:

| RC-001-RC-042 | Javé · Criatura Universal | relaciona-se-a (recomposição do criador) | RC-042 |
| RC-001-RC-074 | Javé · Len Mion (Satã) | relaciona-se-a | RC-074 |
| RC-001-RC-223 | Javé · O Mal: Subproduto da Ignorância Espiritual | agente (ditadura) | RC-223 |
| RC-001-RC-266 | Javé · Sepher ha-Zohar (e Shimon Bar Yochai) | relaciona-se-a | RC-266 |
| RC-001-RC-273 | Javé · A Falsa Trindade (Concílio de Niceia) | "Pai" da trindade | RC-273 |
| RC-001-RC-310 | Javé · Adhyshprabrajna (Adhy que caiu) | variação | RC-310 |
| RC-001-RC-385 | Javé · Egrégora (circuito dos elétrons rebeldes) | associado-a (vampirizava) | RC-385 |
| RC-001-RC-449 | Javé · Criaturas-ferramenta | relaciona-se-a | RC-449 |

(tabela completa no rodapé deste dossiê)

## Desenhos em mesa
- **M3 · duas camadas (recomendado)**: cadastro manda nas duas camadas — RELACOES (tipado) + t[6] (associação); tabelas são 100% geradas; as 233 **promovidas ao espelho t[6] por despacho desta mesa** (com o rótulo que já têm na tabela preservado na geração), RELACOES intocado; nada é apagado de ficha alguma. Cadastro fica superconjunto honesto do que se sabe; o gate T14 passa a valer para sempre.
- **M1 · tudo tipado**: promove os 2.068 pares do espelho sem aresta para RELACOES com tipos das tabelas (904) e `associado` (1.164) — RELACOES 1.887→~3.050; polui o censo taxonômico de tipos (267) com rótulo-coringa; mais poder analítico do que o pedido.
- **M2 · só arestas**: tabelas e t[6] gerados apenas de RELACOES — 2.068 associações curadas deixariam de existir em qualquer superfície viva (só git as recorda); fere "nada de ouro se perde"; rejeitado de partida, listado por honestidade.

## Portões e ritos da execução (U16, após o visto)
Script bifásico (dry-run/APPLY) com reconstrução por ficha (linha só muda o que a função manda); RELACOES e t[6] só tocam se a mesa mandar a promoção; `relacoes/` (o diretório) intocado — aqui não há arestas novas tipadas; suite T14 nova; builds regenerados (o xlsx/README leem cadastro, não tabela — impacto zero; docx verá as tabelas completas).
| Par | Nome A · Nome B | Tipo(s) na tabela | Aparece em |
|---|---|---|---|
| RC-001-RC-042 | Javé · Criatura Universal | relaciona-se-a (recomposição do criador) | RC-042 |
| RC-001-RC-074 | Javé · Len Mion (Satã) | relaciona-se-a | RC-074 |
| RC-001-RC-223 | Javé · O Mal: Subproduto da Ignorância Espiritual | agente (ditadura) | RC-223 |
| RC-001-RC-266 | Javé · Sepher ha-Zohar (e Shimon Bar Yochai) | relaciona-se-a | RC-266 |
| RC-001-RC-273 | Javé · A Falsa Trindade (Concílio de Niceia) | "Pai" da trindade | RC-273 |
| RC-001-RC-310 | Javé · Adhyshprabrajna (Adhy que caiu) | variação | RC-310 |
| RC-001-RC-385 | Javé · Egrégora (circuito dos elétrons rebeldes) | associado-a (vampirizava) | RC-385 |
| RC-001-RC-449 | Javé · Criaturas-ferramenta | relaciona-se-a | RC-449 |
| RC-003-RC-357 | Reintegração Cósmica · Confederações de Mundos | contexto | RC-357 |
| RC-007-RC-450 | Exilados de Capela · Revolta Capelina | resulta-em (desdobramento) | RC-450 |
| RC-008-RC-041 | Tzimtzum · Criador (Brahma/Javé/Demiurgo) | sujeito da queda | RC-008 |
| RC-008-RC-263 | Tzimtzum · Sefirot / Árvore da Vida | contexto | RC-263 |
| RC-009-RC-145 | Sophia (Cristo Cósmico) · Zeus | relaciona-se-a (relação prévia) | RC-145 |
| RC-009-RC-232 | Sophia (Cristo Cósmico) · Ostronomos | comandava | RC-232 |
| RC-009-RC-260 | Sophia (Cristo Cósmico) · Prisioneiros da Brahmaloka | expressão Adhyajna de Vishnu | RC-260 |
| RC-009-RC-408 | Sophia (Cristo Cósmico) · ADHYMAVATANA (nome completo de Mavatna/Vishnu) | gera (cadeia) | RC-408 |
| RC-009-RC-499 | Sophia (Cristo Cósmico) · Forno de Awaymaion (forno de Vishnu; origem de Olm) | relaciona-se-a | RC-499 |
| RC-011-RC-047 | Adhy · Deidade (Pai-Mãe Amantíssimo / Brahman) | criado-por (origem) | RC-047 |
| RC-011-RC-087 | Adhy · Perpérion | habita | RC-011 |
| RC-012-RC-014 | Adhyagia · Adhydaiva | associado-a (família Adhy) | RC-012 |
| RC-012-RC-016 | Adhyagia · Adhyajna | associado-a (família Adhy) | RC-012 |
| RC-012-RC-087 | Adhyagia · Perpérion | associado-a (imantação → Adhyatman) | RC-012 |
| RC-012-RC-260 | Adhyagia · Prisioneiros da Brahmaloka | condição perdida | RC-260 |
| RC-013-RC-149 | Adhyatman · Mônada (Mônada Espiritual) | condição | RC-149 |
| RC-013-RC-152 | Adhyatman · Prabrajna | condição espiritual | RC-152 |
| RC-013-RC-311 | Adhyatman · Adhyagya (formas espirituais Adhy) | relaciona-se-a | RC-311 |
| RC-014-RC-310 | Adhydaiva · Adhyshprabrajna (Adhy que caiu) | forma pós-queda | RC-310 |
| RC-014-RC-311 | Adhydaiva · Adhyagya (formas espirituais Adhy) | responde-por | RC-311 |
| RC-019-RC-041 | Anjos clones · Criador (Brahma/Javé/Demiurgo) | criado-por (agente) | RC-041 |
| RC-019-RC-049 | Anjos clones · Demos | opõe-se-a (outra classe) | RC-049 |
| RC-021-RC-039 | Antares (Sistema) · Capela (Sistema) | relaciona-se-a | RC-021 |
| RC-022-RC-079 | Antlar · Mastlans Phisosferas / Luciferianas | associado-a (Império de Antlar) | RC-079 |
| RC-024-RC-516 | Anunnaki · Hibridização genética (Nefilim reinterpretado) | relaciona-se-a | RC-516 |
| RC-028-RC-236 | Atlan · O Calvário de um Inocente | refúgio | RC-236 |
| RC-036-RC-046 | Biodemos · Dan | relaciona-se-a (mundo-nave de urdidura dos capelinos) | RC-036 |
| RC-036-RC-089 | Biodemos · Processador Val | — (citação desta fala, não aresta) | RC-089 |
| RC-036-RC-499 | Biodemos · Forno de Awaymaion (forno de Vishnu; origem de Olm) | produz | RC-499 |
| RC-037-RC-038 | Brahma (Brajna) · Brahmaloka | morada-de | RC-038 |
| RC-037-RC-040 | Brahma (Brajna) · CFD (Código Fonte Definidor) | fonte | RC-037 |
| RC-039-RC-103 | Capela (Sistema) · Tau Ceti (Sistema) | relaciona-se-a (relação prévia na malha) | RC-103 |
| RC-040-RC-543 | CFD (Código Fonte Definidor) · Espelho da Herança Espiritual no Epigenoma | relaciona-se-a | RC-543 |
| RC-041-RC-152 | Criador (Brahma/Javé/Demiurgo) · Prabrajna | é-um | RC-152 |
| RC-041-RC-195 | Criador (Brahma/Javé/Demiurgo) · Simbiose Quântica | energia geradora | RC-195 |
| RC-041-RC-310 | Criador (Brahma/Javé/Demiurgo) · Adhyshprabrajna (Adhy que caiu) | é-um | RC-310 |
| RC-041-RC-346 | Criador (Brahma/Javé/Demiurgo) · Jeová (grafia da trilogia) | é-um | RC-346 |
| RC-041-RC-378 | Criador (Brahma/Javé/Demiurgo) · A Rebelião dos Elétrons | beneficia | RC-378 |
| RC-041-RC-382 | Criador (Brahma/Javé/Demiurgo) · A Vida do CFD de Javé no Ser Humano | origem | RC-382 |
| RC-047-RC-059 | Deidade (Pai-Mãe Amantíssimo / Brahman) · Espiritualidade Superior | relaciona-se-a | RC-047 |
| RC-047-RC-483 | Deidade (Pai-Mãe Amantíssimo / Brahman) · Barbelo (Mãe-Pai primordial gnóstica) | relaciona-se-a | RC-483 |
| RC-049-RC-434 | Demos · Homoafetividade (resquício da força original) | origem | RC-434 |
| RC-052-RC-054 | Deus / Deus Incognoscível · Divindades (Co-criadoras) | acima-de | RC-052 |
| RC-054-RC-207 | Divindades (Co-criadoras) · Arquiteto Universal | é-um | RC-207 |
| RC-056-RC-192 | Especiação · Pílula vermelha | relaciona-se-a | RC-192 |
| RC-060-RC-264 | Espiritualidade Operacional · Planos de Existência da Cabala (Atziluth, Briah, Yetzirah, Assiah) | inclui (Atziluth) | RC-264 |
| RC-064-RC-091 | Fenvans · Projeto Talm | mensageiros; relaciona-se-a | RC-064, RC-091 |
| RC-064-RC-165 | Fenvans · Karuna | relaciona-se-a | RC-165 |
| RC-064-RC-769 | Fenvans · Corpos Fenvã (terceira forma de vida do universo vizinho) | relaciona-se-a | RC-064 |
| RC-068-RC-323 | Hiperbórea · Entroncamentos Genéticos Intersiderais | local | RC-323 |
| RC-071-RC-257 | Jan Val Ellam (Rogério de Almeida Freitas) · Espiritismo como Expressão do Quarto Logos | codificador atual | RC-257 |
| RC-071-RC-259 | Jan Val Ellam (Rogério de Almeida Freitas) · Apolônio de Tiana (encarnação do Quarto Logos) | atual agente | RC-259 |
| RC-072-RC-192 | Jesus · Pílula vermelha | relaciona-se-a (reinar sobre o processo) | RC-192 |
| RC-072-RC-408 | Jesus · ADHYMAVATANA (nome completo de Mavatna/Vishnu) | gera (cadeia) | RC-408 |
| RC-072-RC-830 | Jesus · Yel Luzbel Como Aventureiro Isolado (2.000 Anos) | desmaiou-aos-pés-da-cruz-de | RC-830 |
| RC-072-RC-831 | Jesus · Sophia Como Biodemo da Ordem e Caos | é-parte-mais-bela-de | RC-831 |
| RC-072-RC-834 | Jesus · Família Aya (Clone de Sophia para Inseminação Artificial de Maria) | é-clone-para-inseminação-de | RC-834 |
| RC-072-RC-835 | Jesus · Família Aye (Clone de Sophia para Inseminação Artificial de Maria) | é-clone-para-inseminação-de | RC-835 |
| RC-075-RC-927 | Lila · Sai Baba de Shirdi (Shirdi Sai Baba) | contexto | RC-927 |
| RC-075-RC-928 | Lila · Sathya Sai Baba | contexto | RC-928 |
| RC-075-RC-929 | Lila · Prema Sai (Prima Sai / Prem Sai) | contexto | RC-929 |
| RC-078-RC-346 | Lúcifer (Yel Luzbel) · Jeová (grafia da trilogia) | relaciona-se-a | RC-346 |
| RC-080-RC-165 | Mensagem Talm · Karuna | relaciona-se-a | RC-165 |
| RC-080-RC-702 | Mensagem Talm · Camuflagem da Realidade | relaciona-se-a | RC-080 |
| RC-086-RC-145 | Pandora · Zeus | cria (o criador tirânico) | RC-145 |
| RC-086-RC-514 | Pandora · Tikun Cósmico (restabelecimento da Criação) | relaciona-se-a | RC-514 |
| RC-087-RC-264 | Perpérion · Planos de Existência da Cabala (Atziluth, Briah, Yetzirah, Assiah) | inclui (Briah) | RC-264 |
| RC-089-RC-446 | Processador Val · Processadores Familiares | análogo; análogo (aresta registrada na ficha RC-446; **não** há aresta em `RELACOES` para RC-089) | RC-089, RC-446 |
| RC-091-RC-106 | Projeto Talm · Universo Antimaterial (Brahmaloka / Universo Paralelo) | origem | RC-091 |
| RC-091-RC-107 | Projeto Talm · Universo Material (Bhuloka) | destino; destino (código de vida) | RC-091, RC-107 |
| RC-091-RC-155 | Projeto Talm · Eras da Criação (10 eras) | promovido-por | RC-155 |
| RC-092-RC-454 | Quarto Logos (Olm / Codificador de Zian) · Elm (Moros — ser LM de Tempérion) | é-um (mesmo gênero) | RC-454 |
| RC-093-RC-499 | Radiatas · Forno de Awaymaion (forno de Vishnu; origem de Olm) | produz | RC-499 |
| RC-097-RC-149 | Seres Extrafísicos · Mônada (Mônada Espiritual) | distingue-se | RC-149 |
| RC-102-RC-160 | Shiva (Savna) · Entropia e Negentropia | relaciona-se-a | RC-102 |
| RC-104-RC-151 | Trimurti · Gunas Criadoras (Sattva, Rajas, Tamas) | corresponde-a | RC-151 |
| RC-104-RC-474 | Trimurti · Arcontes (= Sophias e Indras; Conselho dos 70) | relaciona-se-a | RC-474 |
| RC-106-RC-174 | Universo Antimaterial (Brahmaloka / Universo Paralelo) · Colmeia Universal | parte-de (favo improvisado) | RC-174 |
| RC-107-RC-174 | Universo Material (Bhuloka) · Colmeia Universal | parte-de (favo planejado) | RC-174 |
| RC-107-RC-179 | Universo Material (Bhuloka) · Plano Colmeia (para o Universo Biológico) | destino | RC-179 |
| RC-132-RC-501 | Val Tam · Conselho dos Cinco (comando da Frota Norte: 3 Val + 2 Yel) | relaciona-se-a | RC-132 |
| RC-147-RC-248 | Zont En Drel 29 · Viajores da Rebelião | contato | RC-147 |
| RC-150-RC-165 | Xadrez Cósmico · Karuna | estratégia (modo de agir) | RC-150 |
| RC-151-RC-162 | Gunas Criadoras (Sattva, Rajas, Tamas) · Elétrons (agente básico da vida universal) | criados pela vibração Rajas | RC-151 |
| RC-152-RC-482 | Prabrajna · Ialdabaoth (= Javé/Samael/Saklas/Sabaoth) | relaciona-se-a | RC-482 |
| RC-155-RC-167 | Eras da Criação (10 eras) · Criação Indevida (Obra indevida) | contexto | RC-155 |
| RC-161-RC-195 | Memória Quântica dos Elétrons · Simbiose Quântica | correlato (física quântica) | RC-195 |
| RC-161-RC-379 | Memória Quântica dos Elétrons · Dança dos Elétrons | envolve | RC-379 |
| RC-162-RC-385 | Elétrons (agente básico da vida universal) · Egrégora (circuito dos elétrons rebeldes) | associado-a (circuito) | RC-385 |
| RC-162-RC-826 | Elétrons (agente básico da vida universal) · Rebelião dos Elétrons (Além da Entropia) | protagoniza | RC-826 |
| RC-162-RC-829 | Elétrons (agente básico da vida universal) · Memória dos Elétrons e Arcanos | tem-memória | RC-829 |
| RC-162-RC-831 | Elétrons (agente básico da vida universal) · Sophia Como Biodemo da Ordem e Caos | tem-pulsação-de | RC-831 |
| RC-162-RC-832 | Elétrons (agente básico da vida universal) · Pulsação dos Elétrons Como Afetividade Humana | tem-pulsação | RC-832 |
| RC-164-RC-382 | Criaturas-ferramenta · A Vida do CFD de Javé no Ser Humano | é-um (contexto) | RC-382 |
| RC-165-RC-612 | Karuna · Nova Espiritualidade / Novo Paraíso (Paraíso B) | relaciona-se-a | RC-165 |
| RC-167-RC-210 | Criação Indevida (Obra indevida) · Matriz Modeladora / Matriz de Cocriação | contexto | RC-210 |
| RC-175-RC-765 | Abelha-Rainha (Javé) · Relógio Messiânico | relaciona-se-a | RC-175 |
| RC-176-RC-334 | Modelo Colmeia (Sistema/Controle Colmeia) · Teocracia da Doença de uma Divindade | expressão | RC-334 |
| RC-179-RC-183 | Plano Colmeia (para o Universo Biológico) · Cultura Demodhármica | código transferido | RC-179 |
| RC-179-RC-187 | Plano Colmeia (para o Universo Biológico) · Insectoides | produtos (espécies) | RC-179 |
| RC-184-RC-283 | Trava-demo · Pandora como Serpente do Éden | contexto | RC-283 |
| RC-186-RC-323 | Biodemol · Entroncamentos Genéticos Intersiderais | envolve | RC-323 |
| RC-189-RC-242 | Eva (figura) · Éden do Criador (Éden como laboratório) | habitantes | RC-242 |
| RC-207-RC-210 | Arquiteto Universal · Matriz Modeladora / Matriz de Cocriação | não-conectada-por | RC-210 |
| RC-208-RC-210 | Criador de Padrões Dependentes · Matriz Modeladora / Matriz de Cocriação | opõe-se-a | RC-210 |
| RC-217-RC-223 | DNA como Projeção Holográfica do Psiquismo do Criador · O Mal: Subproduto da Ignorância Espiritual | herança (cota doentia) | RC-223 |
| RC-223-RC-224 | O Mal: Subproduto da Ignorância Espiritual · Prevalece o Amor | contraponto | RC-223 |
| RC-223-RC-328 | O Mal: Subproduto da Ignorância Espiritual · Imperativo Categórico da Moral | freia | RC-328 |
| RC-226-RC-231 | Cidadão Cósmico · Razão Filosófica dos Terráqueos | capacita | RC-226 |
| RC-226-RC-490 | Cidadão Cósmico · Caim (leitura RC: segundo a nascer) | relaciona-se-a | RC-490 |
| RC-231-RC-245 | Razão Filosófica dos Terráqueos · A Humanização do Criador | fator | RC-245 |
| RC-231-RC-371 | Razão Filosófica dos Terráqueos · A Fé de Jesus e a Razão de Nietzsche | relaciona-se-a | RC-371 |
| RC-236-RC-238 | O Calvário de um Inocente · Era Sapiens | contexto | RC-236 |
| RC-238-RC-297 | Era Sapiens · Era dos Humanos (Zeus e a) | paralelo | RC-297 |
| RC-241-RC-293 | Seres dos Portais · Timé (de um deus) | é-um (deuses) | RC-293 |
| RC-242-RC-243 | Éden do Criador (Éden como laboratório) · Genética da Confiança | base; local de surgimento | RC-242, RC-243 |
| RC-242-RC-285 | Éden do Criador (Éden como laboratório) · Opção Inusitada de Pandora (humanização) | contexto posterior | RC-285 |
| RC-243-RC-245 | Genética da Confiança · A Humanização do Criador | fator | RC-245 |
| RC-243-RC-251 | Genética da Confiança · Laboratórios do Criador | contexto | RC-243 |
| RC-253-RC-257 | Liberdade Mental (premissa do Quarto Logos) · Espiritismo como Expressão do Quarto Logos | finalidade | RC-257 |
| RC-253-RC-259 | Liberdade Mental (premissa do Quarto Logos) · Apolônio de Tiana (encarnação do Quarto Logos) | mensagem | RC-259 |
| RC-253-RC-333 | Liberdade Mental (premissa do Quarto Logos) · Democracia do Amor da Deidade | relaciona-se-a | RC-333 |
| RC-253-RC-335 | Liberdade Mental (premissa do Quarto Logos) · Lavagem Cerebral (condicionamento) | antídoto | RC-335 |
| RC-253-RC-369 | Liberdade Mental (premissa do Quarto Logos) · Nietzsche como 'Amigo da Intenção de Jesus' | relaciona-se-a | RC-369 |
| RC-261-RC-264 | Kether (Javé na Cabala) · Planos de Existência da Cabala (Atziluth, Briah, Yetzirah, Assiah) | reside em Yetzirah | RC-264 |
| RC-262-RC-267 | Daath (a Criação na Cabala) · Isaac Luria e o conceito do Tzimtzum | relaciona-se-a | RC-262 |
| RC-263-RC-268 | Sefirot / Árvore da Vida · Gnosticismo (contraponto à Cabala) | origem (reação) | RC-263 |
| RC-268-RC-763 | Gnosticismo (contraponto à Cabala) · As Sete Leis Herméticas | relaciona-se-a | RC-268 |
| RC-273-RC-786 | A Falsa Trindade (Concílio de Niceia) · Racionalidade Humana Trucidada | contribuiu-para | RC-786 |
| RC-282-RC-481 | Mohen So = Phanes / Protogonos / Vasuki / Kalki (correspondências) · Maitreya (Dionísio; forma adiágena de Vishnu) | relaciona-se-a | RC-481 |
| RC-287-RC-476 | Enigma da Esperança (Caixa de Pandora) · En Ma (Emá / Emar — espírito-âncora) | (contexto) | RC-287 |
| RC-287-RC-514 | Enigma da Esperança (Caixa de Pandora) · Tikun Cósmico (restabelecimento da Criação) | relaciona-se-a | RC-287 |
| RC-292-RC-294 | Telos (de um deus) · Eon de Khaos (Universo de Caos) | ambiente | RC-292 |
| RC-293-RC-480 | Timé (de um deus) · Indra (título de arconte) | relaciona-se-a | RC-480 |
| RC-293-RC-494 | Timé (de um deus) · Dinastia das Sophias | relaciona-se-a | RC-494 |
| RC-298-RC-299 | Descendência de Pirra (Pirra e Deucalião) · Kalil Kadmon (nome demo de Pandora) | nome demo de Pandora | RC-298 |
| RC-298-RC-302 | Descendência de Pirra (Pirra e Deucalião) · Epimeteu (titã) | pai de Pirra | RC-298 |
| RC-301-RC-788 | Prometeu (titã) · Revolução Inacabada de Prometeu e Pandora | protagoniza | RC-788 |
| RC-301-RC-789 | Prometeu (titã) · Centro Alquímico-Farmacopédico | operou-segundo | RC-789 |
| RC-301-RC-790 | Prometeu (titã) · Quinaras / Centauros (Seres Reais que Hoje Nascem Humanos) | recebeu-visitas-de | RC-790 |
| RC-301-RC-791 | Prometeu (titã) · Lamúria dos Deuses (Diagnóstico de Prometeu) | diagnosticou | RC-791 |
| RC-301-RC-792 | Prometeu (titã) · Fogo que se Apaga (Fogo de Prometeu Hoje) | trouxe | RC-792 |
| RC-301-RC-796 | Prometeu (titã) · Judaísmo como Destruidor do Mito de Pandora/Lilith | reescreveu-história-de | RC-796 |
| RC-301-RC-806 | Prometeu (titã) · Desvio de Rota de Pandora (Contra o Plano de Zeus) | motivo-da-vingança | RC-806 |
| RC-301-RC-812 | Prometeu (titã) · Prometeu como Saca-Nica dos Olímpicos | protagoniza | RC-812 |
| RC-301-RC-819 | Prometeu (titã) · Prole sem Face (Humanos Modificáveis sem Face Definida) | está-envolvido | RC-819 |
| RC-302-RC-788 | Epimeteu (titã) · Revolução Inacabada de Prometeu e Pandora | protagoniza | RC-788 |
| RC-302-RC-789 | Epimeteu (titã) · Centro Alquímico-Farmacopédico | operou-segundo | RC-789 |
| RC-302-RC-790 | Epimeteu (titã) · Quinaras / Centauros (Seres Reais que Hoje Nascem Humanos) | recebeu-visitas-de | RC-790 |
| RC-302-RC-791 | Epimeteu (titã) · Lamúria dos Deuses (Diagnóstico de Prometeu) | diagnosticou | RC-791 |
| RC-302-RC-806 | Epimeteu (titã) · Desvio de Rota de Pandora (Contra o Plano de Zeus) | alvo-do-plano | RC-806 |
| RC-302-RC-812 | Epimeteu (titã) · Prometeu como Saca-Nica dos Olímpicos | é-irmão-de | RC-812 |
| RC-302-RC-819 | Epimeteu (titã) · Prole sem Face (Humanos Modificáveis sem Face Definida) | está-envolvido | RC-819 |
| RC-305-RC-815 | Têmis · Temis (Têmis) como Mãe-de-Pandora (Co-clonadora) | é-paralelo-com | RC-815 |
| RC-308-RC-313 | Adhytia (nível hierárquico) · Tempo de Apostasia | contexto | RC-308 |
| RC-314-RC-315 | Fenômenos Denunciadores do Fim · O Fim da Lila | contexto | RC-314 |
| RC-314-RC-317 | Fenômenos Denunciadores do Fim · Esgotamento e Solidão (dos Trimurtianos) | consequência | RC-314 |
| RC-319-RC-328 | Fator Dharma · Imperativo Categórico da Moral | desdobramento | RC-319, RC-328 |
| RC-320-RC-321 | Senhores do Dharma (= Senhores da Lila / Trimurti) · Castas Trimurtianas | autores | RC-320 |
| RC-320-RC-322 | Senhores do Dharma (= Senhores da Lila / Trimurti) · Dharma e Castas (origem demo) | autores | RC-320 |
| RC-321-RC-325 | Castas Trimurtianas · Genética Totalitária | instrumento | RC-321, RC-325 |
| RC-325-RC-331 | Genética Totalitária · Ra-Atom / Og-mi (nomes do Criador) | nomes do Criador | RC-325 |
| RC-325-RC-335 | Genética Totalitária · Lavagem Cerebral (condicionamento) | relaciona-se-a | RC-335 |
| RC-329-RC-488 | Kumari Kandan (tradição) · Nefilins (= Anunnaki) | relaciona-se-a | RC-329 |
| RC-332-RC-334 | Favor Divino (conceito invertido) · Teocracia da Doença de uma Divindade | contexto | RC-332 |
| RC-332-RC-422 | Favor Divino (conceito invertido) · Ser-Criador fracassado (autoconfissão de Javé) | relaciona-se-a | RC-422 |
| RC-332-RC-514 | Favor Divino (conceito invertido) · Tikun Cósmico (restabelecimento da Criação) | relaciona-se-a | RC-514 |
| RC-334-RC-335 | Teocracia da Doença de uma Divindade · Lavagem Cerebral (condicionamento) | instrumento | RC-334, RC-335 |
| RC-334-RC-339 | Teocracia da Doença de uma Divindade · A Difícil Cobrança sobre os Humanos | desdobramento | RC-334 |
| RC-344-RC-535 | Transição Planetária · Projeto Orbum (cidadania planetária) | relaciona-se-a (contexto) | RC-535 |
| RC-346-RC-351 | Jeová (grafia da trilogia) · Mestres de Capela | contexto | RC-346 |
| RC-355-RC-357 | Fator Extraterrestre (o Elo Perdido) · Confederações de Mundos | contexto | RC-355, RC-357 |
| RC-355-RC-359 | Fator Extraterrestre (o Elo Perdido) · Abduções e Reparo Espiritual | contexto | RC-359 |
| RC-365-RC-366 | O Fator Judas · O Enigma da Transfiguração | contexto | RC-365 |
| RC-366-RC-368 | O Enigma da Transfiguração · Assessoria Cósmica (equipes espirituais de Jesus) | contexto | RC-366 |
| RC-369-RC-372 | Nietzsche como 'Amigo da Intenção de Jesus' · O Ser Humano Emancipado | desdobramento | RC-369 |
| RC-371-RC-372 | A Fé de Jesus e a Razão de Nietzsche · O Ser Humano Emancipado | desdobramento | RC-371 |
| RC-382-RC-417 | A Vida do CFD de Javé no Ser Humano · Resposta de Javé (em 1ª pessoa) | relaciona-se-a | RC-417 |
| RC-385-RC-787 | Egrégora (circuito dos elétrons rebeldes) · Egrégora de Lilith / Noreia (Loop Mental Vivo) | associado-a (instância) | RC-385 |
| RC-396-RC-815 | Kvasir e Freya (Vanir/Aesir) · Temis (Têmis) como Mãe-de-Pandora (Co-clonadora) | é-paralelo-nórdico-com | RC-815 |
| RC-396-RC-816 | Kvasir e Freya (Vanir/Aesir) · Pacto Aesir-Vanir como Origem Nórdica da Ideia de Pandora | é-resultado-de | RC-816 |
| RC-404-RC-405 | Sentido Gradualístico das Leis da Evolução Cósmica · Alvorecer de Aquário | contexto | RC-404 |
| RC-409-RC-413 | ADHYSAVNA (nome completo de Savna/Shiva) · Hara (avatar de Shiva) | é-um (avatar) | RC-409 |
| RC-409-RC-414 | ADHYSAVNA (nome completo de Savna/Shiva) · Krishna (avatar de Vishnu/Shiva) | é-um (avatar) | RC-409 |
| RC-416-RC-419 | Cartas a Javé (obra e diálogo) · Sou eu que vivo em vocês (Javé) | tema | RC-416 |
| RC-416-RC-421 | Cartas a Javé (obra e diálogo) · As Memórias de Javé (crônicas) | precede | RC-421 |
| RC-417-RC-418 | Resposta de Javé (em 1ª pessoa) · Terminal Nervoso do Criador (humano) | tema | RC-417 |
| RC-422-RC-427 | Ser-Criador fracassado (autoconfissão de Javé) · Criatura-teste (estágio avançado) | contexto | RC-422 |
| RC-432-RC-433 | Agressividade canalizada (DNA doentio) · Força de Atração Sexual (anterior à polaridade) | contexto | RC-433 |
| RC-434-RC-435 | Homoafetividade (resquício da força original) · O Segredo Perdido do Éden | relaciona-se-a | RC-434 |
| RC-437-RC-561 | Joctan e Faleg (filhos de Heber) · Faces de Javé (sucessivas manifestações do Criador) | relaciona-se-a | RC-561 |
| RC-460-RC-625 | Marduk (= Ra; Anunnaki filho de Enki) · Corpo Manásico / Corpo Mental | relaciona-se-a | RC-460 |
| RC-460-RC-627 | Marduk (= Ra; Anunnaki filho de Enki) · Enéade de Heliópolis | relaciona-se-a | RC-460 |
| RC-461-RC-487 | Ninmah (Anunnaki geneticista) · Enlil (deus sumério, par de Enki) | irmã-de; irmão-de | RC-461, RC-487 |
| RC-476-RC-494 | En Ma (Emá / Emar — espírito-âncora) · Dinastia das Sophias | relaciona-se-a | RC-494 |
| RC-477-RC-494 | Ensá (espírito primordial companheiro de En Ma) · Dinastia das Sophias | relaciona-se-a | RC-477, RC-494 |
| RC-482-RC-530 | Ialdabaoth (= Javé/Samael/Saklas/Sabaoth) · Pistis Sophia (feminino cósmico gnóstico) | relaciona-se-a | RC-482 |
| RC-489-RC-490 | Enoque (sétimo patriarca; levado por Javé) · Caim (leitura RC: segundo a nascer) | relaciona-se-a | RC-490 |
| RC-494-RC-770 | Dinastia das Sophias · Hipóstase dos Arcontes (livro gnóstico; 'realidade dos regentes') | relaciona-se-a | RC-494 |
| RC-506-RC-766 | Ekatma (Adam Kadmon — Homem Primordial) · A Raça Inabalável dos Sethianos Emancipados | relaciona-se-a | RC-506 |
| RC-509-RC-735 | Protagonismo consciencial · Abraço aos Fantasmas / Integridade sem Combate | relaciona-se-a | RC-735 |
| RC-518-RC-619 | Genoma Derivado (interação genoma × trajetória) · Genoma da Liberdade | relaciona-se-a | RC-518 |
| RC-530-RC-565 | Pistis Sophia (feminino cósmico gnóstico) · Hochmah (2ª Sefirah — Sabedoria; = Sophia) | relaciona-se-a | RC-565 |
| RC-543-RC-544 | Espelho da Herança Espiritual no Epigenoma · Novo Homo sapiens (evolução que terá de vir) | relaciona-se-a | RC-543 |
| RC-550-RC-554 | Vontade de Progredir (chave dos arquivos mentais) · Gestão Psíquica e Memórias Complexas (Mentalma II) | relaciona-se-a (a Vontade comanda o processo) | RC-554 |
| RC-550-RC-555 | Vontade de Progredir (chave dos arquivos mentais) · Série Mentalma (5 livros + curso) | relaciona-se-a (tema do vol. I) | RC-555 |
| RC-551-RC-553 | Dehatma Buddhi (doença psíquica da mente identificada com o corpo) · Eu Profundo (nível espiritual do Eu) | relaciona-se-a (antídoto) | RC-551 |
| RC-551-RC-555 | Dehatma Buddhi (doença psíquica da mente identificada com o corpo) · Série Mentalma (5 livros + curso) | relaciona-se-a (tema dos vols. I–II) | RC-555 |
| RC-552-RC-554 | Disciplina dos 3As (respiração, mente, alinhamento) · Gestão Psíquica e Memórias Complexas (Mentalma II) | relaciona-se-a; relaciona-se-a (prática-base: PRA) | RC-552, RC-554 |
| RC-552-RC-555 | Disciplina dos 3As (respiração, mente, alinhamento) · Série Mentalma (5 livros + curso) | relaciona-se-a (tema dos vols. I–II) | RC-555 |
| RC-553-RC-554 | Eu Profundo (nível espiritual do Eu) · Gestão Psíquica e Memórias Complexas (Mentalma II) | relaciona-se-a (o "Eu Mais Profundo" como gestor) | RC-554 |
| RC-553-RC-555 | Eu Profundo (nível espiritual do Eu) · Série Mentalma (5 livros + curso) | relaciona-se-a (tema dos vols. I–II) | RC-555 |
| RC-554-RC-555 | Gestão Psíquica e Memórias Complexas (Mentalma II) · Série Mentalma (5 livros + curso) | está-em (volume II); relaciona-se-a (tema do vol. II) | RC-554, RC-555 |
| RC-554-RC-557 | Gestão Psíquica e Memórias Complexas (Mentalma II) · Conectoma humano (pulsações sinápticas e a sensação de eu) | relaciona-se-a ("conectoma mental", p. 190–191) | RC-554 |
| RC-557-RC-614 | Conectoma humano (pulsações sinápticas e a sensação de eu) · Quarto Cérebro Humano | relaciona-se-a | RC-557 |
| RC-558-RC-562 | Sensação de eu (a sensação particular a cada instante) · Baralho genético (metáfora dos 28.869 genes) | relaciona-se-a | RC-562 |
| RC-558-RC-564 | Sensação de eu (a sensação particular a cada instante) · Fios soltos (improviso humano × robô) | relaciona-se-a | RC-564 |
| RC-563-RC-564 | Travas e lacres (mecanismos de controle do despertar) · Fios soltos (improviso humano × robô) | relaciona-se-a | RC-563, RC-564 |
| RC-579-RC-785 | Noreia (Norea) · Sequência Formativa da Racionalidade Humana | compõe | RC-785 |
| RC-579-RC-787 | Noreia (Norea) · Egrégora de Lilith / Noreia (Loop Mental Vivo) | compõe | RC-787 |
| RC-621-RC-795 | Nyx · Nyx como Mãe de Origem de Pandora | é-mãe-de-origem | RC-795 |
| RC-735-RC-938 | Abraço aos Fantasmas / Integridade sem Combate · Livre-arbítrio | relaciona-se-a | RC-735 |
| RC-796-RC-813 | Judaísmo como Destruidor do Mito de Pandora/Lilith · Culto a Lilith (Transformação em Deusa Lil Babilônica) | apagou | RC-813 |
| RC-796-RC-818 | Judaísmo como Destruidor do Mito de Pandora/Lilith · Patriarcado desde Pandora (Origem no Feminino, Dominação pelo Masculino) | é-veículo-de | RC-818 |
| RC-803-RC-803 | Budismo como Exceção (Sem Deus) · Budismo como Exceção (Sem Deus) | qualifica | RC-803 |