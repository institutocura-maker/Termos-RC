#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: DORMENTE-2026-09 (servidor HTTP; inviável no sandbox)
"""Visor somente-leitura do workspace da Base Terminológica RC.

Servidor HTTP em Python puro. Nunca grava, move ou apaga.
Funciona sem dependências; a biblioteca `markdown` é opcional.

Uso:
    python3 ferramentas/visor_workspace.py
    PORT=9090 python3 ferramentas/visor_workspace.py
"""

from __future__ import annotations

import html
import io
import os
import re
import sys
import traceback
import zipfile
from datetime import date
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
PORTA = int(os.environ.get("PORT", "8080"))
HOST = os.environ.get("HOST", "0.0.0.0")

OCULTAR_DIR = {
    ".git",
    ".arena",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}
OCULTAR_ARQ = {".DS_Store", "Thumbs.db", "desktop.ini"}

LIMITE_TEXTO = 2_000_000
LIMITE_PREVIEW = 200_000

TEXTO_EXT = {
    ".md", ".txt", ".py", ".csv", ".json", ".svg", ".html", ".htm",
    ".css", ".js", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".sh",
    ".xml", ".rst", ".log",
}
BAIXAR_EXT = {".docx", ".xlsx", ".pdf", ".zip", ".gz", ".7z"}
IMAGEM_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico"}

try:
    import markdown as _md_lib

    _MD_OK = True
except ImportError:
    _md_lib = None
    _MD_OK = False


# ---------------------------------------------------------------------------
# caminhos
# ---------------------------------------------------------------------------

def caminho_seguro(rel: str) -> Path:
    """Resolve um caminho relativo à raiz e recusa travessia."""
    rel = (rel or "").replace("\\", "/").lstrip("/")
    if rel in ("", ".", "./"):
        alvo = RAIZ
    else:
        alvo = (RAIZ / rel).resolve()
    raiz = RAIZ.resolve()
    try:
        alvo.relative_to(raiz)
    except ValueError as exc:
        raise PermissionError("fora da raiz do workspace") from exc
    return alvo


def rel_de(path: Path) -> str:
    raiz = RAIZ.resolve()
    path = path.resolve()
    if path == raiz:
        return ""
    return path.relative_to(raiz).as_posix()


def url_ver(rel: str) -> str:
    return "/?p=" + quote(rel, safe="/")


def url_baixar(rel: str, forcar: bool = False) -> str:
    u = "/baixar?p=" + quote(rel, safe="/")
    return u + "&dl=1" if forcar else u


def url_zip(rel: str = "") -> str:
    if rel:
        return "/zip?p=" + quote(rel, safe="/")
    return "/zip"


def nome_zip(rel: str = "") -> str:
    dia = date.today().isoformat()
    if rel:
        return f"{Path(rel).name}-{dia}.zip"
    return f"Termos-RC-workspace-{dia}.zip"


def link_dl(href: str, rotulo: str, nome_arq: str, cls: str = "btn") -> str:
    """Link de download que o JS intercepta (o iframe do preview bloqueia anexo nativo)."""
    return (
        f'<a class="{html.escape(cls)}" data-dl href="{html.escape(href, quote=True)}" '
        f'download="{html.escape(nome_arq)}" target="_blank" rel="noopener">'
        f"{html.escape(rotulo)}</a>"
    )


# ---------------------------------------------------------------------------
# util
# ---------------------------------------------------------------------------

def tam_humano(n: int) -> str:
    x = float(n)
    for u in ("B", "KB", "MB", "GB"):
        if abs(x) < 1024 or u == "GB":
            return f"{int(x)} {u}" if u == "B" else f"{x:.1f} {u}"
        x /= 1024
    return f"{x:.1f} GB"


def ler_texto(path: Path) -> str:
    bruto = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return bruto.decode(enc)
        except UnicodeDecodeError:
            continue
    return bruto.decode("utf-8", errors="replace")


def eh_oculto(nome: str, is_dir: bool) -> bool:
    if is_dir and nome in OCULTAR_DIR:
        return True
    if not is_dir and nome in OCULTAR_ARQ:
        return True
    return False


def listar(pasta: Path):
    itens = []
    try:
        for filho in pasta.iterdir():
            if eh_oculto(filho.name, filho.is_dir()):
                continue
            try:
                st = filho.stat()
            except OSError:
                continue
            itens.append((filho, filho.is_dir(), st.st_size))
    except OSError:
        return []
    itens.sort(key=lambda t: (not t[1], t[0].name.lower()))
    return itens


def arvore_pastas(niveis: int = 2):
    """Árvore só de pastas, até `niveis` a partir da raiz."""

    def andar(pasta: Path, nivel: int):
        saida = []
        for filho, is_dir, _tam in listar(pasta):
            if not is_dir:
                continue
            no = {
                "nome": filho.name,
                "rel": rel_de(filho),
                "filhos": andar(filho, nivel + 1) if nivel < niveis else [],
                "n_arq": 0,
                "n_dir": 0,
            }
            for n2, d2, _ in listar(filho):
                if d2:
                    no["n_dir"] += 1
                else:
                    no["n_arq"] += 1
            saida.append(no)
        return saida

    return andar(RAIZ, 1)


