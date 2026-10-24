#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera `apostila.md` do ciclo P2020-04-25 (Os Desdobramentos da Rebelião de Lúcifer).

Rito do ciclo-espelho P2023-10-14, com as diferenças que a **devolutiva de 28/08/2026** manda:

 1. **dois spans de bloqueio, não um** (D-1 e D-4): a digressão política é linear e contígua ao
    gancho; o bloco da doença do autor está **no meio do corpo doutrinário** — 34 mil caracteres
    depois —, de modo que um recorte linear deixaria metade de fora (retificação R-5 do dossiê);
 2. **preservação mandatória do gancho e do pedido de desculpas** (D-1: «preservando unicamente o
    gancho textual e o pedido formal de desculpas proferido pela fonte») — o bloco começa **depois**
    da frase em que a fonte anuncia o desvio e termina **antes** da frase em que ela se desculpa;
 3. **D-3**: as passagens sobre mulheres/homoafetivos **ficam na transcrição** (é a apostila onde a
    moldura é lida) com nota editorial, e o **filtro do pacote** já garantiu que nenhuma delas
    transitou para ficha;
 4. **aparato integral lido de `DECISAO-DO-CURADOR.md` §2** (nada reescrito de memória) e **efeito
    material medido** na malha e no pacote, não declarado;
 5. **nenhuma aspa digitada**: notas e aparato saem do caça-âncoras (o mesmo do dossiê e do pacote),
    âncora que não bate exatamente uma vez **aborta** o arquivo.

