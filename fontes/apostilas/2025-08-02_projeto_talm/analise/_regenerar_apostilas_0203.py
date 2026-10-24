#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera apostila.md (padrão TOP) para ART-2025-08-02 (Projeto TALM) e ART-2025-08-03 (Dossiê Fenvans).
Corrige: # PARTE X — (maiúsculo), ## Capítulo N — (títulos), notas do editor, mantém glossário A-D."""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]  # fontes/apostilas/

# ---- configuração por apostila ----
CONFIG = {
    "2025-08-02_projeto_talm": {
        "inicio_conteudo": "Introdução:",        # marcador que inicia o conteúdo real (2ª ocorrência)
        "titulo_partes": {
            "I": "As Origens Cósmicas do Design da Vida",
            "II": "A Operacionalização do Projeto TALM",
            "III": "A Jornada Humana no Projeto TALM",
            "IV": "O Futuro do Projeto TALM e a Revelação Cósmica",
        },
        "parte_capitulos": {"I": [1,2,3], "II": [4,5,6], "III": [7,8,9], "IV": [10,11]},
        "titulo": "Projeto TALM — A Semente Cósmica e a Arquitetura da Vida Universal",
    },
    "2025-08-03_dossie_fenvans": {
        "inicio_conteudo": "(Prefácio) -",
        "titulo_partes": {
            "I": "A Engenharia da Vida Primordial",
            "II": "A Natureza e a Psique do Fenvan",
            "III": "O Legado e a Esperança de Redenção",
        },
        "parte_capitulos": {"I": [1,2,3], "II": [4,5], "III": [6,7]},
        "titulo": "Dossiê Fenvans — A Gênese Nanotecnológica e o Sacrifício Cósmico",
    },
}

