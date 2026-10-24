#!/usr/bin/env python3
"""Mapa único dos caminhos físicos e destinos planejados do acervo.

A Fase 0 registra a linha de base sem mover dados. Após aprovação curatorial,
este mapa é a única fonte para a rota atual de cada coleção já migrada.
Destinos planejados não são consumidos por scripts; uma migração só ocorre
após manifestos, portões e autorização próprios.
"""
from __future__ import annotations

from pathlib import Path
from types import MappingProxyType

RAIZ = Path(__file__).resolve().parent.parent

# Chaves estáveis de arquitetura. Os caminhos atuais são a verdade de runtime
# durante a Fase 0; destinos planejados não devem ser consumidos por scripts.
CAMINHOS_ATUAIS = MappingProxyType({
    "fonte.livros": Path("fontes") / "livros",
    # Caixa de entrada futura: após R3, conserva apenas seu contrato/estrutura.
    "fonte.recepcao": Path("uploads_recepcao"),
    # Destinos canônicos e imutáveis da reconfiguração curatorial R3.
    "evidencia.recepcao.logs": Path("admin") / "logs",
    "evidencia.recepcao.documentos": Path("admin") / "documentos",
    "fonte.recepcao.docx_originais": Path("fontes") / "docx_originais",
    "fonte.recepcao.pilotos_historicos": Path("fontes") / "pilotos_historicos",
    "fonte.recepcao.stt_lote_2026_10": Path("fontes") / "stt-lote-2026-10",
    "fonte.externas": Path("fontes") / "externas",
    "evidencia.palestras": Path("apostilas"),
    "evidencia.ciclos": Path("ciclos"),
    "evidencia.consolidacoes": Path("consolidacoes"),
    "kb.base": Path("base"),
    "kb.termos": Path("termos"),
    "kb.rag": Path("rag"),
    "kb.registro": Path("ferramentas") / "dados_termos.py",
})

DESTINOS_PLANEJADOS = MappingProxyType({
    "fonte.livros": Path("fontes") / "livros",
    # A rota de recepção fica como caixa de entrada; os destinos R3 acima já são atuais.
    "fonte.recepcao": Path("fontes") / "recepcao",
    "evidencia.recepcao.logs": None,
    "evidencia.recepcao.documentos": None,
    "fonte.recepcao.docx_originais": None,
    "fonte.recepcao.pilotos_historicos": None,
    "fonte.recepcao.stt_lote_2026_10": None,
    "fonte.externas": None,
    "evidencia.palestras": None,
    "evidencia.ciclos": None,
    "evidencia.consolidacoes": None,
    "kb.base": Path("kb") / "base",
    "kb.termos": Path("kb") / "termos",
    "kb.rag": Path("kb") / "rag",
    # dados_termos.py é parte executável do Motor, não arquivo a ser realocado
    # com os dados nesta arquitetura inicial.
    "kb.registro": None,
})


def caminho_atual(chave: str, raiz: Path | None = None) -> Path:
    """Devolve o caminho físico atual de uma camada conhecida."""
    try:
        relativo = CAMINHOS_ATUAIS[chave]
    except KeyError as exc:
        raise KeyError(f"camada de acervo desconhecida: {chave}") from exc
    return (raiz or RAIZ) / relativo


def destino_planejado(chave: str, raiz: Path | None = None) -> Path | None:
    """Devolve o destino futuro, sem implicar autorização para migrar."""
    try:
        relativo = DESTINOS_PLANEJADOS[chave]
    except KeyError as exc:
        raise KeyError(f"camada de acervo desconhecida: {chave}") from exc
    return None if relativo is None else (raiz or RAIZ) / relativo
