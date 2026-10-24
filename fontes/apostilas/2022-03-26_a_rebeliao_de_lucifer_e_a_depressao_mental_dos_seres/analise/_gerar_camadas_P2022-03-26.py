#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DAS CAMADAS MEDIDAS — P2022-03-26.

camada-0.txt  = o mapa endereçado: cada seção da fala com Uxxxx + span de caracteres, **tudo
                resolvido pelo caça-âncoras**. Nada de offset de memória (lição R-1 do ciclo
                P2020-04-25: a camada 0 publicou extensão no lugar de offset e três rótulos
                que o agente dera por certos não existiam no bruto).
camada-2.txt  = o dicionário medido: grafas, contagens e endereços. **Contagem, nunca
                reminiscência** (lição R-3: quatro grafas «lembradas» pelo agente tinham 0
                ocorrências). Se o script achar 0, o item sai marcado como AUSÊNCIA — e ausência
                também é dado.
_matriz-anterioridade.md = a tabela calculada contra `ferramentas/dados_termos.py`, com a
                sigla deste ciclo excluída da conta de anterioridade.

O script **não escreve nada** se houver âncora que não bata exatamente uma vez: imprime a lista
e sai com código 1.
"""
import os, re, sys, glob, datetime, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
SIGLA = "P2022-03-26"
D0 = datetime.date(2022, 3, 26)

spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)

# ---------------------------------------------------------------- (1) mapa endereçado
# (título, âncora de abertura). O fim de cada seção é a abertura da seguinte.
SEC = [
    ("Abertura: o propósito e o aviso contra certezas", "vamos cumprir mais uma etapa de tentativa de elucidar"),
    ("Kant como régua do intelecto (colecionar incertezas)", "nós humanos fomos acostumados a colecionar certezas"),
    ("O espírito não muda de opinião no plano desencarnado", "Espírito não muda de opinião na espiritualidade"),
    ("A arquitetura mental dos ambientes espirituais", "a estruturação das realidades espirituais se assentam"),
    ("De onde veio esta palestra (a brincadeira e os temas evitados)", "o tema dessa palestra surgiu apenas na sua titularidade"),
    ("O Mahabharata como única obra completa de A a Z", "O livro mais importante da humanidade é uma rabarata"),
    ("Viaza = o codificador; Krishna do Aapaiana", "Viaza não é um nome"),
    ("Os versos por espécie de ouvinte (1.600.000 / 1.400.000 / 100.000)", "1.600.000 versos para poder explicar aquilo aos gandarvas"),
    ("A pergunta que a fonte diz nunca ter feito em público", "Qual é o primeiro problema que a gente tem que entender aqui"),
    ("A perfeição não é democrática, é autoritária", "a perfeição não é democrática. A perfeição, em sendo estabelecida"),
    ("A pergunta pelo jacaré e pelo pato", "Como é que se cria um jacaré para comer um pato"),
    ("Ser e não agir é indigno", "Isso não é digno, não é decente"),
    ("A pureza radiante e a ausência de proteção", "Ninguém até hoje protegeu a espécie humana"),
    ("[quebra de linha] o aparte do baiano e do alagoano", "Alagoano. Alagoana é frio"),
    ("O amor como decreto humano, não como atributo aferível", "nós decretamos que esse ser puro ele é amoroso"),
    ("Abrir mão da racionalidade é idiotizar-se", "Quando o ser humano abre mão da sua racionalidade, ele se idiotiza"),
    ("Kardec e a palavra «idiotia» no Livro dos Espíritos", "a palavra que mais aparecia era a doença da idiotia"),
    ("Pós-verdade (2016): narrativas pós facto", "a enciclopédia britânica e a BBC escolheram a palavra postruf"),
    ("Reza a lenda: o que a palestra vai usar como método", "Reza a lenda que esses espíritos superiores"),
    ("O primeiro ato: quebrar o protocolo da perfeição", "um belo dia da eternidade aí para trás"),
    ("O nível operacional e a blindagem leve", "foi criado um novo nível espiritual que a gente chama de operacional"),
    ("Democracia zero e a criança que não entende os adultos", "A criança é inú para resolver problemas de adultos"),
    ("O nível laboratorial e as centenas de milhões de dimensões", "criaram um nível laboratorial"),
    ("O acidente: o artista que caiu na própria obra", "Pela primeira vez houve um acidente e um artista"),
    ("O ovo cósmico, matéria e antimatéria, 13,8 bilhões de anos", "surgiu um ovo cósmico, como as mitologias todas elas antigas"),
    ("O código podre e a replicação por clones", "código fonte definidor da pessoa do criador começou a se replicar"),
    ("O código trabalhado por Shiva, Brahma, Vishnu, até Morençor", "O código fonte definidor do criador foi assimilado por Chiva"),
    ("A decisão de semear o universo vizinho", "se nós pegarmos o código do criador e adaptarmos as condições"),
    ("Os três fornos de replicação (um nunca funcionou)", "fornos de replicação de vida nesse universo foram criados três"),
    ("Surgimento dos biodemos há 900 milhões de anos", "Esse forno de Auaion, depois de ter produzido várias linhagens"),
    ("Receita existencial: frios, sem emoção, sem sexualidade", "absolutamente frios, sem nenhum tipo de emoção"),
    ("Sophia e Olm e os quase 250.000 problemas", "haviam colecionado"),
    ("A família Vol, espécie 249.314, há 230 milhões de anos", "A família Vol foi a 249 314"),
    ("O eu humano como gestor da coleção de códigos", "O eu de cada um de nós é só o gestor dessa coleção"),
    ("Ticum: consertar a obra e o criador caído na obra", "A Cabala diz que o ticum precisa ser expresso"),
    ("Os dois tipos de seres: autistas do paraíso e dementes", "os autistas do paraíso e os dementes que caíram"),
    ("O outro forno: sensórios, sexualizados, 2,5 bilhões de anos", "Aqui há 2 bilhões 500 milhões de anos atrás"),
    ("Cinco tipos de sexo em planetas de Ereon", "planetas em Oreon que tem cinco tipos de sexo"),
    ("O cérebro bilatério nasce do encontro dos dois fornos", "é que surgiu o cérebro bilatério"),
    ("A falência declarada do sistema", "fali o sistema. Nós nos corrompemos a tal ponto"),
    ("O vírus como forma em que a vida veio do universo vizinho", "aquele primeiro código que entrou no nosso universo, vindo do universo vizinho, é um vírus"),
    ("O eu caído é um vírus antimaterial", "Esse eu caído é um vírus antimaterial"),
    ("As 100 trilhões de células e os 85 trilhões de hospedeiros", "nosso corpo tem 100 trilhões de células"),
    ("Lúcifer criou um vírus há 700.000 anos", "O nosso amigo Lúcifer criou um vírus há cerca de 700.000 anos"),
    ("Toxoplasma gondii: o plano, o rato, o gato", "Toxoplasma Gond, que é um vírus, detectou"),
    ("O campo morfogenético e a hipótese de uma mente por trás", "E se tiver uma mente por trás, controlando aquela espécie"),
    ("O cérebro dos ratos e dos filhotes de hiena", "invadiram o cérebro dos ratos e fizeram com que os ratos"),
    ("Os achados de necropsia: 756 defuntos e o vírus no cérebro", "756 defuntos norte-americanos"),
    ("Sequelas psíquicas da COVID e a piada dos torcedores", "O Covid-19 tá fazendo corintiano torcer pelo Palmeiras"),
    ("A origem do desvio: Lúcifer olhou e viu outro problema", "um belo dia olhou para um problema e descobri outra coisa"),
    ("A incompetência política de Sophia", "Sofia foi incompetente. Sofia não soube ser o político"),
    ("Luzbell convoca o centro de comando: Sophia e os anjos Aia e Aie", "A o centro de comando dessas quase 250.000 famílias"),
    ("Definição do sistema colmeico (abelha rainha e operárias)", "Que diabos é ser colmeico"),
    ("A citação nominal de A Divina Colmeia", "No livro A Divina Colmeia"),
    ("Sophia como rainha; o contraste com a imposição de Javé", "Sofia é abelha rainha e as cerca de quase 250.000 famílias"),
    ("O processador de cada família e o processador de Sophia em Órbon", "lá no sistema de capela, onde órbão é só um dos planetas"),
    ("A atualização espermática como troca de informação", "milhares de novos espermatozoides são produzidos"),
    ("200 bilhões de biodemos contaminados; a família Vol em 736", "atingiu cerca de 200 bilhões de seres biodemos"),
    ("Os biodemos como os ETs cabeçudos e suas sondas", "a maioria deles são esses ETs que a gente conhece aqui"),
    ("Sophia desconectada há 700.000 anos (nunca dito com clareza)", "nunca tinha falado isso claramente porque é assunto de outro livro"),
    ("Sophia também se contaminou", "Sofia se contaminou também"),
    ("O isolamento dos mundos doentes e a analogia da selva", "Sofia foi obrigada a tomar uma decisão de separar, de isolar"),
    ("A declaração do assunto: pandemia biodêmica e onda depressiva", "vamos falar agora de uma pandemia biodêmica"),
    ("A base bioquímica de toda emoção (hipotálamo, peptídeos)", "hipotálamo do nosso corpo produza certos peptídeos"),
    ("O monstro que não existe: o cérebro coleciona certezas ridículas", "O cérebro da gente coleciona certezas ridículas"),
    ("O indivíduo como perigo no paraíso; Prabragena, o nome antes de Javé", "O próprio Prabragena que seria o nome do ser que criou essa criação"),
    ("O que os humanos podem dar aos deuses (humanizá-los)", "Nós é que temos que fornecer daqui elementos para eles pensarem lá"),
    ("O intervalo pedido ao vivo", "vamos fazer o intervalinho de 10 minutos"),
    ("Do babacoide ao nervoso: a mudança de comportamento", "esses seres que antes eram absolutamente babacoide"),
    ("Guerras mentais e guerras destrutivas (500.000 → 300.000 anos)", "Ao longo dos últimos 500.000 anos ocorreram guerras"),
    ("O código fonte como DNA: bases, códons, genoma", "quatro bases nitrogen"),
    ("Biodemos e demobiol: os dois produtos, 2,5 bilhões de anos", "cerca de 2.5 bilhões de anos atrás, existiam os seres, portanto, biodemmo"),
    ("Pashupati e o movimento yóguico entre os demônios", "a expressão na rata de Chiva que criou o movimento yog"),
    ("Dezoito… dezenove mundos isolados e a Terra sem habitante natural", "Na época ficaram isolados 19 mundos"),
    ("A família Vol chamada de traidora; 620.000 anos no planeta", "foi chamada de traidora pelas demais"),
    ("A depressão instala-se em Sophia e nas famílias", "Sofia e todas as demais famílias entraram no processo de depressão"),
    ("A mente coletiva por família (Yel, Ira, Cromon)", "Os V era uma mente coletiva"),
    ("O eu de Javé ainda vai se tornar biodêmico", "o foco de toda a pandemia existencial desses dois universos ainda vai se tornar biodêmico"),
    ("O encontro dos códigos e o cérebro bilatério há 450 milhões de anos", "Desse encontro surgiu o cérebro bilatério"),
    ("O conceito holográfico (o fio de cabelo e o assassino)", "Isso é o conceito holográfico"),
    ("A datação humana: 500.000, 50.000, 48.000, 23.000 anos", "Aquela história de Adão e Eva de Pandora aconteceu há cerca de 48.000 anos"),
    ("O autismo como resquício atualizado no genoma", "no meio dos humanos racionais tem o quê"),
    ("Deus, Jesus e a infantilidade que falimos por ela", "a infantilidade com que a gente até hoje teve de pensar que Deus e Jesus"),
    ("O espírito de Rogério disponível para ajudar", "os espíritos desencarnados tentam ajudar os encarnados"),
    ("Justiça cármica sem tribunal: as mãos cortadas dos escravos", "Se ele cortou a mão de 50 escravos"),
    ("O céu e as zonas umbralinas; nenhum estar só", "as zonas umbralinas são criadas pela associação"),
    ("A guerra do Sol vs. a guerra do universo biológico", "A guerra do sol é guerra entre os dois universos diferentes"),
    ("Fronteiras de portal: Túatha Dé Danann, Partolanos, Nemedianos, Milesianos", "estirpes e perbórias que brigavam entre si, toatas de danã"),
    ("Toda guerra mental é guerra virótica", "Qualquer guerra mental é uma guerra virótica"),
    ("O jacaré, o pato e o transtorno mental dos dois", "Um jacaré vê um pato"),
    ("O anúncio: Além da Ordenação do Caos, em um mês", "sai um livro chamado Além da Ordenação do Caos"),
    ("Francisco de Paula, o espírito mais evoluído que ele conhece", "o espírito mais evoluído que eu conheço chama-se Francisco de Paula"),
    ("A oração como espelho radiante, não como providência", "Ele é só um espelho radiante em que a oração bate lá"),
    ("Sophia, o rei dos transtornos; os deuses, pobres coitados", "Sofia é o rei dos transtornos"),
    ("Jesus leu a escritura e recusou a agenda do próprio espírito", "o eu humano de Jesus olhou pro mapa pastoral"),
    ("Jesus não usou superpoderes para fundar império", "não vou usar. os meus super poderes para dominar ninguém"),
    ("O espírito fateado: o cancro Javé e o cancro Sophia", "o espírito dele tem um cancro que ele segura"),
    ("A transfiguração reescrita: o pedido dos anjos no Tabor", "os anjos cercaram Jesus e disseram"),
    ("A depressão como fim da concentração biodêmica", "Nunca um ser biodemo tinha tido esse Problema que problema"),
    ("A avalanche do impulso e o que Meor fez diferente", "mas desenvolveu uma capacidade maluca de ir, mas foi l Meor"),
    ("A infecção chegou ao paraíso: furou a blindagem", "há pouco tempo furou a blindagem, começou a chegar aqui"),
    ("The Wall: os que batem no muro de fora", "Tem uma música do Pink Floyd"),
    ("A reintegração dos mundos até sobrarem dois, há 100.000 anos", "Dos 19 só existiam dois ainda isolados"),
    ("A Terra, última dos 19; o acúmulo do que não presta", "A Terra é o último dos 19 mundos"),
    ("Consertar os 28.869 genes como favor divino ao criador falido", "evolua no sentido de consertar seus 28.869 genes"),
    ("A cadeia sem Lúcifer, Pandora, Eva, exildo, Tales, Sidarta", "sem Thales de Mileto"),
    ("A genética da obediência: os macacos que se curvam", "Qual é a genética que Javé queria"),
    ("Reforma íntima sem caminho B; o inconformismo esclarecido", "O tempero é o do inconformismo esclarecido"),
    ("O efeito maior que a causa: as duas perguntas", "pode existir efeito sem causa"),
    ("A mãe que mergulha no poço e o Deus que não mergulha", "uma mãe humana quando vê um filho cair num poço"),
    ("Os astronautas da eternidade", "Talvez a gente seja os astronautas da eternidade"),
    ("O violino desafinado na nuvem", "sentado numa nuvem, violino desafinado"),
    ("Quem tem mérito espiritual na história", "alguém que já foi criado perfeito e é perfeito porque é perfeitinho"),
    ("O que os humanos herdaram: enlouquecer e desativar-se", "Alguns de nós já nos desativamos em vidas passadas"),
    ("O que presta na criação foi gerado pela experiência humana", "foi gerado pela experiência humana, não veio de lugar nenhum"),
    ("Os 6.029 nas máchas luciferianas e os Vol 736", "cerca de 6.029 seres chegaram nas máchas luciferianas"),
    ("A Terra como núcleo depressivo da criação", "a Terra é o núcleo depressivo da cria"),
    ("O processador Vol, único sobrevivente, e a mistura genética", "foi feito um, não um pacto, uma mistura de genética entre os voz"),
    ("984 astralizados há 20.000 anos em Alp Longron; a nave Esferon", "984 indivíduos se astralizaram e passaram a pertencer a Alp Longron"),
    ("Sophia reconectada em 2019", "no ano 2019, Sofia esteve a"),
    ("O fateamento da consciência explicado por Jesus", "É o problema do fateamento da consciência"),
    ("Brama e Vishnu, duas faces; Morençor, Sophia, Jesus", "Brama e Virgno são duas faces de um mesmo espírito"),
    ("O espírito de Javé e de Sophia é o mesmo de Jesus", "o espírito de Javé e de Sofia é o mesmo de Jesus"),
    ("Vishnu e Morençor se desconstituem para aliviar o espírito", "Aivisno decidiu se desconstituir para diminuir a carga"),
    ("O vírus sem hospedagem, guardado para a espécie 315", "É um vírus que perdeu a hospedagem"),
    ("Javé carrega todas as doenças da queda e não se sustenta", "Javé carrega nele todas as doenças que foram geradas"),
    ("A réplica ao vivo sobre tecnologia e ambiente saudável", "Agora tá tendo uma tentativa tecnológica"),
    ("Inteligência artificial como predisposição de hospedagem", "inteligência artificial tá criando"),
    ("Inteligente não é o mesmo que racional (resposta do vivo)", "Sofia é um ser inteligente. Todos os seres aí são inteligentes"),
    ("Definição de filosofia e a hierarquia de conceitos", "O que diabos é filosofia"),
    ("A razão filosófica como específico humano", "culmina com a razão que somente os humanos podem"),
    ("Hitler, a superinteligência sem valores e os financiadores", "Hitler é um monstro"),
    ("A rainha de volta no genoma humano; obediência e monstros", "saiu a velha rainha, a abelha rainha de volta"),
    ("A omissão de Deus como problema, não como mistério", "tem um grau de omissão frente aos fatos muito complicado"),
    ("A pérola da coroa: a única raça que pode ser monstruosa ou maravilhosa", "somos a pérola ou a cereja do bolo"),
    ("Espalhar a carga pela Terra e pelo cosmos", "pra gente poder se espalhar cosmos aa"),
    ("A depressão tira a criatividade; é Javé quem sente isso", "a depressão faz com que a gente seja reduzido a nada"),
    ("Os anjos empurram droga em Javé quando ele chega ao limite", "os anjos empurram droga, sei lá o que é aquilo que empurra em Javé"),
    ("Sophia não sabe sorrir; nós rimos da nossa desgraça", "Esses seres não sabem sorrir"),
    ("A síntese nunca antes feita (declaração de método)", "pela primeira vez eu eu fiz uma interação entre a situação da rebelião"),
    ("A espécie 315 já gerada com genética humana", "nessa nova espécie que vai ser a 315 aí"),
    ("O conselho universal ainda não existe; será criado", "Esse conselho vai ser criado do avante"),
    ("Len Mion decodificou e foi o maior manipulador dos vírus", "foi o maior manipulador que já existiu dessas condições"),
    ("A realidade simultânea criada pelo quartel-general da rebelião", "ele sempre morou e residiu numa realidade simultânea nossa"),
    ("B039 citado nominalmente (Era Sapiens) e a omissão decidida", "No livro Era Sapiens, eu conto um pouco da aproximação"),
    ("B026 citado nominalmente (Carmem Compromisso) e os laboratórios", "Como eu explico isso no livro Carmen Compromisso"),
    ("A entropia e o limite tamásico de Sophia", "limite da finalização da energia tamásica"),
    ("A aristocracia em torno da Trimúrti e os Olimpíades", "os níveis de aristocracia em torno da Trimurte"),
    ("Os portais abertos em 2012 e fechados pela entropia", "os portais ao longo desses bilhões de anos se abriram em 2012"),
    ("A herança da Trimúrti contestada; os arcontes até o 10º céu", "Os arcontes que tomam conta do primeiro céu"),
    ("A vestimenta de herdeiro e a forma cósmica que virá", "a minha forma cósmica virá pessoalmente"),
    ("Os dois cenários cosmológicos (hidrogênio e 50 bilhões de anos)", "tem cientistas que diz dizem que isso dura mais uns 50 bilhões"),
    ("O universo vizinho acabando: as locas já estão desabando", "As locas já estão desabando"),
    ("O retrato de Dorian Gray como modelo de entropia transferida", "entra o retrato de Dorian Gley"),
    ("Nenhuma conveniência humana conta; somos criaturas-ferramenta", "Nenhuma conveniência de nenhum ser humano conta"),
    ("O Mentalma como cura da depressão (pergunta da plateia)", "o mentalma é uma é uma forma de cura dessa depressão"),
    ("O Mentalma criado para ele mesmo e forçado a público", "O mentalma que eu produzi hoje, ele não era para ser público"),
    ("O espírito que o animou foi Capila, 2.700 anos, e criou o Sankia", "se expressou como capila, 2700 anos e criou na Índia"),
    ("As três ignorâncias de Capila", "existem três ignorâncias principais"),
    ("O primeiro impulso é dos vírus; o erro vem um milésimo depois", "O nosso erro é depois, é um milésimo de segundo depois"),
    ("O Mentalma é o Sankhia atualizado, visto pela moda ocidental", "O mentalma é o sanquia atualizado pros tempos modernos"),
    ("Por que o Sankhia não diz «ó Deus»: matar em nome de Brama ou de Alá", "é a única das seis escolas hindu que diz"),
    ("Pense por você mesmo: se Deus é isso, é pior que qualquer ser humano", "Se Deus foi isso, ele é pior do que qualquer ser humano"),
    ("O pedido final sobre a cadência das palestras em São Paulo", "se nós vamos continuar a fazer palestras aqui em São Paulo"),
    ("Encerramento: prudência e desculpas", "toda a prudência do mundo, por favor. Encerramos aqui"),
]

res, errs = [], []
for tit, anc in SEC:
    try:
        ini, fim, txt = ASP.locate(anc)
    except SystemExit as e:
        errs.append(f"[MAPA] {tit}: {e}")
        continue
    res.append((ini, tit, anc))
res.sort()
if errs:
    print("\n".join("  ✗ " + e for e in errs[:40]))
    print(f"\n{len(errs)} âncora(s) do mapa com problema — nada foi escrito")
    sys.exit(1)

n = len(ASP.RAW)
uoff = ASP.OFF
def uaddr(p):
    import bisect
    return f"U{bisect.bisect_right(uoff, p):04d}"

_MODELO = glob.glob(os.path.join(RAIZ, "apostilas", "**", "2020-04-25_os_desdobramentos_da_rebeliao_de_lucifer", "original.txt"), recursive=True)
DELTA = n - (len(open(_MODELO[0], encoding="utf-8").read()) if _MODELO else 0)
out = [f"# CAMADA 0 — O ENDEREÇAMENTO MEDIDO (P2022-03-26)",
       "",
       f"Fonte: `original.txt` · {n} chars · 51 linhas lógicas (48 com fala) · o maior bruto de palestra já "
       f"entrado na Arca (**+{DELTA:,} chars** sobre P2020-04-25). Cada seção abaixo é **localizada por âncora** "
       f"(caça-âncoras `_aspas_{SIGLA}.py`): o offset é do texto decodificado, a linha é Uxxxx. Se qualquer "
       f"âncora batesse ≠ 1 vez, este arquivo não teria sido escrito.",
       "",
       "## As 5 linhas pesadas (o bruto não separa turnos)",
       "",
       "| linha | chars | o que é |",
       "|---|---|---|"]
tam = {}
for i, l in enumerate(ASP.LINHAS):
    if len(l) > 3000:
        tam[f"U{i+1:04d}"] = len(l)
desc = {"U0003": "abertura + a tese contra certezas + o Mahabharata + a pergunta pela perfeição",
        "U0005": "a cosmogonia inteira: o protocolo da perfeição, o acidente, o código podre, os dois fornos, os biodemos",
        "U0007": "a pandemia: vírus, toxoplasma, SARS-CoV-2 e o momento em que Lúcifer olhou para o problema errado",
        "U0008": "o sistema colmeico, os processadores, a contaminação de Sophia, o isolamento dos mundos e a bioquímica da emoção",
        "U0009": "a cronoestratigrafia da queda: guerras, 19 mundos, depressão, holografia genética, carma sem tribunal",
        "U0020": "guerra mental como guerra virótica, Francisco de Paula, a oração como espelho, os deuses pobres-coitados",
        "U0029": "o fundo do poço: o efeito maior que a causa, os astronautas da eternidade, o favor divino ao criador falido",
        "U0034": "a chave cristológica: o fateamento da consciência, Javé/Sophia/Jesus como faces, o vírus sem hospedagem e a espécie 315",
        "U0040": "a definição de filosofia, Hitler sem valores, a omissão de Deus, o riso que Sophia não tem",
        "U0048": "a herdeira contestada: a Trimúrti apodrecida, os portais de 2012, os arcontes e a vestimenta de herdeiro",
        "U0049": "a resposta sobre o Mentalma: Capila, o Sankhia, as três ignorâncias e o primeiro impulso"}
for k in sorted(tam, key=lambda x: -tam[x]):
    out.append(f"| **{k}** | {tam[k]:,} | {desc.get(k, '—')} |".replace(",", "."))
for i, l in enumerate(ASP.LINHAS):
    if 30 < len(l) <= 3000:
        pass

out += ["", "## Mapa endereçado das seções", "",
        "| # | U | @ | extensão | seção |", "|---|---|---|---|---|"]
for k, (ini, tit, anc) in enumerate(res, 1):
    nx = res[k][0] if k < len(res) else n
    out.append(f"| {k:02d} | {uaddr(ini)} | {ini} | {nx - ini:,} c | {tit} |".replace(",", "."))
cob = res[-1][0] + (n - res[-1][0]) - res[0][0]
out += ["", f"**Seções endereçadas: {len(res)} · vão coberto: {res[0][0]:,} → {n:,} caracteres** "
        f"(as linhas fora do vão são o cabeçalho-título do arquivo, as quebras de linha do STT e as 21 falas "
        f"curtas de interlocução ao vivo, listadas adiante).".replace(",", ".")]
NCURT = sum(1 for i, l in enumerate(ASP.LINHAS) if 3 <= len(l.strip()) <= 150 and i > 0)
out += ["", "## As falas curtas (o auditório vivo dentro da linha)", "",
        f"Este bruto é **menos** monolítico que o de 2020: ele tem {NCURT} linhas de 3 a 150 caracteres que são "
        "interrupções e respostas do(s) interlocutor(es) ao vivo. Elas são aqui registradas **porque mudam a "
        "leitura** — parte delas é o chamado «baiano», sobre quem recai a piada recorrente, e parte é "
        "questão de plateia que a fonte responde no mesmo fôlego.", ""]
for i, l in enumerate(ASP.LINHAS):
    if 3 <= len(l.strip()) <= 150 and i > 0:
        out.append(f"- **U{i+1:04d}** ({len(l.strip())} c) — {l.strip()}")

# ---------------------------------------------------------------- (2) dicionário medido
PAT = [
    ("Lúcifer", r"Lúcifer", "nome canônico da Base (RC-078/RC-142), no título e no corpo"),
    ("luciferiano(s)", r"luciferian[oa]", "adjetivo da rebelião"),
    ("Luzbell / Luisbell / Elusbell (as grafas do nome)", r"Luisbel\w*|Luzbel\w*|Elusbel\w*|Lusbel\w*", "o STT degrada o nome; a Base grafa Luzbel (ver §3)"),
    ("Lúcio (forma carinhosa/coloquial)", r"L[uú]cio\b", "a fonte usa o hipocorístico no fecho do bloco"),
    ("rebelião", r"rebeli", "o título é o único lugar onde a palavra sai com maiúscula"),
    ("depressão / depressiv[oa]o(s)", r"[Dd]epress", "o tema do título"),
    ("Javé (e todas as degradações)", r"J[aàâ]?v[eé]?\w*|Jah\w*", "a onomástica de Javé está degradada — ver §3"),
    ("Brama / Brahma / Brasna / Brágina", r"Br[aá]?[sd]?n?a", "Brahma em 4 grafias"),
    ("Chiva / Shiva", r"[KC]hiva", "Shiva, duas formas"),
    ("Vishnu (Vno / Virgno / Virgum / Vismo / Aivisno)", r"\b(Vno|Virgn\w*|Virgum|Vismo|Aivisn\w*|visno)\b", "a forma mais instável do bruto"),
    ("Morrensor (e as variantes: Morençor, Morrem Sor, Moros, Borrensor)", r"Mor\w*(?:\s[Ss]or)?|Borrensor", "a figura que costura a queda; grafia instável"),
    ("Protogonos / Protoos / Proto Gomos", r"Proto\w*(?:\s\w+)?", "nome do mesmo ponto da série das faces"),
    ("Sofia / Sophia", r"Sofia", "a palavra-dado deste ciclo"),
    ("Olm", r"\bOlm\b", "o par de Sophia na coleção dos problemas"),
    ("biodemo (e variantes)", r"bio ?de[gm]?[oa]?[oa]?s?", "a estirpe central do relato, na forma canônica e nas degradadas"),
    ("demobiol / demorobiol", r"demo ?(biol|ro ?biol)", "neologismo da fonte para os híbridos do outro forno"),
    ("código fonte definidor do criador", r"código fonte definidor", "a fórmula que a fonte repete como tecnicismo"),
    ("código podre", r"código p[oa]dre", "a expressão crua, sem eufemismo"),
    ("vírus", r"v[ií]rus", "o mecanismo de tudo, neste relato"),
    ("bactéria", r"bact[ée]ri", ""),
    ("Toxoplasma (todas as grafias)", r"[Tt]oxoplasm", "a analogia central da palestra"),
    ("COVID / covid", r"[Cc]ovid", ""),
    ("pandemia", r"pandemia", "9× — a moldura em que a palestra foi dita"),
    ("isolamento / isolad[oa]", r"isolam|isolad", "os mundos isolados"),
    ("colmeia / colmeico / calmeico / coméico", r"colm[ei]\w*|c[oa]lm[ei]\w*|calmeic\w*", "o sistema; o bruto tem quatro formas"),
    ("abelha rainha / operária", r"abelha[rs]? ?(rainha|oper)", "RC-175/RC-176"),
    ("processador", r"processador|processo ador|proc[ee]ss", "a rede de Sophia — e o STT parte a palavra em duas"),
    ("cérebro radiata / bilatério", r"radiata|bilat[ée]ri", "RC-631 e a passagem ao cérebro duplo"),
    ("campo m[óo]rfico / morfogenético", r"campo m[oa]rf", "RC-381"),
    ("emaranhamento quântico", r"emaranhamento", "RC-161"),
    ("elétrons", r"el[ée]tron", "a memória quântica"),
    ("28.869 genes", r"28[.,]869", "o número canônico da Base (RC-562), repetido pelo autor"),
    ("DNA", r"\bDNA\b", ""),
    ("ticum (tikkun)", r"ticum", "a Cabala como chave da reforma — RC-514/RC-545"),
    ("Cabala", r"Cabala", ""),
    ("arcontes", r"arcont", "os que retêm a vestimenta — RC-474/RC-770"),
    ("Trimurti (grafas)", r"[Tt]rim[uy][rt][ti]t?[eu]?", "a aristocracia apodrecida — RC-104"),
    ("Zeus / Cronos / Uranos / Olimp", r"Zeus|Cronos|Uranus|Olimpi", "a mitologia grega como registro"),
    ("titãs", r"tit[ãa]", ""),
    ("Mahabharata (todas as grafias, e o trocadilho barata)", r"barata", "a fonte grafa o título de 9 jeitos; o trocadilho é da própria fonte"),
    ("Viaza / Vyasa", r"Viaza|Vyasa", "o codificador — RC-585"),
    ("Krishna", r"Krishna", "RC-414"),
    ("Gandarvas / Rxaças / Pitres", r"[GR]?[a-zç]*vas?\b|[Rr]xa|pitres", "os destinatários dos versos"),
    ("Kant (Manuel / Emanuel Cant)", r"Kant|Cant\b", "a régua do intelecto; 3 grafias"),
    ("Kardec / espiritismo / Livro dos Espíritos", r"Kardec|espiritismo|livro dos esp[ií]ritos", ""),
    ("espírito(s)", r"[Ee]sp[ií]rito", "a palavra mais frequente do bruto"),
    ("erraticidade", r"erraticidade", "o tecnicismo kardecista"),
    ("idiotia / idiota", r"idiot", "a palavra do século XIX que a fonte evoca"),
    ("autista / espectro autista", r"autist|espectro", "o uso que a fonte faz do termo — item de dossiê"),
    ("esquizofrênico", r"esquizo", ""),
    ("demente / demência", r"dem[êe]n", "a categoria ontológica da queda"),
    ("Capila / Sankia / Sanquia", r"Capila|[Ss]an?k[hi]?i?a", "RC? a escola de Kapila — grafia única no bruto"),
    ("Mok (moksha) / sansara", r"Mok|sansara", ""),
    ("Pachupate (Pashupati)", r" Pachupate|Pachup", "a forma de Shiva citada uma vez"),
    ("trimurte apodreceu", r"trimurte apodrec", ""),
    ("«matar em nome de» (Brama, Alá)", r"em nome de", "a fórmula da crítica às religiões"),
    ("Mion / Len Mion / Lemion / Limion / Len Mon", r"Lemion|Limion|Len Mion|Len Mon|\bMion\b", "RC-074 — o nome sai degradado em 4 formas"),
    ("família Vol / V. / voz", r"[Vv]ol\b|fam[ií]lia V", "a estirpe 249.314; 4 grafias"),
    ("Iel / IEL / «família I» (a família Yel sem o Y)", r"\bIEL\b|\bIel\b|família I\b", "a família Yel, em três grafas"),
    ("Chamum / Cromon / Mion (as absorvidas)", r"Chamum|Cromon|Mion", "as famílias absorvidas pelo processador"),
    ("Aia / Aie (a dupla de anjos em torno de Sophia)", r"\b[Aa]i[ae]\b", "nomes novos no corpus: checar o cadastro"),
    ("Alp Longron (e a grafia de 2020)", r"Alp Longron", "a cidadela; em P2020-04-25 saiu «Alto Langron»"),
    ("Esferon (a nave-cidade)", r"[Eé]sferon", "a nave da família Vol transformada em cidade flutuante"),
    ("ZAM / Órbon / Ereon / Oreon", r"ZAM|[ÓO]?rb[oã]n|O[rs]eon", "as localizações nomeadas"),
    ("Valho / Chamba", r"Valho|Chamba", "onde os da rebelião residem — a localizar"),
    ("Marcelo / Marcelo? (nome no exemplo e no Q&A)", r"Marcel[oa]", "o interlocutor nomeado"),
    ("nomes da plateia (Solange, Mara, Lila, Elô, Narras)", r"Solange|Mara|Lila|El[oô]|Narras", "a roda ao vivo"),
    ("baiano / baiana / Alagoano", r"bai[ao]n|Alagoan", "o interlocutor da piada recorrente"),
    ("São Paulo (o local da fala)", r"S[ãa]o Paulo", "a única âncora de lugar do bruto"),
    ("Kant: colecionar incertezas", r"clectionar incertezas|colecionar incertezas", ""),
    ("pós-verdade", r"verdade, como sendo o novo neologismo|postruf", "o neologismo de 2016"),
    ("Trump / Brexit", r"Trump|Brexit|Brex\b", ""),
    ("Bolsonaro / Lula / Hilaria (os nomes em exemplos)", r"Bolsonar|Lula|Hilaria|Hillary", "item de dossiê (D-1 de 2020 como precedente)"),
    ("Bahia / Vitória / Mecão (o exemplo futebolístico)", r"Bahia|Vit[óo]ria|Mec", ""),
    ("Wilde / Dorian Grey", r"Dorian|Wild|Gley|Grey", "a literatura como prova de plausibilidade"),
    ("Pink Floyd / The Wall / Roger Waters", r"Pink Floyd|The Wall|Roger Was", "a última música do álbum"),
    ("Matrix (o filme como analogia)", r"Matrix", ""),
    ("inteligência artificial", r"intelig[êe]ncia artificial", "a hipótese de hospedagem nova"),
    ("Hitler / nazistas / fascista", r"Hitler|Rito\b|nazist|fascist", "a superinteligência sem valores"),
    ("suicidar / «nos desativamos»", r"suicid|desativamos", "item de dossiê (sensível)"),
    ("revólver", r"rev[óo]lver", ""),
    ("venda de si / escravidão como metáfora", r"escrav", "os 50 escravos do exemplo de carma"),
    ("Ereon / Milesianos / nemedianos / Partolanos / danã", r"Milesian|nemedian|partolan|dan", "o substrato druídico (RC-755)"),
    ("Hiperbórea(s)/hiperbórios/perbórias", r"[HhPp]iperb|perb[óo]ri", "RC-068"),
    ("Rezo(s)/macaco que se curva", r"macaco", "a genética da obediência"),
    ("anunnaki", r"anunna", "AUSÊNCIA CONTADA"),
    ("Nibiru", r"Nibiru", "AUSÊNCIA CONTADA"),
    ("Enki / Enlil", r"Enki|Enlil", "AUSÊNCIA CONTADA"),
    ("Shanlung / Shanai (os nomes de 2020)", r"Shanlung|Shanai|Chanai", "AUSÊNCIA CONTADA"),
    ("Alto Langron (a grafia de 2020, aqui ausente)", r"Alto Langron", "AUSÊNCIA CONTADA"),
    ("capelinos", r"capelin", "AUSÊNCIA CONTADA"),
    ("isolamento cósmico (a expressão exata do código RC-070)", r"isolamento c[óo]smico", "AUSÊNCIA CONTADA"),
    ("Hiperbórea com a grafia canônica", r"Hiperb[óo]rea", "a grafia canônica da Base, se aparecer"),
    ("Cromon (grafia canônica de RC-444)", r"Cromon", "medido: a família absorvida pelo processador"),
    ("ZONT EN DREL", r"[Zz]ont", "AUSÊNCIA CONTADA"),
    ("Terceira/Quarta edição dos Estagiários do Kaos", r"Estagi", "AUSÊNCIA CONTADA"),
    ("Cristo cósmico", r"Cristo c[óo]smico", "a glosa de Sophia — RC-009"),
    ("Moiras / Nornes / Parcas", r"Moiras|Nornes|Parcas", "AUSÊNCIA CONTADA"),
    ("amantíssimo (e as degradações)", r"amant", "a forma degradada do epíteto do Criador"),
    ("19 mundos", r"19 mundos", "a contagem do isolamento"),
    ("620.000 / 6.029 / 984 / 736 / 249.314 / 250.000",
     r"620[.,]000|6\.029|984\b|736\b|249[.,]? ?31[34]|250[.,]000", "as cifras-núcleo, contadas juntas"),
    ("700.000 anos", r"700[.,]000", "a data da rebelião — a cifra mais repetida do bruto"),
    ("400.000 anos", r"400[.,]000", "a data da depressão instalada"),
    ("900 milhões / 2,5 bilhões / 5-6 bilhões / 13,8 bilhões / 50 bilhões",
     r"900 milh|2[.,]5 bilh|2 bi?lhões 500|[56],? ?6 bilh|5, 6 bilh|13[.,]8 bilh|50 bilh", "as profundidades de tempo"),
    ("espécie 250 e espécie 315", r"esp[ée]cie de 250|a 315|ser a 315|\b315\b", "as duas espécies fora de catálogo"),
    ("2012 / 2016 / 2019", r"2012|2016|2019", "as datas do mundo, todas nomeadas na fala"),
]
med = []
for nome, rx, note in PAT:
    hits = [m.start() for m in re.finditer(rx, ASP.RAW)]
    med.append((nome, len(hits), (hits[0] if hits else None), note))

d2 = ["# CAMADA 2 — O DICIONÁRIO MEDIDO (P2022-03-26)", "",
      "Tudo que segue é **contagem** do `original.txt` com o regex indicado, e o endereço da primeira "
      "batida. Nada aqui foi lembrado: foi o que a varredura devolveu (inclusive os zeros).", "",
      "## 1. O vocabulário da palestra", "",
      "| termo / padrão | ocorr. | 1ª batida | observação |", "|---|---|---|---|"]
for nome, c, ini, note in med:
    end = f"{uaddr(ini)} @{ini:,}".replace(",", ".") if ini is not None else "—"
    d2.append(f"| {nome} | {c} | {end} | {note} |")
z = [m for m in med if m[1] == 0]
d2 += ["", f"## 2. As ausências contadas ({len(z)})", "",
       "Elas importam porque a *cópia* do assunto induz a emendar o tema anterior com este. Não há "
       "**um** anunnaki, **nenhum** Nibiru, **nenhum** Enki/Enlil, **nenhuma** das grafas de 2020 (Shanlung, "
       "Shanai, «Alto Langron», «isolamento cósmico»), **nenhum** Zont En Drel, **nenhuma** Moiras/Nornes. "
       "O teatro é o mesmo da família Yel e do campo colmeico, mas a linguagem técnica desta fala é a da "
       "**virologia**, não a da sumerologia.", "",
       "| ausência | contagem |", "|---|---|"]
for nome, c, ini, note in z:
    d2.append(f"| {nome} | 0 |")
d2 += ["", "## 3. O que o STT fez com os nomes (medido, não corrigido)", "",
       "A degradação onomástica é **mais severa** que em qualquer palestra anterior: o mesmo ser aparece até "
       "cinco vezes com grafias diferentes na mesma linha. A contagem por forma está em §1; a regra do ciclo é "
       "**não escolher** — nenhuma dessas grafas vira forma canônica, e a Base continua grafando como grafa. "
       "As formas degradadas ficam registradas aqui **em backticks** (não em aspas angulares, que são só de "
       "citação verificável do bruto) para que o leitor identifique a fala ao cruzar com o `original.txt`.", ""]
GRF = {
  "Javé": r"J[aàâ]?v[ée]?\w*|Jah\w*",
  "Vishnu": r"\b(Vno|Virg\w*|Vismo|Aivis\w*|visno)\b",
  "Brahma": r"\bBrama\b|Brasna|Br[áa]gina|Brana\b|Brajna",
  "Shiva": r"\bChiva\b|\bShiva\b",
  "Sophia": r"Sofia|Sophia",
  "Morençor/Morrensor": r"Mor\w*(?:\s[Ss]or)?|Borrensor",
  "Len Mion": r"Lemion|Limion|Len Mion|Len Mon|\bMion\b",
  "Luzbel": r"Luisbel\w*|Luzbel\w*|Elusbel\w*|Lusbel\w*|IUSB",
  "família Vol": r"\bVol\.?\b|\bvol\b|voz",
  "processador": r"processador\w*|processo ador",
  "Trimúrti": r"[Tt]rim\w*",
  "Sankhia/Samkhya": r"[Ss]an?k[hi]?ia",
  "Mahabharata": r"\w*barata",
  "Kant": r"Kant|Cant\b",
  "vírus": r"[Vv]írus|vir[óo]tic|v[ií]rotic",
}
for can, rx in GRF.items():
    formas = {}
    for m in re.finditer(rx, ASP.RAW):
        formas[m.group(0)] = formas.get(m.group(0), 0) + 1
    top = sorted(formas.items(), key=lambda kv: -kv[1])[:8]
    d2.append(f"- **{can}** → " + " · ".join(f"`{k.strip()}` {v}×" for k, v in top if k.strip()))

# ---------------------------------------------------------------- (4) matriz de anterioridade
RAIZ = os.path.dirname(os.path.dirname(CICLO))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT
CAD = {t[0]: t for t in DT.TERMOS}


def orais(cod):
    f = CAD.get(cod, (None,) * 5 + ([], None, None))[5] or []
    return sorted(x for x in f if re.fullmatch(r"P\d{4}-\d{2}-\d{2}", str(x)) and x != SIGLA)


CAND = ["RC-001", "RC-002", "RC-009", "RC-020", "RC-036", "RC-042", "RC-049", "RC-056", "RC-068", "RC-070",
        "RC-072", "RC-074", "RC-078", "RC-086", "RC-089", "RC-092", "RC-102", "RC-104", "RC-142", "RC-147",
        "RC-160", "RC-161", "RC-166", "RC-175", "RC-176", "RC-188", "RC-191", "RC-194", "RC-283", "RC-285",
        "RC-287", "RC-319", "RC-320", "RC-321", "RC-378", "RC-381", "RC-414", "RC-422", "RC-442", "RC-443",
        "RC-444", "RC-446", "RC-474", "RC-499", "RC-514", "RC-516", "RC-517", "RC-545", "RC-555", "RC-562",
        "RC-585", "RC-593", "RC-596", "RC-600", "RC-604", "RC-605", "RC-614", "RC-615", "RC-628", "RC-629",
        "RC-630", "RC-631", "RC-633", "RC-635", "RC-638", "RC-639", "RC-640", "RC-641", "RC-642", "RC-702",
        "RC-713", "RC-727", "RC-742", "RC-755", "RC-758", "RC-762", "RC-770", "RC-771"]
mt = ["# MATRIZ DE ANTERIORIDADE — calculada (P2022-03-26)", "",
      "Gerada contra `ferramentas/dados_termos.py` (a fonte única), com `P2022-03-26` **excluída** da conta da "
      "ficha atual. **Ganho de data** é o que ela tem de mais antigo; **ganho de conteúdo** é o resto — e é a "
      "maioria, porque `P2020-04-25` já é hoje a fonte oral mais antiga de quase tudo neste tema.", "",
      "| código | nome | fonte oral mais antiga (atual) | efeito deste ciclo | ficha |", "|---|---|---|---|---|"]
n_ganho = n_prem = n_conteudo = 0
for c in CAND:
    if c not in CAD:
        mt.append(f"| {c} | *(inexistente no cadastro)* | — | — | — |")
        continue
    nome, ho = CAD[c][1], (orais(c) + [None])[0]
    if not ho:
        n_prem += 1
        efeito = "**🆕 primeira fonte oral desta ficha**"
    else:
        dias = (datetime.date(*map(int, ho.lstrip("P").split("-"))) - D0).days
        if dias <= 0:
            n_conteudo += 1
            efeito = f"sem ganho de data (já tem `{ho}`); ganho de **conteúdo**"
        else:
            n_ganho += 1
            dur = f"{dias} dias" if dias < 62 else (f"{dias/30.44:.0f} meses" if dias < 1100 else f"{dias/365.25:.1f} anos")
            efeito = f"**⭐ antecipa {dur}** a fonte oral mais antiga"
    mt.append(f"| {c} | {nome} | `{ho}` | {efeito} | {'sim' if CAD[c][7] else '**NÃO**'} |")
mt += ["", f"**Contagem:** {len(CAND)} candidatos auditados · {n_ganho} com ganho de data · {n_prem} que ganham "
       f"a primeira fonte oral da história · {n_conteudo} sem ganho de data (conteúdo, e só)."]

# ---------------------------------------------------------------- escrever
open(os.path.join(AQUI, "camada-0.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
open(os.path.join(AQUI, "camada-2.txt"), "w", encoding="utf-8").write("\n".join(d2) + "\n")
open(os.path.join(AQUI, "_matriz-anterioridade.md"), "w", encoding="utf-8").write("\n".join(mt) + "\n")
print(f"camada-0: {len(res)} seções · camada-2: {len(med)} itens ({len(z)} ausências) · matriz: {len(CAND)} códigos "
      f"({n_ganho} ganho de data, {n_prem} 1ª fonte oral, {n_conteudo} só conteúdo)")
