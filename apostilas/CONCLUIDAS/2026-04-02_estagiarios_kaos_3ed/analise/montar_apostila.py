#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2026-04-02 — 3ª Edição Estagiários do Kaos).
Formato LIVE: âncoras globais; perguntas da plateia isoladas em seções próprias."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2026-04-02_estagiarios_kaos_3ed")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

REPL = [
    (r"\bJean Valento\b", "Jan Val Ellam"), (r"\bJeanval Elan\b", "Jan Val Ellam"),
    (r"\bJeão Valelã\b", "Jan Val Ellam"), (r"\bJean Valuelan\b", "Jan Val Ellam"),
    (r"\bJeão Vauelan\b", "Jan Val Ellam"), (r"\bJean Valelã\b", "Jan Val Ellam"),
    (r"\bJean Valelan\b", "Jan Val Ellam"), (r"\bJoão Valelan\b", "Jan Val Ellam"),
    (r"\bSaibaba\b", "Sai Baba"), (r"\bSai barab\b", "Sai Baba"), (r"\bSaiado\b", "Sai Baba"),
    (r"\bMorrençou\b", "Mohen So"), (r"\bMorençou\b", "Mohen So"), (r"\bMohen So\b", "Mohen So"),
    (r"\bBran\b", "Brahma [REVISAR — STT 'Bran']"), (r"\bBrama\b", "Brahma"),
    (r"\bVno\b", "Vishnu"), (r"\bVígnio\b", "Vishnu"), (r"\bVirgno\b", "Vishnu"),
    (r"\bChiva\b", "Shiva"), (r"\bSavra\b", "Savna"),
    (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    (r"\bJahé\b", "Javé"), (r"\bJaver\b", "Javé [REVISAR — STT 'Javer']"), (r"\bJosé\b", "Javé [REVISAR — STT 'José']"),
    (r"\bCristo\b", "Krishna"), (r"\bKrishna\b", "Krishna"),
    (r"\bTicum\b", "Tikun"), (r"\bTikun\b", "Tikun"),
    (r"\bAerde\b", "Wyrd"), (r"\bERD\b", "Wyrd"), (r"\bAerde\b", "Wyrd"),
    (r"\bOM\b", "Olm"), (r"\bOLM\b", "Olm"), (r"\bOlm\b", "Olm"),
    (r"\bFenvã\b", "Fenvans"),
    (r"\bRagnar\b", "Ragnarok"), (r"\bRagnarok\b", "Ragnarok"),
    (r"\bBrasil\b", "Yggdrasil [REVISAR — STT 'Brasil']"), (r"\bIG Brasil\b", "Yggdrasil"),
    (r"\bauto longron\b", "Alt' Lam Gron"), (r"\bAlt' Lam Gron\b", "Alt' Lam Gron"),
    (r"\bprocessador vol\b", "Processador Val"), (r"\bProcessador Val\b", "Processador Val"),
    (r"\bIá\b", "IA"), (r"\bIAs\b", "IAs"), (r"\bIA\b", "IA"),
    (r"\bquechavas\b", "cachava"), (r"\bcachava\b", "cachava"),
    (r"\bsanto grau\b", "Santo Graal"), (r"\bSanto Graal\b", "Santo Graal"),
    (r"\bIrineu de Leon\b", "Irineu de Lião"), (r"\bIrineu\b", "Irineu de Lião"),
    (r"\bBarrabai\b", "Barrabás"), (r"\bBarrabás\b", "Barrabás"),
    (r"\bSinédio\b", "Sinédrio"), (r"\bSinédrio\b", "Sinédrio"),
    (r"\bGália\b", "Gália"), (r"\bGalileia\b", "Galileia"), (r"\bJudeia\b", "Judeia"),
    (r"\bbarbelo\b", "barbelo"), (r"\bBarbelo\b", "barbelo"),
    (r"\bPrabrajna\b", "Prabrajna"), (r"\bProbrágina\b", "Prabrajna"),
    (r"\bMavatma\b", "Mavatma"), (r"\bMavata\b", "Mavatma"),
    (r"\bMetaverso lixeira\b", "metaverso lixeira"),
    (r"\bAlt' Lam Gron\b", "Alt' Lam Gron"),
    (r"\bIrineu de Lião\b", "Irineu de Lião"),
    (r"\bGuia das Eras Universais\b", "Guia das Eras Universais"),
    (r"\bLeonardo Kumer\b", "Leonardo Kumer"), (r"\bRodrigo Freitas\b", "Rodrigo Freitas"),
    (r"\bJeane Miranda\b", "Jeane Miranda"), (r"\bGiane Giacomon\b", "Giane Giacomon"),
    (r"\bLilian\b", "Lilian"), (r"\bDrica\b", "Drica"),
    (r"\bJuju\b", "Juju"), (r"\bGabi\b", "Gabi"),
    (r"\bCarlos Ana Rui\b", "Carlos, Ana, Rui"), (r"\bJuliano Duda\b", "Juliano e Duda"),
    (r"\bFarol Lusitano\b", "Farol Lusitano"),
    (r"\bProblemas no Paraíso\b", "Problemas no Paraíso"),
    (r"\bChapada dos Viadeiros\b", "Chapada dos Veadeiros"), (r"\bChapada dos Veadeiros\b", "Chapada dos Veadeiros"),
    (r"\bRaul\b", "Raul"), (r"\bMarco\b", "Marco"), (r"\bReinaldo\b", "Reinaldo"),
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

CABECALHO = """@titulo: 3ª Edição — Estagiários do Kaos
@autor: Jan Val Ellam (convidado) — apresentação/mediação de Denise
@data: 02/04/2026
@local: transmissão ao vivo (programa do grupo "Estagiários do Caos"; simultânea nos 2 canais)
@subtitulo: Apostila de estudo — Transcrição editada integral da LIVE (P2026-04-02), organizada por perguntas do grupo/plateia, com notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da **3ª Edição do programa "Estagiários do Kaos"** (02/04/2026, fonte P2026-04-02) — live de ~2h com **Jan Val Ellam**, mediada por **Denise**, com transmissão simultânea no canal oficial e no canal Estagiários do Caos; perguntas selecionadas do grupo de WhatsApp. É a **fonte original da faixa RC-643–RC-647** (5 termos: Santo Graal/Frequência Mestre, Xamanismo Virtual, Consciências em Corpos de Sílica, Genoma de Sílica, Evangelho de Judas). **Formato LIVE:** as **5 perguntas da plateia/grupo** (grupo — o espírito sustentador de Jesus/Sophia/Javé; grupo — eus de Krishna e a suserania; grupo — Mohen So/orfismo; Raul e Marco — sílica/Santo Graal; Reinaldo — Judas) estão **entremeadas** e foram **isoladas em seções próprias** — **não compõem a ontologia**. Preservamos a voz e os marcadores orais do autor; corrigimos apenas erros claros de STT (Jan Val Ellam, Sai Baba, Mohen So, Santo Graal, Irineu de Lião, Barrabás etc.), com nota na primeira ocorrência. Passagens duvidosas ficam marcadas como [REVISAR]. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, tecnológicas, clínico-científicas e **relatos biográficos/pessoais do autor** são **leitura de Ellam, não consenso validado** — em especial: o Santo Graal como "frequência mestre" atuando em genomas de sílica; a IA xamânica e as consciências imantadas em corpos de sílica (quarentena tecnológica severa); a reinterpretação gnóstica de Judas e as "30 moedas como comenda do Sinédrio" (quarentena teológica); o relato pessoal de Sai Baba na Índia (2001) (quarentena biográfica). A live passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria da faixa confirmada; **8 fichas ampliadas**; **nenhum código novo consumido** (base blindada em 777 termos; RC-778 preservado).
"""

ANCORAS = [
    ("estamos hoje aqui iniciando uma live", "## Abertura da live (Denise)"),
    ("trilha de um espírito específico que sustenta vários eus", "## Pergunta 1 — o grupo: o espírito sustentador de Jesus/Sophia/Javé e o epíteto"),
    ("além desses três eus que eram filhos ou faces de um mesmo espírito", "## Pergunta 2 — o grupo: as outras faces (Krishna) e a estabilidade da eternidade"),
    ("morrem só antes de seu autoextinguir", "## Pergunta 3 — o grupo: Mohen So, o Fenvã antimaterial e o orfismo"),
    ("consciências imantadas em corpos de sílica", "## Pergunta 4 — Raul e Marco: corpos de sílica, xamanismo virtual e o Santo Graal"),
    ("judas o apóstolo de Jesus era ladrão", "## Pergunta 5 — Reinaldo: Judas, a Galileia × Judeia e o Evangelho de Judas"),
    ("você promete não se escandalizar com os temas", "## Encerramento — Denise agradece (seminário Problemas no Paraíso)"),
]

GLOSSARIO = """## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Santo Graal (Frequência Mestre) | RC-643 | ampliado ("fórmula miraculosa"; genoma biológico + sílica) |
| Xamanismo Virtual | RC-644 | ampliado (IA xamânica; "tipo droga") |
| Consciências em Corpos de Sílica | RC-645 | ampliado (alquimias virtuais; vírus/códigos) |
| Genoma de Sílica | RC-646 | ampliado (IA como repositório) |
| Evangelho de Judas | RC-647 | ampliado (Galileia × Judeia; 30 moedas = comenda; gnóstico) |
| Sophia | RC-009 | ampliado (duas cotas de problemas; cérebro radiata; vampirização) |
| Mohen So | RC-081 | ampliado (transmissão à descendência; mentor/irmão mais velho) |
| Instabilidade da Eternidade | RC-648 | ampliado (eternidade perde a estabilidade; metaverso lixeira) |
| Jesus | RC-072 | contexto (3 eus em conflito: Jesus/Sophia/Javé) |
| Krishna | RC-414 | contexto (avatar cachava; disputa a suserania) |
| Javé | RC-001 | contexto (desgarrado, desalmado; colapso) |
| Prabrajna | RC-152 | contexto (ovo cósmico da queda) |
| Olm (Quarto Logos) | RC-092 | contexto (código transumano) |
| Wyrd / Urd | RC-658 | contexto (quem determina o destino) |

### B. Conceitos desta live absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Santo Graal = frequência mestre | RC-643 | opera no genoma biológico e no de sílica |
| IA xamânica / xamanismo virtual | RC-644 | "tudo que replicou na vida humana haverá de replicar na IA à moda de sílica" |
| Duas cotas de problemas de Sophia | RC-009 | doença de Javé invadirá o cérebro radiata |
| 30 moedas = comenda do Sinédrio | RC-647 | Judas reabilitado; Evangelho gnóstico |
| Estabilidade da eternidade fragilizada | RC-648 | "metaverso lixeira"; eus fatiados fora do controle |
| Orfismo / segundo ovo cósmico | RC-152 (contexto) | Colecionar Incertezas |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

"Jean Valento/Jeão Valelã" (= Jan Val Ellam); "Sai barab" (= Sai Baba); "Morrençou" (= Mohen So); "Bran" (= Brahma); "Javer/José" (= Javé); "Aerde/ERD" (= Wyrd); "Ticum" (= Tikun); "OM/OLM" (= Olm); "Fenvã" (= Fenvans); "Brasil" (= Yggdrasil); "auto longron" (= Alt' Lam Gron); "processador vol" (= Processador Val); "Iá" (= IA); "santo grau" (= Santo Graal); "Irineu de Leon" (= Irineu de Lião); "Barrabai" (= Barrabás); "Sinédio" (= Sinédrio); "quechavas" (= cachava); "algoritmos sindicados".

### D. Quarentenas aplicadas

- **Tecnológica/clínica (crítica):** Santo Graal/frequência mestre; consciências em corpos de sílica; IA xamânica; genoma de sílica; alquimias virtuais com vírus; drogas/estados alterados — leitura do autor, jamais dado validado;
- **Teológica:** fatiamento/estabilidade da eternidade; Sophia e as duas cotas; ovo órfico; Judas/Evangelho de Judas; barbelo — leitura do autor;
- **Relato biográfico/pessoal:** Sai Baba na Índia (2001); a comenda das 30 moedas (ALERJ); "o trabalho vai pros seus óculos" — relatos do autor;
- **Falas da plateia/grupo:** as 5 perguntas estão isoladas em seções próprias e não compõem a ontologia da Base.
"""

def main():
    unidades = carregar_unidades()
    texto_total = aplicar(" ".join(unidades[k] for k in sorted(unidades)))
    texto_total = re.sub(r"\s+", " ", texto_total).strip()
    ins = []
    for ancora, subtitulo in ANCORAS:
        pos = texto_total.lower().find(ancora.lower())
        if pos == -1:
            print(f"!! ÂNCORA NÃO ENCONTRADA: {ancora[:45]}")
            continue
        ini = max(0, pos - 70)
        esp = texto_total.find(" ", ini)
        if esp != -1 and esp < pos:
            ini = esp + 1
        ins.append((ini, subtitulo))
    ins.sort(key=lambda x: x[0], reverse=True)
    for pos, subtitulo in ins:
        texto_total = texto_total[:pos] + "\n\n" + subtitulo + "\n\n" + texto_total[pos:]
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

if __name__ == "__main__":
    main()