def iter_arquivos(pasta: Path):
    """Percorre arquivos visíveis (sem gravar nada)."""
    for dirpath, dirnames, filenames in os.walk(pasta):
        dirnames[:] = sorted(d for d in dirnames if d not in OCULTAR_DIR)
        base = Path(dirpath)
        for fn in sorted(filenames):
            if fn in OCULTAR_ARQ:
                continue
            path = base / fn
            if path.is_file():
                yield path


def montar_zip(pasta: Path, prefixo: str) -> bytes:
    """Monta o ZIP só na memória — o disco do workspace não é tocado."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for path in iter_arquivos(pasta):
            rel = path.relative_to(pasta).as_posix()
            arc = f"{prefixo}/{rel}" if prefixo else rel
            try:
                zf.write(path, arcname=arc)
            except OSError:
                continue
    return buf.getvalue()


def classe_ext(path: Path) -> str:
    ext = path.suffix.lower()
    if path.is_dir():
        return "dir"
    if ext == ".md":
        return "md"
    if ext in TEXTO_EXT:
        return "txt"
    if ext in BAIXAR_EXT:
        return "bin"
    if ext in IMAGEM_EXT:
        return "img"
    return "out"


# ---------------------------------------------------------------------------
# markdown — biblioteca opcional + renderizador de emergência
# ---------------------------------------------------------------------------

def md_emergencia(src: str) -> str:
    """Renderizador interno (off-grid). Tabelas, títulos, código, citações."""
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    if src.startswith("\ufeff"):
        src = src[1:]

    stash: list[str] = []

    def guardar(frag: str) -> str:
        stash.append(frag)
        return f"@@PH{len(stash) - 1}@@"

    def cerca(m: re.Match) -> str:
        lang = html.escape((m.group(1) or "").strip())
        corpo = html.escape(m.group(2).rstrip("\n"))
        return guardar(
            f'<pre class="code"><code data-lang="{lang}">{corpo}</code></pre>'
        )

    src = re.sub(r"```([^\n]*)\n(.*?)```", cerca, src, flags=re.S)

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", s)
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            r'<a href="\2">\1</a>',
            s,
        )
        return s

    def eh_sep_tabela(linha: str) -> bool:
        t = linha.strip()
        if "|" not in t:
            return False
        t = t.strip("|").strip()
        partes = [p.strip() for p in t.split("|")]
        if not partes:
            return False
        return all(re.fullmatch(r":?-{3,}:?", p.replace(" ", "")) for p in partes)

    def tabela(linhas_tab: list[str]) -> str:
        if len(linhas_tab) < 2:
            return ""
        cab = [c.strip() for c in linhas_tab[0].strip().strip("|").split("|")]
        corpo = linhas_tab[2:]
        th = "".join(f"<th>{inline(c)}</th>" for c in cab)
        trs = []
        for ln in corpo:
            cols = [c.strip() for c in ln.strip().strip("|").split("|")]
            tds = "".join(f"<td>{inline(c)}</td>" for c in cols)
            trs.append(f"<tr>{tds}</tr>")
        return (
            '<div class="tbl-wrap"><table>'
            f"<thead><tr>{th}</tr></thead>"
            f"<tbody>{''.join(trs)}</tbody>"
            "</table></div>"
        )

    linhas = src.split("\n")
    out: list[str] = []
    i = 0
    n = len(linhas)
    while i < n:
        ln = linhas[i]
        if ln.strip() == "":
            i += 1
            continue

        m = re.match(r"@@PH(\d+)@@\s*$", ln.strip())
        if m:
            out.append(stash[int(m.group(1))])
            i += 1
            continue

        if ln.startswith("#"):
            m = re.match(r"^(#{1,6})\s+(.*)$", ln)
            if m:
                nv = len(m.group(1))
                out.append(f"<h{nv}>{inline(m.group(2).rstrip('#').strip())}</h{nv}>")
                i += 1
                continue

        if re.match(r"^\s*([-*_])\1{2,}\s*$", ln):
            out.append("<hr>")
            i += 1
            continue

        if "|" in ln and i + 1 < n and eh_sep_tabela(linhas[i + 1]):
            bloco = [ln]
            i += 1
            while i < n and ("|" in linhas[i] or eh_sep_tabela(linhas[i])):
                bloco.append(linhas[i])
                i += 1
            out.append(tabela(bloco))
            continue

        if ln.lstrip().startswith(">"):
            cit = []
            while i < n and linhas[i].lstrip().startswith(">"):
                cit.append(re.sub(r"^\s*>\s?", "", linhas[i]))
                i += 1
            inner = "<br>".join(inline(c) if c.strip() else "" for c in cit)
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        mlist = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", ln)
        if mlist:
            ordered = bool(re.match(r"\d+\.", mlist.group(2)))
            tag = "ol" if ordered else "ul"
            itens_li = []
            while i < n:
                mm = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", linhas[i])
                if not mm:
                    if linhas[i].strip() == "":
                        break
                    break
                itens_li.append(f"<li>{inline(mm.group(3))}</li>")
                i += 1
            out.append(f"<{tag}>{''.join(itens_li)}</{tag}>")
            continue

        para = [ln]
        i += 1
        while i < n and linhas[i].strip() and not linhas[i].startswith("#"):
            if linhas[i].lstrip().startswith(">"):
                break
            if re.match(r"^(\s*)([-*+]|\d+\.)\s+", linhas[i]):
                break
            if linhas[i].startswith("```"):
                break
            if re.match(r"@@PH\d+@@\s*$", linhas[i].strip()):
                break
            if "|" in linhas[i] and i + 1 < n and eh_sep_tabela(linhas[i + 1]):
                break
            para.append(linhas[i])
            i += 1
        out.append("<p>" + "<br>".join(inline(p) for p in para) + "</p>")

    html_final = "\n".join(out)
    html_final = re.sub(
        r"@@PH(\d+)@@", lambda m: stash[int(m.group(1))], html_final
    )
    return html_final


def render_markdown(src: str) -> tuple[str, str]:
    """Retorna (html, origem) — origem = 'markdown' ou 'emergencia'."""
    if _MD_OK:
        try:
            ext = ["tables", "fenced_code", "sane_lists"]
            try:
                html_out = _md_lib.markdown(src, extensions=ext + ["nl2br"])
            except Exception:
                html_out = _md_lib.markdown(src, extensions=ext)
            return html_out, "markdown"
        except Exception:
            pass
    return md_emergencia(src), "emergencia"


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

CSS = """
:root {
  --bg: #121018;
  --bg-side: #1a1624;
  --bg-elev: #221c2e;
  --bg-hover: #2e2740;
  --bg-code: #0d0b12;
  --text: #f2ebe4;
  --text-dim: #c4b8c0;
  --text-mute: #8f8696;
  --sand: #e0c9a0;
  --sand-hi: #f3e2c4;
  --lilac: #cfc0de;
  --border: #3a3348;
  --quote: #8b6f9e;
  --ok: #9dba9a;
  --dir: #cfc0de;
  --warn: #d4a574;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; height: 100%; }
body {
  font-family: "Segoe UI", "Noto Sans", "Liberation Sans", system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  font-size: 16px;
  line-height: 1.55;
}
a { color: var(--sand); text-decoration: none; }
a:hover { color: var(--sand-hi); text-decoration: underline; }
code, pre, .mono { font-family: "Cascadia Code", "Consolas", "Liberation Mono", monospace; }
.app { display: flex; height: 100%; min-height: 100vh; }
.side {
  width: 280px; min-width: 220px; max-width: 360px;
  background: var(--bg-side);
  border-right: 1px solid var(--border);
  overflow: auto;
  padding: 0 0 24px;
}
.side-head {
  padding: 16px 16px 10px;
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; background: var(--bg-side); z-index: 2;
}
.side-head h1 {
  margin: 0 0 4px; font-size: 15px; letter-spacing: .04em;
  color: var(--sand); font-weight: 650; text-transform: uppercase;
}
.side-head p { margin: 0; font-size: 12px; color: var(--text-mute); }
.tree { list-style: none; margin: 8px 0 0; padding: 0 8px; }
.tree ul { list-style: none; margin: 0; padding: 0 0 0 14px; }
.tree a, .tree .leaf {
  display: flex; align-items: baseline; gap: 6px;
  padding: 4px 8px; border-radius: 6px;
  color: var(--lilac); font-size: 13.5px;
}
.tree a:hover { background: var(--bg-hover); text-decoration: none; color: var(--sand-hi); }
.tree .on { background: var(--bg-elev); color: var(--sand-hi); }
.tree .meta { color: var(--text-mute); font-size: 11px; margin-left: auto; }
.main { flex: 1; overflow: auto; min-width: 0; }
.top {
  position: sticky; top: 0; z-index: 3;
  background: #16121e;
  border-bottom: 1px solid var(--border);
  padding: 10px 22px;
  display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
}
.top-acoes { display: flex; align-items: center; gap: 8px; margin-left: auto; flex-wrap: wrap; }
.crumbs { display: flex; flex-wrap: wrap; gap: 4px; align-items: center; font-size: 14px; }
.crumbs a { color: var(--lilac); }
.crumbs span.sep { color: var(--text-mute); }
.crumbs strong { color: var(--sand-hi); font-weight: 600; }
.badge {
  font-size: 11px; letter-spacing: .04em; text-transform: uppercase;
  border: 1px solid var(--border); color: var(--text-mute);
  padding: 2px 8px; border-radius: 999px;
}
.badge.ok { color: var(--ok); border-color: #3d5340; }
.content { padding: 22px 28px 64px; max-width: 1100px; }
.filtro {
  width: 100%; max-width: 360px; margin: 0 0 14px;
  background: var(--bg-elev); color: var(--text);
  border: 1px solid var(--border); border-radius: 8px;
  padding: 8px 12px; font-size: 14px;
}
.filtro:focus { outline: 1px solid var(--sand); }
table.dir { width: 100%; border-collapse: collapse; font-size: 14.5px; }
table.dir th {
  text-align: left; font-size: 11px; letter-spacing: .06em; text-transform: uppercase;
  color: var(--text-mute); font-weight: 600;
  padding: 6px 10px; border-bottom: 1px solid var(--border);
}
table.dir td { padding: 7px 10px; border-bottom: 1px solid #2a2436; }
table.dir tr:hover td { background: var(--bg-elev); }
table.dir .n { color: var(--text-mute); font-variant-numeric: tabular-nums; white-space: nowrap; }
.ico { display: inline-block; width: 1.2em; color: var(--text-mute); }
.ico.dir { color: var(--dir); }
.ico.md { color: var(--sand); }
.meta-bar {
  display: flex; flex-wrap: wrap; gap: 10px 18px;
  color: var(--text-dim); font-size: 13px;
  margin: 0 0 18px; padding: 10px 14px;
  background: var(--bg-elev); border-radius: 8px; border: 1px solid var(--border);
}
.acoes { display: flex; gap: 10px; flex-wrap: wrap; }
.btn {
  display: inline-block; padding: 6px 12px; border-radius: 8px;
  border: 1px solid var(--border); color: var(--sand); background: var(--bg-elev);
  font-size: 13px;
}
.btn:hover { background: var(--bg-hover); text-decoration: none; color: var(--sand-hi); }
.btn.zip { border-color: #6a5a40; }
.btn.busy { opacity: .55; pointer-events: none; }
table.dir td.acao { width: 1%; white-space: nowrap; text-align: right; }
table.dir a.dl { font-size: 12.5px; padding: 3px 8px; }
#dl-status {
  flex: 1 1 100%; font-size: 13px; color: var(--sand-hi);
  background: #2a2114; border: 1px solid #5a4630;
  border-radius: 8px; padding: 6px 10px;
}
#dl-status[hidden] { display: none; }
#dl-caixa {
  margin: 0 0 16px; padding: 16px 18px;
  background: #2a2114; border: 1px solid #6a5a40; border-radius: 10px;
}
#dl-caixa[hidden] { display: none; }
#dl-caixa p { margin: 0 0 10px; color: var(--sand-hi); }
#dl-caixa-link {
  display: inline-block; padding: 10px 18px; border-radius: 8px;
  background: var(--sand); color: #121018; font-weight: 650;
}
#dl-caixa-link:hover { background: var(--sand-hi); color: #121018; text-decoration: none; }
#dl-caixa-pasta {
  display: inline-block; margin-left: 10px; padding: 10px 14px; border-radius: 8px;
  border: 1px solid var(--border); color: var(--sand);
}
#dl-caixa-pasta[hidden] { display: none; }
#dl-caixa-pasta:hover { background: var(--bg-hover); text-decoration: none; }
.md h1, .md h2, .md h3, .md h4 { color: var(--sand-hi); line-height: 1.3; }
.md h1 { font-size: 1.7em; border-bottom: 1px solid var(--border); padding-bottom: .25em; }
.md h2 { font-size: 1.35em; margin-top: 1.4em; }
.md h3 { font-size: 1.15em; color: var(--lilac); }
.md p { color: var(--text); }
.md a { color: var(--sand); }
.md blockquote {
  margin: 1em 0; padding: .4em 1em;
  border-left: 4px solid var(--quote);
  background: #1c1826; color: var(--text-dim);
}
.md pre, pre.code, .fonte pre {
  background: var(--bg-code); border: 1px solid var(--border);
  border-radius: 8px; padding: 12px 14px; overflow: auto;
  font-size: 13.2px; line-height: 1.45; color: var(--text);
}
.md code, p code, li code {
  background: #2a2236; color: var(--sand-hi);
  padding: .1em .35em; border-radius: 4px; font-size: .92em;
}
.md pre code { background: none; padding: 0; color: var(--text); }
.md .tbl-wrap, .md table { overflow-x: auto; }
.md table {
  border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 14.5px;
}
.md th, .md td { border: 1px solid var(--border); padding: 6px 10px; vertical-align: top; }
.md th { background: var(--bg-elev); color: var(--sand); text-align: left; }
.md tr:nth-child(even) td { background: #191522; }
.md hr { border: 0; border-top: 1px solid var(--border); margin: 1.6em 0; }
.aviso {
  background: #2a2114; border: 1px solid #5a4630; color: var(--warn);
  padding: 10px 14px; border-radius: 8px; margin-bottom: 14px;
}
.card-dl {
  background: var(--bg-elev); border: 1px solid var(--border);
  border-radius: 12px; padding: 22px; max-width: 560px;
}
.card-dl h2 { margin: 0 0 8px; color: var(--sand-hi); font-size: 1.2em; }
img.preview {
  max-width: 100%; height: auto; border: 1px solid var(--border);
  border-radius: 8px; background: #000;
}
svg.inline-svg { max-width: 100%; background: #fff; border-radius: 8px; }
.rodape {
  margin-top: 36px; padding-top: 12px; border-top: 1px solid var(--border);
  color: var(--text-mute); font-size: 12px;
}
"""

JS = r"""
(function () {
  var f = document.getElementById('filtro');
  if (f) {
    f.addEventListener('input', function () {
      var q = f.value.toLowerCase();
      document.querySelectorAll('table.dir tbody tr').forEach(function (tr) {
        var nome = (tr.getAttribute('data-nome') || '').toLowerCase();
        tr.style.display = nome.indexOf(q) === -1 ? 'none' : '';
      });
    });
  }

  var pendente = { url: '', nome: '', blob: null };

  function status(msg) {
    var el = document.getElementById('dl-status');
    if (!el) return;
    if (msg) { el.hidden = false; el.textContent = msg; }
    else { el.hidden = true; el.textContent = ''; }
  }

  function caixa(url, nome, blob) {
    pendente.url = url;
    pendente.nome = nome;
    pendente.blob = blob || null;
    var box = document.getElementById('dl-caixa');
    var link = document.getElementById('dl-caixa-link');
    var pasta = document.getElementById('dl-caixa-pasta');
    if (!box || !link) return;
    link.href = url;
    link.target = '_blank';
    link.rel = 'noopener';
    link.removeAttribute('download');
    link.removeAttribute('data-dl');
    link.textContent = 'Abrir e salvar ' + nome;
    if (pasta) {
      pasta.hidden = !window.showSaveFilePicker;
    }
    box.hidden = false;
    try { box.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); } catch (e) {}
  }

  var link = document.getElementById('dl-caixa-link');
  if (link) {
    link.addEventListener('click', function (ev) {
      ev.stopPropagation();
    });
  }

  var pastaBtn = document.getElementById('dl-caixa-pasta');
  if (pastaBtn) {
    pastaBtn.addEventListener('click', function (ev) {
      ev.preventDefault();
      ev.stopPropagation();
      if (!window.showSaveFilePicker) return;
      if (!pendente.blob) {
        status('Ainda nao tenho o arquivo em memoria. Use o botao dourado.');
        return;
      }
      var opts = { suggestedName: pendente.nome || 'download' };
      window.showSaveFilePicker(opts).then(function (handle) {
        return handle.createWritable().then(function (wri) {
          return wri.write(pendente.blob).then(function () { return wri.close(); });
        });
      }).then(function () {
        status('Salvo: ' + pendente.nome);
      }).catch(function (err) {
        if (err && err.name === 'AbortError') {
          status('Gravacao cancelada.');
          return;
        }
        status('Este painel nao deixou escolher a pasta. Use o botao dourado (nova aba).');
      });
    });
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('a[data-dl]');
    if (!a) return;
    ev.preventDefault();
    var url = a.href;
    var nome = a.getAttribute('download') || 'download';
    var zip = url.indexOf('/zip') !== -1;

    status(zip
      ? 'Preparando o ZIP… em seguida aparece o botao dourado.'
      : 'Preparando ' + nome + '…');
    a.classList.add('busy');

    fetch(url, { credentials: 'same-origin' })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.blob();
      })
      .then(function (blob) {
        caixa(url, nome, blob);
        status('Pronto. Clique no botao dourado — abre uma nova aba para salvar. Se a aba so mostrar o arquivo, use Ctrl+S.');
      })
      .catch(function () {
        caixa(url, nome, null);
        status('Nao deu para preparar aqui. Clique no botao dourado para abrir o arquivo numa nova aba.');
      })
      .finally(function () { a.classList.remove('busy'); });
  });
})();
"""


def acoes_padrao(rel: str = "", is_dir: bool = True, is_file: bool = False) -> str:
    bits = ['<span class="badge ok">somente leitura</span>']
    if is_file and rel:
        bits.append(link_dl(url_baixar(rel, True), "baixar arquivo", Path(rel).name))
    bits.append(
        link_dl(url_zip(), "workspace .zip", nome_zip(), "btn zip")
    )
    if is_dir and rel:
        bits.append(link_dl(url_zip(rel), "esta pasta .zip", nome_zip(rel)))
    return f'<div class="top-acoes">{"".join(bits)}</div>'


def pagina(titulo: str, crumbs: str, corpo: str, badge: str = "") -> bytes:
    html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} · Workspace RC</title>
<style>{CSS}</style>
</head>
<body>
<div class="app">
<aside class="side">
  <div class="side-head">
    <h1>Workspace RC</h1>
    <p>somente leitura · raiz do repositório</p>
  </div>
  {html_arvore()}
</aside>
<div class="main">
  <div class="top">
    <nav class="crumbs">{crumbs}</nav>
    {badge}
    <div id="dl-status" hidden></div>
  </div>
  <div class="content">
    <div id="dl-caixa" hidden>
      <p>O arquivo está pronto. Este painel bloqueia o download automático — use um dos botões:</p>
      <p>
        <a id="dl-caixa-link" href="#" target="_blank" rel="noopener">Abrir e salvar</a>
        <a id="dl-caixa-pasta" href="#" hidden>escolher pasta…</a>
      </p>
      <p style="font-size:13px;color:var(--text-mute);margin:10px 0 0">Se abrir uma aba nova e o arquivo não descer sozinho, use Ctrl+S (Salvar como).</p>
    </div>
    {corpo}
    <div class="rodape">Visor somente-leitura — não grava, não move, não apaga.
    Tema escuro em areia/lilás (sem azul intenso). Porta {PORTA}.</div>
  </div>
</div>
</div>
<script>{JS}</script>
</body>
</html>"""
    return html_doc.encode("utf-8")


