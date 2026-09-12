# -*- coding: utf-8 -*-
"""
F045 · item 2 — PAR 3: RC-203 absorvido por RC-314 (despacho do Curador, 07/09/2026).

Diretrizes do despacho:
  1. RC-314 permanece a ancora canonica — ficha, verbatim de Ellam (B022) e
     status intactos; ZERO migracao de conteudo.
  2. RC-203 (codigo mais antigo, sem ficha) e marcado no registro-mestre como
     absorvido/remissiva de RC-314.
  3. A carga de fontes/ocorrencias de RC-203 (titulo do sumario B035 + a
     palestra P2025-03-15) e consolidada DENTRO da ficha de RC-314.
  4. Fica REVOGADA a flag "nao fundir" deste par (registrada nas notas de
     sistema e na propria ficha).

Restricoes herdadas: contiguidade estrita dos codigos (nenhuma remocao),
RELACOES intacto (1898 arestas) e nenhuma aspa digitada a mao — a fonte
P2025-03-15 entra como ocorrencia censada, SEM verbatim inventado.
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

MARCA = "[F045-MERGE 07-09-2026]"
PRIM = "RC-314"
DUP = "RC-203"

# --------------------------------------------------------------- registro ---
EDICOES = {
    PRIM: {
        "pares": [
            # consolidação de fontes: B035 entra no campo `fontes`
            ("['B022', 'P2025-03-15']", "['B022', 'B035', 'P2025-03-15']"),
            # absorção das referências cruzadas de RC-203 (RC-690 já constava)
            ("'RC-313; RC-300; RC-104; RC-094; RC-572; RC-578; RC-690'",
             "'RC-313; RC-300; RC-104; RC-094; RC-572; RC-578; RC-690; RC-155; RC-070; RC-203'"),
        ],
        "comentario": (
            "  # %s absorveu RC-203 (homonimo de B035, candidato sem ficha): fontes e "
            "referencias unificadas aqui. Remissiva em RC-203." % MARCA
        ),
    },
    DUP: {
        "pares": [
            ("'RC-155; RC-070; RC-690'", "'RC-314'"),
        ],
        "comentario": (
            "  # %s DUPLICATA ABSORVIDA por RC-314 (despacho do Curador 07/09/2026 — "
            "revogada a flag \"nao fundir\" deste par). Sem ficha materializada; permanece "
            "na sequencia como REMISSIVA — ver RC-314." % MARCA
        ),
    },
}

# ----------------------------------------------------------------- fichas ---
SECAO_ABSORCAO = """

---

## Absorção de RC-203 (F045 · 07/09/2026)

O código **RC-203** («Fenômenos Denunciadores do Fim», EVENTOS & ERAS / 7.3, status
*candidato*, sem ficha materializada) era duplicata homônima deste verbete e foi
absorvido aqui por despacho do Curador de 07/09/2026, que **revogou expressamente a
flag «não fundir»** registrada para este par durante a varredura bibliográfica —
quando ainda se separava o *título de capítulo* do B035 do *fenômeno narrado* no
B022. Na lógica da Enciclopédia o leitor precisa de **um** verbete conceitual único
para «Fenômenos Denunciadores do Fim», independentemente de o nome aparecer como
título num livro e como texto corrido noutro: duas entradas para o mesmo nome
gerariam redundância na obra final.

O lastro do RC-203 fica consolidado nesta ficha:

| Lastro absorvido | Destino nesta ficha |
|---|---|
| **B035 — *O Big Data do Criador***, sumário: cap. 4 «Fenômenos Denunciadores do Fim» (título homônimo) | já constava na tabela de Fontes; incorporado também ao campo `fontes` do registro-mestre |
| **P2025-03-15 — *A Rebelião dos Elétrons e a era do Colapso do Caos Organizado*** (15/03/2025) | ocorrência registrada no censo da palestra — **sem verbatim recuperado nesta consolidação** (a ficha registra a fonte, não a citação; nenhuma aspa entra digitada à mão) |
| **RC-155** (Eras da Criação) · **RC-070** (Isolamento Cósmico) | referências cruzadas absorvidas no campo `relações` do registro-mestre |

