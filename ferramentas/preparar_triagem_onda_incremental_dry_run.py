#!/usr/bin/env python3
"""Mapeia a onda incremental em lotes e prepara seus dossiês curatoriais.

A alocação é fechada pelo despacho do Curador:

- P1 -> ANUNNAKI_GENETICA
- P2 -> MITOLOGIAS_REINTEGRACAO
- P3 -> COSMOGONIA_HISTORIA_COSMICA
- P4, P5, P6 -> EXPERIENCIA_ESPIRITUAL_ETICA

A entrada operacional são exclusivamente os seis derivados e manifestos de
``onda_incremental_dry_run/``. O executor não abre ``uploads_recepcao/`` e não
cria ciclos, fichas, termos, relações, apostilas ou alterações na Base.

Uso:
    python3 ferramentas/preparar_triagem_onda_incremental_dry_run.py
    python3 ferramentas/preparar_triagem_onda_incremental_dry_run.py --force

``--force`` só recria a subárvore curatorial e os dois mapas derivados desta
onda; nunca toca os derivados normalizados, o diretório do piloto ou os brutos.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


RAIZ = Path(__file__).resolve().parent.parent
ONDA = "onda_incremental_dry_run"
RAIZ_ONDA = RAIZ / ONDA
DERIVADOS = RAIZ_ONDA / "derivados_normalizados"
MANIFESTO_FONTES = RAIZ_ONDA / "manifesto-fontes.json"
MANIFESTO_DERIVADOS = RAIZ_ONDA / "manifesto-derivados.json"
RASTREIO = RAIZ_ONDA / "rastreio-antes-depois.jsonl"
SAIDA = RAIZ_ONDA / "triagem_curatorial"
MAPA_MD = RAIZ_ONDA / "MAPEAMENTO-EIXOS-CURATORIAL.md"
MAPA_JSON = RAIZ_ONDA / "mapeamento-eixos.json"
DADOS_TERMOS = RAIZ / "ferramentas" / "dados_termos.py"
EXECUTOR = "ferramentas/preparar_triagem_onda_incremental_dry_run.py"

MAX_CANDIDATOS_POR_LOTE = 25
MAX_EVIDENCIAS_POR_CANDIDATO = 3
# Data local do Curador fornecida para esta sessão; não derivar do relógio UTC do sandbox.
DATA_GERACAO = "2026-10-22"

# A ordem é também a ordem de publicação dos lotes; não há inferência temática
# nesta tabela, apenas a formalização do despacho curatorial do usuário.
ALOCACOES = (
    (
        "OIDR26-01",
        "ANUNNAKI_GENETICA",
        "Anunnaki, genética e humanidade",
        ("P1",),
    ),
    (
        "OIDR26-02",
        "MITOLOGIAS_REINTEGRACAO",
        "Mitologias, tradições e reintegração",
        ("P2",),
    ),
    (
        "OIDR26-03",
        "COSMOGONIA_HISTORIA_COSMICA",
        "Cosmogonia e história cósmica",
        ("P3",),
    ),
    (
        "OIDR26-04",
        "EXPERIENCIA_ESPIRITUAL_ETICA",
        "Experiência espiritual e ética evolutiva",
        ("P4", "P5", "P6"),
    ),
)

# Termos genéricos não são descritores seguros de um candidato curatorial.
# A exclusão só evita inflação da fila automática: não remove palavras da fonte.
ALIAS_COMUNS = {
    "alma", "amor", "bem", "caos", "corpo", "criador", "deus", "deuses", "demos",
    "demônios", "dor", "ego", "espírito", "fé", "fim", "força", "forma", "homem",
    "humano", "luz", "mãe", "mente", "morte", "mundo", "natureza", "pai", "pecado",
    "pessoa", "povo", "tempo", "terra", "universo", "vida", "verdade", "vontade",
}
FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n.*?^---[ \t]*(?:\r?\n|\Z)", re.DOTALL | re.MULTILINE)


class FalhaTriagem(RuntimeError):
    """Uma invariante de origem ou escopo falhou antes de haver publicação."""


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
    sha256_fonte: str
    sha256_derivado: str
    bytes_derivado: int
    trocas_normalizacao: int
    titulo: str
    data_publicacao_original: str
    id_youtube: str
    duracao: str
    duracao_segundos: int
    primeira_linha_corpo: int
    texto: str


def sha256_bytes(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def sha256_arquivo(caminho: Path) -> str:
    return sha256_bytes(caminho.read_bytes())


def data_geracao() -> str:
    return DATA_GERACAO


def json_deterministico(objeto: object) -> str:
    return json.dumps(objeto, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def escrever_jsonl(caminho: Path, registros: Iterable[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as destino:
        for registro in registros:
            destino.write(json_deterministico(registro))
            destino.write("\n")


def ler_json(caminho: Path) -> object:
    if not caminho.is_file():
        raise FalhaTriagem(f"Artefato obrigatório ausente: {caminho.relative_to(RAIZ)}")
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise FalhaTriagem(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def separar_frontmatter(texto: str, arquivo: str) -> tuple[str, str, int]:
    encontrado = FRONTMATTER.match(texto)
    if not encontrado:
        raise FalhaTriagem(f"{arquivo}: frontmatter YAML delimitado por --- ausente")
    frente = texto[: encontrado.end()]
    return frente, texto[encontrado.end() :], frente.count("\n") + 1


def yaml_escalar(frontmatter: str, chave: str) -> str:
    achado = re.search(rf"^{re.escape(chave)}:[ \t]*([^\r\n]*?)[ \t]*\r?$", frontmatter, re.MULTILINE)
    if not achado:
        raise FalhaTriagem(f"frontmatter sem campo obrigatório {chave!r}")
    valor = achado.group(1).strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in {"'", '"'}:
        valor = valor[1:-1]
    if not valor:
        raise FalhaTriagem(f"frontmatter com campo vazio {chave!r}")
    return valor


def duracao_em_segundos(valor: str, arquivo: str) -> int:
    partes = valor.split(":")
    try:
        valores = [int(item) for item in partes]
    except ValueError as erro:
        raise FalhaTriagem(f"{arquivo}: duração inválida {valor!r}") from erro
    if len(valores) == 2:
        horas, minutos, segundos = 0, *valores
    elif len(valores) == 3:
        horas, minutos, segundos = valores
    else:
        raise FalhaTriagem(f"{arquivo}: duração fora do formato H:MM:SS")
    if horas < 0 or not 0 <= minutos < 60 or not 0 <= segundos < 60:
        raise FalhaTriagem(f"{arquivo}: duração fora da faixa {valor!r}")
    return horas * 3600 + minutos * 60 + segundos


def formatar_duracao(segundos: int) -> str:
    horas, resto = divmod(segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas}:{minutos:02d}:{segundos:02d}"


def carregar_rastreio() -> Counter[str]:
    if not RASTREIO.is_file():
        raise FalhaTriagem(f"Rastreio ausente: {RASTREIO.relative_to(RAIZ)}")
    contagem: Counter[str] = Counter()
    with RASTREIO.open(encoding="utf-8") as origem:
        for numero, linha in enumerate(origem, 1):
            try:
                evento = json.loads(linha)
                arquivo = str(evento["arquivo"])
                if not evento.get("sha256_fonte"):
                    raise KeyError("sha256_fonte")
            except (json.JSONDecodeError, KeyError) as erro:
                raise FalhaTriagem(f"{RASTREIO.name}:{numero}: evento de rastreio inválido") from erro
            contagem[arquivo] += 1
    return contagem


def carregar_documentos() -> tuple[list[Documento], dict[str, object], dict[str, bytes]]:
    """Valida manifestos e derivados, sem abrir qualquer transcrição bruta."""
    fontes_doc = ler_json(MANIFESTO_FONTES)
    derivados_doc = ler_json(MANIFESTO_DERIVADOS)
    if not isinstance(fontes_doc, dict) or not isinstance(derivados_doc, dict):
        raise FalhaTriagem("Manifestos da onda não são objetos JSON")
    fontes = fontes_doc.get("fontes")
    derivados = derivados_doc.get("derivados")
    if not isinstance(fontes, list) or not isinstance(derivados, list):
        raise FalhaTriagem("Manifestos sem listas fontes/derivados")
    if len(fontes) != 6 or len(derivados) != 6:
        raise FalhaTriagem(
            f"Onda incremental exige 6 fontes e 6 derivados; recebido {len(fontes)} e {len(derivados)}"
        )

    por_fonte: dict[str, dict] = {}
    por_derivado: dict[str, dict] = {}
    for fonte in fontes:
        if not isinstance(fonte, dict) or not isinstance(fonte.get("arquivo"), str):
            raise FalhaTriagem("Entrada inválida no manifesto de fontes")
        arquivo = fonte["arquivo"]
        if arquivo in por_fonte:
            raise FalhaTriagem(f"Arquivo fonte duplicado: {arquivo}")
        por_fonte[arquivo] = fonte
    for derivado in derivados:
        if not isinstance(derivado, dict) or not isinstance(derivado.get("arquivo"), str):
            raise FalhaTriagem("Entrada inválida no manifesto de derivados")
        arquivo = derivado["arquivo"]
        if arquivo in por_derivado:
            raise FalhaTriagem(f"Arquivo derivado duplicado: {arquivo}")
        por_derivado[arquivo] = derivado
    if set(por_fonte) != set(por_derivado):
        raise FalhaTriagem("Manifestos de fontes e derivados não formam pares bijetivos")

    arquivos_reais = {caminho.name for caminho in DERIVADOS.glob("*.md")}
    if arquivos_reais != set(por_fonte):
        raise FalhaTriagem("Derivados em disco não correspondem exatamente ao manifesto")

    rastreio = carregar_rastreio()
    documentos: list[Documento] = []
    buffers: dict[str, bytes] = {}
    for posicao, arquivo in enumerate(sorted(por_fonte), 1):
        fonte, derivado = por_fonte[arquivo], por_derivado[arquivo]
        bruto_declarado = str(fonte.get("sha256_fonte", ""))
        if not re.fullmatch(r"[0-9a-f]{64}", bruto_declarado):
            raise FalhaTriagem(f"{arquivo}: SHA-256 de origem ausente/inválido")
        if derivado.get("sha256_fonte") != bruto_declarado:
            raise FalhaTriagem(f"{arquivo}: SHA de origem diverge entre manifestos")
        conteudo = (DERIVADOS / arquivo).read_bytes()
        sha_atual = sha256_bytes(conteudo)
        if sha_atual != derivado.get("sha256_derivado") or len(conteudo) != derivado.get("bytes_derivado"):
            raise FalhaTriagem(f"{arquivo}: derivado em disco diverge do manifesto")
        if rastreio[arquivo] != derivado.get("mudancas"):
            raise FalhaTriagem(
                f"{arquivo}: manifesto declara {derivado.get('mudancas')} troca(s), "
                f"rastreio contém {rastreio[arquivo]}"
            )
        try:
            texto = conteudo.decode("utf-8")
        except UnicodeDecodeError as erro:
            raise FalhaTriagem(f"{arquivo}: derivado não UTF-8") from erro
        frente, _corpo, primeira_linha = separar_frontmatter(texto, arquivo)
        metadados = fonte.get("metadados")
        if not isinstance(metadados, dict):
            raise FalhaTriagem(f"{arquivo}: metadados de origem ausentes")
        titulo = yaml_escalar(frente, "titulo")
        duracao = yaml_escalar(frente, "duracao")
        for chave, valor in (("titulo", titulo), ("duracao", duracao), ("id_youtube", yaml_escalar(frente, "id_youtube"))):
            if metadados.get(chave) != valor:
                raise FalhaTriagem(f"{arquivo}: {chave} do derivado diverge do manifesto de fonte")
        documentos.append(
            Documento(
                ingresso_id=f"P{posicao}",
                arquivo=arquivo,
                caminho_derivado=f"{ONDA}/derivados_normalizados/{arquivo}",
                sha256_fonte=bruto_declarado,
                sha256_derivado=sha_atual,
                bytes_derivado=len(conteudo),
                trocas_normalizacao=int(derivado["mudancas"]),
                titulo=titulo,
                data_publicacao_original=yaml_escalar(frente, "data_publicacao_original"),
                id_youtube=yaml_escalar(frente, "id_youtube"),
                duracao=duracao,
                duracao_segundos=duracao_em_segundos(duracao, arquivo),
                primeira_linha_corpo=primeira_linha,
                texto=texto,
            )
        )
        buffers[arquivo] = conteudo

    ids = {documento.ingresso_id for documento in documentos}
    esperados = {f"P{numero}" for numero in range(1, 7)}
    if ids != esperados:
        raise FalhaTriagem("Registro incremental não possui exatamente P1 a P6")
    integridade: dict[str, object] = {
        "fontes_manifestadas": len(fontes),
        "derivados_manifestados": len(derivados),
        "derivados_conferidos": len(documentos),
        "trocas_rastreadas": sum(rastreio.values()),
        "fontes_brutas_abertas": 0,
        "diretorio_historico_do_piloto_lido_ou_alterado": False,
    }
    return documentos, integridade, buffers


def carregar_termos_base() -> list[TermoBase]:
    if not DADOS_TERMOS.is_file():
        raise FalhaTriagem("dados_termos.py ausente")
    namespace: dict[str, object] = {"__name__": "_triagem_onda_incremental"}
    try:
        exec(compile(DADOS_TERMOS.read_text(encoding="utf-8"), str(DADOS_TERMOS), "exec"), namespace)
    except Exception as erro:
        raise FalhaTriagem(f"Falha ao ler dados_termos.py: {erro}") from erro
    bruto = namespace.get("TERMOS")
    if not isinstance(bruto, list) or len(bruto) < 900:
        raise FalhaTriagem("TERMOS ausente ou inesperadamente pequeno")
    termos: list[TermoBase] = []
    for item in bruto:
        if not isinstance(item, tuple) or len(item) < 4:
            raise FalhaTriagem("Estrutura inesperada em TERMOS")
        termos.append(TermoBase(str(item[0]), str(item[1]), str(item[2]), str(item[3])))
    return termos


def chave_normalizada(texto: str) -> str:
    return " ".join(texto.casefold().split())


def aliases(termo: TermoBase) -> set[str]:
    """Aliases conservadores: nome inteiro e nome sem parênteses, nunca partes de '/'."""
    nome = " ".join(termo.nome.split())
    candidatos = {nome}
    sem_parenteses = re.sub(r"\s*\([^)]*\)", "", nome).strip(" -–—")
    if sem_parenteses:
        candidatos.add(sem_parenteses)
    resultado: set[str] = set()
    for candidato in candidatos:
        chave = chave_normalizada(candidato)
        letras = "".join(caractere for caractere in chave if caractere.isalpha())
        if len(letras) < 5 or chave in ALIAS_COMUNS or chave in {"o", "a", "os", "as"}:
            continue
        resultado.add(candidato)
    return resultado


def compilar_indice(termos: list[TermoBase]) -> tuple[re.Pattern[str], dict[str, TermoBase], int]:
    por_alias: dict[str, list[TermoBase]] = defaultdict(list)
    escrita: dict[str, str] = {}
    for termo in termos:
        for alias in aliases(termo):
            chave = chave_normalizada(alias)
            por_alias[chave].append(termo)
            escrita.setdefault(chave, alias)
    univocos = {
        chave: valores[0]
        for chave, valores in por_alias.items()
        if len({termo.codigo for termo in valores}) == 1
    }
    if not univocos:
        raise FalhaTriagem("Índice de termos ficou vazio")
    alternativas = "|".join(re.escape(escrita[chave]) for chave in sorted(univocos, key=lambda item: (-len(item), item)))
    return re.compile(rf"(?<!\w)({alternativas})(?!\w)", re.IGNORECASE), univocos, len(por_alias) - len(univocos)


def indexar(documentos: list[Documento], padrao: re.Pattern[str], por_alias: dict[str, TermoBase]) -> tuple[list[dict], list[dict]]:
    linhas: list[dict] = []
    ocorrencias: list[dict] = []
    for documento in documentos:
        _frente, corpo, primeira_linha = separar_frontmatter(documento.texto, documento.arquivo)
        for deslocamento, linha_textual in enumerate(corpo.splitlines()):
            if not linha_textual.strip():
                continue
            linha = primeira_linha + deslocamento
            unidade = f"U{linha:05d}"
            linhas.append(
                {
                    "ingresso_id": documento.ingresso_id,
                    "arquivo_derivado": documento.caminho_derivado,
                    "unidade": unidade,
                    "linha": linha,
                    "caracteres": len(linha_textual),
                    "sha256_texto_linha": sha256_bytes(linha_textual.encode("utf-8")),
                }
            )
            # Título e chamada de origem navegam o arquivo, mas não promovem
            # candidatos de cotejo pela simples nomeação do assunto.
            if linha_textual.lstrip().startswith(("#", ">", "---")):
                continue
            for achado in padrao.finditer(linha_textual):
                chave = chave_normalizada(achado.group(1))
                termo = por_alias.get(chave)
                if termo is None:
                    continue
                inicio, fim = max(0, achado.start() - 150), min(len(linha_textual), achado.end() + 260)
                ocorrencias.append(
                    {
                        "ingresso_id": documento.ingresso_id,
                        "arquivo_derivado": documento.caminho_derivado,
                        "sha256_derivado": documento.sha256_derivado,
                        "unidade": unidade,
                        "linha": linha,
                        "codigo": termo.codigo,
                        "nome": termo.nome,
                        "categoria": termo.categoria,
                        "subcategoria": termo.subcategoria,
                        "grafia_encontrada": achado.group(1),
                        "texto_linha_sha256": sha256_bytes(linha_textual.encode("utf-8")),
                        "excerto": ("…" if inicio else "")
                        + " ".join(linha_textual[inicio:fim].split())
                        + ("…" if fim < len(linha_textual) else ""),
                        "natureza": "sinal literal de grafia existente na Base; não é citação nem cotejo de áudio",
                    }
                )
    return linhas, ocorrencias


def planejar_lotes(documentos: list[Documento], ocorrencias: list[dict]) -> list[dict]:
    por_id = {documento.ingresso_id: documento for documento in documentos}
    ids_vistos: list[str] = []
    lotes: list[dict] = []
    por_ingresso: dict[str, list[dict]] = defaultdict(list)
    for ocorrencia in ocorrencias:
        por_ingresso[ocorrencia["ingresso_id"]].append(ocorrencia)

    for lote_id, eixo, nome_eixo, ids in ALOCACOES:
        if any(ingresso not in por_id for ingresso in ids):
            raise FalhaTriagem(f"{lote_id}: alocação aponta ingresso ausente")
        ids_vistos.extend(ids)
        fontes = [por_id[ingresso] for ingresso in ids]
        sinais = [sinal for documento in fontes for sinal in por_ingresso[documento.ingresso_id]]
        peso: Counter[tuple[str, str, str, str]] = Counter(
            (sinal["codigo"], sinal["nome"], sinal["categoria"], sinal["subcategoria"])
            for sinal in sinais
        )
        primeiros: dict[tuple[str, str, str, str], dict] = {}
        for sinal in sinais:
            chave = (sinal["codigo"], sinal["nome"], sinal["categoria"], sinal["subcategoria"])
            primeiros.setdefault(chave, sinal)
        candidatos: list[dict] = []
        for chave, quantidade in sorted(peso.items(), key=lambda item: (-item[1], item[0][0]))[:MAX_CANDIDATOS_POR_LOTE]:
            primeiro = primeiros[chave]
            candidatos.append(
                {
                    "codigo": chave[0],
                    "nome": chave[1],
                    "categoria": chave[2],
                    "subcategoria": chave[3],
                    "sinais_exatos": quantidade,
                    "primeiro_endereco": {
                        "ingresso_id": primeiro["ingresso_id"],
                        "unidade": primeiro["unidade"],
                        "linha": primeiro["linha"],
                    },
                    "estado": "candidato-de-cotejo; não é pérola, citação aprovada ou ordem de ampliação",
                }
            )
        duracao = sum(fonte.duracao_segundos for fonte in fontes)
        lotes.append(
            {
                "lote_id": lote_id,
                "eixo": {"codigo": eixo, "nome": nome_eixo},
                "origem_da_alocacao": "despacho curatorial explícito; não inferido automaticamente",
                "estado": "AGUARDANDO-DESPACHO-CURATORIAL",
                "duracao_estimada_segundos": duracao,
                "duracao_estimada": formatar_duracao(duracao),
                "ressalva_capacidade": "Lote mantido atômico no eixo por alocação curatorial explícita; não há mistura intereixos para atingir faixa horária.",
                "fontes": [
                    {
                        "ingresso_id": fonte.ingresso_id,
                        "arquivo": fonte.arquivo,
                        "titulo": fonte.titulo,
                        "duracao": fonte.duracao,
                        "sha256_derivado": fonte.sha256_derivado,
                    }
                    for fonte in fontes
                ],
                "limite_candidatos": MAX_CANDIDATOS_POR_LOTE,
                "quantidade_candidatos": len(candidatos),
                "candidatos_de_cotejo_base": candidatos,
            }
        )
    if Counter(ids_vistos) != Counter(documento.ingresso_id for documento in documentos):
        raise FalhaTriagem("Alocação perdeu, duplicou ou introduziu ingresso")
    return lotes


def linha_por_numero(documento: Documento, linha: int) -> str:
    linhas = documento.texto.splitlines()
    if linha < 1 or linha > len(linhas):
        raise FalhaTriagem(f"{documento.arquivo}: linha inexistente {linha}")
    return linhas[linha - 1]


def evidencias_representativas(ocorrencias: list[dict]) -> list[dict]:
    """No máximo três: a primeira de cada fonte, na ordem do lote."""
    por_fonte: dict[str, list[dict]] = defaultdict(list)
    ordem: list[str] = []
    for ocorrencia in ocorrencias:
        if ocorrencia["ingresso_id"] not in por_fonte:
            ordem.append(ocorrencia["ingresso_id"])
        por_fonte[ocorrencia["ingresso_id"]].append(ocorrencia)
    return [por_fonte[ingresso][0] for ingresso in ordem[:MAX_EVIDENCIAS_POR_CANDIDATO]]


def preparar_dossie(lote: dict, documentos: dict[str, Documento], indice: list[dict], hashes: dict[str, str], gerado_em: str) -> tuple[dict, list[dict], list[dict]]:
    ids = [fonte["ingresso_id"] for fonte in lote["fontes"]]
    ordem = {ingresso: posicao for posicao, ingresso in enumerate(ids)}
    candidatos = lote["candidatos_de_cotejo_base"]
    codigos = [candidato["codigo"] for candidato in candidatos]
    por_codigo: dict[str, list[dict]] = defaultdict(list)
    for ocorrencia in indice:
        if ocorrencia["ingresso_id"] in ordem and ocorrencia["codigo"] in codigos:
            por_codigo[ocorrencia["codigo"]].append(dict(ocorrencia))
    for ocorrencias in por_codigo.values():
        ocorrencias.sort(key=lambda item: (ordem[item["ingresso_id"]], item["linha"], item["grafia_encontrada"].casefold()))

    saida_candidatos: list[dict] = []
    saida_ocorrencias: list[dict] = []
    for candidato in candidatos:
        codigo = candidato["codigo"]
        ocorrencias = por_codigo.get(codigo, [])
        if len(ocorrencias) != candidato["sinais_exatos"]:
            raise FalhaTriagem(
                f"{lote['lote_id']} / {codigo}: plano={candidato['sinais_exatos']} sinais, índice={len(ocorrencias)}"
            )
        for sequencia, ocorrencia in enumerate(ocorrencias, 1):
            documento = documentos[ocorrencia["ingresso_id"]]
            texto_linha = linha_por_numero(documento, int(ocorrencia["linha"]))
            if sha256_bytes(texto_linha.encode("utf-8")) != ocorrencia["texto_linha_sha256"]:
                raise FalhaTriagem(f"{lote['lote_id']} / {codigo}: linha do derivado diverge do índice")
            evidencia = {
                "evidencia_id": f"{lote['lote_id']}-{codigo}-{sequencia:03d}",
                "lote_id": lote["lote_id"],
                **ocorrencia,
                "natureza": "sinal literal no derivado; não é cotejo com áudio nem citação aprovada",
            }
            ocorrencia["evidencia_id"] = evidencia["evidencia_id"]
            saida_ocorrencias.append(evidencia)
        amostra = evidencias_representativas(ocorrencias)
        saida_candidatos.append(
            {
                "codigo": codigo,
                "nome": candidato["nome"],
                "categoria": candidato["categoria"],
                "subcategoria": candidato["subcategoria"],
                "sinais_exatos": len(ocorrencias),
                "fontes_com_sinal": len({ocorrencia["ingresso_id"] for ocorrencia in ocorrencias}),
                "evidencias_representativas": [
                    {
                        "evidencia_id": ocorrencia["evidencia_id"],
                        "ingresso_id": ocorrencia["ingresso_id"],
                        "unidade": ocorrencia["unidade"],
                        "linha": ocorrencia["linha"],
                        "grafia_encontrada": ocorrencia["grafia_encontrada"],
                        "excerto": ocorrencia["excerto"],
                    }
                    for ocorrencia in amostra
                ],
                "estado": "PENDENTE-DE-DECISAO-CURATORIAL",
                "limite": "Sinal automático literal; não autoriza pérola, ficha, relação, ciclo ou alteração da Base.",
            }
        )

    resumo = {
        "lote_id": lote["lote_id"],
        "gerado_em": gerado_em,
        "estado": "AGUARDANDO-DESPACHO-CURATORIAL",
        "eixo": lote["eixo"],
        "origem_da_alocacao": lote["origem_da_alocacao"],
        "entrada_operacional": f"somente {ONDA}/derivados_normalizados/ e manifestos da onda",
        "fontes_brutas_abertas": 0,
        "fontes": len(ids),
        "duracao_estimada": lote["duracao_estimada"],
        "candidatos": len(saida_candidatos),
        "ocorrencias_literais": len(saida_ocorrencias),
        "max_candidatos": MAX_CANDIDATOS_POR_LOTE,
        "max_evidencias_representativas_por_candidato": MAX_EVIDENCIAS_POR_CANDIDATO,
        "hashes_de_entrada": hashes,
        "mutacoes": {
            "ciclos_criados": 0,
            "fichas_criadas": 0,
            "termos_criados": 0,
            "relacoes_criadas": 0,
            "apostilas_criadas": 0,
            "dados_termos_alterado": False,
        },
    }
    return resumo, saida_candidatos, saida_ocorrencias


def escapar_tabela(texto: str) -> str:
    return " ".join(texto.replace("|", "\\|").split())


def template_despacho(resumo: dict, candidatos: list[dict]) -> dict:
    return {
        "meta": {
            "artefato": "Template de despacho curatorial — onda incremental dry-run",
            "lote_id": resumo["lote_id"],
            "eixo": resumo["eixo"]["codigo"],
            "gerado_em": resumo["gerado_em"],
            "estado": "PENDENTE-CURADOR",
            "fonte_operacional": "somente derivados normalizados da onda; o STT bruto não foi aberto",
            "efeito_atual": "nenhum: não cria ciclo nem altera a Base",
            "instrucoes": [
                "Decidir o conjunto do eixo/lote, não vídeo a vídeo.",
                "Sinal literal não prova conceito, interpretação nem citação apta.",
                "AUTORIZAR-COTEJO-AMPLIADO permite apenas aprofundar evidência no derivado.",
                "ABRIR-CICLO exige despacho posterior com âncoras e fonte derivada explícitas; não é efeito deste template.",
            ],
            "opcoes_por_candidato": [
                "MANTER-EM-TRIAGEM",
                "DESCARTAR-DO-LOTE",
                "AUTORIZAR-COTEJO-AMPLIADO",
                "RESERVAR-PARA-FUTURO-CICLO",
            ],
        },
        "candidatos": [
            {
                "codigo": candidato["codigo"],
                "nome": candidato["nome"],
                "decisao": "PENDENTE",
                "fundamento_curatorial": "",
                "evidencias_disponiveis": [item["evidencia_id"] for item in candidato["evidencias_representativas"]],
                "observacao": "",
            }
            for candidato in candidatos
        ],
        "despacho_de_lote": {
            "resultado": "PENDENTE",
            "candidatos_para_cotejo_ampliado": [],
            "autorizacao_para_abrir_ciclo": False,
            "observacao": "",
        },
    }


def dossie_markdown(lote: dict, resumo: dict, candidatos: list[dict]) -> str:
    fontes = "\n".join(
        f"| `{fonte['ingresso_id']}` | {escapar_tabela(fonte['titulo'])} | {fonte['duracao']} | `{fonte['sha256_derivado']}` |"
        for fonte in lote["fontes"]
    )
    blocos = []
    for candidato in candidatos:
        evidencias = "\n".join(
            f"| `{evidencia['evidencia_id']}` | `{evidencia['ingresso_id']}` · `{evidencia['unidade']}` "
            f"(linha {evidencia['linha']}) | `{evidencia['grafia_encontrada']}` | {escapar_tabela(evidencia['excerto'])} |"
            for evidencia in candidato["evidencias_representativas"]
        )
        blocos.append(
            f"### `{candidato['codigo']}` — {candidato['nome']}\n\n"
            f"- categoria: {candidato['categoria']} · {candidato['subcategoria']};\n"
            f"- sinais literais: **{candidato['sinais_exatos']}** em **{candidato['fontes_com_sinal']}** fonte(s);\n"
            "- estado: **PENDENTE-DE-DECISAO-CURATORIAL**.\n\n"
            "| Evidência | Endereço no derivado | Grafia encontrada | Excerto literal de triagem |\n"
            "|---|---|---|---|\n"
            f"{evidencias}\n\n"
        )
    corpo_candidatos = "".join(blocos) if blocos else "Nenhum sinal literal não ambíguo da Base foi indexado neste lote.\n"
    return f"""# Dossiê curatorial — {lote['lote_id']}

