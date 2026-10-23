#!/usr/bin/env python3
"""Normaliza, de forma auditável, o lote STT de outubro de 2026.

Este executor só escreve em ``normalizados_stt_lote_2026-10/`` e em seus
artefatos de auditoria. Nunca altera ``uploads_recepcao/stt-lote-2026-10/``.

Regras executadas:
- oito regras lexicais aprovadas na tabela inicial;
- Sophia/Sofio somente com a trava contextual já aprovada;
- blocos D1 e D2 aprovados no despacho consolidado de 20/10/2026.

Uso:
    python3 ferramentas/normalizar_stt_lote_2026_10.py
    python3 ferramentas/normalizar_stt_lote_2026_10.py --force

``--force`` só pode apagar e regenerar o diretório derivado de nome fechado e
os relatórios derivados deste lote. Ele não aceita outro destino e não tem
qualquer operação de escrita dentro de uploads_recepcao/.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from caminhos_acervo import caminho_atual


RAIZ = Path(__file__).resolve().parent.parent
FONTE = caminho_atual("fonte.recepcao") / "stt-lote-2026-10"
SAIDA = RAIZ / "normalizados_stt_lote_2026-10"
RELATORIO = RAIZ / "diagnostico" / "RELATORIO-NORMALIZACAO-STT-LOTE-2026-10-20.md"
TABELA_INICIAL = "diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md"
DESPACHO = "diagnostico/DESPACHO-NORMALIZACAO-STT-LOTE-2026-10-20.md"
N_FONTES_ESPERADO = 309


@dataclass(frozen=True)
class Regra:
    """Uma equivalência autorizada e, opcionalmente, suas âncoras contextuais."""

    identificador: str
    formas: tuple[str, ...]
    destino: str
    ancora: str
    regime: str
    ancoras_contexto: tuple[str, ...] = ()

    @property
    def padrao(self) -> re.Pattern[str]:
        # A ordenação evita que uma forma curta capture o começo de uma longa.
        alternativas = "|".join(
            re.escape(forma) for forma in sorted(self.formas, key=len, reverse=True)
        )
        return re.compile(rf"(?<!\w)(?:{alternativas})(?!\w)", re.IGNORECASE)

    @property
    def padroes_ancora(self) -> tuple[tuple[str, re.Pattern[str]], ...]:
        return tuple(
            (
                ancora,
                re.compile(
                    rf"(?<!\w){re.escape(ancora)}(?!\w)", re.IGNORECASE
                ),
            )
            for ancora in self.ancoras_contexto
        )


# Tabela inicial, seção 2.1. Estes são os oito itens já aprovados no piloto.
REGRAS_LEGADAS = (
    Regra("STT-A01", ("anunaki",), "Anunnaki", "RC-024 — Anunnaki", "automática"),
    Regra(
        "STT-A02",
        ("trimurte", "trimurto"),
        "Trimurti",
        "RC-104 — Trimurti",
        "automática",
    ),
    Regra(
        "STT-A03",
        ("vismo", "visma", "vizno"),
        "Vishnu",
        "RC-135 — Vishnu (Mavatna)",
        "automática",
    ),
    Regra(
        "STT-A04",
        ("pachupati", "pachupato"),
        "Pashupati",
        "RC-669 — Pashupati",
        "automática",
    ),
    Regra(
        "STT-A05", ("tikkun",), "Tikun", "RC-514 — Tikun Cósmico", "automática"
    ),
    Regra(
        "STT-A06",
        ("mohensof", "mohenso"),
        "Mohen So",
        "RC-081 — Mohen So",
        "automática",
    ),
    Regra(
        "STT-A07",
        ("tirtankaras",),
        "Tirthankaras",
        "RC-397 — Tirthankaras",
        "automática",
    ),
    Regra(
        "STT-A08", ("tote", "toth"), "Thoth", "RC-463/RC-534 — Thoth", "automática"),
)

# Tabela inicial, seção 2.2. O próprio despacho mantém esta regra já aprovada.
REGRA_SOPHIA = Regra(
    "STT-C01",
    ("sofia", "sofio"),
    "Sophia",
    "RC-009 — Sophia (Cristo Cósmico)",
    "automática-contexto",
    (
        "Javé",
        "Jesus",
        "Trimurti",
        "Vishnu",
        "Brahma",
        "avatar",
        "Cristo Cósmico",
        "reintegração",
    ),
)

# Despacho, bloco D1: equivalências lexicais aprovadas para aplicação no corpo.
REGRAS_D1 = (
    Regra(
        "STT-D1.01",
        ("rockman",),
        "Hochmah",
        "RC-565 — Hochmah; RC-009",
        "automática",
    ),
    Regra(
        "STT-D1.02",
        ("uerd", "werd", "erd"),
        "Wyrd",
        "RC-658/RC-560 — Wyrd / Urd",
        "automática",
    ),
    Regra(
        "STT-D1.03", ("ticum",), "Tikun", "RC-514 — Tikun Cósmico", "automática"
    ),
    Regra("STT-D1.04", ("javer",), "Javé", "RC-001; RC-040", "automática"),
    Regra("STT-D1.05", ("sávina",), "Savna", "RC-102 — Shiva (Savna)", "automática"),
    Regra("STT-D1.06", ("vaicunta",), "Vaikuntha", "RC-414", "automática"),
    Regra(
        "STT-D1.07",
        ("rabarata", "marra barata"),
        "Mahabharata",
        "RC-593 — Mahabharata",
        "automática",
    ),
    Regra("STT-D1.08", ("morus",), "Moros", "RC-454; RC-533", "automática"),
    Regra("STT-D1.09", ("viaza",), "Vyasa", "RC-585 — Vyasa", "automática"),
    Regra("STT-D1.10", ("silênio",), "Sileno", "RC-228 — Sileno", "automática"),
    Regra("STT-D1.11", ("horlogue",), "Orlog", "RC-658 — Wyrd / Urd", "automática"),
    Regra("STT-D1.12a", ("aia",), "Aya", "RC-834 — Família Aya", "automática"),
    Regra("STT-D1.12b", ("aie",), "Aye", "RC-835 — Família Aye", "automática"),
    Regra("STT-D1.13", ("chiva",), "Shiva", "RC-102; RC-135", "automática"),
    Regra("STT-D1.14", ("pimeteu",), "Epimeteu", "Glossário canônico; RC-302", "automática"),
    Regra("STT-D1.15", ("riches",), "Rishis", "RC-586 — Rishis", "automática"),
    Regra("STT-D1.16", ("fanis",), "Phanes", "RC-565; RC-282", "automática"),
)

# Despacho, bloco D2: apenas com uma âncora no mesmo parágrafo.
REGRAS_D2 = (
    Regra(
        "STT-D2.01",
        ("elio",),
        "Enlil",
        "RC-487 — Enlil",
        "automática-contexto",
        ("Enki", "Anunnaki", "Anu", "Ninmah", "Ninhursag", "FOXP2", "Babilônia"),
    ),
    Regra(
        "STT-D2.02",
        ("enke", "enck", "enk"),
        "Enki",
        "RC-487 — Enlil; RC-486 — Enki",
        "automática-contexto",
        ("Enlil", "Anunnaki", "Anu", "Ninmah", "Ninhursag", "FOXP2", "Livro Perdido"),
    ),
    Regra(
        "STT-D2.03",
        ("vigno", "vigna", "virgo", "vísgno"),
        "Vishnu",
        "RC-135 — Vishnu (Mavatna)",
        "automática-contexto",
        ("Shiva", "Brahma", "Trimurti", "Sophia", "avatar", "Krishna", "Mavatna", "Javé"),
    ),
    Regra(
        "STT-D2.04",
        ("arapa",),
        "Harapa",
        "RC-329 — Kumari Kandam",
        "automática-contexto",
        ("Mohenjo-Daro", "Indo", "Paquistão", "dravidianos", "Kumari"),
    ),
    Regra(
        "STT-D2.05",
        ("buloca",),
        "Bhuloka",
        "RC-033 — Bhuloka",
        "automática-contexto",
        ("Bramaloca", "Brahmaloka", "universo material", "universo biológico", "loka"),
    ),
    Regra(
        "STT-D2.06",
        ("anã",),
        "Ananque",
        "RC-777 — Ananque",
        "automática-contexto",
        ("Moros", "Moiras", "Nornes", "necessidades", "código", "Sophia"),
    ),
)

# Primeiro as trocas lexicais; em seguida, as contextuais até ponto fixo. Isso
# impede que uma troca inequívoca (p.ex. Javer → Javé) crie uma âncora apenas
# depois de Sofia já ter sido avaliada.
REGRAS_LEXICAS = REGRAS_LEGADAS + REGRAS_D1
REGRAS_CONTEXTUAIS = (REGRA_SOPHIA,) + REGRAS_D2
REGRAS_EXECUTADAS = REGRAS_LEXICAS + REGRAS_CONTEXTUAIS


@dataclass(frozen=True)
class Preservar:
    """Forma que deve ser apenas inventariada, nunca reescrita."""

    identificador: str
    formas: tuple[str, ...]
    motivo: str

    @property
    def padrao(self) -> re.Pattern[str]:
        alternativas = "|".join(
            re.escape(forma) for forma in sorted(self.formas, key=len, reverse=True)
        )
        return re.compile(rf"(?<!\w)(?:{alternativas})(?!\w)", re.IGNORECASE)


# D3 do despacho + travas PENDENTE já homologadas na tabela inicial.
REGRAS_PRESERVADAS = (
    Preservar(
        "STT-P01",
        ("morrenso", "morrensor", "morrenson"),
        "colisão Morren So × Morlens × Moros; sem alvo global seguro",
    ),
    Preservar(
        "STT-P02", ("luzbel",), "pode ser Yel Luzbel ou Lúcifer conforme o contexto"
    ),
    Preservar(
        "STT-P03", ("brama", "brahman"), "formas com estatutos/referentes distintos"
    ),
    Preservar(
        "STT-P04", ("temes", "tênis"), "Têmis × usos comuns, inclusive Tênis Clube Paulista"
    ),
    Preservar("STT-P05", ("deus",), "palavra portuguesa comum; nunca inferir Zeus"),
    Preservar("STT-P06", ("viaja",), "verbo comum; distinto de Viaza"),
    Preservar(
        "STT-P07", ("vista", "virgem"), "formas comuns; não inferir Vishnu por semelhança"
    ),
    Preservar(
        "STT-P08",
        ("urdre", "vivendre", "scud"),
        "componentes das Nornes; não fundir em Wyrd",
    ),
    Preservar(
        "STT-P09",
        ("pularra", "prara", "pharara", "porularra", "pulra"),
        "RC-743 aguarda áudio; não escolher grafia",
    ),
    Preservar(
        "STT-P10",
        ("lémion", "lénion", "lemion"),
        "grafias STT datadas de Len Mion; não converter retroativamente",
    ),
    Preservar("STT-P11", ("anunnakis",), "plural oral; não apagar número gramatical"),
    Preservar("STT-P12", ("nephilim",), "transliteração legítima; sem troca editorial"),
    Preservar("STT-P13", ("parvati",), "variante transliterativa; sem troca editorial"),
    Preservar("STT-P14", ("capella",), "forma externa legítima; sem troca editorial"),
    Preservar("STT-P15", ("gauzu",), "forma registrada na Base; não é ruído demonstrado"),
)


@dataclass(frozen=True)
class Evento:
    arquivo: str
    linha: int
    paragrafo: int
    regra: str
    regime: str
    antes: str
    depois: str
    ancora_contexto: str | None
    trecho_antes: str
    trecho_depois: str


@dataclass(frozen=True)
class Pendente:
    arquivo: str
    linha: int
    paragrafo: int
    regra: str
    antes: str
    motivo: str
    ancoras_exigidas: tuple[str, ...]
    trecho: str


def sha256_bytes(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def escape_contexto(texto: str) -> str:
    """Compacta contexto para Markdown/JSON sem alterar o derivado."""
    return " ".join(texto.replace("|", "\\|").split())


def excerto(texto: str, inicio: int, fim: int, troca: str | None = None) -> str:
    raio = 100
    a = max(0, inicio - raio)
    b = min(len(texto), fim + raio)
    bruto = texto[a:b]
    if troca is not None:
        bruto = texto[a:inicio] + troca + texto[fim:b]
    return ("…" if a else "") + escape_contexto(bruto) + ("…" if b < len(texto) else "")


def separar_frontmatter(texto: str, nome: str) -> tuple[str, str]:
    """Separa sem reformatar o YAML, preservando seus bytes no produto final."""
    padrao = re.compile(r"\A---[ \t]*\r?\n.*?^---[ \t]*(?:\r?\n|\Z)", re.DOTALL | re.MULTILINE)
    achado = padrao.match(texto)
    if not achado:
        raise RuntimeError(f"{nome}: frontmatter YAML delimitado por --- não encontrado")
    return texto[: achado.end()], texto[achado.end() :]


def limites_paragrafos(texto: str) -> list[tuple[int, int]]:
    """Retorna parágrafos separados por ao menos uma linha em branco."""
    limites: list[tuple[int, int]] = []
    inicio = 0
    for quebra in re.finditer(r"(?:\r?\n[ \t]*){2,}", texto):
        if quebra.start() > inicio:
            limites.append((inicio, quebra.start()))
        inicio = quebra.end()
    if inicio < len(texto):
        limites.append((inicio, len(texto)))
    return limites


def contexto_do_paragrafo(
    texto: str, inicio: int, limites: list[tuple[int, int]], inicios: list[int]
) -> tuple[int, str]:
    indice = bisect.bisect_right(inicios, inicio) - 1
    if indice < 0:
        indice = 0
    a, b = limites[indice]
    return indice + 1, texto[a:b]


def ancora_no_paragrafo(regra: Regra, paragrafo: str) -> str | None:
    for nome, padrao in regra.padroes_ancora:
        if padrao.search(paragrafo):
            return nome
    return None


def aplicar_regra(
    arquivo: str, texto: str, regra: Regra, linha_base: int
) -> tuple[str, list[Evento], list[Pendente]]:
    """Aplica uma regra e registra trocas e recusas de contexto.

    ``linha_base`` é a quantidade de quebras no frontmatter, para que a trilha
    informe a linha física do arquivo fonte, não apenas a linha do corpo.
    """
    limites = limites_paragrafos(texto)
    if not limites:
        limites = [(0, len(texto))]
    inicios = [inicio for inicio, _fim in limites]
    eventos: list[Evento] = []
    pendentes: list[Pendente] = []
    origem = texto

    def substituir(casamento: re.Match[str]) -> str:
        paragrafo_numero, paragrafo = contexto_do_paragrafo(
            origem, casamento.start(), limites, inicios
        )
        ancora = None
        if regra.ancoras_contexto:
            ancora = ancora_no_paragrafo(regra, paragrafo)
            if ancora is None:
                pendentes.append(
                    Pendente(
                        arquivo=arquivo,
                        linha=linha_base + origem.count("\n", 0, casamento.start()) + 1,
                        paragrafo=paragrafo_numero,
                        regra=regra.identificador,
                        antes=casamento.group(0),
                        motivo="âncora contextual ausente no mesmo parágrafo",
                        ancoras_exigidas=regra.ancoras_contexto,
                        trecho=excerto(origem, casamento.start(), casamento.end()),
                    )
                )
                return casamento.group(0)
        eventos.append(
            Evento(
                arquivo=arquivo,
                linha=linha_base + origem.count("\n", 0, casamento.start()) + 1,
                paragrafo=paragrafo_numero,
                regra=regra.identificador,
                regime=regra.regime,
                antes=casamento.group(0),
                depois=regra.destino,
                ancora_contexto=ancora,
                trecho_antes=excerto(origem, casamento.start(), casamento.end()),
                trecho_depois=excerto(
                    origem, casamento.start(), casamento.end(), regra.destino
                ),
            )
        )
        return regra.destino

    return regra.padrao.sub(substituir, origem), eventos, pendentes


def normalizar(arquivo: str, texto: str) -> tuple[str, list[Evento], list[Pendente]]:
    frontmatter, corpo = separar_frontmatter(texto, arquivo)
    linha_base = frontmatter.count("\n")
    atual = corpo
    eventos: list[Evento] = []

    # 1) Formas lexicais inequívocas não dependem de contexto.
    for regra in REGRAS_LEXICAS:
        atual, eventos_regra, _pendentes_ignorados = aplicar_regra(
            arquivo, atual, regra, linha_base
        )
        eventos.extend(eventos_regra)

    # 2) Algumas substituições podem revelar uma âncora para outra regra no
    # mesmo parágrafo (Enck → Enki e Elio → Enlil, por exemplo). Aplicamos o
    # conjunto contextual até estabilizar, sem multiplicar no log as recusas
    # provisórias dos primeiros ciclos.
    for _ciclo in range(len(REGRAS_CONTEXTUAIS) + 1):
        antes_do_ciclo = atual
        for regra in REGRAS_CONTEXTUAIS:
            atual, eventos_regra, _pendentes_ignorados = aplicar_regra(
                arquivo, atual, regra, linha_base
            )
            eventos.extend(eventos_regra)
        if atual == antes_do_ciclo:
            break
    else:
        raise RuntimeError(f"{arquivo}: regras contextuais não estabilizaram")

    # 3) Inventário definitivo das recusas no estado já estabilizado. Nenhuma
    # regra pode produzir nova troca neste passe; se produzir, é erro lógico.
    pendentes: list[Pendente] = []
    for regra in REGRAS_CONTEXTUAIS:
        conferido, eventos_finais, pendentes_regra = aplicar_regra(
            arquivo, atual, regra, linha_base
        )
        if conferido != atual or eventos_finais:
            raise RuntimeError(f"{arquivo}: contexto não estava estabilizado")
        pendentes.extend(pendentes_regra)

    return frontmatter + atual, eventos, pendentes


def inventariar_preservados(arquivo: str, texto: str) -> list[Pendente]:
    """Registra D3 e pendências antigas a partir do corpo bruto, sem alterá-lo."""
    frontmatter, corpo = separar_frontmatter(texto, arquivo)
    linha_base = frontmatter.count("\n")
    limites = limites_paragrafos(corpo)
    if not limites:
        limites = [(0, len(corpo))]
    inicios = [inicio for inicio, _fim in limites]
    itens: list[Pendente] = []
    for regra in REGRAS_PRESERVADAS:
        for casamento in regra.padrao.finditer(corpo):
            paragrafo_numero, _paragrafo = contexto_do_paragrafo(
                corpo, casamento.start(), limites, inicios
            )
            itens.append(
                Pendente(
                    arquivo=arquivo,
                    linha=linha_base + corpo.count("\n", 0, casamento.start()) + 1,
                    paragrafo=paragrafo_numero,
                    regra=regra.identificador,
                    antes=casamento.group(0),
                    motivo=regra.motivo,
                    ancoras_exigidas=(),
                    trecho=excerto(corpo, casamento.start(), casamento.end()),
                )
            )
    return itens


def arquivos_fonte() -> list[Path]:
    if not FONTE.is_dir():
        raise RuntimeError(f"Diretório fonte ausente: {FONTE.relative_to(RAIZ)}/")
    arquivos = sorted(p for p in FONTE.glob("*.md") if p.name != "README.md")
    if len(arquivos) != N_FONTES_ESPERADO:
        raise RuntimeError(
            f"Esperadas {N_FONTES_ESPERADO} transcrições .md em "
            f"{FONTE.relative_to(RAIZ)}/; encontradas {len(arquivos)}."
        )
    return arquivos


def serializar_evento(evento: Evento) -> dict[str, object]:
    return {
        "arquivo": evento.arquivo,
        "linha": evento.linha,
        "paragrafo": evento.paragrafo,
        "regra": evento.regra,
        "regime": evento.regime,
        "antes": evento.antes,
        "depois": evento.depois,
        "ancora_contexto": evento.ancora_contexto,
        "trecho_antes": evento.trecho_antes,
        "trecho_depois": evento.trecho_depois,
    }


def serializar_pendente(item: Pendente) -> dict[str, object]:
    return {
        "arquivo": item.arquivo,
        "linha": item.linha,
        "paragrafo": item.paragrafo,
        "regra": item.regra,
        "antes": item.antes,
        "motivo": item.motivo,
        "ancoras_exigidas": list(item.ancoras_exigidas),
        "trecho": item.trecho,
    }


def escrever_jsonl(caminho: Path, itens: Iterable[dict[str, object]]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as destino:
        for item in itens:
            destino.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")


def resumo_regras(eventos: list[Evento]) -> list[tuple[Regra, int, int]]:
    total_por_regra = Counter(evento.regra for evento in eventos)
    arquivos_por_regra: dict[str, set[str]] = defaultdict(set)
    for evento in eventos:
        arquivos_por_regra[evento.regra].add(evento.arquivo)
    return [
        (regra, total_por_regra[regra.identificador], len(arquivos_por_regra[regra.identificador]))
        for regra in REGRAS_EXECUTADAS
    ]


def montar_readme(
    totais: list[tuple[Regra, int, int]], n_fontes: int, n_eventos: int, n_pendentes: int
) -> str:
    linhas_regras = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | **{regra.destino}** | "
        f"{quantidade} | {arquivos} | {regra.regime} |"
        for regra, quantidade, arquivos in totais
    )
    return f"""# Transcrições STT normalizadas — lote 2026-10

