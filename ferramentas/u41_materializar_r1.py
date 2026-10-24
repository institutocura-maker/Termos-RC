#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: REGISTRO-HISTÓRICO DA U41 (13/09/2026) — rota R1 do dossiê do gap.
"""Materialização das 8 fichas «suspenso-B» do HOLD — U41 (13/09/2026).

Despacho do Curador (13/09/2026): entre as rotas R1–R4 do dossiê
`diagnostico/CENSO-GAP-FICHAS-2026-09-13.md`, abrir pela **R1 · Piloto dos 8
suspenso-B** — os 25 códigos chancelados-e-suspensos das levas P7m/n/o que caem
na família B (prosa citável na fonte declarada).

Regra de ouro herdada da U30 + pacto:
  · o motor NÃO inventa conteúdo — a Definição Sintética é síntese curatorial
    do que a fonte sustém; o que vai entre «» é citação;
  · citação só **verbatim intra-linha**, conferida byte a byte contra o
    `original.txt` (nada de juntar linhas fraturadas pelo hard-wrap);
  · frontmatter SEMPRE regerado por `motor.fm_toml` (nunca à mão) — T15;
  · ficha nasce com «Materialização (não é criação)» + Escopo e evidência +
    tabela Termos Relacionados = espelho t[6] ∪ arestas (T14);
  · `RELACOES` blindado: 0 arestas abertas, fechadas ou reetiquetadas.

Uso
    python3 ferramentas/u41_materializar_r1.py            # executa (escreve)
    python3 ferramentas/u41_materializar_r1.py --dry      # só confere as citações

Saída: 8 fichas em `termos/` + cadastro virado (`ficha=False→True`,
status `provisório`→`verificado` = V chancelado aplicado).
"""
from __future__ import annotations

import io
import os
import re
import sys
from pathlib import Path

from caminhos_acervo import caminho_atual

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))

import motor as _m                                            # noqa: E402
import dados_termos as _d                                     # noqa: E402

HOJE = "2026-09-13"
CADASTRO = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
LIVROS = caminho_atual("fonte.livros")


def livro_concluido(diretorio: str) -> str:
    """Caminho físico da obra, resolvido pelo mapa central de acervo."""
    return os.fspath(LIVROS / "CONCLUIDOS" / diretorio / "original.txt")


# ────────────────────────────────────────────────────────── corpus e localizadores
CORPUS = {
    "B003": livro_concluido("B003_reintegracao_cosmica"),
    "B006": livro_concluido("B006_nos_bastidores_da_luz_i"),
    "B021": livro_concluido("B021_tempos_dificeis_no_olimpo"),
    "B024": livro_concluido("B024_epopeia_agentes_da_vida_universal"),
    "B026": livro_concluido("B026_carma_e_compromisso"),
    "B031": livro_concluido("B031_paineis_emergentes_da_revelacao_cosmica"),
    "B060": livro_concluido("B060_personagens_e_terminologias"),
    "B089": livro_concluido("B089_pandora_3_anunnaki_disputa_genetica_pandora"),
    "P2020-04-04": "ciclos/P2020-04-04/original.txt",
    "P2023-05-21": "fontes/apostilas/2023-05-21_a_hebdomada_de_apolo_o_ultraje_humano/original.txt",
    "P2024-11-09": "fontes/apostilas/2024-11-09_abismo_consciencia_cosmica/original.txt",
}
_CACHE: dict[str, list[str]] = {}


def caminho_corpus(sigla: str) -> Path:
    """Resolve entradas históricas relativas e fontes de livro mapeadas."""
    caminho = Path(CORPUS[sigla])
    return caminho if caminho.is_absolute() else Path(RAIZ) / caminho


def linhas(sigla: str) -> list[str]:
    if sigla not in _CACHE:
        with caminho_corpus(sigla).open(encoding="utf-8", errors="replace") as fh:
            _CACHE[sigla] = fh.read().split("\n")
    return _CACHE[sigla]


def pagina(sigla: str, n: int) -> str:
    """Página impressa mais próxima (marcador `===== [PÁGINA n] =====` do STT/PDF)."""
    L = linhas(sigla)
    for i in range(n - 1, -1, -1):
        m = re.match(r"\s*=+\s*\[PÁGINA (\d+)\]\s*=+\s*$", L[i])
        if m:
            return "p. " + m.group(1)
    return "—"


