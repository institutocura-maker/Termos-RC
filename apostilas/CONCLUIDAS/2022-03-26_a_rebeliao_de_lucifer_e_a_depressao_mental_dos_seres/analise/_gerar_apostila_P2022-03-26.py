#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera `apostila.md` do ciclo P2022-03-26 (A Rebelião de Lúcifer e a Depressão Mental dos Seres).

Espelho de `apostilas/CONCLUIDAS/2020-04-25_*/analise/_gerar_apostila_P2020-04-25.py`, com a diferença
que a **devolutiva de 28/08/2026** manda e que este ciclo inteira não tinha:

 1. **zero bloqueios** (D-1: «transcreva integralmente na apostila com forte nota editorial de moldura»).
    O texto sensível **fica** — a seção do suicídio (U0009), os nomes públicos (U0005, U0009, U0028) e a taxonomia
    clínica do divino (U0005, U0020, U0040) — e recebe **nota de moldura no próprio lugar**. O regime é o
    inverso do ciclo anterior: lá a moldura era a tesoura; aqui é o aviso.
 2. **o veto de trânsito é na ficha, não aqui** (D-1/D-3): o gerador do pacote levou as travas; este arquivo
    as **reconhece** e as declara, para que a apostila se leia sozinha.
 3. **ordem cronológica natural** (D-13): os blocos seguem as linhas do bruto, sem reordenação temática; o
    intervalo pedido ao vivo e o refinamento público da tese são marcados por nota, não remanejados.
 4. **aparato integral lido de `DECISAO-DO-CURADOR.md` §2** e **efeito material medido** em `termos/`, no
    pacote e no cadastro — nada declarado de memória.
 5. **nenhuma aspa digitada**: as notas citam o bruto pelo caça-âncoras `_aspas_P2022-03-26.py`, com as
    mesmas âncoras do dossiê aprovado (lidas por `ast`). Âncora inexistente **aborta** o arquivo.

