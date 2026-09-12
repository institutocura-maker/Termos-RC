# -*- coding: utf-8 -*-
"""
F045 · item 2 — desduplicação de pares homônimos (pares 1 e 2).

Precedente: F044 (RC-941 -> RC-193). Regra do despacho: manter o código mais
antigo/primário e absorver a duplicata.

Restrição herdada que governa o mecanismo: o validador exige CONTIGUIDADE
ESTRITA dos códigos (assert num == i), de modo que NENHUM código do meio da
sequência pode ser deletado sem renumeração em massa. O mecanismo adotado é,
portanto, a REMISSIVA:

  * o PRIMÁRIO (código mais antigo) absorve fontes, referências e conteúdo;
  * a DUPLICATA permanece na sequência (contiguidade preservada) como
    remissiva apontando para o primário — registro marcado com [F045-MERGE]
    e ficha convertida em banner de remissiva + conteúdo histórico;
  * ZERO arestas criadas, removidas ou retargeteadas em RELACOES.

Idempotente nao é: cada edição é asseverada (ocorrência única do trecho
antigo). Rodar duas vezes falha com assert — nunca aplica em silêncio.
"""
import os
import sys
import glob
import importlib

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
REG = os.path.join(AQUI, "dados_termos.py")
DIR_TERMOS = os.path.join(RAIZ, "termos")
sys.path.insert(0, AQUI)

import dados_termos as d  # noqa: E402

DATA = "07/09/2026"
MARCA = "[F045-MERGE 07-09-2026]"

# ---------------------------------------------------------------- registro ---
# Cada par: codigo -> lista de (trecho_antigo, trecho_novo) + sufixo de comentário
EDICOES = {
    # ---- PAR 1: RC-898 (primário, 5 fontes) absorve RC-936 (F043-T3, 0 fontes)
    "RC-898": {
        "pares": [
            ("'RC-892; RC-722; RC-070'",
             "'RC-892; RC-722; RC-070; RC-936'"),
        ],
        "comentario": (
            "  # %s absorveu RC-936 (\"Choque de realidade\", homonimo aberto por "
            "F043-T3): referencias e conteudo unificados aqui. Remissiva em RC-936." % MARCA
        ),
    },
    "RC-936": {
        "pares": [
            ("P, [], '', True)",
             "P, [], 'RC-898', True)"),
        ],
        "comentario": (
            "  # %s DUPLICATA ABSORVIDA por RC-898 — permanece na sequencia "
            "(contiguidade) como REMISSIVA; a ficha aponta para RC-898." % MARCA
        ),
    },
    # ---- PAR 2: RC-164 (primário, 10 fontes) absorve RC-449 (5 fontes)
    "RC-164": {
        "pares": [
            ("['B024', 'B035', 'B019', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', "
             "'P2024-04-13', 'P2024-04-14', 'P2021-03-27', 'P2025-11-29']",
             "['B024', 'B035', 'B019', 'B057', 'B058', 'P2025-03-15', 'P2025-02-15', "
             "'P2024-11-30', 'P2024-04-13', 'P2024-04-14', 'P2021-03-27', 'P2025-11-29']"),
            ("'RC-163; RC-099; RC-160'",
             "'RC-163; RC-099; RC-160; RC-036; RC-001; RC-148; RC-449'"),
        ],
        "comentario": (
            "  # %s absorveu RC-449 (\"Criaturas-ferramenta\", homonimo com lastro "
            "B057/B058): fontes e referencias unificadas aqui. Remissiva em RC-449." % MARCA
        ),
    },
    "RC-449": {
        "pares": [
            ("'RC-036; RC-099; RC-001; RC-148'",
             "'RC-164'"),
        ],
        "comentario": (
            "  # %s DUPLICATA ABSORVIDA por RC-164 — permanece na sequencia "
            "(contiguidade) como REMISSIVA; a ficha aponta para RC-164." % MARCA
        ),
    },
}

# ------------------------------------------------------------------ fichas ---
BANNER_936 = """
> **REMISSIVA — {marca}** Este código é **duplicata absorvida por RC-898
> («Choque de Realidade»)**. O verbete canônico é **RC-898** — é ele que deve ser
> citado. O conteúdo abaixo fica preservado como registro histórico da abertura
> F043-T3 (Anel C, definição do Glossário Krys Amon como fonte secundária).
""".format(marca=MARCA)

BANNER_449 = """
> **REMISSIVA — {marca}** Este código é **duplicata absorvida por RC-164
> («Criaturas-ferramenta»)**. O verbete canônico é **RC-164** — é ele que deve ser
> citado. O conteúdo abaixo fica preservado como registro histórico, notadamente o
> lastro B057/B058 (a metafísica do reflexo), migrado para o verbete canônico.
""".format(marca=MARCA)

