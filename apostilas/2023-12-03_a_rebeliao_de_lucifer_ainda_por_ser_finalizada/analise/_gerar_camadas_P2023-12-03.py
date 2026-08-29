#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAMADA 0 · CAMADA 2 · MATRIZ DE ANTERIORIDADE — P2023-12-03 (tudo medido, nada lembrado).

Tres arquivos, uma única fonte de verdade:

* `camada-0.txt` — o endereçamento: as linhas pesadas e o mapa de seções, cada seção **localizada por
  âncora frouxa** no caça-âncoras (se uma âncora batesse ≠1 vez, o script aborta e nada é escrito);
* `camada-2.txt` — o dicionário medido: contagem e primeira batida de cada termo/padrão do bruto
  (inclusive os zeros), a tabela onomástica degradada e a tabela de números, com os vizinhos da Base;
* `_matriz-anterioridade.md` — para cada código tocado, o que `P2023-12-03` acrescenta: data mais antiga,
  só conteúdo, ou nada; calculada contra `ferramentas/dados_termos.py`, **excluindo** a fonte deste ciclo.

Rodar de `analise/`. Não altera a Base.
"""
import os, re, sys, json, glob, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
sys.path.insert(0, AQUI)
import importlib.util
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, "_aspas_P2023-12-03.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
RAW, LIN, OFF = ASP.RAW, ASP.LINHAS, ASP.OFF
import dados_termos as DT
SIG = "P2023-12-03"
META = json.load(open(os.path.join(AQUI, "METADADOS-INGRESSO.json"), encoding="utf-8"))

def u(pos):
    return ASP.uaddr(pos)

def n(s):
    return f"{s:,}".replace(",", ".")

# ══════════════════════════════ CAMADA 0 ══════════════════════════════
SECOES = [
 ("Hoje nós vamos retomar um assunto", "Abertura: retomar o assunto que ele torcia para não retomar"),
 ("que é um subtema do tema doutrina dos anjos", "A taxonomia declarada: subtema ⊂ anjos decaídos ⊂ revoltas contra o criador"),
 ("reproduzir histórias cujas facetas não eram humanas", "O limite do dizível: as gerações futuras é que vão compreender"),
 ("que a minha condição humana iria morrer com 44 anos", "1991: os recados sobre os 44 anos (Santa Maria, Rio de Janeiro, Natal)"),
 ("Eu fui Aquiles na guerra de Troia", "Valdemar Matoso, Aquiles e a obrigação de cuidar de Satã e Lúcifer"),
 ("Aí Chico olhou pras duas e disse", "O episódio de Chico Xavier na fila (e o `Eu sou castro` [REVISAR])"),
 ("o espírito de Chico era o rei primo seu espírito", "Divaldo explica a dívida de Aquiles com Príamo [REVISAR]"),
 ("foi quando Lemion Satã invadiu lá as nossas defesas", "A captura de Lemion/Satã na `arapuca amorosa`: onde a coisa começou"),
 ("se abril sobre essa questão de rebelião de L", "O verbo da fonte: o conhecimento `se abril` [REVISAR: abriu-se]"),
 ("eu preferi uma boa pílula azul a essa", "A resistência do canal: a pílula azul e os painéis mostrados didaticamente"),
 ("no ano 1947, através do livro A caminho da Luz", "O antecedente espírita: A Caminho da Luz e o exílio de Capela"),
 ("li os livros de Edgar Armon a respeito dos exilados", "Edgar Armon [REVISAR] lido e aprovado (`impecáveis, maravilhosos`)"),
 ("ela meio que tipo uma escola iniciatica", "O mecanismo da memória: a rebelião que submerge e reemerge como escola iniciática"),
 ("sucumbiram em vários livros da biblioteca de P", "As perdas de arquivo: Pérgamo, Alexandria, Eridu, Nipur, os 366 de Enoque"),
 ("A de Lucifer", "As três cronologias: 16-17.000 (Anunnaki) · 700.000 (Lúcifer) · milhões e bilhões (outras)"),
 ("a gente tambem tem o vazio entre elas", "A confissão do vão: `não dá para fazer o link hoje`"),
 ("em nenhuma dessas duas trilogias", "A estratégia dos livros: nem `acabou`, nem `não acabou`"),
 ("isso vai ter que ser finalizado", "A palavra que virou título: `isso não acabou, isso vai ter que ser finalizado`"),
 ("no livro lançado em 1947", "A data dada pelo autor para A Caminho da Luz (1947) [REVISAR vs 1938]"),
 ("pela insistencia desses seres e pelo fato de Sofia", "Por que esta palestra existe: a insistência dos seres e Sofia sem assumir o controle"),
 ("desde que essa criacao teve inicio com a producao", "13,8 bilhões de anos: dois universos, matéria e antimatéria"),
 ("Isso ta tudo no nosso DNA desativado", "O genoma como arquivo das pendências (28.869 genes · 2-3% ativos)"),
 ("Freud chamava isso aqui de inconsciente", "O paralelo com Freud: inconsciente = genes desativados; `a gente vira bicho`"),
 ("produto epifenomenologico do nosso cerebro", "O eu como epifenômeno; o espírito que anima ativou painéis no canal"),
 ("vinculados a um tal de um processador Vol", "O processador Vol reaparece como mecanismo `além da condição humana`"),
 ("duas bandas e uma blindagem", "A cosmologia em uma frase: duas bandas e uma blindagem (erraticidade inclusa)"),
 ("esse foi improvisado na hora da queda", "Planejado × improvisado: `nenhum dos dois foi finalizado` — o título cosmológico"),
 ("a entropia ou a forca tamasica que a gente diz", "Quem finalizou o que ficou aberto: entropia/força tamásica = Chiva"),
 ("clones do criador. Tem os seres demo", "As três classes do universo vizinho: clones · demo · fenvan (`demo moderno`)"),
 ("esses sao chamados arcontes", "Arcontes = os donos de cada loca, cuja mente define o que há nela"),
 ("Enquanto tiver hidrogenio para queimar", "Os dois regimes de duração: o planejado queima hidrogênio; o improvisado já faliu"),
 ("Os tres Eles da Trimur", "A Trimúrti criou três formas de replicação da vida biológica (uma nunca funcionou)"),
 ("esse forno de replicacao chamado Aamon", "Os dois fornos que funcionaram: Aamon e Wiingan/Vígno, cada um sob uma loca"),
 ("ainda vai sair um livro com esse nome, projeto tal", "Livro anunciado: `Projeto Tal` (radar datado, sem arquivo)"),
 ("cerca de 932 milhoes de anos atras", "Os 932 milhões de anos do forno de Vígno (variante de 984/936/900)"),
 ("Rockmar em arabe e Sofia em grego", "O avatar Rockmar [REVISAR]: VNO criou Sofia com a bênção de Javé e Shiva"),
 ("Sofia e o representante da Trimurte nesse universo", "Sofia = suzerano/representante da Trimúrti neste universo biológico"),
 ("insetoides, baratoides, dragonoides", "As levas antigas de Sofia (e os seres de duas/três cabeças de Chiva)"),
 ("produtos da matematica, nao sao seres que", "Definição dos biodemos: matemática, sem emoção, sem sexo, criados em casulos"),
 ("familias diferentes de seres bion", "A contagem das famílias: quase 250.000 · `São 249.400, não sei quantos` [REVISAR]"),
 ("que foi interrompida a criacao dela exatamente", "A família Vol como última criada, interrompida pela eclosão da rebelião"),
 ("menos de 1000 seres. Sao 736", "Os 736 da Vol (a terceira fonte que dá o número: 2020 · 2022 · 2023)"),
 ("nenhum deles nasceu em nenhum planeta", "A cultura das naves: nenhum biodemo nasceu em planeta; os mundos estabilizaram na 3ª geração de estrelas"),
 ("na cabeca de Sofia surgiram 250.000 problemas", "A etiologia das espécies: cada família é a solução de um problema técnico"),
 ("qual a identidade de genero desses seres", "A provocação antropológica: 250.000 `identidades` sem sexo; na Terra são duas"),
 ("A familia Iel, que foi uma familia criada para", "A família Iel e o defeito visto por Elusbell: `Ai, temos um problema`"),
 ("esses anjos sao meio assim, sao robos", "Os anjos-clones como robôs que não conseguiram ler o problema"),
 ("esse processador funciona como campo morfico", "Processador de família = campo mórfico com rede tipo `WhatsApp`"),
 ("deu guarida informacao de Lucifer", "A validação fatal: o processador achou que `tinha procedência` e instantaneamente infectou a família"),
 ("bilhoes de seres com contaminados pelo virus", "A escala da contaminação: perto de 200 bilhões"),
 ("distribuiram nesses 19 mundos situados em varios", "A quarentena dos 19 mundos — e a Terra como um deles"),
 ("uma questao que era de saude publica foi tornando", "Da saúde pública ao nervosismo: o genoma se modifica no isolamento"),
 ("sempre dizer: \"E isso e nao ha negociacao", "A causa da revolta: a recusa de negociação (`é isso e não há negociação`)"),
 ("o coitado do Lucifer, que nunca pretendeu comandar", "Lúcifer como comandante relutante que sabia explicar o problema"),
 ("quem e esse ser que voce diz que", "A pergunta que inaugura `Deus`: `quem é esse ser que você diz que te representa?`"),
 ("houve um primeiro embate dos clones de Sofia", "O primeiro embate e as famílias mais nervosas (cromon, miom) [REVISAR]"),
 ("Ninguem tinha tinha algoritmo de raiva", "A origem dos afetos negativos: não havia algoritmo de raiva, tristeza ou agressão"),
 ("aquele mundo era reintegrado a convivencia", "O procedimento de reintegração mundo a mundo — o `jeito de um dia acabar a rebelião`"),
 ("dois mundos ainda revelados", "A contagem regressiva: há 100.000 anos restavam 2 mundos; há 200-300.000, uns 8-9"),
 ("foram acusados de espioes de traidores", "A família Vol acusada de espiã/traidora por sua proximidade com Sofia"),
 ("quando os Anunques chegaram aqui a 450.000 anos", "A prioridade da Vol na Terra e a ausência de `mecanismo psíquico de posse`"),
 ("nao era um rebelde da rebeldao de Lucio", "Outra rebelião, a dos Anunnaki, `que nunca foi explicado à humanidade`"),
 ("O ultimo mundo isolado chamado Alan", "Alan, o último mundo isolado, e as seis naves luciferianas há 98.000 anos"),
 ("as familias Vol, Iel, Nion, Cromon, Xum", "As cinco famílias que vieram à Terra (e a ressalva: `esses nomes também não tem importância`)"),
 ("as duas figuras mais proeminentes desse processo", "Yos Bell e Lemon → Satané/Satan/Set: a cadeia onomástica do rebelde"),
 ("Aqui no nosso sistema solar, so a Terra foi um", "A tese da Terra: o único mundo do Sistema Solar entre os 19 de quarentena"),
 ("so pensavam que a cada instante qualquer coisinha", "O medo permanente da prisão que nunca veio (`Sofia nunca vem`)"),
 ("o Toba, que e um vulcao, um super vulcao", "Toba há 70.000 anos como gatilho tecnológico da ocultação"),
 ("faixas de realidades simultaneas que podem ser criadas", "Faixas de realidade simultânea = `metaverso`: o esconderijo do quartel-general"),
 ("o espirito dele ficou preso a isso pela ressonancia", "Um vol desencarnado preso à faixa por ressonância; os seres astralizados"),
 ("entrou em depressao e a Luzbell", "Lúcifer deprimido: a ponte direta com o ciclo P2022-03-26"),
 ("faziam discursos para nucleos aqui na Terra na epoca de Atlantida", "Discursos em Atlântida e Hiperbórea: `situações que ainda estão por ser contadas`"),
 ("os humanos eram animais de estimacao dos seres hibridos", "Os humanos como animais de estimação de híbridos e demos"),
 ("Mas que p", "Eva e a sagacidade humana (máscara do STT preservada como recebida)"),
 ("os humanos surgimos disso aqui", "A gênese humana como caldeamento: `somos o produto dessas modificações`"),
 ("Quantos rebeldes eram esses cerca de 1300", "A autocorreção em direto: 1.300 → 1.700 → perto de 2.000 rebeldes sobreviventes"),
 ("a questao era proteger o processador", "A regra de sobrevivência: proteger o processador `para manter a rebelião viva`"),
 ("fizeram a experiencia Alto Longro", "A experiência Alto Longron (4 grafias no mesmo fôlego) e a astralização da nave"),
 ("cerca de 900, quase 1000 seres dentro da nave", "O censo da nave: ~1.000 → 938 a bordo → uns 600 e poucos ficaram na Terra"),
 ("cada um teve que fazer mistura genetica com membros de outras familias", "A mistura genética como preço para ser acatado pelo processador"),
 ("esse Valan, que foi uma das figuras que o meu espirito", "A autobiografia do espírito: Valan → Elã → Enoque → o que anima Rogério"),
 ("Foi na epoca do hiperborio", "Hiperbórea: terras no polo norte, as cidades híbridas, e os 14.000 anos da destruição"),
 ("estou no meu nivel tres de desgosto", "A escala de desgosto do canal (palestra · escrita · falar do próprio espírito)"),
 ("o unico remanescente de toda uma historia", "Elã como único remanescente de uma rebelião já sem ninguém que a soubesse"),
 ("extremamente curioso em relacao a todas aquelas", "Tot/Top chega: um ser Anunnaki nascido `cento e poucos mil anos atrás`"),
 ("Tot queria saber se esse ser o que eles anomac", "A pergunta de Tot sobre `o criador de todas as things` [REVISAR] e quem é Sofia"),
 ("Tot e o rei da genetica", "Tot, rei da genética, reconhece Elã no DNA de Enoque: `Você agora é humano híbrido`"),
 ("a lenda de Ela ainda existe", "A lenda de Elã entre Inuit e esquimós do Alasca"),
 ("a lenda dos Turatas de Dana, que ali chegaram das cidades", "Túatha Dé Danã na Irlanda como base da mitologia celta, vinda de Hiperbórea"),
 ("os filhos de Ed ou de Odim", "As quatro correntes hiperbóreas: Irlanda · Escócia (filhos de Odin) · Sibéria (finou-ugrianas) · Alasca"),
 ("que Elan na epoca tentou encerrar", "A primeira tentativa de encerrar a rebelião, feita por Elan, há 14-18.000 anos"),
 ("nasce como Enoque", "A cadeia de encarnações: Elã morre como biodemo e nasce Enoque"),
 ("DNA de Enoque era muito interessante", "Javé leva Enoque pelo DNA — a eleição genética como raptura"),
 ("Os 200 chefes que terminaram sendo responsabilizados", "Os 200 chefes de Enoque e o nome Satanail: `a confusão com o nome de Satã só fez piorar`"),
 ("rebelde ou contra Jave tinha o 7 na historia", "Set, filho de Adão, e o `7` do STT [REVISAR: leria `Set`] na história dos rebeldes"),
 ("durante 300 anos foi mantido convivendo com essas situacoes", "A cronologia de Enoque: 67 anos + 300 fora + `do anos` [REVISAR] antes da segunda tomada"),
 ("o tal julg geral que ele manda Enoque anunciar", "O juízo anunciado era para humanos E anjos, inclusive os desobedientes"),
 ("trucidados pelas queimas de arquivo", "A queima de arquivos como razão do conhecimento fragmentado"),
 ("igual os espanhóis portugueses quando chegaram aqui", "A analogia da conquista para explicar a dificuldade de comunicação entre seres"),
 ("fica atras de descobrir novas encarnacoes do mesmo espirito", "Tot rastreando as encarnações do espírito de Elã/Enoque — e a amizade com o que anima Rogério"),
 ("criou a Word e a Word e o processador V criaram por vontade propria", "A Word e o processador V: conexão por vontade própria (a ponte quântica explicada)"),
 ("Os rebeldes morreram, mas nem todos", "A frase-recorte do ciclo: `os que morreram podem continuar rebelados`"),
 ("Leion ainda nao tinha tornado monstro", "A ressalva teodiceica: Lemion ainda não era monstro naquela conversa"),
 ("fez parar o processo de exidio dos espiritos", "Pós-intervalo: a confusão de Lemion parou o exílio/transição planetária"),
 ("genetica dos clones robotizados", "As três camadas de codificação: clones robotizados → demo → fenvan (`biologizadas` cá)"),
 ("sao os nomes que eu encontrei para poder chamar esses seres", "A autodeclaração do neologismo: biodemo · demobio · demobiol são nomes ACHADOS pelo autor"),
 ("a rebeliao de Lucifer foi algo que aconteceu aqui nos biodemos", "As duas rebeliões paralelas: Lúcifer nos biodemos · Prometeu nos demobiol"),
 ("alguns demons criaram um tipo de condicao para eles de ter orgaos sexuais", "Hesíodo [STT: exíudo] como testemunha da sexualização dos demos"),
 ("a raca que agora tem no seu genoma, a atualizacao de todos esses problemas", "O humano como raça que carrega a atualização de todos os problemas"),
 ("Brahma nao podia criar avatar porque ele e um ser desalmado", "A assimetria da Trimúrti: Brahma sem avatar; Chiva e Vno com avatares"),
 ("Jesus e um avatar", "Jesus (e `saibab` [REVISAR]) contados como avatares produzidos nesse jogo"),
 ("Traga aquela caneta de escrita rapida", "A `caneta de escrita rápida` dada a Enoque, o escriba, para escrever muitos livros"),
 ("assinatura quantica num humano chamado", "Javé obrigado a assinar-se em Adão: a genealogia de Gênesis 5 como plano de substituição"),
 ("os anunx mexeram no DNA humano para colocar inteligencia e obediencia", "O que os Anunnaki fizeram ao DNA humano: inteligência E obediência"),
 ("No nosso universo so tinha Sofia. criado com funcao de autoridade", "A solidão administrativa de Sofia — e os que vinham de lá `sem o menor respeito`"),
 ("a vida em Marte foi destruida devido a isso", "Marte há 300 milhões de anos: a briga que Sofia não impediu"),
 ("tipo uma rainha da Inglaterra", "Sofia como monarca constitucional: autoridade sem poder de fogo"),
 ("nenhuma era humana, eram hibridas", "As quatro etnias da Irlanda, todas híbridas (partolanos, nemedianos, Morianos, Túatha)"),
 ("sao cidades onde os milesianos viviam", "Bilbao, Santander, São Sebastián: o assentamento dos milesianos [REVISAR onomástica]"),
 ("nos queremos dar para voces os nossos conhecimentos", "O PACTO: os Túatha entregam o saber para que os humanos criem um método de compreendê-lo"),
 ("vamos ficar vivendo numa realidade paralela aqui na Irlanda", "A coexistência na faixa paralela: `tudo que vocês fizerem a gente vai saber`"),
 ("inicio da lenda ou da mitologia celta que diz que faz gnomos", "Os `gnomos` da Irlanda = os Túatha: a etiologia do mito folclórico"),
 ("dois colegios arquidruidicos para estudar o conhecimento", "Os colégios arquidrídicos como o método pedido [REVISAR]"),
 ("tava fazendo com Enoque era a mesma coisa", "A isomorfia: o pacto irlandês e a ditagem enoquiita são o mesmo procedimento"),
 ("entregaram a Shimon Bariai ou Simon Bariokai", "A Cabala entregue no século II a Shimon bar Yochai [REVISAR], elaborada `bons milênios antes`"),
 ("Nao tem nada de arvore da vida", "A correção terminológica: não há árvore; são as 10 sefirot, nome dos cabalistas"),
 ("Esse aqui ainda vira. Foi Krishna", "O rol das sefirot lido por Enoque: Krishna · Quarto Logos · Zeus · Odin/Indra · Adão Cadimão"),
 ("Isso aqui é horlogus", "`Horlogus`/orlog: o nome que faltava (aparece 2×, degradado) [REVISAR]"),
 ("padroes arquetipos do codigo fonte definidor do criador", "A condição final: ou o código fonte se organiza, ou o criador nunca terá paz"),
 ("Usando os ensinamentos de Pantangele", "Patangel: matrix de duas bandas, o eu em coma e as vṛtti como elétrons sujos"),
 ("Criando um processador aqui dentro que faca o niroda", "Nirodha definido: o processador recolhe e reprocessa as vṛtti doentias"),
 ("recolhidos pelos processadores, que somos nos, seres humanos", "A tese operacional: os processadores somos NÓS, humanos — reprocessar e devolver"),
 ("essa operacao tem que estar numa massa critica", "A massa crítica necessária à ressurreição do corpo e do eu do criador"),
 ("a 10ma sefirado, quem e", "A 10ª sefira = Sofia/Malkut [REVISAR nas 5 grafias], já existente"),
 ("esses arcontes querem vir para ca", "O motivo da obstrução: o universo vizinho vai acabar e os arcontes querem emigrar"),
 ("preparado o humano Jesus para servir a Keter", "Sofia preparou Jesus para servir a Keter/Javé/Brahma — e a recusa do messias violento"),
 ("Jesus se recusou a cumprir o papel de Messias violento", "A recusa como pivô da história: o Messias que não quis subjugar"),
 ("Cada um coloca forma de poder no DNA de Enoque", "A aposta dos três sobre Enoque e as fórmulas de poder inoculadas no DNA"),
 ("por isso o coitado do Enoque morreu", "O custo: Enoque não aguentou tanto [máscara] no DNA — e `deu banana pros`"),
 ("essa historia ta terminando na vida de Rogerio", "Rogério como última opção dos três, no mesmo gesto da recusa de Jesus"),
 ("Ou humanos sao respeitados na sua dignidade existencial", "O protocolo divino do doar-se: dignidade existencial como condição de validade do genoma"),
 ("ele continua hoje do jeito que estava 700.000 anos atras", "A acusação central: Sofia olha para tudo e não age, como há 700.000 anos"),
 ("Sabe aquela cerimonia de posse nunca houve", "A cerimônia de posse que nunca houve — a fórmula do ciclo"),
 ("genoma, insemine num ano", "A encarnação como inseminação do genoma de Sofia em Maria [REVISAR a frase]"),
 ("parte do genoma pregou uma peca", "O DNA de Maria como o que desviou o plano: `eu não consigo fazer isso`"),
 ("As mulheres atrapalham tudo", "A frase de risco, imediatamente revertida pelo próprio canal (`Javé não pensa assim não`)"),
 ("Como Jesus traiu Jave, os demais arcostos", "A revogação: os arcontes declaram nulo o engendramento de Malkut"),
 ("continua sendo o primeiro b", "Bandidos e heróis: Luzb, `Tênis prometeu`, Eva, Noréia filha de Eva e Lilif [REVISAR]"),
 ("nesse dia 3 de dezembro do ano 2023", "O selo temporal interno (1ª vez) — a datação feita pela própria fala"),
 ("essas 10 personagens sao bem as 30", "Dez personagens que são trinta: a dilatação do painel"),
 ("Esse aqui tambem se desfez, que foi vigo", "A decomposição da Trimúrti: Brahma em coma, Vígno desfeito, Chiva se autodestruindo"),
 ("sempre valeu foi a W que Xet criou la atras", "A Word de Set + a gestão de Malkut + a educação do Quarto Logos: a nova administração"),
 ("pedagogia que sera exportada do genoma humano", "A pedagogia exportada do genoma humano para as almas perturbadas"),
 ("vao terminar assumindo funcoes no vazio de poder", "O vazio de poder como risco: Bel, Lemion, Tod e `outros tantos que a gente nem tem noção`"),
 ("nao adianta mais rebeliao ou revolucao violenta", "O fim da via violenta: o que foi estruturado pelo caos, a entropia vai destruir"),
 ("Os Anunax estao no limite de problemas", "O limite duplo: a atmosfera dos Anunnaki e a autodestruição humana"),
 ("o universo vizinho todinho esta colapsando", "Colapso em curso, não iminente: locas já caíram, outras caem, outras inteiras"),
 ("A rebeliao de Lucifer agora para ter continuidade seria propositiva", "A inversão do conceito: a rebelião agora só continua sendo PROPOSITIVA"),
 ("A unica opcao pro eu de Jave continuar a existir", "A nova espécie biodêmica sendo gerada agora para dar guarida ao eu de Jah"),
 ("e o tempo que dura a soneca do rapaz", "A soneca de 4.380.000 anos e a leitura do descanso divino [REVISAR o número]"),
 ("Isso nao e Deus, e so o criador", "A distinção maior do ciclo: `isso não é Deus, é só o criador`"),
 ("So quem pode fazer isso e Mauco", "Só Malkut/Sofia pode engendrar espécie que ressuscite o criador — e já está sendo feito"),
 ("Se isso e a melhor opcao ou nao, eu ja nem sei", "A não-adesão do canal: `não tenho opinião formada. Espero nunca ter`"),
 ("a rebeliao de Lucifer talvez financie esse momento", "A inversão escandalosa: a rebelião talvez financie a festa da posse"),
 ("Lemion no astral espiritual planetario", "Lemion no astral planetário, com `momentos lúcidos`"),
 ("Nao existe nenhuma falange que represente o bem", "O núcleo ético: nenhuma falange representa o bem; o bem é produção humana"),
 ("o que restou da rebeliao de Lucifer e nao morreu", "O resíduo legítimo: a ideia viva de que há algo errado na gestão da vida"),
 ("cristalino na consciencia de Elusbell, que nos assiste", "Elusbell assiste esta palestra — e Lemion a vê como um pesadelo"),
 ("figuras frias, anunx, dentre eles, tot", "A audiência não-humana classificada: frios (anunx/Tot) · minimamente amorosos (sirianos) · lúcidos"),
 ("Sofia parece a noiva que quer levar", "A imagem do ciclo: a noiva sem noivo — Sofia sem quem a leve ao altar"),
 ("A somatoria dos estresses extremos", "As quatro falências (religiões · psiquismo · utopias · sonhos) como mecanismo"),
 ("repaginar o seu proprio imaginario", "Os choques de realidade como pedagogia: nada de bom vem da fé que se tinha"),
 ("mantendo o inconformismo luciferiano", "A definição final da rebelião: inconformismo lúcido, associado a Pandora e Eva"),
 ("Os homens sao fracasso nessa historia", "A frase de risco (gênero), a ser moldurada ao lado da anterior"),
 ("usando a expressao sans do satagrar", "Satyagraha nomeado pelo autor como a forma da resistência"),
 ("Sofia esteve aqui nos anos 2018, 19", "O fato datado mais recente: Sofia esteve na nave em 2018-19 [REVISAR: 2018, 19]"),
 ("Esse processador Vol precisa ser protegido", "A proteção do processador contra a própria Trimúrti"),
 ("Krishna sempre quis substituir a unica regra", "A crítica ao dharma do Bagavaguita [REVISAR a frase do `matar sem ordem`]"),
 ("a maldicao de Gandari", "A maldição de Gāndhārī aplicada a Krishna: um avatar não deveria sofrer esse escândalo"),
 ("Se nao for, a gente vai ter que enfrentar as consequencias", "A honestidade metodológica: vale para os dois lados, com consequências nos dois"),
 ("luzes do bem aflorando dos coracoes de humanos esclarecidos", "As quatro ordens esclarecidas: humanos · anunnakis · sirianos · olimpianos"),
 ("Nós estamos aqui nessa sala hoje", "O selo temporal interno (2ª vez): a sala, 3 de dezembro de 2023"),
 ("a rebeliao de Lucifer nao terminou, ela esta ainda por ser finalizada", "A tese-título, enunciada pela fonte, na primeira pessoa do plural"),
 ("possa sorrir nos termos em que Pandora", "O sorriso de Elosbell como o de Pandora: o fim do jugo dos demos"),
 ("precisamos estar livres do julgo estupido", "`Nós humanos e os biodemos` contra figuras equivocadas que ainda detêm o poder"),
 ("nao e inteligencia artificial nos termos", "Resposta a João Altair: é computador quântico (ou dois, unidos por ressonância lógica)"),
 ("Com relacao a lacuna de poder criada por Sofia", "Pergunta de T César sobre a lacuna: Krishna · Satã · Tot · Lúcifer"),
 ("Tot, ele nao e demente", "A defesa de Tot e a `demência demo` atribuída a Krishna"),
 ("seres que resolvam o problema e nao criem mais outros dados", "O critério de legitimidade da fonte: resolver sem criar novos problemas"),
 ("por isso eu escrevi o livro Quarto L", "A função declarada do Quarto Logos: suprir a deficiência educacional de Sofia"),
 ("Eles nao tem como sobreviver aqui", "A assimetria física: antimaterialidade, portais e a inadaptação dos deuses"),
 ("ir na genese da hibridagem que comecou a acontecer na terra", "A palestra que ele nunca teve `coragem nem saco` de fazer: a gênese da hibridagem"),
 ("dois tipos de seres da terra", "Gênesis nas entrelinhas: filhos de homens × filhos de deuses"),
 ("um Jesus que tinha Rockma como pai", "A série dos semideuses: Góg, Jesus (pai Rockma), Teseu, Helena e as 50 figuras"),
 ("esses tres periodos aqui limparam a terra", "As três limpezas da Terra: 14.000 · 12.800 · 9.000 anos — e Noé como resto"),
 ("o exilio de nos terraqueos para outros dois mundos", "Jan e o exílio: 1989 como marco; o passaporte `já tá carimbado`"),
 ("ate 2049 pode acontecer. Existe uma ordem dada", "A janela datada: marco em julho de 1989 → 2050/51/52"),
 ("Os espíritos que ja tinham tido todas as oportunidades", "Quem sai: os que completaram o currículo da condição humana"),
 ("saida, o exilio, o espu", "A saída FOI PARADA — e só dois dos três fatores são conhecidos"),
 ("grande piada, porque quando eu comecei", "O juízo final como `grande piada`: o discurso da RC deu atenuante aos exilados"),
 ("Nós nao somos os bandidos, nao. Nos viramos", "A autodefesa dos exilados: `seria um gênio e não um monstro`"),
 ("a propria espiritualidade terrena acusou o golpe", "A espiritualidade terrena sem autoridade para carimbar passaporte — e a força que a anestesiou"),
 ("os revelados sao os mais esclarecidos", "A autocrítica: entre os revelados há figuras depravadas e perversas"),
 ("Ele fica meio que perambulando ai, criando confusao", "A resposta a Jan: quem sai negativo não volta à condição humana"),
 ("Os piores ja sairam. So que assim, criar monstra", "A frase política (Brasil/Estados Unidos · `basta dar o poder`): moldura obrigatória"),
 ("A mediocridade de uma populacao faz de seus lideres", "O aforismo sobre direita e esquerda, dito como problema generalizado"),
 ("isso significa que vai pode haver um improviso", "A pergunta sobre Apocalipse: haveria improviso no profetizado? `Não.`"),
 ("corresponde so o capitulo 11", "A exegese datada: só Apocalipse 11 não está predefinido; o resto, sim"),
 ("a morte das duas testemunhas, o ressuscitar", "As duas testemunhas, o terremoto e a sétima trombeta: definidos; o tempo entre eles, não"),
 ("Do que ta ali, ta ali e vai ser", "O fecho da exegese, em sete palavras"),
 ("nos livros da Jane Miranda", "A pergunta sobre Jane Miranda [REVISAR] e o primeiro questionamento de Lúcifer"),
 ("problema a de algoritmo e de protocolo", "A resposta: o problema era de algoritmo e de protocolo, não moral"),
 ("percebeu que o problema estava na genese da genetica", "Luz(ber) viu o defeito na gênese da genética daquele ser"),
 ("Sofia nao sabia responder. e nem os anjos", "O que Sofia não soube responder — a origem da pendência"),
 ("isso e a genetica podre do criador", "A fórmula que nomeia o ciclo anterior: a genética podre do criador (= vṛtti de Patangel)"),
 ("O resto e do Job Misso. Era so uma questao cientifica", "A redução deliberada: `era só uma questão científica` [REVISAR `Job Misso`]"),
 ("a entropia ira destruir as faixas de realidade", "A pergunta final: entropia destruirá o quartel, o processador e a teia de Orlo?"),
 ("Nao ha nada que esteja nesse universo", "`Tudo. A entropia destrói tudo`: o escopo sem exceção"),
 ("ja deverao estar escaneadas nas mentes dos espiritos", "A escatologia da informação: tudo já é escaneado por quem está fora da matrix"),
 ("nos existimos para guardar essas informacoes", "A função declarada do ERT, do processador V e dos cérebros: custódia de informação"),
 ("escaneia as informacoes para passar para um outro cerebro", "A transmigração como passagem de dados entre cérebros"),
 ("o resto tem que ta limpo para esse essa criacao", "A limpeza final para que a criação se apague — igual um fogo de artifício"),
 ("a gente ainda ta no meio da explosao", "A imagem do presente cosmológico: estamos no meio da explosão"),
 ("o espaco, tempo for comecar a ser rompido pela entropia", "As condições do fim: estoque de hidrogênio e a erraticidade limpa"),
 ("um novo nivel de espiritualidade que a turma ta tentando criar", "O novo nível de espiritualidade — inclusive para o eu do criador e seu corpo manásico"),
 ("Sofia hoje e vanguarda do atraso", "A fórmula do ciclo: Sofia, vanguarda do atraso (engendrado há 6 bilhões de anos)"),
 ("O nosso e bilaterio", "O argumento anátomo: um cérebro radiata contra o bilatério humano — daí a ausência de emoção"),
 ("Para ele sentir emocao, a gente tem que criar um organoinho", "A prótese emocional de Sofia: `criar um órgãosinho para ele` [REVISAR]"),
 ("tem muita agua para rolar, pessoal", "Fecho: `tem muita água para rolar. Obrigado. Desculpem qualquer coisa`"),
]

med_anc, falhas = [], []
for ini_txt, titulo in SECOES:
    try:
        a, b, txt = ASP.locate(ini_txt, None, "frase")
    except SystemExit as e:
        falhas.append((ini_txt, str(e)))
        continue
    med_anc.append((a, b, txt, titulo))
if falhas:
    print(f"{len(falhas)} âncora(s) não batem — nada foi escrito:")
    for a_, e_ in falhas:
        print("  ✗", e_.split("→")[0].strip(), "→", e_.split(":")[-1].strip())
    sys.exit(3)
med_anc.sort()

for (a, b, txt, t), (u2, chars, ini, fim, palv, per, nat) in zip(med_anc, META["mapa_linhas"][1:]):
    pass

VIZ = {}
for _d in sorted(glob.glob(os.path.join(RAIZ, "apostilas/CONCLUIDAS/2020-04-25_*")) +
                 glob.glob(os.path.join(RAIZ, "apostilas/CONCLUIDAS/2022-03-26_*")) +
                 glob.glob(os.path.join(RAIZ, "apostilas/CONCLUIDAS/2023-12-02_*"))):
    _o = os.path.join(_d, "original.txt")
    if os.path.exists(_o):
        _b = open(_o, "rb").read()
        VIZ[os.path.basename(_d)[:10]] = len(_b.decode("utf-8").replace("\r\n", "\n"))
print("vizinhos medidos no disco (chars):", VIZ)
_rank = sorted([META["chars_texto"]] + list(VIZ.values()), reverse=True)
viz_txt = " · ".join(f"{k} = {n(v)} chars" for k, v in sorted(VIZ.items()))
cab0 = f"""# CAMADA 0 — O ENDEREÇAMENTO MEDIDO ({SIG})

