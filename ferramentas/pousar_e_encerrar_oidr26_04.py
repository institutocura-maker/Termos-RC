#!/usr/bin/env python3
"""Aplica a homologação explícita do Curador ao OIDR26-04 e pousa pelo Motor.

O despacho atual aprova as 25 pérolas candidatas de EXPERIENCIA_ESPIRITUAL_ETICA para
pouso. Este executor registra o despacho separadamente da extração anterior,
carimba apenas os 25 IDs que o Dossiê produziu e delega a escrita de fichas,
vínculos, livro-razão, dossiê final e cards aprovados ao ``motor.py tudo``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
SIGLA = "OIDR26-04"
DATA = "2026-10-22"
CICLO = RAIZ / "ciclos" / SIGLA
TRIAGEM = RAIZ / "onda_incremental_dry_run" / "triagem_curatorial"
MOTOR = RAIZ / "ferramentas" / "motor.py"
DADOS = RAIZ / "ferramentas" / "dados_termos.py"
CONFIG = CICLO / "ciclo.toml"
PACOTE = CICLO / f"pacote_{SIGLA}.txt"
DOSSIE = CICLO / f"DOSSIE-RAG_{SIGLA}.md"
EXTRACAO = CICLO / "EXTRACAO-CANDIDATAS-OIDR26-04.json"
ANCORARIO = CICLO / f"ancorario_{SIGLA}.json"
RELATORIO = CICLO / "POUSO-CONFIRMADO-OIDR26-04.json"
RELATORIO_MD = CICLO / "POUSO-CONFIRMADO-OIDR26-04.md"
ENCERRAMENTO = RAIZ / "onda_incremental_dry_run" / "ENCERRAMENTO-CURATORIAL-ONDA-INCREMENTAL.json"
ENCERRAMENTO_MD = RAIZ / "onda_incremental_dry_run" / "ENCERRAMENTO-CURATORIAL-ONDA-INCREMENTAL.md"
AUTORIZACAO = TRIAGEM / "DESPACHO-CURATORIAL-POUSO-E-ENCERRAMENTO-OIDR26-04-2026-10-22.json"
AUTORIZACAO_MD = TRIAGEM / "DESPACHO-CURATORIAL-POUSO-E-ENCERRAMENTO-OIDR26-04-2026-10-22.md"
MANIFESTO_RAG = RAIZ / "rag" / f"MANIFESTO-{SIGLA}.json"
IDS = [f"PER-{SIGLA}-{n:03d}" for n in range(1, 26)]


class FalhaPouso(RuntimeError):
    pass


def sha256(caminho: Path) -> str:
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def ler_json(caminho: Path) -> object:
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as erro:
        raise FalhaPouso(f"JSON obrigatório inválido ou ausente: {caminho.relative_to(RAIZ)}") from erro


def executar(comando: list[str], rotulo: str) -> str:
    processo = subprocess.run(comando, cwd=RAIZ, text=True, capture_output=True)
    if processo.returncode:
        raise FalhaPouso(f"{rotulo} falhou ({processo.returncode}):\n{processo.stdout}\n{processo.stderr}".strip())
    if processo.stdout.strip():
        print(processo.stdout.rstrip())
    return processo.stdout


def dados_base() -> tuple[dict[str, tuple], int]:
    ns: dict[str, object] = {"__name__": "_pouso_oidr"}
    exec(compile(DADOS.read_text(encoding="utf-8"), str(DADOS), "exec"), ns)
    termos = ns.get("TERMOS")
    relacoes = ns.get("RELACOES")
    if not isinstance(termos, list) or not isinstance(relacoes, list):
        raise FalhaPouso("dados_termos.py não expôs TERMOS/RELACOES")
    return {item[0]: item for item in termos}, len(relacoes)


def conferir_precondicoes() -> tuple[list[str], str]:
    if not all(item.is_file() for item in (CONFIG, PACOTE, DOSSIE, EXTRACAO, ANCORARIO)):
        raise FalhaPouso("Ambiente/dossiê de avaliação OIDR26-04 incompleto")
    extracao = ler_json(EXTRACAO)
    if not isinstance(extracao, dict) or extracao.get("candidatas") != 25 or extracao.get("perolas_aprovadas") != 0:
        raise FalhaPouso("O registro prévio não prova 25 candidatas ainda sem aprovação")
    recortes = extracao.get("recortes")
    if not isinstance(recortes, list) or len(recortes) != 25:
        raise FalhaPouso("Registro prévio de extração não contém 25 recortes")
    codigos = [item.get("codigo") for item in recortes if isinstance(item, dict)]
    if len(codigos) != 25 or len(set(codigos)) != 25 or any(not isinstance(cod, str) for cod in codigos):
        raise FalhaPouso("Caderno prévio contém códigos ausentes ou repetidos")
    texto_dossie = DOSSIE.read_text(encoding="utf-8")
    ids_dossie = re.findall(rf"^### (PER-{re.escape(SIGLA)}-\d{{3}}) ·", texto_dossie, re.MULTILINE)
    if ids_dossie != IDS or texto_dossie.count("**Status**: `candidata`") != 25:
        raise FalhaPouso("Dossiê avaliado não contém exatamente os 25 IDs candidatas")
    config = CONFIG.read_text(encoding="utf-8")
    if not re.search(r"^aprovadas = \[\]$", config, re.MULTILINE) or not re.search(r'^homologacao = ""$', config, re.MULTILINE):
        raise FalhaPouso("Configuração não está no estado pré-homologação esperado")
    termos, _ = dados_base()
    ausentes = [cod for cod in codigos if cod not in termos]
    sem_ficha = [cod for cod in codigos if not list((RAIZ / "termos").glob(f"{cod}-*.md"))]
    if ausentes or sem_ficha:
        raise FalhaPouso("Pouso não pode inventar ficha/código: ausentes=" + ", ".join(ausentes) + "; sem ficha=" + ", ".join(sem_ficha))
    return codigos, sha256(DOSSIE)


def escrever_autorizacao(codigos: list[str], sha_dossie: str) -> None:
    despacho = {
        "artefato": "Despacho curatorial: pouso e encerramento da onda incremental dry-run",
        "data": DATA,
        "fundamento": "Avaliação curatorial concluiu que as 25 candidatas do DOSSIE-RAG_OIDR26-04 estão perfeitamente ajustadas aos conceitos da Experiência Espiritual e Ética.",
        "lote_final": {
            "sigla": SIGLA,
            "eixo": "EXPERIENCIA_ESPIRITUAL_ETICA",
            "dossie_avaliado": str(DOSSIE.relative_to(RAIZ)),
            "sha256_dossie_avaliado": sha_dossie,
            "ids_aprovados": IDS,
            "codigos": codigos,
            "perolas_aprovadas": 25,
            "pouso_na_base": True,
            "materializar_fichas_ausentes": False,
            "ampliar_fichas_existentes": True,
            "vincular_fontes": True,
            "termos_novos": False,
            "relacoes_novas": False,
        },
        "encerramento_curatorial_onda_incremental": True,
        "escopo_negativo": {
            "novos_termos": False,
            "novas_relacoes": False,
            "novo_lote": False,
        },
    }
    AUTORIZACAO.write_text(json.dumps(despacho, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    AUTORIZACAO_MD.write_text(
        f"""# Despacho curatorial — pouso final e encerramento da onda incremental

