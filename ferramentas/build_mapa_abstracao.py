#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o MAPA DE ABSTRAÇÃO (N0) da Revelação Cósmica — SVG + PDF + PNG.

Materializa a melhoria pedagógica nº 1 da PROPOSTA-PEDAGOGICA-TOP-DOWN:
a "figura fixa" do Nível 0 — o diagrama de contexto do método top-down
(Analista de Sistemas) aplicado à Revelação Cósmica.

Desenho:
  - 4 caixas do contexto: O FORA · O ACIDENTE · A TRIMURTI · AQUI
  - as 7 narrativas do Guia-Mestre como setas (① … ⑦)
  - banda lateral "⑥ Os Mundos e o Cosmo" = o substrato onde tudo acontece
  - seta de retorno (⑦) fechando o laço: AQUI → O FORA (Reintegração/Tikun)

Regras da casa (respeitadas por este script):
  - NÃO altera a Base: não toca em termos/, relacoes/ nem dados_termos.py.
  - Toda remissão RC-### usada no desenho é conferida contra a Base
    (assert de existência — nenhuma órfã entra na figura).

Dependência: matplotlib (pip install --user --break-system-packages matplotlib)

Uso:
  python3 ferramentas/build_mapa_abstracao.py
Saída (em pedagogico/top-down/):
  Mapa-de-Abstracao-N0.svg  (vetorial — fonte em path, abre igual em qualquer máquina)
  Mapa-de-Abstracao-N0.pdf  (impressão)
  Mapa-de-Abstracao-N0.png  (preview / inserção no DOCX)
