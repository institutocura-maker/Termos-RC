#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 0 — mapa de ingresso e triagem do lote STT normalizado de 2026-10.

Este programa prepara a fila de produção, mas não a dispara. Sua entrada de
produção são EXCLUSIVAMENTE as cópias em ``normalizados_stt_lote_2026-10/``.
Os SHA-256 dos STT brutos são lidos apenas dos manifestos selados pela etapa de
normalização: nenhum conteúdo em ``uploads_recepcao/`` é aberto, indexado ou
usado para buscar citações.

Produtos (todos derivados):
  ingestao_stt_lote_2026-10/registro-mestre.jsonl
  ingestao_stt_lote_2026-10/mapa-linhas.jsonl
  ingestao_stt_lote_2026-10/indice-termos-base.jsonl
  ingestao_stt_lote_2026-10/mapa-tematico.jsonl
  ingestao_stt_lote_2026-10/lotes-planejados.json
  ingestao_stt_lote_2026-10/resumo-triagem.json
  diagnostico/MAPA-CONSOLIDADO-LINHA-PRODUCAO-STT-LOTE-2026-10-20.md

Uso:
  python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py
  python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --force
  python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --buscar Sophia

A Fase 0 jamais cria ciclos, fichas, termos, relações, apostilas ou alterações
em ``dados_termos.py``. Uma ocorrência é somente um *sinal de busca* de uma
grafia já existente na Base; não prova conceito, não é citação e não promove
candidato algum.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "normalizados_stt_lote_2026-10"
SAIDA = RAIZ / "ingestao_stt_lote_2026-10"
RELATORIO = RAIZ / "diagnostico" / "MAPA-CONSOLIDADO-LINHA-PRODUCAO-STT-LOTE-2026-10-20.md"
MANIFESTO_FONTES = ENTRADA / "manifesto-fontes-sha256.tsv"
MANIFESTO_DERIVADOS = ENTRADA / "manifesto-derivados-sha256.tsv"
RASTREIO = ENTRADA / "rastreio-antes-depois.jsonl"
DADOS_TERMOS = RAIZ / "ferramentas" / "dados_termos.py"

N_FONTES_ESPERADO = 309
META_HORAS_LOTE = 11.0
TETO_HORAS_LOTE = 12.0
MAX_CANDIDATOS_POR_LOTE = 25
DATA_GERACAO = "2026-10-20"

# Taxonomia de triagem, não taxonomia da Base. São apenas sinais para ordenar a
# leitura humana; fontes multicamadas podem aparecer em vários eixos, mas recebem
# uma fila primária determinística para não duplicá-las na capacidade de produção.
TEMAS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "COSMOGONIA_CRIADOR",
        "Cosmogonia, Criador e queda",
        (
            "criador", "criação", "cosmogonia", "javé", "brahma", "brajna",
            "prajapati", "holograma", "antimaterial", "brahmaloka",
        ),
    ),
    (
        "REINTEGRACAO_CRISTO",
        "Reintegração, Sophia e eixo crístico",
        (
            "sophia", "cristo", "jesus", "reintegração", "avatar", "messias",
            "segunda vinda", "crístico",
        ),
    ),
    (
        "ANUNNAKI_GENETICA",
        "Anunnaki, genética e humanidade",
        (
            "anunnaki", "enki", "enlil", "ninhursag", "ninmah", "foxp2", "genoma",
            "genética", "dna", "sapiens", "biodemo",
        ),
    ),
    (
        "ATLANTIDA_CIVILIZACOES",
        "Atlântida, Marte e civilizações antigas",
        (
            "atlântida", "terra atlantis", "marte", "dilúvio", "lemúria", "egito",
            "maias", "astecas", "incas", "arqueologia", "pirâmide",
        ),
    ),
    (
        "MITOLOGIAS_ORIENTAIS",
        "Mitologias orientais e tradições antigas",
        (
            "vishnu", "shiva", "trimurti", "krishna", "mahabharata", "ramayana",
            "buda", "hindu", "ved", "yoga", "ayodhya",
        ),
    ),
    (
        "MEDIUNIDADE_ESPIRITUALIDADE",
        "Mediunidade, espíritos e psiquismo",
        (
            "mediunidade", "mediúnic", "espírito", "psiqu", "obsessor", "psicografia",
            "desencarn", "egregora", "vibraç",
        ),
    ),
    (
        "MORTE_REENCARNACAO_ETICA",
        "Morte, reencarnação e ética evolutiva",
        (
            "reencarna", "karma", "carma", "morte", "encarna", "pecado", "inferno",
            "paraíso", "evolução", "destino",
        ),
    ),
    (
        "EXTRATERRESTRES_TECNOLOGIA",
        "Extraterrestres, tecnologia e cosmos",
        (
            "extraterrest", "alienígen", "nave", "ufologia", "inteligência artificial",
            "transuman", "quântic", "planeta", "galáxia",
        ),
    ),
    (
        "SOCIEDADE_CONTEMPORANEA",
        "Sociedade, comportamento e atualidades",
        (
            "política", "brasil", "governo", "geração", "família", "infância", "corpo",
            "saúde", "pandemia", "escola",
        ),
    ),
)

# Não são bons descritores de um conceito para busca automática. A exclusão não
# apaga a palavra da transcrição, apenas impede que ela infle o ranking curatorial.
ALIAS_COMUNS = {
    "alma", "amor", "bem", "caos", "corpo", "deus", "dor", "ego", "espírito",
    "fé", "fim", "força", "forma", "homem", "humano", "luz", "mãe", "mente",
    "morte", "mundo", "natureza", "pai", "pecado", "pessoa", "povo", "tempo",
    "terra", "universo", "vida", "verdade", "vontade",
}