ABSORCAO_898 = """

---

## Absorção de RC-936 — F045 · 07/09/2026

O código **RC-936** («Choque de realidade», aberto por F043-T3 em 06/09/2026) era
duplicata homônima deste verbete e foi absorvido aqui pelo despacho F045; a ficha
RC-936 passa a remissiva. O material exclusivo daquela ficha — a definição
dicionarizada do *Glossário Krys Amon* — fica preservado abaixo como **sentido
registrado pelo grupo**.

**Sentido 2 — registro do grupo (fonte secundária):** «Situação inesperada e que
causa desilusão, interferindo drasticamente no modo de viver.»
— EXT-2024-01-04 (Glossário Krys Amon), verbete «Choque de realidade»;
paráfrase/definição, **fonte secundária** (a hierarquia das fontes primárias —
obras e falas de Jan Val Ellam — permanece intacta).

**Nota de método (por que os dois verbetes não conflitam):** a definição do grupo
descreve o *efeito* do choque sobre o indivíduo — a desilusão que rompe a zona de
conforto teórico; a definição canônica (acima) descreve a *causa* coletiva — os
processos já represados que a humanidade mesma engatilhou. Efeito e causa: o
despertar forçado é o outro nome da explosão.
""".format(marca=MARCA)

ABSORCAO_164 = """

---

## Absorção de RC-449 — F045 · 07/09/2026

O código **RC-449** («Criaturas-ferramenta», SERES & ENTIDADES / 1.7, com lastro
em B057-B058) era duplicata homônima deste verbete e foi absorvido aqui pelo
despacho F045; a ficha RC-449 passa a remissiva. O material exclusivo daquele
verbete fica preservado abaixo.

### B058 (A Revolta do Anjo Decaído) — a metafísica do reflexo

- **[B058 p. 6 · nota «Imagem e Reflexo» — a definição filosófica do conceito]**
  «apenas uma **criatura-ferramenta**, e passa a constituir **o "deus verdadeiro de
  si mesmo"!**»; «A "Forma Imagem-pensamento" foi subjugada por algumas das suas
  "réplicas" que se libertaram e se autotransformaram em "reflexos de si mesmas",
  independentes do seu Criador.»
- **[B058 p. 8]** «Que culpa têm as **criaturas-ferramentas — como os capelinos e os
  humanos**, por exemplo — que surgiram para a vida nesta Criação "imperfeita", de
  simplesmente pensarem e procederem de acordo com o que foram condicionados?»
  (nota da autora terrena.)
- **[B058 p. 9]** a tríade: «o "Espelho" (o Espírito) modificar o "reflexo" (o ego da
  criatura-ferramenta que ele anima) e a "Imagem" (o próprio Criador que se
  "reconstituiu"...).»
- 0 códigos novos (O-3). «Deus verdadeiro de si mesmo» e a metafísica do reflexo =
  **leitura teológica/filosófica do ser** (O-7 — jamais fato ontológico primário).

### P2025-05-31 — o contexto dos clones

- «todos os seres... são clones de Javé... os tais anjos clones ou seres de condição
  adhyajna que se metamorfoseiam, são seres demoníacos, não no sentido ruim da
  palavra» — o contexto da criação como «criaturas-ferramenta» de Javé.

### P2025-03-15 — o diferencial humano

- «o pior dos 8 bilhões de seres humanos é capaz de agir como um herói em um dado
  instante... ele dá a vida dele por alguém que ele ama. Ponto. Ninguém nesses 13,8
  bilhões de anos consegue fazer isso no paraíso» — o diferencial humano como
  ferramenta de ressignificação.
""".format(marca=MARCA)

APENDICES = {
    "RC-898": ABSORCAO_898,
    "RC-164": ABSORCAO_164,
}

BANNERS = {
    "RC-936": BANNER_936,
    "RC-449": BANNER_449,
}

# Ajustes finos nas fichas primárias: (trecho_antigo, trecho_novo)
AJUSTES_FICHA = {
    "RC-898": [
        ("| **Última atualização** | 2026-09-02 |",
         "| **Última atualização** | 2026-09-07 |"),
    ],
    "RC-164": [
        ("| **Última atualização** | 2026-08-18 |",
         "| **Última atualização** | 2026-09-07 |"),
        ("| Criaturas-ferramenta | RC-449 | sinônimo |",
         "| Criaturas-ferramenta | RC-449 | remissiva — duplicata absorvida por este verbete (%s) |" % MARCA),
    ],
    "RC-449": [
        ("| **Última atualização** | 2026-08-18 |",
         "| **Última atualização** | 2026-09-07 |"),
        ("| Criaturas-ferramenta | RC-164 | sinônimo |",
         "| Criaturas-ferramenta | RC-164 | verbete canônico — este código é remissiva (%s) |" % MARCA),
    ],
    "RC-936": [
        ("| **Última atualização** | 2026-09-06 |",
         "| **Última atualização** | 2026-09-07 |"),
    ],
}