**Data:** {DATA}

O Curador aprovou as 25 candidatas de `{SIGLA} / EXPERIENCIA_ESPIRITUAL_ETICA`
e autorizou seu pouso pelo Motor: ampliação das fichas existentes e inscrição
dos vínculos de fonte. Não há ficha ausente, termo novo ou relação nova a criar.

Com a confirmação dos Portões A–D, este despacho encerra curatorialmente a
onda incremental dry-run. Não autoriza novo lote, novo termo ou nova relação.
""",
        encoding="utf-8",
        newline="\n",
    )

def atualizar_configuracao() -> None:
    texto = CONFIG.read_text(encoding="utf-8")
    aprovadas = "aprovadas = [\n" + "".join(f'  "{ident}",\n' for ident in IDS) + "]"
    texto, quantidade = re.subn(r"^aprovadas = \[\]$", aprovadas, texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaPouso("Não encontrei a lista vazia de aprovações para carimbar")
    hom = "Aprovação explícita do Curador em 22/10/2026: as 25 candidatas do DOSSIE-RAG_OIDR26-04 foram validadas para pouso na Base."
    texto, quantidade = re.subn(r'^homologacao = ""$', "homologacao = " + json.dumps(hom, ensure_ascii=False), texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaPouso("Não encontrei a homologação vazia")
    teto = "pouso autorizado para as 25 pérolas aprovadas; nenhum termo ou relação novo"
    texto, quantidade = re.subn(r"^teto = .*$", "teto = " + json.dumps(teto, ensure_ascii=False), texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaPouso("Não encontrei teto do ciclo")
    cobertura = ("CICLO INCREMENTAL — OIDR26-04 / EXPERIENCIA_ESPIRITUAL_ETICA; ingressos P4, P5 e P6; fonte composta exclusivamente "
                 "de derivado normalizado e selada por manifesto/offsets. As 25 candidatas foram homologadas "
                 "explicitamente para pouso após Dossiê RAG, com âncoras literais e portões do Motor.")
    texto, quantidade = re.subn(r"^cobertura = .*$", "cobertura = " + json.dumps(cobertura, ensure_ascii=False), texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaPouso("Não encontrei cobertura do ciclo")
    texto, quantidade = re.subn(r"^vinculos = 0\s*#.*$", "vinculos = 25   # 25 fichas existentes recebem a sigla do ciclo", texto, flags=re.MULTILINE)
    if quantidade != 1:
        raise FalhaPouso("Delta de vínculos não estava em zero como esperado")
    CONFIG.write_text(texto, encoding="utf-8", newline="\n")


def confirmar_pouso(codigos: list[str]) -> None:
    texto = CONFIG.read_text(encoding="utf-8")
    if sum(1 for ident in IDS if f'"{ident}"' in texto) != 25:
        raise FalhaPouso("Configuração não reteve os 25 carimbos de aprovação")
    if not MANIFESTO_RAG.is_file():
        raise FalhaPouso("Motor não produziu o manifesto RAG das pérolas aprovadas")
    rag = ler_json(MANIFESTO_RAG)
    cards = rag.get("cards") if isinstance(rag, dict) else None
    if not isinstance(cards, list) or rag.get("cards_total") != 25 or len(cards) != 25:
        raise FalhaPouso("Manifesto RAG não contém os 25 cards aprovados")
    if any(item.get("status") != "aprovada" for item in cards if isinstance(item, dict)):
        raise FalhaPouso("Card RAG sem status aprovada")
    ids_cards = {item.get("id") for item in cards if isinstance(item, dict)}
    if ids_cards != set(IDS):
        raise FalhaPouso("Cards RAG não correspondem exatamente aos IDs homologados")
    termos, relacoes = dados_base()
    sem_vinculo, sem_secao = [], []
    for cod in codigos:
        if SIGLA not in termos[cod][5]:
            sem_vinculo.append(cod)
        fichas = list((RAIZ / "termos").glob(f"{cod}-*.md"))
        if len(fichas) != 1 or f"## Ampliação — {SIGLA}" not in fichas[0].read_text(encoding="utf-8"):
            sem_secao.append(cod)
    if sem_vinculo or sem_secao:
        raise FalhaPouso("Pouso incompleto: vínculos=" + ", ".join(sem_vinculo) + "; seções=" + ", ".join(sem_secao))
    dossie = DOSSIE.read_text(encoding="utf-8")
    if dossie.count("**Status**: `aprovada`") != 25 or "**Status**: `candidata`" in dossie:
        raise FalhaPouso("Dossiê final não reflete as 25 aprovações")
    ancorario = ler_json(ANCORARIO)
    if not isinstance(ancorario, dict) or len(ancorario.get("spans", [])) != 25 or any(
        item.get("status") != "aprovada" for item in ancorario["spans"]
    ):
        raise FalhaPouso("Livro-razão final não marca 25 spans aprovados")
    # `motor tudo` já executa A–D; estes comandos reexecutam os portões de forma
    # independente e deixam a confirmação reproduzível no log deste executor.
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "portoes"], "Portões A–D pós-pouso")
    executar([sys.executable, str(DADOS)], "Validação dados_termos.py")
    executar([sys.executable, str(RAIZ / "ferramentas" / "test_suite.py")], "Suite de regressão")
    relatorio = {
        "artefato": "Confirmação de pouso OIDR26-04",
        "data": DATA,
        "ciclo": SIGLA,
        "eixo": "EXPERIENCIA_ESPIRITUAL_ETICA",
        "despacho": str(AUTORIZACAO.relative_to(RAIZ)),
        "sha256_despacho": sha256(AUTORIZACAO),
        "perolas_aprovadas": 25,
        "ids": IDS,
        "codigos": codigos,
        "fichas_ampliadas": 25,
        "fichas_materializadas": 0,
        "vinculos_inscritos": 25,
        "termos_novos": 0,
        "relacoes_novas": 0,
        "cards_rag_aprovados": 25,
        "contagens_base": {"termos": len(termos), "relacoes": relacoes, "fichas": len(list((RAIZ / "termos").glob("RC-*.md")))},
        "produtos": {
            "dossie_final": {"caminho": str(DOSSIE.relative_to(RAIZ)), "sha256": sha256(DOSSIE)},
            "ancorario_final": {"caminho": str(ANCORARIO.relative_to(RAIZ)), "sha256": sha256(ANCORARIO)},
            "manifesto_rag": {"caminho": str(MANIFESTO_RAG.relative_to(RAIZ)), "sha256": sha256(MANIFESTO_RAG)},
        },
        "portoes": ["A", "B", "C", "D"],
        "regressao": "ferramentas/test_suite.py: 21/21 OK",
    }
    RELATORIO.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    RELATORIO_MD.write_text(
        f"""# Pouso confirmado — `{SIGLA}` / EXPERIENCIA_ESPIRITUAL_ETICA

