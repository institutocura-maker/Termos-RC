#!/usr/bin/env python3
"""Abre e sela os quatro ciclos da onda_incremental_dry_run via Motor Único.

Este executor registra a autorização expressa de abertura recebida em 22/10/2026,
compõe cada ``original.txt`` exclusivamente a partir dos derivados selados da
onda e chama ``motor.py novo`` para criar o andaime oficial. A abertura mantém
Delta Zero: não materializa, amplia, vira ficha, vincula ou altera a Base.

Uso:
    python3 ferramentas/abrir_ciclos_onda_incremental_dry_run.py
    python3 ferramentas/abrir_ciclos_onda_incremental_dry_run.py --validar
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
ONDA = "onda_incremental_dry_run"
RAIZ_ONDA = RAIZ / ONDA
TRIAGEM = RAIZ_ONDA / "triagem_curatorial"
DERIVADOS = RAIZ_ONDA / "derivados_normalizados"
MANIFESTO_DERIVADOS = RAIZ_ONDA / "manifesto-derivados.json"
CONSOLIDADO = TRIAGEM / "CONSOLIDADO-DESPACHO-CURATORIAL.json"
AUTORIZACAO_JSON = TRIAGEM / "AUTORIZACAO-ABERTURA-DE-CICLOS-2026-10-22.json"
AUTORIZACAO_MD = TRIAGEM / "AUTORIZACAO-ABERTURA-DE-CICLOS-2026-10-22.md"
CICLOS = RAIZ / "ciclos"
MOTOR = RAIZ / "ferramentas" / "motor.py"
DATA = "2026-10-22"
DATA_FONTE = "22/10/2026"
EXECUTOR = "ferramentas/abrir_ciclos_onda_incremental_dry_run.py"

# Ordem, eixos e lotes expressamente autorizados pelo Curador nesta mensagem.
CICLOS_AUTORIZADOS = (
    ("OIDR26-01", "ANUNNAKI_GENETICA", "Anunnaki, genética e humanidade", ("P1",)),
    ("OIDR26-02", "MITOLOGIAS_REINTEGRACAO", "Mitologias, tradições e reintegração", ("P2",)),
    ("OIDR26-03", "COSMOGONIA_HISTORIA_COSMICA", "Cosmogonia e história cósmica", ("P3",)),
    ("OIDR26-04", "EXPERIENCIA_ESPIRITUAL_ETICA", "Experiência espiritual e ética evolutiva", ("P4", "P5", "P6")),
)


class FalhaAbertura(RuntimeError):
    """Nenhum ciclo deve nascer se a origem, o despacho ou o Delta Zero falhar."""


def sha256_bytes(conteudo: bytes) -> str:
    return hashlib.sha256(conteudo).hexdigest()


def sha256_arquivo(caminho: Path) -> str:
    return sha256_bytes(caminho.read_bytes())


def ler_json(caminho: Path) -> object:
    if not caminho.is_file():
        raise FalhaAbertura(f"Artefato obrigatório ausente: {caminho.relative_to(RAIZ)}")
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise FalhaAbertura(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def executar(comando: list[str], rotulo: str) -> str:
    resultado = subprocess.run(comando, cwd=RAIZ, capture_output=True, text=True)
    if resultado.returncode:
        raise FalhaAbertura(
            f"{rotulo} falhou ({resultado.returncode}):\n"
            f"{resultado.stdout}\n{resultado.stderr}".strip()
        )
    if resultado.stdout.strip():
        print(resultado.stdout.rstrip())
    return resultado.stdout


def baseline_commit() -> str:
    resultado = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=RAIZ, capture_output=True, text=True)
    if resultado.returncode or not resultado.stdout.strip():
        raise FalhaAbertura("Não foi possível obter o commit-base do Delta")
    return resultado.stdout.strip()


def medir_base() -> dict[str, object]:
    dados = RAIZ / "ferramentas" / "dados_termos.py"
    namespace: dict[str, object] = {"__name__": "_abertura_oidr"}
    try:
        exec(compile(dados.read_text(encoding="utf-8"), str(dados), "exec"), namespace)
    except Exception as erro:
        raise FalhaAbertura(f"dados_termos.py não pode ser medido: {erro}") from erro
    termos = namespace.get("TERMOS")
    relacoes = namespace.get("RELACOES")
    if not isinstance(termos, list) or not isinstance(relacoes, list):
        raise FalhaAbertura("Base terminológica não expôs TERMOS/RELACOES")
    return {
        "sha256_dados_termos": sha256_arquivo(dados),
        "termos": len(termos),
        "relacoes": len(relacoes),
        "ficha_true": sum(1 for item in termos if len(item) > 7 and item[7] is True),
        "arquivos_ficha": len(list((RAIZ / "termos").glob("RC-*.md"))),
    }


def carregar_fontes() -> tuple[dict[str, dict], dict[str, bytes]]:
    manifesto = ler_json(MANIFESTO_DERIVADOS)
    if not isinstance(manifesto, dict) or not isinstance(manifesto.get("derivados"), list):
        raise FalhaAbertura("Manifesto de derivados inválido")
    derivados = manifesto["derivados"]
    if len(derivados) != 6:
        raise FalhaAbertura("A onda deveria conter exatamente seis derivados")
    por_id: dict[str, dict] = {}
    buffers: dict[str, bytes] = {}
    for posicao, item in enumerate(sorted(derivados, key=lambda dado: str(dado.get("arquivo", ""))), 1):
        if not isinstance(item, dict) or not isinstance(item.get("arquivo"), str):
            raise FalhaAbertura("Manifesto contém item derivado inválido")
        ingresso = f"P{posicao}"
        arquivo = item["arquivo"]
        caminho = DERIVADOS / arquivo
        conteudo = caminho.read_bytes()
        if len(conteudo) != item.get("bytes_derivado") or sha256_bytes(conteudo) != item.get("sha256_derivado"):
            raise FalhaAbertura(f"{ingresso}: derivado diverge do manifesto selado")
        por_id[ingresso] = {
            "ingresso_id": ingresso,
            "arquivo_derivado": f"{ONDA}/derivados_normalizados/{arquivo}",
            "titulo": _campo_yaml(conteudo.decode("utf-8"), "titulo", arquivo),
            "duracao": _campo_yaml(conteudo.decode("utf-8"), "duracao", arquivo),
            "sha256_derivado": item["sha256_derivado"],
            "bytes_payload": len(conteudo),
        }
        buffers[ingresso] = conteudo
    if set(por_id) != {"P1", "P2", "P3", "P4", "P5", "P6"}:
        raise FalhaAbertura("A indexação de P1…P6 falhou")
    return por_id, buffers


def _campo_yaml(texto: str, chave: str, arquivo: str) -> str:
    frente = re.match(r"\A---[ \t]*\r?\n.*?^---[ \t]*(?:\r?\n|\Z)", texto, re.DOTALL | re.MULTILINE)
    if not frente:
        raise FalhaAbertura(f"{arquivo}: frontmatter ausente")
    achado = re.search(rf"^{re.escape(chave)}:[ \t]*([^\r\n]*?)[ \t]*\r?$", frente.group(0), re.MULTILINE)
    if not achado:
        raise FalhaAbertura(f"{arquivo}: metadado {chave!r} ausente")
    valor = achado.group(1).strip()
    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in {"'", '"'}:
        valor = valor[1:-1]
    return valor


def carregar_despacho() -> tuple[list[dict], str]:
    """Confere as 100 decisões anteriores e a nova autorização explícita de abertura."""
    consolidado = ler_json(CONSOLIDADO)
    if not isinstance(consolidado, dict):
        raise FalhaAbertura("Consolidado curatorial não é objeto")
    totais = consolidado.get("totais")
    if totais != {"lotes": 4, "candidatos": 100, "autorizados_para_cotejo_ampliado": 100, "descartados": 0}:
        raise FalhaAbertura("Consolidado não contém as 100 autorizações esperadas")
    if consolidado.get("autorizacao", {}).get("cotejo_ampliado") is not True:
        raise FalhaAbertura("Cotejo ampliado não está autorizado")
    if consolidado.get("autorizacao", {}).get("abertura_de_ciclo") is not False:
        raise FalhaAbertura("Consolidado anterior deveria registrar a abertura como nova autorização separada")

    planejamento = ler_json(TRIAGEM / "lotes-planejados.json")
    if not isinstance(planejamento, list) or len(planejamento) != 4:
        raise FalhaAbertura("Planejamento incremental inválido")
    por_lote = {item.get("lote_id"): item for item in planejamento if isinstance(item, dict)}
    if set(por_lote) != {item[0] for item in CICLOS_AUTORIZADOS}:
        raise FalhaAbertura("Planejamento não contém exatamente os quatro lotes autorizados")

    lotes: list[dict] = []
    for sigla, eixo, nome_eixo, ingressos in CICLOS_AUTORIZADOS:
        lote = por_lote[sigla]
        if lote.get("eixo", {}).get("codigo") != eixo or tuple(f.get("ingresso_id") for f in lote.get("fontes", [])) != ingressos:
            raise FalhaAbertura(f"{sigla}: eixo ou ingressos divergem da autorização")
        template = ler_json(TRIAGEM / sigla / "DESPACHO-CURATORIAL-TEMPLATE.json")
        candidatos = template.get("candidatos") if isinstance(template, dict) else None
        if not isinstance(candidatos, list) or len(candidatos) != 25:
            raise FalhaAbertura(f"{sigla}: template não contém 25 decisões")
        if any(item.get("decisao") != "AUTORIZAR-COTEJO-AMPLIADO" for item in candidatos):
            raise FalhaAbertura(f"{sigla}: há deliberação fora da autorização integral")
        final = template.get("despacho_de_lote")
        codigos = [item.get("codigo") for item in candidatos]
        if not isinstance(final, dict) or final.get("resultado") != "CONCLUIDO" or final.get("candidatos_para_cotejo_ampliado") != codigos:
            raise FalhaAbertura(f"{sigla}: fechamento de cotejo divergente")
        if final.get("autorizacao_para_abrir_ciclo") is not False:
            raise FalhaAbertura(f"{sigla}: template histórico não pode inventar a nova autorização")
        lotes.append({
            "sigla": sigla,
            "eixo": eixo,
            "nome_eixo": nome_eixo,
            "ingressos": list(ingressos),
            "candidatos": codigos,
            "sha256_template_cotejo": sha256_arquivo(TRIAGEM / sigla / "DESPACHO-CURATORIAL-TEMPLATE.json"),
        })
    return lotes, sha256_arquivo(CONSOLIDADO)


def compor_fonte(lote: dict, fontes: dict[str, dict], buffers: dict[str, bytes]) -> tuple[bytes, list[dict]]:
    cabecalho = (
        "# FONTE OPERACIONAL CONSOLIDADA — ONDA INCREMENTAL DRY RUN\n"
        f"# CICLO: {lote['sigla']}\n"
        f"# EIXO: {lote['eixo']}\n"
        f"# LOTE: {lote['sigla']}\n"
        "# NATUREZA: composição de transcrições STT normalizadas derivadas; não contém STT bruto.\n"
        "# PROVENIÊNCIA: cada payload declara ingresso, caminho e SHA-256; offsets são registrados no manifesto.\n\n"
    ).encode("utf-8")
    saida = bytearray(cabecalho)
    manifesto: list[dict] = []
    for ordem, ingresso in enumerate(lote["ingressos"], 1):
        fonte = fontes[ingresso]
        inicio = (
            f"\n===== INÍCIO FONTE {ordem:02d} · {ingresso} · {lote['sigla']} =====\n"
            f"arquivo_derivado: {fonte['arquivo_derivado']}\n"
            f"sha256_derivado: {fonte['sha256_derivado']}\n"
            f"titulo: {fonte['titulo']}\n"
            f"duracao: {fonte['duracao']}\n"
            "===== CONTEÚDO DERIVADO BYTE-A-BYTE =====\n"
        ).encode("utf-8")
        saida.extend(inicio)
        inicio_payload = len(saida)
        saida.extend(buffers[ingresso])
        fim_payload = len(saida)
        saida.extend(f"\n===== FIM FONTE {ordem:02d} · {ingresso} =====\n".encode("utf-8"))
        manifesto.append({
            "ordem": ordem,
            "ingresso_id": ingresso,
            "arquivo_derivado": fonte["arquivo_derivado"],
            "titulo": fonte["titulo"],
            "duracao": fonte["duracao"],
            "sha256_derivado": fonte["sha256_derivado"],
            "bytes_payload": len(buffers[ingresso]),
            "inicio_byte_payload": inicio_payload,
            "fim_byte_exclusivo_payload": fim_payload,
        })
    return bytes(saida), manifesto


def reconfigurar_ciclo(ciclo_toml: Path, lote: dict, sha_fonte: str, baseline: str) -> None:
    texto = ciclo_toml.read_text(encoding="utf-8")
    valores = {
        "titulo": f"Onda incremental dry-run — {lote['nome_eixo']} (derivados normalizados)",
        "data_fonte": DATA_FONTE,
        "pacote": f"pacote_{lote['sigla']}.txt",
        "sha256_fonte": sha_fonte,
        "baseline_commit": baseline,
        "cobertura": (
            f"CICLO INCREMENTAL — {lote['sigla']} / {lote['eixo']}; "
            f"ingressos {', '.join(lote['ingressos'])}; fonte composta exclusivamente de derivados "
            "normalizados e selada por manifesto/offsets. Abertura expressamente autorizada pelo Curador; "
            "25 candidatos seguem para cotejo com âncoras literais e portões do Motor."
        ),
        "teto": "25 candidatos autorizados para cotejo ampliado; pérolas dependem de recorte e homologação posterior",
    }
    for campo, valor in valores.items():
        padrao = rf"^{re.escape(campo)} = .*$"
        texto, quantidade = re.subn(padrao, f"{campo} = {json.dumps(valor, ensure_ascii=False)}", texto, flags=re.MULTILINE)
        if quantidade != 1:
            raise FalhaAbertura(f"{lote['sigla']}: campo único ausente no andaime do Motor: {campo}")
    texto, quantidade = re.subn(r"^max_perolas = \d+.*$", "max_perolas = 25", texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaAbertura(f"{lote['sigla']}: max_perolas ausente no andaime")
    ciclo_toml.write_text(texto, encoding="utf-8", newline="\n")


def registrar_autorizacao(lotes: list[dict], sha_consolidado: str, baseline: str, base: dict[str, object]) -> None:
    registro = {
        "artefato": "Autorização explícita de abertura de ciclos — onda_incremental_dry_run",
        "data": DATA,
        "fundamento": "Autorização expressa do Curador para abrir OIDR26-01, OIDR26-02, OIDR26-03 e OIDR26-04 no Motor.",
        "executor": EXECUTOR,
        "despacho_anterior": {
            "caminho": str(CONSOLIDADO.relative_to(RAIZ)),
            "sha256": sha_consolidado,
            "cotejo_ampliado_validado": 100,
            "descartes": 0,
        },
        "ciclos_autorizados": [
            {"sigla": lote["sigla"], "eixo": lote["eixo"], "ingressos": lote["ingressos"], "candidatos": len(lote["candidatos"])}
            for lote in lotes
        ],
        "escopo": {
            "abertura_de_ciclo": True,
            "cotejo_ampliado": True,
            "materializacao": False,
            "aprovacao_de_perolas": False,
            "execucao_de_tudo": False,
        },
        "baseline_commit": baseline,
        "base_no_inicio": base,
        "fontes_brutas_abertas": 0,
        "mutacoes_na_abertura": 0,
    }
    AUTORIZACAO_JSON.write_text(json.dumps(registro, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    linhas = "\n".join(
        f"| `{lote['sigla']}` | `{lote['eixo']}` | {', '.join(f'`{ingresso}`' for ingresso in lote['ingressos'])} | {len(lote['candidatos'])} |"
        for lote in lotes
    )
    AUTORIZACAO_MD.write_text(
        f"""# Autorização de abertura de ciclos — {ONDA}