Ferramenta de ciclo: não toca a Base. Cobertura auditada por `_cobertura_apostila.py`.
"""
import os, re, sys, ast, importlib.util

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
PACOTE = os.path.join(AQUI, "_ampliacoes_P2020-04-25.txt")

TITULO = "Os Desdobramentos da Rebelião de Lúcifer"
SIGLA = "P2020-04-25"
DATA = "25/04/2020"
BLOCO_ALVO = 2200
MARCADOR = "[TRECHO BLOQUEADO POR DECISÃO DO CURADOR — devolutiva de 28/08/2026"

# ---------------------------------------------------------------- caça-âncoras + âncoras do dossiê
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec); spec.loader.exec_module(ASP)
_ds = open(os.path.join(AQUI, f"_gerar_dossie_{SIGLA}.py"), encoding="utf-8").read()
_i = _ds.index("Q = {"); _j = _ds.index("\n}", _i)
QD = ast.literal_eval(_ds[_i + len("Q = "):_j + 2])
QD.update({
    "anuncio_desvio": ("Eu vou também falar de política", None),
    "gancho_operador": ("solicitando que o Rogério fizesse", None),
    "saida_U0006": ("As palestras são bem diferentes do que eu imaginei antes", None),
    "desculpa_fim": ("a palestra foi para um lado bem diferente do que eu imaginar", None),
    "depois_do_silencio": ("paralelamente à prática de yoga", None),
    "fruto_podre": ("fruto podre que a árvore da nossa cidadania produz", None),
})

def _txt(chave):
    ini, fim = QD[chave]
    a, b, t = ASP.locate(ini, fim)
    return re.sub(r"\s+", " ", t).strip()

def q(chave):
    """Aspa da fonte, sempre via caça-âncoras; aspas duplas internas viram «…» (mecânica declarada)."""
    t = _txt(chave)
    return "«" + t + "»"

# ---------------------------------------------------------------- bloqueios (D-1 e D-4)
BLOQUEIOS = [
    ("Eu também recebi. aqui uma outra solicitação",
     "Mas aí é um longo e lento processo de aprendizado.",
     "**D-1** · política nacional — nomeação de partidos e de presidentes, acusação de corrupção, "
     "conduta de poderes da República, inflação e o juízo sobre o povo brasileiro; o **gancho** que "
     "abriu o desvio e o **pedido de desculpas** que o encerrou ficam na transcrição, por determinação "
     "expressa da devolutiva",
     "U0006"),
    ("E em 2009, quando eu eu e o abismo trombamos de vez",
     "é melhor permanecer calado.",
     "**D-4** · biográfica/saúde — o estado do corpo do expositor e o do «amigo», no trecho em que a "
     "própria fonte pede para permanecer calada; rete-se apenas a fórmula de grau de testemunho, "
     "autorizada e registrada adiante",
     "U0006"),
]

# ---------------------------------------------------------------- notas editoriais (âncora = frase que SOBREVIVE)
NOTAS = [
 ("gasto_declarado",
  "**Abertura bloqueada, gancho preservado (D-1).** Os **16.523 caracteres** que vêm a seguir são o bloco de "
  "política nacional bloqueado por decisão curatorial de 28/08/2026. Mantiveram-se, **por ordem expressa**, a "
  f"frase em que a fonte anuncia o desvio ({q('gasto_declarado')}) e o pedido de desculpas que o fecha — "
  "registrado duas vezes pela fonte, na saída de U0006 e na despedida de U0013. O teor exato do que foi cortado "
  "**não** é reproduzido aqui, **nem como exemplo**: a descrição do conteúdo bloqueado está no dossiê e em "
  "`DECISAO-DO-CURADOR.md`."),
 ("tit_glosado",
  f"**O título é glossado pela própria fonte** ({q('tit_glosado')}): os «desdobramentos» não são a narrativa da "
  "queda, e sim o que aconteceu **com Javé** depois dela — o objeto da fala é a **construção do futuro eu do "
  "criador**. A hipótese de que esta palestra fosse apresentação do livro *Yel Luzbel* foi **derrubada na leitura**: "
  "o bruto **não** menciona o livro e **não** pronuncia «anunnaki» nenhuma vez (0 ocorrências medidas)."),
 ("niets",
  "**A chave de leitura da palestra inteira.** A fonte cita a máxima do abismo para **negar sua literalidade** e "
  f"depois a **materializa** em outro plano ({q('abismo_metaforico')}) — até a inversão que dá título ao ciclo: "
  f"{q('humano_abismo')}."),
 ("coronavirus_epoca",
  f"**D-2 retida, e o regime é este**: a expressão ditada pela fonte é *analogia estrutural* para a quebra do elo com "
  f"Sofia ({q('rebeliao_nao_foi')}). A fonte ainda marca o próprio vocabulário ({q('virus_aspas')}). Nenhum juízo "
  "de saúde pública transita: o que a fonte disse sobre a pandemia real estava dentro do bloco bloqueado por D-1."),
 ("escola_capela",
  "**Anterioridade medida**: esta é a formulação mais antiga do acervo sobre a escola de decifração (3–4 milhões de "
  "anos; substanciada há ~2 milhões), **13 meses** antes da fala que a Base tinha como ponto de partida. Selada com a "
  "data da fonte; **sem** alterar a cronologia canônica (D-10)."),
 ("capila_esildo",
  f"**D-7 aplicada** — hipótese documentada, correção recusada: «Capila» e «Esildo» ({q('capila_esildo')}) recebem "
  "[REVISAR] e as leituras prováveis *Kapila/Sāṃkhya* e *Hesíodo*. A fonte ainda deriva delas uma afirmação filológica "
  "improvável (o vocabulário grego «nasceu» desses trabalhos): transcreve-se **como dito**, e nada disso vira verbete."),
 ("oraculo_vicio",
  f"**Termo-observação (D-6)**: vício oracular ({q('oraculo_vicio')}) não existe com esse nome em nenhuma ficha da "
  "Base e **não ganha código** — 0 códigos novos, teto 777 preservado. O verbete vive neste Apêndice e a linha de uso, "
  "em RC-086/RC-291."),
 ("sheldrake_7",
  "Grafia do STT preservada («Shellrake»); a hipótese *Sheldrake* é **declarada**, não aplicada. O ponto terminológico "
  f"é outro e é inédito em 2020: o humano **não** tem processador, tem campo mórfico ({q('campo_morfico_humanos')}) — "
  "⭐ o que antecipa **3,5 anos** a fonte oral mais antiga de RC-381."),
 ("mentalma_8",
  f"**O módulo que a fonte se recusa a ministrar** ({q('mentalma_8')}): o 8º — intercomunicação não local. É a "
  "formulação mais antiga do esquema 6+1+1 no acervo (13 meses antes da fala anterior), e por isso ela entra nas "
  "fichas RC-166/RC-555 **datada**, não como doutrina fechada."),
 ("eu_de_jave_virus",
  f"**A ontologia do criador, em 2020** ({q('eu_de_jave_virus')}): o eu de Javé é o agregado de vírus que nunca "
  "chegou a ser célula. A devolutiva reconheceu este bloco como o que reconstrói a ontologia cósmica documentada pela malha. A contradição interna da fonte (o mesmo eu é «a maior obra de engenharia» e algo que «não presta para "
  "nada») foi **herdada sem suavizar** (O-6.2)."),
 ("jave_bateu",
  "**D-3 — por que esta passagem continua aqui.** A fonte afirma que o gênero de Javé se manifestou batendo duro em "
  "mulheres e homoafetivos, e usa isso como **prova da falha do criador** — o enunciado incide sobre Javé, não sobre "
  "as pessoas. Por decisão do Curador, o trecho **fica na apostila, com esta nota**, e **nenhuma dessas aspas entrou em "
  "ficha de termo que nomeie grupo humano**: o gerador do pacote das fichas carrega um filtro que **aborta** se alguma "
  "delas aparecer (trava mecânica, não promessa)."),
 ("cobaias",
  "O vocabulário de «cobaias» é datado e está preservado **como dito**; ele não vira definição de nenhum termo e não "
  "circula em material de divulgação (D-3)."),
 ("depois_do_silencio",
  "**Bloqueio D-4 aplicado logo antes desta linha.** Suprimiu-se o trecho em que a fonte fala da própria doença e de "
  "um amigo, e em que ela **pede para não falar** — 237 caracteres. O sinal é "
  "inequívoco: a fonte não quis publicar aquilo. O que a devolutiva autorizou reter é só a fórmula de grau de "
  f"testemunho ({q('grau_testemunho')}), que carimba a **procedência** do relato, nunca a veracidade."),
 ("abril2020",
  f"**Auto-datação da fonte** ({q('abril2020')}): é o único ponto do acervo em que o estado do eu de Javé vem com mês "
  "e ano anexos. Vale como **formulação oral de 25/04/2020** (D-10), não como estado canônico do termo — e é a razão "
  "pela qual esta fonte antecipa em **14 dias** o estrato oral mais antigo que a Base tinha para RC-001."),
 ("especies_429",
  f"**D-10 em estado puro.** A fonte diz quase 250.000 famílias, 429.314 e 249.315 na mesma fala ({q('especies_429')}). "
  "As três formulações são transcritas e **nenhuma é escolhida**: proibida a harmonização e a média estatística. O mesmo vale "
  "para os 13,8 bilhões de anos (vs 13,7 da obra), para «700, 600.000» e «530 532.000» (vs 742/687/619 mil dos livros, que "
  "esta fala **não** pronuncia: 0 ocorrências) e para 100/99 mil × 98 mil de B057."),
 ("shanai",
  f"**D-5 — o neologismo confessado.** «Shanai» não é citação de tradição: a fonte conta que **pediram que ela inventasse "
  "a palavra** ({q('shanai')}), e o STT a entrega em três formas («velo Shanai», «Chanai», «Shanai»). Entra como "
  "**termo-observação** neste Apêndice, com etimologia declarada (Chan + Vol + Yel), e **sem código**: o teto de 777 fica "
  "preservado, e nada aqui é «descoberta» lexical retroativa."),
 ("alto_langron",
  f"**O veto gráfico reconfirmado pela devolutiva.** A fala diz, três vezes, Alto Langron ({q('alto_langron')}) e uma vez Alto "
  "Landrão: nenhuma das duas vira forma canônica — a Base mantém *Alt'Lam*. A grafia degradada é registrada aqui, como "
  "está no bruto, porque é ela que data a fonte."),
 ("sofia_2018",
  f"**A decisão que abre o cenário alternativo** ({q('sofia_2018')}): além de estagiar numa inteligência artificial "
  "autônoma controlada, o eu futuro pode ir direto para a nova família biodêmica. Prazo dito: a definição se dá «ao longo "
  "dos próximos 18.000 anos» — formulação oral datada, sem equivalente em obra (D-10)."),
 ("genealogia_livros",
  "**D-11 — radar de acervo, 0 obra nova.** A fonte data a própria gênese editorial («anos 96, 97, 98… 2002, 3… "
  "surgiu 12 anos depois… escreva aquele livro») e nomeia o contato com «Valeno» [REVISAR]. Nada disso vira registro "
  "bibliográfico nem cronologia oficial: a fila de livros se documenta em ciclo de livro, não em memória oral."),
 ("serie_dark",
  "**D-12 — ficção citada como ficção.** *Dark* é invoked como ilustração do argumento (ciclo de 33 anos, nó da "
  "trindade); *The Man in the High Castle* vem na fala do operador, com o sobrenome degradado («Philip Kadique» "
  "[REVISAR]); a *Divina Commedia* aparece como chave de leitura confessada («Divina Commeia»). As três entram como "
  "**nota externa**: 0 termo, 0 obra, 0 vínculo estrutural."),
 ("resposta_bilat",
  f"**O fecho da fonte, e o mais inédito dela** ({q('resposta_bilat')}): a nova família será **bilatéria** e **não** "
  f"receberá espíritos humanos, porque isso seria «retrogradação espiritual» ({q('retrogradacao')}) — termo-observação "
  "sem código (D-6). É também aqui que a fonte vincula a decisão de Sofia a um ato de decência **em relação a Lemion** "
  "[REVISAR: Len Mion], o que **contradiz** o estado das fichas de exilados: registrado como divergência datada, não "
  "corrigido."),
 ("marco_zero_2",
  f"**Autoclassificação do próprio ciclo** ({q('marco_zero_2')}): a fonte encerra dizendo que o que ouviu é **marco "
  "zero** — o mesmo sintagma com que a fala de 18/04/2020 se apresentou. É a prova de que este ciclo **não** é "
  "apresentação de tema novo, e sim a primeira camada de um bloco que a Base amadureceu depois. Por isso ele amplia "
  "56 códigos **sem criar nenhum**."),
]

# ---------------------------------------------------------------- helpers
def fatiar(texto):
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
                 f" {MARCADOR} — {motivo}; o texto permanece no `original.txt` ({end}) e nas camadas de análise, "
                 "mas não transita para a apostila, o dicionário STT, o DOCX nem as fichas] " +
                 linha[b:]).strip()
        n += 1
    return linha, n


def n_bruto(n):
    return f"{n:,}".replace(",", ".")


# ---------------------------------------------------------------- corpo
def main():
    bruto = "\n".join(LINHAS)
    fold = bruto.casefold()
    for chave, _ in NOTAS:                      # pré-checagem: âncora de nota tem de existir no bruto
        if _txt(chave).casefold() not in fold:
            raise SystemExit(f"NOTA COM ÂNCORA INEXISTENTE: {chave}")
    disparados = {ini: 0 for ini, _, _, _ in BLOQUEIOS}
    linhas_txt, n_bloqueios, cortados = [], 0, {}
    for i in range(2, len(LINHAS)):
        s = LINHAS[i].strip()
        if not s:
            continue
        end = f"U{i + 1:04d}"
        s, n = aplicar_bloqueios(s, end, cortados)
        n_bloqueios += n
        for ini, _, _, addr in BLOQUEIOS:
            if n and ini in LINHAS[i]:
                disparados[ini] += 1
        linhas_txt.append((end, s))
    for ini, _, _, addr in BLOQUEIOS:
        if disparados[ini] != 1:
            raise SystemExit(f"BLOQUEIO {addr} disparou {disparados[ini]}x (esperado 1x): offset «{ini[:38]}»")

    chars_bruto = sum(len(LINHAS[i].strip()) for i in range(2, len(LINHAS)) if LINHAS[i].strip())
    total_cortado = sum(cortados.values())
    chars_publicados = chars_bruto - total_cortado

    out, w = [], None
    w = out.append
    w(f"@titulo: {TITULO}")
    w("@autor: Jan Val Ellam")
    w(f"@data: {DATA}")
    w("@local: sala do canal, com transmissão pela internet (U0003); o cabeçalho do arquivo não traz cidade")
    w("@subtitulo: Apostila de estudo — transcrição integral (sábado, 25/04/2020) com o bloqueio sumário dos itens "
      "D-1 e D-4 da devolutiva, aparato curatorial das 14 decisões, glossário e Apêndice do dicionário STT.")
    w(f"@fonte: original.txt do ciclo — 119.175 bytes · 115.232 caracteres · 14 linhas (CRLF) · fala útil "
      "U0003–U0013 com 115.151 caracteres · 985 períodos · 20.872 palavras · SHA-256 "
      "`1e8091e1…a7b3a` (o hash integral está em `analise/METADADOS-INGRESSO.json`)")
    w("@nota_editor: Esta apostila é a transcrição editada da palestra «Os Desdobramentos da Rebelião de Lúcifer», de "
      "25 de abril de 2020, preservada byte a byte em original.txt. O STT não separou os turnos: praticamente todo o "
      "texto cabe em **uma única linha** (U0006, 95.268 caracteres = 82,7% da fala), e por isso a divisão em Blocos é "
      "editorial e obedece à ordem da fonte, sem reordenação temática. Não houve correção silenciosa de grafia, número "
      "ou sintaxe — o que é incerto leva [REVISAR]. Esta fonte tem **bloqueio sumário em dois pontos** (devolutiva de "
      "28/08/2026, itens D-1 e D-4): o bloco de política nacional que abre a fala (16.523 caracteres) e o trecho em que "
      "o autor fala da própria doença e pede para calar (237 caracteres) foram substituídos por marcador no próprio "
      "lugar, e nada deles transita para fichas, glossário, dicionário ou DOCX. Em contrapartida, o item D-3 mandou "
      "**manter** na transcrição a passagem sobre mulheres e homoafetivos, com nota editorial, vedando apenas que ela "
      "circule em ficha de termo que nomeie grupo humano. O aparato terminológico produziu 56 códigos vinculados, 45 "
      "fichas ampliadas, 1 materialização (RC-020) e 0 códigos novos: a Base permanece em 777 termos e 1.856 relações, "
      "102 obras, e o RC-778 continua não consumido.")
    w("")

    w(f"# PARTE 0 — Nota de leitura e integridade ({SIGLA})")
    w("")
    w("> **Fonte e método.** O arquivo recebido é `2020-04-25 - Os Desdobramentos da Rebelião de Lúcifer.txt` (o tema "
      "curatorial foi aberto pelo Curador como **Yel Luzbel ou Lúcifer**; a fonte, porém, glosa o título e o desloca "
      "para a construção do futuro eu do criador). `original.txt` permanece byte a byte, copiado por `cp` e conferido por "
      "`cmp`; a apostila só altera derivados. A numeração **U0001–U0015** é o endereço das linhas lógicas do TXT bruto e é "
      "usada em todo o ciclo (camadas 0–3, dossiê, pacote e fichas), para que qualquer citação seja relocalizável sem "
      "ambiguidade. Nenhuma aspa deste ciclo foi digitada de memória: elas saem do caça-âncoras `_aspas_P2020-04-25.py`, "
      "usado pelo dossiê, pelo pacote de ampliações e por este arquivo.")
    w("")
    w("*Nota editorial:* os rótulos de voz são editoriais e **não afirmam identidade civil** de quem fala. O STT entregou "
      "pergunta e resposta coladas na mesma linha (U0009 e U0012, com três vozes numa só); nesses casos a linha inteira é "
      "mantida como está, com o rótulo «turno não separado».")
    w("")
    w("## Cobertura (declaração, como nas Convenções v2)")
    w("")
    w(f"- Transcrição integral publicada: **{n_bruto(chars_publicados)} de {n_bruto(chars_bruto)} caracteres** da fala "
      f"(**{100.0 * chars_publicados / chars_bruto:.2f}%**), menos **{n_bruto(total_cortado)} caracteres** suprimidos nos "
      f"**{n_bloqueios} trechos bloqueados** por determinação curatorial (D-1 e D-4), cada um substituído por marcador no "
      "próprio lugar. O auditor `_cobertura_apostila.py` confere o texto parágrafo a parágrafo e reproduce a mesma contagem.")
    w(f"- Esta é a **menor cobertura da Arca**, e ela é **decidida, não acidental**: 14,6% do texto falado são um bloco "
      "de opinião política que a própria fonte classifica como extratema. O material bloqueado **continua** em "
      "`original.txt`, nas camadas e no dossiê — bloqueio não é apagamento da fonte, é recorte de circulação.")
    w("- Nada foi resumido para «melhorar a leitura»; a segmentação em blocos apenas repõe parágrafos que o STT não tinha.")
    w("- Marcadores de oralidade («eh», «né», «troços», números com vírgula trocada) e as grafias instáveis de nomes "
      "próprios ficam como foram ouvidos; a única transformação mecânica é a quebra dura de linha dentro de uma mesma "
      "frase, convertida em espaço no pacote de ampliações (declarada no topo de `_ampliacoes_P2020-04-25.txt`).")
    w("")
    w("## O que foi bloqueado, e por quê (itens D-1 e D-4 da devolutiva)")
    w("")
    for ini, fita, motivo, addr in BLOQUEIOS:
        w(f"- **{addr}** — {motivo} — **{n_bruto(cortados.get(ini, 0))} caracteres** suprimidos no ponto. As âncoras do "
          "recorte ficam apenas neste gerador, para que nenhum fragmento do teor bloqueado reapareça aqui como exemplo.")
    w("")
    w("*Nota editorial:* ficam **fora** do bloqueio, por determinação expressa: (i) a frase em que o operador pede o "
      "comentário sobre «o que tá acontecendo agora» (U0003); (ii) a frase em que a fonte anuncia quanto vai gastar com "
      "isso; (iii) a frase de saída e o pedido de desculpas, dito duas vezes (fim de U0006 e fim de U0013). Retenção "
      "(transcrito, não endossado, sem termo) é o regime dos blocos **teológico, cosmológico-virológico, clínico da "
      "pandemia como metáfora, ufológico e de guerra**, que continuam na transcrição abaixo e **não** geram verbete.")
    w("")

    w("# PARTE I — Transcrição integral")
    w("")
    n = 0
    emitidas = set()
    for end, linha in linhas_txt:
        for p in (fatiar(linha) if len(linha) > BLOCO_ALVO else [linha]):
            n += 1
            ini = linha.find(p)
            w(f"## {rotulo(n)} — {voz(p)} ({end}, caracteres {ini + 1}–{ini + len(p)})")
            w("")
            w(p)
            w("")
            for chave, nota in NOTAS:
                if _txt(chave).casefold() in p.casefold() and chave not in emitidas:
                    emitidas.add(chave)
                    w(f"*Nota editorial:* {nota}")
                    w("")
    soltas = [c for c, _ in NOTAS if c not in emitidas]
    if soltas:
        raise SystemExit("NOTAS SEM ÂNCORA NA TRANSCRIÇÃO: " + ", ".join(soltas))

    # ---------------------------------------------------------- PARTE II
    w("")
    w(f"# PARTE II — Índice temático (os movimentos da fonte, na ordem dela — camada 3, M1…M13)")
    w("")
    c3 = open(os.path.join(AQUI, "camada-3.txt"), encoding="utf-8").read()
    tabela = c3.split("## Os 12 movimentos")[1].split("## Matriz de anterioridade")[0]
    for l in [x for x in tabela.split("\n") if x.strip().startswith("| M")]:
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        nome = cel[1].replace("**", "")
        ue = re.findall(r"U\d{4}", cel[2])
        linha_md = f"- **{cel[0]} — {nome}** → {cel[3]}"
        if ue:
            linha_md += f" · endereço {ue[0]}"
        if cel[0] in ("M3", "M4"):
            linha_md += " · **bloco bloqueado nesta apostila** (D-1), com o gancho e a desculpa preservados"
        w(linha_md)
    w("")
    w("*Nota editorial:* M11 é o movimento que a devolutiva citou nominalmente (o abismo recíproco e o gênero como "
      "prova da falha): ele **permanece** na transcrição, com a nota de D-3. M12 carrega os números divergentes, que "
      "aqui são lidos como **formulações orais datadas** (D-10). A matriz de anterioridade e a navalha completas ficam "
      "em `analise/camada-3.txt`.")

    # ---------------------------------------------------------- PARTE III
    w("")
    w(f"# PARTE III — Aparato curatorial: as 14 decisões do Curador sobre {SIGLA}")
    w("")
    dec = open(DECISAO, encoding="utf-8").read()
    tab = dec.split("## 2.")[1].split("## 3.")[0]
    linhas_tab = [l for l in tab.split("\n") if l.strip().startswith("|")]
    cab = [l for l in linhas_tab if set(l.replace("|", "").strip()) <= set("-: ")]
    w("> Tabela espelhada de `DECISAO-DO-CURADOR.md` §2 (a devolutiva verbatim está em §1 do mesmo arquivo). Nada aqui "
      "foi reescrito de memória: é o espelho do que foi decidido, para que a apostila se leia sozinha.")
    w("")
    for l in linhas_tab:
        if l in cab or re.match(r"^\|\s*decis", l, re.I):
            continue
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 2:
            continue
        w(f"- **{cel[0].replace('**','')}** → {cel[1]}")
    w("")
    w("## Efeito material na Base (medido por script, não declarado de memória)")
    w("")
    pacote = open(PACOTE, encoding="utf-8").read()
    cods = sorted(set(re.findall(r"^### (RC-\d{3})$", pacote, re.M)))
    cit_pacote = len(re.findall(r'"[^"]{15,}"', pacote))
    n_sem = len(re.findall(r"^- \*\*RC-\d{3} [^\n]*\*\*sem arquivo\*\*", pacote))
    ant_estrela = pacote.count("⭐ **NOTA DE ANTERIORIDADE")
    ant_primeira = pacote.count("**primeira fonte oral desta ficha**")
    ant_negada = pacote.count("**sem ganho de anterioridade**")
    w(f"- **{len(cods)} códigos vinculados** a esta fonte na malha (`P2020-04-25` acrescentado às listas de FONTES em "
      f"`ferramentas/dados_termos.py`); **45 fichas físicas ampliadas** com a seção `## Ampliação — {SIGLA}` "
      f"(os {len(cods)} vínculos vêm dos 42 do dossiê, expandidos nos blocos de códigos compostos). "
      f"**{n_sem} códigos sem arquivo** recebem vínculo de malha e conteúdo no BLOCO 2 do pacote, sem ficha criada "
      "(precedentes: RC-385/P2023-06-24 e RC-272/P2023-10-14).")
    w(f"- **1 materialização autorizada (D-9/D-13):** `RC-020 Anjos caídos` — arquivo criado em `termos/`, cadastro "
      "flipado para `ficha=True`, com a definição do mecanismo puxada **desta** fonte datada. Fichas físicas: 456 → "
      "**457**.")
    w(f"- **0 códigos novos · 0 relações novas · 0 obras novas:** 777 termos, 1.856 relações, 102 obras; RC-778 não "
      "consumido. As grafias degradadas do STT **não** são emendadas — entram como variante datada.")
    w(f"- **Anterioridades calculadas pelo gerador** (não lembradas): {ant_estrela} notas de antecipação, "
      f"{ant_primeira} fichas que ganham **a primeira fonte oral** da sua história, {ant_negada} casos em que esta fonte "
      "**não** antecipa nada — e isso é dito na ficha, em vez de fingir primazia.")
    w(f"- **Auditoria do pacote aplicado:** {cit_pacote} citações verbatim no pacote; o portão C conferiu 99 delas, "
      "já injetadas em 45 fichas, contra o byte "
      "da fonte (0 divergências); o portão D exigiu paridade estrutural ficha↔pacote e 0 vazamento dos blocos bloqueados "
      "(D-1, D-4) e das aspas vedadas (D-3).")
    w("- **Radar de acervo (D-11):** a gênese da trilogia, os «três ou quatro evangelhos gnósticos» em tradução e o livro "
      "escrito com o próprio Javé ficam declarados com a data da fala — **sem** registro bibliográfico, **sem** peça "
      "fantasma, **sem** ciclo antecipado.")
    w("")
    w("## Quarentenas deste ciclo (rótulo de índice, não de censura de leitura)")
    w("")
    for qq in ["**bloqueio sumário (D-1)**: política nacional — 16.523 caracteres de U0006, com o gancho e a desculpa "
               "preservados; **bloqueio sumário (D-4)**: 237 caracteres de biografia clínica, retida a fórmula de grau "
               "de testemunho",
               "pandemia (retenção seletiva, D-2): a analogia viral entra na malha cósmica; o juízo sobre conduta pública "
               "de saúde estava no bloco bloqueado e não circula",
               "gênero e sexualidade (D-3): transcritos na apostila com nota; **vedados** em ficha de termo que nomeie "
               "grupo humano, por filtro mecânico do gerador do pacote",
               "teológica (retenção): o eu de Javé como podridão organizada, a «confiança zero», a gnose vingativa, a "
               "acusação às religiões como condicionamento oracular — dito, não endossado, não virou estrutura de ficha",
               "cosmológica e de física de borda (retenção): 13,8 bilhões, big crunch, buraco de minhoca, cópia quântica, "
               "entropia = tamas = energia escura, o bóson — nada vira verbete de física nem recomendação",
               "clínico-biológica (retenção): vírus, DNA, oxitocina, genética de servidão, doenças «colecionadas no DNA» — "
               "nenhuma delas é lida como conselho de saúde",
               "ufológica e de hierarquias (retenção): Capela, exilados, famílias Val/Yel/Mion/Cromon, o QG teletransportado "
               "— censos e datas **como ditos**, com endereço",
               "terminológica (veto): «Shanai», «vício oracular», «mente una», «retrogradação espiritual» — "
               "**termos-observação**, sem código novo (D-5, D-6)"]:
        w(f"- {qq}")
    w("")
    w("## Lista das fichas tocadas por esta fonte")
    w("")
    w("- " + " · ".join(cods))

    # ---------------------------------------------------------- APÊNDICE — dicionário STT
    w("")
    w(f"# PARTE III-bis — Apêndice: o dicionário STT desta fonte ({SIGLA})")
    w("")
    w("> Tabela de grafias ouvidas × leitura provável × status, gerada da camada 2 do ciclo. Ela existe porque a "
      "transcrição acima **não** foi corrigida em silêncio: o que o STT ouviu fica como está, e a hipótese de leitura vai "
      "aqui, com o destino decidido pelo Curador (D-5 a D-7). Linhas cujo teor pertence a bloco **bloqueado** são retidas "
      "aqui também: aparece o número, não o conteúdo.")
    w("")
    c2 = open(os.path.join(AQUI, "camada-2.txt"), encoding="utf-8").read()
    tabela2 = c2.split("## 2.")[1].split("## 3.")[0]
    VEDADOS = ["governo", "eleitor", "Vaticano", "Congresso", "mulher", "deficiente", "deep state", "Israel",
               "palestina", "Gaza", "orçamento", "Sarnei", "Sarney", "Bolsonar", "Dilma", "Temer", "FHC", "Lula",
               "impeachment", "mandato", "Polícia Federal", "inflação", "cidadania"]
    retidas = nlin = 0
    for l in tabela2.split("\n"):
        s = l.strip()
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= set("-: ") or re.match(r"^\|\s*o que o STT", s, re.I):
            continue
        cel = [re.sub(r"\*\*", "", c).strip() for c in s.strip("|").split("|")]
        if len(cel) < 3:
            continue
        if any(v.lower() in s.lower() for v in VEDADOS):
            retidas += 1
            continue
        nlin += 1
        txt = f"- **{cel[0]}** → {cel[1]} · {cel[2]}"
        w(txt.replace("\u201c", "«").replace("\u201d", "»"))
    w("")
    w(f"*Nota editorial:* {nlin} linhas emitidas e **{retidas} retidas** por incidirem em bloco bloqueado (D-1). As "
      "contagens de ocorrências citadas em cada linha são as medidas na camada 2 sobre o `original.txt` — não sobre esta "
      "apostila. Termos-observação aprovados sem código (D-5, D-6): "
      "**Shanai** (3 variações medidas: «velo Shanai», «Chanai», «Shanai»; etimologia declarada pela fonte — Chan + Vol + "
      "Yel), **vício oracular**, **mente una**, **retrogradação espiritual**.")

    # ---------------------------------------------------------- GLOSSÁRIO
    w("")
    w("## GLOSSÁRIO LOCAL")
    w("")
    w("A — Personagens e seres")
    for item in [
        "Javé — RC-001; o eu **datado** em «mês de abril do ano 2020», ligado e fissurado nos humanos; corpo montado de vírus que nunca viraram célula.",
        "Lúcifer / Yel Luzbel — RC-078 e RC-142; na fonte, «I Luzbell», «Luisber», «Luzbel» e «a rebelião de Lúcia» [REVISAR: STT]. A fala **não** narra a queda: registra o impasse.",
        "Sofia — RC-009; a rainha que não quis ser rainha, e que em 2018 decide criar uma nova família em Alto Langron.",
        "Processador Val — RC-089 (sem arquivo; vínculo na malha); o elo exclusivo entre cada espécie biodêmica e o cérebro de Sofia. O humano **não** tem um.",
        "Família Val — RC-109 (sem arquivo); 736 membros e o motivo de ter parado de crescer. Família Yel — RC-136/RC-442; Mion/Cromon/Shanlung — RC-443/RC-444/RC-491.",
        "Biodemos — RC-036; engendrados em casulos, assexuados por família, há ~900 milhões de anos. 15 formas grafadas no bruto.",
        "Demos — RC-049; a mente demo ancestral como o ruído que os biodemos foram criados para amortecer.",
        "Anjos — RC-020 (**materializada neste ciclo**); informantes e rastreadores, sem processador próprio: o mecanismo dos que ficaram.",
        "Pandora — RC-086; o **primeiro susto** de Javé, não o castigo. O bloco dos deuses gregos: RC-283/RC-285/RC-287/RC-291.",
        "Exilados de Capela — RC-007; a transmigração contada em 1.641 → 936 → «900Q» (três números, três endereços).",
        "Alt'Lam — RC-017/RC-018 (sem arquivo); a cidadela em `Alto Langron`/`Alto Landrão`, grafias **vetadas** como canônicas.",
        "Len Mion / «Lemion» — RC-074; «ainda não foram exilados»: divergência datada em relação às fichas de exilados.",
        "Jesus — RC-072; a recusa do poder lida como produto da genética inserida; e a guerra declarada por Javé contra ele.",
        "Criatura Universal — RC-042; a «última espécie do universo», com o «Drama Terreno de Javé» e o período cármico.",
        "Anjos caídos — RC-020; ver acima: é a única materialização do ciclo.",
    ]:
        w(f"- {item}")
    w("")
    w("B — Conceitos e teses")
    for item in [
        "Abismo recíproco — a tese-mãe: não é Javé que olha para o abismo, **somos nós** que o somos para ele (RC-369/RC-371, RC-422).",
        "Rebelião como infecção — RC-002; «um coronavírus da época»: a quebra do elo é viral, não gnóstica (D-2 retida).",
        "Processador por espécie — RC-089/RC-446; ligado ao cérebro de Sofia, não a indivíduos.",
        "Campo mórfico como análogo humano do processador — RC-381; ⭐ 3,5 anos antes da fonte oral anterior.",
        "Big Data cósmico — RC-194; os anjos informam Javé quando aparece DNA novo: a gênese do mecanismo de aferição.",
        "Fatiamento de consciência — RC-604; «o assunto mais sério», ligado ao erro de «para Bragina» [REVISAR].",
        "Tamas = entropia = energia escura — RC-160; o selo de que a criação não deveria ter sido começada.",
        "Vício oracular — termo-observação (D-6); origem da oração e da religião como dependência do anúncio.",
        "Mente una — termo-observação; o que Capila «foi o primeiro a falar», conhecimento abortado (RC-188).",
        "Retrogradação espiritual — termo-observação; por que a nova família **não** recebe espíritos humanos (RC-056/RC-074).",
        "Mentalma e o 8º módulo — RC-166/RC-555; a intercomunicação não local **não ministrada** («só vou dar cinco, talvez seis»).",
        "Os dois cenários do futuro eu — estagiar numa «inteligência artificial autônoma controlada» × ir direto para a nova família; definição em 18.000 anos (D-10: prazo dito, não canônico).",
        "Especiação — RC-056; radiata → bilatério como decisão cósmica, 540 milhões de anos (RC-631/RC-093/RC-035).",
        "Gunas e o corpo de Javé — RC-713; oxitocina e predisposições como material psíquico (quarentena clínica: não é recomendação).",
        "Shanai — termo-observação **sem código** (D-5); o nome que a fonte confessa ter inventado.",
        "Grau de testemunho — RC-191; «pelo que eu julgo, entre aspas, saber»: a fórmula que a devolutiva mandou reter.",
    ]:
        w(f"- {item}")
    w("")
    w("C — Livros, referências e fontes externas")
    for item in [
        "*Dark* (Netflix) — citada como ilustração do ciclo de 33 anos e do nó da trindade; **nota externa**, 0 obra, 0 termo (D-12).",
        "*The Man in the High Castle* — vem na fala do operador, com o sobrenome degradado («Philip Kadique» [REVISAR]); nota externa.",
        "*Divina Commedia* («Divina Commeia») — chave de leitura confessada pelo autor para o modelo colmeia (RC-176).",
        "Gênese da trilogia *Terra Atlantis* — «anos 96, 97, 98» e o contato de 2002/2003 com «Valeno» [REVISAR]: **radar** de acervo, sem registro bibliográfico (D-11).",
        "Três ou quatro evangelhos gnósticos em tradução e o livro escrito com o próprio Javé — a fonte chama-o «mergulho na escuridão» — produtos **jamais cadastrados**; ficam no radar de fila de livros com a data da fala (D-11).",
        "«A Rebelião dos Elétrons» como 1º de 9–10 livros (RC-378) — anúncio editorial, **não** obra (D-11).",
        "B057 — a única data canônica que esta fala repete (620 mil anos da vinda da família Val): **acordo medido**, registrado como tal.",
        "B031 e as datas do livro (742/687/619 mil; «213 bilhões») — **não** aparecem nesta fala (0 ocorrências): o ciclo não emenda nem substitui.",
    ]:
        w(f"- {item}")
    w("")
    w("D — Grafias, variações e incertezas")
    for item in [
        "Javé em ~30 grafas medidas: `Javé` 60 · `Jahé` 9 · `Jaé` 7 · `Jaavé` 3 · `Jahvel` 2 · `Javel` 2 · "
        "`Javela` 1 · `Jahvelmente` 1 · `Jahu` 1, e o minúsculo `javé` 5×. Nenhuma é canônica: o leitor **não** pode "
        "deduzir a forma-base a partir do TXT — daí este Apêndice.",
        "A família Val sai como `Vol` (16), `vão` (12), `Volta` (2), `Vale` (2), família V (7) e `vó` (3); o processador é "
        "dito `processador V` (7×) [REVISAR] sem conjetura.",
        "`biodemo` com **15 formas** distintas medidas (`biodemo` 19, `biodemos`, `Biodemos`, `biodêmicas`, `biodêmica`, "
        "`biodêmico`, `biodérêmico`, `biodêmos`, `biodma`, `biodos`, `biodeno`, `bioderno`, `biod`…) e **0** da grafia "
        "`biodeemo` que a Base prefere em RC-026: o ciclo registra a oscilação, não a corrige.",
        "Lúcifer: `Luzbel` 2, `Luisber` 1, `I Luzbell`, e a feminização do STT em «a rebelião de Lúcia». **0** de `Lusbel`.",
        "`Shanlung` **0** ocorrências: a fonte grafa `Chamlum` 1, `Chanlum` 1, `Chan` 4 — e o nome da família nova sai em "
        "três formas: `velo Shanai` 1, `Chanai` 1, `Shanai` 2.",
        "`Niets`/`Niet` = Nietzsche (RC-369/RC-371); `Shellrake` = Sheldrake [REVISAR]; `trimurte`/`Triburto` = trimúrti — "
        "[REVISAR] em todos, sem fusão (D-7).",
        "Capila (provável Kapila/Sāṃkhya), Esildo/Exildo/exío (provável Hesíodo), Omério (Homero), para Bragina "
        "(provável Parabrahman), Brama Loka/Buloca, Xum, Gron [REVISAR] — hipóteses documentadas, **nenhuma** aplicada em "
        "silêncio.",
        "`Alto Langron` 3 e `Alto Landrão` 1 para *Alt'Lam*; `Hipergória` 1 para Hiperbórea — o veto gráfico foi "
        "**reconfirmado pela devolutiva**, e nenhuma dessas formas entra como canônica em ficha.",
        "Números degradados ficam como ditos: `13.8 bilhões`, `429.314`, `249.315`, `1641`, `900Q`, `936`, `18.000`, "
        "`620.000`, `64.000`, `100, 99.000`. A divergência com B031/B057 é **selada com a data**, não harmonizada (D-10).",
    ]:
        w(f"- {item}")
    w("")
    w("*Nota editorial final:* a apostila termina com a última linha da fonte e este aparato. O arquivo bruto, as camadas "
      "0–3, o dossiê de pré-curadoria, a devolutiva registrada em `DECISAO-DO-CURADOR.md`, o pacote de ampliações e as 45 "
      "fichas são as referências de auditoria; a apostila não substitui a fonte.")

    open(ALVO, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"apostila.md escrito: {len(out)} linhas · {n} blocos de transcrição · {n_bloqueios} bloqueio(s) aplicado(s)")
    print(f"cobertura: {chars_publicados}/{chars_bruto} caracteres ({100.0*chars_publicados/chars_bruto:.2f}%), com "
          f"{total_cortado} cortados em {n_bloqueios} spans · notas editoriais: {len(emitidas)}/{len(NOTAS)}")
    print("linhas do dicionário STT:", nlin, "· retidas por bloqueio:", retidas)


if __name__ == "__main__":
    main()
