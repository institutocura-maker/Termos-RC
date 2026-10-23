#!/usr/bin/env python3
"""Verifica uma migração física de fonte contra o manifesto imutável da Fase 0.

Uso:
    python3 ferramentas/verificar_migracao_fontes.py --piloto externas

Compara cada caminho relativo, byte e SHA-256 do destino atual com FON-EXTERNAS
no manifesto de pré-migração. Não escreve arquivos.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from caminhos_acervo import RAIZ, caminho_atual

MANIFESTO = RAIZ / "fontes" / "manifestos" / "MANIFESTO-FONTES-FASE-0.json"
PILOTOS = {"externas": ("FON-EXTERNAS", "fonte.externas")}


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--piloto", choices=sorted(PILOTOS), required=True)
    args = parser.parse_args()

    identificador, chave = PILOTOS[args.piloto]
    doc = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    esperado = next(c for c in doc["colecoes"] if c["id"] == identificador)
    destino = caminho_atual(chave)
    if not destino.is_dir():
        raise SystemExit(f"destino ausente: {destino.relative_to(RAIZ)}")

    atual = []
    for arquivo in sorted((p for p in destino.rglob("*") if p.is_file()), key=lambda p: p.as_posix()):
        atual.append({
            "caminho_relativo": arquivo.relative_to(destino).as_posix(),
            "bytes": arquivo.stat().st_size,
            "sha256": sha256_arquivo(arquivo),
        })
    if atual != esperado["arquivos"]:
        raise SystemExit(
            f"MIGRAÇÃO INVÁLIDA: {identificador} diverge do manifesto Fase 0 "
            f"({len(atual)} arquivo(s) no destino; esperado {esperado['total_arquivos']})."
        )
    serial = "".join(
        f"{item['caminho_relativo']}\0{item['bytes']}\0{item['sha256']}\n" for item in atual
    ).encode("utf-8")
    agregado = hashlib.sha256(serial).hexdigest()
    if agregado != esperado["sha256_colecao"]:
        raise SystemExit("MIGRAÇÃO INVÁLIDA: hash agregado da coleção diverge.")
    print(
        f"OK — {identificador}: {len(atual)} arquivo(s), {sum(x['bytes'] for x in atual)} bytes, "
        f"SHA-256 agregado preservado ({agregado})."
    )


if __name__ == "__main__":
    main()
