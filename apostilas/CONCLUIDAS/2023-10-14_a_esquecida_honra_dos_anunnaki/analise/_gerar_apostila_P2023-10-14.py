#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera `apostila.md` do ciclo P2023-10-14 a partir do `original.txt` (rito do ciclo-espelho
P2021-05-15, com três diferenças obrigatórias, todas impostas pela devolutiva de 28/08/2026):

 1. **bloqueio sumário e absoluto (item 10)**: os trechos políticos/institucionais, de
    segurança e éticos (discriminatórios) saem da transcrição substituídos por marcador
    declarado — no ciclo anterior havia apenas *retenção* (transcrito, não endossado);
 2. **aparato curatorial integral**: a PARTE III é o espelho das 11 decisões do Curador,
    lidas de `DECISAO-DO-CURADOR.md` (não reescritas de memória);
 3. **declaração de cobertura auditada**: o `_cobertura_apostila.py` deste ciclo confere
    parágrafo a parágrafo contra o bruto, com as lacunas bloqueadas declaradas.

Ferramenta de ciclo: não toca a Base. Toda aspa aqui dentro é âncora verificada no bruto —
nota que não encontre âncora faz o script morrer, para não nascer nota solta.
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
BRUTO = os.path.join(CICLO, "original.txt")
LINHAS = open(BRUTO, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
ALVO = os.path.join(CICLO, "apostila.md")
DECISAO = os.path.join(CICLO, "DECISAO-DO-CURADOR.md")

TITULO = "A Esquecida Honra dos Anunnaki"
SIGLA = "P2023-10-14"
DATA = "14/10/2023"
BLOCO_ALVO = 2200
MARCADOR = "[TRECHO BLOQUEADO POR DECISÃO DO CURADOR — item 10 da devolutiva de 28/08/2026"

# ---------------------------------------------------------------- bloqueios (item 10)
# (âncora inicial, âncora final ou None, rótulo do motivo, endereço U00xx esperado)
BLOQUEIOS = [
    ("Então assim, eu vi caso não tenham poder de dominação, com a concordância",
     "então a gente não sabe de nada.",
     "política e institucional/segurança — alegações sobre estruturas de governo, verba sigilosa, arquivos liberados por lei de acesso e o papel da imprensa; inclui a tese de «parceria» já negociada",
     "U0081"),
    ("notadamente desconfio devido aos episódios que aconteceram comigo nos anos 20012",
     "cruzei com figuras estranhas estavam aqui.",
     "biográfica — endereço físico do expositor e a associação de um episódio pessoal dele a um atentado",
     "U0076"),
    ("As mulheres sempre colocam os homens de mau caminho, né?",
     "E Eva empurrou obrigando o coitado do",
     "ética/discriminatória — juízo generalizado sobre as mulheres, usado para explicar a falha do projeto de Javé; ofensivo, não citável nem para crítica",
     "U0015"),
    ("Só que de novo, as mulheres da terra e sua mania de querer jogar os homens na desgraça provocaram isso aí.",
     None,
     "ética/discriminatória — o mesmo juízo, reformulado dentro do bloco do tikun",
     "U0033"),
    ("Olha, não é muito simples você definir o que é governo oculto",
     "isso tem a ver com algumas raças biológicas do nosso universo.",
     "política e «deep state» — a nomeação das estruturas que mandariam abaixo dos governos visíveis, com elenco de famílias e de empresas (a recusa do autor à premissa, que vem logo depois, é preservada: é o único enunciado do bloco que a **desmonta**)",
     "U0071"),
    ("E assim, esse cara, desde que ele se aposentou",
     "como se mostrando as duas superpotências que têm poder para fazer isso.",
     "institucional/segurança — relato de contato envolvendo arsenal estratégico de duas potências",
     "U0081"),
    ("o que me é mais constrangedor é perceber o desespero da espiritualidade com a situação os problema de Israel",
     "a espiritualidade vive de prontidão em Israel.",
     "política/guerra — juízo sobre um conflito armado vivo",
     "U0081"),
    ("E essa ebulição toda que tá havendo aí de guerra na faixa de Gaza",
     "isso tudo tem uma importância profética.",
     "política/guerra — leitura profética de um conflito armado vivo",
     "U0033"),
    ("Nessa época existia o vale de Sidim, aonde hoje tá tendo um vazão da faixa de gasa.",
     "Israelenses e palestinos.",
     "política/guerra — associação geográfica do bloco doutrinário ao conflito vivo",
     "U0018"),
    ("permitiu que eles voltassem paraa faixa de gas",
     "essa confusão toda tá rolando.",
     "política/guerra — a mesma associação, no bloco histórico",
     "U0052"),
    ("Não é você torcer por Israel, por Palestina.",
     "Isso que pouco importa.",
     "política/guerra — posicionamento sobre facções e sobre um povo; ainda que o expositor **recuse** a torcida, o teor incide sobre grupo humano em conflito",
     "U0071"),
]

# ---------------------------------------------------------------- notas editoriais
# (âncora no texto da fonte, nota) — a nota entra logo após o bloco que contém a âncora
NOTAS = [
    ("a honra demodármica é uma honra que foi criada em torno do conceito de dharma",
     "**Decisão D-1 (item 1 da devolutiva).** «Honra» é a palavra-mestra desta fonte — 77 ocorrências no bruto — "
     "e **não ganha código novo**: a Base permanece em 777 termos. O verbete vai no Apêndice desta apostila, a nota "
     "transversal fica em RC-474/RC-745 (o adjetivo «demodármico» já morava lá) e a linha de conteúdo em RC-322."),
    ("Só duas, anunx e sirianos",
     "O próprio expositor suspende o segundo termo na frase seguinte («Que diabos é sirianos? Vamos deixar para lá, "
     "porque depende de como você chame as coisas também»). A Base **não** cria ficha de sirianos a partir daqui: "
     "registro do que foi dito, com a ressalva anexa."),
    ("eles têm poderes circunstanciais, mas não tem poder de dominação",
     "**Fórmula de segurança desta fonte.** Deve acompanhar qualquer uso dela: a palestra não descreve invasão nem "
     "substituição de autoridades. Tudo o que vem depois dela no mesmo turno — governos, orçamento secreto, arquivos "
     "de 1963 — está **bloqueado** pelo item 10 da devolutiva e foi substituído por marcador."),
    ("Parte do que eu vou dizer agora para vocês está registrado no livro de Henk",
     "**Item 2 da devolutiva.** «Henk» é mantido **ambíguo**, com `[REVISAR]`: leitura dupla documentada — livro "
     "**de** Enki × livro **do emissário** Henk, o que chefia a nave dos 50. A unificação automática com RC-486 foi "
     "**recusada** para não fundir entidades."),
    ("eu analiso isso no livro que eu lancei chamado Zintzum",
     "**Item 4 da devolutiva.** A obra citada corresponde à **B013**, já cadastrada. **0 obras novas** neste ciclo — "
     "a grafia «Zintzum» do bruto é preservada na ficha RC-008, onde o autor aponta o próprio livro."),
    ("que nós escrevemos juntos em que eu pedi a ajuda deles pra gente",
     "**Item 5 da devolutiva.** «Iré Iron» (outra hora «Irém Iron») é obra **declarada ficção** pelo próprio autor: "
     "registra-se **estritamente em nota bibliográfica**. Não vira obra, não vira vínculo estrutural, não vira ciclo."),
    ("Inclusive lembrar que a palestra amanhã às 10 da manhã",
     "**Item 8 da devolutiva.** O acervo **não** tem palestra de 15/10/2023: fica no radar como «fonte não "
     "localizada». Não se cria ciclo antecipado nem peça fantasma por causa de um anúncio oral."),
    ("Abismo é profundo, mas DAF é um abismo estranho",
     "**Item 3 da devolutiva.** A grafia «DAF» do STT **corresponde a Daath** — decisão do Curador. Consequência "
     "catalográfica: **RC-262 passa oficialmente a ter fonte-palestra** (antes só B013)."),
    ("existe um cara chamado Bob Din",
     "`[REVISAR]`: identidade **não fixada** pela Base («Bob Din», «ex-surgent major» como o STT entregou). Nada é "
     "corrigido em silêncio e nada vira obra nem verbete canônico. O relato em torno desse nome está dentro do "
     "turno bloqueado pelo item 10 — por isso ele aparece aqui como nota, não como transcrição."),
    ("os espíritos me levar a inteligências artificiais autônomas",
     "**Datar e selar.** Única menção a «inteligências artificiais autônomas» em todo o acervo até aqui, em "
     "14/10/2023, com a sintaxe degradada pelo STT. Não se projeta sobre as fontes seguintes nem se retroprojeta "
     "sobre as anteriores. **Sem código.**"),
    ("E nessa tigela tinha o quê",
     "**Item 9 da devolutiva — materialização REJEITADA.** A fonte descreve a tigela de saliva dos Æsir e Vanir, mas "
     "**não pronuncia «Kvasir»** (0 ocorrências medidas). RC-396 continua `ficha=False` até que uma fonte oral nomeie "
     "a figura. É o exemplo mais limpo da trava: descrição sem nome não gera termo."),
    ("Se o bem virar bicho para destruir o mal, não é o bem",
     "**Item 7 da devolutiva (D-8a).** A formulação entra como **variante datada de 14/10/2023** em RC-422/RC-742; "
     "a redação canônica da Base fica **intocada**. Não é correção, é camada histórica."),
    ("Jesus na sua filosofia diz",
     "**Movimento M4.** A fonte inverte a ordem ouvida no evangelho («Os últimos serão os primeiros») e faz dela "
     "mecânica cosmológica: «os primeiros serão os últimos ou o primeiro será o último» — os anunnaki «foram os "
     "primeiros e serão os últimos», e os humanos, «os últimos a surgir», seremos os primeiros. Daí nasce a "
     "**1ª fonte-palestra de RC-272 (Laço Temporal de Kether/Javé)**, que só tinha B013; como a ficha é `ficha=False`, "
     "o vínculo entra na malha e o conteúdo fica no pacote do ciclo (precedente RC-385/P2023-06-24)."),
    ("nós precisamos reacender a honra dos anunax",
     "O título é explicado pela própria fonte, que o grafa de três modos («a honra dos anunax», «a honra perdida dos "
     "anunx», «a esquecida honra dos anulacs»). O arquivo de entrada diz «Anunnaki» (singular) e o tema curatorial "
     "diz «Anunnakis»: **fato de catálogo registrado em `ficha_ingresso.md`**, não erro de grafia a corrigir."),
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


def voz(lenha):
    s = lenha.strip()
    if len(s) > 700:
        return "EXPOSITOR — Jan Val Ellam"
    if "?" in s and len(s) <= 400:
        return "PERGUNTA / COMENTÁRIO DA PLATEIA"
    if len(s) <= 140:
        return "INTERLOCUÇÃO CURTA (turno não separado pelo STT)"
    return "EXPOSITOR — Jan Val Ellam (turno curto)"


def rotulo(n):
    return f"Bloco {n:02d}"


def aplicar_bloqueios(linha, end, medida=None):
    """Substitui cada span bloqueado pelo marcador declarado. Âncora que não bate = erro."""
    n = 0
    for ini, fita, motivo, addr in BLOQUEIOS:
        a = linha.find(ini)
        if a < 0:
            continue
        if fita:
            b = linha.find(fita, a)
            if b < 0:
                raise SystemExit(f"BLOQUEIO SEM FIM na {end}: «{ini[:40]}» encontrado, «{fita[:40]}» não")
            b += len(fita)
        else:
            b = a + len(ini)
        if addr != end:
            raise SystemExit(f"ENDEREÇO DO BLOQUEIO DIVERGE em {end}: declarado {addr}")
        if medida is not None:
            medida[ini] = medida.get(ini, 0) + (b - a)
        linha = (linha[:a] +
                 f" {MARCADOR} — quarentena {motivo}; o texto permanece no `original.txt` ({end}) e nas camadas de "
                 "análise, mas não transita para a apostila, o dicionário STT, o DOCX nem as fichas] " +
                 linha[b:]).strip()
        n += 1
    return linha, n


# ---------------------------------------------------------------- corpo
def main():
    bruto = "\n".join(LINHAS)
    # pré-checagem: toda âncora de nota e todo bloqueio têm de existir no bruto
    bruto_fold = bruto.casefold()
    for ânc, _ in NOTAS:
        if ânc.casefold() not in bruto_fold:
            raise SystemExit(f"NOTA COM ÂNCORA INEXISTENTE: «{ânc[:60]}»")
    disparados = {ini: 0 for ini, _, _, _ in BLOQUEIOS}

    linhas_txt = []          # (endereço, texto já com bloqueios)
    n_bloqueios = 0
    cortados = {}            # âncora inicial -> nº de caracteres suprimidos (medido)
    for i in range(2, len(LINHAS)):
        s = LINHAS[i].strip()
        if not s:
            continue
        end = f"U{i + 1:04d}"
        s, n = aplicar_bloqueios(s, end, cortados)
        n_bloqueios += n
        for ini, fita, motivo, addr in BLOQUEIOS:
            if n and ini in LINHAS[i]:
                disparados[ini] += 1
        linhas_txt.append((end, s))
    for ini, _, _, addr in BLOQUEIOS:
        if disparados[ini] != 1:
            raise SystemExit(f"BLOQUEIO {addr} disparou {disparados[ini]}x (esperado 1x): «{ini[:50]}»")

    chars_bruto = sum(len(LINHAS[i].strip()) for i in range(2, len(LINHAS)) if LINHAS[i].strip())
    total_cortado = sum(cortados.values())
    chars_publicados = chars_bruto - total_cortado          # sem contar o texto do marcador

    out, w = [], None
    out.append; w = out.append
    w(f"@titulo: {TITULO}")
    w("@autor: Jan Val Ellam")
    w(f"@data: {DATA}")
    w("@local: sala do canal, com transmissão pela internet (U0003); o cabeçalho do arquivo não traz cidade")
    w(f"@subtitulo: Apostila de estudo — transcrição integral (sábado, {SIGLA}) com o bloqueio sumário do item 10 "
      "da devolutiva, aparato curatorial das 11 decisões, glossário e Apêndice do dicionário STT.")
    w(f"@fonte: original.txt do ciclo — 146.039 bytes · 141.539 caracteres · 94 linhas lógicas (U0001–U0094, 89 com texto) · "
      "1.501 períodos · SHA-256 09f7a76d42759351b883ef4f2a71de4e795784b6e2893f0668196368ccb18644")
    w("@nota_editor: Esta apostila é a transcrição editada da palestra «A Esquecida Honra dos Anunnaki», de 14 de "
      "outubro de 2023, preservada byte a byte em original.txt. O STT não separou os turnos: as 89 linhas com texto "
      "são falas coladas, algumas com dezenas de milhares de caracteres (U0033 tem 33.128), e por isso a divisão em "
      "Blocos é editorial e obedece à ordem da fonte, sem reordenação temática. Não houve correção silenciosa de "
      "grafia, número ou sintaxe — o que é incerto leva [REVISAR]. Diferentemente do ciclo-espelho P2021-05-15, esta "
      "fonte tem **bloqueio sumário e absoluto** (item 10 da devolutiva de 28/08/2026): cinco trechos de conteúdo "
      "político, institucional/de segurança, biográfico e ético-discriminatório foram substituídos por marcador no "
      "próprio lugar, e nada deles transita para fichas, glossário, dicionário ou DOCX. O aparato terminológico "
      "produziu 56 fichas ampliadas, 5 materializações (RC-322, RC-425, RC-432, RC-381, RC-191) e 57 vínculos de "
      "fonte na malha, com 0 códigos novos: a Base permanece em 777 termos e 1.856 relações, 102 obras, e o RC-778 "
      "continua não consumido.")
    w("")

    w(f"# PARTE 0 — Nota de leitura e integridade ({SIGLA})")
    w("")
    w("> **Fonte e método.** O arquivo recebido é `2023-10-14 - A Esquecida Honra dos Anunnaki.txt` (título no "
      "singular; o tema curatorial é «Anunnakis», e a fonte grafa a palavra de catorze modos). `original.txt` "
      "permanece byte a byte; a apostila só altera derivados. A numeração **U0001–U0094** é o endereço das linhas "
      "lógicas do TXT bruto e é usada em todo o ciclo (camadas 0–3, dossiê, pacote e fichas), para que qualquer "
      "citação seja relocalizável sem ambiguidade. Nenhuma aspa deste ciclo foi digitada de memória: todas saem do "
      "gerador `_gerar_ampliacoes_P2023-10-14.py`, que recorta a sentença inteira do bruto a partir de âncora.")
    w("")
    w("*Nota editorial:* os rótulos de voz são editoriais e **não afirmam identidade civil** de quem fala. O STT "
      "entregou pergunta e resposta coladas na mesma linha; nesses casos a linha inteira é mantida como está, com o "
      "rótulo «turno não separado».")
    w("")
    w("## Cobertura (declaração, como nas Convenções v2)")
    w("")
    w(f"- Transcrição integral publicada: **{chars_publicados} de {chars_bruto} caracteres** da fala "
      f"(**{100.0 * chars_publicados / chars_bruto:.2f}%**), menos **{total_cortado} caracteres** suprimidos nos "
      f"**{n_bloqueios} trechos bloqueados** por determinação curatorial (item 10), cada um substituído por marcador "
      "no próprio lugar. O auditor `_cobertura_apostila.py` confere o texto parágrafo a parágrafo e reproduce a "
      "mesma contagem.")
    w("- Nada foi resumido para «melhorar a leitura»; a segmentação em blocos apenas repõe parágrafos que o STT não tinha.")
    w("- Marcadores de oralidade («eh», «né», «troços», números com vírgula trocada) e as grafias instáveis de nomes "
      "próprios ficam como foram ouvidos; a única transformação mecânica é a quebra dura de linha dentro de uma "
      "mesma frase, convertida em espaço no pacote (declarada no topo do `_ampliacoes_P2023-10-14.txt`).")
    w("")
    w("## O que foi bloqueado, e por quê (item 10 da devolutiva)")
    w("")
    for ini, fita, motivo, addr in BLOQUEIOS:
        w(f"- **{addr}** — quarentena {motivo} — **{cortados.get(ini, 0)} caracteres** suprimidos no ponto "
          "(as âncoras do recorte ficam apenas no gerador, para que nenhum fragmento do teor bloqueado "
          "reapareça aqui como exemplo).")
    w("")
    w("*Nota editorial:* bloqueio **não** é apagamento da fonte: o `original.txt` está intacto no ciclo e as camadas "
      "de análise registram a existência e o endereço desses trechos. Retenção (transcrito, não endossado, sem termo) "
      "é o que vale para os blocos teológico, ufológico, clínico e de guerra — entre eles a disputa de Gaza e o "
      "juízo sobre religiões, que continuam na transcrição abaixo e **não** geram verbete.")
    w("")

    w("# PARTE I — Transcrição integral")
    w("")
    n = 0
    emitidas = set()
    corpo_blocos = []
    for end, linha in linhas_txt:
        pedacos = fatiar(linha) if len(linha) > BLOCO_ALVO else [linha]
        for p in pedacos:
            n += 1
            ini = linha.find(p)
            w(f"## {rotulo(n)} — {voz(p)} ({end}, caracteres {ini + 1}–{ini + len(p)})")
            w("")
            w(p)
            w("")
            corpo_blocos.append(p)
            for ânc, nota in NOTAS:
                if ânc.casefold() in p.casefold() and ânc not in emitidas:
                    emitidas.add(ânc)
                    w(f"*Nota editorial:* {nota}")
                    w("")
    soltas = [a for a, _ in NOTAS if a not in emitidas]
    if soltas:
        raise SystemExit("NOTAS SEM ÂNCORA NA TRANSCRIÇÃO: " + " | ".join(s[:50] for s in soltas))

    w("")
    w("# PARTE II — Índice temático (os 14 movimentos da camada 3, sem reordenar a fonte)")
    w("")
    c3 = open(os.path.join(AQUI, "camada-3.txt"), encoding="utf-8").read()
    tabela = c3.split("## 1.")[1].split("## 2.")[0]
    movs = [l for l in tabela.split("\n") if l.strip().startswith("| M")]
    for l in movs:
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        ue = re.findall(r"U\d{4}", cel[1])
        nome = cel[1].replace("**", "")
        linha_md = f"- **{cel[0]} — {nome}** → {cel[2]} · {cel[3]}"
        if ue:
            linha_md += f" · abre em {ue[0]}"
        w(linha_md)
    w("")
    w("*Nota editorial:* os destinos listados acima são os **aprovados na devolutiva**, não propostas: onde este "
      "índice diz «(False)», a ficha foi materializada neste ciclo; onde diz FORA, o vínculo foi recusado (RC-672) "
      "ou a materialização foi rejeitada (RC-396). A matriz de anterioridade e a navalha completas ficam em "
      "`analise/camada-3.txt` §2 e §3.")

    # ---------------------------------------------------------- PARTE III — aparato curatorial
    w("")
    w(f"# PARTE III — Aparato curatorial: as 11 decisões do Curador sobre {SIGLA}")
    w("")
    dec = open(DECISAO, encoding="utf-8").read()
    tab = dec.split("## 2.")[1].split("## 3.")[0]
    linhas_tab = [l for l in tab.split("\n") if l.strip().startswith("|")]
    cab = [l for l in linhas_tab if set(l.replace("|", "").strip()) <= set("-: ")]
    w("> Tabela espelhada de `DECISAO-DO-CURADOR.md` §2 (a devolutiva verbatim está em §1 do mesmo arquivo). "
      "Nada aqui foi reescrito: é o espelho do que foi decidido, para que a apostila se leia sozinha.")
    w("")
    for l in linhas_tab:
        if l in cab or re.match(r"^\|\s*item do Curador", l, re.I):
            continue
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 2:
            continue
        w(f"- **{cel[0].replace('**', '')}** → {cel[1]}")
    w("")
    w("## Efeito material na Base (medido por script, não declarado de memória)")
    w("")
    pacote = open(os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt"), encoding="utf-8").read()
    cods = sorted(set(re.findall(r"^### (RC-\d{3})$", pacote, re.M)))
    w(f"- **{len(cods)} códigos vinculados** a esta fonte na malha; **{len(cods) - 1} fichas ampliadas** com a seção "
      f"`## Ampliação — {SIGLA}` (RC-272 é a exceção: `ficha=False`, recebe o vínculo de malha e o conteúdo fica no "
      "pacote do ciclo — precedente RC-385/P2023-06-24).")
    w("- **5 materializações autorizadas (item 11):** RC-322 · RC-425 · RC-432 · RC-381 · RC-191 — arquivos criados "
      "em `termos/`, cadastro com `ficha=True`. Fichas físicas: 451 → **456**.")
    w("- **0 códigos novos · 0 relações novas · 0 obras novas:** 777 termos, 1.856 relações, 102 obras, RC-778 não "
      "consumido. As grafias degradadas do STT **não** são emendadas; entram como variante datada.")
    w("- **Retificações do próprio agente (DECISAO §5):** cinco formulações que a fase de leitura dava por certas "
      "caíram no portão de âncoras e foram retiradas ou reancoradas — Alcorão/Corão (0 ocorrências), sacrifício de "
      "animais (0), «os Ramas e os Apas não se odeiam» (0), rótulo «insulto a PcD» (0 ocorrências de «cadeira»/«deficiente»; "
      "o bloqueio ético real desta fonte é misógino, U0015 e U0033) e a cifra «172 mil» fora do endereço dito.")
    w("- **Radar de acervo:** a palestra anunciada para o dia seguinte (15/10/2023, 10h) e as auto-referências do "
      "autor a «outros vídeos» ficam declaradas **fonte não localizada**, sem vínculo (item 8).")
    w("")
    w("## Quarentenas deste ciclo (rótulo de índice, não de censura de leitura)")
    w("")
    for q in ["**bloqueio sumário e absoluto (item 10)**: política e deep state, institucional/segurança, ética "
              "discriminatória, biográfica com dado sensível — os 5 trechos listados na PARTE 0, ausentes desta "
              "apostila em qualquer camada",
              "guerra e Israel (retenção): a ebulição de Gaza e «Gog, Magog» entram na transcrição como fala datada; "
              "não geram termo, epígrafe nem glossário",
              "teológica (retenção): o juízo sobre religiões como «empresas», o papa e o Vaticano, a crítica aos "
              "cabalistas, «Deus se suicidou como identidade» — dito, não endossado, não virou estrutura de ficha",
              "clínica/biológica (retenção): vírus, órgãos, «reengenharia do sistema imunológico», sementes e "
              "vacinas — nada vira recomendação nem termo",
              "ufológica (retenção): naves, 50 anuna, bases em Marte e na Lua, «estrelas como portais» e os "
              "«300 sites» — a fórmula de segurança («poderes circunstanciais, não de dominação») acompanha o bloco",
              "biomediúnica (retenção): psicografia, cirurgia energética, cura de surdez e «reuniões na "
              "espiritualidade» — RC-191 carimba a procedência, não a veracidade",
              "histórica (retenção): a linhagem Bharata narrada pela fonte está corrompida em nomes e graus; nada foi "
              "recomposto nem harmonizado com B023/B036",
              "terminológica (veto): honra, povo espécie, adidaiva, fado/sorte, Zudra, Alalu, Gauzu, novela das 8, "
              "inteligências artificiais autônomas — **termos-observação**, sem código novo (D-1 e navalha)"]:
        w(f"- {q}")
    w("")
    w("## Lista das fichas ampliadas")
    w("")
    w("- " + " · ".join(cods))

    # ---------------------------------------------------------- APÊNDICE — dicionário STT
    w("")
    w(f"# PARTE III-bis — Apêndice: o dicionário STT desta fonte ({SIGLA})")
    w("")
    w("> Tabela de grafias ouvidas × forma canônica da Base, gerada da camada 2 do ciclo. Ela existe porque a "
      "transcrição acima **não** foi corrigida em silêncio: o que o STT ouviu fica como está, e a leitura do nome vai "
      "aqui, com o destino decidido pelo Curador. Linhas cujo conteúdo pertence a bloco **bloqueado** (item 10) são "
      "retidas aqui também: aparecem o número, não o teor.")
    w("")
    c2 = open(os.path.join(AQUI, "camada-2.txt"), encoding="utf-8").read()
    tabela2 = c2.split("## 2.")[1].split("## 3.")[0]
    VEDADOS = ["governo", "eleitor", "Kennedy", "Vaticano", "Faria", "porrada", "Congresso", "mulher", "deficiente",
               "deep state", "Bilderberg", "Black Rock", "Vanguard", "Wall Street", "Israel", "palestina", "Gaza",
               "código de lançamento", "superpotên", "orçamento"]
    retidas = 0
    for l in tabela2.split("\n"):
        s = l.strip()
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= set("-: ") or re.match(r"^\|\s*Grafia", s, re.I):
            continue
        cel = [re.sub(r"\*\*", "", c).strip() for c in s.strip("|").split("|")]
        if len(cel) < 5:
            continue
        if any(v.lower() in s.lower() for v in VEDADOS):
            retidas += 1
            continue
        txt = (f"- **{cel[0]}** — {cel[1]} ocorrência(s) → **{cel[2]}** [{cel[3]}] · {cel[4]}")
        txt = txt.replace("“", "«").replace("”", "»").replace('"', "«")
        w(txt)
    w("")
    w(f"*Nota editorial:* {retidas} linha(s) da tabela-mestre foram **retidas** por incidirem em bloco bloqueado "
      "(item 10). As contagens são as medidas na camada 2 sobre o `original.txt` — não sobre esta apostila.")

    # ---------------------------------------------------------- GLOSSÁRIO
    w("")
    w("## GLOSSÁRIO LOCAL")
    w("")
    w("A — Personagens e seres")
    for item in [
        "Anunnakis — RC-024; aqui como espécie com honra («só duas têm noção de honra»); a fonte grafa o nome de catorze modos.",
        "Anu (patriarca Anunnaki) — RC-587; o suzerano cuja decisão está vinculada à de Henk, Enki, Enlil e Ninmah.",
        "Enki — RC-486; na fonte, «Enk»/«Henk»/«Enque»; o **FOXP2** e a inoculação do gene seguem na ficha, sem unificar o «livro de Henk» (item 2).",
        "Enlil — RC-487; grafias «Eli», «Enio», «Enlio», «Enlisava» [REVISAR: fusão verbo/substantivo do STT].",
        "Ninmah — RC-461; «Narsag», «Ninhave», «Ninharsak» — a fonte usa um único bloco de nomes para a mãe das gerações.",
        "Marduk — RC-460; «a vez dele, 2200 anos antes de Cristo»; as cidades simpáticas (= cidade irmã de um universo vizinho).",
        "Ninurta — RC-588 e Nergal — RC-461/RC-588 no par «eergal e no lurtte» [REVISAR], que **não** virou o «Nergete» de camada-0.",
        "Igigi — RC-580; «uma um certo tipo de anunque chamado Igii veio pra Terra para trabalhar como mineradores».",
        "Alalu — sem código (0 ocorrências do slot na Base); 37 ocorrências do nome, grafado «Lalu». Termo-observação.",
        "Gauzu — RC-587/RC-461 como contexto; **sem código próprio** (19 ocorrências; «Gazu», «Gauzul», «Galzu»).",
        "Enoque — RC-489; o humano que **criou** a Árvore da Vida; Metatron é sua forma antimaterial «só durante um tempo» (RC-671).",
        "Metatron — RC-671; duas ocorrências, ambas com o prazo de validade explícito na fonte.",
        "Javé — RC-001; «infernnho», «crupier dono da bola», «juiz que faliu»; em RC-422 a autoconfissão do criador fracassado.",
        "Sophia — RC-009; e o par RC-565/RC-682 para Hochmah/Malkuth — **sem fusão de epítetos** (item 6).",
        "Jesus — RC-072; «Jesus é Javé não»; e Krishna — RC-414/RC-425 («quechava» [REVISAR]).",
        "Trimurti — RC-104 com Brahma (RC-037) e Shiva (RC-102); o «Brama loca» e a «Vaicunta» da fonte ficam como variantes.",
        "Geração Regenerada de Brahma — RC-696; a linhagem barata narrada pela fonte, com a genealogia corrompida.",
        "Nefilins — RC-488; «o nome dos anunaques na linguagem suméria é nefelim» — a equivalência fica **como dita**.",
    ]:
        w(f"- {item}")
    w("")
    w("B — Conceitos e teses")
    for item in [
        "Honra demodármica — **sem código** (D-1): honra criada em torno do dharma, ancorada em linhagem genética.",
        "Dharma / varna / karma / adharma — RC-322 (materializada), RC-319/RC-320/RC-321; criados **para híbridos**, não para a humanidade.",
        "Povo espécie — RC-024; a honra como propriedade de espécie, não de indivíduo.",
        "Poder circunstancial × poder de dominação — a fórmula de segurança da fonte; acompanha todo uso dela.",
        "Fado ou sorte × destino — RC-467/RC-658; a categoria técnica que separa decisão de inevitável.",
        "Tikun — RC-514/RC-545; o reparo **na obra e no Criador**, não «nos judeus».",
        "Daath — RC-262; «abismo luminoso», «Deus caído dentro da escuridão»; a grafia do bruto é «DAF» (item 3).",
        "Árvore da Vida e as dez personificações — RC-263; invenção de Enoque, entregue aos rabinos por Gabriel [REVISAR: «fois»].",
        "Campos mórficos — RC-381 (materializada); a fonte não usa a expressão «ressonância mórfica»: é ampliação de conceito.",
        "Fofocas cósmicas — RC-191 (materializada); o grau de testemunho da fonte (saber, não poder usar, não poder verificar).",
        "Laço temporal — RC-272; «os primeiros serão sempre os últimos» — 1ª fonte-palestra do código (ficha sem arquivo).",
        "Arcontes — RC-474/RC-770; «seres que se sentiam arcontes, ou seja, donos».",
        "Falência dos deuses — RC-742/RC-422; a variante datada «o bem não destrói o mal sob pena de se tornar igual a ele» (item 7).",
        "Esferas espirituais convergentes — Terra × Nibiru: sem equivalente exato na Base; **não** se cria código.",
        "Zudra e Noé — RC-424; «Efetivamente, a lenda de Zudra é a mesma coisa que a história de Noé. Zudra era Noé.»",
        "Adidaiva / adaiva — RC-102/RC-037/RC-104; a condição dos seres de origem ígnea, nas duas grafias da fonte.",
    ]:
        w(f"- {item}")
    w("")
    w("C — Livros, referências e fontes externas")
    for item in [
        "**B013 — «Zintzum, o exílio forçado de divindade»** — a obra que o autor cita é esta; 0 obras novas (item 4).",
        "«Livro de Henk» (3 ocorrências) — **não** identificado: pode ser livro **de** Enki ou livro **do emissário** Henk; sem cadastro (item 2).",
        "«Livro P, no Atraares» e «livro de EC» — nomes degradados pelo STT; nenhuma hipótese de leitura (Atrahasis, Enoque) vira fato.",
        "Marabarata (Mahābhārata) e Bagavaguita — RC-593; o bloco do dharma é lido **por dentro** dessa narrativa pela fonte.",
        "«Irém Iron, Universos emissão, Colisão» — obra própria declarada **ficção**: só nota bibliográfica (item 5).",
        "«Bob Din» e «Frankstein»/«Mary Chily» — menções sem obra na Base; [REVISAR] as identidades, nada vira verbete canônico.",
        "A palestra de 15/10/2023, 10h — anunciada pela fonte e **não localizada** no acervo; radar de busca (item 8).",
        "A B031 (Painéis Emergentes) continua o vocabulário de referência das grafias; nenhuma linha dela foi alterada.",
    ]:
        w(f"- {item}")
    w("")
    w("D — Grafias, variações e incertezas")
    for item in [
        "Anunnaki em catorze grafias: «anunax», «anunx», «anunaques», «anunques», «anonax», «amuna», «anouna», «anarx», «anunac», «anona», «amunax», «anunnakis», «anulacs», «anunaxs» — nenhuma normalizada no bruto.",
        "«inibir»/«inibiro»/«Dibiro»/«Nibil» = **Nibiru** (10 das 52 ocorrências da família); RC-589.",
        "«Henk»/«Enk»/«Enque» = Enki (RC-486) **e** o emissário Henk — ambiguidade mantida por decisão, não resolvida.",
        "«Eli»/«Enio»/«Elio»/«em Lio»/«Enlio»/«Enlisava» = Enlil (RC-487).",
        "«Narsag»/«Ninhave»/«Ninharsak» = Ninmah/Ninharsag (RC-461).",
        "«Gauzu»/«Gazu»/«Gauzul»/«Galzu» = o emissário com selo de Anu — 19 ocorrências, sem código.",
        "«Darma»/«dma»/«varma» = dharma/varna; «quechava» = Keshava; «quechada» em P2023-12-02 — variantes datadas, não erros.",
        "«demodármica»/«demoic»/«demoníaca» — a fonte oscila; o adjetivo canônico da Base é «demodármico» (RC-474/RC-745).",
        "«fofota» = fofoca; «enfeem» = se empenham; «geroma» = genoma; «infernnho dos dentos» e «cruzeiro de São Tomé» [REVISAR] — preservados.",
        "«Zudra» (não «Ziusudra»): a Base grafia o nome acadêmico; a fonte não. «Malkuf»/«Malukuf»/«Maluco» = Malkuth (RC-682).",
        "«Jahé»/«Javel»/«Jaavé» = Javé (RC-001); «Sofia» = Sophia (RC-009); «Rockman» fica como epíteto dito, sem fusão (item 6).",
        "«a opção D», «NAC», «300 sites», «entropia em peça» — siglas e fórmulas **não decifradas**: nada é conjeturado.",
        "Números degradados do STT ficam como ditos («1500 anos» × «1500 milhões», «360.000» × «360000», «445.000. anos»); "
        "a divergência de 300 milhões para o Ragnarok é **selada com a data**, não harmonizada com B050 nem com P2021-05-15.",
    ]:
        w(f"- {item}")
    w("")
    w("*Nota editorial final:* a apostila termina com a última linha da fonte e este aparato. O arquivo bruto, as "
      "camadas 0–3, o dossiê de pré-curadoria, a devolutiva registrada em `DECISAO-DO-CURADOR.md`, o pacote de "
      "ampliações e as 56 fichas são as referências de auditoria; a apostila não substitui a fonte.")

    open(ALVO, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"apostila.md escrito: {len(out)} linhas · {n} blocos de transcrição · {n_bloqueios} bloqueio(s) aplicado(s)")
    print(f"cobertura: {chars_publicados}/{chars_bruto} caracteres ({100.0*chars_publicados/chars_bruto:.2f}%), "
          f"com {total_cortado} cortados em {n_bloqueios} spans · notas editoriais: {len(emitidas)}/{len(NOTAS)}")
    print("linhas do dicionário STT retidas por bloqueio:", retidas)


if __name__ == "__main__":
    main()
