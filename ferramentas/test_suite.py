#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (14 checks; Onda 0.1 + 1.5 + 2.1 + 2.5)
"""SUITE DE INTEGRIDADE DA BASE RC — Onda 0.1 (12 checks, só-stdlib).

Uso:  python3 ferramentas/test_suite.py        (a partir da raiz do repo)
Portão: exit 0 = verde. Checks com legado conhecido usam regressão contra
`ferramentas/test_baseline.json` (só falha o que for NOVO; item sanado vira
aviso pedindo atualização do baseline — nunca falha silenciosa).

Checks:
  T1  dados_termos importa + validar() OK
  T2  códigos em TERMOS[t][6] existem
  T3  códigos em RELACOES existem
  T4  ficha=True<->arquivo físico (3 sentidos)
  T5  verificar_verbetes.py exit 0
  T6  badge única + igual ao cadastro
  T7  tabela ## Fontes bemformada (regressão)
  T8  sem-fantasma: siglas B/P citadas existem (regressão)
  T9  status dentro do enum
  T10 HOLD.csv íntegro (parse + códigos existem)
  T11 higiene do parser de retorno (testes unitários puros)
  T12 via/confianca_fonte do canônico == regra do loader (1.5, regra interim)
  T13 frontmatter TOML das fichas-piloto parseia e bate com o registro (2.1)
"""
import csv
import glob as _glob
import io
import json
import os
import re
import subprocess
import sys
import unittest

FER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(FER)
sys.path.insert(0, FER)
import dados_termos as d  # noqa: E402

BASELINE = os.path.join(FER, "test_baseline.json")
EMOJI = {"candidato": "⚪", "provisório": "🟡", "em análise": "🟠",
         "verificado": "🟢"}


def _fmap():
    m = {}
    for p in _glob.glob(os.path.join(ROOT, "termos", "*.md")):
        mm = re.match(r"(RC-\d+)-", os.path.basename(p))
        if mm:
            m.setdefault(mm.group(1), []).append(p)
    return m


def _split(s):
    return {r.strip() for r in (s or "").split(";")
            if r.strip() and r.strip() != "—"}


# ------------------------------------------------------------------ T11 puro
def parse_decisao(row):
    """DECISÃO prevalece; letra única no OBS vale se vazia (fallback P7c)."""
    dec = (row.get("DECISÃO (V/X/?)") or "").strip().upper()
    if dec:
        return dec
    obs = (row.get("OBS") or "").strip().upper()
    return obs if obs in ("V", "X", "?") else ""


def validate_retorno_rows(rows):
    """Rejeita linha em branco / sem código (rito E3). Retorna lista."""
    rows = list(rows)
    for i, r in enumerate(rows, start=2):
        if not (r.get("código") or "").strip():
            raise ValueError(f"linha {i}: sem código (linha em branco?)")
    return rows


def load_hold(path=None):
    path = path or os.path.join(ROOT, "chancela", "HOLD.csv")
    with open(path, encoding="utf-8-sig") as f:
        return {r["código"].strip(): r["motivo"].strip()
                for r in csv.DictReader(f, delimiter=";") if r["código"].strip()}


def flag_hold(decisoes, hold=None):
    """decisoes: {cod: 'V'|'X'|'?'}. Retorna {cod: motivo} p/ V-sobre-HOLD."""
    hold = hold if hold is not None else load_hold()
    return {c: hold[c] for c, v in decisoes.items()
            if v == "V" and c in hold}


def assert_template_count(path, esperado):
    """Rito E3: template gerado deve ter exatamente N linhas de dados.

    Cura o incidente `40afd50` (template 5.4 vazio por nome de chunk errado).
    Uso: assert_template_count("chancela/P7-X.csv", n) logo após gerar.
    """
    with open(path, encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f, delimiter=";")
                if (r.get("código") or "").strip()]
    assert len(rows) == esperado, (
        f"{path}: {len(rows)} linhas, esperado {esperado} "
        "(nome de chunk errado? filtro vazio?)")
    return len(rows)


def _load_baseline():
    with open(BASELINE, encoding="utf-8") as f:
        return json.load(f)