def conferir(sigla: str, n: int, trechos: list[str]) -> None:
    """Portão B da casa: todo trecho entre «» tem de existir byte a byte NA LINHA."""
    L = linhas(sigla)
    assert 1 <= n <= len(L), f"{sigla}: linha {n} fora do arquivo ({len(L)} linhas)"
    alvo = L[n - 1]
    for t in trechos:
        assert t in alvo, (f"{sigla} L{n}: trecho NÃO confere byte a byte\n"
                           f"  trecho : {t!r}\n  linha  : {alvo!r}")


# ─────────────────────────────────────────────────────────────── as 8 fichas (U41)
# `cit`: (sigla, linha, [trechos verbatim intra-linha], nota de ancoragem)
# `obs`: observações livres da ficha (a nota de hard-wrap é acrescentada a todas)
FICHAS = [
  dict(
    cod="RC-027", slug="astreia",
    definicao=(
      "Personagem da mitologia grega relida pelas Revelações Cósmicas como identidade cósmica: "
      "filha de Zeus e Têmis, deusa virgem da Justiça (juntamente com a mãe), da Inocência e da "
      "Pureza, que pregava a sabedoria e ensinava aos humanos atividades caseiras — caçar, plantar "
      "(B031, glossário). Na leitura da RC, Astréia era um dos «Seres dos Portais»: antes de renascer "
      "como demo no universo paralelo, foi **Val Bon** (RC-116), biodemo do Sistema de Capela que "
      "habitava o nosso universo e, após falecer no planeta Terra, tornou-se um dos 9 Val dos Corpos "
      "Perdidos (ou Dimensionados) de Val-Ha. A fonte oral a emparelha com Despina (RC-051) entre as "
      "figuras que passaram a criticar a gestão de Zeus."),
    cit=[
      ("B031", 3156, ["Astréia: Na Mitologia Grega é filha de Zeus e Têmis."],
       "glossário, verbete «Astréia» — sentença completa que coube inteira na linha"),
      ("P2023-05-21", 22, ["Então essa figura chamada astreia, ela tinha um padrão de lucidez demo notável."],
       "palestra (STT) — sentença completa; grafia degradada «astreia» mantida como na fonte"),
    ],
    obs=[
      "O lanço do glossário que dá a identidade cósmica («Seres dos Portais» → Val Bon → um dos 9 Val) "
      "ocupa as linhas 3159–3163 de B031 e está fraturado pelo hard-wrap em cinco fragmentos — nenhum "
      "deles é sentença completa intra-linha; por isso a Citações-chave fixa o verbete e a definição "
      "sintética o declara como dado da fonte (reconferência após o refinamento R2).",
    ],
  ),
  dict(
    cod="RC-030", slug="atlantes",
    definicao=(
      "Os «lendários Atlantes» do Império Atlante: segundo B031, eram, na verdade, **biodemos rebeldes "
      "clonados** — depois de chegarem à Terra, uma parte dos biodemos exilados originais, no intuito de "
      "aumentar o contingente e criar um «exército» de defesa contra um possível ataque, começou a clonar-se "
      "(eram assexuados, e a clonagem era a sua única forma de reprodução/multiplicação). A entrada é distinta "
      "de «Atlans» (uma das 40 bases luciferianas do Império Atlante) e articula-se com Atlan (RC-028) e "
      "Atlântida / Terra Atlantis (RC-010)."),
    cit=[
      ("B031", 3177, ["Atlantes: Os lendários Atlantes, do Império Atlante, eram, na"],
       "glossário, verbete «Atlantes» — início da sentença (continua em L3178)"),
      ("B031", 3178, ["verdade, biodemos rebeldes clonados."],
       "mesma sentença, fraturada pelo hard-wrap — fecho intra-linha"),
      ("B031", 3182, ["a clonagem era a sua única forma de reprodução/multiplicação"],
       "fecho da sentença sobre a clonagem (iniciada em L3181; na fonte o fecho é «…multiplicação).»)"),
    ],
    obs=[
      "As três citações são fragmentos de duas sentenças partidas pelo hard-wrap da edição digital: "
      "cada fragmento é verbatim intra-linha, mas nenhuma das duas sentenças cabe inteira numa linha "
      "de B031 (maior linha do arquivo = 92 chars).",
    ],
  ),
  dict(
    cod="RC-050", slug="demonios",
    definicao=(
      "Nas Revelações Cósmicas, «demônio» (ou **demo**, do grego *daemon*) não é o «diabo» das igrejas: é a "
      "denominação dos seres extrafísicos (RC-097) que habitam o universo paralelo antimaterial, que não "
      "pertencem à espécie humana e detêm um corpo etéreo metamorfoseável conforme as circunstâncias — podiam "
      "ser sábios, elevados, cruéis ou estúpidos, «tinha de tudo entre os mesmos». B031 atribui a deturpação "
      "do conceito às igrejas Católica e Protestante (que igualaram «demônio» a «diabo») e recorda que, até o "
      "século II a.C., era natural a propensão a considerar deuses, demônios e anjos bons e maus. Os demos "
      "formam, com os anjos clones (RC-019), as duas classes dos seres extrafísicos, havendo diversas classes "
      "e famílias entre eles; vários deles são os «Seres dos Portais» das mitologias (RC-241)."),
    cit=[
      ("B031", 266, ["“demônio” era apenas a denominação para aqueles seres"],
       "nota da autora (p. 14) — início da sentença (continua em L267)"),
      ("B031", 267, ["dementes que se metamorfoseavam."],
       "fecho intra-linha da mesma sentença"),
      ("B031", 674, ["Também há diversas classes e famílias entre os anjos clones e os demos."],
       "seção «Seres Extrafísicos» — sentença completa intra-linha"),
    ],
    obs=[
      "A entrada de glossário «Demônios» (L3316–L3335), que narra a deturpação do conceito pelas igrejas, "
      "está integralmente fraturada pelo hard-wrap — nem o início nem o fecho couberam numa linha; a "
      "Citações-chave fixa por isso a nota de abertura da obra (p. 14), que diz o mesmo em duas linhas.",
    ],
  ),
  dict(
    cod="RC-051", slug="despina",
    definicao=(
      "Na mitologia grega, deusa filha de Poseidon e Deméter, irmã gêmea do equino Árion; abandonada pela mãe "
      "ao nascer — Deméter estava ocupada em achar Perséfone, raptada por Hades —, nem nome recebeu, e foi "
      "adotada pelo titã Anitos, que lho escolheu. Era uma deusa das sombras relacionada a fenômenos invernais "
      "como as geadas: cuidava da natureza enquanto a irmã estava no mundo dos mortos e era tão temida que a "
      "chamavam apenas de «senhora». Na Revelação Cósmica, Despina é o renascimento de **Val Anen** (RC-112), "
      "biodemo da Família Val falecido na primeira experiência dos Val fora das naves, há 599 mil anos, cuja "
      "consciência foi migrada para a família de demos dos «Seres dos Portais» (Deuses da Mitologia Grega)."),
    cit=[
      ("B031", 3336, ["Despina: Na mitologia grega, era uma deusa, filha"],
       "glossário, verbete «Despina» — início da sentença (continua em L3337)"),
      ("B031", 3337, ["de Poseidon e Deméter."], "fecho intra-linha da mesma sentença"),
      ("B031", 3342, ["uma deusa das sombras relacionada a fenômenos invernais como as geadas."],
       "mesmo verbete — fecho intra-linha da sentença sobre o domínio da deusa"),
      ("B031", 3908, ["Mitologia Grega) e renasceu como Despina."],
       "glossário, verbete «Val Anen» — fecho intra-linha da sentença que dá a identidade cósmica"),
    ],
    obs=[
      "A Citações-chave reúne quatro fragmentos de três sentenças partidas pelo hard-wrap (B031, maior "
      "linha = 92 chars); a sentença da identidade cósmica começa em L3907 («migrada para a família de "
      "demos dos “Seres dos Portais” (Deuses da»).",
    ],
  ),
  dict(
    cod="RC-090", slug="projeto-planeta-azul",
    definicao=(
      "A empreitada cósmica que elegeu a Terra como portal: há cerca de 3 milhões de anos, reunidos em conclave "
      "no planeta Orbum (Sistema de Capela, sede da governadoria de Sophia), seres dos Sistemas de Vega, "
      "Tau Ceti, Próxima Centauri, Epsilon Eridani e muitos outros escolheram o planeta para ser «um importante "
      "portal cósmico como base de saída da nossa galáxia para outras» — o primeiro da história universal com "
      "capacidade de religar este universo ao universo paralelo. Liderado por Sophia, o projeto teve início com "
      "a chegada das primeiras levas de seres extraterrestres, que não se adaptaram à natureza terrestre; há "
      "cerca de 1 milhão e 950 mil anos, quatro grupos distintos com 40 mil humanoides (de 60 cm a 2 m de "
      "altura, pele acinzentada) foram trazidos; há cerca de 800 mil anos começaram a chegar seres de outros "
      "planetas, que formaram colônias comunitárias e se mostraram aptos a edificar o portal intergaláctico e "
      "interuniversal. Na trilogia «Queda e Ascensão Espiritual» (B003/B026) os mesmos eventos são narrados em "
      "primeira mão pelo autor."),
    cit=[
      ("B031", 3692, ["Projeto Planeta Azul: Foi a empreitada que começou a ocorrer na"],
       "glossário, verbete «Projeto Planeta Azul» — início da sentença (continua em L3693)"),
      ("B031", 1846, ["religar este universo ao universo paralelo."],
       "seção «O PROJETO PLANETA AZUL» — fecho intra-linha da sentença sobre a capacidade do portal"),
      ("B031", 1865, ["prontos para realizar o Projeto Planeta Azul."],
       "mesma seção — fecho intra-linha da sentença sobre os cidadãos cósmicos imigrados"),
      ("B003", 477, ["direta ou indiretamente, com o projeto planeta azul."],
       "abertura da trilogia — fecho intra-linha da sentença sobre os seres envolvidos"),
    ],
    obs=[
      "B026 comparece no cadastro como fonte e a busca de 13/09/2026 localizou lá ocorrências de «planeta "
      "azul» (L4487: «A única e última opção para os rebelados era o planeta azul .» — o reduto final da "
      "rebelião, não o conclave de Orbum); não foi usada como citação-chave para não confundir os dois "
      "eventos. O trecho fica declarado aqui, com a grafia do STT preservada (espaço antes do ponto).",
    ],
  ),
  dict(
    cod="RC-097", slug="seres-extrafisicos",
    definicao=(
      "Os habitantes do universo paralelo (antimaterial): não são físicos — e muito menos biológicos — como a "
      "nossa ótica humana entende, têm corpos «eletromagnetizados e plasmáticos» e vidas que duram bilhões de "
      "anos. Classificam-se em dois tipos: os anjos clones (RC-019) e os demos («demônios» ou «daemon», RC-049). "
      "Enquanto os portais entre os dois universos ainda estavam abertos, muitos transitavam entre lá e cá, e "
      "alguns vieram para o nosso universo com suas tecnologias e naves pelos «buracos de minhoca». Entre os "
      "seres extrafísicos estão o próprio Brahma/Javé (o Criador), bem como Vishnu e Shiva; entre os anjos "
      "clones, as famílias Aya e Aye (RC-031 — os Arcanjos Gabriel, Rafael, Miguel da tradição judaico-cristã); "
      "entre os demos, os seres mitológicos ou «Seres dos Portais» (RC-241). A cultura humana passou a conhecê-los "
      "como «deuses» ou seres lendários, quando na mesma medida são seres extrafísicos que habitam realidades "
      "paralelas à nossa; a maioria ainda vive no universo paralelo e já não transita para cá, devido ao "
      "fechamento dos portais e aos efeitos da entropia."),
    cit=[
      ("B031", 664, ["Os seres extrafísicos e antimateriais são os que habitam o universo"],
       "seção «Seres Extrafísicos» — início da sentença (continua em L665)"),
      ("B031", 665, ["paralelo."], "fecho intra-linha da mesma sentença"),
      ("B031", 666, ["Seus corpos são “eletromagnetizados e plasmáticos” e"],
       "mesma seção — início da sentença sobre o corpo (continua em L667)"),
      ("B031", 667, ["suas vidas duram bilhões de anos."], "fecho intra-linha da mesma sentença"),
      ("B031", 673, ["estão o próprio Brahma/Javé (o Criador), bem como Vishnu e Shiva."],
       "mesma seção — fecho intra-linha da sentença iniciada em L672 («Entre os seres extrafísicos»)"),
    ],
    obs=[
      "Cinco fragmentos de três sentenças fraturadas pelo hard-wrap: a seção é um bloco corrido de "
      "L663 a L686 e nenhuma das suas sentenças cabe inteira numa linha de B031.",
    ],
  ),
  dict(
    cod="RC-100", slug="seres-espirituais",
    definicao=(
      "Categoria que B031 reparte em dois regimes. De um lado, os seres espirituais que existem dentro dos "
      "níveis da Espiritualidade Superior (RC-059), Operacional (RC-060) e Laboratorial, mais relacionados às "
      "Divindades ou Divindades Co-Criadoras e mais próximos ao Círculo da Perfeição ou ao Deus Incognoscível, "
      "e que estariam fora da «blindagem» da Criação de Brahma. De outro, os seres espirituais que habitam o "
      "nosso universo material — os quais «nada mais são que os espíritos desencarnados» em erraticidade, "
      "ligados a cada orbe ou planeta entre as bilhões de galáxias, ainda ligados a karmas (em sua grande "
      "maioria) e necessitados de reencarnar. Há ainda os que, já sem karmas, poderiam estar na Espiritualidade "
      "Superior mas permanecem aqui em missões voluntárias de auxílio aos irmãos desencarnados e encarnados "
      "menos favorecidos. A seção «Espíritos» do mesmo glossário trata do subconjunto em erraticidade."),
    cit=[
      ("B031", 3798, ["Seres Espirituais: Existem seres espirituais dentro e fora do universo"],
       "glossário, verbete «Seres Espirituais» — início da sentença (continua em L3799)"),
      ("B031", 640, ["São os seres espirituais que existem dentro dos níveis da"],
       "seção «Seres Espirituais» — início da sentença (continua em L641)"),
      ("B031", 641, ["Espiritualidade Superior, Operacional e Laboratorial, e que estariam mais"],
       "fecho parcial intra-linha da mesma sentença (continua em L642–644)"),
      ("B031", 3803, ["nada mais são que os espíritos desencarnados, que"],
       "glossário — início da sentença de identificação (continua em L3804–3805)"),
      ("B031", 3805, ["galáxias desse universo."], "fecho intra-linha da mesma sentença"),
    ],
    obs=[
      "Cinco fragmentos de três sentenças fraturadas pelo hard-wrap; a sentença da erraticidade vive em "
      "L3803–L3805 e a dos níveis da Espiritualidade, em L640–L644.",
      "B024 e B006 constam do cadastro como fontes e a busca de 13/09/2026 localizou nelas ocorrências do "
      "sintagma, mas sempre em outro emprego («irmãos espirituais», «guias espirituais», «obras "
      "espirituais») — nenhuma delas define o termo, e por isso não foram usadas como citação-chave.",
    ],
  ),
  dict(
    cod="RC-304", slug="deucaliao",
    definicao=(
      "Figura da mitologia grega relida pelas Revelações Cósmicas como produto de manipulação genética demo: "
      "filho de Prometeu (RC-301) com Pirra (RC-303) — ela própria gerada da mistura dos CFDs de Kalil Kadmon "
      "com Epimeteu, um «produto de manipulação genética demo» —, uniu-se a Pirra e com ela gerou a "
      "descendência de que, segundo a fonte oral, saíram os povos Eóleo, Aqueu, Dório e Jônico, fundadores dos "
      "povos gregos. No relato de B021, Prometeu gerou Deucalião ao observar a beleza de Pirra, com o intuito "
      "de irritar Zeus; quando o «Rei dos Deuses» soube que os dois procriavam sexuadamente, os demos "
      "prestaram atenção naquele tipo de relacionamento e passaram a reproduzir o processo, na busca de novas "
      "soluções para a genética problemática deles."),
    cit=[
      ("B021", 4434, ["Observando a beleza de Pirra, Prometeu gerou um filho chamado"],
       "início da sentença de origem (continua em L4435)"),
      ("B021", 4435, ["“Deucalião”, que se uniu a ela."], "fecho intra-linha da mesma sentença"),
      ("B021", 4433, ["“produto de manipulação genética demo”"],
       "classificação de Pirra, mãe da linhagem — expressão completa intra-linha"),
      ("B021", 5259, ["— Prometeu, seu filho Deucalião está com Pirra, e eles tiveram filhos."],
       "fala de Zeus a Prometeu libertado — sentença completa intra-linha"),
      ("P2024-11-09", 85, ["Irmão de Epimeteu, que foi o consorte de Pandora, teve Deucalião como filho."],
       "palestra (STT) — sentença completa; a transcrição degrada o nome na frase seguinte («Decalião»)"),
    ],
    obs=[
      "Em P2024-11-09 todo o corpo da palestra é uma única linha (STT sem quebras), donde a citação "
      "intra-linha ser a sentença inteira; a degradação «Decalião» da frase imediata está preservada na "
      "fonte e não foi corrigida aqui (STT nunca é renomeado por conveniência).",
    ],
  ),
]

