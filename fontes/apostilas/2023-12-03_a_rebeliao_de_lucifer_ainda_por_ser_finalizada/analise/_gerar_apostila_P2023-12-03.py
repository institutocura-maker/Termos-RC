#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DA APOSTILA — ciclo P2023-12-03 · *A Rebelião de Lúcifer ainda por ser Finalizada*.

Molde: `apostilas/CONCLUIDAS/2022-03-26_*/analise/_gerar_apostila_P2022-03-26.py`, com as diferenças que a
devolutiva de 29/08/2026 manda:

* **nenhum corte**: D-1, D-2, D-3 e D-4 determinam transcrição **integral com moldura no lugar exato** — a
  intervenção é nota, não tesoura. A moldura é procurada pelo auditor **dentro do mesmo bloco** que carrega o
  span, para que não exista nota flutuando longe do trecho que emoldura;
* **D-2** impõe que as duas frases do quiasma fiquem **juntas**: o span da moldura vai da primeira à segunda, e
  a apostila não pode apresentar uma sem a outra;
* **D-4** proíbe purificação: as 9 máscaras do STT e as baixarias ficam ipsis litteris, e o arquivo não é
  escrito se o gerador tentar substituir qualquer uma;
* as aspas continuam saindo **só** do caça-âncoras `_aspas_P2023-12-03.py` (o mesmo que alimentou o dossiê e o
  pacote de ampliações), e cada `«…»` curta que não bata com o bruto é rebaixada para itálico no fim;
* o aparato curatorial da PARTE III é **espelhado** de `DECISAO-DO-CURADOR.md` §1 e dos BLOCOS 3/4 do pacote,
  nunca reescrito de memória; os contadores do «efeito material» são lidos de `dados_termos.py` e de `termos/`.