"""
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_termos as BASE  # noqa: E402  — registro-mestre (censo de código)

SAIDA_DIR = os.path.join(RAIZ, "pedagogico", "top-down")
NOME = "Mapa-de-Abstracao-N0"

# ------------------------------------------------------------------ paleta
ROXO = "#331A55"      # título / setas de descida
LILAS = "#6A3D8C"
VERDE = "#2E7D4F"     # seta de retorno / checkpoint
CINZA = "#555555"
CINZA_CLARO = "#9AA0A6"

CAIXAS = {
    "FORA":     dict(fill="#E8F3EC", edge="#2E7D4F", titulo="#1E6B3A"),
    "ACIDENTE": dict(fill="#F3ECF8", edge="#6A3D8C", titulo="#4A2266"),
    "TRIMURTI": dict(fill="#E9EFF8", edge="#2F5D8C", titulo="#1F4570"),
    "AQUI":     dict(fill="#FBF2E4", edge="#B57A2E", titulo="#8A5A12"),
}

# ------------------------------------------------------------------ layout
W, H = 1700, 1215
BX, BW = 330, 970             # coluna das 4 caixas
FORA = (BX, 190, BW, 140)
ACID = (BX, 390, BW, 220)
TRIM = (BX, 670, BW, 180)
AQUI = (BX, 910, BW, 210)
BANDA = (60, 390, 250, 730)   # "⑥ Os Mundos e o Cosmo"

X_SETA = 815                  # eixo vertical das setas de descida
X_RET = 1420                  # canal da seta de retorno (direita)

# ------------------------------------------------------------------ textos
CABECALHO = [
    (60, 52, "MAPA DE ABSTRAÇÃO — A REVELAÇÃO CÓSMICA EM UMA FIGURA (N0)",
     27, "bold", ROXO),
    (60, 97,
     "Diagrama de contexto do percurso top-down: as 4 caixas do conjunto e as "
     "7 narrativas como setas. É a figura a que o aluno volta sempre.",
     14, "normal", CINZA),
    (60, 129,
     "Tese: «Um deus imperfeito caiu na própria criação, e somos nós — suas "
     "criaturas — que podemos ajudá-lo a se curar.» (RC-001 · RC-152 · RC-167)",
     14, "italic", LILAS),
]

CONTEUDO = {
    "FORA": (
        "O FORA — A ESPIRITUALIDADE SUPERIOR (a perfeição obrigatória)",
        [
            "Antes de tudo, a Realidade Maior / Paraíso Original (RC-204): uma única família de seres puros (RC-600),",
            "sob os Protocolos da Perfeição (RC-606) — sem tempo, sem distância, sem mérito. Tudo está contido nela (RC-059).",
            "É o nível do «fora»: o que não é acidente, não caiu e não precisa de conserto.",
        ],
    ),
    "ACIDENTE": (
        "O ACIDENTE — A CRIAÇÃO INDEVIDA (o colapso e a queda)",
        [
            "Prabrajna (RC-152), ser de altíssima hierarquia, quis projetar algo novo e sofreu um colapso psíquico",
            "— a Demência do Criador (RC-526) — e caiu para dentro da própria criação: o Mergulho (RC-528).",
            "Parte do seu espírito ficou presa: é o «eu desalmado» que chamamos Javé / Brahma (RC-001 / RC-037),",
            "refém da própria obra (RC-196). Este universo é a Criação Indevida (RC-167) — um acidente, não um plano.",
        ],
        "② A Queda e o Drama — o que deu errado?",
    ),
    "TRIMURTI": (
        "A TRIMURTI — O JOGO DE PODER (as cocriadoras que mergulharam)",
        [
            "Cocriadoras mergulham: Vishnu / Mavatna (RC-135) e Shiva / Savna (RC-102) juntam-se a Brahma (RC-037)",
            "e formam a Trimurti (RC-104) — um longo jogo de poder sobre quem herdaria a obra.",
            "Dessa linhagem nascem Sophia (RC-009) e Jesus (RC-072); dela é o Messias que ele não assumiu (RC-942).",
        ],
    ),
    "AQUI": (
        "AQUI — A TERRA E A HUMANIDADE (o lado material, isolado)",
        [
            "A vida foi transportada do antimaterial (RC-106) ao material (RC-107) — Projeto Talm (RC-091) — até a Terra,",
            "hoje em Isolamento Cósmico (RC-070) e Quarentena Sideral (RC-342). Somos os Seres Terrenos (RC-099),",
            "de DNA holográfico (RC-217), semeados por Agentes da Vida (RC-148), atravessados por Pandora (RC-086).",
            "É aqui que a criatura ajuda a consertar a Obra — e donde parte o caminho de volta.",
        ],
        "⑤ A Humanidade e a Terra — quem somos nós?",
    ),
}

SETAS = [
    # (y1, y2, rótulo, complemento) — descida, no eixo X_SETA
    (332, 386, "① O Criador e a Criação — quem criou? como?",
     "Prabrajna (RC-152) projeta · CFD (RC-040) · Criação Indevida (RC-167)"),
    (612, 666, "④ Os Seres do Cosmos — quem habita a criação?",
     "cocriadoras mergulham (RC-528) · Trimurti (RC-104) · Demos (RC-049)"),
    (852, 906, "③ A Rebelião e o Exílio — o que partiu a harmonia?",
     "Lúcifer / Yel Luzbel (RC-002 / RC-142) · Exilados de Capela (RC-007) · Isolamento (RC-070)"),
]

BANDA_LINHAS = [
    "⑥ OS MUNDOS",
    "E O COSMO",
    "— onde tudo acontece?",
    "",
    "Material (RC-107)",
    "Antimaterial (RC-106)",
    "Espiritualidades:",
    "Superior · Operacional",
    "· Laboratorial",
    "(RC-059 / 060 / 061)",
    "Perpérion (RC-087)",
    "× Tempérion (RC-472)",
    "Lokas · Khaos (RC-294)",
]

RETORNO = [
    "⑦ O CAMINHO DE VOLTA",
    "— como se conserta?",
    "Reintegração Cósmica",
    "(RC-003) · Tikun (RC-514)",
    "Mentalma (RC-166)",
    "Cidadão Cósmico (RC-226)",
]

RODAPE = [
    (60, 1146,
     "CHECKPOINT N0 — conte a trama inteira em 60 segundos apontando as 4 caixas. "
     "Se não consegue, a base ainda não está firme: não desça de nível.",
     13, "bold", VERDE),
    (60, 1172,
     "Base Terminológica RC · 946 termos · 638 fichas · 1.898 relações · remissões conferidas contra a Base (0 órfãs) · "
     "síntese de leitura (não altera a Base).",
     10, "normal", CINZA),
    (60, 1188,
     "Leitura de Jan Val Ellam — quarentena: o conteúdo teológico, cosmológico e ufológico não é consenso acadêmico ou religioso.",
     10, "normal", CINZA),
]


# ------------------------------------------------------------------ desenho
def caixa(ax, xywh, paleta, titulo, linhas, pill=None):
    x, y, w, h = xywh
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0,rounding_size=14",
        linewidth=2.0, edgecolor=paleta["edge"], facecolor=paleta["fill"],
        zorder=2))
    ax.text(x + 20, y + 26, titulo, fontsize=16, fontweight="bold",
            color=paleta["titulo"], va="top", zorder=3)
    yy = y + 60
    for ln in linhas:
        ax.text(x + 20, yy, ln, fontsize=11.5, color="#222222", va="top", zorder=3)
        yy += 19
    if pill:
        ax.add_patch(FancyBboxPatch(
            (x + 18, y + h - 52), 470, 34,
            boxstyle="round,pad=0,rounding_size=17",
            linewidth=1.2, edgecolor=paleta["edge"], facecolor="#FFFFFF",
            alpha=0.9, zorder=3))
        ax.text(x + 34, y + h - 46, pill, fontsize=11.5, fontweight="bold",
                color=paleta["titulo"], va="top", zorder=4)


def seta_vertical(ax, y1, y2, cor=ROXO):
    ax.annotate("", xy=(X_SETA, y2), xytext=(X_SETA, y1),
                arrowprops=dict(arrowstyle="-|>", color=cor, lw=2.6,
                                mutation_scale=20, shrinkA=0, shrinkB=0),
                zorder=3)


def rotulo_seta(ax, y1, linha1, linha2):
    ax.text(X_SETA + 22, y1 + 6, linha1, fontsize=13.5, fontweight="bold",
            color=ROXO, va="top", zorder=3)
    ax.text(X_SETA + 22, y1 + 28, linha2, fontsize=11, color="#444444",
            va="top", zorder=3)


def banda_cosmos(ax):
    x, y, w, h = BANDA
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0,rounding_size=14",
        linewidth=1.6, edgecolor=CINZA_CLARO, facecolor="#F5F5F7", zorder=1))
    yy = y + 22
    for i, ln in enumerate(BANDA_LINHAS):
        if ln:
            ax.text(x + 16, yy, ln, fontsize=11,
                    fontweight="bold" if i < 3 else "normal",
                    color="#333333" if i < 3 else "#555555", va="top", zorder=2)
        yy += 19 if ln else 10
    # ticks de conexão com as caixas
    for yc in (500, 760, 1015):
        ax.plot([x + w, BX - 2], [yc, yc], color=CINZA_CLARO, lw=1.4,
                linestyle=(0, (4, 3)), zorder=1)


def seta_retorno(ax):
    """AQUI (direita) → canal → O FORA (direita): o laço que fecha o diagrama."""
    ax.plot([BX + BW, X_RET], [1015, 1015], color=VERDE, lw=2.6,
            solid_capstyle="round", zorder=3)
    ax.plot([X_RET, X_RET], [1015, 260], color=VERDE, lw=2.6,
            solid_capstyle="round", zorder=3)
    ax.plot([X_RET, BX + BW], [260, 260], color=VERDE, lw=2.6,
            solid_capstyle="round", zorder=3)
    ax.annotate("", xy=(BX + BW, 260), xytext=(BX + BW + 26, 260),
                arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2.6,
                                mutation_scale=20, shrinkA=0, shrinkB=0),
                zorder=4)
    # rótulo ao lado da linha (sem interromper o traço)
    x0, y0, w, h = 1445, 648, 210, 132
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h, boxstyle="round,pad=0,rounding_size=12",
        linewidth=1.2, edgecolor=VERDE, facecolor="#FFFFFF", zorder=4))
    yy = y0 + 14
    for i, ln in enumerate(RETORNO):
        ax.text(x0 + w / 2, yy, ln, fontsize=11,
                fontweight="bold" if i < 2 else "normal",
                color=VERDE if i < 2 else "#444444",
                ha="center", va="top", zorder=5)
        yy += 18


def desenhar():
    matplotlib.rcParams["svg.fonttype"] = "path"   # SVG sem dependência de fonte
    fig = plt.figure(figsize=(W / 100.0, H / 100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)          # y crescendo para baixo (coordenadas de layout)
    ax.set_axis_off()
    fig.patch.set_facecolor("white")

    for (x, y, txt, tam, estilo, cor) in CABECALHO:
        # 'estilo' vale 'bold' | 'italic' | 'normal' — negrito é weight, não style
        ax.text(x, y, txt, fontsize=tam,
                fontstyle="italic" if estilo == "italic" else "normal",
                fontweight="bold" if estilo == "bold" else "normal",
                color=cor, va="top")

    banda_cosmos(ax)
    caixa(ax, FORA, CAIXAS["FORA"], *CONTEUDO["FORA"])
    caixa(ax, ACID, CAIXAS["ACIDENTE"], *CONTEUDO["ACIDENTE"])
    caixa(ax, TRIM, CAIXAS["TRIMURTI"], *CONTEUDO["TRIMURTI"])
    caixa(ax, AQUI, CAIXAS["AQUI"], *CONTEUDO["AQUI"])

    for (y1, y2, l1, l2) in SETAS:
        seta_vertical(ax, y1, y2)
        rotulo_seta(ax, y1, l1, l2)

    seta_retorno(ax)

    for (x, y, txt, tam, estilo, cor) in RODAPE:
        ax.text(x, y, txt, fontsize=tam,
                fontweight="bold" if estilo == "bold" else "normal",
                color=cor, va="top")

    return fig


# ------------------------------------------------------------------ validação
def textos_do_mapa():
    """Todos os textos que vão para a figura (para o censo de remissões)."""
    tudo = []
    for bloco in CONTEUDO.values():
        tudo.append(bloco[0])
        tudo.extend(bloco[1])
        if len(bloco) > 2:
            tudo.append(bloco[2])
    for (_, _, l1, l2) in SETAS:
        tudo += [l1, l2]
    tudo += BANDA_LINHAS + RETORNO
    tudo += [t[2] for t in CABECALHO] + [t[2] for t in RODAPE]
    return tudo


def validar_remissoes():
    """Nenhuma remissão RC-### órfã entra na figura (regra da casa)."""
    codigos = {t[0] for t in BASE.TERMOS}
    usados = set()
    for txt in textos_do_mapa():
        usados.update(re.findall(r"RC-\d{3}", txt))
    orfas = sorted(c for c in usados if c not in codigos)
    assert not orfas, f"REMISSOES ORFAS NA FIGURA: {orfas}"
    return usados


def main():
    usados = validar_remissoes()
    fig = desenhar()

    os.makedirs(SAIDA_DIR, exist_ok=True)
    saidas = []
    png = os.path.join(SAIDA_DIR, NOME + ".png")
    fig.savefig(png, dpi=150, facecolor="white")
    saidas.append(png)
    svg = os.path.join(SAIDA_DIR, NOME + ".svg")
    fig.savefig(svg, format="svg", facecolor="white")
    saidas.append(svg)
    pdf = os.path.join(SAIDA_DIR, NOME + ".pdf")
    fig.savefig(pdf, format="pdf", facecolor="white")
    saidas.append(pdf)
    plt.close(fig)

    print(f"remissoes conferidas: {len(usados)} codigos RC-### (0 orfas)")
    for s in saidas:
        print("OK ->", os.path.relpath(s, RAIZ))


if __name__ == "__main__":
    main()
