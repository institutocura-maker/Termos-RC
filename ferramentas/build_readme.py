#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (README vivo; Onda 0.4)
"""Gera README.md vivo — Onda 0.4.

Fontes: loader (números, sempre vivos) + STATE-MIRROR §1 (narrativa de fase)
+ HOLD.csv + test_baseline.json (pontos de atenção).
Nunca editar o README à mão: regenere com `python3 ferramentas/build_readme.py`.

Restrição B-errata-1: a seção `## ⚠️ Pontos de atenção` DEVE existir e ser
lista numerada — a PARTE 6 do build_word.py a consome por regex.
"""
import csv
import json
import os
import re
import sys
from collections import Counter
from datetime import date

FER = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(FER)
sys.path.insert(0, FER)
from loader import TERMOS, RELACOES, via_de, confianca_de  # noqa: E402

st = Counter(t[4] for t in TERMOS)
fichas = sum(1 for t in TERMOS if t[7])
biblio_n = len(__import__("loader").BIBLIO)

mirror = open(os.path.join(RAIZ, "STATE-MIRROR.md"), encoding="utf-8").read()
m = re.search(r"^- Base: \*\*(.*?)\*\* \((.*?)\)\.", mirror, re.M)
fase = m.group(2) if m else "ver STATE-MIRROR.md"

with open(os.path.join(RAIZ, "chancela", "HOLD.csv"), encoding="utf-8-sig") as f:
    hold = [r["código"].strip() for r in csv.DictReader(f, delimiter=";")
            if r["código"].strip()]
base = json.load(open(os.path.join(FER, "test_baseline.json"), encoding="utf-8"))

L = []
A = L.append
A("# Base Terminológica RC — Revelações Cósmicas (Jan Val Ellam)")
A("")
A("> **README vivo** — gerado por `ferramentas/build_readme.py` em "
  f"{date.today().strftime('%d/%m/%Y')} — **não editar à mão**.")
A("> O README histórico (ago/2026) está arquivado em "
  "`docs/historico/README-2026-08-17.md`.")
A("")
A("## Números oficiais (lidos do cadastro a cada build)")
A("")
A(f"- **{len(TERMOS)} termos · {fichas} fichas · {len(RELACOES)} relações · "
  f"{biblio_n} obras**")
A(f"- Status: {st['candidato']}⚪ · {st['provisório']}🟡 · "
  f"{st['em análise']}🟠 · {st['verificado']}🟢")
_v = Counter(via_de(t) for t in TERMOS)
_c = Counter(confianca_de(t) for t in TERMOS)
A(f"- Via/confiança (1.5 · regra interim): {_v['P7-conhecimento']} "
  f"`P7-conhecimento` · {_v['P6-evidência']} `P6-evidência` — fontes: "
  f"{_c['alta']} alta · {_c['média']} média · {_c['baixa']} baixa")
A(f"- Fase: {fase}")
A("")
A("## Navegação")
A("")
A("- `indice-mestre.md` — todos os termos, com links para as fichas")
A("- `base-terminologica.xlsx` / `base-terminologica-leitura.docx` — espelhos "
  "gerados (leitura)")
A("- `APRESENTACAO-DO-SISTEMA.md` — arquitetura para auditores")
A("- `diagnostico/PLANO-APRIMORAMENTO-KB-2026-09-11.md` — ondas 0–3")
A("- `STATE-MIRROR.md` — estado operacional entre sessões")
A("- `01-ficha-modelo.md`, `02-vocabulario-controlado.md`, "
  "`convencoes-editoriais-rc.md` — padrões editoriais")
A("")
A("## ⚠️ Pontos de atenção")
A("")
A(f"1. **HOLD curatorial ({len(hold)} códigos)**: {', '.join(hold)} — "
  "ver `chancela/HOLD.csv` (motivo por código). Nenhum vira 🟢 sem despacho.")
A(f"2. **Legado sob regressão**: "
  f"{len(base['fontes_malformadas'])} tabelas Fontes malformadas + "
  f"{len(base['fantasmas'])} menções-fantasma no baseline — o test-suite só "
  "falha no que for novo.")
A("3. **P7 (chancela por conhecimento) pausado** durante a Onda 0; retoma sob "
  "os portões novos (`HOLD.csv` + suite).")
A("4. **Verdade-mestra em transição**: `dados_termos.py` segue vigente; "
  "canônico JSON/SQLite na Onda 1 (despacho pendente).")
A("")
A("---")
A("")
A(f"*Regenerado em {date.today().strftime('%d/%m/%Y')} · "
  "`python3 ferramentas/build_readme.py`*")
A("")

open(os.path.join(RAIZ, "README.md"), "w", encoding="utf-8").write("\n".join(L))
print(f"OK -> README.md ({len(TERMOS)}/{fichas}/{len(RELACOES)}/{biblio_n})")
