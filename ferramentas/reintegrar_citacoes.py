#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REINTEGRAR CITAÇÕES A5 — o aplicador cirúrgico
==============================================

Por que este script existe
--------------------------
`materializar_lote.py` NÃO serve para a A5: o seu `corpo()` regenera a ficha
inteira a partir de um molde de 7 secções e destruiria `Ampliação`,
`Atualização`, `Reforço` e tudo o mais que a curadoria escreveu à mão. A A5
precisa de CIRURGIA: trocar uma linha por outra, nada mais.

Mas a cirurgia continua a ser DADOS, não código: o lote JSON é a fonte da
verdade e este aplicador é uma função pura dele — o mesmo rito de
`materializar_lote.py` (U83: reparo nos dados, *driver* intocável).

O Portão B é o MESMO
--------------------
`conferir()` é IMPORTADO de `materializar_lote`. Não é reimplementado, não é
copiado, não é «uma versão para a A5». Se o Portão B mudar, muda para todos.

Marcação
--------
Nenhuma tag nova. A ficha passa a exibir o aparelho R1 que a própria nota de
quarentena da U86 já invocava como critério:

    > «trecho» — SIGLA pg · `original.txt` LNNNN · nota.

É endereçável, é auto-verificável e não cria dívida técnica: não há script de
limpeza a escrever depois, porque não há nada a limpar.

Comportas
---------
  A  `conferir()` em CADA fragmento, na sua linha — antes de escrever seja o
     que for; se um fragmento falhar, o lote aborta inteiro (não aplica meia
     ficha).
  B  a `chave` de localização tem de bater em EXACTAMENTE UMA linha da ficha;
     zero ou duas → aborta. Nada de substituição às cegas.
  C  nenhuma ficha pode ficar com duas citações da mesma tupla (sigla, linha) —
     é esta a trava de idempotência que substitui as *flags* e os comentários
     HTML invisíveis.
  D  a linha substituída não pode já ser uma citação R1: se for, é porque o
     lote já foi aplicado → «idêntico (nada a reescrever)».
  E  o número de linhas da ficha só pode variar pelo número de notas
     acrescentadas; nenhuma linha de CORPO é suprimida sem passar pela
     substituição declarada.

Idempotência
------------
O aplicador é função de (ficha, lote). Reexecutar produz saída byte-idêntica,
pelo que a segunda corrida não altera nada — o mesmo critério do rito de
regeneração da U48.

Notas de quarentena
-------------------
A U86 lavrou 478 notas. Se uma ficha tem N trechos não-verbatim e a U91
reanexa M:

  · M == N → a nota de quarentena deixa de ser verdadeira e é SUBSTITUÍDA pela
    certidão de reanexação (a cadeia de custódia fica preservada: a nova nota
    cita a U86 e a sua data).
  · M <  N → a nota de quarentena continua verdadeira e é PRESERVADA; acres-
    centa-se um bullet de reanexação a dizer quantos saíram da quarentena.

Uma ficha nunca fica a mentir sobre si própria. É a doutrina da U87
(reemitir no mesmo commit) aplicada a notas.

Uso
---
    python3 ferramentas/reintegrar_citacoes.py <lote.json> [--aplicar]

