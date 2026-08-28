#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica as ampliações P2021-05-15 nas fichas, lendo o pacote de texto puro.

Padrão do rito: `apostilas/CONCLUIDAS/2023-06-24_*/analise/_aplicar_ampliacoes_*.py`
(idem `_aplicar_ampliacoes_B022/B074/B075`). RAIZ = AQUI.parents[2] — rodar **antes**
de mover a pasta do ciclo para `apostilas/CONCLUIDAS/`.

Faz três coisas por ficha, e nada mais:
 1. insere a seção `## Ampliação — P2021-05-15 (…)` antes de `## Fontes` (ou no fim, após `---`);
 2. acrescenta a linha da fonte na tabela `## Fontes` (respeitando o nº de colunas da tabela);
 3. atualiza `**Última atualização**` para 2026-08-28.

Códigos do pacote sem arquivo em `termos/` são pulados (são os `ficha=False` — o vínculo
deles vive na malha, `ferramentas/dados_termos.py`; o conteúdo fica no Bloco 2 do pacote).
"""
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
TERMOS = RAIZ / "termos"
FONTE = AQUI / "_ampliacoes_P2021-05-15.txt"
FONTE_SIGLA = "P2021-05-15"
FONTE_TITULO = "As Etnias Hiperbóreas e os Anunnakis"
TITULO_SECAO = f"## Ampliação — {FONTE_SIGLA} ({FONTE_TITULO})"
DATA = "2026-08-28"

texto = FONTE.read_text(encoding="utf-8")
aplicadas, puladas, sem_ficha, ja = [], [], [], []

for bloco in texto.split("### "):
    bloco = bloco.strip()
    if not bloco:
        continue
    linha1, _, conteudo = bloco.partition("\n")
    linha1 = linha1.strip()
    if not re.fullmatch(r"RC-\d{3}", linha1):
        continue                                  # BLOCOS 2, 3 e 4 não são fichas
    cod = linha1
    conteudo = conteudo.strip()
    alvo = next((f for f in TERMOS.glob(f"{cod}-*.md")), None)
    if not alvo:
        sem_ficha.append(cod)
        continue
    txt = alvo.read_text(encoding="utf-8")
    if TITULO_SECAO in txt or f"## Ampliação — {FONTE_SIGLA}" in txt:
        ja.append(cod)
        continue

    secao = f"\n{TITULO_SECAO}\n\n{conteudo}\n"
    if "## Fontes" in txt:
        txt = txt.replace("## Fontes", secao + "\n## Fontes", 1)
    else:
        txt = txt.rstrip() + "\n" + secao + "\n---\n"

    # --- linha na tabela de fontes (só se a ficha ainda não cita esta fonte) ---
    i = txt.find("## Fontes")
    if i >= 0:
        ini = txt.find("\n", i) + 1
        fim = txt.find("\n\n", ini)
        tabela = txt[ini:fim if fim > 0 else len(txt)]
        linhas = tabela.rstrip("\n").split("\n")
        ncols = max((l.count("|") - 1 for l in linhas if l.strip().startswith("|")), default=3)
        celulas = {
            3: [FONTE_SIGLA, f"{FONTE_TITULO} (palestra/STT)", "citação verbatim; paráfrase"],
            4: [FONTE_SIGLA, f"{FONTE_TITULO} (palestra)", "—", "transcrição automatizada; citação"],
        }.get(ncols, [FONTE_SIGLA, FONTE_TITULO] + ["—"] * (ncols - 2))
        celulas = (celulas + ["—"] * ncols)[:ncols]
        nova = "| " + " | ".join(celulas) + " |"
        if f"| {FONTE_SIGLA} " not in tabela:
            for k, l in enumerate(linhas):            # entra logo após a linha |---|---|
                if re.match(r"^\|[\s:|-]+\|$", l.strip()):
                    linhas.insert(k + 1, nova)
                    break
            else:
                linhas.append(nova)
            corpo = "\n".join(linhas).rstrip("\n") + "\n"
            txt = (txt[:ini] + corpo + txt[fim:]) if fim > 0 else (txt[:ini] + corpo)

    txt = re.sub(r"(\|\s*\*\*Última atualização\*\*\s*\|\s*)[0-9-]{10}(\s*\|)", rf"\g<1>{DATA}\g<2>", txt)
    alvo.write_text(txt, encoding="utf-8")
    aplicadas.append(cod)

print(f"fichas ampliadas: {len(aplicadas)}")
if ja:
    print("já ampliadas (intocadas):", ", ".join(ja))
if sem_ficha:
    print("sem ficha (vínculo só na malha):", ", ".join(sem_ficha))
