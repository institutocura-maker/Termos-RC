#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abre, a partir de um despacho integral autorizado, o ciclo do Motor para um eixo STT.

A fonte de trabalho é uma composição rastreável de cópias normalizadas. O script não
abre os STT brutos em ``uploads_recepcao/`` e não cria pérolas, fichas, termos,
relações ou vínculos na Base. A abertura é feita pelo comando oficial ``motor.py
novo``; qualquer ampliação posterior ainda depende de âncoras literais no pacote
produzido para o ciclo e dos portões do Motor.

Uso:
    python3 ferramentas/abrir_ciclo_eixo_stt_2026_10.py --eixo ANUNNAKI_GENETICA
    python3 ferramentas/abrir_ciclo_eixo_stt_2026_10.py --eixo ANUNNAKI_GENETICA --validar
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
INGESTAO = RAIZ / "ingestao_stt_lote_2026-10"
NORMALIZADOS = RAIZ / "normalizados_stt_lote_2026-10"
TRIAGEM = RAIZ / "triagem_stt_lote_2026-10"
CICLOS = RAIZ / "ciclos"
MOTOR = RAIZ / "ferramentas" / "motor.py"
DATA_ABERTURA = "2026-10-21"


class FalhaAbertura(RuntimeError):
    """Falha de governança: não abre um ciclo parcial, ambíguo ou não autorizado."""


