#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# STATUS: SOB-DEMANDA (era migração-de-chats)
"""
Restaurador dos pacotes de garantia RC (2026-08-16) — v3 (binário, fiel).

Regra documentada no próprio pacote:
    ===ARQ: <caminho>===
    [conteúdo literal]
    ===FIM-ARQ: <caminho>===

v3 corrige dois bugs descobertos em auditoria:
  1. Os pacotes perderam a nova linha final ("\n") de cada arquivo na geração;
     o manifesto (bytes | SHA-256) refere-se aos arquivos ORIGINAIS.
     Correção: se manifest.bytes == len(embutido)+1, repor "\n" e conferir hash.
  2. A leitura em modo texto aplicava universal newlines e corrompia arquivos
     com CRLF interno (caso: original.txt da P2024-11-02). Por isso a leitura
     é feita em MODO BINÁRIO, sem nenhuma tradução de quebra de linha.

FONTE ÚNICA DE VERDADE: ferramentas/dados_termos.py.
"""
import hashlib
import os
import re
import sys

RAIZ = "/home/user/rc-terminologia"
# Apontam para o checkpoint mais recente (2026-08-18). Pacotes mais antigos
# permanecem em /home/user/uploads/ (16/08). Uso:
#   python3 ferramentas/restaurar_pacotes.py                     -> pacotes padrão
#   python3 ferramentas/restaurar_pacotes.py ARQ1 ARQ2 ...       -> pacotes explícitos
PACOTES = [
    os.path.join(RAIZ, "reconstrucao", "pacotes", "PACOTE-DE-REGENERACAO-2026-08-18.txt"),
    os.path.join(RAIZ, "reconstrucao", "pacotes", "PACOTE-DE-FICHAS-2026-08-18.txt"),
    os.path.join(RAIZ, "reconstrucao", "pacotes", "PACOTE-DE-APOSTILAS-2026-08-18.txt"),
    os.path.join(RAIZ, "reconstrucao", "pacotes", "PACOTE-DE-ORIGINAIS-2026-08-18.txt"),
]

# Marcadores em bytes (o caminho pode conter "="; usar [^=\n]+ é suficiente na prática)
ARQ_RE = re.compile(rb"^===ARQ:\s*(.+?)\s*===\s*$", re.M)


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def parse_pacote_bin(caminho):
    """Extrai {caminho: bytes} diretamente dos bytes do pacote, sem traduções."""
    with open(caminho, "rb") as f:
        dados = f.read()

    arqs = [(m.start(), m.group(1).strip()) for m in ARQ_RE.finditer(dados)]

    arquivos = {}
    for pos, nome_b in arqs:
        nome_s = nome_b.decode("utf-8")
        # Busca binária direta do FIM-ARQ: funciona também quando o conteúdo
        # anterior não termina em "\n" (marcador no meio da linha — gerador
        # fiel, correção 2026-08-18).
        marc_fim = b"===FIM-ARQ: " + nome_b + b"==="
        fim = dados.find(marc_fim, pos)
        if fim == -1:
            raise SystemExit(f"ERRO: ===FIM-ARQ: {nome_s} não encontrado em {caminho}")
        if fim <= pos:
            raise SystemExit(f"ERRO: FIM-ARQ de {nome_s} antes do ARQ em {caminho}")
        # o conteúdo começa após o "===\n" que encerra a linha do marcador ARQ
        fim_marcador = dados.find(b"===\n", pos)
        if fim_marcador == -1 or fim_marcador >= fim:
            raise SystemExit(f"ERRO: marcador ARQ malformado para {nome_s} em {caminho}")
        inicio_conteudo = fim_marcador + 4
        arquivos[nome_s] = dados[inicio_conteudo:fim]
    return arquivos


def manifestos_embutidos(caminho):
    """Extrai o bloco '# MANIFESTO (...)' -> {path: (bytes, sha)}."""
    with open(caminho, "r", encoding="utf-8") as f:
        txt = f.read()
    result = {}
    for bloco in re.findall(r"^# MANIFESTO[^\n]*\n((?:^# .*\n)+)", txt, re.M):
        for linha in bloco.split("\n"):
            linha = linha.strip()
            if not linha.startswith("# "):
                continue
            partes = [p.strip() for p in linha[2:].split("|")]
            if len(partes) >= 4 and partes[1].isdigit():
                result[partes[0]] = (int(partes[1]), partes[3])
    return result


def main():
    pacotes = PACOTES
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        pacotes = sys.argv[1:]
    restaurados = {}
    ok_identico = 0
    ok_nova_linha = 0
    problema = []

    for pacote in pacotes:
        nome = os.path.basename(pacote)
        print(f"==> Restaurando {nome} ...")
        arquivos = parse_pacote_bin(pacote)
        manifest = manifestos_embutidos(pacote)
        print(f"    {len(arquivos)} arquivos | {len(manifest)} entradas de manifesto")

        for caminho, bytes_ in arquivos.items():
            destino = os.path.join(RAIZ, caminho)
            os.makedirs(os.path.dirname(destino), exist_ok=True)

            esperado_bytes, esperado_sha = manifest.get(caminho, (None, None))

            final = bytes_
            if esperado_bytes is not None:
                if len(bytes_) == esperado_bytes:
                    ok_identico += 1
                elif len(bytes_) == esperado_bytes - 1:
                    final = bytes_ + b"\n"
                    ok_nova_linha += 1
                else:
                    problema.append((caminho, f"bytes embutidos {len(bytes_)} != manifesto {esperado_bytes}"))
            else:
                problema.append((caminho, "sem entrada no manifesto"))

            with open(destino, "wb") as f:
                f.write(final)
            restaurados[caminho] = final

            if esperado_sha is not None and sha256(final) != esperado_sha:
                problema.append((caminho, f"SHA divergente: {sha256(final)[:12]} != {esperado_sha[:12]}"))

    print()
    print(f"TOTAL restaurados: {len(restaurados)}")
    print(f"  - idênticos ao manifesto:      {ok_identico}")
    print(f"  - com \\n final reposto:        {ok_nova_linha}")
    if problema:
        print(f"PROBLEMAS ({len(problema)}):")
        for p in problema:
            print("  -", p)
    else:
        print("Todos os arquivos conferem SHA-256 com o manifesto. ✔")

    for prefixo in ("ferramentas/", "termos/", "apostilas/", "outros"):
        if prefixo == "outros":
            sel = [p for p in restaurados if not p.startswith(("ferramentas/", "termos/", "apostilas/"))]
        else:
            sel = [p for p in restaurados if p.startswith(prefixo)]
        print(f"  {prefixo}: {len(sel)}")


if __name__ == "__main__":
    main()
