#!/usr/bin/env python3
"""Gera cópias STT normalizadas sem nunca modificar fontes/pilotos_historicos/.

Este é deliberadamente um normalizador pequeno e fechado: aplica apenas as oito
regras AUTOMÁTICA de diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md.
Não é corretor ortográfico e não aplica regras contextuais ou itens marcados
REVISAR/PRESERVAR.

Uso:
    python3 ferramentas/normalizar_stt_dry_run.py
    python3 ferramentas/normalizar_stt_dry_run.py --force

A primeira forma recusa sobrescrever saídas já existentes. --force só pode
reescrever o diretório derivado e o relatório; jamais toca nos brutos.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import textwrap
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from caminhos_acervo import caminho_atual


RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = caminho_atual("fonte.recepcao.pilotos_historicos")
SAIDA_PADRAO = RAIZ / "normalizados_stt_dry_run"
RELATORIO_PADRAO = RAIZ / "diagnostico" / "RELATORIO-NORMALIZACAO-STT-DRY-RUN-2026-10-20.md"
TABELA = "diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md"

# Toda regra abaixo existe na seção 2.1 (AUTOMÁTICA) da tabela diagnóstica.
# A ordem no padrão põe as formas mais longas primeiro para impedir captura
# parcial (p.ex. Mohensof antes de Mohenso). \w garante fronteira Unicode.
@dataclass(frozen=True)
class Regra:
    identificador: str
    formas: tuple[str, ...]
    destino: str
    ancora: str

    @property
    def padrao(self) -> re.Pattern[str]:
        alternativas = "|".join(re.escape(forma) for forma in self.formas)
        return re.compile(rf"(?<!\w)(?:{alternativas})(?!\w)", re.IGNORECASE)


REGRAS = (
    Regra("STT-A01", ("anunaki",), "Anunnaki", "RC-024 — Anunnaki"),
    Regra("STT-A02", ("trimurte", "trimurto"), "Trimurti", "RC-104 — Trimurti"),
    Regra("STT-A03", ("vismo", "visma", "vizno"), "Vishnu", "RC-135 — Vishnu (Mavatna)"),
    Regra("STT-A04", ("pachupati", "pachupato"), "Pashupati", "RC-669 — Pashupati"),
    Regra("STT-A05", ("tikkun",), "Tikun", "RC-514 — Tikun Cósmico"),
    Regra("STT-A06", ("mohensof", "mohenso"), "Mohen So", "RC-081 — Mohen So"),
    Regra("STT-A07", ("tirtankaras",), "Tirthankaras", "RC-397 — Tirthankaras"),
    Regra("STT-A08", ("tote", "toth"), "Thoth", "RC-463/RC-534 — Thoth"),
)

# Censo do primeiro lote. Se uma fonte recebida for alterada antes de uma nova
# execução, o desvio é explícito no relatório em vez de passar despercebido.
CENSO_ESPERADO = {
    "STT-A01": 6,
    "STT-A02": 9,
    "STT-A03": 20,
    "STT-A04": 4,
    "STT-A05": 4,
    "STT-A06": 5,
    "STT-A07": 1,
    "STT-A08": 3,
}
N_AMOSTRAS_ESPERADO = 6


@dataclass(frozen=True)
class Mudanca:
    arquivo: str
    linha: int
    regra: str
    antes: str
    depois: str
    trecho_antes: str
    trecho_depois: str


def sha256_bytes(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def escapar_celula(texto: str) -> str:
    """Torna um trecho seguro e legível para uma célula Markdown."""
    return " ".join(texto.replace("|", "\\|").split())


def trecho(texto: str, inicio: int, fim: int, substituicao: str | None = None) -> str:
    """Janela compacta de contexto, sem alterar o texto da cópia derivada."""
    raio = 82
    a = max(0, inicio - raio)
    b = min(len(texto), fim + raio)
    bruto = texto[a:b]
    if substituicao is not None:
        bruto = texto[a:inicio] + substituicao + texto[fim:b]
    prefixo = "…" if a else ""
    sufixo = "…" if b < len(texto) else ""
    return prefixo + escapar_celula(bruto) + sufixo


def aplicar_regras(nome: str, texto: str) -> tuple[str, list[Mudanca]]:
    """Aplica somente as regras fechadas, preservando quebras/bytes alheios."""
    atual = texto
    mudancas: list[Mudanca] = []

    for regra in REGRAS:
        padrao = regra.padrao
        origem = atual
        locais: list[Mudanca] = []

        def substituir(casamento: re.Match[str]) -> str:
            antes = casamento.group(0)
            linha = origem.count("\n", 0, casamento.start()) + 1
            locais.append(
                Mudanca(
                    arquivo=nome,
                    linha=linha,
                    regra=regra.identificador,
                    antes=antes,
                    depois=regra.destino,
                    trecho_antes=trecho(origem, casamento.start(), casamento.end()),
                    trecho_depois=trecho(
                        origem, casamento.start(), casamento.end(), regra.destino
                    ),
                )
            )
            return regra.destino

        atual = padrao.sub(substituir, origem)
        mudancas.extend(locais)

    # Um segundo passe deve ser nulo: garante que os destinos não acionem
    # outras regras e que o dry-run seja idempotente no seu próprio produto.
    for regra in REGRAS:
        if regra.padrao.search(atual):
            raise RuntimeError(
                f"A saída de {nome} ainda casa a regra {regra.identificador}; "
                "normalização não idempotente."
            )
    return atual, mudancas


def obter_arquivos_entrada() -> list[Path]:
    arquivos = sorted(p for p in ENTRADA.glob("*.md") if p.name != "README.md")
    if len(arquivos) != N_AMOSTRAS_ESPERADO:
        raise RuntimeError(
            f"Esperadas {N_AMOSTRAS_ESPERADO} amostras Markdown em {ENTRADA.relative_to(RAIZ)}/; "
            f"encontradas {len(arquivos)}. O conjunto mudou: revise a tabela antes de rodar."
        )
    return arquivos


def montar_readme(saida: Path, arquivos: list[Path], totais: Counter[str]) -> str:
    regras = "\n".join(
        f"- `{regra.identificador}`: `{'` / `'.join(regra.formas)}` → "
        f"**{regra.destino}** ({totais[regra.identificador]} ocorrência(s))"
        for regra in REGRAS
    )
    return f"""# Cópias STT normalizadas — dry-run

