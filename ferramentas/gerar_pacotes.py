#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PACOTES DE RECONSTRUÇÃO/MIGRAÇÃO — Base Terminológica RC.

Gera arquivos TXT anexáveis (a plataforma aceita TXT, não ZIP/MD) no formato:
    ===ARQ: <caminho>===
    [conteúdo literal, byte a byte]
    ===FIM-ARQ: <caminho>===

Cada pacote embute um MANIFESTO (caminho | bytes | linhas | SHA-256) no cabeçalho.
O restaurador correspondente é `ferramentas/restaurar_pacotes.py` (v3, binário).

Uso:
    python3 ferramentas/gerar_pacotes.py [--pasta SAIDA]

Saída padrão: reconstrucao/pacotes/
"""
import hashlib
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA_PADRAO = os.path.join(RAIZ, "reconstrucao", "pacotes")

# Estado canônico COMPUTADO DINAMICAMENTE a partir da fonte única de verdade
# (correção 2026-08-18: o manifesto externo usava contagens fixas e ficava
# desatualizado conforme a Base crescia — ex.: 757 fixo quando a Base já
# tinha 765 termos).
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
try:
    from dados_termos import TERMOS, RELACOES
except ImportError:
    TERMOS, RELACOES = [], []

# ---------------------------------------------------------------- grupos de arquivos
GRUPO_REGENERACAO = [
    "ferramentas/dados_termos.py",
    "ferramentas/build_indice.py",
    "ferramentas/build_xlsx.py",
    "ferramentas/build_word.py",
    "ferramentas/build_apostila.py",
    "ferramentas/criar_pasta_palestra.py",
    "ferramentas/restaurar_pacotes.py",
    "ferramentas/gerar_pacotes.py",
    "README.md",
    "CONTINUIDADE.md",
    "convencoes-editoriais-rc.md",
    "01-ficha-modelo.md",
    "02-vocabulario-controlado.md",
    "GUIA-MESTRE-RC-APOSTILA.txt",
    "apostilas/INDICE-PALESTRAS.md",
    "apostilas/INDICE-CURADOR-2026-08-17.txt",
]

GRUPO_FICHAS = [
    os.path.join("termos", f)
    for f in sorted(os.listdir(os.path.join(RAIZ, "termos")))
    if f.endswith(".md")
]

GRUPO_APOSTILAS = []
GRUPO_ORIGINAIS = []
for slug in sorted(os.listdir(os.path.join(RAIZ, "apostilas", "CONCLUIDAS"))):
    base = os.path.join("apostilas", "CONCLUIDAS", slug)
    if os.path.isfile(os.path.join(RAIZ, base, "apostila.md")):
        GRUPO_APOSTILAS.append(os.path.join(base, "apostila.md"))
    if os.path.isfile(os.path.join(RAIZ, base, "ficha_ingresso.md")):
        GRUPO_APOSTILAS.append(os.path.join(base, "ficha_ingresso.md"))
    if os.path.isfile(os.path.join(RAIZ, base, "original.txt")):
        GRUPO_ORIGINAIS.append(os.path.join(base, "original.txt"))
# Apostilas temáticas (pedagogia / Super-Nó Semântico) — também regeneráveis
for f in sorted(os.listdir(os.path.join(RAIZ, "pedagogico"))):
    if f.startswith("Apostila-Estudo-") and f.endswith(".md"):
        GRUPO_APOSTILAS.append(os.path.join("pedagogico", f))

PACOTES = [
    ("PACOTE-DE-REGENERACAO-2026-08-18.txt", GRUPO_REGENERACAO, "núcleo canônico + builders + documentação"),
    ("PACOTE-DE-FICHAS-2026-08-18.txt", GRUPO_FICHAS, "fichas detalhadas (termos/)"),
    ("PACOTE-DE-APOSTILAS-2026-08-18.txt", GRUPO_APOSTILAS, "apostila.md + ficha_ingresso.md (regenera DOCX)"),
    ("PACOTE-DE-ORIGINAIS-2026-08-18.txt", GRUPO_ORIGINAIS, "original.txt das apostilas concluídas (fonte primária)"),
]


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def linhas_de(b: bytes) -> int:
    return b.count(b"\n") + (0 if b.endswith(b"\n") else 1)


def gerar_pacote(nome, arquivos, descricao, saida):
    cabecalho = [
        f"# PACOTE — BASE TERMINOLÓGICA RC (Jan Val Ellam)",
        f"# Gerado em 2026-08-18 · {descricao}",
        f"#",
        f"# COMO USAR: reconstruir cada arquivo no caminho exato indicado por",
        f"# ===ARQ: <caminho>===, copiando literalmente até",
        f"# ===FIM-ARQ: <caminho>===. Conteúdos em UTF-8 (byte a byte).",
        f"#",
        f"# FONTE ÚNICA DE VERDADE: ferramentas/dados_termos.py.",
        f"#",
        f"# MANIFESTO (caminho | bytes | linhas | SHA-256):",
    ]
    corpo = []
    total_bytes = 0
    total_arquivos = 0
    for rel in arquivos:
        caminho = os.path.join(RAIZ, rel)
        if not os.path.isfile(caminho):
            print(f"  !! AUSENTE: {rel}")
            continue
        with open(caminho, "rb") as f:
            dados = f.read()
        total_bytes += len(dados)
        total_arquivos += 1
        cabecalho.append(f"# {rel} | {len(dados)} | {linhas_de(dados)} | {sha256(dados)}")
        # FIDELIDADE byte a byte (correção 2026-08-18): o corpo é CONCATENADO
        # sem join, para que o conteúdo fique literalmente entre o "===\n" do
        # marcador ARQ e o marcador FIM-ARQ — o restaurador extrai exatamente
        # esses bytes. Um join aqui injetaria um "\n" extra quando o arquivo
        # termina sem quebra de linha (ex.: original.txt do podcast irmãos
        # Dias, sem "\n" final), e um "\n" extra também com CRLF misto.
        conteudo = dados.decode("utf-8", errors="replace")
        corpo.append(f"===ARQ: {rel}===\n")
        corpo.append(conteudo)
        corpo.append(f"===FIM-ARQ: {rel}===\n")

    cabecalho.append(f"#")
    cabecalho.append(f"# TOTAL: {total_arquivos} arquivos; {total_bytes} bytes de conteúdo embutido.")
    texto = "\n".join(cabecalho) + "\n" + "".join(corpo) + "\n"
    destino = os.path.join(saida, nome)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(texto)
    pacote_sha = sha256(texto.encode("utf-8"))
    print(f"OK -> {nome} | {total_arquivos} arquivos | {total_bytes} bytes embutidos | SHA-256 {pacote_sha[:16]}…")
    return nome, total_arquivos, total_bytes, pacote_sha


def main():
    saida = SAIDA_PADRAO
    if "--pasta" in sys.argv:
        i = sys.argv.index("--pasta")
        saida = sys.argv[i + 1]
    os.makedirs(saida, exist_ok=True)

    resumo = []
    for nome, grupo, desc in PACOTES:
        resumo.append(gerar_pacote(nome, grupo, desc, saida))

    # MANIFESTO geral — estado canônico computado dinamicamente
    n_termos = len(TERMOS)
    n_rel = len(RELACOES)
    n_ficha_flag = sum(1 for t in TERMOS if t[7])
    fichas_fisicas = [f for f in sorted(os.listdir(os.path.join(RAIZ, "termos")))
                      if f.startswith("RC-") and f.endswith(".md")]
    n_fisicas = len(fichas_fisicas)
    prox = f"RC-{n_termos + 1:03d}"
    n_apostilas = len([s for s in sorted(os.listdir(os.path.join(RAIZ, "apostilas", "CONCLUIDAS")))
                       if os.path.isdir(os.path.join(RAIZ, "apostilas", "CONCLUIDAS", s))])
    m = [
        "# MANIFESTO DOS PACOTES DE GARANTIA — PROJETO RC",
        "# Checkpoint: 2026-08-18",
        "",
        "# ESTADO CANÔNICO",
        f"# - {n_termos} termos (RC-001–RC-{n_termos:03d})",
        f"# - {n_rel} relações",
        f"# - {n_ficha_flag} termos com ficha; {n_fisicas} fichas físicas ({n_ficha_flag} canônicas + RC-004 investigação)",
        f"# - próximo código: {prox}",
        f"# - {n_apostilas} apostilas concluídas em apostilas/CONCLUIDAS/",
        "",
        "# ARQUIVOS",
    ]
    for nome, n, b, s in resumo:
        m.append(f"{s}  {nome}  ({n} arquivos; {b} bytes)")
    m.append("")
    m.append("# REGRA DE RESTAURAÇÃO")
    m.append("# Cada pacote usa os delimitadores:")
    m.append("#     ===ARQ: caminho/do/arquivo===")
    m.append("#     [conteúdo literal]")
    m.append("#     ===FIM-ARQ: caminho/do/arquivo===")
    m.append("# A fonte única de verdade é ferramentas/dados_termos.py.")
    m.append("# Restaurador: ferramentas/restaurar_pacotes.py (v3, binário).")
    m.append("# XLSX/DOCX/PDF são REGENERÁVEIS pelos builders; não embutidos (binários).")
    m.append("# O GUIA-MESTRE-RC-APOSTILA.pdf original deve ser anexado junto, se disponível.")
    m.append("")
    manifesto = "\n".join(m)
    with open(os.path.join(saida, "MANIFESTO-PACOTES-2026-08-18.txt"), "w", encoding="utf-8") as f:
        f.write(manifesto)
    print("\nMANIFESTO-PACOTES-2026-08-18.txt gerado.")
    print(f"\nPasta de saída: {saida}")
    print("Tamanhos:")
    for nome, n, b, s in resumo:
        p = os.path.join(saida, nome)
        print(f"  {nome}: {os.path.getsize(p)/1024:.0f} KB")


if __name__ == "__main__":
    main()
