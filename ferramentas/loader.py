#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: ATIVO-P7 (loader único; Onda 0.2)
"""LOADER ÚNICO DA BASE RC — Onda 0.2.

Um módulo, uma API, três consumidores (build_xlsx, build_word, build_indice,
verificar_verbetes, test_suite). Aposenta:
  - exec() de dados_termos.py (build_word::carregar_py)
  - ast-scraping de build_xlsx.py p/ BIBLIO (build_word::carregar_literal)

INTERIM (até Onda 1.3): BIBLIO continua morando no código de build_xlsx.py;
a extração via AST vive aqui, num SÓ lugar, documentada. Quando a Onda 1.3
mover BIBLIO para os dados canônicos, só este arquivo muda.
"""
import os
import sys

FER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FER)

import dados_termos as _d  # noqa: E402

TERMOS = _d.TERMOS
RELACOES = _d.RELACOES


def validar():
    return _d.validar()


def _biblio_do_json():
    import json
    doc = json.load(open(os.path.join(RAIZ := os.path.dirname(FER),
                                      "base", "biblio.json"), encoding="utf-8"))
    return [[o["codigo"], o["titulo"], o["subtitulo"], o["editora"],
             o["ano"], o["status"], o["nota"]] for o in doc["obras"]]


BIBLIO = _biblio_do_json()
