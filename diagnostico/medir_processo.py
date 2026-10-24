#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEDIDOR DO PROCESSO — Base Terminológica RC
================================================
Produz `medicoes.json` com as grandezas que sustentam o
`DIAGNOSTICO-DO-PROCESSO-2026-08-29.md`. Não escreve em nenhum outro lugar,
não altera nenhum arquivo do acervo e não decide nada: é instrumento de
medição, na régua da casa (número medido em arquivo relido, nunca de memória).

Rodar da raiz do repositório:
    python3 diagnostico/medir_processo.py

O que ele mede, e por quê:
  1. corpo      — o tamanho da esteira (ciclos engavetados, apostilas, aparatos)
  2. superficie — o custo de reconciliação (ciclos que tocam cada ficha)
  3. motor      — quanto do Python de um ciclo é máquina re-escrita (similaridade
                  entre cópias da mesma família de script) e quanto é decisão
  4. governanca — o imposto de leitura no início de sessão
  5. cadastro   — o estado verificativo da Base (índice mestre, fichas, malha)
"""
import glob
import json
import os
import re
import statistics as st
import subprocess
import sys
from pathlib import Path

# RAIZ resolvida subindo até achar `ferramentas/dados_termos.py`, para que o
# medidor funcione tanto na raiz quanto de dentro de uma pasta de ciclo.
def achar_raiz():
    d = os.path.abspath(os.path.dirname(__file__))
    while d != "/":
        if os.path.exists(os.path.join(d, "ferramentas", "dados_termos.py")):
            return d
        d = os.path.dirname(d)
    raise SystemExit("raiz não encontrada (ferramentas/dados_termos.py ausente acima de aqui)")

RAIZ = achar_raiz()
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
from caminhos_acervo import caminho_atual  # noqa: E402

RECEPCAO = os.fspath(caminho_atual("fonte.recepcao", Path(RAIZ)))
CONC = os.fspath(caminho_atual("fonte.apostilas_concluidas", Path(RAIZ)))
SIGLA_RE = re.compile(r"P?(20\d\d)-(\d\d)-(\d\d)")
GATE_RE = re.compile(r"portao|verificar|cobertura|auditor|aspas|cheque", re.I)


def _linhas(f):
    return len(open(f, encoding="utf-8", errors="ignore").read().splitlines())


def _bytes(f):
    return os.path.getsize(f) if os.path.exists(f) else 0


def ciclos():
    """Um registro por ciclo engavetado. O recorte entre `legado` e `nova fase`
    é feito pela marca do despacho (DECISAO-DO-CURADOR.md), não pela data —
    para que o corte não dependa da minha memória de quais ciclos foram quais."""
    out = []
    for p in sorted(glob.glob(os.path.join(CONC, "*"))):
        if not os.path.isdir(p):
            continue
        nome = os.path.basename(p)
        an = os.path.join(p, "analise")
        arquivos = sorted(os.listdir(an)) if os.path.isdir(an) else []
        py = [os.path.join(an, x) for x in arquivos if x.endswith(".py")]
        docs = [x for x in arquivos if x.endswith((".md", ".txt", ".json"))]
        port = [f for f in py if GATE_RE.search(os.path.basename(f))]
        pacote = [os.path.join(an, x) for x in arquivos
                  if x.startswith("_ampliac") or x.startswith("_pacote")]
        ap = os.path.join(p, "apostila.md")
        br = os.path.join(p, "original.txt")
        out.append(dict(
            ciclo=nome,
            data=nome[:10] if re.match(r"\d{4}-\d{2}-\d{2}", nome) else "?",
            despacho_formal=os.path.exists(os.path.join(p, "DECISAO-DO-CURADOR.md")),
            relatorio=any("RELATORIO" in x.upper() for x in arquivos),
            n_analise=len(arquivos),
            n_py=len(py),
            linhas_py=sum(_linhas(f) for f in py),
            n_portoes=len(port),
            linhas_portoes=sum(_linhas(f) for f in port),
            # linhas com código de termo ou aspa de fonte: o dado curatorial
            # embutido dentro do script, que é o que NÃO pode virar ferramenta
            linhas_dado=sum(1 for f in py
                            for l in open(f, encoding="utf-8", errors="ignore").read().splitlines()
                            if re.search(r"RC-\d{3}|«", l)),
            pacote_bytes=sum(_bytes(f) for f in pacote),
            docs_bytes=sum(_bytes(os.path.join(an, x)) for x in docs),
            apostila_bytes=_bytes(ap),
            apostila_linhas=_linhas(ap) if os.path.exists(ap) else 0,
            bruto_bytes=_bytes(br),
        ))
    return out


def superficie():
    """Quantos ciclos tocam cada ficha — a origem do custo que cresce mais rápido
    que o número de ciclos: cada ciclo novo tem de ser reconciliado com todos os
    que já passaram pela mesma ficha."""
    per_ficha = []
    por_ciclo = {}
    for f in glob.glob(os.path.join(RAIZ, "termos", "*.md")):
        t = open(f, encoding="utf-8", errors="ignore").read()
        se = re.findall(r"^## Ampliação — (P?\d{4}-\d{2}-\d{2})", t, re.M)
        per_ficha.append(len(se))
        for s in se:
            por_ciclo[s] = por_ciclo.get(s, 0) + 1
    from collections import Counter
    dist = Counter(per_ficha)
    return dict(
        fichas=len(per_ficha),
        secoes_total=sum(per_ficha),
        media_por_ficha=round(sum(per_ficha) / max(1, len(per_ficha)), 2),
        max_por_ficha=max(per_ficha) if per_ficha else 0,
        fichas_intocadas=dist[0],
        distribuicao={str(k): v for k, v in sorted(dist.items())},
        pares_a_reconciliar=sum(k * (k - 1) // 2 for k in per_ficha),
        ciclos_com_secao=len(por_ciclo),
        top10=dict(sorted(por_ciclo.items(), key=lambda x: -x[1])[:10]),
    )


def motor():
    """Similaridade entre as cópias do mesmo script nos ciclos com despacho.
    Família de igualdade alta (portões) = máquina que pode virar ferramenta.
    Família de igualdade baixa (geradores) = motor disfçado de conteúdo, porque a
    decisão foi escrita dentro do código em vez de num arquivo de configuração."""
    import difflib
    despachos = [c["data"] for c in ciclos() if c["despacho_formal"]]
    fam = {}
    for c in despachos:
        for f in glob.glob(os.path.join(CONC, "*%s*" % c, "analise", "*.py")):
            base = re.sub(r"[-_]?P?\d{4}[-_]\d{2}[-_]\d{2}", "", os.path.basename(f))
            fam.setdefault(base, []).append(f)
    res = {}
    for k, v in sorted(fam.items()):
        if len(v) < 2:
            continue
        ts = []
        for f in v:
            t = open(f, encoding="utf-8", errors="ignore").read()
            t = re.sub(r"\d{4}-\d{2}-\d{2}", "<C>", t)
            t = "\n".join(l.strip() for l in t.split("\n")
                          if l.strip() and not l.strip().startswith("#"))
            ts.append((len(t), t))
        ts.sort(reverse=True)
        pares = [round(100 * difflib.SequenceMatcher(None, ts[0][1], ts[i][1]).ratio())
                 for i in range(1, len(ts))]
        res[k] = dict(copias=len(v), bytes=[b for b, _ in ts],
                      igualdade_1x2=pares[0], igualdade_min=min(pares))
    return dict(ciclos_com_despacho=despachos, familias=res)


def governanca():
    def sz(*parts):
        return _bytes(os.path.join(RAIZ, *parts))

    cont = os.path.join(RAIZ, "admin", "logs", "CONTINUIDADE.md")
    txt = open(cont, encoding="utf-8", errors="ignore").read() if os.path.exists(cont) else ""
    blocos = [b for b in txt.split("\n\n") if b.strip()]
    cab = "\n\n".join(blocos[:4])
    arquivos = sorted(glob.glob(os.path.join(CONC, "*", "apostila.md")))
    return dict(
        PROMPT_bytes=sz("prompts", "PROMPT-PROXIMA-SESSAO.md"),
        CONTINUIDADE_bytes=len(txt.encode()),
        CONTINUIDADE_blocos=len(blocos),
        CONTINUIDADE_bytes_por_bloco=int(len(txt.encode()) / max(1, len(blocos))),
        cabecalho_bytes=len(cab.encode()),
        INDICE_RAIZ_bytes=sz("INDICE-PALESTRAS.md"),
        INDICE_APOSTILAS_bytes=sz("apostilas", "INDICE-PALESTRAS.md"),
        GUIA_bytes=sz("GUIA-MESTRE-RC-APOSTILA-v1.1.md"),
        CONVENCOES_bytes=sz("convencoes-editoriais-rc.md"),
        leitura_obrigatoria_bytes=sum([sz("prompts", "PROMPT-PROXIMA-SESSAO.md"), sz("admin", "logs", "CONTINUIDADE.md"),
                                      sz("INDICE-PALESTRAS.md"), sz("apostilas", "INDICE-PALESTRAS.md"),
                                      sz("GUIA-MESTRE-RC-APOSTILA-v1.1.md"),
                                      sz("convencoes-editoriais-rc.md")]),
        apostilas_no_acervo=len(arquivos),
        apostilas_total_bytes=sum(_bytes(f) for f in arquivos),
        apostilas_mediana_bytes=int(st.median([_bytes(f) for f in arquivos])) if arquivos else 0,
        apostilas_maxima_bytes=max([_bytes(f) for f in arquivos]) if arquivos else 0,
    )


def cadastro():
    im = os.path.join(RAIZ, "indice-mestre.md")
    linhas = [l for l in open(im, encoding="utf-8", errors="ignore").read().split("\n")
              if l.startswith("| RC-")] if os.path.exists(im) else []
    selo = {s: sum(1 for l in linhas if s in l) for s in ["⚪", "🟡", "🟠", "🟢"]}
    dt = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
    cad = open(dt, encoding="utf-8", errors="ignore").read() if os.path.exists(dt) else ""
    # a contagem autoritativa é a que o próprio cadastro imprime na validação
    try:
        v = subprocess.run([sys.executable, dt], capture_output=True, text=True,
                           cwd=RAIZ, timeout=180).stdout
    except Exception:
        v = ""
    mv = re.search(r"(\d+)\s*termos,\s*(\d+)\s*rela", v)
    fichas = glob.glob(os.path.join(RAIZ, "termos", "*.md"))
    up = glob.glob(os.path.join(RECEPCAO, "*.txt"))
    conc = {os.path.basename(p)[:10] for p in glob.glob(os.path.join(CONC, "*"))}
    pend = []
    for f in up:
        m = SIGLA_RE.search(os.path.basename(f))
        sigla = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m and all(m.groups()) else "?"
        if sigla not in conc:
            pend.append(dict(arquivo=os.path.basename(f), data=sigla, bytes=os.path.getsize(f)))
    return dict(
        termos_no_indice=len(linhas),
        status=selo,
        sem_verificacao=sum(1 for l in linhas if "🟢" not in l),
        cadastro_linhas=cad.count("\n") + 1,
        cadastro_bytes=len(cad.encode()),
        termos_na_malha=int(mv.group(1)) if mv else 0,
        relacoes_na_malha=int(mv.group(2)) if mv else 0,
        validacao_cadastro=v.strip().splitlines()[-1] if v.strip() else "",
        fichas_arquivo=len(fichas),
        fichas_sem_arquivo=max(0, len(linhas) - len(fichas)),
        uploads_recepcao_total=len(up),
        uploads_recepcao_sem_ciclo=len(pend),
        uploads_recepcao_bytes=sum(os.path.getsize(f) for f in up),
        obras_fisicas=len(glob.glob(os.path.join(RAIZ, "livros", "CONCLUIDOS", "*"))),
    )


def corpo(cs):
    d = lambda c: c["despacho_formal"]

    def med(sel, k):
        v = [c[k] for c in cs if sel(c)]
        return round(st.median(v), 1) if v else 0

    def soma(k):
        return sum(c[k] for c in cs)

    grupo = lambda sel: dict(
        ciclos=len([c for c in cs if sel(c)]),
        scripts_py=med(sel, "n_py"),
        linhas_py=med(sel, "linhas_py"),
        portoes=med(sel, "n_portoes"),
        pacote_bytes=med(sel, "pacote_bytes"),
        apostila_bytes=med(sel, "apostila_bytes"),
        bruto_bytes=med(sel, "bruto_bytes"),
        docs_aparato_bytes=med(sel, "docs_bytes"),
    )
    sem = lambda c: not d(c)
    nova = [c for c in cs if d(c)]
    return dict(
        ciclos=len(cs),
        ciclos_com_despacho=len(nova),
        ciclos_com_relatorio=sum(1 for c in cs if c["relatorio"]),
        comparativo=dict(legado=grupo(sem), nova_fase=grupo(d)),
        totais=dict(linhas_py=soma("linhas_py"),
                    linhas_py_nos_ciclos_com_despacho=sum(c["linhas_py"] for c in nova),
                    pacote_bytes=soma("pacote_bytes"),
                    docs_aparato_bytes=soma("docs_bytes"),
                    apostila_bytes=soma("apostila_bytes"),
                    bruto_bytes=soma("bruto_bytes")),
        linhas_por_ciclo=sorted((dict(ciclo=c["data"], scripts=c["n_py"], linhas=c["linhas_py"],
                                     portoes=c["n_portoes"], linhas_portoes=c["linhas_portoes"],
                                     dados_em_codigo=c["linhas_dado"], pacote=c["pacote_bytes"],
                                     apostila=c["apostila_bytes"], bruto=c["bruto_bytes"],
                                     despacho=c["despacho_formal"]) for c in cs),
                                key=lambda r: r["linhas"], reverse=True)[:12],
    )


def calcular():
    cs = ciclos()
    return dict(gerado_em="2026-08-29",
                metodo="leitura de arquivo por script; nenhum número digitado à mão",
                corpo=corpo(cs),
                superficie=superficie(),
                motor=motor(),
                governanca=governanca(),
                cadastro=cadastro(),
                ciclos=cs)


def tabela_md(R):
    a, b = R["corpo"]["comparativo"]["legado"], R["corpo"]["comparativo"]["nova_fase"]
    L = ["| grandeza (mediana por ciclo) | legado | nova fase | fator |", "|---|---|---|---|"]
    for k, rot in [("ciclos", "ciclos"), ("scripts_py", "scripts .py"),
                   ("linhas_py", "linhas de .py"), ("portoes", "portões"),
                   ("pacote_bytes", "pacote de aplicação (B)"),
                   ("docs_aparato_bytes", "docs de aparato (B)"),
                   ("apostila_bytes", "apostila (B)"), ("bruto_bytes", "bruto (B)")]:
        f = ("×%.1f" % (b[k] / a[k])) if a.get(k) else "—"
        L.append(f"| {rot} | {a[k]} | {b[k]} | {f} |")
    s, g, c = R["superficie"], R["governanca"], R["cadastro"]
    L.append("")
    L.append(f"Superfície de reconciliação: {s['secoes_total']} seções em {s['fichas']} fichas · "
             f"média {s['media_por_ficha']} · máx {s['max_por_ficha']} ciclos numa ficha · "
             f"**{s['pares_a_reconciliar']} pares** a reconciliar.")
    L.append(f"Leitura obrigatória de início de sessão: {g['leitura_obrigatoria_bytes']} B "
             f"(CONTINUIDADE {g['CONTINUIDADE_bytes']} B em {g['CONTINUIDADE_blocos']} blocos).")
    L.append(f"Estado verificativo: {c['status']} · sem selo de verificação: "
             f"{c['sem_verificacao']}/{c['termos_no_indice']} · fichas sem arquivo: "
             f"{c['fichas_sem_arquivo']}.")
    L.append(f"Malha: {c['validacao_cadastro']}")
    return "\n".join(L)


if __name__ == "__main__":
    R = calcular()
    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "medicoes.json")
    with open(destino, "w", encoding="utf-8") as fh:
        json.dump(R, fh, ensure_ascii=False, indent=1)
    print("escrito:", destino)
    print(tabela_md(R))