# ───────────────────────────────────────────────────────── tabela de relacionados
def tabela_relacionados(cod: str) -> str:
    """T14: a tabela é f(cadastro) — espelho t[6] ∪ arestas RELACOES, dos dois polos."""
    T = {t[0]: t for t in _d.TERMOS}
    esp: dict[str, set[str]] = {}
    for t in _d.TERMOS:
        for c in str(t[6]).split(";"):
            c = c.strip()
            if c in T and c != t[0]:
                esp.setdefault(t[0], set()).add(c)
                esp.setdefault(c, set()).add(t[0])
    tipo: dict[frozenset, str] = {}
    for a, tp, b, _f in _d.RELACOES:
        if a in T and b in T:
            tipo[frozenset((a, b))] = tp
    saida = ["| Termo | Código | Tipo de relação |", "|---|---|---|"]
    for x in sorted(esp.get(cod, set())):
        tp = tipo.get(frozenset((cod, x)), "associado")
        for a, t2, b, _f in _d.RELACOES:
            if {a, b} == {cod, x} and b == cod:
                tp = "← " + t2
        saida.append(f"| {T[x][1]} | {x} | {tp} |")
    return "\n".join(saida)


# ───────────────────────────────────────────────────────────────── corpo da ficha
NOTA_HARDWRAP = (
    "**Fratura de hard-wrap:** a edição digital das fontes quebra as sentenças em linhas curtas "
    "(B031 = 92 chars na maior linha · B021 = 106 · B026 = 109 · B003 = 111). Cada fragmento entre "
    "«» é verbatim **intra-linha**, conferido byte a byte contra o `original.txt` da obra declarada; "
    "quando uma sentença foi partida, o seu início e o seu fecho aparecem como fragmentos distintos, "
    "com as linhas indicadas. A sentença íntegra só será citável após o refinamento **R2** "
    "(reconstrução de parágrafos), previsto no dossiê do gap."
)
NOTA_V = (
    "Ficha nascida com o **V já chancelado** pelo Curador nas levas P7m/n/o e aplicado nesta unidade "
    "(a trava §7 «sem ficha → bloqueia» deixa de incidir): `chancela/HOLD.csv` baixado com desfecho."
)