**Data de geração:** {resumo['gerado_em']}

**Eixo:** {lote['eixo']['nome']} (`{lote['eixo']['codigo']}`)
**Duração estimada:** {lote['duracao_estimada']}
**Estado:** **AGUARDANDO-DESPACHO-CURATORIAL**

## Escopo e trava

Este dossiê abrange **{resumo['fontes']}** ingresso(s) alocado(s) por despacho
curatorial explícito e **{resumo['candidatos']}** candidato(s) de cotejo. A
entrada é exclusivamente `{ONDA}/derivados_normalizados/` e os manifestos
selados da onda; conteúdos STT brutos abertos nesta etapa: **0**.

A alocação de eixo não foi inferida por palavras-chave. Os sinais abaixo são
apenas ocorrências literais de grafias canônicas já existentes na Base, usadas
para ordenar a leitura humana. Não confirmam áudio, não são citações prontas e
não criam ciclo, ficha, termo, relação ou apostila.

## Fontes do lote

| Ingresso | Título | Duração | SHA-256 do derivado |
|---|---|---:|---|
{fontes}

## Candidatos de cotejo — máximo {MAX_CANDIDATOS_POR_LOTE}

{corpo_candidatos}## Leitura do despacho

1. Deliberar cada candidato no template, em bloco.
2. `AUTORIZAR-COTEJO-AMPLIADO` permite aprofundar evidência apenas no derivado.
3. Sem despacho posterior explícito, nenhuma fonte entra em `ciclo.toml` e o
   `motor.py` permanece vedado.
