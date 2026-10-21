#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida os dossiês pendentes por eixo temático, sem decidir pela Curadoria.

O consolidado reduz a leitura repetida quando um mesmo código aparece em dois ou
mais lotes do mesmo eixo. Ele não aumenta o teto de 25 candidatos POR LOTE,
não cria pérola, não seleciona citação e não chama o Motor. A entrada continua
sendo os dossiês produzidos exclusivamente a partir dos derivados normalizados;
nenhum STT bruto é aberto.

Uso:
    python3 ferramentas/consolidar_despacho_eixo_stt_2026_10.py \
        --eixo ANUNNAKI_GENETICA
    python3 ferramentas/consolidar_despacho_eixo_stt_2026_10.py \
        --eixo ANUNNAKI_GENETICA --force

Produtos:
    triagem_stt_lote_2026-10/EIXOS/<EIXO>/DOSSIE-CURATORIAL-EIXO.md
    triagem_stt_lote_2026-10/EIXOS/<EIXO>/MATRIZ-CANDIDATOS-EIXO.json
    triagem_stt_lote_2026-10/EIXOS/<EIXO>/DESPACHO-EIXO-TEMPLATE.json
    triagem_stt_lote_2026-10/EIXOS/<EIXO>/resumo-eixo.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
INGRESSO = RAIZ / "ingestao_stt_lote_2026-10"
PLANEJAMENTO = INGRESSO / "lotes-planejados.json"
TRIAGEM = RAIZ / "triagem_stt_lote_2026-10"
EIXOS = TRIAGEM / "EIXOS"
MAX_CANDIDATOS_POR_LOTE = 25
DATA_GERACAO = "2026-10-20"
DECISOES_PERMITIDAS = (
    "MANTER-EM-TRIAGEM",
    "DESCARTAR-DO-LOTE",
    "AUTORIZAR-COTEJO-AMPLIADO",
    "RESERVAR-PARA-FUTURO-CICLO",
)
DECISOES_VALIDAS = {"PENDENTE", *DECISOES_PERMITIDAS}