def html_arvore() -> str:
    nos = arvore_pastas(2)

    def no_html(no: dict, atual: str = "") -> str:
        cls = "on" if False else ""
        meta_partes = []
        if no["n_dir"]:
            meta_partes.append(f"{no['n_dir']} pastas")
        if no["n_arq"]:
            meta_partes.append(f"{no['n_arq']} arq.")
        meta = " · ".join(meta_partes)
        filhos = ""
        if no["filhos"]:
            filhos = "<ul>" + "".join(no_html(f) for f in no["filhos"]) + "</ul>"
        return (
            f'<li><a class="{cls}" href="{url_ver(no["rel"])}">'
            f'<span class="ico dir">▸</span>{html.escape(no["nome"])}'
            f'<span class="meta">{html.escape(meta)}</span></a>{filhos}</li>'
        )

    itens = "".join(no_html(n) for n in nos)
    return (
        f'<ul class="tree">'
        f'<li><a href="/"><span class="ico dir">▸</span>raiz'
        f'<span class="meta">repositório</span></a></li>'
        f"{itens}</ul>"
    )


def migalhas(rel: str) -> str:
    partes = [p for p in rel.split("/") if p]
    bits = [f'<a href="/">raiz</a>']
    acc = []
    for i, p in enumerate(partes):
        acc.append(p)
        caminho = "/".join(acc)
        if i == len(partes) - 1:
            bits.append('<span class="sep">/</span>')
            bits.append(f"<strong>{html.escape(p)}</strong>")
        else:
            bits.append('<span class="sep">/</span>')
            bits.append(f'<a href="{url_ver(caminho)}">{html.escape(p)}</a>')
    return "".join(bits)


