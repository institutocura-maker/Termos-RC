#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: DORMENTE-2026-09 (era esteira-leve; P6/P7 não invocam)
"""MOTOR ÚNICO DA ESTEIRA LEVE — Base Terminológica RC.

Nasce do despacho do Curador de 29/08/2026, §4 (Mandato para a Engenharia):

    Fim da reescrita de código por ciclo: o aparato técnico de validação será
    unificado em um Motor Único padronizado em `ferramentas/`. Configuração
    declarativa: cada ciclo passa a ser operado por arquivos de configuração leves
    (.toml), mantendo a rigidez dos portões essenciais (integridade de fonte, veto
    de trânsito e consistência de dados) sem o peso industrial anterior.

Este arquivo é o aparato. **A curadoria não mora aqui**: ela mora em
`ciclos/<SIGLA>/ciclo.toml`. Nenhum alvo, âncora, rótulo ou juízo editorial está
codificado dentro do motor — é isso que separa "motor único" de "script do último
ciclo renomeado".

Uso
    python3 ferramentas/motor.py --ciclo P2023-12-03 status
    python3 ferramentas/motor.py --ciclo P2023-12-03 tudo
    python3 ferramentas/motor.py selftest

Passos: status · entrada · ancorario · dossier · rag · materializar · portoes · tudo
Portões essenciais:
  A · integridade da fonte — SHA-256, bytes, unidades e caracteres de controle do bruto
  B · verbatim             — toda aspa do pacote, do dossiê e das seções de ficha tem de
                            existir byte a byte na fonte; nada é digitado à mão
  C · fichas e trânsito     — paridade ficha ↔ pacote e veto de léxico em ficha que
                            nomeia pessoa, paciente ou grupo humano
  D · contadores            — DELTA contra o commit-base do ciclo. Portão que mede estado
                            absoluto apodrece no ciclo seguinte: foi o que o portão D do
                            ciclo P2023-12-03 fez ao fixar `460 arquivos`, e é a regra
                            que este motor inverte.

Regras de construção, obrigadas pelo histórico medido dos 71 ciclos:
  · âncora que bate 0 ou >1 vez ABORTA — a ferramenta não "aproxima" citação;
  · `ç ø đ æ ß ð þ` não decompõem em NFD: o mapa `_EXTRA` é o que corrige isso no
    instrumento, e não na memória de quem digita;
  · número nunca digitado: lido do arquivo, do `git` ou da validação do cadastro;
  · chave de config não lida é erro — com motor único o defeito migra do script para o
    `.toml`, e o validador de uso é o que impede o silêncio;
  · byte de controle no bruto é abortado na entrada: foi um `0x08` que derrubou o DOCX
    do último ciclo pesado.
"""
from __future__ import annotations

import argparse
import subprocess
import bisect
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata

try:
    import tomllib
except ImportError:                                                     # pragma: no cover
    sys.exit("este motor exige Python ≥ 3.11 (tomllib)")

# As duas famílias de linha do cadastro. Os dois estilos de aspa convivem no arquivo por
# herança de ciclos, então a régua autoritativa é `medir_codigo` (executa o texto medido).
# As regex ficam como fallback, e errar aqui é o que faria o portão acusar a Base de ter
# aberto uma aresta que ninguém abriu.
LINHA_TERMO = re.compile(r"^\s*\(\s*['\"](RC-\d{3})['\"]\s*,.*,\s*(True|False)\s*\)\s*,?\s*$", re.M)
LINHA_ARESTA = re.compile(r"^\s*\(\s*['\"]RC-\d{3}['\"]\s*,\s*['\"][^'\"]+['\"]\s*,\s*['\"]RC-\d{3}", re.M)


# ─────────────────────────────────────────────────────────────────────────── util
def _fold_ch(ch: str) -> str:
    """Folding de um caractere, com mapa para as letras que o NFD não decompõe."""
    extra = {"ç": "c", "Ç": "C", "ø": "o", "Ø": "O", "đ": "d", "Đ": "D", "æ": "ae", "Æ": "ae",
             "ß": "ss", "ð": "d", "Ð": "d", "þ": "th", "Þ": "th"}
    ch = extra.get(ch, ch)
    base = "".join(c for c in unicodedata.normalize("NFD", ch) if not unicodedata.combining(c)).lower()
    return base or ch.lower()


def fold(txt: str) -> str:
    return "".join(_fold_ch(c) for c in txt)


def re_norm(txt: str) -> str:
    out = []
    for ch in txt:
        if ch.isspace():
            out.append(r"\s+")
            continue
        out.append(re.escape(_fold_ch(ch)))
    return "".join(out)


def sha256(caminho: str) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def n_vinculos(termos: list, sigla: str) -> int:
    """Quantos termos carregam `sigla` na lista de fontes — o contador que faz o vínculo ser
    conferível: 'o ciclo disse que tocou 61 códigos' vira número medido, não asserção."""
    if not sigla:
        return 0
    return sum(1 for t in termos if any(str(x) == sigla for x in (t[5] if len(t) > 5 else [])))


def medir_codigo(txt: str, sigla: str = "") -> dict:
    """Contagem simétrica de um `dados_termos.py` — hoje e baseline pelo MESMO caminho.

    Executar o texto medido é a única régua que não depende de como a linha foi escrita:
    há aspas simples e duplas misturadas por herança de ciclos e há `RELACOES` somada
    fora do bloco principal. Regex que não sabe disso conta 1.855 e acusa o ciclo de ter
    aberto uma aresta. O instrumento é que estava errado, não a Base — e o portão nasceu
    consertado por ler o cadastro do jeito que a própria Arca o lê."""
    ns = {"__name__": "_medidor_do_motor", "__file__": "<dados_termos medido>"}
    try:
        exec(compile(txt, "dados_termos.py", "exec"), ns)
        termos = list(ns.get("TERMOS", []))
        relas = list(ns.get("RELACOES", []))
        return dict(termos=len(termos),
                    ficha_true=sum(1 for t in termos if len(t) > 7 and t[7] is True),
                    relacoes=len(relas), vinculos=n_vinculos(termos, sigla), medido_por="exec")
    except Exception as e:                                        # pragma: no cover
        m = medir_regex(txt)
        m["vinculos"] = 0
        m["medido_por"] = f"regex (fallback após {type(e).__name__})"
        return m


def medir_regex(txt: str) -> dict:
    """Último recurso, e só isto: uma régua que não executa pode contar errado o `ficha`."""
    termos = fichas = 0
    for m in LINHA_TERMO.finditer(txt):
        termos += 1
        if m.group(2) == "True":
            fichas += 1
    return dict(termos=termos, ficha_true=fichas, relacoes=len(LINHA_ARESTA.findall(txt)))


SECAO = "## Ampliação — "


def secao_da_ficha(texto: str, sigla: str) -> str:
    """A seção deste ciclo numa ficha: do cabeçalho até o próximo `## ` ou até a régua
    `---`. Ler a ficha inteira é o que faz um auditor acusar o histórico de outro ciclo
    como se fosse vazamento deste (lição medida em `RC-378` e `RC-071`)."""
    m = re.search(r"^" + re.escape(SECAO + sigla) + r".*?(?=^## |^---\s*$|\Z)", texto, re.M | re.S)
    return m.group(0).rstrip() if m else ""


class FalhaPortao(Exception):
    """Portão vermelho. O motor para: não existe 'seguir com ressalva'."""


def chk(ok: bool, bom: str, ruim: str) -> None:
    print(("  ✓ " if ok else "  ✗ ") + (bom if ok else ruim))
    if not ok:
        raise FalhaPortao(ruim)


class Cfg:
    """`ciclo.toml` com auditoria de uso: chave declarada e nunca lida é erro de config."""

    def __init__(self, caminho: str):
        self.caminho = caminho
        with open(caminho, "rb") as fh:
            self.dados = tomllib.load(fh)
        self._lidas: set[str] = set()

    def get(self, chave: str, padrao=None, obrigatorio: bool = False):
        self._lidas.add(chave)
        if chave not in self.dados:
            if obrigatorio:
                sys.exit(f"[{os.path.basename(self.caminho)}] chave obrigatória ausente: {chave}")
            return padrao
        return self.dados[chave]

    def tabela(self, chave: str) -> dict:
        self._lidas.add(chave)
        return self.dados.get(chave, {}) or {}

    def conferir_uso(self, cad: set[str] | None = None) -> None:
        sobras = sorted(set(self.dados) - self._lidas)
        if sobras:
            sys.exit(f"[{os.path.basename(self.caminho)}] chaves declaradas e NUNCA lidas: "
                     f"{', '.join(sobras)} — ou o motor perdeu a regra, ou o .toml tem resíduo")
        # A mesma exigência vale DENTRO das mesas: subchave que o motor não lê é regra
        # perdida, e código que não existe no cadastro é ordem órfã nascendo do .toml.
        formas = {"tese": {"pontos"}, "materializar": {"codigos"}, "ampliar": {"codigos", "substituir"},
                  "vitorias": {"provas"}}
        for mesa, permitidas in formas.items():
            residuo = sorted(set(self.tabela(mesa)) - permitidas)
            if residuo:
                sys.exit(f"[{os.path.basename(self.caminho)}] `[mesa] {mesa}` tem chave que o motor "
                         f"não lê: {', '.join(residuo)}")
        if cad is None:
            return          # Cfg não conhece caminhos da Base; quem a tem carrega o conjunto
        for mesa in ("definicoes", "observacoes", "travas", "lacunas"):
            for cod in self.tabela(mesa):
                if cod not in cad:
                    sys.exit(f"[{os.path.basename(self.caminho)}] `[mesa] {mesa}` nomeia {cod}, "
                             f"que não existe no cadastro — ordem órfã não se fabrica em config")
        for cod in self.tabela("materializar").get("codigos", []):
            if cod not in cad:
                sys.exit(f"[{os.path.basename(self.caminho)}] [materializar] quer criar {cod}, "
                         f"que não tem linha no cadastro: materialização é virar ficha existente, "
                         f"não inventar termo")


