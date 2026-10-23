#!/usr/bin/env python3
"""Extrai, pelo Motor, as 25 candidatas do OIDR26-03 e gera seu DOSSIE-RAG.

A autorização vigente permite cotejo ampliado e dossiê, não homologação. Por isso este
executor usa a evidência literal normalizada como âncora de busca, chama ``motor.py busca``
para recortar a citação, deixa ``[perolas].aprovadas`` vazio e nunca chama materializar,
ampliar, vincular, rag ou tudo.

Uso:
    python3 ferramentas/extrair_dossie_oidr26_03.py
    python3 ferramentas/extrair_dossie_oidr26_03.py --validar
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
SIGLA = "OIDR26-03"
INGRESSO = "P3"
MOTOR = RAIZ / "ferramentas" / "motor.py"
DADOS_TERMOS = RAIZ / "ferramentas" / "dados_termos.py"
CICLO = RAIZ / "ciclos" / SIGLA
PACOTE = CICLO / f"pacote_{SIGLA}.txt"
DOSSIE = CICLO / f"DOSSIE-RAG_{SIGLA}.md"
ANCORARIO = CICLO / f"ancorario_{SIGLA}.json"
MANIFESTO = CICLO / "EXTRACAO-CANDIDATAS-OIDR26-03.json"
CANDIDATOS = RAIZ / "onda_incremental_dry_run" / "triagem_curatorial" / SIGLA / "candidatos-cotejo.json"
DESPACHO = RAIZ / "onda_incremental_dry_run" / "triagem_curatorial" / SIGLA / "DESPACHO-CURATORIAL-TEMPLATE.json"
AUTORIZACAO = RAIZ / "onda_incremental_dry_run" / "triagem_curatorial" / "DESPACHO-CURATORIAL-POUSO-OIDR26-02-E-EXTRACAO-OIDR26-03-2026-10-22.json"
POUSO_ANTERIOR = RAIZ / "ciclos" / "OIDR26-02" / "POUSO-CONFIRMADO-OIDR26-02.json"


class FalhaExtracao(RuntimeError):
    pass


def sha256(caminho: Path) -> str:
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def ler_json(caminho: Path) -> object:
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as erro:
        raise FalhaExtracao(f"Não foi possível ler {caminho.relative_to(RAIZ)}") from erro


def executar(comando: list[str], rotulo: str) -> str:
    resultado = subprocess.run(comando, cwd=RAIZ, capture_output=True, text=True)
    if resultado.returncode:
        raise FalhaExtracao(f"{rotulo} falhou ({resultado.returncode}):\n{resultado.stdout}\n{resultado.stderr}".strip())
    if resultado.stdout.strip():
        print(resultado.stdout.rstrip())
    return resultado.stdout


def validar_autorizacao() -> list[dict]:
    if not CICLO.is_dir() or not AUTORIZACAO.is_file() or not POUSO_ANTERIOR.is_file():
        raise FalhaExtracao("Ambiente OIDR26-03, despacho ou confirmação do pouso anterior ausente")
    registro = ler_json(AUTORIZACAO)
    if not isinstance(registro, dict) or not isinstance(registro.get("lotes"), dict):
        raise FalhaExtracao("Despacho sequencial não tem lotes legíveis")
    anterior = registro["lotes"].get("OIDR26-02")
    atual = registro["lotes"].get(SIGLA)
    if not isinstance(anterior, dict) or anterior.get("perolas_aprovadas") != 25 or anterior.get("pouso_na_base") is not True:
        raise FalhaExtracao("O despacho não confirma a autorização de pouso integral do lote anterior")
    if not isinstance(atual, dict) or atual.get("extrair_candidatas_e_gerar_dossie") is not True:
        raise FalhaExtracao("OIDR26-03 não recebeu autorização explícita de extração e dossiê")
    if atual.get("perolas_aprovadas") is not False or atual.get("materializar") is not False or atual.get("vincular") is not False:
        raise FalhaExtracao("Autorização do OIDR26-03 não preserva o bloqueio de pouso")
    pouso = ler_json(POUSO_ANTERIOR)
    if not isinstance(pouso, dict) or pouso.get("perolas_aprovadas") != 25 or pouso.get("vinculos_inscritos") != 25:
        raise FalhaExtracao("Pouso OIDR26-02 não foi confirmado antes do próximo dossiê")

    candidatos = ler_json(CANDIDATOS)
    despacho = ler_json(DESPACHO)
    if not isinstance(candidatos, list) or len(candidatos) != 25:
        raise FalhaExtracao("O arquivo de candidatas precisa conter exatamente 25 entradas")
    por_codigo = {item.get("codigo"): item for item in candidatos if isinstance(item, dict)}
    if len(por_codigo) != 25 or None in por_codigo:
        raise FalhaExtracao("Códigos candidatos ausentes ou repetidos")
    decisoes = despacho.get("candidatos") if isinstance(despacho, dict) else None
    if not isinstance(decisoes, list) or len(decisoes) != 25:
        raise FalhaExtracao("Despacho do lote não contém 25 decisões")
    if {item.get("codigo") for item in decisoes} != set(por_codigo):
        raise FalhaExtracao("Despacho e lista de candidatas não têm o mesmo caderno")
    if any(item.get("decisao") != "AUTORIZAR-COTEJO-AMPLIADO" for item in decisoes):
        raise FalhaExtracao("Há candidata sem autorização de cotejo ampliado")
    for candidato in candidatos:
        evidencias = candidato.get("evidencias_representativas")
        if not isinstance(evidencias, list) or len(evidencias) != 1:
            raise FalhaExtracao(f"{candidato.get('codigo')}: esperava uma evidência representativa")
        evidencia = evidencias[0]
        if evidencia.get("ingresso_id") != INGRESSO or not evidencia.get("grafia_encontrada") or not evidencia.get("excerto"):
            raise FalhaExtracao(f"{candidato.get('codigo')}: evidência não é literal do ingresso {INGRESSO}")
    return candidatos


def candidatos_de_ancora(excerto: str, grafia: str) -> list[str]:
    """Deriva âncoras da evidência de triagem sem usar título/frontmatter como prova.

    O excerto tem reticências apenas nas bordas quando foi resumido para a triagem. O
    recorte central, que contém a grafia encontrada, é literal. Tentamos do menor para
    o maior trecho até o Motor identificar uma única ocorrência no payload P3.
    """
    alvo = grafia.casefold()
    posicao = excerto.casefold().find(alvo)
    if posicao < 0:
        raise FalhaExtracao(f"A grafia {grafia!r} não aparece no excerto de origem")
    fim_grafia = posicao + len(grafia)
    saida: list[str] = []
    for raio in (45, 65, 90, 120, 160, 220, 320):
        inicio = max(0, posicao - raio)
        fim = min(len(excerto), fim_grafia + raio)
        trecho = excerto[inicio:fim]
        # Uma reticência é marcador de truncamento, jamais parte da âncora.
        if "…" in trecho:
            if trecho.find("…") < posicao - inicio:
                trecho = trecho[trecho.rfind("…") + 1:]
            if "…" in trecho:
                trecho = trecho[:trecho.find("…")]
        trecho = trecho.strip(" \t\r\n,;:.-")
        if len(trecho) >= max(12, len(grafia)) and grafia.casefold() in trecho.casefold() and trecho not in saida:
            saida.append(trecho)
    if not saida:
        raise FalhaExtracao(f"Não foi possível derivar âncora da evidência {grafia!r}")
    return saida


def buscar_uma_ancora(ancora: str) -> tuple[str, str, int, int]:
    """Pede ao Motor a aspa; a função não lê nem corta o original por conta própria."""
    resultado = subprocess.run(
        [sys.executable, str(MOTOR), "--ciclo", SIGLA, "busca", ancora, "1", INGRESSO],
        cwd=RAIZ,
        capture_output=True,
        text=True,
    )
    if resultado.returncode:
        raise FalhaExtracao(f"Motor não encontrou âncora {ancora!r}: {resultado.stderr.strip()}")
    cabecalho = re.search(r"^  \[1/(\d+)\] (U\d+) · chars (\d+)-(\d+) ·", resultado.stdout, re.MULTILINE)
    cita = re.search(r"^      «(.*)»$", resultado.stdout, re.MULTILINE)
    if not cabecalho or not cita:
        raise FalhaExtracao(f"Saída de busca do Motor fora do formato auditável para {ancora!r}")
    quantidade, unidade, inicio, fim = cabecalho.groups()
    if int(quantidade) != 1:
        raise FalhaExtracao(f"Âncora ainda ambígua ({quantidade} ocorrências): {ancora!r}")
    aspa = " ".join(cita.group(1).split())
    # Este filtro torna explícita a proibição de tomar título/frontmatter por evidência.
    if re.match(r"^(titulo|data_publicacao_original|canal_autor|id_youtube|link_original|duracao)\s*:", aspa, re.I):
        raise FalhaExtracao(f"Busca devolveu metadado, não fala: {ancora!r}")
    return aspa, unidade, int(inicio), int(fim)


def recortar(candidato: dict) -> dict:
    evidencia = candidato["evidencias_representativas"][0]
    grafia = str(evidencia["grafia_encontrada"])
    ultimo_erro: Exception | None = None
    for ancora in candidatos_de_ancora(str(evidencia["excerto"]), grafia):
        try:
            aspa, unidade, inicio, fim = buscar_uma_ancora(ancora)
            if grafia.casefold() not in aspa.casefold():
                raise FalhaExtracao("A aspa recortada não contém a grafia da candidata")
            return {
                "codigo": candidato["codigo"],
                "nome": candidato["nome"],
                "evidencia_id": evidencia["evidencia_id"],
                "ingresso_id": INGRESSO,
                "unidade_triagem": evidencia["unidade"],
                "unidade_motor": unidade,
                "grafia": grafia,
                "ancora_literal": ancora,
                "aspa": aspa,
                "chars": [inicio, fim],
                "sha256_aspa": hashlib.sha256(aspa.encode("utf-8")).hexdigest(),
            }
        except FalhaExtracao as erro:
            ultimo_erro = erro
    raise FalhaExtracao(f"{candidato['codigo']}: nenhuma âncora inequívoca derivada da evidência passou ({ultimo_erro})")


def escrever_pacote(recortes: list[dict]) -> None:
    # `motor novo` cria um andaime comentado; o que não pode ser sobrescrito é um
    # pacote que já tenha blocos de termo/cotejo, não esse esqueleto vazio.
    if re.search(r"^### RC-\d{3}\s*$", PACOTE.read_text(encoding="utf-8"), re.MULTILINE):
        raise FalhaExtracao("Pacote já contém cotejo; não sobrescrever extração existente")
    linhas = [
        f"# Pacote de cotejo ampliado — {SIGLA}",
        "",
        "Este pacote foi gerado por `ferramentas/extrair_dossie_oidr26_01.py`. Cada aspa foi",
        "recortada pelo Motor a partir de âncora literal da evidência normalizada do ingresso P3.",
        "As vinte e cinco entradas são candidatas: o pacote não declara aprovação, ficha, termo,",
        "relação, vínculo, materialização ou exportação de card RAG.",
        "",
        "### BLOCO 1 · Candidatas para avaliação curatorial",
        "",
    ]
    for item in recortes:
        linhas += [
            f"### {item['codigo']}",
            "",
            f"- **[{INGRESSO} · {item['nome']}]** «{item['aspa']}» ({item['unidade_motor']}) — "
            f"candidata de cotejo ampliado; evidência `{item['evidencia_id']}`, "
            f"grafia literal `{item['grafia']}`, sem homologação de pérola.",
            "",
        ]
    linhas += [
        "### BLOCO 2 · Limites do despacho",
        "",
        "* As vinte e cinco pérolas permanecem no status `candidata` até despacho curatorial posterior.",
        "* Não há cards RAG aprovados, materialização de fichas, criação de termos/relações ou vínculos de fonte.",
        "",
    ]
    PACOTE.write_text("\n".join(linhas), encoding="utf-8", newline="\n")


def conferir_produtos(recortes: list[dict]) -> None:
    ancorario = ler_json(ANCORARIO)
    if not isinstance(ancorario, dict) or len(ancorario.get("spans", [])) != 25:
        raise FalhaExtracao("Livro-razão não contém os 25 spans extraídos")
    spans = ancorario["spans"]
    if any(item.get("status") != "candidata" or not item.get("verificada") for item in spans):
        raise FalhaExtracao("Livro-razão contém aprovação implícita ou span não verificado")
    if {item.get("codigo") for item in spans} != {item["codigo"] for item in recortes}:
        raise FalhaExtracao("Livro-razão e pacote não têm o mesmo caderno")
    texto = DOSSIE.read_text(encoding="utf-8")
    if len(re.findall(rf"^### PER-{re.escape(SIGLA)}-\d{{3}} ·", texto, re.MULTILINE)) != 25:
        raise FalhaExtracao("Dossiê não expôs as 25 candidatas")
    if texto.count("**Status**: `candidata`") != 25 or "**Status**: `aprovada`" in texto:
        raise FalhaExtracao("Dossiê não preserva as 25 como candidatas")
    if (RAIZ / "rag" / f"MANIFESTO-{SIGLA}.json").exists():
        raise FalhaExtracao("Não deveria existir manifesto de exportação RAG antes de homologação")


def executar_fluxo() -> None:
    candidatos = validar_autorizacao()
    recortes = [recortar(candidato) for candidato in candidatos]
    if len(recortes) != 25 or len({item["codigo"] for item in recortes}) != 25:
        raise FalhaExtracao("Extração não produziu 25 códigos distintos")
    escrever_pacote(recortes)
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "entrada"], "Portão A após extração")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "verbatim"], "Portão B após extração")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "ancorario"], "Livro-razão do Motor")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "dossier"], "Dossiê RAG do Motor")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "delta"], "Portão D após extração")
    executar([sys.executable, str(DADOS_TERMOS)], "Validação da Base")
    conferencia = {
        "artefato": "Extração literal e DOSSIE-RAG para avaliação curatorial",
        "ciclo": SIGLA,
        "eixo": "COSMOGONIA_HISTORIA_COSMICA",
        "executor": "ferramentas/extrair_dossie_oidr26_01.py",
        "autorizacao_extracao": str(AUTORIZACAO.relative_to(RAIZ)),
        "sha256_autorizacao_extracao": sha256(AUTORIZACAO),
        "fontes": {"candidatos": str(CANDIDATOS.relative_to(RAIZ)), "despacho": str(DESPACHO.relative_to(RAIZ))},
        "sha256_fontes": {"candidatos": sha256(CANDIDATOS), "despacho": sha256(DESPACHO)},
        "candidatas": len(recortes),
        "status": "candidata",
        "perolas_aprovadas": 0,
        "exportacao_rag": 0,
        "materializacao": 0,
        "mutacao_base": 0,
        "recortes": recortes,
        "produtos": {
            "pacote": {"caminho": str(PACOTE.relative_to(RAIZ)), "sha256": sha256(PACOTE)},
            "ancorario": {"caminho": str(ANCORARIO.relative_to(RAIZ)), "sha256": sha256(ANCORARIO)},
            "dossie": {"caminho": str(DOSSIE.relative_to(RAIZ)), "sha256": sha256(DOSSIE)},
        },
        "portoes_executados_pos_extracao": ["A", "B", "D"],
        "portao_c": "validado no ambiente vazio pré-cotejo; requer paridade ficha-pacote somente após autorização de pouso",
    }
    MANIFESTO.write_text(json.dumps(conferencia, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    conferir_produtos(recortes)
    print("OK — 25 candidatas extraídas pelo Motor e DOSSIE-RAG gerado; nenhuma pérola foi aprovada ou exportada.")


def validar_fluxo() -> None:
    candidatos = validar_autorizacao()
    if not all(caminho.is_file() for caminho in (PACOTE, ANCORARIO, DOSSIE, MANIFESTO)):
        raise FalhaExtracao("Produtos de extração/dossiê incompletos")
    manifesto = ler_json(MANIFESTO)
    if not isinstance(manifesto, dict) or manifesto.get("candidatas") != 25 or manifesto.get("perolas_aprovadas") != 0:
        raise FalhaExtracao("Manifesto de extração não preserva o escopo curatorial")
    recortes = manifesto.get("recortes")
    if not isinstance(recortes, list) or len(recortes) != 25:
        raise FalhaExtracao("Manifesto não registra os 25 recortes")
    if {item["codigo"] for item in recortes} != {item["codigo"] for item in candidatos}:
        raise FalhaExtracao("Manifesto e caderno curatorial divergem")
    if any(sha256(Path(info["caminho"]) if Path(info["caminho"]).is_absolute() else RAIZ / info["caminho"]) != info["sha256"]
           for info in manifesto.get("produtos", {}).values()):
        raise FalhaExtracao("Hash de produto do manifesto diverge")
    conferir_produtos(recortes)
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "entrada"], "Portão A de validação")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "verbatim"], "Portão B de validação")
    executar([sys.executable, str(MOTOR), "--ciclo", SIGLA, "delta"], "Portão D de validação")
    executar([sys.executable, str(DADOS_TERMOS)], "Validação da Base")
    print("OK — dossiê, 25 candidatas, Portões A/B/D e Delta Zero conferidos.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validar", action="store_true", help="confere produtos existentes sem escrever")
    args = parser.parse_args()
    try:
        if args.validar:
            validar_fluxo()
        else:
            executar_fluxo()
        return 0
    except (FalhaExtracao, OSError, subprocess.SubprocessError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