def corpo_diretorio(pasta: Path) -> str:
    itens = listar(pasta)
    if not itens:
        return "<p>Pasta vazia (ou só com itens ocultos).</p>"
    linhas = []
    for filho, is_dir, tam in itens:
        rel = rel_de(filho)
        kind = classe_ext(filho)
        ico = "▸" if is_dir else "·"
        nome = filho.name + ("/" if is_dir else "")
        tipo = "pasta" if is_dir else (filho.suffix.lower() or "arquivo").lstrip(".")
        href = url_ver(rel)
        if is_dir:
            acao = link_dl(url_zip(rel), "zip", nome_zip(rel), "btn dl")
        else:
            acao = link_dl(url_baixar(rel, True), "baixar", filho.name, "btn dl")
        linhas.append(
            f'<tr data-nome="{html.escape(filho.name)}">'
            f'<td><span class="ico {kind}">{ico}</span> '
            f'<a href="{href}">{html.escape(nome)}</a></td>'
            f'<td class="n">{html.escape(tipo)}</td>'
            f'<td class="n">{"" if is_dir else tam_humano(tam)}</td>'
            f'<td class="acao">{acao}</td>'
            f"</tr>"
        )
    return (
        f'<input class="filtro" id="filtro" type="search" '
        f'placeholder="filtrar {len(itens)} itens…" autocomplete="off">'
        f'<table class="dir"><thead><tr>'
        f"<th>nome</th><th>tipo</th><th>tamanho</th><th></th>"
        f"</tr></thead><tbody>{''.join(linhas)}</tbody></table>"
    )