**Data:** {DATA}

O Curador autorizou explicitamente a abertura, no Motor, dos quatro ciclos
abaixo após a validação das 100 deliberações de cotejo ampliado.

| Ciclo | Eixo | Ingressos | Candidatos autorizados para cotejo |
|---|---|---|---:|
{linhas}

## Limites preservados

A autorização abre os ambientes selados e permite o cotejo/recorte literal.
Ela não aprova pérolas, não materializa a Base e não autoriza `motor.py tudo`.
Qualquer pouso permanece dependente de nova avaliação e homologação curatorial.
""",
        encoding="utf-8",
        newline="\n",
    )


def abrir_lote(lote: dict, fontes: dict[str, dict], buffers: dict[str, bytes], sha_consolidado: str, baseline: str, base: dict[str, object]) -> None:
    pasta = CICLOS / lote["sigla"]
    if pasta.exists():
        raise FalhaAbertura(f"Ciclo já existe: {pasta.relative_to(RAIZ)}; use --validar")
    fonte, fontes_manifesto = compor_fonte(lote, fontes, buffers)
    with tempfile.TemporaryDirectory(prefix=f".{lote['sigla']}-") as temporario:
        entrada = Path(temporario) / f"2026-10-22_{lote['sigla']}_DERIVADOS_NORMALIZADOS.txt"
        entrada.write_bytes(fonte)
        executar([sys.executable, str(MOTOR), "--ciclo", lote["sigla"], "novo", str(entrada)], f"motor novo {lote['sigla']}")
    original = pasta / "original.txt"
    if original.read_bytes() != fonte:
        raise FalhaAbertura(f"{lote['sigla']}: Motor não preservou a fonte consolidada byte a byte")
    reconfigurar_ciclo(pasta / "ciclo.toml", lote, sha256_arquivo(original), baseline)
    manifesto = {
        "artefato": "Manifesto de origem da fonte consolidada — onda incremental dry-run",
        "gerado_em": DATA,
        "ciclo": lote["sigla"],
        "eixo": lote["eixo"],
        "ingressos": lote["ingressos"],
        "fonte_operacional": f"somente {ONDA}/derivados_normalizados/",
        "fontes_brutas_abertas": 0,
        "autorizacao_de_abertura": {
            "caminho": str(AUTORIZACAO_JSON.relative_to(RAIZ)),
            "sha256": sha256_arquivo(AUTORIZACAO_JSON),
            "despacho_cotejo_consolidado": str(CONSOLIDADO.relative_to(RAIZ)),
            "sha256_despacho_cotejo_consolidado": sha_consolidado,
            "candidatos_autorizados_para_cotejo": lote["candidatos"],
        },
        "baseline_commit": baseline,
        "base_no_inicio": base,
        "sha256_original_consolidado": sha256_arquivo(original),
        "fontes": fontes_manifesto,
        "delta_esperado": {"arquivos": 0, "ficha_true": 0, "termos": 0, "relacoes": 0, "vinculos": 0},
        "mutacoes_na_abertura": {"dados_termos_alterado": False, "fichas_criadas": 0, "termos_criados": 0, "relacoes_criadas": 0, "apostilas_criadas": 0},
    }
    (pasta / "MANIFESTO-ORIGEM-DERIVADOS.json").write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    validar_lote(lote, fontes, buffers, baseline, base, executar_portoes=True)


def validar_lote(lote: dict, fontes: dict[str, dict], buffers: dict[str, bytes], baseline: str, base: dict[str, object], executar_portoes: bool) -> None:
    pasta = CICLOS / lote["sigla"]
    original = pasta / "original.txt"
    config = pasta / "ciclo.toml"
    manifesto_path = pasta / "MANIFESTO-ORIGEM-DERIVADOS.json"
    if not all(item.is_file() for item in (original, config, manifesto_path)):
        raise FalhaAbertura(f"{lote['sigla']}: ambiente selado incompleto")
    fonte_esperada, fontes_manifesto = compor_fonte(lote, fontes, buffers)
    manifesto = ler_json(manifesto_path)
    if original.read_bytes() != fonte_esperada:
        raise FalhaAbertura(f"{lote['sigla']}: original consolidado diverge dos derivados atuais")
    if not isinstance(manifesto, dict) or manifesto.get("fontes") != fontes_manifesto:
        raise FalhaAbertura(f"{lote['sigla']}: manifesto diverge da proveniência")
    if manifesto.get("sha256_original_consolidado") != sha256_arquivo(original):
        raise FalhaAbertura(f"{lote['sigla']}: SHA da fonte não confere no manifesto")
    if manifesto.get("baseline_commit") != baseline or manifesto.get("base_no_inicio") != base:
        raise FalhaAbertura(f"{lote['sigla']}: baseline da abertura diverge")
    toml = config.read_text(encoding="utf-8")
    if f'sha256_fonte = "{sha256_arquivo(original)}"' not in toml or f'baseline_commit = "{baseline}"' not in toml:
        raise FalhaAbertura(f"{lote['sigla']}: ciclo.toml não sela fonte/baseline")
    if executar_portoes:
        # Antes de qualquer pacote de cotejo, os quatro portões podem ser aferidos sem
        # materializar ficha alguma: B e C conferem legitimamente 0 citações/0 seções.
        # Depois de iniciado o cotejo, C só volta a ser aplicável no eventual pouso —
        # exigir paridade de ficha agora obrigaria a alterar a Base, justamente o oposto
        # do Delta Zero desta abertura.
        pacote = (pasta / f"pacote_{lote['sigla']}.txt").read_text(encoding="utf-8")
        if not re.search(r"^### RC-\d{3}\s*$", pacote, re.MULTILINE):
            executar([sys.executable, str(MOTOR), "--ciclo", lote["sigla"], "portoes"],
                     f"Portões A–D pré-cotejo {lote['sigla']}")
        else:
            executar([sys.executable, str(MOTOR), "--ciclo", lote["sigla"], "entrada"], f"Portão A {lote['sigla']}")
            executar([sys.executable, str(MOTOR), "--ciclo", lote["sigla"], "verbatim"], f"Portão B {lote['sigla']}")
            executar([sys.executable, str(MOTOR), "--ciclo", lote["sigla"], "delta"], f"Portão D {lote['sigla']}")
    print(f"Ambiente {lote['sigla']} selado: {len(fontes_manifesto)} derivado(s), Delta Zero confirmado.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validar", action="store_true", help="valida os quatro ambientes já abertos, sem escrever")
    args = parser.parse_args()
    try:
        lotes, sha_consolidado = carregar_despacho()
        fontes, buffers = carregar_fontes()
        baseline = baseline_commit()
        base = medir_base()
        if args.validar:
            if not AUTORIZACAO_JSON.is_file():
                raise FalhaAbertura("Registro da autorização de abertura ausente")
            for lote in lotes:
                validar_lote(lote, fontes, buffers, baseline, base, executar_portoes=True)
            print("OK — quatro ambientes OIDR selados e Delta Zero confirmado.")
        else:
            if any((CICLOS / lote["sigla"]).exists() for lote in lotes):
                existentes = [lote["sigla"] for lote in lotes if (CICLOS / lote["sigla"]).exists()]
                raise FalhaAbertura("Ciclo já existe: " + ", ".join(existentes) + "; use --validar")
            registrar_autorizacao(lotes, sha_consolidado, baseline, base)
            for lote in lotes:
                abrir_lote(lote, fontes, buffers, sha_consolidado, baseline, base)
            print("OK — quatro ciclos OIDR abertos pelo Motor, selados e em Delta Zero.")
        return 0
    except (FalhaAbertura, subprocess.SubprocessError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