"""


def readme_triagem(lotes: list[dict], resumos: list[dict]) -> str:
    por_lote = {resumo["lote_id"]: resumo for resumo in resumos}
    linhas = "\n".join(
        f"| `{lote['lote_id']}` | `{lote['eixo']['codigo']}` | {lote['duracao_estimada']} | "
        f"{len(lote['fontes'])} | {por_lote[lote['lote_id']]['candidatos']} | `{lote['estado']}` |"
        for lote in lotes
    )
    return f"""# Triagem curatorial — {ONDA}

A alocação abaixo foi declarada pelo Curador, sem classificação automática. Cada
subdiretório contém uma fila de sinais literais no derivado e um template para
despacho. Nenhum desses artefatos altera a Base ou abre ciclo do Motor.

| Lote | Eixo | Duração | Ingressos | Candidatos | Estado |
|---|---|---:|---:|---:|---|
{linhas}

A entrada operacional permanece limitada a `{ONDA}/derivados_normalizados/` e
aos manifestos da mesma onda. Os STT brutos e `normalizados_stt_dry_run/` não
foram abertos nem usados como fonte de leitura nesta etapa.
"""


def mapa_markdown(documentos: list[Documento], lotes: list[dict], gerado_em: str) -> str:
    por_id = {documento.ingresso_id: documento for documento in documentos}
    linhas = []
    for lote in lotes:
        for fonte in lote["fontes"]:
            documento = por_id[fonte["ingresso_id"]]
            linhas.append(
                f"| `{documento.ingresso_id}` | {escapar_tabela(documento.titulo)} | "
                f"`{lote['eixo']['codigo']}` | `{lote['lote_id']}` | {documento.duracao} |"
            )
    lotes_tabela = "\n".join(
        f"| `{lote['lote_id']}` | `{lote['eixo']['codigo']}` | {len(lote['fontes'])} | "
        f"{lote['duracao_estimada']} | {lote['quantidade_candidatos']}/{MAX_CANDIDATOS_POR_LOTE} |"
        for lote in lotes
    )
    return f"""# Mapeamento curatorial de eixos — {ONDA}