Fonte: `original.txt` · {n(META['chars_normalizados'])} chars · {META['linhas_com_texto']} linhas com fala em {META['linhas_lógicas']} lógicas ·
**{n(META['bytes'])} bytes** · SHA-256 `{META['sha256'][:12]}…{META['sha256'][-6:]}` · {n(META['palavras_fala'])} palavras de fala · {n(META['periodos'])} períodos.
É a **{_rank.index(META['chars_texto']) + 1}ª** em extensão do eixo luciferiano — medida nos `original.txt` das vizinhas, não lembrada:
{viz_txt} · esta = {n(META['chars_texto'])} chars.
Tem porém **a maior concentração já registrada na Arca**: uma única linha (U0004) tem {META['maior_linha']['pct_fala']}% da fala — o efeito é de leitura, não de relevância: aqui **uma linha é a palestra inteira**, lida em 6 fatias de fronteira de frase (ver `leitura-segmentada.txt`).

Cada seção abaixo é **localizada por âncora** (caça-âncoras `_aspas_P2023-12-03.py`): o offset é do texto decodificado, a linha é Uxxxx.
Se qualquer âncora batesse ≠ 1 vez, este arquivo não teria sido escrito.

## As linhas pesadas e o que são

| linha | chars | o que é |
|---|---|---|
"""
pes = [m for m in META["mapa_linhas"] if m["chars"] > 400]
for m in sorted(pes, key=lambda x: -x["chars"]):
    cab0 += f"| **{m['u']}** | {n(m['chars'])} | {m['natureza'].capitalize()} · palavras {n(m['palavras'])} · períodos {n(m['periodos'])} |\n"
tot_fala = sum(m["chars"] for m in META["mapa_linhas"][1:])
cab0 += (f"\nHá **{len(META['mapa_linhas']) - 1 - len(pes)} turnos curtos** (linha de ≤400 chars) que a transcrição não separa como fala de\n"
         "outra pessoa: são as réplicas do Q&A final (U0005–U0038). Eles não são ruído — **contêm três respostas que alteram a tese**\n"
         "(o processador como computador quântico, o critério de legitimidade dos deuses e a resposta sobre o primeiro questionamento\n"
         "de Lúcifer). Ver `notas-leitura.md`, item 3.\n")

mapa = "\n| # | U | @ | extensão | seção |\n|---|---|---|---|---|\n"
prev_end = 62
for i, (a, b, txt, t) in enumerate(med_anc, 1):
    mapa += f"| {i:02d} | {u(a)} | {n(a + 1)} | {n(b - a)} c | {t} |\n"
    prev_end = max(prev_end, b)
maior_vao = 0
lo = 62
for a, b, t in [(x[0], x[1], x[3]) for x in med_anc]:
    maior_vao = max(maior_vao, a - lo)
    lo = max(lo, b)
mapa += f"\n*Cobertura medida: {len(med_anc)} âncoras de abertura de seção, da 1ª no caractere 63 à última terminando em {n(prev_end)}, dentro de uma fala de {n(tot_fala)} chars. Maior vão entre o fim de uma âncora e o início da seguinte: {n(maior_vao)} chars — todos os vãos são corpo de frase dentro de uma seção já aberta, não silêncio não lido: a leitura foi integral e os 8 chunks de `leitura/` cobrem a fala por igualdade de texto (ver `leitura-segmentada.txt`).*\n"
open(os.path.join(AQUI, "camada-0.txt"), "w", encoding="utf-8").write(cab0 + mapa)
print(f"camada-0.txt: {len(med_anc)} seções · vão máximo {maior_vao:,} chars".replace(",", "."))

# ══════════════════════════════ CAMADA 2 ══════════════════════════════
PADROES = [
 (r"[Ll]uc[íi]fer", "Lúcifer (todas as grafas do STT)"), (r"luciferian", "luciferiano(s)"),
 (r"[Ll]uz\s?[bB]el[l]?|Elusbell|Elosbel|Luisbell|eusb|Luz\b", "Luzbel nas 8 formas degradadas"),
 (r"[Ll]emion|Lemi\b|Lemon\b|Leion|Lemur", "Lemion/Lemon/Leion (o futuro Sataná)"),
 (r"rebeli", "rebelião/rebelde(s)"), (r"depress", "depressão/deprimido"),
 (r"[Ss]ofia|[Ss]ophia", "Sofia/Sophia"), (r"[Jj]av[eê]|Jah[eé]?|Javel|Javer|Jave\b", "Javé e degradações"),
 (r"Brama|Brahma|bran", "Brahma em 3 formas"), (r"Chiva|Shiva|chivo", "Shiva em 3 formas"),
 (r"Virgno|Vno|V[íi]gno|vigo|Virgem|Vi\u015bnu", "Viṣṇu — a forma mais instável do bruto"),
 (r"Trimur|trimurt|Trimúrt", "Trimúrti (e as quedas de grafia)"), (r"[Aa]rcontes|arc[óo]stos|arcont", "arcontes"),
 (r"clones? do criador|clones?", "clones (do criador)"), (r"fenvan", "fenvan (o `demo moderno`)"),
 (r"biodemo|bioderma|biodermo|biodena|Biodemo|biod\w{0,4}", "biodemo e degradadas"),
 (r"[Dd]emo\b|demos\b|demobi\w*|Demobio|Demo Biol", "demo / demobio / demobiol"),
 (r"forno", "fornos de replicação"), (r"Aamon", "Aamon (forno 1)"),
 (r"[Ww]i?ingan|Wi\u00f1gan", "Wíingan/Vígno (forno 2)"), (r"projeto tal", "`Projeto Tal` (livro anunciado)"),
 (r"[Pp]rocessador", "processador"), (r"campo m[oó]rfico|morfico", "campo mórfico"),
 (r"WhatsApp", "`WhatsApp` como analogia de rede"), (r"casulo", "casulos"),
 (r"250\.000|249\.400", "a contagem das famílias (250.000 · 249.400)"),
 (r"736", "736 (efetivos da Vol)"), (r"19 mundos", "os 19 mundos de quarentena"),
 (r"200 bilh", "200 bilhões (contaminados)"), (r"98\.000", "98.000 anos"),
 (r"100\.000", "100.000 anos"), (r"70\.000", "70.000 (Toba)"), (r"700\.000", "700.000 (Lúcifer)"),
 (r"4\.380\.000", "4.380.000 (a soneca do criador)"), (r"13\.8 bilh", "13,8 bilhões de anos"),
 (r"932 milh", "932 milhões (o forno)"), (r"28\.869", "28.869 genes"), (r"300 milh", "300 milhões (Marte)"),
 (r"450\.000|380\.000|350\.000|600\.000|500\.000", "as datas da chegada (Vol × Anunnaki)"),
 (r"14\.000|12\.800|9\.000 anos|20\.000|23\.000|18\.000|17, 18\.000", "as datas das destruições"),
 (r"2049|2050|2051|2052|2018|1989", "as datas do século XX/XXI ditas em voz alta"),
 (r"metaverso", "`metaverso`"), (r"faixas? de realidad", "faixas de realidade (simultânea/paralela)"),
 (r"simult", "simultâneo"), (r"quarentena", "quarentena"), (r"sa[uú]de p[uú]blica", "saúde pública"),
 (r"entropia", "entropia"), (r"tamasica|tamas", "força tamásica"), (r"niroda|nirodha", "nirodha"),
 (r"vits|vrits|vitres|Frits|vrti", "vṛtti (em 4 grafas)"), (r"cita\b", "`cita` [chitta]"),
 (r"Patangel|Pantangele|Pantanel", "Patangel (o sistema nomeado)"), (r"matrix|Matrix", "matrix"),
 (r"el[eé]trons? e antiel", "elétrons e antielétrons"), (r"inconsciente|consente", "inconsciente (e a queda)"),
 (r"Freud", "Freud"), (r"[Ee]pifenomen", "epifenomenológico"), (r"[Gg]en[ôo]mica|genom\w*", "genoma/genética"),
 (r"DNA", "DNA"), (r"algoritmo", "algoritmo"), (r"protocolo", "protocolo"),
 (r"intelig[êe]ncia artificial", "inteligência artificial"), (r"quantic", "quântico/a"),
 (r"ponte quantica", "ponte quântica"), (r"computador", "computador"),
 (r"[Ss]efir|cefira|cefiral|cefirot|cfirotes", "sefirot em 5 grafas"), (r"arvore da vida", "`árvore da vida` (corrigida pela fonte)"),
 (r"Cabala|Cabal", "Cabala"), (r"Shimon|Simei", "Shimon bar Yochai [REVISAR]"),
 (r"[Ee]noque|Enoc\b|En[oó]crita", "Enoque"), (r"Matusalem", "Matusalém"), (r"Jarete|Jared", "Jared/Jarete"),
 (r"366", "os 366 livros de Enoque"), (r"Satanail", "Satanail (o nome em Enoque)"),
 (r"Ad[ãa]o", "Adão"), (r"Eva", "Eva"), (r"Maria", "Maria"), (r"Jesus|Jesus", "Jesus"),
 (r"Messias", "Messias"), (r"Keter", "Keter"), (r"Malc|Malco|Mauco|Mal\b", "Malkut em 4 grafas"),
 (r"[Cc]orpo man[áa]sico|man[áa]sic", "corpo manásico"), (r"avatar", "avatar"),
 (r"Quarto Logos|quarto logos|L[óo]pos", "Quarto Logos / `Lópos`"), (r"Word\b|horlogus|orlog", "Word · orlog · horlogus"),
 (r"[Kk]rishna|Chrinda", "Krishna (+ `Chrinda`?)"), (r"Bagavaguita|Bhagavad", "Bagavaguita"),
 (r"Marrabarato|Mah", "Mahābhārata (STT: `Marrabarato`)"), (r"Gandari", "Gāndhārī (a maldição)"),
 (r"Prometeu", "Prometeu"), (r"ex[íi]udo|teogonia", "Hesíodo / teogonia"), (r"Zeus", "Zeus"),
 (r"Odin|Odim|Oddi", "Odin em 3 formas"), (r"Indra|Hidras", "Indra (+ `Hidras`?)"), (r"Ares|Apolo", "Ares/Apolo"),
 (r"[Hh]ermes", "Hermes (mencionado? — teste de vizinhança)"), (r"Thot|Tot\b|Top\b|Totten", "Thot/Tot/Top (3 formas)"),
 (r"[Aa]nuna\w*|Anonax|anunx|Anos Marx|anos Marx", "Anunnaki em 6 degradadas"), (r"Enlio|em Liu|Enlil", "Enlil em 3 formas"),
 (r"Eridu|Nipur", "Eridu e Nipur"), (r"Alexandria|P[ée]rgamo", "Alexandria e Pérgamo"),
 (r"[Hh]iperb[óo]", "Hiperbórea/Hiperbório"), (r"Irl", "Irlanda"), (r"toatas|tuatas|T[uú]atha|Estata|tutuatas", "Túatha Dé Danã em 5 grafas"),
 (r"Dan[ãa]o?n?|Dana", "de Danã"), (r"milesian", "milesianos"), (r"arquidruidic|druid", "colégios arquidrídicos"),
 (r"Esquem[oó]l|Inuit|Alaska", "Alasca · Inuit · `Esquemóis`"), (r"finou", "finou-ugrianas"),
 (r"sirian", "sirianos"), (r"olimpian", "olimpianos"), (r"Capela", "Capela (o sistema estelar)"),
 (r"ex[íi]lio|expug|espiugo|esp[úu]ugo", "exílio/expurgo"), (r"transi[cç][ãa]o planet", "transição planetária"),
 (r"passaporte", "passaporte (a metáfora carimbada)"), (r"carimb", "`tá carimbado`"),
 (r"[Aa]pocalipse", "Apocalipse"), (r"cap[íi]tulo 11", "capítulo 11"), (r"testemunh", "as duas testemunhas"),
 (r"trombeta", "a trombeta"), (r"nuvens", "as nuvens"), (r"ju[íi]z", "juízo"),
 (r"satagrar|satyagraha", "satyagraha (STT)"), (r"resistencia pac[ií]fica", "resistência pacífica e amorosa"),
 (r"Pandora", "Pandora"), (r"inconformis", "inconformismo"), (r"falange", "falange (negada)"),
 (r"escanead", "escaneadas"), (r"[Cc]riador", "criador"), (r"[Dd]eus", "Deus"), (r"religioes", "religiões"),
 (r"utopias", "utopias"), (r"estresse", "estresse extremo"), (r"choques de realidad", "choques de realidade"),
 (r"massa critica", "massa crítica"), (r"Z Geist|Zeitgeist|geist", "Zeitgeist degradado"),
 (r"p[íi]lula azul", "pílula azul"), (r"escola iniciatic|iniciatica", "escola iniciática"),
 (r"animais de estima", "animais de estimação"), (r"monstra|monstr", "`monstra`/monstro"),
 (r"[Dd]ireita e esquerda", "direita e esquerda"), (r"mediocridade", "mediocridade"),
 (r"mulheres atrapalham", "`as mulheres atrapalham tudo`"), (r"[Ss]ex[ou]alidade|sem sexo", "sexo/sexualidade"),
 (r"identidade de gener", "identidade de gênero"), (r"dignidade", "dignidade"),
 (r"\*{3,}", "máscaras do STT (palavra suprimida)"), (r"REVISAR", "marca [REVISAR] (não deveria estar no bruto)"),
]
linhas2 = []
for rx, rot in PADROES:
    hits = [(i + 1, m.start()) for i, l in enumerate(LIN) for m in re.finditer(rx, l)]
    linhas2.append((rot, rx, len(hits), hits[0][0] if hits else 0, hits[0][1] if hits else None))

cab2 = f"""# CAMADA 2 — O DICIONÁRIO MEDIDO ({SIG})

