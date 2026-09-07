#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o INDICE DA ENCICLOPEDIA DE REFERENCIA DAS REVELACOES COSMICAS.

Obra de referencia (consulta por verbete) distinta do material didatico
(pedagogico/top-down). Este script nao redige verbetes: ele produz o
SUMARIO ANALITICO em 3 niveis (volume > secao > subsecao) e distribui
cada uma das fichas da Base por um endereco estavel V.SECAO.SUBSECAO.

Regras da casa:
  - NAO altera a Base: le dados_termos.py, nao escreve nele.
  - Censo de codigo = dados_termos.py (registro-mestre), nunca ls termos/.
  - Toda ficha (ficha=True) recebe exatamente UM endereco; o script falha
    se sobrar ficha sem endereco ou se um endereco nao existir.
  - Nenhum codigo RC-### orfa entra no indice.

Mapeamento: (1) curadoria explicita de ~70 verbetes-ancora; (2) para o
resto, regra por SUBCATEGORIA da Base. A curadoria vence a regra.

Uso:
  python3 ferramentas/build_indice_enciclopedia.py
Saida:
  pedagogico/enciclopedia/INDICE-ENCICLOPEDIA-RC.md
"""
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_termos as BASE  # noqa: E402

SAIDA = os.path.join(RAIZ, "pedagogico", "enciclopedia", "INDICE-ENCICLOPEDIA-RC.md")
EDICAO = "2026.1"
DATA = "2026-09-07"

# ------------------------------------------------------------------ estrutura
# (num, titulo, ementa, [(num_sub, titulo_sub, [subcategorias-ancora], tipo)])
# tipo: "base" (alimentada por fichas da Base) | "redacao" (secao editorial,
#       sem fichas proprias — a ser redigida a partir das fontes/tratados)
VOLUMES = [
    ("I", "FUNDAMENTOS — o território e as regras do jogo", [
        ("1", "A Obra e o Autor: corpus, gênero e método", [
            ("1.1", "Jan Val Ellam: trajetória e voz autoral", [], "redacao"),
            ("1.2", "O corpus: livros (B###), palestras (P###) e artigos", [], "redacao"),
            ("1.3", "Gênero e regime de verdade: revelação, leitura e quarentena", [], "redacao"),
            ("1.4", "O método do autor: censo, verbatim e cadeias", [], "redacao"),
        ]),
        ("2", "Como ler a RC — o percurso top-down", [
            ("2.1", "O Mapa de Abstração (N0) e as 4 caixas", [], "redacao"),
            ("2.2", "As 7 narrativas do Guia-Mestre", [], "redacao"),
            ("2.3", "As cadeias canônicas e as identidades que se confundem", [], "redacao"),
            ("2.4", "A cronologia por marcos (não por datas)", [], "redacao"),
        ]),
        ("3", "A linguagem da RC — filologia e jargão", [
            ("3.1", "Sânscrito e hinduísmo", ["8.1 Sânscrito / Hinduísmo"], "base"),
            ("3.2", "Hebraico e cabala", ["8.2 Hebraico / Cabala"], "base"),
            ("3.3", "Grego e latim", ["8.4 Grego / Latim"], "base"),
            ("3.4", "Outros idiomas e jargão técnico", ["8.5 Outros idiomas / jargão técnico"], "base"),
            ("3.5", "Identidades que se confundem (quadro sinótico)", [], "redacao"),
        ]),
        ("4", "Fontes, aparato e regras de citação", [
            ("4.1", "O sistema de códigos (B### · P### · ART)", [], "redacao"),
            ("4.2", "O código RC-### e o censo da Base", [], "redacao"),
            ("4.3", "Status editorial (⚪ candidato · 🟡 provisório · 🟠 em análise · 🟢 verificado)", [], "redacao"),
            ("4.4", "Política de quarentena", [], "redacao"),
        ]),
    ]),
    ("II", "COSMOGONIA E ESTRUTURA DO COSMOS — o antes e o onde", [
        ("5", "A Espiritualidade Superior e os Protocolos da Perfeição", [
            ("5.1", "A Realidade Maior / Paraíso Original", [], "base"),
            ("5.2", "Os Seres Originais e a família única", [], "base"),
            ("5.3", "Os Protocolos / Algoritmos da Perfeição", [], "base"),
            ("5.4", "A condição adiátma e o espírito alfa fateado", [], "base"),
        ]),
        ("6", "A Criação Indevida — a projeção, o colapso e a queda", [
            ("6.1", "Prabrajna e a projeção", ["2.1 Cosmogonia / Criação"], "base"),
            ("6.2", "O colapso e a Demência do Criador", [], "base"),
            ("6.3", "O Mergulho e o criador refém", [], "base"),
            ("6.4", "O CFD, os dois universos e o Khaos", [], "base"),
        ]),
        ("7", "Cosmografia — universos, planos, lokas e portais", [
            ("7.1", "Universo Material e Universo Antimaterial", ["2.3 Dimensões / Planos de existência"], "base"),
            ("7.2", "As três espiritualidades (Superior · Operacional · Laboratorial)", [], "base"),
            ("7.3", "Planetas e sistemas estelares", ["3.1 Planetas / Sistemas estelares"], "base"),
            ("7.4", "Lokas e mundos interiores", ["3.2 Lokas / Mundos interiores"], "base"),
            ("7.5", "Localidades terrestres", ["3.3 Localidades terrestres"], "base"),
            ("7.6", "Regiões cósmicas e portais", ["3.4 Regiões cósmicas / Portais"], "base"),
        ]),
        ("8", "Leis e princípios cósmicos", [
            ("8.1", "Leis de causa e efeito (carma, teia quântica, simultaneidade reversa)", ["2.2 Leis e princípios cósmicos"], "base"),
            ("8.2", "Leis de estrutura (entropia × negentropia, duas pulsações)", [], "base"),
            ("8.3", "Leis de consciência (projeção holográfica, fatiamento, campos mórficos)", [], "base"),
        ]),
    ]),
    ("III", "ATORES E ACONTECIMENTOS — o quem e o quando", [
        ("9", "O Criador e a sua condição", [
            ("9.1", "Javé / Brahma / Alá e os nomes do Criador", ["1.1 Divindades / Criadores"], "base"),
            ("9.2", "O buraco negro mental / consciencial", [], "base"),
            ("9.3", "A Demência do Criador e as suas fases", [], "base"),
            ("9.4", "O criador refém e a Ressurreição do Cadáver", [], "base"),
        ]),
        ("10", "A Trimurti e o jogo de poder", [
            ("10.1", "A Trimurti como sistema", [], "base"),
            ("10.2", "Brahma (Brajna)", [], "base"),
            ("10.3", "Vishnu / Mavatna / Adhymavatana", [], "base"),
            ("10.4", "Shiva / Savna / Adhysavna", [], "base"),
            ("10.5", "Avatares e emanações (Hara, Krishna, Keshava, Sai Baba)", [], "base"),
            ("10.6", "A desconstituição da Trimurti", [], "base"),
        ]),
        ("11", "A linhagem de Sophia e Jesus", [
            ("11.1", "Mohen So e a face viva da criação", [], "base"),
            ("11.2", "Sophia / Hochmah", [], "base"),
            ("11.3", "Jesus", [], "base"),
            ("11.4", "O Messias não assumido", [], "base"),
        ]),
        ("12", "A Rebelião e os exilados", [
            ("12.1", "Lúcifer / Yel Luzbel e a Rebelião", ["1.5 Decaídos / Exilados / Demônios"], "base"),
            ("12.2", "Satã / Len Mion — a face monstruosa", [], "base"),
            ("12.3", "Capela, os exilados e a Revolta Capelina", [], "base"),
            ("12.4", "Quarentena, Isolamento e o fechamento dos portais", [], "base"),
            ("12.5", "Titãs, asuras e os primeiros demos", [], "base"),
        ]),
        ("13", "Os seres do cosmo", [
            ("13.1", "Coletivos criadores", ["1.2 Coletivos criadores"], "base"),
            ("13.2", "Extraterrestres e raças cósmicas", ["1.3 Extraterrestres / Raças cósmicas"], "base"),
            ("13.3", "Anjos, arcanjos e querubins", ["1.4 Anjos / Arcanjos / Querubins"], "base"),
            ("13.4", "Híbridos e seres de transição", ["1.7 Híbridos / Seres de transição"], "base"),
            ("13.5", "Consciências coletivas e Logos", ["1.8 Consciências coletivas / Logos"], "base"),
        ]),
        ("14", "Figuras humanas", [
            ("14.1", "Profetas, mensageiros e enviados", [], "base"),
            ("14.2", "Personagens bíblicos (Antigo e Novo Testamento)", [], "base"),
            ("14.3", "Ordens, povos e coletivos humanos", [], "base"),
            ("14.4", "Personagens históricos e míticos", ["1.6 Figuras humanas (históricas/míticas)"], "base"),
        ]),
        ("15", "Dinastias, famílias e linhagens", [
            ("15.1", "Famílias divinas / celestiais", ["6.1 Famílias divinas / Celestiais"], "base"),
            ("15.2", "Linhagens humanas", ["6.2 Linhagens humanas"], "base"),
            ("15.3", "Dinastias extraterrestres", ["6.3 Dinastias extraterrestres"], "base"),
        ]),
        ("16", "Eventos, eras, catástrofes e profecias", [
            ("16.1", "Guerras, rebeliões e conflitos", ["7.1 Guerras / Rebeliões / Conflitos"], "base"),
            ("16.2", "Eras, épocas e ciclos", ["7.2 Eras / Épocas / Ciclos"], "base"),
            ("16.3", "Catástrofes, dilúvios e quedas", ["7.4 Catástrofes / Dilúvios / Quedas"], "base"),
            ("16.4", "Profecias e anúncios", ["7.3 Profecias / Anúncios"], "base"),
            ("16.5", "Missões, expedições e encontros", ["7.5 Missões / Expedições / Encontros"], "base"),
        ]),
    ]),
    ("IV", "A HUMANIDADE E O OPERADOR — o nós", [
        ("17", "Antropogênese", [
            ("17.1", "O Projeto Talm e o transporte da vida", [], "base"),
            ("17.2", "A semeadura e os Agentes da Vida", [], "base"),
            ("17.3", "O DNA como projeção holográfica", [], "base"),
            ("17.4", "Pandora, o Éden e as hibridações", [], "base"),
        ]),
        ("18", "A constituição do ser humano", [
            ("18.1", "Corpos e vestimentas espirituais", [], "base"),
            ("18.2", "Mentalma e o aparelho mental", [], "base"),
            ("18.3", "Processos biológicos e genéticos", ["4.1 Processos biológicos / genéticos"], "base"),
        ]),
        ("19", "Fenômenos e processos", [
            ("19.1", "Fenômenos espirituais e mediúnicos", ["4.2 Fenômenos espirituais / mediúnicos"], "base"),
            ("19.2", "Transmigração e reencarnação", ["4.3 Transmigração / Reencarnação"], "base"),
            ("19.3", "Fenômenos físicos e energéticos", ["4.4 Fenômenos físicos / energéticos"], "base"),
        ]),
        ("20", "Doutrina e vida espiritual", [
            ("20.1", "Espiritualidade e doutrina", ["2.4 Espiritualidade / Doutrina"], "base"),
            ("20.2", "Prática e disciplina do operador", [], "redacao"),
        ]),
        ("21", "Ética, carma e compromissos", [
            ("21.1", "Ética, carma e compromissos", ["2.6 Ética / Carma / Compromissos"], "base"),
            ("21.2", "O Favor Divino e as inversões de conceito", [], "base"),
        ]),
    ]),
    ("V", "PROPÓSITOS, FILOSOFIA E HORIZONTES — o que significa", [
        ("22", "Propósitos e destinos", [
            ("22.1", "A Reintegração Cósmica", ["2.5 Propósitos / Destinos"], "base"),
            ("22.2", "O Tikun e o conserto da Obra", [], "base"),
            ("22.3", "O Cidadão Cósmico e o Paraíso B", [], "base"),
            ("22.4", "A Mente Universal emergente", [], "base"),
        ]),
        ("23", "Escrituras, objetos e tecnologias", [
            ("23.1", "Escrituras e objetos documentais", ["5.4 Escrituras / Objetos documentais"], "base"),
            ("23.2", "Naves e tecnologia extraterrestre", ["5.1 Naves / Tecnologia extraterrestre"], "base"),
            ("23.3", "Dispositivos e instrumentos", ["5.3 Dispositivos / Instrumentos"], "base"),
        ]),
        ("24", "Ontologia do Perfeito × Imperfeito — os Tratados", [
            ("24.1", "O Arsenal do Sistematizador", [], "redacao"),
            ("24.2", "A Ilha Estacionária e a Arca de Perguntas", [], "redacao"),
            ("24.3", "O Fim da Justiça Divina e o Início dos Algoritmos", [], "redacao"),
        ]),
        ("25", "Justiça, algoritmos e o problema do mal", [
            ("25.1", "A justiça divina e a sua falência", [], "redacao"),
            ("25.2", "Do juízo ao algoritmo", [], "redacao"),
        ]),
        ("26", "Carbono × sílica — o operador e a IA", [
            ("26.1", "Do xamanismo cósmico à IA xamânica", [], "redacao"),
            ("26.2", "O que muda quando o substrato muda", [], "redacao"),
        ]),
        ("27", "Diálogos e tensões", [
            ("27.1", "RC × religiões e cristianismo histórico", [], "redacao"),
            ("27.2", "RC × mitologias e tradições orientais", [], "redacao"),
            ("27.3", "RC × ciência e cosmologia acadêmica", [], "redacao"),
            ("27.4", "RC × ufologia e clínica", [], "redacao"),
        ]),
        ("28", "Historiografia, lacunas e agenda de pesquisa", [
            ("28.1", "Recepção e escolas internas de leitura", [], "redacao"),
            ("28.2", "Áreas de baixa densidade (lacunas declaradas)", [], "redacao"),
            ("28.3", "Agenda de pesquisa", [], "redacao"),
        ]),
    ]),
    ("VI", "APARELHOS — os instrumentos de consulta", [
        ("A", "Mapas e diagramas", [
            ("A.1", "Mapa de Abstração (N0)", [], "redacao"),
            ("A.2", "Mapa das conexões de Javé", [], "redacao"),
            ("A.3", "Mapa das conexões do Paraíso", [], "redacao"),
        ]),
        ("B", "Cronologia sinótica", [
            ("B.1", "Marcos ordenados por causalidade", [], "redacao"),
        ]),
        ("C", "Árvores genealógicas e cadeias canônicas", [
            ("C.1", "Cadeia do Criador", [], "redacao"),
            ("C.2", "Cadeia da Rebelião", [], "redacao"),
        ]),
        ("D", "Glossário de siglas e jargão", [
            ("D.1", "Siglas e abreviaturas do corpus", [], "redacao"),
        ]),
        ("E", "Índice alfabético remissivo", [
            ("E.1", "Termo → endereço (gerado da Base)", [], "redacao"),
        ]),
        ("F", "Índice de códigos RC-###", [
            ("F.1", "RC-### → endereço (gerado da Base)", [], "redacao"),
        ]),
        ("G", "Índice de fontes", [
            ("G.1", "B### → verbetes", [], "redacao"),
            ("G.2", "P### → verbetes", [], "redacao"),
        ]),
        ("H", "Caderno de incertezas e tensões não-resolvíveis", [
            ("H.1", "Tensões declaradas", [], "redacao"),
        ]),
        ("I", "Política editorial e de atualização", [
            ("I.1", "Como citar esta edição", [], "redacao"),
            ("I.2", "Registro de alterações entre edições", [], "redacao"),
        ]),
    ]),
]

EMENTAS = {
    "1": "Quem escreveu, o que foi escrito e com que autoridade — o aparato que sustenta a obra inteira.",
    "2": "A porta de entrada do pesquisador: o percurso top-down já publicado, aqui como chave de leitura.",
    "3": "A RC tem léxico próprio e empréstimos do sânscrito, do hebraico e do grego; sem isso, nada se lê.",
    "4": "Como citar, como conferir, como duvidar — o sistema de códigos, os status e a quarentena.",
    "5": "O estado anterior a tudo: a perfeição como protocolo, e a indagação que a desestabiliza.",
    "6": "O evento fundador: um ser projeta, colapsa e cai dentro da própria criação.",
    "7": "Onde tudo acontece: os dois universos, os três níveis de espiritualidade, as lokas e os portais.",
    "8": "As regras do jogo depois da queda — o que nem o criador pode desobedecer.",
    "9": "O personagem central e a sua patologia: o deus que adoeceu e ficou refém da própria obra.",
    "10": "As cocriadoras que mergulharam e a disputa pela herança da obra.",
    "11": "A linhagem que produz a saída: de Mohen So a Jesus, passando por Sophia.",
    "12": "O outro lado do conflito: a rebelião, o exílio e o isolamento da Terra.",
    "13": "A população da criação: raças, anjos, coletivos, logoi e híbridos.",
    "14": "As figuras humanas que a leitura de Ellam reinterpreta.",
    "15": "Parentesco como estrutura: de quem cada um descende e de que lado está.",
    "16": "O enredo no tempo: eras, catástrofes, profecias e missões.",
    "17": "Como a vida chegou aqui e o que foi feito com ela.",
    "18": "De que material o operador humano é feito, segundo a RC.",
    "19": "O que acontece com o operador: mediunidade, transmigração, fenômenos energéticos.",
    "20": "A doutrina e a prática do dia a dia do operador.",
    "21": "A ética de um universo acidentado — e os conceitos que a RC inverte.",
    "22": "Para onde tudo vai: a reintegração, o conserto e o destino final.",
    "23": "Os objetos e as tecnologias que a obra atribui à criação.",
    "24": "A ontologia dos Tratados: o Perfeito, o Imperfeito e o método da Arca.",
    "25": "Se a justiça divina faliu, o que a substitui — o juízo ou o algoritmo.",
    "26": "A ponte com o presente: o que o operador é quando o substrato muda.",
    "27": "As quatro fronteiras: religião, mitologia, ciência e ufologia — e a quarentena entre elas.",
    "28": "A obra vista de fora: recepção, lacunas e o que ainda falta pesquisar.",
    "A": "As figuras fixas: o N0 e os mapas de conexões já publicados.",
    "B": "A linha do tempo em uma página — marcos, não datas.",
    "C": "As genealogias que o pesquisador consulta o tempo todo.",
    "D": "Siglas do corpus e jargão técnico do autor.",
    "E": "Acesso alfabético: o termo leva ao endereço do verbete.",
    "F": "Acesso por código: o RC-### leva ao endereço do verbete.",
    "G": "Acesso por fonte: o livro ou a palestra levam aos verbetes que a citam.",
    "H": "Onde a Base declara não saber — o aparelho crítico da obra.",
    "I": "Como citar, como atualizar, o que mudou entre edições.",
}

# ------------------------------------------------- curadoria (vence a regra)
# verbetes-âncora cuja colocação nao se resolve pela subcategoria da Base
CURADORIA = {
    # o autor e o seu nome cosmico abrem a obra
    "RC-071": "I.1.1", "RC-120": "I.1.1",
    # II.5 — a Espiritualidade Superior
    "RC-204": "II.5.1", "RC-600": "II.5.2", "RC-606": "II.5.3", "RC-603": "II.5.3",
    "RC-601": "II.5.4", "RC-602": "II.5.4",
    # II.6 — a Criação Indevida
    "RC-152": "II.6.1", "RC-310": "II.6.1", "RC-410": "II.6.1",
    "RC-526": "II.6.2", "RC-167": "II.6.4", "RC-040": "II.6.4", "RC-294": "II.6.4",
    "RC-106": "II.7.1", "RC-107": "II.7.1",
    "RC-059": "II.7.2", "RC-060": "II.7.2", "RC-061": "II.7.2",
    "RC-087": "II.7.2", "RC-472": "II.7.2",
    "RC-528": "II.6.3", "RC-196": "II.6.3",
    # II.8 — leis
    "RC-160": "II.8.2", "RC-636": "II.8.2", "RC-559": "II.8.1", "RC-628": "II.8.1",
    "RC-604": "II.8.3", "RC-217": "IV.17.3",
    # III.9 — o Criador
    "RC-001": "III.9.1", "RC-037": "III.9.1", "RC-261": "III.9.1", "RC-284": "III.9.1",
    "RC-331": "III.9.1", "RC-482": "III.9.1", "RC-717": "III.9.2", "RC-638": "III.9.4",
    # III.10 — a Trimurti
    "RC-104": "III.10.1", "RC-135": "III.10.3", "RC-408": "III.10.3",
    "RC-102": "III.10.4", "RC-409": "III.10.4",
    "RC-414": "III.10.5", "RC-413": "III.10.5",
    # III.11 — Sophia e Jesus
    "RC-081": "III.11.1", "RC-282": "III.11.1", "RC-009": "III.11.2", "RC-565": "III.11.2",
    "RC-258": "III.11.2", "RC-072": "III.11.3", "RC-942": "III.11.4",
    # III.12 — rebelião e exílio
    "RC-002": "III.12.1", "RC-078": "III.12.1", "RC-142": "III.12.1", "RC-074": "III.12.2",
    "RC-007": "III.12.3", "RC-039": "III.12.3", "RC-450": "III.12.3",
    "RC-070": "III.12.4", "RC-342": "III.12.4", "RC-295": "III.12.4",
    # IV.17 — antropogênese
    "RC-091": "IV.17.1", "RC-099": "IV.17.1", "RC-148": "IV.17.2", "RC-281": "III.13.5",
    "RC-086": "IV.17.4", "RC-283": "IV.17.4", "RC-118": "IV.17.4", "RC-299": "IV.17.4",
    "RC-242": "IV.17.4",
    # IV.18 / IV.21
    "RC-166": "IV.18.2", "RC-332": "IV.21.2",
    # V.22 — propósitos e destinos
    "RC-003": "V.22.1", "RC-514": "V.22.2", "RC-226": "V.22.3", "RC-612": "V.22.3",
    "RC-163": "V.22.4", "RC-042": "V.22.4",
    # V.23 — escrituras
    "RC-887": "V.23.1", "RC-862": "III.14.3",
}

# ------------------------------------------------- regra por subcategoria
REGRA_SUBCATEGORIA = {
    "8.1 Sânscrito / Hinduísmo": "I.3.1",
    "8.2 Hebraico / Cabala": "I.3.2",
    "8.4 Grego / Latim": "I.3.3",
    "8.5 Outros idiomas / jargão técnico": "I.3.4",
    "2.1 Cosmogonia / Criação": "II.6.1",
    "2.3 Dimensões / Planos de existência": "II.7.1",
    "3.1 Planetas / Sistemas estelares": "II.7.3",
    "3.2 Lokas / Mundos interiores": "II.7.4",
    "3.3 Localidades terrestres": "II.7.5",
    "3.4 Regiões cósmicas / Portais": "II.7.6",
    "2.2 Leis e princípios cósmicos": "II.8.1",
    "1.1 Divindades / Criadores": "III.9.1",
    "1.2 Coletivos criadores": "III.13.1",
    "1.3 Extraterrestres / Raças cósmicas": "III.13.2",
    "1.4 Anjos / Arcanjos / Querubins": "III.13.3",
    "1.5 Decaídos / Exilados / Demônios": "III.12.1",
    "1.6 Figuras humanas (históricas/míticas)": "III.14.4",
    "1.7 Híbridos / Seres de transição": "III.13.4",
    "1.8 Consciências coletivas / Logos": "III.13.5",
    "6.1 Famílias divinas / Celestiais": "III.15.1",
    "6.2 Linhagens humanas": "III.15.2",
    "6.3 Dinastias extraterrestres": "III.15.3",
    "7.1 Guerras / Rebeliões / Conflitos": "III.16.1",
    "7.2 Eras / Épocas / Ciclos": "III.16.2",
    "7.3 Profecias / Anúncios": "III.16.4",
    "7.4 Catástrofes / Dilúvios / Quedas": "III.16.3",
    "7.5 Missões / Expedições / Encontros": "III.16.5",
    "4.1 Processos biológicos / genéticos": "IV.18.3",
    "4.2 Fenômenos espirituais / mediúnicos": "IV.19.1",
    "4.3 Transmigração / Reencarnação": "IV.19.2",
    "4.4 Fenômenos físicos / energéticos": "IV.19.3",
    "2.4 Espiritualidade / Doutrina": "IV.20.1",
    "2.6 Ética / Carma / Compromissos": "IV.21.1",
    "2.5 Propósitos / Destinos": "V.22.1",
    "5.1 Naves / Tecnologia extraterrestre": "V.23.2",
    "5.3 Dispositivos / Instrumentos": "V.23.3",
    "5.4 Escrituras / Objetos documentais": "V.23.1",
}


# ------------------------------------------------- regras globais (todas as areas)
# Aplicadas DEPOIS da curadoria e ANTES da regra fina: resolvem deslocamentos
# evidentes (um "Corpo Budico" classificado como 2.3 na Base e, na verdade,
# material do Volume IV; um "Budismo como Excecao" que e dialogo comparado).
REGRAS_GLOBAIS = [
    (r"^corpo\b|corpo (átmico|búdico|manásico|sutil|mental|daiva|demoníaco)", "IV.18.1"),
    (r"^jesus\b|jesus", "III.11.3"),
    (r"sophia|hochmah", "III.11.2"),
    (r"^javé\b", "III.9.1"),
    (r"vishnu|mavatna|mavátma|adhymavatana", "III.10.3"),
    (r"shiva|savna|adhysavna", "III.10.4"),
    (r"trimurti", "III.10.1"),
    (r"titã|titãs|asura", "III.12.5"),
    (r"judaísmo|cristianismo|católic|protestante|islam|budismo|espiritismo|"
     r"igreja|concílio|niceia|teologia comparada", "V.27.1"),
    (r"^druida|druidas|essêni|sethiano|seita|irmandade", "III.14.3"),
    (r"^ciência pessoal", "IV.20.1"),
    (r"\bciência\b|científic|academia|universidade|método científico|física quântica", "V.27.3"),
    (r"clínic|psiquiatr|terapia|terapêutic|psicanál", "V.27.4"),
]

# ------------------------------------------------- regra fina (palavra-chave)
# Uma subcategoria da Base pode alimentar varias subsecoes. A regra fina e
# aplicada DENTRO da subcategoria, antes do endereco-padrao: a primeira
# expressao que bater no nome do termo vence. E heuristic — revisar a cada
# edicao (o relatorio de densidade no Apêndice B e o instrumento de revisao).
REGRAS_FINAS = {
    "2.2 Leis e princípios cósmicos": [
        (r"consciên|mental|psiquismo|mórfico|holográfic|fatiamento|mente", "II.8.3"),
        (r"entropia|negentropia|pulsaç|vibraç|frequên|algoritmo|geometria|fractal|"
         r"código[- ]fonte|matriz|campo", "II.8.2"),
        (r"carma|teia|simultaneidade|causal|causa|efeito|ressonân|retribuiç|justiça", "II.8.1"),
    ],
    "2.3 Dimensões / Planos de existência": [
        (r"^corpo|vestimenta|casulo|perispírito|envoltório", "IV.18.1"),
        (r"espiritualidade|ereon|perpérion|tempérion|archeon|antérion|danérion|mermérion", "II.7.2"),
        (r"universo|dimensão|plano|antimaterial|material|brahmaloka|bhuloka|erraticidade|"
         r"faixa|zona|circuito", "II.7.1"),
    ],
    "1.1 Divindades / Criadores": [
        (r"buraco[- ]negro", "III.9.2"),
        (r"demência|doença|fase|colapso", "III.9.3"),
        (r"refém|cadáver|ressurreiç", "III.9.4"),
        (r"vishnu|mavatna|adhymavatana", "III.10.3"),
        (r"shiva|savna|adhysavna", "III.10.4"),
        (r"avatar|krishna|hara|keshava|sai baba|emação", "III.10.5"),
        (r"mohen so|phanes|protogonos", "III.11.1"),
        (r"sophia|hochmah|sabedoria|cristo cósmico", "III.11.2"),
        (r"^jesus|jesus", "III.11.3"),
        (r"messias", "III.11.4"),
        (r"trimurti|desconstituiç", "III.10.1"),
    ],
    "1.5 Decaídos / Exilados / Demônios": [
        (r"satã|satanas|mion|monstr", "III.12.2"),
        (r"capela|exilado|revolta|degredo", "III.12.3"),
        (r"quarentena|isolamento|portal|fechamento", "III.12.4"),
        (r"lúcifer|luzbel|rebelião|demo|involu|obsessor", "III.12.1"),
    ],
    "1.6 Figuras humanas (históricas/míticas)": [
        (r"profeta|mensageiro|enviado|instrutor|precursor|avatar|"
         r"hermes trismegisto|vyasa|kashyapa|orunmilá|sai baba|prema sai|"
         r"apolônio|^enoque|melquizedec", "III.14.1"),
        (r"abel|caim|^eva|agar|joão|pedro|maria madalena|paulo|saulo|"
         r"arimatéia|pilatos|caifás|sinédrio|quirino|joctan|faleg|"
         r"testamento|bíblic", "III.14.2"),
        (r"druida|essêni|sethiano|milésios|rishis|raça|povo|ordem|seita|"
         r"irmandade", "III.14.3"),
    ],
    "2.4 Espiritualidade / Doutrina": [
        (r"prática|disciplina|meditaç|oraç|exercício|conduta|treino|vivência", "IV.20.2"),
    ],
    "2.6 Ética / Carma / Compromissos": [
        (r"favor|invers|perdão|compaixão|misericórd|invertido", "IV.21.2"),
    ],
    "2.5 Propósitos / Destinos": [
        (r"tikun|conserto|reparo|restabelecimento|correç", "V.22.2"),
        (r"cidadão|paraíso b|nova espiritualidade|nova dimensão|espécie futura|"
         r"criatura universal", "V.22.3"),
        (r"mente universal|biocosmos|emergente|supraconciência", "V.22.4"),
    ],
    "4.1 Processos biológicos / genéticos": [
        (r"corpo|búdico|manásico|vestimenta|casulo|perispírito|envoltório|"
         r"constituiç", "IV.18.1"),
        (r"mentalma|cérebro|pensamento|psique|emoç|sentimento|vontade", "IV.18.2"),
    ],
    "5.4 Escrituras / Objetos documentais": [
        (r"nag hammadi|essênio|bíblia|evangelho|apócrifo|manuscrito|pergaminho|"
         r"torá|cabala textual|livro", "V.23.1"),
    ],
    "4.4 Fenômenos físicos / energéticos": [
        (r"psíquic|bolha|delírio|egrég|emoç|sentiment|mente coletiva|"
         r"choque de realidade|percepç", "IV.19.1"),
        (r"bondade|virtude|código filosófico|caráter|conduta|amor ao próximo|"
         r"solidaried", "IV.21.1"),
        (r"tempo|espaço|gravidade|luz|energia|eletromagné|partícula|quântic|"
         r"vibraç|frequên|plasma", "IV.19.3"),
    ],
}

# ------------------------------------------------- notas editoriais por subseção
# Advertências honestas sobre os limites do mapeamento automático.
NOTAS = {
    "II.8.1": "Subseção agregadora: 2.2 (Leis e princípios) é a subcategoria mais densa "
              "da Base (73 códigos). A separação entre leis de causa, de estrutura e de "
              "consciência é parcialmente heurística — recuradoria recomendada.",
    "IV.19.3": "Subseção agregadora: 4.4 é a subcategoria mais heterogênea do acervo — "
               "mistura fenômenos físicos, psíquicos e morais. A triagem por palavra-chave "
               "é parcial; recuradoria recomendada na próxima edição.",
    "V.22.1": "Subseção agregadora: 2.5 reúne propósitos e destinos. Os temas específicos "
              "(Tikun, Cidadão Cósmico, Mente Universal) foram deslocados para V.22.2–V.22.4.",
    "III.14.4": "Subseção de depósito das figuras humanas: recebe o que não é enviado "
                "(III.14.1), bíblico (III.14.2) nem coletivo (III.14.3).",
    "III.12.1": "Nomes próprios de demos e decaídos não rotulados como titãs, satânicos, "
                "capelinos ou de quarentena permanecem aqui.",
}

# ------------------------------------------------------------------ utilitários
def chave_ordem(nome):
    """Ordenação alfabética ignorando acentos e caixa."""
    n = unicodedata.normalize("NFKD", nome)
    n = "".join(c for c in n if not unicodedata.combining(c))
    return n.casefold()


STATUS_LEGENDA = {
    "candidato": "⚪", "provisorio": "🟡", "provisório": "🟡",
    "em analise": "🟠", "em análise": "🟠", "verificado": "🟢",
}


def selo(status):
    return STATUS_LEGENDA.get(status.strip().casefold(), "⚪")


# ------------------------------------------------------------------ mapeamento
def construir_indice():
    """Endereços válidos e fichas por endereço. Falha se algo não fechar."""
    enderecos = {}
    for vol, _, secoes in VOLUMES:
        for num_sec, _, subs in secoes:
            for num_sub, titulo_sub, _, _tipo in subs:
                enderecos[f"{vol}.{num_sub}"] = titulo_sub
    # subcategorias declaradas como âncora de uma subseção
    ancora_sub = {}
    for vol, _, secoes in VOLUMES:
        for num_sec, _, subs in secoes:
            for num_sub, _, subs_cat, _tipo in subs:
                for cat in subs_cat:
                    if cat in ancora_sub:
                        raise SystemExit(f"subcategoria ancora duplicada: {cat}")
                    ancora_sub[cat] = f"{vol}.{num_sub}"

    fichas = [t for t in BASE.TERMOS if t[7] is True]
    distribuido = defaultdict(list)
    def regra_global(nome):
        """Regras que valem para qualquer area (deslocamentos evidentes)."""
        for padrao, end in REGRAS_GLOBAIS:
            if re.search(padrao, nome, re.IGNORECASE):
                return end
        return None

    def endereco_fino(nome, subcat):
        """Regra fina por palavra-chave dentro da subcategoria (heurística)."""
        for padrao, end in REGRAS_FINAS.get(subcat, []):
            if re.search(padrao, nome, re.IGNORECASE):
                return end
        return None

    for termo in fichas:
        cod, nome, area, subcat, status, fontes, rels, _f = termo
        # precedência: curadoria > regras globais > regra fina > âncora > padrão
        end = (CURADORIA.get(cod)
               or regra_global(nome)
               or endereco_fino(nome, subcat)
               or ancora_sub.get(subcat)
               or REGRA_SUBCATEGORIA.get(subcat))
        if end is None:
            raise SystemExit(f"SEM ENDERECO: {cod} {nome} ({area} / {subcat})")
        if end not in enderecos:
            raise SystemExit(f"ENDERECO INEXISTENTE: {end} para {cod} {nome}")
        distribuido[end].append(termo)

    # a curadoria so pode apontar codigo existente (senao e erro de digitacao)
    orfa = [c for c in CURADORIA if c not in {t[0] for t in BASE.TERMOS}]
    if orfa:
        raise SystemExit(f"CURADORIA APONTA CODIGO INEXISTENTE: {orfa}")

    # ancoras ESTRUTURAIS sem ficha materializada — achado editorial, nao erro:
    # sao os verbetes que a Enciclopedia exige e a Base ainda nao tem.
    cod_ficha = {t[0] for t in fichas}
    mapa = {t[0]: t for t in BASE.TERMOS}
    ancoras_sem_ficha = [
        (cod, mapa[cod][1], mapa[cod][2], mapa[cod][3], CURADORIA[cod])
        for cod in sorted(CURADORIA) if cod not in cod_ficha
    ]

    return enderecos, distribuido, fichas, ancoras_sem_ficha


# ------------------------------------------------------------------ emissão
def detectar_duplicatas():
    """Nomes repetidos em codigos diferentes (desduplicacao pendente)."""
    visto = defaultdict(list)
    for t in BASE.TERMOS:
        k = re.sub(r"[^a-z0-9 ]", "", chave_ordem(t[1])).strip()
        if k:
            visto[k].append((t[0], t[7], t[1]))
    return [(itens[0][2], [(c, f) for c, f, _n in itens])
            for _k, itens in sorted(visto.items()) if len(itens) > 1]


def gerar_md(enderecos, distribuido, fichas, ancoras_sem_ficha, duplicatas):
    total_fichas = len(fichas)
    sem_ficha = [t for t in BASE.TERMOS if t[7] is not True]
    L = []
    A = L.append

    A(f"# ÍNDICE — Enciclopédia de Referência das Revelações Cósmicas · ed. {EDICAO}")
    A("")
    A("> **Obra de referência** (consulta por verbete) distinta do **material didático** ")
    A("> (`pedagogico/top-down/`). Este documento é o **sumário analítico em 3 níveis** ")
    A("> (volume → seção → subseção) com o **mapeamento das fichas da Base** por endereço ")
    A("> estável `V.SEÇÃO.SUBSEÇÃO`. Nenhum verbete está redigido aqui — este é o contrato ")
    A("> editorial da obra.")
    A("")
    A(f"- **Edição:** {EDICAO} · **Data de fechamento:** {DATA}")
    A(f"- **Base de referência:** {len(BASE.TERMOS)} termos · {total_fichas} fichas · "
      f"{len(BASE.RELACOES)} relações")
    A("- **Fonte do censo:** `ferramentas/dados_termos.py` (registro-mestre) — nunca `ls termos/`")
    A(f"- **Gerado por:** `ferramentas/build_indice_enciclopedia.py` (não editar à mão)")
    A("- **Natureza:** obra de referência sobre a **leitura de Jan Val Ellam**. Conteúdo ")
    A("  teológico, cosmológico, ufológico e clínico é **quarentenado**: não é consenso ")
    A("  acadêmico nem religioso.")
    A("")
    A("## Como este índice foi construído")
    A("")
    A("1. **Precedência do mapeamento (5 níveis):** (a) **curadoria explícita** dos ")
    A("   verbetes-âncora; (b) **regras globais** — deslocamentos evidentes, como um ")
    A("   «Corpo Búdico» que a Base classifica em 2.3 mas é material do Volume IV; ")
    A("   (c) **regra fina por palavra-chave dentro da subcategoria**; (d) **âncora ")
    A("   declarada** da subseção; (e) **padrão por subcategoria** da Base.")
    A("2. **Heurística declarada:** os níveis (b) e (c) são heurísticos, não infalíveis. ")
    A("   Onde eles não resolvem, a subseção fica **agregadora** — e isso está advertido ")
    A("   no corpo do índice e reaparece no Apêndice B.")
    A("3. **Toda ficha recebe exatamente um endereço.** O script falha se sobrar ficha sem ")
    A("   endereço, se um endereço não existir ou se a curadoria apontar código inexistente.")
    A("4. **A classificação da Base é preservada.** Cada verbete carrega também a sua ")
    A("   área/subárea original (8 áreas × 34 subáreas) — a taxonomia temática da enciclopédia ")
    A("   não substitui o censo de código.")
    A("5. **Seções de redação** (marcadas como tais quando vazias) não têm fichas próprias ")
    A("   na Base: serão escritas a partir das fontes, dos tratados e das apostilas. Estão no ")
    A("   índice porque são parte da obra — a ausência de âncora é informação, não defeito.")
    A("6. **Achados automáticos:** os Apêndices **D** (âncoras estruturais sem ficha) e **E** ")
    A("   (duplicatas) são subprodutos do confronto entre a estrutura da obra e a Base. ")
    A("   Nada foi alterado na Base — as duas decisões dependem de despacho do Curador.")
    A("")
    A("## Legenda de status")
    A("")
    A("| Selo | Status | Significado |")
    A("|---|---|---|")
    A("| ⚪ | candidato | termo registrado, sem fonte publicada confirmada |")
    A("| 🟡 | provisório | fonte publicada, aguardando revisão |")
    A("| 🟠 | em análise | em revisão cruzada com as obras primárias |")
    A("| 🟢 | verificado | revisado e estável |")
    A("")

    # ----------------Sumário geral
    A("## Sumário geral")
    A("")
    A("| Vol. | Título | Seções | Verbetes (fichas) |")
    A("|---|---|---|---|")
    for vol, titulo_v, secoes in VOLUMES:
        n = sum(len(distribuido.get(f"{vol}.{num_sub}", []))
                for _ns, _ts, subs in secoes for num_sub, *_ in subs)
        A(f"| **{vol}** | {titulo_v} | {len(secoes)} | {n} |")
    A(f"| | **TOTAL** | {sum(len(s) for _v, _t, s in VOLUMES)} | **{total_fichas}** |")
    A("")

    # ----------------Corpo
    for vol, titulo_v, secoes in VOLUMES:
        n_vol = sum(len(distribuido.get(f"{vol}.{num_sub}", []))
                    for _ns, _ts, subs in secoes for num_sub, *_ in subs)
        A("---")
        A("")
        A(f"# VOLUME {vol} — {titulo_v}")
        A("")
        A(f"*Verbetes ancorados neste volume: **{n_vol}***")
        A("")
        for num_sec, titulo_s, subs in secoes:
            n_sec = sum(len(distribuido.get(f"{vol}.{num_sub}", [])) for num_sub, *_ in subs)
            A(f"## {vol}.{num_sec} — {titulo_s}")
            A("")
            if num_sec in EMENTAS:
                A(f"*{EMENTAS[num_sec]}*")
                A("")
            A(f"**Verbetes:** {n_sec}")
            A("")
            for num_sub, titulo_sub, subs_cat, tipo in subs:
                end = f"{vol}.{num_sub}"
                entradas = sorted(distribuido.get(end, []), key=lambda t: chave_ordem(t[1]))
                if entradas:
                    marcador = ""
                elif tipo == "base":
                    marcador = " *(a preencher — nenhuma ficha ancorada)*"
                else:
                    marcador = " *(seção de redação — sem fichas próprias na Base)*"
                A(f"### {end} — {titulo_sub}{marcador}")
                A("")
                if end in NOTAS:
                    A(f"> {NOTAS[end]}")
                    A("")
                if entradas:
                    for t in entradas:
                        cod, nome, area, subcat, status, fontes, rels, _f = t
                        nfontes = len(fontes)
                        A(f"- **{nome}** — `{cod}` {selo(status)} · {area} › {subcat} · {nfontes} fonte(s)")
                else:
                    if tipo == "base":
                        A("- *(nenhuma ficha ancorada — subseção a preencher ou alimentada por outra seção)*")
                    else:
                        A("- *(seção de redação editorial)*")
                A("")

    # ----------------Apêndices
    A("---")
    A("")
    A("# APÊNDICES")
    A("")
    A(f"## Apêndice A — Índice alfabético remissivo ({total_fichas} verbetes)")
    A("")
    A("| Termo | Código | Endereço | Selo |")
    A("|---|---|---|---|")
    todas = []
    for end, termos in distribuido.items():
        for t in termos:
            todas.append((chave_ordem(t[1]), t[1], t[0], end, selo(t[4])))
    for _k, nome, cod, end, s in sorted(todas):
        A(f"| {nome} | `{cod}` | {end} | {s} |")
    A("")

    A(f"## Apêndice B — Densidade por subseção (onde o acervo é mais fino)")
    A("")
    A("Subseções com **6 fichas ou menos** — lacunas declaradas da obra.")
    A("")
    A("| Endereço | Subseção | Fichas | Tipo |")
    A("|---|---|---|---|")
    finas = []
    for vol, _, secoes in VOLUMES:
        for _ns, _ts, subs in secoes:
            for num_sub, titulo_sub, _cats, tipo in subs:
                end = f"{vol}.{num_sub}"
                n = len(distribuido.get(end, []))
                if tipo == "base" and n <= 6:
                    finas.append((n, end, titulo_sub))
    for n, end, titulo_sub in sorted(finas):
        A(f"| {end} | {titulo_sub} | {n} | {'lacuna' if n <= 2 else 'baixa densidade'} |")
    A("")

    A(f"## Apêndice D — Âncoras estruturais SEM ficha ({len(ancoras_sem_ficha)}) — materialização prioritária")
    A("")
    A("Achado editorial deste índice: são códigos **exigidos pela estrutura da Enciclopédia** ")
    A("(foram escolhidos como verbete-âncora de uma subseção) que a Base ainda **não materializou** ")
    A("como ficha. Não são erro: são a lista de prioridades de materialização da obra. ")
    A("Nenhum deles pôde ser distribuído como verbete nesta edição.")
    A("")
    A("| Código | Termo | Área › Subárea | Endereço previsto |")
    A("|---|---|---|---|")
    for cod, nome, area, subcat, end in ancoras_sem_ficha:
        A(f"| `{cod}` | **{nome}** | {area} › {subcat} | {end} |")
    A("")

    A(f"## Apêndice C — Termos sem ficha ({len(sem_ficha)} códigos)")
    A("")
    A("Códigos existentes no registro-mestre **sem ficha materializada**. São candidatos a ")
    A("verbete: constam do censo, mas ainda não têm entrada de referência.")
    A("")
    A("| Código | Termo | Área › Subárea | Selo |")
    A("|---|---|---|---|")
    for t in sorted(sem_ficha, key=lambda x: chave_ordem(x[1])):
        cod, nome, area, subcat, status, _f, _r, _fi = t
        A(f"| `{cod}` | {nome} | {area} › {subcat} | {selo(status)} |")
    A("")
    A(f"## Apêndice E — Duplicatas detectadas ({len(duplicatas)} nomes repetidos)")
    A("")
    A("Detecção automática: nomes idênticos (desconsiderando caixa, acentos e ")
    A("pontuação) em códigos diferentes. São **pendências de desduplicação da Base** — ")
    A("o precedente é o merge RC-941 → RC-193 (F044, Anel C). **Nenhuma alteração foi ")
    A("feita aqui**: a decisão é do Curador e depende de despacho.")
    A("")
    if duplicatas:
        A("| Nome | Códigos | Fichas | Situação |")
        A("|---|---|---|---|")
        for nome, itens in duplicatas:
            cods = " · ".join(f"`{c}`" for c, _f in itens)
            nf = sum(1 for _c, f in itens if f)
            sit = ("duplicata de fichas — merge a avaliar" if nf >= 2
                   else "código sem ficha — alias a avaliar")
            A(f"| {nome} | {cods} | {nf}/{len(itens)} | {sit} |")
    else:
        A("- *(nenhuma duplicata detectada)*")
    A("")

    A("---")
    A("")
    A(f"*Fim do índice — Enciclopédia de Referência das Revelações Cósmicas, edição {EDICAO} ")
    A(f"(fechada em {DATA}). Base: {len(BASE.TERMOS)} termos · {total_fichas} fichas · "
      f"{len(BASE.RELACOES)} relações. Síntese de leitura: nada em `termos/`, `relacoes/` ou "
      f"`ferramentas/dados_termos.py` foi alterado.*")
    A("")
    return "\n".join(L)


def main():
    enderecos, distribuido, fichas, ancoras_sem_ficha = construir_indice()
    # validações finais
    mapeados = sum(len(v) for v in distribuido.values())
    assert mapeados == len(fichas), f"fichas mapeadas {mapeados} != {len(fichas)}"
    usados = set()
    for end in distribuido:
        usados.update(re.findall(r"RC-\d{3}", end))
    vazios_extras = [e for e in enderecos if e not in distribuido]
    duplicatas = detectar_duplicatas()
    md = gerar_md(enderecos, distribuido, fichas, ancoras_sem_ficha, duplicatas)
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"fichas distribuidas : {mapeados} em {len(distribuido)} subsecoes")
    print(f"subsecoes vazias    : {len(vazios_extras)} (redacao ou a preencher)")
    print(f"ancoras sem ficha   : {len(ancoras_sem_ficha)} (materializacao prioritaria)")
    print("OK ->", os.path.relpath(SAIDA, RAIZ))


if __name__ == "__main__":
    main()