# ─────────────────────────────────────────────────────────────────── fonte e índice
class Fonte:
    """O bruto, com índice de offsets. `Uxxxx` = N-ésima linha do arquivo (1-based), a
    mesma régua dos ciclos pesados: uma linha pode ter 79 mil chars e continua sendo um
    endereço. É por ela que o fatiamento por fronteira de frase pega o que pega."""

    def __init__(self, caminho: str):
        self.caminho = caminho
        self.raw = open(caminho, encoding="utf-8").read().replace("\r\n", "\n")
        self.linhas = self.raw.split("\n")
        self.off = [0]
        for l in self.linhas:
            self.off.append(self.off[-1] + len(l) + 1)
        chars, mapa = [], []
        for i, ch in enumerate(self.raw):
            if ch.isspace():
                chars.append(" ")
                mapa.append(i)
                continue
            for c in _fold_ch(ch):
                chars.append(c)
                mapa.append(i)
        norm, mp = [], []
        for c, i in zip(chars, mapa):
            if c == " " and norm and norm[-1] == " ":
                continue
            norm.append(c)
            mp.append(i)
        self.norm = "".join(norm)
        self.mapa = mp
        self.bytes = os.path.getsize(caminho)
        self.controles = sum(1 for ch in self.raw if unicodedata.category(ch) == "Cc" and ch not in "\n\t\r")
        self.unidades = [u for u in (f"U{i:04d}" for i in range(1, len(self.linhas) + 1))
                         if len(self.u_texto(u).strip()) > 40]

    def uaddr(self, pos: int) -> str:
        return f"U{bisect.bisect_right(self.off, pos):04d}"

    def u_texto(self, u: str) -> str:
        k = int(u[1:]) - 1
        return self.raw[self.off[k]:self.off[k + 1]]

    def _fim_frase(self, p: int) -> int:
        mel = p
        for sep in (". ", "? ", "! ", ".\n", "?\n", "!\n"):
            q = self.raw.find(sep, p)
            if q != -1 and (mel == p or q < mel):
                mel = q + 1
        return mel

    def verificar(self, aspa: str) -> tuple[bool, int, int]:
        """A aspa existe na fonte byte a byte? Devolve (ok, início, fim)."""
        alvo = re_norm(" ".join(aspa.split()))
        if not alvo:
            return False, -1, -1
        m = re.search(alvo, self.norm)
        if not m:
            return False, -1, -1
        a = self.mapa[m.start()]
        b = self._fim_frase(self.mapa[min(m.end() - 1, len(self.mapa) - 1)])
        return True, a, b

    def localizar(self, ancora: str, fim: str | None = None) -> tuple[int, int, str]:
        """Garimpo: âncora frouxa → span exato estendido à fronteira de frase.
        0 ou >1 ocorrência aborta; é assim que o motor se protege da memória alheia."""
        ini = [m.start() for m in re.finditer(re_norm(ancora), self.norm)]
        if len(ini) != 1:
            raise SystemExit(f"ÂNCORA {ancora[:52]!r} → {len(ini)} ocorrência(s); tem de ser exatamente 1")
        a = self.mapa[ini[0]]
        if fim:
            j = [m.start() for m in re.finditer(re_norm(fim), self.norm[ini[0]:])]
            if len(j) != 1:
                raise SystemExit(f"FIM {fim[:40]!r} após {ancora[:24]!r} → {len(j)} ocorrência(s)")
            b = self._fim_frase(self.mapa[ini[0] + j[0]] + len(fim))
        else:
            b = self._fim_frase(a + len(ancora))
        return a, b, self.raw[a:b].strip()


# ────────────────────────────────────────────────────────────────────────── pacote
ASP = re.compile("«(.+?)»", re.S)
UBLOCO = re.compile(r"\((U\d{4})")


class Pacote:
    """O pacote de ampliações continua sendo a interface entre o despacho e a Base:
    é onde a curadoria está escrita. O motor lê, confere e distribui; não interpreta."""

    def __init__(self, caminho: str, fonte: Fonte):
        self.caminho = caminho
        self.texto = open(caminho, encoding="utf-8").read()
        self.fonte = fonte
        if "### BLOCO 1" in self.texto:
            corpo = self.texto.split("### BLOCO 1", 1)[1].split("### BLOCO 2", 1)[0]
        else:
            corpo = self.texto
        partes = re.split(r"^### (RC-\d{3})\s*$", corpo, flags=re.M)
        self.blocos = {partes[i]: partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}
        # Em cada item do pacote, a PRIMEIRA aspa é a citação; as demais são prosa do
        # aplicador. Confundir as duas é o que faz um portão cobrar de uma nota o que só
        # um span pode dar — e é o que faz uma paráfrase virar "citação" no corpus.
        self.pares: list[tuple[str, str]] = []
        self.glosas: list[tuple[str, str]] = []
        for cod, corpo_ in self.blocos.items():
            for item in re.split(r"(?=^\s*-\s)", corpo_, flags=re.M):
                if not item.strip().startswith("-"):
                    continue
                asp = [" ".join(a.split()) for a in ASP.findall(item)]
                if asp:
                    self.pares.append((cod, asp[0]))
                    self.glosas += [(cod, a) for a in asp[1:]]
        self.retidos: set[str] = set()
        self.retidos_spans: list[str] = []
        if "### BLOCO 5" in self.texto:
            bloco5 = self.texto.split("### BLOCO 5", 1)[1].split("### BLOCO", 1)[0]
            self.retidos = set(re.findall(r"`(RC-\d{3})`", bloco5))
            # um mesmo código pode ter mais de um span retido: o rite pesado contava spans
            # (3), e é com spans que o livro-razão trabalha. Contar só códigos perdia 1.
            self.retidos_spans = [l for l in bloco5.splitlines() if l.strip().startswith("-")]

    def verificar(self, alvos: list[tuple[str, str]] | None = None) -> tuple[int, list[str]]:
        alvos = alvos if alvos is not None else self.pares
        ruins = [f"{cod}: {a[:56]!r}" for cod, a in alvos if not self.fonte.verificar(a)[0]]
        return len(alvos) - len(ruins), ruins

    def rebaixar_glosas(self, bloco: str, fonte: Fonte, log: list | None = None) -> str:
        """Dentro de um bloco, a PRIMEIRA aspa do item é a citação; o resto é glosa do
        aplicador. Aspa de glosa que não bate byte a byte na fonte não é citação e não tem
        direito a aspa: vira `backticks`. Nada é apagado, e o que foi rebaixado é impresso
        (silêncio é que não é opção nesta casa)."""
        def trata(item: str) -> str:
            partes = re.split(r"(«[^»]+»)", item)
            for k in range(1, len(partes), 2):
                if k == 1 and item.strip().startswith("- **"):
                    continue                                    # a citação do próprio item
                asp = " ".join(partes[k][1:-1].split())
                if asp and not fonte.verificar(asp)[0]:
                    if log is not None:
                        log.append(asp[:70])
                    partes[k] = "`" + partes[k][1:-1].replace("`", "'") + "`"
            return "".join(partes)

        saida = []
        for item in re.split(r"(?=^\s*-\s)", bloco, flags=re.M):
            saida.append(trata(item) if item.strip().startswith("-") else item)
        return "".join(saida)

    def bullets(self, cod: str) -> list[str]:
        """Cada item de um bloco do pacote: `- **[SIGLA · TÍTULO]** «span» (Uxxxx) — glosa`."""
        return [b.strip() for b in re.split(r"^\s*-\s+", self.blocos.get(cod, ""), flags=re.M)
                if "[P" in b[:80] or b.strip().startswith("**[")]


# ────────────────────────────────────────────────────────────────────────── ciclo
class Ciclo:
    def __init__(self, sigla: str, raiz: str | None = None):
        self.raiz = raiz or self._raiz()
        self.sigla = sigla
        candidatos = [os.path.join(self.raiz, "ciclos", sigla, "ciclo.toml")]
        for raio in ("apostilas", "apostilas/CONCLUIDAS"):
            candidatos += glob.glob(os.path.join(self.raiz, raio, f"*{sigla.lstrip('P')}*", "ciclo.toml"))
        self.toml = next((c for c in candidatos if os.path.exists(c)), None)
        if not self.toml:
            sys.exit(f"sem ciclo.toml para {sigla} (procurei em ciclos/{sigla}/ e nas pastas do ciclo)")
        self.dir = os.path.dirname(self.toml)
        self.cfg = Cfg(self.toml)
        self._ler_config()
        self.fonte = Fonte(os.path.join(self._resolve(self.pasta_fonte), self.arquivo_fonte))
        self.pacote = Pacote(self._resolve(self.pacote_rel), self.fonte)
        self.base = Base(self.raiz, sigla)
        self.fichas = self.base.arquivos()

    @staticmethod
    def _raiz() -> str:
        d = os.path.abspath(os.path.dirname(__file__))
        while d != "/" and not os.path.exists(os.path.join(d, "ferramentas", "dados_termos.py")):
            d = os.path.dirname(d)
        return d

    def _ler_config(self) -> None:
        c = self.cfg
        sigla_cfg = c.get("sigla", self.sigla, obrigatorio=True)
        if sigla_cfg != self.sigla:
            sys.exit(f"o ciclo.toml declara sigla {sigla_cfg!r} mas o ciclo pedido foi {self.sigla!r} — "
                     f"config de outro ciclo não roda neste")
        self.titulo = c.get("titulo", "")
        self.data_fonte = c.get("data_fonte", "")
        self.pasta_fonte = c.get("pasta_fonte", obrigatorio=True)
        self.arquivo_fonte = c.get("arquivo_fonte", "original.txt")
        self.pacote_rel = c.get("pacote", "analise/_ampliacoes_%s.txt" % self.sigla)
        self.baseline = c.get("baseline_commit", obrigatorio=True)
        self.max_perolas = int(c.get("max_perolas", 25))
        self.portoes_ativos = list(c.get("portoes_ativos", ["A", "B", "C", "D"]))
        self.veto = list(c.get("veto_lexico", []))
        self.fichas_grupo = set(c.get("fichas_que_nomeiam_grupo", []))
        self.teto = c.get("teto", "vigente")
        self.cobertura = c.get("cobertura",
                               "não-transcrita neste formato — fonte integral preservada em `original.txt`, selada por hash")
        self.exportar_candidatas = bool(c.get("exportar_candidatas", False))
        self.sha256_esperado = c.get("sha256_fonte", "")
        self.delta_esperado = c.tabela("delta_esperado")
        self.materializar = list(c.tabela("materializar").get("codigos", []))
        self.ampliar = list(c.tabela("ampliar").get("codigos", []))
        self.substituir = bool(c.tabela("ampliar").get("substituir", False))
        self.definicoes = c.tabela("definicoes")
        self.observacoes = c.tabela("observacoes")
        self.travas = c.tabela("travas")
        self.lacunas = c.tabela("lacunas")
        # `[vitorias]` é mesa com a chave `provas`: cada linha declara O QUE O CICLO CONSEGUIU
        # e onde está a prova (um trecho literal da `## Ampliação — <SIGLA>` da ficha). O dossiê
        # nasce do que foi conferido, nunca do que foi narrado.
        self.vitorias = list(c.tabela("vitorias").get("provas", []))
        # `[tese]` é MESA com a chave `pontos` — ler a mesa como lista dava a lista das
        # chaves, e o §2 do dossiê saiu com um item chamado "pontos". Config lida é config
        # entendida.
        tese = c.tabela("tese")
        self.tese = list(tese.get("pontos", []))
        self.termos_novos = list(c.get("termos_novos", []))

    def _resolve(self, relativo: str) -> str:
        for p in (os.path.join(self.raiz, relativo), os.path.join(self.dir, relativo)):
            if os.path.exists(p):
                return p
        sys.exit(f"caminho declarado no .toml não existe: {relativo}")

    def secao_limpa(self, cod: str) -> str:
        """O bloco do pacote, já com aspas de glosa rebaixadas — a única versão que entra
        em ficha e a única versão contra a qual a paridade é aferida."""
        if not hasattr(self, "_limpo"):
            self._limpo: dict[str, str] = {}
            self.log_rebaixado: dict[str, list[str]] = {}
        if cod not in self._limpo:
            log: list[str] = []
            self._limpo[cod] = self.pacote.rebaixar_glosas(self.pacote.blocos[cod], self.fonte, log)
            self.log_rebaixado[cod] = log
        return self._limpo[cod]

    # ── garimpo: candidatas pontuadas por critério mecânico; o juízo é do Curador
    def candidatas(self) -> list[dict]:
        reg: dict[tuple[str, str], dict] = {}
        for cod in self.pacote.blocos:
            for bullet in self.pacote.bullets(cod):
                ach = ASP.search(bullet)
                if not ach:
                    continue
                aspa = " ".join(ach.group(1).split())
                u = UBLOCO.search(bullet)
                tit = re.match(r"\s*\[(?:[^\]·]*·\s*)?([^\]]+)\]", bullet)
                glossa = re.search(r"»\s*\([^)]*\)\s*(?:—|-{2})\s*(.+)", bullet, re.S)
                r = reg.setdefault((cod, aspa), dict(
                    codigo=cod, aspa=aspa, u=(u.group(1) if u else self.fonte.uaddr(self.fonte.verificar(aspa)[1])),
                    titulo=(tit.group(1).strip() if tit else cod),
                    glossa=(" ".join(glossa.group(1).split())[:600] if glossa else ""),
                    pontos=0, porque=[], menacoes=[]))
                if cod not in self.fichas:
                    r["pontos"] += 3
                    r["porque"].append("código tocado sem arquivo de ficha")
                if re.search(r"(?:\b19\d\d\b|\b20\d\d\b|\b\d{1,3}(?:\.\d{3})+\b)", aspa):
                    r["pontos"] += 2
                    r["porque"].append("traz data ou grandeza, conferível na íntegra")
                men = self.mencoes(aspa)
                if men:
                    r["pontos"] += min(3, len(men))
                    r["porque"].append(f"cruza {len(men)} termo(s) da Base")
                    r["menacoes"] = men
                if re.search(r"diverg|sem harmoniz|coexist|anterioridade", bullet, re.I):
                    r["pontos"] += 2
                    r["porque"].append("divergência selada em vez de harmonizada")
                if cod in self.pacote.retidos:
                    r["pontos"] -= 5
                    r["porque"].append("span retido pelo caça-âncoras (máscara do STT)")
                if cod in self.fichas_grupo:
                    r["pontos"] -= 4
                    r["porque"].append("veto de trânsito: ficha que nomeia grupo humano")
        out = sorted(reg.values(), key=lambda r: (-r["pontos"], r["codigo"]))
        for n, r in enumerate(out, 1):
            r["id"] = f"PER-{self.sigla.lstrip('P')}-{n:03d}"
            r["status"] = "candidata"
            r["selecionada"] = n <= self.max_perolas and r["pontos"] >= 0
            # O despacho quer o MOTIVO da recusa, não só a conta: "fora do teto" é outra
            # coisa que "pontuação negativa", e quem audita o caderno precisa ler a diferença.
            if r["selecionada"]:
                r["recusa"] = None
            elif r["pontos"] < 0:
                r["recusa"] = f"pontuação negativa ({r['pontos']}) no baricentro do ciclo: " + " · ".join(
                    x for x in r["porque"] if x.startswith(("span retido", "veto de")))
            else:
                r["recusa"] = (f"ficou fora do teto de {self.max_perolas} por pontuação "
                               f"({r['pontos']} pt(s), a #{n} do ranque)")
            r["lacuna"] = self.lacunas.get(r["codigo"], "")
        return out

    def mencoes(self, txt: str) -> list[str]:
        alvo = fold(txt)
        hits = []
        for cod, t in self.base.termos.items():
            nome = re.sub(r"\(.*?\)", "", t[1]).strip()
            if len(nome) >= 6 and re.search(r"\b" + re_norm(nome) + r"\b", alvo):
                hits.append(cod)
        return sorted(set(hits))


