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
from pathlib import Path

from caminhos_acervo import caminho_atual

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))

import motor as _m                                             # noqa: E402
import dados_termos as _d                                      # noqa: E402

from loader import BIBLIO                                      # noqa: E402

CADASTRO = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
_CACHE: dict[str, list[str]] = {}
LIVROS = caminho_atual("fonte.livros")
APOSTILAS_CONCLUIDAS = caminho_atual("fonte.apostilas_concluidas")


# ────────────────────────────────────────────────────────────────────── corpus
def caminho_da_obra(sigla: str) -> str:
    """Localiza o `original.txt` da obra pelo seu diretório canônico."""
    if sigla in _CACHE and _CACHE[sigla] is None:
        raise FileNotFoundError(sigla)
    for base in (LIVROS / "CONCLUIDOS", APOSTILAS_CONCLUIDAS,
                 Path(RAIZ) / "ciclos"):
        for dd in sorted(os.listdir(base)):
            b = dd.split("_")[0]
            if b[0].isdigit():
                b = "P" + b
            if b == sigla:
                p = base / dd / "original.txt"
                if p.exists():
                    return os.fspath(p.relative_to(RAIZ))
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


def nota_chancela(lote: dict, status: str = "provisório") -> str:
    """Governança: só recebe 🟢 quem tem V do Curador. O resto nasce 🟡 e vai a leva.

    U77 — `status` é o status REAL do código no cadastro. Até aqui todos os
    lotes da R1 eram «provisório»; RC-931 é «candidato». Dizer «provisório»
    a quem o cadastro registra como «candidato» seria a ficha emprestar ao
    registro um status que ele não tem (U60).
    """
    av = lote.get("aplicar_V")
    if av == "presuncao-livro":
        return ("**V presuntivo (fonte de livro):** despacho do Curador de 13/09/2026 — "
                "`diagnostico/DESPACHO-V-POR-FONTE-DE-LIVRO-2026-09-13.md`. O 🟢 vem do lastro em obra "
                "publicada (fonte `B###` declarada) + citação verbatim conferida byte a byte, **não** de "
                "revisão termo a termo; as guardas E1–E5 foram verificadas antes da escrita. Reversível a "
                "qualquer tempo, e identificado na Base por `via = P6-evidência` + `confianca_fonte = alta`.")
    if av:
        return ("Ficha nascida com o **V já chancelado** pelo Curador e aplicado nesta unidade "
                "(a trava §7 «sem ficha → bloqueia» deixa de incidir).")
    if lote.get("v_revogado"):
        if status == "provisório":
            return ("**Status de nascença:** 🟡 **provisório** — a presunção de V por fonte de livro, que "
                    "chancelou os lotes 1 e 2, foi **REVOGADA pelo Curador para os lotes 3 em diante** "
                    "(`diagnostico/DESPACHO-ROTAS-POS-V2-2026-09-13.md`): o instrumento que a lastreava "
                    "estava submedido e estender a presunção sobre base comprometida comprometeria a Base. "
                    "Sem V não há 🟢: a ficha nasce provisória e segue para leva de chancela, com as "
                    "citações já extraídas e conferidas.")
        # U77 — status diverso de «provisório» (ex.: «candidato», RC-931): o texto
        # genérico diria «provisório» e emprestaria ao registro um status que ele
        # não tem (U60). Diz-se o status REAL; o mais fica idêntico.
        return (f"**Status de nascença:** 🟡 **{status}** — o status é o do cadastro, preservado "
                "sem promoção (U42). A presunção de V por fonte de livro, que "
                "chancelou os lotes 1 e 2, foi **REVOGADA pelo Curador para os lotes 3 em diante** "
                "(`diagnostico/DESPACHO-ROTAS-POS-V2-2026-09-13.md`): o instrumento que a lastreava "
                "estava submedido e estender a presunção sobre base comprometida comprometeria a Base. "
                f"Sem V não há 🟢: a ficha nasce **{status}** e segue para leva de chancela, com as "
                "citações já extraídas e conferidas.")
    if status == "provisório":
        return ("**Status de nascença:** 🟡 **provisório** — este código nunca passou por leva de chancela "
                "(nenhuma planilha `chancela/P7-*.csv` o contém): a materialização da ficha foi despachada, "
                "o **V não**, e marcar 🟢 sem chancela seria autocancela. A ficha segue para a próxima leva "
                "de chancela, com as citações já extraídas e conferidas.")
    return (f"**Status de nascença:** 🟡 **{status}** — este código nunca passou por leva de chancela "
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
    tab = tabela_relacionados(f["cod"])
    n_tab = max(0, tab.count("\n") - 1)
    secoes = [
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
        (f"- Arestas em `RELACOES`: {n_arestas} — a tabela abaixo soma a essas as do espelho "
         f"do cadastro ({n_tab} no total). Nada aberto, fechado ou reetiquetado nesta ficha."),
        "- Censo do gap (13/09/2026): família **B · prosa citável na fonte declarada** "
        "(`CENSO-GAP-FICHAS-2026-09-13.json`).",
        "",
        "## Termos Relacionados",
        tab,
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
        f"- {nota_chancela(lote, termo[4])}",
    ]
    if f.get("historico"):
        # Gaveta instituída pelo despacho DESPACHO-DIVERGENCIAS-CROSSREF-E-GRAFIA:
        # para que contradição da FONTE não seja lida como erro de extração.
        secoes += ["", "## 6. Histórico Curatorial e Auditoria", "",
                   # renderização NEUTRA: o lote diz como quer o texto
                   # (parágrafos, tabelas, listas). O driver não decide.
                   "\n".join(f["historico"])]
    secoes.append("")
    return "\n".join(secoes)


# ─────────────────── guardas da presunção de V (DESPACHO-V-POR-FONTE-DE-LIVRO)
def checar_excecoes(cods: list[str], lote: dict) -> list[str]:
    """E1–E5 antes de qualquer escrita. Lista de impedimentos (vazia = pode seguir).

    E1 HOLD ativo · E2 famílias A/F · E3 família E · E4 colisão Base×fichas viva.
    A E4 é viva (conferida no ato), não a lista estática da auditoria P5b.
    """
    if not lote.get("aplicar_V"):
        return []
    import glob, json as _json, os as _os, unicodedata

    def sa(x):
        return ''.join(c for c in unicodedata.normalize('NFD', x)
                       if unicodedata.category(c) != 'Mn').lower()

    T = {t[0]: t for t in _d.TERMOS}
    hold = set()                                                     # E1
    with open(_os.path.join(RAIZ, "chancela", "HOLD.csv"), encoding="utf-8-sig") as fh:
        for ln in fh:
            campos = ln.rstrip("\r\n").split(";")
            if campos and campos[0].strip() in T and "DESFECHO" not in ln:
                hold.add(campos[0].strip())
    # Censo v3 primeiro (HOMOLOGADO pelo Curador em 13/09/2026, U51): ele
    # acrescenta à v2 o colapso da caixa alta espaçada (regra que resgatou a
    # RC-309 de D para B sem produzir um falso positivo sequer). A v2 vem a
    # seguir e a v1 por último — o v1 submedia a família E em ~70% (falso
    # negativo do hard-wrap) e a guarda E3 barraria códigos que são família B
    # de verdade — foi o caso da RC-171, que motivou a unidade U45.
    fam = {}
    for nome in ("CENSO-V3-ESPACADAS-2026-09-13.json",
                 "CENSO-RECLASSIFICADO-2026-09-13.json",
                 "CENSO-GAP-FICHAS-2026-09-13.json"):
        censo = _os.path.join(RAIZ, "diagnostico", nome)
        if _os.path.exists(censo):
            fam = {c["cod"]: c.get("fam_v2", c["fam"])
                   for c in _json.load(open(censo, encoding="utf-8"))}
            break
    usos = {c: set() for c in cods}                                  # E4
    for arq in glob.glob(_os.path.join(RAIZ, "termos", "*.md")):
        with open(arq, encoding="utf-8") as fh:
            for ln in fh:
                for c in cods:
                    if c in ln:
                        m = re.match(r"^\|\s*([^|]+?)\s*\|\s*" + c + r"\s*\|", ln.strip())
                        if m:
                            usos[c].add(sa(m.group(1)))
    ruins = []
    for c in cods:
        if c in hold:
            ruins.append(f"E1 · {c}: HOLD ativo")
        f = fam.get(c, "")
        if f.startswith(("A.", "F.")):
            ruins.append(f"E2 · {c}: família {f} (ambíguo/alias — qualificar antes)")
        if f.startswith("E."):
            ruins.append(f"E3 · {c}: família {f} (não achado no corpus — auditar)")
        div = sorted(u for u in usos[c] if u != sa(T[c][1]))
        if div:
            ruins.append(f"E4 · {c}: colisão Base×fichas — uso divergente {div[:3]}")
    return ruins


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
            # a linha pode carregar comentario de rastro depois de `False),` — ancorar na tupla
            cabeca, sep, cauda = l.partition(", False),")
            if not sep:
                # Já virado (`True`): IDEMPOTÊNCIA. Re-executar um lote é o
                # ritual de prova de regeneração — as fichas têm de voltar
                # byte a byte. Só a virada do cadastro é que já está feita.
                cabeca, sep, cauda = l.partition(", True),")
                if not sep:
                    raise AssertionError(
                        f"{cod}: linha nao casa com o padrao da tupla — {l!r}")
            corpo, resto = cabeca, cauda
            if aplicar_v and ", P, [" in corpo:
                corpo = corpo.replace(", P, [", ', "verificado", [', 1)
            novo = corpo + ", True)," + resto
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
        sys.exit("uso: materializar_lote.py <lote.json> [--dry] "
                 "[--sobrescrever]")
    lote = json.load(open(sys.argv[1], encoding="utf-8"))
    dry = "--dry" in sys.argv
    sobrescrever = "--sobrescrever" in sys.argv
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
    imped = checar_excecoes(cods, lote)
    if imped:
        sys.exit("PRESUNÇÃO DE V BLOQUEADA (DESPACHO-V-POR-FONTE-DE-LIVRO):\n  " +
                 "\n  ".join(imped))
    print("  guardas E1–E5: 0 impedimentos (presunção de V por fonte de livro)"
          if lote.get("aplicar_V") else "  guardas E1–E5: não aplicáveis (lote sem V)")
    print(f"\ncadastro: {virar_cadastro(cods, aplicar_v)} linha(s) virada(s) na região TERMOS (ficha False→True" + (" · provisório→verificado — V do Curador)" if aplicar_v else " · status PRESERVADO — sem V)"))

    import importlib
    importlib.reload(_d)
    importlib.reload(_m)
    T = {t[0]: t for t in _d.TERMOS}
    for f in lote["fichas"]:
        t = T[f["cod"]]
        assert t[7] is True, f"{f['cod']}: ficha não virou True"
        # U77 — sem V o status é PRESERVADO, nunca promovido (U42). A asserção não
        # fixa um valor: «candidato» (RC-931) é tão legítimo quanto «provisório»;
        # o que não pode é nascer «verificado» sem V do Curador.
        assert (t[4] == "verificado") == bool(aplicar_v), (
            f"{f['cod']}: status {t[4]!r} incompatível com aplicar_V={aplicar_v!r} "
            f"(sem V o status do cadastro é preservado, nunca promovido)")
        texto = _m.fm_toml(t, lote["data"]) + corpo(f, t, lote)
        arq = os.path.join(RAIZ, "termos", f"{f['cod']}-{f['slug']}.md")
        if os.path.exists(arq):
            # Só com --sobrescrever. É o ritual da PROVA DE REGENERAÇÃO: o JSON
            # do lote é a fonte da verdade e tem de voltar a gerar a ficha
            # byte a byte (despacho de 13/09/2026, U48).
            assert sobrescrever, (
                f"já existe: {arq} — use --sobrescrever para regerar pelo lote")
            _antigo = open(arq, encoding="utf-8").read()
            if _antigo == texto:
                print(f"  = termos/RC-{os.path.basename(arq)}: idêntico (nada a reescrever)")
                continue
            _salvo = arq + ".bak-u51"
            open(_salvo, "w", encoding="utf-8").write(_antigo)
            print(f"  ~ {os.path.basename(arq)}: REGERADO (cópia em "
                  f"{os.path.basename(_salvo)})")
        open(arq, "w", encoding="utf-8").write(texto)
        print(f"  ficha: termos/{os.path.basename(arq)} · {len(texto):,} B")
    print(f"\n{lote['unidade']}: {len(lote['fichas'])} fichas materializadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