class FalhaEixo(RuntimeError):
    """Falha de coerência; nenhum consolidado parcial deve ser publicado."""


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
        raise FalhaEixo(f"Artefato ausente: {caminho.relative_to(RAIZ)}") from erro
    except json.JSONDecodeError as erro:
        raise FalhaEixo(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def despacho_tem_decisoes(caminho: Path) -> bool:
    """Informa se o template já recebeu despacho humano e não pode ser refeito."""
    despacho = ler_json(caminho)
    for candidato in despacho.get("candidatos", []):
        if candidato.get("decisao_eixo") != "PENDENTE":
            return True
        if any(decisao != "PENDENTE" for decisao in candidato.get("decisao_por_lote", {}).values()):
            return True
    registro = despacho.get("despacho_de_eixo", {})
    return (
        registro.get("resultado") != "PENDENTE"
        or bool(registro.get("lotes_autorizados_para_cotejo_ampliado"))
        or registro.get("autorizacao_para_abrir_ciclo") is True
        or bool(registro.get("observacao"))
    )


def carregar_eixo(codigo_eixo: str) -> tuple[list[dict], list[dict], dict]:
    lotes = ler_json(PLANEJAMENTO)
    if not isinstance(lotes, list):
        raise FalhaEixo("Planejamento de lotes não é lista")
    selecionados = [lote for lote in lotes if lote.get("tema_primario", {}).get("codigo") == codigo_eixo]
    if not selecionados:
        disponiveis = sorted({str(lote.get("tema_primario", {}).get("codigo")) for lote in lotes})
        raise FalhaEixo(f"Eixo inexistente: {codigo_eixo}; disponíveis: {', '.join(disponiveis)}")

    entradas: list[dict] = []
    hash_referencia: dict | None = None
    todos_ingressos: set[str] = set()
    for lote in selecionados:
        lote_id = lote["lote_id"]
        pasta = TRIAGEM / lote_id
        resumo = ler_json(pasta / "resumo-triagem.json")
        candidatos = ler_json(pasta / "candidatos-cotejo.json")
        template = ler_json(pasta / "DESPACHO-CURATORIAL-TEMPLATE.json")
        if resumo.get("lote_id") != lote_id or resumo.get("estado") != "AGUARDANDO-DESPACHO-CURATORIAL":
            raise FalhaEixo(f"{lote_id}: estado de triagem inválido")
        if resumo.get("fontes_brutas_abertas") != 0 or any(resumo.get("mutacoes", {}).values()):
            raise FalhaEixo(f"{lote_id}: triagem não respeita a barreira de não mutação")
        if len(candidatos) > MAX_CANDIDATOS_POR_LOTE or len(candidatos) != resumo.get("candidatos"):
            raise FalhaEixo(f"{lote_id}: teto ou contagem de candidatos inconsistente")
        if len(template.get("candidatos", [])) != len(candidatos) or any(
            item.get("decisao") != "PENDENTE" for item in template["candidatos"]
        ):
            raise FalhaEixo(f"{lote_id}: template não está pendente e íntegro")
        ingressos = [fonte["ingresso_id"] for fonte in lote.get("fontes", [])]
        if len(ingressos) != len(set(ingressos)) or todos_ingressos.intersection(ingressos):
            raise FalhaEixo(f"{lote_id}: fonte repetida dentro do eixo")
        todos_ingressos.update(ingressos)
        hashes = resumo.get("hashes_de_entrada")
        if hash_referencia is None:
            hash_referencia = hashes
        elif hashes != hash_referencia:
            raise FalhaEixo(f"{lote_id}: hashes de entrada diferem dos demais lotes do eixo")
        entradas.append(
            {
                "lote": lote,
                "resumo": resumo,
                "candidatos": candidatos,
                "pasta": pasta,
            }
        )
    assert hash_referencia is not None
    metadados = {
        "codigo": codigo_eixo,
        "nome": selecionados[0]["tema_primario"]["nome"],
        "hash_planejamento": sha256(PLANEJAMENTO),
        "hashes_fase0": hash_referencia,
    }
    return selecionados, entradas, metadados


def matriz_candidatos(entradas: list[dict]) -> list[dict]:
    por_codigo: dict[str, list[dict]] = defaultdict(list)
    for entrada in entradas:
        lote = entrada["lote"]
        for candidato in entrada["candidatos"]:
            por_codigo[candidato["codigo"]].append(
                {
                    "lote_id": lote["lote_id"],
                    "sinais_exatos": candidato["sinais_exatos"],
                    "fontes_com_sinal": candidato["fontes_com_sinal"],
                    "evidencias_representativas": candidato["evidencias_representativas"],
                }
            )
    matriz = []
    for codigo, ocorrencias in por_codigo.items():
        primeiro = next(
            candidato
            for entrada in entradas
            for candidato in entrada["candidatos"]
            if candidato["codigo"] == codigo
        )
        matriz.append(
            {
                "codigo": codigo,
                "nome": primeiro["nome"],
                "categoria": primeiro["categoria"],
                "subcategoria": primeiro["subcategoria"],
                "classificacao_tecnica": (
                    "COMPARTILHADO-NO-EIXO" if len(ocorrencias) > 1 else "ESPECIFICO-DE-UM-LOTE"
                ),
                "lotes": sorted(ocorrencias, key=lambda item: item["lote_id"]),
                "sinais_exatos_no_eixo": sum(item["sinais_exatos"] for item in ocorrencias),
                "fontes_com_sinal_somadas": sum(item["fontes_com_sinal"] for item in ocorrencias),
                "estado": "PENDENTE-DE-DECISAO-CURATORIAL",
                "limite": (
                    "Consolidação técnica de dossiês; não converte sinais em citação, "
                    "pérola, ficha, relação ou ciclo."
                ),
            }
        )
    return sorted(matriz, key=lambda item: (-item["sinais_exatos_no_eixo"], item["codigo"]))


def resumo_eixo(lotes: list[dict], entradas: list[dict], metadados: dict, matriz: list[dict]) -> dict:
    compartilhados = sum(1 for item in matriz if item["classificacao_tecnica"] == "COMPARTILHADO-NO-EIXO")
    fontes = sum(len(lote["fontes"]) for lote in lotes)
    segundos = sum(lote["duracao_estimada_segundos"] for lote in lotes)
    horas, resto = divmod(segundos, 3600)
    minutos, segundos_restantes = divmod(resto, 60)
    return {
        "eixo": {"codigo": metadados["codigo"], "nome": metadados["nome"]},
        "gerado_em": DATA_GERACAO,
        "estado": "AGUARDANDO-DESPACHO-CURATORIAL-POR-EIXO",
        "lotes": [entrada["lote"]["lote_id"] for entrada in entradas],
        "fontes": fontes,
        "duracao_estimada_segundos": sum(lote["duracao_estimada_segundos"] for lote in lotes),
        "duracao_estimada": f"{horas}:{minutos:02d}:{segundos_restantes:02d}",
        "candidatos_por_lote": {entrada["lote"]["lote_id"]: len(entrada["candidatos"]) for entrada in entradas},
        "candidatos_unicos_no_eixo": len(matriz),
        "candidatos_compartilhados_no_eixo": compartilhados,
        "candidatos_especificos_de_lote": len(matriz) - compartilhados,
        "entrada_operacional": "somente dossiês derivados de normalizados_stt_lote_2026-10/",
        "fontes_brutas_abertas": 0,
        "mutacoes": {
            "ciclos_criados": 0,
            "fichas_criadas": 0,
            "termos_criados": 0,
            "relacoes_criadas": 0,
            "apostilas_criadas": 0,
            "dados_termos_alterado": False,
        },
        "hashes_de_entrada": {
            "lotes-planejados.json": metadados["hash_planejamento"],
            **metadados["hashes_fase0"],
        },
    }


def despacho_template(resumo: dict, matriz: list[dict]) -> dict:
    return {
        "meta": {
            "artefato": "Template de despacho curatorial por eixo STT",
            "eixo": resumo["eixo"],
            "lotes": resumo["lotes"],
            "gerado_em": DATA_GERACAO,
            "estado": "PENDENTE-CURADOR",
            "escopo": (
                "Matriz transversal: preserva o teto de 25 candidatos por lote; "
                "os códigos repetidos são vistos juntos sem fundir decisões de lote."
            ),
            "efeito_atual": "nenhum: não cria ciclo e não altera a Base",
            "opcoes": list(DECISOES_PERMITIDAS),
        },
        "candidatos": [
            {
                "codigo": item["codigo"],
                "nome": item["nome"],
                "classificacao_tecnica": item["classificacao_tecnica"],
                "decisao_eixo": "PENDENTE",
                "fundamento_curatorial": "",
                "decisao_por_lote": {
                    item_lote["lote_id"]: "PENDENTE" for item_lote in item["lotes"]
                },
                "evidencias_disponiveis": {
                    item_lote["lote_id"]: [
                        evidencia["evidencia_id"] for evidencia in item_lote["evidencias_representativas"]
                    ]
                    for item_lote in item["lotes"]
                },
                "observacao": "",
            }
            for item in matriz
        ],
        "despacho_de_eixo": {
            "resultado": "PENDENTE",
            "lotes_autorizados_para_cotejo_ampliado": [],
            "autorizacao_para_abrir_ciclo": False,
            "observacao": "",
        },
    }


def escapar(texto: str) -> str:
    return " ".join(texto.replace("|", "\\|").split())


def montar_dossie(resumo: dict, matriz: list[dict]) -> str:
    linhas = []
    for item in matriz:
        lotes = "<br>".join(
            f"`{ocorrencia['lote_id']}`: {ocorrencia['sinais_exatos']} sinal(is), "
            f"{ocorrencia['fontes_com_sinal']} fonte(s)"
            for ocorrencia in item["lotes"]
        )
        evidencias = "<br>".join(
            f"`{ocorrencia['lote_id']}`: "
            + ", ".join(f"`{evidencia['evidencia_id']}`" for evidencia in ocorrencia["evidencias_representativas"])
            for ocorrencia in item["lotes"]
        )
        linhas.append(
            f"| `{item['codigo']}` | {escapar(item['nome'])} | `{item['classificacao_tecnica']}` | "
            f"{item['sinais_exatos_no_eixo']} | {lotes} | {evidencias} |"
        )
    por_lote = " · ".join(f"`{lote}`: {quantidade}" for lote, quantidade in resumo["candidatos_por_lote"].items())
    return f"""# Dossiê curatorial por eixo — {resumo['eixo']['nome']}

**Eixo:** `{resumo['eixo']['codigo']}`
**Lotes:** {', '.join(f'`{lote}`' for lote in resumo['lotes'])}
**Duração combinada:** {resumo['duracao_estimada']}
**Estado:** **AGUARDANDO-DESPACHO-CURATORIAL-POR-EIXO**

## Finalidade e trava

Este caderno consolida candidatos repetidos nos lotes do mesmo eixo para a
Curadoria decidir com menos leitura duplicada. Ele **não mistura os limites**:
cada lote continua com no máximo 25 candidatos. O eixo contém
**{resumo['candidatos_unicos_no_eixo']} códigos únicos**: {resumo['candidatos_compartilhados_no_eixo']}
compartilhados e {resumo['candidatos_especificos_de_lote']} específicos.

A entrada operacional são apenas os dossiês derivados das cópias normalizadas.
Conteúdos brutos abertos: **0**. Este documento não cria ciclo, ficha, termo,
relação ou apostila e não altera a Base.

Use `DESPACHO-EIXO-TEMPLATE.json` para a decisão: ela mantém uma decisão por
código **e** por lote, de modo que ver um item compartilhado não o promove para
ambos automaticamente.

## Capacidade

- fontes no eixo: **{resumo['fontes']}**;
- candidatos por lote: {por_lote};
- candidatos únicos no eixo: **{resumo['candidatos_unicos_no_eixo']}**;
- candidatos compartilhados entre lotes: **{resumo['candidatos_compartilhados_no_eixo']}**.

## Matriz curatorial

| Código | Nome | Alcance | Sinais no eixo | Cobertura por lote | Evidências representativas disponíveis |
|---|---|---|---:|---|---|
{chr(10).join(linhas)}

## Próxima decisão permitida

O Curador pode registrar `MANTER-EM-TRIAGEM`, `DESCARTAR-DO-LOTE`,
`AUTORIZAR-COTEJO-AMPLIADO` ou `RESERVAR-PARA-FUTURO-CICLO`. As decisões
permanecem distintas por lote; a última não abre ciclo por si só. Qualquer
chamada futura ao `motor.py` ainda exige fonte derivada, âncoras e despacho
específico.
"""


def validar_despacho(codigo_eixo: str) -> None:
    """Valida o despacho humano sem regenerá-lo nem tocar na Base."""
    lotes, entradas, metadados = carregar_eixo(codigo_eixo)
    matriz_esperada = matriz_candidatos(entradas)
    resumo_esperado = resumo_eixo(lotes, entradas, metadados, matriz_esperada)
    destino = EIXOS / codigo_eixo
    if not destino.is_dir():
        raise FalhaEixo(f"Eixo não publicado: {destino.relative_to(RAIZ)}")

    resumo = ler_json(destino / "resumo-eixo.json")
    matriz = ler_json(destino / "MATRIZ-CANDIDATOS-EIXO.json")
    despacho = ler_json(destino / "DESPACHO-EIXO-TEMPLATE.json")
    if resumo != resumo_esperado:
        raise FalhaEixo("Resumo do eixo diverge das entradas derivadas")
    if matriz != matriz_esperada:
        raise FalhaEixo("Matriz do eixo diverge dos dossiês de lote")

    modelo = despacho_template(resumo_esperado, matriz_esperada)
    if despacho.get("meta") != modelo["meta"]:
        raise FalhaEixo("Metadados ou opções do despacho divergentes")
    candidatos = despacho.get("candidatos")
    if not isinstance(candidatos, list) or len(candidatos) != len(matriz_esperada):
        raise FalhaEixo("Quantidade de decisões diverge da matriz")
    por_codigo = {item.get("codigo"): item for item in candidatos}
    if len(por_codigo) != len(candidatos) or set(por_codigo) != {item["codigo"] for item in matriz_esperada}:
        raise FalhaEixo("Códigos do despacho não cobrem exatamente a matriz")

    contagens_por_lote: dict[str, Counter] = {lote["lote_id"]: Counter() for lote in lotes}
    for esperado in matriz_esperada:
        codigo = esperado["codigo"]
        candidato = por_codigo[codigo]
        for campo in ("codigo", "nome", "classificacao_tecnica"):
            if candidato.get(campo) != modelo["candidatos"][matriz_esperada.index(esperado)][campo]:
                raise FalhaEixo(f"{codigo}: {campo} diverge da matriz")
        decisao_eixo = candidato.get("decisao_eixo")
        if decisao_eixo not in DECISOES_VALIDAS:
            raise FalhaEixo(f"{codigo}: decisão de eixo inválida")
        por_lote = candidato.get("decisao_por_lote")
        lotes_esperados = {item["lote_id"] for item in esperado["lotes"]}
        if not isinstance(por_lote, dict) or set(por_lote) != lotes_esperados:
            raise FalhaEixo(f"{codigo}: escopo por lote diverge da matriz")
        for lote_id, decisao in por_lote.items():
            if decisao not in DECISOES_VALIDAS:
                raise FalhaEixo(f"{codigo}/{lote_id}: decisão inválida")
            contagens_por_lote[lote_id][decisao] += 1
        evidencias = candidato.get("evidencias_disponiveis")
        evidencias_esperadas = modelo["candidatos"][matriz_esperada.index(esperado)]["evidencias_disponiveis"]
        if evidencias != evidencias_esperadas:
            raise FalhaEixo(f"{codigo}: evidências disponíveis divergentes")
        if not isinstance(candidato.get("fundamento_curatorial"), str) or not isinstance(candidato.get("observacao"), str):
            raise FalhaEixo(f"{codigo}: campos curatoriais devem ser textuais")

    registro = despacho.get("despacho_de_eixo")
    if not isinstance(registro, dict) or set(registro) != {
        "resultado", "lotes_autorizados_para_cotejo_ampliado", "autorizacao_para_abrir_ciclo", "observacao"
    }:
        raise FalhaEixo("Registro final do despacho inválido")
    pendencias = sum(contagens["PENDENTE"] for contagens in contagens_por_lote.values())
    despacho_integral = pendencias == 0
    resultado_esperado = "CONCLUIDO" if despacho_integral else "PENDENTE"
    if registro["resultado"] != resultado_esperado:
        raise FalhaEixo(
            f"Resultado do eixo deve ser {resultado_esperado} para o conjunto atual de decisões"
        )
    if not despacho_integral and registro["autorizacao_para_abrir_ciclo"] is not False:
        raise FalhaEixo("O eixo parcial não pode autorizar abertura de ciclo")
    if not isinstance(registro["autorizacao_para_abrir_ciclo"], bool):
        raise FalhaEixo("Autorização para abertura de ciclo deve ser booleana")
    autorizados = registro["lotes_autorizados_para_cotejo_ampliado"]
    esperados_autorizados = sorted(
        lote_id
        for lote_id, contagens in contagens_por_lote.items()
        if contagens["AUTORIZAR-COTEJO-AMPLIADO"]
    )
    if autorizados != esperados_autorizados:
        raise FalhaEixo("Lotes autorizados para cotejo não correspondem às decisões")
    if not isinstance(registro["observacao"], str):
        raise FalhaEixo("Observação final do despacho deve ser textual")
    if resumo["fontes_brutas_abertas"] != 0 or any(resumo["mutacoes"].values()):
        raise FalhaEixo("Barreira de não mutação violada")

    detalhes = "; ".join(
        f"{lote_id}: " + ", ".join(f"{decisao}={quantidade}" for decisao, quantidade in sorted(contagens.items()))
        for lote_id, contagens in contagens_por_lote.items()
    )
    print(
        f"Despacho do eixo {codigo_eixo} íntegro: {len(candidatos)} códigos, "
        f"{resumo['fontes']} fontes derivadas, 0 fontes brutas, 0 mutações. {detalhes}"
    )


def publicar(codigo_eixo: str, resumo: dict, matriz: list[dict], force: bool) -> None:
    EIXOS.mkdir(parents=True, exist_ok=True)
    destino = EIXOS / codigo_eixo
    if destino.exists() and not force:
        raise FileExistsError(f"Eixo já publicado: {destino.relative_to(RAIZ)}; use --force para regenerar")
    if destino.exists() and despacho_tem_decisoes(destino / "DESPACHO-EIXO-TEMPLATE.json"):
        raise FalhaEixo(
            f"{codigo_eixo}: despacho humano já preenchido; regeneração bloqueada para preservá-lo"
        )
    if destino.parent.resolve() != EIXOS.resolve() or not codigo_eixo.replace("_", "").isalnum():
        raise FalhaEixo("Destino de eixo inválido")
    with tempfile.TemporaryDirectory(prefix=f".{codigo_eixo}-", dir=EIXOS) as temporario:
        estagio = Path(temporario) / codigo_eixo
        estagio.mkdir()
        (estagio / "DOSSIE-CURATORIAL-EIXO.md").write_text(
            montar_dossie(resumo, matriz), encoding="utf-8", newline="\n"
        )
        (estagio / "MATRIZ-CANDIDATOS-EIXO.json").write_text(
            json.dumps(matriz, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        (estagio / "DESPACHO-EIXO-TEMPLATE.json").write_text(
            json.dumps(despacho_template(resumo, matriz), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (estagio / "resumo-eixo.json").write_text(
            json.dumps(resumo, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )
        anterior = EIXOS / f".{codigo_eixo}-anterior"
        if anterior.exists():
            shutil.rmtree(anterior)
        if destino.exists():
            destino.rename(anterior)
        try:
            estagio.rename(destino)
        except Exception:
            if destino.exists():
                shutil.rmtree(destino)
            if anterior.exists():
                anterior.rename(destino)
            raise
        else:
            if anterior.exists():
                shutil.rmtree(anterior)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--eixo", required=True, help="código do eixo, p.ex. ANUNNAKI_GENETICA")
    parser.add_argument("--force", action="store_true", help="regenera apenas o eixo informado")
    parser.add_argument(
        "--validar-despacho",
        action="store_true",
        help="valida despacho humano já preenchido, sem regenerar artefatos",
    )
    args = parser.parse_args()
    try:
        if args.validar_despacho:
            if args.force:
                raise FalhaEixo("--force não pode ser combinado com --validar-despacho")
            validar_despacho(args.eixo)
            return 0
        lotes, entradas, metadados = carregar_eixo(args.eixo)
        matriz = matriz_candidatos(entradas)
        resumo = resumo_eixo(lotes, entradas, metadados, matriz)
        publicar(args.eixo, resumo, matriz, args.force)
        print(
            f"Eixo {args.eixo} consolidado: {len(lotes)} lotes, {resumo['fontes']} fontes, "
            f"{len(matriz)} candidatos únicos ({resumo['candidatos_compartilhados_no_eixo']} compartilhados)."
        )
        return 0
    except (FalhaEixo, FileExistsError) as erro:
        print(f"Consolidação abortada: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