class Base:
    """A Base Terminológica, lida — nunca escrita — pelo motor, exceto onde o ciclo
    manda (materialização de fichas)."""

    def __init__(self, raiz: str, sigla: str = ""):
        self.sigla = sigla
        sys.path.insert(0, os.path.join(raiz, "ferramentas"))
        # Cache de import é a última coisa que se quer depois de virar uma ficha: o módulo
        # continuaria o de antes da escrita, e o portão D acusaria o ciclo de não ter feito
        # o que acabou de fazer.
        sys.modules.pop("dados_termos", None)
        import dados_termos as DT                                           # noqa: E402
        self.DT = DT
        self.termos = {t[0]: t for t in DT.TERMOS}
        self.relas = list(getattr(DT, "RELACOES", []))
        self.raiz = raiz
        self.cadastro_txt = open(os.path.join(raiz, "ferramentas", "dados_termos.py"),
                                 encoding="utf-8").read()

    def arestas(self, cod: str) -> list:
        return [r for r in self.relas if cod in (r[0], r[2])]

    def arquivos(self) -> dict[str, str]:
        out = {}
        for f in glob.glob(os.path.join(self.raiz, "termos", "*.md")):
            m = re.search(r"(RC-\d{3})", os.path.basename(f))
            if m:
                out[m.group(1)] = f
        return out

    def validacao(self) -> str:
        r = subprocess.run([sys.executable, os.path.join(self.raiz, "ferramentas", "dados_termos.py")],
                           capture_output=True, text=True, cwd=self.raiz, timeout=240)
        return (r.stdout.strip().splitlines() or ["—"])[-1]

    def no_commit(self, commit: str) -> dict:
        ls = subprocess.run(["git", "-C", self.raiz, "ls-tree", "-r", "--name-only", commit, "--", "termos/"],
                            capture_output=True, text=True).stdout
        cad = subprocess.run(["git", "-C", self.raiz, "show", f"{commit}:ferramentas/dados_termos.py"],
                             capture_output=True, text=True).stdout
        if not cad.strip():
            sys.exit(f"não consegui ler {commit}:ferramentas/dados_termos.py — o baseline do ciclo está errado?")
        m = medir_codigo(cad, self.sigla)
        # `git ls-tree` cita caminhos com byte não-ASCII (×, ṅ): sem tolerar a aspa final do
        # nome escapado, três fichas somem da contagem e o delta sai 9 em vez de 6.
        return dict(arquivos=len([l for l in ls.splitlines() if re.search(r"RC-\d{3}.*\.md\"?$", l)]),
                    termos=m["termos"], ficha_true=m["ficha_true"], relacoes=m["relacoes"],
                    vinculos=m["vinculos"], como=m["medido_por"])

    def agora(self) -> dict:
        m = medir_codigo(self.cadastro_txt, self.sigla)
        ao_vivo = dict(termos=len(self.termos), relacoes=len(self.relas),
                       ficha_true=sum(1 for t in self.termos.values() if t[7] is True))
        for campo in ("termos", "relacoes", "ficha_true"):
            if m[campo] != ao_vivo[campo]:
                print(f"  ⚠️ contador do motor diverge do cadastro importado em {campo}: "
                      f"{m[campo]} vs {ao_vivo[campo]} — é o instrumento que tem de ser consertado")
        return dict(arquivos=len(self.arquivos()), termos=ao_vivo["termos"],
                    ficha_true=ao_vivo["ficha_true"], relacoes=ao_vivo["relacoes"],
                    vinculos=n_vinculos(list(self.termos.values()), self.sigla), como=m["medido_por"])


# ────────────────────────────────────────────────────────────────────────── portões
def portao_A(c: Ciclo) -> None:
    print("PORTÃO A · integridade da fonte")
    real = sha256(c.fonte.caminho)
    esperado = c.sha256_esperado
    if esperado:
        chk(real.startswith(esperado), f"SHA-256 {real[:12]}… bate com o ingresso ({esperado}…)",
            f"SHA-256 diverge do ingresso: {real[:12]}… ≠ {esperado}… — a fonte foi tocada")
    else:
        print(f"  · SHA-256 atual: {real}  (registre em `sha256_fonte` e o portão passa a morder)")
    chk(c.fonte.controles == 0,
        f"0 caracteres de controle · {c.fonte.bytes:,} B · {len(c.fonte.unidades)} unidades com fala".replace(",", "."),
        f"{c.fonte.controles} caractere(s) de controle no bruto — DOCX e corpus RAG quebram adiante")


def portao_B(c: Ciclo) -> None:
    print("PORTÃO B · verbatim — nenhuma aspa digitada à mão")
    ok, ruins = c.pacote.verificar()
    chk(not ruins, f"{ok}/{len(c.pacote.pares)} citações do pacote conferidas byte a byte no bruto",
        f"{len(ruins)} aspa(s) do pacote não batem na fonte: " + "; ".join(ruins[:5]))
    okg, ruimg = c.pacote.verificar(c.pacote.glosas)
    print(f"  · aspas de glosa (prosa do aplicador): {okg} de {len(c.pacote.glosas)} são span verificado; "
          f"{len(ruimg)} são referência e perdem a aspa na materialização")
    if c.pacote.glosas and okg == len(c.pacote.glosas):
        print("    (todas verificáveis: nenhum rebaixamento necessário)")
    alvos = [("dossiê", os.path.join(c.dir, f"DOSSIE-RAG_{c.sigla}.md"), None)]
    alvos += [(cod, c.fichas[cod], c.sigla) for cod in c.pacote.blocos if cod in c.fichas]
    for rot, caminho, filtro in alvos:
        if not os.path.exists(caminho):
            continue
        texto = open(caminho, encoding="utf-8").read()
        if filtro:                       # só a seção deste ciclo: ler a ficha toda acusa o histórico alheio
            texto = secao_da_ficha(texto, filtro)
        asp = [" ".join(a.split()) for a in ASP.findall(texto)]
        ruins = [a[:56] for a in asp if a and not c.fonte.verificar(a)[0]]
        chk(not ruins, f"{rot}: {len(asp)} aspa(s) conferidas",
            f"{rot}: {len(ruins)} aspa(s) sem correspondência na fonte: " + "; ".join(repr(r) for r in ruins[:5]))