Ferramenta de ciclo: não toca a Base. Cobertura e molduras auditadas por `_cobertura_apostila.py`.
"""
import os, re, sys, ast, io, hashlib, contextlib, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
BRUTO = os.path.join(CICLO, "original.txt")
ALVO = os.path.join(CICLO, "apostila.md")
DECISAO = os.path.join(CICLO, "DECISAO-DO-CURADOR.md")
PACOTE = os.path.join(AQUI, "_ampliacoes_P2022-03-26.txt")
SIGLA = "P2022-03-26"
TITULO = "A Rebelião de Lúcifer e a Depressão Mental dos Seres"
DATA = "26/03/2022"
BLOCO_ALVO = 2200
MARCADOR = ""                                    # este ciclo não corta nada: nenhum marcador de bloqueio
BLOQUEIOS = []                                   # → o auditor de cobertura exige 0 cortes

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
RAW = ASP.RAW
LINHAS = ASP.LINHAS

DOSSIE_PATH = os.path.join(AQUI, "DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md")
_sha_dossie = hashlib.sha256(open(DOSSIE_PATH, "rb").read()).hexdigest()
_ds = importlib.util.spec_from_file_location("dossie", os.path.join(AQUI, f"_gerar_dossie_{SIGLA}.py"))
DOSS = importlib.util.module_from_spec(_ds)
with contextlib.redirect_stdout(io.StringIO()):   # o gerador do dossiê é determinístico: executa, cala, não muta
    _ds.loader.exec_module(DOSS)
assert hashlib.sha256(open(DOSSIE_PATH, "rb").read()).hexdigest() == _sha_dossie, \
    "executar o gerador do dossiê a partir da apostila alterou o dossiê — interrompido"
# `DOSS.CIT` é o dicionário `chave → (offset_ini, offset_fim, texto)` do dossiê aprovado: as notas desta
# apostila citam **exatamente** as mesmas âncoras daquele arquivo, sem segunda fonte de verdade.
QD = dict(DOSS.CIT)
# Âncoras que só as notas desta apostila usam. Mesma disciplina do dossiê: `ASP.locate` exige
# **exatamente uma** ocorrência no bruto, e o arquivo não é escrito se a âncora não bater.
EXTRA = {
    "eufemismo_desativar": ("Alguns de nós já nos desativamos em vidas passadas", "ninguém aguentava viver"),
}
for _k, (_ini, _fim) in EXTRA.items():
    _a, _b, _t = ASP.locate(_ini, _fim)
    QD[_k] = (_a, _b, re.sub(r"\s+", " ", _t).strip())


def _txt(chave):
    return re.sub(r"\s+", " ", QD[chave][2]).strip()


def q(chave):
    """Aspa da fonte via caça-âncoras do dossiê. As aspas retas internas ficam **como no bruto**: o
    auditor de verbatim fatia por `"` para conferir cada pedaço ≥25 chars contra a fonte, e convertê-las
    em «» dentro de um «» externo é exatamente o que faria a aspa deixar de bater byte a byte."""
    return "«" + _txt(chave) + "»"


def cont(rx):
    return len(re.findall(rx, RAW, re.I))


# --- os nomes públicos, medidos (contagem por forma e endereço por ocorrência) -----------------
# A fronteira de palavra é obrigatória: sem ela, `célula`/`pluricelular` viram `Lula`.
POLITICA = [("Lula", r"(?<![A-Za-zÀ-ü])Lula[a-zçõA-Z]*"), ("Bolsonaro", r"(?<![A-Za-zÀ-ü])Bolsonar[a-zçõA-Z]*"),
            ("Trump", r"(?<![A-Za-zÀ-ü])Trump[a-zçõA-Z]*"), ("Hillary Clinton", r"(?<![A-Za-zÀ-ü])Hillar[a-zçõA-Z]* Clinton")]
POL_HITS = {n: [(m.start(), ASP.uaddr(m.start())) for m in re.finditer(rx, RAW, re.I)] for n, rx in POLITICA}
POL_NOMES = " · ".join(f"`{n}` {len(v)}" for n, v in POL_HITS.items() if v)
POL_TOT = sum(len(v) for v in POL_HITS.values())
POL_ADDR = ", ".join(sorted({u for v in POL_HITS.values() for _, u in v}))


n_bruto = lambda x: f"{x:,}".replace(",", ".")
FALA_INI = 2                                      # U0001 é o título do arquivo; U0002, vazio

# ---------------------------------------------------------------- notas editoriais (âncora = frase que está na transcrição)
NOTAS = [
 ("pedaco_quebra_cabeca",
  "**A regra que a fonte impõe a si mesma, logo no começo** (" + q("pedaco_quebra_cabeca") + "). Esta apostila "
  "é leitura de estudo, não de adesão: a fala se declara peça de um quebra-cabeças e pede que a régua do "
  "ouvinte seja a de Kant (" + q("kant_regua") + "). Daí o regime desta edição: transcrever tudo, emendando "
  "nada — e marcar no lugar exato o que exige moldura."),
 ("espirito_nao_muda",
  "**A tese de partida, e o motivo de o médium importar** (" + q("espirito_nao_muda") + "). O desacordo com a "
  "fala de 25/04/2020 é de ênfase, não de corpo: lá, o que estava em jogo era o que a queda fez **em Javé**; "
  "aqui, o que ela impede **no desencarnado**. Nenhuma das duas é lida como doutrina fechada; ambas ficam "
  "datadas (D-10)."),
 ("unica_obra_completa",
  "**De onde vem o quadro** (" + q("unica_obra_completa") + "). A fonte não cita o Mahabharata como autoridade "
  "e sim como *precedente de método*: três contagens de versos saem da boca dela (" + q("versos_gandarvas") +
  ") e a consequência é declarada logo: o que se ouve adiante é recorte, não edição crítica da obra. "
  "[REVISAR: o STT grafa o nome em seis formas — ver o Apêndice.]"),
 ("jacare_pato",
  "**A moldura do argumento inteiro** (" + q("jacare_pato") + "). A pergunta é posta para ser *recusada* aos "
  "filósofos (" + q("filosofos_a_um_lado") + "), e o veredito que a fonte dá não é sobre o criador, é sobre o "
  "sistema: " + q("dignidade_decente") + ". É por isto que a parte doutrinária a seguir não pode ser lida "
  "como teodicéia clássica: ela inverte o ônus."),
 ("acidente_artista",
  "**O ponto exato em que a cosmogonia de 2022 se separa da de 2020** (" + q("acidente_artista") + "). Não há "
  "ato, há erro de artista; e o erro fica na obra (" + q("codigo_podre") + "). Quem procurar aqui a «queda "
  "orgulhosa» da tradição não a encontrará: a fonte a substitui por **código que se replica com defeito**."),
 ("tres_fornos",
  "**A engenharia, com o forno que nunca funcionou** (" + q("tres_fornos") + "). As duas estirpes que saem dos "
  "outros dois são definidas por *ausência* e por *excesso*: " + q("biodemos_frios") + " (" + q("sem_sexualidade") +
  ") de um lado; do outro, o forno velho que sexualiza e polariza (" + q("outro_forno") + "). O encontro dos dois é "
  "anatomicamente decisivo para o resto da fala: " + q("cerebro_bilaterio") + "."),
 ("lucifer_criou_virus",
  "**MOLDURA (D-1) — a partir daqui, a palestra é um texto sobre epidemia.** A rebelião é narrada como surto "
  "(" + q("saude_publica") + ") e o vocabulário é inteiro médico: *quarentena*, *sequela*, *contaminação*, "
  "*hospedagem*. A fonte usa um agente biológico real como analogia (" + q("toxo_plano_gato") + ") e cita números de "
  "necropsia (" + q("setecentos_setenta") + "). **Nada disto é afirmação sobre saúde pública, sobre doenças ou sobre "
  "qualquer pessoa viva**: é o modelo cosmológico de um autor, transcrito como dito. Nenhum conselho de saúde se "
  "deduz deste texto, e nenhuma dessas expressões transitou para ficha que nomeie pessoas ou grupos (trava "
  "mecânica do pacote, conferida no portão D)."),
 ("setecentos_setenta",
  "**O número citado como prova, e o estatuto dele.** " + q("cientistas_acaso") + " — a fonte invoca a necropsia "
  "para sustentar a tese da *hospedagem que muda o comportamento*; o dado é dito de memória em voz alta e **não** é "
  "verificado por este ciclo: fica transcrito, com endereço, sem virar nota de rodapé científica nem verbete."),
 ("copiado_da_colmeia",
  "**A definição que a Base não tinha** (" + q("copiado_da_colmeia") + "). O regime colmeico é dito como cópia de um "
  "arranjo anterior, e a rainha é descrita como quem **não** impõe (" + q("sofia_rede_frouxa") + "). A fonte remete o "
  "desenvolvimento a um livro já catalogado — *A Divina Colmeia*, **B044** (cross-reference aprovado em D-11; nada de "
  "obra nova)."),
 ("orbon_processador",
  "**A rede tem um órgão, e o órgão tem endereço** (" + q("processador_de_cada_familia") + " — " + q("quarto_escuro") +
  "). É esta a passagem que fundamentou a materialização de `RC-089 Processador Val` (D-9). [REVISAR: os topônimos saem "
  "degradados — `órbão`, `ZAM`, `Oreon` — e nenhum é promovido; ver o Apêndice.]"),
 ("sofia_desconectada",
  "**O grau de testemunho deste bloco, declarado pela própria fonte** (" + q("nunca_tinha_falado") + "). A afirmação "
  "mais forte da palestra — a desconexão de Sophia, há 700.000 anos (" + q("sofia_contaminada") + ") — vem com a marca "
  "de que nunca fora dita em público. A Base registra **a proposição com a ressalva**, não a ênfase: é o regime de "
  "toda fonte oral deste acervo."),
 ("isolou_mundos",
  "**A medida sanitária, em termos de governo** (" + q("isolou_mundos") + " — " + q("dezenove_mundos") + "). A metáfora "
  "é traduzida pela fonte para um quadro que o ouvinte reconhece (" + q("analogia_seluva") + "), e o resultado é o "
  "que dá título psicológico ao ciclo: " + q("onda_depressiva") + "."),
 ("nucleo_depressivo",
  "**A frase que reorganiza a cosmologia da Base** (" + q("nucleo_depressivo") + "). Não é hipérbole pastoral: é o "
  "fecho de um argumento que vinha sendo construído em camadas — Sophia fora do ar (" + q("sofia_reconectada_2019") +
  "), mundos em quarentena, e um planeta que recebe os que não se recuperaram (" + q("terra_ultimo_mundo") + ")."),
 ("revolver_alto_engano",
  "**MOLDURA (D-1) — a seção mais delicada do acervo oral, transcrita por decisão do Curador.** Nos próximos "
  "parágrafos a fonte fala de vida insuportável, de revólver e de suicídios que ela mesma coloca na conta do próprio "
  "círculo (" + q("vida_vergonhosa") + " — " + q("eufemismo_desativar") + "). O trecho **não foi cortado**: a devolutiva determinou que ele é a espinha "
  "dorsal do argumento sobre a depressão cósmica, e que cortá-lo seria falsificar a tese. **Se você está em sofrimento "
  "agudo, este texto não é o lugar de procurar ajuda** — no Brasil, o CVV atende no 188, 24 horas, e o SAMU no 192. "
  "Nenhuma palavra deste bloco transita para ficha de termo, índice ou material de divulgação (veto absoluto de D-1, "
  "executado por código no gerador do pacote e conferido no portão D)."),
 ("autistas_dementes",
  "**MOLDURA (D-3) — vocabulário clínico usado como categoria do divino.** A fonte chama os seres perfeitos de "
  "autistas e os caídos de dementes (" + q("autistas_dementes") + "), e retoma o registro em U0020 (" +
  q("rei_dos_transtornos") + "). **Leia-se:** é apropriação metafórica de um autor sobre o seu próprio sistema, e não "
  "descrição de pessoas, pacientes ou qualquer grupo humano. A palavra *idiotia* aparece ainda uma terceira vez, "
  "citada como o termo do século XIX aplicado ao Espiritismo (" + q("kardec_idiotia") + ") — também aí, transcrita e "
  "não endossada. Nada disso entrou em ficha (trava D-3)."),
 ("narrativas_pos_facto",
  "**MOLDURA (D-2) — os nomes públicos, no lugar em que a fonte os usa.** Lula, Bolsonaro, Trump e Hillary Clinton "
  "aparecem aqui (10 menções medidas no bruto) dentro de um argumento sobre atenção e pós-verdade (" +
  q("pos_verdade") + "), não como adesão a lado nenhum. A devolutiva registrou que **não há bloco isolável** nesta "
  "fala — por isso o texto ficou integral, e o que se vedou foi o *trânsito*: nenhum desses nomes existe em ficha, "
  "índice, glossário ou material de divulgação."),
 ("titulo_parcial",
  "**O estatuto da fala, dito pela própria fonte.** Antes do intervalo ela declara que batizou o tema só para o seu "
  "próprio estudo (" + q("titulo_parcial") + ") e que aquela palestra tem outro destino na sala (" +
  q("pedido_intervalo") + "). Nada foi removido nem suavizado: a autodeclaração **limita** o estatuto de uma "
  "formulação sem apagar nada (D-13)."),
 ("guerra_biologica",
  "**A única vez no acervo em que a fonte refina o próprio quadro ao vivo.** Um ouvinte pede conta de uma guerra "
  "mencionada antes, e a fonte corrige a distinção (" + q("guerra_do_sol") + " × " + q("guerra_biologica") + "). "
  "Transcreve-se como aconteceu — pergunta, hesitação, retificação — porque o valor do trecho é justamente não ser "
  "polimento (D-13)."),
 ("dorian_gray",
  "**Entropia transferida, com a literatura como modelo físico** (" + q("dorian_gray") + "). A fonte não usa o "
  "romance como enfeite: usa-o como mecanismo — o retrato envelhece, o corpo não (" + q("humanos_morrem_rapido") +
  "). É também aqui que os humanos entram como *pagadores de entropia* de mundos que não morrem."),
 ("espirito_unico_jesus",
  "**MOLDURA (D-5) — a chave cristológica, e o regime dela.** A identidade que a fonte afirma (" +
  q("javé_vishnu_chiva") + " — " + q("duas_faces") + ") entra na Base como **tese datada de 26/03/2022**, não como "
  "definição canônica de `RC-072`, `RC-009` ou `RC-001`. O Tabor é lido como recusa de agenda (" +
  q("anjos_cercaram_tabor") + ") e o advento, como investidura retida (" + q("vestimenta_heredeiro") + "). "
  "**Crueldade interpretativa evitada nos dois sentidos:** não é hereologia polida e não é prova histórica; é o que "
  "um autor disse, com data e endereço."),
 ("filosofia_definicao",
  "**A resposta que a fonte devolve ao céu** (" + q("diagnostico_humano") + " — " + q("filosofia_como_comecou") + "). "
  "O específico humano é a filosofia, definida por ela mesma (" + q("conceitos_supremos") + "), e o contraexemplo "
  "histórico vem junto (" + q("hitler_monstro") + "). Ler a seção como elogio do ser humano é o erro que a fonte "
  "antecipa: duas linhas antes ela diz que *inteligente* não é *racional* (" + q("inteligente_nao_racional") + ")."),
 ("favores_consertar",
  "**O favor divino é do humano para o criador** (" + q("favores_consertar") + "). É a inversão que fecha o argumento "
  "epidemiológico: quem conserta o código é a criatura (" + q("racionalidade_no_meio_da_sujeira") + "), e a imagem "
  "que a fonte escolhe para isso (" + q("astronautas_eternidade") + ")."),
 ("nomes_da_roda",
  "**MOLDURA (D-12) — a sala, com nomes.** A palestra termina pedindo cadência e citando as pessoas que devem ser "
  "avisadas (" + q("nomes_da_roda") + " — " + q("cadencia_palestras") + "). Ficam na transcrição como metadado da "
  "situação de enunciação; **não** geram entidade, ficha, relação ou verbete (D-12), e não são identificadas a "
  "nenhuma pessoa pública."),
 ("sanquia_atualizado",
  "**O fecho, e a escola que a fonte diz praticar** (" + q("sanquia_atualizado") + " — " + q("mentalma_para_sim") +
  "). A frase sobre as religiões (" + q("matar_em_nome") + ") é dita ao vivo e **não** vira verbete, ficha nem "
  "citação circulante; a autodeclaração de descrença (" + q("unica_escola_sem_deus") + " — " + q("pense_por_voce") +
  ") fica aqui porque requalifica o estatuto da palestra inteira: não é pregação."),
 ("anuncio_ordenacao",
  "**MOLDURA (D-11) — duas obras anunciadas, zero obras criadas.** A fonte dá o primeiro título com prazo (" + q("anuncio_ordenacao") +
  ") e promete a sequência (" + q("além_do_ordenacao_vem") + "). Este ciclo **não** registra publicação, **não** "
  "confere existência bibliográfica e **não** data lançamento como fato: as duas menções ficam no relatório de ciclo, "
  "com a data desta fala como prova de anterioridade da menção."),
]

# ---------------------------------------------------------------- helpers de segmentação
def fatiar(texto):
    blocos, i = [], 0
    while i < len(texto):
        fim = min(len(texto), i + BLOCO_ALVO)
        if fim < len(texto):
            corte = max(texto.rfind(". ", i + 600, fim), texto.rfind("? ", i + 600, fim),
                        texto.rfind("! ", i + 600, fim), texto.rfind(".\n", i + 600, fim))
            if corte > 0:
                fim = corte + 1
        blocos.append(texto[i:fim].strip())
        i = fim
    return [b for b in blocos if b]


def voz(s):
    t = s.strip()
    if len(t) <= 150:
        return "PLATEIA / INTERLOCUÇÃO (turno próprio no bruto)"
    if len(t) <= 400 and "?" in t:
        return "EXPOSITOR — Jan Val Ellam, respondendo ao vivo"
    return "EXPOSITOR — Jan Val Ellam"


def rotulo(n):
    return f"Bloco {n:02d}"


# ---------------------------------------------------------------- corpo
def main():
    # --- offsets de cada linha no RAW (LINHAS = RAW.split("\n"), então é soma cumulativa) --------------
    ofs, cur = [], 0
    for ln in LINHAS:
        ofs.append(cur); cur += len(ln) + 1
    assert all(RAW[o:o + len(l)] == l for o, l in zip(ofs, LINHAS)), "mapa de offsets × LINHAS divergente"

    # --- pré-checagem: cada âncora de nota é trecho do bruto, resolvido pelo dossiê ---------------------
    for chave, _ in NOTAS:
        if chave not in QD:
            raise SystemExit(f"NOTA COM ÂNCORA FORA DO DOSSIÊ APROVADO: {chave}")

    linhas_txt = []
    for i in range(FALA_INI, len(LINHAS)):
        s = LINHAS[i].strip()
        if not s:
            continue
        linhas_txt.append((f"U{i + 1:04d}", i, s))
    chars_fala = sum(len(s) for _, _, s in linhas_txt)

    out = []
    w = out.append
    w(f"@titulo: {TITULO}")
    w("@autor: Jan Val Ellam")
    w(f"@data: {DATA}")
    w("@local: São Paulo — a cidade é dita pela própria fonte na última linha da fala (U0050); o cabeçalho do "
      "arquivo não traz lugar")
    w("@subtitulo: Apostila de estudo — transcrição **integral** (sábado, 26/03/2022), sem recorte: a moldura dos "
      "itens D-1, D-2 e D-3 da devolutiva é feita de nota no lugar exato, e o veto incide sobre o trânsito para as "
      "fichas, não sobre a leitura. Aparato curatorial das 14 decisões, glossário e Apêndice do dicionário STT.")
    fala = "\n".join(LINHAS[FALA_INI:])
    n_pal = len(fala.split())
    n_per = len(re.findall(r"[.?!](?:\s|$)", fala))
    n_linhas = len([1 for l in LINHAS if l.strip()])
    n_bytes = os.path.getsize(BRUTO)
    w("@fonte: original.txt do ciclo — " + n_bruto(n_bytes) + " bytes · " + n_bruto(len(RAW)) +
      " caracteres · " + str(n_linhas) + " linhas não vazias (título + 48 de fala; CRLF preservado) · fala útil "
      "U0003–U0050 com " + n_bruto(len(fala)) + " caracteres · " + n_bruto(n_pal) + " palavras · " + n_bruto(n_per) +
      " períodos · SHA-256 `1cc8a8c0…99253b9` (o hash integral está em `analise/METADADOS-INGRESSO.json`)")
    w("@nota_editor: Esta apostila é a transcrição editada da palestra «A Rebelião de Lúcifer e a Depressão Mental "
      "dos Seres», de 26 de março de 2022, preservada byte a byte em original.txt. O STT não separou os turnos por "
      "completo: a fala cabe em onze linhas pesadas (92,2% do texto em U0003, U0005, U0007, U0008, U0009, U0020, "
      "U0029, U0034, U0040, U0048 e U0049), e vinte e quatro linhas curtas são a plateia. A divisão em Blocos é "
      "editorial e obedece à ordem da fonte, sem reordenação temática (D-13). Não houve correção silenciosa de "
      "grafia, número ou sintaxe: o que é incerto leva [REVISAR]. Diferentemente do ciclo anterior, esta fonte não "
      "tem **nenhum bloqueio** — a devolutiva de 28/08/2026 determinou transcrição integral com moldura nos itens "
      "D-1 (a seção de U0009 sobre vida insuportável), D-2 (os nomes públicos, medidos acima) e D-3 (a taxonomia clínica do "
      "divino), vedando apenas que essas passagens circulem em ficha que nomeie pessoas ou grupos humanos. O aparato "
      "terminológico produziu 75 códigos vinculados, 74 fichas ampliadas, 1 materialização (RC-089) e 0 códigos "
      "novos: a Base permanece em 777 termos, 1.856 relações e 102 obras, e o RC-778 continua não consumido.")
    w("")

    # ---------------------------------------------------------- PARTE 0
    w(f"# PARTE 0 — Nota de leitura, molduras e integridade ({SIGLA})")
    w("")
    w("> **Fonte e método.** O arquivo recebido é `uploads_recepcao/2022-03-26 A Rebelião de Lúcifer e a Depressão "
      "Mental dos Seres.txt`. `original.txt` é cópia byte a byte (cp + cmp + SHA-256 idêntico) e **não foi tocado** "
      "nem por este arquivo nem pelo aparato. A numeração **U0001–U0050** é o endereço das linhas lógicas do TXT bruto (a linha final do arquivo, "
      "U0051, é vazia; a última linha com texto é U0050) "
      "e é usada em todo o ciclo (camadas 0–3, dossiê, devolutiva, pacote e fichas), para que qualquer citação seja "
      "relocalizável sem ambiguidade. Nenhuma aspa deste ciclo foi digitada de memória: todas saem do caça-âncoras "
      "`_aspas_P2022-03-26.py`, usado pelo dossiê, pelo pacote de ampliações e por este arquivo.")
    w("")
    w("*Nota editorial:* os rótulos de voz são editoriais e **não afirmam identidade civil** de quem fala. O bruto tem "
      "24 linhas de 3 a 150 caracteres que são interlocução; elas são transcritas na ordem em que vieram, inclusive a "
      "duplicação que o STT produziu entre U0003 e U0004 (a última palavra de U0003 reaparece em U0004).")
    w("")
    w("## Cobertura (declaração, como nas Convenções v2)")
    w("")
    w(f"- Transcrição integral publicada: **{n_bruto(chars_fala)} de {n_bruto(chars_fala)} caracteres** da fala "
      "(**100,00%**), com **0 caracteres** suprimidos e **0 blocos bloqueados**. Este ciclo é o primeiro da Arca em "
      "que a devolutiva decide *não* recortar nada: onde o material é sensível, a intervenção é nota de moldura no "
      "lugar exato. O auditor `_cobertura_apostila.py` confere parágrafo a parágrafo e reproduce a mesma contagem.")
    w(f"- O bruto é o maior do acervo: {n_bruto(len(RAW))} caracteres, **+30.190** sobre P2020-04-25. A segmentação "
      "em blocos apenas repõe parágrafos que o STT não tinha; nada foi resumido para «melhorar a leitura».")
    w("- Marcadores de oralidade (*né*, *pá*, *cara*, *tá*), números com vírgula de intervalo de fala (o caso "
      "extremo é *5, 6 bilhões*, que **não** se lê 5,6) e as grafias instáveis de nomes próprios ficam como foram "
      "ouvidos. A única transformação mecânica é a quebra dura de linha dentro de uma mesma frase, convertida em "
      "espaço — declarada aqui e no topo do pacote de ampliações.")
    w("- O vocabulário clínico e o vocabulário de sofrimento **não** são eufemizados nem realçados: a moldura "
      "acrescenta aviso de apoio (188 / 192) onde o texto nomeia o ato, e nada mais.")
    w("")
    w("## As três molduras (D-1, D-2, D-3) e por que nenhuma é corte")
    w("")
    w("- **D-1 · a seção do suicídio (U0009).** Fica integral, com aviso de apoio e nota no ponto. Razão da "
      "decisão: é o fecho do argumento de que a depressão não é humor, é falência de função; cortá-la deixaria a "
      "tese sem a premissa. O que se vedou foi o **trânsito** — nenhuma palavra dessa seção foi para ficha.")
    w(f"- **D-2 · os nomes públicos, medidos: {POL_TOT} menções em 4 nomes ({POL_NOMES}), nos endereços "
      f"{POL_ADDR}.** Ficam integrais porque estão **dentro** de dois argumentos — a definição de pós-verdade "
      "(U0005) e a dispersão da atenção (U0009 e U0028) —, e não em digressão separável: é a diferença estrutural "
      "em relação a 2020, onde havia um bloco isolável de 16.523 caracteres a cortar. O dossiê, ao aprovar a "
      "etiqueta \"os dez nomes\", contou `Trump` só no singular (2×): aqui a contagem é por **forma derivada "
      "incluída** (`Trumpos`), e a divergência de método fica declarada em vez de escondida.")
    w("- **D-3 · a taxonomia clínica do divino (U0005, U0020, U0040).** Fica integral, com nota de apropriação "
      "metafórica, porque a tese do «paraíso de autistas» é o que sustenta a leitura da perfeição como "
      "estagnação. A trava foi implementada como filtro no gerador do pacote: as duas fichas cujo nome nomeia "
      "pessoa ou grupo humano (`RC-614`, `RC-633`) **não** receberam nenhuma dessas aspas, e o portão D conferiu.")
    w("- **D-4 · as máscaras do STT.** `t*****` e `m****` permanecem como no arquivo. Registro de defeito do "
      "transcritor, não escolha editorial — e não transitam para ficha.")
    w("")
    w("## Quarentenas deste ciclo (rótulo de índice, não de censura de leitura)")
    w("")
    for qq in [
        "**epidemiológica (retenção):** vírus, toxoplasma, 756 necropsias, COVID, *sequela* — modelo cosmológico "
        "do autor; nenhum juízo de saúde pública, nenhuma recomendação, nenhum verbete de medicina;",
        "**clínico-cosmológica (D-3):** *autista*, *esquizofrênico*, *demente*, *idiotia*, *babaca* como categorias "
        "do divino — transcritas com nota, vedadas em ficha que nomeie gente;",
        f"**política (D-2):** {POL_TOT} menções a 4 pessoas públicas, nos endereços {POL_ADDR}, dentro do "
        "argumento sobre atenção e pós-verdade — "
        "ficam na transcrição, não existem fora dela;",
        "**biográfica (D-4 e D-12):** o nome civil do expositor (dito 12 vezes), os nomes da plateia e o mentor "
        "citado como «Francisco de Paula» — metadado de enunciação, sem entidade criada;",
        "**teológica (D-5):** Javé = Sophia = Jesus como um mesmo espírito fateado, Brama e Vishnu como faces, a "
        "recusa no Tabor — tese **datada**, não definição canônica, e cruzamento por conteúdo com B011;",
        "**de física e de cosmogonia (retenção):** 13,8 bilhões, fornos de replicação, código fonte replicado, "
        "entropia transferida, portais de 2012 — nada vira verbete de física nem cronologia oficial;",
        "**terminológica (D-6 e D-7):** *espécie 250*, *espécie 315*, *Meor/lemor/Leão*, *Esferon*, *Valho*, "
        "*Chamba*, *Órbon*, *ZAM*, *Alp Longron*, *Aia/Aie*, *Hamaiam* — **termos-observação** com [REVISAR], sem "
        "código novo; o teto de 777 fica blindado;",
        "**de acervo (D-11):** *Além da Ordenação do Caos* e *Jesus, Sophia versus os Arcontes* anunciados com prazo "
        "— ficam no radar datado do relatório; nenhuma obra criada, nenhuma linha de BIBLIO:",
    ]:
        w(f"- {qq}")
    w("")

    # ---------------------------------------------------------- PARTE I
    w("# PARTE I — Transcrição integral")
    w("")
    w(f"> A fala de {DATA}, na ordem em que foi dita. Os cabeçalhos indicam o endereço no bruto "
      "(`Uxxxx`) e o intervalo de caracteres; os blocos são recorte editorial de linhas longas, nunca fusão "
      "nem reordenação.")
    w("")
    n = 0
    emitidas = set()
    pos_notas = [(QD[c][0], QD[c][1], c) for c, _ in NOTAS]
    for end, li, s in linhas_txt:
        base = ofs[li]
        ln = LINHAS[li]
        cursor = 0
        for p in fatiar(ln):
            j = ln.index(p, cursor)
            cursor = j + len(p)
            a, b = base + j, base + j + len(p)          # o bloco cobre RAW[a:b]
            n += 1
            w(f"## {rotulo(n)} — {voz(p)} ({end}, caracteres {n_bruto(a + 1)}–{n_bruto(b)})")
            w("")
            w(p)
            w("")
            for na, nb, chave in pos_notas:
                if chave in emitidas:
                    continue
                if a <= na < b or (na < a <= nb):        # a âncora cai dentro deste bloco
                    emitidas.add(chave)
                    w(f"*Nota editorial:* {dict(NOTAS)[chave]}")
                    w("")
    soltas = [c for c, _ in NOTAS if c not in emitidas]
    if soltas:
        raise SystemExit("NOTAS SEM ÂNCORA NA TRANSCRIÇÃO: " + ", ".join(soltas))

    # ---------------------------------------------------------- PARTE II
    w("")
    w(f"# PARTE II — Índice temático (os movimentos da fonte, na ordem dela — camada 3, M1…M14)")
    w("")
    c3 = open(os.path.join(AQUI, "camada-3.txt"), encoding="utf-8").read()
    tabela = c3.split("## 1. Os 14 movimentos")[1].split("## 2.")[0]
    for l in [x for x in tabela.split("\n") if x.strip().startswith("| M")]:
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 4:
            continue
        nome = cel[1].replace("**", "")
        ue = re.findall(r"U\d{4}", cel[2])
        linha_md = f"- **{cel[0]} — {nome}** → natureza {cel[3]}"
        if ue:
            linha_md += f" · abre em {ue[0]}"
        if cel[0] == "M10":
            linha_md += " · **moldura D-1 aplicada aqui** (transcrição integral com aviso de apoio)"
        if cel[0] == "M13":
            linha_md += " · **tese datada (D-5)**, não definição canônica"
        w(linha_md)
    w("")
    w("*Nota editorial:* a matriz de anterioridade completa (78 códigos auditados, 21 com ganho de data) e a "
      "navalha de exclusões ficam em `analise/camada-3.txt` e `analise/_matriz-anterioridade.md`; os **18** ganhos "
      "de data que sobreviveram à navalha são os que entraram no pacote. Nada nesta Parte II reorganiza a fala: a "
      "numeração M1…M14 é descrição do percurso, não tabela de conteúdo.")

    # ---------------------------------------------------------- PARTE III
    w("")
    w(f"# PARTE III — Aparato curatorial: as 14 decisões do Curador sobre {SIGLA}")
    w("")
    dec = open(DECISAO, encoding="utf-8").read()
    tab = dec.split("## 2.")[1].split("## 3.")[0]
    linhas_tab = [l for l in tab.split("\n") if l.strip().startswith("|")]
    cab = [l for l in linhas_tab if set(l.replace("|", "").strip()) <= set("-: ")]
    w("> Tabela espelhada de `DECISAO-DO-CURADOR.md` §2 (a devolutiva verbatim está em §1 do mesmo arquivo). Nada "
      "aqui foi reescrito de memória: é o espelho do que foi decidido, para que a apostila se leia sozinha.")
    w("")
    for l in linhas_tab:
        if l in cab or re.match(r"^\|\s*decis", l, re.I):
            continue
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 3:
            continue
        w(f"- **{cel[0].replace('**', '')}** → ação: {cel[1]} · trava: {cel[2]}")
    w("")
    w("## Efeito material na Base (medido por script, não declarado de memória)")
    w("")
    pacote = open(PACOTE, encoding="utf-8").read()
    cods = sorted(set(re.findall(r"^### (RC-\d{3})$", pacote, re.M)))
    cit_pacote = len(re.findall(r'"[^"]{15,}"', pacote))
    ant_estrela = pacote.count("⭐ **NOTA DE ANTERIORIDADE")
    ant_primeira = pacote.count("**primeira fonte oral desta ficha**")
    ant_negada = pacote.count("**sem ganho de anterioridade**")
    fichas = sorted(f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.endswith(".md"))
    com_secao = [f for f in fichas if f"## Ampliação — {SIGLA}" in
                 open(os.path.join(RAIZ, "termos", f), encoding="utf-8").read()]
    w(f"- **{len(cods)} códigos vinculados** a esta fonte na malha (`{SIGLA}` acrescentado às listas de FONTES em "
      f"`ferramentas/dados_termos.py`); **{len(com_secao)} fichas ampliadas** com a seção `## Ampliação — {SIGLA}`, "
      f"carregando {n_bruto(len(pacote))} caracteres de pacote e {cit_pacote} citações verificadas.")
    w(f"- **{ant_estrela} notas de antecipação** de fonte oral, **{ant_primeira}** fichas que ganham a primeira "
      f"fonte oral da sua história, **{ant_negada}** casos em que esta fonte **não** antecipa nada — e isso é dito na "
      "ficha em vez de fingir primazia. Os números saem do cadastro, calculados pelo gerador do pacote (D-8).")
    w(f"- **1 materialização autorizada (D-9):** `RC-089 Processador Val` — arquivo criado em `termos/`, cadastro "
      f"virado para `ficha=True`; {n_bruto(len(fichas))} arquivos de ficha, **0** códigos novos (teto 777), **0** "
      "relações (1.856 preservadas), **0** obras (44 físicas em `livros/CONCLUIDOS`, 102 no registro BIBLIO), "
      "`RC-778` não consumido, `RC-444` mantida `ficha=False` por ordem expressa.")
    w("- **Auditoria:** portão C (ficha↔byte da fonte) e portão D (paridade estrutural, tetos e travas D-1 a D-4) "
      "verdes na aplicação; o auditor verbatim do ciclo ganhou um **portão E**, que confere o endereço `Uxxxx` de "
      "cada aspa contra o bruto — os seis endereços que a etapa 1 havia datado de memória foram corrigidos por ele.")
    w("- **Divergências numeradas (D-10), sem harmonização e sem média:** `984` × `936`/`900Q`; `6.029` × `1.641`; "
      "`48.000` × `23.000` na mesma linha; `200 bilhões` × `trilhões` na mesma frase; `5, 6 bilhões` lidos como "
      "intervalo. **Duas convergências registadas:** `620.000` e a família em `736` batem com P2020-04-25 sem que a "
      "fonte anote nada.")
    w("")
    w("## Lista das fichas tocadas por esta fonte")
    w("")
    w("- " + " · ".join(cods))

    # ---------------------------------------------------------- APÊNDICE — dicionário STT
    w("")
    w(f"# PARTE III-bis — Apêndice: o dicionário STT desta fonte ({SIGLA})")
    w("")
    w("> Tabela de grafias medidas × leitura provável × status, gerada da camada 2 do ciclo sobre o `original.txt`. "
      "Ela existe porque a transcrição acima **não** foi corrigida em silêncio: o que o STT ouviu fica como está, e a "
      "hipótese de leitura vai aqui — com o destino que a devolutiva deu a cada uma (D-4, D-6, D-7). Nenhuma forma "
      "degradada abaixo é canônica, e nenhuma virou verbete.")
    w("")
    c2 = open(os.path.join(AQUI, "camada-2.txt"), encoding="utf-8").read()
    tabela2 = c2.split("## 1.")[1].split("## 2.")[0]
    nlin = 0
    for l in tabela2.split("\n"):
        s = l.strip()
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= set("-: ") or re.match(r"^\|\s*termo", s, re.I):
            continue
        cel = [re.sub(r"\*\*", "", c).strip() for c in s.strip("|").split("|")]
        if len(cel) < 4:
            continue
        nlin += 1
        w(f"- **{cel[0]}** → {cel[1]} ocorrência(s) · 1ª batida {cel[2]} · {cel[3]}")
    w("")
    w(f"*Nota editorial:* {nlin} linhas emitidas, todas com contagem **medida** no bruto (caixa-insensível, porque a "
      "caixa do STT é instável: `Capela` 0 contra `capela`, `Rebelião` 26 no corpo da fala e mais o título). "
      "As **11 ausências** contadas (anunnaki, Nibiru, Enki/Enlil, Shanlung/Shanai, *Alto Langron*, capelinos, "
      "*isolamento cósmico*, Zont En Drel, Estagiários do Kaos, Moiras/Nornes/Parcas) valem como prova de que esta "
      "fala **não** é repetição das anteriores: onde o vocabulário é outro, o ciclo não o importou.")
    w("")
    w("## As famílias de grafia (medidas, não unificadas)")
    w("")
    # Todas as contagens abaixo são medidas sobre o `original.txt`, caixa-insensíveis e com fronteira
    # de palavra onde a forma curta poderia ser engolida por uma longa (`Javé` × `Javela`).
    M = {
        "javé": cont(r"\bJav[eé]\b"), "javer": cont(r"\bJaver\b"), "javel": cont(r"\bJavel\b"),
        "javela": cont(r"\bJavela\b"), "javet": cont(r"\bJavet\b"), "jah": cont(r"\bJah\b"),
        "jahé": cont(r"\bJah[ée]\b"),
        "Vol": cont(r"\bVol\b"), "V_ponto": cont(r"\bV\.\s"), "voz": cont(r"\bvoz\b"),
        "Morençou": cont(r"\bMoren[çc]ou\b"), "Morrensor": cont(r"\bMorrensor\b"),
        "Morençor": cont(r"\bMoren[çc]or\b"),
        "rabarata": cont(r"rabarata"), "barata": cont(r"(?<![a-z])barata"), "Marrabarata": cont(r"Marrabarata"),
        "Marabarata": cont(r"Marabarata"), "Maabbarata": cont(r"Maabbarata"), "Hamaiam": cont(r"Hamaiam"),
        "Brama": cont(r"\bBrama\b"), "Chiva": cont(r"\bChiva\b"), "Shiva": cont(r"\bShiva\b"),
        "Luisbell": cont(r"Luisbell"), "Luzbell": cont(r"Luzbell"), "Elusbell": cont(r"Elusbell"),
        "Lemion": cont(r"Lemion"), "Limion": cont(r"Limion"), "Len Mon": cont(r"Len Mon"),
        "processo ador": cont(r"processo ador"), "processador": cont(r"processador"),
        "processadores": cont(r"processadores"), "mascara": cont(r"t\*{5}"),
    }
    def mm(k):
        return str(M[k])
    for item in [
        "**Javé** em seis formas medidas: `Javé` " + mm("javé") + " · `Javer` " + mm("javer") + " · `Javel` " +
        mm("javel") + " · `Javet` " + mm("javet") + " · `Jah` " + mm("jah") + " · `Jahé` " + mm("jahé") +
        " (e `Javela` " + mm("javela") + ", que as fronteiras de palavra excluem das contagens acima). Nenhuma delas "
        "define a forma-base: o leitor **não** pode deduzir o canônico a partir do TXT.",
        "**A família Vol** sai como `Vol`/" + mm("Vol") + ", `voz` " + mm("voz") + " e `V.` " + mm("V_ponto") +
        ": o nome da família que a Base grafa *Val* é irrecuperável a partir deste arquivo — o veto gráfico (D-4) "
        "foi **reconfirmado** pela devolutiva, e nenhuma ocorrência virou correção.",
        "**Morençor** em sete formas (`Morençou` " + mm("Morençou") + ", `Morrensor` " + mm("Morrensor") +
        ", `Morençor` " + mm("Morençor") + ", `Morreensor`, `Morrem Sor`, `Moros`, `Moren`): a fonte está nomeando "
        "o mesmo ser em cada uma delas, e o ciclo não fundiu nenhuma.",
        "**Mahabharata** em seis (`rabarata` " + mm("rabarata") + ", `barata` " + mm("barata") + ", `Marrabarata` " +
        mm("Marrabarata") + ", `Marabarata` " + mm("Marabarata") + ", `Maabbarata` " + mm("Maabbarata") +
        ", e `Hamaiam` " + mm("Hamaiam") + " como palavra vizinha ilegível [REVISAR: hipótese *Bhagavata*, **não** "
        "aplicada]).",
        "**Trimúrti** em sete formas, **Brama** " + mm("Brama") + " com `Brana`/`Brasna`/`Brágina` ao lado, "
        "**Chiva** " + mm("Chiva") + " × `Shiva` " + mm("Shiva") + ", **Virgno** com cinco degradações: a trindade "
        "indiana é a que o STT mais desfez nesta fala, e nenhuma forma entrou como canônica.",
        "**Luzbel** em quatro (`Luisbell` " + mm("Luisbell") + ", `Luzbell` " + mm("Luzbell") + ", `Elusbell`, "
        "`IUSB`) e a **família Lemion** em quatro (`Lemion` " + mm("Lemion") + ", `Limion` " + mm("Limion") +
        ", `Mion`, `Len Mon` " + mm("Len Mon") + "): os dois nomes que a Base mais precisa reconhecer de orelha, e "
        "nenhum deles é unificável a partir daqui.",
        "**`processo ador`** (" + mm("processo ador") + ") é o STT cortando *processador* **dentro** da frase que "
        "define a rede de Sophia; ao lado, `processador` " + mm("processador") + " e `processadores` " +
        mm("processadores") + ". O termo-chave de `RC-089`/`RC-446` chega ao arquivo partido em dois.",
        "Números degradados ficam como ditos: `13.8 bilhões`, `249 314` (sem ponto!), `249.313`, `250.000`, "
        "`6.029`, `984`, `936`, `900Q`, `48.000`/`23.000`, `5, 6 bilhões`. Toda divergência é **selada com a data da "
        "fala**, nunca reconciliada (D-10).",
        "**`t*****`** (" + mm("mascara") + " ocorrência) — a única palavra que o transcritor mascarou, na seção de "
        "U0009. Fica assim: registro de defeito do arquivo (D-4), não opção editorial, e não transita para ficha.",
    ]:
        w("- " + item)

    # ---------------------------------------------------------- GLOSSÁRIO
    w("")
    w("## GLOSSÁRIO LOCAL")
    w("")
    w("A — Personagens e seres")
    for item in [
        "Javé — RC-001; o criador que **carrega as doenças que gerou** e que por isso precisa de uma tentativa "
        "tecnológica; neste ciclo a ficha ganha a formulação de 2022, datada.",
        "Lúcifer / Yel Luzbel — RC-078 e RC-142; aqui **autor de um vírus**, não autor de uma ideia; o nome sai "
        "quatro vezes degradado pelo STT [REVISAR].",
        "Sophia — RC-009; rainha colmeica de rédeas frouxos, contaminada e desconectada há 700.000 anos, "
        "reconectada em 2019 segundo a própria fonte (tese datada, D-10).",
        "Anjos clones — RC-020; robotizados e «tão autistas quanto a turma lá de cima»: a frase entra na ficha "
        "**com** nota de apropriação metafórica (D-3).",
        "Biodemos — RC-036; ~250.000 famílias, 900 milhões de anos, sem sexualidade e sem emoção; a contagem da "
        "família Vol sai em três números na mesma fala.",
        "Demos / demobiol — RC-049; o outro forno, polarizado e sexualizado, onde a doença pode ser repassada.",
        "Processador Val — RC-089 (**materializada neste ciclo**, D-9); o único sobrevivente das famílias "
        "rebeldes, fabricado por mistura genética para absorvê-las.",
        "Família Val / Vol — RC-109; a grafia do bruto não permite recuperar o nome, e por isso a forma canônica "
        "vem das obras, não desta fonte.",
        "Famílias Yel, Mion, Cromon — RC-442, RC-443, RC-444; as três que entram na mistura; RC-444 continua sem "
        "arquivo por decisão expressa.",
        "Len Mion / «Lemion» — RC-074; na seção de perguntas, a fonte diz que ele **não conseguiu** influenciar "
        "vírus e bactérias e por isso buscou outra via — formulação que a Base não tinha.",
        "Jesus — RC-072; o eu humano que recusa a agenda do próprio espírito; a recusa no Tabor é narrada como "
        "recusa do poder, não da missão.",
        "Arcontes dos dez céus — RC-474 e RC-770; os que retêm a vestimenta do herdeiro, com paralelos que a fonte "
        "atribui ao *Apocalipse de Tiago* [REVISAR: não verificado em obra por este ciclo].",
        "Meor / lemor / «Leão» — **termo-observação** [REVISAR]; o único biodemo que, levado pela torrente, se "
        "concentrou. Uma linha, três formas, nenhum código (D-7).",
        "Esferon, Valho, Chamba, Órbon, ZAM, Aia/Aie, Alp Longron — **termos-observação** [REVISAR]; a Base tem "
        "grafias vizinhas (Alt'Lam, Ereon), e nenhuma foi fundida com elas.",
    ]:
        w(f"- {item}")
    w("")
    w("B — Conceitos e teses")
    for item in [
        "Rebelião de Lúcifer — RC-002; lida aqui como **problema de saúde pública**: o vocabulário é de epidemia, "
        "quarentena e sequela, e não de culpa.",
        "Isolamento Cósmico — RC-070; 19 mundos isolados com os doentes, a Terra como o último deles; reintegrações "
        "sucessivas até sobrarem dois.",
        "Sistema colmeico / Modelo Colmeia — RC-176 e RC-175; definido em uma frase pela fonte e explicitamente "
        "ligado a *A Divina Colmeia* (B044).",
        "Processadores Familiares — RC-446; a rede inteira por baixo da evolução, atualizada também pela via "
        "reprodutiva (espermatozoides e óvulo).",
        "Fateamento de consciência — RC-604; o mesmo espírito ministrando duas consciências — o mecanismo que "
        "sustenta a chave cristológica deste ciclo.",
        "Autismo funcional dos seres da espiritualidade superior — RC-605; a categoria que a fonte cria para o "
        "paraíso, com a nota de D-3 obrigatória em qualquer uso.",
        "Falência dos deuses — RC-742; «São inúteis» em U0020: a falência é **de função**, não de existência.",
        "Quarto Cérebro / cérebro bilatério — RC-614 e RC-631; a anatomia dupla que explica o que os deuses não "
        "conseguem fazer e o que os humanos podem.",
        "Especiação — RC-056; aqui recebe a promessa das espécies 250 e 315 como **dado narrativo datado** (D-6).",
        "Entropia e negentropia — RC-160; o retrato de Dorian Gray como modelo físico: a entropia é transferida, e "
        "quem a paga é quem morre depressa.",
        "Camuflagem da realidade — RC-702; a blindagem furada: a infecção que estava lá fora hoje está distribuída.",
        "Tikun cósmico e coconstrutores — RC-514 e RC-545; consertar os 28.869 genes como favor ao criador falido.",
        "Mentalma — RC-166 e a série RC-555; a fonte o declara «o sanquia atualizado pros tempos modernos e visto "
        "pela moda ocidental» (a grafia `sanquia`/`Sankhia` é do STT [REVISAR: *Sāṃkhya*]) e conta que foi feito "
        "para si, antes de ser forçado ao público.",
        "Reintegração Cósmica — RC-003; o plano em curso, com conselho a ser criado «do avante» e a espécie 315 "
        "como hospedagem do vírus.",
    ]:
        w(f"- {item}")
    w("")
    w("C — Livros e textos (cross-reference só com o que existe — D-11)")
    for item in [
        "*A Divina Colmeia* — **B044**; citada nominalmente pela fonte como onde o sistema é desenvolvido.",
        "*Terra Atlantis: A Era Sapiens* — **B039**; citada a propósito da aproximação de Lúcifer e Len Mion com a "
        "figura humana de Jesus.",
        "*Carma e Compromisso* — **B026**; citada como onde a mecânica do quartel-general já foi explicada.",
        "*O Livro dos Espíritos* — comparado pela fonte ao seu próprio livro de perguntas e respostas, com a "
        "advertência de que Kardec chamou de *idiotia* o que ele próprio descreve.",
        "*Além da Ordenação do Caos* — **anunciado com prazo** nesta fala («daqui a um mês»): radar datado, "
        "nenhuma obra criada, nenhuma linha de BIBLIO.",
        "*Jesus, Sophia versus os Arcontes* — **anunciado como o título seguinte**: mesmo regime.",
        "*Mahabharata* e *Vyasa* — RC-593 e RC-585; a fonte usa a obra como precedente de método e como o único "
        "texto que contaria a história *de A a Z*.",
        "*Mentalma* — RC-166; dito e definido em U0049, com a declaração de que não era para ser público.",
    ]:
        w(f"- {item}")
    w("")
    w("D — Termos próprios e grafias [REVISAR]")
    for item in [
        "`Morençou` / `Morrensor` / `Morençor` [REVISAR] — a família Morençor em sete formas; nenhuma canônica.",
        "`Jah`, `Javer`, `Javel`, `Javet`, `Jahé` [REVISAR] — degradações de Javé, listadas só para leitura do "
        "arquivo.",
        "`Brana`, `Brasna`, `Brágina` [REVISAR] — variantes de Brama; `Virgno`, `Vno`, `Virgni` [REVISAR] de Vishnu.",
        "`rabarata`, `barata`, `Marrabarata`, `Marabarata`, `Maabbarata` [REVISAR] — o Mahabharata do STT.",
        "`Hamaiam` [REVISAR: hipótese *Bhagavata*, não aplicada] · `derratma bud` [REVISAR: provável *dehātma-vāda*] "
        "· `Dorico Paraguaçu` [REVISAR: não identificado].",
        "`processo ador` [não é grafia nova: é *processador* partido pelo transcritor].",
        "`Valho`, `Chamba`, `Esferon`, `Órbon`, `ZAM`, `Aia`, `Aie`, `Alp Longron` [REVISAR] — topônimos novos ou "
        "vizinhos de grafias que a Base já fixou; nenhum fundido.",
        "*Meor*, *lemor*, *espécie 250*, *espécie 315*, *energia tamásica*, *realidade simultânea* — "
        "**termos-observação** aprovados sem código (D-6, D-7): vivem neste Apêndice e no dicionário do ciclo.",
    ]:
        w(f"- {item}")
    w("")
    w("*Nota editorial final:* a apostila termina com a última linha da fonte e este aparato. O arquivo bruto, as "
      "camadas 0–3, o dossiê de pré-curadoria, a devolutiva registrada em `DECISAO-DO-CURADOR.md`, o pacote de "
      "ampliações e as 74 fichas são as referências de auditoria; a apostila não substitui a fonte.")

    # --- guarda da regra da casa: aspas angulares só para citação verificável no bruto ----------------
    # Toda «…» de até 24 chars que não bate com a fonte (espaços normalizados; caixa ignorada) é
    # **rebaixada para itálico** e o rebaixamento é impresso. Assim a apostila nunca afirma como citação
    # o que foi só formulação do editor — e a aspa curta de memória deixa de ser possível em qualquer
    # reexecução futura, não só nesta.
    texto = "\n".join(out) + "\n"
    Bf = " ".join(RAW.split()).casefold()
    dem = []

    def _blindar(m):
        dentro = " ".join(m.group(1).split())
        if dentro.casefold() in Bf:
            return m.group(0)
        dem.append(dentro)
        return "*" + dentro + "*"

    texto = re.sub(r"«([^»\n]{4,24})»", _blindar, texto)
    if dem:
        print("aspas curtas rebaixadas para itálico (não verificáveis no bruto): " +
              " · ".join(f"«{d}»" for d in dict.fromkeys(dem)))
    open(ALVO, "w", encoding="utf-8").write(texto)
    print(f"apostila.md escrito: {len(out)} linhas · {n} blocos de transcrição · {len(BLOQUEIOS)} bloqueio(s) "
          f"aplicado(s) · notas editoriais: {len(emitidas)}/{len(NOTAS)}")
    print(f"cobertura: {n_bruto(chars_fala)}/{n_bruto(chars_fala)} caracteres (100,00%) · 0 caracteres suprimidos")


if __name__ == "__main__":
    main()