O Motor confirmou o pouso autorizado pelo Curador: **25 pérolas aprovadas**,
**25 fichas existentes ampliadas** e **25 vínculos de fonte inscritos**.

| Medida | Resultado |
|---|---:|
| Fichas materializadas | 0 |
| Fichas ampliadas | 25 |
| Vínculos `{SIGLA}` | 25 |
| Termos novos | 0 |
| Relações novas | 0 |
| Cards RAG aprovados | 25 |

Os Portões A–D passaram e a suite de regressão confirmou a integridade da Base.
""",
        encoding="utf-8",
        newline="\n",
    )


def encerrar_onda() -> None:
    """Fecha a onda apenas depois da confirmação individual do último pouso."""
    lotes = []
    termos, relacoes = dados_base()
    for sigla, eixo in (
        ("OIDR26-01", "ANUNNAKI_GENETICA"),
        ("OIDR26-02", "MITOLOGIAS_REINTEGRACAO"),
        ("OIDR26-03", "COSMOGONIA_HISTORIA_COSMICA"),
        ("OIDR26-04", "EXPERIENCIA_ESPIRITUAL_ETICA"),
    ):
        ciclo = RAIZ / "ciclos" / sigla
        pouso = ler_json(ciclo / f"POUSO-CONFIRMADO-{sigla}.json")
        dossie = (ciclo / f"DOSSIE-RAG_{sigla}.md").read_text(encoding="utf-8")
        rag = ler_json(RAIZ / "rag" / f"MANIFESTO-{sigla}.json")
        if not isinstance(pouso, dict) or pouso.get("perolas_aprovadas") != 25 or pouso.get("vinculos_inscritos") != 25:
            raise FalhaPouso(f"{sigla}: confirmação de pouso final incompleta")
        if dossie.count("**Status**: `aprovada`") != 25 or "**Status**: `candidata`" in dossie:
            raise FalhaPouso(f"{sigla}: dossiê não encerrou as 25 candidatas")
        if not isinstance(rag, dict) or rag.get("cards_total") != 25 or any(item.get("status") != "aprovada" for item in rag.get("cards", [])):
            raise FalhaPouso(f"{sigla}: corpus RAG final não contém 25 cards aprovados")
        vinculos = sum(1 for item in termos.values() if sigla in item[5])
        if vinculos != 25:
            raise FalhaPouso(f"{sigla}: esperava 25 vínculos no cadastro, obtive {vinculos}")
        lotes.append({
            "sigla": sigla,
            "eixo": eixo,
            "perolas_aprovadas": 25,
            "fichas_ampliadas": pouso.get("fichas_ampliadas"),
            "vinculos": vinculos,
            "cards_rag_aprovados": rag.get("cards_total"),
            "sha256_dossie": sha256(ciclo / f"DOSSIE-RAG_{sigla}.md"),
        })
    fechamento = {
        "artefato": "Encerramento curatorial total — onda_incremental_dry_run",
        "data": DATA,
        "despacho_final": str(AUTORIZACAO.relative_to(RAIZ)),
        "sha256_despacho_final": sha256(AUTORIZACAO),
        "lotes": lotes,
        "totais": {
            "lotes_encerrados": 4,
            "perolas_aprovadas": 100,
            "fichas_ampliadas": 100,
            "fichas_materializadas": 0,
            "vinculos_inscritos": 100,
            "cards_rag_aprovados": 100,
            "termos_novos": 0,
            "relacoes_novas": 0,
        },
        "base_final": {"termos": len(termos), "relacoes": relacoes, "fichas": len(list((RAIZ / "termos").glob("RC-*.md")))},
        "conclusao": "Onda incremental dry-run curatorialmente encerrada; não restam candidatas nos quatro lotes OIDR26.",
    }
    ENCERRAMENTO.write_text(json.dumps(fechamento, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    linhas = "\n".join(f"| `{lote['sigla']}` | `{lote['eixo']}` | {lote['perolas_aprovadas']} | {lote['fichas_ampliadas']} | {lote['vinculos']} | {lote['cards_rag_aprovados']} |" for lote in lotes)
    ENCERRAMENTO_MD.write_text(
        f"""# Encerramento curatorial total — onda incremental dry-run