def portao_C(c: Ciclo) -> None:
    print("PORTÃO C · paridade ficha ↔ pacote e veto de trânsito")
    divergentes, vazamentos = [], []
    conferidas = 0
    for cod, corpo in c.pacote.blocos.items():
        arq = c.fichas.get(cod)
        if not arq:
            continue
        conferidas += 1
        ficha = open(arq, encoding="utf-8").read()
        corpo_ficha = secao_da_ficha(ficha, c.sigla)
        if not corpo_ficha:
            divergentes.append(f"{cod} sem a seção do ciclo")
            continue
        # paridade de CONTEÚDO: o cabeçalho pode levar o título da palestra e o corpo não pode
        # levar nem um caractere a mais — é o corpo que o Curador aprovou no pacote.
        cab, _, resto = corpo_ficha.partition("\n")
        if not cab.startswith(f"## Ampliação — {c.sigla}"):
            divergentes.append(f"{cod} cabeçalho de seção divergente: {cab[:40]!r}")
        if " ".join(resto.split()) != " ".join(c.secao_limpa(cod).split()):
            divergentes.append(f"{cod} corpo divergente do pacote")
        for v in c.veto:
            if v and v in corpo_ficha:
                vazamentos.append(f"{cod} → {v!r} na seção do ciclo")
    chk(not divergentes, f"{conferidas} fichas com a seção do ciclo em paridade com o pacote",
        "paridade DIVERGE: " + "; ".join(divergentes[:8]))
    chk(not vazamentos, f"0 vazamentos do léxico vetado ({len(c.veto)} marca(s)) nas {conferidas} fichas",
        "VETO DE TRÂNSITO VIOLADO: " + "; ".join(vazamentos[:8]))
    grupo = [k for k in c.fichas_grupo if k in c.pacote.blocos]
    print(f"  · fichas que nomeiam grupo humano sob vigilância neste ciclo: {len(grupo)}")


def portao_D(c: Ciclo) -> None:
    print("PORTÃO D · contadores como DELTA contra o commit-base")
    antes, agora = c.base.no_commit(c.baseline), c.base.agora()
    delta = {k: agora[k] - antes.get(k, 0) for k in agora if isinstance(agora[k], int)}
    print(f"  base {c.baseline[:7]}: {antes}"
          + (f"   (medido por: {antes.get('como')})" if antes.get("como") else ""))
    print(f"  hoje           : {agora}   (medido por: {agora.get('como')})")
    print(f"  delta          : {delta}")
    for campo, valor in c.delta_esperado.items():
        chk(delta.get(campo) == valor, f"Δ {campo} = {delta.get(campo)} — exatamente o declarado no ciclo ({valor})",
            f"Δ {campo} = {delta.get(campo)}, mas o ciclo declarou {valor}: há escrita fora do mandado")
    if c.teto == "suspenso-com-cadencia":
        limite = len(c.termos_novos)
        chk(delta.get("termos", 0) <= limite,
            f"teto suspenso com cadência: {delta.get('termos')} termo(s) novo(s) ≤ {limite} autorizado(s)",
            f"nasceram {delta.get('termos')} termos e o ciclo autorizou {limite}: materialização virou criação")
    else:
        chk(delta.get("termos", 0) == 0, "nenhum termo novo (teto em vigor)",
            f"nasceram {delta.get('termos')} termos com o teto em vigor")
    chk(c.base.validacao().startswith("OK"), f"cadastro válido: {c.base.validacao()}", "cadastro inválido")


# ──────────────────────────────────────────────────────────────── produtos do ciclo
def ancorario(c: Ciclo) -> None:
    """Livro-razão de âncoras: a apólice que substitui o calhamaço. Registra cada span
    que a fonte contém e cada candidata que o garimpo **recusou**, com motivo — assim,
    'não transcrevemos tudo' não passa a significar 'não podemos responder se algo se
    perdeu'."""
    sel = c.candidatas()
    reg = dict(sigla=c.sigla, politica_de_cobertura=c.cobertura,
               fonte=os.path.relpath(c.fonte.caminho, c.raiz), sha256=sha256(c.fonte.caminho),
               bytes=c.fonte.bytes, unidades_com_fala=len(c.fonte.unidades),
               spans=[], recusa=[])
    for cod in c.pacote.blocos:
        for bullet in c.pacote.bullets(cod):
            a = ASP.search(bullet)
            if not a:
                continue
            aspa = " ".join(a.group(1).split())
            ok, i, f = c.fonte.verificar(aspa)
            reg["spans"].append(dict(codigo=cod, u=c.fonte.uaddr(i), chars=[i, f], largura=f - i,
                                     verificada=ok, texto=aspa))
    for r in sel:
        if not r["selecionada"]:
            reg["recusa"].append(dict(codigo=r["codigo"], u=r["u"], pontos=r["pontos"],
                                     recusada_por=r["recusa"], sinais=r["porque"],
                                     aspa=r["aspa"][:220]))
    destino = os.path.join(c.dir, f"ancorario_{c.sigla}.json")
    with open(destino, "w", encoding="utf-8") as fh:
        json.dump(reg, fh, ensure_ascii=False, indent=1)
    n_ok = sum(1 for s in reg["spans"] if s["verificada"])
    if not reg["spans"]:
        chk(False, "", "o pacote não tem uma aspa sequer: nada foi garimpado ainda — o ciclo não "
                       "fecha vazio por omissão, e sim por declaração no `.toml`")
    chk(n_ok == len(reg["spans"]) and reg["spans"],
        f"livro-razão {os.path.basename(destino)}: {len(reg['spans'])} spans verificados · "
        f"{len(reg['recusa'])} recusadas com motivo",
        f"{len(reg['spans']) - n_ok} span(s) no livro-razão sem correspondência na fonte")


def dossie(c: Ciclo) -> None:
    sel = [r for r in c.candidatas() if r["selecionada"]]
    L = [f"# Dossiê RAG — {c.sigla} · {c.titulo}", "",
         "> Gerado pelo Motor Único (`ferramentas/motor.py`) no formato do despacho de 29/08/2026. "
         "Nenhuma aspa digitada à mão: toda citação foi recortada do `original.txt` pelo índice de "
         "âncoras e conferida pelo portão B.", "",
         "## 1 · Cabeçalho de metadados", "",
         "| Campo | Valor |", "|---|---|",
         f"| Sigla | `{c.sigla}` |",
         f"| Data da fonte | {c.data_fonte} |",
         f"| Hash da fonte | `{sha256(c.fonte.caminho)[:16]}…` · {c.fonte.bytes:,} B".replace(",", "."),
         f"| Cobertura | {c.cobertura} |",
         f"| Termos tocados | {len(c.pacote.blocos)} códigos, {len([k for k in c.pacote.blocos if k in c.fichas])} com arquivo |",
         f"| Citações verificadas | {len(c.pacote.pares)} |",
         f"| Caderno | {len(sel)} pérolas de {len(c.candidatas())} candidatas |",
         f"| Teto curatorial | {c.teto} |",
         f"| Livro-razão | `ancorario_{c.sigla}.json` |", "",
         *vitorias_para_dossie(c),
         "## 2 · Resumo executivo da tese", ""]
    L += ([f"* {t}" for t in c.tese] or ["* (declarações de tese em `ciclo.toml`, seção ausente)"])
    L += ["", "## 3 · O Caderno de Pérolas", "",
          "Toda pérola nasce `candidata`. O corpus RAG só recebe a que tiver carimbo do Curador "
          "(`aprovada`) — o garimpo é do agente, a escolha é do curador.", ""]
    for p in sel:
        _, i, f = c.fonte.verificar(p["aspa"])
        L += [f"### {p['id']} · {p['titulo']}", "",
              f"* **Endereço**: `{c.sigla}` · {p['u']} · chars {i}–{f} · {f - i} c",
              f"* **Termo**: `{p['codigo']}`" + ("" if p["codigo"] in c.fichas else " — sem arquivo de ficha"),
              f"* **Status**: `{p['status']}` · **Por quê**: {'; '.join(p['porque']) or '—'}",
              *([f"* **Lacuna que fecha**: {p['lacuna']}"] if p["lacuna"] else []),
              *([f"* **Cruza**: " + ", ".join(f"`{m}`" for m in p["menacoes"])] if p.get("menacoes") else []),
              "", f"> «{p['aspa']}»", ""]
    fila = [k for k in c.pacote.blocos if k not in c.fichas and k not in c.materializar]
    L += ["## 4 · Atualizações para a Base", ""]
    if c.materializar:
        L.append(f"* **Materializações executadas**: {len(c.materializar)} — "
                 + ", ".join(f"`{k}`" for k in c.materializar)
                 + ". Virada `ficha=False → ficha=True`, com o bloco do pacote copiado byte a byte.")
    L += [f"* **Termos novos**: {len(c.termos_novos)}"
          + (f" — cadência do teto suspenso: {', '.join(c.termos_novos)}" if c.termos_novos else "")
          + ". Cada um existe porque uma pérola o exigiu, não porque a fonte o nomeou.",
          "* **Relações**: nenhuma aresta criada, fechada ou reetiquetada por este ciclo. "
          "Aresta só entra tipada, com evidência (span + endereço) e selo datado.",
          "* **Divergências**: com selo datado, sem média — a Base não harmoniza números por decisão de quem aplica.",
          f"* **Fila aberta**: {len(fila)} código(s) tocado(s) por esta fonte e ainda sem arquivo — "
          "a fila nasce deste produto, e não de memória.", ""]
    destino = os.path.join(c.dir, f"DOSSIE-RAG_{c.sigla}.md")
    open(destino, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"dossiê: {os.path.relpath(destino, c.raiz)} · {len(L)} linhas · {os.path.getsize(destino):,} B"
          .replace(",", "."))


def rag(c: Ciclo) -> None:
    """Export atômico: um card por pérola, com front-matter. RAG não indexa calhamaço;
    indexa card com id, endereço e status — e o status manda: sem carimbo do Curador,
    nada entra (salvo ensaio explícito do ciclo zero)."""
    sel = [r for r in c.candidatas() if r["selecionada"]
           and (r["status"] == "aprovada" or c.exportar_candidatas)]
    pasta = os.path.join(c.raiz, "rag", "perolas")
    os.makedirs(pasta, exist_ok=True)
    cards = []
    for p in sel:
        _, i, f = c.fonte.verificar(p["aspa"])
        nome = c.base.termos.get(p["codigo"], (p["codigo"], "—"))[1]
        corpo = "\n".join([
            "---",
            f"id: {p['id']}",
            f"ciclo: {c.sigla}",
            f"titulo_ciclo: {c.titulo}",
            f"data_fonte: {c.data_fonte}",
            f"arquivo_fonte: {os.path.relpath(c.fonte.caminho, c.raiz)}",
            f"sha256_fonte: {sha256(c.fonte.caminho)}",
            f"unidade: {p['u']}",
            f"chars: {i}-{f}",
            f"termo: {p['codigo']}",
            f"nome_termo: {nome}",
            f"status: {p['status']}",
            f"trava: {c.travas.get(p['codigo'], '—')}",
            f"lacuna: {p['lacuna'] or '—'}",
            "tipo: perola",
            "---", "",
            p["aspa"], "",
            f"_Glosa do ciclo:_ {p['glossa'] or '—'}", ""])
        destino = os.path.join(pasta, f"{p['id']}.md")
        open(destino, "w", encoding="utf-8").write(corpo)
        cards.append(dict(id=p["id"], arquivo=os.path.relpath(destino, c.raiz), sha256=sha256(destino),
                          termo=p["codigo"], status=p["status"]))
    manifest = dict(motor="ferramentas/motor.py", ciclo=c.sigla,
                    politica=("ensaio do ciclo zero: exportou candidatas sem carimbo" if c.exportar_candidatas
                              else "apenas `status: aprovada` entra no corpus"),
                    fonte=os.path.relpath(c.fonte.caminho, c.raiz), sha256_fonte=sha256(c.fonte.caminho),
                    cards_total=len(cards), cards=cards)
    open(os.path.join(c.raiz, "rag", f"MANIFESTO-{c.sigla}.json"), "w", encoding="utf-8").write(
        json.dumps(manifest, ensure_ascii=False, indent=1))
    print(f"corpus RAG: {len(cards)} card(s) em `rag/perolas/` · `rag/MANIFESTO-{c.sigla}.json`")


