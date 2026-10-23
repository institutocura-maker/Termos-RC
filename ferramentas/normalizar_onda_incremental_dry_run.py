#!/usr/bin/env python3
"""Inventa e normaliza, com proveniência fechada, os seis brutos do piloto STT.

A onda ``onda_incremental_dry_run`` é independente do piloto histórico:
ela lê exclusivamente os seis brutos de ``uploads_recepcao/`` e escreve todos
os seus produtos em ``onda_incremental_dry_run/``. Nunca lê, altera, reutiliza
ou remove produtos em ``normalizados_stt_dry_run/``.

O executor aplica somente as oito regras lexicais AUTOMÁTICA já homologadas na
tabela de normalização. YAML/frontmatter e URLs são preservados byte a byte;
regras contextuais, itens para revisão e formas bloqueadas não são aplicados.

Uso:
    python3 ferramentas/normalizar_onda_incremental_dry_run.py
    python3 ferramentas/normalizar_onda_incremental_dry_run.py --force

``--force`` só pode recriar a árvore derivada de nome fechado desta onda.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from caminhos_acervo import caminho_atual


RAIZ = Path(__file__).resolve().parent.parent
ONDA = "onda_incremental_dry_run"
ENTRADA = caminho_atual("fonte.recepcao")
SAIDA = RAIZ / ONDA
DERIVADOS = SAIDA / "derivados_normalizados"
TABELA_REGRAS = "diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md"
EXECUTOR = "ferramentas/normalizar_onda_incremental_dry_run.py"

# A seleção e os hashes travam explicitamente o lote que serviu ao piloto.
# Uma recepção futura em uploads_recepcao/ não pode entrar nesta onda por acaso;
# tampouco um bruto alterado pode fingir continuidade com o experimento inicial.
PILOTO_FONTES: dict[str, str] = {
    "2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md": "335a1b24cdcad1adb707e585c617a50dd277f550310abbbb35c328cf00d33134",
    "2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md": "d501d087d9113c91ee1cdf21b2ec7c1514252bc0acf69bf5881e988405f274fb",
    "2025-07_002_lS8Bw-eaFYQ_A_Falencia_dos_Deuses_e_a_Destinacao_do_Lobo_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md": "260115a68f01c5c5d7a7669b8756624d0f0c74af28a47f42b998d6a67ba5b812",
    "2025-07_035_JDaxXjYGyu0_Direitos_e_Deveres_Espirituais_VSC_10.md": "4d6b32ef39504d28291d2e73f458c4af5a7fceaa220a74f037b11092dd4ca649",
    "2025-09_029_SzZtXArSltg_O_Quarto_Caminho_de_Gurdjieff_VSC_16.md": "8656437f5b36dbb7e12b947584dacb8690d0d96415cfd6312fe87b8825fb3246",
    "2026-02_019_E2fBs7aocgU_O_Grande_Caminho_VSC_26.md": "9d7e52325e556d5508f930ac4be32967bd3acbf9bfec1ed82f7c3892a323c33f",
}


@dataclass(frozen=True)
class Regra:
    identificador: str
    formas: tuple[str, ...]
    destino: str
    ancora: str

    @property
    def padrao(self) -> re.Pattern[str]:
        alternativas = "|".join(
            re.escape(forma) for forma in sorted(self.formas, key=len, reverse=True)
        )
        return re.compile(rf"(?<!\w)(?:{alternativas})(?!\w)", re.IGNORECASE)


# Seção 2.1 da tabela: somente equivalências lexicais já automáticas no piloto.
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

# URL é dado de proveniência, nunca uma região de normalização. O padrão cobre
# links autônomos e o destino de links Markdown, sem inferir texto de âncora.
URL = re.compile(r"https?://[^\s)>]+", re.IGNORECASE)
FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n.*?^---[ \t]*(?:\r?\n|\Z)", re.DOTALL | re.MULTILINE)
METADADO = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*[\"']?([^\"'\r\n]+)", re.MULTILINE)


@dataclass(frozen=True)
class Evento:
    arquivo: str
    sha256_fonte: str
    linha: int
    coluna: int
    # Ambos os offsets são baseados em caracteres Unicode da fonte original.
    # O do corpo permite reconstruir o produto; o absoluto documenta a posição
    # inequívoca na fonte Markdown completa, inclusive o frontmatter.
    offset_corpo_caractere: int
    offset_fonte_caractere: int
    regra: str
    antes: str
    depois: str
    ancora: str
    contexto_antes: str
    contexto_depois: str


def sha256(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def data_geracao() -> str:
    # O repositório usa a data local do Curador para todos os relatórios da onda.
    return datetime.now().astimezone().date().isoformat()


def escapar_tabela(texto: str) -> str:
    return " ".join(texto.replace("|", "\\|").split())


def contexto(texto: str, inicio: int, fim: int, troca: str | None = None) -> str:
    raio = 82
    a, b = max(0, inicio - raio), min(len(texto), fim + raio)
    recorte = texto[a:b]
    if troca is not None:
        recorte = texto[a:inicio] + troca + texto[fim:b]
    return ("…" if a else "") + escapar_tabela(recorte) + ("…" if b < len(texto) else "")


def extrair_frontmatter(texto: str, nome: str) -> tuple[str, str]:
    encontrado = FRONTMATTER.match(texto)
    if not encontrado:
        raise RuntimeError(f"{nome}: frontmatter YAML delimitado por --- não encontrado")
    return texto[: encontrado.end()], texto[encontrado.end() :]


def obter_fontes() -> list[Path]:
    encontradas = sorted(p for p in ENTRADA.glob("*.md") if p.name != "README.md")
    nomes = [p.name for p in encontradas]
    esperadas = sorted(PILOTO_FONTES)
    if nomes != esperadas:
        faltantes = sorted(set(esperadas) - set(nomes))
        extras = sorted(set(nomes) - set(esperadas))
        raise RuntimeError(
            "Conjunto de fontes não é exatamente o piloto de seis transcrições; "
            f"faltantes={faltantes or '—'}; extras={extras or '—'}."
        )
    return encontradas


def intervalos_url(texto: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in URL.finditer(texto)]


def protegido(inicio: int, fim: int, intervalos: list[tuple[int, int]]) -> bool:
    return any(inicio < b and fim > a for a, b in intervalos)


def localizar_eventos(
    nome: str, sha_fonte: str, corpo: str, linha_base: int, caracteres_frontmatter: int
) -> list[Evento]:
    """Localiza no corpo original e monta eventos com posição estável da fonte."""
    urls = intervalos_url(corpo)
    eventos: list[Evento] = []
    for regra in REGRAS:
        for casamento in regra.padrao.finditer(corpo):
            if protegido(casamento.start(), casamento.end(), urls):
                continue
            inicio, fim = casamento.span()
            eventos.append(
                Evento(
                    arquivo=nome,
                    sha256_fonte=sha_fonte,
                    linha=linha_base + corpo.count("\n", 0, inicio) + 1,
                    coluna=inicio - (corpo.rfind("\n", 0, inicio) + 1) + 1,
                    offset_corpo_caractere=inicio,
                    offset_fonte_caractere=caracteres_frontmatter + inicio,
                    regra=regra.identificador,
                    antes=casamento.group(0),
                    depois=regra.destino,
                    ancora=regra.ancora,
                    contexto_antes=contexto(corpo, inicio, fim),
                    contexto_depois=contexto(corpo, inicio, fim, regra.destino),
                )
            )
    eventos.sort(key=lambda item: item.offset_corpo_caractere)
    for anterior, seguinte in zip(eventos, eventos[1:]):
        if (
            anterior.offset_corpo_caractere + len(anterior.antes)
            > seguinte.offset_corpo_caractere
        ):
            raise RuntimeError(f"{nome}: regras concorrentes sobre a mesma faixa de texto")
    return eventos


def aplicar_eventos(corpo: str, eventos: list[Evento]) -> str:
    partes: list[str] = []
    cursor = 0
    for evento in eventos:
        inicio = evento.offset_corpo_caractere
        fim = inicio + len(evento.antes)
        if corpo[inicio:fim] != evento.antes:
            raise RuntimeError(f"{evento.arquivo}: rastreio não corresponde ao corpo fonte")
        partes.extend((corpo[cursor:inicio], evento.depois))
        cursor = fim
    partes.append(corpo[cursor:])
    return "".join(partes)


def normalizar(nome: str, bruto: bytes) -> tuple[bytes, list[Evento], dict[str, str]]:
    try:
        texto = bruto.decode("utf-8")
    except UnicodeDecodeError as erro:
        raise RuntimeError(f"{nome}: fonte não UTF-8 ({erro})") from erro
    frontmatter, corpo = extrair_frontmatter(texto, nome)
    sha_fonte = sha256(bruto)
    if sha_fonte != PILOTO_FONTES[nome]:
        raise RuntimeError(
            f"{nome}: SHA-256 não corresponde ao bruto usado no piloto; "
            f"esperado {PILOTO_FONTES[nome]}, obtido {sha_fonte}."
        )
    eventos = localizar_eventos(
        nome, sha_fonte, corpo, frontmatter.count("\n"), len(frontmatter)
    )
    derivado = (frontmatter + aplicar_eventos(corpo, eventos)).encode("utf-8")

    # Invariantes de isolamento e idempotência: metadados inteiros ficam idênticos
    # e um segundo passe não pode sugerir qualquer alteração adicional.
    if not derivado.startswith(frontmatter.encode("utf-8")):
        raise RuntimeError(f"{nome}: violação do frontmatter imutável")
    texto_derivado = derivado.decode("utf-8")
    frontmatter_2, corpo_2 = extrair_frontmatter(texto_derivado, nome)
    if frontmatter_2 != frontmatter:
        raise RuntimeError(f"{nome}: frontmatter foi alterado")
    if URL.findall(texto) != URL.findall(texto_derivado):
        raise RuntimeError(f"{nome}: URL foi alterada")
    if localizar_eventos(
        nome, sha_fonte, corpo_2, frontmatter.count("\n"), len(frontmatter)
    ):
        raise RuntimeError(f"{nome}: produto não é idempotente")

    campos = {chave: valor.strip() for chave, valor in METADADO.findall(frontmatter)}
    return derivado, eventos, campos


def inventario_md(resultados: list[dict[str, object]], gerado_em: str) -> str:
    linhas = []
    for indice, item in enumerate(resultados, 1):
        meta = item["metadados"]
        linhas.append(
            f"| P{indice} | `{item['arquivo']}` | `{meta.get('id_youtube', '—')}` | "
            f"{meta.get('data_publicacao_original', '—')} | {meta.get('duracao', '—')} | "
            f"{item['linhas']} | {item['bytes_fonte']} | `{item['sha256_fonte']}` |"
        )
    return f"""# Inventário de fontes — {ONDA}

