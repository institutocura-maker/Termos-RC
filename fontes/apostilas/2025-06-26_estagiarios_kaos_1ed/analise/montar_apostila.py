#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2025-06-26 — 1ª Edição Estagiários do Kaos).
Formato LIVE: âncoras globais; perguntas da plateia isoladas em seções próprias."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2025-06-26_estagiarios_kaos_1ed")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

REPL = [
    (r"\bJean Valelan\b", "Jan Val Ellam"), (r"\bJeão Valelan\b", "Jan Val Ellam"),
    (r"\bJoão Vauelão\b", "Jan Val Ellam"), (r"\bJan Valelan\b", "Jan Val Ellam"),
    (r"\bJoão Vauelan\b", "Jan Val Ellam"), (r"\bJan Vauelan\b", "Jan Val Ellam"),
    (r"\bMorrençó\b", "Mohen So"), (r"\bMorenço\b", "Mohen So"), (r"\bMorrensor\b", "Mohen So"),
    (r"\bMorrençou\b", "Mohen So"), (r"\bMorrençor\b", "Mohen So"), (r"\bMorençor\b", "Mohen So"),
    (r"\bERD\b", "Wyrd"), (r"\bWerd\b", "Wyrd"), (r"\bUrdre\b", "Urd"), (r"\bUer\b", "Wyrd"),
    (r"\bERDE\b", "Wyrd"), (r"\baerde\b", "a Wyrd"),
    (r"\bCadru\b", "Kadru"), (r"\bMaroharagas\b", "Maharagas"),
    (r"\bOrumilá\b", "Orunmilá"), (r"\bOrumi\b", "Orunmilá"), (r"\bOrum Milá\b", "Orunmilá"),
    (r"\bSaibaba\b", "Sai Baba"),
    (r"\bIG Brasil\b", "Yggdrasil"), (r"\bEmdrazi\b", "Yggdrasil"),
    (r"\bAura Catena\b", "Áurea Catena"), (r"\bAurecatena\b", "Áurea Catena"), (r"\baureacatena\b", "Áurea Catena"),
    (r"\btirtancaras\b", "Tirthankaras"),
    (r"\bprima sai\b", "Prema Sai [REVISAR — STT 'prima sai']"),
    (r"\bGand\b", "Gandhi"), (r"\bJohn Lemon\b", "John Lennon"),
    (r"\bRecate\b", "Hécate"), (r"\bEcat\b", "Hécate"), (r"\bEcate\b", "Hécate"),
    (r"\bBrama\b", "Brahma"), (r"\bbrama\b", "Brahma"), (r"\bVirgno\b", "Vishnu"), (r"\bVígno\b", "Vishnu"),
    (r"\bChiva\b", "Shiva"), (r"\bchiva\b", "Shiva"), (r"\bChiv\b", "Shiva"),
    (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    (r"\bJahé\b", "Javé"), (r"\bJosé\b", "Javé [REVISAR — STT 'José']"), (r"\bJahvel\b", "Javé [REVISAR]"),
    (r"\bCristo\b", "Krishna"), (r"\bCrista\b", "Krishna"),
    (r"\bTrimurte\b", "Trimurti"),
    (r"\bPrabragána\b", "Prabrajna"), (r"\bPrabragena\b", "Prabrajna"), (r"\bpara Bragna\b", "Prabrajna"),
    (r"\bSávna\b", "Savna"),
    (r"\bZamo\b", "Zian [REVISAR — STT 'Zamo']"),
    (r"\bFenvães\b", "Fenvans"), (r"\bfenvães\b", "fenvans"),
    (r"\bTânatos\b", "Tânatos"), (r"\bHípos\b", "Hipnos"),
    (r"\bÉrebo\b", "Érebo"), (r"\bNix\b", "Nix"),
    (r"\bMorfia\b", "Morphia [REVISAR — STT 'Morfia']"),
    (r"\babaiã\b", "abaiã [REVISAR — STT; provável 'aparigraha']"),
    (r"\bOrum\b", "Orum"), (r"\bIrém\b", "Irém"), (r"\bIron\b", "Iron"),
    (r"\bOdis\b", "Odus"), (r"\bOdus\b", "Odus"),
    (r"\bifismo\b", "ifismo"), (r"\bIfá\b", "Ifá"), (r"\bIFA\b", "Ifá"),
    (r"\bMentalma\b", "Mentalma"),
    (r"\bTerra Atlantes\b", "Terra Atlantis"), (r"\bTerra Atlantis\b", "Terra Atlantis"),
    (r"\bSinal de Landzen\b", "O Sinal de Landzen"),
    (r"\bDrosn\b", "Michael Drosnin [REVISAR — STT 'Drosn']"),
    (r"\bSatinov\b", "Jeffrey Satinover [REVISAR — STT 'Satinov']"),
    (r"\bCibell\b", "Cibell [REVISAR — nome da perguntadora]"),
]

def aplicar(txt):
    for pat, rep in REPL:
        txt = re.sub(pat, rep, txt)
    return txt

def carregar_unidades():
    u = {}
    for linha in FONTE.read_text(encoding="utf-8").splitlines():
        if linha.startswith("U") and "\t" in linha:
            cod, _, texto = linha.partition("\t")
            u[cod] = texto.strip()
    return u

CABECALHO = """@titulo: 1ª Edição — Estagiários do Kaos
@autor: Jan Val Ellam (convidado) — apresentação/mediação de Denise
@data: 26/06/2025
@local: transmissão ao vivo (programa do grupo "Estagiários do Caos")
@subtitulo: Apostila de estudo — Transcrição editada integral da LIVE (P2025-06-26), organizada por perguntas do grupo/plateia, com notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da **1ª Edição do programa "Estagiários do Kaos"** (26/06/2025, fonte P2025-06-26) — live de ~2h com **Jan Val Ellam**, mediada por **Denise**, com perguntas selecionadas do grupo de WhatsApp "RC LAN Estagiários do Caos" (+430 pessoas). É a **fonte original da faixa RC-658–RC-666** (9 termos: Wyrd/Urd, Quirino Cornélio, Pegadinha de Javé, Seres Desalmados, Agenda do Desespero, Áurea Catena, Descendência de Kadru, Orunmilá, Obatalá). **Formato LIVE:** as **10 perguntas da plateia/grupo** (Simone Piemonte e Tânia; Cibell; João Maia; Adilson; grupo; Denise; Renata Prado) estão **entremeadas** no fluxo e foram **isoladas em seções próprias** — **não compõem a ontologia**. Preservamos a voz e os marcadores orais do autor; corrigimos apenas erros claros de STT (Jan Val Ellam, Mohen So, Wyrd/Urd, Orunmilá, Obatalá, Kadru, Yggdrasil etc.), com nota na primeira ocorrência. Passagens duvidosas ficam marcadas como [REVISAR]. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, políticas, clínico-psicológicas e **relatos biográficos/pessoais do autor** (o espírito que o anima ter sido o centurião; a "quarta cabeça" de Mohen So passando arquivos) são **leitura de Ellam, não consenso validado** — em especial: o Great Reset/bilionários/criptomoedas (quarentena política); o desmonte da "justiça divina" (quarentena teológica); a "mochila vibracional"/"programa quântico do eu" (quarentena clínica). A live passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria da faixa confirmada; **10 fichas ampliadas**; **nenhum código novo consumido** (base blindada em 777 termos; RC-778 preservado).
"""


def main():
    unidades = carregar_unidades()
    texto_total = aplicar(" ".join(unidades[k] for k in sorted(unidades)))
    # normaliza espaços
    texto_total = re.sub(r"\s+", " ", texto_total).strip()

    ANCORAS = [
        ("estamos ao vivo", "## Abertura da live (Denise)"),
        ("existem outros seres desalmados", "## Pergunta 1 — Simone Piemonte e Tânia: os seres desalmados"),
        ("great reset", "## Pergunta 2 — Cibell: o Great Reset e a grande reinicialização"),
        ("espírito que me anima na época de Jesus ter sido centurião", "## O relato do centurião (Quirino Cornélio)"),
        ("messias pela espada", "## Pergunta 3 — João Maia: a crucificação e a pegadinha de Javé"),
        ("mensagem talm", "## Pergunta 4 — Denise/Adilson: a Mensagem Talm e os fornos"),
        ("quarta cabeça", "## Pergunta 5 — o grupo: a quarta cabeça de Mohen So"),
        ("descendente de uma ainda desconhecida linhagem", "## Pergunta 6 — Denise: Odin, o fatiamento e a Áurea Catena"),
        ("boi de piranhas", "## Pergunta 7 — Adilson: Prabrajna e a contaminação"),
        ("mochila vibracional", "## Pergunta 8 — o grupo: a Wyrd e a mochila vibracional"),
        ("engenharia reversa", "## Pergunta 9 — Renata Prado: engenharia reversa e a indignação"),
        ("orunmilá era moros", "## Orunmilá = Moros de Irém e Obatalá = Javé caído"),
        ("não considero os livros", "## Pergunta 10 — Denise: o legado do autor"),
        ("tocha de Hécate", "## Encerramento: a tocha de Hécate e a luz própria"),
    ]
    # insere headings por posição de caractere (decrescente)
    ins = []
    for ancora, subtitulo in ANCORAS:
        pos = texto_total.lower().find(ancora.lower())
        if pos == -1:
            print(f"!! ÂNCORA NÃO ENCONTRADA: {ancora[:45]}")
            continue
        # recua no máximo 70 chars até um espaço (não há pontuação no STT)
        ini = max(0, pos - 70)
        esp = texto_total.find(" ", ini)
        if esp != -1 and esp < pos:
            ini = esp + 1
        ins.append((ini, subtitulo))
    ins.sort(key=lambda x: x[0], reverse=True)
    for pos, subtitulo in ins:
        texto_total = texto_total[:pos] + "\n\n" + subtitulo + "\n\n" + texto_total[pos:]

    # quebra em parágrafos de citação
    partes = texto_total.split("\n\n")
    linhas = [CABECALHO]
    for pp in partes:
        pp = pp.strip()
        if not pp:
            continue
        if pp.startswith("## "):
            linhas.append(pp)
        else:
            linhas.append(f"> {pp}")
    linhas.append("")
    linhas.append(GLOSSARIO)
    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    n_cit = sum(len(l.split()) for l in linhas if l.startswith(">"))
    n_ed = sum(len(l.split()) for l in linhas if not l.startswith(">"))
    print(f"apostila.md: {len(linhas)} linhas | citações ~{n_cit} | editorial ~{n_ed}")

GLOSSARIO = """## GLOSSÁRIO LOCAL
"""

if __name__ == "__main__":
    main()
