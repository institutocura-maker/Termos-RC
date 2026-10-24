#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO PACOTE DE AMPLIAÇÕES — P2023-10-14 (ferramenta de ciclo).

Princípio (idêntico ao do ciclo-espelho P2021-05-15): **eu não digito citações.**
Cada aspa deste pacote nasce de uma ÂNCORA (subsequência curta que garanto existir na
fonte); o script devolve a SENTENÇA inteira da fonte que contém a âncora, recortada
byte a byte de `original.txt`, já endereçada pelo bloco U00xx. Assim é impossível
citar de memória, inverter palavra ou «melhorar» o autor. Âncora não encontrada =
erro e o bloco não é emitido.

Fonte da decisão: `../DECISAO-DO-CURADOR.md` (devolutiva de 28/08/2026).
Travas aplicadas: +0 códigos · +0 relações · +0 obras · nada do bloco político/ético
bloqueado entra em ficha · «Henk» não unificado (item 2) · RC-672 e RC-396 fora.
"""
import re, os, sys, bisect

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
FONTE = os.path.join(CICLO, "original.txt")
SAIDA = os.path.join(AQUI, "_ampliacoes_P2023-10-14.txt")
SIGLA = "P2023-10-14"

src = open(FONTE, encoding="utf-8").read().replace("\r\n", "\n")
_starts = [0] + [k + 1 for k, ch in enumerate(src) if ch == "\n"]
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
    s = re.sub(r"\s*\n\s*", " ", s)   # 2ª alteração mecânica declarada: as quebras duras do
    # bruto dentro de uma mesma frase viram espaço — nenhuma palavra é alterada, e o portão A
    # (paridade de aspas, por linha) passa a poder ser auditado em linha única.
    if len(s) > 1400:
        s = s[:1400].rsplit(" ", 1)[0] + "…"
    return s, u_of(OFF[i])

def aspas_internas(s):
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
        if s in vistos:
            continue
        vistos.add(s)
        saida.append('"%s" (%s)' % (aspas_internas(s), u))
    return "; ".join(saida)

ANT = lambda ficha: (f"⭐ **NOTA DE ANTERIORIDADE — {SIGLA}: esta é a fonte mais antiga da ficha "
                     f"(hoje: {ficha}) para o conteúdo acima.** Selada com a data da fonte; "
                     "**sem** alteração da cronologia canônica da Base.")

BLOCOS = {
"RC-024": [
 ("A HONRA COMO PROPRIEDADE DE ESPÉCIE — e só duas espécies na Terra a teriam",
  ["Então, seja lá que número for, só duas tem noção de honra", "Ou seja, duas não irão nos destruir nunca", "Só duas, anunx e sirianos"],
  "⚠️ O **próprio autor suspende** o segundo termo logo em seguida («Que diabos é sirianos? Vamos deixar para lá»): nenhuma ficha de sirianos recebe este uso."),
 ("DEFINIÇÃO OPERACIONAL DE «HONRA» NESTA FONTE",
  ["a honra demodármica é uma honra que foi criada"],
  "A Base não tem termo com a palavra «honra» no nome (77 ocorrências no bruto) — decisão D-1 do Curador: sem código novo; verbete no Apêndice do dicionário STT da apostila."),
 ("HONRA, DECÊNCIA E A AUSÊNCIA DE HERANÇA MORAL",
  ["Honra não é para todo mundo", "E de repente a coisa desandou"],
  None),
 ("PODERES CIRCUNSTANCIAIS ≠ PODER DE DOMINAÇÃO (a fórmula de segurança da fonte)",
  ["eles têm poderes circunstanciais, mas não tem poder de dominação"],
  "⚠️ **Obrigatória em todo uso desta fonte**: desarma a leitura apocalíptica do bloco ufológico."),
 ("A CONVERSABILIDADE COMO CRITÉRIO DE PARCERIA",
  ["Os anunacos, pelo menos conversam com os humanos"],
  None),
 ("A GENÉTICA DE OBEDIÊNCIA: O MODELO DA DOMESTICAÇÃO (linha que a leitura inicial tinha «lembrado» ao contrário)",
  ["como se a gente pegasse vaca, cachorro, gato, cavalo e mexesse na genética deles para que eles aprendessem a obedecer as nossas ordens"],
  "⭐ A fórmula real da fonte é a da **genética de obediência como método aplicado a animais**, e não uma sentença sobre «escravidão de filhos» — a formulação lembrada na leitura inicial **não existe** no bruto e foi substituída por esta aspa (U0005)."),
 ("O POVO ESPÉCIE E O REACENDIMENTO (o título explicado pela fonte)",
  ["Nós precisamos reacender a honra dos anunax", "Por isso que eu coloquei o nome da palestra de da esquecida honra dos anunac"],
  "⚠️ Fato de catálogo: a fonte registra **três** títulos (o do arquivo, «a honra esquecida dos anunx» e «a honra perdida dos anunx» nos arquivos do autor)."),
 ("O DOMÍNIO QUE NÃO SE CONQUISTOU, SE PERDEU",
  ["os anunx também se acham don dos humanos", "Eles não têm a opção D"],
  "[REVISAR: «a opção D» — sigla não decifrada na fonte; não conjeturar.]"),
],
"RC-001": [
 ("O «INFERNNHO» E O CORPO COLAPSADO — a condição de Javé descrita sem eufemismo",
  ["Javé está numa", "Ele é um eu implodido num corpo colapsado que nunca morre porque os anjos dão choque o tempo todo"],
  None),
 ("O CRUPIER DONO DA BOLA",
  ["Javé é aquele dono, é um crupier", "Acabou o jogo, tá"],
  None),
 ("O PLANO NÃO FINALIZADO (a tese do universo planejado × improvisado)",
  ["Esse nosso foi todo planejado, só não foi finalizado porque o criador caiu na própria criação"],
  None),
 ("AS COISAS PODRES E O COLAPSO DATADO DE 2021",
  ["As coisas estão colapsando", "As coisas podres", "O corpo de Javé e o eu dele é só um dos exemplos de colapsos que estão ocorrendo"],
  None),
 ("A COVARDIA ATRIBUÍDA E A RETIRADA DE MÉRITO",
  ["Javé é um ser tão covarde que ele na Bíblia cita como se ele Javé tivesse tomado a decisão de destruir aquilo por cá"],
  "⚠️ quarentena teológica (retenção): entrada de ficha com rótulo, **não** para a apostila."),
 ("JAVÉ E A OBRA QUE ELE DEIXOU AOS HUMANOS",
  ["Essa foi a obra que Javé nos deixou"],
  None),
],
"RC-422": [
 ("A AUTOCONFISSÃO DO CRIADOR FRACASSADO, EM 2023 (anterioridade)",
  ["o julgador, o juiz faliu, colapsou", "Afinal, o criador de todas as coisas não está mais no comando"],
  "🆕 anterioridade: P2024-11-09"),
 ("A VARIANTE DITADA PELA FONTE (D-8a: variante, não substituição)",
  ["Por o bem não destrói o mal sob pena de se tornar igual a ele", "O bem perde sempre para continuar sendo bem, senão ele se desconfigura"],
  "⚠️ A redação canônica da Base fica **intocada** (decisão D-8a do Curador): o que se registra aqui é a **variante oral de 14/10/2023**."),
 ("A AUSÊNCIA DE REPRESENTAÇÃO DO BEM",
  ["Nada que existe na Terra representa o bem, a não ser uma pessoa que o produza"],
  None),
],
"RC-742": [
 ("O JUIZ QUE FOI JULGADO",
  ["Quem marcou o julgamento é que foi julgado", "Jahé foi quem marcou, mas ele colapsou antes dos próprios fatos"],
  None),
 ("A CULPA DEVOLVIDA À ESPIRITUALIDADE",
  ["O criador já não julga ninguém, mas é assim mesmo"],
  None),
 ("A VARIANTE DATADA DA FÓRMULA (D-8a)",
  ["Se o bem virar bicho para destruir o mal, não é o bem", "Então o bem não ganha"],
  "Registrada como variante de 2023; a fórmula canônica permanece a da Base."),
],
"RC-745": [
 ("O ADJETIVO «DEMODÁRMICO» GANHA DEFINIÇÃO ORAL (D-1)",
  ["a honra demodármica é uma honra que foi criada", "Essa honra demodármica sempre se ancorou nas relações da linhagem"],
  "Decisão D-1 do Curador: nota transversal nesta ficha — o adjetivo já vivia aqui; a **honra** não vira código."),
 ("O LEGADO MAL ENDEREÇADO",
  ["nós humanos ficamos escutando essas palavras sem entender que no princípio isso foi criado"],
  None),
],
"RC-474": [
 ("ARCONTES = DONOS, E A HONRA DEMODÁRMICA APLICADA A ELES (D-1)",
  ["a honra demodármica é uma honra que foi criada", "E esses arcontes de lá todos eles vão se ferrar"],
  None),
 ("QUEM SE SENTIA ARCONTE E O QUE OS PORTAIS FECHARAM",
  ["seres que se sentiam arcontes, ou seja, donos"],
  "A definição «arcontes, ou seja, donos» é dada **em fala** — material raro, e anterior a quase todas as fichas do tema."),
],
"RC-770": [
 ("A DEFINIÇÃO ORAL DE ARCONTE, COM ANTERIORIDADE",
  ["seres que se sentiam arcontes, ou seja, donos"],
  "🆕 anterioridade: P2026-07-25"),
 ("OS HIPÓSTASES E O «BLÁ BLÁ BLÁ» DOS NOMES",
  ["Quem são Zeus, Krishna", "Blá blá blá blá blá blá"],
  "⚠️ a fonte nivela os nomes do panteão a «blá blá blá»: juízo da fonte, não da Base."),
],
"RC-009": [
 ("«ZERO À ESQUERDA»: A MINIMIZAÇÃO DE SOPHIA POR UMA FONTE DE 2023",
  ["Sofia é um zero à esquerda na perspectiva do que os anonaques pensam"],
  "⚠️ **Divergência selada com a data da fonte** (regra do Curador): nada na ficha canônica muda."),
 ("A NÃO-INTERFERÊNCIA TRÍPLICE DE SOPHIA",
  ["Quando os anunques souberam do Rainarok ocorrido há 300 milhões de anos e que Sofia também não fez nada", "Há 700.000 anos ocorreu A rebelião de Lúcia"],
  None),
 ("A SUZERANIA E A DATAÇÃO DO ENGENDRAMENTO",
  ["E aqui só tem um suzerano construído ou engendrado para isso que foi Sofia", "Aí aqui tem Sofia o Rockman"],
  None),
 ("O PAI DE JESUS E O ELOGIO DA AUSÊNCIA",
  ["Ou seja, Sofia era pai de Jesus", "Era para Sofia ter entrado com nos anulxos também não fez nada"],
  None),
],
"RC-565": [
 ("A TESE DATADA DA FUSÃO DE EPÍTETOS (D-7: tese da fonte, não estrutura da ficha)",
  ["Esse cara é o pai de Jesus, tá pessoal", "É o Rockman em hebraico, Sofia em grego"],
  "⚠️ Item 6 da devolutiva: a fusão **não** entra na estrutura das fichas; vive aqui como **tese datada** (com RC-682) e no aparato da apostila."),
 ("A GRAFIA DO STT PARA A 2ª SEFIRAH",
  ["Aí tem Shockma e biná"],
  "[REVISAR: «Shockma» = Hochmah (canônico da Base); grafia preservada na citação.]"),
],
"RC-682": [
 ("«MALUKUF»: A 10ª SEFIRAH PELA BOCA DA FONTE (D-7)",
  ["Então, Malukuf é o Messias prometido por aos judeus", "mas Malukuf já existia, que é Sofia ou Rock, é figura cósmica do Messias"],
  "⚠️ A ficha não funde Malkuth/Sophia/Hochmah: o que se registra é a **equivalência afirmada em 14/10/2023**."),
 ("O ESPERADO QUE JULGA OS PRÓPRIOS DEUSES",
  ["os Anunax estão esperando serem julgados por esse ser", "Estranhamente eles ainda acreditam no julgamento de deuses e humanos"],
  None),
],
"RC-263": [
 ("A ÁRVORE DA VIDA COMO INVENÇÃO DE UM HUMANO",
  ["É uma representação que Enoque, um humano, criou", "É um joguinho que Enoque humano criou pros seres demos jogarem"],
  "⭐⭐⭐ A inversão da direção da revelação (humano → deuses) está aqui, em fala."),
 ("AS DEZ PERSONIFICAÇÕES E OS DESÍGNIOS",
  ["a árvore da vida mostra as 10 principais personificações", "São encarnações as que movem os principais 10 processos que acontecem dentro da matrix"],
  None),
 ("A PONTE COM O TARÔ",
  ["A relação entre essas 10firais aí aqui dá toda a margem do tarô"],
  None),
 ("A ENTREGA AOS RABINOS E O MATERIAL PRIMÁRIO",
  ["Gabriel entregou a rabinos Shimon Bariokai"],
  "[REVISAR: «fois» é truncamento do STT; o canônico da Base é Shimon bar Yochai. A expressão «ver também» aparece degradada na linha 280 do bruto. [TEXTO CORROMPIDO]."),
],
"RC-261": [
 ("JAVÉ = KETHER, AFIRMADO EM FALA (anterioridade)",
  ["Então, Javé é que ter, é, a primeira que foi reconstruída aqui dentro", "Olha, o principal aqui entre vocês que vocês consideram é keter"],
  "🆕 anterioridade: P2024-07-14"),
 ("AS NOVE RESTANTES RECONSTRUÍDAS NA MATRIX",
  ["As outras nove são outras nove personif"],
  None),
],
"RC-262": [
 ("«ABISMO LUMINOSO»: A DEFINIÇÃO ORAL DE DAATH (D-6 aprovado)",
  ["Abismo luminoso", "Abismo é profundo, mas DAF é um abismo estranho", "Então, por isso que é luminoso, porque lá no fundo do abismo a luz de do Deus caiu"],
  "🆕 anterioridade: B013 (só livro) — a ficha passa oficialmente a ter fonte-palestra, por decisão do Curador em 28/08/2026 —  ⚠️ A grafia do bruto é «DAF»; o Curador confirmou a leitura Daath."),
 ("A CRÍTICA AOS CABALISTAS",
  ["E os cabalistas não entendem isso de forma crítica, de forma romântica"],
  "⚠️ quarentena teológica (retenção): não vai para a apostila."),
],
"RC-008": [
 ("O AUTOR APONTA O PRÓPRIO LIVRO (D-5; B013 confirmada pelo Curador)",
  ["eu analiso isso no livro que eu lancei chamado Zintzum, o exílio forçado de divindade"],
  "**Item 4 da devolutiva:** a obra citada é a **B013** que a Base já possui — **0 obras novas**. A grafia do bruto é «Zintzum»."),
 ("O EXÍLIO REFORMULADO PELOS RABINOS",
  ["Um ser se exilou na sua própria criação por amor aos que nela estão", "mas os rabinos transformaram a queda do criador num passo de dança"],
  "⭐ A fórmula «passo de dança» é a imagem mais comentável do bloco cabalístico de 2023."),
 ("A QUEDA DITA SEM EMBELO",
  ["Que um criador caiu na própria criação", "Mas fica feio o negócio de queda"],
  None),
],
"RC-272": [
 ("O «LOOP TEMPORAL» DITO EM INGLÊS (1ª fonte-palestra do código)",
  ["tão somente o desdobramento de um loop temporal", "até porque eles foram os primeiros e serão os últimos"],
  "🆕 anterioridade: B013 (só livro) — RC-272 tem `ficha=False`: o vínculo é de **malha**, o conteúdo fica neste bloco (precedente RC-385/P2023-06-24)."),
 ("A OUTRA FACE: O HUMANOS COMO ÚLTIMOS QUE SERÃO PRIMEIROS",
  ["Jesus na sua filosofia diz"],
  None),
],
"RC-514": [
 ("TIKUN DEFINIDO COMO REPARO NA OBRA **E NO CRIADOR**",
  ["O ticum cabalístico quer dizer exatamente o reparo na obra e no criador", "É para realizar o reparo no genoma do criador"],
  "⭐⭐⭐ O deslocamento do objeto do tikun (não «nos judeus»: nos humanos e no criador) é a tese da fonte."),
 ("A RELEITURA DO AVISO",
  ["Só que os judeus transformaram esse aviso num entendimento muito romântico"],
  None),
 ("O TIKUN COMO PROJETO DE JAVÉ",
  ["A partir desse ponto, Javé pensava em se apoderar do controle sobre os seres humanos paraa realização do seu ticum"],
  None),
],
"RC-545": [
 ("AS SEFIROT COMO COCONSTRUTORAS DA OBRA (anterioridade)",
  ["que foram reconstruídas dentro da matrix para resolver o problema da matrix"],
  "🆕 anterioridade: P2024-07-14"),
 ("OS QUE FAZEM DA VIDA O QUE SABEM CONSTRUÍ-LA",
  ["E nós aqui do lado biológico é que podemos fazer da nossa vida o que nós soubermos construir nela"],
  None),
],
"RC-322": [
 ("A MATERIALIZAÇÃO — o dharma criado PARA os híbridos, não para a humanidade (D-3)",
  ["E Darma foi o principal conceito que na época foi educado para gerar honra entre seres híbridos que não tinham honra",
   "Porque ele também criou essa coisa chamada casta, mas não era pros humanos, era para seres híbridos"],
  "🆕 anterioridade: P2024-11-30 (hoje a ficha não tem arquivo próprio; o Curador autorizou a materialização — Devolutiva item 11)."),
 ("A HONRA DEMODÁRMICA É O CONTEÚDO DESTA FICHA",
  ["a honra demodármica é uma honra que foi criada em torno do conceito de dharma"],
  "Decisão D-1: «honra» ganha **linha de conteúdo** aqui, sem código novo."),
 ("O DEVER DE CASTA COMO SUSPENSÃO DO KARMA",
  ["Você vai gerar karma negativo se você não for paraa guerra"],
  "⚠️ **Ponto mais delicado do ciclo** (dever de casta justificando violência): entra com rótulo de quarentena e **não** vai para a apostila sem nota editorial."),
 ("O QUE RESTOU QUANDO OS PORTAIS FECHARAM",
  ["Os humanos apenas herdaram isso agora porque os portais fecharam esses seres sumiram e restou o quê"],
  None),
],
"RC-319": [
 ("A TRÍADE VARNA–DHARMA–KARMA COMO PEDAGOGIA PARA HÍBRIDOS (anterioridade)",
  ["Então varma, dma e karma são três conceitos foram criados não para humanidade"],
  "🆕 anterioridade: P2024-11-30 —  [REVISAR: «varma, dma» são as grafias do bruto para varna/dharma.]"),
],
"RC-320": [
 ("OS «TRÊS SENHORES ATRIBUT» E O AVATAR QUE CARREGAVA GENÉTICA",
  ["trazia na sua um pouco da genética dos três senhores atribut desse universo vizinho"],
  "🆕 anterioridade: P2024-11-30 —  [REVISAR: «quechava» = Keshava, fusão de STT.]"),
],
"RC-321": [
 ("O BEM DEFINIDO PELA CLASSE (a formulação mais nua que a Base tem)",
  ["era cumprir com o dharma da sua varna", "o bem era definido pela caixa dos braes"],
  "🆕 anterioridade: P2024-11-30 —  ⚠️ «caixa dos braes» = grafia do bruto para, provavelmente, «classe dos brâmanes»; nada emendado."),
],
"RC-414": [
 ("KRISHNA COMO INTRODUTOR DECLARADO DO DHARMA",
  ["porque ele se diz o introdutor do conceito de dharma", "ensinei o conceito do dharma"],
  None),
 ("O BEM E O MAL NO CAMPO DE BATALHA (Arjuna)",
  ["Eles representam o mal e você aqui representa o bem e o bem tem que destruir o mal"],
  "⚠️ registrar **como fala da fonte sobre o Gita**; não confundir com a fórmula canônica da Base sobre o bem que não destrói o mal (ver RC-422/RC-742)."),
],
"RC-425": [
 ("OS AVATARES ANTERIORES E O «QUECHAVA» (materialização autorizada)",
  ["em encarnações anteriores dele mesmo como avatar de Chiva, Vígno e Brama"],
  "🆕 anterioridade: P2024-11-30 —  ⚠️ «quechava» é a grafia que o STT deu a Keshava ao fundir o pronome; a ficha materializada **não** renomeia nada."),
],
"RC-432": [
 ("TRAVAS E CONTROLES NO CAMPO DO RETARDAMENTO MENTAL (materialização autorizada)",
  ["Nenhum no NAC consegue devido à travas e controles que ele tem no campo do retardamento mental"],
  "⚠️ Retificação medida na aplicação: o **bloqueio ético** desta fonte está noutras linhas — as duas frases misóginas de U0015 e U0033 ficam **retidas** (não transcritas aqui, nem para crítica, por determinação expressa do Curador): não entram em ficha, nem no glossário, nem na apostila. Já o uso de «retardados» (U0003/U0005/U0062, 4 ocorrências) **não** se dirige a pessoas com deficiência — recai sobre os próprios anunnaki e sobre os humanos: o rótulo do dossiê O-5 foi retificado. Esta aspa é o enunciado doutrinário sobre «sangue azul» e sustenta a materialização autorizada (Devolutiva item 11)."),
 ("A PURANÇA DE SANGUE QUE NÃO EXISTE",
  ["em busca dessa pureza de sangue que não existe"],
  None),
],
"RC-593": [
 ("«MARRA BARAT»: A OBRA CITADA COM A GRAFIA DA FONTE",
  ["Existe uma outra obra chamada Marra Barat, que do começo ao fim fala de uma linhagem regenerada de Braba",
   "E o próprio Marrabarata diz que em certas situações a mentira é mais aplic que é a verdade"],
  "[REVISAR: «Marra Barat»/«Marrabarata» = Mahabharata; «Braba» = Brahma. A mentira «mais aplicável» que a verdade é juízo da fonte sobre o próprio épico.]"),
 ("O DIÁLOGO DE KRISHNA NO BAGAVAGUITA",
  ["Então, Krishna no Bagavaguita, que é um dos capítulos do Marabarata"],
  None),
],
"RC-696": [
 ("A LINHAGEM REGENERADA DE BRAHMA, DITA COMO «DE JAVÉ» (anterioridade)",
  ["fala de uma linhagem regenerada de Braba, ou seja, de Javé"],
  "🆕 anterioridade: P2024-07-13"),
 ("OS SETE FILHOS E A CLONAGEM",
  ["a partir de um certo ponto, Brahma teve sete filhos, uma dessas, mas aí não é filho no sentido de de sexo, filho clonado"],
  None),
 ("A ESCOLHA DA LINHAGEM PARA DOMINAR A TERRA",
  ["era o nome de um dos quatro filhos de uma geração que Brama diz que foi especial"],
  None),
],
"RC-037": [
 ("O ANJO CLONE, A PORRADA E O NASCIMENTO DA DESCENDÊNCIA DEMONÍACA",
  ["um anjo clone deu uma porrada em Brama e Brama devolveu a porrada nesse anjo clone"],
  None),
 ("A AUTODECLARAÇÃO DE PUREZA DOS DEUSES",
  ["Nós somos limpos", "Os humanos surgiam do barro e dos restosos"],
  None),
],
"RC-102": [
 ("CHIVA E O PRIMEIRO SER ADIDAIVA",
  ["emergiu no meio do fogo que estava destruindo o corpo do anjo clone e conseguiu levar o código do criador nele e se transformou no primeiro ser adidaiva",
   "Aí toda a descendência de Chiva é a descendência demoníaca"],
  "A fonte grafa «adidaiva» aqui e «adaiva» adiante — duas grafias, mesma palavra (ver camada-2)."),
 ("O FOGO DE QUE ELES DIZEM TER SURGIDO",
  ["eles dizem o que?", "A nossa origem é celestial, porque nós surgimos do fogo"],
  None),
],
"RC-104": [
 ("A TRIMÚRTI QUE NUNCA VEIO — E OS AVATARES NO LUGAR",
  ["tinha uma trimurte, uma trindade, um trium virato, uma tríade de seres super poderosos",
   "nenhum dos três nunca saía lá desse universo e vinha para esse, mas mandavam avatares"],
  "[REVISAR: «trium virato» é a grafia do bruto.]"),
],
"RC-486": [
 ("O MARCADOR GENÉTICO UNIFORMIZADO DA CONDIÇÃO HUMANA",
  ["há um marcador genético, antiquís, que corresponde a um a uma marca uniformizada na condição humana"],
  "⚠️ **[REVISAR — item 2 da devolutiva]:** o bruto grafa «Enk» e «Henk»; **a mesma grafia «Henk» designa também o chefe da nave dos 50**. O Curador **recusou a unificação** a RC-486: manter a leitura dupla (livro de Enki × livro do emissário Henk)."),
 ("A DESTINAÇÃO: O DNA DE ENKI, JAMAIS O DE PANDORA",
  ["O tipo de ser humano a surgir na natureza terrestre era o produzido pela interferência do DNA de Enk, jamais o de Pandora"],
  None),
 ("O CRITÉRIO DO JULGAMENTO GENÉTICO",
  ["Quais Os que ele iria reaproveitar, os que estivessem aliados com os padrões do genoma de Enk"],
  None),
],
"RC-487": [
 ("O LAMENTO DE ENLIL: PRISIONEIROS POR TEREM SE FEITO COMO OS TERRESTRES",
  ["Antes os terrestres se estavam fazendo como nós", "Agora nós nos temos feito como os terrestres para ficar prisioneiros deste planeta", "Toda a missão se converteu em um pesadelo"],
  "⭐⭐ A peça retórica mais citável do ciclo; grafia do bruto: «enque» para Enki, «Elio» para Enlil."),
 ("A PROIBIÇÃO DE FALAR COM OS HUMANOS",
  ["mas o proibia os deuses de falarem com os humanos"],
  None),
],
"RC-488": [
 ("A ETIMOLOGIA FALADA: ANUNA = ACARIANO, NOME SUMÉRIO = NEFELIM",
  ["o nome Anuna é uma expressão acadiana que foi encontrada nas tábulas sumérias", "Mas o nome dos anunaques na linguagem suméria é nefelim"],
  None),
 ("A TRADUÇÃO QUE CANCELA A PERCEPÇÃO",
  ["Gigante é uma coisa, o extraterrestre é outra", "as traduções foram nos emborrecendo, foram nos cegando"],
  "⭐ É também o argumento metodológico desta Base: se a tradução perde, a grafia do STT é dado filológico — ver camada-1 §7."),
],
"RC-516": [
 ("OS TESTES COM CASAIS DE HOMINÍDIOS",
  ["fazer os testes de manipulação genética com vários casais de hominídios para ver o que é que dava de resultado",
   "começaram a fazer teste de manipulação genética assim que laboratórios puderam ser construídos por eles aqui na Terra"],
  None),
 ("A PANDORA COMO CONTRAPROGRAMA",
  ["O gene de Henk e a revolução de metamorfose que Pandora fez no próprio genoma quando se transformou numa fêmea racional"],
  "[REVISAR: «Henk» — ver RC-486 e o item 2 da devolutiva.]"),
],
"RC-461": [
 ("A IRMÃ QUE DECIDIU COM ELE: NINHARSAK NOS TESTES",
  ["se por trás da decisão que ele e a irmã dele Ninharsak tomaram"],
  "⚠️ A fonte usa a mesma família de grafias para Ninmah/Ninharsag (8 ocorrências); não desmembrar sem decisão do Curador."),
],
"RC-489": [
 ("ENOQUE TRADUZIDO EM REGISTRO TÉCNICO-ORAL: «DENTRO DE UM MACACÃO»",
  ["mas Eno foi dentro de um macacão e ainda assim morreu porque não conseguiu ficar muito tempo lá"],
  "⭐⭐ Nenhuma fonte anterior da Base contém esse detalhe (a travessia com traje)."),
 ("A EMBAIXADA E A AGENDA",
  ["quando Javé mandou Enoque ser levado até o seu hábitat para ele dizer a Enoque a agenda"],
  None),
 ("A ÁRVORE CRIADA POR ELE",
  ["É uma representação que Enoque, um humano, criou"],
  None),
],
"RC-671": [
 ("METATRON = FORMA ANTIMATERIAL DE ENOQUE, **COM PRAZO**",
  ["ficou a figura de Metatron, que é a forma antimaterial de Enoque, mas que funcionou só durante um tempo"],
  "⭐⭐⭐ A limitação temporal da função não consta das fontes anteriores da Base → ampliação de conteúdo."),
 ("A PREPARAÇÃO DOS POUCOS DESPERTOS",
  ["explicar os anjos de Jaavé, os poucos despertos que tinham aquela situação"],
  None),
],
"RC-673": [
 ("A INTERCESSÃO NARRADA EM 14/10/2023 (anterioridade)",
  ["Javé mandou Enoque ser levado até o seu hábitat", "ainda que Enoque depois disso fosse viver definitivamente no universo vizinho"],
  "🆕 anterioridade: P2023-12-02 — esta fonte é **7 semanas** anterior."),
],
"RC-424": [
 ("A LISTA DOS PATRIARCAS, COM O CORTE PRÓPRIO DA FONTE",
  ["Aí Adão termina produzindo um terceiro filho chamado Sete", "todo Os escolhios de Javé se fazem"],
  "⚠️ Duas listas patriarcais na mesma fonte, com cortes diferentes (U0015 × U0033): divergência de STT, **não** de doutrina — registrar sem harmonizar."),
],
"RC-072": [
 ("A INSEMINAÇÃO E A PATERNIDADE CÓSMICA",
  ["O DNA de Sofia, inseminado artificialmente em Maria"],
  "⚠️ quarentena teológica (retenção): conteúdo de ficha, não de apostila."),
 ("A TRANSFIGURAÇÃO REDESCRITA: OS ANJOS COMO PLATEIA",
  ["Jesus não se transfigurou na chamada transfiguração descrita nos nos evangelhos para que os anjos vissem que mesmo ele na condição humana, ele tava sabendo muito bem o que tava fazendo"],
  None),
 ("O GETSÊMANI E A RECUSA DOS PODERES COMO QUESTÃO DE HONRA",
  ["Javé, me livre desse cálice", "Não use os seus poderes para escapar da crucificação, que seria deshonroso para você"],
  "⭐⭐ É o ponto exato em que o tema do título (honra) toca a cristologia da fonte."),
 ("O REINO NÃO DESSE MUNDO E O «FEZ DE TUDO E NADA»",
  ["Meu reino não é desse mundo", "Fez de tudo e nada"],
  None),
],
"RC-005": [
 ("A VOLTA COMO QUESTÃO DE HONRA, NÃO DE PODER",
  ["vou cumprir as promessas que o meu eu humano fez enquanto Jesus", "É uma questão de honra"],
  None),
 ("O HEDGE TRIPLO QUE FECHA A PROFECIA",
  ["Vai acontecer se não matar ele", "É conveniente que a gente não espere, ainda que ele venha, mas também não muda nada"],
  "⭐⭐ A fonte **mantém** a promessa e **recomenda não esperá-la**: registrar o par, sem escolher um dos lados."),
 ("A CONDIÇÃO CELESTE DA VOLTA",
  ["ele voltaria no futuro, não nascendo como um simples homem, mas na sua condição celeste"],
  None),
],
"RC-161": [
 ("A MEMÓRIA QUÂNTICA COMO IMPEDIMENTO DO JUIZ",
  ["Os próprios fatos da obra de Javé marcado na memória quântica dos elétrons inviabilizaram a conduta de Javé como juiz"],
  None),
 ("O BURACO NEGRO DE MÃO ÚNICA (a física oral da fonte)",
  ["Então, buraco negro seria o que leva notícia, notícia daqui para lá, mas não traz notícia de lá para cá",
   "aquela informação se transforma em 2D, entra no buraco negro e deixa de existir"],
  "⭐⭐⭐ A «cópia da informação aqui se mantém» é o ponto de contato exato com a tese desta ficha; a grafia do bruto é «pronto de evento»."),
],
"RC-378": [
 ("A OBRA CITADA NOMINALMENTE EM PALESTRA, EM 2023",
  ["E só entende isso quem entendeu que tá escrito no livro Rebelião dos Elétrons"],
  None),
],
"RC-094": [
 ("OS POSTULADOS DA REVELAÇÃO CÓSMICA COMO ÚNICA VIA DE COMPREENSÃO",
  ["mais razoável sobre o universo vizinho e seus habitantes através dos postulados da revelação cósmica"],
  None),
],
"RC-381": [
 ("CAMPOS MÓRFICOS COMO INSTRUMENTO DE OPERAÇÃO (materialização autorizada)",
  ["Nós estamos falando aqui de campos mórficos que são usados por seres desse universo vizinho"],
  "🆕 anterioridade: P2024-04-14"),
 ("O ROUBO DO SENSO CRÍTICO",
  ["Essas locas que sabem disso estão acompanhando o progresso dos seres humanos e roubando o senso crítico da para eles poderem passar melhor"],
  None),
 ("A NOVELA DAS 8",
  ["Nós somos a novela das 8 para eles"],
  None),
],
"RC-191": [
 ("A «REDE DE FOFOCA» DA ESPIRITUALIDADE, DITA PELO EXPOSITOR (materialização autorizada)",
  ["o espírito que me anima faz parte de uma rede de fofota grande na espiritualidade", "pelas fofocas do circuito ao qual o espírito que me anima pertence"],
  "🆕 anterioridade: P2025-02-15"),
  ("O LIMITE ÉTICO QUE ELE MESMO SE IMPÕE",
  ["Segundo eu postar errado naquilo que eu percebi e trouxe"],
  "⭐⭐ A autodeclaração de **grau de testemunho** da fonte: saber sem poder usar. Deve acompanhar qualquer citação desta ficha."),
 ("A NEGAÇÃO DA FACULDADE DE PERCEBER",
  ["Eu não, eu eu não tenho essa capacidade de perceber"],
  None),
],
"RC-589": [
 ("A ÓRBITA DE 3.600 ANOS E O «CHARLES» DO STT",
  ["Então aqui dá 3.600 anos", "a última vez que Nibiro passou aqui próximo à Terra"],
  "⚠️ **Não fixar a data da última passagem**: a resposta é autocontraditória na própria fala («2000 496» / «499» / «6 anos de Cristo»)."),
 ("O POUSO EM TRÊS NÚMEROS",
  ["Pousou na Terra cerca de 450.000 anos atrás", "abrir caminho no cinturão de asteroides usando bombas nucleares"],
  None),
 ("2012: O LACRAMENTO DOS PORTAIS POR ENTROPIA CÓSMICA",
  ["no ano 2012 eles se lacraram devido a entropia cósmica", "Em 2012 isso foi lacrado"],
  "⭐⭐⭐ ⚠️ **Divergência de objeto, selada com a data da fonte**: aqui 2012 é o lacramento dos **portais**; a Base trata 2012 como recuo de consciência humana. Nenhuma das duas leituras substitui a outra."),
 ("O SOL COMO VIA DE TRÂNSITO (e não como «o portal»)",
  ["eles passaram a usar as estrelas como sendo um tipo de portal natural", "E essa invasão tá se dando pelo sol, mas também já está se dando portais"],
  "A formulação «o portal é o Sol», aventada na leitura inicial, **não existe na fonte** (retirada documentada em camada-0 §23)."),
],
"RC-587": [
 ("O SELO DE ANU NA CARTA DE GAUZU (material inédito para a ficha)",
  ["E Gauzu entrega a Enque e a Enlil uma carta de recomendação com o selo de Anu", "É, mas eu não conheço nemum o Gauzu"],
  "⭐⭐ A cena do emissor desconhecido — o selo autêntico e a assinatura não reconhecida — não consta das fontes atuais da Base."),
 ("ANU E O CONSELHO DOS SETE DIANTE DA INVASÃO",
  ["E Anu e o conselho dos sete ainda valiam os efeitos colaterais que a invasão na parte das forças do universo vizinho poderá provocar"],
  None),
 ("A EXPECTATIVA DE UMA DECISÃO QUE NÃO CHEGA",
  ["eles estão esperando uma decisão de Anu, que por sua vez está vinculada de Henk"],
  "[REVISAR: «Henk» — item 2 da devolutiva (leitura dupla documentada; não unificar a Enki).]"),
],
"RC-583": [
 ("AS CINCO BOMBAS RESTANTES E O VALE DO SIDIM",
  ["Tomam as cinco bombas restantes e soltam em cima das cidades do vale do Sidim",
   "que se deu a cerca de 4.000 anos atrás, exatamente na mudança da era zodiacal"],
  "⚠️ Selar: a data das bombas **nesta fonte** é ~4.000 anos; os «2200 anos antes de Cristo» pertencem a outro evento (a vez de Marduque). Não fundir as duas cronologias."),
 ("A GUERRA QUE OS TIROU DA TERRA",
  ["desde que eles explodiram as bombas em cima Sodoma e Gomorra e mais as outras cidades do Vale do Sidim"],
  None),
 ("OS POUROS QUE FICARAM: A GUARDA BAIXA",
  ["não têm concentração de força suficiente aqui para dominar nada"],
  None),
],
"RC-580": [
 ("A REVOLTA DOS IGIGI, DATADA POR ESTA FONTE",
  ["uma um certo tipo de anunque chamado Igii veio pra Terra"],
  None),
 ("A ESCASSEZ DE MÃO DE OBRA COMO CAUSA DA FABRICAÇÃO",
  ["sempre eram poucos para a quantidade de trabalhos 300.000 anos, 200.000 anos, 100.000 anos"],
  None),
],
"RC-588": [
 ("NINURTA E A RECUSA DA CHEFIA",
  ["Ninurta, filho de Eli, disse:", "Não, os dois foram pro pau"],
  "⚠️ A grafia «Eli» para Enlil é do STT; o par Marduk–Ninurta é o da fonte, não uma dedução."),
],
"RC-460": [
 ("MARDUK, A VEZ DELE E AS CIDADES SIMPÁTICAS",
  ["Quando chegou a vez de Marduque assumir, 2200 anos antes de Cristo, a chefia ou comando Anuna aqui na terra", "essas cidades eram simpáticas a Marduk"],
  None),
 ("O REI QUE NÃO CHEGOU A REINAR: NERGAL E NINURTA",
  ["eergal e no lurtte", "Isso tá descrito nos livros animais"],
  "[TEXTO CORROMPIDO: «eergal e no lurtte» ≈ Nergal e Ninurta; «livros animais» ≈ livros annunaki — [REVISAR], não decodificar.]"),
],
"RC-559": [
 ("A TESITURA DA TEIA DA VIDA, ESTUDADA PELAS TRÊS FIGURAS",
  ["cada um estudava parte da tesitura da teia da vida, ou seja, da teia da existência dos deuses"],
  None),
 ("O QUE SAI VOLTA — E O CAMPO QUE O GUARDA",
  ["Tudo volta a ser energia que pode ser colapsada de acordo com o que o euma"],
  None),
],
"RC-658": [
 ("ORLOG CRIA A WYRD E AS TRÊS NORMES",
  ["Porque o ser chamado Orlog, ao criar a Word, criou três normes e as três, cada um estudava parte da tesitura da teia da vida"],
  "[REVISAR: «Word» = Wyrd (grafia do bruto); «normes» = Nornes.]"),
 ("O ESTUDO DA WER COMO ÚNICO ACESSO À QUESTÃO DO DESTINO",
  ["Só o estudo da WER, que é uma teia quântica da mitologia nórdica"],
  None),
],
"RC-467": [
 ("A DISTINÇÃO TÉCNICA QUE A FONTE ATRIBUI AOS ANUNNAKIS",
  ["tudo na vida deles é ou acontece por fado ou sorte ou acontece por destino",
   "o que era o inevitável destino"],
  "⭐⭐ A fonte não usa as Moiras/Nornes como metáfora: usa a distinção como **categoria de decisão** de outro povo."),
 ("A PERGUNTA QUE ABRE O BLOCO FILOSÓFICO",
  ["tudo na vida deles é ou acontece por fado ou sorte ou acontece por destino"],
  None),
],
"RC-702": [
 ("A CAMUFLAGEM COMO CONDIÇÃO DO AFFETO (uso novo, não anterioridade)",
  ["para que a camuflagem da realidade nos faça pensar isso", "Se a gente abrir o corpo de um ser humano ou de qualquer ser vivo dentro Tudo é podridão, só que bem organizada, funcionando maravilhosamente"],
  "As fontes desta ficha já são anteriores a 14/10/2023: entra **uso novo**, sem nota de anterioridade."),
],
"RC-395": [
 ("RAGNAROK: OS 300 MILHÕES DE ANOS DESTA FONTE (três vezes)",
  ["Quando os anunques souberam do Rainarok ocorrido há 300 milhões de anos e que Sofia também não fez nada",
   "A mitologia nórdica aponta que há 300 milhões de anos atrás, oito dos níveis de um universo vizinho que existe paralelo ao nosso"],
  "⚠️ Terceira cifra no acervo para o mesmo evento (a Base tem 300 mi em B050 e 400 mi em P2021-05-15): **selar com a data**, não harmonizar."),
 ("A SOBRE-VIDA COMO «SOBRA DE UM PROBLEMA»",
  ["eles sejam uma sobra de um problema ocorrido a cerca de 300 milhões de anos atrás"],
  None),
],
}

BLOCOS.update({
"RC-713": [
 ("TEURGIA, MAGIA E A FACE DA TEOLOGIA (fecho do bloco cabalístico)",
  ["Sim, porque daí é trabalho com os elementos", "Magia é uma das faces da teologia"],
  "A pergunta é do ouvinte («isso chama-se teurgia, não é?») e o expositor **aceita o termo**: a ficha registra o uso, não a prática. ⚠️ Nenhum código novo para «teurgia» (navalha; Devolutiva D-1)."),
 ("A DECLARAÇÃO DE QUE A PARTIR DE AMANHÃ PODE PARAR",
  ["Pode ser que a partir de amanhã entropia em peça, mas até hoje sim"],
  "[TEXTO CORROMPIDO: «entropia em peça» é o que o STT entregou; preservar, não decodificar.]"),
],
})

# BLOCO 2 — termos de cadastro SEM FICHA (vínculo na malha; conteúdo aqui).
SEM_FICHA = [
 ("RC-396 · Kvasir e Freya (Vanir/Aesir) — **NÃO VINCULADA** (Devolutiva item 9)",
  ["E nessa tigela tinha o quê", "A saliva de várias pessoas"],
  "A fonte **descreve** a nascença a partir da tigela de saliva dos Æsir e Vanir, mas **não pronuncia «Kvasir»** (0 ocorrências medidas). Por decisão expressa do Curador, a ficha permanece `ficha=False` e **esta fonte não entra no cadastro**; fica pendente de uma fonte oral que nomeie a figura."),
 ("RC-672 · Os 366 Manuscritos de Enoque — **NÃO VINCULADA** (checagem verbatim)",
  ["anunciada desde os tempos de Enoque e confirmada por Gauzu"],
  "⚠️ A contagem «366 manuscritos» **não ocorre** nesta fonte (0 ocorrências medidas). A hipótese levantada na leitura inicial foi **retirada** e documentada em `camada-0.txt` §23; o vínculo foi recusado antes da aplicação."),
 ("RC-167 · Criação indevida (obra indevida) — leitura acessória",
  ["para romancear esse problema de abertura de portais e o fato de seres desse universo vizinho usarem humanos, manipularem humanos"],
  "A auto-declaração de «romancear» um problema real é a fronteira entre ficção e doutrina nesta fonte; fica como conteúdo de leitura, sem vínculo estrutural."),
]

# BLOCO 3 — TERMOS-OBSERVAÇÃO: veto de código mantido (Devolutiva D-1); viram glossário/ Apêndice da apostila.
OBSERVACAO = [
 ("HONRA / «HONRA DEMODÁRMICA» (77 ocorrências no bruto; nenhum termo da Base no nome)",
  ["a honra demodármica é uma honra que foi criada em torno do conceito de dharma"],
  "Decisão D-1: **sem código novo**; verbete no Apêndice do dicionário STT, nota em RC-474/RC-745 e linha de conteúdo em RC-322."),
 ("POVO ESPÉCIE", ["questão de honra do povo espécie nesse contexto"], "absorvido em RC-024, sem termo"),
 ("PODER CIRCUNSTANCIAL × PODER DE DOMINAÇÃO", ["eles têm poderes circunstanciais, mas não tem poder de dominação"], "absorvido em RC-024/RC-742 como **fórmula de segurança** obrigatória da fonte"),
 ("FADO OU SORTE (a grafia do bruto: «fato ou sorte»)", ["que eles chamam de fato ou sorte"], "absorvido em RC-467/RC-658; o STT grafa «fato» em pelo menos uma linha — não corrigir"),
 ("ADIDAIVA / «ADAIVA» (duas grafias, mesma palavra)", ["São seres de condição adaiva"], "absorvido em RC-102/RC-037/RC-104, sem termo novo"),
 ("ZUDRA (≈ Ziusudra; a Base não grafia o nome acadêmico)", ["É, Zudra e Noé são efetivamente a mesma pessoa"], "absorvido em RC-424; grafar **Zudra** com [REVISAR]"),
 ("ALALU", ["Quando a Lalu veio pra Terra, e descobriu que aqui tem ouro"], "absorvido em RC-024/RC-587; sem código (o slot não existe e a navalha manda)"),
 ("GAUZU (Gazu · Gauzul · Galzu — 19 ocorrências)", ["Gauzu diz no livro de Henk, a morte, meus camarados, chegou com rapidez aos retornados"], "absorvido em RC-587/RC-487; verbete no Apêndice"),
 ("«LIVRO DE HENK» (3 ocorrências) — item 2 da devolutiva", ["Parte do que eu vou dizer agora para vocês está registrado no livro de Henk"],
  "⚠️ **Leitura dupla documentada, por decisão do Curador**: (a) livro **de** Enki (a voz «Henk» = Enki) × (b) livro **sobre/entregue por** Henk, o emissário que chefia os 50 («uma espaçonave com 50 anuna chefeados por Henk»). **Não** unificar com RC-486; **nenhuma** obra entra no cadastro."),
 ("«LOCA» (morada divina) — 11 ocorrências", ["o Brama loca, ou seja, a loca do próprio criador caído"], "absorvido em RC-037/RC-102, sem termo novo"),
 ("ESFERAS ESPIRITUAIS CONVERGENTES (Terra × Nibiru)", ["no que se refere a suas esferas espirituais"], "sem equivalente exato na Base: **não** criar código; nota de leitura em RC-532/RC-324 fica pendente de decisão futura"),
 ("INTULIÇÂO? «INTELIGÊNCIAS ARTIFICIAIS AUTÔNOMAS» (1 menção, 14/10/2023)", ["os espíritos me levar a inteligências artificiais autônomas estão funcionando aqui na terra"],
  "⚠️ Datar e selar; não retroprojetar sobre fontes anteriores nem projetar sobre as posteriores. Sem código."),
]

# BLOCO 4 — RADAR DE ACERVO (fonte não localizada: declarar, não vincular).
RADAR = [
 ("Palestra anunciada para o dia seguinte (15/10/2023, 10h — o autor pensava 15h)",
  ["Inclusive lembrar que a palestra amanhã às 10 da manhã"],
  "✅ **Devolutiva item 8:** manter no radar como «fonte não localizada»; **não** criar ciclo antecipado nem peça fantasma."),
 ("Memória de falas anteriores do autor", ["Você já falou isso em outros vídeos"],
  "as auto-referências a «outros vídeos» e às citações já dadas «aqui mesmo» (os avisos de Gauzu repetidos em U0003 e U0041) ficam declaradas como fonte não localizada, sem vínculo na malha"),
 ("«Irém Iron, Universos emissão, Colisão» (obra própria, declarada ficção)",
  ["Existe um livro, Iré Iron, que nós escrevemos juntos em que eu pedi a ajuda deles pra gente"],
  "✅ **Devolutiva item 5:** registrar **estritamente em nota bibliográfica** — não vira obra, não vira vínculo estrutural, não vira ciclo. A grafia do bruto oscila «Iré Iron» × «Irém Iron»."),
 ("«Zintzum, o exílio forçado de divindade»", ["eu analiso isso no livro que eu lancei chamado Zintzum"],
  "✅ **Devolutiva item 4:** corresponde à **B013** já cadastrada; **0 obras novas**."),
 ("Obras nomeadas pela fonte sem identificação estável («livro de E», «obra de Z», «livro P», «Atraares», «livro de EC»)",
  ["Isso está registrado no livro P, no Atraares"],
  "⚠️ [TEXTO CORROMPIDO]/censura do transcritor: **nenhum** título entra no cadastro; hipóteses de leitura (Atrahasis, Enoque) ficam como hipótese do auditor, nunca como fato."),
 ("«300 sites» e os circuitos de informação não nomeados", ["tem uns 300 sites dizendo que Nibiro tá atrás do sol"],
  "⚠️ bloqueado pelo item 10 da devolutiva: declarar a existência da alegação, não a reproduzir em material de divulgação"),
 ("«Bob Din» [REVISAR] e os relatos de contato", ["existe um cara chamado Bob Din que que é um ex-surgent major das Forças Armadas dos Estados Unidos"],
  "identidade **não fixada** pela Base: hipótese de leitura do auditor apenas; sem vínculo, sem obra, sem verbete canônico"),
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
        txt = f"- **{cod}**"
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
            txt = f"- **[{SIGLA} · {rot}]**"
            if corpo:
                txt += f" {corpo}"
            if nota:
                txt += (f" — {nota}" if corpo else f" {nota}")
            linhas.append(txt)
        linhas.append("")
    extra = []
    extra += _corpo(SEM_FICHA, "\n## BLOCO 2 — TERMOS DE CADASTRO SEM FICHA (vínculo na malha; conteúdo aqui)\n")
    extra += _corpo([(f"TERMO-OBSERVAÇÃO · {c}", a, n) for c, a, n in OBSERVACAO],
                    "\n## BLOCO 3 — TERMOS-OBSERVAÇÃO (VETO DE CÓDIGO MANTIDO — Devolutiva D-1)\n"
                    "Nenhum vira código: entram no glossário e no Apêndice do dicionário STT da apostila, absorvidos nas fichas indicadas.\n")
    extra += _corpo([(f"RADAR · {c}", a, n) for c, a, n in RADAR],
                    "\n## BLOCO 4 — RADAR DE ACERVO (fonte não localizada — declarar, não vincular)\n")
    cab = (f"# PACOTE DE AMPLIAÇÕES — {SIGLA} (A Esquecida Honra dos Anunnaki)\n"
           "# Gerado por _gerar_ampliacoes_P2023-10-14.py: toda citação foi extraída byte a byte do\n"
           "# `original.txt` a partir de âncoras — nada aqui foi digitado de memória.\n"
           "# Alterações mecânicas declaradas: (i) aspas duplas internas da fonte viram «…» (aspas_internas());\n"
           "# (ii) quebras de linha do bruto dentro da mesma frase viram espaço — nenhuma palavra é tocada.\n"
           "# 0 códigos novos (Devolutiva 28/08/2026: teto 777 inviolável; «honra» fica como termo-observação — D-1).\n"
           "# Nada dos blocos bloqueados (item 10) entra aqui; RC-396 e RC-672 estão fora por decisão/checagem.\n\n")
    open(SAIDA, "w", encoding="utf-8").write(cab + "\n".join(linhas + extra))
    print(f"pacote emitido: {len(BLOCOS)} fichas · {sum(1 for l in linhas if l.startswith('- '))} blocos")
    if erros:
        print("\nERROS (corrigir âncoras):")
        for e in erros:
            print("  ✗", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