def materializar(c: Ciclo) -> None:
    """Cria (ou reescreve) o arquivo de ficha a partir do cadastro e do pacote. Não abre
    aresta, não cria termo e não inventa definição: o que não está no `.toml` ou no
    pacote não entra na Base."""
    hoje = datetime.date.today().isoformat()
    for cod in c.materializar:
        if cod not in c.pacote.blocos:
            sys.exit(f"{cod} não tem bloco no pacote — o motor não inventa conteúdo para materializar")
        t = c.base.termos[cod]
        arq = c.fichas.get(cod)
        if arq and MARCACICLO not in open(arq, encoding="utf-8").read():
            sys.exit(f"{cod}: a ficha existe e não foi escrita por este motor — `materializar` "
                     f"reescreveria o arquivo inteiro e apagaria o histórico dela. Para ficha que "
                     f"já existe o passo é `ampliar` (insere só a seção do ciclo).")
        if not arq:
            slug = re.sub(r"-{2,}", "-", re.sub(r"[^A-Za-z0-9]+", "-", fold(t[1].replace("´", " ")))).strip("-")
            arq = os.path.join(c.raiz, "termos", f"{cod}-{slug.lower()}.md")
        arestas = c.base.arestas(cod)
        rels = [x.strip() for x in (t[6] or "").split(";") if x.strip()]
        com_aresta = [r for r in rels if any(r in (a[0], a[2]) for a in arestas)]
        sem_arquivo = [r for r in rels if r not in c.fichas]
        obras = [x for x in (t[5] or []) if not str(x).startswith("P")]
        secao = c.secao_limpa(cod)
        rebatidas = c.log_rebaixado.get(cod, [])
        L = [f"# {t[1]} — {cod}", "",
             "| Campo | Valor |", "|---|---|",
             f"| **Categoria Principal** | {t[2].title()} |",
             f"| **Subcategoria** | {t[3]} |",
             f"| **Status** | 🟡 {str(t[4]).capitalize()} |",
             f"| **Última atualização** | {hoje} |", "",
             "## Definição Sintética", "", c.definicoes.get(cod, "(sem definição no ciclo.toml)"), "",
             "## Contexto / Origem", "",
             f"**Materialização (não é criação).** `{cod}` vivia só no cadastro: linha em "
             f"`ferramentas/dados_termos.py`, `ficha=False`, sem arquivo em `termos/`. A virada foi autorizada "
             f"pelo despacho do Curador de 29/08/2026, na linha que trata das ordens nomeadas sem arquivo, e "
             f"executada pelo Motor Único em `ciclos/{c.sigla}/`.", "",
             "Com isso:", "",
             "* a Base ganha um **arquivo**; 0 termos novos e **0 relações novas** por este ciclo;",
             f"- o cadastro lista {len(rels)} código(s) em `relacionados`: {len(com_aresta)} com aresta "
             f"correspondente em `RELACOES` e {len(sem_arquivo)} sem arquivo de ficha. A ficha **declara** a "
             "lacuna em vez de preenchê-la — abrir aresta é decisão curatorial;",
             f"- as fontes já registradas no cadastro são "
             + (", ".join(f"`{x}`" for x in (t[5] or [])) or "nenhuma") + ".", "",
             f"**Origem do conteúdo da ampliação:** palestra `{c.sigla} — {c.titulo}` ({c.data_fonte}). "
             "Transcrição automatizada, **não conferida com o áudio**; cada aspa foi recortada do `original.txt` "
             "pelo índice de âncoras do motor e conferida byte a byte pelo portão B. Nada foi digitado de memória.",
             "", "## Observações sobre o Estado da Malha", ""]
        L += ([f"* {o}" for o in (c.observacoes.get(cod) or [])])
        if rebatidas:
            L.append("* **Aspas de glosa rebaixadas para `backticks` nesta ficha**: "
                     + "; ".join(f"`{x}`" for x in rebatidas)
                     + ". Não eram span verificado no `original.txt`; a regra da casa é aspa só para "
                       "citação conferível, e a paridade com o pacote é aferida já com esta normalização.")
        L += [f"* **Trava aplicável**: {c.travas.get(cod, 'nenhuma além das gerais do despacho')}.", "",
              f"## Ampliação — {c.sigla}" + (f" ({c.titulo})" if c.titulo else ""), "",
              secao, "",
              "## Fontes", "| Obra (sigla) | Título | Página | Tipo |", "|---|---|---|---|",
              f"| {c.sigla} | {c.titulo} (palestra) | — | transcrição automatizada; citação |"]
        L += [f"| {x} | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |" for x in obras]
        L += ["", "## Termos Relacionados", "| Termo | Código | Estado na malha |", "|---|---|---|"]
        L += [f"| {c.base.termos[r][1] if r in c.base.termos else '—'} | {r} | "
              + ("**sem aresta** em `RELACOES`" if r not in com_aresta else "aresta pré-existente")
              + ("; **sem arquivo**" if r not in c.fichas else "; arquivo existe") + " |" for r in rels] or \
             ["| — | — | o cadastro não lista relacionados |"]
        corpo = re.sub(r"[ \t]+$", "", "\n".join(L) + "\n", flags=re.M)
        open(arq, "w", encoding="utf-8").write(corpo)
        assert f"## Ampliação — {c.sigla}" in corpo, f"{cod}: a seção do ciclo não entrou na ficha"
        print(f"  ficha: {os.path.relpath(arq, c.raiz)} · {os.path.getsize(arq):,} B · "
              f"{len(ASP.findall(corpo))} aspa(s)".replace(",", "."))
    tot = [x for v in getattr(c, "log_rebaixado", {}).values() for x in v]
    if tot:
        print(f"  ⚠️ {len(tot)} aspa(s) de glosa rebaixada(s) para `backticks` — não eram span verificado "
              f"na fonte: " + "; ".join(f"{x!r}" for x in tot))
    else:
        print("  · 0 aspas de glosa precisaram ser rebaixadas")


def virar_ficha(c: Ciclo) -> None:
    """Única escrita permitida no cadastro por este motor: `ficha=False → ficha=True`,
    linha a linha, preservando o resto do arquivo. `RELACOES` não é tocada."""
    caminhos = os.path.join(c.raiz, "ferramentas", "dados_termos.py")
    linhas = open(caminhos, encoding="utf-8").read().split("\n")
    feitos, ja_viradas, faltam = [], [], []
    for cod in c.materializar:
        achou = False
        for i, l in enumerate(linhas):
            if not re.match(r"^\s*\(?'?\"?" + cod + "\"?'?,", l):
                continue
            if l.rstrip().endswith("False),"):
                linhas[i] = re.sub(r"False\),\s*$", "True),", l.rstrip()) + l[len(l.rstrip()):]
                feitos.append(cod)
            elif l.rstrip().endswith("True),"):
                ja_viradas.append(cod)                    # idempotência: rodar duas vezes é neutro
            else:
                faltam.append(f"{cod} (terminal inesperado: {l.rstrip()[-14:]!r})")
            achou = True
            break
        if not achou:
            faltam.append(f"{cod} (linha ausente no cadastro)")
    if feitos:
        open(caminhos, "w", encoding="utf-8").write("\n".join(linhas))
    if ja_viradas:
        print(f"  · já viradas no cadastro (nenhuma reescrita): {', '.join(ja_viradas)}")
    chk(not faltam, f"cadastro: {len(feitos)} virada(s) nova(s)"
        + (f", {len(ja_viradas)} já virada(s)" if ja_viradas else ""),
        "cadastro não confere: " + "; ".join(faltam))


def status(c: Ciclo) -> None:
    sel = [r for r in c.candidatas() if r["selecionada"]]
    print(f"ciclo {c.sigla} · config {os.path.relpath(c.toml, c.raiz)}")
    print(f"  fonte {os.path.relpath(c.fonte.caminho, c.raiz)}: {c.fonte.bytes:,} B · "
          f"{len(c.fonte.unidades)} unidades com fala".replace(",", "."))
    print(f"  pacote: {len(c.pacote.blocos)} códigos · {len(c.pacote.pares)} citações · "
          f"{len(c.pacote.retidos_spans)} span(s) retido(s) em {len(c.pacote.retidos)} código(s)")
    print(f"  fichas com arquivo: {len([k for k in c.pacote.blocos if k in c.fichas])} de {len(c.pacote.blocos)}")
    print(f"  malha: {len(c.pacote.blocos)} codigo(s) a vincular - "
          f"{len([x for x in c.pacote.blocos if x in c.fichas])} fichas a ampliar - "
          f"{len([x for x in c.materializar if x not in c.fichas])} fichas a criar")
    print(f"  caderno: {len(sel)} pérolas de {len(c.candidatas())} candidatas (teto {c.max_perolas})")
    print(f"  portões ativos {''.join(c.portoes_ativos)} · teto {c.teto} · baseline {c.baseline[:7]}")
    if c.vitorias:
        for cod, af, prova, ok in vitorias_do_ciclo(c):
            print(f"  vitória {'conferida' if ok else 'AINDA NÃO CONFERIDA'}: `{cod}` — {af[:60]}")


# ────────────────────────────────────── abertura de ciclo e garimpo assistido
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD_ATUAL = "?"


def _raiz_do_repo() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


FRASE = re.compile(r"[.!?…]")