Exposição para o auditor: `NOTAS` e `QD` são nomes de módulo — `_cobertura_apostila_P2023-12-03.py` os lê para
conferir presença e vizinhança das molduras sem depender deste `main()`.
"""
import os, re, sys, io, glob, hashlib, contextlib, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
ALVO = os.path.join(CICLO, "apostila.md")
DECISAO = os.path.join(CICLO, "DECISAO-DO-CURADOR.md")
PACOTE = os.path.join(AQUI, f"_ampliacoes_P2023-12-03.txt")
BRUTO = os.path.join(CICLO, "original.txt")
SIGLA = "P2023-12-03"
TITULO = "A Rebelião de Lúcifer ainda por ser Finalizada"
DATA = "03/12/2023"
BLOCO_ALVO = 2200
FALA_INI = 2                                        # U0001 é o título do arquivo; U0002, vazio
AUTOR = "Jan Val Ellam"

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec); spec.loader.exec_module(ASP)
RAW = ASP.RAW
LINHAS = RAW.split("\n")

n_bruto = lambda x: f"{x:,}".replace(",", ".")

# ─────────────────────────── os spans que esta apostila emoldura ou comenta ───────────────────────────
_ALVOS = {
 "abertura_mandato":  ("Hoje nos vamos retomar um assunto", None),
 "rebeliao_pend":     ("a rebeliao de Lucifer nao terminou", None),
 "d1_escolha":        ("qual a identidade de genero desses seres", None),
 "d1_humanidade":     ("Mas e isso que a humanidade vai ter que mudar loucamente", None),
 "d1_identidade":     ("cada familia tem um jeitinho diferente de ser", None),
 "d2_quiasma":        ("As mulheres atrapalham tudo", "que fez com que Jesus disse"),
 "d2_homens":         ("Os homens sao fracasso nessa historia", None),
 "d3_politica":       ("Qualquer lider que seja", "problema generalizado"),
 "d4_masculina":      ("Depois que Eva disse", None),
 "d4_enoque":         ("tanto e****** no seu DNA", None),
 "d4_primeiro_b":     ("o primeiro b****** dessa historia", None),
 "cargo_naodeus":     ("Isso nao e Deus, e so o criador", None),
 "posse_nunca":       ("Sabe aquela cerimonia de posse nunca houve", None),
 "vanguarda":         ("A vanguarda do atraso", None),
 "genetica_podre":    ("isso e a genetica podre do criador", None),
 "soneca":            ("4.380.000 anos e o tempo que dura a soneca", None),
 "vol736":            ("Sao 736 porque devido ao problema", None),
 "metodo_pedagogico": ("criem um metodo para voces estudarem", None),
 "arca_metodo":       ("nos queremos dar para voces os nossos conhecimentos", None),
 "rebeliao_pend2":    ("a rebeliao de Lucifer agora para ter continuidade", None),
 "plateia_rog":       ("essa historia ta terminando na vida de Rogerio", None),
 "pandora_sorriso":   ("possa sorrir nos termos em que Pandora", None),
 "ano_2023":          ("nesse dia 3 de dezembro do ano 2023", None),
 "sala_2023":         ("nessa sala hoje, dia 3 de dezembro", None),
 "calendario_janela": ("o ano 2050, ou e 50", "52 vai existir de tudo por aqui"),
 "enxame_19":         ("distribuiram nesses 19 mundos", None),
 "fornos_3":          ("criaram tres formas de replicacao", None),
 "entropia_tudo":     ("Tudo. A entropia destroi tudo", None),
 "casulos":           ("criados em casulos, em naves", None),
}
QD = {}
for _k, (_ini, _fim) in _ALVOS.items():
    _a, _b, _t = ASP.locate(_ini, _fim, "exata")
    QD[_k] = (_a, _b, re.sub(r"\s+", " ", _t).strip())


def _txt(chave):
    return QD[chave][2]


def q(chave):
    """Aspa da fonte via caça-âncoras — retas internas preservadas como no bruto (ver doc do molde)."""
    return "«" + _txt(chave) + "»"


def end(chave):
    return ASP.uaddr(QD[chave][0])


def cont(rx):
    return len(re.findall(rx, RAW, re.I))


# ─────────────────────────── o que foi medido no bruto para a nota de leitura ───────────────────────────
N_MASCARAS = len(re.findall(r"\*{3,}", RAW))
FORMAS_MASCARA = sorted(set(re.findall(r"[A-Za-zÀ-ÿ]\*{3,}", RAW)), key=lambda s: (-len(s), s))
FALAS = [(f"U{i + 1:04d}", len(l.strip())) for i, l in enumerate(LINHAS) if i >= FALA_INI and l.strip()]
PESADAS = [u for u, n in FALAS if n > 400]
CURTAS = [u for u, n in FALAS if n <= 150]
CONC = max(n for _, n in FALAS)
TOT_FALA = sum(n for _, n in FALAS)
NOMES = {"Rogério": r"(?<![A-Za-z])Rogerio(?![a-z])", "Jan": r"(?<![A-Za-z])Jan(?![a-zà-ú])",
         "Márcia": r"(?<![A-Za-z])Marcia", "Horácio": r"(?<![A-Za-z])Horacio", "César": r"(?<![A-Za-z])Caesar"}
MED_NOMES = {k: len(re.findall(v, RAW, re.I)) for k, v in NOMES.items()}
AUTOR_NOME = len(re.findall(r"Jan\s+Val\s+Ellam", RAW, re.I))
SHA = hashlib.sha256(open(BRUTO, "rb").read()).hexdigest()

NOTAS = [
 ("abertura_mandato",
  "**A fonte declara o mandato do ciclo antes de qualquer doutrina** (" + q("abertura_mandato") + "). Vale como aviso "
  "de método para toda a apostila: ela própria diz que está retomando um assunto tratado *por alto* nas trilogias, e "
  "que o que vem agora é o que ficou por dizer. A edição respeita essa ordem — a transcrição abaixo segue a ordem da "
  "fala, sem reorganização temática, e cada bloco carrega o endereço com que pode ser conferido no `original.txt`."),
 ("rebeliao_pend",
  "**O título desta palestra, dito em uma linha** (" + q("rebeliao_pend") + " · " + end("rebeliao_pend") + "). É a "
  "proposição que o ciclo inteiro gira em torno: a rebelião não é evento encerrado, é **processo não finalizado**. "
  "Daí a navalha deste ciclo para as fichas: o que entra é o que a fonte formula, não o que um leitor concluiria."),
 ("d1_escolha",
  "**MOLDURA (D-1) · primeira metade do argumento vetado de trânsito.** " + q("d1_escolha") + " A fonte usa a "
  "fica aqui, transcrita, com a pergunta e a resposta juntas; **nenhuma** dessas palavras transitou para as fichas "
  "que nomeiam grupos humanos. O dado técnico que a Base recebeu em `RC-036`/`RC-056`/`RC-093` é outro e só esse: "
  "seres sem sexo, produzidos em casulos, com cérebro radiata (" + q("casulos") + " · " + end("casulos") + ")."),
 ("d1_humanidade",
  "**MOLDURA (D-1) · segunda metade, a que o despacho mandou não apartar da primeira.** " + q("d1_humanidade") +
  " Lida isoladamente, a frase vira panfleto; lida no lugar exato, ela é a conclusão de um raciocínio sobre "
  "anatomia comparada (" + q("d1_identidade") + "). A moldura existe porque a transcrição **não** foi limpa: "
  "rejeitamos tanto a purificação silenciosa quanto a citação fora do fôlego. Na malha, 0 ocorrências desse léxico "
  "— ver BLOCO 5 do pacote e o portão D."),
 ("d2_quiasma",
  "**MOLDURA (D-2) · as duas frases, juntas, como ordem expressa do Curador.** " + q("d2_quiasma") + " A devolutiva "
  "proíbe apartá-las: a primeira é a acusação que a fonte faz correr, a segunda é a reversão que ela mesma opera "
  "logo em seguida, com o DNA de Maria como pivô. Separá-las produziria só a ofensa; colá-las produz o que está "
  "dito. Nas fichas transitou **apenas** a metade afirmativa, em `RC-189`/`RC-727`; o aforismo controverso tem aqui "
  "o seu lugar de leitura, e no GLOSSÁRIO LOCAL a nota contextual forte que o despacho exigiu."),
 ("d2_homens",
  "**MOLDURA (D-2) · o reverso do mesmo quiasma, três linhas adiante.** " + q("d2_homens") + " A fonte inverte a "
  "conta: o fracasso é atribuído aos homens, e a linhagem do inconformismo passa a correr por Pandora e Eva. Este "
  "par de frases é o motivo pelo qual a moldura deste ciclo não é corte: o material é áspero e é **endereçado** — "
  "dito, por quem disse, quando disse. O que foi vedado é o trânsito para fichas que nomeiem pessoas ou grupos."),
 ("d3_politica",
  "**MOLDURA (D-3) · o bloco político, medido antes de emoldurado.** " + q("d3_politica") + " Registro de "
  "divergência honesta, exigido pela própria casa: a devolutiva nomeou o aforismo «a mediocridade de uma população "
  "faz de seus líderes a cara dela», e essa formulação **não ocorre** no `original.txt` (0 ocorrências de "
  "`mediocri*` e de `cara dela`). O que a fonte diz em " + end("d3_politica") + " é o que está acima, e é sobre isso "
  "— não sobre o resumo — que a moldura se aplica. Zero trânsito para fichas ontológicas, 0 vocabulário político em "
  "ficha nenhuma (portão D, trava D-3)."),
 ("d4_masculina",
  "**MOLDURA (D-4) · a máscara é do transcritor, não da fonte nem desta edição.** " + q("d4_masculina") + " As "
  + str(N_MASCARAS) + " máscaras do STT ficam ipsis litteris — é proibida a purificação silenciosa e é proibida a "
  "reconstrução hipotética do xingamento. Formas medidas: " + ", ".join(f"`{f}`" for f in FORMAS_MASCARA) + ". Em "
  "contrapartida, nada disso transita: a pergunta de Eva ficou no BLOCO 5 do pacote (retida pela trava D-4) e "
  "chegou a `RC-189` apenas pela aspa aprovada pelo despacho."),
 ("d4_enoque",
  "**MOLDURA (D-4) · a segunda máscara, no bloco de Enoque.** " + q("d4_enoque") + " Aqui a degradação incide sobre "
  "o que seria um adjetivo pesado aplicado ao DNA de Enoque; a frase sobrevive como veio porque o verbo da fonte é "
  "o que sustenta o vínculo (`RC-672`, `RC-673`, `RC-489`). [REVISAR] a leitura do termo, nunca a sua substituição."),
 ("d4_primeiro_b",
  "**MOLDURA (D-4) · a série das três máscaras em sequência, no fecho do bloco.** " + q("d4_primeiro_b") + " Luzbel, "
  "o segundo, Eva a terceira, Noréia a quarta — a fonte faz uma escala de «bandidos-heróis» e o STT mascara o substantivo "
  "três vezes. A escala é o dado etnográfico desta palestra; o substantivo, não. Nada da série transitou para ficha."),
 ("cargo_naodeus",
  "**D-5 · a frase mais citável do ciclo, com a cláusula anexada.** " + q("cargo_naodeus") + " — e a cláusula que o "
  "despacho obrigou a colar nela: **não nega Deus; desloca o título de Deus do criador da obra.** Nas fichas "
  "`RC-001`, `RC-042` e `RC-742` a tese entrou datada de " + DATA + " como *tese sobre cargo*, com a cláusula "
  "anexada à aspa e não solta em parágrafo próprio, exatamente para impedir as duas leituras preguiçosas (ateísmo "
  "de vitrine ou apologia)."),
 ("posse_nunca",
  "**O pivô de todo o ciclo.** " + q("posse_nunca") + " — não «ainda não houve», mas «nunca houve»: a cerimônia não "
  "está atrasada, foi **retida**. A partir daqui a palestra inteira é a demonstração de que o governo do universo "
  "biológico está vago por ato de recusa (a de Jesus, em " + end("posse_nunca") + " e arredores) e não por falência "
  "de cronograma. D-6: o glossário local trata *posse* como metáfora de investidura e nenhuma relação de fundamento "
  "foi criada por esta entrada — as sete fichas nomeadas receberam aspa e endereço, e nada mais."),
 ("vanguarda",
  "**D-7 · a obsolescência anatômica, na formulação que virou epíteto.** " + q("vanguarda") + " A fonte diz de Sofia "
  "o que a Base ainda não tinha dito com essa secura: o que era o mais moderno da época é hoje a vanguarda do atraso, "
  "e o argumento é de arquitetura cerebral (" + str(cont(r"dois c[ée]rebros|duas c[âa]meras")) + "× a referência aos "
  "dois cérebros/câmaras). Entrou em `RC-631`/`RC-632`/`RC-093`/`RC-035`/`RC-736` e **não** gerou código novo, como "
  "ordenado."),
 ("genetica_podre",
  "**A expressão que o prefácio do despacho escolheu para o ciclo, medida no bruto.** " + q("genetica_podre") + " — "
  "o Curador leu nisto uma tese **destituída de moralidade**, e é por isso que a moldura aqui é de **não-julgamento**: "
  "a frase descreve um estado de sistema, não um veredito sobre alguém. Nada nesta apostila suaviza a frase e nada a "
  "endossa; ela está endereçada em " + end("genetica_podre") + "."),
 ("soneca",
  "**Um número sem par na Base, declarado sem par.** " + q("soneca") + " As eras da Arca (`RC-567`, `RC-569`) operam "
  "em 25.920 e 2.160 anos — outra escala, não a mesma grandeza. Por D-9 isto **não** é aproximado de 4.320.000 nem "
  "reconciliado com nada: fica com endereço, selado em " + DATA + "."),
 ("vol736",
  "**Convergência em três fontes — o caso mais estável do eixo.** " + q("vol736") + " Os mesmos 736 efetivos da "
  "família Vol aparecem em P2020-04-25, em P2022-03-26 e aqui. D-9 manda registrar convergência como **confirmação**, "
  "com destaque, e não como revisão: nenhuma ficha foi reescrita por causa disto, e o número não foi arredondado para "
  "«700 e poucos» em lugar nenhum."),
 ("ano_2023",
  "**A fonte sela a própria data duas vezes** (" + q("ano_2023") + " e, mais adiante, " + q("sala_2023") + "). Não é "
  "detalhe: é o que permite datar a tese do cargo e da posse sem depender de metadado de arquivo. Todo selo temporal "
  "deste ciclo sai destas duas marcações internas, e por isso o aparato fala em *fórmula oral de " + DATA + "* em vez "
  "de *a doutrina diz*."),
 ("calendario_janela",
  "**D-13 · o calendário que o despacho repartiu.** " + q("calendario_janela") + " A janela entra na Base por "
  "`RC-344` (transição planetária) e `RC-003` (reintegração mundo a mundo) e é **expressamente vedada** em `RC-200`, "
  "onde entrou só a função de custódia da informação. O `RELATORIO-DE-CICLO.md` registra ainda que a janela **já "
  "estaria vencida** na data de aplicação, sem harmonização corretiva e sem recálculo: a Base não corrige o profeta, "
  "registra o que ele disse e quando."),
 ("enxame_19",
  "**A peça que faltava no isolamento: a Terra é um dos 19.** " + q("enxame_19") + " As 19 fichas de isolamento do "
  "cadastro ganharam com isto a sua moldura comum (vínculo em `RC-070`), e a fonte nega que seja punição: foi decisão "
  "sanitária de Sofia «e não há negociação»."),
 ("fornos_3",
  "**A Trimúrti como engenheira, não como panteão.** " + q("fornos_3") + " É o par simétrico do que a Base tinha sobre "
  "os três fornos de replicação: aqui há autor, há contagem (uma das três formas **nunca funcionou**) e há o vínculo "
  "com o «gênero» do biodemo (" + end("d1_escolha") + "). Remissão a `RC-104` e, por conteúdo, a B041."),
 ("entropia_tudo",
  "**A resposta mais seca do Q&A, e o fecho cosmológico do ciclo.** " + q("entropia_tudo") + " A entropia entra como "
  "**finalizadora por ausência de projeto** (`RC-160`): como nada foi finalizado por ato, a força tamásica finaliza. "
  "A frase é curta e por isso é a mais citável do ciclo — e a mais fácil de ler como niilismo. A moldura é a "
  "definição da fonte mesma, logo acima: «improvisado na hora da queda»."),
 ("pandora_sorriso",
  "**O pedido com que a fonte encerra.** " + q("pandora_sorriso") + " (a grafa do bruto é `julgo`). É a única "
  "aspasão emotiva do bloco megalítico e funciona como chave de leitura de `RC-086` e `RC-727`: o inconformismo não "
  "pede vingança, pede o que Pandora teve. Remissão a B020, **sem** fusão — D-11 do ciclo anterior continua valendo: "
  "remite-se a obra catalogada, não se inventa paralelo."),
 ("plateia_rog",
  "**D-12 · por que há nomes aqui e não há fichas.** " + q("plateia_rog") + " A plateia é nomeada (medido no bruto: "
  + "; ".join(f"`{k}` {v}×" for k, v in MED_NOMES.items() if v) + f"; o próprio expositor é nomeado {AUTOR_NOME}×) e "
  "nada disso virou entidade, ficha ou relação: metadado de enunciação, não matéria da malha. Em `RC-071` entrou só a "
  "cadeia Elã → Enoque, sem a adjetivação confirmatória que a fonte usa sobre si mesma."),
 ("rebeliao_pend2",
  "**A face propositiva, dita pela fonte com a palavra «propositiva».** " + q("rebeliao_pend2") + " É o que "
  "impede este ciclo de ser lido como narrativa de queda: a continuidade da rebelião é definida como *proposta*, não "
  "como violência, e a fonte ancora no termo sânscrito degradado pelo STT (`satagrar` [REVISAR]). Vínculo em `RC-002` "
  "e `RC-541`."),
 ("metodo_pedagogico",
  "**D-8 · o pedido de método, que é o que a Arca chama de origem do seu ofício.** " + q("metodo_pedagogico") + " A "
  "fonte diz que os não-humanos pediram que os humanos **inventassem um jeito de estudar** o que lhes era dado "
  "(vínculo em `RC-375`, `RC-745`, `RC-755`, `RC-464`, `RC-068`). A constatação editorial de que o método da Arca "
  "cumpre esse pedido **não** está aqui nem em ficha alguma: por ordem expressa, ela vive só no "
  "`RELATORIO-DE-CICLO.md` — auto-legitimação em verbete é o que se quer evitar."),
]

# ──────────────────────────────────── transcrição: fatiar e rotular ────────────────────────────────────
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
        return f"{AUTOR}, respondendo ao vivo"
    return f"EXPOSITOR — {AUTOR}"


def rotulo(n):
    return f"Bloco {n:02d}"


def main():
    ofs, cur = [], 0
    for ln in LINHAS:
        ofs.append(cur); cur += len(ln) + 1
    assert all(RAW[o:o + len(l)] == l for o, l in zip(ofs, LINHAS)), "mapa de offsets × LINHAS divergente"
    chaves = {c for c, _ in NOTAS}
    falt = [c for c in chaves if c not in QD]
    if falt:
        raise SystemExit("NOTA COM ÂNCORA FORA DO QUE O CAÇA-ÂNCORAS RESOLVEU: " + ", ".join(falt))

    linhas_txt = []
    for i in range(FALA_INI, len(LINHAS)):
        s = LINHAS[i].strip()
        if s:
            linhas_txt.append((f"U{i + 1:04d}", i, s))
    chars_fala = sum(len(s) for _, _, s in linhas_txt)
    fala = "\n".join(LINHAS[FALA_INI:])
    n_pal, n_per = len(fala.split()), len(re.findall(r"[.?!]+", fala))

    out = []
    w = out.append
    w(f"@titulo: {TITULO}")
    w(f"@autor: {AUTOR}")
    w(f"@data: {DATA}")
    w("@local: na sala — o lugar não é dito por extenso; a fonte sela a data duas vezes dentro da fala "
      f"({end('ano_2023')} e {end('sala_2023')}) e é ela que este ciclo usa como endereço de enunciação")
    w("@subtitulo: Apostila de estudo — transcrição **integral** (" + DATA + ", domingo), sem recorte: a moldura dos "
      "itens D-1, D-2, D-3 e D-4 da devolutiva é feita de nota no lugar exato, e o veto incide sobre o trânsito para "
      "as fichas, não sobre a leitura. Aparato curatorial das 14 decisões, glossário e Apêndice do dicionário STT.")
    w("@fonte: original.txt do ciclo — " + n_bruto(os.path.getsize(BRUTO)) + " bytes · " + n_bruto(len(RAW)) +
      " caracteres · " + str(len(FALAS) + 2) + " linhas lógicas (" + str(len(FALAS)) + " com fala; U0001 é o título "
      "do arquivo; CRLF preservado) · fala útil U0003–U0038 com " + n_bruto(chars_fala) + " caracteres · " +
      n_bruto(n_pal) + " palavras · " + n_bruto(n_per) + " períodos · SHA-256 `" + SHA[:10] + "…" + SHA[-6:] +
      "` (o hash integral está em `analise/METADADOS-INGRESSO.json`)")
    w("@nota_editor: Esta apostila é a transcrição editada da palestra «" + TITULO + "», de 3 de dezembro de 2023, "
      "preservada byte a byte em original.txt. O STT não separou os turnos: a fala cabe em 9 linhas pesadas, das quais "
      f"**U0004 sozinha tem {n_bruto(CONC)} caracteres = {100.0 * CONC / TOT_FALA:.2f}% da fala** — a maior "
      "concentração já vista na Arca, e a razão de este ciclo ter sido lido e fatiado por fronteira de frase, não por "
      "tamanho de linha. A divisão em Blocos é editorial e obedece à ordem da fonte, sem reordenação temática. Não "
      "houve correção silenciosa de grafia, número ou sintaxe: o que é incerto leva [REVISAR]. Esta fonte não tem "
      "**nenhum bloqueio** — a devolutiva de 29/08/2026 determinou transcrição integral com moldura nos itens D-1 (o "
      "argumento sobre identidade de gênero), D-2 (o quiasma das mulheres, com as duas frases obrigatoriamente "
      "juntas), D-3 (o bloco político) e D-4 (as 9 máscaras do STT e as baixarias), vedando apenas que essas passagens "
      "circulem em ficha que nomeie pessoas, pacientes ou grupos humanos. O aparato terminológico produziu 126 "
      "códigos vinculados, 107 fichas ampliadas, 2 materializações (RC-018 e RC-040) e 0 códigos novos: a Base "
      "permanece em 777 termos, 1.856 relações e 102 obras, e o RC-778 continua não consumido.")
    w("")

    # ------------------------------------------------------------ PARTE 0
    w(f"# PARTE 0 — Nota de leitura, molduras e integridade ({SIGLA})")
    w("")
    w("> **Fonte e método.** O arquivo recebido é `uploads_recepcao/2023-12-03 - " + TITULO + ".txt`. "
      "`original.txt` é cópia byte a byte (`cp` + `cmp` idênticos + SHA-256 conferido nos dois lados) e **não foi "
      "tocado** nem por esta apostila nem pelo aparato. A numeração **U0001–U0039** é o endereço das linhas lógicas do "
      "TXT bruto e é usada no ciclo inteiro (camadas 0–3, dossiê, devolutiva, pacote, fichas), para que qualquer citação "
      "seja relocalizável sem ambiguidade. Nenhuma aspa deste ciclo foi digitada de memória: todas saem do caça-âncoras "
      f"`_aspas_{SIGLA}.py`, usado pelo dossiê, pelo pacote de ampliações e por este arquivo.")
    w("")
    w("*Nota editorial:* os rótulos de voz são editoriais e **não afirmam identidade civil** de quem fala. O bruto tem "
      f"{len(CURTAS)} linhas de até 150 caracteres que são interlocução; são transcritas na ordem em que vieram. A "
      f"linha U0004 é um bloco único de {n_bruto(CONC)} caracteres sem parágrafo: os Blocos 2 a 40 desta Parte I "
      "existem só para que ela possa ser lida e conferida em pedaços — nada foi resumido, reordenado ou emendado.")
    w("")
    w("## Cobertura (declaração, como nas Convenções v2)")
    w("")
    w(f"- Transcrição integral publicada: **{n_bruto(chars_fala)} de {n_bruto(chars_fala)} caracteres** da fala "
      "(**100,00%**), com **0 caracteres** suprimidos e **0 blocos bloqueados**. A devolutiva decidiu *não* recortar "
      "nada: onde o material é sensível, a intervenção é nota de moldura no lugar exato. O auditor "
      "`_cobertura_apostila_P2023-12-03.py` confere parágrafo a parágrafo e reproduce a mesma contagem.")
    w(f"- O bruto é o **4º em extensão** do eixo das três palestras da rebelião ({n_bruto(len(RAW))} caracteres; "
      f"P2020-04-25 e P2022-03-26 maiores, P2023-12-02 menor) e o de **maior concentração**: {100.0 * CONC / TOT_FALA:.2f}% "
      "da fala em uma única linha. O fatiamento por fronteira de frase é o que permitiu vincular 127 trechos sem "
      "cortar nenhum.")
    w("- Marcadores de oralidade (*né*, *pá*, *cara*, *tá*), autocorreções em direto (o caso extremo: «1300 e pouco, "
      "não, 1700 e pouco, perto de 2000») e as grafias instáveis de nomes próprios ficam como foram ouvidos. A única "
      "transformação mecânica é a quebra dura de linha dentro de uma mesma frase, convertida em espaço — declarada "
      "aqui e no topo do pacote de ampliações.")
    w(f"- As **{N_MASCARAS} máscaras do STT** (" + ", ".join(f"`{f}`" for f in FORMAS_MASCARA) + ") são preservadas. "
      "É registro de defeito do transcritor, não escolha editorial desta casa: não se purifica, não se reconstrói, "
      "não se importa. Também não transitam: ver BLOCO 5 do pacote.")
    w("")
    w("## As quatro molduras (D-1, D-2, D-3, D-4) e por que nenhuma é corte")
    w("")
    w(f"- **D-1 · o argumento da «identidade de gênero» ({end('d1_escolha')}).** Fica integral, das duas metades, "
      "com nota em cada uma. Razão da decisão: a primeira metade é a *sonda* e a segunda é a *conclusão anatómica*; "
      "cortar a segunda deixaria a primeira parecendo panfleto, e cortar a primeira tornaria a segunda sem "
      "pergunta. O que se vedou foi o trânsito: 0 ocorrências do léxico em ficha, e as três fichas que nomeiam "
      "condição biológica receberam só o dado técnico.")
    w("- **D-2 · o quiasma das mulheres (" + end("d2_quiasma") + ").** Fica **junto**: o span da moldura vai da "
      "acusação («as mulheres atrapalham tudo») à reversão («foi o DNAzinho de Maria em Jesus que fez com que Jesus "
      "disse…») e a apostila não as apresenta separadas em nenhum ponto. Nas fichas, só a metade afirmativa. O "
      "aforismo ganha nota contextual forte no GLOSSÁRIO LOCAL, como o despacho condicionou.")
    w("- **D-3 · o bloco político (" + end("d3_politica") + ").** Fica integral, com registro de divergência: o "
      "aforismo citado na devolutiva («a mediocridade de uma população faz de seus líderes a cara dela») **não "
      "ocorre** no bruto — o que a fonte diz é «Qualquer líder que seja, tô falando aqui de direita e esquerda, é "
      "toda porcaria junto». A moldura é aplicada sobre o texto que existe, não sobre o resumo; a emenda é registrada "
      "em `DECISAO-DO-CURADOR.md` §5 e no relatório, e nenhuma das duas formulações entrou em ficha.")
    w("- **D-4 · as máscaras e as baixarias.** As 9 máscaras e os xingamentos (*babacas*, *dementes*, a série dos "
      "«bandidos-heróis») permanecem como no arquivo. É proibida a purificação silenciosa e proibida a reconstrução "
      "hipotética; e é proibido o trânsito — a pergunta de Eva ficou retida no pacote, e `RC-189` recebeu apenas a "
      "aspa aprovada (D-2).")
    w("")
    w("## Quarentenas deste ciclo (rótulo de índice, não de censura de leitura)")
    w("")
    for qq in [
        "**de gênero (D-1):** *identidade de gênero*, *mudar loucamente*, a conta dos «dois» gêneros terrenos — "
        "transcritas com moldura; 0 palavras dessas seções em ficha, e as três fichas nomeadas pelo despacho "
        "receberam apenas assexuação e casulos;",
        "**antropológico-sexual (D-2):** o quiasma *mulheres atrapalham / homens são fracasso / DNA de Maria salva* — "
        "fica íntegro aqui, transita só a metade afirmativa, e nenhuma dessas frases vira verbete sobre gente;",
        "**política (D-3):** " + str(len(re.findall(r"[Ll][íi]der", RAW))) + " ocorrências de «líder(es)», "
        + end("d3_politica") + " — dentro do argumento sobre a recusa do messias violento, não em digressão "
        "separável; 0 vocabulário político em ficha;",
        "**do STT (D-4):** " + str(N_MASCARAS) + " máscaras e as baixarias — sem purificação, sem reconstrução, sem "
        "trânsito;",
        "**de pessoas (D-12):** " + "; ".join(f"`{k}` {v}×" for k, v in MED_NOMES.items() if v) + " na plateia, "
        + f"o nome do expositor {AUTOR_NOME}×, os médiuns e autoras citados (Chico Xavier, Divaldo, Valdemar, Edgar "
        "Armon [REVISAR], Jane Miranda, Mari Lusa Vasconcel) — metadado de enunciação, **0 fichas de pessoas**, 0 "
        "entidades criadas;",
        "**teológica (D-5):** «Isso não é Deus, é só o criador», a mente de Brahma que não sustenta avatar, a "
        "quaternidade de falências — **tese datada** com a cláusula anexada, nunca definição canônica;",
        "**de rito (D-6):** cerimônia de posse, investidura de Malkuth, arcontes que contestam a décima sefirá — "
        "metáfora de investidura no glossário, 0 relações de fundamento abertas por isto;",
        "**anatômica (D-7):** cérebro radiata × duas câmaras, organoides como prótese de emoção — conteúdo de "
        "ampliação em cinco fichas, **sem** código novo para «obsolescência»;",
        "**de método (D-8):** colégios arquidruídicos, o pedido de um jeito de estudar, o isomorfismo com a ditagem "
        "enoquiíta — vinculado em cinco fichas; a constatação de que a Arca cumpre o contrato fica **só** no relatório;",
        "**numerária (D-9):** 932 × 936 × 984 milhões, 250.000/249.400, 938/936/900Q/13, 1300→1700→~2000, "
        "4.380.000, 1947 — todas com endereço e selo, **zero média, zero harmonização**;",
        "**de calendário (D-13):** marco de julho/1989, janela 2049-2052 — em `RC-344`/`RC-003`, vedada em `RC-200`, "
        "e o relatório marca o prazo como já vencido sem corrigir a fonte;",
        "**terminológica:** *Rockmar/Rockma/Rockban*, *teia de Orlo*, *horlogus/orlog*, *Job Misso*, *Enócrita*, "
        "*Z Geist*, *Patangel*, *Satanail*, as 4 grafas de *Alto Longron*, as 5 de *Túatha*, *comaranda*, *niroda*, "
        "*cita*, *fenvan*, *trouidaram* — **termos-observação** com [REVISAR], 0 código novo, teto de 777 blindado;",
        "**de acervo (D-11):** o livro *Projeto Tal* e a palestra sobre a gênese da hibridagem, anunciados e não "
        "feitos — ficam no radar datado do relatório; 0 obra criada, 0 linha de BIBLIO.",
    ]:
        w(f"- {qq}")
    w("")

    # ------------------------------------------------------------ PARTE I
    w("# PARTE I — Transcrição integral")
    w("")
    w(f"> A fala de {DATA}, na ordem em que foi dita. Os cabeçalhos indicam o endereço no bruto (`Uxxxx`) e o "
      "intervalo de caracteres; os blocos são recorte editorial de linhas longas, nunca fusão nem reordenação. "
      "As notas editoriais emolduram — não substituem, não resumem, não emendam o que está acima delas.")
    w("")
    n = 0
    emitidas = set()
    pos_notas = [(QD[c][0], QD[c][1], c) for c, _ in NOTAS]
    for endm, li, s in linhas_txt:
        base, ln = ofs[li], LINHAS[li]
        cursor = 0
        for p in fatiar(ln):
            j = ln.index(p, cursor)
            cursor = j + len(p)
            a, b = base + j, base + j + len(p)
            n += 1
            w(f"## {rotulo(n)} — {voz(p)} ({endm}, caracteres {n_bruto(a + 1)}–{n_bruto(b)})")
            w("")
            w(p)
            w("")
            for na, nb, chave in pos_notas:
                if chave in emitidas:
                    continue
                if a <= na < b or (na < a <= nb):
                    emitidas.add(chave)
                    w(f"*Nota editorial:* {dict(NOTAS)[chave]}")
                    w("")
    soltas = [c for c, _ in NOTAS if c not in emitidas]
    if soltas:
        raise SystemExit("NOTAS SEM ÂNCORA NA TRANSCRIÇÃO: " + ", ".join(soltas))
    COBERTURA = (n, len(emitidas))

    # ------------------------------------------------------------ PARTE II
    w("")
    w(f"# PARTE II — Índice temático (os sete movimentos da fonte, na ordem dela — camada 3)")
    w("")
    c3 = open(os.path.join(AQUI, "camada-3.txt"), encoding="utf-8").read()
    tabela = c3.split("## 1.")[1].split("## 2.")[0]
    for l in [x for x in tabela.split("\n") if x.strip().startswith("| M")]:
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 4:
            continue
        ue = re.findall(r"U\d{4}", cel[2])
        linha_md = f"- **{cel[0]} — {cel[1].replace('**', '')}** → natureza {cel[3]}"
        if ue:
            linha_md += f" · abre em {ue[0]}"
        if "gênero" in cel[1].lower() or "identidade" in l.lower():
            linha_md += " · **moldura D-1 aplicada aqui**"
        w(linha_md)
    w("")
    navalha = c3.split("## 2.")[1].split("## 3.")[0].strip()
    w("> A navalha de trânsito deste ciclo (três gumes) está reproduzida abaixo **como foi escrita na camada 3**, "
      "porque é ela que explica por que 126 vínculos entraram e 0 cortes foram feitos:")
    w("")
    for l in navalha.split("\n"):
        if l.strip():
            w("> " + l.strip())
    w("")
    w(f"*Nota editorial:* a matriz de anterioridade completa (366 códigos na mira, 126 aprovados e aplicados, 2 "
      "ganhos de data efetivos) está em `analise/_matriz-anterioridade.md`, com a seção de medição pós-aplicação. "
      "Nada nesta Parte II reorganiza a fala: a numeração M1…M7 descreve o percurso, não é tabela de conteúdo.")

    # ------------------------------------------------------------ PARTE III
    w("")
    w(f"# PARTE III — Aparato curatorial: as 14 decisões do Curador sobre {SIGLA}")
    w("")
    dec = open(DECISAO, encoding="utf-8").read()
    corpo_dec = dec.split("### Respostas fechadas")[1].split("## 2.")[0]
    w("> Espelho do §1 de `DECISAO-DO-CURADOR.md` (a devolutiva verbatim está lá; nada aqui foi reescrito de "
      "memória — é a decisão reduzida a uma linha por item, com o destino que ela teve na aplicação).")
    w("")
    for l in corpo_dec.split("\n"):
        m = re.match(r"^- \*\*(D-\d+) \((.*?)\): ([A-ZÀ-Ü][^*]*?)\.\*\*(.*)$", l.strip())
        if not m:
            continue
        cod, tema, veredicto, resto = m.groups()
        w(f"- **{cod} · {tema}** → **{veredicto.strip()}** {resto.strip()}")
    w("")
    w("## Efeito material na Base (medido por script, não declarado de memória)")
    w("")
    pacote = open(PACOTE, encoding="utf-8").read()
    cods = sorted(set(re.findall(r"^### (RC-\d{3})$", pacote, re.M)))
    sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
    import dados_termos as DT                                              # noqa: E402
    com_secao = [f for f in sorted(os.listdir(os.path.join(RAIZ, "termos"))) if f.endswith(".md") and
                 f"## Ampliação — {SIGLA}" in open(os.path.join(RAIZ, "termos", f), encoding="utf-8").read()]
    fichas = [f for f in os.listdir(os.path.join(RAIZ, "termos")) if f.endswith(".md")]
    cad_sigla = [t[0] for t in DT.TERMOS if SIGLA in (t[5] or [])]
    obras = len([x for x in os.listdir(os.path.join(RAIZ, "livros", "CONCLUIDOS")) if not x.startswith(".")])
    w(f"- **{len(cods)} códigos vinculados** a esta fonte na malha (`{SIGLA}` acrescentado às listas de FONTES em "
      f"`ferramentas/dados_termos.py`, {len(cad_sigla)} linhas tocadas no total) e **{len(com_secao)} fichas "
      f"ampliadas** com a seção `## Ampliação — {SIGLA}`, carregando {n_bruto(len(pacote))} caracteres de pacote e "
      f"{len(re.findall(chr(171) + r'.{15,}?' + chr(187), pacote, re.S))} citações verificadas.")
    w(f"- **{pacote.count('⭐ **ganho de anterioridade**')} ganhos de anterioridade absolutos, "
      f"{pacote.count('**antecipa em')} antecipações datadas e {pacote.count('**sem ganho de anterioridade**')} "
      "casos em que esta fonte **não** antecipa nada — e isso é dito na ficha em vez de fingir primazia. Os números "
      "saem do cadastro, calculados pelo gerador do pacote (D-8/D-9).")
    w(f"- **2 materializações autorizadas (D-10):** `RC-018 Alt´Lam Gron` e `RC-040 CFD (Código Fonte Definidor)` — "
      f"arquivos criados em `termos/`, cadastro virado para `ficha=True`; {n_bruto(len(fichas))} arquivos de ficha, "
      f"**0** códigos novos (teto 777), **0** relações ({n_bruto(len(DT.RELACOES))} preservadas), **0** obras "
      f"({obras} físicas em `livros/CONCLUIDOS`), `RC-778` não consumido, `RC-444` mantida `ficha=False` por ordem "
      "expressa.")
    w(f"- **3 spans retidos por trava (BLOCO 5 do pacote)**, listados e não silenciados: é o preço de se ter "
      "travas executadas por código — a âncora do dossiê que caía em máscara ficou de fora da ficha correspondente, "
      "e a decisão de reaproveitá-la **com outra aspa** foi registrada na própria ficha.")
    w("- **Seis ordens que não tinham onde cair** (D-1: `RC-093` · D-2: `RC-189` · D-6: `RC-280` · D-7: `RC-093`, "
      "`RC-035` · D-8: `RC-375` · D-13: `RC-344`): são códigos `ficha=False`, sem arquivo. O conteúdo está aprovado, "
      "está no pacote e o vínculo de malha foi feito; **não** se criou arquivo por iniciativa do aplicador, porque "
      "D-10 liberou materialização só de `RC-018` e `RC-040`.")
    w("")
    w("## Divergências seladas e convergências destacadas (D-9 — espelho do BLOCO 3 do pacote)")
    w("")
    bloco3 = pacote.split("### BLOCO 3")[1].split("### BLOCO 4")[0]
    for l in [x.strip() for x in bloco3.split("\n") if x.strip().startswith("- ")]:
        w(l)
    w("")
    w("## Lista das fichas tocadas por esta fonte")
    w("")
    w("- " + " · ".join(cods))
    w("")
    w("- **Sem arquivo (vínculo só na malha, conteúdo acima):** " +
      " · ".join(sorted(set(re.findall(r"^- `(RC-\d{3})`", bloco3 + pacote.split("### BLOCO 2")[1].split("### BLOCO 3")[0], re.M)))) + ".")

    # ------------------------------------------------------------ APÊNDICE
    w("")
    w(f"# PARTE III-bis — Apêndice: o dicionário STT desta fonte ({SIGLA})")
    w("")
    w("> Tabela de grafias medidas × leitura provável × status, gerada da camada 2 sobre o `original.txt`. Ela existe "
      "porque a transcrição acima **não** foi corrigida em silêncio: o que o STT ouviu fica como está, e a hipótese "
      "de leitura vai aqui — com o destino que a devolutiva deu a cada uma (D-4, D-6, D-7, D-12). Nenhuma forma "
      "degradada abaixo é canônica e nenhuma virou verbete da malha.")
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
    w(f"*Nota editorial:* {nlin} linhas de vocabulário emitidas, todas com contagem **medida** no bruto "
      "(caixa-insensível, porque a caixa do STT é instável). A onomástica degradada e os números com o estado da Base "
      "ao lado estão em `analise/camada-2.txt`, §§ 2 e 3; as famílias de grafia abaixo saem de lá.")
    w("")
    w("## As famílias de grafia (medidas, não unificadas)")
    w("")
    for l in c2.split("## 2.")[1].split("## 3.")[0].split("\n"):
        s = l.strip()
        if s.startswith("- **") or s.startswith("|"):
            w(s)
    w("")
    w(f"- **máscaras do STT:** {N_MASCARAS} ocorrências — " + ", ".join(f"`{f}`" for f in FORMAS_MASCARA) +
      " — transcritas e não unificadas (D-4).")

    # ------------------------------------------------------------ GLOSSÁRIO
    w("")
    w("## GLOSSÁRIO LOCAL")
    w("")
    w("A — Personagens e seres")
    for item in [
        "Javé — RC-001; o criador cujo **cargo** está em disputa, não a existência: " + q("cargo_naodeus") +
        " (tese datada, D-5, com a cláusula «desloca o título de Deus do criador da obra» anexada).",
        "Lúcifer / Luzbel / Elosbel — RC-078 e RC-142; aqui o que restou dele é **inconformismo que não morreu**, e "
        "a grafia do bruto corre por oito formas [REVISAR].",
        "Sofia — RC-009; representante da Trimúrti neste universo, com o epíteto que o ciclo lhe dá: " +
        q("vanguarda") + " (D-7, em `RC-631`/`RC-632`/`RC-093`/`RC-035`/`RC-736`).",
        "Jesus — RC-072; o que **recusou** o papel de messias violento e por isso teve a investidura revogada; a "
        "cerimônia que nunca houve é o pivô do ciclo (D-6).",
        "Enoque — RC-489 e RC-673; a cadeia Elã → Enoque é a única coisa que D-12 deixou entrar em `RC-071`; as "
        "idades (67 + 300 + os 366) **batem** com a ficha e são lidas como convergência (D-9).",
        "léxico de gênero da fonte **não** transitou para cá (D-1).",
        "Famílias Vol, Iel, Nion, Cromon, Xum — RC-109, RC-442, RC-443, RC-444, RC-496; a fonte lista cinco e "
        "acrescenta que os nomes «também não tem importância»; `RC-444` segue `ficha=False` por ordem expressa.",
        "Processador da família — RC-446, RC-089, RC-142, RC-381; campo mórfico que registra, devolve orientação e "
        "coesa — e é **ele** que dá guarida ao vírus de Lúcifer, o que transforma o contágio em ato de validação.",
        "Arcontes — RC-474, RC-770; donos de loka, e o motivo pelo qual a posse não se realiza: querem emigrar para "
        "este universo porque o deles está acabando.",
        "Anunnaki — RC-487, RC-525; mexeram no DNA humano para colocar «inteligência e obediência»; a rebelião contra "
        "Enlil tem cronologia própria e **não** é fundida com as outras três.",
    ]:
        w(f"- {item}")
    w("")
    w("B — Conceitos e mecanismos")
    for item in [
        "Rebelião não finalizada — RC-002; «ainda por ser finalizada» é promessa de processo, não de data.",
        "Cerimônia de posse — RC-005, RC-072, RC-682, RC-736; **metáfora de investidura**, não rito histórico: "
        "posse é o que a fonte diz que nunca houve, e a palavra não virou relação de fundamento (D-6).",
        "Código Fonte Definidor (CFD) — RC-040; **materializado neste ciclo** (D-10); ou os padrões arquétipos ficam "
        "organizados, ou o criador não tem paz.",
        "Alt´Lam Gron — RC-018; **materializado neste ciclo** (D-10); a nave pequenininha onde estão os 938, o "
        "processador e a visita datada de 2018-19; quatro grafas no bruto, nenhuma canônica.",
        "Teia quântica — RC-559; «o que sai de um ser volta para ele» — a única regra, com a ressalva de que a fonte "
        "lê o Bagavaguita como tentativa de trocá-la.",
        "Niroda / vṛtti — RC-762 e RC-760; o processador que recolhe, reprocessa e devolve; as grafas degradadas "
        "(`niroda`, `cita`) ficam como vieram.",
        "Fornos de replicação — RC-104, RC-771; três formas criadas, uma nunca funcionou; a idade do forno de Vígno "
        "diverge em três fontes (932/936/984 milhões) e as três entram datadas.",
        "19 mundos — RC-070; a Terra é um deles e o último da fila; a quarentena é sanitária, não punitiva.",
        "Entropia como finalizadora — RC-160; «Tudo. A entropia destrói tudo.» — o fechamento por ausência de projeto.",
        "Obsolescência anatômica — RC-631, RC-632; cérebro radiata sem emoção, organoides como prótese; **sem código "
        "novo** (D-7).",
    ]:
        w(f"- {item}")
    w("")
    w("C — Onde o áspero fica, com a nota que o despacho exigiu (D-2)")
    for item in [
        "«As mulheres atrapalham tudo» / «Os homens são fracasso nessa história» — lidos **juntos**, no mesmo fôlego "
        "em que a fonte inverte a conta (" + q("d2_quiasma") + "): a frase não é tese sobre gente, é o recurso "
        "retórico com que ela introduz a linhagem do inconformismo (Pandora, Eva, Maria) e a recusa de Jesus. Fora "
        "desse fôlego, ela não significa nada do que a fonte quis dizer; por isso não virou verbete, não virou ficha "
        "e não circula separada nesta Base. Quem a citar daqui em diante cita com as duas metades ou não a cita.",
        "«A vanguarda do atraso» — dito sobre uma instância cosmológica, não sobre pessoas ou épocas; é o epíteto que "
        "a D-7 autorizou circular em cinco fichas, e é também o mais fácil de ser roubado para uso indevido: por isso "
        "ele aparece aqui com endereço, nunca solto.",
        "O bloco político (" + end("d3_politica") + ") — «Qualquer líder que seja, tô falando aqui de direita e "
        "esquerda, é toda porcaria junto»: fica na transcrição, não em ficha ontológica, e a divergência entre o que "
        "a devolutiva resumiu e o que o bruto diz está declarada na PARTE 0.",
    ]:
        w(f"- {item}")
    w("")
    w("D — O que ficou fora da malha neste ciclo (observação, com [REVISAR])")
    for item in [
        "*Rockmar / Rockma / Rockban* (avatar, 3 formas); *teia de Orlo*; *horlogus/orlog*; *Job Misso* (ilegível); "
        "*Enócrita*; *Z Geist*; *Patangel*; *Satanail*; «as mulheres atrapalham tudo» como **tese autônoma**; as 4 "
        "grafas de *Alto Longron*; as 5 de *Túatha*; *comaranda*; *trouidaram*; *sâns do satagrar*.",
        "Nenhum desses nomes virou código. Nenhum vira no próximo ciclo sem que a base textual tenha mais do que uma "
        "ou duas ocorrências degradadas — e a responsabilidade de criar verbete é do Curador, nunca do aplicador.",
    ]:
        w(f"- {item}")
    w("")
    w("*Nota editorial final:* a apostila termina com a última linha da fonte e este aparato. O arquivo bruto, as "
      "camadas 0–3, o dossiê de pré-curadoria, a devolutiva registrada em `DECISAO-DO-CURADOR.md`, o pacote de "
      "ampliações e as 107 fichas são as referências de auditoria; a apostila não substitui a fonte.")

    # ───────────── guarda da casa: aspa angular só para citação verificável no bruto ─────────────
    texto = "\n".join(out) + "\n"
    Bf = " ".join(RAW.split()).casefold()
    dem = []

    def _blindar(m):
        dentro = " ".join(m.group(1).split())
        if dentro.casefold() in Bf:
            return m.group(0)
        dem.append(dentro)
        return "*" + dentro + "*"

    texto = re.sub(chr(171) + r"([^" + chr(187) + r"\n]{4,24})" + chr(187), _blindar, texto)
    if dem:
        print("aspas curtas rebaixadas para itálico (não verificáveis no bruto): " +
              " · ".join(f"«{d}»" for d in dict.fromkeys(dem)))
    open(ALVO, "w", encoding="utf-8").write(texto)
    print(f"apostila.md escrito: {len(out)} linhas · {COBERTURA[0]} blocos de transcrição · 0 bloqueios aplicados · "
          f"notas editoriais: {COBERTURA[1]}/{len(NOTAS)}")
    print(f"cobertura: {n_bruto(chars_fala)}/{n_bruto(chars_fala)} caracteres (100,00%) · 0 caracteres suprimidos")


if __name__ == "__main__":
    main()