def corpo_texto(path: Path, rel: str) -> str:
    tam = path.stat().st_size
    truncado = False
    if tam > LIMITE_TEXTO:
        texto = path.read_bytes()[:LIMITE_PREVIEW].decode("utf-8", errors="replace")
        truncado = True
    else:
        texto = ler_texto(path)
    n_lin = texto.count("\n") + (0 if texto.endswith("\n") or texto == "" else 1)
    if texto == "":
        n_lin = 0
    n_car = len(texto)
    ext = path.suffix.lower()
    aviso = ""
    if truncado:
        aviso = (
            f'<div class="aviso">Arquivo grande ({tam_humano(tam)}). '
            f"Mostrando só os primeiros {tam_humano(LIMITE_PREVIEW)}. "
            f'{link_dl(url_baixar(rel, True), "baixar integral", path.name)}.</div>'
        )

    meta = (
        f'<div class="meta-bar">'
        f"<span>{n_lin} linhas</span>"
        f"<span>{n_car} caracteres</span>"
        f"<span>{tam_humano(tam)}</span>"
        f'<span class="acoes">{link_dl(url_baixar(rel, True), "baixar", path.name)}</span>'
        f"</div>"
    )

    if ext == ".md":
        html_md, origem = render_markdown(texto)
        selo = "extensão markdown" if origem == "markdown" else "renderizador interno"
        return (
            aviso + meta
            + f'<p class="badge">{html.escape(selo)}</p>'
            + f'<article class="md">{html_md}</article>'
        )

    if ext == ".csv":
        return aviso + meta + render_csv(texto)

    if ext == ".json":
        return aviso + meta + render_json(texto)

    if ext == ".svg":
        # SVG local: preview + fonte
        preview = (
            f'<p>pré-visualização</p>'
            f'<img class="preview" alt="SVG" src="{url_baixar(rel)}">'
        )
        return aviso + meta + preview + fonte_pre(texto)

    return aviso + meta + fonte_pre(texto)


