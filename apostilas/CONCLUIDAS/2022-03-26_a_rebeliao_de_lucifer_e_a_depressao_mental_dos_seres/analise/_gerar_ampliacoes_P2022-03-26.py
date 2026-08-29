#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO PACOTE DE AMPLIAÇÕES — P2022-03-26 (A Rebelião de Lúcifer e a Depressão Mental dos Seres).

Fonte da decisão: `../DECISAO-DO-CURADOR.md` (devolutiva de 28/08/2026, D-1…D-14).

Princípio da casa, endurecido ciclo a ciclo: **nenhuma aspa é digitada à mão**. Cada citação vem de uma
âncora frouxa resolvida pelo caça-âncoras `_aspas_P2022-03-26.py`, que devolve o trecho byte a byte do
`original.txt` e **aborta se a âncora não bater exatamente uma vez**. As âncoras e os códigos **são lidos
do gerador do dossiê por `ast`** — assim o pacote injeta exatamente o que o Curador leu e aprovou, e não
uma releitura dele.

Travas impostas por este script (a devolutiva não é confiança, é código):

* **D-1** — `SPAN_SUICIDA`: medido no bruto; nenhuma âncora que caia nesse span é aceita no pacote;
* **D-2** — `POLITICA`: nenhum nome de pessoa pública (e nenhum termo de campanha) pode aparecer em
  citação de ficha, ainda que a fala o diga dentro do argumento;
* **D-3** — trava **léxica e calculada**: se o NOME da ficha de destino nomeia pessoa, paciente ou grupo
  humano (`GRUPO_RX` lido do próprio cadastro), nenhuma aspa com vocabulário clínico (`CLINICA`) é injetada;
* **D-4** — nenhuma máscara do STT (`*****`) transita: fica na apostila, onde a moldura é lida;
* **D-10** — números divergentes entram **listados com selo temporal**, nunca harmonizados;
* anterioridade é **calculada** do cadastro, nunca lembrada.