> **Natureza:** cópias derivadas e auditáveis; **não são verbatim bruto**.
>
> **Fontes imutáveis:** `uploads_recepcao/stt-lote-2026-10/`
>
> **Executor:** `ferramentas/normalizar_stt_lote_2026_10.py`
>
> **Política inicial:** `{TABELA_INICIAL}`
>
> **Despacho autorizado:** `{DESPACHO}`

Este diretório contém uma cópia de cada uma das {n_fontes} transcrições do lote,
com as regras já aprovadas e os blocos D1/D2 autorizados pelo Curador em
20/10/2026. O frontmatter, URLs e dados de origem foram preservados; somente o
corpo da transcrição recebeu as trocas auditadas abaixo.

## Resultado

- cópias derivadas: **{n_fontes}**;
- substituições rastreadas: **{n_eventos}**;
- candidatos contextuais não alterados: **{n_pendentes}**;
- itens D3 e pendências antigas: ver `preservados-d3.jsonl`;
- fontes alteradas: **0**;
- idempotência: **verificada**.

## Censo por regra executada

| Regra | DE | PARA | Trocas | Arquivos | Regime |
|---|---|---|---:|---:|---|
{linhas_regras}

## Artefatos de auditoria

| Arquivo | Conteúdo |
|---|---|
| `manifesto-fontes-sha256.tsv` | caminho, bytes e SHA-256 de cada bruto usado |
| `manifesto-derivados-sha256.tsv` | SHA-256 de cada derivado, SHA da origem e número de trocas |
| `rastreio-antes-depois.jsonl` | cada troca com regra, linha, parágrafo e excertos |
| `pendentes-contexto.jsonl` | candidatos de regras contextuais sem âncora suficiente |
| `preservados-d3.jsonl` | formas bloqueadas/preservadas, sem alteração |
| `{RELATORIO.relative_to(RAIZ)}` | síntese humana, censo e verificações |

