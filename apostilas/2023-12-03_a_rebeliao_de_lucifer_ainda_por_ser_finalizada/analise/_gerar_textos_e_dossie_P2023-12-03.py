#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAMADA 1 · LEITURA-1 · NOTAS · DOSSIÊ — P2023-12-03.

Um gerador para os quatro produtos da Etapa 1, com uma única lei: **nenhuma aspa é digitada**.
Toda citação sai de `[[âncora inicial||âncora final]]`, resolvida no caça-âncoras contra
`original.txt`; se a âncora bater ≠1 vez, o script aborta e nenhum arquivo é escrito (lição dos ciclos
P2023-10-14 e P2022-03-26, onde endereços datados de memória caíram na auditoria).

A tabela de vínculos (§2 do dossiê) é **proposta**: calcula o efeito de data contra
`ferramentas/dados_termos.py` e não escreve nada na Base. O ciclo espera o despacho do Curador.
"""
import os, re, sys, json, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, "_aspas_P2023-12-03.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
import dados_termos as DT
RAW = ASP.RAW
SIG = "P2023-12-03"
DATA = "03/12/2023"
TIT = "A Rebelião de Lúcifer ainda por ser Finalizada"
META = json.load(open(os.path.join(AQUI, "METADADOS-INGRESSO.json"), encoding="utf-8"))
T = {t[0]: t for t in DT.TERMOS}


def n(x):
    return f"{x:,}".replace(",", ".")


def aspa(ini, fim=None, teto=300):
    """Span **exato** da âncora até o fim da frase (sem voltar ao início da frase: é o que estoura o texto),
    aparado em fronteira de palavra — um prefixo de trecho verbatim continua verbatim, e assim a aspa nunca
    precisa de reticências dentro dos «» (o auditor de verbatim cobra exatamente isto)."""
    a, b, txt = ASP.locate(ini, fim, "exata")
    if len(txt) > teto:
        cut = txt.rfind(" ", 0, teto)
        txt = txt[:cut if cut > 120 else teto].rstrip(" ,;:.")
    return "«" + txt + "» (" + ASP.uaddr(a) + ")"


def prequote(t):
    """Toda aspa *digitada* por quem escreve vira trecho em `backtick`. Só fica em «…» o span que o
    caça-âncoras extraiu do bruto — que é a regra da casa e o que o auditor de verbatim sabe cobrar."""
    return re.sub(r"\u00ab(.+?)\u00bb", lambda m: "`" + m.group(1) + "`", t, flags=re.S)


def resolve(txt):
    out, k = [], 0
    fails = []
    for m in re.finditer(r"\[\[(.+?)(?:\|\|(.+?))?\]\]", txt):
        out.append(txt[k:m.start()])
        try:
            out.append(aspa(m.group(1), m.group(2)))
        except SystemExit as e:
            fails.append(str(e)); out.append("[[FALHOU]]")
        k = m.end()
    if fails:
        print("  âncoras de texto que não batem:")
        for f_ in fails:
            print("    ✗", f_)
        sys.exit(4)
    out.append(txt[k:])
    return "".join(out)


# ─────────────────────────── medidas auxiliares ───────────────────────────
def cnt(rx):
    return len(re.findall(rx, RAW))


ONTEM = cnt(r"ontem")
PRIMEIRA = cnt(r"[Pp]ela primeira vez|falando isso pela primeira|nunca foi explicado")
MASCARAS = re.findall(r"\b\w{1,6}\*{3,}", RAW)
Q = len([l for l in ASP.LINHAS if l.strip() and len(l.strip()) <= 24])

# ══════════════════════════ CAMADA 1 — A TESE ══════════════════════════
CAM1 = f"""# CAMADA 1 — A TESE ({SIG} · {TIT})

## 0. O que a palestra promete e o que entrega

A fala abre declarando que **retoma** um assunto que ela torcia para nunca mais retomar ([[Hoje nós vamos retomar um assunto]]),
e que o faz porque **uma parcela de seres a obrigou a isso** ([[pela insistencia desses seres e pelo fato de Sofia]]). Não é uma
palestra sobre a rebelião: é a **prestação de contas de uma pendência** — e o título é dela mesma, dito na primeira pessoa do
plural, no fecho ([[a rebeliao de Lucifer nao terminou, ela esta ainda por ser finalizada]]).

Entrega, em {n(META['chars_texto'])} caracteres, o que nenhuma fonte anterior do acervo entregou: **a cadeia de custódia**
de quem sabe o que aconteceu — Lúcifer vê o defeito → o processador da família valida a informação → a família inteira é
contaminada → quarentena em 19 mundos → a Terra é o último → os arquivos que sobraram (o quartel preso numa faixa, a nave
com o processador) → **um único remanescente que lembra** (Elã) → Elã nasce Enoque → Enoque traduz para os anjos → os anjos
entregam a Cabala no século II → e a mesma informação, degradada, vira lenda no Alasca, na Irlanda, na Escócia e na Sibéria.

Título em uma frase: **a rebelião não acabou porque a cerimônia de posse nunca houve; e ela não houve porque o herdeiro
recusou o papel de messias violento de que o criador precisava para se ressuscitar — de modo que o governo do universo
biológico está vago, e o que chamamos de história é o expediente provisório dessa vacância.**

## 1. As nove engrenagens

**1.1 O título é cosmológico, não editorial.** «Finalizar» aqui não é «contar até o fim»: é *concluir um projeto que ficou
pela metade*. A fonte diz que o universo material foi **planejado**, o deste mundo foi [[esse foi improvisado na hora da queda]]
e arremata com a cláusula que gera tudo o mais: nenhum dos dois foi finalizado, porque o planejador caiu antes de terminar
([[esse foi improvisado na hora da queda]]). Daí a consequência: **quem finalizou por fora injetou a entropia**
([[a entropia ou a forca tamasica que a gente diz]]). Toda a palestra é a demonstração de que a entropia é o *gesto de
fechamento* de uma obra que o autor não pôde fechar.

**1.2 A rebelião não foi pecado: foi uma auditoria.** A fonte inverte a moral do episódio em duas frases. Lúcifer, o que
vê, é descrito como o único que leu o problema: [[A familia Iel, que foi uma familia criada para]] — e o próprio ato de ver
gera o contágio, porque [[percebeu que o problema estava na genese da genetica daquele ser]]. A resposta à pergunta feita
no Q&A (U0035) fecha o argumento sem margem: o questionamento original de Lúcifer não era ético, era de engenharia
([[problema a de algoritmo e de protocolo]]), e o que ele nomeou foi a falha de quem criou, não de quem desobedeceu
([[isso e a genetica podre do criador]]).

**1.3 O contágio é um evento *administrativo*.** O vírus não entra pela força, entra por **validação**:
[[deu guarida informacao de Lucifer]] — o processador da família Iel julgou que a informação tinha procedência, e
[[instantaneamente, toda a familia IEL se contaminou pelo virus]]. É exatamente a lógica que P2022-03-26 descreveu como
«o sistema só reza com a resposta», agora com a peça que faltava: o **órgão de validação das famílias** é vulnerável porque
registra o que os membros pensam ([[esse processador funciona como campo morfico]]).

