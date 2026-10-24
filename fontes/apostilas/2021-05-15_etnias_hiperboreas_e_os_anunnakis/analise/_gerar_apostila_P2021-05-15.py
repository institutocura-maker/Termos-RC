#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera `apostila.md` do ciclo P2021-05-15 a partir do `original.txt` (byte a byte).

Por que um gerador e não redação direta: a apostila é **transcrição integral**. Digitar
106.835 caracteres à mão é convite a "melhorar" o autor. Aqui o texto da fala é
recortado do bruto; o que eu escrevo são só os rótulos de bloco, as notas editoriais
(verdes) e os aparatos. Regras do rito cumpridas por construção:

 - a ORDEM da fonte é preservada (nenhum trecho é reordenado por conveniência temática);
 - os marcadores de oralidade e os truncamentos ficam como estão (nenhuma correção silenciosa);
 - as falas de plateia/mediação são ISOLADAS por rótulo (linhas curtas do Q&A);
 - o desabafo pessoal (U0018) sai SUBSTITUÍDO por marcador declarado — bloqueio aprovado
   na Devolutiva O-5; a retenção em bloco (política, islã) fica no texto com NOTA verde;
 - o glossário usa remissão RC-### (o builder confere o código).
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
# RAIZ: sobe até o diretório que contém `ferramentas` (funciona antes e depois do engavetamento em CONCLUIDAS/)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
LINHAS = open(os.path.join(CICLO, "original.txt"), encoding="utf-8").read().replace("\r\n", "\n").split("\n")
ALVO = os.path.join(CICLO, "apostila.md")

TITULO = "As Etnias Hiperbóreas e os Anunnakis"
SIGLA = "P2021-05-15"
BLOCO_ALVO = 2000          # caracteres por bloco de leitura (cortado no fim de frase)

BLOQUEIO = (  # decisão O-5: vida privada, não transcrita — marcador declarado no lugar
    ("Que coisa boa. Só assim eu paro.", "só fiz me ferrar."),
)
NOTAS = [  # (âncora no texto da fonte, nota verde) — a nota entra logo após o bloco que a contém
    ("Não esqueçam de dar o desconto",
     "O «desconto» pedido pelo expositor é parte da moldura da fala: ele anuncia que o material é "
     "instável e pede indulgência. Nada aqui é afirmação verificada pela Base; é registro do que foi dito."),
    ("são seis, basicamente, as principais parcelas",
     "A taxonomia de seis componentes é a espinha dorsal desta palestra e a formulação mais completa que "
     "existe no acervo sobre o tema (ver RC-068). A fonte mesma avisa que «na verdade não são só seis»."),
    ("a turma de Alto Langron continuou existindo",
     "Quarentena biográfica/institucional: a passagem localiza um grupo numa ilha móvel pós-diluviana. "
     "A resolução do rótulo «ALTA LANGRON» (→ Alt'Lam Gron, RC-018) é **decisão do Curador** (Devolutiva O-8), "
     "não demonstração do agente — e «Alto Langron» fica vedado como sinônimo canônico."),
    ("ao fundar o islamismo",
     "**Retenção em bloco aprovada (Devolutiva O-5).** A afirmação sobre o islã e sobre a «maior marca do campo "
     "mórfico» pertence ao expositor, incide sobre religião viva e **não** entra em termo, epígrafe ou glossário. "
     "Publica-se o texto porque a transcrição é integral; o juízo não é endossado."),
    ("doutrinas políticas absurdas",
     "**Retenção em bloco aprovada (Devolutiva O-5).** Juízo político conjuntural de maio de 2021; sem valor "
     "terminológico, sem partido, sem candidato. Mantido na transcrição, bloqueado para a Base."),
    ("Então não há plano B. Deus ao diabo",
     "Alerta de precisão aceito pelo Curador: esta fórmula é **metafísica do autor**, citada como tal. "
     "Não vira epígrafe, título nem síntese de doutrina da Base."),
    ("Só que o Adão bíblico viveu quase 1000 anos",
     "O paralelismo Adão (930 anos) × Adapa (vida curta) é o argumento da sabotagem genética. A Base mantém as "
     "datções seladas por fonte: Pandora ~49.000 e Eva/Adão ~22–23.000 [P2025-02-22] — **não fundidas** com esta fala."),
    ("não há livro nenhum do mundo e nunca mais",
     "Declaração de impossível documental: é o fundamento curatorial de se tratar esta fala como fonte primária "
     "de um bloco temático (ver RC-068). Não é afirmação sobre acervos reais."),
]

