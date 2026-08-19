#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Amplia fichas existentes com a seção '## Ampliação — P2026-07-25'
(Devolutiva D-6 aprovada em 19/08/2026). Insere antes de '## Fontes'."""
from pathlib import Path
import re

P = Path(__file__).resolve().parent.parent / "termos"

AMP = {
"RC-072": """- **Missão recusada:** esperava-se de Jesus um super-Messias que dominasse as 70 linhagens para entregá-las a Javé e ao conselho (criar super exército judeu, livrar-se do jugo romano); Jesus recusou ("meu pai e vírgula" — STT de "pai e vírgula" [REVISAR] — ver inseminação abaixo).
- **Gênese:** inseminação artificial em Maria feita por Hochmah/Sophia (RC-565; RC-009) — DNA de Sophia + DNA de Maria; o eu de Jesus "ficou balançando" entre ser o Messias e não dominar ninguém.
- **Os 500 passos (Evangelho de Bartolomeu, absorvido na devolutiva):** na cruz, Jesus invadiu o Tártaro (RC-286), aprisionou Hades/Reides e Belial (RC-479) e libertou os espíritos presos desde Adão — ato tipificado como **crime contra a Timé** (RC-293) → processo aberto sem resolução; penalidade recaiu sobre Sophia (RC-009).
- **Jó número dois:** dignidade na submissão — "Javé tava pisando em Jesus e Jesus ainda assim com dignidade".
- **Ectoplasma:** o eu encarnado usa a condutora do corpo (STT "condaline" [REVISAR]) para produzir ectoplasma — "desencarnado, ninguém faz isso".
- **Cruzamento devolutiva:** RC-647 (Evangelho de Judas) relacionado (narrativas gnósticas da Paixão).""",

"RC-009": """- **"Sophia não é nome — é epíteto"** (personificação de um tipo de sabedoria); os membros do conselho são "personificações diversas de Sophia" (eus de Emá/Ensá).
- **Origem:** criada no 2º conselho, logo após Dev/Aurora e Cama/Kama; corpo "engendrado para jamais morrer, para durar enquanto este universo durar".
- **Suzerana do universo biológico:** representante do conselho neste universo; "você tá cuidando aí do nosso gado, mas não pense que esse gado é seu" (gado = humanidade); os seres que criou invadiram sua descendência.
- **Penalização:** perdeu o direito de herdeira do legado trimurtiano por ter produzido o avatar Jesus que descumpriu a missão; "a Sofia biológica tá fora" do conselho.
- **Krishna impede a vinda:** medo da perda total da devoção humana (2 bilhões de muçulmanos + 2 bilhões de adoradores de Krishna); vinda = "festival de naves" (quarentena ufológica).
- **Consórcio:** humanos + Sophia (RC-720) — "somos todos sócios e parceiros de um destino"; vinda como "finalização de uma etapa".""",

"RC-474": """- **Três conselhos (esqueleto da palestra):** 1º Trimurti (deuses primevos, ~4 bi anos) → 2º Dev/Aurora + Cama/Kama + descendência trimurtiana → 3º Dinastia das Sophias/Conselho dos 70 (com os humanos).
- **Eloim/Elohim (RC-004):** variação usada na fala; 70 clãs de descendentes do dilúvio (Gênesis 11/Torre de Babel; Deuteronômio; Septuaginta; Manuscritos do Mar Morto; Talmud; Midrach).
- **Função declarada:** manter o criador caído vivo; "os conselhos servem a Javé".
- **Lógica não humana:** nenhum membro pensa como humano; únicos candidatos humanos: Jesus (rejeitado) e Saibaba (não quis entrar).
- **Crise:** "dias contados" — universo vizinho colapsando, sem novos membros, seres de Ensá saindo, Krishna alinhado ao inevitável; transição: arcontes nascendo como humanos.""",

"RC-293": """- **Ritos de passagem** (absorvido na devolutiva): mudança de status instituída entre os arcontes (porteiro do portão do céu, toga do STF, coroa) — "esses seres que não obedecem a nada obedecem a isso".
- **Crime de Jesus:** agredir a Timé de um arconte é crime no conselho — Jesus invadiu o Tártaro (Timé de Hades e Belial) → processo aberto contra Jesus, sem resolução até hoje.
- **Aumento de Timé:** cada ser que assumia assento no conselho dos 70 tinha a Timé aumentada — motivo de guerras e perseguição a humanos (ex.: Apolo obrigado a "se livrar" de jogadores humanos).""",

"RC-414": """- **Rama e a sinarquia (RC-584):** ordem de reinar na Terra respeitada pelos arcontes; destruída pela guerra de Kurukshetra entre as famílias que mantinham a dinastia.
- **Criação de Krishna:** CFD dos três senhores da Trimurti para servi-los; "se achou maior que os três e de fato era" — obrigou a Trimurti a venerá-lo; crise geral no conselho (últimos ~5.000 anos).
- **Perda do corpo Adhyajna (RC-016):** maldição da rainha Gandhari (STT "Gandares"; esposa de Dhritarashtra — STT "Diriarastra") no Mahabharata → Krishna perde a forma de arconte clássico (ser astralizado).
- **Caitanya Mahaprabhu (STT "Caetânia Mahaprabu"):** revitalizou o culto a Krishna ([REVISAR] "século X" — cronologia interna; Caitanya é tradicionalmente séc. XV/XVI).
- **Zoroastro:** a disputa Ahura Mazda × Arimã (STT "Urazda") = brigas Brahma×Krishna e Jesus×Krishna (leitura do autor).
- **Geopolítica da devoção:** manipula a epifania; Índia como reino terrestre (18h diárias de adoração); templos bramânicos → vaishnavas.
- **Decisão recente:** teria conversado com Shiva e "baixado as armas mentais", alinhando-se ao inevitável — abertura para a vinda de Sophia; o autor declara confiança "muito modesta" (informação recebida por canais que não pode pôr em dúvida; "Krishna desde a semana passada").""",

"RC-476": """- **Apresentado pela primeira vez em B068 (O Funeral da Evidência):** o espírito que produziu Brahma, Vishnu e todos os descendentes, inclusive Sophia e Jesus — "100% responsável por tudo que está acontecendo no caos".
- **Consciência fatiada:** os 70 membros do conselho dos arcontes são eus representativos da consciência fatiada de Emá (e de Ensá, RC-477).
- **Fellini:** o autor abre B068 com um filme de Fellini em que alguém grita "De quem é a culpa? De quem é a culpa?" — "De quem é a culpa por a gente existir?".
- **Não é Deus:** "nem EMÁ é um Deus, é só um espírito que criou um problemaço".""",

"RC-489": """- **67 anos:** "aos 67 anos de idade" foi levado (dois anjos de Javé; "você foi escolhido"); 300 anos convivendo com Javé; voltou e ditou ao filho Matusalém os 366 livros (RC-672); foi levado de novo e investido de "um macão vibratório" → Metatron (RC-671); "nunca mais voltou à condição humana".
- **Anafiel e Raziel (RC-485):** levaram Enoque na primeira ida a Arabot-Ráquia; "todos os habitantes do entorno de Javé perceberam o cheiro dele mesmo à distância".
- **Testemunha de acusação:** Javé queria Enoque como testemunha contra a humanidade transviada pré-diluviana no "julgamento geral" (demência de Javé).""",

"RC-671": """- **Enfraquecimento:** "quando Enoque morreu, o que restou dele feito Metatron passou a existir como um tipo de ser que só circunstancialmente era acionado pela força dos três senhores da Trimurti" — o Metatron que sobrou é "só um pouco do que era de fato".
- **"Desse aqui eu cuido, vocês não se metam":** Javé defendia Metatron frente aos arcontes; com o enfraquecimento, os anjos perdem a disputa política contra a dinastia dos arcontes.
- **Plano falhado:** Javé não pôde usar Metatron para dominar a humanidade → Vishnu propõe o avatar Jesus (via Sophia).""",

"RC-658": """- **Unificação Wert (decisão estrita da devolutiva):** a grafia "Wert" (STT da palestra: teia da vida criada por Moros/Olog no tempo do 1º conselho) é desvio fonético — **não vira termo autônomo**; absorver e unificar exclusivamente como **Wyrd/Urd**.
- **Função na palestra:** "a partir da Wert, o que saía de um ser voltava para ele ao invés de contaminar todo mundo" — estabilização da comunicação entre os seres daiva (ver RC-559 Teia quântica).
- **Processador da teia:** na Hipóstase dos Arcontes, o processador da teia da vida (Wyrd/Moiras/Nornas) mostra os cenários dos destinos dos arcontes — os arcontes "se ficaram loucos" quando Noreia recebeu de Eleleth as notícias sobre o destino deles.""",

"RC-559": """- **Ampliação P2026-07-25:** a "Teia da vida" do 1º conselho (criada por Moros) é descrita na palestra como "Wert" [STT] — unificada em RC-658 (Wyrd) por decisão da devolutiva; este termo permanece como o princípio "o que sai de um ser volta para ele" (karma quântico da RC).""",

"RC-630": """- **Metamorfose:** "na cultura deles não rola um papo entre dois humanos... se Rogério e Mateus fossem daiva, a cada minuto um se transforma numa coisa, com personalidade diferente" — comunicação via "linha ressonante".
- **Anjos clones:** a condição daiva surgiu quando um anjo clone despertou, confrontou Brahma, perdeu o corpo ígneo e o corpo mental virou daiva; "seres do paraíso mergulharam dentro dessa criação maluca e assumiram essa condição daiva" (dezenas de milhões de seres daiva; quase 1 bilhão de seres ígneos).
- **Daiva ≠ diabólico:** "não são diabólicos, são demoníacos no sentido de que seus corpos se metamorfoseiam".
- **Formas de Javé (RC-001):** ígneo → daiva → Fenvã (RC-769) → biológicas (cuscuta, cefalópodes, dragonoide, humano).""",

"RC-037": """- **Bipartição:** sob o desejo criado por Cama (RC-622) via Aurora (RC-475), Brahma se divide em dois: o "Brahma podre de sempre" + "Braminha Júnior tetracéfalo" (4 faces) — versão Fenvã (RC-769).
- **Geração regenerada (RC-696):** da mente: Atri, Marichi, Pulastya, Pulaha, Kratu; do corpo tetracéfalo: Bhrigu e Daksha (RC-701) — Daksha gerou 69 filhas (13 últimas; Olímpicos e Titãs; "Ira" [REVISAR] produziu as plantas, inclusive a cuscuta).
- **Formas:** cuscuta (1ª vegetal), cefalópodes (3 corações, 9 cérebros — "investimento nos invertebrados"), dragonoide, tentativa humana.
- **Senhor Brahma Parameshthi:** a face humana de Brahma, descrita por Vyasa (STT "Viaza") no Mahabharata (STT "Marrabarata") — "cerca de 270 mundos que observam o que se passa na Terra" (RC-265).
- **Comas:** Javé/Brahma ficava milhões de anos apagado, mantido pelos anjos clones; colapso atual "ano 2020 e alguma coisa" (RC-001).""",

"RC-001": """- **Formas assumidas (cronologia da palestra):** corpo ígneo de plasma → condição daiva → cuscuta → cefalópodes → dragonoide → tentativa humana (Senhor Brahma Parameshthi) — "o eu de Javé foi sendo essas coisas todas".
- **Demência e coma:** ficava milhões de anos apagado; os anjos clones mantinham a forma dele viva; colapso do corpo humano "ano 2020 e alguma coisa" (cronologia interna: 2021).
- **Epítetos gnósticos:** Samael (cego), Saklas (ignorante), Ialdabaoth (blasfemador), Sabaoth — todos Javé (RC-482); antes da queda: Pistis Sophia (RC-530) = Prabrajna (RC-152).
- **"Eu fiz e eu carrego":** resposta aos anjos ministradores (RC-485), reproduzida por Isaías.""",

"RC-696": """- **Gerações regeneradas (P2026-07-25):** Brahma criou uma geração regenerada da sensação mental (Atri, Marichi, Pulastya, Pulaha, Kratu) e outra do corpo tetracéfalo (Bhrigu, Daksha) — unidas para criar o mundo biológico.""",

"RC-701": """- **69 filhas de Daksha:** as últimas 13 deram origem a Olímpicos e Titãs; duas dessas 13 → os olimpianos/titãs; uma delas ("Ira" [REVISAR]) produziu todas as plantas, inclusive a cuscuta (STT da palestra P2026-07-25).""",

"RC-475": """- **Primeiro ser feminino:** surgiu da cólera de todos os deuses do 2º conselho ("a energia raivosa de todos os seres presentes... convergiu para a pessoa de Brahma") — princípio da externalização (RC-768); "surgiu nua e a turma, que nunca tinha visto nada nem parecido, ficou olhando".
- **Poder apagado:** "o componente feminino produziu tudo... e isso foi absolutamente apagado" (fariseus, viúva enterrada viva com o marido — crítica do autor a costumes).
- **Relevância:** "é impressionante o poder que essa Deusa Dev ou Aurora tem nessa história" — origem do 2º conselho.""",

"RC-622": """- **Cama = Kama (STT "Cama"):** egrégora do desejo criada por Vishnu a partir da influência de Aurora — "eu tenho em mim essa força que Vishnu criou vindo de Aurora"; flecha do cupido/Eros; Cama Sutra (referência do autor); desejo que rompe a desconfiança entre os deuses.""",

"RC-104": """- **1º conselho dos deuses (deuses primevos):** ~4 bilhões de anos após o Big Bang; Trimurti "três inderrotáveis" (ninguém mata o outro); "manicômio... mas tem três malucões"; pacificação da descendência; criação da teia da vida (Wyrd/RC-658) por Moros.
- **Sucessão de conselhos:** 2º com Dev/Aurora e Cama/Kama; 3º dinastia das Sophias (RC-494) — ver RC-474.""",

"RC-584": """- **Sinarquia (absorvida na devolutiva):** ordem de reinar na Terra criada por Rama, respeitada pela dinastia dos arcontes; "não conseguiu ir adiante" — destruída pela guerra de Kurukshetra (ver RC-414).""",

"RC-722": """- **Kant e Sócrates:** Kant — dignidade = aderir aos próprios valores e viver com coerência ("a sua insignificância se torna uma bomba atômica"); Sócrates (RC-406) — recusa da corrupção (fuga da prisão): "prefiro morrer a me sujar".
- **Pulsação digna (absorvida):** a pulsação que sai de um ser humano detém "todas as senhas de abertura de portais interdimensionais"; emite fragrância ao entrelaçamento quântico dos elétrons (metáfora do autor).
- **Cisne negro (RC-192):** a dignidade como "o pior cisne negro" para os arcontes — não conseguem entender um ser que dá a vida por honra.""",

"RC-192": """- **Cisne Negro (absorvido na devolutiva — metáfora epistemológica):** aquilo que o ser humano julga impossível e que, ao se revelar, provoca choques de realidade; a mitologia como "o grande cisne negro da história humana"; a RC como "porrada de cisnes negros"; "bem-vindos ao Clube do Cisne Negro" (P2026-07-25). Metáfora de despertar ligada à pílula vermelha; nota em RC-702 (Camuflagem da Realidade).""",

"RC-702": """- **Nota P2026-07-25:** o "cisne negro" (absorvido em RC-192) é a chave da camuflagem: a realidade se camufla sob a crença de que o impossível não existe; os véus "se decerram" quando o eu se autodescobre (pulsação digna — RC-722).""",

"RC-647": """- **Cruzamento P2026-07-25:** junto ao Evangelho de Bartolomeu (absorvido em RC-072), compõe o corpus gnóstico da Paixão citado na palestra (Jesus ressuscitado instruindo discípulos).""",

"RC-086": """- **Pandora e Zeus (P2026-07-25):** "Pandora criou os humanos e Zeus ficou pé da vida" (queria destruir os animais de estimação de Epimeteu/Prometeu); humanos racionais surgiram "ao longo dos últimos 48.000 anos"; a morte passou a existir com a vida biológica — e os eus mentais passaram a ser aprisionados no Tártaro (RC-286).""",

"RC-727": """- **Noreia (RC-579):** a linhagem Pandora–Eva–Noreia reaparece na Hipóstase dos Arcontes — Noreia, filha de Eva, "pura de caráter", que recebeu de Eleleth o destino dos arcontes; a palestra indica que esse "ser espiritual vivo vai começar a nascer na terra agora" (ver quarentena de gênero).""",

"RC-265": """- **Parameshthi (P2026-07-25):** "o senhor Brahma Parameshthi... cerca de 270 mundos que observam o que se passa na Terra" (Vyasa/Mahabharata) — alinhado ao registro do Zohar (RC-265).""",

"RC-655": """- **Renovação do Ifá (P2026-07-25):** "Javé ou Obatalá pediu a Orumilá para criar revelação de Ifá para que os povos da África fossem devotos de Obatalá, de Orumilá, de Olodumaré, para que Cristo não dominasse os povos da África" — geopolítica da devoção (absorvida em RC-474).""",

"RC-666": """- **Obatalá = Javé (P2026-07-25):** "Jafé ou Obatalá pediu a Orumilá para criar revelação de Ifá" (STT "Jafé/Jahé") — renovação do Ifá como contramedida à expansão de Krishna na África.""",

"RC-582": """- **Monstros de Vishnu e Shiva (P2026-07-25):** Ravana (10 cabeças; decepava uma a cada 1.000 anos pensando em Brahma — arrancava fórmulas de poder) e Hiranyakashipu (STT "Iraniakashipu") foram criados para enfraquecer Brahma e saíram do controle — "pandemônio que dissolvia o conselho".""",

"RC-672": """- **P2026-07-25:** Enoque ditou os 366 livros ao filho Matusalém entre as duas subidas; Javé queria Enoque como testemunha de acusação contra a humanidade pré-diluviana.""",

"RC-674": """- **P2026-07-25:** com a morte de Enoque, Metatron se enfraquece — a "urdidura" perde a sagacidade que Enoque lhe emprestava; os anjos perdem a disputa frente à dinastia dos arcontes.""",

"RC-106": """- **P2026-07-25:** Arabot-Ráquia (RC-495) situa-se no Brahmaloka — "uma morada no Brama Loca, onde há uma grande base laboratorial"; Shekinah como nave antimaterial que une os dois universos.""",

"RC-274": """- **P2026-07-25:** a vinda de Sophia é tratada como "finalização de uma etapa" — contexto da cápsula do tempo (João).""",

"RC-720": """- **Távola Redonda (absorvida na devolutiva):** o Rei Artur como símbolo dos sonhos humanos de viver com dignidade; "um conselho universal, uma távola redonda instalada no paraíso por espíritos humanizados"; consórcio humanos + Sophia — "somos todos sócios e parceiros de um destino".""",

"RC-579": """- **Eleleth (STT "Elelf/Elelet"):** anjo (não arconte) que explica a Noreia a origem e o destino do poder dos arcontes — "os arcontes não sabem da história deles e não sabem do destino deles"; o único que sabe é Moros (RC-454); a revelação a uma humana (Noreia) enfureceu os arcontes ("ferraram com a vida de Noréa").
- **P2026-07-25:** "um ser espiritual vivo que vai começar a nascer na terra agora tentando refazer o papel" — ver quarentena de identidade de gênero.""",

"RC-454": """- **Sabe o destino dos arcontes (P2026-07-25):** "o único ser que sabe do destino deles é Moros... nunca se sentou nesse conselho, nunca quis ser dono de alguma coisa, nunca se submeteu à Trimurti".
- **Criou a teia da vida (Wert [STT] → Wyrd, RC-658):** "a teia foi criada por Moros/Olog... a partir da Wert, o que saía de um ser voltava para ele".
- **Hipóstase dos Arcontes (RC-770):** Moros é um dos personagens-chave do livro gnóstico.""",

"RC-665": """- **P2026-07-25:** "a revelação de Ifá e Orunmilá — o coqueiro que existiu em Orum": um pé de coqueiro surgiu primeiro em Orum/Irém (universo vizinho), ser vivo, sofisticando-se até produzir o coco — transferido para este universo (coco verde).""",

"RC-261": """- **P2026-07-25:** "Javé se sentiu novamente traído e, por isso, introduziu a Cabala (ou 'acabalá' [STT])" — como contramedida à expansão de Krishna na Europa.""",

"RC-732": """- **P2026-07-25:** "externalizaram lá tudo que tinha para ser externalizado... jogaram o problema todo para cá" ao tempo da emergência da espécie humana (últimos ~25.000 anos) — reforça o termo; genoma como "joia" disputada (ver RC-518).""",

"RC-748": """- **P2026-07-25 (referência marginal):** o padrão de "gentileza/dominação" mencionado na palestra permanece em quarentena — sem novos dados nesta fonte.""",
}

n = 0
for cod, conteudo in AMP.items():
    alvo = None
    for f in P.glob(f"{cod}-*.md"):
        alvo = f
        break
    if not alvo:
        print(f"!! ficha {cod} não encontrada")
        continue
    txt = alvo.read_text(encoding='utf-8')
    if "## Ampliação — P2026-07-25" in txt:
        print(f"!! {cod} já ampliada")
        continue
    secao = f"\n## Ampliação — P2026-07-25\n\n{conteudo.strip()}\n"
    if "## Fontes" in txt:
        txt = txt.replace("## Fontes", secao + "\n## Fontes", 1)
    else:
        txt = txt.rstrip() + "\n" + secao + "\n---\n"
    alvo.write_text(txt, encoding='utf-8')
    n += 1
print(f"fichas ampliadas: {n}")