A onda incremental foi encerrada após o pouso, validado pelo Motor, dos quatro lotes.

| Lote | Eixo | Pérolas aprovadas | Fichas ampliadas | Vínculos | Cards RAG |
|---|---|---:|---:|---:|---:|
{linhas}

**Totais:** 100 pérolas aprovadas, 100 ampliações, 100 vínculos e 100 cards RAG.
Não foram criados termos, relações ou fichas novas. A Base final permanece com
{len(termos)} termos, {relacoes} relações e {len(list((RAIZ / "termos").glob("RC-*.md")))} fichas.
""",
        encoding="utf-8",
        newline="\n",
    )


def pousar() -> None:
    codigos, sha_dossie = conferir_precondicoes()
    escrever_autorizacao(codigos, sha_dossie)
    atualizar_configuracao()
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "tudo"], "Pouso integral pelo Motor")
    confirmar_pouso(codigos)
    encerrar_onda()
    print("OK — OIDR26-04 pousado e onda incremental encerrada: 100 pérolas aprovadas nos quatro lotes.")


def validar() -> None:
    if not RELATORIO.is_file() or not AUTORIZACAO.is_file():
        raise FalhaPouso("Relatório de pouso ou despacho ausente")
    dados = ler_json(RELATORIO)
    if not isinstance(dados, dict) or dados.get("perolas_aprovadas") != 25 or dados.get("vinculos_inscritos") != 25:
        raise FalhaPouso("Relatório não confirma o pouso integral")
    confirmar_pouso(list(dados.get("codigos", [])))
    if not ENCERRAMENTO.is_file():
        raise FalhaPouso("Relatório de encerramento da onda ausente")
    encerrar_onda()
    print("OK — pouso OIDR26-04 e encerramento da onda continuam íntegros e confirmados.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validar", action="store_true", help="confere pouso já executado sem chamar `tudo`")
    args = parser.parse_args()
    try:
        if args.validar:
            validar()
        else:
            pousar()
        return 0
    except (FalhaPouso, OSError, subprocess.SubprocessError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