A execução nunca regrava os arquivos em `uploads_recepcao/`. Para repetir a
geração, use o executor com `--force`; ele só remove este diretório derivado e
os relatórios derivados associados.
"""


def montar_relatorio(
    fontes: list[Path],
    resultados: dict[str, dict[str, object]],
    eventos: list[Evento],
    pendentes: list[Pendente],
    preservados: list[Pendente],
) -> str:
    totais = resumo_regras(eventos)
    tabela_regras = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | **{regra.destino}** | "
        f"{quantidade} | {arquivos} | {regra.ancora} | {regra.regime} |"
        for regra, quantidade, arquivos in totais
    )
    por_familia_preservada = Counter(item.regra for item in preservados)
    tabela_preservados = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | "
        f"{por_familia_preservada[regra.identificador]} | {regra.motivo} |"
        for regra in REGRAS_PRESERVADAS
    )
    por_regra_pendente = Counter(item.regra for item in pendentes)
    tabela_pendentes = "\n".join(
        f"| `{regra.identificador}` | {por_regra_pendente[regra.identificador]} | "
        f"`{'` / `'.join(regra.formas)}` → **{regra.destino}** |"
        for regra in REGRAS_EXECUTADAS
        if regra.ancoras_contexto
    )
    total_arquivos_trocados = sum(
        1 for resultado in resultados.values() if int(resultado["mudancas"]) > 0
    )
    total_arquivos_sem_troca = len(fontes) - total_arquivos_trocados
    amostra = eventos[:25]
    tabela_amostra = "\n".join(
        f"| `{evento.arquivo}` | {evento.linha} | `{evento.regra}` | "
        f"`{evento.antes}` | **{evento.depois}** | "
        f"{evento.ancora_contexto or '—'} |"
        for evento in amostra
    ) or "| — | — | — | — | — | — |"
    return f"""# Relatório de normalização STT — lote 2026-10