**Data:** {gerado_em}
**Executor:** `{EXECUTOR}`
**Fundamento:** alocação explícita do Curador, formalizada sem inferência automática.

## Mapa de ingressos

| Ingresso | Título | Eixo alocado | Lote de triagem | Duração |
|---|---|---|---|---:|
{chr(10).join(linhas)}

## Lotes preparados

| Lote | Eixo | Ingressos | Duração | Candidatos de cotejo |
|---|---|---:|---:|---:|
{lotes_tabela}

## Guardas de escopo

- a leitura operacional usou apenas os seis derivados normalizados e seus manifestos;
- conteúdos em `uploads_recepcao/` abertos: **0**;
- uso ou escrita no diretório histórico `normalizados_stt_dry_run/`: **0**;
- ciclos, fichas, termos, relações, apostilas e mutações em `dados_termos.py`: **0**;
- cada dossiê segue aguardando despacho humano antes de qualquer cotejo ampliado ou abertura de ciclo.
"""


def publicar(
    lotes: list[dict], documentos: list[Documento], linhas: list[dict], indice: list[dict],
    integridade: dict[str, object], termos: list[TermoBase], aliases_ambiguos: int, force: bool,
) -> None:
    if SAIDA.exists() and not force:
        raise FileExistsError(f"Saída já existe: {SAIDA.relative_to(RAIZ)}/. Use --force para recriar apenas a triagem da onda.")
    if SAIDA.resolve() == DERIVADOS.resolve() or DERIVADOS.resolve() in SAIDA.resolve().parents:
        raise FalhaTriagem("A saída de triagem não pode coincidir com os derivados")
    gerado_em = data_geracao()
    hashes = {
        "manifesto-fontes.json": sha256_arquivo(MANIFESTO_FONTES),
        "manifesto-derivados.json": sha256_arquivo(MANIFESTO_DERIVADOS),
        "rastreio-antes-depois.jsonl": sha256_arquivo(RASTREIO),
        "dados_termos.py": sha256_arquivo(DADOS_TERMOS),
    }
    por_id = {documento.ingresso_id: documento for documento in documentos}
    resumos: list[dict] = []

    with tempfile.TemporaryDirectory(prefix=".triagem-", dir=RAIZ_ONDA) as temporario:
        estagio = Path(temporario) / "triagem_curatorial"
        estagio.mkdir()
        escrever_jsonl(
            estagio / "registro-mestre.jsonl",
            (
                {
                    "ingresso_id": documento.ingresso_id,
                    "estado": "APTO-PARA-TRIAGEM-SEM-MUTAR-BASE",
                    "natureza_fonte": "TRANSCRICAO-STT-NORMALIZADA-DERIVADA",
                    "arquivo_derivado": documento.caminho_derivado,
                    "sha256_derivado": documento.sha256_derivado,
                    "bytes_derivado": documento.bytes_derivado,
                    "origem_declarada": {
                        "sha256_fonte": documento.sha256_fonte,
                        "verificacao": "manifesto-fonte ↔ manifesto-derivado ↔ hash-atual-do-derivado",
                    },
                    "normalizacao": {"trocas_rastreadas": documento.trocas_normalizacao},
                    "metadados": {
                        "titulo": documento.titulo,
                        "data_publicacao_original": documento.data_publicacao_original,
                        "id_youtube": documento.id_youtube,
                        "duracao": documento.duracao,
                    },
                    "proxima_etapa_permitida": "despacho curatorial por lote; motor.py somente após autorização posterior",
                }
                for documento in documentos
            ),
        )
        escrever_jsonl(estagio / "mapa-linhas.jsonl", linhas)
        escrever_jsonl(estagio / "indice-termos-base.jsonl", indice)
        (estagio / "lotes-planejados.json").write_text(
            json.dumps(lotes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )

        for lote in lotes:
            resumo, candidatos, ocorrencias = preparar_dossie(lote, por_id, indice, hashes, gerado_em)
            resumos.append(resumo)
            pasta = estagio / lote["lote_id"]
            pasta.mkdir()
            (pasta / "DOSSIE-CURATORIAL.md").write_text(
                dossie_markdown(lote, resumo, candidatos), encoding="utf-8", newline="\n"
            )
            (pasta / "candidatos-cotejo.json").write_text(
                json.dumps(candidatos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
            )
            escrever_jsonl(pasta / "ocorrencias-candidatos.jsonl", ocorrencias)
            (pasta / "DESPACHO-CURATORIAL-TEMPLATE.json").write_text(
                json.dumps(template_despacho(resumo, candidatos), ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            (pasta / "resumo-triagem.json").write_text(
                json.dumps(resumo, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
                newline="\n",
            )

        resumo_mapa = {
            "onda": ONDA,
            "gerado_em": gerado_em,
            "executor": EXECUTOR,
            "alocacao": "despacho curatorial explícito; sem classificação automática",
            "integridade": integridade,
            "base_terminologica": {
                "termos_lidos": len(termos),
                "aliases_ambiguos_excluidos": aliases_ambiguos,
                "ocorrencias_exatas_indexadas": len(indice),
            },
            "mapeamento": {
                "ingressos": len(documentos),
                "eixos": len(lotes),
                "lotes": len(lotes),
                "enderecos_de_linha": len(linhas),
                "candidatos_de_cotejo": sum(resumo["candidatos"] for resumo in resumos),
            },
            "hashes_entrada_e_base_lida": hashes,
            "barreiras": {
                "fontes_brutas_abertas": 0,
                "ciclos_criados": 0,
                "fichas_criadas": 0,
                "termos_criados": 0,
                "relacoes_criadas": 0,
                "apostilas_criadas": 0,
                "dados_termos_alterado": False,
            },
        }
        (estagio / "resumo-mapeamento.json").write_text(
            json.dumps(resumo_mapa, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (estagio / "README.md").write_text(
            readme_triagem(lotes, resumos), encoding="utf-8", newline="\n"
        )

        anterior = RAIZ_ONDA / ".triagem_curatorial-anterior"
        if anterior.exists():
            shutil.rmtree(anterior)
        if SAIDA.exists():
            SAIDA.rename(anterior)
        try:
            estagio.rename(SAIDA)
        except Exception:
            if SAIDA.exists():
                shutil.rmtree(SAIDA)
            if anterior.exists():
                anterior.rename(SAIDA)
            raise
        else:
            if anterior.exists():
                shutil.rmtree(anterior)

    mapa_json = {
        "onda": ONDA,
        "gerado_em": gerado_em,
        "executor": EXECUTOR,
        "fundamento": "alocação explícita do Curador; sem inferência automática",
        "lotes": [
            {
                "lote_id": lote["lote_id"],
                "eixo": lote["eixo"],
                "ingressos": [fonte["ingresso_id"] for fonte in lote["fontes"]],
                "duracao_estimada": lote["duracao_estimada"],
                "dossie": f"{ONDA}/triagem_curatorial/{lote['lote_id']}/DOSSIE-CURATORIAL.md",
            }
            for lote in lotes
        ],
    }
    mapa_tmp = RAIZ_ONDA / ".mapeamento-eixos.json.tmp"
    mapa_tmp.write_text(json.dumps(mapa_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(mapa_tmp, MAPA_JSON)
    mapa_md_tmp = RAIZ_ONDA / ".MAPEAMENTO-EIXOS-CURATORIAL.md.tmp"
    mapa_md_tmp.write_text(mapa_markdown(documentos, lotes, gerado_em), encoding="utf-8", newline="\n")
    os.replace(mapa_md_tmp, MAPA_MD)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="recria somente os mapas e a triagem desta onda")
    args = parser.parse_args()
    try:
        documentos, integridade, buffers = carregar_documentos()
        termos = carregar_termos_base()
        padrao, por_alias, aliases_ambiguos = compilar_indice(termos)
        linhas, ocorrencias = indexar(documentos, padrao, por_alias)
        lotes = planejar_lotes(documentos, ocorrencias)
        publicar(lotes, documentos, linhas, ocorrencias, integridade, termos, aliases_ambiguos, args.force)
        # Confirma que nenhum derivado operacional foi alterado durante a triagem.
        for arquivo, antes in buffers.items():
            if (DERIVADOS / arquivo).read_bytes() != antes:
                raise FalhaTriagem(f"Violação: derivado alterado durante a triagem: {arquivo}")
        print(
            "OK — mapeamento incremental concluído: "
            f"{len(documentos)} ingressos · {len(lotes)} eixos/lotes · "
            f"{sum(lote['quantidade_candidatos'] for lote in lotes)} candidatos de cotejo · 0 mutações da Base"
        )
        return 0
    except (FalhaTriagem, FileExistsError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
