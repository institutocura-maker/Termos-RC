#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO PACOTE DE AMPLIAÇÕES — P2023-12-03 (A Rebelião de Lúcifer ainda por ser Finalizada).

Fonte da decisão: `../DECISAO-DO-CURADOR.md` (devolutiva de 29/08/2026, D-1…D-14, 100% aprovado).

Princípio da casa, endurecido ciclo a ciclo: **nenhuma aspa é digitada à mão**. Cada citação vem de uma âncora
frouxa resolvida pelo caça-âncoras `_aspas_P2023-12-03.py`, que devolve o trecho byte a byte do `original.txt` e
**aborta se a âncora não bater exatamente uma vez**. A lista de códigos e as âncoras-mestre são **lidas do
dossiê aprovado** (`_gerar_textos_e_dossie_P2023-12-03.py`, variável `LIG`) por `ast` — o que entra na Base é
exatamente o que o Curador leu, não uma releitura.

Travas impostas por este script (o despacho não é confiança, é código):

* **D-1** — o argumento antropológico sobre «identidade de gênero» e a frase sobre a humanidade ter que mudar
  **não transitam**: nenhum span que contenha esse léxico entra em ficha. Nas fichas RC-036/RC-056/RC-093 fica
  só o dado técnico (assexuação, casulos, cérebro radiata).
* **D-2** — a frase-geral sobre mulheres é retida; só transita a aspa da **salvação pelo DNA de Maria**.
* **D-3** — nenhum vocabulário político (líderes, direita/esquerda, nações em juízo político) entra em ficha.
* **D-4** — nenhuma máscara do STT (`*****`) transita: fica na apostila, onde a moldura é lida.
* **D-12** — nenhum nome de pessoa real (plateia, médiuns, autoras) transita para ficha, **inclusive** em RC-071,
  onde entra só a cadeia Elã → Enoque, sem adjetivação confirmatória.
* **D-13** — o calendário 1989/2049-2052 não entra em RC-200; entra em RC-344 e RC-003.
* anterioridade é **calculada** do cadastro, nunca lembrada.