def novo(txt: str, sigla: str = "") -> None:
    """Abre um ciclo leve a partir do TXT que chegou — sem tocar na Base, sem tocar no bruto.

    `novo` é o único passo do ciclo que escreve andaime: copia o TXT byte a byte para
    `ciclos/<SIGLA>/original.txt`, sela com SHA-256, e escreve `ciclo.toml` + `pacote` com os
    números já medidos. A curadoria continua sendo de quem escreve o `.toml`: o andaime nasce
    com os campos vazios, para que a ausência seja visível em vez de um zero disfarçado de
    resultado. E a fonte não se reescreve — se o `original.txt` do ciclo já existe e difere,
    o passo aborta; preservação é o que resta da transcrição depois do fim da apostila."""
    bruto = open(txt, "rb").read()
    nome = os.path.basename(txt)
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", nome)
    if not m:
        sys.exit(f"não achei data no nome do arquivo ({nome}) — a sigla do ciclo é a data da fonte")
    sigla = sigla or "P" + m.group(0)
    titulo = re.sub(r"^.*?\d{4}-\d{2}-\d{2}\s*[-–—]?\s*", "", nome)[:-4].strip() or sigla
    pasta = os.path.join(RAIZ, "ciclos", sigla)
    destino = os.path.join(pasta, "original.txt")
    os.makedirs(pasta, exist_ok=True)
    t = bruto.decode("utf-8", errors="surrogateescape").replace("\r\n", "\n")
    ctrl = sum(1 for b in bruto if b < 32 and b not in (9, 10, 13))
    if ctrl:
        sys.exit(f"⛔ o TXT tem {ctrl} byte(s) de controle e NADA foi copiado — a esteira exige "
                 f"entrada limpa: trate o arquivo antes (o portão A existe para ser lido, "
                 f"não para ser apagado)")
    if os.path.exists(destino):
        if open(destino, "rb").read() == bruto:
            print("  · `original.txt` já batia byte a byte com o recebido: nenhuma reescrita")
        else:
            sys.exit(f"⛔ `ciclos/{sigla}/original.txt` existe e É DIFERENTE do TXT recebido — "
                     f"fonte preservada não se sobrescreve: traga o arquivo certo ou abra o "
                     f"ciclo com outra sigla, declarando por quê")
    else:
        with open(destino, "wb") as fh:
            fh.write(bruto)
    cfg, pac = os.path.join(pasta, "ciclo.toml"), os.path.join(pasta, f"pacote_{sigla}.txt")
    linhas = t.split("\n")
    com_fala = [l for l in linhas if len(l.strip()) > 40]
    if not os.path.exists(cfg):
        open(cfg, "w", encoding="utf-8").write("\n".join([
            f"# ciclo.toml — ciclo leve {sigla} · andaime escrito por `motor.py novo`",
            "# ──────────────────────────────────────────────────────────────────────────────",
            "# Toda curadoria mora AQUI. Regras vigentes: DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md.",
            "# O que está vazio abaixo é pendência do aplicador, não estado da Base: o portão D",
            "# confere cada número declarado e o livro-razão responde pelo que foi recusado.",
            "",
            f'sigla = "{sigla}"',
            f'titulo = "{titulo}"',
            f'data_fonte = "{m.group(3)}/{m.group(2)}/{m.group(1)}"',
            f'pasta_fonte = "ciclos/{sigla}"',
            'arquivo_fonte = "original.txt"',
            f'pacote = "pacote_{sigla}.txt"',
            f'sha256_fonte = "{sha256(destino)}"',
            "",
            f'baseline_commit = "{HEAD_ATUAL}"   # HEAD de onde o ciclo partiu; o portão D mede DELTA',
            'portoes_ativos = ["A", "B", "C", "D"]',
            "max_perolas = 25",
            "exportar_candidatas = false       # true só em ensaio declarado: o portão real é `aprovada`",
            "",
            'cobertura = "não-transcrita neste formato (deliberado: despacho de 29/08/2026 encerra a '
            'exigência de apostila integral); fonte integral preservada em original.txt, selada por '
            'SHA-256 na entrada; livro-razão de âncoras registra cada span encontrado, aceito e recusado"',
            'teto = "suspenso-com-cadencia"',
            "termos_novos = []",
            'veto_lexico = ["p****", "m****", "b******", "e******"]',
            "fichas_que_nomeiam_grupo = []",
            "",
            "[delta_esperado]",
            "arquivos = 0      # fichas criadas por este ciclo",
            "ficha_true = 0   # viradas no cadastro",
            "termos = 0       # termos novos: só por pérola aprovada, com linha no §4 do dossiê",
            "relacoes = 0     # arestas novas: tipada + evidência + selo datado, ou nada",
            "vinculos = 0    # códigos que passam a carregar a sigla do ciclo na lista de fontes",
            "",
            "[materializar]",
            "codigos = []      # fichas a CRIAR (ordem do Curador; só com bloco no pacote)",
            "",
            "[vitorias]",
            "provas = []         # uma linha por vitória: \"RC-xxx = <afirmativa> | prova: <trecho>\"",
            "# A prova é um trecho LITERAL da `## Ampliação — <SIGLA>` da ficha: o motor confere byte a",
            "# byte depois de ampliar e o §0 do dossiê só imprime o que passou. Mesa vazia é lícita (nem",
            "# todo ciclo vence algo novo); linha sem `| prova:` aborta — vitória narrada não é vitória.",
            "[ampliar]",
            "codigos = []      # vazio = todos os códigos do pacote que já têm arquivo",
            "",
            "[tese]",
            "pontos = []      # prosa SEM «…»: sem apostila, o verbatim não cobre o resumo",
            "",
            "[definicoes]",
            "",
            "[observacoes]",
            "",
            "[travas]",
            "",
            "[lacunas]",
            "",
        ]))
    if not os.path.exists(pac):
        open(pac, "w", encoding="utf-8").write("\n".join([
            f"# Pacote de ampliação — {sigla} · andaime por `motor.py novo`",
            "# Cada item de BLOCO 1 é UMA aspa cortada do bruto por",
            f'#   motor.py --ciclo {sigla} busca "<âncora>"',
            "# colada como veio, com rótulo entre [colchetes] e glosa depois do travessão. Aspa de",
            "# glosa que não seja span conferido perde a aspa na materialização — e o motor imprime.",
            "# BLOCO 2/3/4/5 são as notas do rite: fila sem arquivo, datas, radar e retidos.",
            "",
            "### BLOCO 1 — o que entra em ficha",
            "",
            "### BLOCO 2 — termos tocados sem arquivo (fila para a cadência do teto)",
            "",
            "### BLOCO 3 — obras, datas e anterioridade (nada harmonizado: D-9)",
            "",
            "### BLOCO 4 — radar datado (promessa só aqui, nunca em ficha: D-11)",
            "",
            "### BLOCO 5 — retidos por trava (nada é silenciado; nada destes entra em ficha)",
            "",
        ]))
    print(f"ciclo {sigla} aberto · {len(bruto):,} B copiados byte a byte".replace(",", "."))
    print(f"  sha256: {sha256(destino)[:16]}… · bytes de controle: {ctrl}")
    print(f"  {len(linhas)} linhas · {len(com_fala)} com fala (>40 chars) · "
          f"{len(t.split()):,} palavras".replace(",", "."))
    print(f"  maior linha: {max(len(l) for l in linhas):,} chars".replace(",", "."))
    print(f"  andaime: {os.path.relpath(cfg, RAIZ)} · {os.path.relpath(pac, RAIZ)}")
    print("  ⚠️ nada da Base foi tocado e nada foi garimpado ainda: edite `ciclo.toml` e o pacote; "
          "leitura integral com `fatias`, aspas cortadas com `busca`, portões com `tudo`")


def busca(c: Ciclo, termo: str, limite: int = 20) -> None:
    """Corta a aspa em vez de deixá-la digitada: para cada ocorrência do termo, imprime o
    período verbatim com endereço — o que se cola no pacote é o que o motor acabou de tirar
    do bruto, e o portão B confere outra vez na saída. Nenhuma aspa digitada à mão significa
    isto, não «prometo transcrever certo»."""
    if not termo:
        sys.exit("busca pede a expressão-âncora: --ciclo <SIGLA> busca \"trecho do bruto\"")
    f = c.fonte
    achados = [m.start() for m in re.finditer(re.escape(termo), f.raw, re.I)]
    if not achados:
        sys.exit(f"busca: {termo!r} não ocorre no bruto — âncora inventada é o que a casa mais "
                 f"teme; confira a grafia que o STT escreveu (`fatias` mostra o que existe)")
    for n, i in enumerate(achados[:limite], 1):
        a = i
        while a > 0 and f.raw[a - 1] != "\n" and not FRASE.search(f.raw[a - 1]):
            a -= 1
        b = i + len(termo)
        while b < len(f.raw) and not FRASE.search(f.raw[b - 1]):
            b += 1
        span = " ".join(f.raw[a:b].split())
        ok, _, _ = f.verificar(span)
        print(f"  [{n}/{len(achados)}] {f.uaddr(a)} · chars {a}-{b} · {len(span)} c · "
              f"{'✓ verifica' if ok else '✗ NÃO VERIFICA'}")
        print("      «" + span + "»")
    if len(achados) > limite:
        print(f"  … {len(achados) - limite} ocorrência(s) além do limite {limite}: refine a âncora "
              f"— largo demais é recorte ruim, não falta de aspas")


def fatias(c: Ciclo, largura: int = 15000) -> None:
    """Leitura integral com prova de cobertura, o único pedaço do rite pesado que a esteira
    leve não pode perder de vista: ela não reescreve a transcrição, mas quem a garimpa tem de
    tê-la lido inteira. Corte em fronteira de período, endereço em cada fatia, e no fim a
    asserção de que a concatenação É o arquivo — cobertura é igualdade de texto, não promessa."""
    t = c.fonte.raw
    corte, i = [], 0
    while i < len(t):
        j = min(len(t), i + largura)
        if j < len(t):
            k = max((m.end() for m in re.finditer(r"[.!?…]\s", t[i:j])), default=0)
            j = i + k if k else j
        corte.append((i, j))
        i = j
    print(f"fonte com {len(t):,} chars em {len(corte)} fatias de até {largura:,} chars "
          f"(fronteira de período)".replace(",", "."))
    for n, (a, b) in enumerate(corte, 1):
        print(f"\n── FATIA {n}/{len(corte)} · {c.fonte.uaddr(a)} · chars {a}-{b} "
              f"· {b - a:,} c ".replace(",", ".") + "─" * 8)
        print(t[a:b])
    recon = "".join(t[a:b] for a, b in corte)
    chk(recon == t, f"cobertura provada: {len(corte)} fatias reconstituem o bruto byte a byte "
                    f"({len(t):,} chars)".replace(",", "."),
        "as fatias NÃO reconstituem o bruto — o cortador é que está errado, consertar aqui")


# ───────────────────────────────────────────────────────────────────────── selftest
CASOS_SELFTEST = 9        # a régua é UMA: o `9/9` impresso e o código de saída vêm daqui


