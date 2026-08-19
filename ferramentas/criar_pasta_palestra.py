#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria a pasta padrão de uma nova palestra (estrutura canônica).

Uso:
  python3 ferramentas/criar_pasta_palestra.py YYYY-MM-DD_slug_resumido

Cria:
  apostilas/YYYY-MM-DD_slug_resumido/
    ├── ficha_ingresso.md   (modelo com cabeçalho)
    ├── original.txt        (placeholder — transcrição bruta)
    └── apostila.md         (cópia do modelo de apostila)

Valida o formato do slug (data YYYY-MM-DD + _ + slug minúsculo sem acentos).
"""
import os, re, sys, shutil

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APOSTILAS = os.path.join(RAIZ, "apostilas")

SLUG_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9_]{1,50}$")

def validar_slug(slug):
    if not SLUG_RE.match(slug):
        print("ERRO: slug inválido. Use o formato YYYY-MM-DD_slug_resumido")
        print("  - data com 4-2-2 dígitos (ex.: 2024-09-28)")
        print("  - underline, depois slug minúsculo (a-z, 0-9, _), máx 50 chars")
        print("  - ex.: 2024-09-28_setianos_emancipados")
        sys.exit(1)

def criar(slug):
    validar_slug(slug)
    pasta = os.path.join(APOSTILAS, slug)
    if os.path.exists(pasta):
        print(f"⚠️  Pasta já existe: {pasta}")
        sys.exit(0)
    os.makedirs(pasta)

    # ficha de ingresso (v2.0 simplificada — 2 campos opcionais; o resto é inferido pela IA)
    ficha = os.path.join(RAIZ, "apostilas", "00-ficha-ingresso-modelo.md")
    conteudo = open(ficha, encoding="utf-8").read()
    conteudo = conteudo.replace("`YYYY-MM-DD_slug_resumido`",
                                f"`{slug}`")
    open(os.path.join(pasta, "ficha_ingresso.md"), "w", encoding="utf-8").write(conteudo)

    # original.txt placeholder
    open(os.path.join(pasta, "original.txt"), "w", encoding="utf-8").write(
        f"# TRANSCRIÇÃO BRUTA — {slug}\n\n"
        "> Substitua este arquivo pela transcrição original da palestra (sem edição).\n"
        "> Este é o texto-fonte; NUNCA editar aqui — a edição acontece em apostila.md.\n"
    )

    # apostila.md (cópia do modelo)
    modelo = os.path.join(RAIZ, "apostilas", "00-modelo-apostila.md")
    if os.path.exists(modelo):
        shutil.copy(modelo, os.path.join(pasta, "apostila.md"))

    print(f"✅ Pasta criada: apostilas/{slug}/")
    print("   ├── ficha_ingresso.md")
    print("   ├── original.txt   (substituir pela transcrição)")
    print("   └── apostila.md    (editar → build_apostila.py → DOCX)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 ferramentas/criar_pasta_palestra.py YYYY-MM-DD_slug")
        sys.exit(1)
    criar(sys.argv[1])