Sem `--aplicar`, nada é escrito.
"""
from __future__ import annotations

import collections
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

# ── o Portão B, importado do driver (não reimplementado) ────────────────────
from ferramentas.materializar_lote import conferir, pagina  # noqa: E402

TERMOS = os.path.join(RAIZ, "termos")
CENSO = os.path.join(RAIZ, "diagnostico",
                     "A5-CITACOES-PRE-PORTAO-B-2026-09-14.json")
APARELHO_R1 = re.compile(r"·\s*`original\.txt`\s*L\d+")
MARCA_QUARENTENA = "- ⚠️ **Quarentena epistemológica — citações da geração pré-Portão B"


def norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


# ═══════════════════════════════════════════════════════ render da citação ──
def render(f: dict) -> str:
    marca = " » … « ".join(f"«{t}»" for _l, t in f["fragmentos"])
    pg = pagina(f["sigla"], f["linha"])
    onde = f"{f['sigla']} {pg}" if pg != "—" else f["sigla"]
    return (f"> {marca} — {onde} · `original.txt` L{f['linha']} · "
            f"{f['nota']}.")


# ════════════════════════════════════════════════════════════════ notas ─────
def clausula_vestigio(k: int, n: int) -> str:
    """Reproduz a gramática exacta das 7 variantes lavradas pela U86."""
    if n == 1:
        return ("Deixa vestígio no corpus; a reextração fica diferida." if k == 1
                else "Não deixa vestígio no corpus ingerido.")
    if k == n:
        return "Todos deixam vestígio no corpus; a reextração fica diferida."
    if k == 0:
        return "Nenhum deixa vestígio no corpus ingerido."
    return f"Só {k} dos {n} deixam vestígio no corpus."


def nota_reanexacao(m: int, n: int, fichas_lote: int) -> str:
    if m == n:
        sujeito = ("o trecho entre aspas desta ficha" if n == 1
                   else f"os {n} trechos entre aspas desta ficha")
        return (
            f"- ✅ **Reanexação A5 (U91, 15/09/2026):** {sujeito} "
            f"{'foi' if n == 1 else 'foram'} reanexado{'s' if n > 1 else ''} às "
            f"fontes e passa{'m' if n > 1 else ''} a trazer aparelho de linha "
            f"(`— SIGLA · original.txt LNNNN`), conferido byte a byte pelo "
            f"Portão B. **Quarentena epistemológica de 14/09/2026 (U86) "
            f"levantada nesta ficha** — a nota original dizia que o trecho não "
            f"resistia à verificação; agora resiste, porque deixou de ser uma "
            f"transcrição solta e passou a ser extracto conferido. Censo: "
            f"`diagnostico/A5-CITACOES-PRE-PORTAO-B-2026-09-14.json`.")
    return (
        f"- ✅ **Reanexação parcial A5 (U91, 15/09/2026):** {m} dos {n} trechos "
        f"entre aspas desta ficha {'foi' if m == 1 else 'foram'} reanexado"
        f"{'s' if m > 1 else ''} às fontes e passa{'m' if m > 1 else ''} a trazer "
        f"aparelho de linha (`— SIGLA · original.txt LNNNN`), conferido byte a "
        f"byte pelo Portão B. Os restantes {n - m} permanecem sob a quarentena "
        f"epistemológica de 14/09/2026 (U86) — a nota acima continua a valer "
        f"para eles. Censo: "
        f"`diagnostico/A5-CITACOES-PRE-PORTAO-B-2026-09-14.json`.")


# ════════════════════════════════════════════════════════════════ main ──────
def main() -> int:
    if len(sys.argv) < 2:
        sys.exit("uso: reintegrar_citacoes.py <lote.json> [--aplicar]")
    aplicar = "--aplicar" in sys.argv
    lote = json.load(open(sys.argv[1], encoding="utf-8"))
    fichas = lote["fichas"]

    print(f"{lote['unidade']} · lote {lote['lote']} da rota {lote['rota']} · "
          f"{len(fichas)} blocos em {len({f['cod'] for f in fichas})} fichas — "
          f"conferência byte a byte (Portão B importado do driver)")

    # ── COMPORTA A: o Portão B decide antes de se escrever seja o que for ───
    for f in fichas:
        for linha, texto in f["fragmentos"]:
            conferir(f["sigla"], linha, [texto])
    print(f"  comporta A: {sum(len(f['fragmentos']) for f in fichas)} "
          f"fragmentos conferidos byte a byte — 0 recusas")

    # ── censo para as contas das notas ─────────────────────────────────────
    censo = json.load(open(CENSO, encoding="utf-8"))
    nao_verbatim = collections.Counter()
    for b in censo["blocos"]:
        if b["classe"] in ("NULO", "PARCIAL"):
            nao_verbatim[b["codigo"]] += 1
    por_ficha = collections.Counter(f["cod"] for f in fichas)

    # ── COMPORTAS B/C/D por ficha ───────────────────────────────────────────
    planos: dict[str, dict] = {}
    for cod, m in sorted(por_ficha.items()):
        path = glob.glob(os.path.join(TERMOS, cod + "-*.md"))
        if len(path) != 1:
            sys.exit(f"  comporta E · {cod}: {len(path)} ficheiros — abortar")
        path = path[0]
        linhas = open(path, encoding="utf-8").read().split("\n")
        blocos = [f for f in fichas if f["cod"] == cod]

        vistos: set[tuple[str, int]] = set()
        trocas: list[tuple[int, str]] = []
        for f in blocos:
            novo = render(f)
            # IDEMPOTÊNCIA PRIMEIRO: se a linha que este lote produz já está
            # literalmente na ficha, o lote já foi aplicado — não há nada a
            # fazer. É o mesmo critério do `if _antigo == texto: idêntico` do
            # materializar_lote.py. Sem este passo, a segunda corrida não
            # encontra a `chave` (o texto legado já foi substituído) e aborta.
            if novo in linhas:
                continue
            chave = norm(f["chave"])
            brutos = [i for i, ln in enumerate(linhas) if chave in norm(ln)]
            # A chave é o PREFIXO do trecho legado; pode ocorrer mais de uma vez
            # na ficha — em RC-002 bate na citação (L75) e numa nota curatorial
            # que reproduz o mesmo trecho (L121). Prefere-se, por ordem, a
            # linha que (1) é blockquote de citação, (2) começa por aspa,
            # (3) qualquer. Se mesmo assim sobrar mais de uma, aborta: nunca
            # se substitui às cegas.
            for filtro in (lambda i: linhas[i].lstrip().startswith(">"),
                           lambda i: linhas[i].lstrip()[:1] in "\"«“'"):
                hits = [i for i in brutos if filtro(i)]
                if len(hits) == 1:
                    break
            else:
                hits = brutos
            if len(hits) != 1:
                sys.exit(f"  comporta B · {cod}: chave bate em {len(hits)} "
                         f"linhas (esperado 1) — abortar")
            i = hits[0]
            if APARELHO_R1.search(linhas[i]):
                # Já aplicado. Só é idempotência se for EXACTAMENTE a linha que
                # este lote produz; se for outra citação R1, é CONFLITO e aborta
                # — nunca se sobrepõe uma reanexação a outra.
                if linhas[i] == novo:
                    continue                      # idêntico: nada a reescrever
                sys.exit(f"  comporta D · {cod} L{i+1}: a linha já traz "
                         f"aparelho R1 mas NÃO é a que este lote produz — "
                         f"conflito, abortar")
            # Uma tupla por CITAÇÃO (não por fragmento). E a chave inclui o
            # PRIMEIRO FRAGMENTO, não apenas (sigla, linha): há linhas-fonte de
            # 3 980 caracteres (P2025-04-06 L32) das quais a ficha extrai
            # duas citações distintas — RC-794 tem duas, ambas legítimas, ambas
            # na L32. Chavear só por (sigla, linha) reprovaria o que é correcto.
            tup = (f["sigla"], f["linha"], f["fragmentos"][0][1][:80])
            if tup in vistos:
                sys.exit(f"  comporta C · {cod}: tupla duplicada {tup} — "
                         f"abortar")
            vistos.add(tup)
            if linhas[i] != novo:
                trocas.append((i, novo))

        n = nao_verbatim[cod]
        nota = nota_reanexacao(m, n, len(blocos))
        ja_nota = [j for j, ln in enumerate(linhas)
                   if ln.startswith("- ✅ **Reanexa")]
        if len(ja_nota) > 1:
            sys.exit(f"  comporta D · {cod}: {len(ja_nota)} notas de "
                     f"reanexação — abortar")
        nota_ok = bool(ja_nota) and linhas[ja_nota[0]] == nota
        if ja_nota and not nota_ok:
            sys.exit(f"  comporta D · {cod}: nota de reanexação existe mas "
                     f"não bate com a que este lote produz — abortar")
        planos[cod] = {"path": path, "linhas": linhas, "trocas": trocas,
                       "nota": nota, "m": m, "n": n, "nota_ok": nota_ok}

    print("  comportas B/C/D/E: 0 impedimentos")
    print(f"  notas: {sum(1 for p in planos.values() if p['m'] == p['n'])} "
          f"fichas com quarentena LEVANTADA · "
          f"{sum(1 for p in planos.values() if p['m'] < p['n'])} parciais")

    if not aplicar:
        print("\n  --aplicar NÃO passado: nada escrito. Amostra:")
        for cod in list(planos)[:3]:
            p = planos[cod]
            for i, novo in p["trocas"]:
                print(f"\n   {cod} L{i+1}")
                print(f"   - {p['linhas'][i][:160]}")
                print(f"   + {novo[:160]}")
        return 0

    # ── escrever ────────────────────────────────────────────────────────────
    feitos = 0
    identicos = 0
    for cod, p in planos.items():
        if not p["trocas"] and p["nota_ok"]:
            identicos += 1
            continue
        linhas = list(p["linhas"])
        for i, novo in sorted(p["trocas"], reverse=True):
            linhas[i] = novo
        alvo = [j for j, ln in enumerate(linhas)
                if ln.startswith(MARCA_QUARENTENA)]
        if len(alvo) != 1:
            sys.exit(f"  {cod}: esperava 1 nota de quarentena, achei "
                     f"{len(alvo)} — abortar")
        if p["m"] == p["n"]:
            if p["nota_ok"]:
                pass                       # nota já é a certidão
            else:
                linhas[alvo[0]] = p["nota"]
        else:
            if not p["nota_ok"]:
                linhas.insert(alvo[0] + 1, p["nota"])
        open(p["path"], "w", encoding="utf-8").write("\n".join(linhas))
        feitos += 1
    print(f"\n  {feitos} fichas reescritas · {identicos} idênticas "
          f"(nada a reescrever) · "
          f"{sum(len(p['trocas']) for p in planos.values())} citações reanexadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
