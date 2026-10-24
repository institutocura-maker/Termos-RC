#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o texto-base editado da apostila P2021-01-23 a partir do leitura-segmentada.txt.
Correções canônicas conservadoras + marcas [REVISAR] em passagens severas.
Saída: apostila_trabalho/parte-XX.md (texto em blockquote, ainda sem título/notas finais)."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2021-01-23_vyasa_descortinar_novo_paraiso")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
OUT = BASE / "apostila_trabalho"
OUT.mkdir(exist_ok=True)

PARTES = [
    ("01", "U0001", "U0030"),
    ("02", "U0030", "U0075"),
    ("03", "U0075", "U0120"),
    ("04", "U0120", "U0200"),
    ("05", "U0200", "U0450"),
    ("06", "U0450", "U0525"),
    ("07", "U0525", "U0571"),
    ("08", "U0575", "U0750"),
    ("09", "U0750", "U0820"),
    ("10", "U0820", "U1050"),
    ("11", "U1050", "U1300"),
    ("12", "U1300", "U1404"),
]

# ---- replaces canônicos (ordem importa; nomes longos primeiro) ----
REPL = [
    (r"\bApantaratamas\b", "Apantaratamas"),
    (r"\bapantaratamas\b", "Apantaratamas"),
    (r"\bAparantaras\b", "Apantaratamas"),
    (r"\bapantar[atãa]?ras?\b", "Apantaratamas"),
    (r"\bPantaratas\b", "Apantaratamas"),
    (r"\bParachara\b", "Parashara"),
    (r"\bParacharada\b", "Parashara"),
    (r"\bParachá\b", "Parashara"),
    (r"\bCharasa\b", "Parashara"),
    (r"\bParach\b", "Parashara"),
    (r"\bViaza\b", "Vyasa"),
    (r"\bViasa\b", "Vyasa"),
    (r"\bviaza\b", "Vyasa"),
    (r"\bViáa\b", "Vyasa"),
    (r"\bVia\b", "Vyasa"),
    (r"\bMarrabarata\b", "Mahabharata"),
    (r"\bBarrabarata\b", "Mahabharata"),
    (r"\bmarrabarata\b", "Mahabharata"),
    (r"\bMarrabarato\b", "Mahabharata"),
    (r"\bBarrabarat\b", "Mahabharata"),
    (r"\bGiotista\b", "Jyotisha"),
    (r"\bGiosticha\b", "Jyotisha"),
    (r"\bGiatis\b", "Jyotisha"),
    (r"\bJotisha\b", "Jyotisha"),
    (r"\bVedanca\b", "Vedanga"),
    (r"\bBagabagita\b", "Bhagavad Gita"),
    (r"\bRamaiana\b", "Ramayana"),
    (r"\bVígno Pur\b", "Vishnu Purana"),
    (r"\bVígnio Pur\b", "Vishnu Purana"),
    (r"\bDuarca\b", "Dwarka"),
    (r"\bDuar[ck]a\b", "Dwarka"),
    (r"\bCapila\b", "Kapila"),
    (r"\bSidarta Galutano\b", "Sidarta Gautama"),
    (r"\bSidarta Galutan\b", "Sidarta Gautama"),
    (r"\bGina Marvira\b", "Mahavira"),
    (r"\bGinamarravira\b", "Mahavira"),
    (r"\bGinamaravira\b", "Mahavira"),
    (r"\btirtancaras\b", "Tirthankaras"),
    (r"\bTirtancara\b", "Tirthankara"),
    (r"\bTirtancaras\b", "Tirthankaras"),
    (r"\bFriga\b", "Frigga"),
    (r"\bfragil\b", "Frigga"),
    (r"\bFrida\b", "Frigga"),
    (r"\bCristva\b", "Krishna"),
    (r"\bCristo\b", "Krishna"),
    (r"\bCrist\b", "Krishna"),
    (r"\bChiva\b", "Shiva"),
    (r"\bchiva\b", "Shiva"),
    (r"\bChilo\b", "Shiva"),
    (r"\bChica\b", "Shiva"),
    (r"\bChila\b", "Shiva"),
    (r"\bde China\b", "de Shiva"),
    (r"\bChirão\b", "Shiva"),
    (r"\bVirghiva\b", "Vishnu"),
    (r"\bVirgometeu\b", "Vishnu"),
    (r"\bVirgem\b", "Vishnu"),
    (r"\bVirgo\b", "Vishnu"),
    (r"\bVgo\b", "Vishnu"),
    (r"\bVism\b", "Vishnu"),
    (r"\bVirg\b", "Vishnu"),
    (r"\bBrama\b", "Brahma"),
    (r"\bbrama\b", "Brahma"),
    (r"\bJaé\b", "Javé"),
    (r"\bJahé\b", "Javé"),
    (r"\bJosavé\b", "Javé"),
    (r"\bJabé\b", "Javé"),
    (r"\bJé\b", "Javé"),
    (r"\bJaé\b", "Javé"),
    (r"\bde mos\b", "de Moros"),
    (r"\bde móveis\b", "de Moros"),
    (r"\bde mores\b", "de Moros"),
    (r"\bde mortos\b", "de Moros"),
    (r"\bMórus\b", "Moros"),
    (r"\bas loiras\b", "as moiras"),
    (r"\bas noras\b", "as nornes"),
    (r"\bno modo\b", "Odino"),
    (r"\bRoché\b", "Rochester"),
    (r"\bRocheste\b", "Rochester"),
    (r"\brochester\b", "Rochester"),
    (r"\bZéfra\b", "Zéfiro"),
    (r"\bRivai\b", "Rivail"),
    (r"\bSofia\b", "Sophia"),
    (r"\bsofia\b", "Sophia"),
    (r"\bdo suf\b", "de Sophia"),
    (r"\bFale\b", "Faleg"),
    (r"\bfalec\b", "Faleg"),
    (r"\bJoquã\b", "Joctã"),
    (r"\bJotã\b", "Joctã"),
    (r"\bJoquan\b", "Joctã"),
    (r"\bGommer\b", "Gomer"),
    (r"\bPacho Pato\b", "Pashupati"),
    (r"\bPachupati\b", "Pashupati"),
    (r"\bPashupati\b", "Pashupati"),
    (r"\bcom mar e candão\b", "Tamil [REVISAR — STT 'com mar e candão']"),
    (r"\bMaric Candô\b", "Tamil [REVISAR — STT 'Maric Candô']"),
    (r"\bálbum branco dos bits\b", "álbum branco dos Beatles"),
    (r"\bdos bits\b", "dos Beatles"),
    (r"\bBeetles\b", "Beatles"),
    (r"\bIA\b", "IEA"),
    (r"\bIa\b", "IEA"),
    (r"\btrigerina\b", "vanguarda [REVISAR — STT 'trigerina']"),
    (r"\bMéxica\b", "Méxica [REVISAR]"),
    (r"\bcachava\b", "cachava [REVISAR — STT]"),
    (r"\bAranque\b", "Aran"),
    (r"\bBiocosmos\b", "Biocosmos"),
    (r"\bbiocosmos\b", "Biocosmos"),
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

def main():
    unidades = carregar_unidades()
    total = 0
    for num, ini, fim in PARTES:
        chaves = [k for k in unidades if ini <= k <= fim]
        # trata sobreposição de fronteira: unidade do fim pertence à parte seguinte
        if num not in ("12",):
            chaves = [k for k in chaves if k != fim]
        blocos = [unidades[k] for k in chaves]
        texto = " ".join(blocos)
        texto = aplicar(texto)
        # parágrafos: quebra a cada ~3 frases por pontuação forte
        frases = re.split(r"(?<=[.!?…])\s+", texto)
        paragrafos, atual = [], ""
        for f in frases:
            if len(atual) + len(f) > 420:
                paragrafos.append(atual)
                atual = f
            else:
                atual = (atual + " " + f).strip()
        if atual:
            paragrafos.append(atual)
        corpo = "\n".join(f"> {p}" for p in paragrafos if p.strip())
        arq = OUT / f"parte-{num}.md"
        arq.write_text(corpo + "\n", encoding="utf-8")
        n = sum(len(p.split()) for p in paragrafos)
        total += n
        print(f"parte-{num}: U{chaves[0]}–U{chaves[-1]} | {len(chaves)} unidades | ~{n} palavras")
    print(f"TOTAL ~{total} palavras")

if __name__ == "__main__":
    main()