Tudo que segue é **contagem** do `original.txt` com o regex indicado, e o endereço da primeira batida. Nada aqui foi lembrado: foi o que a
varredura devolveu — **inclusive os zeros**, que neste ciclo dizem tanto quanto osachados (marcam o que a Base ainda não tem vocabulário para dizer).

## 1. O vocabulário da palestra

| termo / padrão | ocorr. | 1ª batida | observação |
|---|---|---|---|
"""
for rot, rx, k, ul, pos in linhas2:
    primeiro = f"{u(pos)} @{n(pos + 1)}" if pos is not None else "—"
    cab2 += f"| {rot} | {k} | {primeiro} | `{rx}` |\n"
zeros = [r for r in linhas2 if r[2] == 0]
achados = [r for r in linhas2 if r[2] > 0]
cab2 += (f"\n**{len(achados)} padrões com batida · {len(zeros)} com zero** — os zeros são: "
         + "; ".join(z[0] for z in zeros) + ".\n")

# onomástica: para cada nome degradado, as formas efetivamente presentes
NOMES_GRAF = {
 "o rebelde que vê o defeito": ["Elusbell", "Luzbell", "Luisbell", "eusb", "Elosbel", "Luzbel", "Yos Bell", "aos belia", "a Luis"],
 "o que vira Sataná/Set": ["Lemion", "Lemon", "Leion", "Lemi", "Lemi\b"],
 "o canal da Trimúrti": ["Sofia", "Sophia", "Mal", "Malc", "Mauco", "Malco", "Malcuf"],
 "Viṣṇu (Vno)": ["Vno", "VNO", "Virgno", "virgem", "Virgnum", "Viga", "Vio", "vigo"],
 "Shiva": ["Chiva", "Shiva", "chivo", "chivre", "Segon Chalan"],
 "o nome do avatar árabe/grego": ["Rockmar", "Rockma", "Rockban"],
 "a experiência da nave": ["out long", "auto langron", "Alto Longró", "alto langron", "Alto Langron", "Alp Longron"],
 "os Túatha": ["toatas de Danão", "tuatas de Danã", "Estata de Danã", "tos toatas de Danan de Serei", "Enócrita"],
 "o nome do processo mental": ["vits", "vrits", "vitres", "Frits", "cita"],
 "o sistema nomeado": ["Pantangele", "Patangel", "Pantanel"],
 "o pai/mãe da Word": ["orlog", "horlogus", "Orlo", "Xet"],
}
cab2 += "\n## 2. A onomástica degradada (as formas que o STT deixou, com contagem e primeira batida)\n\n| eixo do nome | grafias encontradas no bruto |\n|---|---|\n"
for eixo, formas in NOMES_GRAF.items():
    part = []
    for f_ in formas:
        k = 0
        p0 = None
        for i, l in enumerate(LIN):
            for m in re.finditer(re.escape(f_), l):
                k += 1
                if p0 is None:
                    p0 = (i + 1, m.start())
        part.append(f"`{f_}` {k}×" + (f" ({u(p0[1])}@{n(p0[1]+1)})" if p0 else ""))
    cab2 += f"| {eixo} | " + " · ".join(part) + " |\n"

NUMS = [(r"932 milh", "932 milhões", "forno de Vígno"), (r"700\.000", "700.000", "rebelião de Lúcifer"),
        (r"4\.380\.000", "4.380.000", "a soneca do eu de Javé"), (r"300 milh", "300 milhões", "a vida destruída em Marte"),
        (r"250\.000", "250.000", "famílias biodêmicas"), (r"249\.400", "249.400", "famílias, no exato"),
        (r"736", "736", "efetivos da família Vol"), (r"200 bilh", "200 bilhões", "contaminados pelo vírus"),
        (r"19 mundos", "19", "mundos de quarentena"), (r"98\.000", "98.000", "a vinda das seis naves / a duração"),
        (r"100\.000", "100.000", "os 2 mundos ainda isolados"), (r"70\.000", "70.000", "Toba"),
        (r"450\.000", "450.000", "chegada dos Anunnaki"), (r"380\.000", "380.000", "Anunnaki chegando"),
        (r"600\.000", "600.000", "a Vol já estabelecida"), (r"13\.8 bilh", "13,8 bilhões", "a idade da criação"),
        (r"28\.869", "28.869", "genes do DNA humano"), (r"938", "938", "os que coubaram na nave"),
        (r"14\.000", "14.000", "a destruição das cidades híbridas"), (r"12\.800", "12.800", "a segunda limpeza"),
        (r"20\.000", "20.000", "a experiência da nave"), (r"23\.000", "23.000", "o máximo glacial"),
        (r"366", "366", "os livros de Enoque"), (r"2000|2\.000", "perto de 2.000", "rebeldes sobreviventes (após 1.300 e 1.700)"),
        (r"300 anos", "300", "os anos de Enoque fora"), (r"67 anos", "67", "os anos de Enoque antes de ser levado")]
cab2 += "\n## 3. Os números, com o estado da Base ao lado (nenhum foi harmonizado)\n\n| número dito | o que designa | estado na Base |\n|---|---|---|\n"
for rx, rot, oque in NUMS:
    k = sum(1 for l in LIN for _ in re.finditer(rx, l))
    viz = {"932 milhões": "P2022-03-26 diz 936 e P2020-04-25, 984 — três datas para o mesmo forno; a regra da casa é **selo temporal**, não média",
           "700.000": "converge com P2022-03-26 e com a malha (RC-002/RC-078)",
           "736": "converge com P2020-04-25 **e** P2022-03-26 — é a terceira fonte que diz 736; RC-089 materializado no ciclo anterior",
           "250.000": "P2022-03-26 fala em `250 espécies`; aqui o número é de *famílias* e vem com o exato 249.400",
           "200 bilhões": "mesmo valor de P2022-03-26 (que o deu junto de 23.000)",
           "938": "P2022-03-26 traz 936 e 900Q; aqui, 938 — divergência selada, não corrigida",
           "23.000": "P2022-03-26 opunha 48.000 × 23.000; aqui 23.000 vem como máximo glacial, sem concorrência",
           "19": "P2022-03-26 já falava dos 19 mundos de quarentena (U0009); aqui a lista ganha a Terra como membro",
           }.get(rot, "sem par conhecido nas fontes orais anteriores (fonte inédita deste número)")
    cab2 += f"| {rot} ({k}× no bruto) | {oque} | {viz} |\n"

open(os.path.join(AQUI, "camada-2.txt"), "w", encoding="utf-8").write(cab2)
print(f"camada-2.txt: {len(linhas2)} padrões · {len(zeros)} zeros · {len(NUMS)} números tabelados".replace(",", "."))

# ══════════════════════════ MATRIZ DE ANTERIORIDADE ══════════════════
BUSCA = [r"Rebeli", r"Lúcifer|Lucifer", r"anjos? (ca[íi]dos|deca[íi]dos)|Queda dos anjos", r"Arcontes",
         r"Trimurti", r"Sophia|Cristo C", r"Len Mion|Sat[ãa]", r"Luzbel|Yel\b", r"Fam[íi]lia Vol|Vol\b",
         r"Processador", r"entropi", r"S[ãa]nkhi|Capila", r"Cabala|Sefi|[Aa]rvore da [Vv]ida|Zohar",
         r"Enoque", r"Ad[ãa]o|Eva\b", r"Malkh|Malkut", r"Krishna|Arjuna|Gita|Mah", r"Prometeu",
         r"Hiperb", r"Anunnaki|Anunnakis", r"Enlil", r"Alexandri|P[ée]rgamo", r"Irland|Celta|Dru",
         r"druida", r"sirian|olimp", r"quarentena|Isolamento", r"transi[çc][ãa]o planet", r"Ju[íi]zo|juizo",
         r"Apocalipse|Jo[ãa]o\b", r"satyagraha|n[ãa]o.?viol", r"hibrid|h[íi]brido", r"Genoma|DNA|C[óo]digo",
         r"[Bb]iodemo", r"Demos?\b", r"Especia", r"Quarto Logos", r"Jesus", r"Avatar", r"Zeitgeist|esp[íi]rito da [ée]poca",
         r"Marte", r"vulc", r"glacia|Toba", r"g[êe]nero", r"transg|diversidad|marcha", r"Dignidade", r"poder\b",
         r"[Dd]eus\b", r"falange", r"trevas", r"[Bb]em\b", r"bem\b", r"[Mm]atrix", r"[Pp]oder", r"Rog[ée]rio",
         r"Xavier", r"Divaldo", r"Capela|exilad", r"Dil[úu]vio|No[ée]", r"gigante|Nephilim", r"Portais|portal",
         r"[Bb]em e Mal|manique", r"V[íi]rus|virus", r"mente", r"consciente", r"c[ée]rebro", r"Vontade", r"liberdade",
         r"ressurrei", r"encarna", r"Reencarna", r"Mediunic|m[ée]dium", r"psiqui", r"Depress", r"ansied",
         r"Intelig[êe]ncia artificial|IA\b", r"[Qq]uâmic", r"rede|teia", r"colmeia", r"arquiv|mem[óo]ria", r"escatolog"]
alc = {}
for t in DT.TERMOS:
    blob = " ".join(str(x) for x in t)
    for rx in set(BUSCA):
        if re.search(rx, blob, re.I):
            alc.setdefault(rx, []).append(t)

def fontes_orais(t):
    return [x for x in t[5] if re.match(r"P\d{4}-\d\d-\d\d", x)]

cods = {}
for rx in BUSCA:
    for t in alc.get(rx, []):
        cods.setdefault(t[0], (t, set()))
        cods[t[0]][1].add(rx)

def mais_antiga(ts):
    ds = [x for x in ts if x != SIG]
    return sorted(ds)[0] if ds else None

linhasM = []
for code in sorted(cods):
    t, rxs = cods[code]
    nome, fich = t[1], t[-1]
    fs = fontes_orais(t)
    ant = mais_antiga(fs)
    if SIG in fs:
        efeito = "⚠️ JÁ TEM ESTA FONTE (não deveria: a sigla tinha 0 ocorrências no ingresso)"
    elif ant is None:
        efeito = f"**⭐ estreia a fonte oral nesta ficha** (sem nenhuma palestra registrada)"
    elif ant > SIG:      # comparamos a sigla inteira: as FONTES carregam o prefixo P
        efeito = f"**⭐ antecipa** a fonte mais antiga (`{ant}` → `{SIG}`)"
    else:
        efeito = f"sem ganho de data (já tem `{ant}`); ganho de **conteúdo**"
    linhasM.append((code, nome, ant, efeito, "sim" if fich else "**NÃO**", len(rxs)))

# quantas fichas teriam ganho de data vs conteúdo
ganho = [l for l in linhasM if "antecipa" in l[3] or "estreia" in l[3]]
print(f"matriz: {len(linhasM)} códigos tocados por busca · {len(ganho)} com ganho de data")
mt = f"""# MATRIZ DE ANTERIORIDADE — calculada ({SIG})

