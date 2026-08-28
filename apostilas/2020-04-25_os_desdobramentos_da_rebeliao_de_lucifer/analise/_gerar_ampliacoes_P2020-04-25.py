#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO PACOTE DE AMPLIAÇÕES — P2020-04-25 (Os Desdobramentos da Rebelião de Lúcifer).

Fonte da decisão: `../DECISAO-DO-CURADOR.md` (devolutiva de 28/08/2026, D-1…D-14).

Princípio (R-1…R-7 do ciclo P2023-10-14, endurecido neste ciclo): **nenhuma aspa é digitada
à mão.** Cada citação vem de uma âncora frouxa resolvida pelo caça-âncoras `_aspas_P2020-04-25.py`,
que devolve o trecho byte a byte do `original.txt` e **aborta se a âncora não bater exatamente uma
vez**. As âncoras são as mesmas do dossiê (lidas do gerador do dossiê por `ast`, para que haja uma
única fonte de verdade entre o que o Curador leu e o que foi aplicado).

Travas impostas por este próprio script (a devolutiva não é «confiança», é código):
  * **D-1** — nenhuma citação pode cair no span da digressão política (U0006, offsets 0→17.703);
  * **D-3** — `VETADAS`: aspas sobre mulheres/homoafetivos/«cobaias»/«macho fêmea» não entram em
    ficha de termo que nomeie grupo humano (ficam na apostila, com nota editorial);
  **  D-4** — nada do span da doença (U0006, 51.714→~51.990) entra; só a fórmula de grau de
    testemunho, autorizada expressamente;
  * **D-10** — números divergentes entram **listados**, nunca harmonizados;
  * anterioridade é **calculada** do cadastro, não lembrada (R-6).