class TestBase(unittest.TestCase):
    def test_T1_carrega_e_valida(self):
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            d.validar()
        finally:
            sys.stdout = old
        self.assertIn("OK:", buf.getvalue())

    def test_T2_t6_existem(self):
        exist = {t[0] for t in d.TERMOS}
        ruins = sorted({r for t in d.TERMOS for r in _split(t[6])
                        if r not in exist})
        self.assertEqual(ruins, [], f"t[6] órfãos: {ruins}")

    def test_T3_relacoes_existem(self):
        exist = {t[0] for t in d.TERMOS}
        ruins = sorted({c for a, _, b, _ in d.RELACOES for c in (a, b)
                        if c not in exist})
        self.assertEqual(ruins, [], f"RELACOES órfãs: {ruins}")

    def test_T4_ficha_arquivo(self):
        T = {t[0]: t for t in d.TERMOS}
        fm = _fmap()
        falhas = []
        falhas += [f"True-sem-arq:{c}" for c in T if T[c][7] and c not in fm]
        falhas += [f"False-com-arq:{c}" for c in T
                   if not T[c][7] and c in fm]
        falhas += [f"arq-sem-cad:{c}" for c in fm if c not in T]
        falhas += [f"multi-arq:{c}" for c, v in fm.items() if len(v) > 1]
        self.assertEqual(falhas, [], falhas)

    def test_T5_verbetes(self):
        r = subprocess.run(
            [sys.executable, os.path.join(FER, "verificar_verbetes.py"),
             os.path.join(ROOT, "pedagogico", "enciclopedia", "verbetes")],
            capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(r.returncode, 0, r.stderr[-2000:] or r.stdout[-2000:])

    def test_T6_badge(self):
        T = {t[0]: t for t in d.TERMOS}
        fm = _fmap()
        falhas = []
        for cod, paths in sorted(fm.items()):
            x = open(paths[0], encoding="utf-8").read()
            if x.startswith("+++"):
                # 2.1: envelope virou frontmatter TOML — xor estrito (G3.3)
                end = x.find("\n+++\n", 4)
                try:
                    import tomllib
                    front = tomllib.loads(x[4:end]) if end > 0 else {}
                except Exception as e:  # noqa: BLE001
                    falhas.append(f"{cod}: frontmatter inválido ({e})")
                    continue
                if "| **Status** |" in x[end:]:
                    falhas.append(f"{cod}: envelope duplicado (TOML e tabela)")
                if front.get("status") != T[cod][4]:
                    falhas.append(f"{cod}: status TOML x registro")
                continue
            b = re.findall(r"\| \*\*Status\*\* \| ([^|]+) \|", x)
            if len(b) != 1:
                falhas.append(f"{cod}: {len(b)} badges")
            elif not b[0].strip().startswith(EMOJI[T[cod][4]]):
                falhas.append(f"{cod}: badge {b[0].strip()!r} x {T[cod][4]}")
        self.assertEqual(falhas, [], falhas)

    def _regressao(self, chave, atuais):
        base = set(_load_baseline()[chave])
        novos = sorted(set(atuais) - base)
        sanados = sorted(base - set(atuais))
        self.assertEqual(novos, [], f"[{chave}] NOVOS: {novos}")
        if sanados:
            print(f"\nAVISO [{chave}] sanados, atualizar baseline: {sanados}")

    def test_T7_fontes_wellformed(self):
        fm = _fmap()
        ruins = []
        for cod, paths in sorted(fm.items()):
            x = open(paths[0], encoding="utf-8").read()
            m = re.search(r"^## Fontes\n(.*?)(?=^## |\Z)", x, re.M | re.S)
            if not m:
                continue  # ausência é matéria de curadoria, não de forma
            rows = [ln for ln in m.group(1).split("\n") if ln.startswith("|")]
            if len(rows) >= 2 and any(
                    r.count("|") != rows[0].count("|") for r in rows[2:]):
                ruins.append(cod)
        self._regressao("fontes_malformadas", ruins)

    def test_T8_sem_fantasma(self):
        dirsB, dirsP = set(), set()
        for base in ("livros/CONCLUIDOS", "livros/AMOSTRAS"):
            bp = os.path.join(ROOT, base)
            if os.path.isdir(bp):
                for dd in os.listdir(bp):
                    m = re.match(r"(B\d{3})", dd)
                    if m:
                        dirsB.add(m.group(1))
        for base in ("apostilas/CONCLUIDAS", "ciclos"):
            bp = os.path.join(ROOT, base)
            for dd in os.listdir(bp):
                m = re.search(r"P?(\d{4}-\d{2}-\d{2})", dd)
                if m:
                    dirsP.add("P" + m.group(1))
        fantas = set()
        for t in d.TERMOS:
            f5 = t[5] if isinstance(t[5], str) else ";".join(t[5])
            for s in set(re.findall(r"B\d{3}", f5)) - dirsB:
                fantas.add(f"cad:{t[0]}:{s}")
        for p in _glob.glob(os.path.join(ROOT, "termos", "*.md")):
            cod = re.match(r"(RC-\d+)-", os.path.basename(p)).group(1)
            with open(p, encoding="utf-8") as _f:
                x = _f.read()
            if x.startswith("+++\n"):  # 2.1: varredura é da CARTA; o envelope
                _e = x.find("\n+++\n", 4)  # reflete o registro, que já é fiscalizado
                if _e >= 0:
                    x = x[_e + 5:]
            for s in set(re.findall(r"\b(B\d{3})\b", x)) - dirsB:
                fantas.add(f"ficha:{cod}:{s}")
            for s in set(re.findall(r"\b(P\d{4}-\d{2}-\d{2})\b", x)) - dirsP:
                fantas.add(f"ficha:{cod}:{s}")
        self._regressao("fantasmas", sorted(fantas))

    def test_T9_status_enum(self):
        ruins = [(t[0], t[4]) for t in d.TERMOS if t[4] not in EMOJI]
        self.assertEqual(ruins, [], ruins)

    def test_T12_via_confianca(self):
        """1.5: campos derivados no canônico coincidem com a regra do loader;
        conjunto P7-conhecimento == conjunto `em análise` (166 hoje)."""
        from loader import via_de, confianca_de
        doc = json.load(open(os.path.join(ROOT, "base", "canonico.json"),
                             encoding="utf-8"))
        by = {t["codigo"]: t for t in doc["termos"]}
        ruins = []
        for t in d.TERMOS:
            j = by.get(t[0])
            if j is None:
                ruins.append(f"{t[0]}: ausente no canônico")
                continue
            if j.get("via") != via_de(t):
                ruins.append(f"{t[0]}: via {j.get('via')!r} != regra")
            if j.get("confianca_fonte") != confianca_de(t):
                ruins.append(f"{t[0]}: confianca_fonte != regra")
        emana = {t[0] for t in d.TERMOS if t[4] == "em análise"}
        p7 = {k for k, v in by.items() if v.get("via") == "P7-conhecimento"}
        if p7 != emana:
            ruins.append(f"P7 != em análise: sóP7={sorted(p7 - emana)[:5]} "
                         f"sóAnálise={sorted(emana - p7)[:5]}")
        self.assertEqual(ruins[:5], [], ruins[:5])

    def test_T13_frontmatter(self):
        """2.1: fichas com frontmatter -> TOML parseia e bate 1:1 com o registro."""
        import tomllib
        T = {t[0]: t for t in d.TERMOS}
        ruins = []
        n_front = 0
        for p in _glob.glob(os.path.join(ROOT, "termos", "*.md")):
            x = open(p, encoding="utf-8").read()
            if not x.startswith("+++"):
                continue
            n_front += 1
            cod = re.match(r"(RC-\d+)-", os.path.basename(p)).group(1)
            end = x.find("\n+++\n", 4)
            if end < 0:
                ruins.append(f"{cod}: frontmatter não fechado")
                continue
            try:
                f = tomllib.loads(x[4:end])
            except Exception as e:  # noqa: BLE001
                ruins.append(f"{cod}: TOML inválido ({e})")
                continue
            t = T.get(cod)
            if t is None:
                ruins.append(f"{cod}: sem registro")
                continue
            exp = {"codigo": cod, "nome": t[1], "categoria": t[2],
                   "subcategoria": t[3], "status": t[4], "fontes": list(t[5])}
            for k, v in exp.items():
                if f.get(k) != v:
                    ruins.append(f"{cod}: TOML.{k} diverge do registro")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(f.get("atualizado", ""))):
                ruins.append(f"{cod}: atualizado fora do ISO")
        print(f"\n[T13] {n_front} fichas com frontmatter (piloto 2.1)")
        self.assertEqual(ruins[:8], [], ruins[:8])

    def test_T14_tabelas_relacionados(self):
        """2.5 (M3): tabela '## Termos Relacionados' == f(cadastro) — par visto dos dois
        polos (espelho t[6] ∪ arestas RELACOES); linhas-candidato/auto/sem-código fora do match."""
        T = {t[0]: t for t in d.TERMOS}
        esp = {}
        for t in d.TERMOS:
            for c in str(t[6]).split(";"):
                c = c.strip()
                if c in T and c != t[0]:
                    esp.setdefault(t[0], set()).add(c)
                    esp.setdefault(c, set()).add(t[0])
        for a, _tip, b, _f in d.RELACOES:
            if a in T and b in T:
                esp.setdefault(a, set()).add(b)
                esp.setdefault(b, set()).add(a)
        ruins = []
        for p in sorted(_glob.glob(os.path.join(ROOT, "termos", "*.md"))):
            mc = re.match(r"(RC-\d+)-", os.path.basename(p))
            if not mc or mc.group(1) not in T:
                continue
            cod = mc.group(1)
            x = open(p, encoding="utf-8").read()
            carta = x[x.find("\n+++\n", 4) + 5:] if x.startswith("+++\n") else x
            m = re.search(r"(?ms)^## Termos Relacionados\n(.*?)(?=^## |\Z)", carta)
            have = set()
            for line in (m.group(1).splitlines() if m else []):
                for c in [y.strip() for y in line.strip().strip("|").split("|")]:
                    if re.fullmatch(r"RC-\d+", c) and c in T and c != cod:
                        have.add(c)
            if have != esp.get(cod, set()):
                ruins.append(cod)
        print(f"\n[T14] tabelas == cadastro (M3) · divergentes: {len(ruins)}")
        self.assertEqual(ruins[:8], [], f"tabelas divergem do cadastro: {ruins[:8]}")

    def test_T10_hold(self):
        hold = load_hold()
        exist = {t[0] for t in d.TERMOS}
        self.assertTrue(hold, "HOLD.csv vazio?")
        ruins = [c for c in hold if c not in exist]
        self.assertEqual(ruins, [], f"HOLD c/ código inexistente: {ruins}")


