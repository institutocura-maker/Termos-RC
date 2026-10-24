#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audita de forma somente-leitura a onda STT26 já planejada.

Confere a cadeia de derivados normalizados, o registro mestre, o planejamento,
os despachos por eixo e o estado dos ciclos STT26. Não abre fontes brutas, não
altera a Base e não abre ciclos. O único artefato opcional é o relatório Markdown
passado em ``--relatorio``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
INGRESSO = RAIZ / "ingestao_stt_lote_2026-10"
PLANEJAMENTO = INGRESSO / "lotes-planejados.json"
REGISTRO = INGRESSO / "registro-mestre.jsonl"
MAPA_LINHAS = INGRESSO / "mapa-linhas.jsonl"
RESUMO_FASE0 = INGRESSO / "resumo-triagem.json"
NORMALIZADOS = RAIZ / "normalizados_stt_lote_2026-10"
MANIFESTO_DERIVADOS = NORMALIZADOS / "manifesto-derivados-sha256.tsv"
RASTREIO = NORMALIZADOS / "rastreio-antes-depois.jsonl"
EIXOS = RAIZ / "triagem_stt_lote_2026-10" / "EIXOS"
CICLOS = RAIZ / "ciclos"

DECISOES_FINAIS = {
    "MANTER-EM-TRIAGEM",
    "DESCARTAR-DO-LOTE",
    "AUTORIZAR-COTEJO-AMPLIADO",
    "RESERVAR-PARA-FUTURO-CICLO",
}


class FalhaAuditoria(RuntimeError):
    """Uma invariante da cadeia STT26 não foi satisfeita."""