**Gerado em:** {gerado_em}
**Executor:** `{EXECUTOR}`
**Natureza:** inventário imutável dos seis brutos que compuseram o piloto STT.

## Escopo fechado

Foram aceitos exclusivamente os seis arquivos Markdown listados abaixo, todos
em `uploads_recepcao/`. Cada SHA-256 foi confrontado com a identidade registrada
para o piloto. A presença de qualquer outro `.md`, ausência de um destes ou
alteração de um único byte faz o executor abortar antes de produzir derivados.

| ID | Arquivo bruto | YouTube | Publicação | Duração | Linhas | Bytes | SHA-256 bruto |
|---|---|---|---|---|---:|---:|---|
{chr(10).join(linhas)}

## Garantias deste inventário

- brutos lidos: **{len(resultados)}**;
- hashes do piloto confirmados: **{len(resultados)}/{len(resultados)}**;
- arquivos sob `uploads_recepcao/` alterados pela execução: **0**;
- o inventário JSON estruturado equivalente é `manifesto-fontes.json`;
- este diretório não utiliza nem modifica `normalizados_stt_dry_run/`.
"""


def readme(totais: Counter[str], n_eventos: int, gerado_em: str) -> str:
    regras = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | **{regra.destino}** | "
        f"{totais[regra.identificador]} | {regra.ancora} |"
        for regra in REGRAS
    )
    return f"""# {ONDA}

