#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador de FIDELIDADE dos pacotes de garantia RC (2026-08-23).

Checagem NÃO-DESTRUTIVA (diferente de restaurar_pacotes.py, que grava no
workspace): para cada pacote, extrai os bytes embutidos de cada
===ARQ: <caminho>=== ... ===FIM-ARQ: <caminho>=== e compara:
  (A) bytes embutidos  ×  bytes/SHA-256 declarados no MANIFESTO do cabeçalho;
  (B) bytes embutidos  ×  bytes do arquivo no disco (byte a byte).

O formato do corpo do pacote (gerador fiel) é:
    ===ARQ: <caminho>===\n + <dados byte a byte> + ===FIM-ARQ: <caminho>===\n
logo a extração entre o "\\n" do marcador ARQ e o FIM-ARQ recupera os dados
exatos (se o arquivo termina em "\\n", esse "\\n" faz parte dos dados).

Resultado esperado: "OK: N/N arquivos fiéis" em todos os pacotes.

Uso:
    python3 ferramentas/verificar_pacotes.py [PACOTE1 PACOTE2 ...]
    (padrão: os 4 pacotes de reconstrucao/pacotes/)
"""
import hashlib
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACOTES_PADRAO = [
    os.path.join(RAIZ, "reconstrucao", "pacotes", f)
    for f in (
        "PACOTE-DE-REGENERACAO-2026-08-18.txt",
        "PACOTE-DE-FICHAS-2026-08-18.txt",
        "PACOTE-DE-APOSTILAS-2026-08-18.txt",
        "PACOTE-DE-ORIGINAIS-2026-08-18.txt",
    )
]
ARQ_RE = re.compile(rb"^===ARQ:\s*(.+?)\s*===\s*$", re.M)
MANI_RE = re.compile(rb"^# (\S.*?) \| (\d+) \| (\d+) \| ([0-9a-f]{64})\s*$", re.M)


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def manifestos_de(caminho_pacote: str) -> dict:
    """{relpath: (bytes, linhas, sha)} do MANIFESTO no cabeçalho do pacote."""
    with open(caminho_pacote, "rb") as f:
        dados = f.read()
    # o cabeçalho da doc menciona "===ARQ:" — usar o primeiro marcador REAL
    m1 = ARQ_RE.search(dados)
    cab = dados[: m1.start()]
    mani = {}
    for m in MANI_RE.finditer(cab):
        mani[m.group(1).decode("utf-8")] = (
            int(m.group(2)),
            int(m.group(3)),
            m.group(4).decode("ascii"),
        )
    return mani


def principal():
    pacotes = sys.argv[1:] or PACOTES_PADRAO
    total_ok = total_n = 0
    exit_code = 0
    for pacote in pacotes:
        if not os.path.isfile(pacote):
            print(f"!! AUSENTE: {pacote}")
            exit_code = 1
            continue
        with open(pacote, "rb") as f:
            dados = f.read()
        mani = manifestos_de(pacote)
        arqs = [(m.start(), m.group(1).strip()) for m in ARQ_RE.finditer(dados)]
        ok = 0
        erros = []
        for pos, nome_b in arqs:
            nome = nome_b.decode("utf-8")
            marc_fim = b"===FIM-ARQ: " + nome_b + b"==="
            idx_fim = dados.find(marc_fim, pos)
            if idx_fim < 0:
                erros.append(f"FIM-ARQ ausente: {nome}")
                continue
            inicio = dados.find(b"\n", pos) + 1  # após a quebra do marcador ARQ
            embutido = dados[inicio:idx_fim]
            # (A) x MANIFESTO
            if nome not in mani:
                erros.append(f"ausente do MANIFESTO: {nome}")
                continue
            nb, nl, nsha = mani[nome]
            if len(embutido) != nb or sha256(embutido) != nsha:
                erros.append(f"BYTES/SHA != manifesto: {nome} ({len(embutido)} vs {nb})")
                continue
            # (B) x DISCO
            disco = os.path.join(RAIZ, nome)
            if not os.path.isfile(disco):
                erros.append(f"AUSENTE NO DISCO: {nome}")
                continue
            with open(disco, "rb") as f:
                no_disco = f.read()
            if no_disco != embutido:
                erros.append(f"DIFERE DO DISCO: {nome}")
                continue
            ok += 1
        total_ok += ok
        total_n += len(arqs)
        status = "OK" if not erros else "FALHOU"
        print(f"{status} -> {os.path.basename(pacote)}: {ok}/{len(arqs)} arquivos fiéis (manifesto + disco)")
        for e in erros[:10]:
            print(f"   !! {e}")
        if erros:
            exit_code = 1
    print(f"\nTOTAL: {total_ok}/{total_n} arquivos fiéis em {len(pacotes)} pacotes.")
    return exit_code


if __name__ == "__main__":
    sys.exit(principal())
