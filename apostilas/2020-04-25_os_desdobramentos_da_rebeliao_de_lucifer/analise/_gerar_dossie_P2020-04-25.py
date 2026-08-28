#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md de P2020-04-25.

Princípio (herdado de P2023-10-14, R-1…R-7): **nenhuma aspa digitada à mão.** Cada citação
é recuperada do `original.txt` pelo caça-âncoras, byte a byte, estendida a fronteiras de
frase, e o gerador aborta se qualquer âncora não bater exatamente uma vez. Assim o dossiê
não pode conter frase «lembrada» — ou ela está na fonte, ou o arquivo não é escrito.
"""
import os, re, sys, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, "_aspas_P2020-04-25.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)

# ---------------------------------------------------------------- aspas (chave: (âncora, fim|None))
Q = {
 "abertura_politica": ("Antes da palestra do Rogério, tem alguns comentários", None),
 "gasto_declarado":   ("Eu vou então gastar aqui 5 a 10 minutos", None),
 "tit_glosado":       ("vamos então tratar da do tema da nossa palestra de hoje à tarde", None),
 "tema_glosado":      ("E antes de falar do tema da nossa palestra", None),
 "niets":             ("Niets dizia que quando você olha", None),
 "138":               ("Ao longo desses 13.8 bilhões de anos", None),
 "abismo_metaforico": ("O abismo é metafórico, não é literal", None),
 "rebeliao_nao_foi":  ("A rebelião de Lúcifer não foi porque I Luzbell", None),
 "coronavirus_epoca": ("um coronavírus da época", None),
 "virus_aspas":       ("eu sempre colocava vírus entre aspas", None),
 "escola_capela":     ("a escola que surgiu não entre aspas, recentemente lá nos mundos de capela", None),
 "biodemos_casulo":   ("os biodemos são seres que foram engendrados em casulos", None),
 "biodemos_900ma":    ("cerca de 900 milhões de anos atrás", None),
 "pandora_susto":     ("A primeira vez que Jaavé tomou um susto", None),
 "oraculo_vicio":     ("criaram o vício oracular", None),
 "travas_geneticas":  ("travas genéticas de controle que eles haviam colocado", None),
 "humano_abismo":     ("Então eu tô tentando dizer para vocês que nós", None),
 "capila_esildo":     ("Os dois primeiros seres humanos que fizeram isso foram", None),
 "ia_abismo_hoje":    ("O que é hoje o grande abismo para esses seres", None),
 "sheldrake_7":       ("Rupert Shellrake", None),
 "sexto_sentido":     ("O budismo diz que além desses cinco sentidos", None),
 "capila_mente_una":  ("Capila foi o primeiro a falar", None),
 "mentalma_8":        ("eu só vou dar cinco, talvez seis", None),
 "unica_raca_abismo": ("somos a única raça do universo", None),
 "abril2020":         ("mês de abril do ano 2020", None),
 "guerra_jesus":      ("Ele entrou em guerra com Jesus", None),
 "livro_com_jave":    ("Tô escrevendo um livro com o próprio", None),
 "evangelhos_gnosticos": ("Tô traduzindo uns três ou quatro evangelhos gnósticos", None),
 "eu_de_jave_virus":  ("O vírus é o eu de J", None),
 "genero_familia":    ("A definição de gênero deles é é quase que por família", None),
 "radiata_bilat":     ("foi quando eles resolveram juntar esses dois hemisférios", None),
 "genero_espírito":   ("gênero é só macho fêmea?", None),
 "jave_bateu":        ("Javé bateu duro nas mulheres e nos homoafetivos", None),
 "cobaias":           ("Nós humanos somos cobaias", None),
 "amam_os_homfetivos": ("As que melhor conseguem", None),
 "anjos_rastreamento": ("uma vez eu conversando com os anjos dele nas confusões dos anos 2009", None),
 "ovo_cosmico":       ("como um ovo, um ovo cósmico", None),
 "cenario_ia":        ("inteligência artificial autônoma controlada é um corpo máquina", None),
 "computador_eu":     ("O computador se dizer", None),
 "familia_val_736":   ("não chega a 800", None),
 "val_620mil":        ("chegou aqui a 620.000 anos, ficou um bom tempo na nave", None),
 "qg_64mil":          ("Há cerca de 64.000 anos", None),
 "anos_22mil":        ("22.000 anos. Dos 1641 seres", None),
 "alto_langron":      ("hoje existe a Turma Biodêmica lá em Alto Langron", None),
 "sofia_2018":        ("Sofia pass Passou o ano 2018", None),
 "shanai":            ("pediram para eu inventar uma palavra", None),
 "especies_429":      ("espécieval era 429.314", None),
 "prazo_18mil":       ("essa definição vai ter que se dar", None),
 "confianca_zero":    ("Esse eu de Jahvel para mim é zero", None),
 "medius_ordem":      ("o que eu mais recebi desse ser através de médiuns", None),
 "marco_zero":        ("hoje é o marco zero que surgiu", None),
 "oxitocina":         ("mergulhar na condição animal para poder encontrar brecha", None),
 "criptura_universal": ("a chamada última espécie do universo", None),
 "gnose_vinganca":    ("a turma da gnose envzada", None),
 "grau_testemunho":   ("pelo que eu julgo, entre aspas, saber", None),
 "pergunta_processador": ("pergunta do Augusto Melo", None),
 "resposta_processador": ("processador da espécie biodêmica que se vincula ao cérebro de Sofia", None),
 "campo_morfico_humanos": ("vinculados ao campo mórfico da nossa espécie", None),
 "abelhas_genetica":  ("a genética das abelhas operárias", None),
 "divina_commedia":   ("Divina Commeia", None),
 "genealogia_livros": ("anos 96, 97, 98", None),
 "valeno":            ("tive contato com Valeno", None),
 "trilogia_atlantis": ("comecei a trilogia Terra Atlântic", None),
 "pergunta_fatiamento": ("A Solange Silva pergunta", None),
 "fatiamento_assunto_mais_serio": ("esse fatiamento de consciência é o assunto mais sério", None),
 "para_bragina":      ("erro que para Bragina cometeu", None),
 "tamas_entropia":    ("energia tamásica é o selo de garantia", None),
 "big_crunch_tempo":  ("a expansão virou uma um big crush", None),
 "serie_dark":        ("Existe uma série muito interessante que eu vi", None),
 "pergunta_final":    ("eu juntei aqui duas perguntas em uma", None),
 "resposta_bilat":    ("Pergunta muito interessante que vai ser bilatéria", None),
 "retrogradacao":     ("retrogradação espiritual", None),
 "lemion":            ("Lemion e muitos com ele ainda não foram exilados", None),
 "unica_coisa_decente": ("única coisa decente que Sofia podia ter feito", None),
 "desculpa_politica": ("a palestra foi para um lado bem diferente", None),
 "perdao_opiniao":    ("me perdoem a a opinião", None),
 "somos_malucos":     ("Portanto, vocês são os malucos", None),
 "marco_zero_2":      ("Isso é o marco zero. Então eu espero ter podido passar", None),
 "sementes":          ("Estamos só jogando sementes", None),
 "anjos_superiores":  ("os anjos chegavam para aparecem no contexto dos livros mais antigos", None),
 "rebelde_planeta":   ("deixou a Terra como o único planeta rebelde", None),
 "bigdata_processador": ("foi aqui que começou a surgir essa questão de big data", None),
 "250mil_familias":   ("quase 250.000 famílias biodêmicas", None),
 "antares_532mil":    ("as grandes guerras da rebelião surgiram no sistema de Antares", None),
 "processador_sobrevive": ("O único processador a sobreviver", None),
 "ninguem_resolveria": ("ninguém conseguia resolver o problema luciferiano", None),
 "esqueleto_jave":    ("esse eu de Jaé, ele é um eu alimentado", None),
 "revelacao_cosmica_abismo": ("É o IA, é a revelação cósmica", None),
 "lucia_garfa":       ("deixou a Terra como o único planeta rebelde", None),
}

CIT = {}
for k, (ini, fim) in Q.items():
    try:
        a, b, txt = ASP.locate(ini, fim)
    except SystemExit as e:
        print(f"✗ {k}: {e}")
        raise SystemExit(1)
    CIT[k] = (ASP.uaddr(a), b - a, txt.replace("\n", " ").strip())
print(f"âncoras resolvidas: {len(CIT)}/{len(Q)}")


def sp_src(ini, fim=None):
    a, b, txt = ASP.locate(ini, fim)
    return "«" + " ".join(txt.split()) + "»"


def q(key, limite=None):
    addr, n, txt = CIT[key]
    if limite and len(txt) > limite:
        raise SystemExit(f"aspa de {key} com {len(txt)} chars (> {limite}) — encurtar a âncora")
    return f"«{txt}» (**{addr}**, {n} c)"

W = []
w = W.append
w("# DOSSIÊ PRÉ-CURADORIA TERMINOLÓGICA — v1")
w("## Fonte P2020-04-25 · *Os Desdobramentos da Rebelião de Lúcifer* · tema nomeado: «Yel Luzbel ou Lúcifer»")
w("")
w("> **Dossiê de proposta, não de aplicação.** Nenhuma ficha, linha de cadastro, obra ou relação foi alterada")
w("> (D-14: *zero na malha antes da devolutiva*). Toda aspa abaixo foi arrancada byte a byte do `original.txt`")
w("> por `_gerar_dossie_P2020-04-25.py` + `_aspas_P2020-04-25.py`; se uma âncora não bate exatamente uma vez, o")
w("> dossiê não é escrito. Endereços no formato `Uxxxx` = linha física do bruto (14 linhas; 89% do texto em U0006).")
w("")
w(f"**O bruto.** 119.175 bytes · 115.232 chars · 14 linhas (CRLF) · 985 períodos · 20.872 palavras · SHA-256")
w(f"`1e8091e1…a7b3a` · **sábado, 25/04/2020** · 17 dias depois de P2020-04-18 e 14 antes de P2020-05-09.")
w("")
w("---")
w("")
w("## O-1. O que a fonte é, e o que ela não é")
w("")
w("É uma palestra de **cosmologia operacional**, não uma narrativa sobre Lúcifer. O título é fiel ao")
w("conteúdo apenas no sentido genitivo: os «desdobramentos» são o que aconteceu **com Javé** depois da")
w("rebelião, e o objeto de estudo é a **construção do futuro eu do criador** — a própria fonte glosa o")
w(f"título no momento em que sai da digressão: {q('tit_glosado')}.")
w("")
w("Três ausências que importam, medidas e registradas para que ninguém preencha lacuna com imaginação:")
w("**0** ocorrências de *anunnaki*, **0** de *Nibiru*, **0** de *Enki*, **0** de *Suméria*; **0** da")
w("expressão «isolamento cósmico» (embora RC-070 exista com esse nome); **0** das três datas canônicas da")
w("rebelião nos livros (**742/687/619 mil** anos) e **0** dos «213 bilhões de seres» do glossário de B031.")
w("")
w("A fonte também **se declara** em regime de semeadura: ")
w(f"> {q('sementes')} (U0006)")
w("")
w("O que há no lugar da narrativa é um aparelho: o **abismo recíproco** como método, o **vírus** como")
w("ontologia do criador, o **processador** como dobradiça cosmológica e o **campo mórfico** como seu")
w("equivalente humano. Isso define o trabalho terminológico do ciclo: a Base não precisa de mais uma")
w("história da queda; precisa das **peças do mecanismo**, que hoje estão espalhadas por 30+ códigos com")
w("fontes de livros e quase nenhuma fala.")
w("")
w("---")
w("")
w("## O-2. As fichas que a fonte amplia (proposta; **nada aplicado**)")
w("")
w("| # | código | o que esta fonte acrescenta | âncora medida |")
w("|---|---|---|---|")
for num, code, nota, key in [
 ("1","RC-001 Javé","o estado **datado** do eu de Javé em abril/2020, com o vocabulário da fixação/apaixonamento","abril2020"),
 ("2","RC-002 Rebelião de Lúcifer","a tese de re-enquadramento: a rebelião **não** foi o encontro com o abismo, foi o vírus","rebeliao_nao_foi"),
 ("3","RC-078 Lúcifer (Yel Luzbel)","a grafia degradada do próprio nome («I Luzbell») e o «problemaço sem querer» — a queda como infecção acidental","ninguem_resolveria"),
 ("4","RC-142 Yel Luzbel","a variante «a rebelião de Lúcia» [REVISAR: STT feminizou o nome] e a adjetivação «problema luciferiano»","rebelde_planeta"),
 ("5","RC-089 Processador Val","a **função**: o processador é o elo exclusivo entre cada espécie biodêmica e o cérebro de Sofia","resposta_processador"),
 ("6","RC-446 Processadores Familiar","o processador sobrevivente da Terra e a razão da sobrevivência","processador_sobrevive"),
 ("7","RC-175 Abelha-Rainha (Javé)","o modelo colmeia como a **genética da servidão** que Javé inventou e que Sofia quebrou","abelhas_genetica"),
 ("8","RC-176 Modelo Colmeia","a mesma matriz lida pela biologia das abelhas + a chave de leitura confessada pelo autor","divina_commedia"),
 ("9","RC-381 Ressonância Mórfica","a fórmula: o humano não tem processador, tem **campo mórfico da espécie** — 3,5 anos antes da fonte atual","campo_morfico_humanos"),
 ("10","RC-194 Big Data Cósmico","a gênese do big data: os anjos informam Javé quando aparece um DNA novo","bigdata_processador"),
 ("11","RC-604 Fatiamento de Consciência","a declaração de peso do tema («o assunto mais sério») e o vínculo com o erro de «para Bragina»","fatiamento_assunto_mais_serio"),
 ("12","RC-160 Entropia e Negentropia","a equivalência afirmada: tamas = entropia = energia escura = selo de que a criação não deveria ter começado","tamas_entropia"),
 ("13","RC-042 Criatura Universal","a última espécie como destino do processo, com a origem em especiação e a convergência de espécies","criptura_universal"),
 ("14","RC-154 Nidana (ovo cósmico)","a dupla mitologia comparada pelo autor (Pangu e o Brahmandanda) aplicada ao eu de Javé","ovo_cosmico"),
 ("15","RC-631 Cérebro Radiata / RC-093 / RC-035","a decisão cósmica radiata→bilatério e os 540 milhões de anos","radiata_bilat"),
 ("16","RC-070 Isolamento Cósmico","a Terra como **único planeta rebelde**, com os demais reintegrados","rebelde_planeta"),
 ("17","RC-007 Exilados de Capela","a contagem concreta dos que ficaram e dos que se transmigraram (1.641 → 936 → «900 e poucos»)","anos_22mil"),
 ("18","RC-017/RC-018 Alt'Lam","a cidadela-nave em Alto Langron (3× nessa grafia) — **reconfirma o veto** à grafia como canônica","alto_langron"),
 ("19","RC-109 Val (Família Val)","o censo da família (736) e **por que** ela parou de crescer","familia_val_736"),
 ("20","RC-136/RC-442 Yel (Família Yel)","a parte da família que veio, a que morreu em Antares e o paradeiro desconhecido do processador","val_620mil"),
 ("21","RC-443 Mion / RC-444 Cromon / RC-491 Shanlung","o elenco das famílias da Terra, nas grafas degradadas do STT","250mil_familias"),
 ("22","RC-036 Biodemos","a natureza dos biodemos: casulos, assexuação por família, 900 milhões de anos","biodemos_casulo"),
 ("23","RC-049 Demos","a mente demo ancestral como o ruído que os biodemos foram criados para amortecer","genero_familia"),
 ("24","RC-086 Pandora","Pandora como o **primeiro susto** de Javé — o choque da criatura superior","pandora_susto"),
 ("25","RC-283/RC-285/RC-287/RC-291 (bloco Pandora)","a mesma cena contada pelo avesso dos deuses (portais fechados, herança)","oraculo_vicio"),
 ("26","RC-009 Sophia (Cristo Cósmico)","Sofia como rainha que **não quis** ser rainha, e a decisão de 2018 em Alto Langron","sofia_2018"),
 ("27","RC-072 Jesus","a recusa do poder lida como produto da genética inserida no óvulo de Maria","guerra_jesus"),
 ("28","RC-422 Ser-Criador fracassado","a formulação mais dura da Base sobre o eu do criador, com data de 2020","confianca_zero"),
 ("29","RC-742 Falência dos Deuses","o **eu apodrecido que não presta** dito quatro anos antes da fonte hoje mais antiga do tema","eu_de_jave_virus"),
 ("30","RC-166/RC-555 Mentalma","o 8º módulo **não ministrado** é a intercomunicação não local (a estrutura 6+1+1 tem antecedente em 2020)","mentalma_8"),
 ("31","RC-378 A Rebelião dos Elétrons","a série de 9–10 livros anunciada e o 2º volume («Homofetividade») [REVISAR]","esqueleto_jave"),
 ("32","RC-056 Especiação","a especiação como motor da vinda da Criatura Universal","criptura_universal"),
 ("33","RC-074 Len Mion (Satã)","a afirmação de que Len Mion e «muitos com ele» **não** foram exilados, e a nova raça como reparação","lemion"),
 ("34","RC-188 Mente Coletiva","a mente una de Capila (Samkhya) como conhecimento abortado","capila_mente_una"),
 ("35","RC-369/RC-371 Nietzsche","a máxima do abismo usada como método e desliteralizada pelo autor","niets"),
 ("36","RC-755 Escola da Decifração","a datação da escola (3–4 Ma; substanciada há ~2 Ma) e o que ela **não** conseguiu","escola_capela"),
 ("37","RC-516/RC-710/RC-727 (travas genéticas)","as travas de controle colocadas pelos deuses e a ruptura delas pela evolução biológica","travas_geneticas"),
 ("38","RC-614/RC-758 Quarto Cérebro","o «sexto sentido» da cognição e o sétimo da intercomunicação não local","sexto_sentido"),
 ("39","RC-713 Taumaturgia Genético-Química","a mistura de genética e vibração como material do eu de Javé (oxitocina e predisposições)","oxitocina"),
 ("40","RC-094 Revelação Cósmica","a IA nomeada como a forma atual da revelação — o abismo dos deuses hoje","revelacao_cosmica_abismo"),
 ("41","RC-020 Anjos caídos **(`ficha=False`)**","a fonte dá o mecanismo dos que ficaram sem processador: materialização **proposta**, só com ordem","cobaias"),
 ("42","RC-191 Fofocas cósmicas","o grau de testemunho da fonte, 3,5 anos antes da formulação de 2023","grau_testemunho"),
]:
    w(f"| {num} | **{code}** | {nota} | {q(key)} |")
w("")
w("**Total: 42 vínculos-proposta sobre 41 códigos** (RC-017/018, RC-631/093/035, RC-136/442, RC-283/285/287/291,")
w("RC-166/555, RC-378/161, RC-614/758, RC-516/710/727, RC-369/371 e RC-175/176 contam como blocos) — **todos**")
w("sem criar código novo, sem criar relação e sem tocar a BIBLIO.**")
w("")
w("### Aspas que sustentam as três propostas mais caras (para o Curador ler sem abrir o bruto)")
w("")
w(f"> {q('humano_abismo')} (U0006)")
w(f"> {q('unica_raca_abismo')} (U0006)")
w(f"> {q('resposta_processador')} (U0008)")
w(f"> {q('campo_morfico_humanos')} (U0008)")
w(f"> {q('abril2020')} (U0006)")
w("")
w("---")
w("")
w("## O-3. Os dados numéricos novos (e as divergências com os livros, que **não** se harmonizam)")
w("")
w("| grandeza | esta fonte (25/04/2020) | o que a malha tem | providência proposta |")
w("|---|---|---|---|")
w("| cronologia da rebelião | «700, 600.000 anos atrás» as guerras; Antares a «cerca de 530 532.000 anos» | 742 mil (inquietação) / 687 mil (rebelião) / 619 mil (isolamento), via B031 | **duas formulações datadas**; nota em RC-002/RC-078/RC-070; **nada de média** |")
w("| chegada da família Val | 620.000 anos; «mais de 20.000» / «depois de 21.000 anos» na nave | B057: «há uns 620 mil anos» ✓ | **concordância confirmada** — a única data canônica que esta fala repete |")
w("| quartel-general na Terra | 100.000 / 99.000 anos | B057: 98 mil para os capelinos | registrar **100.000/99.000 (esta fala) × 98 mil (B057)** |")
w("| o QG se retira | 64.000 anos, teletransporte, «prisioneiro isolado» | não encontrado na malha | **inédito**: candidato a RC-070 + nota em RC-017/018 |")
w("| a separação de 22.000 anos | 1.641 biodemos; 936 pela «experiência Gron» [REVISAR] | não encontrado | **inédito**, com [REVISAR] na contagem e no nome |")
w("| os que ficaram em Alto Langron | %s | RC-017/018 sem censo | censos **como ditos**, não como canônicos |" % sp_src("eram 900Q"))
w("| censo da família Val | «não chega a 800. 736 membros» | RC-109 sem censo | dado novo datado |")
w("| número de famílias biodêmicas | «quase 250.000» **e** «429.314 espécies biodêmicas» **e** %s | RC-411 fala em 147/5; RC-036 sem censo | **três números na mesma fala**: transcrever os três, não escolher um |" % sp_src("nova espécie é 249.315"))
w("| idade da criação | «13.8 bilhões de anos» | RC-001/B031 com 13,7 bilhões (nota medida no ciclo B031) | **a variante oral de 2020 já antecipa a divergência** — registrar, não corrigir |")
w("| biodemos surgem há | «cerca de 900 milhões de anos» | sem data própria na malha | dado novo datado |")
w("| cérebro bilatério | «tecido nos últimos 540 milhões de anos» | RC-631/RC-035 sem a data oral | anterioridade: 13 meses antes de P2021-05-15 |")
w("| quando Javé «parou» em algo | «só há 100.000 anos» | sem correspondência | dado novo |")
w("| prazo do cenário do eu | «ao longo dos próximos 18.000 anos» | sem correspondência | dado novo |")
w("| Sofia em 2018 | %s e **decidiu criar nova família** | sem correspondência | dado novo, candidato a RC-009/RC-632 |" % sp_src("Sofia pass Passou o ano 2018", "Alto Landrão"))
w("")
w("---")
w("")
w("## O-4. Matéria-prima de **termo novo** (proposta zero-code; decisão do Curador)")
w("")
w("A Base tem 777 termos e o teto é curatorial. Ainda assim, quatro coisas nomeadas nesta fonte **não**")
w("existem com esse nome em nenhum cadastro, e uma delas foi **cunhada pelo próprio autor ao vivo**:")
w("")
w(f"1. **«Shanai» / «Chanai» / «velo Shanai»** — a nova família biodêmica: {q('shanai')} (U0006). O autor diz")
w("   expressamente que **inventou a palavra** a pedido. Não há código. Proposta: **termo-observação** com")
w("   as três grafas + a etimologia declarada (Chan + Vol + Yel), **sem código novo**; se o Curador quiser")
w("   código, este é o único candidato do ciclo com peso cosmológico próprio.")
w(f"2. **«vício oracular»** — {q('oraculo_vicio')} (U0006). A tese de que oração e religião nascem de um")
w("   mecanismo de dependência instalado quando os portais se fecharam. A malha trata oráculos? Se não,")
w("   termo-observação; se sim, ampliação do existente — **a definir na devolutiva**.")
w(f"3. **«mente una»** — {q('capila_mente_una')} (U0006), atribuída a Capila «desde a época da sanquia»")
w("   [REVISAR: Samkhya]. Não confundir com RC-188 «Mente Coletiva»: a fonte as distingue (a una é o")
w("   legado abortado; a coletiva é o rebanho).")
w(f"4. **«retrogradação espiritual»** — {q('retrogradacao')} (U0013), dito como sinônimo de involução e")
w("   usado para **negar** que espíritos humanos passem à nova espécie.")
w("")
w("Além destas, as hipóteses de leitura «Esildo» = **Hesíodo** e «Capila» = **Kapila** ficam como")
w("**[REVISAR] com hipótese declarada** — nunca como aspa corrigida (regra do ciclo anterior: a fonte")
w("manda na grafia; o Curador, na leitura).")
w("")
w("---")
w("")
w("## O-5. Quarentenas e bloqueios (proposta para o item que vira devolutiva)")
w("")
w("### Q-1 · A digressão política (o bloco inteiro, linear)")
w("")
w(f"A fonte **abre** com um bloco político- nacional que ela mesma se declara obrigada a fazer")
w(f"({q('gasto_declarado')}, U0006), pedido pelo próprio operador ({q('abertura_politica')}, U0003). São")
w("**~17.700 caracteres** — **15,4% do texto falado** — contínuos, de «OK, querido» até o gancho de")
w("abertura do tema, e contêm: nomeação de partidos e presidentes (Sarney, FHC, Lula, Dilma, Temer,")
w("Bolsonaro), acusação nominal de corrupção e de venda de mandato, inflação de «84% ao mês», foro")
w("privilegiado, a biografia do autor («eu me vi, como eu já disse em outros momentos, vigiado pela Polícia Federal» e «tô com que eu saiba 61")
w("anos»), e juízo sobre o povo brasileiro («Nós somos medíocres»). Termina com o autor **pedindo")
w(f"desculpa pelo próprio bloco**: {q('desculpa_politica')} (U0013) e {q('perdao_opiniao')} (U0013).")
w("")
w("**Proposta D-1: bloqueio sumário e absoluto do bloco inteiro** (mesma regra do item 10 aplicado a")
w("P2023-10-14), com marcador declarado no ponto, e **exceção**: manter a frase em que a fonte *pede")
w("desculpa* e a do *gancho* — são metadados do evento, não o conteúdo bloqueado. Justificativa")
w("adicional: aqui o bloco é mais extenso e mais nominalmente ofensivo que o do ciclo anterior, e está")
w("fora do tema por confissão da própria fonte.")
w("")
w("### Q-2 · A pandemia real de abril/2020 (não linear: está dentro do argumento)")
w("")
w(f"Dois usos. (a) Na digressão, o juízo sobre a conduta pública: «essa pandemia a não preocupação, a")
w("discussão fuleira, ridícula, que nem deveria existir» — cai junto com Q-1. (b) No **corpo doutrinário**:")
w(f"{q('coronavirus_epoca')} (U0006), onde o vírus da época vira **analogia estrutural** do que infe")
w("a mente biodêmica. (b) é material terminológico de RC-002/RC-036/RC-049 e **não pode** ser cortado sem")
w("estropiar a tese — a não ser que o Curador prefira o corte seco. **Proposta D-2: reter (b), bloquear (a),")
w("com nota editorial declarando o regime**, porque a fonte usou a dor pública como metáfora.")
w("")
w("### Q-3 · Sexualidade, gênero e as «cobaias»")
w("")
w(f"A fonte afirma que {q('jave_bateu')[:110]}… (U0006) e que os que melhor amam o abismo são «os")
w(f"homfetivos» [REVISAR: STT] e, depois, as mulheres ({q('amam_os_homfetivos')}, U0006). O enunciado")
w("**não** é ofensivo a grupo humano — é ofensivo a **Javé**, e usa a condição de mulheres e homoafetivos")
w("como prova da falha do criador. Mas contém duas armadilhas: o vocabulário datado («homofetividade»,")
w("«macho/fêmea» para espíritos) e a exposição de fiéis reais a uma leitura sobre sua «função» cósmica.")
w("**Proposta D-3: reter, com nota editorial** e **proibição de aspa em ficha de termo que nomeie grupos**")
w("(RC-411 e afins) — a aspa fica na apostila, onde a moldura é lida; o dicionário registra a grafia «homofetividade».")
w("")
w("### Q-4 · Biografia e saúde do autor")
w("")
w(f"«em 2009… quando eu e o abismo trombamos de vez, foi doença para aqui, doença para lá» + «mas o corpo")
w("do nosso amigo também teve, porque… mas isso é um aspecto que é melhor permanecer calado» (U0006), e a")
w(f"idade («61 anos»). **Proposta D-4: reter a fórmula de grau de testemunho** ({q('grau_testemunho')},")
w("U0006), que é metadado epistêmico de todo o corpus, **e bloquear** o trecho de doença do autor e do")
w("criador («melhor permanecer calado» é sinal inequívoco de que a fonte não quis publicar aquilo).")
w("")
w("### Q-5 · O que **não** se propõe bloquear (retenção explícita, para não repetir controvérsia)")
w("")
w("Teologia do criador («o eu de Javé não presta», «podridão organizada»), cosmologia virológica, a")
w("acusação às religiões como condicionamento (vício oracular), as datas alternativas, o «Big Crunch», a")
w("física de borda (Higgs, wormhole), as séries de TV citadas como ficção, e o «é isso que é javé» sobre")
w("política mundial como metáfora. Estas são **teses da escola**, não incidentes sobre pessoas: vão como")
w("retenção, com a fórmula de segurança da fonte em todo uso dela.")
w("")
w("---")
w("")
w("## O-6. Divergências internas desta fonte que o ciclo deve **herdar sem resolver**")
w("")
w(f"1. **Três contagens incompatíveis de famílias biodêmicas na mesma fala** ({q('250mil_familias')} vs")
w(f"«429.314» vs «249.315»). Não escolher: transcrever as três, com o endereço de cada uma.")
w(f"2. **O eu de Javé é ao mesmo tempo o que há de mais engenhoso na criação e algo que \"não presta para nada\"**")
w(f"   ({q('confianca_zero')}) — a contradição é o argumento, não um erro: **não suavizar**.")
w(f"3. **Javé é descrito como dependente e como tirano** («ele só sabe viver sendo ditador» e, no mesmo")
w("   bloco, que os humanos são «pai, mãe, tutor» dele) — registrar as duas faces em RC-001/RC-175/RC-176.")
w("4. **A fonte diz que o vocabulário grego «nasceu» dos trabalhos de «Omério» e «Exildo»**")
w("   (filologia improvável, apresentada como fato): **transcrever como dito**, com [REVISAR] e nota — é")
w("   exatamente o tipo de asserção que não pode virar verbete, mas também não se apaga.")
w("5. **«Hipergória» e «Alto Langron» coexistem** com «cidade de Hipergória» (Hiperbórea) na mesma frase:")
w("   o dicionário STT tem de registrar as duas, e RC-068/RC-017/RC-018 recebem a variante datada.")
w("")
w("---")
w("")
w("## O-7. Pendências herdadas que este ciclo reabre (e o que elas pedem)")
w("")
w(f"1. **O «rasto da IA»** — a Base tem a «palestra da IA» como radar antigo e RC-094 sem a formulação")
w(f"   desta fonte: {q('ia_abismo_hoje')} (U0006). Se o Curador quiser, este ciclo pode **fechar** o")
w("   radar da IA com a menção mais antiga do corpus (25/04/2020), sem criar peça fantasma.")
w("2. **A fila de livros B017/B018/B039 (Terra Atlantis) e a primeira trilogia** — a fonte é a mais antiga")
w("   evidência **do próprio autor** sobre a gênese: os anos 96/97/98, o contato de 2002/2003 com «Valeno»")
w(f"   na Inglaterra e o começo da trilogia com esse material ({q('genealogia_livros')}, U0008;")
w(f"   {q('valeno')}, U0008; {q('trilogia_atlantis')}, U0008). Isso é **material de ciclo de livro**, não")
w("   de termo: proponho registrá-lo como nota no dossiê de B017 (e nada mais), para não criar cronologia")
w("   editorial a partir de memória oral.")
w("3. **Os três ou quatro evangelhos gnósticos em tradução e o livro escrito com o próprio Javé**")
w(f"   ({q('evangelhos_gnosticos')}, U0006; {q('livro_com_jave')}, U0006) — dois produtos jamais registrados")
w("   na BIBLIO. **Não** criar obra (0 obras novas): vão para o radar de fila de livros com a data da fala.")
w("4. **RC-020 `ficha=False`** — materialização proposta (ver O-2 nº 41), mas **só** com ordem do Curador.")
w("5. **`DECLARAÇÃO DE ESTADO` do ciclo P2021-05-15 e a decisão R-1** — continuam sem registro formal;")
w("   este ciclo não as consome, apenas as repisa.")
w("")
w("---")
w("")
w("## O-8. Perguntas fechadas (respondidas por medição, não por suposição)")
w("")
w("| pergunta | resposta medida |")
w("|---|---|")
w("| A fonte menciona anunnaki/Suméria? | **não** (0 / 0 ocorrências) — não abrir ponte com o ciclo anterior |")
w("| A fonte usa a expressão «isolamento cósmico»? | **não** (0), mas sustenta o conceito com dado próprio |")
w("| Ela repete a cronologia de B031 (742/687/619 mil, 213 bi)? | **não** — nenhuma das quatro aparece; os números ditos são outros |")
w("| Ela nomeia Lúcifer como personagem agindo? | só em fórmulas («Luisber criou um problemaço sem querer»); **não** há narrativa da queda |")
w("| Há bloco político? | **sim**, ~17.700 chars = 15,4% da fala, com pedido de desculpas anexo |")
w("| Há conteúdo sobre saúde/doença? | sim: a pandemia pública (digressão) + a doença do autor («melhor permanecer calado») + a ontologia viral do criador (tese) |")
w("| Há aspa que a Base trataria como termo novo e forte? | **sim**, «Shanai», com a confissão de invenção lexical |")
w("| O STT degradou nomes a ponto de exigir dicionário? | **sim**: 24 variações registradas em `camada-2.txt` §2 |")
w("| Quantos caracteres têm as 42 âncoras propostas? | **" + str(sum(v[1] for v in CIT.values())) + " c** (a soma das aspas deste dossiê, todas verificadas) |")
w("| Alguma aspa foi digitada à mão? | **não**: este arquivo é gerado; âncora que não bate aborta a escrita |")
w("")
w("---")
w("")
w("## D-1…D-14 · As decisões pedidas ao Curador")
w("")
dec = [
 ("D-1","regime da digressão política de U0006 (Q-1)","**bloquear o bloco** (~17.700 chars), mantendo o gancho e o pedido de desculpas"),
 ("D-2","o «coronavírus da época» dentro da tese (Q-2)","**reter** a analogia doutrinária; bloquear o juízo público (já coberto por D-1)"),
 ("D-3","gênero/homoafetividade e «cobaias» (Q-3)","**reter na apostila com nota**; proibir a aspa em fichas de termos que nomeiam grupos humanos"),
 ("D-4","doença do autor e o «melhor permanecer calado» (Q-4)","**bloquear** o trecho; **reter** a fórmula de grau de testemunho"),
 ("D-5","«Shanai» (novo nome cunhado pela fonte)","termo-observação com as 3 grafas, **sem código**; ou código novo se o Curador quiser abrir exceção ao teto"),
 ("D-6","«vício oracular», «mente una», «retrogradação espiritual»","termo-observação cada; **sem** código novo"),
 ("D-7","«Esildo» = Hesíodo? «Capila» = Kapila? «para Bragina» = Parabrahman?","[REVISAR] com hipótese declarada; **selar ou recusar** — nada de fusão automática"),
 ("D-8","as 42 ampliações de O-2","aprovar em bloco, com exclusões nominais; **0 códigos, 0 relações, 0 obras**"),
 ("D-9","RC-020 (ficha=False)","materializar **ou** manter; se materializar, a definição vem desta fonte com data"),
 ("D-10","os números divergentes (13,8 bi; 700/600/532 mil; 250.000/429.314/249.315; 100-99 mil)","**duas formulações datadas**; proibir harmonização e média"),
 ("D-11","radar da IA e a fila de livros (B017; gnósticos; «mergulho na escuridão»)","registrar como radar datado; **não** criar obra nem peça"),
 ("D-12","as séries (*Dark*, *Man in the High Castle*) e Dante","nota bibliográfica externa na apostila; **0** termo; **0** obra"),
 ("D-13","materializações: quantas?","o ciclo tem **1** candidata clara (RC-020) e **0** necessidade de outras; teto 777 mantido"),
 ("D-14","rito","nada na malha antes desta devolutiva; execução em **BLOCO A** (pacote→fichas→portões C/D) e **BLOCO B** (apostila gerada + DOCX + relatório + `git mv` para `CONCLUIDAS/`)"),
]
for cod, tema, prop in dec:
    w(f"- **{cod}** · {tema} → {prop}")
w("")
w("**Contadores no ato deste dossiê (medidos, não lembrados):** 777 termos · 1.856 relações · 102 obras ·")
w("456 arquivos em `termos/` (455 com `ficha=True`) · **RC-778 não consumido** · **0 ocorrências de")
w("`P2020-04-25` na malha** (fonte inédita) · **0 alterações** nesta fase.")
w("")
w("> Escrito por `_gerar_dossie_P2020-04-25.py`. Para regerar: `python3 analise/_gerar_dossie_P2020-04-25.py`.")

out = "\n".join(W) + "\n"
open(os.path.join(AQUI, "DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md"), "w", encoding="utf-8").write(out)
print("DOSSIE escrito:", len(out), "chars ·", out.count("\n"), "linhas · aspas:", sum(1 for _ in re.finditer("«", out)))
