#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO (U42+) — driver genérico de materialização por lote (rota R1 do gap).
"""Materializa um lote de fichas da família B do gap a partir de um `lote.json`.

Nasce na U42 (13/09/2026) para não repetir 400 linhas por lote: o **driver** é
genérico e o **lote** é dado (`diagnostico/U*-R1-LOTE*-*.json`). O lote 1 da U41
continua registrado no seu próprio script histórico, intacto.

Regra de ouro herdada da U30 + pacto (inalterada):
  · o motor NÃO inventa conteúdo — a Definição Sintética é síntese curatorial do
    que a fonte sustém; o que vai entre «» é citação;
  · citação só **verbatim intra-linha**, conferida byte a byte contra o
    `original.txt` (nada de juntar linhas fraturadas pelo hard-wrap);
  · frontmatter SEMPRE regerado por `motor.fm_toml` (nunca à mão) — T15;
  · ficha nasce com «Materialização (não é criação)» + Escopo e evidência +
    tabela Termos Relacionados = espelho t[6] ∪ arestas (T14);
  · `RELACOES` blindado: 0 arestas abertas, fechadas ou reetiquetadas;
  · o cadastro é virado ANTES do frontmatter nascer — assim a ficha reflete o
    registro, nunca o contrário.

Uso
    python3 ferramentas/materializar_lote.py <caminho/do/lote.json> [--dry]
"""
from __future__ import annotations

import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))

import motor as _m                                             # noqa: E402
import dados_termos as _d                                      # noqa: E402

from loader import BIBLIO                                      # noqa: E402

CADASTRO = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
_CACHE: dict[str, list[str]] = {}


# ────────────────────────────────────────────────────────────────────── corpus
def caminho_da_obra(sigla: str) -> str:
    """Localiza o `original.txt` da obra pelo seu diretório canônico."""
    if sigla in _CACHE and _CACHE[sigla] is None:
        raise FileNotFoundError(sigla)
    for base in ("livros/CONCLUIDOS", "apostilas/CONCLUIDAS", "ciclos"):
        for dd in sorted(os.listdir(os.path.join(RAIZ, base))):
            b = dd.split("_")[0]
            if b[0].isdigit():
                b = "P" + b
            if b == sigla:
                p = os.path.join(base, dd, "original.txt")
                if os.path.exists(os.path.join(RAIZ, p)):
                    return p
    _CACHE[sigla] = None
    raise FileNotFoundError(f"sem corpus processado para {sigla}")


def linhas(sigla: str) -> list[str]:
    if sigla not in _CACHE or _CACHE[sigla] is None:
        with open(os.path.join(RAIZ, caminho_da_obra(sigla)), encoding="utf-8",
                  errors="replace") as fh:
            _CACHE[sigla] = fh.read().split("\n")
    return _CACHE[sigla]


def pagina(sigla: str, n: int) -> str:
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
        assert t in alvo, (f"PORTÃO B · {sigla} L{n}: trecho NÃO confere byte a byte\n"
                           f"  trecho : {t!r}\n  linha  : {alvo!r}")


def titulo(sigla: str) -> str:
    for row in BIBLIO:
        if row[0] == sigla:
            return row[1]
    return sigla  # palestra sem entrada na BIBLIO: a sigla já é o rótulo


# ────────────────────────────────────────────────────── tabela de relacionados
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
    saida = ["| Termo | Código | Tipo de relação |", "|---|---|---|"]
    for x in sorted(esp.get(cod, set())):
        tp = "associado"
        for a, t2, b, _f in _d.RELACOES:
            if {a, b} == {cod, x}:
                tp = ("← " + t2) if b == cod else t2
        saida.append(f"| {T[x][1]} | {x} | {tp} |")
    return "\n".join(saida)


# ───────────────────────────────────────────────────────────── corpo da ficha
def nota_hardwrap(lote: dict) -> str:
    return lote.get("nota_hardwrap", (
        "**Fratura de hard-wrap:** a edição digital das fontes quebra as sentenças em linhas "
        "curtas. Cada fragmento entre «» é verbatim **intra-linha**, conferido byte a byte "
        "contra o `original.txt` da obra declarada; quando uma sentença foi partida, o seu "
        "início e o seu fecho aparecem como fragmentos distintos, com as linhas indicadas. "
        "A sentença íntegra só será citável após o refinamento **R2** (reconstrução de "
        "parágrafos), previsto no dossiê do gap."))


def nota_chancela(lote: dict) -> str:
    """Governança: só recebe 🟢 quem tem V do Curador. O resto nasce 🟡 e vai a leva."""
    if lote.get("aplicar_V"):
        return ("Ficha nascida com o **V já chancelado** pelo Curador e aplicado nesta unidade "
                "(a trava §7 «sem ficha → bloqueia» deixa de incidir).")
    return ("**Status de nascença:** 🟡 **provisório** — este código nunca passou por leva de chancela "
            "(nenhuma planilha `chancela/P7-*.csv` o contém): a materialização da ficha foi despachada, "
            "o **V não**, e marcar 🟢 sem chancela seria autocancela. A ficha segue para a próxima leva "
            "de chancela, com as citações já extraídas e conferidas.")


