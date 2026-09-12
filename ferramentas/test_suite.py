#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SUITE DE INTEGRIDADE DA BASE RC — Onda 0.1 (11 checks, só-stdlib).

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
            for s in set(re.findall(r"\b(B\d{3})\b", x)) - dirsB:
                fantas.add(f"ficha:{cod}:{s}")
            for s in set(re.findall(r"\b(P\d{4}-\d{2}-\d{2})\b", x)) - dirsP:
                fantas.add(f"ficha:{cod}:{s}")
        self._regressao("fantasmas", sorted(fantas))

    def test_T9_status_enum(self):
        ruins = [(t[0], t[4]) for t in d.TERMOS if t[4] not in EMOJI]
        self.assertEqual(ruins, [], ruins)

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


if __name__ == "__main__":
    unittest.main(verbosity=1)