# Famílias de capacidade para não deixar caudas artificiais de 1–5 horas.
# Cada família é semanticamente explicitada no relatório e mantém os eixos de
# origem no JSON do lote; ela não é uma classificação ou relação nova da Base.
FAMILIAS_DE_LOTE: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("ANUNNAKI_GENETICA", "Anunnaki, genética e humanidade", ("ANUNNAKI_GENETICA",)),
    (
        "COSMOGONIA_HISTORIA_COSMICA",
        "Cosmogonia, quedas e história cósmica",
        ("COSMOGONIA_CRIADOR", "ATLANTIDA_CIVILIZACOES"),
    ),
    ("EXTRATERRESTRES_TECNOLOGIA", "Extraterrestres, tecnologia e cosmos", ("EXTRATERRESTRES_TECNOLOGIA",)),
    (
        "EXPERIENCIA_ESPIRITUAL_ETICA",
        "Experiência espiritual, morte e ética evolutiva",
        ("MEDIUNIDADE_ESPIRITUALIDADE", "MORTE_REENCARNACAO_ETICA"),
    ),
    (
        "MITOLOGIAS_REINTEGRACAO",
        "Mitologias, tradições e eixo de reintegração",
        ("MITOLOGIAS_ORIENTAIS", "REINTEGRACAO_CRISTO", "GERAL_SEM_SINAL_FORTE"),
    ),
    ("SOCIEDADE_CONTEMPORANEA", "Sociedade, comportamento e atualidades", ("SOCIEDADE_CONTEMPORANEA",)),
)


class FalhaFase0(RuntimeError):
    """Invariante de entrada quebrada: não há saída parcial aproveitável."""


@dataclass(frozen=True)
class FonteManifestada:
    arquivo: str
    bytes: int
    sha256: str


@dataclass(frozen=True)
class DerivadoManifestado:
    arquivo: str
    bytes: int
    sha256: str
    sha256_fonte: str
    trocas: int


@dataclass(frozen=True)
class TermoBase:
    codigo: str
    nome: str
    categoria: str
    subcategoria: str