NOTAS = {
    "2025-08-02_projeto_talm": [
        ("## Introdução — O Prefácio do Arquiteto Cósmico",
         "Nota do editor: material de curadoria do ART-2025-08-02 (baseado estritamente em Ellam). O acrônimo expandido do TALM — 'Transferência do Código-fonte Definidor Pessoal do Criador para o Universo Material' — foi registrado pela 1ª vez na Base em RC-091 (ciclo Trilogia TALM)."),
        ("## Capítulo 1 — O \"Design Inteligente\" do Universo e o Vácuo do Acaso",
         "Nota do editor: 'código-fonte definidor de vida' remete a RC-217 (DNA como projeção holográfica do psiquismo) e ao nidana (RC-154); 'Matriz Divina/Campo de Energia' é leitura do autor [REVISAR — conferir grafia com fonte primária]."),
        ("## Capítulo 2 — O Drama do Criador e a Criação Imperfeita",
         "Nota do editor: QUARENTENA TEOLÓGICA — a 'doença de impulso nervoso' de Javé (RC-001) e o CFDP 'doentio' são leitura de Ellam; 'Tikun' (conserto) é conceito da Cabala (ver RC-263/RC-092)."),
        ("## Capítulo 3 — O \"Nidana\": A Semente Primordial da Vida",
         "Nota do editor: nidana (RC-154) — 'código-fonte primordial definidor de vida'; os quatro universos cabalísticos (Atziluth, Briah, Yetzirah, Assiah) são referência externa (Cabala), não ontologia própria."),
        ("## Capítulo 4 — A Semeadura da Vida Biológica e os Fornos Replicadores",
         "Nota do editor: os três fornos (RC-771) e as esferas coloridas (Awayen cinzenta; Awaymaion esverdeada opaca; Awaylengan amarronzada) — ver Trilogia TALM (ART-2025-08-01) e a Mensagem Talm (RC-080)."),
        ("## Capítulo 5 — O DNA Humano: Herança e Singularidade",
         "Nota do editor: QUARENTENA CLÍNICA — 'DNA lixo 95–97%', 'YHWH registrado nas bases químicas do DNA' e a 'brecha psíquica' (RC-541) são leitura do autor, jamais dado biomédico validado."),
        ("## Capítulo 6 — A \"Rebelião dos Elétrons\" e o Tecido da Existência",
         "Nota do editor: elétrons como memória quântica (RC-161/RC-160); a Rebelião dos Elétrons como 'único padrão modificador do CFDP'; Yel Luzbel (RC-002) e a família Val (RC-065/RC-089)."),
        ("## Capítulo 7 — A Humanidade como Artífice da Redenção",
         "Nota do editor: Criatura Universal (RC-042) e o 'favor divino' — a condição humana como 'protótipo possível' — leitura de Ellam (quarentena teológica)."),
        ("## Capítulo 8 — Os Desafios da Consciência: Mitos, Verdades e a Busca por Sentido",
         "Nota do editor: referências externas não ontológicas: Jeane Miranda (autora citada) e o resgate de 'mitos como fontes de conhecimento' — leitura do autor."),
        ("## Capítulo 9 — A Liberdade de Pensamento e a Maioridade Espiritual",
         "Nota do editor: 'sementes para reflexão, não dogmas' — o mesmo princípio metodológico da Arca (a revelação não se pretende verdadeira; ver RC-094)."),
        ("## Capítulo 10 — O Quarto Logos e a Reintegração Cósmica",
         "Nota do editor: Sophia (RC-009) como forma gloriosa de Jesus/Cristo Cósmico e 'Coagente' do Quarto Logos (RC-092); reintegração cósmica = fim do isolamento da Terra (RC-612/RC-638)."),
        ("## Capítulo 11 — Transformação do \"Nidana\" e o Futuro da Vida",
         "Nota do editor: o objetivo final do TALM — nidana → saccidanandhagana (RC-091/RC-154) — 'só será plenamente alcançado quando o problema da podridão de Brahma for resolvido'."),
        ("## Conclusão — O Legado em Evolução do Projeto TALM",
         "Nota do editor: encerramento — 'executar a sinfonia universal'; a humanidade como artífice; material do curador, não fonte primária."),
    ],
    "2025-08-03_dossie_fenvans": [
        ("## Prefácio — O Convite à Epopeia Oculta da Criação",
         "Nota do editor: dossiê técnico do ART-2025-08-03; os 'pré-requisitos' citados ('Projeto TALM – A Epopeia', 'O Éon das Três Esferas', 'Nanotecnologia e Projeto TALM') são obras do curador, não de Ellam."),
        ("## Capítulo 1 — O Arquiteto e a Ferramenta",
         "Nota do editor: Morlens (RC-772), Nanotecnologia Prânica (RC-773) e PEP (RC-774) — os três códigos novos criados neste ciclo Trilogia TALM (Devolutiva O-3)."),
        ("## Capítulo 2 — O Laboratório Cósmico - O Éon das Três Esferas",
         "Nota do editor: Éon das Três Esferas (RC-775, 'superloka'/'geno'); as esferas correspondem aos fornos (RC-771): cinzenta (Awayen/Brahma), esverdeada opaca (Awaymaion/Vishnu), amarronzada (Awaylengan/Shiva); a 'chave repassada para uma condição humana' vai para a Colecionar Incertezas."),
        ("## Capítulo 3 — A Gênese dos \"Primeiros Astronautas\"",
         "Nota do editor: Fenvans (RC-064) — 'seres-cobaias'/'primeiros astronautas'; o poema 'Venham até a borda' (Christopher Logue) é referência externa; Ginnungagap (RC-776) é a zona intercessória dos sobreviventes frustrados."),
        ("## Capítulo 4 — A \"Doença\" do Pensamento Único",
         "Nota do editor: QUARENTENA TEOLÓGICA — a 'programação suicida' e a 'demência original' do Criador Caído são leitura de Ellam via curador; 'lixo existencial' é termo do autor."),
        ("## Capítulo 5 — O Véu da Entropia e a Manipulação Inconsciente",
         "Nota do editor: QUARENTENA CLÍNICA CRÍTICA — a analogia do Toxoplasma Gondii é figura de linguagem do autor (manipulação inconsciente), JAMAIS parasitologia real; 'DNA lixo' e vírus como 'nanorrobôs' são leitura da RC, não biomedicina."),
        ("## Capítulo 6 — O Eco da \"Mensagem TALM\"",
         "Nota do editor: Mensagem Talm (RC-080) — 'carta de cinco partes', encontrada por Yel Lupon (RC-141), guardada no Processador Val (RC-089) em Alt' Lam Gron (RC-018); 'Seremos nós recebendo, de nós mesmos, o que agora transmitimos'; Dasein de Heidegger é referência externa."),
        ("## Capítulo 7 — A Humanidade como \"Luz no Fim do Túnel\"",
         "Nota do editor: Consciência Karuna (RC-165 — ficha materializada neste ciclo) como 'resposta silenciosa'; o 'novo eu' de Javé estruturado a partir dos humanos; a egrégora do IEEA e a verbalização 'reativando os filmes parados' (RC-094/RC-612)."),
        ("## Conclusão — A Sinfonia Inacabada da Redenção Cósmica",
         "Nota do editor: encerramento — humanos como 'catalisadores ativos na cura das feridas mais antigas da Criação'; material do curador, não fonte primária."),
    ],
}

