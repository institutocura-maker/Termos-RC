#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO PACOTE DE AMPLIAÇÕES — P2021-05-15 (ferramenta de ciclo).

Princípio: **eu não digito citações.** Cada aspa deste pacote nasce de uma ÂNCORA
(subsequência curta que eu garanto existir na fonte); o script devolve a SENTENÇA
inteira da fonte que contém a âncora, recortada byte a byte de `original.txt`.
É impossível, assim, citar de memória, inverter palavra ou "melhorar" o autor.

Formato de saída (lido por `_aplicar_ampliacoes_P2021-05-15.py`):

    ### RC-XXX
    - **[P2021-05-15 · RÓTULO]** "sentença verbatim"; "sentença verbatim" — NOTA EDITORIAL
      (a nota fica sempre FORA das aspas).

Âncora não encontrada = erro e o bloco não é emitido. O pacote nunca contém
citação que a fonte não tenha dito.
"""
import re, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
FONTE = os.path.join(CICLO, "original.txt")
SAIDA = os.path.join(AQUI, "_ampliacoes_P2021-05-15.txt")

src = open(FONTE, encoding="utf-8").read().replace("\r\n", "\n")
# sentenças com offset — o offset devolve o endereço U#### (linha lógica do TXT bruto,
# a mesma numeração de `camada-0.txt`), para a citação nascer já endereçada.
_starts = [0] + [k + 1 for k, ch in enumerate(src) if ch == "\n"]
import bisect
def u_of(pos):
    return "U%04d" % bisect.bisect_right(_starts, pos)
_pontos = [0] + [m.end() for m in re.finditer(r"(?<=[.!?])\s+", src)] + [len(src)]
SENT, OFF = [], []
for a, b in zip(_pontos, _pontos[1:]):
    bruto = src[a:b]
    s = bruto.strip()
    if len(s) > 3:
        SENT.append(s)
        OFF.append(a + (len(bruto) - len(bruto.lstrip())))
KEY = [re.sub(r"[^0-9a-zA-ZÀ-ÿ]+", " ", s).strip().lower() for s in SENT]

def frase(ancora):
    a = re.sub(r"[^0-9a-zA-ZÀ-ÿ]+", " ", ancora).strip().lower()
    hits = [i for i, k in enumerate(KEY) if a in k]
    if not hits:
        raise LookupError(ancora)
    i = hits[0]
    s = SENT[i]
    if len(s) > 1400:
        s = s[:1400].rsplit(" ", 1)[0] + "…"
    return s, u_of(OFF[i])

def aspas_internas(s):
    """Declaração de fidelidade: as aspas duplas QUE JÁ EXISTEM na fonte viram «…»,
    porque senão quebram o portão A (paridade) do verificador. Nenhum caractere do
    dito é alterado — só o sinal de aspas."""
    if '"' not in s:
        return s
    out, aberto = [], False
    for ch in s:
        if ch == '"':
            out.append("«" if not aberto else "»"); aberto = not aberto
        else:
            out.append(ch)
    if aberto:
        out.append("»")
    return "".join(out)

def aspas(lst):
    saida, vistos = [], set()
    for a in lst:
        s, u = frase(a)
        if s in vistos:                       # duas âncoras na mesma sentença = uma citação só
            continue
        vistos.add(s)
        saida.append('"%s" (%s)' % (aspas_internas(s), u))
    return "; ".join(saida)

BLOCOS = {
"RC-464": [
 ("A MATERIALIZAÇÃO — a ficha existia só no cadastro (B060); a fonte oral de 15/05/2021 a fundamenta",
  ["a deusa Danana é a deusa inana", "toatas quer dizer seguidores"],
  "⚠️ Divergência SEM FUSÃO com B060: aqui Inana não é «deusa da terra» nem «mãe dos Tuatha» — é a neta e amante de Anu a quem os *tuatha* (seguidores) devem o nome; a direção da equivalência se inverte."),
 ("O PODER E O CICLO DE 3.600 ANOS",
  ["Anu tinha uma neta chamada Inana", "assim avô e Népta se tornaram amantes"],
  None),
 ("A DATAÇÃO ORAL DO PODER DE INANA",
  ["Essa figura teve um poder absolutamente grande"],
  "⚠️ [TEXTO CORROMPIDO no STT] na frase que antecede («na verdade é Inana e neta de Essa figura»): preservar como está, não decodificar."),
 ("OS MIL NOMES E OS DEVOTOS (Q&A U0007)",
  ["O segundo nome mais importante de Inana é ISAR", "essas figuras todas eram devotos de Inana"],
  "[REVISAR: «ISAR» ≈ ISHTAR; «Senequiribe/Senequaribe» = Senaqueribe, grafia oscilante na própria fonte.]"),
 ("ONTOLOGIA: nem demo, nem extrafísica — e a recusa do panteão nórdico",
  ["era uma extraterrestre, não era um ser extrafísico", "Na nórdica isso não é muito claro"],
  None),
 ("A VIRADA POLÍTICA A FAVOR DA HUMANIDADE",
  ["Nana chegou a uma conclusão que os seres humanos viveram bem melhor", "sempre atrapalhou Javé e usou Eva e Lilif"],
  "⚠️ quarentena religiosa na menção a Eva/Lilif; não equiparar «Lilif» a Lilith sem decisão do Curador."),
 ("ANU × ZEUS: A GUERRA INTERNA QUE ENFRAQUECE E NÃO MULTIPLICA",
  ["já que o Zanuna defendiu a tese", "E se enfraqueciam, não se multiplicavam"],
  None),
 ("A ORIGEM: NETA DE ANU, NASCIDA EM NIBIRU, VINDA À TERRA",
  ["É neta de Anô", "o Anon Chic é quem nascia em Nibiro e Nanau na terra"],
  "[REVISAR: «Anon Chic» = STT para Anunnaki; «Nanau» ≈ Inana/Anu — grafias da fonte preservadas.]"),
],
"RC-068": [
 ("A PALESTRA INTEIRAMENTE DEDICADA AO TEMA (a fonte mais completa da taxonomia)",
  ["as etnias, as espécies que nos definiram são exatamente essas", "são seis, basicamente, as principais parcelas ou componentes"],
  None),
 ("O CRITÉRIO DO SEXO: demobios assexuados × demobiol sexuados",
  ["aqueles seres descendentes de Odim, os Aesir e Vanir", "eu chamo de Demobiol, porque muitos deles"],
  "⚠️ A fonte distingue DEMOBIO de BIODEMO («um padrão diferente dos biodemos»): não fundir com RC-036/RC-186; a equação demol↔demobio é decisão do Curador."),
 ("A TRIMÚRTI EXCLUÍDA POR NÃO TER PISADO NAS ILHAS",
  ["Eles nunca colocaram o pé deles em nenhuma dessas ilhas"],
  None),
 ("AS SEIS COMPONENTES E A JANELA 40.000→10.000",
  ["A essas duas se associaram o quê", "aproximadamente uns 30.000 anos de muita importância situada entre"],
  None),
 ("A CAUSA DO POVOAMENTO: A BRIGA QUE NÃO PODIA SE FIXAR",
  ["E e por isso essa hibridagem", "o pacto que muitas das estirpes"],
  None),
 ("THULE: AS GRAFIAS ORAIS DO NORTE",
  ["lá no Polo Norte existia um lendário continente", "nesse grande continente de Lu"],
  "Grafias preservadas como ouvidas (Tul / Thu / Tool / Tur ≈ Thule). **Thule não vira termo** (Devolutiva O-8)."),
 ("O MAPA: 72 ETNIAS → 14 CARAVANAS → ESCANDINÁVIA/GRÃ-BRETANHA/IRLANDA",
  ["Essas ilhas, elas tinham aproximadamente umas umas 72 etnias", "cada nome desses representa um dos segmentos das 14"],
  None),
 ("O CATACLISMO E A CHEGADA DOS TUATHA",
  ["quando essas eh etnias se viram todas em perigo de morte devido ao cataclismo", "Exatamente aí é que ficava essas 72 civilizações"],
  None),
 ("O QUE A HUMANIDADE HERDOU DELAS",
  ["os humanos herdaram a porcaria dessa criação", "Repito, por incompetência da tribúcia"],
  "⚠️ RETIRADA: a frase «o que nós vivemos de ruim de espiritualidade hoje é um decalque», citada no dossiê, NÃO existe neste bruto (contaminação de memória do agente). Nada foi aplicado em nome dela."),
 ("OS PROTÓTIPOS «MUITO BONS» E O LIMITE",
  ["produziram sim protótipos muito bons", "O único problema é que todos eles tinham um grande fator de herança"],
  "⚠️ quarentena étnica no uso de «tipo ideal» (camada-2 §5)."),
 ("O LIVRO IMPOSSÍVEL",
  ["não há livro nenhum do mundo e nunca mais"],
  None),
],
"RC-024": [
 ("TIPOLOGIA: «OS ANUNNA NÃO SÃO FARINHA DO MESMO SACO»",
  ["O ser humano, todos nós somos farinha do mesmo saco, mas os anuna não são"],
  None),
 ("O EGITO COMO BASE GEOPOLÍTICA PÓS-DILUVIANA",
  ["os anunacos foram obrigados a fazer uma opção de vida geopolítica planetária", "os anunques deixaram a sua força maior em torno do Egito"],
  None),
 ("O RETORNO A NIBIRU HÁ 2.600 ANOS (e o novo aparecimento «daqui a uns 1000 anos»)",
  ["alguns voltaram eh para Nibir 2600 anos atrás", "vão aparecer aqui de novo os deibir daqui a uns 1000 anos"],
  "[REVISAR: «os deibir».] ⚠️ Divergência SEM FUSÃO: a base fixa a retirada «por volta de ~600 a.C.» [P2021-03-27]; 2.600 anos antes de 2021 ≈ 579 a.C. — convergência parcial, **não identidade**."),
 ("A EXPULSÃO POR CONTAMINAÇÃO, NÃO POR DERROTA",
  ["terminou expulsando eles da Terra"],
  None),
 ("ANU × ZEUS: QUEM TINHA SENSO CRÍTICO",
  ["O Zeus não tinha a consciência crítica que Anu tinha", "esqueceu de olhar pra descendência"],
  None),
 ("A INEFICIÊNCIA COMO CAUSA DA HERANÇA HUMANA",
  ["Os humanos herdaram a porcaria dessa criação"],
  None),
 ("OS ANUNNAKI EM MARTE, NA LUA E NAS NAVES DOS SIRIANOS",
  ["terminaram também ocupando Marte e Lua"],
  "⚠️ quarentena ufológica."),
],
"RC-587": [
 ("O PREDOMÍNIO DE ANU NAS ETNIAS HIPERBÓREAS (o dado que faltava à ficha)",
  ["o Deus que mais tinha prestígio, o Deus que mais era reverenciado"],
  None),
 ("A VISITA PERIÓDICA À TERRA",
  ["ela quando a nu vinha a Terra cada cerca de 3600 anos"],
  "⚠️ a mesma cifra de 3.600 anos serve aqui para a periodicidade da vinda, não só para a órbita; o autor a relativiza no Q&A (ver RC-589)."),
 ("O SENSO CRÍTICO E A LEITURA DA PRÓPRIA VANTAGEM",
  ["Anu tinha um senso crítico e na época de fato ele dominava a situação", "algo de estranho parecia estar ocorrendo nas moradas"],
  None),
 ("A ENDOGAMIA ANUNNAKI ATRIBUÍDA A ANU",
  ["já que o Zanuna defendiu a tese"],
  None),
 ("O PONTO CEGO: A DESCENDÊNCIA DOS DOIS FILHOS",
  ["esqueceu de olhar pra descendência de seus dois filhos"],
  None),
],
"RC-486": [
 ("FOXP2 DADO PARA QUE SE APRENDESSE A LINGUAGEM DOS ANUNAX",
  ["lá atrás quando quis transformar a humanidade numa humanidade que aprendesse a linguagem"],
  None),
 ("A CRIAÇÃO DO TIPO RACIONALIZADO A PARTIR DO DNA DE ENKI",
  ["Quando enk junto com essa sua irmã e com Ning Ningicida"],
  "[REVISAR: «Ning Ningicida, que é o deus Thor» é quarentena histórica — não decodificar.]"),
 ("A ADVERTÊNCIA SOBRE O CÉREBRO DELES",
  ["os que detém não é o mesmo do nosso tipo"],
  None),
 ("ADAPA: A VIDA ENCURLADA POR MEDO",
  ["encurtou mais ainda a genética do ser humano", "Porque diferente do Adão movido, escolhido por Javé"],
  None),
 ("A FONTE ERUDITA NOMEDADA (a lenda de Adapa)",
  ["uma delas se chama a lenda de Adapa"],
  "[REVISAR: «bibliotecas da antiga capital de Min» = STT provável para Nínive; manter a grafia da fonte na apostila.]"),
 ("OS DOIS FOXP2 (Q&A U0006)",
  ["o gene da cognição Fox P2 dos descendentes", "É um mesmo genoma"],
  None),
 ("O PAR ADÃO/ADAPA COMO DIAGNÓSTICO DO PRESENTE",
  ["o adapa em que ano ainda é um padrão de genética que está presente"],
  "⚠️ T-11: a fonte põe Adão e Adapa juntos na janela de ~49.000 anos; a base selou Pandora ~49.000 × Eva/Adão ~22-23.000 [P2025-02-22]. Selar, **não fundir**."),
],
"RC-487": [
 ("A GRAFIA FUNDIDA NO STT («Enquenil»)",
  ["quando Nerginta, filho de Enquenil"],
  "⚠️ «Enquenil» = fusão de STT entre Enki e Enlil; a linha canônica separa os dois clãs. Não decodificar o nome do pai nem o do filho."),
 ("O CLÃ NAS BOMBAS",
  ["outras figuras aí do clã Hen Lil"],
  None),
],
"RC-460": [
 ("«MARDUR» NA BRIGA QUE GEROU AS BOMBAS",
  ["terminaram saltando bombas de uma briga com Mardur"],
  "⚠️ Divergência SEM FUSÃO: a base descreve a guerra como disputa «pelo controle de terras raras» [P2022-12-17]; aqui é narrada como briga de clãs, sem menção a terras raras. Selar as duas leituras."),
],
"RC-461": [
 ("A IRMÃ-CO-AUTORA DA CRIAÇÃO RACIONALIZADA",
  ["Quando enk junto com essa sua irmã e com Ning Ningicida"],
  None),
 ("OS FILHOS DE ANU A FAVOR DE JAVÉ (a 1ª vez que a fonte diz isso)",
  ["eles criaram um outro tipo de ser humano também racionalizado"],
  "⚠️ RETIRADA NESTE CICLO (declaração de engano): a frase que o dossiê atribuiu a esta fonte — «os dois filhos de Anu, os dois genéticos que trabalharam a favor de Javé» — NÃO existe no `original.txt` de 15/05/2021. Era contaminação de memória. O T-13 não se aplica e nada foi aplicado em nome dele; a ficha mantém a linha B060 sem essa inflexão."),
],
"RC-583": [
 ("A LOCALIZAÇÃO EM DUAS FRANJAS (SINAI + SIDIM)",
  ["soltaram bombas atômicas no Vale do Sinai e no Vale do Sidim"],
  "Vale do Sidim ✓ canônico (B031); «Vale do Sinai» é o acréscimo desta fonte. Sodoma/Gomorra entram como pista geográfica, não como juízo teológico."),
 ("A MECÂNICA DO FIM: A POEIRA NUCLEAR",
  ["as bombas que eles soltaram para resolver o problema"],
  "⚠️ Divergência de etiologia SEM FUSÃO: a base tem «Expulsão: por ordem de Javé» [P2023-12-02]; aqui é autoexílio por contaminação. Manter as duas."),
 ("OS ATORES COM A GRAFIA ORAL",
  ["quando Nerginta, filho de Enquenil"],
  "[REVISAR]."),
 ("A MEMÓRIA DE UMA FALA ANTERIOR (radar de acervo)",
  ["que foi aquilo que a gente falou numa numas palestras meses atrás"],
  "«fonte não localizada» — Devolutiva O-8; não criar vínculo."),
],
"RC-589": [
 ("A AUTOCORREÇÃO DO AUTOR SOBRE A ÓRBITA (material raro de história do pensamento)",
  ["se modificava a cada vez que ele passava próximo ao sistema solar"],
  None),
 ("O ESTADO DA OBSERVAÇÃO EM 2021 (Q&A)",
  ["nós só vamos ter certeza desses fatos quando nós tivermos telescópios", "você deveria observar Nibiro"],
  None),
 ("A CRÍTICA À ARROGANÇA CIENTÍFICA (sem elevar Nibiru a fato)",
  ["Só que alguns cientistas pecam pela arrogância e falam como se soubessem", "assisti a discussão de Zé Cars astrônomos"],
  "[REVISAR: «Zé Carity / Zecaria City / Zacas City / Robert Bv / Graham Hancock» — nomes como ouvidos pelo STT; a fonte não os grafou por extenso, não decodificar.]"),
 ("O CONTEXTO ASTRONÔMICO CITADO (com [REVISAR] e quarentena científica)",
  ["Até pouco tempo atrás, Plutão era um planeta considerado assim", "Saturno e Júpiter com as suas 81 e 72 luas"],
  "[REVISAR: «nuvem de Earth» ≈ nuvem de Oort; «SEDA» ≈ Sedna.] ⚠️ as luas são dadas como cifra viva pelo próprio autor («constantemente se descobre e se atualiza o número»)."),
 ("QUARENTENA UFOLÓGICA (a frase que não se amplia)",
  ["tem grupos de cientistas conversando com a Nunx escondido"],
  "[STT: «a Nunx» ≈ os Anunnaki.] Registro apenas."),
],
"RC-036": [
 ("O CRITÉRIO ANATÔMICO: O BIODEMO NÃO TEM OSSO",
  ["Então quer dizer que Sofia como ser biodemo, não tem osso", "Os biodemos surgiram a partir de Sofia"],
  None),
 ("O QUE OS BIODEMOS NÃO PODIAM SOZINHOS",
  ["os biodemos sozinhos iam se prestar"],
  None),
 ("A RETIRADA PÓS-DILUVIANA: A ILHA QUE SE MOVE",
  ["Porque a essa altura a turma de Alto Langron continuou existindo"],
  None),
 ("✅ RESOLUÇÃO DO [REVISAR] DA FICHA (Devolutiva O-8 de 28/08/2026)",
  [],
  "A ficha carregava desde P2020-08-08 a grafia «ALTA LANGRON» como protótipo mais avançado dos biodemos. Esta fonte repete a forma («Alto Langron») e lhe dá contexto (a ilha móvel entre Irlanda e Islândia). **Resolução aprovada:** forma correspondente = ALT´LAM GRON (RC-018) / ALT´LAM (RC-017). ⚠️ A equivalência é decisão do Curador, não demonstração fonética; registrar como leitura oficial."),
],
"RC-049": [
 ("O PROBLEMA DEMO COMO HERANÇA QUE INVIABILIZA",
  ["O único problema é que todos eles tinham um grande fator de herança"],
  None),
 ("A AUSÊNCIA DE DUALISMO MORAL",
  ["Eles não tem esse tipo de dualismo na cabeça"],
  None),
 ("O PACTO DAS ESTIRPES DE DEMO ANTIGA",
  ["o pacto que muitas das estirpes de demo antiga"],
  None),
],
"RC-631": [
 ("O LIMITE DOS DEUSES É A ARQUITETURA DO CÉREBRO",
  ["eles compreenderam isso primeiro nos cérebros que não tinham crânio", "não tem toda a riqueza de curvas e de idas e vidas"],
  None),
 ("A TENTATIVA DE EXPANSÃO E O EXEMPLO DO POLVO",
  ["os testes realizados na tentativa de expansão da capacidade dos potenciais cerebrais", "O único exemplo que eles têm de expansão de um cérebro nos moldes"],
  "[REVISAR: «o povo» = polvo no STT; «os ardinianos» é ininteligível — não decodificar.]"),
 ("A DECISÃO NÃO-AUTÔNOMA DE SOFIA",
  ["Nessa época ainda havia ordens de tribur em cima de Sofia"],
  None),
 ("O QUE A EXPANSÃO PREJUDICOU",
  ["isso prejudicou, Sofia, isso prejudicou muitos seres"],
  None),
],
"RC-632": [
 ("A ANTERIORIDADE (2021) DA TESE QUE A FICHA DE 2024 CONSAGROU",
  ["Tudo que Sofia pode fazer para evoluir a sua condição de radiata é pegar a organ"],
  "⚠️ [TEXTO CORROMPIDO no STT: «pegar a organ a partir de a de»]. Nota de anterioridade, **sem retrodatação** da ficha (Devolutiva O-8)."),
 ("O LIMITE OPERACIONAL DECLARADO NO Q&A",
  ["Só a importação de organoides ou de sequências genéticas tiradas diretamente do ser humano"],
  None),
 ("POR QUE NÃO HÁ ATALHO BILATÉRIO",
  ["seria uma outra espécie e não dá para esperar isso"],
  None),
],
"RC-771": [
 ("A FORMULAÇÃO ORAL ANTERIOR AOS DOCUMENTOS DE 2025",
  ["Se lembra que eu tenho falado que quando os produto de Aáon"],
  "⚠️ grafias orais: «Aáon» (≈ Aáon/Awaymaion), «Virgno e Morrenç» (≈ Vishnu/Morren So), «Pachu Pathiba» (≈ Pasupati), «Hawaiingan» (≈ Havaingã/Awaylengan). **Não renomear nada na Base.**"),
 ("O EFEITO DO ENCONTRO: O CÉREBRO BILATÉRIO E O HUMANO COMO ÚLTIMO",
  ["É que surgiu a questão do cérebro bilatério", "porque ele é produto da evolução de tudo que veio desse momento"],
  "⚠️ T-14: a cifra «900, 1 bilhão de anos» nesta fonte qualifica o encontro dos produtos, não o surgimento do Homo sapiens; não confundir com a linha dos 197 mil anos (B061) nem com P2025-07-18. Selar, não fundir."),
],
"RC-499": [
 ("A GRAFIA ORAL DO FORNO E O SEU ADMINISTRADOR",
  ["que é o forno de replicação"],
  "⚠️ «de vidre» é lido pela linha da base como FORRAGEM (B061). Mantida a grafia da fonte + [TEXTO CORROMPIDO]; a decisão de grafar «forragem» continua pendente."),
],
"RC-500": [
 ("A INSTABILIDADE GRÁFICA CONFIRMADA POR ESTA FONTE",
  ["desse momento em que se uniram as conquistas evolutivas"],
  "A fonte grafa o nome «Aamaion» nesta linha e «Aáon» noutra passagem do mesmo bloco — evidência a mais de que a família «Almaior/Alamaior/Aáon/Aamaion» é campo de instabilidade de STT, não termos distintos. Nada a corrigir na ficha (que é de advertência)."),
],
"RC-102": [
 ("SIVA COMO ADMINISTRADOR DO SEGUNDO FORNO — E O «JAMAIS» NAS ILHAS",
  ["Eles nunca colocaram o pé deles em nenhuma dessas ilhas"],
  "⚠️ quarentena religiosa/hinduísta: as grafias orais da Trimúrti nesta fonte («Brama, virgem e chiva») **não** substituem as grafias canônicas da Base."),
],
"RC-104": [
 ("A TRIMÚRTI COMO MOTOR DA DISPUTA (e sua ausência física na Terra)",
  ["os descendentes de primeira, segunda e terceira ordem dessa trimurte"],
  None),
 ("LILA COMO REGRA DE CONDUTA GEOPOLÍTICA",
  ["da sua regra de conduta chamada Lila"],
  "[RC-075 Lila não tem ficha — o dado fica neste bloco e na apostila.]"),
 ("A INEFICIÊNCIA DAS FORÇAS DO UNIVERSO VIZINHO",
  ["nenhum desses seres nunca conseguiu sair das suas moradas"],
  None),
],
"RC-585": [
 ("VYASA, O 1º A SISTEMATIZAR (a 2ª atestação, 2 meses depois da P2021-01-23)",
  ["eu falei que Viaza foi o primeiro a conseguir organizar uma mesma história", "aprenderam a sistematizar o conhecimento histórico"],
  None),
 ("A FINALIDADE DA SISTEMATIZAÇÃO: A BUSCA DA VERDADE",
  ["O fato de eu discordar não quer dizer que eu esteja certo e ele errado"],
  "a fórmula «razão filosófica… sem afetação» aparece no mesmo bloco (U0003) e é o elo com RC-755."),
],
"RC-756": [
 ("GANESHA, A CANETA ESPECIAL E A TRADUÇÃO PARA OS GANDARVAS",
  ["Gene ajudou adaptando o que Viaza tava contando"],
  "⚠️ A fonte classifica Ganesha como «aquele tipo de ser demobio» — leitura ausente da base: registrar como variante, sem alterar a ficha."),
],
"RC-232": [
 ("O PRESTÍGIO DOS «ASTRONOMOS» JUNTO ÀS ETNIAS HIPERBÓREAS",
  ["esses dois seres tinham muito mais prestígio junto às ilhas"],
  "[REVISAR: «Apólogo» ≈ Apolo.]"),
 ("⚠️ A AMBIGUIDADE QUE O CURADOR DETERMINOU PRESERVAR (Devolutiva O-8 / T-9)",
  ["tem a astrônomos aí dizendo que Nibiro não existe"],
  "Na mesma fonte a palavra designa também os astrônomos profissionais humanos (Q&A U0009–U0010). Vinculado à RC-232 **com ressalva**: os dois sentidos não se fundem; a ambiguidade fica registrada aqui e na apostila."),
],
"RC-188": [
 ("MEMETE — A DEFINIÇÃO EM BOCA DO AUTOR (termo nunca cadastrado)",
  ["a sequência da internet humana, que eu chamo Memete", "o genoma de cada ser humano pula loucamente a cada microssegundo"],
  None),
 ("O TECLADO GENÉTICO COMO INTERFACE DA REDE",
  ["É o uso que a atitude mental de cada ser humano faz do seu teclado genético"],
  "⚠️ **VETO DE CÓDIGO MANTIDO (Devolutiva O-8):** «Memete» permanece termo-observação absorvido aqui e em RC-194; **não** ocupa RC-778."),
],
"RC-194": [
 ("QUEM CRIOU O BIG DATA E O MAPA DAS 10 ENCARNAÇÕES",
  ["foram eles que criaram esses troços de certa forma eh do chamado big data", "você pega suas últimas 10 encarnações como ser humano e você vê a mesma assinatura quântica"],
  None),
 ("A CONTRIBUIÇÃO INDIVIDUAL MEDIDA NO CAMPO",
  ["Como também se pode saber a contribuição específica de Zezinho dos Anzóis"],
  "⚠️ A frase seguinte (o fundador do islamismo e o «campo mófico») é trecho RETIDO em bloco (Devolutiva O-5) — não transcrever."),
],
"RC-751": [
 ("A ANTERIORIDADE (3 ANOS ANTES DA FICHA) — O MECANISMO JÁ DESCRITO",
  ["Porque tá tendo um problema seríssimo na espiritualidade que começou de uns anos para cá"],
  None),
 ("A VISTA GROSSA COMO TÉCNICA DE CONTAMINAÇÃO",
  ["Poucos são os níveis espirituais que retém as informações"],
  None),
 ("A ECOLOGIA DA PSICOSFERA (o urubu e o vírus)",
  ["Passou avião, passou urubu, nada fica ali parado olhando para você"],
  "⚠️ quarentena biomediúnica leve: é descrição de mecanismo espiritual, não técnica prescrita."),
],
"RC-617": [
 ("ANTERIORIDADE EM 7 MESES (a data real do anúncio)",
  ["existe um livro que eu chamo de inquisição espiritual"],
  None),
 ("A TÉTRADE DAS INQUISIÇÕES",
  ["Eu já eh inquisição filosófica, inquisição poética, inquisição trimurtiana"],
  "⚠️ manter a ressalva de que o nome é provisório («não sei se vai ser esse o nome, se um dia eu publicar»)."),
 ("O DESTINO ANUNCIADO DO LIVRO",
  ["conta a história desse troço e do que se passou e do que se passa"],
  None),
],
"RC-745": [
 ("A BANCA ESPIRITUAL DE RESISTÊNCIA (a proposta de 2021)",
  ["É preciso que mais grupos espirituais mantenham ou construam aquilo que eu tô chamando de banca espiritual"],
  None),
 ("POR QUE A ERRATICIDADE NÃO RETÉM",
  ["A estrutura da operacional é manter em funcionamento novas atitudes e buscas"],
  "[STT: «os aliceces magnéticos» = os alicerces magnéticos.]"),
 ("A TURMA QUE SE POUPOU DE ENCARNAR",
  ["já tem uma turma agora que tá defendendo que alguns algumas consciências humanizadas"],
  "⚠️ quarentena biomediúnica — registro, não doutrina."),
],
"RC-755": [
 ("A ORIGEM HISTÓRICA DO COLÉGIO (a lacuna que a ficha tinha)",
  ["Quando os toatas de Nanã entregaram isso pros milesianos", "E foi daqui que surgiu um colégio druídico"],
  None),
 ("O QUE FOI ENTREGUE AOS MILESIANOS",
  ["então esse essa turma aqui tinha muita informação, inclusive sobre CPH4"],
  None),
],
"RC-759": [
 ("A 2ª FONTE DO BLOCO TUATHA × MILESIANOS (e a divergência de data)",
  ["os chamados milesianos, que a gente já falou em outras palestras"],
  "⚠️ **Divergência SEM FUSÃO** (Devolutiva O-8 / T-5): a P2021-01-23 fixa «uns 11.000 anos atrás, quando os milesianos subiram pra Irlanda»; esta fonte não data o contato e ancora o período no cataclismo (14/13/12.000). As duas cronologias ficam lado a lado; nenhuma é corrigida."),
 ("OS NOMES DO BLOCO (com [REVISAR])",
  ["o rei deles se chamava noada"],
  "[REVISAR: «noada» = Nuada; «neta de amor» é STT corrompido — não decodificar.]"),
 ("A CHEGADA E O RECORTE MITOLÓGICO",
  ["A gente conhece os toatas de Danã porque afinal de contas foi a base da mitologia celta na Irlanda"],
  None),
],
"RC-516": [
 ("PAMÍXIA: O NOME DO REGIME QUE A BASE NÃO CADASTROU",
  ["que significa membros de diversas espécies terem relações entre si", "Nessa época as coisas não eram assim"],
  None),
 ("O FIM DO REGIME: A AÇÃO DE JAVÉ (ver RC-001)",
  ["Mas Javé foi um dos caras que mais trabalhou para que a ponixia não fosse adiante"],
  "[STT: «ponixia».] ⚠️ **VETO DE CÓDIGO MANTIDO:** «Pamíxia» fica como termo-observação (aqui, RC-056, RC-729)."),
 ("OS DOIS CANAIS DE TROCA: SEXO E LABORATÓRIO",
  ["E isso se dava através da atitude sexual dos seres"],
  None),
 ("O CONSTRANGIMENTO MORAL COMO CAMADA HISTÓRICA",
  ["aí isso passou a ser nos olhos da atualidade uma coisa absurda devido a ao sentido do pecado"],
  None),
],
"RC-056": [
 ("A ESPECIAÇÃO COMO FUTURO ABERTO (e a dieta que a permitiria)",
  ["o tipo de alimentação ou dieta das gerações futuras que vão se especiar"],
  None),
 ("O PROJETO DA NOVA FAMÍLIA BIODEMÔNICA DECLARADO IMPOSSÍVEL",
  ["não há a menor possibilidade de no esp"],
  None),
],
"RC-729": [
 ("O «JABUTI» CÓSMICO CONTADO EM CIFRAS",
  ["as principais 100.000 maluquiças que foram feitas nos laboratórios"],
  None),
 ("O MESMO LABORATÓRIO COMO ORIGEM DA NOSSA LOUCURA PRESENTE",
  ["porque o que nós vivenciamos hoje é um pouco ou muito ou total desdobramento"],
  None),
],
"RC-009": [
 ("SOFIA COMO O PRIMEIRO BIODEMO — SEM OSSO, COM CÉREBRO RADIADE",
  ["foi o primeiro tipo de ser biodemo que surgiu", "Sofia foi criada há 6 bilhões de anos lá atrás"],
  None),
 ("A EXPANSÃO QUE FOI E NÃO FOI",
  ["os Aios meio que determinaram e Sofia foi e não foi"],
  "[REVISAR: «os Aios» ≈ Aia/Aie — RC-031 sem ficha; ver Bloco 2 do pacote.]"),
 ("SOFIA COMO FORÇA DESTE UNIVERSO",
  ["tem Sofia, que é a força desse universo"],
  None),
 ("A ÚNICA VIA PRÁTICA DE SOFIA",
  ["Fora isso, nada a Sofia pode fazer"],
  None),
 ("A VINDA, A POSSE E A COORDENAÇÃO DO QUARTO LOGOS",
  ["A vinda de Sofia tem como objetivo ele assumir o dia da posse dele"],
  "⚠️ a fórmula «a espiritualidade humana é a única alavanca da reintegração» é de OUTRA fonte — não atribuir a P2021-05-15."),
],
"RC-092": [
 ("O QUARTO LOGOS DEFINIDO EM UMA LINHA (a 1ª atestação oral da fórmula)",
  ["todos convergirem pro comando Sofia, o comando prático e para a coordenação do quarto logos"],
  None),
 ("A CONDIÇÃO DO FUTURO",
  ["Hoje a visão que eu tenho na no da minha pequenez é que não há futuro"],
  None),
],
"RC-005": [
 ("A VINDA COMO ASSUNÇÃO DA POSSE (e a ausência de garantia)",
  ["considerando que sempre esses seres têm tido dificuldades em pr"],
  None),
],
"RC-003": [
 ("A REINTEGRAÇÃO VISTA PELO LADO DOS QUE PERDEM",
  ["esperando ver como é que acaba essa zorra aqui do isolamento terrestre"],
  "⚠️ A frase «a espiritualidade humana é a única alavanca» NÃO pertence a esta fonte (é de P2024-11-03) — registrada em RC-003 por aquela fonte apenas."),
],
"RC-086": [
 ("O QUE OS OLÍMPICOS PASSARAM PARA PANDORA (a inversão do padrão)",
  ["que Zeus mandou repassar para Pandora só eh sequências genéticas ruins"],
  None),
 ("A RACIONALIZAÇÃO EM ALTO NÍVEL (a tese que a ficha esperava)",
  ["ela automaticamente já estava racionalizada em alto nível"],
  None),
 ("PANDORA QUE SE FEZ FÊMEA HUMANA E PROCRIOU",
  ["Pandora, que terminou se tornando uma fêmea humana e procri", "assumir como sendo a sua próxima cara"],
  None),
],
"RC-307": [
 ("HEFESTO COMO QUEM ABRE O GENOMA DE PANDORA",
  ["O genoma de Pandora foi aberto por Efestos"],
  None),
 ("O FILHO DE AFRODITE QUE TRANSFORMOU OS SERES",
  ["como Efestos tinha dado paraa Pandora essa transição de fase"],
  "⚠️ RETIRADA: «o filho de Afrodite, que é o cara que transformou os seres» NÃO está neste bruto (a palavra «Afrodite» não ocorre); era memória de outra fonte."),
],
"RC-302": [
 ("AS BEBERAGENS DE EPIMETEU COMO BANCO DE SEQUÊNCIAS",
  ["já tinha várias beberagens repetidas das poções de epimeteu", "Epimeteu recolheu o DNA deles e os transformou em poção deberagem"],
  None),
],
"RC-727": [
 ("A LINHAGEM DE PANDORA COMO A MAIS PRÓXIMA DE SOFIA",
  ["os demos podem ser o que eles quiserem no padrão do que o genoma deles permit"],
  "⚠️ RETIRADA: «os manipulados por Pandora são os seres mais próximos de Sofia» não ocorre nesta fonte; a proximidade com Sofia fica como leitura da camada-3, não como citação."),
 ("A AUSÊNCIA DE ESCÂNDALO NA MISTURA",
  ["a Pamixia ela não"],
  "⚠️ [TEXTO CORROMPIDO no STT: «a Pamixia ela não Não, não, não existia escândalo»] — preservar, não normalizar."),
],
"RC-299": [
 ("PANDORA NA MITOLOGIA DESTE CICLO (sem o nome demo)",
  ["Pandora, que terminou se tornando uma fêmea humana e procri"],
  "⚠️ KALIL KADMON NÃO É CITADO nesta fonte; o vínculo é nominal. Registrar a ausência (para não inflar a ficha)."),
],
"RC-301": [
 ("O FOGO DE PROMETEU COMO RECICLAGEM DE INFORMAÇÃO (o elo com o filme)",
  ["É o fogo de Prometeu realmente queimando tudo e reciclando e colocando novas informações que nunca antes haviam sido trabalhadas"],
  None),
],
"RC-395": [
 ("⚠️ T-1: A CIFRA DE 400 MILHÕES (a selar, sem correção do canônico)",
  ["por volta de 400 milhões de anos"],
  "Divergência registrada: a linha canônica fixa o Ragnarok em Marte em 300 milhões de anos (B050); esta fonte dá 400 milhões e usa o mesmo número para a convergência da briga. **Nenhuma alteração no canônico** (Devolutiva O-8)."),
 ("O DADO ZOOLÓGICO ASSOCIADO",
  ["Porque o povo também tem a sua história de como ele há 400 milhões de anos"],
  "[STT: «o povo» = o polvo.]"),
],
"RC-593": [
 ("O MAHABHARATA NA GRAFIA ORAL E O SEU USO",
  ["quando a gente lê os livros de antiguidade, Ramaiana, Marrabarata"],
  None),
],
"RC-614": [
 ("O QUARTO CÉREBRO ANUNCIADO PARA O DIA SEGUINTE",
  ["são os protocolos da mente e o quarto cérebro vão criando"],
  "⚠️ **Radar (Devolutiva O-8):** a palestra de domingo 16/05/2021 entra em busca prioritária — ainda não a temos."),
 ("A RÉGUA DO FILME, SEPARADA DO QUE É DELE",
  ["A gente só pode responder o que é um ser humano quando a gente chegar a usar 100"],
  None),
 ("O CRÂNIO COMO ÚLTIMA FRONTEIRA",
  ["com crânio protegendo um cérebro que ainda tem espaço"],
  None),
],
"RC-758": [
 ("O MESMO ANÚNCIO, PELA CHAVE DA COLONIZAÇÃO",
  ["vão colonizando esses neurônios que ainda nem foram ativados"],
  "Registrar como antecessor de linguagem: a fórmula «centro de sabedoria vibracional» (2026) não é idêntica à de 2021 — não equiparar."),
],
"RC-517": [
 ("PROTOCOLOS DA MENTE JÁ CIRCULAVAM NO IEA EM MAIO/2021",
  ["são os protocolos da mente e o quarto cérebro vão criando"],
  "⚠️ não equiparar «protocolos da mente» (2021, oral) a «Protocolo Mental» (RC-517, doc. posterior). Só se registra a circulação do sintagma."),
],
"RC-070": [
 ("O ISOLAMENTO COMO VANTAGEM DECLARADA",
  ["A permanência do isolamento faz com que nós continuemos desconhecidos e tem as suas vantagens"],
  None),
 ("OS QUE ESPERAM O FIM DO ISOLAMENTO PARA PEGAR UMA FATIA",
  ["esperando ver como é que acaba essa zorra aqui do isolamento terrestre"],
  "⚠️ quarentena ufológica."),
],
"RC-160": [
 ("A ENTROPIA COMO ÚNICA CERTEZA",
  ["Só a certeza da entropia", "ou isso vai ser feito ou a entropia vai sempre imperar"],
  None),
 ("A ENTROPIA COMO POLÍTICA DOS DEUSES (o medo de 49.000 anos atrás)",
  ["eles se perguntarem se o que fez para garantir que com entropia funcionando"],
  None),
 ("⚠️ «NÃO HÁ PLANO B» (restrito à citação, por decisão do Curador)",
  ["Então não há plano B"],
  "A fórmula permanece como citação de U0016 nesta ficha e na apostila — não vira epígrafe nem síntese de doutrina (Devolutiva O-5)."),
],
"RC-710": [
 ("A RESERVA CORTICAL DITA EM 2021",
  ["nós aqui precisamos romper essa barreira para usar os 84"],
  None),
 ("O CRÂNIO COMO INVÓLUCRO DO QUE IMPORTA",
  ["talvez a principal seja o fato de ter crânio"],
  None),
 ("O DIAGNÓSTICO DO ESTACIONAMENTO",
  ["Porque os humanos estacionaram"],
  None),
],
"RC-713": [
 ("CPH4: O QUE É, DE FATO, SEGUNDO O AUTOR",
  ["quem tem osso mesmo são os humanos", "os organismos das mães produzem esse CPH4"],
  None),
 ("A DROGA DO FILME × A ENZIMA REAL",
  ["é aquela droga sintética, desculpe o Pleonasmo"],
  "⚠️ quarentena científica: a farmacologia é do filme *Lucy* (2014, Luc Besson) — que **não** tem obra nem termo na Base [RETIFICAÇÃO: o piloto citava «B036»; B036 é «As Memórias de Javé»]."),
 ("O QUE OS DEUSES FIZERAM COM ESSA DESCOBERTA",
  ["eles descobriram o CPH4 na condição humana"],
  None),
],
"RC-562": [
 ("⚠️ T-2: A VARIANTE «28.879» (selo temporal, SEM correção do canônico)",
  ["os nossos 28.879 genes, cada um gene desses tem milhares de cons"],
  "**Reancoragem declarada (ciclo P2021-05-15):** o dossiê apontava RC-055/RC-128/RC-238 — engano meu de âncora; o selo foi aplicado nesta ficha, que é a que carrega o número canônico 28.869. Nenhuma alteração do canônico, nenhum outro número do cadastro foi tocado."),
],
"RC-001": [
 ("JAVÉ COMO O AGENTE QUE FECHOU A PAMÍXIA",
  ["Mas Javé foi um dos caras que mais trabalhou para que a ponixia não fosse adiante"],
  None),
 ("O CONDICIONAMENTO DOS HUMANOS E O ADÃO IMPOSITIVO",
  ["os seres humanos continuaram sendo condicionados na disputa maluca que Jahé fez"],
  "⚠️ [STT: «Jahé».] A fórmula do «Adão religioso impositivo» pertence a outro bloco da fonte (U0010) — não fundir os dois."),
 ("A RODA QUE JAVÉ CRIOU FUNCIONA SOZINHA",
  ["A roda que Javé criou funciona por ela mesma"],
  None),
 ("JAVÉ × INANA (a aliança invertida)",
  ["sempre atrapalhou Javé e usou Eva e Lilif"],
  "⚠️ Reancoragem declarada: o dossiê citava «RC-010 (Javé)»; RC-010 é Atlântida — a âncora correta é RC-001. Nenhuma ficha de Atlântida foi tocada."),
],
"RC-742": [
 ("A FALÊNCIA OLÍMPICA DESCRITA DE DENTRO DA DISPUTA",
  ["doença, peste e incapacidade de se reproduzir"],
  None),
 ("O VEREDITO DA INCOMPETÊNCIA",
  ["Se essas forças forem competentes nesse sentido"],
  None),
 ("A DESCONTINUIDADE CÓSMICA (a fórmula da cretinice)",
  ["É de uma cretinícia, de uma descontinuidade no sentido negativo"],
  None),
],
}

# ================================================================ BLOCOS 2, 3 e 4
# BLOCO 2 — termos do cadastro SEM FICHA: o vínculo de fonte vai para a malha
# (dados_termos.py) e o conteúdo fica documentado aqui; não há arquivo em `termos/`.
# O precedente é o RC-385 do ciclo P2023-06-24.
SEM_FICHA = [
 ("RC-186 · Biodemol", ["que é uma mistura de demo e de bio, mas um padrão diferente dos biodemos"],
  "⚠️ Não identificar com «demobio»/«demobiol»: a fonte mantém as três estirpes separadas. A equação demol↔demobio fica em aberto (decisão do Curador)."),
 ("RC-401 · Família Demolle", ["o pacto que muitas das estirpes de demo"],
  "Corroboração do pacto de hibridagem entre estirpes de demo antiga."),
 ("RC-035 · Bilatérios", ["É que surgiu a questão do cérebro bilatério, aqueles dois hemisférios"],
  "Dado que faltava à ficha (a fonte não tem ficha própria)."),
 ("RC-093 · Radiatas", ["nunca foi bilatério, tipo do povo, e em corpos invertebrados"],
  "Com o caso-teste do polvo: «Putz, mas são nove cérebros»."),
 ("RC-031 · Aya e Aye", ["foram eles que criaram esses troços de certa forma eh do chamado big data"],
  "[REVISAR: a fonte grafa «os Aia e Aia» (não «Aie»).]"),
 ("RC-075 · Lila", ["da sua regra de conduta chamada Lila"],
  "A regra de conduta como critério da geopolítica da Trimúrti — ver RC-104."),
 ("RC-017 · Alt´Lam / RC-018 · Alt´Lam Gron", ["a essa altura a turma de Alto Langron continuou existindo lá eh nessa ilha que se move"],
  "✅ RESOLUÇÃO APROVADA (Devolutiva O-8 / T-10) do [REVISAR] «ALTA LANGRON» de RC-036. Fichas sem arquivo: o dado fica aqui e o vínculo de fonte vai na malha."),
 ("RC-189 · Eva (figura)", ["Porque diferente do Adão movido, escolhido por Javé"],
  "⚠️ A sintaxe da contravontade de Eva não é recuperável no STT («Jahferência de Eva») — [TEXTO CORROMPIDO]; a aliança Inana–Eva–Lilif fica quarentenada."),
 ("RC-089 · Processador Val", [],
  "Nada de conteúdo próprio nesta fonte. **Sem âncora para «Sefira dos Ossos»/«Cérebro Humano»**: RC-612 existe mas não é essa seira; o dado anatômico (osso/crânio) ficou em RC-036/RC-710/RC-631."),
]

# BLOCO 3 — TERMOS-OBSERVAÇÃO: veto de código mantido (Devolutiva O-8); viram glossário da apostila.
OBSERVACAO = [
 ("MEMETE", ["a sequência da internet humana, que eu chamo Memete"], "absorvido em RC-188 · RC-194"),
 ("PAMÍXIA (grafias: pamixia / ponixia / Pamixia)", ["que significa membros de diversas espécies terem relações entre si"], "absorvido em RC-516 · RC-056 · RC-729"),
 ("CPH4", ["O que diabos é o CPH4"], "absorvido em RC-713 · RC-710 · RC-751"),
 ("THULE / Tul / Tool / Tur / «continente de Lu»", ["lá no Polo Norte existia um lendário continente"], "absorvido em RC-068; MU/Lemúria só como menção"),
 ("AESIR / VANIR / ODIM", ["aqueles seres descendentes de Odim, os Aesir e Vanir"], "absorvido em RC-068 (taxonomia), sem termo"),
 ("TUATHA DE DANANN / MILESIANOS / NUADA", ["o rei deles se chamava noada"], "absorvido em RC-759 · RC-755 · RC-464, sem termo"),
 ("ADAPA («a lenda de Adapa»)", ["uma delas se chama a lenda de Adapa"], "absorvido em RC-486 · RC-587 · RC-001, sem termo novo"),
 ("ISAR (≈ Ishtar)", ["O segundo nome mais importante de Inana é ISAR"], "absorvido em RC-464, com [REVISAR]"),
 ("OSTRONOMOS vs astrônomos", ["tem a astrônomos aí dizendo que Nibiro não existe"], "absorvido em RC-232 com a ressalva filológica decidida pelo Curador"),
 ("«ilha que se move»", ["nessa ilha que se move em cima do Oceano Atlântico"], "absorvido em RC-036/RC-017/RC-018, sem termo"),
 ("BANCA ESPIRITUAL DE RESISTÊNCIA", ["aquilo que eu tô chamando de banca espiritual"], "absorvido em RC-745, sem termo"),
 ("«72 etnias» / «14 caravanas»", ["elas tinham aproximadamente umas umas 72 etnias importantes"], "absorvido em RC-068, sem termo"),
 ("SITCHIN / Graham Hancock / NASA / Plutão / Sedna / nuvem de Oort", ["constantemente se descobre e se atualiza o número"], "quarentena científica e ufológica: não entram como termos nem como obras"),
]

# BLOCO 4 — RADAR DE ACERVO (fontes não localizadas; decisão do Curador: declarar, não vincular).
RADAR = [
 ("Palestra anunciada para o dia seguinte", ["são os protocolos da mente e o quarto cérebro vão criando"],
  "busca prioritária — o título «os protocolos da mente e o quarto cérebro» é anunciado para domingo 16/05/2021 e não está no acervo"),
 ("Memória de falas anteriores", ["que eu já citei em palestras anteriores"],
  "as auto-referências («já fiz umas duas ou três palestras sobre isso», «aquilo que a gente falou numa numas palestras meses atrás», «Já falei disso aí no na outra palestra», «quando a gente aqui analisou o filme Lucy») ficam declaradas como fonte não localizada, sem vínculo na malha"),
]

def _corpo(itens, cabecalho):
    L = [cabecalho]
    for cod, anc, nota in itens:
        corpo = ""
        if anc:
            try:
                corpo = aspas(anc)
            except LookupError as e:
                raise SystemExit(f"ÂNCORA NÃO ENCONTRADA em {cod}: {e}")
        txt = f"### {cod}" if False else f"- **{cod}**"
        if corpo:
            txt += f" {corpo}"
        if nota:
            txt += (f" — {nota}" if corpo else f" — {nota}")
        L.append(txt)
    L.append("")
    return L



def main():
    linhas, erros = [], []
    for cod, itens in BLOCOS.items():
        linhas.append(f"### {cod}")
        for rot, ancoras, nota in itens:
            corpo = ""
            if ancoras:
                try:
                    corpo = aspas(ancoras)
                except LookupError as e:
                    erros.append(f"{cod} · {rot[:44]} → ÂNCORA NÃO ENCONTRADA: {e}")
                    continue
            if not corpo and not nota:
                erros.append(f"{cod} · {rot[:44]} → bloco vazio")
                continue
            txt = f"- **[P2021-05-15 · {rot}]**"
            if corpo:
                txt += f" {corpo}"
            if nota:
                txt += (f" — {nota}" if corpo else f" {nota}")
            linhas.append(txt)
        linhas.append("")
    for cod, anc, nota in SEM_FICHA + OBSERVACAO + RADAR:
        pass  # validado abaixo, ao emitir
    extra = []
    extra += _corpo(SEM_FICHA, "\n## BLOCO 2 — TERMOS DE CADASTRO SEM FICHA (vínculo na malha; conteúdo aqui)\n")
    extra += _corpo([(f"TERMO-OBSERVAÇÃO · {c}", a, n) for c, a, n in OBSERVACAO],
                    "\n## BLOCO 3 — TERMOS-OBSERVAÇÃO (VETO DE CÓDIGO MANTIDO — Devolutiva O-8)\n"
                    "Nenhum vira código: entram no glossário da apostila e no vocabulário de leitura, absorvidos nas fichas indicadas.\n")
    extra += _corpo([(f"RADAR · {c}", a, n) for c, a, n in RADAR],
                    "\n## BLOCO 4 — RADAR DE ACERVO (fonte não localizada — declarar, não vincular)\n")
    cab = ("# PACOTE DE AMPLIAÇÕES — P2021-05-15 (As Etnias Hiperbóreas e os Anunnakis)\n"
           "# Gerado por _gerar_ampliacoes_P2021-05-15.py: toda citação foi extraída byte a byte do\n"
           "# `original.txt` a partir de âncoras — nada aqui foi digitado de memória.\n"
           "# Única alteração mecânica declarada: aspas duplas internas da fonte viram «…» (ver aspas_internas()).\n"
           "# 0 códigos novos (Devolutiva O-8: teto 777 inviolável; Memete/Pamíxia/CPH4 seguem termos-observação).\n\n")
    open(SAIDA, "w", encoding="utf-8").write(cab + "\n".join(linhas + extra))
    print(f"pacote emitido: {len(BLOCOS)} fichas · {sum(1 for l in linhas if l.startswith('- '))} blocos")
    if erros:
        print("\nERROS (corrigir âncoras):")
        for e in erros:
            print("  ✗", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
