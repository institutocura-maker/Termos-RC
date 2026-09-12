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

Hierarquia das relações (Onda 1.4): TERMOS[t][6] = NAVEGAÇÃO ampla
("ver também", não-tipado); RELACOES = CURATORIAL tipado (tipo + fonte).
Regra: todo par RELACOES existe em t[6] (reconciliado 12/09/2026); o inverso
não vale (4.662 navegações x 1.723 pares tipados únicos).

Tipos de RELACOES = RÓTULO LIVRE controlado por censo (despacho Onda 1.4:
fundir só flexões óbvias [Grupo A], manter pares de preposição com sentido próprio,
dedup de espelhos; ver diagnostico/CENSO-TIPOS-RELACAO-2026-09-12.md e certidão em
diagnostico/DESPACHO-FUSAO-TIPOS-1.4-2026-09-12.md). Vocabulário fechado = Onda 2+.
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


# ------------------------------------------------- Onda 1.5 — regra interim (Opção A)
# `via` e `confianca_fonte` são DERIVADAS (não vivem na tupla do registro):
#   via: status `em análise` -> P7-conhecimento (os 166 da linha de auditoria);
#        demais status -> P6-evidência.
#   confianca_fonte: alta = verificado COM >=1 fonte de livro (B###);
#        baixa = candidato ou em análise; média = demais.
# Reversível: mudar a regra aqui regenera o canônico (exportar_json).
def via_de(t):
    return "P7-conhecimento" if t[4] == "em análise" else "P6-evidência"


def confianca_de(t):
    tem_livro = any(str(f).startswith("B") for f in t[5])
    if t[4] == "verificado" and tem_livro:
        return "alta"
    if t[4] in ("candidato", "em análise"):
        return "baixa"
    return "média"


def _biblio_do_json():
    import json
    doc = json.load(open(os.path.join(RAIZ := os.path.dirname(FER),
                                      "base", "biblio.json"), encoding="utf-8"))
    return [[o["codigo"], o["titulo"], o["subtitulo"], o["editora"],
             o["ano"], o["status"], o["nota"]] for o in doc["obras"]]


def carregar_canonico():
    """Onda 1.7 (JSON-primeiro, despacho 1.2 Opção A): TERMOS/RELACOES lidos
    de base/canonico.json. Reconstrói as tuplas no formato do registro
    (relacionados voltam a string "; ") para que os builders troquem de fonte
    sem tocar na lógica. O PRODUTOR do JSON segue sendo exportar_json.py
    (registro-mestre -> json); `validar` continua a porta dos dados.
    Aceite de paridade por builder: espelhos byte-idênticos (exceto a placa
    de procedência, quando houver)."""
    import json
    raiz = os.path.dirname(FER)
    doc = json.load(open(os.path.join(raiz, "base", "canonico.json"),
                         encoding="utf-8"))
    termos = [(t["codigo"], t["nome"], t["categoria"], t["subcategoria"],
               t["status"], list(t["fontes"]), "; ".join(t["relacionados"]),
               t["ficha"]) for t in doc["termos"]]
    rels = [(r["a"], r["tipo"], r["b"], r["fonte"]) for r in doc["relacoes"]]
    return termos, rels


BIBLIO = _biblio_do_json()
