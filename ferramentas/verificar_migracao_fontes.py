#!/usr/bin/env python3
"""Verifica uma coleção de fontes contra o manifesto imutável da Fase 0.

Uso:
    python3 ferramentas/verificar_migracao_fontes.py --colecao FON-LIVROS
    python3 ferramentas/verificar_migracao_fontes.py --colecao FON-LIVROS \
        --averbacao fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1B.json
    python3 ferramentas/verificar_migracao_fontes.py --piloto externas

Compara cada caminho relativo, byte e SHA-256 da rota atual declarada em
``caminhos_acervo.py`` com a coleção correspondente no manifesto de
pré-migração. Uma averbação opcional é uma lista explícita e verificável de
deltas posteriores à Fase 0; ela não altera o manifesto original. Não escreve
arquivos. ``--piloto`` é mantido como atalho compatível para pilotos já
publicados.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from caminhos_acervo import RAIZ, caminho_atual

MANIFESTO = RAIZ / "fontes" / "manifestos" / "MANIFESTO-FONTES-FASE-0.json"
PILOTOS = {"externas": "FON-EXTERNAS"}


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def hash_agregado(arquivos: list[dict]) -> str:
    serial = "".join(
        f"{item['caminho_relativo']}\0{item['bytes']}\0{item['sha256']}\n" for item in arquivos
    ).encode("utf-8")
    return hashlib.sha256(serial).hexdigest()


def carregar_colecao(identificador: str) -> dict:
    doc = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    for colecao in doc["colecoes"]:
        if colecao["id"] == identificador:
            return colecao
    conhecidos = ", ".join(c["id"] for c in doc["colecoes"])
    raise SystemExit(f"coleção desconhecida: {identificador} (conhecidas: {conhecidos})")


def aplicar_averbacao(arquivos_base: list[dict], identificador: str, arquivo: Path) -> tuple[list[dict], int]:
    """Aplica um delta encadeado sem reescrever o manifesto de referência."""
    try:
        doc = json.loads(arquivo.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"averbação ausente: {arquivo}") from None
    if doc.get("colecao") != identificador:
        raise SystemExit(f"averbação de {doc.get('colecao')!r} não pode ser aplicada a {identificador}.")
    arquivos = [dict(item) for item in arquivos_base]
    por_caminho = {item["caminho_relativo"]: item for item in arquivos}
    alteracoes = doc.get("alteracoes", [])
    if not alteracoes:
        raise SystemExit("averbação sem alterações declaradas.")
    for delta in alteracoes:
        caminho = delta.get("caminho_relativo")
        anterior = delta.get("fase_0", delta.get("anterior"))
        atual = delta.get("pre_migracao", delta.get("pos_migracao"))
        item = por_caminho.get(caminho)
        if not item or {"bytes": item["bytes"], "sha256": item["sha256"]} != anterior:
            raise SystemExit(f"averbação inválida para {caminho}: não coincide com a Fase 0.")
        if not isinstance(atual, dict) or set(atual) != {"bytes", "sha256"}:
            raise SystemExit(f"averbação inválida para {caminho}: destino incompleto.")
        item.update(atual)
    arquivos.sort(key=lambda item: item["caminho_relativo"])
    agregado = hash_agregado(arquivos)
    declarado = doc.get("sha256_colecao_resultante", doc.get("sha256_colecao_pre_migracao"))
    if agregado != declarado:
        raise SystemExit("averbação inválida: hash agregado declarado não confere.")
    return arquivos, len(alteracoes)


def diagnostico_divergencia(atual: list[dict], esperado: list[dict]) -> str:
    atual_por_caminho = {item["caminho_relativo"]: item for item in atual}
    esperado_por_caminho = {item["caminho_relativo"]: item for item in esperado}
    ausentes = sorted(esperado_por_caminho.keys() - atual_por_caminho.keys())
    extras = sorted(atual_por_caminho.keys() - esperado_por_caminho.keys())
    alterados = sorted(caminho for caminho in atual_por_caminho.keys() & esperado_por_caminho.keys()
                       if atual_por_caminho[caminho] != esperado_por_caminho[caminho])
    partes = []
    for rotulo, itens in (("ausente(s)", ausentes), ("extra(s)", extras), ("alterado(s)", alterados)):
        if itens:
            amostra = ", ".join(itens[:5])
            partes.append(f"{len(itens)} {rotulo}: {amostra}{' …' if len(itens) > 5 else ''}")
    return "; ".join(partes) or "divergência não classificada"


def verificar(identificador: str, averbacoes_paths: list[Path] | None = None) -> None:
    colecao = carregar_colecao(identificador)
    esperado = colecao["arquivos"]
    averbacoes = 0
    for averbacao in averbacoes_paths or []:
        esperado, quantidade = aplicar_averbacao(esperado, identificador, averbacao)
        averbacoes += quantidade
    if colecao.get("modo_verificacao") == "distribuida_por_arquivo":
        # Uma coleção R3 pode ocupar rotas canônicas distintas. Neste modo, os
        # caminhos do manifesto são relativos à raiz e cada item é verificado
        # diretamente, sem tratar diretórios administrativos compartilhados como
        # se fossem exclusivos da coleção.
        atual = []
        for esperado_item in colecao["arquivos"]:
            arquivo = RAIZ / esperado_item["caminho_relativo"]
            if arquivo.is_file():
                atual.append({
                    "caminho_relativo": esperado_item["caminho_relativo"],
                    "bytes": arquivo.stat().st_size,
                    "sha256": sha256_arquivo(arquivo),
                })
        atual.sort(key=lambda item: item["caminho_relativo"])
    else:
        destino = caminho_atual(colecao["chave"])
        if not destino.is_dir():
            raise SystemExit(f"rota atual ausente: {destino.relative_to(RAIZ)}")
        atual = [{
            "caminho_relativo": arquivo.relative_to(destino).as_posix(),
            "bytes": arquivo.stat().st_size,
            "sha256": sha256_arquivo(arquivo),
        } for arquivo in sorted((p for p in destino.rglob("*") if p.is_file()), key=lambda p: p.as_posix())]
    if atual != esperado:
        raise SystemExit(
            f"INTEGRIDADE INVÁLIDA: {identificador} diverge do manifesto Fase 0 "
            f"({len(atual)} arquivo(s) na rota atual; esperado {len(esperado)}; "
            f"{diagnostico_divergencia(atual, esperado)})."
        )
    agregado = hash_agregado(atual)
    agregado_esperado = hash_agregado(esperado) if averbacoes_paths else colecao["sha256_colecao"]
    if agregado != agregado_esperado:
        raise SystemExit("INTEGRIDADE INVÁLIDA: hash agregado da coleção diverge.")
    qualificacao = f"; {averbacoes} averbação(ões) aplicada(s)" if averbacoes else ""
    print(f"OK — {identificador}: {len(atual)} arquivo(s), {sum(x['bytes'] for x in atual)} bytes, "
          f"SHA-256 agregado preservado ({agregado}){qualificacao}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--colecao", metavar="ID", help="ID estável do manifesto, como FON-LIVROS")
    grupo.add_argument("--piloto", choices=sorted(PILOTOS), help="atalho compatível para piloto publicado")
    parser.add_argument("--averbacao", action="append", default=[], type=Path,
                        help="delta a aplicar; repita em ordem para uma cadeia de averbações")
    args = parser.parse_args()
    verificar(args.colecao or PILOTOS[args.piloto], args.averbacao)


if __name__ == "__main__":
    main()
