#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (validador de schema hand-rolled; Onda 1.1)
"""Valida base/canonico.json — Onda 1.1 (schema hand-rolled, stdlib).

Regras: chaves presentes, tipos corretos, status no enum, códigos únicos,
sequência sem gaps, refs (relacionados + relacoes) existentes, ficha bool,
fontes lista de str. Exit 0 = válido; imprime falhas e exit 1 caso contrário.
"""
import json
import os
import re
import sys

FER = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(FER)
DOC = os.path.join(RAIZ, "base", "canonico.json")
ENUM = {"candidato", "provisório", "em análise", "verificado"}
TCAMPO = {"codigo": str, "nome": str, "categoria": str, "subcategoria": str,
          "status": str, "fontes": list, "relacionados": list, "ficha": bool}


def validar(path=DOC):
    doc = json.load(open(path, encoding="utf-8"))
    falhas = []
    termos = doc.get("termos", [])
    vistos = set()
    for i, t in enumerate(termos):
        ctx = t.get("codigo", f"#{i}")
        for k, tp in TCAMPO.items():
            if k not in t:
                falhas.append(f"{ctx}: sem chave {k}")
            elif not isinstance(t[k], tp):
                falhas.append(f"{ctx}: {k} tipo {type(t[k]).__name__}")
        if t.get("codigo") in vistos:
            falhas.append(f"{ctx}: código duplicado")
        vistos.add(t.get("codigo"))
        if t.get("status") not in ENUM:
            falhas.append(f"{ctx}: status {t.get('status')!r}")
        if not re.fullmatch(r"RC-\d{3}", t.get("codigo", "")):
            falhas.append(f"{ctx}: código fora do padrão")
    nums = sorted(int(c[3:]) for c in vistos if re.fullmatch(r"RC-\d{3}", c))
    if nums:
        gaps = [n for n in range(1, nums[-1] + 1) if n not in set(nums)]
        if gaps:
            falhas.append(f"gaps na sequência: {gaps[:10]}")
    for t in termos:
        for r in t.get("relacionados", []):
            if r not in vistos:
                falhas.append(f"{t['codigo']}: relacionado {r} inexistente")
    for j, r in enumerate(doc.get("relacoes", [])):
        for k in ("a", "tipo", "b", "fonte"):
            if k not in r:
                falhas.append(f"rel#{j}: sem chave {k}")
        if r.get("a") not in vistos or r.get("b") not in vistos:
            falhas.append(f"rel#{j}: ponta inexistente {r.get('a')}-{r.get('b')}")
    return falhas


if __name__ == "__main__":
    falhas = validar(sys.argv[1] if len(sys.argv) > 1 else DOC)
    if falhas:
        print(f"{len(falhas)} FALHAS:")
        for f in falhas[:20]:
            print("  X", f)
        sys.exit(1)
    doc = json.load(open(sys.argv[1] if len(sys.argv) > 1 else DOC))
    print(f"OK: {len(doc['termos'])} termos, {len(doc['relacoes'])} relações — "
          "canônico válido.")
