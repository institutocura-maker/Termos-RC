#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pós-processamento: insere notas editoriais ('Nota do editor:') na apostila
P2021-01-23 — padrão verde das demais apostilas."""
import sys
from pathlib import Path

ARQ = Path(sys.argv[1] if len(sys.argv) > 1 else "apostila.md")
NOTAS = [
    ("essa palestra de hoje ela é chata",
     "Nota do editor: abertura — o autor classifica a palestra como 'chata, mas necessária' e pede prudência; tema ligado a Vyasa (RC-585) e ao Novo Paraíso (RC-612)."),
    ("Vamos imaginar um poste, outro poste",
     "Nota do editor: a metáfora dos 'fios soltos' (poste e fios elétricos) — fonte original do conceito (RC-604; RC-104): 'quando o criador caiu, ele ficou com bilhões de fios soltos'."),
    ("ele gerou três seres que não são mulheres",
     "Nota do editor: as Moiras/Nornes (RC-467) como 'três seres que não são mulheres, como as mitologias falam' — herdeiros dos fios soltos; funcionam como 'computador/GPS' das assinaturas quânticas (U0075–U0120)."),
    ("quando as três flechas de Moros consorciassem",
     "Nota do editor: as três setas/flechas de Moros (RC-454): quando reencontradas, 'a história universal retroagiria ao momento zero e seria finalmente contada' (U0107–U0108; U1359–U1372)."),
    ("tudo que até hoje nós seres humanos pensamos sobre paraíso está absolutamente furado",
     "Nota do editor: tema-título — o paraíso 'furado' e os três reinos da antiguidade (RC-612); 'se isso aqui for paraíso, vamos inventar outro' (U1099)."),
    ("eu aposto meu poder contra esses seres",
     "Nota do editor: a aposta Javé×Vishnu (RC-001; RC-135 — ficha retida) envolvendo Enoque; 'eles têm um código de honra que quando um desafia o outro, o outro tem que aceitar' (U0369)."),
    ("Enoque foi chamado de Apantaratamas",
     "Nota do editor: Enoque = Apantaratamas (RC-489), nome da tradição védica; 'Tamas é energia de Shiva' — ver também Metatron (RC-671) e o corpo especial (U0525–U0540)."),
    ("pegou o DNA de Enoque e saiu fertilizando",
     "Nota do editor: [REVISAR — QUARENTENA]: 'o DNA de Enoque fertilizando demos e minérios' é passagem severa do STT e leitura do autor; registrada na Colecionar Incertezas (U0530–U0531)."),
    ("a humanidade é dividida em quatro grandes segmentos genéticos",
     "Nota do editor: os quatro segmentos genéticos (RC-024) — QUARENTENA CIENTÍFICA: leitura do autor ('estudo do genoma humano, não religião'), jamais dado validado (U0435–U0442)."),
    ("o nome Brahma surge aqui",
     "Nota do editor: Javé apresentando-se aos arianos como Brahma (RC-001/RC-037) após a recusa de Faleg (= espírito de Rochester) — 'Faleg = Rochester' na Colecionar Incertezas (U0461–U0475)."),
    ("Parashara foi um gênio",
     "Nota do editor: Parashara (RC-585) — pai de Vyasa, neto de Enoque; criador dos critérios da astrologia védica (Jyotisha) para comprovar avatares (U0538–U0545)."),
    ("Então a gente vai dar uma parada aí para tomar um café",
     "Nota do editor: INTERVALO — o autor interrompe para o café (U0571) e anuncia '15 minutinhos' (U0575)."),
    ("Druid quer dizer busca pela verdade",
     "Nota do editor: o método druida (RC-759): 'Druid quer dizer busca pela verdade'; os colégios druídicos, Tuatha de Danann e milesianos (U0732–U0760)."),
    ("professor Rivail na França",
     "Nota do editor: Kardec (RC-190 — ampliação retida, sem ficha física): o espírito que codificou foi Zéfiro (Rochester), 'já foi druida lá atrás' (U0762–U0769)."),
    ("Vyasa teve a ideia de criar um grupo",
     "Nota do editor: o grupo de 20 (de 250 a 21) e a Escola de Decifração (RC-585/RC-094): 'nós nascemos nessa vida para dar continuidade ao que Vyasa fez' (U0704–U0719; U0797–U0820)."),
    ("se apresentaram como avatar cachava",
     "Nota do editor: Krishna (RC-414) — STT 'avatar cachava' [REVISAR]: avatar que trazia 'uma porção da genética de cada um dos três seres' da Trimurti; Dwarka e a morte por flechada (U0876–U1097)."),
    ("surgiu a prosa, que foi Vyasa",
     "Nota do editor: o Mahabharata (RC-593): a prosa como inovação de Vyasa (vs. poesia métrica); as várias versões para cada família demo (U0799–U0800; U0868–U0871)."),
    ("nós próprios já estamos criando no Biocosmos emergente",
     "Nota do editor: o Biocosmos emergente e o novo fio (RC-163 — ampliação retida, sem ficha física; RC-612): 'parte biodêmica, parte humana' (U1142; U1185–U1187)."),
    ("Eu terminei um livro essa semana, chama-se Nem Deus",
     "Nota do editor: obra cadastrada como B082 — 'Nem Deus, nem Javé, nem Darwin: a evolução do cérebro' (U1259–U1260); sinopse reconstruída da fala, aguardando confirmação bibliográfica."),
    ("tem a assinatura quântica daqueles 28.869 genes",
     "Nota do editor: QUARENTENA CLÍNICA — '28.869 genes' e 'assinatura quântica do DNA' são leitura do autor, jamais dado validado (U1108–U1110)."),
    ("a astrologia ocidental ou mesmo védica, tem sua razão de existir",
     "Nota do editor: Pergunta 1 da plateia — resposta sobre a astrologia védica (função prática hoje; liberdade do ser humano); fala da plateia não compõe a ontologia (U1300–U1310)."),
    ("Próxima pergunta é uma pergunta um pouco mais técnica",
     "Nota do editor: Pergunta 2 da plateia — Jyotisha/Vedanga (STT 'Giotista'); o aparte de Ellam sobre Zeus e Apolo e os oráculos está registrado (U1311–U1324)."),
    ("o espírito de Marcos em Rochester teriam relação com o espírito das moiras",
     "Nota do editor: Pergunta 3 da plateia — espírito de Marcos/Rochester × moiras; resposta inclui Frigga/Aran e as três setas de Moros (U1348–U1372)."),
    ("Bem, agradeço então a vocês",
     "Nota do editor: encerramento — 'amanhã a gente continua às 10'; falas da plateia isoladas na PARTE XII não compõem a ontologia (U1402–U1404)."),
]

def main():
    linhas = ARQ.read_text(encoding="utf-8").splitlines()
    inseridas = 0
    faltantes = []
    for ancora, nota in NOTAS:
        idx = None
        for i, l in enumerate(linhas):
            if ancora.lower() in l.lower():
                idx = i
                break
        if idx is None:
            faltantes.append(ancora[:50])
            continue
        j = idx
        while j + 1 < len(linhas) and linhas[j + 1].startswith(">"):
            j += 1
        k = j + 1
        while k < len(linhas) and linhas[k].strip() == "":
            k += 1
        if k < len(linhas) and linhas[k].startswith("Nota do editor"):
            continue
        linhas.insert(k, nota)
        linhas.insert(k, "")
        inseridas += 1
    ARQ.write_text("\n".join(linhas), encoding="utf-8")
    print(f"notas inseridas: {inseridas}")
    if faltantes:
        print("âncoras não encontradas:")
        for f in faltantes:
            print("  -", f)

if __name__ == "__main__":
    main()