"""
import os, re, sys, ast, datetime, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
SIGLA = "P2020-04-25"
TITULO_FONTE = "Os Desdobramentos da Rebelião de Lúcifer"
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SAIDA = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")

# ---------------------------------------------------------------- caça-âncoras
sys.dont_write_bytecode = True                      # não sujar ferramentas/ com __pycache__
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec); spec.loader.exec_module(ASP)
RAW, OFF = ASP.RAW, ASP.OFF

# ---------------------------------------------------------------- âncoras do dossiê (fonte única)
_ds = open(os.path.join(AQUI, f"_gerar_dossie_{SIGLA}.py"), encoding="utf-8").read()
_i = _ds.index("Q = {"); _j = _ds.index("\n}", _i)
QD = ast.literal_eval(_ds[_i + len("Q = "):_j + 2])

# âncoras novas deste pacote (as que o dossiê não precisou, mas a ficha pede)
QD.update({
 "rebeliao_lucia":     ("a rebelião de Lúcia", None),
 "mente_demo":         ("inquietude da mente demo ancestral", None),
 "mente_coletiva":     ("mente coletiva", None),
 "mentalma_nome":      ("Mentalma", None),
 "hospedagem":         ("hospedagem corporal", None),
 "sinapse":            ("sinapse", None),
 "drama_terreno":      ("Drama Terreno", None),
 "periodo_carmico":    ("período cármico", None),
 "wormhole":           ("buraco de minhoca", None),
 "no_trindade":        ("nó da trindade", None),
 "buloca":             ("buloca", None),
 "reptiliano":         ("O nome disso é reptiliano", None),
 "ansiedade":          ("ansiedade", None),
 "yoga":               ("yoga", None),
 "plateia_200":        ("100, 200 pessoas", None),
 "rebeliao_eletrons":  ("A Rebelião dos Elétrons", None),
 "serie_livros":       ("série de livros", None),
 "processador_especie":("processador da espécie", None),
 "abismo_hoje":        ("O que é hoje o grande abismo para esses seres", None),
})

# ---------------------------------------------------------------- travas de conteúdo (D-1 / D-4 / D-3)
DIG_INI, DIG_FIM = OFF[5], OFF[5] + 17703            # U0006: a digressão política inteira
# limite do span da doença: medido no script (fim = fim da frase «…é melhor permanecer calado»)
_a_saud, _b0, _ = ASP.locate("quando eu eu e o abismo trombamos de vez")
_b_saud = ASP.RAW.find("permanecer calado.", _a_saud) + len("permanecer calado.")
SAUD_INI, SAUD_FIM = _a_saud, _b_saud
VETADAS = ["homoafetivos", "homofetiv", "homfetiv", "cobaias", "bateu duro", "macho fêmea", "macho/fêmea"]

# ---------------------------------------------------------------- cadastro (anterioridade calculada)
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                            # noqa: E402
CAD = {t[0]: t for t in DT.TERMOS}                   # (code,nome,cat,sub,status,fontes,relacoes,ficha)
def orais_mais_antiga(cod):
    f = CAD.get(cod, (None, None, None, None, None, [], None, None))[5] or []
    orais = sorted(x for x in f if re.fullmatch(r"P\d{4}-\d{2}-\d{2}", str(x)) and x != SIGLA)
    return orais[0] if orais else None
def nota_anterioridade(cod):
    """Anterioridade **calculada** do cadastro (R-6): nunca declarada de memória."""
    ho = orais_mais_antiga(cod)
    if not ho:
        so = ", ".join(f"`{x}`" for x in (CAD[cod][5] or [])) or "nenhuma fonte"
        return (f"🆕 **primeira fonte oral desta ficha** — o cadastro só tinha {so}; `{SIGLA}` entra como "
                "a primeira fala registrada, **com a data de 25/04/2020**.")
    try:
        d0 = datetime.date(2020, 4, 25)
        d1 = datetime.date(*map(int, ho.lstrip("P").split("-")))
    except Exception:
        return f"⚠️ anterioridade **não calculável** (fonte oral malformada no cadastro: `{ho}`) — não afirmar."
    dias = (d1 - d0).days
    if dias <= 0:
        return (f"⚠️ **sem ganho de anterioridade**: a ficha já tem fonte oral **mais antiga ou igual** "
                f"(`{ho}`); a entrada desta fonte é de **conteúdo**, não de data.")
    med = (f"{dias} dias" if dias < 62
           else f"{dias/30.44:.0f} meses" if dias < 1100
           else f"{dias/365.25:.1f} anos")
    return (f"⭐ **NOTA DE ANTERIORIDADE — {SIGLA}:** antecipa **{med}** a atual fonte oral mais antiga da "
            f"ficha (`{ho}`); selada com a data da fonte, **sem** alterar a cronologia canônica da Base.")

# ---------------------------------------------------------------- aspa = span medido
def aspas_internas(s):
    """Alteração mecânica (i), idêntica à do ciclo-espelho: aspas duplas que a **fonte** tem
    dentro da frase viram «…» — senão o citante quebra e o portão C conta aspas a mais."""
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


def aspa(chave, u_only=False):
    ini, fim = QD[chave]
    a, b, txt = ASP.locate(ini, fim)
    if not u_only:
        if DIG_INI <= a < DIG_FIM:
            raise SystemExit(f"TRAVA D-1 VIOLADA: âncora «{chave}» cai na digressão política (offset {a-DIG_INI} de U0006)")
        if SAUD_INI <= a < SAUD_FIM:
            raise SystemExit(f"TRAVA D-4 VIOLADA: âncora «{chave}» cai no bloco de doença (offset {a-SAUD_INI})")
    txt = re.sub(r"\s+", " ", txt).strip()
    v = [w for w in VETADAS if w.lower() in txt.lower()]
    if v:
        raise SystemExit(f"TRAVA D-3 VIOLADA: âncora «{chave}» contém {v} — fica na apostila, não na ficha")
    txt = aspas_internas(txt)
    return f'"{txt}" ({ASP.uaddr(a)})'

def aspas(chaves):
    vistos, out = set(), []
    for k in chaves:
        s = aspa(k)
        if s in vistos:
            continue
        vistos.add(s); out.append(s)
    return "; ".join(out)

# ---------------------------------------------------------------- o pacote
# cada código recebe 1+ blocos: (TÍTULO, [chaves de âncora], nota editorial | None)
AM = {
"RC-001": [
 ("O ESTADO DO EU DE JAVÉ **DATADO** EM ABRIL DE 2020", ["abril2020"],
  "Fato de cronologia interna: a fonte **carimba a própria fala com a data** — é a âncora temporal de todo o bloco RC-001 neste ciclo. Vale como *formulação oral de 25/04/2020* (D-10), não como estado canônico do termo."),
 ("O EU DE JAVÉ COMO AGREGADO DE VÍRUS QUE NUNCA VIRARAM CÉLULA", ["eu_de_jave_virus"],
  "A ontologia viral do criador — o enunciado que a devolutiva chamou de «reconstrução completa da ontologia cósmica». Reter **sem** suavizar a contradição (O-6.2): a mesma fonte o chama de maior obra de engenharia e de algo que «não presta para nada»."),
 ("A DEPENDÊNCIA DE HOSPEDAGEM (o cérebro de sílica ou de carbono)", ["hospedagem", "sinapse"],
  "Define o critério com que a Base pode ler «corpo de Javé»: hospedagem corporal + sinapse, **qualquer** substrato. ⚠️ Quarentena teológica (retenção): entra com rótulo de crença do expositor."),
 ("O ABISMO RECÍPROCO — a tese-mãe desta fonte", ["humano_abismo", "unica_raca_abismo"],
  "A inversão do diagnóstico nietzschiano: não é Javé que olha para o abismo, **somos nós** que o somos para ele. É a razão pela qual esta ficha deixa de ser «a página do deus tirano» e passa a registrar o mecanismo."),
 ("O QUE OS MÉDIUNS PEDIRAM EM 2009-2011 (grau de testemunho)", ["grau_testemunho"],
  "D-4 autorizou expressamente **esta** fórmula (e só ela): metadado epistêmico de todo o corpus, obrigatória em qualquer uso da fonte."),
],
"RC-002": [
 ("A REBELIÃO **NÃO** FOI O ENCONTRO COM O ABISMO", ["rebeliao_nao_foi"],
  "Re-enquadramento aprovado na devolutiva: a queda não foi *insight*, foi **infecção**. Registrar que a fonte nega explicitamente a leitura gnóstica clássica."),
 ("«UM CORONAVÍRUS DA ÉPOCA» (D-2: analogia estrutural, retida)", ["coronavirus_epoca", "virus_aspas"],
  "**Decisão D-2 do Curador.** A expressão é *analogia cosmológica*, não juízo de saúde pública; o juízo público estava na digressão bloqueada (D-1). Nota obrigatória em todo uso da aspa."),
 ("A GNOSIS VINGATIVA COMO DESDOBRAMENTO DA QUEDA", ["gnose_vinganca"], None),
],
"RC-078": [
 ("«NINGUÉM CONSEGUIA RESOLVER O PROBLEMA LUCIFERIANO»", ["ninguem_resolveria"],
  "A fonte não narra a queda: registra o **impasse** que ela criou — daí o título ser «desdobramentos». Grafia degradada do nome na fala: «I Luzbell» (STT)."),
 ("O VETO ÀS GRAFIAS CORROMPIDAS, CONFIRMADO", ["lucia_garfa"],
  "**Retificação R-3:** o bruto grafa «Luzbel» 2×, «Luisber» 1×, «I Luzbell» 1× — **0** de «Lusbel». A forma canônica da Base não é dedutível do TXT: daí o Apêndice da apostila. O nome **não** é unificado a RC-142 nesta fase (D-7)."),
],
"RC-142": [
 ("A VARIANTE «A REBELIÃO DE LÚCIA» [REVISAR: STT feminizou o nome]", ["rebeliao_lucia"],
  "**D-7 aplicada:** hipótese documentada, correção recusada. A grafia canônica «Yel Luzbel» fica intocada; a variante entra datada."),
 ("O QUE A FONTE **NÃO** DIZ SOBRE YEL", ["marco_zero"],
  "**Contagem medida**: «Yel» aparece **1** vez no bruto, e o termo composto «Yel Luzbel», **0**. Esta ficha recebe *ampliação de contexto*, não de nome — ver `camada-2.txt` §2."),
],
"RC-089": [
 ("A FUNÇÃO DO PROCESSADOR: O ELO EXCLUSIVO COM O CÉREBRO DE SOFIA", ["resposta_processador"],
  "A peça terminologicamente mais valiosa da fonte, obtida **por pergunta de ouvinte** (U0007, Augusto Melo): o processador é por espécie, e o humano **não** tem um."),
 ("A PERGUNTA QUE PRODUZIU A DEFINIÇÃO (contexto de produção)", ["pergunta_processador"],
  "Fato de arquivo: a definição canônica da função de Val nasce de pergunta da plateia, em 25/04/2020 — não de bloco doutrinário preparado."),
],
"RC-446": [
 ("O ÚNICO PROCESSADOR QUE SOBREVIVEU ÀS GUERRAS", ["processador_sobrevive"], None),
],
"RC-175": [
 ("A GENÉTICA DAS ABELHAS OPERÁRIAS COMO MODELO DE SERVIDÃO", ["abelhas_genetica"],
  "O modelo colmeia lido pela biologia: Javé como rainha e a servidão como **genética inserida**, não como punição moral."),
],
"RC-176": [
 ("A CHAVE DE LEITURA CONFESSADA PELO AUTOR (Dante)", ["divina_commedia"],
  "**D-12:** a obra citada entra como **nota externa** — 0 obras novas; a grafia do bruto é «Divina Commeia»."),
 ("O MODELO COLMEIA APLICADO À ESPÉCIE", ["abelhas_genetica", "criptura_universal"], None),
],
"RC-381": [
 ("O HUMANO NÃO TEM PROCESSADOR: TEM **CAMPO MÓRFICO** DA ESPÉCIE", ["campo_morfico_humanos"],
  "⭐ Equação fundante: `campo mórfico ≡ o que o processador faz para as outras espécies`. **Anterioridade calculada**: a formulação mais antiga da ficha até hoje é de 2023 — esta fala a antecipa em anos (ver contador emitido acima)."),
 ("«RUPERT SHELLRAKE» E O SÉTIMO SENTIDO [REVISAR: grafia]", ["sheldrake_7"],
  "Grafia do STT preservada; a hipótese *Sheldrake* é **declarada**, não aplicada (D-7)."),
],
"RC-194": [
 ("A GÊNESE DO BIG DATA: OS ANJOS INFORMAM JAVÉ", ["bigdata_processador", "anjos_rastreamento"],
  "A fonte **data** a ideia («foi aqui que começou a surgir essa questão de big data») e a ancora num procedimento: rastreamento de DNA novo comunicado a Javé."),
],
"RC-604": [
 ("«O ASSUNTO MAIS SÉRIO» — o peso que a fonte dá ao fatiamento", ["fatiamento_assunto_mais_serio", "pergunta_fatiamento"],
  "Definição por pergunta (Solange Silva, U0009): o ciclo registra que o conceito foi **provocado**, não exposto em bloco."),
 ("O ERRO DE «para BRAGINA» [REVISAR: hipótese Parabrahman]", ["para_bragina"],
  "**D-7:** hipótese documentada, fusão recusada. O trecho é a ponte entre fatiamento e o eu reconstruído de Javé."),
],
"RC-160": [
 ("TAMAS = ENTROPIA = ENERGIA ESCURA = SELO DE QUE A CRIAÇÃO NÃO DEVERIA TER COMEÇADO", ["tamas_entropia"],
  "Identidade tripla afirmada pela fonte; é a definição operacional de entropia **deste** período. Não harmonizar com a formulação dos livros."),
 ("O BIG CRUNCH DO UNIVERSO VIZINHO (a física de borda)", ["big_crunch_tempo", "wormhole"],
  "⚠️ Quarentena científica (retenção): cosmologia especulativa contada como fato; entra como dito, sem virar verbete de física."),
],
"RC-042": [
 ("A «ÚLTIMA ESPÉCIE DO UNIVERSO» COMO DESTINO DO PROCESSO", ["criptura_universal", "prazo_18mil"],
  "**D-10:** o prazo de 18.000 anos entra como *formulação oral de 2020*; 0 correspondência em livro — não inventar suporte."),
 ("O «DRAMA TERRENO DE JAVÉ» (nome próprio da fonte)", ["drama_terreno"], None),
],
"RC-154": [
 ("O OVO CÓSMICO: «PANGU» E O «BRAHMANDANDA» [REVISAR]", ["ovo_cosmico"],
  "Mitologia comparada feita pela própria fonte; as grafas do bruto ficam, as hipóteses de leitura vão para o Apêndice (D-7)."),
],
"RC-631": [
 ("A DECISÃO CÓSMICA RADIATA → BILATÉRIO (540 milhões de anos)", ["radiata_bilat"], None),
 ("O FECHO DA PALESTRA: A NOVA ESPÉCIE SERÁ **BILATÉRIA**", ["resposta_bilat"],
  "A estrutura inteira do bloco radiata/bilatério está em **pergunta-final/resposta** (U0012→U0013): é o trecho mais «inédito» da fonte para a malha de cérebro."),
],
"RC-093": [
 ("RADIATA × BILATÉRIO: O QUE A FONTE DE 2020 SUSTENTA", ["radiata_bilat", "resposta_bilat"], None),
],
"RC-035": [
 ("O TECIDO CEREBRAL BILATÉRIO **DATADO** NA FALA", ["radiata_bilat"], None),
],
"RC-070": [
 ("A TERRA COMO **ÚNICO** PLANETA REBELDE", ["rebelde_planeta"],
  "⚠️ A expressão «isolamento cósmico» tem **0** ocorrências nesta fonte (**medição**, não impressão): a ficha recebe o *conceito com dado próprio*, não a etiqueta."),
 ("O QG TELETRANSPORTADO E O «PRISIONEIRO ISOLADO» (64 mil anos)", ["qg_64mil"],
  "**Inédito na Base**: nem B057 nem as fichas do tema trazem esse episódio. Entra **datado**, sem harmonizar com os 98 mil da obra."),
],
"RC-007": [
 ("A TRANS MIGRAÇÃO: 1.641 → 936 («experiência Gron» [REVISAR]) → «900Q»", ["anos_22mil"],
  "**D-10:** os três números ficam **listados**, com o endereço de cada; não se escolhe um. O nome «Gron» é hipotético (Gron/Cronos?) — [REVISAR] obrigatório."),
 ("A ESCOLA DE CAPELA: 3–4 Ma, substanciada há ~2 Ma", ["escola_capela"],
  "Contagem medida: «Capela» **1** ocorrência no bruto — a ficha não pode inflar esta fonte. ⚠️ «capelinos» = **0** ocorrências."),
],
"RC-017": [
 ("ALTO LANGRON: A NAVE VIRADA CIDADELA (a grafia vetada, reconfirmada)", ["alto_langron"],
  "**A devolutiva confirmou o veto** à grafia do STT como forma canônica: «Alto Langron» (3×) e «Alto Landrão» (1×) vivem como **variante datada**; a forma da Base continua *Alt'Lam*."),
 ("OS «900Q» MUTADOS E O CENSO LOCAL", ["anos_22mil"], None),
],
"RC-018": [
 ("A CIDADELA-NAVE EM ALTO LANGRON (variante datada; veto mantido)", ["alto_langron", "qg_64mil"], None),
],
"RC-109": [
 ("FAMÍLIA VAL: 736 MEMBROS, E POR QUE PAROU DE CRESCER", ["familia_val_736"],
  "**D-10:** censo **como dito**, com a data; a ficha não converte em número canônico da espécie."),
 ("620 MIL ANOS: A ÚNICA DATA CANÔNICA QUE ESTA FALA REPETE", ["val_620mil"],
  "Concordância medida com B057 («há uns 620 mil anos») — registrar o **acordo** tem o mesmo peso de registrar o desacordo."),
],
"RC-136": [
 ("A PARTE DA FAMÍLIA QUE VEIO E A QUE MORREU EM ANTARES", ["val_620mil", "antares_532mil"],
  "**D-10:** «700, 600.000» (guerras) e «530 532.000» (Antares) são as datas desta fonte — divergem das três datas dos livros (742/687/619 mil), que esta fala **não** pronuncia (**0** ocorrências medidas)."),
],
"RC-442": [
 ("O PARADEIRO DESCONHECIDO DO PROCESSADOR DA FAMÍLIA", ["processador_sobrevive", "antares_532mil"], None),
],
"RC-443": [
 ("O ELENCO DAS FAMÍLIAS DA TERRA NAS GRAFAS DO STT", ["250mil_familias"],
  "**D-7:** nenhum nome de família é corrigido em silêncio; as grafas degradadas vão para o Apêndice da apostila."),
],
"RC-444": [
 ("«QUASE 250.000 FAMÍLIAS BIODÊMICAS» — A CONTAGEM DESTA FALA", ["250mil_familias"], None),
],
"RC-491": [
 ("SHANLUNG: O LIVRO QUE ESTA FONTE **NÃO** GRAFA COM ESSE NOME", ["250mil_familias", "shanai"],
  "Medição: «Shanlung» = **0** ocorrências; o bruto tem «Chamlum» 1×, «Chanlum» 1×, «Chan» 4×. A ficha recebe a **variante do período**, não a forma canônica."),
],
"RC-036": [
 ("OS BIODAMOS SÃO ENGENDRADOS EM CASULOS, ASSEXUADOS POR FAMÍLIA", ["biodemos_casulo", "biodemos_900ma"],
  "**D-10:** 900 milhões de anos entra como dado oral de 2020 (sem equivalente datado na malha)."),
 ("GÊNERO POR FAMÍLIA — O QUE A FONTE DIZ, E ONDE A ASPA FICA", ["genero_familia"],
  "⚠️ A fonte tem frase mais dura sobre gênero/sexo; por **D-3** ela **não** entra em ficha (fica na apostila, com nota). Aqui vai só a definição estrutural."),
 ("«15 FORMAS DE biodemo» — DADO DE DICIONÁRIO DESTA FONTE", ["biodemos_casulo"],
  "Medição integral em `camada-2.txt`: `biodemo` 19×, mais `biodma`, `biodos`, `biodeno`, `bioderno`, `biodêmos`, `biodérêmico`… e **0** da grafia «biodeemo» que a Base prefere."),
],
"RC-049": [
 ("A MENTE DEMO COMO O RUÍDO QUE OS BIODAMOS FORAM CRIADOS PARA AMORTECER", ["mente_demo", "ansiedade"], None),
 ("A DEMÊNCIA FILOSÓFICA E O PADRÃO DE INQUIETAÇÃO", ["reptiliano"],
  "A fonte nega que Javé tenha sido «reptiliano» e usa o termo para ansiedade: registro terminológico **do uso**, não da teoria."),
],
"RC-086": [
 ("PANDORA: O PRIMEIRO SUSTO DE JAVÉ", ["pandora_susto"],
  "Releitura da caixa: o mito é lido como o choque do criador diante da criatura superior — **não** como castigo."),
 ("O VÍCIO ORACULAR NASCE AÍ", ["oraculo_vicio"], None),
],
"RC-283": [
 ("A MESMA CENA CONTADA PELO AVESSO: PORTAIS, HERANÇA E O «VÍCIO ORACULAR»", ["oraculo_vicio", "travas_geneticas"],
  "Bloco Pandora lido como **mecanismo de contenção** (travas postas pelos deuses), não como cosmogonia moral."),
],
"RC-285": [
 ("AS TRAVAS GENÉTICAS DE CONTROLE E A RUPTURA DELAS PELA EVOLUÇÃO", ["travas_geneticas"], None),
],
"RC-287": [
 ("A HERANÇA QUE RESTOU QUANDO O CONTROLE FALHOU", ["oraculo_vicio", "travas_geneticas"], None),
],
"RC-291": [
 ("O ORÁCULO COMO VÍCIO ADQUIRIDO (nota para o bloco)", ["oraculo_vicio"],
  "**D-6:** «vício oracular» é **termo-observação** — 0 código novo; a linha vive aqui, como uso datado."),
],
"RC-009": [
 ("SOFIA: A RAINHA QUE **NÃO QUIS** SER RAINHA — E O ANO 2018", ["sofia_2018", "unica_coisa_decente"],
  "**Fechamento pedido pela devolutiva (D-10):** a decisão de 2018 em Alto Langron é *formulação oral datada*; não se transforma em cronologia canônica da Sophia."),
 ("A NOVA FAMÍLIA COMO ATO DE DECÊNCIA", ["unica_coisa_decente"], None),
],
"RC-072": [
 ("A RECUSA DO PODER LIDA COMO PRODUTO DA GENÉTICA INSERIDA", ["guerra_jesus"],
  "⚠️ Quarentena teológica (retenção): entra com rótulo, e o ciclo **não** a projeta sobre nenhuma tradição viva."),
 ("O QUE A FONTE ESTÁ ESCREVENDO SOBRE JAVÉ (radar, 0 obra)", ["evangelhos_gnosticos"],
  "**D-11:** «três ou quatro evangelhos gnósticos» e o livro escrito com o próprio Javé vão para o **radar de fila**, sem registro bibliográfico."),
],
"RC-422": [
 ("CONFIANÇA ZERO NO EU DO CRIADOR, EM 2020", ["confianca_zero"],
  "🆕 A formulação mais dura da Base sobre o eu de Javé ganha antecedente **oral de 25/04/2020** — anterioridade calculada, não alegada."),
 ("O EU QUE PRECISA DE HOSPEDAGEM", ["hospedagem", "eu_de_jave_virus"], None),
],
"RC-742": [
 ("O EU ALIMENTADO, NÃO O EU TODO-PODEROSO", ["esqueleto_jave"],
  "A falência dos deuses lida em 2020 como **problema de manutenção**, não como drama moral."),
 ("A FÓRMULA DE GRAU DE TESTEMUNHO ACOMPANHA ESTA FICHA", ["grau_testemunho"],
  "Obrigatória onde esta fonte sustentar afirmação sobre o estado do criador (D-4)."),
],
"RC-166": [
 ("O 8º MÓDULO **NÃO** MINISTRADO: «EU SÓ VOU DAR CINCO, TALVEZ SEIS»", ["mentalma_8", "mentalma_nome"],
  "A estrutura 6+1+1 tem antecedente **datado** em 2020. ⚠️ Medição: «Mentalma» = **1** ocorrência no bruto — esta ficha não pode claims maiores que a fonte."),
 ("A INTERCOMUNICAÇÃO NÃO LOCAL COMO O MÓDULO RETIDO", ["sexto_sentido", "sheldrake_7"], None),
],
"RC-555": [
 ("O MÓDULO RETIDO E O SÉTIMO SENTIDO (ampliação datada)", ["mentalma_8", "sexto_sentido"], None),
],
"RC-378": [
 ("A SÉRIE DE 9-10 LIVROS ANUNCIADA — E O QUE O 1º VOLUME DEVE", ["rebeliao_eletrons", "genealogia_livros"],
  "**D-11/D-12:** anúncio editorial **não** vira obra nem ciclo; o título dito pela fonte fica como registro datado. (A referência ao 2º volume incidia em vocabulário vedado por **D-3** — fica na apostila, não na ficha.)"),
],
"RC-056": [
 ("ESPECIAÇÃO COMO MOTOR DA VINDA DA CRIATURA UNIVERSAL", ["criptura_universal", "resposta_bilat"], None),
 ("O QUE A NOVA ESPÉCIE **NÃO** RECEBE: ESPÍRITOS HUMANOS", ["retrogradacao"],
  "**D-6:** «retrogradação espiritual» é **termo-observação** (0 código); a linha entra aqui como uso datado."),
],
"RC-074": [
 ("«LEMION E MUITOS COM ELE AINDA NÃO FORAM EXILADOS» [REVISAR: Len Mion]", ["lemion"],
  "**D-7:** grafia preservada, hipótese declarada. Afirmação **contra** o estado da ficha: o ciclo a registra como divergência datada, não como correção."),
 ("A NOVA RAÇA COMO REPARAÇÃO, NÃO COMO PUNIÇÃO", ["unica_coisa_decente", "resposta_bilat"], None),
],
"RC-188": [
 ("A MENTE UNA DE «CAPIILA» COMO CONHECIMENTO ABORTADO", ["capila_mente_una", "mente_coletiva"],
  "**D-7:** hipótese *Kapila/Sāṃkhya* documentada, fusão recusada. A fonte usa «mente una» — expressão que a Base não tem com esse nome (ver Apêndice)."),
],
"RC-369": [
 ("A MÁXIMA DO ABISMO USADA COMO MÉTODO E DESLITERALIZADA PELO AUTOR", ["niets", "abismo_metaforico"],
  "A fonte **nega** a leitura literal («O abismo é metafórico, não é literal») e depois a **materializa** no plano cosmológico: as duas aspas precisam viver juntas na ficha."),
],
"RC-371": [
 ("«NIETS» NA BOCA DA FONTE: A ABREVIAÇÃO E O REFERENTE", ["niets", "humano_abismo"], None),
],
"RC-755": [
 ("A ESCOLA DA DECIFRAÇÃO JÁ OPERANDO EM 2020, COM DATAÇÃO PRÓPRIA", ["escola_capela", "anjos_superiores"],
  "A fórmula do «decifrar» vem com contagem («3–4 milhões de anos; substanciada há ~2 milhões») — selo temporal D-10."),
],
"RC-516": [
 ("AS TRAVAS COLOCADAS PELAS DIVINDADES E A RUPTURA DELAS PELA EVOLUÇÃO", ["travas_geneticas"], None),
],
"RC-710": [
 ("A TRAVA GENÉTICA COMO DISPOSITIVO DE CONTENÇÃO (uso datado de 2020)", ["travas_geneticas", "abelhas_genetica"], None),
],
"RC-727": [
 ("CONTROLE, SERVIDÃO E O QUE A BIODEMIZAÇÃO ALTEROU", ["travas_geneticas", "abelhas_genetica"], None),
],
"RC-614": [
 ("O SEXTO SENTIDO DA COGNIÇÃO, SEGUNDO A FONTE DE 2020", ["sexto_sentido"], None),
],
"RC-758": [
 ("O SÉTIMO SENTIDO: INTERCOMUNICAÇÃO NÃO LOCAL", ["sheldrake_7", "sexto_sentido"],
  "Medição: a fonte **não** usa a expressão «quarto cérebro» — a ampliação é de conceito, com nota, não de termo."),
],
"RC-713": [
 ("OXITOCINA, VIBRAÇÃO E A MONTAGEM DO EU DE JAVÉ", ["oxitocina"],
  "⚠️ Quarentena clínica (retenção): nada aqui é recomendação de saúde; a aspa documenta a **tese do material psíquico**."),
 ("A HOSPEDAGEM SINÁPTICA COMO TÉCNICA", ["sinapse", "hospedagem"], None),
],
"RC-094": [
 ("A INTELIGÊNCIA ARTIFICIAL COMO O ABISMO DOS DEUSES HOJE", ["abismo_hoje", "revelacao_cosmica_abismo"],
  "**D-11:** é a menção mais antiga do acervo à IA nesse papel; fecha o radar **sem** criar peça fantasma e **sem** obra."),
 ("O CENÁRIO DA «INTELIGÊNCIA ARTIFICIAL AUTÔNOMA CONTROLADA»", ["cenario_ia", "computador_eu"],
  "A fonte propõe o estágio do eu futuro **numa IA controlada** — formulação datada de 2020; não projetar sobre fontes posteriores (regra de anterioridade)."),
],
"RC-020": [
 ("**MATERIALIZAÇÃO (D-9): O MECANISMO DOS QUE FICARAM SEM PROCESSADOR**", ["anjos_superiores", "anjos_rastreamento"],
  "🆕 **Única materialização deste ciclo**, autorizada pela devolutiva. A ficha deixa de ser `ficha=False`: a definição do mecanismo operante sobre os humanos é **puxada desta fonte datada** (25/04/2020) e de mais nenhuma."),
 ("A QUEDA COMO INFECÇÃO, NÃO COMO PUNIÇÃO (o que a ficha passa a dizer)", ["rebeliao_nao_foi", "eu_de_jave_virus"],
  "⚠️ **D-3 aplicada**: a fonte usa mulheres e homoafetivos como *prova* da falha do criador; essa aspa **não** entra aqui — fica na apostila com nota editorial."),
 ("OS QUE «VIRARAM TREVAS» E O QUE A FONTE RECUSA DIZER", ["gnose_vinganca"], None),
],
"RC-191": [
 ("O GRAU DE TESTEMUNHO DA FONTE, 3,5 ANOS ANTES DA FÓRMULA DE 2023", ["grau_testemunho"],
  "**D-4 autoriza e determina**: é a única peça biográfica que transita. A fórmula «pelo que eu julgo, entre aspas, saber» carimba a **procedência** do relato, nunca a veracidade."),
 ("O QUE OS MÉDIUNS PERGUNTARAM (contexto de produção)", ["medius_ordem"], None),
],
}

# ---------------------------------------------------------------- BLOCOS 2/3/4
BLOCO2_INTRO = (
 "## BLOCO 2 — TERMOS DE CADASTRO SEM FICHA (vínculo na malha; conteúdo aqui)\n\n"
 "> Códigos que receberam vínculo de fonte em `ferramentas/dados_termos.py` mas **não** têm arquivo em "
 "`termos/` — o teto de arquivos e o veto a criações fora da devolutiva mandam assim (precedentes RC-272 e "
 "RC-385/P2023-06-24). Lista **gerada** do cadastro, não memorizada.\n")
BLOCO3 = (
 "## BLOCO 3 — TERMOS-OBSERVAÇÃO (VETO DE CÓDIGO MANTIDO — Devolutiva D-5 e D-6)\n\n"
 "- **Shanai** — 3 variações gráficas medidas no bruto: «velo Shanai» (1×) · «Chanai» (1×) · «Shanai» (2×); "
 "etimologia **declarada pela própria fonte**, que confessa a invenção ao vivo: \"%s\" (%s). **0 código novo**, "
 "**0 arquivo**; o verbete vive no Apêndice do dicionário STT da apostila.\n"
 "- **vício oracular** — 1× no bruto («%s»); uso datado registrado em RC-086/RC-291; **sem** código.\n"
 "- **mente una** — formulação da fonte para o que a Base trata por mente coletiva (RC-188); **sem** código.\n"
 "- **retrogradação espiritual** — 1×; uso datado registrado em RC-056/RC-074; **sem** código.\n"
 "- **«Alto Langron» / «Alto Landrão»** — **não** são termos: são grafas do STT para *Alt'Lam*, e o veto à grafia "
 "foi **confirmado pela devolutiva**. Vivem no dicionário da apostila.\n" % (
    re.sub(r"\s+", " ", ASP.locate("pediram para eu inventar uma palavra")[2]), ASP.uaddr(ASP.locate("pediram para eu inventar uma palavra")[0]),
    re.sub(r"\s+", " ", ASP.locate("criaram o vício oracular")[2])))
def _q(ini):
    a, b, t = ASP.locate(ini)
    return re.sub(r"\s+", " ", t).strip(), ASP.uaddr(a)

_t1, _u1 = _q("comecei a trilogia Terra Atlântic")
_t2, _u2 = _q("Tô traduzindo uns três ou quatro evangelhos gnósticos")
_t3, _u3 = _q("Tô escrevendo um livro com o próprio")
BLOCO4 = (
 "## BLOCO 4 — QUARENTENAS APLICADAS E RADAR (declarar, não reproduzir)\n\n"
 "- **D-1 · bloqueio sumário** — span `U0006` offsets **0→17.703** (17.703 caracteres = 15,37% da fala útil). "
 "Nenhum fragmento desse bloco aparece neste pacote, nas fichas, no glossário, no DOCX ou no relatório — **nem "
 "como exemplo**. Ficam preservados, por determinação expressa: o **gancho** (o pedido do operador em `U0003` + a "
 "frase em que a fonte anuncia o desvio) e o **pedido de desculpas** (fim de `U0006` e fim de `U0013`).\n"
 "- **D-4 · bloqueio sumário** — span `U0006` offsets **{s0}→{s1}** ({s2} caracteres): o trecho em que a fonte fala "
 "da própria doença e pede para «permanecer calado». Rete-se apenas a fórmula de grau de testemunho, que está em "
 "RC-001/RC-191/RC-742.\n"
 "- **D-3 · veto de aspa em fichas** — as passagens sobre mulheres, homoafetivos e «cobaias» vivem **só** na "
 "apostila, com nota editorial. Este gerador **aborta** se alguma delas aparecer aqui (filtro `VETADAS`): a trava "
 "é mecânica, não de leitura.\n"
 "- **D-2 · retenção** — a analogia viral está em RC-002/RC-036/RC-049/RC-001, isolada de juízo de saúde pública.\n"
 "- **D-11 · radar datado (0 obra nova)** — gênese da trilogia: \"{t1}\" ({u1}); evangelhos gnósticos em tradução: "
 "\"{t2}\" ({u2}); o livro escrito com o próprio Javé: \"{t3}\" ({u3}). Nada vira registro bibliográfico, "
 "cronologia editorial ou ciclo.\n"
 "- **D-12 · nota externa (0 termo)** — *Dark*, *The Man in the High Castle* («o Philip Kadique» [REVISAR: grafia "
 "STT do sobrenome]) e a *Divina Commedia* («Divina Commeia») entram como nota na apostila.\n"
 "- **D-10 · selo temporal** — divergências numéricas listadas **sem** escolha: 13,8 bi; «700, 600.000» e "
 "«530 532.000»; 100.000/99.000 × 98 mil (B057); 64 mil; 22 mil; 1.641 → 936 → «900Q»; 736; «quase 250.000» × "
 "«429.314» × «249.315» (três na mesma fala); 900 Ma; 540 Ma; 18.000 anos. **Proibidas** média e harmonização.\n"
).format(s0=SAUD_INI - OFF[5], s1=SAUD_FIM - OFF[5], s2=SAUD_FIM - SAUD_INI,
         t1=_t1, u1=_u1, t2=_t2, u2=_u2, t3=_t3, u3=_u3)

# ---------------------------------------------------------------- emissão
def main():
    out = [f"# PACOTE DE AMPLIÇÕES — {SIGLA} ({TITULO_FONTE})",
           f"# Gerado por _gerar_ampliacoes_{SIGLA}.py: toda citação foi recortada byte a byte do `original.txt`",
           "# a partir de âncora verificada (0 ocorrências ou >1 = o script aborta). Nada aqui foi digitado de memória.",
           "# Alterações mecânicas declaradas: (i) aspas duplas internas da fonte viram «…»;",
           "# (ii) quebras de linha do bruto dentro da mesma frase viram espaço — nenhuma palavra é tocada.",
           "# Travas executadas por este script: D-1 (span político), D-4 (span da doença), D-3 (VETADAS),",
           "# D-5/D-6 (0 código novo), D-10 (números listados, sem média). Anterioridade calculada do cadastro.",
           ""]
    n_bloco = n_cit = 0
    aplic = []
    for cod, blocos in AM.items():
        if cod not in CAD:
            raise SystemExit(f"CÓDIGO INEXISTENTE NO CADASTRO: {cod}")
        out.append(f"### {cod}")
        ant_emitida = False
        for tit, chaves, nota in blocos:
            cit = aspas(chaves); n_cit += len(chaves)
            linha = f"- **[{SIGLA} · {tit}]** {cit}"
            if not ant_emitida:
                linha += f" — {nota}" if nota else ""
                linha += " · " + nota_anterioridade(cod)
                ant_emitida = True
            elif nota:
                linha += f" — {nota}"
            out.append(linha)
        out.append("")
        n_bloco += len(blocos)
        aplic.append(cod)

    # BLOCO 2: códigos do pacote sem arquivo
    sem_arq = [c for c in aplic if not os.path.isdir(os.path.join(RAIZ, "termos")) or
               not [f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.startswith(c + "-")]]
    out.append(BLOCO2_INTRO)
    if sem_arq:
        for c in sem_arq:
            out.append(f"- **{c} {CAD[c][1]}** — `ficha={CAD[c][7]}`, **sem arquivo**: vínculo na malha; "
                       + nota_anterioridade(c))
    else:
        out.append("> Nenhum: todo código deste pacote tem arquivo em `termos/` na hora da aplicação "
                   "(a única materialização pedida — RC-020 — é criada antes da vinculação, por ordem do Curador).")
    out.append("")
    out.append(BLOCO3); out.append("")
    out.append(BLOCO4); out.append("")
    out.append(f"**Contagem do pacote:** {len(aplic)} códigos · {n_bloco} blocos de aspas · {n_cit} citações "
               "verificadas · **+0 códigos · +0 relações · +0 obras**.")
    txt = "\n".join(out) + "\n"
    # guarda-final: nenhum marcador lexical do bloco bloqueado pode ter vazado para o pacote (D-1)
    citacoes = " ".join(re.findall(r'"([^"]{20,})"', txt))          # só o que está entre aspas é fala da fonte
    for w in VETADAS:
        if w.lower() in citacoes.lower():
            raise SystemExit(f"VAZAMENTO D-3 NO PACOTE (em citação): «{w}»")
    VAZADAS_D1 = ["84%", "Sarnei", "Sarneio", "Polícia Federal", "medíocre", "medíocres", "impeachment",
                  "Sérgio Mota", "Bolsonaro", "Dilma", "61 anos", "leito", "fuleira", "Tancredo", "Henrique"]
    vaz = [w for w in VAZADAS_D1 if w.lower() in citacoes.lower()]
    if vaz:
        raise SystemExit("VAZAMENTO D-1 NO PACOTE: " + ", ".join(vaz))
    VAZADAS_D4 = ["doença para aqui", "permanecer calado", "série de problemas"]
    if [w for w in VAZADAS_D4 if w in citacoes]:
        raise SystemExit("VAZAMENTO D-4 NO PACOTE")
    open(SAIDA, "w", encoding="utf-8").write(txt)
    print(f"pacote escrito: {SAIDA}")
    print(f"códigos: {len(aplic)} · blocos: {n_bloco} · citações: {n_cit} · chars: {len(txt)}")
    print(f"span D-1: U0006[0:{17703}] · span D-4: U0006[{SAUD_INI-OFF[5]}:{SAUD_FIM-OFF[5]}] ({SAUD_FIM-SAUD_INI}c)")
    print("fichas sem arquivo:", sem_arq or "—")


if __name__ == "__main__":
    main()