def quebrar(texto, limite=400):
    frases = re.split(r"(?<=[.!?…])\s+", texto.strip())
    blocos, atual = [], ""
    for f in frases:
        if len(atual) + len(f) > limite:
            blocos.append(atual); atual = f
        else:
            atual = (atual + " " + f).strip()
    if atual:
        blocos.append(atual)
    return [b for b in blocos if b.strip()]

def extrair_glossario(apostila_atual):
    """Extrai '## GLOSSÁRIO LOCAL' até o fim do arquivo atual."""
    txt = apostila_atual.read_text(encoding="utf-8")
    i = txt.find("## GLOSSÁRIO LOCAL")
    if i == -1:
        return ""
    return txt[i:].rstrip() + "\n"

def main():
    for slug, cfg in CONFIG.items():
        pasta = RAIZ / slug
        orig = (pasta / "original.txt").read_text(encoding="utf-8-sig")
        linhas = [l.rstrip("\r") for l in orig.splitlines()]
        # --- localiza o início do conteúdo real (2ª ocorrência do marcador) ---
        marc = cfg["inicio_conteudo"]
        ocorrencias = [i for i, l in enumerate(linhas) if marc in l]
        if len(ocorrencias) == 0:
            print(f"!! {slug}: marcador '{marc}' não encontrado")
            inicio = 0
        else:
            inicio = ocorrencias[-1]  # última ocorrência = conteúdo (após o sumário)
        # --- mapeia número do capítulo -> parte ---
        cap_para_parte = {}
        for parte, caps in cfg["parte_capitulos"].items():
            for c in caps:
                cap_para_parte[c] = parte
        # --- parse do conteúdo ---
        out = []
        # cabeçalho @: reutiliza o do arquivo atual
        atual = (pasta / "apostila.md")
        cab = atual.read_text(encoding="utf-8").split("\n\n", 1)[0]
        out.append(cab.strip() + "\n")
        parte_atual = None
        capitulo_num = None
        for l in linhas[inicio:]:
            s = l.strip()
            if not s or re.match(r"^[=\-_]{5,}$", s):
                continue
            m_parte = re.match(r"^Parte ([IVX]+):\s*(.*)$", s)
            m_cap = re.match(r"^Capítulo (\d+|[IVX]+):\s*(.*)$", s)
            m_pref = re.match(r"^\(Prefácio\)\s*-?\s*(.*)$", s)
            m_conc = re.match(r"^Conclusão:?\s*(.*)$", s)
            m_intro = re.match(r"^Introdução:?\s*(.*)$", s)
            m_dossie = re.match(r"^Dossiê:?\s*(.*)$", s)
            if m_parte:
                # parte no conteúdo (03 tem; 02 não) — emite o heading
                rom = m_parte.group(1)
                if rom in cfg["titulo_partes"] and parte_atual != rom:
                    out.append(f"\n# PARTE {rom} — {cfg['titulo_partes'][rom]}\n")
                parte_atual = rom
                continue
            if m_cap:
                num_raw = m_cap.group(1)
                numero = int(num_raw) if num_raw.isdigit() else {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7}[num_raw]
                capitulo_num = numero
                titulo = m_cap.group(2).strip()
                # separa título fundido do texto introdutório (ex.: "Acaso Aqui, mergulharemos...")
                m_split = re.match(r"^(.*?)\s+(Aqui,|Este capítulo|Neste capítulo|Nesta seção|Aprofundaremos|Exploraremos|Adentraremos|Analisaremos|Abordaremos|Descreveremos|Discutiremos|Faremos|Reconheceremos|Reforçaremos|O ser humano|A capacidade|A ação|A existência|Apesar|No âmbito|Para|Neste|Esta)\b", titulo)
                if m_split and len(m_split.group(1)) > 10:
                    titulo = m_split.group(1).strip().rstrip(":")
                    resto = (m_split.group(2) + m_split.group(0)[len(m_split.group(1)):]).strip()
                else:
                    resto = ""
                parte_dest = cap_para_parte.get(numero)
                if parte_dest and parte_dest != parte_atual:
                    out.append(f"\n# PARTE {parte_dest} — {cfg['titulo_partes'][parte_dest]}\n")
                    parte_atual = parte_dest
                out.append(f"\n## Capítulo {numero} — {titulo}\n")
                if resto:
                    for par in quebrar(resto):
                        out.append(f"> {par}\n")
                continue
            if m_pref:
                out.append(f"\n## Prefácio — {m_pref.group(1).strip() or 'O Convite à Epopeia Oculta da Criação'}\n")
                continue
            if m_conc:
                out.append(f"\n## Conclusão — {m_conc.group(1).strip() or 'A Sinfonia Inacabada da Redenção Cósmica'}\n")
                continue
            if m_intro:
                out.append(f"\n## Introdução — {m_intro.group(1).strip() or 'O Prefácio do Arquiteto Cósmico'}\n")
                continue
            if m_dossie:
                out.append(f"\n## {s}\n")
                continue
            # bullets
            if s.startswith(("•", "o\t", "o ")):
                texto_bullet = s.lstrip("• o\t").strip()
                for par in quebrar(texto_bullet):
                    out.append(f"> • {par}\n")
                continue
            # parágrafo normal
            for par in quebrar(s):
                out.append(f"> {par}\n")
        # --- insere notas do editor após o título do capítulo correspondente ---
        corpo = "\n".join(out)
        for titulo_heading, nota in NOTAS[slug]:
            # a nota entra logo após o heading (antes do primeiro '>')
            idx = corpo.find(titulo_heading)
            if idx == -1:
                print(f"!! {slug}: heading não encontrado: {titulo_heading[:50]}")
                continue
            fim_linha = corpo.find("\n", idx)
            insere = fim_linha + 1
            corpo = corpo[:insere] + nota + "\n\n" + corpo[insere:]
        # --- glossário ---
        gloss = extrair_glossario(atual)
        corpo = corpo.rstrip() + "\n\n" + gloss + "\n"
        (pasta / "apostila.md").write_text(corpo, encoding="utf-8")
        n_partes = corpo.count("# PARTE ")
        n_notas = corpo.count("Nota do editor")
        n_pal = len(corpo.split())
        print(f"{slug}: {n_partes} PARTES | {n_notas} notas | {n_pal} palavras | glossário {'OK' if gloss else 'AUSENTE'}")

if __name__ == "__main__":
    main()