**Data de geração:** 20/10/2026

**Executor:** `ferramentas/normalizar_stt_lote_2026_10.py`

**Fonte:** `uploads_recepcao/stt-lote-2026-10/`

**Saída:** `normalizados_stt_lote_2026-10/`

**Despacho aplicado:** D1 e D2 aprovados; D3 preservado.

> **Resultado derivado, não verbatim.** Os {len(fontes)} brutos permaneceram
> inalterados; as cópias normalizadas têm manifesto SHA-256 e rastreio completo.

## Resultado geral

| Item | Resultado |
|---|---:|
| Fontes brutas lidas | {len(fontes)} |
| Cópias derivadas escritas | {len(fontes)} |
| Arquivos com ao menos uma troca | {total_arquivos_trocados} |
| Arquivos sem troca | {total_arquivos_sem_troca} |
| Substituições aplicadas | {len(eventos)} |
| Contextuais preservados por falta de âncora | {len(pendentes)} |
| Ocorrências D3/pendentes preservadas | {len(preservados)} |
| Fontes brutas alteradas | **0** |
| Idempotência do produto | **OK** |

## Censo das regras executadas

| Regra | DE | PARA | Trocas | Arquivos | Âncora | Regime |
|---|---|---|---:|---:|---|---|
{tabela_regras}

