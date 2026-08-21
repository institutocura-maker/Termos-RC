#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pós-processamento: insere notas editoriais ('Nota do editor:') no padrão verde
das apostilas anteriores. As notas são parágrafos simples (sem '>'), inseridos
logo após o fim do bloco de citação que contém a âncora."""
import sys
from pathlib import Path

ARQ = Path(sys.argv[1] if len(sys.argv) > 1 else "apostila.md")
NOTAS = [
    # (âncora, nota) — âncora: substring única numa linha de citação (ou heading)
    ("Meu fraternal abraço a vocês",
     "Nota do editor: abertura da palestra; o autor pede prudência máxima por tratar de temas 'além, muito além do nosso horizonte de percepção' e adverte que 'o assunto é zebra, é zebrado' (U0001–U0038)."),
    ("quem introduziu isso no pensamento humano foi a leitura do Mahabharata",
     "Nota do editor: STT 'Marata' = Mahabharata (RC-593); o autor atribui à recitação do Mahabharata, 'de seus diversos parvas', a introdução da noção de passado/presente/futuro no pensamento humano — leitura de Ellam."),
    ("intramuros vibratórios para não exportar",
     "Nota do editor: 'departamentalização da vida... intramuros vibratórios' (RC-601) e 'blindagens interdimensionais' (RC-602) — grafias canônicas da Base."),
    ("que eu chamo de Ereon",
     "Nota do editor: STT 'héreo' = Ereon; STT 'arquelos/arquieron/arcãos' = Archeons (RC-596) — grafia canônica da Base."),
    ("são cinco Archeons",
     "Nota do editor: os cinco Archeons de Ereon — Antérion (RC-597), Danérion (RC-598), Mermérion (RC-599), Perpérion (RC-087) e Tempérion (RC-472) — ver também a apostila P2020-07-11 (Ogdóade)."),
    ("seriam considerados autistas",
     "Nota do editor: 'autismo funcional' (RC-605) — QUARENTENA CLÍNICA CRÍTICA: é figura de linguagem filosófica do autor aplicada aos Seres da Espiritualidade Superior; jamais um diagnóstico ou afirmação médica sobre indivíduos terrestres."),
    ("A espécie Pashvnaj com 43 figuras",
     "Nota do editor: STT 'vinage/pasivagem' = Pashvnaj (RC-455), espécie de 43 seres do Gênero Adhy (RC-411 — 147 seres, 5 espécies)."),
    ("ilha estacionária do paraíso",
     "Nota do editor: 'ilha estacionária' é um epíteto emprestado do Livro de Urântia (RC-600) — referência externa, não é obra de Ellam; o autor ressalva que Urantia dá outro sentido à história."),
    ("vibrante em coma na parte de Perpérion",
     "Nota do editor: o 'espírito fatiado em coma em Perpérion' refere-se a Adhy Prabrajna (RC-152), com parte implodida na queda — ver também Perpérion (RC-087) e Fatiamento de Consciência (RC-604)."),
    ("Perpérion foi meio que invadida",
     "Nota do editor: a 'invasão' de Perpérion por grupos de todos os quadrantes da espiritualidade superior (à exceção do paraíso) — sem isolamento — é detalhe exclusivo desta fonte (RC-596/RC-087)."),
    ("cujos nomes eram Elm e Olm",
     "Nota do editor: Elm (RC-454 — Moros, ser LM de Tempérion) e Olm (RC-092 — Quarto Logos); o gênero Ser LM é RC-456 e Tempérion é RC-472."),
    ("a [Ogdóade] composta por seis Seres Adhy e dois Seres LM",
     "Nota do editor: a composição da Ogdóade de Hermópolis (RC-609) como 6 Seres Adhy (que formariam a Trimurti/Tridevi — RC-104/RC-610) + 2 Seres LM (Elm e Olm — RC-607) é confirmação da fonte original; ver apostila P2020-07-11."),
    ("filhos do abismo",
     "Nota do editor: 'filhos do abismo' — denominação dos Seres Adhy (RC-411): 'eles olharam no abismo e caíram' (U0402–U0404)."),
    ("as flechas de Moros, nas profecias de Moros",
     "Nota do editor: as Flechas/Profecias de Moros (RC-611; RC-454): 'só quando as flechas fossem revividas no sentido de revelação psíquica, espiritual e cósmica, a história do universo voltaria ao ponto zero para ser novamente contada'."),
    ("vem dos Seres Adhy, vem com essa infecção dos AD",
     "Nota do editor: QUARENTENA TEOLÓGICA — 'as religiões opressivas e impositivas vêm dos Seres Adhy' é leitura de Ellam, não fato; ver também RC-411."),
    ("general Ludd",
     "Nota do editor: STT 'geral Lud' = general Ludd [REVISAR — referência cultural; Colecionar Incertezas]."),
    ("são 18.000 anos difíceis",
     "Nota do editor: os '18.000 anos difíceis' (U0579) confirmam o prazo já registrado na Colecionar Incertezas; ligado ao pacto de convivência com o universo vizinho (RC-614/RC-615)."),
    ("Apolônio de Tiana foi a única encarnação",
     "Nota do editor: Apolônio de Tiana = única encarnação de Olm (RC-092) — revelação desta fonte; o autor remete ao livro 'O Quarto Logos' (B016)."),
    ("Inquisição Espiritual e alguém de dentre vocês",
     "Nota do editor: 'Inquisição Espiritual' (RC-617) é obra ANUNCIADA (B079) — 3 Inquisições já lançadas (Poética, Filosófica, Trimurtiana); o Roseral do Alto (RC-616) é descrito nesta resposta."),
    ("surgiu a linguagem através do gene FOXP2",
     "Nota do editor: 'genoma da liberdade' (RC-619) — QUARENTENA CLÍNICA: menções a FOXP2, 28.869 genes e Julian Jaynes são leitura do autor, jamais dado validado."),
    ("isso aqui é só o início",
     "Nota do editor: encerramento — 'a gente aprender a colecionar incertezas' (U0699–U0713); falas da plateia isoladas na PARTE X não compõem a ontologia da Base."),
]

def main():
    linhas = ARQ.read_text(encoding="utf-8").splitlines()
    inseridas = 0
    faltantes = []
    for ancora, nota in NOTAS:
        # localiza a linha que contém a âncora
        idx = None
        for i, l in enumerate(linhas):
            if ancora.lower() in l.lower():
                idx = i
                break
        if idx is None:
            faltantes.append(ancora[:50])
            continue
        # avança até o fim do bloco de citação (linha vazia ou não iniciada por '>')
        j = idx
        while j + 1 < len(linhas) and linhas[j + 1].startswith(">"):
            j += 1
        # pula linhas em branco após o bloco
        k = j + 1
        while k < len(linhas) and linhas[k].strip() == "":
            k += 1
        # se a próxima linha já é uma nota do editor, não duplicar
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