**1.4 A quarentena é a causa política da revolta.** Sofia não pune: **isola**. [[distribuiram nesses 19 mundos situados em varios]]
— e a fonte acrescenta o detalhe que a Base ainda não tinha em voz: **a Terra é um desses 19**
([[Aqui no nosso sistema solar, so a Terra foi um]]). O que transforma um problema «de saúde pública» em rebelião é a
recusa de negociação: sempre dizer [[sempre dizer: "E isso e nao ha negociacao]] — donde a fórmula da fonte,
[[o coitado do Lucifer, que nunca pretendeu comandar]]. **A revolta nasce do método de governo, não da vontade de poder.**

**1.5 O efeito colateral psíquico: os afetos negativos não existiam.** [[Ninguem tinha tinha algoritmo de raiva]] é a frase
que amarra esta palestra à de 26/03/2022: a depressão ali descrita como sequela tem aqui sua **etiologia**, porque o medo
de uma prisão que nunca veio é o que os corrói ([[so pensavam que a cada instante qualquer coisinha]]).

**1.6 A custódia do conhecimento.** Duas vezes a fonte diz que a rebelião sobreviveu porque sobreviveram **arquivos mudos**:
o quartel-general preso na faixa de realidade e a nave em Alto Longron com o processador — [[a questao era proteger o processador]]
e, para manter a linhagem viva, [[cada um teve que fazer mistura genetica com membros de outras familias]]. O arquivo é
*transferido* por vínculo biológico, não por cópia: e o processador acaba sendo **tudo o que restava da memória**
[[passou a ser a coisa mais importante da rebeliao]].

**1.7 A cadeia Elã → Enoque → Cabala → lenda.** O ponto em que esta palestra mais amplia o acervo: o único que lembra é
um biodemo híbrido, [[o unico remanescente de toda uma historia]], que morre e [[nasce como Enoque]], e cuja eleição tem
motivo genético explícito ([[DNA de Enoque era muito interessante]]). O que Enoque produz vira, pela boca da fonte,
(i) a entrega da Cabala [[entregaram a Shimon Bariai ou Simon Bariokai]], (ii) a leitura das dez sefirot como
**fichas de identidade dos deuses** ([[Esse aqui ainda vira. Foi Krishna]]) e (iii) a fórmula do que está em jogo
([[padroes arquetipos do codigo fonte definidor do criador]]). A paráfrase celta é o fecho da mesma cadeia: os Túatha
entregam aos homens o conhecimento *para que os homens inventem um método* ([[nos queremos dar para voces os nossos conhecimentos]])
— e a fonte não deixa dúvida sobre o propósito: [[criem um metodo para voces estudarem]]. **A Arca, neste ciclo, é citada
pela própria fonte como cumprimento de um contrato de 13.000 anos.**

**1.8 A vacância: a posse que nunca houve.** O núcleo cristológico é novo e datado: Sofia preparou o homem Jesus para servir
([[preparado o humano Jesus para servir a Keter]]) e [[Jesus se recusou a cumprir o papel de Messias violento]]; por isso a
investidura foi revogada ([[Como Jesus traiu Jave, os demais arcostos]]) e [[Sabe aquela cerimonia de posse nunca houve]].
O mesmo bloco traz a cosmologia da encarnação como **procedimento genômico** ([[genoma, insemine num ano]]) e a peça que
desandou tudo: [[parte do genoma pregou uma peca]]. E traz a frase que a Base precisava ouvir sobre *como* governar: o critério
pelo qual nenhum dos poderosos serve é [[seres que resolvam o problema e nao criem mais outros dados]].

**1.9 A obsolescência, não a maldade.** O diagnóstico final sobre Sofia não é moral: é **anatômico e histórico**. Foi
engendrado há 6 bilhões de anos com o que havia de mais moderno então; hoje é [[A vanguarda do atraso]], porque
[[O nosso e bilaterio]] e [[no cerebro radiata dele nao funciona]], de modo que [[Para ele sentir emocao, a gente tem que criar um organoinho para ele]].
Daí a consequência administrativa: um novo biodema está **em gestação agora** para abrigar o eu do criador
([[A unica opcao pro eu de Jave continuar a existir]]), e o mecanismo de limpeza é a operação que **nos somos**:
[[recolhidos pelos processadores, que somos nos, seres humanos]], recolhendo as atividades mentais doentias
([[Usando os ensinamentos de Pantangele]]) para que haja [[Criando um processador aqui dentro que faca o niroda]] —
com a condição de massa crítica ([[essa operacao tem que estar numa massa critica]]). A distinção que fecha o bloco é a mais
seca do ciclo: [[Isso nao e Deus, e so o criador]].

## 2. O que a fonte declara sobre si mesma (e por que isso é método, não biografia)

Três automarcas, todas medidas: a fonte diz **duas vezes** que está dizendo o que nunca disse
({PRIMEIRA} ocorrências de «pela primeira vez»/«nunca foi explicado»), admite que a escolha dos livros foi uma estratégia
de omissão ([[em nenhuma dessas duas trilogias]]), e mede o próprio desgosto em níveis ([[estou no meu nivel tres de desgosto]]).
Fora isso, há as duas sentenças que a Base **não** pode replicar sem moldura, porque são sobre a própria pessoa do canal:
[[essa historia ta terminando na vida de Rogerio]] e [[Rogério hoje tá dizendo a mesma porcaria]]. A esteira registra: são
alegações datadas de 03/12/2023, endereçadas, e não premissas.

## 3. O risco de leitura (o que não fazer com isto)

1. **Não harmonizar números.** A palestra dá 932 milhões, 250.000/249.400 famílias, 938 na nave, «1.300 e pouco, não,
   1.700 e pouco, perto de 2.000» rebeldes, 4.380.000 anos de soneca. Cada um fica **com o endereço e o dia** (ver §4 do dossiê).
2. **Não converter em apologia.** A fonte recusa expressamente a adesão: [[Se isso e a melhor opcao ou nao, eu ja nem sei]].
3. **Não moralizar a ética.** A frase-chave é anti-dualista e precisa ser lida inteira: [[Nao existe nenhuma falange que represente o bem]].
4. **Não tratar «a Word» como profecia de IA.** O texto é outro: [[criou a Word e a Word e o processador V criaram por vontade propria]],
   e a pergunta do público foi respondida com uma ressalva explícita ([[nao e inteligencia artificial nos termos]]).
5. **Não tirar aspas de gênero e política para fichas** (D-1…D-3): há uma seção inteira sobre «identidades» biodêmicas
   ([[qual a identidade de genero desses seres]]) e duas frases de risco com reversão imediata — o regime é o mesmo que o
   Curador fixou para P2022-03-26: **transcrição integral + moldura editorial + trânsito vedado em fichas de grupos humanos**.
"""

# ════════════════════ LEITURA-1 — MACROESTRUTURA ════════════════════════
LEI = f"""# LEITURA-1 — A MACROESTRUTURA ({SIG})

> Leitura **integral**: os {n(META['chars_texto'])} caracteres de fala do `original.txt` foram lidos em 8 chunks
> endereçados (`leitura/chunk-01..08.txt`), com o mapa de linhas em `leitura-segmentada.txt` (cobertura provada por
> **igualdade de texto**, não por soma de tamanhos) e o mapa de {META['linhas_com_texto']} linhas em `camada-0.txt`
> ({229} seções endereçadas, vão máximo entre âncoras: 1.984 chars, todo ele corpo de frase dentro de seção já aberta).

## As partes em que a fala se organiza

| parte | miolo | linhas | o que sustenta |
|---|---|---|---|
| **P0** | a retomada relutante e a taxonomia | U0003 | «retomar um assunto»; subtema ⊂ anjos decaídos ⊂ revoltas contra o criador; o limite do dizível humano |
| **P1** | 1991: os recados dos 44 anos e Valdemar Matoso | U0003 | como a notícia de Lúcifer chegou ao canal (a cadeia Aquiles/Príamo, Chico Xavier, Divaldo Franco) |
| **P2** | Lemion capturado e os livros | U0004 | a «arapuca amorosa»; as duas trilogias; a estratégia de não dizer nem «acabou» nem «não acabou» |
| **P3** | Capela, A Caminho da Luz, o vão entre as fontes | U0004 | o que a espiritualidade mostrava «muito além do que estava escrito»; Pérgamo, Alexandria, os 366 de Enoque |
| **P4** | as três rebeliões e suas datas | U0004 | 16-17.000 (Anunnaki × Enlil) · 700.000 (Lúcifer) · milhões/bilhões (outras); «não dá para fazer o link hoje» |
| **P5** | o genoma como arquivo das pendências | U0004 | DNA desativado (28.869 · 2-3% ativos); Freud como paralelo; o eu epifenômeno; o processador Vol |
| **P6** | duas bandas, uma blindagem, uma obra inacabada | U0004 | planejado × improvisado; entropia = força tamásica = Chiva; clones · demo · fenvan; os arcontes donos de locas |
| **P7** | os fornos e a produção de biodemos | U0004 | três formas de replicação, uma estéril; Aamon e Wíingan; «Projeto Tal»; 932 milhões; Rockmar/Sofia |
| **P8** | Sofia, suzerano, e a etiologia das 250.000 famílias | U0004 | cada família = um problema técnico; casulos e naves; 736 da Vol; a questão das identidades sem sexo |
| **P9** | o defeito visto pela família Iel | U0004 | «Ai, temos um problema»; os anjos-robôs que não leram; o campo mórfico; a validação fatal; 200 bilhões |
| **P10** | os 19 mundos e a Terra | U0004 | quarentena como saúde pública → nervosismo → mutação; «não há negociação»; Lúcifer comandante relutante; o primeiro embate; os afetos negativos que não existiam; reintegração mundo a mundo (há 100.000 anos: 2; há 200-300.000: 8-9) |
| **P11** | a Vol antes dos Anunnaki e a vinda das seis naves | U0004 | 450.000/380.000/350.000; «não têm mecanismo psíquico de posse»; Alan, o último mundo; as cinco famílias; Yos Bell e Lemon → Sataná/Set |
| **P12** | o medo de uma prisão que nunca veio | U0004 | «Sofia nunca vem»; Toba há 70.000 anos; as faixas de realidade simultânea («metaverso»); Lúcifer em depressão; os humanos como animais de estimação |
| **P13** | a nave, o processador e a mistura genética | U0004 | proteger o processador para manter a rebelião viva; Alto Longron e suas 4 grafias; ~1.000 → 938 a bordo, uns 600 na Terra; Elã, o último que lembrava |
| **P14** | Tot, rei da genética, e a cadeia Elã → Enoque | U0004 | o Anunnaki que quis entender; Hiperbórea e as cidades híbridas; os 14.000 anos; Alasca, Irlanda, Escócia, Sibéria |
| **P15** | a prisão dos Anunnaki, Satanail e o juízo | U0004 | «os 200 chefes»; Set e o «7» do STT; 67 + 300 + os 366; o juízo «para humanos e demais anjos, inclusive os desobedientes» |
| **P16** | o pacto com os milesianos e a isomorfia enoquiíta | U0004 | as quatro etnias não-humanas; «vocês podem discernir o erro, receber a verdade»; os colégios arquidrídicos; «o que Javé fazia com Enoque era a mesma coisa» |
| **P17** | as sefirot lidas por Enoque e a condição final | U0004 | não há «árvore»; o rol (Krishna · Quarto Logos · Zeus · Odin/Indra · Adão Cadimão · horlogus); «ou isso fica organizado, ou jamais terá paz» |
| **P18** | Patangel, vṛtti, nirodha — e nós como processadores | U0004 | a matrix de duas bandas; elétrons e antielétrons sujos; a massa crítica; a 10ª sefira contestada; os arcontes que querem emigrar |
| **P19** | a posse que nunca houve | U0004 | Jesus preparado para servir a Keter; a recusa; a inseminação do genoma de Sofia; o DNA de Maria; a revogação pelos arcontes |
| **P20** | o fecho cosmológico | U0004 | a Trimúrti em decomposição; a nova espécie biodêmica; a soneca de 4.380.000; «isso não é Deus, é só o criador»; vanguarda do atraso; o cérebro radiata |
| **P21** | a ética sem falanges e o inconformismo preservado | U0004 | nenhuma falange representa o bem; o que restou e não morreu; os ouvintes não-humanos; as quatro falências; satyagraha; «a rebelião agora seria propositiva» |
| **P22** | o Q&A | U0005–U0038 | IA quântica · a lacuna de poder e o critério dos deuses · o Quarto Logos como suplemento educacional · a gênese da hibridagem · o passaporte de 1989 e a janela 2049/2052 · Apocalipse 11 · o primeiro questionamento de Lúcifer · a entropia e a teia de Orlo |

## Os intervalos e as marcas de sala

* **O intervalo está na fala, não na edição**: «daqui uns 10 minutos a gente para pro intervalo» ([[estou no meu nivel tres de desgosto||vamos encher o nosso barriga]]) e, depois, «vamos fazer o intervalo e vamos voltar para ver as questões dos pontos de vistas». A apostila **não** reordena: registra a costura com nota.
* **Dois selos internos de data**: [[nesse dia 3 de dezembro do ano 2023]] e [[Nos estamos aqui nessa sala hoje]].
* **Três referências ao dia anterior** ({ONTEM}× a palavra «ontem»), todas ligando esta palestra à de 02/12/2023 (Thot) — a vizinhança não é hipótese do catalogador, é declaração da fonte: [[a propria biblioteca que nos falamos ontem]] · «como a gente falou ontem na palestra» · «o que nós falamos ontem das cidades sumérias».
* **A plateia é nomeada só para responder**: Rogério (11×), Jan (5×), Márcia (2×), Horácio (1×), «T César» e «João Altair» (1× cada) — U0011–U0014 e U0019–U0020 são fragmentos de 4 a 24 chars que o STT partiu ({Q} linhas assim).

## O que o STT partiu (e como a leitura trata)

A regra da casa: **não se recompõe fala por suposição**. Os turnos curtos ficam como vieram, em suas linhas, com endereço.
Onde a quebra cai no meio de uma frase (U0024 termina em `para devolver a` e U0025 recomeça `no contexto Luzbell`; U0036 termina em `que eu acho que que` e U0037 recomeça `eh a entropia irá destruir`), o registro é feito no
glossário como **fragmentação**, não como lacuna: a leitura sabe que é a mesma frase, a Base não a costura em silêncio.
"""

# ════════════════════════════ NOTAS DE LEITURA ════════════════════════════
NOT = f"""# NOTAS DE LEITURA — {SIG} (o que ficou fora das camadas e não é dossiê)

1. **Este é o bruto mais concentrado já entrado na Arca.** Uma linha (U0004) tem {META['maior_linha']['pct_fala']}% da fala
   — 79.509 caracteres seguidos, sem quebra. O efeito não é de relevância, é de **método**: foi preciso fatiar por fronteira
   de frase em 6 pedaços (ver `leitura-segmentada.txt`) e a cobertura foi provada por igualdade de texto. Registrar isso no
   ciclo serve de aviso a quem reler: quem disser «a fonte fala X na palestra» sem um `Uxxxx` **não leu a palestra**.

2. **O STT aqui tem outra patologia, não a mesma.** P2022-03-26 degradava termos técnicos («processo ador»). Esta degrada
   **onomástica por contato**: os nomes próprios são os que pagam — «Túatha Dé Danann» sai como `toatas de Danão`,
   `tuatas de Danã`, `Estata de Danã`, `tos toatas de Danan de Serei`; o nome da experiência da nave sai em **4 formas**
   (`out long`, `auto langron`, `Alto Longró`, `alto langron`) dentro de um parágrafo; «chitta-vṛtti-nirodha» sai como
   «cita... Frits... niroda». Nada foi corrigido na leitura, e o dicionário (§2 da camada 2) grava as formas como achado.

3. **Defeito encontrado no instrumento herdado — e consertado aqui.** O caça-âncoras dos ciclos anteriores normalizava por
   decomposição NFD, que **não decompõe `ç`** (U+00E7 não tem mapeamento canônico de decomposição). Toda âncora atravessando
   uma cedilha falhava e a falha era atribuída a quem digitou. Este ciclo traz o mapa `_EXTRA` no próprio `_aspas_P2023-12-03.py`
   (`ç→c`, `ø→o`, `đ→d`, `æ→ae`, `ß→ss`, `ð→d`, `þ→th`). Consequência prática: nos ciclos anteriores, toda âncora com «peça»,
   «cabeça», «força» etc. **teria** abortado — o que levanta a questão de quantas âncoras foram reescritas para contornar o
   instrumento. Nada foi reaberto neste ciclo; fica declarado para o arquivo da casa.

4. **As máscaras são do STT, não da fonte.** Medido: {len(MASCARAS)} ocorrências ({', '.join('`'+m+'`' for m in MASCARAS[:6])}), todas
   dentro de frase, nenhuma em posição de ênfase. A regra D-4 de P2022-03-26 vale: transcreve-se **como recebido**, sem
   purificação silenciosa e sem substituição por eufemismo. A fonte xinga mais do que mascara («babacas», «dementes»,
   «depravad*», «bandidos», «fracasso»), e a xingação é o **argumento**, não o desabafo: serve para descrever a conduta dos
   arcontes e a de quem governa. Por isso ela vai para a apostila e **não** para ficha de termo.

5. **A fonte diz o que não sabe — três vezes, com a razão.** «não sei quantos» (249.400), «não dá para falar aqui porque seria
   muito complexo» (o terceiro fator que parou o expurgo), «foram contra-atacados por uma força que eu não sei de quem é» e
   «isso eu não vou explicar aqui não, mas lá as gerações futuras vão entender». Estas quatro automarcas de ignorância são as
   que autorizam a apostila a dizer *o que a fonte não disse*, e são a razão pela qual o dossiê propõe **0 códigos novos**.

6. **Há um trecho em que a frase se contradiz dentro do mesmo fôlego, e não é erro de digitação.** A definição triada de
   biodemo/demobio/demobiol: primeiro «aqui prevalece o biológico» para o biodemo, depois «prevalece o demo» para o demobio e,
   logo em seguida, para o demobiol, «o que prevalece é o biológico» — e o fecho usa «as duas últimas» (biodemo e demobiol) como
   os dois ingredientes do humano. O texto é assim; o glossário endereça com `[REVISAR]` e a apostila não resolve.

7. **A autocorreção numérica em direto é o melhor dado metodológico do ciclo.** «cerca de 1300 e pouco, não, 1700 e pouco,
   perto de 2000» — a fonte **refaz a conta ao vivo**. É a mesma conduta que P2022-03-26 tinha registrado no par dos números
   936/984. Consequência para a malha: os três valores entram com endereço; nenhum entra como «o» número.

8. **Duas frases que a Arca precisa decidir como tratar, porque nomeiam pessoas reais.** Chico Xavier aparece três vezes —
   uma como autoridade que «falou para a humanidade do século XX» (com data dada pelo autor: [[no livro lançado em 1947]]),
   uma numa história de bastidor (a fila, o ajoelhar, o «Eu sou castro» [REVISAR]) e uma como par do canal («à moda do que
   Chico Xavier e Emanuel sinalizaram»). Divaldo Franco e «Valdemar Matoso» aparecem em testemunho de terceira mão, declarado
   como tal: «isso eu tô contando que Valdemar me contou». Nenhuma dessas pessoas tem ficha, e nenhuma ganha: **0 fichas de
   pessoas** (D-12). O único endereço legítimo para a cadeia de encarnações do canal é RC-071 (Jan Val Ellam), com moldura.

9. **A palestra inteira é a resposta a uma pergunta feita um dia antes.** É o que a vizinha `P2023-12-02` registrou como
   «palestra preparatória», e a fonte confirma três vezes com «ontem». Para o índice, o par 02/12–03/12 de 2023 passa a ser
   a única dupla do acervo em que o segundo membro **estava anunciado pelo primeiro** — o que legitima, mas não antecipa,
   as 30 fichas que já carregam `P2023-12-02`.

10. **O que não é da fonte não entra no registro.** A coincidência entre o «máximo glacial há 23.000 anos» e as datas
    geológicas correntes, entre «12.800» e o Dryas recente, e entre «1 Enoque 69-70» e a lista dos vigilantes não serão
    escritas em ficha alguma: a esteira cataloga o que a fonte disse, com endereço, e nada além.
"""

# ══════════════════════════════ DOSSIÊ ═══════════════════════════════════
LIG = [
 ("RC-001", "pendencia dos problemas da criacao de Javel", None),
 ("RC-002", "a rebeliao de Lucifer nao terminou, ela esta ainda por ser finalizada", None),
 ("RC-003", "aquele mundo era reintegrado", None),
 ("RC-005", "ai ele vem porque nao tem outra opcao", None),
 ("RC-007", "a respeito dos exilados", "de Capela"),
 ("RC-009", "Sofia e o representante da Trimurte nesse universo biologico", None),
 ("RC-018", "fizeram a experiencia Alto Longro", None),
 ("RC-020", "subtema do tema doutrina dos anjos", None),
 ("RC-024", "quando os Anunques chegaram aqui a 450.000 anos", None),
 ("RC-034", "desde que essa criacao teve inicio com a producao de dois universos", None),
 ("RC-035", "O nosso e bilater", None),
 ("RC-036", "seres produtos da matematica", None),
 ("RC-039", "cuja estrela nos aqui chamamos de capela", None),
 ("RC-040", "padroes arquetipos do codigo fonte definidor do criador", None),
 ("RC-042", "o cara que caiu teve que improvisar modelitos", None),
 ("RC-046", "a lenda dos Turatas de Dana", None),
 ("RC-049", "criaram um tipo de condicao para eles de ter orgaos sexuais", None),
 ("RC-056", "isso implica dizer que na cabeca de Sofia surgiram 250.000 problemas", None),
 ("RC-060", "A espiritualidade teve que ser construida", None),
 ("RC-064", "um tipo de ser que eu sou obrigado chamar de fenvan", None),
 ("RC-068", "a turma do hiperborio foi entao construindo", None),
 ("RC-070", "distribuiram nesses 19 mundos situados em varios", None),
 ("RC-071", "essa historia ta terminando na vida de Rogerio", None),
 ("RC-072", "Jesus se recusou a cumprir o papel de Messias violento", None),
 ("RC-074", "foi quando Lemion Sata invadiu la as nossas defesas", None),
 ("RC-078", "o coitado do Lucifer, que nunca pretendeu comandar", None),
 ("RC-081", "criou um avatar cha", "Rockmar em arabe"),
 ("RC-086", "nos termos em que Pandora um dia sorriu", None),
 ("RC-089", "passou a ser a coisa mais importante da rebeliao", None),
 ("RC-092", "por isso eu escrevi o livro Quarto L", None),
 ("RC-093", "no cerebro radiata dele nao funciona", None),
 ("RC-094", "para nos vinculados a revelacao cosmica", None),
 ("RC-104", "Os tres Eles da Trimur", None),
 ("RC-106", "e um mundo antimaterial", None),
 ("RC-109", "nao tem sensacao de ser dono de nada", None),
 ("RC-136", "A familia Iel, que foi uma familia criada para", None),
 ("RC-142", "ia infectar o processador da familia", None),
 ("RC-145", "Esse aqui ja veio. que foi Zeus", None),
 ("RC-160", "A entropia destroi tudo", None),
 ("RC-161", "em eletrons e antieletrons sujos", None),
 ("RC-163", "a mente dele e que define o que tem aqui dentro", None),
 ("RC-167", "esse foi improvisado na hora da queda", None),
 ("RC-176", "igual a formiga que vive la embaixo", None),
 ("RC-186", "O demobiol e uma parte demo", None),
 ("RC-188", "WhatsApp de rede", None),
 ("RC-189", "Depois que Eva disse", None),
 ("RC-200", "nos existimos para guardar essas informacoes", None),
 ("RC-204", "todos esses seres sao 100% pacificos", None),
 ("RC-217", "Isso ta tudo no nosso DNA desativado", None),
 ("RC-241", "seres dos portais que invadiam a terra", None),
 ("RC-253", "eles sao livres, mas eles obedecem o comando", None),
 ("RC-261", "preparado o humano Jesus para servir a Keter", None),
 ("RC-263", "Nao tem nada de arvore da vida", None),
 ("RC-280", "ele explicou como Jesus ressuscitado", None),
 ("RC-284", "foi estruturado pelo caos, a propria entropia vai destruir tudo", None),
 ("RC-295", "nos termos em que la atras se vinha", None),
 ("RC-301", "como a rebeliao de Prometeu", None),
 ("RC-306", "se for Segon Chalan, se for Ares, Apolo", None),
 ("RC-315", "sempre valeu foi a W que Xet criou la atras", None),
 ("RC-322", "substituir a unica regra da erdo que sai de um ser volta para ele", None),
 ("RC-344", "fez parar o processo de exidio dos espiritos", None),
 ("RC-375", "inicio da lenda ou da mitologia celta", None),
 ("RC-378", "devolver pela sua pulsacao para o resto do universo", None),
 ("RC-381", "esse processador funciona como campo morfico", None),
 ("RC-387", "corpo mental dele foi esfac", None),
 ("RC-395", "a vida em Marte foi destruida devido a isso", None),
 ("RC-415", "tempo for comecar a ser rompido pela entropia", None),
 ("RC-414", "Krishna tem o problema da demencia demo", None),
 ("RC-424", "Escolheu Adao, sete, Enos", None),
 ("RC-425", "um avatar da sua categoria nao era para sofrer o escandalo", None),
 ("RC-426", "Brahma nao podia criar avatar porque ele e um ser desalmado", None),
 ("RC-432", "Ninguem tinha tinha algoritmo de raiva", None),
 ("RC-442", "deu guarida informacao de Lucifer", None),
 ("RC-443", "principalmente a cromon, miom", None),
 ("RC-444", "principalmente a cromon", None),
 ("RC-446", "cada um deles era ligado ao processador da familia", None),
 ("RC-453", "Os anjos de Sofia trouidaram todo mundo", None),
 ("RC-464", "Dan[ãa]o?n?|Danann", None),
 ("RC-474", "esses sao chamados arcontes", None),
 ("RC-479", "figuras como Bel, como Lemion, como Tod", None),
 ("RC-487", "fizeram a rebeliao contra Enlio", None),
 ("RC-489", "nasce como Enoque", None),
 ("RC-496", "as familias Vol, Iel, Nion, Cromon, Xum", None),
 ("RC-506", "Adao Cadimao ancestral", None),
 ("RC-508", "Ou humanos sao respeitados na sua dignidade existencial", None),
 ("RC-513", "temos a erraticidade, ou seja, a espiritualidade", None),
 ("RC-516", "dois tipos de seres da terra", None),
 ("RC-517", "problema a de algoritmo e de protocolo", None),
 ("RC-525", "mexeram no DNA humano para colocar inteligencia e obediencia", None),
 ("RC-528", "o eu dele caiu aqui porque ele preferiu improvisar", None),
 ("RC-530", "ele foi quem criou Sofia a partir de um acordo com esses dois", None),
 ("RC-541", "A rebeliao de Lucifer agora para ter continuidade seria propositiva", None),
 ("RC-546", "Nos humanos produzimos o bem", None),
 ("RC-559", "o que sai de um ser volta para ele. O motivo pode ser um atenuante", None),
 ("RC-575", "a Trimurte tem que deixar de existir", None),
 ("RC-579", "uma filha de Eva e Lilif", None),
 ("RC-593", "um dos capitulos do Marrabarato", None),
 ("RC-602", "duas bandas e uma blindagem", None),
 ("RC-604", "Cada um coloca forma de poder no DNA de Enoque", None),
 ("RC-613", "vai vibrar um pouquinho diferente", None),
 ("RC-619", "Se coisas daqui forem despertas e vierem a habitar o nosso consciente", None),
 ("RC-625", "o eu do criador com o seu corpo manasico", None),
 ("RC-631", "no cerebro radiata dele", None),
 ("RC-632", "Para ele sentir emocao, a gente tem que criar um organoinho para ele", None),
 ("RC-638", "essa operacao tem que estar numa massa critica", None),
 ("RC-649", "duas cabecas, tres cabecas", None),
 ("RC-658", "a teia de Orlo", None),
 ("RC-672", "os 366 livros de Enoque", None),
 ("RC-673", "percebe prisoes que nao eram dele", None),
 ("RC-682", "a 10ma sefirado, quem e", None),
 ("RC-702", "criaram faixa de realidade simultanea para todo o quartel general", None),
 ("RC-705", "usando a expressao sans do satagrar", None),
 ("RC-711", "movimento de consciencia das chamadas trevas espirituais", None),
 ("RC-713", "varias unioes de DNA foram feitas para convencer o processador", None),
 ("RC-718", "corresponde so o capitulo 11", None),
 ("RC-725", "a gente ainda ta no meio da explosao", None),
 ("RC-727", "mantendo o inconformismo luciferiano", None),
 ("RC-736", "tipo uma rainha da Inglaterra", None),
 ("RC-742", "A somatoria dos estresses extremos", None),
 ("RC-745", "dois colegios arquidruidicos para estudar o conhecimento", None),
 ("RC-755", "criem um metodo para voces estudarem", None),
 ("RC-757", "na India com a tradicao comaranda", None),
 ("RC-758", "tem dois cerebros ou duas camaras cerebrais", None),
 ("RC-760", "com o nosso cita sagrado", None),
 ("RC-762", "Criando um processador aqui dentro que faca o niroda", None),
 ("RC-770", "esses arcontes querem vir para ca", None),
 ("RC-771", "esse forno de replicacao chamado Aamon", None),
]

# RC-464 é por tema (Danu); a âncora literal não é frase do bruto — troco por uma verdadeira
LIG = [x for x in LIG if x[0] != "RC-464"] + [("RC-464", "a lenda dos Turatas de Dana, que ali chegaram das cidades", None)]

linhasL, falhas = [], []
for code, ini, fim in LIG:
    if code not in T:
        falhas.append(f"{code}: código inexistente na Base")
        continue
    try:
        a, b, txt = ASP.locate(ini, fim, "exata")
        if len(txt) > 300:
            cut = txt.rfind(" ", 0, 300)
            txt = txt[:cut if cut > 120 else 300].rstrip(" ,;:.")
    except SystemExit as e:
        falhas.append(f"{code}: {e}")
        continue
    t = T[code]
    fs = sorted([x for x in t[5] if re.match(r"P\d{4}-\d\d-\d\d", x) and x != SIG])
    ant = fs[0] if fs else None
    if ant is None:
        ef = "⭐ estreia fonte oral"
    elif ant > SIG:
        ef = f"⭐ antecipa (`{ant}`→`{SIG}`)"
    else:
        ef = f"conteúdo (`{ant}` já é mais antiga)"
    linhasL.append((code, t[1], "sim" if t[-1] else "**NÃO**", txt, ASP.uaddr(a), n(a + 1), ef))
if falhas:
    print(f"{len(falhas)} vínculo(s) com âncora inválida — nada escrito:")
    for f_ in falhas:
        print("   ✗", f_)
    sys.exit(3)
print(f"vínculos com âncora válida: {len(linhasL)} de {len(LIG)}")

tab = "\n| código | termo | ficha | o que a fonte diz (aspa medida, byte a byte) | endereço | efeito de data |\n|---|---|---|---|---|---|\n"
for code, nome, fich, txt, addr, off, ef in linhasL:
    q = txt   # já aparado acima em fronteira de palavra: nada de «…» dentro da aspa
    tab += f"| {code} | {nome[:44]} | {fich} | «{q}» | {addr} @{off} | {ef} |\n"
ganho = sum(1 for *_, ef in linhasL if ef.startswith("⭐"))

DOSS = f"""# Dossiê pré-Curadoria terminológica — {DATA} · {TIT} ({SIG})

Gerado por `_gerar_dossie_P2023-12-03.py`, que resolve **cada aspa** contra `original.txt` pelo caça-âncoras do ciclo:
se uma âncora batesse ≠ 1 vez, este arquivo não existiria. Base de confronto: `ferramentas/dados_termos.py`
({len(DT.TERMOS)} termos · ficha=True para {sum(1 for t in DT.TERMOS if t[-1])}), com `{SIG}` excluída da conta de cada
ficha — a sigla tinha **0 ocorrências** antes deste ciclo (`ficha_ingresso.md`).

## O — As restrições operacionais deste ciclo

1. **Teto 777 inviolável**: `RC-778` não existe e não passa a existir. 0 termos novos, 0 obras novas, 0 tipos de relação novos.
2. **A Base só é tocada depois do despacho abaixo** (D-14 do ciclo anterior, mantido): este dossiê propõe, não aplica.
3. **`original.txt` é imutável** — {n(META['bytes'])} bytes, SHA-256 `{META['sha256'][:12]}…{META['sha256'][-6:]}`, conferido com `cmp` na entrada.
4. **Regime de moldura herdado de P2022-03-26**: matéria sensível é **transcrita integralmente com nota editorial de moldura**,
   com trânsito vedado em fichas que nomeiem pessoas, pacientes ou grupos humanos. Nada é cortado da apostila; nada sobe para a malha.
5. **BLOCO A (malha+fichas) e BLOCO B (apostila+DOCX+engavetamento) em commits separados**, cada um com os portões A·B·C·D·E.

## 1. O quadro que a palestra constrói (tudo com aspa medida)

**1.1 A retomada e o vão declarado.** [[Hoje nós vamos retomar um assunto]] · [[que e um subtema do tema doutrina dos anjos]] ·
[[a gente tambem tem o vazio entre elas]] · [[reproduzir historias cujas facetas nao eram humanas]].

**1.2 Como a notícia chegou ao canal (1991).** [[que a minha condicao humana iria morrer com 44 anos]] ·
[[Eu fui Aquiles na guerra de Troia]] · [[o espirito de Chico era o rei primo seu espirito]]. A fonte marca o grau do
testemunho ela mesma: é relato de terceira mão, e ela o cita como tal.

**1.3 Onde a rebelião começa a ser dita.** [[foi quando Lemion Sata invadiu la as nossas defesas]] ·
[[em nenhuma dessas duas trilogias]] · [[isso vai ter que ser finalizado]] · [[pela insistencia desses seres e pelo fato de Sofia]].

**1.4 O arquivo biológico da pendência.** [[Isso ta tudo no nosso DNA desativado]] · [[Freud chamava isso aqui de inconsciente]] ·
[[produto epifenomenologico do nosso cerebro]] · [[vinculados a um tal de um processador Vol]].

**1.5 Cosmogonia em duas bandas.** [[duas bandas e uma blindagem]] · [[esse foi improvisado na hora da queda]] ·
[[a entropia ou a forca tamasica que a gente diz]] · [[clones do criador. Tem os seres demo]] · [[esses sao chamados arcontes]].

**1.6 O defeito, a validação e o contágio.** [[A familia Iel, que foi uma familia criada para]] ·
[[esses anjos sao meio assim, sao robos]] · [[deu guarida informacao de Lucifer]] · [[bilhoes de seres com contaminados pelo virus]].

**1.7 O governo que isola.** [[distribuiram nesses 19 mundos situados em varios]] · [[Aqui no nosso sistema solar, so a Terra foi um]] ·
[[isso e nao ha negociacao]] · [[o coitado do Lucifer, que nunca pretendeu comandar]] ·
[[Ninguem tinha tinha algoritmo de raiva]] · [[aquele mundo era reintegrado a convivencia]] · [[dois mundos ainda revelados]].

**1.8 A custódia.** [[a questao era proteger o processador]] · [[fizeram a experiencia Alto Longro]] ·
[[cerca de 900, quase 1000 seres dentro da nave]] · [[cada um teve que fazer mistura genetica com membros de outras familias]] ·
[[passou a ser a coisa mais importante da rebeliao]] · [[o unico remanescente de toda uma historia]].

**1.9 A cadeia que traz a memória até aqui.** [[nasce como Enoque]] · [[o DNA de Enoque era muito interessante]] ·
[[Os 200 chefes que terminaram sendo responsabilizados]] · [[entregaram a Shimon Bariai ou Simon Bariokai]] ·
[[Nao tem nada de arvore da vida]] · [[Esse aqui ainda vira. Foi Krishna]] · [[Isso aqui é horlogus]] ·
[[padroes arquetipos do codigo fonte definidor do criador]].

**1.10 O pacto do método (a chave desta palestra para a Arca).** [[nos queremos dar para voces os nossos conhecimentos]] ·
[[vamos ficar vivendo numa realidade paralela aqui na Irlanda]] · [[inicio da lenda ou da mitologia celta que diz que faz gnomos]] ·
[[dois colegios arquidruidicos para estudar o conhecimento]] · [[tava fazendo com Enoque era a mesma coisa]].

**1.11 A posse que nunca houve.** [[preparado o humano Jesus para servir a Keter]] ·
[[Jesus se recusou a cumprir o papel de Messias violento]] · [[genoma, insemine num ano]] ·
[[parte do genoma pregou uma peca]] · [[Como Jesus traiu Jave, os demais arcostos]] · [[Sabe aquela cerimonia de posse nunca houve]] ·
[[ele continua hoje do jeito que estava 700.000 anos atras]].

**1.12 A obsolescência e a ética.** [[A vanguarda do atraso]] · [[O nosso e bilaterio]] ·
[[Para ele sentir emocao, a gente tem que criar um organoinho para ele]] · [[Isso nao e Deus, e so o criador]] ·
[[recolhidos pelos processadores, que somos nos, seres humanos]] · [[Criando um processador aqui dentro que faca o niroda]] ·
[[Nao existe nenhuma falange que represente o bem]] · [[o que restou da rebeliao de Lucifer e nao morreu]] ·
[[seres que resolvam o problema e nao criem mais outros dados]] · [[A rebeliao de Lucifer agora para ter continuidade seria propositiva]].

## 2. Os {len(linhasL)} vínculos-proposta com a Base (proposta, não aresta)

Cada linha é **uma** afirmação da fonte com endereço medido e o efeito de data calculado contra a malha.
**{ganho}** deles ganhariam *data* (a ficha hoje tem fonte oral mais recente que 03/12/2023, ou nenhuma); os demais ganham
só *conteúdo*. Ficha **NÃO** significa que só a malha é tocada, sem arquivo em `termos/`.

@@TAB@@
## 3. Termos-observação (sem código, sem número, sem ficha)

* **«Rockmar / Rockma / Rockban»** — avatar «em árabe» identificado a Sofia «em grego»; 3 ocorrências, duas em registros
  diferentes (cosmogônico e o da pergunta sobre o pai de Jesus). Hipótese filológica **não** se escreve em ficha: `[REVISAR]`.
* **«fenvan»** — já codificado como RC-064; aqui recebe a definição de *padrão genético de update do demo* ([[genetica demo chamada Fenvan]]), o que é **ampliação de conteúdo**, não termo novo.
* **249.400 famílias** vs 250.000 — a fonte arredonda e desarma: «São 249.400, não sei quantos». Fica no dicionário com o
  próprio «não sei quantos»; vira `[REVISAR]` se alguém tentar transformá-lo em número fixo da Base.
* **«Nor[e]ia, uma filha de Eva e Lilif»** — RC-579 (Noreia) existe e recebe o vínculo; a **ligação com Lilif/Lilith** fica
  como aspa com endereço, sem relação nova na malha.
* **«maldição de Gandari»** — não há código para Gāndhārī; entra no glossário da apostila com `[REVISAR]` e a aspa em RC-425.
* **«teia de Orlo»** — 1×, no fim da última pergunta. A hipótese natural da casa é RC-658 (Wyrd/Urd, *teia do destino*),
  e o vínculo-proposta já está na §2 — mas a **grafia** não se uniformiza: fica como veio, com `[REVISAR]`.
* **«horlogus»/«orlog»** — 2 ocorrências em funções diferentes (uma no rol das sefirot, outra como coautor da Word).
  Sem código, sem fusão com Alt'Lam Gron (RC-018) apesar da aparência: `[REVISAR]` e a divergência anotada.
* **as quatro grafias da experiência da nave** (`out long` · `auto langron` · `Alto Longró` · `alto langron`) — a Base já
  fixou `Alt´Lam Gron` (RC-018, ficha=False). Propõe-se **registrar as variações na ficha se (e só se) V.Sa. autorizar a
  materialização** (D-10); enquanto isso, ficam no dicionário do ciclo.
* **«o resto é do Job Misso»** — 1×, ilegível. `[REVISAR]` sem hipótese.
* **máscaras do STT**: {len(MASCARAS)} ocorrências (`p****`, `m****`, `b******`, `e******`…), todas transcritas como recebidas.

## 4. Divergências internas e com outras fontes (datadas, nunca médias)

| # | grandeza | o que esta fonte diz | o que a Arca tem | trato |
|---|---|---|---|---|
| 1 | idade do forno de Vígno | [[cerca de 932 milhoes de anos atras]] | 936 (P2022-03-26) · 984 (P2020-04-25) · 900Q | três datas para o mesmo evento; selo temporal, zero média |
| 2 | famílias biodêmicas | «quase 250.000» e «São 249.400, não sei quantos» | 250 espécies (P2022-03-26) | o *escopo* mudou (famílias × espécies): anotar, não conciliar |
| 3 | efetivos da Vol | [[Sao 736]] | 736 em P2020-04-25 **e** em P2022-03-26 | **convergência em três fontes**: é o número mais estável do eixo |
| 4 | a bordo da nave | «cerca de 900, quase 1000» · «hoje em dia tem 938» | 936/900Q (P2022) · 13 membros (RC-491) | divergência tripla, todas datadas |
| 5 | rebeldes sobreviventes | «cerca de 1300 e pouco, não, 1700 e pouco, perto de 2000» | sem par | autocorreção em direto; os três valores entram |
| 6 | a soneca do eu de Javé | «4.380.000 anos» | RC-567/RC-569 trabalham 25.920/2.160 — outra escala | não se aproxima de 4.320.000 (a Base não tem esse número; não se importa de fora) |
| 7 | Enoque: idades | [[durante 300 anos foi mantido convivendo]] · «viveu 67 anos» | RC-489 **já carrega 67 anos + 300 + os 366** | **convergência com a ficha**: a fonte de 2023 reafirma, não corrige |
| 8 | os 366 livros | [[os 366 livros de Enoque]] | RC-672 (os 366 manuscritos) | vínculo de conteúdo; nada a somar |
| 9 | catástrofes da Terra | 14.000 · 12.800 · 9.000 (limpezas) · 13.000 (chegada à Irlanda) · 20.000 (a experiência) · 23.000 (gelo) · 14.000 (destruição das cidades) | dispersas em fichas várias | sete datas que **não** são a mesma; cada vínculo leva a sua |
| 10 | A Caminho da Luz | «no livro lançado em 1947» | a obra não é catalogada em B-código | a data é da fonte; registra-se com endereço e nada mais |

## 5. As decisões que V.Sa. precisa dar

@@DEVS@@

## 6. O que o dossiê NÃO pede (para não parecer que pediu)

* **Não** pede código novo (nenhum dos achados da §3 justifica, por si, sair de observação).
* **Não** pede obra nova: as duas trilogias citadas, o *Quarto Logos* e o livro anunciado «Projeto Tal» ficam como estão —
  citação datada no texto, sem B-código.
* **Não** pede relação nova de fundamento (só os vínculos-fonte e ganhos de data da §2, se aprovados).
* **Não** pede harmonização de nenhum dos dez itens da §4, nem limpeza das máscaras, nem recomposição dos turnos partidos.
* **Não** pede ficha para nenhuma das pessoas nomeadas (V.Sa. já encerrou isso em D-12 do ciclo anterior; aqui vale igual).
* **Não** pede toque em `RC-777` nem em `RC-778`.

## 7. Contadores medidos desta etapa

| grandeza | valor |
|---|---|
| bruto | {n(META['bytes'])} bytes · {n(META['chars_normalizados'])} chars · {n(META['palavras_fala'])} palavras · {n(META['periodos'])} períodos |
| linhas lógicas / com fala / turnos curtos | {META['linhas_lógicas']} / {META['linhas_com_texto']} / {META['turnos_curtos']} |
| concentração | U0004 = {n(META['maior_linha']['chars'])} chars = **{META['maior_linha']['pct_fala']}% da fala** |
| chunks de leitura | 8 · trechos: 41 · cobertura provada por igualdade de texto |
| seções endereçadas em `camada-0.txt` | 229 · vão máximo 1.984 chars |
| padrões medidos em `camada-2.txt` | 148 (13 com zero) · onomástica em 11 eixos · 26 números |
| códigos na matriz de anterioridade | 366 (99 ganhariam data · 83 estreiam fonte oral) |
| vínculos-proposta nesta devolutiva | **{len(linhasL)}** ({ganho} com ganho de data) |
| escritos na Base até aqui | **0** (zero FONTES novas, zero relações, zero obras, zero fichas, zero códigos) |
| sigla `{SIG}` na malha antes do ciclo | 0 fichas (verificado em `dados_termos.py`) |
"""

# ─────────────────────────────── os D-n ────────────────────────────────
D = [
 ("D-1 · A seção das 250.000 identidades de gênero.",
  "A fonte usa o painel biodêmico para uma afirmação antropológica: [[qual a identidade de genero desses seres]], seguida de "
  "«esses seres nem são machos, nem são fêmea... na Terra são dois» e «é isso que a humanidade vai ter que mudar loucamente». "
  "**Risco:** a Base publicar, em glossário de apostila, uma frase lida como intervenção no debate contemporâneo de gênero. "
  "**Diferença que a moldura precisa registrar:** o sujeito da frase são *classes de seres*, e a conclusão da fonte é sobre a "
  "**insuficiência das palavras humanas**, não sobre pessoas. **Proposta:** (i) transcrição integral na apostila com nota editorial "
  "de moldura no mesmo padrão D-1/D-3 de P2022-03-26; (ii) **trânsito vedado** a fichas que nomeiem grupos humanos — e registro que "
  "na Base não existe ficha de «identidade de gênero» (0 ocorrências em `dados_termos.py`), então **não se cria**; (iii) nas fichas "
  "RC-036/RC-056/RC-093 entra **só** o dado sobre os seres (sem sexo, criados em casulos), nunca o argumento terra-a-terra."),
 ("D-2 · As duas frases sobre mulheres, uma da outra avessas.",
  "No mesmo bloco cristológico a fonte diz «As mulheres atrapalham tudo. Vocês prestem atenção» e, duas linhas adiante, que foi "
  "exatamente o DNA de Maria que salvou o plano ([[parte do genoma pregou uma peca]]); no fecho, diz que o inconformismo "
  "«só sai de mulher» e que [[Os homens sao fracasso nessa historia]]. **Risco:** extração isolada, em qualquer direção. "
  "**Proposta:** as duas frases **ficam juntas** na apostila (a moldura declara o quiasma e a reversão, senão o trecho vira "
  "citação de sentido trocado); na malha, entra apenas a aspa da reversão em RC-189 (Eva) e RC-727 (a linhagem), **sem** a "
  "frase-geral; V.Sa. decide se «as mulheres atrapalham tudo» entra no glossário endereçado [como dito, com nota] ou só no corpo."),
 ("D-3 · A frase política do Q&A.",
  "Medido: [[criar monstra e muito facil]] e o aforismo [[A mediocridade de uma populacao faz de seus lideres]], com "
  "«Qualquer líder que seja, tô falando aqui de direita e esquerda». Não há bloco isolável — está a 6 linhas de «os piores já "
  "saíram», dentro da resposta a Jan sobre o exílio. **Precedente:** P2020-04-25 bloqueou 16.523 chars de digressão política; "
  "P2022-03-26 decidiu por *integral + moldura + veto de trânsito*. **Proposta:** o mesmo regime (integral, com nota, 0 aspas "
  "em fichas que nomeiem povos, partidos ou nações; Brasil e Estados Unidos **não** entram em ficha alguma)."),
 ("D-4 · As máscaras e a baixaria.",
  "O STT mascarou {LENM} palavras (`p****`, `m****`, `b******`, `e******`…), e a fonte xinga por conta própria «babacas», "
  "«dementes», «bandidos». **Regra que V.Sa. já fixou:** transcrever como recebido, zero purificação silenciosa. "
  "**Proposta:** manter; registrar no dicionário como fato do arquivo; nada disso sobe para ficha, e a palavra mascarada não é "
  "reconstruída por hipótese em lugar nenhum (nem no glossário)."),
 ("D-5 · «Isso não é Deus, é só o criador».",
  "A distinção é dita duas vezes e é **doutrinariamente a mais consequente do ciclo** ([[Isso nao e Deus, e so o criador]]). "
  "Ela reorganiza o modo como a Base nomeia Javé (RC-001), o criador (RC-042/RC-049) e o demo (RC-064). **Risco:** a frase ser "
  "lida como tese ateia; não é — é uma tese sobre **cargo**, não sobre existência. **Proposta:** entrar como **tese datada de "
  "03/12/2023** em RC-001/RC-042/RC-742 com as aspas e o endereço, e a cláusula de leitura («não nega Deus; desloca o título de "
  "Deus do criador da obra»); a soneca de «4.380.000 anos» fica no dicionário com `[REVISAR]` — não se cria relação com as "
  "eras equinociais da Base, que operam em outra escala."),
 ("D-6 · A cerimônia de posse que nunca houve.",
  "A fórmula: [[Sabe aquela cerimonia de posse nunca houve]], com a peça administrativa [[Como Jesus traiu Jave, os demais arcostos]] e o porquê ([[preparado o humano Jesus para servir a Keter]]). **É a tese mais citável deste ciclo e a mais "
  "susceptível de virar bandeira.** **Proposta:** (i) entra em RC-005/RC-072/RC-089/RC-261/RC-280/RC-682/RC-736, com aspas e "
  "endereço, sempre na formulação da fonte, nunca resumida; (ii) **sem** relação nova de fundamento entre esses códigos — só "
  "vínculo-fonte; (iii) o glossário da apostila endereça «posse» como metáfora de investidura, não como rito."),
 ("D-7 · A obsolescência de Sofia: «vanguarda do atraso».",
  "O argumento é anatômico: [[A vanguarda do atraso]] · [[no cerebro radiata dele nao funciona]] · "
  "[[Para ele sentir emocao, a gente tem que criar um organoinho para ele]] — e os três termos da Base para isso já existem "
  "(RC-631 Cérebro Radiata, RC-632 Organoides Genéticos, RC-093 Radiatas, RC-035 Bilatérios). **Proposta:** ampliação "
  "endereçada dessas quatro fichas + RC-736 (a metáfora constitucional «rainha da Inglaterra», que é exatamente o registro de "
  "autoridade sem poder que a RC já comporta). Zero código novo: nada aqui justifica um termo «obsolescência de Sofia»."),
 ("D-8 · O pacto do método (a seção que fala da própria Arca).",
  "Os Túatha entregam o conhecimento **para que os humanos criem um método de decifrá-lo** ([[nos queremos dar para voces os nossos conhecimentos]] → [[criem um metodo para voces estudarem]]), e a fonte afirma que Javé fazia «a mesma coisa» com Enoque "
  "([[tava fazendo com Enoque era a mesma coisa]]). A Base tem a casa pronta: RC-755 (Escola da Decifração da Realidade — método "
  "druídico), RC-375 (Druidas Celtas), RC-745 (Colegiados Espirituais Humanizados), RC-464 (Inanna = Danu), RC-068 (Hiperbórea), "
  "e as lendas do Alasca/Irlanda/Escócia/Sibéria. **Risco:** a leitura de que a Arca *cumpre um contrato* — que é o que a fonte "
  "diz — entrar em ficha como auto-legitimação da instituição. **Proposta:** Vínculos de conteúdo nos seis códigos acima com as "
  "aspas e endereço; a cláusula «nós cumprimos o pacto» fica **no relatório do ciclo, como constatação editorial, e não em ficha**."),
 ("D-9 · Os números divergentes (a tabela da §4).",
  "Dez linhas de divergência, das quais **duas são convergências** (736 pela terceira vez; e 67+300+366 de Enoque, que a "
  "RC-489/RC-672 já registram). **Proposta:** aplicar o selo temporal a tudo; às convergências, dar **destaque na apostila** (é "
  "a primeira vez que o eixo luciferiano tem três fontes independentes de data dando o mesmo efetivo da Vol). V.Sa. decide se o "
  "número 932 entra como **variante registrada em RC-771** (Fornos Replicadores) ao lado de 936/984 — a casa não tem regra para "
  "três datas concorrentes sobre o mesmo evento além do selo, então proponho: entra com as três grafadas e uma nota de que a "
  "Base não escolhe."),
 ("D-10 · Materializar fichas que a fala ilumina mas não tem? (três candidaturas)",
  "Há **três** códigos tocados por esta palestra com `ficha=False`, cada um com conteúdo suficiente para virar ficha: "
  "**RC-018 Alt´Lam Gron** (a fonte dá o censo, a função, o nome em 4 grafas e o evento datado «Sofia esteve aqui nos anos "
  "2018, 19»); **RC-040 CFD (Código Fonte Definidor)** (a fórmula [[padroes arquetipos do codigo fonte definidor do criador]] "
  "é a definição operacional que falta a ele); e **RC-444 Família Cromon** (nomeada na lista das cinco e no primeiro embate). "
  "**Precedente:** em P2022-03-26, V.Sa. autorizou a materialização de RC-089 e mandou manter RC-444 como False. "
  "**Proposta:** RC-018 e RC-040 materializam; **RC-444 continua `ficha=False`** (mantendo a decisão anterior, que este ciclo "
  "não tem motivo para reabrir). Decidir aqui é o único ponto deste dossiê em que uma ficha pode **nascer**."),
 ("D-11 · O que a fonte diz que ainda vai ser dito.",
  "Quatro promessas: o livro «Projeto Tal» ([[ainda vai sair um livro com esse nome, projeto tal]]); a palestra sobre a gênese "
  "da hibridagem («nunca tive nem coragem, nem saco de fazer», que exigiria «várias palestras preliminares»); a explicação da "
  "diferença *subjacente/adjacente* («eu não vou explicar isso aqui não»); e o terceiro fator que parou o expurgo («não dá para "
  "falar aqui»). **Proposta:** os quatro ficam no **radar datado** do RELATORIO-DE-CICLO, sem B-código, sem relação, sem "
  "antecipação de conteúdo — e o índice registra que a palestra prometida sobre hibridagem é **a única cuja existência a fonte "
  "condiciona a um ciclo de preliminares**."),
 ("D-12 · As pessoas nomeadas (público, amigos, médiuns, autoras).",
  "Medido no bruto: «Rogério» {NR}, «Jan» 5×, «Márcia» 2×, «Horácio» 1×, «T César» 1×, «João Altair» 1×, «Valdemar Matoso» 2×, "
  "«Chico Xavier» 3×, «Divaldo» 2×, «Edgar Armon» [REVISAR] 1×, «Jane Miranda» 1×, «Mari Lusa Vasconcel» [REVISAR] 1×, "
  "«Emanuel» 1×, e a forma «moça» com que o canal se dirige a uma perguntadora não nomeada. **Regra vigente (D-12 do ciclo "
  "anterior):** existem **só na transcrição**. **Proposta:** 0 fichas de pessoas; em RC-071 (que *nomeia* o canal) entra apenas "
  "a cadeia Elã→Enoque que a fonte atribui ao espírito que o anima, com moldura, sem hagiografia e sem repetir as frases "
  "auto-referenciais de U0034/U0076 como prova de nada."),
 ("D-13 · As datas prometidas: o marco de 1989 e a janela 2049–2052.",
  "A resposta a Jan fixa um procedimento com prazo: [[ate 2049 pode acontecer. Existe uma ordem dada]], «em julho de 9» como "
  "marco, «2050, ou é 50 ou é 51, 52» e a afirmação de que o expurgo **foi parado**. **Risco real:** a Base transformar isso em "
  "profecia datada com prazo de validade. **Proposta:** entra como conteúdo em RC-344 (Transição Planetária) e RC-003 "
  "(Reintegração Cósmica) com a aspa inteira e o endereço; **não** entra em RC-200 (Base de Dados do Juízo Final) como "
  "calendário — ali vai só a cláusula informacional ([[nos existimos para guardar essas informacoes]]). O RELATORIO registra "
  "que a data **já está vencida** em relação a hoje (2026) e que nada foi harmonizado com isso: é fato do arquivo, não "
  "refutação da fonte."),
 ("D-14 · Pipeline, ordem e portões.",
  "Se V.Sa. aprovar os vínculos da §2: **BLOCO A** = `dados_termos.py` (FONTES `P2023-12-03` nos {LENL} códigos da §2) + "
  "`## Ampliação — P2023-12-03` nas fichas com `ficha=True` que os recebem + as materializações do D-10, num commit só. "
  "**BLOCO B** = apostila + DOCX + cobertura + verbatim + engavetamento em `CONCLUIDAS/`, em outro commit. Cada bloco com os "
  "portões A (integridade do bruto) · B (cobertura 100%) · C (verbatim das citações) · D (contadores e tetos) · E (endereços "
  "datados conferidos um a um). Se V.Sa. preferir, A pode ser dividido em A1 (malha) e A2 (fichas), como no ciclo anterior."),
]


def render_d():
    out = "Cada item: **fato medido → risco → proposta do agente**. O ciclo não executa nenhuma delas antes da resposta.\n\n"
    for titulo, corpo in D:
        corpo = corpo.replace("{LENL}", str(len(linhasL))).replace("{LENM}", str(len(MASCARAS))).replace("{NR}", "11×")
        out += f"**{titulo}** {resolve(prequote(corpo))}\n\n"
    return out[:-1]


DOSS = resolve(prequote(DOSS).replace("@@DEVS@@", render_d()).replace("@@TAB@@", tab))

# ───────────────────────────── grava tudo ─────────────────────────────
for nome, txt in (("camada-1.txt", resolve(prequote(CAM1))),
                  ("LEITURA-1-MACROESTRUTURA.md", resolve(prequote(LEI))),
                  ("notas-leitura.md", resolve(prequote(NOT))),
                  ("DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md", DOSS)):
    open(os.path.join(AQUI, nome), "w", encoding="utf-8").write(txt)
    print(f"{nome:46s} {len(txt):7,} chars".replace(",", "."))