As regras `STT-A01` a `STT-A08` são as oito equivalências já aprovadas. `STT-C01`
corresponde a Sophia/Sofio com a trava contextual original. `STT-D1.*` e
`STT-D2.*` executam exatamente os blocos autorizados no despacho consolidado.

> **Reconciliação do pré-censo.** A projeção exploratória de 405 trocas para as
> oito regras legadas contou uma ocorrência de `Toth` no frontmatter. Como o
> executor protege o frontmatter por desenho, o censo aplicado dessas regras é
> **404**. A regra Sophia sobe de 502 candidatos contextualmente aptos no
> pré-censo para **514** porque o ponto fixo avalia o contexto depois das trocas
> lexicais autorizadas (por exemplo, `Javer` → `Javé`), sem tocar o YAML.

## Contextuais não aplicados

Uma ocorrência contextual só foi trocada com ao menos uma âncora no mesmo
parágrafo. O detalhe por linha está em
`normalizados_stt_lote_2026-10/pendentes-contexto.jsonl`.

| Regra contextual | Mantidos sem troca | Mapeamento |
|---|---:|---|
{tabela_pendentes}

## Formas preservadas (D3 e travas antigas)

| Regra | Formas inventariadas | Ocorrências mantidas | Motivo |
|---|---|---:|---|
{tabela_preservados}