def selftest() -> int:
    """As 9 anomalias canônicas da casa, plantadas numa fonte falsa. Cada portão tem de
    pegar a sua. Sem isto, 'menos código por ciclo' significa só 'menos freio'."""
    import tempfile
    print("SELFTEST · anomalias plantadas, todas têm de ser detectadas")
    pegou = 0
    texto = ("Título da palestra falsa\n\n"
             "A nave pequena flutuava sobre o mar. O cérebro radiata não funciona aqui.\n"
             "O processo de exídio foi parado por contrato em 2050, e a peça estava limpa.\n"
             "A nave pequena flutuava sobre o mar. repetida para o caso ambíguo.\n"
             "Frase sem aspa alguma, apenas para dar corpo ao arquivo. " * 12)
    with tempfile.TemporaryDirectory() as tmp:
        bruto = os.path.join(tmp, "original.txt")
        open(bruto, "w", encoding="utf-8").write(texto)
        f = Fonte(bruto)
        chk(not f.verificar("o criador assinou o contrato com os túatha")[0],
            "1 · âncora inexistente é rejeitada", "âncora inventada passou — o motor aceitaria citação falsa")
        pegou += 1
        try:
            f.localizar("A nave pequena flutuava")
            amb = False
        except SystemExit:
            amb = True
        chk(amb, "2 · âncora ambígua aborta em vez de escolher por conta própria",
            "âncora ambígua foi resolvida em silêncio")
        pegou += 1
        sujo = texto.replace("Frase sem", "Frase\x08 sem")          # a linha-padrão se repete: contam-se todos
        open(bruto, "w", encoding="utf-8").write(sujo)
        n_ctrl = Fonte(bruto).controles
        chk(n_ctrl == sujo.count("\x08"),
            f"3 · byte de controle contado na entrada: {n_ctrl} de {sujo.count(chr(8))} plantados (o `0x08` do DOCX)",
            f"byte de controle invisível ao portão A: contou {n_ctrl}, plantados {sujo.count(chr(8))}")
        pegou += 1
        chk(not f.verificar("O cérebro radiata não funcionava aqui")[0],
            "4 · paráfrase vestida de citação não passa no verbatim",
            "o verbatim deixou passar aspa alterada — o veneno de um corpus RAG")
        pegou += 1
        chk(f.verificar("a peça estava limpa")[0] and f.verificar("processo de exídio")[0],
            "5 · cedilha e acento atravessam a normalização (o defeito herdado do `ç`)",
            "cedilha quebrou o caça-âncoras de novo")
        pegou += 1
        i = re.search(r"O cérebro radiata", f.raw).start()
        a = i
        while a > 0 and f.raw[a - 1] != "\n" and not FRASE.search(f.raw[a - 1]):
            a -= 1
        b = i
        while b < len(f.raw) and not FRASE.search(f.raw[b - 1]):
            b += 1
        span = " ".join(f.raw[a:b].split())
        chk(f.verificar(span)[0],
            f"6 · o cortador de aspas devolve span que verifica ({len(span)} c)",
            "o recorte por período não confere com o bruto — nada que ele corta é citável")
        pegou += 1
        sig = "P0000-00-00"
        RAIZ_ant, HEAD_ant = globals()["RAIZ"], globals()["HEAD_ATUAL"]
        globals()["RAIZ"], globals()["HEAD_ATUAL"] = tmp, "selftest"
        try:
            os.makedirs(os.path.join(tmp, "ciclos", sig), exist_ok=True)
            with open(os.path.join(tmp, "ciclos", sig, "original.txt"), "w", encoding="utf-8") as fh:
                fh.write("outra coisa, que não é o bruto")
            open(os.path.join(tmp, "2023-12-17 Falsa.txt"), "w", encoding="utf-8").write(texto)
            recusou = False
            try:
                novo(os.path.join(tmp, "2023-12-17 Falsa.txt"), sig)
            except SystemExit as e:
                recusou = "DIFERENTE" in str(e)
        finally:
            globals()["RAIZ"], globals()["HEAD_ATUAL"] = RAIZ_ant, HEAD_ant
        chk(recusou, "7 · `novo` recusa sobrescrever uma fonte preservada que difere",
            "a abertura deixaria o ciclo reescrever um `original.txt` já selado")
        pegou += 1
        chk(_selftest_vincular(tmp),
            "8 · o vínculo na lista de fontes é idempotente e não toca em linha de relação",
            "`inscreve_fonte` corromperia o cadastro: reexecução mudando o texto, ou aresta "
            "sendo tratada como termo")
        pegou += 1
        chk(_selftest_vitoria(),
            "9 · a vitória declarada é conferida na seção da ficha (e um caractere reprova)",
            "`[vitorias]` deixaria o dossiê narrar uma vitória que a ficha não contém — o "
            "produto passaria a valer mais do que a prova")
        pegou += 1
    print(f"  selftest: {pegou}/{CASOS_SELFTEST}")
    return pegou


# ───────────────────────────────────────────────────────────────────────────── CLI
def main() -> None:
    ap = argparse.ArgumentParser(description="Motor Único da esteira leve")
    ap.add_argument("--ciclo", default="")
    ap.add_argument("passo", nargs="?", default="status",
                    choices=["status", "entrada", "ancorario", "dossier", "rag", "materializar",
                             "virar", "ampliar", "vincular", "portoes", "tudo", "novo", "busca",
                             "fatias", "selftest"])
    ap.add_argument("args", nargs="*", default=[],
                    help="`novo`: o TXT recebido · `busca`: a expressão-âncora [limite] · "
                         "`fatias`: largura em chars")
    a = ap.parse_args()
    if a.passo == "novo":
        if not a.args:
            ap.error("novo pede o TXT recebido: motor.py novo <arquivo.txt> [SIGLA]")
        globals()["RAIZ"] = _raiz_do_repo()
        globals()["HEAD_ATUAL"] = subprocess.run(["git", "-C", globals()["RAIZ"], "rev-parse",
                                                  "--short", "HEAD"],
                                                 capture_output=True, text=True).stdout.strip() or "?"
        txt = a.args[0] if os.path.isabs(a.args[0]) else os.path.join(globals()["RAIZ"], a.args[0])
        novo(txt, a.ciclo or (os.path.basename(a.args[1]) if len(a.args) > 1 else ""))
        sys.exit(0)
    if a.passo == "selftest":
        try:
            n = selftest()
        except FalhaPortao as e:
            print(f"  SELFTEST FALHOU: {e}")
            sys.exit(3)
        sys.exit(0 if n == CASOS_SELFTEST else 3)
    if not a.ciclo:
        ap.error("--ciclo <SIGLA> é obrigatório (exceto para selftest)")
    c = Ciclo(a.ciclo)
    if a.passo == "busca":
        busca(c, a.args[0] if a.args else "", int(a.args[1]) if len(a.args) > 1 else 20)
        sys.exit(0)
    if a.passo == "fatias":
        fatias(c, int(a.args[0]) if a.args else 15000)
        sys.exit(0)
    try:
        if a.passo == "status":
            status(c)
        elif a.passo == "entrada":
            portao_A(c)
        elif a.passo == "ancorario":
            ancorario(c)
        elif a.passo == "dossier":
            dossie(c)
        elif a.passo == "rag":
            rag(c)
        elif a.passo == "materializar":
            materializar(c)
        elif a.passo == "virar":
            virar_ficha(c)
        elif a.passo == "ampliar":
            ampliar(c)
        elif a.passo == "vincular":
            vincular(c)
        elif a.passo == "vitorias":
            vistoria(c)
        elif a.passo == "portoes":
            for nome, letra in (("portao_A", "A"), ("portao_B", "B"), ("portao_C", "C"), ("portao_D", "D")):
                if letra in c.portoes_ativos:
                    globals()[nome](c)
        elif a.passo == "tudo":
            portao_A(c)
            materializar(c)
            ampliar(c)
            virar_ficha(c)
            vincular(c)
            c = Ciclo(a.ciclo)                                 # relê: a Base mudou de estado
            vistoria(c)                                        # a vitória é conferida na ficha
            ancorario(c)
            dossie(c)
            rag(c)
            for nome in ("portao_A", "portao_B", "portao_C", "portao_D"):
                if nome[-1] in c.portoes_ativos:
                    globals()[nome](c)
    except FalhaPortao as e:
        print(f"\nPORTÃO VERMELHO: {e}")
        sys.exit(3)
    c.cfg.conferir_uso(set(c.base.termos))
    print("motor: fim")



# ──────────────────────────── o ciclo leve sobre fichas que já existem, e a malha
MARCACICLO = "**Materialização (não é criação).**"
FONTE_LINHA = "| {sigla} | {titulo} (palestra) | — | transcrição automatizada; citação |"


def inscreve_fonte(txt: str, cod: str, sigla: str) -> tuple[str, str]:
    """Acrescenta `sigla` à lista de fontes do termo `cod` no TEXTO do cadastro, e devolve
    (texto, estado). Pura de propósito: é o que permite testar a inserção antes de ela
    tocar no arquivo, e é a razão de o selftest poder garanti-la sem reescrever a Base.

    estado: `inseriu` · `ja-estava` · `sem-linha` · `sem-lista`.
    `sem-lista` não cria a lista — linha de cadastro sem o sexto campo é anomalia do
    cadastro, e o ciclo declara, não conserta por cima."""
    mudou = "sem-linha"
    linhas = txt.split("\n")
    for n, l in enumerate(linhas):
        m = re.match(r"^(\s*)\(\s*[\"']" + cod + "[\"']\s*,", l)
        if not m:
            continue
        abre, fecha = l.rfind("["), l.rfind("]")
        if abre < 0 or fecha <= abre:
            mudou = "sem-lista"
            break
        dentro = l[abre:fecha]
        if re.search(r"[\"']" + sigla + r"[\"']", dentro):
            mudou = "ja-estava"
            break
        novo = dentro.rstrip()
        novo = novo + f', "{sigla}"]' + l[fecha + 1:]               # fecha a lista, reabre o resto
        linhas[n] = l[:abre] + novo
        mudou = "inseriu"
        break
    return "\n".join(linhas), mudou


def vincular(c: Ciclo) -> None:
    """Catálogo é vínculo: sem a sigla na lista de fontes do cadastro, a ampliação existe na
    ficha e não existe na malha — quem procura 'que fontes tocam RC-378' não acharia este
    ciclo. Um código por linha, idempotente, e só para quem tem bloco no pacote (o motor não
    vincula o que não leu)."""
    caminho = os.path.join(c.raiz, "ferramentas", "dados_termos.py")
    txt = open(caminho, encoding="utf-8").read()
    estados: dict[str, int] = {}
    for cod in sorted(c.pacote.blocos):
        txt, est = inscreve_fonte(txt, cod, c.sigla)
        estados[est] = estados.get(est, 0) + 1
    if estados.get("inseriu"):
        open(caminho, "w", encoding="utf-8").write(txt)
        c.base = Base(c.raiz, c.sigla)                              # relê: a Base mudou de estado
    c.base = Base(c.raiz, c.sigla)
    resumo = " · ".join(f"{k}: {v}" for k, v in sorted(estados.items()))
    chk(not estados.get("sem-linha") and not estados.get("sem-lista"),
        f"vínculos do ciclo na malha — {resumo}",
        f"não consegui vincular: " + "; ".join(
            f"{n} código(s) {k}" for k, n in estados.items() if k in ("sem-linha", "sem-lista")))