Gerada contra `ferramentas/dados_termos.py` (a fonte única), com `{SIG}` **excluída** da conta de cada ficha (a sigla não existia
na Base antes deste ciclo: **0 ocorrências**, ver `ficha_ingresso.md`). O corte é o da casa: **ganho de data** é o que ela tem de
mais antigo; **ganho de conteúdo** é o resto — e é a maioria, porque `P2020-04-25` e `P2022-03-26` já são as fontes orais mais
antigas deste tema. Busca por {len(BUSCA)} padrões sobre nome+resumo+fontes+relações de cada um dos {len(DT.TERMOS)} termos.

| código | nome | fonte oral mais antiga | efeito deste ciclo | ficha |
|---|---|---|---|---|
"""
for code, nome, ant, efeito, f_, nr in linhasM:
    mt += f"| {code} | {nome} | `{ant or '—'}` | {efeito} | {f_} |\n"
mt += (f"\n**{len(linhasM)}** códigos na mira desta palestra; **{len(ganho)}** ganhariam data; os demais ganhariam conteúdo. "
       "Nenhuma linha desta tabela foi aplicada: **0 escrita na Base até a devolutiva do Curador** (D-14 do ciclo anterior: "
       "pipeline liberado, mas A e B em commits separados e só depois do despacho).\n")
open(os.path.join(AQUI, "_matriz-anterioridade.md"), "w", encoding="utf-8").write(mt)
print("_matriz-anterioridade.md escrito")