class TestParser(unittest.TestCase):
    def test_decisao_direta(self):
        self.assertEqual(parse_decisao({"DECISÃO (V/X/?)": "V", "OBS": ""}),
                         "V")

    def test_fallback_obs(self):
        self.assertEqual(parse_decisao({"DECISÃO (V/X/?)": "", "OBS": "x"}),
                         "X")

    def test_branco(self):
        self.assertEqual(parse_decisao({"DECISÃO (V/X/?)": "", "OBS": ""}),
                         "")

    def test_rejeita_linha_em_branco(self):
        with self.assertRaises(ValueError):
            validate_retorno_rows([{"código": "RC-001"}, {"código": ""}])

    def test_flag_hold(self):
        hold = {"RC-833": "retido", "RC-001": "x"}
        dec = {"RC-833": "V", "RC-001": "X"}
        self.assertEqual(flag_hold(dec, hold), {"RC-833": "retido"})

    def test_template_count_ok(self):
        import tempfile
        with tempfile.NamedTemporaryFile(
                "w", suffix=".csv", delete=False, encoding="utf-8-sig",
                newline="") as f:
            f.write("código;termo\nRC-001;X\nRC-002;Y\n")
            path = f.name
        try:
            self.assertEqual(assert_template_count(path, 2), 2)
        finally:
            os.unlink(path)

    def test_template_count_falha(self):
        import tempfile
        with tempfile.NamedTemporaryFile(
                "w", suffix=".csv", delete=False, encoding="utf-8-sig",
                newline="") as f:
            f.write("código;termo\n")
            path = f.name
        try:
            with self.assertRaises(AssertionError):
                assert_template_count(path, 12)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main(verbosity=1)
