#!/usr/bin/env python3
"""Gera e valida manifestos imutáveis da Fase 0 da arquitetura Fontes/KB.

Não move, reescreve ou abre conteúdo das coleções. Para cada arquivo, mede
caminho relativo, bytes e SHA-256; o hash da coleção deriva dessa lista
ordenada. Os manifestos permitem provar que uma futura migração preservou o
conteúdo antes de qualquer troca de caminho.

Uso:
    python3 ferramentas/gerar_manifestos_acervo.py
    python3 ferramentas/gerar_manifestos_acervo.py --validar
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from caminhos_acervo import CAMINHOS_ATUAIS, DESTINOS_PLANEJADOS, RAIZ, caminho_atual

DATA_FASE_0 = "2026-10-23"
ALGORITMO = "sha256"

FONTES = (
    ("FON-LIVROS", "fonte.livros", "fonte primária", "obras e amostras de livros"),
    ("FON-RECEPCAO", "fonte.recepcao", "recepção bruta", "caixa de entrada e transcrições recebidas"),
    ("FON-EXTERNAS", "fonte.externas", "fonte externa", "materiais de apoio e fontes de terceiros"),
    ("EVD-PALESTRAS", "evidencia.palestras", "evidência derivada", "apostilas e cópias seladas de fontes"),
    ("EVD-CICLOS", "evidencia.ciclos", "evidência de processamento", "ciclos, âncoras e cópias de proveniência"),
    ("EVD-CONSOLIDACOES", "evidencia.consolidacoes", "evidência consolidada", "ciclos de consolidação e seus registros"),
)

KB = (
    ("KB-CADASTRO", "kb.base", "cadastro canônico", "exportações canônicas JSON"),
    ("KB-FICHAS", "kb.termos", "fichas terminológicas", "fichas Markdown por código RC"),
    ("KB-RAG", "kb.rag", "derivado RAG", "cards e manifestos para recuperação"),
    ("KB-REGISTRO", "kb.registro", "registro executável", "dados_termos.py, mantido em ferramentas/"),
)


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def arquivos_de(caminho: Path) -> list[Path]:
    if caminho.is_file():
        return [caminho]
    if not caminho.is_dir():
        raise FileNotFoundError(caminho)
    return sorted((p for p in caminho.rglob("*") if p.is_file()), key=lambda p: p.as_posix())


def inventariar(identificador: str, chave: str, classe: str, descricao: str) -> dict[str, Any]:
    caminho = caminho_atual(chave)
    entradas = []
    for arquivo in arquivos_de(caminho):
        relativo = arquivo.relative_to(caminho).as_posix() if caminho.is_dir() else arquivo.name
        entradas.append({
            "caminho_relativo": relativo,
            "bytes": arquivo.stat().st_size,
            "sha256": sha256_arquivo(arquivo),
        })

    serial = "".join(
        f"{item['caminho_relativo']}\0{item['bytes']}\0{item['sha256']}\n"
        for item in entradas
    ).encode("utf-8")
    destino = DESTINOS_PLANEJADOS[chave]
    return {
        "id": identificador,
        "chave": chave,
        "classe": classe,
        "descricao": descricao,
        "caminho_atual": CAMINHOS_ATUAIS[chave].as_posix(),
        "destino_planejado": destino.as_posix() if destino else None,
        "mover_nesta_fase": False,
        "arquivos": entradas,
        "total_arquivos": len(entradas),
        "total_bytes": sum(item["bytes"] for item in entradas),
        "sha256_colecao": hashlib.sha256(serial).hexdigest(),
    }


def documento(nome: str, colecoes: tuple[tuple[str, str, str, str], ...]) -> dict[str, Any]:
    return {
        "formato": "manifesto-acervo-fase-0/v1",
        "nome": nome,
        "data_referencia": DATA_FASE_0,
        "algoritmo": ALGORITMO,
        "sem_migracao_fisica": True,
        "nota": (
            "Inventário de pré-migração. Caminhos atuais são autoritativos; destinos "
            "planejados não são caminhos de runtime nem autorizam movimentação."
        ),
        "colecoes": [inventariar(*colecao) for colecao in colecoes],
    }


def saidas() -> dict[Path, dict[str, Any]]:
    return {
        RAIZ / "fontes" / "manifestos" / "MANIFESTO-FONTES-FASE-0.json": documento("fontes", FONTES),
        RAIZ / "kb" / "manifestos" / "MANIFESTO-KB-FASE-0.json": documento("kb", KB),
    }


def escrever() -> None:
    for caminho, conteudo in saidas().items():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(json.dumps(conteudo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        total = sum(c["total_arquivos"] for c in conteudo["colecoes"])
        tamanho = sum(c["total_bytes"] for c in conteudo["colecoes"])
        print(f"OK -> {caminho.relative_to(RAIZ)} ({total} arquivos; {tamanho} bytes)")


def validar() -> None:
    falhas = []
    for caminho, esperado in saidas().items():
        if not caminho.exists():
            falhas.append(f"ausente: {caminho.relative_to(RAIZ)}")
            continue
        atual = json.loads(caminho.read_text(encoding="utf-8"))
        if atual != esperado:
            falhas.append(f"divergente: {caminho.relative_to(RAIZ)}")
    if falhas:
        raise SystemExit("MANIFESTOS INVÁLIDOS:\n- " + "\n- ".join(falhas))
    print("OK — manifestos Fase 0 conferem byte a byte com todas as coleções inventariadas.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validar", action="store_true", help="recalcula e compara sem escrever")
    args = parser.parse_args()
    validar() if args.validar else escrever()


if __name__ == "__main__":
    main()