**Iniciada em:** {gerado_em}
**Estado:** normalização concluída; aguardando o mapeamento dos eixos temáticos.

Esta é uma área de processamento exclusivamente derivada dos seis brutos do
piloto STT. Ela é fisicamente separada de `normalizados_stt_dry_run/` e não
altera nenhuma fonte em `uploads_recepcao/`.

## Produtos

| Caminho | Conteúdo |
|---|---|
| `INVENTARIO-FONTES.md` | inventário humano dos seis brutos, IDs e hashes confirmados |
| `manifesto-fontes.json` | proveniência estruturada das fontes de entrada |
| `derivados_normalizados/` | as seis cópias normalizadas; não são brutos |
| `manifesto-derivados.json` | hashes de saída, hash de origem e quantidade de trocas por derivado |
| `rastreio-antes-depois.jsonl` | cada substituição com regra, posição e contexto da fonte |
| `RELATORIO-NORMALIZACAO.md` | confirmação humana, censo e limites do processamento |

## Regras executadas

Somente as oito regras `AUTOMÁTICA` da seção 2.1 de
`{TABELA_REGRAS}` foram aplicadas ao corpo Markdown. Frontmatter YAML e URLs
foram mantidos byte a byte; regras contextuais, itens em revisão e formas
preservadas ficaram fora desta execução.