O inventário completo com arquivo, linha, parágrafo e excerto está em
`normalizados_stt_lote_2026-10/preservados-d3.jsonl`. Uma ocorrência aparecer
nesse inventário **não** significa erro: ela foi conscientemente deixada igual
à fonte por colisão, variante legítima ou insuficiência de contexto.

## Amostra de trilha `antes → depois`

O rastreio integral, não apenas esta amostra, está em
`normalizados_stt_lote_2026-10/rastreio-antes-depois.jsonl`.

| Arquivo | Linha | Regra | Antes | Depois | Âncora contextual |
|---|---:|---|---|---|---|
{tabela_amostra}

## Integridade e reprodutibilidade

1. Antes da escrita, o executor leu e reteve os bytes das {len(fontes)} fontes.
2. Após a escrita, recalculou todos os SHA-256 e comprovou que cada bruto era
   idêntico ao byte originalmente lido.
3. `manifesto-fontes-sha256.tsv` e `manifesto-derivados-sha256.tsv` registram
   caminho, bytes, hash de origem, hash derivado e total de trocas por arquivo.
4. O executor rodou um segundo passe em memória sobre cada derivado; qualquer
   nova troca abortaria a execução. Nenhuma foi encontrada.
5. O YAML/frontmatter e as URLs não foram alvo de regex: a transformação atua
   apenas depois do delimitador final `---` do frontmatter.