def caminho_ficha(codigo):
    achou = glob.glob(os.path.join(DIR_TERMOS, codigo + "-*.md"))
    assert len(achou) == 1, f"ficha de {codigo}: esperava 1 arquivo, achei {len(achou)}"
    return achou[0]


def editar_registro():
    src = open(REG, encoding="utf-8").read()
    linhas = src.split("\n")
    fim = next((i for i, l in enumerate(linhas) if l.startswith("RELACOES")), None)
    assert fim is not None, "nao achei o inicio do bloco RELACOES"
    feitos = []
    for i, ln in enumerate(linhas[:fim]):
        for cod, cfg in EDICOES.items():
            if not ln.lstrip().startswith('("%s",' % cod):
                continue
            assert cod not in feitos, f"linha duplicada para {cod}"
            for antigo, novo in cfg["pares"]:
                assert ln.count(antigo) == 1, f"{cod}: trecho nao encontrado/ambiguo -> {antigo!r}"
                ln = ln.replace(antigo, novo)
            ln = ln.rstrip() + cfg["comentario"]
            linhas[i] = ln
            feitos.append(cod)
            break
    faltando = [c for c in EDICOES if c not in feitos]
    assert not faltando, f"codigos nao encontrados no bloco TERMOS: {faltando}"
    open(REG, "w", encoding="utf-8").write("\n".join(linhas))
    return feitos


def editar_fichas():
    tocados = []
    for cod, banner in BANNERS.items():
        p = caminho_ficha(cod)
        txt = open(p, encoding="utf-8").read()
        linhas = txt.split("\n")
        assert linhas[0].startswith("# "), f"{cod}: primeira linha nao e H1"
        assert MARCA not in txt, f"{cod}: marca {MARCA} ja presente (edicao repetida?)"
        linhas[0] = linhas[0] + "\n" + banner
        txt = "\n".join(linhas)
        open(p, "w", encoding="utf-8").write(txt)
        tocados.append(p)

    for cod, secao in APENDICES.items():
        p = caminho_ficha(cod)
        txt = open(p, encoding="utf-8").read()
        assert MARCA not in txt, f"{cod}: marca ja presente (edicao repetida?)"
        open(p, "w", encoding="utf-8").write(txt.rstrip() + "\n" + secao)
        tocados.append(p)

    for cod, pares in AJUSTES_FICHA.items():
        p = caminho_ficha(cod)
        txt = open(p, encoding="utf-8").read()
        for antigo, novo in pares:
            assert txt.count(antigo) == 1, f"{cod}: ajuste ambiguo/ausente -> {antigo!r}"
            txt = txt.replace(antigo, novo)
        open(p, "w", encoding="utf-8").write(txt)
        tocados.append(p)
    return tocados


def main():
    antes = (len(d.TERMOS), sum(1 for t in d.TERMOS if t[7]), len(d.RELACOES))
    print("ANTES: %d termos · %d fichas · %d relações" % antes)
    d.validar()

    feitos = editar_registro()
    print("registro: %d linhas editadas -> %s" % (len(feitos), ", ".join(sorted(feitos))))
    for p in editar_fichas():
        print("  ficha atualizada:", os.path.relpath(p, RAIZ))

    importlib.reload(d)
    d.validar()
    depois = (len(d.TERMOS), sum(1 for t in d.TERMOS if t[7]), len(d.RELACOES))
    print("DEPOIS: %d termos · %d fichas · %d relações" % depois)
    assert antes == depois, "censo mudou — nada alem das edicoes autorizadas e aceitavel"

    # contiguidade / integridade do matcher
    fichas = [t for t in d.TERMOS if t[7]]
    arqs = glob.glob(os.path.join(DIR_TERMOS, "*.md"))
    sem_arq = [t[0] for t in fichas if not glob.glob(os.path.join(DIR_TERMOS, t[0] + "-*.md"))]
    codigos = {t[0] for t in d.TERMOS}
    sem_cod = [a for a in arqs if os.path.basename(a)[:6] not in codigos]
    assert not sem_arq, f"ficha sem arquivo: {sem_arq}"
    assert not sem_cod, f"arquivo sem codigo: {sem_cod}"
    print("matcher ficha<->arquivo: %d/%d OK" % (len(fichas), len(arqs)))

    # conferencia das remissivas
    idx = {t[0]: t for t in d.TERMOS}
    for dup, prim in (("RC-936", "RC-898"), ("RC-449", "RC-164")):
        assert idx[dup][6] == prim, f"{dup} nao aponta para {prim}: {idx[dup][6]!r}"
        assert dup in idx[prim][6], f"{prim} nao registra a absorcao de {dup}"
        print("remissiva ok: %s -> %s" % (dup, prim))
    assert "B057" in idx["RC-164"][5] and "B058" in idx["RC-164"][5], "fontes B057/B058 nao absorvidas"
    print("fontes absorvidas em RC-164: B057, B058")
    print("\nOK — pares 1 e 2 desduplicados sem tocar em RELACOES.")


if __name__ == "__main__":
    main()
