#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2026-07-30 — 4ª Edição Estagiários do Kaos).
Formato LIVE: âncoras globais; perguntas da plateia isoladas em seções próprias."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2026-07-30_estagiarios_kaos_4ed")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

REPL = [
    (r"\bJeão Valelão\b", "Jan Val Ellam"), (r"\bJean Valuelan\b", "Jan Val Ellam"),
    (r"\bJeão Val Elan\b", "Jan Val Ellam"), (r"\bJeanva Elan\b", "Jan Val Ellam"),
    (r"\bJoão Valelão\b", "Jan Val Ellam"), (r"\bJean Valuelão\b", "Jan Val Ellam"),
    (r"\bJan Valelan\b", "Jan Val Ellam"), (r"\bJean Valelan\b", "Jan Val Ellam"),
    (r"\bOgod\b", "Ogdóade"), (r"\bOgat\b", "Ogdóade"), (r"\bAugdod\b", "Ogdóade"),
    (r"\bTênit\b", "TÊNET"), (r"\bTÊNET\b", "TÊNET"), (r"\bTênet\b", "TÊNET"),
    (r"\bEmá\b", "En Ma"), (r"\bEMÁ\b", "En Ma"), (r"\bEmar\b", "En Ma [REVISAR — STT 'Emar']"),
    (r"\bEn Ma\b", "En Ma"),
    (r"\bVisno\b", "Vishnu"), (r"\bVígena\b", "Vishnu"), (r"\bVirgno\b", "Vishnu"),
    (r"\bLaxme\b", "Lakshmi"), (r"\bDilaxme\b", "Lakshmi"),
    (r"\bPrabrag\b", "Prabrajna"), (r"\bPrabragen\b", "Prabrajna"), (r"\bPrabrajna\b", "Prabrajna"),
    (r"\bmetator\b", "Metatron"), (r"\bMetatron\b", "Metatron"),
    (r"\bSávna\b", "Savna"), (r"\bEnsara\b", "Ensá [REVISAR — STT 'Ensara']"), (r"\bEnsá\b", "Ensá"),
    (r"\bórbum\b", "Orbum"), (r"\bOrbum\b", "Orbum"),
    (r"\bBrama\b", "Brahma"), (r"\bJahé\b", "Javé"), (r"\bJaver\b", "Javé [REVISAR — STT 'Javer']"),
    (r"\bChiva\b", "Shiva"), (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    (r"\bCristo\b", "Krishna"), (r"\bTrimurte\b", "Trimurti"),
    (r"\bexculhambação\b", "exculhambação [REVISAR — STT]"),
    (r"\baséase\b", "ascese [REVISAR — STT 'aséase']"),
    (r"\bfóssil\b", "fósforo [REVISAR — STT 'fóssil']"),
    (r"\bAdhy Shakti\b", "Adhy Shakti [REVISAR — STT]"),
    (r"\bGé\b", "Giane [REVISAR — STT 'Gé']"),
    (r"\bGiane Miranda\b", "Giane Miranda"), (r"\bGiane Giacomon\b", "Giane Giacomon"),
    (r"\bGiane decom\b", "Giane Giacomon"), (r"\bdupla GG\b", "dupla GG"),
    (r"\bCristal Plaza\b", "Cristal Plaza"), (r"\bHermópolis\b", "Hermópolis"),
    (r"\bRodrigo\b", "Rodrigo"), (r"\bMartina\b", "Martina"),
    (r"\bJuju\b", "Juju"), (r"\bKardec\b", "Kardec"), (r"\bperespírito\b", "perispírito"),
    (r"\bPão de Açúcar\b", "Pão de Açúcar"), (r"\bbondinho\b", "bondinho"),
    (r"\bcaos 2.0\b", "caos 2.0"), (r"\buniverso B\b", "universo B"),
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

CABECALHO = """@titulo: 4ª Edição — Estagiários do Kaos (Perguntas e Reflexões)
@autor: Jan Val Ellam (convidado) — apresentação/mediação de Denise Ferreira da Silva
@data: 30/07/2026
@local: transmissão ao vivo (programa do grupo "Estagiários do Caos")
@subtitulo: Apostila de estudo — Transcrição editada integral da LIVE (P2026-07-30), organizada por perguntas do grupo/plateia, com notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da **4ª e última Edição do programa "Estagiários do Kaos"** (30/07/2026, fonte P2026-07-30) — live de ~1h30 com **Jan Val Ellam** (que se desculpa por estar "um pouco rouco"), mediada por **Denise Ferreira da Silva**, com perguntas selecionadas do grupo de WhatsApp "Estagiários do Caos" (12 selecionadas, 5 respondidas). É a **fonte original da faixa RC-620–RC-627** (8 termos: Eu Coalescente, Nyx, Kama, Corpo Átmico, Corpo Búdico, Corpo Manásico, Universo TÊNET, Enéade de Heliópolis) + **RC-476 (En Ma)** + **RC-475 (Deva/Aurora)**. **Formato LIVE:** as **5 perguntas da plateia/grupo** (grupo — Ogdóade/Goiânia; grupo — Tridevi/Deva/Aurora; grupo — ímpeto criativo; grupo — En Ma/Eu Coalescente; grupo — dignificação) estão **entremeadas** e foram **isoladas em seções próprias** — **não compõem a ontologia**. Preservamos a voz e os marcadores orais do autor; corrigimos apenas erros claros de STT (Jan Val Ellam, Ogdóade, TÊNET, En Ma, Lakshmi, Metatron etc.), com nota na primeira ocorrência. Passagens duvidosas ficam marcadas como [REVISAR]. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, clínico-psicológicas e **relatos biográficos/pessoais do autor** são **leitura de Ellam, não consenso validado** — em especial: o "segredo de estado" sobre En Ma; a vulnerabilidade de Sophia; a agressão a Sophia no início da Covid; o "caos 2.0" (quarentenas biográfica e teológica estritas); o "buraco negro mental" e a ascese (quarentena clínico-psicológica). A live passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria confirmada; **9 fichas ampliadas**; **nenhum código novo consumido** (base blindada em 777 termos; RC-778 preservado).
"""

ANCORAS = [
    ("estamos ao vivo aqui no canal Estagiários do Caos", "## Abertura da live (Denise)"),
    ("o senhor abordará o tema dod e o controle do tempo", "## Pergunta 1 — o grupo: Ogdóade e o controle do tempo (evento em Goiânia)"),
    ("os oito personagens estivessem relacionados a apenas seis espíritos", "## Pergunta 2 — o grupo: a Tridevi, Deva/Aurora e a conta dos oito seres"),
    ("no início do livro Funeral da Evidência o senhor descreve que houve um movimento misterioso", "## Pergunta 3 — o grupo: o movimento misterioso e o ímpeto criativo no paraíso"),
    ("em má é apresentado como o espírito que ancora quatro centros de consciência", "## Pergunta 4 — o grupo: En Ma, os quatro centros e o Eu Coalescente"),
    ("a maneira em que você pode medir o seu grau de dignificação pessoal", "## Pergunta 5 — o grupo: a dignificação e a ascese espiritual"),
    ("siga você mesmo siga sua consciência", "## Encerramento — a dignificação de cada um"),
]

GLOSSARIO = """## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Eu Coalescente | RC-620 | ampliado (bondinho do Pão de Açúcar; dignificação) |
| En Ma (Emá/Emar) | RC-476 | ampliado (4 centros; caos 2.0; segredo de estado) |
| Deva / Aurora (A Grande Deusa) | RC-475 | ampliado ("Deva é Aurora"; forma mais ancestral) |
| Universo TÊNET | RC-626 | tema do evento de Goiânia (Hermópolis → TÊNET) |
| Enéade de Heliópolis | RC-627 | contexto (Ogdóade/Hermópolis) |
| Tridevi | RC-610 | ampliada (a conta dos espíritos; Adhy Shakti [REVISAR]) |
| Trimurti | RC-104 | ampliada (3 seres/2 espíritos; só Elm e Olm atuando) |
| Sophia | RC-009 | ampliada (agressão no início da Covid; vinda frágil) |
| Jesus | RC-072 | ampliado (não-continuidade; "não sabe acender o fósforo") |
| Metatron | RC-671 | ampliado (cubo = 12 funções) |
| Prabrajna | RC-152 | ampliado (um dos eus; resiliência) |
| Nyx / Kama / Corpos | RC-621 / RC-622 / RC-623-625 | contexto (faixa) |
| Vishnu / Lakshmi | RC-408 / RC-135 | contexto (colapso/desconstituição; Lakshmi [REVISAR — sem ficha]) |
| Ogdóade de Hermópolis | RC-609 | tema do evento; os 8 personagens |

### B. Conceitos desta live absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Eu Coalescente / bondinho | RC-620 | eu mental que une todos os eus do espírito |
| Deva = Aurora | RC-475 | a Grande Deusa de muitos nomes |
| En Ma / 4 centros | RC-476 | Javé, Sophia, Jesus, Vishnu; sobreposição futura |
| Caos 2.0 / universo B | RC-476 (contexto) | Colecionar Incertezas |
| Cubo de Metatron (12 funções) | RC-671 | contexto |
| A conta dos 8 seres | RC-104 / RC-610 | só Elm e Olm atuando |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

"Jeão Valelão/Jean Valuelan" (= Jan Val Ellam); "Ogod/Ogat/Augdod" (= Ogdóade); "Tênit" (= TÊNET); "Emá/Emar" (= En Ma); "Visno/Vígena" (= Vishnu); "Laxme/Dilaxme" (= Lakshmi); "Prabrag" (= Prabrajna); "metator" (= Metatron); "Ensara" (= Ensá); "exculhambação"; "aséase" (= ascese); "fóssil" (= fósforo); "Adhy Shakti"; "Gé" (= Giane); "cubo de metator".

### D. Quarentenas aplicadas

- **Teológica:** Ogdóade/Tridevi/Deva; Eu Coalescente; En Ma; "caos 2.0"; devoção/endeusamento — leitura do autor;
- **Clínica/psicológica:** "buraco negro mental"; "idiotice clínica"; ascese — leitura do autor, jamais dado validado;
- **Relato biográfico/pessoal:** "segredo de estado" sobre En Ma; "sem orientação ética para falar de Lakshmi"; vulnerabilidade de Sophia; agressão a Sophia no início da Covid — relatos do autor, jamais fato validado;
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
