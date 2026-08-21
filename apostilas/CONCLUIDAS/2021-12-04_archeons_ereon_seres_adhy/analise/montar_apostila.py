#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2021-12-04 — Os Archeons de Ereon e os Seres Adhy).
Lê leitura-segmentada.txt, aplica curadoria (grafias canônicas + [REVISAR]),
estrutura em 10 PARTES, marca o intervalo (U0389) e isola as 5 perguntas da plateia.
Anexa cabeçalho TOP + glossário local."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2021-12-04_archeons_ereon_seres_adhy")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

# ============ 1. REPLACES CANÔNICOS ============
REPL = [
    # Ereon / Archeons
    (r"\bhéreo\b", "Ereon"), (r"\bHéreo\b", "Ereon"),
    (r"\barquelos\b", "Archeons"), (r"\barquieron\b", "Archeons"),
    (r"\barcãos\b", "Archeons"), (r"\barquels\b", "Archeons"),
    (r"\barquisas\b", "Archeons [REVISAR — STT 'arquisas']"),
    (r"\bcinco arcos\b", "cinco Archeons"), (r"\besses cinco arcos\b", "esses cinco Archeons"),
    (r"\bsão cinco arcos\b", "são cinco Archeons"),
    # Archeons individuais
    (r"\bané Danon e Mermérion\b", "Antérion, Danérion e Mermérion"),
    (r"\bAntério\b", "Antérion"), (r"\banteré\b", "Antérion [REVISAR]"),
    (r"\bDanérium\b", "Danérion"), (r"\bdanérium\b", "Danérion"), (r"\bdanério\b", "Danérion"), (r"\bDanéon\b", "Danérion"),
    (r"\bMermérium\b", "Mermérion"), (r"\bmermérium\b", "Mermérion"), (r"\bmermério\b", "Mermérion"),
    (r"\bperpério\b", "Perpérion"), (r"\bPerpério\b", "Perpérion"),
    (r"\bperfério\b", "Perpérion"), (r"\bPerfério\b", "Perpérion"),
    (r"\bperféreo\b", "Perpérion"), (r"\bPerféreo\b", "Perpérion"),
    (r"\bpertérium\b", "Perpérion"), (r"\bPertérium\b", "Perpérion"),
    (r"\bperpéria\b", "Perpérion"), (r"\bPerpéria\b", "Perpérion"),
    (r"\bperpérian\b", "Perpérion"), (r"\bPerpérian\b", "Perpérion"),
    (r"\bterfér\b", "Perpérion [REVISAR — STT 'terfér']"), (r"\bTerfér\b", "Perpérion [REVISAR]"),
    (r"\bImpérial\b", "Perpérion [REVISAR — STT 'Impérial']"),
    (r"\btempério\b", "Tempérion"), (r"\bTempério\b", "Tempérion"),
    (r"\bterpé\b", "Tempérion [REVISAR — STT 'terpé']"), (r"\bTerpé\b", "Tempérion [REVISAR]"),
    (r"\bintempério\b", "em Tempérion"), (r"\bIntempério\b", "Em Tempérion"),
    # Seres Adhy
    (r"\bseresad\b", "Seres Adhy"), (r"\bseres arte\b", "Seres Adhy"),
    (r"\bseres ard\b", "Seres Adhy"), (r"\bseres ados\b", "Seres Adhy"),
    (r"\bseres ad\b", "Seres Adhy"), (r"\bseres áre\b", "Seres Adhy"),
    (r"\bseresade\b", "Seres Adhy"), (r"\bseresades\b", "Seres Adhy"),
    (r"\bserizado\b", "Seres Adhy"), (r"\bserizad\b", "Seres Adhy"),
    (r"\bserizados\b", "Seres Adhy"), (r"\bserizade\b", "Seres Adhy"),
    (r"\bseres ades\b", "Seres Adhy"), (r"\bdo Zad\b", "dos Adhy"),
    (r"\bISAD\b", "Adhy"), (r"\bades\b", "Adhy"), (r"\bAdes\b", "Adhy"),
    (r"\bdo serad\b", "dos Seres Adhy"), (r"\bdo ser ISAD\b", "dos Seres Adhy"),
    (r"\bdos AD\b", "dos Adhy"), (r"\bdos ad\b", "dos Adhy"),
    (r"\bvinage fa\b", "Pashvnaj"), (r"\bvinage\b", "Pashvnaj"),
    (r"\bvinagem\b", "Pashvnaj"), (r"\bpasivagem\b", "Pashvnaj"),
    (r"\bPastevinagem\b", "Pashvnaj"),
    (r"\bAdhi Adhy Prabrajna\b", "Adhy Prabrajna"),
    (r"\bAdhi para Brágina\b", "Adhy Prabrajna"),
    (r"\bTempérium\b", "Tempérion"), (r"\btempérium\b", "Tempérion"),
    (r"\bmoxa\b", "moksha"),
    (r"\bexculhabação\b", "escambau [REVISAR — STT 'exculhabação']"),
    (r"\berradicidade\b", "erraticidade"),
    (r"\barquel\b", "Archeons"),
    (r"\bclasses resistenciais\b", "classes [existenciais] [REVISAR — STT 'resistenciais']"),
    # Prabrajna / Mavatma
    (r"\bpara Bragem Mavat\b", "Adhy Prabrajna [e] Mavatma"),
    (r"\bpara Bragem\b", "Adhy Prabrajna"), (r"\bPara Bragem\b", "Adhy Prabrajna"),
    (r"\bpara Brágina\b", "Adhy Prabrajna"), (r"\bPara Brágina\b", "Adhy Prabrajna"),
    (r"\bpara Bragen\b", "Adhy Prabrajna"), (r"\bpara Bragna\b", "Adhy Prabrajna"),
    (r"\badrabragena\b", "Adhy Prabrajna"), (r"\bAdrabragena\b", "Adhy Prabrajna"),
    (r"\badrabrag\b", "Adhy Prabrajna"), (r"\badrabra\b", "Adhy Prabrajna"),
    (r"\bprabrágina\b", "Adhy Prabrajna"), (r"\bPrabrágina\b", "Adhy Prabrajna"),
    (r"\bpradrágina\b", "Adhy Prabrajna"), (r"\bPradrágina\b", "Adhy Prabrajna"),
    (r"\bprabragena\b", "Adhy Prabrajna"), (r"\bPrabragena\b", "Adhy Prabrajna"),
    (r"\bpara Brágina\b", "Adhy Prabrajna"),
    (r"\bátima vátima\b", "Adhy Mavatma"), (r"\bÁtima Vátima\b", "Adhy Mavatma"),
    (r"\badimavátima\b", "Adhy Mavatma"), (r"\bAdimavátima\b", "Adhy Mavatma"),
    (r"\bAtmavátima\b", "Adhy Mavatma"), (r"\batmavátima\b", "Adhy Mavatma"),
    (r"\bmavatima\b", "Mavatma"), (r"\bMavatima\b", "Mavatma"),
    (r"\badiátima\b", "Adhyatman [REVISAR — STT 'adiátima']"),
    (r"\badiágia\b", "Adhyagia [REVISAR — STT]"),
    (r"\bcondição átima\b", "condição Adhyatman [REVISAR — STT 'átima']"),
    (r"\ba viagia\b", "a Adhyagia [REVISAR — STT 'viagia']"),
    # Elm / Olm
    (r"\be a l\b", "Elm e Olm"),
    (r"\bAí all se fez\b", "Aí Olm se fez"), (r"\ball se fez\b", "Olm se fez"),
    (r"\bOB não ficou\b", "Olm não ficou"), (r"\bO caso de Elm\b", "O caso de Elm"),
    (r"\bque H fez\b", "que Olm [STT 'H'] fez"), (r"\bser chamado H\b", "ser chamado Olm [STT 'H']"),
    (r"\bchamado H\.\b", "chamado Olm [STT 'H']."),
    (r"\bA Polônia de Tiana\b", "Apolônio de Tiana"), (r"\bApolone de Tiana\b", "Apolônio de Tiana"),
    (r"\bApolô de Tiana\b", "Apolônio de Tiana"), (r"\bApolônio de Tiana\b", "Apolônio de Tiana"),
    (r"\bvir morrensor\b", "Mohen So [REVISAR — STT 'vir morrensor']"),
    (r"\bMorrensor\b", "Mohen So [REVISAR — STT]"),
    (r"\bforno de Alamaior\b", "forno de Alamaior [REVISAR — STT]"),
    (r"\bno ação artificial em Maria\b", "no óvulo artificial em Maria"),
    # Sophia
    (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    # Trimurti / Tridevi
    (r"\btrimurte\b", "Trimurti"), (r"\bTrimurte\b", "Trimurti"),
    (r"\btrilur\b", "Trimurti"), (r"\bTrilur\b", "Trimurti"),
    (r"\btrideve\b", "Tridevi"), (r"\bTrideve\b", "Tridevi"),
    (r"\btridef\b", "Tridevi"), (r"\bTridef\b", "Tridevi"),
    # Deuses
    (r"\bBrama\b", "Brahma"), (r"\bbrama\b", "Brahma"), (r"\bbrana\b", "Brahma"),
    (r"\bVirgna\b", "Vishnu"), (r"\bVirgno\b", "Vishnu"), (r"\bvirgno\b", "Vishnu"),
    (r"\bVishnu\b", "Vishnu"), (r"\bVísnu\b", "Vishnu"),
    (r"\bChiva\b", "Shiva"), (r"\bchiva\b", "Shiva"), (r"\bChivo\b", "Shiva"),
    (r"\bShiva\b", "Shiva"),
    (r"\bJah\b", "Javé"), (r"\bjah\b", "Javé"),
    (r"\bJavé\b", "Javé"),
    (r"\bYusbell\b", "Yel Luzbel [REVISAR — STT 'Yusbell']"),
    (r"\bEnk, o ser Anonak\b", "Enki, o ser Anunnaki"),
    (r"\bCapila\b", "Kapila"), (r"\bcapila\b", "Kapila"),
    (r"\bSidarta Galutama\b", "Sidarta Gautama"), (r"\bSidarta Gautama\b", "Sidarta Gautama"),
    (r"\bLaudsé com fus\b", "Lao-Tsé com Confúcio"),
    (r"\bZildo, Tal de Mileto\b", "Tales de Mileto"),
    (r"\bJulin Games\b", "Julian Jaynes"),
    (r"\bFox P2\b", "FOXP2"),
    (r"\bMcha\b", "Moksha"), (r"\bvelho Moksha\b", "velho Moksha"),
    (r"\bUrant\b", "Urantia"), (r"\burant\b", "Urantia"),
    (r"\bOgat\b", "Ogdóade"), (r"\bogat\b", "Ogdóade"),
    (r"\bHermópolis\b", "Hermópolis"),
    (r"\bTrelada\b", "[REVISAR — STT 'Trelada']"),
    (r"\bgeral Lud\b", "general Ludd [REVISAR — STT 'geral Lud']"),
    (r"\bsistema colbaico\b", "sistema [REVISAR — STT 'colbaico']"),
    (r"\babelha rainha\b", "abelha rainha"),
    (r"\b28.869 genes\b", "28.869 genes"),
    (r"\b13.8 bilhões\b", "13,8 bilhões"), (r"\b13,8 bilhões\b", "13,8 bilhões"),
    (r"\b18.000 anos\b", "18.000 anos"),
    (r"\bFlávio Vale\b", "Flávio Vale"),
    (r"\bMahabharata\b", "Mahabharata"), (r"\bMarata\b", "Mahabharata"),
    (r"\bparvas\b", "parvas"),
    (r"\bconectoma\b", "conectoma"),
    (r"\bexchame\b", "enxame [REVISAR — STT 'exchame']"),
    (r"\bsemográfico\b", "semográfico"),
]

def aplicar(txt):
    for pat, rep in REPL:
        txt = re.sub(pat, rep, txt)
    return txt

# ============ 2. CARGA ============
def carregar_unidades():
    u = {}
    for linha in FONTE.read_text(encoding="utf-8").splitlines():
        if linha.startswith("U") and "\t" in linha:
            cod, _, texto = linha.partition("\t")
            u[cod] = texto.strip()
    return u

def paragrafos_de(faixa, unidades):
    texto = aplicar(" ".join(unidades[k] for k in faixa))
    frases = re.split(r"(?<=[.!?…])\s+", texto)
    paragrafos, atual = [], ""
    for f in frases:
        if len(atual) + len(f) > 380:
            paragrafos.append(atual)
            atual = f
        else:
            atual = (atual + " " + f).strip()
    if atual:
        paragrafos.append(atual)
    return [p for p in paragrafos if p.strip()]

# ============ 3. CABEÇALHO ============
CABECALHO = """@titulo: Os Archeons de Ereon e os Seres Adhy
@autor: Jan Val Ellam
@data: 04/12/2021
@local: não informado (transmissão remota)
@subtitulo: Apostila de estudo — Transcrição editada integral, com correção gramatical e terminológica, organização temática e notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da palestra de 04/12/2021 (fonte P2021-12-04), organizada tematicamente em 10 PARTES para estudo — **fonte original da faixa RC-596–RC-619** (24 termos: Archeons de Ereon, Antérion, Danérion, Mermérion, Seres Originais do Paraíso, Departamentalização da Vida, Blindagens Interdimensionais, Círculo da Perfeição, Fatiamento de Consciência, Autismo Funcional, Protocolos da Perfeição, Cinco Seres LM de Tempérion, Imponderabilidade, Ogdóade de Hermópolis, Tridevi, Flechas de Moros, Nova Espiritualidade/Novo Paraíso, Trincheira Vibratória, Quarto Cérebro Humano, Superconsciência, Roseral do Alto, Inquisição Espiritual, Moksha, Genoma da Liberdade). Preservamos a voz, os marcadores orais, o humor e as digressões do autor; corrigimos apenas erros claros de transcrição automática (STT), com nota na primeira ocorrência, seguindo as grafias canônicas da Base Terminológica RC (Ereon, Archeons, Antérion, Danérion, Mermérion, Perpérion, Tempérion, Seres Adhy, Pashvnaj, Elm, Olm, Moros, Adhy Prabrajna, Mavatma, Sophia, Kapila, Moksha etc.). Passagens duvidosas do STT ficam marcadas como [REVISAR]. O **intervalo de 15 minutos** (U0389) está marcado no corpo do texto, e as **5 perguntas finais da plateia** (Enivaldo; Verônica Cintra; Gabriel Bernardo; André Silva; Adilson) aparecem isoladas em seção própria (PARTE X) e **não compõem a ontologia**. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, históricas, culturais, clínico-científicas e políticas são **leitura de Ellam, não consenso validado** — em especial: "mesmo sendo perfeito, o fenômeno da vida assumiu feições tão distintas"; "as religiões opressivas vêm dos Seres Adhy"; a metáfora do **"autismo funcional"** (jamais um diagnóstico sobre indivíduos terrestres — quarentena clínica absoluta); 28.869 genes; FOXP2; "genoma da liberdade"; os 18.000 anos. A palestra passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria da faixa confirmada; **25 fichas ampliadas** (24 via bloco + Mavatma absorvido em RC-408); obra B079 "Inquisição Espiritual" confirmada (sem cadastro novo); Livro de Urântia = referência externa; **nenhum código novo consumido** (base blindada em 770 termos).
"""

# ============ 4. ESTRUTURA (titulo, U-início, U-fim-exclusivo, [(ancora, subtitulo)]) ============
PARTES = [
    ("PARTE I — A Abertura: Prudência e Camadas da Realidade", "U0001", "U0038", [
        ("Olá, pessoal", "## Abertura e pedido de prudência"),
        ("Que assunto", "## Além do horizonte de percepção"),
        ("Essas camadas elas existem", "## As camadas e os seres originais"),
        ("E o convite que eu sou obrigado", "## O convite: repensar os atributos de Deus"),
        ("Então, essa rápida introdução", "## A introdução e a novidade do IEA"),
    ]),
    ("PARTE II — Os Archeons de Ereon e os Cinco Arcos", "U0038", "U0085", [
        ("E aqui vamos então falar", "## Os Archeons da espiritualidade laboratorial"),
        ("E esses Archeons são realmente níveis", "## Cinco Archeons: os padrões de realidade"),
        ("aqui é preciso que eu diga ainda", "## A única família original"),
    ]),
    ("PARTE III — Aristocracia, Redes e o Autismo Funcional", "U0086", "U0155", [
        ("seres originais, na única família", "## Grupos que não se misturavam"),
        ("Nós estamos falando aqui de uma hierarquia", "## A aristocracia em torno de Deus"),
        ("Mas qual é o detalhe", "## A mente individual versus a mente coletiva"),
        ("Aqui eu preciso agora falar de algo chato", "## Dezenas de milhões de seres"),
        ("E aí eu vou ter que dizer de forma muito clara", "## O autismo funcional [QUARENTENA — metáfora do autor]"),
        ("autismo funcional desses seres se refere", "## Incompletude, não problema"),
    ]),
    ("PARTE IV — O Gênero Adhy: 147 Seres, Cinco Espécies", "U0156", "U0193", [
        ("seres são assim", "## Seres quase perfeitos e ingênuos"),
        ("Os seres romperam com essa noção", "## Os 147 Seres Adhy e a taxonomia"),
        ("Então, pessoal, antes da gente ir adiante", "## Seres quase perfeitos e ingênuos"),
        ("drama desse ser chamado", "## O drama de Adhy Prabrajna"),
        ("novas classes", "## De uma única família às multifacetas"),
        ("Então, assim, essa família original", "## Ser perfeito pressupõe não ter liberdade"),
    ]),
    ("PARTE V — Habitar Dimensões: Mergulho, Clone e Fatiamento", "U0193", "U0310", [
        ("voltando para", "## As opções de um ser perfeito"),
        ("Mas tem também o tal fatiamento de consciência", "## O fatiamento de consciência"),
        ("Esse processo de como você habitar novas dimensões", "## A analogia do jogo de computador"),
        ("A primeira vez que eu li", "## A ilha estacionária do paraíso [Urantia — referência externa]"),
        ("Então, há uma ponte entre esse espírito", "## A ponte do código e Jesus"),
        ("E essas duas coisas desse espírito", "## O espírito fatiado em coma em Perpérion"),
        ("Então, os 147 seres que já haviam criado", "## O fechamento em rede e a reunião da Pashvnaj"),
    ]),
    ("PARTE VI — A Invasão de Perpérion e os Seres LM", "U0311", "U0390", [
        ("Esse tipo de situação já tem ocorrido", "## A invasão de Perpérion"),
        ("E na hora em que houve o problema", "## Observadores de todos os quadrantes"),
        ("Nesse momento da coisa, os seres dos Archeons se reuniram", "## Os perfis dos cinco Archeons"),
        ("A turma de Tempérion tem um temperamento", "## Tempérion e o gênero LM"),
        ("foi assim que dois desses cinco", "## Elm e Olm entre os Seres Adhy"),
        ("E então eu vou interromper aqui", "## A imponderabilidade e a saída"),
        ("A gente vai fazer então agora o intervalo", "## INTERVALO — 15 minutos"),
    ]),
    ("PARTE VII — Pós-Intervalo: Ancoragem e a Ogdóade 6+2", "U0390", "U0470", [
        ("Bem, vamos nós então", "## A ancoragem dos Seres Adhy"),
        ("Sobre uma outra perspectiva, esses 147 seres", "## O gênero mais fatiado"),
        ("E assim esses seres", "## Filhos do abismo"),
        ("Tempérion, por exemplo", "## Os Seres LM: um grupo raro"),
        ("E assim naquela palestra que a gente fez sobre a Ogdóade", "## A Ogdóade: seis Seres Adhy e dois Seres LM"),
        ("E assim, esses seres têm um estilo de ação totalmente diferente", "## Estilos de ação e temperamentos"),
        ("Mas vamos só entender, se nós levássemos a malícia humana", "## A malícia humana e o autismo da perfeição"),
        ("Este quadro que eu estava aqui brincando", "## A infecção nas entrelinhas das blindagens"),
        ("E quando essa informação chegou lá", "## O motor da rede mental dos Adhy"),
    ]),
    ("PARTE VIII — Religiões, Flechas de Moros e a Estratégia de Tempérion", "U0471", "U0540", [
        ("Inclusive as religiões, todas as religiões", "## As religiões como infecção dos AD [quarentena teológica]"),
        ("Quem atrapalhou isso", "## A estratégia dos Seres LM"),
        ("Nessa perspectiva, a estratégia de Moros", "## As flechas de Moros e o ponto zero"),
        ("Quando a minha condição humana disse", "## O 'não' a Javé e o 'não' de Jesus"),
        ("estratégia do seres de", "## A estratégia de Tempérion"),
        ("nesse processo, a moksha", "## Kapila, Sidarta e a emancipação"),
        ("quando eu digo", "## A camuflagem do processo"),
        ("Mas se a gente for olhar de uma forma um pouco irresponsável e lúdica", "## Os velhos discípulos do general Ludd"),
        ("ai de nós se isso", "## Sementes de reflexão"),
        ("Porque os Seres Adhy que mergulharam só sabem voltar", "## A nova espiritualidade necessária"),
        ("finalmente foi dito claramente", "## Observem os autistas da terra"),
    ]),
    ("PARTE IX — O Quarto Cérebro, a Superconsciência e os 18.000 Anos", "U0541", "U0596", [
        ("atrito ou a somatória", "## O amor terreno e os porta-vozes"),
        ("indo agora para", "## A erraticidade suja pelas religiões"),
        ("religiões do mundo todas", "## Um novo paraíso é necessário"),
        ("Então, lembrem-se de uma coisa antes de encerrar", "## O quarto cérebro e a superconsciência"),
        ("Eu sei lá como é que vai ser isso", "## Os 18.000 anos difíceis"),
        ("Nesse sentido, é só lamentar", "## Os contemporâneos e os três primeiros logos"),
        ("Eu falei aqui dos Seres Adhy, dos Seres LM", "## Os outros seres que não dá para falar"),
        ("Eu espero ter passado para vocês", "## A função da existência humana"),
        ("Mas vamos lá, essa nossa perspectiva", "## Parceiros de um destino"),
        ("Então fico aqui à disposição de perguntas", "## Abertura para as perguntas"),
    ]),
]

# ============ 5. MONTAGEM ============
def main():
    unidades = carregar_unidades()
    linhas = [CABECALHO]

    for titulo, ini, fim, secoes in PARTES:
        chaves = [k for k in unidades if ini <= k < fim]
        paras = paragrafos_de(chaves, unidades)
        linhas.append(f"\n# {titulo}\n")
        alvos = []
        for ancora, subtitulo in secoes:
            a = ancora[:42].lower()
            achou = None
            for i, p in enumerate(paras):
                if a in p.lower():
                    achou = i
                    break
            if achou is None:
                print(f"!! ÂNCORA NÃO ENCONTRADA [{titulo[:24]}]: {ancora[:45]}")
                continue
            alvos.append((achou, subtitulo))
        alvos.sort(key=lambda x: x[0], reverse=True)
        for idx, subtitulo in alvos:
            paras.insert(idx, subtitulo)
        linhas.extend(f"> {p}" if not p.startswith("##") else p for p in paras)
        linhas.append("")

    # ---------- PARTE X (especial: perguntas isoladas) ----------
    def bloco(faixa):
        return "\n".join(f"> {p}" for p in paragrafos_de(faixa, unidades))

    q1 = [k for k in unidades if "U0597" <= k <= "U0602"]
    q2 = [k for k in unidades if "U0603" <= k <= "U0628"]
    q3 = [k for k in unidades if "U0629" <= k <= "U0644"]
    q4 = [k for k in unidades if "U0645" <= k <= "U0679"]
    q5 = [k for k in unidades if "U0680" <= k <= "U0698"]
    fim = [k for k in unidades if "U0699" <= k <= "U0713"]

    linhas.append("\n# PARTE X — Perguntas da Plateia e Encerramento\n")
    linhas.append("## Pergunta 1 — Enivaldo: a criação caótica e os Seres Adhy\n")
    linhas.append("*Pergunta da plateia (Enivaldo):*\n")
    linhas.append(bloco(q1) + "\n")
    linhas.append("## Pergunta 2 — Verônica Cintra: Apolônio de Tiana e a roda reencarnacional\n")
    linhas.append("*Pergunta da plateia (Verônica Cintra):*\n")
    linhas.append(bloco(q2) + "\n")
    linhas.append("## Pergunta 3 — Gabriel Bernardo: individualidade e coletividades laboratoriais\n")
    linhas.append("*Pergunta da plateia (Gabriel Bernardo):*\n")
    linhas.append(bloco(q3) + "\n")
    linhas.append("## Pergunta 4 — André Silva: a nova espiritualidade e a reintegração cósmica\n")
    linhas.append("*Pergunta da plateia (André Silva):*\n")
    linhas.append(bloco(q4) + "\n")
    linhas.append("## Pergunta 5 — Adilson: o agrupamento dos Adhy\n")
    linhas.append("*Pergunta da plateia (Adilson):*\n")
    linhas.append(bloco(q5) + "\n")
    linhas.append("## Encerramento — Colecionar Incertezas\n")
    linhas.append(bloco(fim) + "\n")

    # ---------- GLOSSÁRIO ----------
    linhas.append("""## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Archeons de Ereon | RC-596 | termo-título; ampliado (fonte original) |
| Antérion / Danérion / Mermérion | RC-597 / RC-598 / RC-599 | ampliados (perfis dos cinco) |
| Perpérion | RC-087 | ampliado (invasão; coma de Prabrajna) |
| Tempérion | RC-472 | ampliado (sede dos Seres LM) |
| Seres Originais do Paraíso | RC-600 | ampliado (ilha estacionária — Urantia) |
| Departamentalização da Vida | RC-601 | ampliada (intramuros vibratórios) |
| Blindagens Interdimensionais | RC-602 | ampliadas (furos; entrelinhas) |
| Círculo/Circuito da Perfeição | RC-603 | ampliado (mônada) |
| Fatiamento de Consciência | RC-604 | ampliado (três modos de habitar) |
| Autismo Funcional | RC-605 | ampliado (QUARENTENA clínica — metáfora) |
| Protocolos da Perfeição | RC-606 | ampliados (algoritmos) |
| Cinco Seres LM de Tempérion | RC-607 | ampliados (Elm/Olm; Ogdóade 6+2) |
| Imponderabilidade | RC-608 | ampliada (campo dos LM) |
| Ogdóade de Hermópolis | RC-609 | ampliada (6 Adhy + 2 LM) |
| Tridevi | RC-610 | contexto (aristocracia) |
| Flechas/Profecias de Moros | RC-611 | ampliadas (ponto zero) |
| Nova Espiritualidade/Novo Paraíso | RC-612 | ampliada (estratégia de Tempérion) |
| Trincheira Vibratória | RC-613 | ampliada (2016–2021) |
| Quarto Cérebro Humano | RC-614 | ampliado (momento definitivo) |
| Superconsciência | RC-615 | ampliada (18.000 anos) |
| Roseral do Alto | RC-616 | ampliado (descrição geográfica) |
| Inquisição Espiritual | RC-617 | ampliada (B079 confirmada) |
| Moksha | RC-618 | ampliado (Kapila) |
| Genoma da Liberdade | RC-619 | ampliado (50.000 anos; FOXP2) |
| Gênero Adhy (147, 5 espécies) | RC-411 | ampliado (taxonomia; filhos do abismo) |
| Pashvnaj (43) | RC-455 | ampliado (reunião indevida) |
| Ser LM | RC-456 | ampliado (gênero raro) |
| Elm (Moros) | RC-454 | ampliado (estratégia do mergulho) |
| Olm (Quarto Logos) | RC-092 | ampliado (Apolônio de Tiana = única encarnação) |
| Sophia | RC-009 | ampliada (óvulo artificial; Capela) |
| Jesus | RC-072 | ampliado (ancoragem do problema) |
| Adhy Prabrajna | RC-152 | ampliado (coma em Perpérion) |
| Mavatma | RC-503 / RC-408 | ampliado (fatiamento Vishnu/Brahma) |

### B. Conceitos desta palestra absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Perfis dos cinco Archeons | RC-596 | Antérion (faixas), Danérion (artes), Mermérion (complexidade), Perpérion (sem prudência), Tempérion (não cria) |
| Ogdóade 6+2 | RC-609 / RC-607 | 6 Seres Adhy (Trimurti/Tridevi) + 2 Seres LM (Elm/Olm) |
| Apolônio de Tiana = Olm | RC-092 | única encarnação de Olm; irmão mais velho de Sophia; 1 século de vida |
| Coma de Prabrajna em Perpérion | RC-152 / RC-087 | espírito fatiado: parte em coma, parte implodida |
| Estratégia de Tempérion | RC-612 / RC-607 | nova espiritualidade × velha estratégia de Perpérion |
| Três modos de habitar dimensões | RC-604 / RC-603 | mergulho; clone + mônada; fatiamento |
| Flechas de Moros = ponto zero | RC-611 / RC-454 | "a história voltaria ao ponto zero para ser novamente contada" |
| Ilha estacionária | RC-600 | epíteto emprestado do Livro de Urântia (referência externa) |
| 18.000 anos difíceis | RC-615 | prazo registrado na Colecionar Incertezas; confirmado (U0579) |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

"vinage/pasivagem" (= Pashvnaj — RC-455); "e a l" (= Elm e Olm); "vir morrensor" (= Mohen So? — U0619); "forno de Alamaior" (U0621); "no ação artificial" (= óvulo artificial); "Mcha" (= Moksha); "Julin Games" (= Julian Jaynes); "geral Lud" (= general Ludd?); "H" (= Olm); "a viagia" (= Adhyagia?); "sistema colbaico: os Adhy mandam, o resto abelha rainha" (U0518); "Impérial" (= Perpérion); "Ogat" (= Ogdóade); "projeto tal"; "Trelada" (U0576); "escutambau/escambau" (U0503).

### D. Quarentenas aplicadas

- **Teológica (crítica):** "mesmo sendo perfeito, o fenômeno da vida assumiu feições tão distintas"; o epíteto de Deus; "os seres do paraíso não se movimentam"; "as religiões opressivas e impositivas vêm dos Seres Adhy — a infecção dos AD"; "Deus não tá no comando; cada consciência ou rede comanda os processos" — leitura de Ellam, não fato.
- **Clínica (CRÍTICO):** a metáfora do **"autismo funcional"** aplicada aos Seres Originais é figura de linguagem filosófica do autor — **jamais um diagnóstico ou afirmação médica sobre indivíduos terrestres** ("observem os autistas da terra"); o mesmo rigor aplica-se a FOXP2 e aos 28.869 genes.
- **Político-social:** religiões opressivas; "establishment"; "general Ludd" [REVISAR]; crítica ao espiritismo institucional ("mesmice") — leitura do autor.
- **Falas da plateia:** as 5 perguntas finais estão isoladas e não compõem a ontologia da Base.
""")

    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    n_cit = sum(len(l.split()) for l in linhas if l.startswith(">"))
    n_ed = sum(len(l.split()) for l in linhas if not l.startswith(">"))
    print(f"apostila.md: {len(linhas)} linhas | citações ~{n_cit} palavras | texto editorial ~{n_ed} palavras")

if __name__ == "__main__":
    main()