def corpo(f: dict, termo: tuple) -> str:
    cit = []
    for sigla, n, trechos, nota in f["cit"]:
        conferir(sigla, n, trechos)
        pg = pagina(sigla, n)
        onde = f"{sigla} {pg}" if pg != "—" else sigla
        marca = " » … « ".join(f"«{t}»" for t in trechos)
        cit.append(f"> {marca} — {onde} · `original.txt` L{n} · {nota}.")
    fontes_rows = ["| Obra (sigla) | Título | Página | Tipo |", "|---|---|---|---|"]
    vistos = []
    for sigla, n, _t, _x in f["cit"]:
        if sigla in vistos:
            continue
        vistos.append(sigla)
    titulos = {s: _titulo(s) for s in vistos}
    for sigla in vistos:
        ps = sorted({pagina(sigla, n) for s2, n, _t, _x in f["cit"] if s2 == sigla})
        fontes_rows.append(f"| {sigla} | {titulos[sigla]} | {', '.join(ps)} | livro; citação intra-linha |"
                           if sigla.startswith("B")
                           else f"| {sigla} | {titulos[sigla]} | — | palestra/STT; citação intra-linha |")
    declaradas = ", ".join(termo[5])
    n_arestas = sum(1 for a, _t, b, _f in _d.RELACOES if f["cod"] in (a, b))
    return "\n".join([
        f"# {termo[1]} — {f['cod']}",
        "",
        "## Definição Sintética",
        "",
        f["definicao"],
        "",
        "## Contexto / Origem",
        "",
        "**Materialização (não é criação).** Este código vivia só no cadastro (`ficha=False`). A virada foi "
        "despachada pelo Curador em 13/09/2026 — rota **R1** do dossiê `diagnostico/CENSO-GAP-FICHAS-2026-09-13.md` "
        "(o piloto dos 8 suspensos com V chancelado que caem na família B) — e executada na unidade U41, na "
        "esteira do precedente U30 (RC-367/RC-537). Conteúdo restrito ao que a fonte sustém.",
        "",
        "## Escopo e evidência",
        "",
        f"- Fontes declaradas no cadastro: {declaradas}.",
        f"- Arestas em `RELACOES`: {n_arestas} — nada aberto, fechado ou reetiquetado nesta ficha.",
        f"- Censo do gap (13/09/2026): família **B · prosa citável na fonte declarada** "
        f"(`CENSO-GAP-FICHAS-2026-09-13.json`).",
        "",
        "## Termos Relacionados",
        tabela_relacionados(f["cod"]),
        "",
        "## Fontes",
        "",
        "\n".join(fontes_rows),
        "",
        "## Citações-chave",
        "",
        "\n\n".join(cit),
        "",
        "## Observações",
        "",
        "\n".join("- " + o for o in f["obs"]),
        f"- {NOTA_HARDWRAP}",
        f"- {NOTA_V}",
        "",
    ])