> **Gerado por:** `ferramentas/normalizar_stt_dry_run.py`
>
> **Fontes brutas:** `fontes/pilotos_historicos/` (não modificadas)
>
> **Tabela de regras:** `{TABELA}`

Este diretório contém cópias derivadas, não verbatim bruto. Foram aplicadas
somente as oito regras classificadas como **AUTOMÁTICA** na tabela, sempre com
fronteira de palavra. Nenhuma regra `AUTOMÁTICA-CONTEXTO`, `REVISAR` ou
`PRESERVAR / PENDENTE` foi executada.

## Regras executadas

{regras}

## Conteúdo

- {len(arquivos)} cópias Markdown, uma por transcrição bruta;
- relatório detalhado em `{RELATORIO_PADRAO.relative_to(RAIZ)}`;
- nenhuma alteração nos arquivos sob `fontes/pilotos_historicos/`.
"""


def montar_relatorio(
    arquivos: list[Path],
    resultados: dict[str, dict[str, object]],
    mudancas: list[Mudanca],
) -> str:
    totais = Counter(m.regra for m in mudancas)
    por_arquivo: dict[str, list[Mudanca]] = defaultdict(list)
    for mudanca in mudancas:
        por_arquivo[mudanca.arquivo].append(mudanca)

    regras_md = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | "
        f"**{regra.destino}** | {totais[regra.identificador]} | {regra.ancora} |"
        for regra in REGRAS
    )
    resumo_arquivos = "\n".join(
        f"| `{arquivo.name}` | {len(resultados[arquivo.name]['original'].splitlines())} | "
        f"{resultados[arquivo.name]['sha_origem']} | {resultados[arquivo.name]['sha_saida']} | "
        f"{len(por_arquivo[arquivo.name])} |"
        for arquivo in arquivos
    )
    detalhes = []
    for arquivo in arquivos:
        linhas = por_arquivo[arquivo.name]
        detalhes.append(f"### `{arquivo.name}` — {len(linhas)} mudança(s)\n")
        if not linhas:
            detalhes.append("Nenhuma regra automática incidiu neste arquivo.\n")
            continue
        detalhes.append(
            "| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |\n"
            "|---:|---|---|---|---|---|\n"
        )
        for m in linhas:
            detalhes.append(
                f"| {m.linha} | `{m.regra}` | `{m.antes}` | **{m.depois}** | "
                f"{m.trecho_antes} | {m.trecho_depois} |\n"
            )
        detalhes.append("\n")

    censo_real = {regra.identificador: totais[regra.identificador] for regra in REGRAS}
    estado_censo = "OK — coincide com o censo da tabela inicial (52 ocorrências)."
    if censo_real != CENSO_ESPERADO:
        estado_censo = (
            "ATENÇÃO — o censo difere do esperado; revisar fontes/regras antes de usar "
            "este resultado como referência."
        )

    return f"""# Relatório de normalização STT — dry-run

**Data de geração:** 20/10/2026

**Executor:** `ferramentas/normalizar_stt_dry_run.py`

**Tabela aplicada:** `{TABELA}`

**Modo:** cópia derivada; **0 arquivos brutos alterados**.

## Escopo e guarda