O código RC-203 permanece na sequência (a contiguidade é requisito do validador)
como **remissiva** para este verbete. Nenhuma aresta foi criada, removida ou
redirecionada em `RELACOES` — inclusive a aresta `RC-203 -[variação]-> RC-314 [B035]`,
que agora aponta da remissiva para o verbete canônico.
"""

ANTIGO_NAO_FUNDIR = (
    "Título homônimo no sumário de B035 = **não fundir**."
)
NOVO_NAO_FUNDIR = (
    "Título homônimo no sumário de B035 = **flag «não fundir» REVOGADA pelo despacho "
    "F045 (07/09/2026)** — o homônimo RC-203 foi absorvido por este verbete (seção "
    "«Absorção de RC-203», abaixo)."
)

LINHA_FONTE_P2025 = (
    "| A Rebelião dos Elétrons e a era do Colapso do Caos Organizado (P2025-03-15) "
    "| ocorrência no censo da palestra (15/03/2025) "
    "| citação indireta — sem verbatim recuperado |\n"
)

OBS_ANTIGA = (
    "Ficha baseada em B022 (obra primária) + B035 (título de capítulo). Termo promovido "
    "de candidato (⚪) para provisório (🟡) com o conteúdo de B022."
)
OBS_NOVA = (
    "Ficha baseada em B022 (obra primária) + B035 (título de capítulo). Termo promovido "
    "de candidato (⚪) para provisório (🟡) com o conteúdo de B022.\n\n"
    "**F045 (07/09/2026):** o homônimo RC-203 foi absorvido por este verbete e a flag "
    "«não fundir» deste par foi revogada por despacho do Curador — ver «Absorção de "
    "RC-203», acima."
)

AJUSTES_FICHA = {
    PRIM: [
        ("| **Última atualização** | 2026-08-12 |",
         "| **Última atualização** | 2026-09-07 |"),
        (ANTIGO_NAO_FUNDIR, NOVO_NAO_FUNDIR),
        ("| O Big Data do Criador (B035) | sumário (cap. 4) | — | título de capítulo (candidato) |",
         "| O Big Data do Criador (B035) | sumário (cap. 4) | — | título de capítulo (candidato) |\n" + LINHA_FONTE_P2025),
        (OBS_ANTIGA, OBS_NOVA),
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
            assert MARCA not in ln, f"{cod}: marca ja presente (edicao repetida?)"
            for antigo, novo in cfg["pares"]:
                assert ln.count(antigo) == 1, f"{cod}: trecho ausente/ambiguo -> {antigo!r}"
                ln = ln.replace(antigo, novo)
            linhas[i] = ln.rstrip() + cfg["comentario"]
            feitos.append(cod)
            break
    faltando = [c for c in EDICOES if c not in feitos]
    assert not faltando, f"codigos nao encontrados no bloco TERMOS: {faltando}"
    open(REG, "w", encoding="utf-8").write("\n".join(linhas))
    return feitos


def editar_fichas():
    tocados = []
    p = caminho_ficha(PRIM)
    txt = open(p, encoding="utf-8").read()
    assert MARCA not in txt, "marca ja presente (edicao repetida?)"
    for antigo, novo in AJUSTES_FICHA[PRIM]:
        assert txt.count(antigo) == 1, f"{PRIM}: ajuste ausente/ambiguo -> {antigo[:60]!r}"
        txt = txt.replace(antigo, novo)
    txt = txt.rstrip() + "\n" + SECAO_ABSORCAO
    open(p, "w", encoding="utf-8").write(txt)
    tocados.append(p)
    # RC-203 nao tem ficha — e assim deve permanecer
    assert not glob.glob(os.path.join(DIR_TERMOS, DUP + "-*.md")), \
        "RC-203 nao deveria ter ficha; o despacho pede remissiva sem materializacao"
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
    assert antes == depois, "censo mudou — so as edicoes autorizadas sao aceitaveis"

    idx = {t[0]: t for t in d.TERMOS}
    assert idx[DUP][6] == PRIM, f"{DUP} nao aponta para {PRIM}"
    assert DUP in idx[PRIM][6], f"{PRIM} nao registra a absorcao de {DUP}"
    assert "B035" in idx[PRIM][5] and "B022" in idx[PRIM][5], "fontes nao consolidadas"
    assert idx[DUP][7] is False, "RC-203 nao deve ganhar ficha nesta operacao"
    assert idx[PRIM][7] is True, "RC-314 deve continuar com ficha"
    for ref in ("RC-155", "RC-070"):
        assert ref in idx[PRIM][6], f"referencia {ref} nao absorvida"
    print("remissiva ok: %s -> %s" % (DUP, PRIM))
    print("fontes de %s: %s" % (PRIM, idx[PRIM][5]))

    # integridade global
    fichas = [t[0] for t in d.TERMOS if t[7]]
    arqs = glob.glob(os.path.join(DIR_TERMOS, "*.md"))
    assert not [c for c in fichas if not glob.glob(os.path.join(DIR_TERMOS, c + "-*.md"))]
    codigos = {t[0] for t in d.TERMOS}
    assert not [a for a in arqs if os.path.basename(a)[:6] not in codigos]
    nums = sorted(int(c.split("-")[1]) for c in codigos)
    assert nums == list(range(1, len(nums) + 1)), "contiguidade quebrada"
    print("matcher %d/%d · contiguidade RC-001..RC-%d OK" % (len(fichas), len(arqs), len(nums)))
    print("\nOK — par 3 desduplicado (RC-314 canonico) sem tocar em RELACOES.")


if __name__ == "__main__":
    main()