def ampliar(c: Ciclo) -> None:
    """Insere ou substitui a seção `## Ampliação — <sigla>` numa ficha que JÁ EXISTE, sem
    tocar em mais nada do arquivo. É o passo que o ciclo zero não exercitou (ele só criou
    fichas novas) e sem o qual o ciclo leve não tem como pousar numa palestra nova: a fonte
    não reescreve a ficha, acrescenta a seção dela."""
    alvos = list(c.ampliar) or [cod for cod in c.pacote.blocos if cod in c.fichas]
    substituídas, novas, divergentes = 0, 0, []
    for cod in alvos:
        arq = c.fichas.get(cod)
        if not arq:
            novas.append(cod)
            continue
        corpo = open(arq, encoding="utf-8").read()
        secao = (f"## Ampliação — {c.sigla}" + (f" ({c.titulo})" if c.titulo else "") + "\n\n"
                 + c.secao_limpa(cod) + "\n\n")
        m = re.search(r"^## Ampliação — " + re.escape(c.sigla) + r".*?(?=^## |^---\s*$|\Z)",
                      corpo, re.M | re.S)
        if m:
            if " ".join(m.group(0).split()) != " ".join(secao.split()) and not c.substituir:
                divergentes.append(cod)
                continue
            corpo = corpo[:m.start()] + secao + corpo[m.end():]
            substituídas += 1
        else:
            i = corpo.find("\n## Fontes")
            corpo = (corpo[:i] + "\n" + secao + corpo[i:] if i >= 0
                     else corpo.rstrip() + "\n\n" + secao)
            substituídas += 0
            novas += 0
        # a tabela de Fontes da ficha também precisa ficar coerente com a seção que entrou
        secao_fontes = re.search(r"^## Fontes\s*$(.*?)(?=^## |\Z)", corpo, re.M | re.S)
        if secao_fontes and f"| {c.sigla} |" not in secao_fontes.group(1) and f"{c.sigla}." not in secao_fontes.group(1):
            i_fontes = corpo.index("## Fontes")
            j = corpo.find("|---|", i_fontes)
            if j >= 0:
                linha = FONTE_LINHA.format(sigla=c.sigla, titulo=c.titulo)
                k = corpo.index("\n", j)
                corpo = corpo[:k + 1] + linha + corpo[k:]
            else:
                # `## Fontes` sem tabela markdown (prosa): acrescenta a sigla como linha de prosa
                k = corpo.index("\n", i_fontes)
                corpo = corpo[:k + 1] + f"{c.sigla}.\n" + corpo[k + 1:]
        open(arq, "w", encoding="utf-8").write(corpo)
        assert f"## Ampliação — {c.sigla}" in corpo, f"{cod}: a seção não entrou na ficha"
        print(f"  · {cod}: seção do ciclo {'substituída (reexecução)' if m else 'inserida'} em "
              f"{os.path.relpath(arq, c.raiz)}")
    if divergentes:
        print(f"  ⚠️ {len(divergentes)} ficha(s) já tinham seção deste ciclo ESCRITA À MÃO "
              f"(conteúdo divergente do pacote): " + ", ".join(divergentes[:12]) +
              " — nada foi sobrescrito. Se a intenção é substituir, declare "
              "`substituir = true` em [ampliar] e diga por quê no relatório do ciclo.")
    if novas:
        print(f"  · {len(novas)} código(s) do pacote sem arquivo de ficha: fila declarada no §4 "
              f"do dossiê, e criação de ficha é `materializar`, com ordem no `.toml`")
    tot = [x for v in getattr(c, "log_rebaixado", {}).values() for x in v]
    if tot:
        print(f"  ⚠️ {len(tot)} aspa(s) de glosa rebaixada(s) — não eram span verificado na fonte: "
              + "; ".join(f"{x!r}" for x in tot))


def _selftest_vincular(tmp: str) -> bool:
    """A inserção na lista de fontes, fora do arquivo real: idempotência e forma. Duas
    execuções têm de dar o mesmo texto, e uma linha de RELACOES não pode ser tocada."""
    amostra = "\n".join([
        "TERMOS = [",
        '    ("RC-001", "Javé", A[0], A[1], P, ["B031", \'P2020-08-08\'], "RC-017", True),',
        '    (\'RC-002\', "Rebelião", B[0], B[1], P, [\'B031\'], "", False),',
        "]",
        'RELACOES = [',
        '    ("RC-001", "sinônimo", "RC-037", "B031"),',
        "]",
    ])
    a, e1 = inscreve_fonte(amostra, "RC-001", "P2023-12-17")
    b, e2 = inscreve_fonte(a, "RC-001", "P2023-12-17")
    _, e3 = inscreve_fonte(a, "RC-002", "P2023-12-17")
    _, e4 = inscreve_fonte(a, "RC-999", "P2023-12-17")
    return (e1, e2, e3, e4) == ("inseriu", "ja-estava", "inseriu", "sem-linha") and a == b \
        and '("RC-001", "sinônimo", "RC-037", "B031"),' in a
# ──────────────────────────────────── a vitória do ciclo: declarada, e provada na ficha
LINHA_VITORIA = re.compile(r"^(RC-\d{3})\s*=\s*(.+)$")


def corta_vitoria(linha: str) -> tuple[str, str, str]:
    """`RC-xxx = <afirmativa> | prova: <trecho literal da seção>` → (código, afirmativa,
    trecho). Corte puro, sem Base: é o que permite ao selftest exercitar a regra inteira.

    A afirmativa é prosa do aplicador; a prova é o trecho que o motor escreveu na ficha.
    Sem `| prova:` a linha não é vitória, é narração — e narração não entra em dossiê."""
    m = LINHA_VITORIA.match(linha.strip())
    if not m:
        raise ValueError(f"linha de vitória ilegível (esperado `RC-xxx = … | prova: …`): {linha!r}")
    cod, corpo = m.group(1), " ".join(m.group(2).split())
    af, sep, prova = corpo.partition("| prova:")
    if not sep:
        raise ValueError(f"{cod}: vitória sem `| prova: <trecho da seção>` — sem testemunha é narrativa")
    prova = " ".join(prova.strip().split())
    if len(prova) < 20:
        raise ValueError(f"{cod}: prova de {len(prova)} c é referência, não trecho; o portão "
                         f"confronta o trecho com a seção escrita por este ciclo")
    if not af.strip():
        raise ValueError(f"{cod}: linha com prova e sem afirmativa")
    return cod, af.strip(), prova


def confere_vitoria(secao: str, trecho: str) -> bool:
    """A prova só vale se o trecho está DENTRO da `## Ampliação — <SIGLA>` deste ciclo.
    Espaço colapsado, acento preservado: um caractere a mais ou a menos reprova — é assim
    que a mesa declara o que a ficha contém, e não o contrário."""
    if not secao or not trecho:
        return False
    return " ".join(trecho.split()) in " ".join(secao.split())


def vitorias_do_ciclo(c: Ciclo) -> list[tuple[str, str, str, bool]]:
    """[(código, afirmativa, prova, conferida)] — a conferência lê a ficha como ela está AGORA
    no disco, depois de `ampliar`; por isso a vistoria vem depois da ampliação e não antes."""
    out = []
    for linha in c.vitorias:
        cod, af, prova = corta_vitoria(linha)
        secao = ""
        if cod in c.fichas:
            secao = secao_da_ficha(open(c.fichas[cod], encoding="utf-8").read(), c.sigla)
        out.append((cod, af, prova, confere_vitoria(secao, prova)))
    return out


def vistoria(c: Ciclo) -> None:
    """Vistoria de vitória: cada linha de `[vitorias]` tem de estar provada na ficha. Mesa
    vazia é lícita (nem todo ciclo vence algo novo); linha divergente aborta o passo."""
    if not c.vitorias:
        print("  vitorias: mesa vazia — o ciclo não declara vitória (lícito)")
        return
    ruins = []
    for cod, af, prova, ok in vitorias_do_ciclo(c):
        print(f"  {'✓' if ok else '✗'} {cod} · {af}")
        if not ok:
            ruins.append(f"{cod}: a afirmativa não está na `## Ampliação — {c.sigla}` da ficha")
    if ruins:
        sys.exit("PORTÃO DE VITÓRIA: " + " · ".join(ruins) +
                 " — ou a ficha ainda não foi ampliada por este ciclo, ou a mesa "
                 "prometeu mais do que o pacote escreveu")
    print(f"  vitorias: {len(c.vitorias)} vitória(s) conferida(s) byte a byte na ficha")


def vitorias_para_dossie(c: Ciclo) -> list[str]:
    """§0 do dossiê. A prova sai em `backticks`, nunca em aspas: aspas do dossiê são
    conferidas contra o `original.txt` pelo portão B, e o trecho da prova é da FICHA."""
    if not c.vitorias:
        return []
    L = ["## 0 · A vitória do ciclo (declarada, e provada na ficha)", "",
         "Prova = trecho literal da seção `## Ampliação — %s` da ficha, conferido byte a byte "
         "pelo motor. Nada aqui é promessa de resultado: é o que está no arquivo." % c.sigla, ""]
    for cod, af, prova, ok in vitorias_do_ciclo(c):
        L += [f"* **`{cod}`** — {af}",
              f"  · *prova* ({len(prova)} c, conferida={'sim' if ok else 'NÃO'}): "
              f"`{' '.join(prova.split())}`", ""]
    return L


def _selftest_vitoria() -> bool:
    """A vitória tem de ser provada na seção deste ciclo: um caractere de diferença reprova,
    ficha sem seção reprova, e linha sem prova não é linha de vitória."""
    secao = ("## Ampliação — P0000-00-00\n\n"
             "- **[P0000-00-00 · T]** «aspa» (U0002) — glosa que prova o ponto central.\n\n")
    ok_bom = confere_vitoria(secao, "glosa que prova o ponto central")
    ok_ruim = confere_vitoria(secao, "glosa que prova o ponto central, e mais o que não está")
    ok_troca = confere_vitoria(secao, "glosa que prova o ponto central.")   # "central." na seção: o ponto extra não é acréscimo de aspas
    ok_acento = confere_vitoria(secao, "glosa que prova o ponto central")  # mesma coisa, espaço duplo
    ok_austrado = confere_vitoria("", "glosa que prova o ponto central")
    try:
        cod, af, prova = corta_vitoria("RC-001 = Afirmativa qualquer. | prova: glosa que prova o ponto central")
        formato = (cod, af, prova) == ("RC-001", "Afirmativa qualquer.", "glosa que prova o ponto central")
        sem_prova = False
        try:
            corta_vitoria("RC-001 = Afirmativa sem testemunha")
        except ValueError:
            sem_prova = True
        curta = False
        try:
            corta_vitoria("RC-001 = A. | prova: curto")
        except ValueError:
            curta = True
    except ValueError:
        formato = sem_prova = curta = False
    return (ok_bom and ok_troca and ok_acento and not ok_ruim and not ok_austrado
            and formato and sem_prova and curta)

if __name__ == "__main__":
    main()