def sha256_bytes(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def sha256(caminho: Path) -> str:
    return sha256_bytes(caminho.read_bytes())


def ler_json(caminho: Path):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError as erro:
        raise FalhaAbertura(f"Artefato ausente: {caminho.relative_to(RAIZ)}") from erro
    except json.JSONDecodeError as erro:
        raise FalhaAbertura(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def dados_eixo(codigo_eixo: str) -> tuple[dict, list[dict], list[dict], dict]:
    """Confere despacho completo e devolve lotes/fontes, sem consultar qualquer bruto."""
    pasta_eixo = TRIAGEM / "EIXOS" / codigo_eixo
    despacho_path = pasta_eixo / "DESPACHO-EIXO-TEMPLATE.json"
    despacho = ler_json(despacho_path)
    meta = despacho.get("meta", {})
    registro = despacho.get("despacho_de_eixo", {})
    if meta.get("eixo", {}).get("codigo") != codigo_eixo:
        raise FalhaAbertura("Template de despacho não pertence ao eixo solicitado")
    if registro.get("resultado") != "CONCLUIDO":
        raise FalhaAbertura("Despacho do eixo não está concluído")
    if registro.get("autorizacao_para_abrir_ciclo") is not True:
        raise FalhaAbertura("Curadoria não autorizou a abertura do ciclo")

    planejamento = ler_json(INGESTAO / "lotes-planejados.json")
    lotes = [
        lote for lote in planejamento
        if lote.get("tema_primario", {}).get("codigo") == codigo_eixo
    ]
    ids_lotes = [lote["lote_id"] for lote in lotes]
    if meta.get("lotes") != ids_lotes:
        raise FalhaAbertura("Lotes do despacho divergem do planejamento")

    candidatos = despacho.get("candidatos")
    if not isinstance(candidatos, list) or not candidatos:
        raise FalhaAbertura("Template sem candidatos para validar")
    por_lote = {lote_id: Counter() for lote_id in ids_lotes}
    for candidato in candidatos:
        decisoes = candidato.get("decisao_por_lote")
        if not isinstance(decisoes, dict):
            raise FalhaAbertura(f"{candidato.get('codigo')}: decisões por lote inválidas")
        for lote_id, decisao in decisoes.items():
            if lote_id not in por_lote:
                raise FalhaAbertura(f"{candidato.get('codigo')}: lote alheio no despacho")
            if decisao == "PENDENTE":
                raise FalhaAbertura(f"{candidato.get('codigo')}/{lote_id}: decisão pendente")
            if decisao not in set(meta.get("opcoes", [])):
                raise FalhaAbertura(f"{candidato.get('codigo')}/{lote_id}: decisão não permitida")
            por_lote[lote_id][decisao] += 1
    if sorted(registro.get("lotes_autorizados_para_cotejo_ampliado", [])) != sorted(
        lote_id for lote_id, contagem in por_lote.items() if contagem["AUTORIZAR-COTEJO-AMPLIADO"]
    ):
        raise FalhaAbertura("Lista de lotes autorizados não corresponde ao despacho")

    registro_mestre = {}
    for linha in (INGESTAO / "registro-mestre.jsonl").read_text(encoding="utf-8").splitlines():
        item = json.loads(linha)
        registro_mestre[item["ingresso_id"]] = item

    fontes: list[dict] = []
    vistos: set[str] = set()
    for lote in lotes:
        for fonte in lote["fontes"]:
            ingresso = fonte["ingresso_id"]
            if ingresso in vistos:
                raise FalhaAbertura(f"Fonte repetida no eixo: {ingresso}")
            vistos.add(ingresso)
            registro_fonte = registro_mestre.get(ingresso)
            if not registro_fonte:
                raise FalhaAbertura(f"{ingresso}: ausente do registro-mestre")
            rel = Path(registro_fonte["arquivo_derivado"])
            if rel.parts[0] != NORMALIZADOS.name:
                raise FalhaAbertura(f"{ingresso}: caminho fora da camada normalizada")
            caminho = RAIZ / rel
            if not caminho.is_file():
                raise FalhaAbertura(f"{ingresso}: derivado ausente")
            conteudo = caminho.read_bytes()
            if sha256_bytes(conteudo) != registro_fonte["sha256_derivado"]:
                raise FalhaAbertura(f"{ingresso}: SHA-256 do derivado não confere")
            fontes.append(
                {
                    "lote_id": lote["lote_id"],
                    "ingresso_id": ingresso,
                    "arquivo_derivado": str(rel),
                    "titulo": fonte["titulo"],
                    "duracao": fonte["duracao"],
                    "sha256_derivado": registro_fonte["sha256_derivado"],
                    "conteudo": conteudo,
                }
            )
    return despacho, lotes, fontes, {"caminho": despacho_path, "sha256": sha256(despacho_path), "contagens": por_lote}


def montar_fonte(codigo_eixo: str, lotes: list[dict], fontes: list[dict]) -> tuple[bytes, list[dict]]:
    """Monta uma fonte única, com cada payload normalizado preservado byte a byte."""
    cabecalho = (
        "# FONTE OPERACIONAL CONSOLIDADA — CICLO STT\n"
        f"# EIXO: {codigo_eixo}\n"
        f"# LOTES: {', '.join(lote['lote_id'] for lote in lotes)}\n"
        "# NATUREZA: composição de transcrições STT normalizadas derivadas; não contém STT bruto.\n"
        "# PROVENIÊNCIA: cada bloco declara ingresso, caminho e SHA-256 do derivado; "
        "o manifesto do ciclo registra offsets byte a byte.\n\n"
    ).encode("utf-8")
    saida = bytearray(cabecalho)
    manifesto = []
    for ordem, fonte in enumerate(fontes, 1):
        inicio = (
            f"\n===== INÍCIO FONTE {ordem:02d} · {fonte['ingresso_id']} · {fonte['lote_id']} =====\n"
            f"arquivo_derivado: {fonte['arquivo_derivado']}\n"
            f"sha256_derivado: {fonte['sha256_derivado']}\n"
            f"titulo: {fonte['titulo']}\n"
            f"duracao: {fonte['duracao']}\n"
            "===== CONTEÚDO DERIVADO BYTE-A-BYTE =====\n"
        ).encode("utf-8")
        saida.extend(inicio)
        inicio_payload = len(saida)
        saida.extend(fonte["conteudo"])
        fim_payload = len(saida)
        fim = f"\n===== FIM FONTE {ordem:02d} · {fonte['ingresso_id']} =====\n".encode("utf-8")
        saida.extend(fim)
        manifesto.append(
            {
                "ordem": ordem,
                **{chave: fonte[chave] for chave in (
                    "lote_id", "ingresso_id", "arquivo_derivado", "titulo", "duracao", "sha256_derivado"
                )},
                "bytes_payload": len(fonte["conteudo"]),
                "inicio_byte_payload": inicio_payload,
                "fim_byte_exclusivo_payload": fim_payload,
            }
        )
    return bytes(saida), manifesto


def alterar_ciclo(ciclo_toml: Path, codigo_eixo: str, lotes: list[dict]) -> None:
    """Especializa somente os campos que o Motor reconhece no andaime oficial."""
    texto = ciclo_toml.read_text(encoding="utf-8")
    nome_eixo = lotes[0]["tema_primario"]["nome"]
    quantidade_fontes = sum(len(lote["fontes"]) for lote in lotes)
    titulo = f"Eixo STT26 — {nome_eixo} (derivados normalizados)"
    cobertura = (
        f"CICLO DE EIXO — {codigo_eixo}; lotes "
        f"{', '.join(lote['lote_id'] for lote in lotes)}; {quantidade_fontes} transcrições STT normalizadas "
        "derivadas, consolidadas com manifesto de origem e seladas no original.txt. "
        "Abertura autorizada pela Curadoria após despacho integral. O ciclo inicia sem pérolas: "
        "cada eventual aspa deverá ser cortada do derivado consolidado e passar nos portões do Motor."
    )
    substituicoes = {
        "titulo": titulo,
        "data_fonte": "21/10/2026",
        "cobertura": cobertura,
        "teto": "cotejo-autorizado; pérolas ainda dependem de âncoras e portões",
    }
    for campo, valor in substituicoes.items():
        padrao = rf"^{re.escape(campo)} = .*$"
        texto, quantidade = re.subn(padrao, f"{campo} = {json.dumps(valor, ensure_ascii=False)}", texto, flags=re.M)
        if quantidade != 1:
            raise FalhaAbertura(f"Andaime do Motor sem campo único: {campo}")
    ciclo_toml.write_text(texto, encoding="utf-8", newline="\n")


def validar_ciclo(codigo_eixo: str) -> None:
    despacho, lotes, fontes, referencia = dados_eixo(codigo_eixo)
    sigla = f"STT26-{codigo_eixo}"
    pasta = CICLOS / sigla
    manifesto_path = pasta / "MANIFESTO-ORIGEM-DERIVADOS.json"
    original = pasta / "original.txt"
    ciclo_toml = pasta / "ciclo.toml"
    if not all(caminho.is_file() for caminho in (manifesto_path, original, ciclo_toml)):
        raise FalhaAbertura("Ciclo aberto incompleto: faltam fonte, manifesto ou configuração")
    manifesto = ler_json(manifesto_path)
    fonte_esperada, fontes_manifesto = montar_fonte(codigo_eixo, lotes, fontes)
    if original.read_bytes() != fonte_esperada:
        raise FalhaAbertura("original.txt do ciclo diverge da composição atual de derivados")
    if manifesto.get("fontes") != fontes_manifesto:
        raise FalhaAbertura("Manifesto do ciclo diverge das fontes derivadas")
    if manifesto.get("sha256_original_consolidado") != sha256(original):
        raise FalhaAbertura("SHA-256 de original.txt diverge do manifesto")
    if manifesto.get("despacho", {}).get("sha256") != referencia["sha256"]:
        raise FalhaAbertura("Manifesto não aponta para o despacho atual")
    if f'sha256_fonte = "{sha256(original)}"' not in ciclo_toml.read_text(encoding="utf-8"):
        raise FalhaAbertura("ciclo.toml não sela o SHA-256 de original.txt")
    if not despacho["despacho_de_eixo"]["autorizacao_para_abrir_ciclo"]:
        raise FalhaAbertura("Despacho perdeu a autorização de abertura")
    print(
        f"Ciclo {sigla} íntegro: {len(fontes)} derivados, SHA-256 da fonte consolidada conferido, "
        "0 brutos lidos, 0 mutações de Base na abertura."
    )


def abrir(codigo_eixo: str) -> None:
    despacho, lotes, fontes, referencia = dados_eixo(codigo_eixo)
    sigla = f"STT26-{codigo_eixo}"
    pasta = CICLOS / sigla
    if pasta.exists():
        raise FalhaAbertura(f"Ciclo já existe: {pasta.relative_to(RAIZ)}; use --validar")
    fonte, fontes_manifesto = montar_fonte(codigo_eixo, lotes, fontes)
    with tempfile.TemporaryDirectory(prefix="stt-eixo-") as temporario:
        entrada = Path(temporario) / f"{DATA_ABERTURA}_STT26-{codigo_eixo}-DERIVADOS-CONSOLIDADOS.txt"
        entrada.write_bytes(fonte)
        subprocess.run(
            [sys.executable, str(MOTOR), "--ciclo", sigla, "novo", str(entrada)],
            cwd=RAIZ,
            check=True,
        )
    original = pasta / "original.txt"
    if original.read_bytes() != fonte:
        raise FalhaAbertura("Motor não preservou byte a byte a fonte consolidada")
    alterar_ciclo(pasta / "ciclo.toml", codigo_eixo, lotes)
    manifesto = {
        "artefato": "Manifesto de origem da fonte consolidada do ciclo STT",
        "gerado_em": DATA_ABERTURA,
        "eixo": codigo_eixo,
        "lotes": [lote["lote_id"] for lote in lotes],
        "fonte_operacional": "somente normalizados_stt_lote_2026-10/",
        "fontes_brutas_abertas": 0,
        "despacho": {
            "caminho": str(referencia["caminho"].relative_to(RAIZ)),
            "sha256": referencia["sha256"],
            "resultado": despacho["despacho_de_eixo"]["resultado"],
            "autorizacao_para_abrir_ciclo": despacho["despacho_de_eixo"]["autorizacao_para_abrir_ciclo"],
            "contagens_por_lote": {lote_id: dict(contagem) for lote_id, contagem in referencia["contagens"].items()},
        },
        "sha256_original_consolidado": sha256(original),
        "fontes": fontes_manifesto,
        "mutacoes_na_abertura": {
            "dados_termos_alterado": False,
            "fichas_criadas": 0,
            "termos_criados": 0,
            "relacoes_criadas": 0,
            "apostilas_criadas": 0,
        },
    }
    (pasta / "MANIFESTO-ORIGEM-DERIVADOS.json").write_text(
        json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    validar_ciclo(codigo_eixo)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eixo", required=True, help="código do eixo, p.ex. ANUNNAKI_GENETICA")
    parser.add_argument("--validar", action="store_true", help="valida um ciclo de eixo já aberto")
    args = parser.parse_args()
    try:
        if args.validar:
            validar_ciclo(args.eixo)
        else:
            abrir(args.eixo)
        return 0
    except (FalhaAbertura, subprocess.CalledProcessError) as erro:
        print(f"Abertura/validação abortada: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