def fonte_pre(texto: str) -> str:
    return f'<div class="fonte"><pre>{html.escape(texto)}</pre></div>'


def render_csv(texto: str) -> str:
    linhas = texto.splitlines()
    if not linhas:
        return "<p>CSV vazio.</p>"
    # parser simples (não cobre aspas aninhadas complexas — suficiente p/ a base)
    def split_csv(ln: str) -> list[str]:
        return [c.strip() for c in ln.split(",")]

    cab = split_csv(linhas[0])
    th = "".join(f"<th>{html.escape(c)}</th>" for c in cab)
    trs = []
    max_lin = min(len(linhas), 501)
    for ln in linhas[1:max_lin]:
        cols = split_csv(ln)
        trs.append("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in cols) + "</tr>")
    extra = ""
    if len(linhas) > 501:
        extra = f"<p>… {len(linhas) - 501} linhas omitidas na tabela (arquivo completo no download).</p>"
    return (
        f'<article class="md"><div class="tbl-wrap"><table>'
        f"<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody>"
        f"</table></div>{extra}</article>"
    )


def render_json(texto: str) -> str:
    import json

    try:
        obj = json.loads(texto)
        pretty = json.dumps(obj, ensure_ascii=False, indent=2)
        return fonte_pre(pretty)
    except Exception:
        return '<div class="aviso">JSON inválido — exibindo fonte bruta.</div>' + fonte_pre(texto)


def corpo_binario(path: Path, rel: str) -> str:
    ext = path.suffix.lower().lstrip(".") or "arquivo"
    tam = tam_humano(path.stat().st_size)
    return (
        f'<div class="card-dl">'
        f"<h2>Download</h2>"
        f"<p>Arquivo <strong>{html.escape(path.name)}</strong> "
        f"({html.escape(ext.upper())}, {html.escape(tam)}).</p>"
        f"<p>DOCX, XLSX e PDF não são renderizados aqui — só baixados "
        f"(somente leitura; o visor não altera o disco).</p>"
        f"<p>{link_dl(url_baixar(rel, True), 'baixar ' + path.name, path.name)}</p>" 
        f"</div>"
    )


def corpo_imagem(path: Path, rel: str) -> str:
    tam = tam_humano(path.stat().st_size)
    return (
        f'<div class="meta-bar"><span>{html.escape(tam)}</span>'
        f'{link_dl(url_baixar(rel, True), "baixar", path.name)}</div>'
        f'<img class="preview" alt="{html.escape(path.name)}" src="{url_baixar(rel)}">'
    )


def mime_de(path: Path) -> str:
    ext = path.suffix.lower()
    return {
        ".md": "text/markdown; charset=utf-8",
        ".txt": "text/plain; charset=utf-8",
        ".py": "text/plain; charset=utf-8",
        ".csv": "text/csv; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml",
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    }.get(ext, "application/octet-stream")


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

class Handler(BaseHTTPRequestHandler):
    server_version = "VisorRC/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _html(self, code: int, corpo: bytes):
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(corpo)

    def _erro(self, code: int, msg: str):
        corpo = pagina(
            f"erro {code}",
            '<a href="/">raiz</a>',
            f'<div class="aviso">{html.escape(msg)}</div>',
        )
        self._html(code, corpo)

    def do_GET(self):
        try:
            self._get()
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            return
        except PermissionError:
            try:
                self._erro(403, "Caminho fora da raiz do workspace.")
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                return
        except FileNotFoundError:
            try:
                self._erro(404, "Arquivo ou pasta não encontrado.")
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                return
        except Exception:
            traceback.print_exc()
            try:
                self._erro(500, "Falha interna do visor (nada foi gravado no disco).")
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                return

    def _enviar(self, data: bytes):
        view = memoryview(data)
        passo = 64 * 1024
        for i in range(0, len(view), passo):
            self.wfile.write(view[i : i + passo])
        try:
            self.wfile.flush()
        except Exception:
            pass

    def do_HEAD(self):
        self.do_GET()

    def do_POST(self):
        self._erro(405, "Somente leitura: POST recusado.")

    def do_PUT(self):
        self._erro(405, "Somente leitura: PUT recusado.")

    def do_DELETE(self):
        self._erro(405, "Somente leitura: DELETE recusado.")

    def _get(self):
        u = urlparse(self.path)
        qs = parse_qs(u.query)
        rel = unquote(qs.get("p", [""])[0])

        if u.path == "/baixar":
            self._baixar(rel, forcar=bool(qs.get("dl")))
            return
        if u.path == "/zip":
            self._zip(rel)
            return
        if u.path not in ("/", "/index.html"):
            self._erro(404, "Rota inexistente.")
            return

        alvo = caminho_seguro(rel)
        if not alvo.exists():
            raise FileNotFoundError(rel)
        if alvo.is_dir():
            titulo = alvo.name if rel else "raiz"
            topo = acoes_padrao(rel, is_dir=True, is_file=False)
            self._html(200, pagina(titulo, migalhas(rel), corpo_diretorio(alvo), topo))
            return

        ext = alvo.suffix.lower()
        titulo = alvo.name
        crumbs = migalhas(rel)
        topo = acoes_padrao(rel, is_dir=False, is_file=True)
        if ext in BAIXAR_EXT:
            corpo = corpo_binario(alvo, rel)
        elif ext in IMAGEM_EXT:
            corpo = corpo_imagem(alvo, rel)
        elif ext in TEXTO_EXT or not ext:
            # sem extensão: tenta texto
            corpo = corpo_texto(alvo, rel)
        else:
            corpo = corpo_binario(alvo, rel)
        self._html(200, pagina(titulo, crumbs, corpo, topo))

    def _baixar(self, rel: str, forcar: bool = False):
        alvo = caminho_seguro(rel)
        if not alvo.exists() or not alvo.is_file():
            raise FileNotFoundError(rel)
        data = alvo.read_bytes()
        nome = alvo.name.replace('"', "")
        ext = alvo.suffix.lower()
        if forcar:
            ctype = "application/octet-stream"
            disposicao = "attachment"
        elif ext in IMAGEM_EXT or ext == ".svg":
            ctype = mime_de(alvo)
            disposicao = "inline"
        else:
            ctype = mime_de(alvo)
            disposicao = "attachment"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header(
            "Content-Disposition", f'{disposicao}; filename="{nome}"'
        )
        self.send_header("Access-Control-Expose-Headers", "Content-Disposition")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self._enviar(data)

    def _zip(self, rel: str):
        alvo = caminho_seguro(rel)
        if not alvo.exists():
            raise FileNotFoundError(rel)
        if alvo.is_file():
            alvo = alvo.parent
            rel = rel_de(alvo)
        if rel:
            prefixo = alvo.name
            nome = f"{alvo.name}-{date.today().isoformat()}.zip"
        else:
            prefixo = "Termos-RC"
            nome = f"Termos-RC-workspace-{date.today().isoformat()}.zip"
        nome = nome.replace('"', "")
        if self.command == "HEAD":
            self.send_response(200)
            self.send_header("Content-Type", "application/zip")
            self.send_header("Content-Disposition", f'attachment; filename="{nome}"')
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            return
        data = montar_zip(alvo, prefixo)
        self.send_response(200)
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Content-Disposition", f'attachment; filename="{nome}"')
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self._enviar(data)


def main() -> int:
    # recusa qualquer tentativa de mudar de diretório de trabalho para gravar
    os.chdir(RAIZ)
    httpd = ThreadingHTTPServer((HOST, PORTA), Handler)
    print(
        f"Visor RC (somente leitura) em http://{HOST}:{PORTA}/  raiz={RAIZ}",
        flush=True,
    )
    print(
        f"markdown={'sim' if _MD_OK else 'emergência (pip markdown ausente)'}",
        flush=True,
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nencerrado", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
