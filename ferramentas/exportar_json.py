#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (exportador canônico; Onda 1.1)
"""Exporta dados_termos.py -> base/canonico.json — Onda 1.1.

Normaliza tipos (C7): fontes=lista (já era), relacionados=string-`;` -> lista.
Round-trip HONESTO (ver nota): semântico, não textual — regenerar o .py
byte-idêntico é inviável (constantes SER_DIV[0], aspas mistas, comentários).
Aceite = estruturas importadas iguais (testado em __main__).
"""
import json
import os
import sys

FER = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(FER)
sys.path.insert(0, FER)
from loader import TERMOS, RELACOES, via_de, confianca_de  # noqa: E402

OUT = os.path.join(RAIZ, "base", "canonico.json")


def split_rel(s):
    return [r.strip() for r in (s or "").split(";")
            if r.strip() and r.strip() != "—"]


def exportar(out=OUT):
    VIA = {t[0]: via_de(t) for t in TERMOS}
    CONF = {t[0]: confianca_de(t) for t in TERMOS}
    doc = {
        "meta": {"formato": "canonico-1.1",
                 "gerado_de": "ferramentas/dados_termos.py",
                 "nota": "Verdade-mestra (despacho 1.2, Opção A); via/confianca_fonte =\n                  regra interim 1.5 (loader.py)."},
        "termos": [
            {"codigo": c, "nome": n, "categoria": cat, "subcategoria": sub,
             "status": st, "fontes": list(f), "relacionados": split_rel(r),
             "ficha": bool(fc), "via": VIA[c], "confianca_fonte": CONF[c]}
            for c, n, cat, sub, st, f, r, fc in TERMOS],
        "relacoes": [
            {"a": a, "tipo": t, "b": b, "fonte": f}
            for a, t, b, f in RELACOES],
    }
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write("\n")
    return out, doc


def roundtrip_check(doc):
    """Igualdade semântica json x importado. Retorna lista de falhas."""
    falhas = []
    if len(doc["termos"]) != len(TERMOS):
        falhas.append(f"n termos: {len(doc['termos'])} x {len(TERMOS)}")
    jt = {t["codigo"]: t for t in doc["termos"]}
    for c, n, cat, sub, st, f, r, fc in TERMOS:
        j = jt.get(c)
        if not j:
            falhas.append(f"{c}: ausente no json")
            continue
        if (j["nome"], j["categoria"], j["subcategoria"], j["status"],
                j["fontes"], j["relacionados"], j["ficha"]) != (
                n, cat, sub, st, list(f), split_rel(r), bool(fc)):
            falhas.append(f"{c}: divergência de conteúdo")
    jr = [(x["a"], x["tipo"], x["b"], x["fonte"]) for x in doc["relacoes"]]
    if jr != [tuple(x) for x in RELACOES]:
        falhas.append("RELACOES: divergência (ordem/conteúdo)")
    return falhas


if __name__ == "__main__":
    out, doc = exportar()
    falhas = roundtrip_check(doc)
    assert not falhas, falhas[:5]
    print(f"OK -> {out} ({len(doc['termos'])} termos, "
          f"{len(doc['relacoes'])} relações, round-trip semântico limpo)")