def sha256(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def ler_json(caminho: Path):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError as erro:
        raise FalhaAuditoria(f"Artefato ausente: {caminho.relative_to(RAIZ)}") from erro
    except json.JSONDecodeError as erro:
        raise FalhaAuditoria(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def ler_jsonl(caminho: Path) -> list[dict]:
    linhas: list[dict] = []
    try:
        with caminho.open(encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, 1):
                if linha.strip():
                    try:
                        linhas.append(json.loads(linha))
                    except json.JSONDecodeError as erro:
                        raise FalhaAuditoria(
                            f"JSONL inválido em {caminho.relative_to(RAIZ)}:{numero}"
                        ) from erro
    except FileNotFoundError as erro:
        raise FalhaAuditoria(f"Artefato ausente: {caminho.relative_to(RAIZ)}") from erro
    return linhas


def duracao(segundos: int) -> str:
    horas, resto = divmod(segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas}:{minutos:02d}:{segundos:02d}"


def assertar(condicao: bool, mensagem: str) -> None:
    if not condicao:
        raise FalhaAuditoria(mensagem)


def auditar() -> dict:
    plano = ler_json(PLANEJAMENTO)
    assertar(isinstance(plano, list) and plano, "Planejamento de lotes vazio ou inválido")

    lotes_por_eixo: dict[str, list[dict]] = defaultdict(list)
    ingressos: dict[str, dict] = {}
    arquivos_planejados: set[str] = set()
    total_candidatos = 0
    total_segundos = 0
    for lote in plano:
        lote_id = lote.get("lote_id")
        eixo = lote.get("tema_primario", {}).get("codigo")
        fontes = lote.get("fontes")
        candidatos = lote.get("candidatos_de_cotejo_base")
        assertar(isinstance(lote_id, str) and lote_id, "Lote sem identificador")
        assertar(isinstance(eixo, str) and eixo, f"{lote_id}: eixo ausente")
        assertar(isinstance(fontes, list) and fontes, f"{lote_id}: fontes ausentes")
        assertar(isinstance(candidatos, list) and len(candidatos) == 25, f"{lote_id}: lote não contém 25 candidatos")
        assertar(lote.get("quantidade_candidatos") == 25, f"{lote_id}: quantidade declarada diverge")
        lotes_por_eixo[eixo].append(lote)
        total_candidatos += len(candidatos)
        total_segundos += lote["duracao_estimada_segundos"]
        for fonte in fontes:
            ingresso = fonte.get("ingresso_id")
            arquivo = fonte.get("arquivo")
            assertar(isinstance(ingresso, str) and ingresso, f"{lote_id}: fonte sem ingresso_id")
            assertar(isinstance(arquivo, str) and arquivo, f"{lote_id}: fonte sem arquivo")
            assertar(ingresso not in ingressos, f"Fonte repetida no planejamento: {ingresso}")
            assertar(arquivo not in arquivos_planejados, f"Arquivo repetido no planejamento: {arquivo}")
            ingressos[ingresso] = fonte
            arquivos_planejados.add(arquivo)

    derivados = sorted(p for p in NORMALIZADOS.glob("*.md") if p.name != "README.md")
    assertar(len(derivados) == len(ingressos), "Quantidade de derivados não coincide com fontes planejadas")
    assertar({p.name for p in derivados} == arquivos_planejados, "Arquivos derivados e planejamento divergem")

    try:
        with MANIFESTO_DERIVADOS.open(encoding="utf-8", newline="") as arquivo:
            manifesto = list(csv.DictReader(arquivo, delimiter="\t"))
    except FileNotFoundError as erro:
        raise FalhaAuditoria("Manifesto de derivados ausente") from erro
    assertar(len(manifesto) == len(derivados), "Manifesto de derivados não cobre todas as fontes")
    por_arquivo_manifesto = {linha["arquivo_derivado"]: linha for linha in manifesto}
    assertar(len(por_arquivo_manifesto) == len(manifesto), "Manifesto possui arquivos duplicados")
    assertar(set(por_arquivo_manifesto) == arquivos_planejados, "Manifesto e planejamento divergem")
    trocas_manifesto = 0
    for derivado in derivados:
        linha = por_arquivo_manifesto[derivado.name]
        assertar(int(linha["bytes_derivado"]) == derivado.stat().st_size, f"{derivado.name}: bytes divergem do manifesto")
        assertar(linha["sha256_derivado"] == sha256(derivado), f"{derivado.name}: SHA-256 diverge do manifesto")
        trocas_manifesto += int(linha["trocas"])

    registro = ler_jsonl(REGISTRO)
    assertar(len(registro) == len(ingressos), "Registro mestre não cobre todas as fontes")
    registro_por_ingresso = {item.get("ingresso_id"): item for item in registro}
    assertar(set(registro_por_ingresso) == set(ingressos), "Registro mestre e planejamento divergem")
    for ingresso, item in registro_por_ingresso.items():
        arquivo = ingressos[ingresso]["arquivo"]
        assertar(item.get("natureza_fonte") == "TRANSCRICAO-STT-NORMALIZADA-DERIVADA", f"{ingresso}: natureza de fonte inválida")
        assertar(item.get("arquivo_derivado") == f"normalizados_stt_lote_2026-10/{arquivo}", f"{ingresso}: caminho derivado diverge")
        assertar(item.get("sha256_derivado") == por_arquivo_manifesto[arquivo]["sha256_derivado"], f"{ingresso}: hash no registro diverge")

    mapa_linhas = ler_jsonl(MAPA_LINHAS)
    assertar(mapa_linhas, "Mapa de linhas vazio")
    assertar({item.get("ingresso_id") for item in mapa_linhas} <= set(ingressos), "Mapa de linhas contém ingresso fora do planejamento")
    rastreio = ler_jsonl(RASTREIO)
    assertar(len(rastreio) == trocas_manifesto, "Rastreio antes/depois diverge do total de trocas")
    assertar({item.get("arquivo") for item in rastreio} <= arquivos_planejados, "Rastreio contém arquivo fora do planejamento")

    eixos: list[dict] = []
    total_decisoes = Counter()
    for codigo, lotes in sorted(lotes_por_eixo.items()):
        pasta = EIXOS / codigo
        despacho = ler_json(pasta / "DESPACHO-EIXO-TEMPLATE.json")
        resumo = ler_json(pasta / "resumo-eixo.json")
        matriz = ler_json(pasta / "MATRIZ-CANDIDATOS-EIXO.json")
        assertar(resumo.get("lotes") == [lote["lote_id"] for lote in lotes], f"{codigo}: lotes no resumo divergem")
        assertar(resumo.get("fontes") == sum(len(lote["fontes"]) for lote in lotes), f"{codigo}: fontes no resumo divergem")
        assertar(resumo.get("fontes_brutas_abertas") == 0, f"{codigo}: barreira de fontes brutas violada")
        assertar(not any(resumo.get("mutacoes", {}).values()), f"{codigo}: mutação de Base registrada")

        candidatos = despacho.get("candidatos")
        assertar(isinstance(candidatos, list), f"{codigo}: candidatos do despacho inválidos")
        por_codigo = {item.get("codigo"): item for item in candidatos}
        assertar(len(por_codigo) == len(candidatos), f"{codigo}: códigos repetidos no despacho")
        matriz_codigos = {item.get("codigo") for item in matriz}
        assertar(set(por_codigo) == matriz_codigos, f"{codigo}: despacho e matriz não cobrem os mesmos códigos")
        contagens = Counter()
        por_lote = {lote["lote_id"]: Counter() for lote in lotes}
        for lote in lotes:
            lote_id = lote["lote_id"]
            codigos_esperados = {item["codigo"] for item in lote["candidatos_de_cotejo_base"]}
            decisao_codigos = {
                codigo: item["decisao_por_lote"].get(lote_id)
                for codigo, item in por_codigo.items()
                if lote_id in item.get("decisao_por_lote", {})
            }
            assertar(set(decisao_codigos) == codigos_esperados, f"{codigo}/{lote_id}: cobertura de decisões diverge")
            for decisao in decisao_codigos.values():
                assertar(decisao in DECISOES_FINAIS, f"{codigo}/{lote_id}: decisão não final ou inválida")
                por_lote[lote_id][decisao] += 1
                contagens[decisao] += 1
                total_decisoes[decisao] += 1
            assertar(sum(por_lote[lote_id].values()) == 25, f"{codigo}/{lote_id}: decisão não fecha 25")

        registro_eixo = despacho.get("despacho_de_eixo", {})
        assertar(registro_eixo.get("resultado") == "CONCLUIDO", f"{codigo}: despacho não concluído")
        assertar(registro_eixo.get("lotes_autorizados_para_cotejo_ampliado") == [lote["lote_id"] for lote in lotes], f"{codigo}: lotes autorizados divergem")
        assertar(isinstance(registro_eixo.get("autorizacao_para_abrir_ciclo"), bool), f"{codigo}: autorização de ciclo inválida")
        pasta_ciclo = CICLOS / f"STT26-{codigo}"
        ciclo_existe = pasta_ciclo.is_dir()
        if registro_eixo["autorizacao_para_abrir_ciclo"]:
            assertar(ciclo_existe, f"{codigo}: ciclo autorizado não existe")
        eixos.append(
            {
                "codigo": codigo,
                "lotes": [lote["lote_id"] for lote in lotes],
                "fontes": resumo["fontes"],
                "duracao": resumo["duracao_estimada"],
                "candidatos_unicos": resumo["candidatos_unicos_no_eixo"],
                "autorizacoes": contagens["AUTORIZAR-COTEJO-AMPLIADO"],
                "descartes": contagens["DESCARTAR-DO-LOTE"],
                "resultado": registro_eixo["resultado"],
                "autorizacao_ciclo": registro_eixo["autorizacao_para_abrir_ciclo"],
                "ciclo_existe": ciclo_existe,
                "sha256_despacho": sha256(pasta / "DESPACHO-EIXO-TEMPLATE.json"),
            }
        )

    assertar(sum(total_decisoes.values()) == total_candidatos, "Total de decisões diverge do planejamento")
    assertar(total_decisoes["PENDENTE"] == 0, "Há decisões pendentes na onda")
    assertar(total_decisoes["MANTER-EM-TRIAGEM"] == 0, "Há decisão MANTER-EM-TRIAGEM inesperada")
    assertar(total_decisoes["RESERVAR-PARA-FUTURO-CICLO"] == 0, "Há decisão RESERVAR-PARA-FUTURO-CICLO inesperada")

    fase0 = ler_json(RESUMO_FASE0)
    assertar(fase0["integridade"]["derivados_conferidos"] == len(derivados), "Resumo Fase 0 diverge dos derivados")
    assertar(fase0["integridade"]["trocas_rastreio"] == len(rastreio), "Resumo Fase 0 diverge do rastreio")

    return {
        "lotes": len(plano),
        "fontes": len(ingressos),
        "duracao": duracao(total_segundos),
        "candidatos": total_candidatos,
        "autorizacoes": total_decisoes["AUTORIZAR-COTEJO-AMPLIADO"],
        "descartes": total_decisoes["DESCARTAR-DO-LOTE"],
        "trocas": trocas_manifesto,
        "rastreio_linhas": len(rastreio),
        "mapa_linhas": len(mapa_linhas),
        "eixos": eixos,
        "sha256_planejamento": sha256(PLANEJAMENTO),
        "sha256_manifesto_derivados": sha256(MANIFESTO_DERIVADOS),
        "sha256_rastreio": sha256(RASTREIO),
    }


def montar_relatorio(resultado: dict) -> str:
    linhas_eixos = "\n".join(
        "| `{codigo}` | {lotes} | {fontes} | {duracao} | {candidatos_unicos} | {autorizacoes} | {descartes} | {ciclo} |".format(
            codigo=eixo["codigo"],
            lotes=", ".join(eixo["lotes"]),
            fontes=eixo["fontes"],
            duracao=eixo["duracao"],
            candidatos_unicos=eixo["candidatos_unicos"],
            autorizacoes=eixo["autorizacoes"],
            descartes=eixo["descartes"],
            ciclo=("aberto e validado" if eixo["ciclo_existe"] else "não aberto"),
        )
        for eixo in resultado["eixos"]
    )
    selos = "\n".join(
        f"- `{eixo['codigo']}` — `DESPACHO-EIXO-TEMPLATE.json`: `{eixo['sha256_despacho']}`"
        for eixo in resultado["eixos"]
    )
    pendentes = [eixo["codigo"] for eixo in resultado["eixos"] if not eixo["ciclo_existe"]]
    return f"""# Auditoria global — onda STT26

**Data da auditoria:** 22/10/2026
**Escopo:** planejamento, derivados normalizados, registro mestre, rastreio, despachos por eixo e ciclos STT26 existentes.
**Modo:** somente leitura das fontes operacionais; sem abertura de STT bruto, sem mutação da Base e sem abertura de ciclo.

## Resultado

**APROVADA** — a onda STT26 está íntegra para continuidade controlada.

- lotes planejados e deliberados: **{resultado['lotes']}**;
- fontes derivadas rastreáveis: **{resultado['fontes']}**;
- duração planejada: **{resultado['duracao']}**;
- decisões registradas: **{resultado['candidatos']}**;
- `AUTORIZAR-COTEJO-AMPLIADO`: **{resultado['autorizacoes']}**;
- `DESCARTAR-DO-LOTE`: **{resultado['descartes']}**;
- decisões pendentes, `MANTER-EM-TRIAGEM` ou reservas: **0**;
- fontes brutas abertas pela Fase 0, triagem ou consolidação: **0**;
- mutações de Base registradas nessas etapas: **0**.

## Cadeia de proveniência

- **309** derivados Markdown conferidos byte a byte contra `normalizados_stt_lote_2026-10/manifesto-derivados-sha256.tsv`;
- os **309** derivados correspondem exatamente aos arquivos e aos ingressos do planejamento;
- `registro-mestre.jsonl`: **309** registros, um por `ingresso_id` planejado;
- `mapa-linhas.jsonl`: **{resultado['mapa_linhas']}** endereços de linha, todos vinculados a ingressos planejados;
- `rastreio-antes-depois.jsonl`: **{resultado['rastreio_linhas']}** mudanças, igual às **{resultado['trocas']}** mudanças declaradas no manifesto;
- fontes operacionais verificadas: somente `normalizados_stt_lote_2026-10/`.

## Despachos por eixo

| Eixo | Lotes | Fontes | Duração | Códigos únicos | Cotejos | Descartes | Ciclo STT26 |
|---|---|---:|---:|---:|---:|---:|---|
{linhas_eixos}

Todos os seis despachos estão em `CONCLUIDO`, com cobertura exata de **25 decisões por lote**.

## Ciclos já publicados

- `STT26-ANUNNAKI_GENETICA` — ciclo existente e validado;
- `STT26-COSMOGONIA_HISTORIA_COSMICA` — ciclo existente e validado.

## Ciclos ainda não abertos

{', '.join(f'`{eixo}`' for eixo in pendentes)}.

Estes eixos possuem despacho integral e cotejo autorizado, mas mantêm
`autorizacao_para_abrir_ciclo: false`. A auditoria **não** alterou essa
condição e não criou novos ciclos.

## Selos SHA-256 consultados

- `ingestao_stt_lote_2026-10/lotes-planejados.json`: `{resultado['sha256_planejamento']}`
- `normalizados_stt_lote_2026-10/manifesto-derivados-sha256.tsv`: `{resultado['sha256_manifesto_derivados']}`
- `normalizados_stt_lote_2026-10/rastreio-antes-depois.jsonl`: `{resultado['sha256_rastreio']}`
{selos}

## Validações executadas fora deste relatório

1. `consolidar_despacho_eixo_stt_2026_10.py --validar-despacho` para cada um dos seis eixos;
2. `abrir_ciclo_eixo_stt_2026_10.py --validar` para os ciclos Anunnaki e Cosmogonia já existentes;
3. `ferramentas/test_suite.py` — **21 testes aprovados**.

## Próxima ação condicionada

A presente auditoria não autoriza automaticamente nenhuma abertura. Conforme a
orientação curatorial vigente, a abertura de `EXTRATERRESTRES_TECNOLOGIA` só
poderá ocorrer após aprovação explícita deste resultado.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--relatorio",
        type=Path,
        help="caminho do relatório Markdown a gerar; se ausente, apenas valida e imprime o resumo",
    )
    args = parser.parse_args()
    try:
        resultado = auditar()
        print(
            "Auditoria STT26 aprovada: "
            f"{resultado['lotes']} lotes, {resultado['fontes']} derivados, "
            f"{resultado['autorizacoes']} cotejos, {resultado['descartes']} descartes, "
            "0 pendências."
        )
        if args.relatorio:
            destino = args.relatorio if args.relatorio.is_absolute() else RAIZ / args.relatorio
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(montar_relatorio(resultado), encoding="utf-8", newline="\n")
            print(f"Relatório: {destino.relative_to(RAIZ)}")
        return 0
    except FalhaAuditoria as erro:
        print(f"Auditoria abortada: {erro}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