Se qualquer trava morder, o arquivo **não é escrito**.
"""
import os, re, sys, ast, datetime, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
SIGLA = "P2022-03-26"
TITULO_FONTE = "A Rebelião de Lúcifer e a Depressão Mental dos Seres"
DATA_FALA = datetime.date(2022, 3, 26)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SAIDA = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
DOSSIE = os.path.join(AQUI, f"_gerar_dossie_{SIGLA}.py")

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)

# ---------------------------------------------------------------- fonte única: Q e VINC do dossiê
_ds = open(DOSSIE, encoding="utf-8").read()
_i = _ds.index("Q = {")
_j = _ds.index("\n}", _i)
QD = ast.literal_eval(_ds[_i + len("Q = "):_j + 2])
_i = _ds.index("VINC = [")
_j = _ds.index("\n]", _i)
VINC = ast.literal_eval(_ds[_i + len("VINC = "):_j + 2])
print(f"âncoras do dossiê: {len(QD)} · vínculos propostos e aprovados: {len(VINC)}")

# ---------------------------------------------------------------- travas (medidas, não declaradas)
_a_suic, _, _ = ASP.locate("pegar um revólver é melhor o alto engano")
_b_suic0, _, _ = ASP.locate("O ser humano que se suicida tá ferrado por uns problemas")
_b_suic = ASP.RAW.find("uma outra história.", _b_suic0) + len("uma outra história.")
SPAN_SUICIDA = (_a_suic, _b_suic)

POLITICA = ["Bolsonar", "Lula", "Trump", "Clinton", "Brexit", "Haddad", "Dilma", "Moro", "PT "]
CLINICA = ["suicid", "revólver", "autist", "esquiz", "idiot", "dement", "babaca", "drogad",
           "alcoól", "psiquiatr", "transtorn", "manicomial"]
GRUPO_RX = r"humano|mortal|pessoa|indiv[íi]du|paciente|doente|autista|esquiz|depress|suicid|drogad|alco[óo]l|idiota|crian[çc]|mulher|homem "

sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                                        # noqa: E402
CAD = {t[0]: t for t in DT.TERMOS}


def ficha_nome_grupo_humano(cod):
    return bool(re.search(GRUPO_RX, CAD[cod][1], re.I))


# ---------------------------------------------------------------- anterioridade calculada
def orais_mais_antiga(cod):
    f = CAD.get(cod, (None,) * 5 + ([], None, None))[5] or []
    o = sorted(x for x in f if re.fullmatch(r"P\d{4}-\d{2}-\d{2}", str(x)) and x != SIGLA)
    return o[0] if o else None


def nota_anterioridade(cod):
    ho = orais_mais_antiga(cod)
    if not ho:
        so = ", ".join(f"`{x}`" for x in (CAD[cod][5] or [])) or "nenhuma fonte"
        return (f"🆕 **primeira fonte oral desta ficha** — o cadastro só tinha {so}; `{SIGLA}` entra como a "
                "primeira fala registrada, **com a data de 26/03/2022**.")
    try:
        d1 = datetime.date(*map(int, ho.lstrip("P").split("-")))
    except Exception:
        return f"⚠️ anterioridade **não calculável** (fonte oral malformada no cadastro: `{ho}`) — não afirmar."
    dias = (d1 - DATA_FALA).days
    if dias <= 0:
        return (f"⚠️ **sem ganho de anterioridade**: a ficha já tem fonte oral **mais antiga ou igual** "
                f"(`{ho}`); a entrada desta fonte é de **conteúdo**, não de data.")
    med = f"{dias} dias" if dias < 62 else (f"{dias/30.44:.0f} meses" if dias < 1100 else f"{dias/365.25:.1f} anos")
    return (f"⭐ **NOTA DE ANTERIORIDADE — {SIGLA}:** antecipa **{med}** a atual fonte oral mais antiga da "
            "ficha (`{}`); selada com a data da fonte, **sem** alterar a cronologia canônica da Base.".format(ho))


# ---------------------------------------------------------------- aspa = span medido
def aspas_internas(s):
    if '"' not in s:
        return s
    out, aberto = [], False
    for ch in s:
        if ch == '"':
            out.append("«" if not aberto else "»")
            aberto = not aberto
        else:
            out.append(ch)
    if aberto:
        out.append("»")
    return "".join(out)


def aspa(chave, cod=None):
    ini, fim = (tuple(QD[chave]) + (None,))[:2]
    try:
        a, b, txt = ASP.locate(ini, fim)
    except SystemExit:
        a, b, txt = ASP.locate(ini)                     # recuo: uma frase, âncora única
    if SPAN_SUICIDA[0] <= a < SPAN_SUICIDA[1]:
        raise SystemExit(f"TRAVA D-1 VIOLADA: «{chave}» cai no span do suicídio (offset {a-SPAN_SUICIDA[0]} "
                         f"de {SPAN_SUICIDA[1]-SPAN_SUICIDA[0]}) — fica na apostila")
    if "*****" in txt:
        raise SystemExit(f"TRAVA D-4 VIOLADA: «{chave}» contém máscara do STT — não transita para ficha")
    pol = [w for w in POLITICA if (re.search(r"\b" + re.escape(w.strip()) + r"\b", txt) if w.strip()[:1].isupper() and len(w.strip()) <= 6 else w in txt)]
    if pol:
        raise SystemExit(f"TRAVA D-2 VIOLADA: «{chave}» contém nome público {pol} — 0 trânsito em ficha")
    if cod and ficha_nome_grupo_humano(cod):
        cli = [w for w in CLINICA if w in txt.lower()]
        if cli:
            raise SystemExit(f"TRAVA D-3 VIOLADA: «{chave}» tem vocabulário clínico {cli} e a ficha "
                             f"`{cod} {CAD[cod][1]}` nomeia pessoa/grupo humano — não entra")
    txt = re.sub(r"\s+", " ", txt).strip()
    return f'"{aspas_internas(txt)}" ({ASP.uaddr(a)})'


def aspas(chaves, cod=None):
    vistos, out = set(), []
    for k in chaves:
        s = aspa(k, cod)
        if s in out or s in vistos:
            continue
        vistos.add(s)
        out.append(s)
    return "; ".join(out)


# ---------------------------------------------------------------- os blocos por código
# um bloco por linha da tabela de vínculos do dossiê (a fonte que o Curador aprovou)
NOTA_PADRAO = ("**Selo temporal (D-10):** fórmula oral de 26/03/2022, transcrita como dita — grafia "
               "degradada do STT preservada, nenhuma cifra arredondada, nenhuma divergência harmonizada.")
AM = {}
for cod, nome, k in VINC:
    AM.setdefault(cod, []).append((f"{nome.upper()} NA FALA DE 26/03/2022", [k], NOTA_PADRAO))

# acréscimos curados: segunda e terceira aspas onde a fala diz mais do que uma frase,
# e onde a devolutiva mandou tratamento específico (D-3, D-5, D-6, D-9, D-10)
EXTRA = {
 "RC-001": [
  ("O ESTADO DE JAVÉ EM 2022: O CRIADOR QUE NÃO SUSTENTA A PRÓPRIA EXISTÊNCIA", ["jave_carrega_doencas", "tentativa_tecnologica"],
   "A ficha deixa de ser só «o deus tirano da Gnose»: aqui o tirano está **doente** e a Base ganha a formulação datada do mecanismo. ⚠️ Retenção teológica: entra com rótulo de crença do expositor (O-8).")],
 "RC-002": [
  ("A REBELIÃO COMO EPIDEMIA, NÃO COMO CULPA", ["codigo_virus", "saude_publica"],
   "O deslocamento decisivo desta fala em relação a P2020-04-25: o vocabulário da queda é **sanitário** (*problema de saúde pública*, *quarentena*, *sequela*). Registrar que a moral foi substituída por epidemiologia, sem apagar a autoria (Lúcifer é nomeado como quem criou o agente).")],
 "RC-009": [
  ("SOPHIA CONTAMINADA E DESCONECTADA HÁ 700.000 ANOS", ["sofia_contaminada", "sofia_desconectada", "nunca_tinha_falado"],
   "A automarca *nunca tinha falado isso claramente* incide exatamente sobre esta afirmação: grau de testemunho alto, e por isso ela entra **com** a ressalva, não apesar dela. A ficha recebe a tese, não a ênfase."),
  ("A RECONEXÃO DATADA: 2019", ["sofia_reconectada_2019"],
   "**D-10**: a data é da fala de 2022 e não tem paralelo em outra fonte. Não harmonizar com nenhuma outra cronologia de religação.")],
 "RC-020": [
  ("OS ANJOS CLONES: TÃO AUTISTAS QUANTO A TURMA DE CIMA", ["anjos_clones_robot"],
   "**Enquadramento de D-3:** o adjetivo é usado pela fonte como categoria do divino, não como diagnóstico; a ficha de `RC-020` não nomeia grupo humano, então a aspa transita **com** esta nota. Proibido reempregar a frase em qualquer contexto que descreva pessoas.")],
 "RC-036": [
  ("O REINO BIODÊMICO EM NÚMEROS, COMO A FALA O DISSE", ["novecentos_milhoes", "biodemos_frios", "sem_sexualidade"],
   "Três datas e três magnitudes de uma só vez (900 milhões de anos, ~250.000 famílias, forno estéril). Cada cifra é reproduzida com o endereço; a contagem de espécies da família Vol está em `RC-056` e em `RC-442`.")],
 "RC-056": [
  ("A PROMESSA DAS ESPÉCIES 250 E 315 (D-6: dado narrativo, 0 código)", ["especie_250_nasce", "cenario_futuro_315", "conselho_vai_ser_criado"],
   "**Ordem expressa da devolutiva:** a promessa entra aqui, como dado narrativo datado, e as duas numerações **não** viram termo — ficam como termo-observação `[REVISAR]` no dicionário da apostila. O bruto ainda grafa a frase de abertura em linha própria (U0006).")],
 "RC-072": [
  ("A RECUSA DA AGENDA: JESUS DIZ NÃO AO PRÓPRIO ESPÍRITO", ["jesus_recusa_agenda2", "nao_usar_poderes", "quatro_evangelhos"],
   "D-5: tese **datada de 26/03/2022**, não definição canônica. A fonte nega o uso de poder e relee o Segundo Advento como investidura recusada — registrar as três aspas juntas para que a recusa não seja lida como recusa da missão.")],
 "RC-078": [
  ("LUCIFER COMO AUTOR DO AGENTE, COM O NOME DEFORMADO PELO STT", ["luisbell_descobre", "eu_antimaterial"],
   "A fala grafa o nome em quatro formas degradadas (ver dicionário da apostila); nenhuma é promovida. O conteúdo que transita é o ato — *criar um vírus* — e a definição do agente como eu antimaterial."),
],
 "RC-089": [
  ("A GÊNESE TÉCNICA DO PROCESSADOR (o que justifica a materialização)", ["processador_sozinho_sobrou", "mistura_genetica", "esferon_nave"],
   "**D-9:** é esta a passagem que autorizou a virada de `ficha=False` → `ficha=True`: o processador da família Vol como único sobrevivente, produzido por mistura genética para absorver as famílias rebeldes, hospedado na nave-cidade. Nada aqui é inferido de outra fonte."),
  ("ONDE O PROCESSADOR MORA E O QUE ELE PROCESSA", ["orbon_processador", "processador_de_cada_familia", "quarto_escuro"],
   "A definição de função (um processador por família, ligado a Sophia, atualizando o campo escuro) vem da mesma fala; a Base não tinha a mecânica, tinha só o nome.")],
 "RC-142": [
  ("O CENTRO DE COMANDO DAS QUASE 250.000 FAMÍLIAS", ["centro_de_comando", "anjos_batiam"],
   "A família Yel/Luzbel aparece aqui como **polo de comando** e não como mito de origem; os anjos Aia/Aie são ditos *magnéticos*, com mais uma grafia degradada do STT.")],
 "RC-160": [
  ("ENTROPIA TRANSFERIDA: O RETRATO DE DORIAN GRAY COMO MECÂNICA", ["dorian_gray", "humanos_morrem_rapido"],
   "A fonte usa a literatura como modelo **físico** (a entropia vai para o retrato; o retrato é a humanidade). Registrar a comparação como ela é dita, sem transformá-la em alegoria moral.")],
 "RC-175": [
  ("O MODELO DA COLMEIA COPIADO DO QUE EXISTIA ENTRE JAVÉ E OS CLONES", ["copiado_da_colmeia", "definicao_colmeico", "operaria_sem_querer"],
   "Definição de regime, com a nota de que a operária não tem conveniência — a Base ganha a fórmula explícita, que em 2020 só estava implícita.")],
 "RC-176": [
  ("RÉDEAS FROUXAS: SOPHIA COMO RAINHA QUE NÃO IMPÕE", ["sofia_rede_frouxa", "divina_colmeia_livro"],
   "A fonte remete o desenvolvimento ao livro já catalogado (cross-reference D-11): **B044 A Divina Colmeia**. Nada de obra nova: o vínculo é de conteúdo com endereço.")],
 "RC-378": [
  ("GUERRAS DE 500.000 ANOS: QUEM SE DESTRÓI E QUEM SÓ SE BATE", ["guerras_500_ano", "comecam_destruir", "guerras_entre_biodemos"],
   "Três marcos de duração na mesma linha (500.000 / 400.000 / 300.000 anos) — reproduzidos como ditos, com o intervalo aberto (D-10).")],
 "RC-446": [
  ("A REDE INTEIRA E O QUE O VÍRUS FERROU", ["orbon_processador", "virus_ferrou_processo", "espermatozoides_atualizam"],
   "A mecânica de atualização (espermatozoides e óvulo como portadores da mudança) é o detalhe que faltava na Base para ler `RC-089` e `RC-446` como a mesma infraestrutura em duas escalas.")],
 "RC-517": [
  ("O PROTOCOLO DA PERFEIÇÃO E A QUEBRA DELE", ["perfeicao_autoritaria", "quebrar_o_protocolo", "nivel_operacional"],
   "A fórmula *a perfeição não é democrática, ela é autoritária* é a premissa de todo o ciclo; a quebra do protocolo é o que abre o nível operacional. Entram juntas para que a primeira não seja lida como elogio da autoridade.")],
 "RC-545": [
  ("O FAVOR DIVINO É DO HUMANO PARA O CRIADOR", ["favores_consertar", "cede_alma_protege", "culpas_que_nao_causamos"],
   "A inversão que dá título à saída prática da palestra: *consertar os 28.869 genes* como favor a um Deus inoperante. Registrar com a ressalva de que a fonte apresenta isso como conselho ao vivo, não como doutrina fechada.")],
 "RC-555": [
  ("MENTALMA COMO SANKHIA ATUALIZADO — E FEITO PARA SI", ["sanquia_atualizado", "mentalma_para_sim", "unica_escola_sem_deus"],
   "**Retenção (D-3/D-5):** a frase sobre as religiões (*mata em nome de Brama, mata em nome de Alá*) **não** transita — fica na apostila. Aqui entram só a definição da escola e a declaração de destino do material.")],
 "RC-596": [
  ("O QUE OS ARCHEONS TÊM DE SEXO E O QUE ISSO FAZ DA REBELIÃO", ["cinco_sexos_ereon", "sexualidade_repasse", "outro_forno"],
   "A fala liga a polarização sexual à possibilidade de transmitir doença — a chave para ler `RC-596` sem exotismo: o sexo entra como **via de infecção** no argumento sanitário.")],
 "RC-604": [
  ("FATEAMENTO: O MESMO ESPÍRITO MINISTRANDO DUAS CONSCIÊNCIAS", ["fateamento_consciencia", "duas_consciencias", "espirito_nao_assimila"],
   "D-5: é o mecanismo que sustenta a tese cristológica desta fala. Entra como **tese datada**, e o parágrafo da recusa no Tabor fica em `RC-072` para que não se leia fateamento como determinismo.")],
 "RC-605": [
  ("O AUTISMO FUNCIONAL: A CATEGORIA QUE A FALA CRIA PARA O PARAÍSO", ["pervertidos", "espirito_ingenuo", "autismo_resquicio"],
   "**Enquadramento de D-3 (obrigatório em todo uso):** o termo é usado pela fonte como categoria cosmológica — ausência de malícia, não diagnóstico. A fala **nega** que isto descreva pessoas; qualquer reemprego em contexto humano está vedado por decisão do Curador.")],
 "RC-631": [
  ("RADIATA: O CORPO QUE EXPLICA POR QUE SOPHIA NÃO SORRI", ["sofia_dores_costas", "sorriso_sofia", "rir_da_desgraca"],
   "A anatomia é usada como argumento, não como piada: o cérebro radiata não tem o circuito do riso. Manter as três aspas juntas para que a última não vire escárnio do quadro clínico.")],
 "RC-742": [
  ("A FALÊNCIA DECLARADA: OS DEUSES NÃO SABEM O QUE FAZER", ["deuses_inuteis", "falencia_geral", "medito_espiritual"],
   "A frase de fechamento (*quem medita, quem é espiritual…*) é a que a fonte usa para inverter a hierarquia: o divino precisa do humano. Registrar que a falência é **de função**, não de existência — a mesma fala afirma os deuses o tempo todo.")],
 "RC-758": [
  ("FILOSOFIA COMO ESPECÍFICO HUMANO, E O QUE ELA NÃO É", ["filosofia_definicao", "conceitos_supremos", "inteligente_nao_racional"],
   "A definição que a fonte dá de filosofia é a premissa da saída prática; o par *inteligente ≠ racional* é o que impede de ler a fala como elogio da inteligência dos deuses.")],
}
for cod, blocos in EXTRA.items():
    AM.setdefault(cod, []).extend(blocos)

# RC-072: a âncora do Tabor, que só existe no dossiê como chave de texto
QD.setdefault("jesus_recusa_agenda2", QD.get("jose_recusa_agenda"))
# o dossiê grafou uma chave com acento; aqui o alias normaliza sem tocar no dossiê
QD.setdefault("espirito_nao_assimila", QD.get("espírito_nao_assimila"))
QD.pop("jesus_recusa_agenda2", None) if QD.get("jesus_recusa_agenda2") is None else None
for cod in AM:
    for _, chaves, _ in AM[cod]:
        for k in chaves:
            if k not in QD:
                raise SystemExit(f"âncora ausente do dossiê: {cod} → {k}")

# ---------------------------------------------------------------- escrita
BLOCO2_INTRO = "### BLOCO 2 — códigos do pacote sem arquivo em `termos/`\n"
BLOCO3 = (
 "### BLOCO 3 — SELO TEMPORAL E DIVERGÊNCIAS (D-10, por ordem expressa do Curador)\n\n"
 "Nenhuma cifra deste ciclo foi arredondada, média ou reconciliada. O que diverge, diverge **datado**:\n\n"
 "- `984` indivíduos astralizados há 20.000 anos (esta fala, U0034) × `936`/`900Q` na fala de 25/04/2020 — "
 "duas formulações de um mesmo episódio, ambas registradas;\n"
 "- `6.029` chegadas há 100.000 anos (esta fala) × `1.641` (2020) — a Base mantém as duas com endereço;\n"
 "- `48.000` e `23.000` anos ditos na **mesma linha** por esta fonte (U0040) — divergência interna, não "
 "contradição entre fontes;\n"
 "- `5, 6 bilhões de anos` para a engendração de Sophia: o bruto grafa vírgula de **intervalo de fala**, "
 "não decimal — ler *5 a 6 bilhões*;\n"
 "- `200 bilhões` de biodemos contaminados × `trilhões` existentes, na mesma frase (U0009) — a fonte corrige "
 "a ordem de grandeza ao longo do período;\n"
 "- **duas convergências que valem registro**: `620.000` e a família em `736` aparecem iguais em 2020 e em "
 "2022, ditas sem anotação — a Base as mantém como estão, e é isso que faz desta fala uma confirmação e não "
 "uma revisão.")
BLOCO4 = (
 "### BLOCO 4 — cruzamentos, radar e metadados de enunciação (D-11, D-12, D-13)\n\n"
 "**Cross-reference com o que já existe no BIBLIO** (D-11, ordem expressa: só obras catalogadas):\n\n"
 "- `B044 — A Divina Colmeia`: citada nominalmente pela fonte em U0008 como o lugar onde o modelo é "
 "desenvolvido → cruzamento em `RC-175`, `RC-176`, `RC-147`;\n"
 "- `B039 — Terra Atlantis: A Era Sapiens`: citada em U0047 a propósito da aproximação de Lúcifer e Len "
 "Mion com a figura humana de Jesus → cruzamento em `RC-074`, `RC-078`, `RC-072`;\n"
 "- `B026 — Carma e Compromisso`: citada em U0047 como onde a mecânica do quartel-general já foi explicada → "
 "cruzamento em `RC-702`, `RC-604`.\n\n"
 "**Radar datado (0 obra criada, 0 linha de BIBLIO):** `Além da Ordenação do Caos` é **anunciado com prazo** "
 "pela fonte (*daqui a um mês*, em 26/03/2022 ⇒ 26/04/2022) e `Jesus, Sophia versus os Arcontes` é anunciado "
 "como o título **seguinte**. Nenhuma verificação de publicação é feita por este ciclo; o registro fica no "
 "relatório, com a data da fala como prova de anterioridade da menção.\n\n"
 "**Metadados de enunciação (D-12/D-13):** a palestra tem pausa pedida ao vivo, tem plateia nomeada na "
 "última linha (Marcelo, Solange, Mara, Lila, Elô, Narras) e a fonte declara o estatuto do próprio material "
 "(*só para meu estudo*; *essa palestra não é para vocês*). Nada disso gera entidade, ficha ou relação: "
 "são o quadro em que a fala foi dita, e é assim que a apostila os transcreve.")

out = [
 f"# PACOTE DE AMPLIAÇÕES — {SIGLA} · {TITULO_FONTE}",
 "",
 f"Fonte: `original.txt` do ciclo ({DATA_FALA:%d/%m/%Y}, São Paulo). Cada aspa é span verificado pelo "
 f"caça-âncoras `_aspas_{SIGLA}.py`; as âncoras e a lista de códigos são **lidas do dossiê aprovado** "
 "(`_gerar_dossie_P2022-03-26.py`), para que não exista diferença entre o que o Curador leu e o que foi "
 "injetado. Travas D-1 (span do suicídio), D-2 (nomes públicos), D-3 (léxico clínico em ficha que nomeia "
 "grupo humano) e D-4 (máscaras do STT) são executadas por este script, e não por promessa.",
 "",
 "### BLOCO 1 — seções a inserir nas fichas",
 "",
]
aplic, n_bloco, n_cit = [], 0, 0
for cod in sorted(AM):
    if cod not in CAD:
        raise SystemExit(f"CÓDIGO INEXISTENTE NO CADASTRO: {cod}")
    blocos = AM[cod]
    out.append(f"### {cod}")
    ant_emitida = False
    vistas = set()                                            # dedupe ENTRE blocos da mesma ficha
    emitidos = 0
    for tit, chaves, nota in blocos:
        partes = []
        for k in chaves:
            c = aspa(k, cod)
            if c in vistas:
                continue
            vistas.add(c)
            partes.append(c)
        if not partes:
            continue                                          # bloco redundante: não é escrito
        cit = "; ".join(partes)
        n_cit += len(partes)
        emitidos += 1
        tit = tit.replace("«", "").replace("»", "")          # rótulo de bloco não é citação
        linha = f"- **[{SIGLA} · {tit}]** {cit}"
        if not ant_emitida:
            linha += (f" — {nota}" if nota else "") + " · " + nota_anterioridade(cod)
            ant_emitida = True
        elif nota:
            linha += f" — {nota}"
        out.append(linha)
    if not emitidos:
        raise SystemExit(f"ficha {cod} ficou sem nenhuma aspa — rever o pacote")
    out.append("")
    n_bloco += emitidos

sem_arq = [c for c in sorted(AM) if not [f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.startswith(c + "-")]]
out.append(BLOCO2_INTRO)
if sem_arq:
    for c in sem_arq:
        fl = CAD[c][7]
        out.append(f"- **{c} {CAD[c][1]}** — `ficha={fl}` e **sem arquivo**: o vínculo vive na malha "
                   f"(`dados_termos.py`); {nota_anterioridade(c)}")
    out.append("")
    out.append("> `RC-089` aparece acima **porque o pacote é gerado antes da materialização**: por ordem do "
               "Curador (D-9) o arquivo `termos/RC-089-*.md` é criado em seguida, a partir deste bloco, e o "
               "cadastro é virado para `ficha=True`. `RC-444` continua sem arquivo, como decidido.")
else:
    out.append("> Nenhum: todo código deste pacote tem arquivo em `termos/` na hora da aplicação.")
out += ["", BLOCO3, "", BLOCO4, ""]

ganho = sum(1 for c in AM if "antecipa" in nota_anterioridade(c))
out.append(f"**Contagem do pacote:** {len(AM)} códigos · {n_bloco} blocos de aspas · {n_cit} citações "
           f"verificadas · **{ganho} com ganho de data calculado** · **+0 códigos · +0 relações · +0 obras**.")
txt = "\n".join(out) + "\n"

# guarda-final: nenhum marcador vedado pode ter vazado para o pacote (as aspas são o que transita)
citacoes = " ".join(re.findall(r'"([^"]{15,})"', txt))
for w in POLITICA:
    if re.search(r"\b" + re.escape(w.strip()) + r"\b", citacoes):
        raise SystemExit(f"VAZAMENTO D-2 NO PACOTE: {w}")
for w in ("suicid", "revólver", "*****", "t*****"):
    if w in citacoes:
        raise SystemExit(f"VAZAMENTO D-1/D-4 NO PACOTE (em citação): {w}")
for w in ("Haddad", "Dilma", "impeachment", "PT "):
    if w in citacoes:
        raise SystemExit(f"VAZAMENTO D-2 NO PACOTE: {w}")

open(SAIDA, "w", encoding="utf-8").write(txt)
print(f"pacote escrito: {SAIDA}")
num = lambda x: f"{x:,}".replace(",", ".")
print(f"códigos: {len(AM)} · blocos: {n_bloco} · citações: {n_cit} · ganho de data: {ganho} · chars: {num(len(txt))}")
print(f"span D-1 medido: {ASP.uaddr(SPAN_SUICIDA[0])} {num(SPAN_SUICIDA[1]-SPAN_SUICIDA[0])} c "
      f"({SPAN_SUICIDA[0]}→{SPAN_SUICIDA[1]})")
print("fichas sem arquivo:", ", ".join(sem_arq) or "—")
print("fichas que a trava D-3 protege:", ", ".join(f"{c} {CAD[c][1]}" for c in sorted(AM) if ficha_nome_grupo_humano(c)))
