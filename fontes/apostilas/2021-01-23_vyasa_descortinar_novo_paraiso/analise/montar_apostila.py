#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2021-01-23 — Vyasa e o Descortinar de um Novo Paraíso).
Lê leitura-segmentada.txt, aplica curadoria (grafias canônicas + [REVISAR]),
estrutura em 12 PARTES com subseções, isola intervalos e perguntas da plateia,
e anexa cabeçalho TOP + glossário local."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2021-01-23_vyasa_descortinar_novo_paraiso")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

# ============ 1. REPLACES CANÔNICOS ============
REPL = [
    (r"\bApantaratamas\b", "Apantaratamas"), (r"\bapantaratamas\b", "Apantaratamas"),
    (r"\bAparantaras\b", "Apantaratamas"), (r"\bapantar[atãa]?ras?\b", "Apantaratamas"),
    (r"\bPantaratas\b", "Apantaratamas"),
    (r"\bParachara\b", "Parashara"), (r"\bParacharada\b", "Parashara"),
    (r"\bParachá\b", "Parashara"), (r"\bCharasa\b", "Parashara"), (r"\bParach\b", "Parashara"),
    (r"\bViaza\b", "Vyasa"), (r"\bViasa\b", "Vyasa"), (r"\bviaza\b", "Vyasa"),
    (r"\bViáa\b", "Vyasa"), (r"\bVia\b", "Vyasa"), (r"\bViada\b", "Vyasa"),
    (r"\bMarrabarata\b", "Mahabharata"), (r"\bBarrabarata\b", "Mahabharata"),
    (r"\bmarrabarata\b", "Mahabharata"), (r"\bMarrabarato\b", "Mahabharata"),
    (r"\bBarrabarat\b", "Mahabharata"),
    (r"\bGiotista\b", "Jyotisha"), (r"\bGiosticha\b", "Jyotisha"), (r"\bGiatis\b", "Jyotisha"),
    (r"\bJotisha\b", "Jyotisha"), (r"\bVedanca\b", "Vedanga"),
    (r"\bBagabagita\b", "Bhagavad Gita"), (r"\bRamaiana\b", "Ramayana"),
    (r"\bVígno Pur\b", "Vishnu Purana"), (r"\bVígnio Pur\b", "Vishnu Purana"),
    (r"\bDuarca\b", "Dwarka"), (r"\bDuar[ck]a\b", "Dwarka"),
    (r"\bCapila\b", "Kapila"),
    (r"\bSidarta Galutano\b", "Sidarta Gautama"), (r"\bSidarta Galutan\b", "Sidarta Gautama"),
    (r"\bGina Marvira\b", "Mahavira"), (r"\bGinamarravira\b", "Mahavira"),
    (r"\bGinamaravira\b", "Mahavira"),
    (r"\btirtancaras\b", "Tirthankaras"), (r"\bTirtancara\b", "Tirthankara"),
    (r"\bTirtancaras\b", "Tirthankaras"),
    (r"\bFriga\b", "Frigga"), (r"\bfragil\b", "Frigga"), (r"\bFrida\b", "Frigga"),
    (r"\bCristva\b", "Krishna"), (r"\bCristo\b", "Krishna"), (r"\bCrist\b", "Krishna"),
    (r"\bChiva\b", "Shiva"), (r"\bchiva\b", "Shiva"), (r"\bChilo\b", "Shiva"),
    (r"\bChica\b", "Shiva"), (r"\bChila\b", "Shiva"), (r"\bde China\b", "de Shiva"),
    (r"\bChirão\b", "Shiva"), (r"\bChva\b", "Shiva"),
    (r"\bVirghiva\b", "Vishnu"), (r"\bVirgometeu\b", "Vishnu"),
    (r"\bVirgem\b", "Vishnu"), (r"\bVirgo\b", "Vishnu"), (r"\bVgo\b", "Vishnu"),
    (r"\bVism\b", "Vishnu"), (r"\bVirg\b", "Vishnu"),
    (r"\bvirgem\b", "Vishnu"), (r"\bvirg\b", "Vishnu"),
    (r"\bBrama\b", "Brahma"), (r"\bbrama\b", "Brahma"),
    (r"\bJaé\b", "Javé"), (r"\bJahé\b", "Javé"), (r"\bJosavé\b", "Javé"),
    (r"\bJabé\b", "Javé"), (r"\bJé\b", "Javé"), (r"\bou ja viu\b", "ou Javé viu [REVISAR — STT 'ja']"),
    (r"\bde mos\b", "de Moros"), (r"\bde móveis\b", "de Moros"),
    (r"\bde mores\b", "de Moros"), (r"\bde mortos\b", "de Moros"),
    (r"\bMórus\b", "Moros"), (r"\bmodos\b", "Moros"),
    (r"\bas loiras\b", "as moiras"), (r"\bas noras\b", "as nornes"),
    (r"\bno modo\b", "Odino"), (r"\bOdino\b", "Odino"),
    (r"\bRoché\b", "Rochester"), (r"\bRocheste\b", "Rochester"),
    (r"\brochester\b", "Rochester"), (r"\bRochesta\b", "Rochester"),
    (r"\bZéfra\b", "Zéfiro"), (r"\bZéfo\b", "Zéfiro"), (r"\bRivai\b", "Rivail"),
    (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"), (r"\bdo suf\b", "de Sophia"),
    (r"\bFale\b", "Faleg"), (r"\bfalec\b", "Faleg"), (r"\bFalec\b", "Faleg"),
    (r"\bJoquã\b", "Joctã"), (r"\bJotã\b", "Joctã"), (r"\bJoquan\b", "Joctã"),
    (r"\bGommer\b", "Gomer"),
    (r"\bPacho Pato\b", "Pashupati"), (r"\bPachupati\b", "Pashupati"),
    (r"\bcom mar e candão\b", "Tamil [REVISAR — STT 'com mar e candão']"),
    (r"\bMaric Candô\b", "Tamil [REVISAR — STT 'Maric Candô']"),
    (r"\bálbum branco dos bits\b", "álbum branco dos Beatles"), (r"\bdos bits\b", "dos Beatles"),
    (r"\bBeetles\b", "Beatles"),
    (r"\bIA\b", "IEA"), (r"\bIa\b", "IEA"),
    (r"\btrigerina\b", "vanguarda [REVISAR — STT 'trigerina']"),
    (r"\bMéxica\b", "Méxica [REVISAR]"), (r"\bcachava\b", "cachava [REVISAR — STT]"),
    (r"\bAranque\b", "Aran"),
    (r"\bbiocosmos\b", "Biocosmos"), (r"\bdiapómos\b", "Biocosmos"),
    (r"\bO paraísoar\b", "O paraíso"),
    (r"\bmitologia nores\b", "mitologia nórdica"), (r"\bTrimurte\b", "Trimurti"),
    (r"\bas mães ou as normas\b", "as moiras ou as nornes"),
    (r"\bdo DNA dessec\b", "do DNA desses seres"),
    (r"\bVisto já\b", "Vishnu já"),
    (r"\bdos primórdios do I do universo é o I\b", "dos primórdios do universo é o IEA"),
    (r"\bO I tá\b", "O IEA tá"), (r"\bespírito de moros\b", "espírito de Moros"),
    (r"\bse endo as mo as nornes\b", "sendo as moiras ou as nornes"),
    (r"\bcolégio druído\b", "colégio druídico"), (r"\bcolégio druída\b", "colégio druídico"),
    (r"\bo seu dono de Allan Kardec\b", "o codinome de Allan Kardec [REVISAR — STT 'dono']"),
    (r"\bjá foi proído lá atrás\b", "já foi druida lá atrás [REVISAR — STT 'proído']"),
    (r"\bera Zéfo\b", "era Zéfiro"),
    (r"\bsábio a pantaratamas\b", "sábio Apantaratamas"),
    (r"\ba pedido de viso\b", "a pedido de Vishnu [REVISAR — STT 'viso']"),
    (r"\bfios sortos de dama de Shiva\b", "fios soltos de Brahma e de Shiva [REVISAR — STT 'dama']"),
    (r"\bo buloca\b", "o 'bhuloka' [REVISAR — STT 'buloca']"),
    (r"\bprocura Abraham\b", "procura Abraão [REVISAR — STT 'Abraham']"),
    (r"\bvirg pediu\b", "Vishnu pediu"),
    (r"\bessa promessa de virgem\b", "essa promessa de Vishnu"),
    (r"\bvir quis dizer\b", "Vishnu quis dizer"),
    (r"\bdo Danacha e dos utanichas\b", "do [Dhanurveda?] e dos Upanishads [REVISAR — STT 'Danacha/utanichas']"),
    (r"\bnarrar uma rabarata\b", "narrar o Mahabharata"),
    (r"\bpros gandavas\b", "pros gandarvas"), (r"\bpros rachaças\b", "pros rakshasas"),
    (r"\bessa época de viado\b", "essa época de Vyasa"),
    (r"\bdo viado\b", "de Vyasa [REVISAR — STT 'viado']"),
    (r"\bViada, filho\b", "Vyasa, filho"), (r"\bde Parachar\b", "de Parashara"),
    (r"\bos hiperórios\b", "os hiperbórios"),
    (r"\bé uma rabarata\b", "é o Mahabharata"), (r"\buma rabarata\b", "o Mahabharata"),
    (r"\bessa escura\b", "essa estrutura [REVISAR — STT 'escura']"),
    (r"\bo projeto Tal\b", "o projeto [Tal?] [REVISAR]"),
    (r"\bcorpo de metatron\b", "corpo de Metatron"),
    (r"\bSobrou de En\.", "Sobrou de Enoque"),
    (r"\blinhagem de C\b", "linhagem de Cam [REVISAR — STT 'C']"),
    (r"\bde C, ele não podia\b", "de Cam, ele não podia [REVISAR — STT]"),
    (r"\bCã viu Noé\b", "Cam viu Noé [REVISAR — STT 'Cã']"),
    (r"\bde Seno\b", "de Sem [REVISAR — STT 'Seno']"),
    (r"\blinhagem de Sé\b", "linhagem de Sem"),
    (r"\bos branises\b", "os brâmanes [REVISAR — STT 'branises']"),
    (r"\bÉder Javé, Éder J Feg\b", "Éber, Javé, Éber e Faleg [REVISAR — STT]"),
    (r"\bÉder\b", "Éber"),
    (r"\bna altura da folha de brana\b", "na altura da fala de Brahma [REVISAR — STT 'folha']"),
    (r"\ba ponte dialétrica\b", "a ponte dielétrica"),
    (r"\bmisturando gêmeo por clagem\b", "misturando genoma por clonagem [REVISAR — STT]"),
    (r"\bplomagem assexual\b", "clonagem assexual"),
    (r"\ba entropia lacrodupa\b", "a entropia lacrou de vez [REVISAR — STT 'lacrodupa']"),
    (r"\bépoca das moedas\b", "época das moiras [REVISAR — STT 'moedas']"),
    (r"\bo nome de Enque conhecido na tradição velha\b", "o nome de Enoque conhecido na tradição védica"),
    (r"\bé aparantar. Apantaratã\b", "é Apantaratamas"),
    (r"\bficou a mí e ficou o anjo corpo lá\b", "ficou a múmia, ficou o anjo, o corpo lá [REVISAR — STT]"),
    (r"\bsaiu fertilizando al Umas dem\b", "saiu fertilizando... umas demos [REVISAR — STT]"),
    (r"\bde Apar Apantaratamas\b", "de Apantaratamas"),
    (r"\besse parachá\b", "esse Parashara"),
    (r"\bo pai de via\b", "o pai de Vyasa"), (r"\bde via\b", "de Vyasa"),
    (r"\bgerado numa del\b", "gerado numa demo"),
    (r"\bpara os delos pararem\b", "para os demos pararem"),
    (r"\bde qual fio solto vivis de Shiva\b", "de qual fio solto, de Vishnu, de Shiva"),
    (r"\bse apresentar como abajo\b", "se apresentar como avatar [REVISAR — STT 'abajo']"),
    (r"\bos versos do Ribe\b", "os versos do Rig Veda"),
    (r"\bno gramadismo\b", "no bramanismo"),
    (r"\bmistura de genética dea\b", "mistura de genética [REVISAR — STT]"),
    (r"\bÉ o mesmo de Éba\b", "é o mesmo de Éber [REVISAR — STT 'Éba']"),
    (r"\balgumas páginas do Marata\b", "algumas páginas do Mahabharata"),
    (r"\bseres hígridos\b", "seres híbridos"),
    (r"\bRenê Decart\b", "René Descartes"),
    (r"\brainho do bom senso\b", "rainha do bom senso"),
    (r"\bj com o que roda\b", "julga com o que roda"),
    (r"\bcondição Adaiva\b", "condição adhydaiva [REVISAR — STT 'Adaiva']"),
    (r"\bgerador brano\b", "gerador, Brahma não [REVISAR — STT 'brano']"),
    (r"\bcomando metal\b", "comando mental [REVISAR — STT 'metal']"),
    (r"\bavatar de virgem, Brahma\b", "avatar de Vishnu, de Brahma"),
    (r"\bencardernações\b", "encarnações"),
    (r"\butam entre elas\b", "brigam entre elas [REVISAR — STT 'utam']"),
    (r"\bBrahma não conseguiu criar batalhas\b", "Brahma não conseguiu criar [avatares estáveis] [REVISAR — STT 'batalhas']"),
    (r"\bde Deus combo\b", "de Deus [REVISAR — STT 'combo']"),
    (r"\bE esse aé significa\b", "E esse IEA significa [REVISAR — STT 'aé']"),
    (r"\bas pessoas que a gente ama, pastor\b", "as pessoas que a gente ama [REVISAR — STT 'pastor']"),
    (r"\bNós íos\b", "Nós [REVISAR — STT 'íos']"),
    (r"\bo meu eu acho hospedar\b", "o meu eu acho... hospedar [REVISAR — STT]"),
    (r"\bdesordinar a verdade\b", "discernir a verdade [REVISAR — STT 'desordinar']"),
    (r"\bNão fique tem problema\b", "Não tem problema"),
    (r"\bcom viança\b", "com Vyasa [REVISAR — STT 'viança']"),
    (r"\bessas Zeistem\b", "esses Zeus existem [REVISAR — STT 'Zeistem']"),
    (r"\ba ter sido viagem\b", "a ter sido Vyasa [REVISAR — STT 'viagem']"),
    (r"\bvivo para rabar\b", "vivi para reencarnar [REVISAR — STT 'rabar']"),
    (r"\bcom intra numa\b", "com [intra?] numa [REVISAR — STT]"),
    (r"\bvai ser pulante\b", "vai ser [REVISAR — STT 'pulante']"),
    (r"\bB is você amostra\b", "[REVISAR — STT 'B is você amostra']"),
    (r"\b4800, 48. 805 5000 poucos anos\b", "4.800, 4.805, 5.000 e poucos anos [REVISAR — STT]"),
    (r"\bse manta a alma\b", "se mantém: a alma"),
    (r"\buma face de seu filho\b", "uma face de [Vishnu] [REVISAR — STT 'seu filho']"),
    (r"\bEsse gruto Vishnu\b", "Esse [grupo?] Vishnu [REVISAR — STT 'gruto']"),
    (r"\ba narrativa que nasceu a partir de via\b", "a narrativa que nasceu a partir de Vyasa"),
    (r"\bcom a espe ação das prescrições\b", "com a [esperança?] das prescrições [REVISAR — STT]"),
    (r"\bcambója\b", "Camboja [REVISAR — STT]"), (r"\bGuadeste\b", "[REVISAR — STT 'Guadeste']"),
    (r"\bToma mais pro Dimitro Forz até supositório bandeira da China\b", "[REVISAR — STT severo]"),
    (r"\bÁbia Saudita\b", "Arábia Saudita"),
    (r"\bmomentos dificíos\b", "momentos difíceis"),
    (r"\bViver na Terra vai ser um sábado\b", "Viver na Terra vai ser um [sábado?] [REVISAR — STT]"),
    (r"\bmelhor será reiniciar o processo a arte do grupo\b", "melhor será reiniciar o processo à parte do grupo [REVISAR — STT]"),
    (r"\b200 anos de sol na terra sem sem poder verar\b", "200 anos de sol na terra sem poder [verar?] [REVISAR — STT 'verar']"),
    (r"\bProcessador nosso é a espércia\b", "Processador nosso é a [espécie?] [REVISAR — STT 'espércia']"),
    (r"\bno Narutos institutos\b", "nos [outros] institutos [REVISAR — STT 'Narutos']"),
    (r"\bnenhum tipo de cresce\b", "nenhum tipo de [crença?] [REVISAR — STT 'cresce']"),
    (r"\bcada membro pode construir o e um conjunto\b", "cada membro pode construir, e um conjunto"),
    (r"\bem cima do norte paraa movimentação\b", "em cima do norte para a movimentação"),
    (r"\bastrologia vélica\b", "astrologia védica"), (r"\bastrologia vética\b", "astrologia védica"),
    (r"\bastrologia médica\b", "astrologia védica"),
    (r"\bApóo\b", "Apolo"),
    (r"\bOs mistérios dos livros oraculares, Lucas e Tarô\b", "Os mistérios dos livros oraculares, [Lúcifer?] e Tarô [REVISAR — STT 'Lucas']"),
    (r"\bcom os indiciados\b", "com os iniciados [REVISAR — STT 'indiciados']"),
    (r"\bem giotista e com as ágas\b", "entre Jyotisha e as [águas?] [REVISAR — STT 'ágas']"),
    (r"\báguia seria engenharia\b", "[águia?] seria engenharia [REVISAR — STT]"),
    (r"\bÉ o Ed vacá\b", "É o [Ed?] [REVISAR — STT 'Ed vacá']"),
    (r"\bdesassustada\b", "desassombrada [REVISAR — STT 'desassustada']"),
    (r"\bsenhor dos seus qualitos\b", "senhor dos seus [destinos?] [REVISAR — STT 'qualitos']"),
    (r"\bParad estragado\b", "Para [definir] estragado [REVISAR — STT 'Parad']"),
    (r"\bcoisas lins\b", "coisas ruins [REVISAR — STT 'lins']"),
    (r"\bfontas e baixa você sentir\b", "[REVISAR — STT 'fontas e baixa']"),
    (r"\beu tomaria bastante pele\b", "eu tomaria bastante [cuidado] [REVISAR — STT 'pele']"),
    (r"\bVocê tem no Espírito Santo\b", "[REVISAR — STT 'Espírito Santo']"),
    (r"\bem Voches\b", "em Rochester [REVISAR — STT 'Voches']"),
    (r"\bnem a Paulo\b", "nem a pau [REVISAR — STT 'Paulo']"),
    (r"\bresícios as flechas\b", "resíduos das flechas"),
    (r"\bse eu nascer julo\b", "se eu nascer [cedo?] [REVISAR — STT 'julo']"),
    (r"\bassinatura crítica do corpo\b", "assinatura quântica do corpo [REVISAR — STT 'crítica']"),
    (r"\baí é cabe o trabalho\b", "aí é que cabe o trabalho"),
    (r"\bchama chamada Frigga\b", "chamada Frigga"),
    (r"\bfriga na mitologia norma\b", "Frigga na mitologia nórdica"),
    (r"\bAs normes ou asivas\b", "As nornes ou as moiras [REVISAR — STT 'asivas']"),
    (r"\bpara as nornes esti agora de norção\b", "para as nornes [REVISAR — STT]"),
    (r"\bàs séculas\b", "às [três] [REVISAR — STT 'séculas']"),
    (r"\bfossem repidas\b", "fossem repetidas [REVISAR — STT 'repidas']"),
    (r"\bretro e retrogradaria\b", "retroagiria"),
    (r"\bque é esse dos livros que produzido\b", "[REVISAR — STT 'que é esse dos livros que produzido']"),
    (r"\bum substanciante termo de informação\b", "um [substancial?] termo de informação [REVISAR — STT]"),
    (r"\bno século XX\b", "no século XXI"),
    (r"\bvai carbar\b", "vai [se corromper] [REVISAR — STT 'carbar']"),
    (r"\btrabalhando no EA\b", "trabalhando no IEA"),
    (r"\bumas felic\b", "umas [vitaminas?] [REVISAR — STT 'felic']"),
    (r"\bmuitos verbentes\b", "muitos verbetes"),
    (r"\bgeestacionárias\b", "geoestacionárias"),
    (r"\bcidade do arca\b", "cidade de Dwarka [REVISAR — STT 'arca']"),
    (r"\btrabalham conjuntamente cima disso\b", "trabalham conjuntamente em cima disso"),
    (r"\bnós nos Amos a espécie humana\b", "nós amamos a espécie humana [REVISAR — STT 'Amos']"),
    (r"\bI need a F down\b", "'I need a fix...' [REVISAR — STT]"),
    (r"\beu preciso de um concerto\b", "eu preciso de um conserto"),
    (r"\btá doendado\b", "tá doendo [REVISAR — STT 'doendado']"),
    (r"\bquando viaja conversando\b", "quando Vyasa conversando"),
    (r"\bque viaja fez\b", "que Vyasa fez"),
    (r"\bviaja aí espiritualmente\b", "Vyasa aí espiritualmente"),
    (r"\bfalar de viagem\b", "falar de Vyasa [REVISAR — STT 'viagem']"),
    (r"\blado del da palestra\b", "lado bom da palestra [REVISAR — STT 'del']"),
    (r"\bMas e virgem\b", "Mas e Vishnu"), (r"\bE chi\b", "E Shiva"),
    (r"\ba razão de virgem\b", "a razão de Vishnu"),
    (r"\bflechada acidental para um pouquinho do carro que ele matou\b", "flechada acidental [REVISAR — STT 'pouquinho do carro']"),
    (r"\bviaja foi enastecendo\b", "Vyasa foi [amadurecendo] [REVISAR — STT 'enastecendo']"),
    (r"\btudo que um vinculado ao espírito faz\b", "tudo que um [ser] vinculado ao espírito faz"),
    (r"\b28.869 ges\b", "28.869 genes"),
    (r"\bentão Vi ele foi\b", "Então, Vyasa, ele foi [REVISAR — STT 'Vi']"),
    (r"\bao trabalho do Paz\b", "ao trabalho de [Paz?] [REVISAR — STT]"),
    (r"\bA banda cita também\b", "A banda [cita?] também [REVISAR — STT]"),
    (r"\btudo foi seulado\b", "tudo foi [selado] [REVISAR — STT 'seulado']"),
    (r"\bcada humanda\b", "cada um anda [REVISAR — STT 'humanda']"),
    (r"\bUm manda é o serviço do contribu\b", "[REVISAR — STT 'serviço do contribu']"),
    (r"\bprocesso dea com esses 20\b", "processo de decifração com esses 20 [REVISAR — STT]"),
    (r"\besse gurburinho\b", "esse [burburinho] [REVISAR — STT 'gurburinho']"),
    (r"\bEssa turma de viagem não brigaram\b", "Essa turma de Vyasa não brigou [REVISAR — STT 'viagem']"),
    (r"\bÉ igual Juna\b", "É igual Arjuna"),
    (r"\bSão filhos de do tio Dadá\b", "São filhos do tio [Dadhika?] [REVISAR — STT 'Dadá']"),
    (r"\bDadá é o Darast\b", "[REVISAR — STT 'Dadá é o Darast']"),
    (r"\binoculado do DNA\b", "inoculado no DNA"),
    (r"\ba microparte que nos quer fazer\b", "a microparte que nos [coube] [REVISAR — STT]"),
    (r"\bela vai por uma alquímica\b", "ela vai por uma [via] alquímica [REVISAR — STT]"),
    (r"\blama menos enameada\b", "lama menos [emanada?] [REVISAR — STT 'enameada']"),
    (r"\bQuem manda é marca\b", "Quem manda é Maria"),
    (r"\bNão vai ter mais negócio de mal sair levando para ter o valor\b", "[REVISAR — STT 'mal sair levando']"),
    (r"\bAcho eu acho que eu Marcos e Simon\b", "Acho que eu, Marcos e Simon [REVISAR — STT]"),
    (r"\bsó pra gente situar, isso aqui tem\b", "só pra gente situar: isso aqui tem"),
    (r"\bA primeira doutora que descobriu o Covid-19 fora da China\b", "A primeira doutora que descobriu a Covid-19 fora da China"),
    (r"\bpior que o COVID\b", "pior que a COVID"),
    (r"\b40 e 70% dos infectados\b", "40 e 70% dos infectados [REVISAR — quarentena clínica]"),
    (r"\b50 vírus desse\b", "50 vírus desses"),
    (r"\bproblemas ambientais saem ferrando\b", "os problemas ambientais saem ferrando"),
    (r"\bmissá\b", "missão [REVISAR — STT 'missá']"),
    (r"\bDiritarastra\b", "Dhritarashtra"), (r"\bGandari\b", "Gandhari"),
    (r"\bcursoos cauras\b", "Kauravas"), (r"\b199 com 1001\b", "[REVISAR — STT '199 com 1001']"),
    (r"\bSimp nasceu\b", "[Símio?] nasceu [REVISAR — STT 'Simp']"),
    (r"\bApan[dt]ar ?Tamas\b", "Apantaratamas"),
    (r"\bmais próximo a Javel\b", "mais próximo a Javé"),
    (r"\bque complicação aquiaracha\b", "que complicação [REVISAR — STT 'aquiaracha']"),
    (r"\bSuca não teve continuidade\b", "Suka não teve continuidade"),
    (r"\bEsse cara aqui é um cego\b", "Esse cara aqui é um cego [Dhritarashtra]"),
    (r"\bdando botinada\b", "dando botinada [REVISAR — STT]"),
    (r"\bele procurou principalmente o parachara\b", "ele procurou principalmente o Parashara"),
    (r"\besse parachar é uma maluquíssimo\b", "esse Parashara é [uma maluquice] [REVISAR — STT 'maluquíssimo']"),
    (r"\bDNA da MED de Enoque\b", "DNA da [mídia?] de Enoque [REVISAR — STT 'MED']"),
    (r"\bele ousva como\b", "ele se [mostrava] como [REVISAR — STT 'ousva']"),
    (r"\bera um Jesus\b", "era um Jesus [comparação]"),
    (r"\bNesse povo mistiçado\b", "Nesse povo mestiçado"),
    (r"\bera mais um mistiro\b", "era mais um mestiço"),
    (r"\bsó paim teria nascido\b", "só [Krishna] teria nascido [REVISAR — STT 'paim']"),
    (r"\bos cinco filhos de Pampo\b", "os cinco filhos de [Pandu] [REVISAR — STT 'Pampo']"),
    (r"\ba rainha Plut\b", "a rainha [Kunti] [REVISAR — STT 'Plut']"),
    (r"\bPaul era a questão do dma\b", "[Pau?] era a questão do dharma [REVISAR — STT]"),
    (r"\ba questão da honra dma\b", "a questão da honra, do dharma"),
    (r"\bEle veio de virgem\b", "Ele veio de Vishnu"),
    (r"\bmas não dizia veio do GR\b", "mas não dizia veio do [quarto logos] [REVISAR — STT 'GR']"),
    (r"\bcomportamento bem parecido com o que os sátilos tinham\b", "comportamento bem parecido com o que os sátiros tinham"),
    (r"\bde trip trip\b", "[REVISAR — STT 'de trip trip']"),
    (r"\bAr um pouco os defeitos\b", "[a]r um pouco os defeitos [REVISAR — STT]"),
    (r"\brúdio, satírico\b", "rúdio, satírico [REVISAR — STT 'rúdio']"),
    (r"\bEle tinha disfador\b", "Ele tinha disfarce [REVISAR — STT 'disfador']"),
    (r"\bnão está sua disse\b", "não está, [disse] [REVISAR — STT]"),
    (r"\bmas é de mim, é de é do meu eu ser assim\b", "mas é de mim, é do meu eu ser assim"),
    (r"\bAí via disse\b", "Aí Vyasa disse"),
    (r"\bentão via Krishna, eles trocavam figurias\b", "então Vyasa e Krishna trocavam figurinhas"),
    (r"\bprincipalmente via e Krishna aprenderam com esse parachar\b", "principalmente Vyasa e Krishna aprenderam com esse Parashara"),
    (r"\bEssa essa figura tá desencarnada esse parachar\b", "Essa figura tá desencarnada, esse Parashara"),
    (r"\bVai voltar nessa época\b", "Vai voltar nessa época"),
    (r"\bO filho de de Asa teve três filhos\b", "O filho de [Parashara] teve três filhos [REVISAR — STT 'de Asa']"),
    (r"\bPandu, diria e suca\b", "Pandu, [Dhritarashtra] e Suka [REVISAR — STT 'diria']"),
    (r"\bVias foi quem escreveu para barato\b", "Vyasa foi quem escreveu o Mahabharata"),
    (r"\bparte dos curantes\b", "parte dos Puranas [REVISAR — STT 'curantes']"),
    (r"\bescreveu o Rig V\.\b", "escreveu o Rig Veda"),
    (r"\bEsildo chama amor solta membros\b", "[REVISAR — STT 'Esildo chama amor solta membros']"),
    (r"\ba missigenação\b", "a miscigenação"),
    (r"\bmistura erva de seres humanos\b", "mistura [híbrida] de seres humanos [REVISAR — STT 'erva']"),
    (r"\bbiodemo\b", "biodemos"),
    (r"\bo espírito de Joquã foi nazalé\b", "o espírito de Joctã [REVISAR — STT 'nazalé']"),
    (r"\bE o espírito de que viria ser Roché\b", "E o espírito de quem viria ser Rochester"),
    (r"\bfoi nazalé, filho de Enoque escrever\b", "foi [nascido?], filho de Enoque escrever [REVISAR — STT]"),
    (r"\bnos vitimando\b", "nos vitimando"),
    (r"\bpara manter já vivo\b", "para manter [Javé?] vivo [REVISAR — STT 'já']"),
    (r"\bDeus foi\b", "[REVISAR — STT 'Deus foi']"),
    (r"\bA vida de todos nós é de forma\b", "A vida de todos nós é [dessa] forma [REVISAR — STT]"),
    (r"\bEu me chamo na espiritualidade brincando palhaço\b", "Eu me chamo na espiritualidade, brincando, palhaço"),
    (r"\bque entra os palhaços\b", "que entram os palhaços"),
    (r"\bela vai o palhaço para para chamar\b", "vai o palhaço para chamar"),
    (r"\bO espírito da gente, infelizmente ferra os ceros\b", "O espírito da gente, infelizmente, ferra os [zeros?] [REVISAR — STT 'ceros']"),
    (r"\bNenhum espírita aqui se procura\b", "Nenhum espírita aqui se procura [REVISAR — STT]"),
    (r"\bquando eu nascer e tenta Rogério e Renato\b", "quando eu nascer e [encarnar] Rogério e Renato [REVISAR — STT]"),
    (r"\bhoje existe Rogério Renato há 100 anos atrás\b", "hoje existe Rogério; Renato, há 100 anos atrás,"),
    (r"\bo nosso espírito sabia nem que era Rogério Renato\b", "o nosso espírito sabia nem que era Rogério [ou] Renato"),
    (r"\bjá traçaram planos para vida e Rogério Renato que deu certo errado\b", "já traçaram planos para a vida, e Rogério [ou] Renato deu certo [ou] errado [REVISAR — STT]"),
    (r"\bpercebiu que você botou todo mundo dentro da barr\b", "percebeu que você botou todo mundo dentro da barriga [REVISAR — STT]"),
    (r"\bMas fala ficando galinha\b", "[REVISAR — STT 'fala ficando galinha']"),
    (r"\bdentro da que ano é\b", "dentro da [barriga], que ano é [REVISAR — STT]"),
    (r"\bÉ a foto\b", "É a foto [REVISAR — STT]"),
]

def aplicar(txt):
    for pat, rep in REPL:
        txt = re.sub(pat, rep, txt)
    return txt

# ============ 2. CARGA ============
def carregar_unidades():
    u = {}
    for linha in FONTE.read_text(encoding="utf-8").splitlines():
        if linha.startswith("U") and "\t" in linha:
            cod, _, texto = linha.partition("\t")
            u[cod] = texto.strip()
    return u

def paragrafos_de(faixa, unidades):
    texto = aplicar(" ".join(unidades[k] for k in faixa))
    frases = re.split(r"(?<=[.!?…])\s+", texto)
    paragrafos, atual = [], ""
    for f in frases:
        if len(atual) + len(f) > 330:
            paragrafos.append(atual)
            atual = f
        else:
            atual = (atual + " " + f).strip()
    if atual:
        paragrafos.append(atual)
    return [p for p in paragrafos if p.strip()]

# ============ 3. CABEÇALHO ============
CABECALHO = """@titulo: Vyasa e o Descortinar de um Novo Paraíso
@autor: Jan Val Ellam
@data: 23/01/2021
@local: não informado (transmissão remota)
@subtitulo: Apostila de estudo — Transcrição editada integral, com correção gramatical e terminológica, organização temática e notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da palestra de 23/01/2021 (fonte P2021-01-23), organizada tematicamente em 12 PARTES para estudo — **palestra inédita na base e fonte original** do detalhamento de Vyasa (RC-585), das Moiras/Nornes (RC-467), dos "fios soltos" da Trimurti, de Parashara, da Escola de Decifração e das três setas de Moros (RC-454). Preservamos a voz, os marcadores orais, o humor e as digressões do autor; corrigimos apenas erros claros de transcrição automática (STT), com nota na primeira ocorrência, seguindo as grafias canônicas da Base Terminológica RC (Vyasa, Parashara, Apantaratamas, Moiras/Nornes, Moros, Enoque, Metatron, Trimurti, Brahma, Vishnu, Shiva, Krishna, Sophia, Mahabharata, Mohen So, método druida, Kardec etc.). Passagens duvidosas do STT ficam marcadas como [REVISAR]. Os **2 intervalos** (café; 15 minutos) estão marcados no corpo do texto, e as **3 perguntas finais da plateia** aparecem isoladas em seção própria (PARTE XII) e **não compõem a ontologia**. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, históricas, culturais, clínico-científicas e políticas são **leitura de Ellam, não consenso validado** — em especial: "tudo que até hoje nós seres humanos pensamos sobre paraíso está absolutamente furado"; "nenhum dos seres que tratamos como Deus é de fato Deus"; a leitura da genética humana (28.869 genes; quatro segmentos genéticos), da evolução do cérebro e das projeções sobre vírus pós-COVID (quarentenas estritas; apenas a interpretação do autor). A palestra passou por re-curadoria (Dossiê + Devolutiva do curador, 20/08/2026 — O-1 a O-7 aprovados): auditoria confirmada; **16 fichas ampliadas**; obra "Nem Deus, nem Javé, nem Darwin: a evolução do cérebro" cadastrada como **B082**; **nenhum código novo consumido** (base blindada em 770 termos).
"""

# ============ 4. ESTRUTURA (titulo, U-início, U-fim-exclusivo, [(ancora, subtitulo)]) ============
PARTES = [
    ("PARTE I — A Abertura: Uma Palestra Chata, Mas Necessária", "U0001", "U0030", [
        ("Mas assim, essa palestra de hoje", "## Uma palestra chata, mas necessária"),
        ("Mas logo de saída eu vou dizer", "## O contexto e o marco temporal encarnatório"),
        ("Por falar em pergunta", "## Perguntas e arquivos: o que não pode ser aprofundado"),
        ("Seu DNA se alinha", "## A resignação e a remontagem do criador"),
    ]),
    ("PARTE II — Os Fios Soltos: a Queda do Criador", "U0030", "U0075", [
        ("Então, pra gente iniciar", "## A metáfora do poste e dos fios"),
        ("Quando o criador caiu", "## Bilhões de fios soltos"),
        ("Todos os fiozinhos soltos", "## Moros e a transmissão limpa"),
        ("E o que são fios soltos", "## O que são fios soltos"),
        ("O assunto é chato", "## O celular de advogado"),
    ]),
    ("PARTE III — As Moiras/Nornes: Herdeiras dos Fios Soltos", "U0075", "U0120", [
        ("Então pessoal, qual é o drama", "## Três seres que não são mulheres"),
        ("Esses três seres que hoje se entendem", "## Os herdeiros dos fios soltos"),
        ("Então, as moiras ou as nornes, elas funcionam", "## O computador-GPS das assinaturas quânticas"),
        ("Ainda assim, Vishnu e Shiva conseguiram", "## O drama dos avatares da Trimurti"),
        ("A única linha que vincula o ano 2021", "## As três flechas de Moros"),
        ("E dos seres maravilhosos", "## A única lógica capaz de tratar dos assuntos"),
    ]),
    ("PARTE IV — O Paraíso Furado e os Três Reinos da Antiguidade", "U0120", "U0200", [
        ("Nós temos que entender que o ser humano", "## O ser humano, peça do jogo da criação"),
        ("Então assim, regra número um", "## Regra número um: não definir o que se entendeu"),
        ("Então, pessoal, conceitos como Deus", "## Desenraizar conceitos do psiquismo"),
    ]),
    ("PARTE V — Adão e Eva: a Aposta entre Javé e Vishnu", "U0200", "U0450", [
        ("A coisa chegou nesse ponto", "## A entropia e a produção de informação"),
        ("A irracionalidade foi produzida", "## A irracionalidade e os fios soltos"),
        ("Há tempos atrás eu falei", "## O episódio de Adão e Eva"),
        ("Quando Brahma ou Javé viu", "## Shiva no sul da Índia"),
        ("Aí Vishnu disse para ele", "## A aposta: \"eu aposto meu poder contra esses seres\""),
        ("Sobrou de Enoque", "## Enoque, o corpo de Metatron e o \"big data\""),
        ("E é nesse contexto", "## O cataclismo de 14.000 anos"),
        ("Então, quando Noé tentou reorganizar", "## Noé e os portais"),
        ("tudo que a gente imaginar de Oriente", "## Os quatro segmentos genéticos da humanidade"),
        ("desde o tempo de Adão, Caim foi", "## As Américas: a descendência de Caim"),
        ("O que é que eu conto no livro", "## A descendência até Éber"),
    ]),
    ("PARTE VI — Noé, os Segmentos Genéticos e o Nome Brahma", "U0450", "U0525", [
        ("Éber tem dois filhos", "## Joctã e Faleg: a recusa da linhagem"),
        ("Na altura do tempo de Faleg", "## A vingança de Javé"),
        ("Quando ele viu que a linhagem", "## Javé se apresenta aos arianos como Brahma"),
        ("Só que a linhagem de Jafé", "## Linhagens, anjos e demos dos portais"),
        ("É nesse ponto aqui que surge a figura", "## A entrada de Vyasa na cena"),
        ("O pai de Vyasa, chamado Parashara", "## Parashara: a astrologia védica e o Rig Veda"),
        ("Mas entendam, essa turma aqui era humana", "## Os demos se tornando sexuados"),
        ("Nós estamos falando aqui de uma parte do período", "## O período dos hiperbórios"),
        ("E é sobre esse período aí que eu não vou poder responder", "## Fios soltos e a exceção de Maria Helena"),
        ("Todos nós participamos de quê", "## O aviso do intervalo"),
    ]),
    ("PARTE VII — Enoque (Apantaratamas), Parashara e Vyasa", "U0525", "U0576", [
        ("Então assim, Vyasa foi neto", "## Apantaratamas, o nome védico de Enoque"),
        ("Cerca de uns 9.000 anos depois", "## O DNA de Enoque [REVISAR — quarentena]"),
        ("Tamas é energia de Shiva", "## Parashara, o gênio"),
        ("A astrologia védica", "## A astrologia védica e os critérios de avatar"),
        ("Até então não existia conhecimento", "## O Rig Veda e a assinatura quântica"),
        ("Então, pessoal, eu vou mostrar", "## A necessidade de uma escola de entendimento"),
        ("Por quê? Aí a gente volta", "## Descartes e o bom senso"),
        ("Então a gente vai dar uma parada", "## INTERVALO — o café"),
        ("15 minutinhos de intervalo", "## INTERVALO — 15 minutos"),
    ]),
    ("PARTE VIII — Pós-Intervalo: Portais, Colégios Druídicos e Kardec", "U0576", "U0750", [
        ("Bem, vamos lá", "## Os portais e o fechamento de 21/12/2012"),
        ("Eu terminei de ler um livro", "## Steven Weinberg e o anacronismo"),
        ("E aí existia uma mistureba", "## A mistura de seres e a sexualização dos demos"),
        ("Nós falamos que antes do dilúvio", "## A herança de Enoque e a cisão patriarcal"),
        ("Quando isso aconteceu", "## Tuatha de Danann e milesianos"),
        ("Os fatos complexos começaram", "## A necessidade de interpretar os eventos"),
        ("Vyasa teve a ideia de criar", "## O grupo de 20 (de 250 a 21)"),
        ("Nesse ponto foi que surgiu", "## O Jyotisha de Parashara"),
    ]),
    ("PARTE IX — Vyasa e o Grupo de 20: a Escola de Decifração", "U0750", "U0820", [
        ("E desse tipo de contato surgiu", "## O método druida: \"busca pela verdade\""),
        ("Vyasa tava retomando essa ideia", "## Kardec e o espírito de Zéfiro (Rochester)"),
        ("Quando Vyasa estava retomando", "## O método druida entre os mestiços"),
        ("E segundo a tradição bramânica", "## A promessa de Vishnu e a aposta"),
        ("Nas entrevinhas", "## O Jyotisha como arquivo dos fios"),
        ("E falando claramente", "## A Escola de Decifração e o IEA"),
        ("Quando Javé se frustrou com Jesus", "## O anúncio do IEA: \"esclarecer os 270 mundos\""),
        ("E é isso que tá fazendo", "## A escola de decifração: o sonho do processo"),
        ("Eu não imaginava que nessa vida", "## O trabalho com os verbetes"),
    ]),
    ("PARTE X — Krishna, o Mahabharata e a Invenção da Prosa", "U0820", "U1050", [
        ("Então a gente vai fazer", "## A \"bagunça organizada\" da Escola de Decifração"),
        ("Vocês não fazem ideias de quantas noites", "## Do fogo de 250 às fogueiras de 21"),
        ("Quando Vyasa, filho de Parashara", "## A cena de Brahma: a aprovação do Mahabharata"),
        ("Isso aqui é o seguinte", "## A prosa: inovação de Vyasa e Parashara"),
        ("conversa de Krishna com Arjuna", "## Krishna e Arjuna: o Bhagavad Gita"),
        ("alguém percebeu no big data", "## Pandavas e Kauravas"),
        ("Por entendam", "## O DNA de Enoque e o apoio de Krishna"),
        ("Então, Krishna, ele muitas vezes", "## Parashara: mais de 10.000 anos"),
        ("Então, Krishna, ele para todo mundo", "## O mestiço de pele azul"),
        ("Mas Krishna tem um detalhe", "## O comportamento satírico de Krishna"),
        ("Vyasa disse uma vez para ele", "## A troca entre Vyasa e Krishna"),
    ]),
    ("PARTE XI — O Novo Paraíso e o Biocosmos Emergente", "U1050", "U1300", [
        ("O senhor Krishna morou mais de 10.000 anos", "## Krishna em Dwarka"),
        ("A única coisa que está em pé hoje", "## A informação limpa de infecção: o IEA"),
        ("E aquela música", "## Os palhaços do circo"),
        ("Então, pessoal, quando Vyasa conversando com Krishna", "## \"Se isso aqui for paraíso, vamos inventar outro\""),
        ("Porque na medida em que Vyasa foi", "## A assinatura quântica e os 28.869 genes"),
        ("Aí depois que Vyasa fez isso", "## Institutos de busca e decifração no Oriente"),
        ("É mais ou menos a frase", "## \"Quem manda é Maria...\""),
        ("Então, pessoal, essa história da percepção", "## A percepção de que havia algo errado com os deuses"),
        ("Não, mas ou seja, a vida humana", "## A vida humana como palhaçada"),
        ("O paraíso não é muito ético", "## A meritocracia do paraíso"),
        ("Então nós próprios já estamos criando", "## O Biocosmos emergente"),
        ("E essa história começou com Vyasa", "## Sophia e Zeus: o problema do final de 2020"),
        ("O espírito que me anima apenas ativou Rogério", "## O espírito que anima: Vyasa [relato pessoal]"),
        ("Não, veja só, ela tava viva nessa época", "## Maria Helena, a vanguarda do novo paraíso"),
        ("Acho que eu, Marcos e Simon", "## A criação do B a partir do A"),
        ("Mas a gente não pode se preservar", "## O compromisso com o processo"),
        ("Nós vamos ter que criar um novo fio", "## O novo fio: parte biodêmica, parte humana"),
        ("A única coisa boa construída nessa história", "## A narrativa de Vyasa"),
        ("Eu não sei se vocês sabem", "## Projeções e vírus [REVISAR — quarentena clínica]"),
        ("Viver na Terra vai ser um", "## Tempos difíceis pela frente"),
        ("Mas a internet que ainda dá espaço", "## A internet e a espiritualidade"),
        ("Então o que nós tivermos edificado", "## O material da Revelação Cósmica"),
        ("E é um processo, repito", "## Um processo sem autoridade"),
        ("Então nós vamos nos vitimando", "## A programação encarnatória"),
        ("Eu acho que daqui pra frente não vai ter mais nem isso", "## Daqui pra frente: o grupo"),
    ]),
]

# ============ 5. MONTAGEM ============
def main():
    unidades = carregar_unidades()
    linhas = [CABECALHO]

    for titulo, ini, fim, secoes in PARTES:
        chaves = [k for k in unidades if ini <= k < fim]
        paras = paragrafos_de(chaves, unidades)
        linhas.append(f"\n# {titulo}\n")
        # localizar posição de cada âncora
        alvos = []
        for ancora, subtitulo in secoes:
            a = ancora[:42].lower()
            achou = None
            for i, p in enumerate(paras):
                if a in p.lower():
                    achou = i
                    break
            if achou is None:
                print(f"!! ÂNCORA NÃO ENCONTRADA [{titulo[:24]}]: {ancora[:45]}")
                continue
            alvos.append((achou, subtitulo))
        # inserir em ordem (decrescente de índice para não deslocar)
        alvos.sort(key=lambda x: x[0], reverse=True)
        for idx, subtitulo in alvos:
            paras.insert(idx, subtitulo)
        linhas.extend(f"> {p}" if not p.startswith("##") else p for p in paras)
        linhas.append("")

    # ---------- PARTE XII (especial: perguntas isoladas) ----------
    def bloco(faixa):
        return "\n".join(f"> {p}" for p in paragrafos_de(faixa, unidades))

    p1 = [k for k in unidades if "U1300" <= k <= "U1301"]
    r1 = [k for k in unidades if "U1302" <= k <= "U1310"]
    p2 = [k for k in unidades if "U1311" <= k <= "U1324"]
    r2 = [k for k in unidades if "U1325" <= k <= "U1347"]
    p3 = [k for k in unidades if "U1348" <= k <= "U1353"]
    r3 = [k for k in unidades if "U1354" <= k <= "U1372"]
    fim = [k for k in unidades if "U1373" <= k <= "U1404"]

    linhas.append("\n# PARTE XII — Perguntas da Plateia e Encerramento\n")
    linhas.append("## Pergunta 1 — A astrologia védica tem função hoje?\n")
    linhas.append("*Pergunta da plateia:*\n")
    linhas.append(bloco(p1) + "\n")
    linhas.append("**Resposta de Jan Val Ellam:**\n")
    linhas.append(bloco(r1) + "\n")
    linhas.append("## Pergunta 2 — Jyotisha e Vedanga (matemática e engenharia védicas)\n")
    linhas.append("*Pergunta da plateia (o STT embaralhou a fala: a pergunta foi anunciada antes de um aparte de Ellam sobre Zeus, Apolo e os oráculos — U1311–U1321):*\n")
    linhas.append(bloco(p2) + "\n")
    linhas.append("**Resposta de Jan Val Ellam:**\n")
    linhas.append(bloco(r2) + "\n")
    linhas.append("## Pergunta 3 — O espírito de Marcos/Rochester e as moiras\n")
    linhas.append("*Pergunta da plateia:*\n")
    linhas.append(bloco(p3) + "\n")
    linhas.append("**Resposta de Jan Val Ellam** (inclui Frigga/Aran e as três setas de Moros):\n")
    linhas.append(bloco(r3) + "\n")
    linhas.append("## Encerramento — A Revelação Cósmica e o Perspectivismo\n")
    linhas.append(bloco(fim) + "\n")

    # ---------- GLOSSÁRIO ----------
    linhas.append("""## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Vyasa | RC-585 | termo-título; ampliado (fonte original) |
| Moiras / Nornes / Parcas | RC-467 | ampliado (fonte original) |
| Elm (Moros) | RC-454 | ampliado (fonte original — transmissão limpa; três setas) |
| Enoque | RC-489 | ampliado (Apantaratamas; promessa de Vishnu) |
| Metatron | RC-671 | ampliado (corpo especial) |
| Revelação Espiritual (Kardec) | RC-190 | ampliação retida (sem ficha física) |
| Novo Paraíso / Paraíso B | RC-612 | tema-título; ampliado |
| Mente Universal (Emergente) | RC-163 | ampliação retida (sem ficha física) |
| Trimurti | RC-104 | ampliada (fios soltos) |
| Javé | RC-001 | ampliado (aposta; Abel; Brahma) |
| Vishnu (Mavatna) | RC-135 | ampliação retida (sem ficha física) |
| Shiva (Savna) | RC-102 | ampliado (sul da Índia) |
| Krishna | RC-414 | ampliado (avatar cachava; Dwarka) |
| Mahabharata | RC-593 | ampliado (fonte original — prosa; versões) |
| Mohen So | RC-081 | ampliado (fios soltos de Brahma e Shiva) |
| Jainismo / antigo Druidismo | RC-759 | ampliado (método druida) |
| Anunnakis | RC-024 | ampliado (quatro segmentos genéticos) |
| Brahma (Brajna) | RC-037 | contexto (Javé→arianos como Brahma) |
| Revelação Cósmica (conceito) | RC-094 | ampliada (Escola de Decifração) |
| Fatiamento de Consciência | RC-604 | ampliado (fios soltos) |
| Wyrd / Urd | RC-658 | contexto (teia do destino) |
| Teia quântica | RC-559 | contexto (Moiras) |

### B. Conceitos desta palestra absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Fios Soltos | RC-604 / RC-467 / RC-104 | herança genético-informacional truncada do criador caído; "a história morre ali" |
| Parashara | RC-585 | pai de Vyasa, neto de Enoque; gênio da astrologia védica (Jyotisha) |
| Escola de Decifração | RC-094 / RC-585 | o grupo de 20 (250→21); o método druida; o IEA como continuidade |
| As Três Setas de Moros | RC-454 | quando reencontradas, a história retroagiria ao momento zero |
| Apantaratamas | RC-489 | nome védico de Enoque; "Tamas é energia de Shiva" |
| Frigga / Aran | RC-467 | ajudou as Nornes a tecer até as três setas se consumarem |
| Jyotisha / Vedanga | Colecionar Incertezas | astrologia/matemática védica; critérios de avatar |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

Vyasa ("Viaza/Viasa"); Parashara ("Parachara"); Apantaratamas; o DNA de Enoque fertilizando demos e minérios; "avatar cachava" (Krishna); "Brama Mestre"/"avatar de Brahma"; "Méxica"; "o espírito que me anima foi Vyasa" (relato pessoal — U1153); "Parashara viveu mais de 10.000 anos" e "vai voltar nessa época" (U1040–U1050); a aposta Javé×Vishnu marcada no DNA de Enoque; "Faleg = espírito de Rochester"; "a quarta região genética (Américas) = descendência de Caim"; as três setas de Moros; "o trabalho se zera a partir de agora" (marco 2020/2021); projeções de vírus pós-COVID (40–70% infectados); 28.869 genes; Zeus e Apolo criando os oráculos; obra "Nem Deus, nem Javé, nem Darwin: a evolução do cérebro" (B082).

### D. Quarentenas aplicadas

- **Teológica (crítica):** "tudo que até hoje nós seres humanos pensamos sobre paraíso está absolutamente furado"; conceitos de Deus/paraísos/sentido de vida "a desenraizar do psiquismo"; Javé "assassino de Abel"; "nenhum dos seres que tratamos como Deus é de fato Deus" — leitura de Ellam, não fato.
- **Clínico-científica:** 28.869 genes e assinatura quântica do DNA; vacinas e vírus pós-COVID; genética dos quatro segmentos humanos; evolução do cérebro — leitura do autor, jamais dado validado.
- **Político-social:** Trump/Bolsonaro e a "pós-verdade"; crítica à astrologia e aos oráculos (Zeus/Apolo); colonização de Marte — leitura do autor.
- **Falas da plateia:** as 3 perguntas finais estão isoladas e não compõem a ontologia da Base.
""")

    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    n_pal = sum(len(l.split()) for l in linhas if not l.startswith(">"))
    n_cit = sum(len(l.split()) for l in linhas if l.startswith(">"))
    print(f"apostila.md: {len(linhas)} linhas | citações ~{n_cit} palavras | texto editorial ~{n_pal} palavras")

if __name__ == "__main__":
    main()