Foram lidas as seis amostras Markdown de `fontes/pilotos_historicos/` e escritas cópias
em `normalizados_stt_dry_run/`. O processo usa apenas as oito regras
**AUTOMÁTICA** da seção 2.1 da tabela. Ele não aplica `Sophia` por contexto,
nem qualquer item de `REVISAR` ou `PRESERVAR / PENDENTE`.

- fontes brutas: **{len(arquivos)}**;
- cópias derivadas: **{len(arquivos)}**;
- substituições: **{len(mudancas)}**;
- alteração em `fontes/pilotos_historicos/`: **0**;
- idempotência das cópias geradas: **conferida**.

## Censo por regra

| Regra | DE | PARA | Ocorrências | Âncora oficial |
|---|---|---|---:|---|
{regras_md}

**Censo:** {estado_censo}

## Manifesto de arquivos

| Fonte bruta | Linhas | SHA-256 original | SHA-256 cópia | Mudanças |
|---|---:|---|---|---:|
{resumo_arquivos}

Os SHA-256 são deliberadamente diferentes quando a cópia recebeu uma troca; a
proveniência fica verificável pelo diff e pelas linhas abaixo.

## Registro `antes → depois`

{''.join(detalhes)}

## Limites deste resultado

- A cópia normalizada não substitui nem corrige o bruto STT.
- O relatório não afirma cotejo com áudio; ele registra a aplicação de um
  vocabulário já ancorado na Base.
- Qualquer ampliação de regra deve primeiro entrar na tabela de normalização,
  com regime e evidência próprios.
"""


def escrever_novo(caminho: Path, conteudo: bytes, force: bool) -> None:
    if caminho.exists() and not force:
        raise FileExistsError(
            f"Saída já existe: {caminho.relative_to(RAIZ)}. "
            "Use --force apenas para regenerar o produto derivado."
        )
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_bytes(conteudo)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="permite reescrever somente as cópias e o relatório derivados",
    )
    args = parser.parse_args()

    arquivos = obter_arquivos_entrada()
    if SAIDA_PADRAO.resolve() == ENTRADA.resolve():
        raise RuntimeError("Saída não pode coincidir com fontes/pilotos_historicos/.")
    if SAIDA_PADRAO.exists() and not args.force:
        raise FileExistsError(
            f"Diretório de saída já existe: {SAIDA_PADRAO.relative_to(RAIZ)}/. "
            "Use --force para regenerar apenas artefatos derivados."
        )

    # Leitura integral antes de qualquer escrita: evita produzir um lote parcial.
    origens: dict[str, bytes] = {arquivo.name: arquivo.read_bytes() for arquivo in arquivos}
    resultados: dict[str, dict[str, object]] = {}
    todas_mudancas: list[Mudanca] = []

    for arquivo in arquivos:
        bruto = origens[arquivo.name]
        try:
            texto = bruto.decode("utf-8")
        except UnicodeDecodeError as erro:
            raise RuntimeError(f"{arquivo.name} não é UTF-8: {erro}") from erro
        normalizado, mudancas = aplicar_regras(arquivo.name, texto)
        resultados[arquivo.name] = {
            "original": texto,
            "normalizado": normalizado,
            "sha_origem": sha256_bytes(bruto),
            "sha_saida": sha256_bytes(normalizado.encode("utf-8")),
        }
        todas_mudancas.extend(mudancas)

    totais = Counter(m.regra for m in todas_mudancas)
    censo_real = {regra.identificador: totais[regra.identificador] for regra in REGRAS}
    if censo_real != CENSO_ESPERADO:
        raise RuntimeError(
            "Censo das regras diverge do lote de referência: "
            f"esperado {CENSO_ESPERADO}; obtido {censo_real}."
        )

    # O único diretório que --force pode limpar é o derivado com nome fechado.
    if SAIDA_PADRAO.exists() and args.force:
        shutil.rmtree(SAIDA_PADRAO)
    SAIDA_PADRAO.mkdir(parents=True, exist_ok=False)

    for arquivo in arquivos:
        destino = SAIDA_PADRAO / arquivo.name
        destino.write_text(str(resultados[arquivo.name]["normalizado"]), encoding="utf-8", newline="")

    readme = montar_readme(SAIDA_PADRAO, arquivos, totais)
    (SAIDA_PADRAO / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    relatorio = montar_relatorio(arquivos, resultados, todas_mudancas)
    escrever_novo(RELATORIO_PADRAO, relatorio.encode("utf-8"), args.force)

    # Verificação posterior: os bytes da entrada devem permanecer idênticos.
    for arquivo in arquivos:
        if arquivo.read_bytes() != origens[arquivo.name]:
            raise RuntimeError(f"Violação: a fonte bruta foi alterada: {arquivo.name}")

    print(
        "OK — dry-run concluído: "
        f"{len(arquivos)} cópias · {len(todas_mudancas)} substituições · "
        f"0 fontes alteradas · relatório {RELATORIO_PADRAO.relative_to(RAIZ)}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, RuntimeError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        raise SystemExit(2)