@dataclass(frozen=True)
class Documento:
    ingresso_id: str
    arquivo: str
    caminho_derivado: str
    sha256_derivado: str
    sha256_fonte_declarado: str
    bytes: int
    trocas_normalizacao: int
    titulo: str
    data_publicacao_original: str | None
    id_youtube: str | None
    link_original: str | None
    duracao_texto: str | None
    duracao_segundos: int | None
    linha_inicio_corpo: int
    texto: str


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def json_deterministico(objeto: object) -> str:
    return json.dumps(objeto, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def escrever_jsonl(caminho: Path, registros: Iterable[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as fh:
        for registro in registros:
            fh.write(json_deterministico(registro))
            fh.write("\n")


def carregar_tsv_fontes(caminho: Path) -> dict[str, FonteManifestada]:
    if not caminho.is_file():
        raise FalhaFase0(f"Manifesto de fontes ausente: {caminho.relative_to(RAIZ)}")
    with caminho.open("r", encoding="utf-8", newline="") as fh:
        linhas = list(csv.DictReader(fh, delimiter="\t"))
    esperadas = {"arquivo_fonte", "bytes", "sha256_fonte"}
    if not linhas or set(linhas[0]) != esperadas:
        raise FalhaFase0(f"Cabeçalho inesperado em {caminho.name}")
    saida: dict[str, FonteManifestada] = {}
    for linha in linhas:
        nome = linha["arquivo_fonte"]
        if not nome or nome in saida:
            raise FalhaFase0(f"Nome vazio ou duplicado no manifesto de fontes: {nome!r}")
        saida[nome] = FonteManifestada(nome, int(linha["bytes"]), linha["sha256_fonte"])
    return saida


def carregar_tsv_derivados(caminho: Path) -> dict[str, DerivadoManifestado]:
    if not caminho.is_file():
        raise FalhaFase0(f"Manifesto de derivados ausente: {caminho.relative_to(RAIZ)}")
    with caminho.open("r", encoding="utf-8", newline="") as fh:
        linhas = list(csv.DictReader(fh, delimiter="\t"))
    esperadas = {"arquivo_derivado", "bytes_derivado", "sha256_derivado", "sha256_fonte", "trocas"}
    if not linhas or set(linhas[0]) != esperadas:
        raise FalhaFase0(f"Cabeçalho inesperado em {caminho.name}")
    saida: dict[str, DerivadoManifestado] = {}
    for linha in linhas:
        nome = linha["arquivo_derivado"]
        if not nome or nome in saida:
            raise FalhaFase0(f"Nome vazio ou duplicado no manifesto de derivados: {nome!r}")
        saida[nome] = DerivadoManifestado(
            nome,
            int(linha["bytes_derivado"]),
            linha["sha256_derivado"],
            linha["sha256_fonte"],
            int(linha["trocas"]),
        )
    return saida


def contar_rastreio_por_arquivo(caminho: Path) -> Counter[str]:
    if not caminho.is_file():
        raise FalhaFase0(f"Rastreio de normalização ausente: {caminho.relative_to(RAIZ)}")
    contagem: Counter[str] = Counter()
    with caminho.open("r", encoding="utf-8") as fh:
        for n_linha, linha in enumerate(fh, 1):
            try:
                evento = json.loads(linha)
                arquivo = evento["arquivo"]
            except (json.JSONDecodeError, KeyError) as erro:
                raise FalhaFase0(f"{caminho.name}:{n_linha}: JSONL inválido") from erro
            contagem[arquivo] += 1
    return contagem


def separar_frontmatter(texto: str, nome: str) -> tuple[str, str, int]:
    # Aceita CRLF herdado; não reescreve o conteúdo lido.
    encontrado = re.match(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)", texto, re.S | re.M)
    if not encontrado:
        raise FalhaFase0(f"{nome}: frontmatter YAML delimitado por --- ausente")
    frente = encontrado.group(0)
    return frente, texto[encontrado.end():], frente.count("\n") + 1


def valor_yaml_simples(frontmatter: str, chave: str) -> str | None:
    # Metadados de ingresso são escalares de uma linha. Não usamos um parser
    # YAML para não "consertar" nem reserializar o frontmatter herdado. Há um
    # título de origem com aspas duplas internas não escapadas; por isso a aspa
    # externa é retirada somente se também fechar a última posição da linha.
    m = re.search(rf"^{re.escape(chave)}:[ \t]*([^\r\n]*?)[ \t]*\r?$", frontmatter, re.M)
    if not m:
        return None
    valor = m.group(1).strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in {"\"", "'"}:
        valor = valor[1:-1]
    return valor


def parse_duracao(valor: str | None, nome: str) -> int | None:
    if valor is None or not valor.strip():
        return None
    partes = valor.strip().split(":")
    try:
        numeros = [int(p) for p in partes]
    except ValueError as erro:
        raise FalhaFase0(f"{nome}: duração inválida {valor!r}") from erro
    if len(numeros) == 2:
        horas, minutos, segundos = 0, numeros[0], numeros[1]
    elif len(numeros) == 3:
        horas, minutos, segundos = numeros
    else:
        raise FalhaFase0(f"{nome}: duração deve ser MM:SS ou H:MM:SS, não {valor!r}")
    if horas < 0 or not 0 <= minutos < 60 or not 0 <= segundos < 60:
        raise FalhaFase0(f"{nome}: duração fora da faixa {valor!r}")
    return horas * 3600 + minutos * 60 + segundos


def formatar_duracao(segundos: int | None) -> str:
    if segundos is None:
        return "não informada"
    horas, resto = divmod(segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:d}:{minutos:02d}:{segundos:02d}"


def carregar_documentos() -> tuple[list[Documento], dict[str, int], dict[str, str]]:
    """Confere a cadeia manifesto → cópia derivada sem abrir os STT brutos."""
    fontes = carregar_tsv_fontes(MANIFESTO_FONTES)
    derivados = carregar_tsv_derivados(MANIFESTO_DERIVADOS)
    rastreio = contar_rastreio_por_arquivo(RASTREIO)
    arquivos_reais = sorted(p.name for p in ENTRADA.glob("*.md") if p.name != "README.md")

    if len(fontes) != N_FONTES_ESPERADO or len(derivados) != N_FONTES_ESPERADO or len(arquivos_reais) != N_FONTES_ESPERADO:
        raise FalhaFase0(
            "O lote não contém os 309 pares esperados: "
            f"fontes no manifesto={len(fontes)}, derivados no manifesto={len(derivados)}, "
            f"arquivos derivados reais={len(arquivos_reais)}."
        )
    conjuntos = {"fontes": set(fontes), "derivados": set(derivados), "arquivos": set(arquivos_reais)}
    if len({frozenset(valor) for valor in conjuntos.values()}) != 1:
        detalhes = "; ".join(
            f"{nome}: faltam {len(set(fontes) - conjunto)}, sobram {len(conjunto - set(fontes))}"
            for nome, conjunto in conjuntos.items()
            if conjunto != set(fontes)
        )
        raise FalhaFase0(f"Pares fonte ↔ derivado não são bijetivos ({detalhes})")

    documentos: list[Documento] = []
    total_trocas = 0
    for posicao, nome in enumerate(arquivos_reais, 1):
        meta_fonte = fontes[nome]
        meta_derivado = derivados[nome]
        caminho = ENTRADA / nome
        conteudo = caminho.read_bytes()  # única fonte textual da Fase 0
        sha_atual = hashlib.sha256(conteudo).hexdigest()
        if len(conteudo) != meta_derivado.bytes or sha_atual != meta_derivado.sha256:
            raise FalhaFase0(f"{nome}: derivado difere do manifesto selado")
        if meta_derivado.sha256_fonte != meta_fonte.sha256:
            raise FalhaFase0(f"{nome}: SHA da fonte diverge entre os dois manifestos")
        if rastreio[nome] != meta_derivado.trocas:
            raise FalhaFase0(
                f"{nome}: manifesto declara {meta_derivado.trocas} troca(s), "
                f"rastreio contém {rastreio[nome]}"
            )
        try:
            texto = conteudo.decode("utf-8")
        except UnicodeDecodeError as erro:
            raise FalhaFase0(f"{nome}: derivado não é UTF-8") from erro
        frente, _corpo, linha_corpo = separar_frontmatter(texto, nome)
        titulo = valor_yaml_simples(frente, "titulo")
        if not titulo:
            raise FalhaFase0(f"{nome}: metadado obrigatório 'titulo' ausente")
        duracao_texto = valor_yaml_simples(frente, "duracao")
        documentos.append(
            Documento(
                ingresso_id=f"STT-2026-10-{posicao:03d}",
                arquivo=nome,
                caminho_derivado=f"normalizados_stt_lote_2026-10/{nome}",
                sha256_derivado=sha_atual,
                sha256_fonte_declarado=meta_fonte.sha256,
                bytes=len(conteudo),
                trocas_normalizacao=meta_derivado.trocas,
                titulo=titulo,
                data_publicacao_original=valor_yaml_simples(frente, "data_publicacao_original"),
                id_youtube=valor_yaml_simples(frente, "id_youtube"),
                link_original=valor_yaml_simples(frente, "link_original"),
                duracao_texto=duracao_texto,
                duracao_segundos=parse_duracao(duracao_texto, nome),
                linha_inicio_corpo=linha_corpo,
                texto=texto,
            )
        )
        total_trocas += meta_derivado.trocas

    # Uma origem por nome e um único destino por nome é requisito de ingresso. O
    # hash pode coincidir em fontes sem troca, por isso não é usado como chave.
    if len({d.arquivo for d in documentos}) != N_FONTES_ESPERADO:
        raise FalhaFase0("Registro mestre contém par não unívoco")
    dados_integridade = {
        "fontes_manifestadas": len(fontes),
        "derivados_manifestados": len(derivados),
        "derivados_conferidos": len(documentos),
        "trocas_rastreio": sum(rastreio.values()),
        "trocas_manifesto": total_trocas,
        "fontes_brutas_abertas": 0,
    }
    hashes = {
        "dados_termos.py": sha256_arquivo(DADOS_TERMOS),
        "manifesto-fontes-sha256.tsv": sha256_arquivo(MANIFESTO_FONTES),
        "manifesto-derivados-sha256.tsv": sha256_arquivo(MANIFESTO_DERIVADOS),
        "rastreio-antes-depois.jsonl": sha256_arquivo(RASTREIO),
    }
    return documentos, dados_integridade, hashes


def carregar_termos_base() -> list[TermoBase]:
    if not DADOS_TERMOS.is_file():
        raise FalhaFase0("dados_termos.py ausente")
    namespace: dict[str, object] = {"__name__": "_fase0_ingestao_stt"}
    try:
        exec(compile(DADOS_TERMOS.read_text(encoding="utf-8"), str(DADOS_TERMOS), "exec"), namespace)
    except Exception as erro:
        raise FalhaFase0(f"Não foi possível ler a Base terminológica: {erro}") from erro
    termos = namespace.get("TERMOS")
    if not isinstance(termos, list):
        raise FalhaFase0("dados_termos.py não expôs TERMOS como lista")
    resultado: list[TermoBase] = []
    for termo in termos:
        if not isinstance(termo, tuple) or len(termo) < 4:
            raise FalhaFase0("Estrutura inesperada em TERMOS")
        resultado.append(TermoBase(str(termo[0]), str(termo[1]), str(termo[2]), str(termo[3])))
    if len(resultado) < 900:
        raise FalhaFase0(f"Base terminológica inesperadamente pequena: {len(resultado)}")
    return resultado


def normalizar_chave(texto: str) -> str:
    return " ".join(texto.casefold().split())


def aliases_termo(nome: str) -> set[str]:
    """Gera grafias de busca conservadoras a partir do nome canônico da Base."""
    bruto = " ".join(nome.split())
    candidatos = {bruto}
    sem_parenteses = re.sub(r"\s*\([^)]*\)", "", bruto).strip(" -–—")
    if sem_parenteses:
        candidatos.add(sem_parenteses)
    # Itens compostos do cadastro podem ter a forma "A / B". Cada parte só
    # entra se continuar distintiva e não colidir com outro código.
    for base in list(candidatos):
        for parte in re.split(r"\s*/\s*|\s+ou\s+", base, flags=re.I):
            parte = parte.strip(" .,:;-–—")
            if parte:
                candidatos.add(parte)
    limpos: set[str] = set()
    for candidato in candidatos:
        chave = normalizar_chave(candidato)
        letras = "".join(ch for ch in chave if ch.isalpha())
        if len(letras) < 5 or chave in ALIAS_COMUNS:
            continue
        # Evita rótulos longos artificiais que começam por artigo isolado.
        if chave in {"o", "a", "os", "as"}:
            continue
        limpos.add(candidato)
    return limpos


def compilar_indice_termos(termos: list[TermoBase]) -> tuple[re.Pattern[str], dict[str, TermoBase], int]:
    por_alias: dict[str, list[TermoBase]] = defaultdict(list)
    escrita: dict[str, str] = {}
    for termo in termos:
        for alias in aliases_termo(termo.nome):
            chave = normalizar_chave(alias)
            por_alias[chave].append(termo)
            escrita.setdefault(chave, alias)
    univocos = {chave: valores[0] for chave, valores in por_alias.items() if len({t.codigo for t in valores}) == 1}
    if not univocos:
        raise FalhaFase0("Nenhum alias unívoco da Base disponível para triagem")
    # Grupo nomeado permite recuperar a chave independente de caixa/acento da fonte.
    alternativas = "|".join(re.escape(escrita[chave]) for chave in sorted(univocos, key=lambda x: (-len(x), x)))
    return re.compile(rf"(?<!\w)({alternativas})(?!\w)", re.IGNORECASE), univocos, len(por_alias) - len(univocos)


def temas_do_texto(texto: str, titulo: str) -> list[dict[str, object]]:
    alvo = f"{titulo}\n{texto}".casefold()
    saida: list[dict[str, object]] = []
    for ordem, (codigo, nome, chaves) in enumerate(TEMAS):
        ocorrencias = 0
        chaves_presentes: list[str] = []
        for chave in chaves:
            n = alvo.count(chave.casefold())
            if n:
                ocorrencias += n
                chaves_presentes.append(chave)
        if ocorrencias:
            saida.append(
                {
                    "codigo": codigo,
                    "tema": nome,
                    "sinais": ocorrencias,
                    "palavras_chave": chaves_presentes,
                    "ordem": ordem,
                }
            )
    return sorted(saida, key=lambda t: (-int(t["sinais"]), int(t["ordem"])))


def registros_linhas_e_termos(
    documentos: list[Documento], padrao: re.Pattern[str], termos_por_alias: dict[str, TermoBase]
) -> tuple[list[dict], list[dict], list[dict]]:
    """Endereços estáveis por linha e sinais exatos de termos canônicos."""
    linhas: list[dict] = []
    ocorrencias: list[dict] = []
    mapa_tematico: list[dict] = []
    for documento in documentos:
        frente, corpo, linha_corpo = separar_frontmatter(documento.texto, documento.arquivo)
        temas = temas_do_texto(corpo, documento.titulo)
        tema_primario = temas[0]["codigo"] if temas else "GERAL_SEM_SINAL_FORTE"
        mapa_tematico.append(
            {
                "ingresso_id": documento.ingresso_id,
                "arquivo": documento.arquivo,
                "tema_primario": tema_primario,
                "temas": [{k: v for k, v in tema.items() if k != "ordem"} for tema in temas],
            }
        )
        for deslocamento, texto_linha in enumerate(corpo.splitlines()):
            if not texto_linha.strip():
                continue
            numero_linha = linha_corpo + deslocamento
            unidade = f"U{numero_linha:05d}"
            texto_limpo = " ".join(texto_linha.split())
            linhas.append(
                {
                    "ingresso_id": documento.ingresso_id,
                    "arquivo": documento.arquivo,
                    "unidade": unidade,
                    "linha": numero_linha,
                    "caracteres": len(texto_linha),
                    "sha256_texto_linha": hashlib.sha256(texto_linha.encode("utf-8")).hexdigest(),
                }
            )
            for achado in padrao.finditer(texto_linha):
                alias = normalizar_chave(achado.group(1))
                termo = termos_por_alias.get(alias)
                if termo is None:
                    # Com nomes que diferem apenas por normalização Unicode, o
                    # padrão pode devolver uma grafia equivalente à chave salva.
                    continue
                inicio = max(0, achado.start() - 120)
                fim = min(len(texto_linha), achado.end() + 180)
                ocorrencias.append(
                    {
                        "ingresso_id": documento.ingresso_id,
                        "arquivo": documento.arquivo,
                        "unidade": unidade,
                        "linha": numero_linha,
                        "codigo": termo.codigo,
                        "nome": termo.nome,
                        "categoria": termo.categoria,
                        "subcategoria": termo.subcategoria,
                        "grafia_encontrada": achado.group(1),
                        "excerto": ("…" if inicio else "")
                        + " ".join(texto_linha[inicio:fim].split())
                        + ("…" if fim < len(texto_linha) else ""),
                        "natureza": "sinal-exato-de-grafia-base",
                    }
                )
    return linhas, ocorrencias, mapa_tematico


def _particionar_por_capacidade(fontes: list[Documento]) -> list[tuple[list[Documento], int, str | None]]:
    """Particiona uma família em blocos contíguos, balanceados e no máximo 12h.

    A ordem interna é temática e cronológica. O DP permite deslocar uma fronteira
    quando o corte guloso produziria uma cauda curta, sem quebrar uma fonte.
    """
    if not fontes:
        return []
    duracoes = [fonte.duracao_segundos or 0 for fonte in fontes]
    total = sum(duracoes)
    teto = int(TETO_HORAS_LOTE * 3600)
    meta = int(META_HORAS_LOTE * 3600)
    minimo = max(1, round(total / meta), (total + teto - 1) // teto)
    minimo = min(minimo, len(fontes))
    prefixos = [0]
    for duracao in duracoes:
        prefixos.append(prefixos[-1] + duracao)

    # Se a ordem temática exigir uma fronteira adicional para honrar 12h,
    # acrescentamo-la. Essa é a única razão para haver mais lotes que a divisão
    # aritmética ideal; fonte alguma é fatiada para maquiar a capacidade.
    solucao: tuple[int, dict[tuple[int, int], tuple[float, int]]] | None = None
    for quantidade in range(minimo, len(fontes) + 1):
        alvo = total / quantidade
        dp: dict[tuple[int, int], tuple[float, int]] = {(0, 0): (0.0, -1)}
        for k in range(1, quantidade + 1):
            for j in range(k, len(fontes) + 1):
                melhor: tuple[float, int] | None = None
                for i in range(k - 1, j):
                    anterior = dp.get((k - 1, i))
                    if anterior is None:
                        continue
                    segundos = prefixos[j] - prefixos[i]
                    indivisivel = j - i == 1 and segundos > teto
                    if segundos > teto and not indivisivel:
                        continue
                    custo = ((segundos - alvo) / 3600) ** 2
                    if segundos < 10 * 3600:
                        custo += ((10 * 3600 - segundos) / 3600) ** 2 * 0.15
                    if indivisivel:
                        custo += 1000
                    candidato = (anterior[0] + custo, i)
                    if melhor is None or candidato[0] < melhor[0] - 1e-12:
                        melhor = candidato
                if melhor is not None:
                    dp[(k, j)] = melhor
        if (quantidade, len(fontes)) in dp:
            solucao = (quantidade, dp)
            break
    if solucao is None:
        raise FalhaFase0("Não foi possível particionar a família temática no teto de 12 horas")

    quantidade, dp_final = solucao
    faixas: list[tuple[int, int]] = []
    j = len(fontes)
    for k in range(quantidade, 0, -1):
        i = dp_final[(k, j)][1]
        faixas.append((i, j))
        j = i
    faixas.reverse()
    saida = []
    for i, j in faixas:
        segundos = prefixos[j] - prefixos[i]
        ressalva = "fonte atômica excede o teto e não foi fracionada" if j - i == 1 and segundos > teto else None
        saida.append((fontes[i:j], segundos, ressalva))
    return saida


def selecionar_lotes(
    documentos: list[Documento], mapa_tematico: list[dict], ocorrencias: list[dict]
) -> list[dict]:
    """Agrupa em famílias temáticas e equilibra cada uma perto de 10–12 horas."""
    tema_por_id = {registro["ingresso_id"]: registro["tema_primario"] for registro in mapa_tematico}
    familia_por_tema = {
        tema: (codigo, nome, eixos)
        for codigo, nome, eixos in FAMILIAS_DE_LOTE
        for tema in eixos
    }
    if set(tema_por_id.values()) - set(familia_por_tema):
        raise FalhaFase0("Tema primário sem família de capacidade")

    docs_por_familia: dict[str, list[Documento]] = defaultdict(list)
    definicao_familias = {codigo: (nome, eixos) for codigo, nome, eixos in FAMILIAS_DE_LOTE}
    for documento in documentos:
        codigo_familia, _nome, _eixos = familia_por_tema[tema_por_id[documento.ingresso_id]]
        docs_por_familia[codigo_familia].append(documento)

    # Dentro de uma família, fontes do mesmo eixo ficam juntas e cronológicas:
    # a capacidade pode aproximar eixos compatíveis, mas nunca mistura-os sem
    # revelar a composição no lote resultante.
    ordem_temas = {codigo: posicao for posicao, (codigo, _nome, _chaves) in enumerate(TEMAS)}
    ordem_temas["GERAL_SEM_SINAL_FORTE"] = len(ordem_temas)
    for fontes in docs_por_familia.values():
        fontes.sort(key=lambda d: (ordem_temas[tema_por_id[d.ingresso_id]], d.data_publicacao_original or "9999-99-99", d.arquivo))

    provisorios: list[tuple[str, list[Documento], int, str | None]] = []
    for codigo_familia, _nome, _eixos in FAMILIAS_DE_LOTE:
        for fontes, segundos, ressalva in _particionar_por_capacidade(docs_por_familia[codigo_familia]):
            provisorios.append((codigo_familia, fontes, segundos, ressalva))

    ocorrencias_por_id: dict[str, list[dict]] = defaultdict(list)
    for ocorrencia in ocorrencias:
        ocorrencias_por_id[ocorrencia["ingresso_id"]].append(ocorrencia)

    lotes: list[dict] = []
    for indice, (familia, fontes, segundos, ressalva) in enumerate(provisorios, 1):
        # Não usar conjunto aqui: a primeira evidência de cada candidato é
        # publicada no JSON e precisa ser byte a byte reprodutível.
        sinais = [
            ocorrencia
            for fonte in fontes
            for ocorrencia in ocorrencias_por_id[fonte.ingresso_id]
        ]
        peso: Counter[tuple[str, str, str, str]] = Counter(
            (s["codigo"], s["nome"], s["categoria"], s["subcategoria"]) for s in sinais
        )
        exemplos: dict[tuple[str, str, str, str], dict] = {}
        for sinal in sinais:
            chave = (sinal["codigo"], sinal["nome"], sinal["categoria"], sinal["subcategoria"])
            exemplos.setdefault(chave, sinal)
        candidatos = []
        for chave, quantidade in sorted(peso.items(), key=lambda par: (-par[1], par[0][0]))[:MAX_CANDIDATOS_POR_LOTE]:
            exemplo = exemplos[chave]
            candidatos.append(
                {
                    "codigo": chave[0],
                    "nome": chave[1],
                    "categoria": chave[2],
                    "subcategoria": chave[3],
                    "sinais_exatos": quantidade,
                    "primeiro_endereco": {
                        "ingresso_id": exemplo["ingresso_id"],
                        "unidade": exemplo["unidade"],
                        "linha": exemplo["linha"],
                    },
                    "estado": "candidato-de-cotejo; não é pérola nem ordem de ampliação",
                }
            )
        nome_familia, eixos = definicao_familias[familia]
        composicao = Counter(tema_por_id[fonte.ingresso_id] for fonte in fontes)
        lotes.append(
            {
                "lote_id": f"STT26-{indice:02d}",
                "tema_primario": {"codigo": familia, "nome": nome_familia},
                "eixos_de_origem": [
                    {"codigo": eixo, "fontes": composicao[eixo]}
                    for eixo in eixos if composicao[eixo]
                ],
                "estado": "AGUARDANDO-DESPACHO-CURATORIAL",
                "duracao_estimada_segundos": segundos,
                "duracao_estimada": formatar_duracao(segundos),
                "dentro_da_faixa_planejada_10a12h": int(10 * 3600) <= segundos <= int(TETO_HORAS_LOTE * 3600),
                "ressalva_capacidade": ressalva,
                "fontes": [
                    {
                        "ingresso_id": fonte.ingresso_id,
                        "arquivo": fonte.arquivo,
                        "titulo": fonte.titulo,
                        "duracao": fonte.duracao_texto,
                    }
                    for fonte in fontes
                ],
                "candidatos_de_cotejo_base": candidatos,
                "limite_candidatos": MAX_CANDIDATOS_POR_LOTE,
                "quantidade_candidatos": len(candidatos),
            }
        )
    if sum(len(lote["fontes"]) for lote in lotes) != len(documentos):
        raise FalhaFase0("Planejamento perdeu ou duplicou fonte")
    return lotes


def registro_mestre(documentos: list[Documento], mapa_tematico: list[dict]) -> list[dict]:
    temas_por_id = {registro["ingresso_id"]: registro for registro in mapa_tematico}
    registros: list[dict] = []
    for documento in documentos:
        tema = temas_por_id[documento.ingresso_id]
        registros.append(
            {
                "ingresso_id": documento.ingresso_id,
                "estado": "APTO-PARA-TRIAGEM-SEM-MUTAR-BASE",
                "natureza_fonte": "TRANSCRICAO-STT-NORMALIZADA-DERIVADA",
                "arquivo_derivado": documento.caminho_derivado,
                "sha256_derivado": documento.sha256_derivado,
                "bytes_derivado": documento.bytes,
                "origem_declarada": {
                    "arquivo_stt_bruto": f"uploads_recepcao/stt-lote-2026-10/{documento.arquivo}",
                    "sha256_fonte": documento.sha256_fonte_declarado,
                    "verificacao": "manifesto-fonte ↔ manifesto-derivado ↔ hash-atual-do-derivado",
                },
                "normalizacao": {
                    "trocas_rastreadas": documento.trocas_normalizacao,
                    "politica": "D1 e D2 aplicadas; D3 preservado",
                },
                "metadados": {
                    "titulo": documento.titulo,
                    "data_publicacao_original": documento.data_publicacao_original,
                    "id_youtube": documento.id_youtube,
                    "link_original": documento.link_original,
                    "duracao": documento.duracao_texto,
                },
                "enderecamento": {"primeira_linha_corpo": documento.linha_inicio_corpo},
                "triagem": {
                    "tema_primario": tema["tema_primario"],
                    "temas_sinalizados": [item["codigo"] for item in tema["temas"]],
                },
                "proxima_etapa_permitida": "triagem e despacho curatorial por lote; motor.py somente após despacho",
            }
        )
    return registros


def montar_resumo(
    documentos: list[Documento], integridade: dict[str, int], hashes: dict[str, str], termos: list[TermoBase],
    aliases_ambiguos: int, linhas: list[dict], ocorrencias: list[dict], mapa_tematico: list[dict], lotes: list[dict]
) -> dict:
    distribuicao_temas = Counter(m["tema_primario"] for m in mapa_tematico)
    total_segundos = sum(d.duracao_segundos or 0 for d in documentos)
    sem_duracao = [d.ingresso_id for d in documentos if d.duracao_segundos is None]
    return {
        "lote_origem": "stt-lote-2026-10",
        "fase": "0 — registro, validação e triagem; sem mutação da Base",
        "gerado_em": DATA_GERACAO,
        "politica_de_entrada": "somente normalizados_stt_lote_2026-10; STT bruto não foi aberto",
        "integridade": integridade,
        "hashes_entrada_e_base_lida": hashes,
        "base_terminologica": {
            "termos_lidos": len(termos),
            "aliases_ambiguos_excluidos": aliases_ambiguos,
            "ocorrencias_exatas_indexadas": len(ocorrencias),
        },
        "mapeamento": {
            "enderecos_de_linha": len(linhas),
            "fontes_com_tema_primario": sum(distribuicao_temas.values()),
            "distribuicao_tema_primario": dict(sorted(distribuicao_temas.items())),
        },
        "capacidade": {
            "duracao_total_segundos": total_segundos,
            "duracao_total": formatar_duracao(total_segundos),
            "fontes_sem_duracao": sem_duracao,
            "lotes_planejados": len(lotes),
            "meta_horas_por_lote": META_HORAS_LOTE,
            "teto_horas_por_lote": TETO_HORAS_LOTE,
            "max_candidatos_por_lote": MAX_CANDIDATOS_POR_LOTE,
        },
        "barreiras": {
            "ciclos_criados": 0,
            "fichas_criadas": 0,
            "termos_criados": 0,
            "relacoes_criadas": 0,
            "apostilas_criadas": 0,
            "dados_termos_alterado": False,
        },
    }


def montar_readme(resumo: dict) -> str:
    return f"""# Fase 0 — ingresso STT normalizado (lote 2026-10)

> **Estado:** registro, integridade e triagem. Não é um ciclo do Motor e não altera a Base.

## Regra de fonte

A entrada operacional é exclusivamente `normalizados_stt_lote_2026-10/`. Os
caminhos e SHA-256 dos STT brutos aparecem como proveniência declarada pelos
manifestos da normalização; a Fase 0 não abriu, pesquisou nem transcreveu os
brutos em `uploads_recepcao/`.

## Resultado desta geração

- registros mestre: **{resumo['integridade']['derivados_conferidos']}**;
- pares fonte declarada ↔ derivado: **{resumo['integridade']['derivados_conferidos']}**;
- duração total informada: **{resumo['capacidade']['duracao_total']}**;
- lotes temáticos planejados: **{resumo['capacidade']['lotes_planejados']}**;
- sinais exatos da Base indexados: **{resumo['base_terminologica']['ocorrencias_exatas_indexadas']}**;
- mutações em `dados_termos.py`, fichas, relações, ciclos e apostilas: **0**.

## Artefatos

| Arquivo | Finalidade |
|---|---|
| `registro-mestre.jsonl` | Um registro por derivado, sua proveniência declarada, hashes e metadados. |
| `mapa-linhas.jsonl` | Endereço estável `Uxxxxx` e hash de cada linha textual do derivado. |
| `indice-termos-base.jsonl` | Ocorrências exatas e não ambíguas de grafias da Base; é sinal de triagem, não citação. |
| `mapa-tematico.jsonl` | Eixos temáticos e palavras-sinal por fonte. |
| `lotes-planejados.json` | Lotes sem sobreposição, capacidade estimada e no máximo 25 candidatos de cotejo por lote. |
| `resumo-triagem.json` | Contadores, hashes de entrada e barreiras de escopo. |

## Consulta reproduzível

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --buscar Sophia
```

A busca lê apenas os derivados e devolve endereços de linha. Para regenerar a
Fase 0 com segurança, use `--force`: o diretório é construído em estágio e só
substitui a geração anterior depois de todas as verificações passarem.

## Próxima fronteira

Cada lote permanece em `AGUARDANDO-DESPACHO-CURATORIAL`. O limite de 25 é um
teto para **candidatos de cotejo**; ele não cria pérolas nem autoriza ampliação.
Somente um despacho consolidado poderá selecionar candidatos e abrir um
`ciclo.toml` para o `motor.py`.
"""


def montar_relatorio(resumo: dict, lotes: list[dict]) -> str:
    tabela_lotes = []
    for lote in lotes:
        arquivos = "<br>".join(f"`{f['ingresso_id']}`" for f in lote["fontes"])
        ressalva = lote["ressalva_capacidade"] or "—"
        faixa = "sim" if lote["dentro_da_faixa_planejada_10a12h"] else "aproximação"
        tabela_lotes.append(
            f"| `{lote['lote_id']}` | {lote['tema_primario']['nome']} | {lote['duracao_estimada']} | "
            f"{len(lote['fontes'])} | {lote['quantidade_candidatos']}/{lote['limite_candidatos']} | {faixa} | {ressalva} | {arquivos} |"
        )
    temas = "\n".join(
        f"| `{tema}` | {quantidade} |" for tema, quantidade in resumo["mapeamento"]["distribuicao_tema_primario"].items()
    )
    integridade = resumo["integridade"]
    return f"""# Mapa consolidado — linha de produção STT (Fase 0)

**Data:** {DATA_GERACAO}
**Lote:** `stt-lote-2026-10`
**Executor:** `ferramentas/fase0_ingestao_stt_lote_2026_10.py`
**Estado:** **Fase 0 concluída — triagem preparada, nenhuma mutação da Base.**

## Delimitação operacional

A linha de produção começa unicamente nas **309 cópias derivadas normalizadas**
em `normalizados_stt_lote_2026-10/`. Os STT em `uploads_recepcao/` não foram
abertos nem pesquisados por este executor; seus nomes e SHA-256 permanecem no
registro apenas como proveniência declarada nos manifestos que a normalização
selou. Portanto, esta geração não transforma o bruto em fonte operacional.

Também não criou ciclo, ficha, termo, relação, apostila ou alteração em
`ferramentas/dados_termos.py`. O `motor.py` permanece fora desta etapa e só
poderá ser chamado para uma fonte/lote após despacho curatorial específico.

## Portão de ingresso — aprovado

| Verificação | Resultado |
|---|---:|
| Fontes declaradas no manifesto de normalização | {integridade['fontes_manifestadas']} |
| Derivados declarados | {integridade['derivados_manifestados']} |
| Derivados presentes e com SHA-256 conferido | {integridade['derivados_conferidos']} |
| Ligações unívocas por arquivo fonte ↔ derivado | {integridade['derivados_conferidos']} |
| Trocas no rastreio | {integridade['trocas_rastreio']} |
| Trocas declaradas no manifesto | {integridade['trocas_manifesto']} |
| Conteúdos brutos abertos nesta Fase 0 | **{integridade['fontes_brutas_abertas']}** |

**Resultado:** os 309 derivados podem entrar em **triagem**, não em
materialização. Cada `ingresso_id` no `registro-mestre.jsonl` guarda o SHA do
derivado usado na produção e o SHA da fonte STT declarada no seu vínculo.

## Índice e mapa de linhas

- endereços textuais criados: **{resumo['mapeamento']['enderecos_de_linha']}**;
- termos canônicos lidos da Base: **{resumo['base_terminologica']['termos_lidos']}**;
- aliases ambíguos excluídos do índice automático: **{resumo['base_terminologica']['aliases_ambiguos_excluidos']}**;
- sinais exatos e não ambíguos da Base: **{resumo['base_terminologica']['ocorrencias_exatas_indexadas']}**.

O endereço `Uxxxxx` é a linha física no derivado. O índice registra apenas uma
correspondência literal de grafia existente na Base; não é verificação contra
a fala, não é citação e não equivale a juízo editorial. A consulta operacional
é feita exclusivamente contra os derivados:

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --buscar "Sophia"
```

### Distribuição de fila por tema primário

| Tema | Fontes |
|---|---:|
{temas}

## Planejamento de capacidade curatorial

Duração total informada: **{resumo['capacidade']['duracao_total']}**. O plano
forma lotes sem sobreposição por família temática, buscando **10–12 h** e sem
fracionar uma transcrição. O teto de **25** é para candidatos de cotejo da Base
por lote, não para criação automática de pérolas.

| Lote | Tema | Duração estimada | Fontes | Candidatos | Faixa 10–12h | Ressalva | Ingressos |
|---|---|---:|---:|---:|---|---|---|
{chr(10).join(tabela_lotes)}

Os membros e a evidência inicial de cada fila estão em
`ingestao_stt_lote_2026-10/lotes-planejados.json`. A seleção de 25 candidatos
usa frequência de sinais exatos da Base como **ordem de leitura**, não como
prova, nem como abertura de termo ou alteração de ficha.

## Próximo despacho necessário

Para um lote `STT26-xx`, a curadoria deve deliberar em bloco:

1. quais, se houver, candidatos de cotejo tornam-se pérolas/citações elegíveis;
2. quais hipóteses permanecem pendentes ou são descartadas;
3. qual fonte derivada e quais âncoras entram em um `ciclo.toml` próprio;
4. se algum resultado autoriza o Motor a alterar a Base.

Até esse despacho, o estado de todos os lotes é
`AGUARDANDO-DESPACHO-CURATORIAL` e a Fase 0 é somente um mapa recuperável e
reproduzível.

## Reprodução e retomada segura

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --force
```

A geração valida tudo antes de publicar, constrói os artefatos em diretório
temporário e só troca a versão anterior quando a saída completa está pronta.
"""


def gerar(force: bool) -> None:
    # Toda leitura e validação ocorre antes de criar a saída: falha de entrada não
    # publica lote parcial nem elimina uma geração anterior válida.
    documentos, integridade, hashes = carregar_documentos()
    termos = carregar_termos_base()
    padrao, termos_por_alias, aliases_ambiguos = compilar_indice_termos(termos)
    linhas, ocorrencias, mapa_tematico = registros_linhas_e_termos(documentos, padrao, termos_por_alias)
    lotes = selecionar_lotes(documentos, mapa_tematico, ocorrencias)
    mestre = registro_mestre(documentos, mapa_tematico)
    resumo = montar_resumo(
        documentos, integridade, hashes, termos, aliases_ambiguos, linhas, ocorrencias, mapa_tematico, lotes
    )
    readme = montar_readme(resumo)
    relatorio = montar_relatorio(resumo, lotes)

    if SAIDA.exists() and not force:
        raise FileExistsError(
            f"Saída já existe: {SAIDA.relative_to(RAIZ)}/. Use --force para regenerar somente a Fase 0."
        )
    if SAIDA.resolve() == ENTRADA.resolve() or SAIDA.resolve() == (RAIZ / "uploads_recepcao").resolve():
        raise FalhaFase0("Destino Fase 0 jamais pode ser uma fonte")

    # Temp no mesmo filesystem torna a troca final atômica. Uma falha preserva a
    # saída anterior; arquivo bruto, Base e diretórios da esteira não são tocados.
    prefixo = f".{SAIDA.name}-"
    with tempfile.TemporaryDirectory(prefix=prefixo, dir=RAIZ) as temporario:
        estagio = Path(temporario) / SAIDA.name
        estagio.mkdir()
        (estagio / "README.md").write_text(readme, encoding="utf-8", newline="\n")
        escrever_jsonl(estagio / "registro-mestre.jsonl", mestre)
        escrever_jsonl(estagio / "mapa-linhas.jsonl", linhas)
        escrever_jsonl(estagio / "indice-termos-base.jsonl", ocorrencias)
        escrever_jsonl(estagio / "mapa-tematico.jsonl", mapa_tematico)
        (estagio / "lotes-planejados.json").write_text(
            json.dumps(lotes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        (estagio / "resumo-triagem.json").write_text(
            json.dumps(resumo, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )
        relatorio_tmp = Path(temporario) / RELATORIO.name
        relatorio_tmp.write_text(relatorio, encoding="utf-8", newline="\n")

        anterior = RAIZ / f".{SAIDA.name}-anterior"
        if anterior.exists():
            shutil.rmtree(anterior)
        if SAIDA.exists():
            SAIDA.rename(anterior)
        try:
            estagio.rename(SAIDA)
            os.replace(relatorio_tmp, RELATORIO)
        except Exception:
            if SAIDA.exists():
                shutil.rmtree(SAIDA)
            if anterior.exists():
                anterior.rename(SAIDA)
            raise
        else:
            if anterior.exists():
                shutil.rmtree(anterior)

    print(
        "Fase 0 concluída: "
        f"{len(documentos)} registros, {len(linhas)} endereços, {len(ocorrencias)} sinais, {len(lotes)} lotes."
    )


def buscar(consulta: str, limite: int) -> int:
    if not consulta.strip():
        raise FalhaFase0("A consulta de busca não pode ser vazia")
    # A busca não depende do índice para não ficar desatualizada se um derivado
    # for trocado indevidamente: ela refaz a verificação dos SHA de entrada.
    documentos, _integridade, _hashes = carregar_documentos()
    padrao = re.compile(re.escape(consulta), re.IGNORECASE)
    achados: list[dict] = []
    for documento in documentos:
        _frente, corpo, linha_corpo = separar_frontmatter(documento.texto, documento.arquivo)
        for deslocamento, linha in enumerate(corpo.splitlines()):
            if padrao.search(linha):
                n = linha_corpo + deslocamento
                achados.append(
                    {
                        "ingresso_id": documento.ingresso_id,
                        "arquivo": documento.arquivo,
                        "unidade": f"U{n:05d}",
                        "linha": n,
                        "texto": " ".join(linha.split()),
                    }
                )
                if len(achados) >= limite:
                    break
        if len(achados) >= limite:
            break
    for achado in achados:
        print(json.dumps(achado, ensure_ascii=False))
    print(f"# {len(achados)} ocorrência(s) exibida(s); limite={limite}.", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("--force", action="store_true", help="regenera somente os artefatos derivados da Fase 0")
    grupo.add_argument("--buscar", metavar="TEXTO", help="busca literal nas cópias derivadas, sem usar STT bruto")
    parser.add_argument("--limite", type=int, default=50, help="máximo de linhas exibidas por --buscar (padrão: 50)")
    args = parser.parse_args()
    try:
        if args.buscar is not None:
            if args.limite < 1:
                raise FalhaFase0("--limite deve ser positivo")
            return buscar(args.buscar, args.limite)
        gerar(args.force)
        return 0
    except (FalhaFase0, FileExistsError) as erro:
        print(f"Fase 0 abortada: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