Se qualquer trava morder, o bloco é **retido e listado** no BLOCO 5 (nada é silenciado). Se uma âncora não
bater, o arquivo **não é escrito**.
"""
import os, re, sys, ast, glob, datetime, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
SIGLA = "P2023-12-03"
TITULO_FONTE = "A Rebelião de Lúcifer ainda por ser Finalizada"
DATA_FALA = datetime.date(2023, 12, 3)
DATA_APLIC = "2026-08-29"
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
DOSSIE_GERADOR = os.path.join(AQUI, f"_gerar_textos_e_dossie_{SIGLA}.py")
SAIDA = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_for_spec(spec) if hasattr(importlib.util, "module_for_spec") else importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                                                    # noqa: E402
CAD = {t[0]: t for t in DT.TERMOS}

# ─────────────────────────── os vínculos aprovados, lidos do dossiê ───────────────────────────
_gs = open(DOSSIE_GERADOR, encoding="utf-8").read()
_i = _gs.index("LIG = [")
_j = _gs.index("\n]", _i)
LIG = ast.literal_eval(_gs[_i + len("LIG = "):_j + 2])
LIG = [x for x in LIG if x[0] != "RC-464"] + [("RC-464", "a lenda dos Turatas de Dana, que ali chegaram das cidades", None)]
print(f"vínculos do dossiê: {len(LIG)}")

# ─────────────────────────── travas (léxicos medidos, não adjetivados) ───────────────────────────
MASCARA = re.compile(r"\*{3,}")
GENERO_ARG = re.compile(r"identidade de g|identidades|genero na historia|mudar loucamente|palavras humanas para", re.I)
POLITICA = re.compile(r"direita e esquerda|mediocridade|lideres|monstra|Brasil, Estados Unidos|campanha|voto", re.I)
PESSOAS = re.compile(r"Chico Xavier|Divaldo|Valdemar|Edgar Ar|Jane Miranda|João Altair|César|Márcia|\bJan\b|Horácio"
                     r"|Emanuel|Rog[ée]rio|Vasconcel|Mo[çc]a\b|Shimon|Gandari|Krishna\??\s*$", re.I)
# Para o RÓTULO que se injeta na ficha vale outra régua: `Jan Val Ellam` é designação canônica de termo na Base
# (está no cadastro e em 390 fichas), não nome de plateia introduzido por esta palestra. Sem esta distinção, o
# rótulo de `RC-071` virava «RC-071 (forma curta…)» e a ficha perdia o próprio nome do termo — troca de instrumento
# por instrumento. Para o CONTEÚDO das aspas a trava continua sendo `PESSOAS`, inteira.
PESSOAS_LABEL = re.compile(r"Chico Xavier|Divaldo|Valdemar|Edgar Ar|Jane Miranda|João Altair|Márcia|Horácio"
                           r"|Emanuel|Rog[ée]rio|Vasconcel|Shimon|Gandari", re.I)
CALENDARIO = re.compile(r"2049|2050|2051|2052|1989|julho de 9|passaporte", re.I)
VETO_CALENDARIO_EM = {"RC-200"}
VETO_GENERO_EM_GRUPO = True                                  # D-1: fichas que nomeiam grupos humanos
GRUPO_RX = re.compile(r"humanos|homens|mulheres|povos|ind[íi]genas|crian[çc]as|pacientes|doen[çc]a|transtorno", re.I)


def trava(txt, cod, fim_veto=None):
    """Devolve o motivo da retenção, ou None se o span pode transitar para a ficha `cod`."""
    if MASCARA.search(txt):
        return "D-4 · máscara do STT no span"
    if GENERO_ARG.search(txt):
        return "D-1 · argumento antropológico de gênero"
    if POLITICA.search(txt):
        return "D-3 · vocabulário político"
    if PESSOAS.search(txt):
        return "D-12 · nome de pessoa real no span"
    if cod in VETO_CALENDARIO_EM and CALENDARIO.search(txt):
        return "D-13 · calendário profético vedado nesta ficha"
    if VETO_GENERO_EM_GRUPO and GENERO_ARG.search(txt) and GRUPO_RX.search(CAD.get(cod, ["", ""])[1]):
        return "D-1 · gênero em ficha que nomeia grupo humano"
    if fim_veto and re.search(fim_veto, txt):
        return "veto nominal do despacho"
    return None


# ─────────────────────────── substituições nomeadas pelo despacho ───────────────────────────
# D-12: em RC-007 a frase da fonte cita «Edgar Armon»; troca-se pelo span sem nome próprio.
# D-2:  em RC-189 o span da pergunta de Eva carrega máscara; entra a aspa da salvação pelo DNA de Maria.
# D-12: em RC-071 entra só a cadeia Elã → Enoque (a âncora-mestre do dossiê citava o canal).
SUB = {
 "RC-071": ("nasce como Enoque", None),
}

# ─────────────────────────── o que cada ficha ganha de específico ───────────────────────────
# (código, título do bloco, (âncora-início, âncora-fim|None), nota editorial)
NOTA = {
 "RC-007": ("O ÚNICO TOQUE DE CAPELA NA PALESTRA", ("a respeito dos exilados", "impecáveis, maravilhosos"),
  "A palestra menciona Capela **uma vez**, e a menção vem dentro de uma frase em que a fonte nomeia uma pessoa "
  "cuja obra ela leu — o nome fica na apostila (D-12) e aqui entra só o fragmento verificável do juízo. É registro "
  "de leitura, não de doutrina: nenhuma relação nova com `RC-006` (exilium) é aberta por esta entrada."),
 "RC-189": ("SÓ A ASPA APROVADA TRANSITA", ("foi o DNAzinho de Maria em Jesus", None),
  "D-2: a âncora-mestre do dossiê nesta ficha («Depois que Eva disse…») atravessa uma máscara do STT e por isso foi "
  "**retida** (BLOCO 5) — o que se aproveita aqui é apenas a aspa da salvação pelo DNA de Maria, que a fonte põe na "
  "boca de Jesus. Na apostila as duas frases do quiasma ficam juntas, como ordem expressa; aqui não."),
 "RC-001": ("O CARGO, NÃO A EXISTÊNCIA", ("Isso nao e Deus, e so o criador", None),
  "D-5: a cláusula de leitura vem **anexada à aspa**, não solta — a frase não nega Deus; desloca o título de Deus "
  "do criador da obra. É tese oral de 03/12/2023, não doutrina da Base."),
 "RC-002": ("O QUE RESTOU E NÃO MORREU", ("o que restou da rebeliao de Lucifer e nao morreu", None),
  "A definição que a fonte dá do resíduo da rebelião não é culpa, é **inconformismo**: «ideia viva de que algo de "
  "errado existe na gestão da vida e que é preciso ser superada». A ficha deixa de poder ser lida como narrativa de "
  "queda moral e passa a ter a formulação datada do que a fonte chama de face propositiva."),
 "RC-003": ("O PROCEDIMENTO, MUNDO POR MUNDO", ("aquele mundo era reintegrado", None),
  "D-9/D-13: a reintegração ganha mecanismo e contagem — a cada mundo saneado, os doentes remanescentes eram "
  "redistribuídos e o planeta voltava à convivência. Com isso o método deixa de ser inferido das 19 fichas de "
  "isolamento e passa a ter texto: há 100.000 anos restavam **dois** mundos; há 200-300.000, **oito ou nove**."),
 "RC-005": ("A POSSE QUE NÃO HOUVE", ("Sabe aquela cerimonia de posse nunca houve", None),
  "D-6: a segunda vinda é lida pela fonte como **cerimônia de posse retida**, não como atraso. «posse» é metáfora "
  "de investidura no glossário, nunca rito histórico, e nenhuma relação de fundamento é aberta por esta entrada."),
 "RC-009": ("O SUZERANO COM TESTEIRAS FLOUXAS", ("Sofia e o representante da Trimurte nesse universo biologico", None),
  "A ficha passa a ter a definição de cargo: representante da Trimúrti neste universo biológico, com os seres de lá "
  "vindo «sem o menor respeito» por ele. É o par simétrico do que P2022-03-26 registrara como contaminação: aqui, a "
  "impotência administrativa."),
 "RC-018": ("A NAVE, O CENSO E A VISITA DATADA", ("Sofia esteve aqui nos anos 2018, 19", None),
  "D-10: materialização autorizada. A fonte entrega o que o cadastro não tinha: a grafia em quatro formas, o censo "
  "da nave (~1.000 → 938 a bordo, uns 600 e poucos na Terra) e **um evento datado** — a presença de Sofia ali em "
  "2018-19. Nada é harmonizado com os 936/984 de ciclos anteriores: divergência selada (D-9)."),
 "RC-020": ("OS ANJOS QUE NÃO SOUBERAM LER", ("esses anjos sao meio assim, sao robos", None),
  "A doutrina dos anjos decaídos recebe a variante da fonte: os clones-robôs da Trimúrti examinaram o problema e "
  "**não fizeram a leitura que Luzbel fez**. O item ancora a taxonomia declarada no início da própria palestra "
  "(rebelião = subtema da doutrina dos anjos decaídos)."),
 "RC-034": ("DOIS UNIVERSOS DE UMA VEZ", ("desde que essa criacao teve inicio com a producao de dois universos", None),
  "A cosmogonia ganha a cifra interna da fonte (13,8 bilhões de anos) **com a ressalva dela mesma**: «o universo "
  "vizinho está colapsando já, não é que vai colapsar»."),
 "RC-035": ("O ARGUMENTO ANATÔMICO", ("O nosso e bilaterio", None),
  "D-7: a vantagem humana é dita em termos de neuroanatomia comparada — duas câmaras cerebrais e emoção contra um "
  "cérebro radiata sem elas. É o fundamento físico que a Base não tinha para a tese da obsolescência."),
 "RC-036": ("ASSEXUAÇÃO E CASULO, SÓ O DADO TÉCNICO", ("criados em casulos, em naves", None),
  "D-1: entra o dado (seres sem sexo, produzidos em casulos, nenhum nascido em planeta) e **não** o argumento "
  "sobre identidades. A frase da fonte sobre a Terra ter «dois» gêneros fica na apostila, com moldura."),
 "RC-040": ("O QUE TEM DE FICAR ORGANIZADO", ("padroes arquetipos do codigo fonte definidor do criador", None),
  "D-10: materialização autorizada pela robustez da fórmula — a fonte dá ao CFD o que as obras só descreviam: a "
  "condição de que os padrões arquétipos sejam organizados para que o criador tenha paz. A ficha existe a partir de "
  "agora; o vínculo de malha já estava no cadastro."),
 "RC-042": ("O CRIADOR QUE NÃO PÔDE FAZER AVATAR", ("Brahma nao podia criar avatar porque ele e um ser desalmado", None),
  "D-5: a assimetria da Trimúrti (um sem avatares porque a mente não sustenta mais de um ser) entra como tese datada "
  "com a cláusula de leitura da D-5 — trata de *cargo e capacidade*, não de inexistência."),
 "RC-046": ("DANÃ E OS QUE VEIO DELE", ("a lenda dos Turatas de Dana, que ali chegaram das cidades", None),
  "A fonte ancora o povo de Danã em Hiperbórea e data a chegada à Irlanda em 13.000 anos. A onomástica do bruto é "
  "instável (5 grafas): o nome entra **como dito**, com [REVISAR], e a Base não unifica."),
 "RC-049": ("O QUE OS DEMOS FIZERAM PARA TER SEXO", ("criaram um tipo de condicao para eles de ter orgaos sexuais", None),
  "O demo é caracterizado aqui por uma **aquisição** (órgãos sexuais por imitação dos mamíferos do universo "
  "vizinho), com a teogonia hesiódica como testemunha nomeada pela fonte — não como prova."),
 "RC-056": ("CADA FAMÍLIA, UM PROBLEMA", ("na cabeca de Sofia surgiram 250.000 problemas", None),
  "D-1: a etiologia das espécies em sua forma mais nua — cada estirpe foi criada para resolver um problema técnico "
  "que o suzerano não sabia resolver. Nenhuma cifra arredondada: a fonte diz «250.000» e emenda «São 249.400, não "
  "sei quantos»."),
 "RC-064": ("O TERCEIRO PADRÃO DE GENÉTICA DEMO", ("genetica demo chamada Fenvan", None),
  "A ficha ganha a posição do fenvan na série: não é espécie nova, é **padrão de atualização** da genética demo, o "
  "terceiro depois dos clones robotizados e do demo. A grafia do bruto varia e fica [REVISAR]."),
 "RC-068": ("AS CIDADES E A DISPERSÃO", ("a turma do hiperborio foi entao construindo", None),
  "D-8: Hiperbórea deixa de ser só o mundo do norte e passa a ter função no relato: das cidades híbridas saem as "
  "quatro correntes (Irlanda, Escócia, Sibéria, Alasca) que carregam a memória da rebelião como lenda."),
 "RC-070": ("A QUARENTENA DOS 19", ("distribuiram nesses 19 mundos situados em varios", None),
  "O isolamento ganha a peça que faltava: **a Terra é um dos 19 mundos** e o último a ser reintegrado. A fonte "
  "nega que haja punição — foi decisão de contenção sanitária tomada por Sofia «e não há negociação»."),
 "RC-071": ("A CADEIA ELÃ → ENOQUE", ("esse Valan, que foi uma das figuras que o meu espirito", None),
  "D-12: entra **só** a cadeia de encarnações que a fonte atribui ao espírito que a anima (Valan/Elã → Enoque), "
  "sem adjetivação confirmatória e sem as frases em que a fonte se coloca como «a última opção» dos três — essas "
  "ficam na transcrição, com moldura, e não aqui."),
 "RC-072": ("A RECUSA COMO PIVÔ", ("Jesus se recusou a cumprir o papel de Messias violento", None),
  "D-6: a recusa deixa de ser only-agonia e passa a ter consequência administrativa narrada: a investidura de "
  "Malkut é revogada pelos arcontes. A aspa vem com endereço e sem relação nova de fundamento."),
 "RC-074": ("QUEM FOI CAPTURADO PRIMEIRO", ("foi quando Lemion Sata invadiu la as nossas defesas", None),
  "A fonte dá a gênese do contato com o próprio canal (a «arapuca amorosa» e a captura) e a cadeia onomástica "
  "Lemon → Satané → Satan → Set. Fica [REVISAR] a identidade do «Set» do fim da linha, que o STT também grafa como "
  "«7»."),
 "RC-078": ("O COMANDANTE QUE NÃO QUERIA COMANDAR", ("o coitado do Lucifer, que nunca pretendeu comandar", None),
  "A ficha ganha o contrapeso explícito: o comando foi consequência de ser o único que sabia explicar o problema, "
  "num contexto em que os seres eram «100% pacíficos» e não tinham algoritmo de raiva."),
 "RC-081": ("O AVATAR DE QUEM?", ("Rockmar em arabe e Sofia em grego", None),
  "A fonte nomeia um avatar (Rockmar/Rockma/Rockban, 3 grafas no bruto) criado por Vno para atuar em duas línguas "
  "e culturas. [REVISAR] — o nome não é unificável a partir do TXT e nenhuma hipótese etimológica entra na ficha."),
 "RC-086": ("O SORRISO PEDIDO NO FIM", ("possa sorrir nos termos em que Pandora", None),
  "A Pandora da fonte fecha o ciclo com um sorriso *emprestado*: o desejo explícito é que Luzbel sorria «nos termos "
  "em que Pandora um dia sorriu quando se viu». O bruto grafa `julgo` e corta ali; remissão a B020, sem fusão."),
 "RC-089": ("O ÚNICO ARQUIVO VIVO DA REBELIÃO", ("passou a ser a coisa mais importante da rebeliao", None),
  "Materializada no ciclo anterior, esta ficha recebe a peça de fechamento: o processador da Vol sobreviveu porque "
  "**era o mais moderno**, atualizado até o fim, e acabou apropriando a memória dos cabeças da rebelião — é isso "
  "que, na fala, mantém a rebelião viva («a questão era proteger o processador»)."),
 "RC-092": ("A FUNÇÃO DECLARADA DO LIVRO", ("por isso eu escrevi o livro Quarto L", None),
  "A fonte diz para que serve o Quarto Logos: suprir a deficiência educacional de Sofia, produzindo padrões de "
  "conduta. É a mais externa das auto-atribuições do acervo sobre uma obra catalogada (B016) e por isso entra com "
  "endereço e aspas, não como resumo."),
 "RC-093": ("POR QUE ELE NÃO SENTE", ("no cerebro radiata dele nao funciona", None),
  "D-1/D-7: entra o dado anatômico (cérebro radiata, sem emoção) e não o argumento sobre gêneros. A peça da "
  "prótese («criar um órgãosinho para ele») pertence a `RC-632`, que já a comporta."),
 "RC-104": ("TRÊS FORMAS DE REPLICAR, UMA ESTÉRIL", ("Os tres Eles da Trimur", None),
  "A Trimúrti deixa de ser só panteão e ganha ato técnico: criou três formas de replicação da vida biológica, uma "
  "das quais nunca funcionou — a mesma tríade dos fornos, agora com autor."),
 "RC-109": ("O POVO SEM MECANISMO DE POSSE", ("nao tem sensacao de ser dono de nada", None),
  "A ficha recebe a prioridade de presença (já estavam na Terra quando os Anunnaki chegaram) e a razão pela qual "
  "a Terra foi declarada deles por outros: os vol não tinham mecanismo psíquico de posse."),
 "RC-142": ("O PROCESSADOR VALIDOU", ("deu guarida informacao de Lucifer", None),
  "O contágio de Lúcio passa a ter órgão e verbo: o processador da família Iel considerou a informação procedente "
  "e a família inteira foi contaminada instantaneamente. É a formulação mais compacta do que a Base chama de "
  "validação do que se pensa."),
 "RC-160": ("O FINALIZADOR QUE NÃO FOI ESCOLHIDO", ("a entropia ou a forca tamasica que a gente diz", None),
  "A entropia aparece como **ato de fechamento delegado**: como nada foi finalizado por projeto, a força tamásica "
  "finaliza. A frase do Q&A («Tudo. A entropia destrói tudo.») é a versão seca, e entra ao lado."),
 "RC-161": ("O QUE HÁ PARA RECOLHER", ("em eletrons e antieletrons sujos", None),
  "As atividades mentais doentias do criador viram elétrons e antielétrons sujos na matrix — a ficha ganha o "
  "substrato que faltava entre a queda e a operação de recolha descrita em `RC-378`."),
 "RC-167": ("IMPROVISADO NA HORA DA QUEDA", ("esse foi improvisado na hora da queda", None),
  "A categoria de «obra indevida» recebe a sentença que a define sem metáfora: planejado × improvisado, e "
  "**nenhum dos dois finalizado**. É a chave de leitura do título desta palestra."),
 "RC-176": ("A COLMEIA COM NOME DE FAMÍLIA", ("igual a formiga que vive la embaixo", None),
  "O modelo colmeico ganha o vínculo biográfico: a nave é para o biodemo o que o formigueiro é para a formiga — e "
  "por isso nenhum deles se sente preso a planeta. Remissão a B044, sem fusão."),
 "RC-186": ("OS NOMES QUE O AUTOR ENCONTROU", ("sao os nomes que eu encontrei para poder chamar esses seres", None),
  "A fonte **declara a invenção** dos termos da tríade (biodemo · demobio · demobiol) e troca a prevalência de um "
  "para o outro dentro do mesmo fôlego. Registro com [REVISAR]: a ficha não resolve a contradição, registra a "
  "autoria do neologismo."),
 "RC-188": ("O WHATSAPP DOS BIODAMOS", ("WhatsApp de rede", None),
  "A rede psíquica das famílias é dita pela fonte em termos contemporâneos e com função técnica (registrar, "
  "devolver orientação, coesar). A analogia é da fala de 2023 e fica datada como tal."),
 "RC-200": ("CUSTÓDIA, NÃO CALENDÁRIO", ("nos existimos para guardar essas informacoes", None),
  "D-13: entra a **função** (cérebros e processadores como custódia temporária da informação até a finalização) e "
  "**não** a janela de anos que a fonte fixou em outro ponto da fala, nominalmente vetada nesta ficha. A "
  "escatologia datada fica na apostila (U0016) e em `RC-003`/`RC-344`, onde o despacho a colocou."),
 "RC-241": ("OS QUE APARECIAM E DESAPARECIAM", ("seres dos portais que invadiam a terra", None),
  "Os seres dos portais entram na narrativa da memória: é essa a história que Tot estudava «cento e poucos mil anos "
  "atrás». Remissão a B021, sem fusão."),
 "RC-263": ("NÃO HÁ ÁRVORE", ("Nao tem nada de arvore da vida", None),
  "A fonte corrige o nome, não o objeto: o que os cabalistas chamaram de árvore da vida são as dez sefirot lidas "
  "como **identidades** — e é assim que a ficha passa a registrar a releitura oral, com selo de 03/12/2023."),
 "RC-280": ("O QUE ELE EXPLICOU DEPOIS", ("ele explicou como Jesus ressuscitado", None),
  "A ressurreição é lida como resposta à inação: Sofia explica, como ressuscitado, por que não assume. Entrada com "
  "aspa e endereço; nenhuma relação nova com RC-005 além da que o cadastro já tinha."),
 "RC-295": ("O QUE SE PERDEU COM OS PORTAIS", ("nos termos em que la atras se vinha", None),
  "A travessia do universo antimaterial para o material era possível «nos termos em que lá atrás se vinha através "
  "dos portais» — a fonte usa isso como prova de que os deuses de lá não podem simplesmente mudar-se para cá."),
 "RC-301": ("A OUTRA REBELIÃO, ENTRE OS QUE TINHAM SEXO", ("como a rebeliao de Prometeu", None),
  "Prometeu deixa de ser paralelo poético: na fala, é a **mesma estrutura de evento** ocorrida na outra estirpe "
  "(demobiol). Fica como tipologia das rebeliões, não como alegoria moral."),
 "RC-344": ("O QUE PAROU A TRANSIÇÃO", ("fez parar o processo de exidio dos espiritos", None),
  "D-13: a transição planetária ganha causa narrada para a suspensão (a confusão de Lemion na espiritualidade) e "
  "janela datada pela fonte (marco em julho de 1989; saída até 2050/51/52). O relatório registra que o prazo já "
  "estaria vencido na data de hoje, sem harmonização corretiva."),
 "RC-375": ("O QUE OS DRUIDAS RECEBERAM", ("dois colegios arquidruidicos para estudar o conhecimento", None),
  "D-8: os colégios entram como o *método pedido*, não como instituição étnica: os Túatha pediram que os humanos "
  "criassem um jeito de estudar o que recebiam. A etnicidade fica na transcrição, não na ficha."),
 "RC-378": ("DEVOLVER AO UNIVERSO", ("devolver pela sua pulsacao para o resto do universo", None),
  "A operação da rebelião dos elétrons recebe o segundo tempo, que faltava: recolher, reprocessar, **devolver pela "
  "pulsação**. A fonte diz explicitamente quem são os processadores — e a frase vai com a ressalva dela mesma."),
 "RC-381": ("ONDE O VÍRUS FOI VALIDADO", ("esse processador funciona como campo morfico", None),
  "A ressonância mórfica é nomeada **como o que o processador é**, e é por isso que a informação de Lúcifer teve "
  "guarida. Esta ficha passa a ter o mecanismo do contágio em vez de só a sua metáfora."),
 "RC-387": ("O CORPO MENTAL ESFACELADO", ("corpo mental dele foi esfac", None),
  "A fragmentação do poder mental recebe o verbo da fonte (esfacelado em pequenas coisas **nos dois universos**) e "
  "o complemento operativo: a limpeza é feita por processadores, não por perdão."),
 "RC-395": ("O QUE SOFIA NÃO IMPEDIU", ("a vida em Marte foi destruida devido a isso", None),
  "A fonte dá a Marte um evento próprio (destruição da vida por briga dos seres de lá, há 300 milhões de anos) e o "
  "usa como prova da omissão estrutural de Sofia. Cifra datada, sem confronto com outras idades da Base."),
 "RC-414": ("A DEMÊNCIA ATRIBUÍDA A UM AVATAR", ("Krishna tem o problema da demencia demo", None),
  "A crítica de U0007 entra com as duas metades, porque separá-las produziria calúnia ou apologia: a fonte nega "
  "demência a Tot («só não tem a racionalidade do padrão que nós temos») e a atribui a Krishna. Nenhuma das duas é "
  "aspa de juízo: é releitura datada de um texto épico."),
 "RC-424": ("A ESCOLHA COMO PLANO DE SUBSTITUIÇÃO", ("Escolheu Adao, sete, Enos", None),
  "A genealogia de Gênesis 5 é lida pela fonte como **sequência intencional** para viabilizar um messias, com os "
  "nomes degradados pelo STT (`sete`, `Cainâ`, `Lalahelu`, `Jaré`): entram como dito, com [REVISAR] em cada um."),
 "RC-426": ("POR QUE ELE PRECISAVA DE UM HUMANO", ("Brahma nao podia criar avatar porque ele e um ser desalmado", None),
  "O «não tenho isto» ganha explicação técnica na fala de 2023: sem avatar, a saída foi assinar-se em Adão — a "
  "assinatura quântica como procedimento de substituição, com o paralelo que a fonte faz com os avatares na Índia."),
 "RC-432": ("O QUE NÃO EXISTIA ANTES DO CONFLITO", ("Ninguem tinha tinha algoritmo de raiva", None),
  "A agressividade canalizada passa a ter antes/depois narrado: os algoritmos de raiva, tristeza e agressão "
  "**surgiram na confusão**. Entrada datada, sem diagnóstico humano, sem clínica."),
 "RC-442": ("A FAMÍLIA QUE VIU E FOI CONTAMINADA", ("A familia Iel, que foi uma familia criada para", None),
  "A Iel deixa de ser lista de membros e passa a ter função no relato: criada para resolver um problema específico, "
  "foi dela o primeiro membro a perceber o defeito na criação — e dela o primeiro processador a dar guarida."),
 "RC-446": ("CADA FAMÍLIA, UM PROCESSADOR", ("cada um deles era ligado ao processador da familia", None),
  "Os processadores familiares ganham definição operacional completa: campo mórfico que registra a atividade de "
  "todos, devolve orientação e coesa. A fonte diz também que um biodemo **não pode viver** sem ele — a dependência "
  "é lei da espécie, não costume."),
 "RC-453": ("O QUE OS ANJOS FIZERAM NOS OUTROS MUNDOS", ("Os anjos de Sofia trouidaram todo mundo", None),
  "A hoste recebe o ato que a fala lhe atribui nos mundos do conflito — e o contraste que sustenta o título: na "
  "Terra, ninguém veio. O verbo degradado pelo STT (`trouidaram`) é preservado como veio, com [REVISAR]."),
 "RC-464": ("A ROTA ATÉ A IRLANDA", ("a lenda dos Turatas de Dana, que ali chegaram das cidades", None),
  "O elo Danu ← Hiperbórea ← cidades híbridas é dito pela fonte com data (13.000 anos) e com a afirmação de que "
  "nenhuma das quatro etnias irlandesas era humana. Registro com [REVISAR] nas grafas; nada unificado."),
 "RC-474": ("OS DONOS DE LOKA", ("esses sao chamados arcontes", None),
  "A definição de arconte pela fonte é **patrimonial**: cada um é dono de uma loka e a mente dele define o que há "
  "nela. E o despacho da posse que não houve passa por eles — são eles que não querem que Sofia assuma."),
 "RC-479": ("A QUEM O VAZIO BENEFICIA", ("figuras como Bel, como Lemion, como Tod", None),
  "A fonte nomeia os candidatos ao preenchimento do vazio de poder — e a lista inclui Bel, Lemion e Tot, o que dá "
  "a esta ficha um papel no quadro que antes era só gnóstico. Sem relação nova de fundamento."),
 "RC-487": ("A OUTRA REBELIÃO, CONTRA ENLIL", ("fizeram a rebeliao contra Enlio", None),
  "A rebelião anunnaki contra Enlil (16-17.000 anos, grafia do bruto) entra como **cronologia própria**, não como "
  "o mesmo evento: a fonte diz que não consegue ligar as três rebeliões e que o vão é fato."),
 "RC-489": ("A ELEIÇÃO PELA GENÉTICA", ("o DNA de Enoque era muito interessante", None),
  "D-9: a raptura de Enoque ganha motivo segundo a fonte (o DNA interesse de Javé) e suas idades coincidem com o "
  "que a ficha já registra — **convergência datada**, que o ciclo destaca como confirmação e não como revisão."),
 "RC-496": ("AS CINCO FAMÍLIAS, O MESMO NÚMERO", ("as familias Vol, Iel, Nion, Cromon, Xum", None),
  "A fonte lista cinco famílias vindas à Terra e acrescenta, na mesma frase, que «esses nomes também não tem "
  "importância». O paralelo com os cinco Archeons de Ereon é **observação de catálogo**, não aresta: fica anotado "
  "aqui e em nenhum outro lugar."),
 "RC-506": ("O ADÃO QUE É UMA SEFIRÁ LIDA", ("Adao Cadimão ancestral", None),
  "O Adão Cadimão aparece no rol que Enoque teria feito diante dos anjos — registro com endereço, sem relação nova "
  "com `RC-211`/`RC-424` além das existentes."),
 "RC-508": ("A DIGNIDADE COMO CONDIÇÃO DE VALIDADE", ("Ou humanos sao respeitados na sua dignidade existencial", None),
  "A fonte enuncia um protocolo: o que é arrancado sem dignidade **não vale**, como órgão rejeitado. A fórmula é "
  "dita contra «os que detêm o poder»; entra como ética da fala, sem trânsito para fichas que nomeiem grupos."),
 "RC-516": ("O QUE AS ENTRELINHAS DIZEM", ("dois tipos de seres da terra", None),
  "A hibridagem é lida pela fonte como o que a Bíblia diz nas entrelinhas (filhos de homens × filhos de deuses). "
  "A ficha recebe a leitura com endereço, e a autodeclaração dela: explicar a gênese exigiria várias palestras "
  "preliminares — que a fonte diz nunca ter tido coragem de dar."),
 "RC-517": ("O PROBLEMA ERA DE ALGORITMO E PROTOCOLO", ("problema a de algoritmo e de protocolo", None),
  "A resposta a U0034 é o fecho do ciclo anterior aberto: o primeiro questionamento de Lúcifer é apresentado como "
  "diagnóstico de protocolo, e a fonte remata reduzindo-o a ciência. A ficha ganha a primeira formulação explícita "
  "disso no acervo oral."),
 "RC-525": ("O QUE FOI COLOCADO NO DNA HUMANO", ("mexeram no DNA humano para colocar inteligencia e obediencia", None),
  "A semente da racionalidade recebe a autoria anunnaki segundo a fonte, com o par que a incomoda (inteligência **e "
  "obediência**). Entrada datada, sem harmonizar com as formulações das obras."),
 "RC-530": ("SOFIA COMO CRIATURA DE UM ACORDO", ("ele foi quem criou Sofia a partir de um acordo com esses dois", None),
  "Pistis Sophia ganha, na leitura da fonte, origem contratual: criado por Vno de acordo com Javé e Shiva. Fica com "
  "aspa e selo; nenhuma relação nova com RC-009."),
 "RC-541": ("A VIA QUE NÃO É REBELIÃO NEM OBEDIÊNCIA", ("A rebeliao de Lucifer agora para ter continuidade seria propositiva", None),
  "A terceira via recebe a formulação da fonte: não adianta mais revolução violenta; a rebelião que continua é "
  "**propositiva**. A palavra é da fala, não da Base, e o contexto (satyagraha) vai ao lado."),
 "RC-546": ("O BEM SEM FALANGE", ("Nao existe nenhuma falange que represente o bem", None),
  "O primado da consciência criativa ganha a negação simétrica: nenhuma hoste representa o bem; ele existe como "
  "produção humana. É a frase mais citável da palestra e por isso vai com endereço e sem paráfrase."),
 "RC-559": ("A REGRA ÚNICA E O QUE KRISHNA QUERIA TROCAR", ("o que sai de um ser volta para ele pelo tipo de karma", None),
  "A teia quântica é apresentada como única regra e a crítica ao Bagavaguita como tentativa de substituí-la. "
  "Atenção: o bruto diz «se você matar sem ordem, isso não gera karma para você», o que contradiz a leitura corrente da "
  "fonte externa — **não se emenda**; fica como dito, com [REVISAR]."),
 "RC-575": ("A TRIMÚRTI EM LIQUIDAÇÃO", ("a Trimurte tem que deixar de existir", None),
  "A ancoragem do conglomerado trimurtiano é descrita pela fonte como desmonte deliberado (Brahma em coma, Vno "
  "desfeito, Chiva destruindo os próprios avatares). Entrada com aspa, sem relação de fundamento nova."),
 "RC-579": ("NORÉIA, FILHA DE EVA E LILIF", ("uma filha de Eva e Lilif", None),
  "A fonte acrescenta filiação a Noréia (filha de Eva e «Lilif») dentro da série dos que a fala chama de bandidos-heróis. "
  "Fica [REVISAR] a identidade do pai/mãe; nenhuma relação nova com RC-489/RC-189."),
 "RC-602": ("DUAS BANDAS E UMA BLINDAGEM", ("duas bandas e uma blindagem", None),
  "A cosmologia da blindagem ganha a frase-síntese da fonte e a sua consequência: o corpo mental esfacelado ficou "
  "**dentro** da blindagem, e é daí que sai a operação de recolha."),
 "RC-604": ("A APOSTA SOBRE O MESMO HUMANO", ("Cada um coloca forma de poder no DNA de Enoque", None),
  "O fatiamento de consciência recebe um episódio: os três disputam Enoque e resolvem inoculando cada um sua "
  "fórmula de poder no DNA. Entrada datada; o desfecho («por isso o coitado do Enoque morreu») fica na apostila."),
 "RC-613": ("UMA FREQUÊNCIA POUCO DIFERENTE", ("vai vibrar um pouquinho diferente", None),
  "A fonte explica a ocultação do quartel-general como deslocamento de frequência **adjacente**, e não subjacente, "
  "recusando-se a explicar a diferença — recusa que a ficha registra como limite, não como lacuna a preencher."),
 "RC-619": ("O QUE É BOM QUE FIQUE DESATIVADO", ("Se coisas daqui forem despertas e vierem a habitar o nosso consciente", None),
  "O genoma da liberdade recebe o avesso da promessa: despertar os genes dormentes é o que faria «a gente virar "
  "bicho». Fica com a ressalva da própria fonte (o paralelo com Freud é analogia, não teoria)."),
 "RC-625": ("O CORPO QUE PRECISA SER RECONSTRUÍDO", ("o eu do criador com o seu corpo manasico", None),
  "A condição final descrita pela fonte: o corpo manásico despedaçado reconstruído, e a erraticidade limpa antes do "
  "fim do estoque de hidrogênio. Entrada datada com as duas cláusulas, sem ordenação delas."),
 "RC-631": ("O CÉREBRO QUE FALTA", ("no cerebro radiata dele nao funciona", None),
  "D-7: a incompatibilidade anatômica vira conteúdo de ficha — um cérebro radiata contra o bilatério humano, e "
  "desta vez **com a consequência** dita pela fonte (sem emoção, sem sorriso, sem atualização possível)."),
 "RC-632": ("A PRÓTESE EMENDANDO O QUE NÃO FOI PROJETADO", ("Para ele sentir emocao, a gente tem que criar um organoinho para ele", None),
  "D-7: os organoides ganham a finalidade explícita que P2024-05-04 não dava: são para que Sofia **sinta**. A "
  "frase contém «a gente tem que criar»: a operação é cooperada, não decretada — e é isso que a ficha registra."),
 "RC-638": ("A MASSA CRÍTICA DO CADÁVER", ("essa operacao tem que estar numa massa critica", None),
  "A ressurreição do criador deixa de ser só prometida e passa a ter condição física: massa crítica de processamento "
  "para recriar corpo e reinstalar o eu. A fonte recusa qualquer cronograma: «espero nunca ter opinião formada»."),
 "RC-658": ("A TEIA E O QUE A LIGA FORA", ("a teia de Orlo", None),
  "A pergunta final do Q&A nomeia uma teia («de Orlo», [REVISAR]) como terceiro item que a entropia destruiria, ao "
  "lado do quartel e do processador. Fica a aspa, fica a dúvida de grafa, e nada é fundido com Alt'Lam Gron."),
 "RC-672": ("OS 366, PELA BOCA DA FONTE", ("os 366 livros de Enoque", None),
  "D-9: a cifra dos manuscritos reaparece igual e com a mesma degradação («sobraram pedaços de dois»). É a "
  "segunda fonte oral independente dizendo o mesmo número — convergência registrada como confirmação."),
 "RC-673": ("AS PRISÕES QUE NÃO ERAM DELE", ("percebe prisoes que nao eram dele", None),
  "A intercessão ganha cenário: Enoque encontra prisões de anunnakis desobedientes e o nome que a fonte diz estar "
  "na lista («Satanail»), com a confusão que o nome produziu com Satã. Sem relação nova com `RC-074`."),
 "RC-682": ("A DÉCIMA QUE CONTESTAM", ("a 10ma sefirado, quem e", None),
  "D-6: Malkuth é dito como a sefirá que **já existe** e cuja titularidade é disputada porque o universo vizinho "
  "vai acabar. Entrada com aspa e selo; nenhuma relação de fundamento com RC-009."),
 "RC-702": ("A FAIXA FEITA PARA SUMIR", ("criaram faixa de realidade simultanea para todo o quartel general", None),
  "A camuflagem ganha técnica: faixas de realidade simultânea podem ser **criadas**, e a fonte chama isso de "
  "metaverso, acrescentando que «um dia a gente vai entender melhor». O termo corrente fica sem relação com o "
  "assunto contemporâneo, por D-1/D-3."),
 "RC-705": ("O NOME DA RESISTÊNCIA ESCOLHIDA", ("usando a expressao sans do satagrar", None),
  "A fonte invoca o termo sânscrito (degradado pelo STT: «sâns do satagrar») e o define à sua moda: resistência "
  "pacífica e amorosa em torno da verdade que se crê real. Fica com a grafa [REVISAR] e com a recusa dela própria "
  "à via violenta."),
 "RC-711": ("AS TREVAS QUE TAMBÉM TÊM PODER", ("movimento de consciencia das chamadas trevas espirituais", None),
  "O universo de egrégoras emocionais recebe a cláusula de risco da fonte: o movimento das trevas tem poder de "
  "perturbar os dois universos, e por isso se lhe concedem «momentos lúcidos»."),
 "RC-713": ("CONVENCER UMA MÁQUINA A SER PADRINHO", ("varias unioes de DNA foram feitas para convencer o processador", None),
  "A taumaturgia genético-química aparece aqui como **recurso administrativo**: uniões de DNA foram feitas para que "
  "o processador acatasse as famílias que haviam perdido os seus. É a origem, na fala, do vínculo que depois se "
  "torna linhagem."),
 "RC-718": ("O ÚNICO CAPÍTULO ABERTO", ("corresponde so o capitulo 11", None),
  "A fonte data a exceção: dos profetizados em Apocalipse, **só o capítulo 11** não está predefinido; o resto está. "
  "Entram as duas aspas (a exceção e a regra «Do que tá ali, tá ali e vai ser») — e nada de cálculo de prazo (D-13)."),
 "RC-725": ("NO MEIO DA EXPLOSÃO", ("a gente ainda ta no meio da explosao", None),
  "A imagem do presente cosmológico da fonte (criação como fogo de artifício, ainda em estouro) entra ao lado da "
  "ilha de negentropia: é o que justifica, na fala, que a recolha ainda seja necessária."),
 "RC-727": ("O INCONFORMISMO HERDADO", ("mantendo o inconformismo luciferiano", None),
  "D-2: entra **só** a linhagem do inconformismo (associada a Pandora e Eva) e a aspa da salvação pelo DNA de "
  "Maria; a frase-geral sobre mulheres não transita para cá, nem para RC-189 isolada, e o quiasma fica íntegro na "
  "apostila, como despacho manda."),
 "RC-736": ("A MONARQUIA SEM EXÉRCITO", ("tipo uma rainha da Inglaterra", None),
  "D-6/D-7: a aristocracia olimpiana é descrita pela fonte pelo que **não** pode: a soberania de Sofia é nominal, "
  "contestada pelos arcontes porque querem emigrar para este universo. Uma única frase sustenta a ficha inteira."),
 "RC-742": ("A QUATRO FALÊNCIAS", ("A somatoria dos estresses extremos", None),
  "D-5: a falência dos deuses ganha o mecanismo que a fonte prevê — soma de estresses extremos, falência das "
  "religiões, do psiquismo, das utopias e do que os humanos sonharam, produzindo os choques de realidade. Com a "
  "cláusula: não é tese ateia, é tese sobre cargo."),
 "RC-745": ("O PEDIDO POR TRÁS DOS COLÉGIOS", ("criem um metodo para voces estudarem", None),
  "D-8: os colegiados ganham origem narrada: os não-humanos pediram que os humanos **inventassem um método**, com a "
  "promessa de aprenderem com o nível de compreensão alcançado. A constatação de que a Arca seria esse método fica "
  "no relatório — e é vedada como auto-legitimação na ficha."),
 "RC-755": ("O CONTRATO DO MÉTODO", ("nos queremos dar para voces os nossos conhecimentos", None),
  "D-8: a Escola da Decifração recebe da fonte a sua **justificativa mítica**: discernir o erro e receber a verdade "
  "foi pedido expresso, e o isomorfismo com a ditagem enoquiíta é afirmado pela própria fala."),
 "RC-757": ("O QUE O TRADIÇÃO FEZ NO LUGAR DA TRIMÚRTI", ("na India com a tradicao comaranda", None),
  "A fonte usa a tradição indiana (grafia degradada «comaranda» [REVISAR]) como o precedente que obrigou Javé a "
  "escolher um humano. Fica como afirmação datada da fala, sem equivalência doutrinária."),
 "RC-760": ("O NÚCLEO MENTAL E SUAS ATIVIDADES DOENTIAS", ("com o nosso cita sagrado", None),
  "A ficha recebe a fórmula operativa que a Base não tinha em voz: o «cita» (chitta [REVISAR]) como núcleo mental "
  "formado por vṛtti, e a tarefa de reprocessá-las. As quatro grafas do bruto ficam como vieram."),
 "RC-762": ("O QUE É NIRODA, DITO PELA FONTE", ("Criando um processador aqui dentro que faca o niroda", None),
  "A fonte define niroda (grafada «niroda») como a atitude do processador de recolher as vṛtti doentias, "
  "reprocessar e devolver — e ela mesma marca a palavra como difícil. Escala tripla mantida; nenhuma tradução nova."),
 "RC-770": ("O QUE OS ARCONTES QUEREM", ("esses arcontes querem vir para ca", None),
  "A hipóstase ganha motivo concreto na fala: a obstrução à posse existe porque o universo deles está acabando. "
  "Entrada com aspa; nada de relação nova com RC-474 além da já registrada."),
 "RC-771": ("OS DOIS FORNOS QUE FUNCIONARAM", ("esse forno de replicacao chamado Aamon", None),
  "D-9: os fornos replicadores recebem nome, gestor e uma **idade divergente** (932 milhões aqui; 936 em P2022 e "
  "984 em P2020). As três entram datadas; a Base não escolhe uma."),
}
print(f"notas editoriais curadas: {len(NOTA)}")

# ───────────────────────────────── resolve tudo ─────────────────────────────────
def aspa(ini, fim=None, teto=300):
    a, b, txt = ASP.locate(ini, fim, "exata")
    if len(txt) > teto:
        cut = txt.rfind(" ", 0, teto)
        txt = txt[:cut if cut > 120 else teto].rstrip(" ,;:.")
    return txt, a


def efeito(cod):
    t = CAD[cod]
    fs = sorted([x for x in t[5] if re.match(r"P\d{4}-\d\d-\d\d", x) and x != SIGLA])
    if not fs:
        return (f"**⭐ ganho de anterioridade**: nenhuma fonte oral estava registrada nesta ficha; "
                f"`{SIGLA}` passa a ser a mais antiga.")
    ant = fs[0]
    if ant > SIGLA:
        # meses contados como nº absoluto de mês (todas as siglas têm o prefixo `P`, hence [6:8]);
        # usar [5:7] lia "-1" e devolvia contagem negativa — defeito de medição, não da fonte.
        meses = (int(ant[1:5]) * 12 + int(ant[6:8])) - (int(SIGLA[1:5]) * 12 + int(SIGLA[6:8]))
        return (f"**⭐ antecipa em {meses} meses** a fonte oral mais antiga (`{ant}` → `{SIGLA}`); o efeito desta "
                f"entrada é de **data**, além de conteúdo.")
    return (f"⚠️ **sem ganho de anterioridade**: a ficha já tem fonte oral **mais antiga ou igual** (`{ant}`); a "
            f"entrada desta fonte é de **conteúdo**, não de data.")


# D-13: a janela datada entra **aqui** (RC-344 e RC-003) e é **vedada** em RC-200 — ordem expressa do despacho.
DATA_D13 = {
 "RC-344": ("O MARCO E A JANELA, COMO A FONTE OS DISSE",
   ("o ano 2050, ou e 50", "52 vai existir de tudo por aqui"),
   "D-13: a fonte finca o marco em `1989` («Em julho de 9, alguém na espiritualidade fincou um marco») e a janela "
   "`2050, ou é 50 ou é 51, 52`. Entram **como ditos**, com a grafa degradada (`áas`, `foi foi fincado`) e sem "
   "cálculo de prazo: o `RELATORIO-DE-CICLO.md` é que registra que a janela **já estaria vencida** na data desta "
   "aplicação, sem harmonização corretiva e sem recálculo da data original."),
 "RC-003": ("ATÉ QUANDO, SEGUNDO A FONTE", ("Mas ate o ano 2049", None),
   "D-13: a reintegração world-by-world recebe da fonte um horizonte declarado — «até o ano 2049, 50, 51, 52, isso "
   "aqui vai continuar a acontecer» — que é **o que a fala diz**, não uma previsão da Base. O valor para a ficha é o "
   "procedimento (redistribuir os doentes e reintegrar o mundo), não o calendário; a janela viaja com endereço."),
}

ROTULOS_AJUSTADOS = []      # D-12: o NOME do termo às vezes é que carrega o nome civil


def rotulo_master(cod):
    """Rótulo do bullet-mestre: o nome do termo em caixa alta, **sem** nome civil de pessoa.

    `RC-071` chama-se `Jan Val Ellam (Rogério de Almeida Freitas)` no cadastro — é pré-existente na Base e não
    é nossa decisão mexer nele. Mas o rótulo que este ciclo escreve **dentro** da ficha pode escolher a forma
    curta, e é isso que D-12 pede: nenhum nome de pessoa sai desta esteira.
    """
    nome = CAD[cod][1]
    if PESSOAS_LABEL.search(nome):
        limpo = re.sub(r"\s*\([^)]*\)", "", nome).strip()
        rot = limpo if limpo and not PESSOAS_LABEL.search(limpo) else f"{cod} (forma curta do cadastro, sem nome civil)"
        ROTULOS_AJUSTADOS.append((cod, nome, rot))
        return rot
    return nome


AM, retidos, falhas = {}, [], []
for cod, ini, fim in LIG:
    ini, fim = SUB.get(cod, (ini, fim))
    try:
        txt, pos = aspa(ini, fim)
    except SystemExit as e:
        falhas.append(f"{cod}: {e}")
        continue
    mot = trava(txt, cod)
    if mot:
        retidos.append((cod, "âncora-mestre", mot, txt[:70]))
        continue
    AM.setdefault(cod, []).append((f"{rotulo_master(cod).upper()} NA FALA DE {DATA_FALA:%d/%m/%Y}", [(txt, pos)],
                                   "**Selo temporal (D-9/D-10):** fórmula oral de 03/12/2023, transcrita como dita "
                                   "— grafia degradada do STT preservada, nenhuma cifra arredondada, nenhuma "
                                   "divergência harmonizada. · " + efeito(cod)))

for cod, (tit, (ini, fim), nota) in NOTA.items():
    try:
        txt, pos = aspa(ini, fim, teto=420)
    except SystemExit as e:
        falhas.append(f"{cod} (nota): {e}")
        continue
    mot = trava(txt, cod, fim_veto=("Rog[ée]rio" if cod != "RC-071" else None))
    if mot:
        retidos.append((cod, tit, mot, txt[:70]))
        continue
    AM.setdefault(cod, []).append((tit, [(txt, pos)], nota))

for cod, (tit, (ini, fim), nota) in DATA_D13.items():
    txt, pos = aspa(ini, fim, teto=520)
    mot = trava(txt, cod)
    if mot:
        retidos.append((cod, tit, "D-13/trava: " + mot, txt[:60]))
        continue
    AM.setdefault(cod, []).append((tit, [(txt, pos)], nota))

if falhas:
    print(f"{len(falhas)} âncora(s) inválida(s) — nada escrito:")
    for f in falhas:
        print("   ✗", f[:140])
    sys.exit(3)

# ───────────────────────────────── BLOCOS 2-5 ─────────────────────────────────
SEM_ARQ = sorted(c for c in AM if not glob.glob(os.path.join(RAIZ, "termos", f"{c}-*.md")))
MATERIALIZADAS = {"RC-018", "RC-040"}
BLOCO2 = (["### BLOCO 2 — códigos sem arquivo em `termos/` antes deste ciclo (vínculo de malha + o que a fonte disse)\n",
           "",
           "Nestes códigos **não há `## Ampliação` para inserir**: o vínculo `P2023-12-03` vive em "
           "`ferramentas/dados_termos.py` e o conteúdo fica aqui, à espera de materialização. "
           "Dois deles (RC-018 e RC-040) **são materializados** por este ciclo por ordem expressa do despacho "
           "(D-10); os demais permanecem `ficha=False`.\n", ""]
          + [f"- `{c}` — {CAD[c][1]}: {CAD[c][1] and 'ficha a ser criada' if c in MATERIALIZADAS else 'sem materialização autorizada'}"
             for c in SEM_ARQ] + [""])

BLOCO3 = (
 "### BLOCO 3 — SELO TEMPORAL, DIVERGÊNCIAS E CONVERGÊNCIAS (D-9, por ordem expressa do Curador)\n\n"
 "Nenhuma cifra foi arredondada, média ou reconciliada. O que diverge, diverge **datado**:\n\n"
 "- `932 milhões` de anos para o forno de Vígno (esta fala, U0004) × `936` (P2022-03-26) × `984` (P2020-04-25): "
 "três idades para o mesmo forno, todas com endereço, nenhuma preferida — a ficha `RC-771` carrega as três;\n"
 "- `250.000` famílias biodêmicas e, na frase seguinte, `249.400, não sei quantos` × `250 espécies` (2022): a "
 "grandeza mudou de unidade (famílias × espécies), e por isso **não se concilia**;\n"
 "- `938` a bordo da nave, precedido de `cerca de 900, quase 1000` × `936`/`900Q` (2022) × `13 membros` "
 "(cadastro, em `RC-491`): quatro magnitudes para a tripulação; a Base mantém as quatro;\n"
 "- rebeldes sobreviventes ditos **em autocorreção ao vivo**: `1300 e pouco, não, 1700 e pouco, perto de 2000` — "
 "os três valores entram, porque a correção é o dado;\n"
 "- `4.380.000 anos` para a soneca do eu de Javé, sem par na Base (as eras `RC-567`/`RC-569` operam em 25.920 e "
 "2.160 — escala diferente, não divergência a reconciliar);\n"
 "- `1947` dado pela fonte como o ano de *A Caminho da Luz* — a data é da fala; nenhuma ficha de obra é criada e "
 "nenhuma correção bibliográfica é feita por este ciclo;\n"
 "- **três convergências com destaque de confirmação (ordem expressa D-9)**: os `736` efetivos da família Vol "
 "(2020 · 2022 · **2023**, pela terceira vez, sem anotação); as idades de Enoque `67 + 300 + os 366` que já estão "
 "em `RC-489`/`RC-672`; e os `200 bilhões` de contaminados ditos de novo com o mesmo algarismo de 2022. São "
 "confirmações, não revisões — e a Base as registra como tal.")

BLOCO4 = (
 "### BLOCO 4 — cruzamentos, radar e metadados de enunciação (D-11, D-12, D-13)\n\n"
 "**Remissões a obras já catalogadas** (D-11: só obra existente; 0 obra nova):\n\n"
 "- a fonte nomeia a primeira trilogia — `B003`/`B025`/`B026` (*Reintegração Cósmica*, *Caminhos Espirituais*, "
 "*Carma e Compromisso*) — como o lugar onde a rebelião foi tratada por alto, e o diz para justificar o título: "
 "«nenhuma dessas duas trilogias Eu falei claramente que acabou»; remissão em `RC-002`, `RC-003`, `RC-078`;\n"
 "- a trilogia `B017`/`B018`/`B039` (*Terra Atlantis*) é citada como onde «o nome dessas naves» e das famílias "
 "está explicado; remissão em `RC-089`, `RC-109`, `RC-142`, `RC-442`;\n"
 "- `B016` (*O Quarto Logos*) é citado **pela função** que a fonte lhe dá — suprir a deficiência educacional de Sofia, na fórmula "
 "da nota de `RC-092`; remissão em `RC-092`, `RC-253`;\n"
 "- `B020` (*O Sorriso de Pandora*) é o intertexto do fecho («o próprio Elosbel possa sorrir nos termos em que "
 "Pandora um dia sorriu»); remissão em `RC-086`, `RC-727`;\n"
 "- `B044` (*A Divina Colmeia*) cobre o processador-família como campo mórfico; remissão em `RC-176`, `RC-446`, "
 "`RC-381`;\n"
 "- `B057`/`B058` cobrem a revolta do anjo decaído e o início da revolta capelina, que a fala de 2023 descreve "
 "por dentro (a validação do processador da família Iel); remissão em `RC-074`, `RC-078`, `RC-142`;\n"
 "- `B021` (*Tempos Difíceis no Olimpo*) é o quadro dos «seres dos portais» que Tot estudava; remissão em `RC-241`, "
 "`RC-295`.\n\n"
 "**Radar datado (0 obra criada, 0 linha de catálogo — D-11):** `Projeto Tal` é anunciado como livro futuro («se tempo de vida eu tiver, ainda vai sair um livro com esse nome»); a **palestra sobre a gênese da "
 "hibridagem** é anunciada como algo que a fonte nunca teve «coragem nem saco» de fazer e que exigiria várias "
 "preliminares; a explicação da diferença *subjacente/adjacente* e o **terceiro fator** que parou o expurgo são "
 "declarados retidos pela própria fonte. Os quatro ficam aqui, com data, e viram nada.\n\n"
 "**Metadados de enunciação (D-12):** plateia nomeada só para responder (Rogério, Jan, Márcia, Horácio, «T César», "
 "«João Altair»); dois selos internos de data na fala («nesse dia 3 de dezembro do ano 2023» e «nessa sala hoje, "
 "dia 3 de dezembro de 2023»); o intervalo declarado no meio (com o «nível três de desgosto»); três referências ao "
 "dia anterior, que fazem deste ciclo a palestra **anunciada** por `P2023-12-02`. Nada disso gera entidade, ficha "
 "ou relação: é o quadro em que a fala foi dita, e assim a apostila o transcreve.")

BLOCO5 = (["### BLOCO 5 — retidos por trava (nada é silenciado; nada destes entra em ficha)\n", ""]
          + [f"- `{c}` ({t}) → **{mot}** — span começava em «{q}…»".replace("«", "«").replace("»", "»")
             for c, t, mot, q in retidos] + [""])
if not retidos:
    BLOCO5 = ["### BLOCO 5 — retidos por trava\n", "",
              "**Nenhum span foi retido por trava de conteúdo**: as âncoras foram escritas já dentro do regime do "
              "despacho (sem máscaras, sem nomes de pessoas, sem léxico político ou de gênero), e o BLOCO 5 existe "
              "para que isso seja **verificável**, não suposto. As aspas das seções vetadas (D-1, D-2, D-3) continuam "
              "na transcrição integral da apostila, onde a moldura é lida junto."]

out = [f"# PACOTE DE AMPLIAÇÕES — {SIGLA} · {TITULO_FONTE}", "",
       f"Fonte: `original.txt` do ciclo ({DATA_FALA:%d/%m/%Y}, na sala, com selo interno na fala). Cada aspa é span "
       f"verificado pelo caça-âncoras `_aspas_{SIGLA}.py`; os códigos e as âncoras-mestre são **lidos do dossiê "
       f"aprovado** (`_gerar_textos_e_dossie_{SIGLA}.py`) por `ast`, para que não exista diferença entre o que o "
       f"Curador leu e o que foi injetado. As travas D-1 (léxico de gênero), D-2 (quiasma das mulheres), D-3 "
       f"(política), D-4 (máscaras), D-12 (pessoas nomeadas) e D-13 (calendário vedado em RC-200) são executadas "
       f"por este script, e não por promessa — e o BLOCO 5 lista o que foi retido.",
       "",
       "**Rótulos ajustados por D-12** (nome do termo no cadastro carrega nome civil de pessoa; o rótulo injetado "
       "na ficha usa a forma curta, e a Base não é tocada nesse ponto): " +
       ("; ".join(f"`{c}`: rótulo do cadastro `{a}` → rótulo injetado `{b}`" for c, a, b in ROTULOS_AJUSTADOS) if ROTULOS_AJUSTADOS else "nenhum"),
       "", "### BLOCO 1 — seções a inserir nas fichas", ""]
n_cit = 0
for cod in sorted(AM):
    out.append(f"### {cod}")
    vistos, emit = set(), 0
    todos = [t for _, sp, _ in AM[cod] for t, _ in sp]
    for tit, spans, nota in AM[cod]:
        partes = []
        for txt, pos in spans:
            if txt in vistos or any(txt != o and txt in o for o in todos):
                continue
            vistos.add(txt)
            partes.append(f"«{txt}» ({ASP.uaddr(pos)})")
            n_cit += 1
        if not partes:
            continue
        emit += 1
        out.append(f"- **[{SIGLA} · {tit}]** " + " ; ".join(partes) + f" — {nota}")
    if emit:
        out.append("")
out += BLOCO2 + [""] + [BLOCO3, "", BLOCO4, "", *BLOCO5, ""]
TEXTO = "\n".join(out)
open(SAIDA, "w", encoding="utf-8").write(TEXTO)
print(f"fichas no BLOCO 1: {sum(1 for l in out if re.match(r'^### RC-', l))} · citações: {n_cit}")
print(f"sem arquivo (BLOCO 2): {len(SEM_ARQ)} · retidos (BLOCO 5): {len(retidos)}")
print(f"_ampliacoes_{SIGLA}.txt escrito: {len(TEXTO):,} chars".replace(",", "."))