def _titulo(sigla: str) -> str:
    sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
    from loader import BIBLIO
    for row in BIBLIO:
        if row[0] == sigla:
            return row[1]
    if sigla.startswith("P"):
        return {
            "P2020-04-04": "palestra de 04/04/2020 (transcrição)",
            "P2023-05-21": "A hebdomada de Apolo — o ultraje humano",
            "P2024-11-09": "Abismo — consciência cósmica",
        }[sigla]
    raise KeyError(sigla)


# ───────────────────────────────────────────────── virada do cadastro (região TERMOS)
def virar_cadastro(codes: list[str]) -> int:
    src = open(CADASTRO, encoding="utf-8").read()
    linhas_arq = src.split("\n")
    ini = next(i for i, l in enumerate(linhas_arq) if l.strip() == "TERMOS = [")
    fim = next(i for i in range(ini, len(linhas_arq)) if linhas_arq[i].strip() == "]")
    feitos = []
    for cod in codes:
        for i in range(ini, fim):
            l = linhas_arq[i]
            if not l.lstrip().startswith(f'("{cod}"'):
                continue
            assert l.rstrip().endswith("False),"), f"{cod}: linha não termina em False), — {l!r}"
            novo = l.replace(", P, [", ', "verificado", [', 1).replace(", False),", ", True),")
            assert novo != l, f"{cod}: substituição não pegou — {l!r}"
            linhas_arq[i] = novo
            feitos.append(cod)
            break
        else:
            raise AssertionError(f"{cod}: não achado na região TERMOS")
    open(CADASTRO, "w", encoding="utf-8").write("\n".join(linhas_arq))
    return len(feitos)