| Regra | DE | PARA | Trocas | Âncora canônica |
|---|---|---|---:|---|
{regras}

**Total:** {n_eventos} substituições, em 6 derivados.
**Idempotência:** verificada.
**Alterações nos brutos:** 0.
"""


def relatorio(resultados: list[dict[str, object]], eventos: list[Evento], gerado_em: str) -> str:
    totais = Counter(evento.regra for evento in eventos)
    linhas_regras = "\n".join(
        f"| `{regra.identificador}` | `{'` / `'.join(regra.formas)}` | **{regra.destino}** | "
        f"{totais[regra.identificador]} | {regra.ancora} |"
        for regra in REGRAS
    )
    linhas_fontes = "\n".join(
        f"| `{item['arquivo']}` | {item['mudancas']} | `{item['sha256_fonte']}` | `{item['sha256_derivado']}` |"
        for item in resultados
    )
    amostra = "\n".join(
        f"| `{evento.arquivo}` | {evento.linha}:{evento.coluna} | `{evento.regra}` | "
        f"`{evento.antes}` | **{evento.depois}** |"
        for evento in eventos[:20]
    )
    return f"""# Relatório de normalização — {ONDA}

**Data de geração:** {gerado_em}
**Executor:** `{EXECUTOR}`
**Entrada:** `uploads_recepcao/` (os seis brutos selados do piloto)
**Saída exclusiva:** `{ONDA}/`

> **CONFIRMADO — normalização concluída com proveniência limpa.**
> Foram lidas seis fontes previamente inventariadas, escritas seis cópias
> derivadas e preservadas integralmente as fontes brutas.

## Resultado

| Verificação | Resultado |
|---|---:|
| Fontes brutas inventariadas | 6 |
| Hashes do piloto confirmados | 6/6 |
| Derivados normalizados escritos | 6 |
| Substituições rastreadas | {len(eventos)} |
| Regras contextuais executadas | 0 |
| Itens de revisão/preservação executados | 0 |
| Alterações em `uploads_recepcao/` | **0** |
| Frontmatters preservados byte a byte | **6/6** |
| URLs preservadas | **6/6** |
| Idempotência do produto | **6/6** |
| Uso ou escrita em `normalizados_stt_dry_run/` | **0** |

## Censo das regras autorizadas

| Regra | DE | PARA | Trocas | Âncora canônica |
|---|---|---|---:|---|
{linhas_regras}

O censo de **{len(eventos)}** coincide com a linha de base do piloto (52). Nenhuma
regra foi ampliada, nem foi inferida a partir de semelhança fonética.

## Manifesto de proveniência

| Derivado | Trocas | SHA-256 bruto | SHA-256 derivado |
|---|---:|---|---|
{linhas_fontes}

Cada linha de `rastreio-antes-depois.jsonl` carrega o SHA da fonte, a posição
original (linha, coluna e offset), a regra, a âncora canônica e os contextos
antes/depois. Assim, a cópia derivada é auditável sem consultar o diretório
histórico de testes.

## Amostra do rastreio

| Arquivo | Posição no bruto | Regra | Antes | Depois |
|---|---|---|---|---|
{amostra}

## Limites vigentes antes do mapeamento temático

- Este resultado não é um cotejo com áudio e não altera o bruto STT.
- Somente as oito regras lexicais automáticas foram usadas.
- Sophia/Sofio por contexto, ambiguidades e itens preservados continuam fora do
  produto, sem decisão implícita.
- Não foram criados termos, relações, fichas, candidatos ou eixos.