def corpo(f: dict, termo: tuple, lote: dict) -> str:
    cit, vistos = [], []
    for sigla, n, trechos, nota in f["cit"]:
        conferir(sigla, n, trechos)
        pg = pagina(sigla, n)
        onde = f"{sigla} {pg}" if pg != "—" else sigla
        marca = " » … « ".join(f"«{t}»" for t in trechos)
        cit.append(f"> {marca} — {onde} · `original.txt` L{n} · {nota}.")
        if sigla not in vistos:
            vistos.append(sigla)
    rows = ["| Obra (sigla) | Título | Página | Tipo |", "|---|---|---|---|"]
    for sigla in vistos:
        ps = sorted({pagina(sigla, n) for s2, n, _t, _x in f["cit"] if s2 == sigla})
        tipo = "livro; citação intra-linha" if sigla.startswith("B") else "palestra/STT; citação intra-linha"
        rows.append(f"| {sigla} | {titulo(sigla)} | {', '.join(ps)} | {tipo} |")
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
        f"**Materialização (não é criação).** Este código vivia só no cadastro (`ficha=False`). "
        f"A virada foi despachada pelo Curador em 13/09/2026 — rota **R1** do dossiê "
        f"`diagnostico/CENSO-GAP-FICHAS-2026-09-13.md` — e executada na unidade "
        f"{lote['unidade']} (lote {lote['lote']} da família B), na esteira do precedente U30 "
        f"(RC-367/RC-537) e do piloto U41. Conteúdo restrito ao que a fonte sustém.",
        "",
        "## Escopo e evidência",
        "",
        f"- Fontes declaradas no cadastro: {', '.join(termo[5])}.",
        f"- Arestas em `RELACOES`: {n_arestas} — nada aberto, fechado ou reetiquetado nesta ficha.",
        "- Censo do gap (13/09/2026): família **B · prosa citável na fonte declarada** "
        "(`CENSO-GAP-FICHAS-2026-09-13.json`).",
        "",
        "## Termos Relacionados",
        tabela_relacionados(f["cod"]),
        "",
        "## Fontes",
        "",
        "\n".join(rows),
        "",
        "## Citações-chave",
        "",
        "\n\n".join(cit),
        "",
        "## Observações",
        "",
        "\n".join("- " + o for o in f["obs"]),
        f"- {nota_hardwrap(lote)}",
        f"- {nota_chancela(lote)}",
        "",
    ])


# ──────────────────────────────────────────── virada do cadastro (região TERMOS)
def virar_cadastro(codes: list[str], aplicar_v: bool = False) -> int:
    linhas_arq = open(CADASTRO, encoding="utf-8").read().split("\n")
    ini = next(i for i, l in enumerate(linhas_arq) if l.strip() == "TERMOS = [")
    fim = next(i for i in range(ini, len(linhas_arq)) if linhas_arq[i].strip() == "]")
    feitos = []
    for cod in codes:
        for i in range(ini, fim):
            l = linhas_arq[i]
            if not l.lstrip().startswith(f'("{cod}"'):
                continue
            assert l.rstrip().endswith("False),"), f"{cod}: linha não termina em False), — {l!r}"
            novo = l.replace(", False),", ", True),")
            if aplicar_v:
                assert ", P, [" in l, f"{cod}: esperava status P (provisório) — {l!r}"
                novo = novo.replace(", P, [", ', "verificado", [', 1)
            assert novo != l, f"{cod}: substituição não pegou — {l!r}"
            linhas_arq[i] = novo
            feitos.append(cod)
            break
        else:
            raise AssertionError(f"{cod}: não achado na região TERMOS")
    open(CADASTRO, "w", encoding="utf-8").write("\n".join(linhas_arq))
    return len(feitos)


# ───────────────────────────────────────────────────────────────────────── main
def main() -> int:
    if len(sys.argv) < 2:
        sys.exit("uso: materializar_lote.py <lote.json> [--dry]")
    lote = json.load(open(sys.argv[1], encoding="utf-8"))
    dry = "--dry" in sys.argv
    print(f"{lote['unidade']} · lote {lote['lote']} da rota {lote.get('rota','R1')} · "
          f"{len(lote['fichas'])} fichas — conferência byte a byte (portão B)")
    for f in lote["fichas"]:
        for sigla, n, trechos, _nota in f["cit"]:
            conferir(sigla, n, trechos)
        print(f"  {f['cod']}: {sum(len(t) for _s,_n,t,_x in f['cit'])} fragmento(s) conferidos")
    if dry:
        print("\n--dry: nada escrito.")
        return 0

    cods = [f["cod"] for f in lote["fichas"]]
    aplicar_v = bool(lote.get("aplicar_V"))
    print(f"\ncadastro: {virar_cadastro(cods, aplicar_v)} linha(s) virada(s) na região TERMOS (ficha False→True" + (" · provisório→verificado — V do Curador)" if aplicar_v else " · status PRESERVADO — sem V)"))

    import importlib
    importlib.reload(_d)
    importlib.reload(_m)
    T = {t[0]: t for t in _d.TERMOS}
    for f in lote["fichas"]:
        t = T[f["cod"]]
        assert t[7] is True, f"{f['cod']}: ficha não virou True"
        assert t[4] == ("verificado" if aplicar_v else "provisório"), f"{f['cod']}: status inesperado {t[4]!r}"
        texto = _m.fm_toml(t, lote["data"]) + corpo(f, t, lote)
        arq = os.path.join(RAIZ, "termos", f"{f['cod']}-{f['slug']}.md")
        assert not os.path.exists(arq), f"já existe: {arq}"
        open(arq, "w", encoding="utf-8").write(texto)
        print(f"  ficha: termos/{os.path.basename(arq)} · {len(texto):,} B")
    print(f"\n{lote['unidade']}: {len(lote['fichas'])} fichas materializadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