# ─────────────────────────────────────────────────────────────────────────── main
def main() -> int:
    dry = "--dry" in sys.argv
    print("U41 · R1 — conferência byte a byte das citações (portão B)")
    for f in FICHAS:
        for sigla, n, trechos, _nota in f["cit"]:
            conferir(sigla, n, trechos)
        print(f"  {f['cod']}: {len(f['cit'])} citação(ões) conferidas · "
              f"{sum(len(t) for _s, _n, t, _x in f['cit'])} fragmento(s) verbatim")
    if dry:
        print("\n--dry: nada escrito.")
        return 0

    cods = [f["cod"] for f in FICHAS]
    n = virar_cadastro(cods)
    print(f"\ncadastro: {n} linhas viradas na região TERMOS (ficha False→True · P→verificado)")

    # recarrega o registro já virado — o frontmatter nasce DELE, nunca da mão (T13/T15)
    import importlib
    importlib.reload(_d)
    importlib.reload(_m)
    T = {t[0]: t for t in _d.TERMOS}
    for f in FICHAS:
        t = T[f["cod"]]
        assert t[7] is True, f"{f['cod']}: ficha não virou True"
        assert t[4] == "verificado", f"{f['cod']}: status não virou verificado"
        texto = _m.fm_toml(t, HOJE) + corpo(f, t)
        arq = os.path.join(RAIZ, "termos", f"RC-{f['cod'][3:]}-{f['slug']}.md")
        assert not os.path.exists(arq), f"já existe: {arq}"
        open(arq, "w", encoding="utf-8").write(texto)
        print(f"  ficha: termos/{os.path.basename(arq)} · {len(texto):,} B · "
              f"{len(re.findall('«', texto)) // 2} fragmento(s) entre aspas")
    print(f"\nU41: {len(FICHAS)} fichas materializadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
