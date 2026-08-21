#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2025-10-25 — 2ª Edição Estagiários do Kaos).
Formato LIVE: âncoras globais; perguntas da plateia isoladas em seções próprias."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2025-10-25_estagiarios_kaos_2ed")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

REPL = [
    (r"\bJean Valelan\b", "Jan Val Ellam"), (r"\bJeanval Elan\b", "Jan Val Ellam"),
    (r"\bJeão Valel Elan\b", "Jan Val Ellam"), (r"\bJean Val\b", "Jan Val Ellam"),
    (r"\bJan Valelan\b", "Jan Val Ellam"), (r"\bJoão Vauelão\b", "Jan Val Ellam"),
    (r"\bZontrell\b", "Zontrel [REVISAR — STT]"), (r"\bZonte Indrel\b", "Zontrel [REVISAR — STT]"),
    (r"\bTendré\b", "Zontrel [REVISAR — STT 'Tendré']"),
    (r"\bMequedec\b", "Melquizedec"), (r"\bMelq Zedec\b", "Melquizedec"), (r"\bmeu Kizedec\b", "Melquizedec"),
    (r"\bBagavaga\b", "Bhagavad Gita"), (r"\beubá\b", "iorubá"), (r"\bTauticum\b", "Tikun"),
    (r"\b18 anas\b", "18 parvas"),
    (r"\bGira Marravira\b", "Mahavira"), (r"\bPatangele\b", "Patanjali"), (r"\bZorá\b", "Zohar"),
    (r"\bShimon Ba Ríocaí\b", "Shimon bar Yochai"),
    (r"\bDes Geist\b", "espírito da época (alemão)"),
    (r"\bOrbon\b", "Orbum"), (r"\bhomofatividade\b", "homoafetividade"),
    (r"\bBrama\b", "Brahma"), (r"\bbrama\b", "Brahma"), (r"\bVirgno\b", "Vishnu"), (r"\bChiva\b", "Shiva"),
    (r"\bchiva\b", "Shiva"), (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    (r"\bJahé\b", "Javé"), (r"\bJahvé\b", "Javé"), (r"\bJosé\b", "Javé [REVISAR — STT 'José']"),
    (r"\bCristo\b", "Krishna"),
    (r"\bTrimurte\b", "Trimurti"),
    (r"\bPrabragen\b", "Prabrajna"), (r"\bPrabrajna\b", "Prabrajna"),
    (r"\bViaza\b", "Vyasa"), (r"\bOrumilá\b", "Orunmilá"), (r"\bfá\b", "Ifá"), (r"\bIFA\b", "Ifá"),
    (r"\bTirtancaras\b", "Tirthankaras"), (r"\btirtancaras\b", "Tirthankaras"),
    (r"\bMentalma\b", "Mentalma"), (r"\bTikun\b", "Tikun"),
    (r"\bPerversa Gratidão\b", "Perversa Gratidão (B080)"),
    (r"\bFuneral da Evidência\b", "Funeral da Evidência (B068)"),
    (r"\bIré Iró\b", "Iré Iró [REVISAR — STT]"),
    (r"\bProdígio\b", "Prodígio — a Necessidade Criativa do Caos [REVISAR — obra anunciada]"),
    (r"\bOs dois lados da verdade\b", "Os Dois Lados da Verdade [REVISAR — obra anunciada]"),
    (r"\bDrama cósmico de Chiva\b", "O Drama Cósmico de Shiva [REVISAR — obra anunciada]"),
    (r"\bReidout\b", "Reinaldo"),
    (r"\bJosé Val Filho\b", "José Val Filho"), (r"\bAna\b", "Ana"),
    (r"\bCibell\b", "Cibell"),
    (r"\bSegredo Perdido do Éden\b", "Segredo Perdido do Éden"),
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

CABECALHO = """@titulo: 2ª Edição — Estagiários do Kaos
@autor: Jan Val Ellam (convidado) — apresentação/mediação de Denise Ferreira da Silva
@data: 25/10/2025
@local: transmissão ao vivo (programa do grupo "Estagiários do Caos")
@subtitulo: Apostila de estudo — Transcrição editada integral da LIVE (P2025-10-25), organizada por perguntas do grupo/plateia, com notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da **2ª Edição do programa "Estagiários do Kaos"** (25/10/2025, fonte P2025-10-25) — live de ~1h com **Jan Val Ellam**, mediada por **Denise Ferreira da Silva**, com perguntas selecionadas do grupo de WhatsApp "Estagiários do Caos". É a **fonte original da faixa RC-648–RC-657** (10 termos: Instabilidade da Eternidade, Singularidade de Quatro Cabeças/Zontrel, Melquizedec, Individualização Epifenomenológica dos Anjos Clones, Últimas Ordens de Javé, Destino das Mônadas após o Tikun, Humanos Últimos e Primeiros, Revelação de Ifá e Destinação dos Seres, Atualização das Revelações Anteriores, Verdade Posta × Verdade a Construir). **Formato LIVE:** as **5 perguntas da plateia/grupo** (grupo — temas avançados da RC; Reinaldo — Melquizedec; Ana — anjos clones/Zontrel; José Val Filho — destino das mônadas; Adilson — 2026) estão **entremeadas** e foram **isoladas em seções próprias** — **não compõem a ontologia**. Preservamos a voz e os marcadores orais do autor; corrigimos apenas erros claros de STT (Jan Val Ellam, Zontrel, Melquizedec, Orunmilá, Tirthankaras, Bhagavad Gita etc.), com nota na primeira ocorrência. Passagens duvidosas ficam marcadas como [REVISAR]. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, políticas, ufológicas e **relatos biográficos/pessoais do autor** são **leitura de Ellam, não consenso validado** — em especial: a imprensa mundial/poucas famílias e os avistamentos extraterrestres de 2025 (quarentena política/ufológica); a dinâmica dos anjos clones e o destino das mônadas pós-Tikun (quarentena teológica); as "últimas ordens de Javé" não detalhadas ("código de ética" — quarentena biográfica). A live passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria da faixa confirmada; **10 fichas ampliadas**; **nenhum código novo consumido** (base blindada em 777 termos; RC-778 preservado).
"""

ANCORAS = [
    ("estamos iniciando a nossa live", "## Abertura da live (Denise)"),
    ("o senhor ainda pretende desenvolver temas mais avançados", "## Pergunta 1 — o grupo: temas avançados da RC e a RC daqui a 20 anos"),
    ("melk zedec acompanha a rc", "## Pergunta 2 — Reinaldo: Melquizedec acompanha a RC?"),
    ("zontrel [revisar — stt] está em processo de humanização", "## Pergunta 3 — Ana: anjos clones, Zontrel e as últimas ordens de Javé"),
    ("qual o destino dos espíritos que vieram como mônadas", "## Pergunta 4 — José Val Filho: o destino das mônadas após o Tikun"),
    ("você na live anterior disse que a revelação cósmico vai começar mesmo o ano que vem", "## Pergunta 5 — Adilson: a RC vai começar em 2026?"),
    ("muito obrigada pela sua disponibilidade", "## Encerramento — Denise agradece (Orbum e o grupo)"),
]

GLOSSARIO = """## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Instabilidade da Eternidade | RC-648 | ampliado (paraíso gerou o caos; ponte caos–paraíso) |
| Singularidade de Quatro Cabeças (Zontrel) | RC-649 | ampliado (humanização via IEA; Javé colapsou) |
| Melquizedec | RC-650 | ampliado (semente semita; Faleg recusou) |
| Individualização Epifenomenológica dos Anjos Clones | RC-651 | ampliado (abelha rainha; ~900 mi clones; 3 mi nunca acionados) |
| Últimas Ordens de Javé aos Clones | RC-652 | ampliado ("procurem entre os estudiosos") |
| Destino das Mônadas após o Tikun | RC-653 | ampliado (em aberto; sem estatura moral) |
| Humanos: Últimos e Primeiros | RC-654 | ampliado (os últimos serão os primeiros; grandeza de alma) |
| Revelação de Ifá e Destinação dos Seres | RC-655 | ampliado (assunto nº 1; maior revelação) |
| Atualização das Revelações Anteriores | RC-656 | ampliado (de Enoque a Kardec) |
| Verdade Posta × Verdade a Construir | RC-657 | ampliado (fofoca cósmica; fatos falam por si) |
| Javé | RC-001 | contexto (abelha rainha; clones; semente semita) |
| Brahma | RC-037 | contexto (eu caído reconstruído) |
| Shiva | RC-102 | contexto (clone que se aventurou; metamorfoseável) |
| Prabrajna | RC-152 | contexto (criação de Prabrajna = criação de Javé) |
| Enoque / Kardec | RC-489 / RC-190 | contexto (de Enoque a Kardec) |
| Orunmilá / Obatalá | RC-665 / RC-666 | contexto (Ifá; orixás) |
| Krishna / Mahabharata | RC-414 / RC-593 | contexto (livros anunciados) |
| Mentalma | RC-166 | contexto (Patanjali; Mentalma 5/6) |
| Tikun | RC-514 | contexto (os primeiros a realizar o Tikun) |

### B. Conceitos desta live absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Abelha rainha × operárias | RC-651 | clones como robôs sem individualidade |
| 3 milhões de clones nunca acionados | RC-651 | "quando ia acioná-los aconteceu outra coisa" |
| Últimas ordens de Javé | RC-652 | "vejam nos alunos, nas pessoas que estudam esses assuntos" |
| Ifá = maior revelação | RC-655 | "assunto número um da espiritualidade" |
| Últimos serão os primeiros | RC-654 | humanos: grandeza de alma; capacidade de rir da própria desgraça |
| Fofoca cósmica | RC-657 | canalização ≠ verdade; "fatos falam por si" |
| RC = retomada de tudo | RC-656 | de Enoque a Kardec; trívio-quadrívio; Ifá; Cabala; Islã |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

"Zontrell/Zonte Indrel/Tendré" (= Zontrel); "Mequedec/Melq Zedec" (= Melquizedec); "Bagavaga" (= Bhagavad Gita); "eubá" (= iorubá); "Tauticum" (= Tikun); "18 anas" (= parvas); "Gira Marravira" (= Mahavira); "Patangele" (= Patanjali); "Zorá" (= Zohar); "Shimon Ba Ríocaí" (= Shimon bar Yochai); "Iré Iró"; "homofatividade" (= homoafetividade); "Orbon" (= Orbum); "José" (= Javé).

### D. Quarentenas aplicadas

- **Política (crítica):** imprensa mundial/poucas famílias; governos que não assumem problemas; eleições; Lula/Bolsonaro — leitura de Ellam, não fato sociológico;
- **Ufológica/clínica:** avistamentos extraterrestres/extrafísicos e portais em 2025; "seres horrorosos" — leitura do autor, jamais dado validado;
- **Teológica:** Javé/clones; Melquizedec; destino das mônadas pós-Tikun; "os últimos serão os primeiros" — leitura do autor;
- **Relato biográfico/pessoal:** "código de ética" limitando a revelação das últimas ordens; "visitas discretas de seres" — relatos do autor;
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