**Próximo portão:** mapeamento dos eixos temáticos a partir destes derivados,
mediante orientação do Curador.
"""


def escrever_json(caminho: Path, objeto: object) -> None:
    caminho.write_text(json.dumps(objeto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def escrever_jsonl(caminho: Path, itens: Iterable[Evento]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as destino:
        for item in itens:
            destino.write(json.dumps(asdict(item), ensure_ascii=False, sort_keys=True) + "\n")


def preparar_saida(force: bool) -> None:
    if SAIDA.resolve() == ENTRADA.resolve() or ENTRADA.resolve() in SAIDA.resolve().parents:
        raise RuntimeError("A saída da onda não pode coincidir com a árvore das fontes")
    if SAIDA.exists():
        if not force:
            raise FileExistsError(
                f"A onda já existe em {ONDA}/. Use --force apenas para recriar seus derivados."
            )
        shutil.rmtree(SAIDA)
    SAIDA.mkdir(parents=True, exist_ok=False)
    DERIVADOS.mkdir(parents=False, exist_ok=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help=f"recria somente {ONDA}/; nunca toca fontes ou o diretório do piloto",
    )
    args = parser.parse_args()

    fontes = obter_fontes()
    # Captura todos os bytes antes de qualquer escrita, impedindo produto parcial.
    brutos = {fonte.name: fonte.read_bytes() for fonte in fontes}
    resultados: list[dict[str, object]] = []
    eventos: list[Evento] = []
    for fonte in fontes:
        derivado, eventos_fonte, metadados = normalizar(fonte.name, brutos[fonte.name])
        eventos.extend(eventos_fonte)
        resultados.append(
            {
                "arquivo": fonte.name,
                "caminho_fonte": str(fonte.relative_to(RAIZ)),
                "caminho_derivado": str((DERIVADOS / fonte.name).relative_to(RAIZ)),
                "bytes_fonte": len(brutos[fonte.name]),
                "bytes_derivado": len(derivado),
                "linhas": brutos[fonte.name].count(b"\n") + (0 if brutos[fonte.name].endswith(b"\n") else 1),
                "sha256_fonte": sha256(brutos[fonte.name]),
                "sha256_derivado": sha256(derivado),
                "mudancas": len(eventos_fonte),
                "metadados": metadados,
                "_conteudo_derivado": derivado,
            }
        )

    totais = Counter(evento.regra for evento in eventos)
    censo_real = {regra.identificador: totais[regra.identificador] for regra in REGRAS}
    if censo_real != CENSO_ESPERADO:
        raise RuntimeError(
            f"Censo de normalização diverge da base selada: esperado {CENSO_ESPERADO}; obtido {censo_real}."
        )

    gerado_em = data_geracao()
    preparar_saida(args.force)
    for item in resultados:
        (DERIVADOS / str(item["arquivo"])).write_bytes(bytes(item.pop("_conteudo_derivado")))

    manifesto_fontes = {
        "onda": ONDA,
        "gerado_em": gerado_em,
        "executor": EXECUTOR,
        "origem": "uploads_recepcao/",
        "escopo": "seis transcrições brutas seladas do piloto STT",
        "fontes": [
            {k: v for k, v in item.items() if k not in {"caminho_derivado", "bytes_derivado", "sha256_derivado", "mudancas"}}
            for item in resultados
        ],
    }
    manifesto_derivados = {
        "onda": ONDA,
        "gerado_em": gerado_em,
        "executor": EXECUTOR,
        "regras": [
            {
                "id": regra.identificador,
                "formas": list(regra.formas),
                "destino": regra.destino,
                "ancora": regra.ancora,
                "trocas": totais[regra.identificador],
            }
            for regra in REGRAS
        ],
        "derivados": [
            {
                k: v
                for k, v in item.items()
                if k not in {"metadados", "caminho_fonte", "bytes_fonte", "linhas"}
            }
            for item in resultados
        ],
    }
    escrever_json(SAIDA / "manifesto-fontes.json", manifesto_fontes)
    escrever_json(SAIDA / "manifesto-derivados.json", manifesto_derivados)
    escrever_jsonl(SAIDA / "rastreio-antes-depois.jsonl", eventos)
    (SAIDA / "INVENTARIO-FONTES.md").write_text(
        inventario_md(resultados, gerado_em), encoding="utf-8", newline="\n"
    )
    (SAIDA / "RELATORIO-NORMALIZACAO.md").write_text(
        relatorio(resultados, eventos, gerado_em), encoding="utf-8", newline="\n"
    )
    (SAIDA / "README.md").write_text(
        readme(totais, len(eventos), gerado_em), encoding="utf-8", newline="\n"
    )

    # Verificação decisiva depois de toda a escrita: cada bruto deve continuar
    # idêntico ao buffer lido antes do processamento e ao SHA do piloto.
    for fonte in fontes:
        atual = fonte.read_bytes()
        if atual != brutos[fonte.name] or sha256(atual) != PILOTO_FONTES[fonte.name]:
            raise RuntimeError(f"Violação de integridade da fonte: {fonte.name}")

    print(
        "OK — onda_incremental_dry_run concluída: "
        f"6 fontes inventariadas · 6 derivados · {len(eventos)} substituições · "
        "6/6 hashes do piloto · 0 brutos alterados · idempotência OK"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, RuntimeError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        raise SystemExit(2)
