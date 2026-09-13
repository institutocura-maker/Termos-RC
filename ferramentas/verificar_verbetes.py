# -*- coding: utf-8 -*-
"""
# STATUS: ATIVO-P7 (portão verbatim; Onda 0.2 loader)
Verificacao mecanica dos verbetes da Enciclopedia (ed. 2026.1).

Dois asserts, nenhuma indulgencia:
  1. VERBATIM — todo trecho entre « » de um verbete tem de ocorrer BYTE A BYTE
     em alguma ficha de `termos/`. Nenhuma aspa e composta a mao: se o trecho
     nao esta no corpus de fichas, ele nao e citacao — e interpretacao nossa, e
     por isso nao pode estar entre aspas.
  2. CODIGOS — todo `RC-NNN` citado tem de existir no registro-mestre
     (`ferramentas/dados_termos.py`). Verbete nao cria codigo.

Uso: python3 ferramentas/verificar_verbetes.py [pasta]
"""
import os
import re
import sys
import glob

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import loader as d  # noqa: E402 — Onda 0.2: loader único


def carregar_documento(caminho):
    """Le um caminho relativo a raiz, aceitando glob (ex.: termos/RC-600-*.md)."""
    alvo = os.path.join(RAIZ, caminho)
    if any(ch in alvo for ch in "*?["):
        achou = sorted(glob.glob(alvo))
        assert achou, f"glob sem resultado: {caminho}"
        return "".join(open(p, encoding="utf-8").read() for p in achou)
    assert os.path.exists(alvo), f"documento-fonte declarado inexistente: {caminho}"
    return open(alvo, encoding="utf-8").read()


def main(pasta=None):
    pasta = pasta or os.path.join(RAIZ, "pedagogico", "enciclopedia", "verbetes-modelo")
    corpus = ""
    for p in sorted(glob.glob(os.path.join(RAIZ, "termos", "*.md"))):
        corpus += open(p, encoding="utf-8").read()
    # 2.4 (12/09/2026): notas de processo migraram verbatim para notas/fichas/ —
    # lastro lá é lastro da ficha; o corpus do verificador acompanha o arquivo.
    for p in sorted(glob.glob(os.path.join(RAIZ, "notas", "fichas", "*.md"))):
        corpus += open(p, encoding="utf-8").read()
    codigos = {t[0] for t in d.TERMOS}

    falhas_q, falhas_c, total_q, n_cod = [], [], 0, 0
    # READMEs de laboratorio nao sao verbetes: ficam fora da conferencia
    arquivos = sorted(g for g in glob.glob(os.path.join(pasta, "**", "*.md"), recursive=True)
                      if os.path.basename(g).lower() != "readme.md")
    assert arquivos, f"nenhum verbete em {pasta}"

    for arq in arquivos:
        txt = open(arq, encoding="utf-8").read()
        # secoes de redacao (sem ficha na Base) declaram os seus documentos-fonte:
        # todo caminho .md entre crases entra no corpus de conferencia.
        declarados = re.findall(r"`([^`\n]+\.(?:md|txt))`", txt)
        extra = ""
        for cam in sorted(set(declarados)):
            if "verbetes-modelo" in cam or "verbetes-secao-24" in cam:
                continue
            # caminho relativo ao verbete (../algo.md) ou a raiz do repositorio
            alvo = (os.path.normpath(os.path.join(os.path.dirname(arq), cam))
                    if cam.startswith(".") else os.path.join(RAIZ, cam))
            extra += carregar_documento(alvo)
        for cit in re.findall(r"«([^»]+)»", txt):
            total_q += 1
            if cit not in corpus and cit not in extra:
                falhas_q.append((os.path.basename(arq), cit))
        for c in sorted(set(re.findall(r"RC-\d{3}", txt))):
            n_cod += 1
            if c not in codigos:
                falhas_c.append((os.path.basename(arq), c))

    print("verbetes conferidos : %d" % len(arquivos))
    print("verbatim conferidos : %d · falhas: %d" % (total_q, len(falhas_q)))
    for a, c in falhas_q:
        print("  X %s: %s" % (a, c[:120]))
    print("codigos conferidos  : %d · falhas: %d" % (n_cod, len(falhas_c)))
    for a, c in falhas_c:
        print("  X %s: %s" % (a, c))

    assert not falhas_q, "%d verbatim nao conferem com as fichas" % len(falhas_q)
    assert not falhas_c, "%d codigos inexistentes no registro-mestre" % len(falhas_c)
    print("\nOK — todo verbatim confere byte a byte e todo codigo existe na Base.")
    print("Base intacta: %d termos · %d fichas · %d relacoes"
          % (len(d.TERMOS), sum(1 for t in d.TERMOS if t[7]), len(d.RELACOES)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