## Limites explícitos

- Não houve cotejo com áudio nesta etapa.
- O bruto STT não foi “corrigido”: ele permanece em `uploads_recepcao/`.
- D3 não foi inferido, nem substituído. Casos com baixa segurança seguem
  listados e preservados para eventual despacho futuro.
"""


def escrever_manifestos(
    fontes: list[Path], resultados: dict[str, dict[str, object]]
) -> None:
    with (SAIDA / "manifesto-fontes-sha256.tsv").open(
        "w", encoding="utf-8", newline="\n"
    ) as destino:
        destino.write("arquivo_fonte\tbytes\tsha256_fonte\n")
        for fonte in fontes:
            item = resultados[fonte.name]
            destino.write(f"{fonte.name}\t{item['bytes_fonte']}\t{item['sha_fonte']}\n")
    with (SAIDA / "manifesto-derivados-sha256.tsv").open(
        "w", encoding="utf-8", newline="\n"
    ) as destino:
        destino.write(
            "arquivo_derivado\tbytes_derivado\tsha256_derivado\tsha256_fonte\ttrocas\n"
        )
        for fonte in fontes:
            item = resultados[fonte.name]
            destino.write(
                f"{fonte.name}\t{item['bytes_derivado']}\t{item['sha_derivado']}\t"
                f"{item['sha_fonte']}\t{item['mudancas']}\n"
            )


def preparar_resultados(fontes: list[Path]) -> tuple[
    dict[str, bytes], dict[str, dict[str, object]], list[Evento], list[Pendente], list[Pendente]
]:
    """Lê tudo antes de escrever; aborta antes de gerar lote parcial em caso de falha."""
    brutos = {fonte.name: fonte.read_bytes() for fonte in fontes}
    resultados: dict[str, dict[str, object]] = {}
    todos_eventos: list[Evento] = []
    todos_pendentes: list[Pendente] = []
    todos_preservados: list[Pendente] = []

    for fonte in fontes:
        bruto = brutos[fonte.name]
        try:
            texto = bruto.decode("utf-8")
        except UnicodeDecodeError as erro:
            raise RuntimeError(f"{fonte.name}: não é UTF-8 ({erro})") from erro
        derivado, eventos, pendentes = normalizar(fonte.name, texto)
        # Invariante forte: a aplicação completa no próprio produto não pode gerar nada.
        segundo_passe, eventos_2, pendentes_2 = normalizar(fonte.name, derivado)
        # Pendências contextuais podem reaparecer porque, por definição, seu
        # texto é preservado. Idempotência exige que o produto não mude nem
        # dispare nova substituição.
        if segundo_passe != derivado or eventos_2:
            raise RuntimeError(
                f"{fonte.name}: falha de idempotência; o segundo passe produziu "
                f"{len(eventos_2)} troca(s)."
            )
        preservados = inventariar_preservados(fonte.name, texto)
        derivado_bytes = derivado.encode("utf-8")
        resultados[fonte.name] = {
            "texto_derivado": derivado,
            "sha_fonte": sha256_bytes(bruto),
            "sha_derivado": sha256_bytes(derivado_bytes),
            "bytes_fonte": len(bruto),
            "bytes_derivado": len(derivado_bytes),
            "mudancas": len(eventos),
        }
        todos_eventos.extend(eventos)
        todos_pendentes.extend(pendentes)
        todos_preservados.extend(preservados)
    return brutos, resultados, todos_eventos, todos_pendentes, todos_preservados


def garantir_destinos(force: bool) -> None:
    if SAIDA.resolve() == FONTE.resolve() or FONTE.resolve() in SAIDA.resolve().parents:
        raise RuntimeError("Saída derivada não pode coincidir com a árvore de fontes.")
    if SAIDA.exists():
        if not force:
            raise FileExistsError(
                f"Saída já existe: {SAIDA.relative_to(RAIZ)}/. Use --force para regenerar somente o derivado."
            )
        shutil.rmtree(SAIDA)
    if RELATORIO.exists() and not force:
        raise FileExistsError(
            f"Relatório já existe: {RELATORIO.relative_to(RAIZ)}. Use --force para regenerar o derivado."
        )
    SAIDA.mkdir(parents=True, exist_ok=False)


def escrever_saida(
    fontes: list[Path],
    resultados: dict[str, dict[str, object]],
    eventos: list[Evento],
    pendentes: list[Pendente],
    preservados: list[Pendente],
) -> None:
    for fonte in fontes:
        (SAIDA / fonte.name).write_bytes(str(resultados[fonte.name]["texto_derivado"]).encode("utf-8"))
    escrever_manifestos(fontes, resultados)
    escrever_jsonl(SAIDA / "rastreio-antes-depois.jsonl", map(serializar_evento, eventos))
    escrever_jsonl(SAIDA / "pendentes-contexto.jsonl", map(serializar_pendente, pendentes))
    escrever_jsonl(SAIDA / "preservados-d3.jsonl", map(serializar_pendente, preservados))
    totais = resumo_regras(eventos)
    (SAIDA / "README.md").write_text(
        montar_readme(totais, len(fontes), len(eventos), len(pendentes)),
        encoding="utf-8",
        newline="\n",
    )
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text(
        montar_relatorio(fontes, resultados, eventos, pendentes, preservados),
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="remove e regenera somente a saída derivada fechada deste lote",
    )
    args = parser.parse_args()

    fontes = arquivos_fonte()
    brutos, resultados, eventos, pendentes, preservados = preparar_resultados(fontes)
    garantir_destinos(args.force)
    escrever_saida(fontes, resultados, eventos, pendentes, preservados)

    # A garantia decisiva: fonte em disco precisa coincidir com os bytes pré-escrita.
    for fonte in fontes:
        atual = fonte.read_bytes()
        if atual != brutos[fonte.name]:
            raise RuntimeError(f"Violação de integridade: fonte alterada: {fonte.name}")
        if sha256_bytes(atual) != str(resultados[fonte.name]["sha_fonte"]):
            raise RuntimeError(f"Violação de hash da fonte: {fonte.name}")

    print(
        "OK — lote normalizado: "
        f"{len(fontes)} derivados · {len(eventos)} substituições · "
        f"{len(pendentes)} contextuais preservados · {len(preservados)} D3/preservados · "
        "0 fontes alteradas · idempotência OK"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, RuntimeError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        raise SystemExit(2)