# ---------------------------------------------------------------- helpers
def fatiar(texto):
    """Divide em blocos de leitura cortando no fim de frase mais próximo do alvo."""
    blocos, i = [], 0
    while i < len(texto):
        fim = min(len(texto), i + BLOCO_ALVO)
        if fim < len(texto):
            corte = max(texto.rfind(". ", i + 600, fim), texto.rfind("? ", i + 600, fim),
                        texto.rfind("! ", i + 600, fim))
            if corte > 0:
                fim = corte + 1
        blocos.append(texto[i:fim].strip())
        i = fim
    return [b for b in blocos if b]


def voz(linha):
    s = linha.strip()
    if len(s) <= 320:
        return "INTERLOCUTOR / PLATEIA"
    if s.startswith(("OK. Eh, próxima", "Só um minutinho")):
        return "EXPOSITOR E MEDIAÇÃO"
    return "EXPOSITOR — Jan Val Ellam"


def rotulo(n):
    return f"Bloco {n:02d}"


# ---------------------------------------------------------------- corpo
def main():
    u3 = LINHAS[2]
    u5 = LINHAS[4]
    qa = [(f"U{i+6:04d}", LINHAS[i + 5]) for i in range(len(LINHAS) - 5) if LINHAS[i + 5].strip()]

    # bloqueio declarado do desabafo (só na fala do U0018)
    n_bloqueios = 0
    qa2 = []
    for end, linha in qa:
        for ini, fita in BLOQUEIO:
            a, b = linha.find(ini), linha.find(fita)
            if a >= 0 and b > a:
                linha = (linha[:a] +
                         "[TRECHO BLOQUEADO POR DECISÃO DO CURADOR — O-5: conteúdo de vida privada do "
                         "expositor, preservado apenas como nota de existência em `analise/camada-2.txt`]" +
                         linha[b + len(fita):]).strip()
                n_bloqueios += 1
        qa2.append((end, linha))
    qa = qa2

    out = []
    w = out.append
    w(f"@titulo: {TITULO}")
    w("@autor: Jan Val Ellam")
    w("@data: 15/05/2021")
    w("@local: [REVISAR — o cabeçalho da transcrição não traz local; a agenda interna anuncia o tema para o dia seguinte]")
    w(f"@subtitulo: Apostila de estudo — transcrição integral (sábado, {SIGLA}), plateia isolada, aparato terminológico RC e glossário.")
    w(f"@fonte: original.txt do ciclo — 110.198 bytes · 106.835 caracteres · 20 linhas lógicas (U0001–U0020) · SHA-256 57f8e002f830a9226d8b557c642dd6a1e1c475e0c10738e62aa888825417bec4")
    w("@nota_editor: Esta apostila é a transcrição integral e editada da palestra «As Etnias Hiperboreas e os Anunnakis», de 15 de maio de 2021, preservada byte a byte em original.txt. O monólogo inteiro vem numa única linha do arquivo de STT (U0003, 71.574 caracteres), com o intervalo de café embutido; por isso a divisão em Blocos é editorial e obedece à ordem da fonte, sem reordenação temática. Não houve correção silenciosa: grafias oscilantes de nomes, repetições, truncamentos e frases sem fecho sintático aparecem como foram ouvidas, e o que é incerto leva [REVISAR]. Três decisões do Curador (Devolutiva O-5, de 28/08/2026) estão aplicadas aqui: a retenção em bloco dos juízos sobre religião e política (transcritos, não endossados, sem gerar termo) e o bloqueio do trecho de vida pessoal do expositor em U0018, substituído por marcador. O aparato terminológico desta fonte produziu 54 fichas ampliadas e a materialização de RC-464 (Inanna = Danu), sem nenhum código novo: a Base permanece em 777 termos e 1.856 relações, e o RC-778 continua não consumido.")
    w("")

    w(f"# PARTE 0 — Nota de leitura e integridade ({SIGLA})")
    w("")
    w("> **Fonte e método.** O cabeçalho recebido é “2021-05-15 - As Etnias Hiperboreas e os Anunnakis”. "
      "`original.txt` permanece byte a byte (SHA-256 no alto deste arquivo); a apostila só altera derivados. "
      "A numeração U0001–U0020 é o endereço das linhas lógicas do TXT bruto e é usada em todo o ciclo "
      "(camadas, dossiê e fichas) para que qualquer citação seja relocalizável sem ambiguidade.")
    w("")
    w("*Nota editorial:* os rótulos “EXPOSITOR”, “INTERLOCUTOR / PLATEIA” e “EXPOSITOR E MEDIAÇÃO” são "
      "editoriais: servem para tornar visíveis as camadas de voz, não afirmam identidade civil de quem fala. "
      "Nesta fonte o Q&A não veio separado por falante — quando a pergunta e a resposta estão no mesmo "
      "parágrafo, a linha inteira é mantida como está, com o aviso acima.")
    w("")
    w("## Cobertura (declaração, como nas Convenções v2)")
    w("")
    w(f"- Transcrição integral publicada nesta apostila: **100% do conteúdo da fonte**, exceto o trecho "
      f"de vida pessoal bloqueado por decisão curatorial ({n_bloqueios} marcação(ões), declarada no próprio local).")
    w("- Nada foi resumido para “melhorar a leitura”; a segmentação em blocos apenas repõe parágrafos que o STT não tinha.")
    w("- Marcadores de oralidade («eh», «né», repetições, números com vírgula trocada) e as grafias instáveis de nomes próprios foram preservados.")
    w("")

    w("# PARTE I — Transcrição integral")
    w("")
    n = 0
    emitidos_notas = set()
    for k, bloco in enumerate(fatiar(u3)):
        n += 1
        ini = k * BLOCO_ALVO
        w(f"## {rotulo(n)} — EXPOSITOR — Jan Val Ellam (U0003, caracteres {ini + 1}–{ini + len(bloco)})")
        w("")
        w(bloco)
        w("")
        for ânc, nota in NOTAS:
            if ânc in bloco and ânc not in emitidos_notas:
                emitidos_notas.add(ânc)
                w(f"*Nota editorial:* {nota}")
                w("")
    n += 1
    w(f"## {rotulo(n)} — EXPOSITOR — retomada após o intervalo (U0005)")
    w("")
    for b in fatiar(u5):
        w(b); w("")
    for ânc, nota in NOTAS:
        if ânc in u5 and ânc not in emitidos_notas:
            emitidos_notas.add(ânc); w(f"*Nota editorial:* {nota}"); w("")
    w("## Q&A — as falas de plateia não são apêndice")
    w("")
    for end, fala in qa:
        w(f"### {rotulo(n + 1)} ({end}) — {voz(fala)}")
        n += 1
        w("")
        partes = fatiar(fala) if len(fala) > BLOCO_ALVO else [fala]
        for p in partes:
            w(p); w("")
        for ânc, nota in NOTAS:
            if ânc in fala and ânc not in emitidos_notas:
                emitidos_notas.add(ânc); w(f"*Nota editorial:* {nota}"); w("")
    w(f"*Nota editorial:* as notas não fixadas acima ({', '.join(a for a, _ in NOTAS if a not in emitidos_notas)}) "
      "não correspondem a bloco desta apostila — registradas apenas no dossiê do ciclo.")

    # ---------------------------------------------------------- PARTE II — índice temático
    w("")
    w("# PARTE II — Índice temático (o que a camada de análise marcou, sem reordenar a fonte)")
    w("")
    cam = open(os.path.join(AQUI, "camada-1.txt"), encoding="utf-8").read()
    temas = re.findall(r"^## (\d+)\. (.+)$", cam, re.M)
    chaves = {"1": "desconto", "2": "seis, basicamente", "3": "cataclismo", "4": "reverenciado",
              "5": "Danana", "6": "CPH4", "7": "radiata", "8": "pamixia", "9": "Adão bíblico",
              "10": "colégio druídico", "11": "não há livro nenhum", "12": "inquisição espiritual",
              "13": "Primeira pergunta", "14": "não há plano B", "15": "revelação cósmica"}
    corpo = u3 + "\n" + u5
    total_blocos = n
    for num, nome in temas:
        chave = chaves.get(num, "")
        onde = ""
        if chave:
            alvos = [i for i in range(1, total_blocos + 1)]
            pos = corpo.find(chave)
            if pos >= 0:
                bn = pos // BLOCO_ALVO + 1
                onde = f" — abre no {rotulo(max(1, min(bn, total_blocos)))}"
            elif any(chave in f for _, f in qa):
                onde = " — no Q&A"
        w(f"- **{num}. {nome.strip()}**{onde}")
    w("")
    w("*Nota editorial:* o índice é um aparelho de leitura. A numeração dos blocos acima é aproximada por "
      "construção (corte em fim de frase), e serve para localizar, não para citar; a citação rigorosa usa U00xx "
      "e a posição em caracteres.")

    # ---------------------------------------------------------- PARTE III — aparato curatorial
    w("")
    w(f"# PARTE III — Aparato curatorial: o que {SIGLA} mudou na Base RC")
    w("")
    pacote = open(os.path.join(AQUI, "_ampliacoes_P2021-05-15.txt"), encoding="utf-8").read()
    cods = re.findall(r"^### (RC-\d{3})$", pacote, re.M)
    w(f"- **{len(cods)} fichas ampliadas**, uma seção `## Ampliação — {SIGLA}` em cada, com a citação recortada "
      "byte a byte do `original.txt` e o endereço U00xx.")
    w("- **Ficha nova: RC-464 — Inanna (= Danu; Anunnaki)**, materialização autorizada de código que só existia "
      "no cadastro [B060]. Fichas: 450 → 451.")
    w("- **0 termos novos** (tetos mantidos: 777 termos · 1.856 relações · 102 obras · RC-778 intocado). "
      "Memete, Pamíxia, CPH4, Thule, Aesir/Vanir, Tuatha de Danann, Milesianos, Adapa, Isar e Nibiru-cifras "
      "ficam como termos-observação ou absorvidos nas fichas indicadas.")
    w("- **Vínculo de fonte** `'P2021-05-15'` em 63 códigos do cadastro: os 54 com ficha + 9 termos sem arquivo "
      "físico que têm conteúdo próprio nesta fonte (precedente: RC-385 no ciclo P2023-06-24).")
    w("- **Divergências seladas, nunca fundidas:** 400 milhões (fonte) × 300 milhões (B050) para o Ragnarok em Marte; "
      "«28.879 genes» (fonte) × 28.869 (canônico, RC-562); retorno a Nibiru «2600 anos atrás» × «por volta de ~600 a.C.» "
      "[P2021-03-27]; «900, 1 bilhão de anos» qualifica aqui o **encontro dos fornos**, não o Homo sapiens; "
      "11.000 anos [P2021-01-23] × cataclismo 14/13/12.000 (esta fonte) para o bloco Tuatha × Milesianos.")
    w("- **Anterioridades registradas sem retrodatação:** a formulação dos Fornos Replicadores (RC-771/RC-499), a tese "
      "dos organoides para Sophia (RC-632), a poluição vibratória (RC-751) e o anúncio da «Inquisição Espiritual» "
      "(RC-617) aparecem aqui **antes** das fichas que as consagraram; as fichas não foram re-datadas.")
    w("- **Retificações declaradas do próprio agente:** quatro âncoras erradas no dossiê (Javé é RC-001, não RC-010; "
      "o selo dos genes é RC-562; «Hibridação» é RC-516; «Campo Morfogenético» não existe na Base) e **seis citações "
      "que esta fonte não contém**, retiradas antes de aplicar (a do «decalque» espiritual; a dos «espíritos que "
      "vivenciaram isso»; a dos «filhos de Anu a favor de Javé» — o que esvazia o T-13; a do «filho de Afrodite»; "
      "a dos «mais próximos de Sofia»; e a etimologia «Druid = busca pela verdade»).")
    w("- **Radar de acervo:** a palestra anunciada para o dia seguinte («os protocolos da mente e o quarto cérebro», "
      "domingo 16/05/2021) e as cinco auto-referências internas ficam declaradas **fonte não localizada**, sem vínculo.")
    w("")
    w("## Lista das fichas ampliadas")
    w("")
    for c in cods:
        w(f"- {c}")
    w("")
    w("## Quarentenas aplicadas neste ciclo (rótulo de índice, não de censura de leitura)")
    w("")
    for q in ["política (juízo conjuntural de maio/2021)", "teológica (Deus ao diabo, caso exista — só como citação)",
              "clínica/biomediúnica (psicosfera, bagagem vibratória, turma que se poupou de encarnar)",
              "ufológica (naves, Marte e Lua, cientistas que conversam “com a Nunx escondido”)",
              "histórica (a «biblioteca de Nínive» e as datas de Sitchin/Hancock)",
              "institucional e biográfica (o desabafo bloqueado; a ilha que se move)",
              "ética (#QUARENTENA-ÉTNICA: «tipo ideal» das 72 etnias — descrição da fala, não classificação)"]:
        w(f"- {q}")

    # ---------------------------------------------------------- APÊNDICE — dicionário STT
    w("")
    w("# PARTE III-bis — Apêndice: o dicionário STT desta fonte")
    w("")
    w("> Este apêndice é a tabela de grafias ouvidas × forma canônica da Base, gerada da camada 2 do ciclo. "
      "Ele existe porque a transcrição acima **não** foi corrigida em silêncio: o que o STT ouviu fica como está, "
      "e a leitura do nome vai aqui, com o destino decidido.")
    w("")
    c2 = open(os.path.join(AQUI, "camada-2.txt"), encoding="utf-8").read()
    linhas_tabela = [l for l in c2.split("\n") if l.strip().startswith("|")]
    cab = [l for l in linhas_tabela if set(l.replace("|", "").strip()) <= set("-: ")]
    for l in linhas_tabela:
        s = l.strip()
        if not s.startswith("|") or s in cab or re.match(r"^\|\s*Grafia", s, re.I) or set(s.replace("|", "").strip()) <= set("-: "):
            continue
        cel = [re.sub(r"\*\*", "", c).strip() for c in s.strip("|").split("|")]
        if len(cel) < 5:
            continue
        w(f"- **{cel[0]}** — {cel[1]} ocorrência(s) → **{cel[2]}** [{cel[3]}] · {cel[4]}")
    w("")
    w("*Nota editorial:* as contagens de ocorrência são as medidas na camada 2 sobre o `original.txt` (não sobre a "
      "apostila); «» no texto da tabela são rótulos de tabela, não aspas de fala.")

    # ---------------------------------------------------------- GLOSSÁRIO
    w("")
    w("## GLOSSÁRIO LOCAL")
    w("")
    w("A — Personagens e seres")
    for item in [
        "Anunnakis — RC-024; «os anuna não são farinha do mesmo saco».",
        "Anu — RC-587; o mais reverenciado nas ilhas hiperbóreas; visita “cada cerca de 3600 anos”.",
        "Inanna = Danu — RC-464; neta e amante de Anu; «toatas quer dizer seguidores».",
        "Enki — RC-486; FOXP2 para “aprender a linguagem dos Anunax”; criação racionalizada.",
        "Enlil — RC-487; na fonte as duas grafias se fundem (“Enquenil”).",
        "Ninmah — RC-461; irmã-co-autora da criação racionalizada.",
        "Marduk — RC-460; «briga com Mardur» como origem das bombas.",
        "Sophia — RC-009; 1ª biodemo, cérebro radiata, sem osso.",
        "Biodemos — RC-036; protótipos sem osso; retirada pós-dilúvio na ilha que se move.",
        "Demos — RC-049; herança que inviabiliza; ausência de dualismo moral.",
        "Pandora — RC-086; racionalizada em alto nível antes de se fazer humana.",
        "Hefesto — RC-307; abre o genoma de Pandora (“transição de fase”).",
        "Epimeteu — RC-302; as beberagens-poção como banco de sequências.",
        "Prometeu — RC-301; o fogo que recicla e informationa.",
        "Eva (figura) — RC-189; «atrapalhou Javé e usou Eva e Lilif» (quarentena teológica).",
        "Javé — RC-001; fecha a pamíxia; «a roda que Javé criou funciona por ela mesma».",
        "Ostronomos — RC-232; prestígio nas ilhas; a palavra também designa astrônomos humanos na mesma fonte.",
        "Ganesha — RC-756; a “caneta especial” e a tradução para os gandarvas.",
        "Vyasa — RC-585; o primeiro a sistematizar uma mesma história.",
        "Trimurti — RC-104; «nunca colocaram o pé» nas ilhas.",
        "Shiva/Savna — RC-102; administrador do segundo forno nesta fala.",
        "Quarto Logos — RC-092; «comando prático» e coordenação.",
    ]:
        w(f"- {item}")
    w("")
    w("B — Conceitos")
    for item in [
        "Hiperbórea — RC-068; as 72 etnias, as 14 caravanas, o cataclismo e o «livro impossível».",
        "Guerra Nuclear Anunnaki — RC-583; «Vale do Sinai e Vale do Sidim»; autoexílio por contaminação.",
        "Nibiru — RC-589; órbita relativizada pelo próprio autor; a observação humana ainda não decide.",
        "Ragnarok em Marte — RC-395; a fonte diz 400 milhões de anos.",
        "Cérebro Radiata — RC-631; o limite arquitetural dos deuses.",
        "Organoides para Sophia — RC-632; única via prática declarada em 2021.",
        "Fornos Replicadores — RC-771 e RC-499; o encontro dos produtos e o cérebro bilatério.",
        "Bagagem Espiritual Intransferível — RC-751; poluição vibratória e «vista grossa».",
        "Inquisição Espiritual — RC-617; nome provisório do livro anunciado em 2021.",
        "Colegiados Espirituais Humanizados — RC-745; a «banca espiritual de resistência».",
        "Escola da Decifração da Realidade — RC-755; do colégio druídico à busca da verdade.",
        "Jainismo (antigo Druidismo) — RC-759; o bloco Tuatha × Milesianos.",
        "Mente Coletiva / Redes Psíquicas — RC-188; «a sequência da internet humana, que eu chamo Memete».",
        "Big Data Cósmico — RC-194; assinatura quântica e o mapa das últimas 10 encarnações.",
        "Hibridização genética — RC-516; pamíxia como regime; o sexo e o laboratório.",
        "Especiação — RC-056; a dieta que permitiria especiar.",
        "Jabutis Genéticos — RC-729; «as 100.000 maluquiças dos laboratórios».",
        "Quarto Cérebro Humano — RC-614 e RC-758; a reserva cortical de 2021 antes da fórmula de 2026.",
        "Taumaturgia Genético-Química — RC-713; CPH4 como enzima do sexto mês.",
        "Genes Críticos / Dorminhocos — RC-710; o crânio como invólucro do que importa.",
        "Baralho genético — RC-562; a fonte grafa 28.879.",
        "Isolamento Cósmico — RC-070; “o isolamento faz com que continuemos desconhecidos”.",
        "Entropia e Negentropia — RC-160; “só a certeza da entropia”.",
        "Reintegração Cósmica — RC-003; os que esperam o fim do isolamento.",
        "Segundo Advento / Vinda — RC-005; a assunção da posse, sem garantia.",
        "Falência dos Deuses — RC-742; incompetência declarada de dentro da disputa.",
        "Mahabharata — RC-593; “Ramaiana, Marrabarata” na grafia ouvida.",
        "Protocolo Mental — RC-517; só a circulação do sintagma “protocolos da mente” em 2021.",
    ]:
        w(f"- {item}")
    w("")
    w("C — Livros, referências e fontes externas")
    for item in [
        "Lucy (2014, Luc Besson) — **sem termo e sem obra na Base**; a régua dos 100% e a droga do filme, separadas da enzima real. [RETIFICAÇÃO: o piloto do ciclo ligou o filme a B036, que é «As Memórias de Javé» — engano desfeito aqui e em camada-2.]",
        "B060 — obra primária da linhagem anunnaki; de lá vem o cadastro de Inanna = Danu.",
        "B031 — Painéis Emergentes; o vocabulário das grafias.",
        "B087/B088/B089 — Pandora, Epimeteu e a revolta; o bloco grego desta fala.",
        "“Bibliotecas da antiga capital de Min / Nínive” e «a lenda de Adapa» — referência erudita nomedada pelo expositor; [REVISAR] a grafia do topônimo.",
        "Zacarias/Sitchin, Graham Hancock, “Robert Bv”, NASA, Plutão, Sedna, nuvem de Oort — radar externo, quarentena científica e ufológica; nada vira obra nem termo.",
        "A palestra de domingo 16/05/2021 («os protocolos da mente e o quarto cérebro») — anunciada e **não localizada** no acervo; busca prioritária.",
    ]:
        w(f"- {item}")
    w("")
    w("D — Grafias, variações e incertezas")
    for item in [
        "Thule: «Tul», «Thu», «Tool», «Tur» — formas ouvidas; **não** cadastradas.",
        "«continente de Lu» ≈ Lemúria/MU — **não há termo MU nem Lemúria na Base** (o que existe é RC-010 «Atlântida / Terra Atlantis», ficha=False, que esta fonte não toca); menção apenas.",
        "«Demobio», «Demobil», «Demobiol», «biodemos» — três estirpes + os biodemos; **não fundir** (decisão curatorial).",
        "«Aáon», «Aamaion», «Virgno», «Morrenç», «Pachu Pathiba», «Hawaiingan» — instabilidade de STT da família dos Fornos; nenhuma grafia da Base foi alterada.",
        "«Brama, Virgem e Chiva» — Trimúrti como ouvida; os nomes canônicos permanecem.",
        "«Alto Langron» → **Alt'Lam Gron (RC-018) / Alt'Lam (RC-017)** — resolução do Curador; vedado como sinônimo canônico.",
        "«ISAR» ≈ Ishtar; «noada» = Nuada; «Apólogo» ≈ Apolo; «o povo» = o polvo; «a Nunx» = os Anunnaki — todos [REVISAR], sem decodificação.",
        "«pamixia / ponixia / Pamixia» — o regime sem código; «Memete» — a internet humana, sem código; «CPH4» — enzima do filme e da fala, sem código.",
        "«50.0000 anos», «13 bi» e demais cifras truncadas do STT ficaram como estão; a Base não “conserta” número de fonte oral.",
    ]:
        w(f"- {item}")
    w("")
    w("*Nota editorial final:* a apostila termina com a última fala da fonte (U0018) e este aparato. O arquivo bruto, "
      "as camadas 0–3, o dossiê, a devolutiva registrada em `DECISAO-DO-CURADOR.md` e as fichas são as referências de "
      "auditoria; a apostila não substitui a fonte.")

    open(ALVO, "w", encoding="utf-8").write("\n".join(out) + "\n")
    cob = sum(len(b) for b in fatiar(u3)) + len(u5) + sum(len(f) for _, f in qa)
    print(f"apostila.md escrito: {len(out)} linhas · {n} blocos de transcrição · cobertura ≈ {cob} chars de {len(u3) + len(u5) + sum(len(f) for _, f in qa)}")
    print("notas editoriais aplicadas:", len(emitidos_notas), "de", len(NOTAS))
    print("bloqueios:", n_bloqueios)


if __name__ == "__main__":
    main()
