#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara um dossiê curatorial consolidado para um lote STT da Fase 0.

Entrada operacional: somente as cópias em ``normalizados_stt_lote_2026-10/``
e os artefatos produzidos pela Fase 0. O programa nunca abre, lê ou pesquisa
``fontes/stt-lote-2026-10/``. Também não cria ciclo, ficha, termo, relação ou apostila.

Cada dossiê reúne até 25 candidatos de cotejo já limitados pela Fase 0 e até
três ocorrências representativas por candidato. As ocorrências são endereços
literais no DERIVADO, não são cotejo com áudio e não são citações prontas para a
Base. A decisão continua integralmente do Curador.

Uso:
    python3 ferramentas/triagem_stt_lotes_2026_10.py --lote STT26-01
    python3 ferramentas/triagem_stt_lotes_2026_10.py --lote STT26-01 --force
    python3 ferramentas/triagem_stt_lotes_2026_10.py --proximo

Produtos de ``--lote STT26-01``:
    triagem_stt_lote_2026-10/STT26-01/DOSSIE-CURATORIAL.md
    triagem_stt_lote_2026-10/STT26-01/candidatos-cotejo.json
    triagem_stt_lote_2026-10/STT26-01/ocorrencias-candidatos.jsonl
    triagem_stt_lote_2026-10/STT26-01/DESPACHO-CURATORIAL-TEMPLATE.json
    triagem_stt_lote_2026-10/STT26-01/resumo-triagem.json
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Iterable


RAIZ = Path(__file__).resolve().parent.parent
INGRESSO = RAIZ / "ingestao_stt_lote_2026-10"
PLANEJAMENTO = INGRESSO / "lotes-planejados.json"
REGISTRO = INGRESSO / "registro-mestre.jsonl"
INDICE = INGRESSO / "indice-termos-base.jsonl"
SAIDA = RAIZ / "triagem_stt_lote_2026-10"
DADOS_TERMOS = RAIZ / "ferramentas" / "dados_termos.py"
FASE0_SCRIPT = RAIZ / "ferramentas" / "fase0_ingestao_stt_lote_2026_10.py"

MAX_CANDIDATOS = 25
MAX_EVIDENCIAS_POR_CANDIDATO = 3
DATA_GERACAO = "2026-10-20"


class FalhaTriagem(RuntimeError):
    """Invariante quebrada: o lote não deve produzir um dossiê parcial."""


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def ler_jsonl(caminho: Path) -> list[dict]:
    if not caminho.is_file():
        raise FalhaTriagem(f"Artefato de Fase 0 ausente: {caminho.relative_to(RAIZ)}")
    resultado = []
    with caminho.open(encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, 1):
            try:
                resultado.append(json.loads(linha))
            except json.JSONDecodeError as erro:
                raise FalhaTriagem(f"{caminho.name}:{numero}: JSONL inválido") from erro
    return resultado


def escrever_jsonl(caminho: Path, registros: Iterable[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as arquivo:
        for registro in registros:
            arquivo.write(json.dumps(registro, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            arquivo.write("\n")


def carregar_fase0():
    """Carrega o verificador de derivado sem reimplementar a guarda da Fase 0."""
    if not FASE0_SCRIPT.is_file():
        raise FalhaTriagem("Executor da Fase 0 ausente")
    spec = importlib.util.spec_from_file_location("_fase0_stt", FASE0_SCRIPT)
    if spec is None or spec.loader is None:
        raise FalhaTriagem("Não foi possível importar o verificador da Fase 0")
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def carregar_lotes() -> list[dict]:
    if not PLANEJAMENTO.is_file():
        raise FalhaTriagem("Planejamento de lotes da Fase 0 ausente")
    try:
        lotes = json.loads(PLANEJAMENTO.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise FalhaTriagem("lotes-planejados.json inválido") from erro
    if not isinstance(lotes, list) or not lotes:
        raise FalhaTriagem("Planejamento de lotes vazio ou fora do formato")
    ids = [lote.get("lote_id") for lote in lotes]
    if len(ids) != len(set(ids)) or any(not isinstance(item, str) for item in ids):
        raise FalhaTriagem("IDs de lote ausentes ou duplicados")
    return lotes


def escolher_lote(lotes: list[dict], solicitado: str | None, proximo: bool) -> dict:
    if proximo:
        for lote in lotes:
            if not (SAIDA / lote["lote_id"] / "resumo-triagem.json").is_file():
                return lote
        raise FalhaTriagem("Não há lote pendente de dossiê em triagem_stt_lote_2026-10/")
    assert solicitado is not None
    for lote in lotes:
        if lote["lote_id"] == solicitado:
            return lote
    raise FalhaTriagem(f"Lote inexistente no planejamento: {solicitado}")


def linha_do_documento(documento, linha: int) -> str:
    linhas = documento.texto.splitlines()
    if linha < 1 or linha > len(linhas):
        raise FalhaTriagem(f"{documento.arquivo}: índice aponta linha {linha} inexistente")
    return linhas[linha - 1]


def excerto_da_linha(linha: str, grafia: str) -> str:
    inicio = linha.casefold().find(grafia.casefold())
    if inicio < 0:
        raise FalhaTriagem("Índice da Fase 0 não coincide com a linha atual do derivado")
    fim_grafia = inicio + len(grafia)
    raio_antes, raio_depois = 180, 300
    a = max(0, inicio - raio_antes)
    b = min(len(linha), fim_grafia + raio_depois)
    texto = " ".join(linha[a:b].split())
    return ("…" if a else "") + texto + ("…" if b < len(linha) else "")


def evidencias_representativas(ocorrencias: list[dict]) -> list[dict]:
    """Até três exemplos, priorizando fontes diversas e ordem estável do lote."""
    por_fonte: dict[str, list[dict]] = defaultdict(list)
    ordem_fontes: list[str] = []
    for ocorrencia in ocorrencias:
        if ocorrencia["ingresso_id"] not in por_fonte:
            ordem_fontes.append(ocorrencia["ingresso_id"])
        por_fonte[ocorrencia["ingresso_id"]].append(ocorrencia)
    escolhidas: list[dict] = []
    for ingresso_id in ordem_fontes:
        escolhidas.append(por_fonte[ingresso_id][0])
        if len(escolhidas) == MAX_EVIDENCIAS_POR_CANDIDATO:
            break
    return escolhidas


def preparar(lote: dict) -> tuple[dict, list[dict], list[dict], dict]:
    """Confronta plano, registro, índice e bytes dos derivados antes de escrever."""
    fontes = lote.get("fontes")
    candidatos = lote.get("candidatos_de_cotejo_base")
    if not isinstance(fontes, list) or not fontes:
        raise FalhaTriagem(f"{lote['lote_id']}: fontes ausentes")
    if not isinstance(candidatos, list) or not candidatos or len(candidatos) > MAX_CANDIDATOS:
        raise FalhaTriagem(f"{lote['lote_id']}: candidatos fora do limite 1–{MAX_CANDIDATOS}")
    codigos = [candidato.get("codigo") for candidato in candidatos]
    if len(codigos) != len(set(codigos)) or any(not isinstance(codigo, str) for codigo in codigos):
        raise FalhaTriagem(f"{lote['lote_id']}: códigos candidatos ausentes ou duplicados")

    fase0 = carregar_fase0()
    documentos, integridade, hashes_fase0 = fase0.carregar_documentos()
    por_ingresso = {documento.ingresso_id: documento for documento in documentos}
    ids_lote = [fonte.get("ingresso_id") for fonte in fontes]
    if len(ids_lote) != len(set(ids_lote)) or any(ingresso not in por_ingresso for ingresso in ids_lote):
        raise FalhaTriagem(f"{lote['lote_id']}: plano contém ingresso ausente ou repetido")

    registro = ler_jsonl(REGISTRO)
    registro_por_id = {item.get("ingresso_id"): item for item in registro}
    if len(registro_por_id) != len(registro):
        raise FalhaTriagem("Registro mestre contém ingresso duplicado")
    for ingresso in ids_lote:
        documento = por_ingresso[ingresso]
        item = registro_por_id.get(ingresso)
        if not item or item.get("sha256_derivado") != documento.sha256_derivado:
            raise FalhaTriagem(f"{ingresso}: SHA não confere entre registro mestre e derivado")
        if item.get("estado") != "APTO-PARA-TRIAGEM-SEM-MUTAR-BASE":
            raise FalhaTriagem(f"{ingresso}: estado de ingresso não permite triagem")

    indice = ler_jsonl(INDICE)
    # Preserva a ordem de fontes planejada; a Fase 0 já é a única origem dos
    # candidatos, mas todos os endereços são verificados outra vez no derivado.
    ordem = {ingresso: posicao for posicao, ingresso in enumerate(ids_lote)}
    ocorrencias_por_codigo: dict[str, list[dict]] = defaultdict(list)
    for ocorrencia in indice:
        if ocorrencia.get("ingresso_id") in ordem and ocorrencia.get("codigo") in codigos:
            ocorrencias_por_codigo[ocorrencia["codigo"]].append(ocorrencia)
    for ocorrencias in ocorrencias_por_codigo.values():
        ocorrencias.sort(key=lambda item: (ordem[item["ingresso_id"]], item["linha"], item["grafia_encontrada"].casefold()))

    candidatos_preparados: list[dict] = []
    ocorrencias_saida: list[dict] = []
    for candidato in candidatos:
        codigo = candidato["codigo"]
        ocorrencias = ocorrencias_por_codigo.get(codigo, [])
        if len(ocorrencias) != candidato.get("sinais_exatos"):
            raise FalhaTriagem(
                f"{lote['lote_id']} / {codigo}: plano declara {candidato.get('sinais_exatos')} sinais; "
                f"índice retornou {len(ocorrencias)}"
            )
        if not ocorrencias:
            raise FalhaTriagem(f"{lote['lote_id']} / {codigo}: candidato sem endereço verificável")
        for sequencia, ocorrencia in enumerate(ocorrencias, 1):
            documento = por_ingresso[ocorrencia["ingresso_id"]]
            linha = linha_do_documento(documento, int(ocorrencia["linha"]))
            saida = {
                "evidencia_id": f"{lote['lote_id']}-{codigo}-{sequencia:03d}",
                "lote_id": lote["lote_id"],
                "ingresso_id": ocorrencia["ingresso_id"],
                "arquivo_derivado": documento.caminho_derivado,
                "sha256_derivado": documento.sha256_derivado,
                "unidade": ocorrencia["unidade"],
                "linha": ocorrencia["linha"],
                "codigo": codigo,
                "nome": candidato["nome"],
                "grafia_encontrada": ocorrencia["grafia_encontrada"],
                "texto_linha_sha256": hashlib.sha256(linha.encode("utf-8")).hexdigest(),
                "excerto": excerto_da_linha(linha, ocorrencia["grafia_encontrada"]),
                "natureza": "sinal literal no derivado; não é cotejo com áudio nem citação aprovada",
            }
            ocorrencias_saida.append(saida)
            ocorrencia["evidencia_id"] = saida["evidencia_id"]
            ocorrencia["excerto_confirmado"] = saida["excerto"]

        exemplos = evidencias_representativas(ocorrencias)
        candidatos_preparados.append(
            {
                "codigo": codigo,
                "nome": candidato["nome"],
                "categoria": candidato["categoria"],
                "subcategoria": candidato["subcategoria"],
                "sinais_exatos": len(ocorrencias),
                "fontes_com_sinal": len({item["ingresso_id"] for item in ocorrencias}),
                "evidencias_representativas": [
                    {
                        "evidencia_id": exemplo["evidencia_id"],
                        "ingresso_id": exemplo["ingresso_id"],
                        "unidade": exemplo["unidade"],
                        "linha": exemplo["linha"],
                        "grafia_encontrada": exemplo["grafia_encontrada"],
                        "excerto": exemplo["excerto_confirmado"],
                    }
                    for exemplo in exemplos
                ],
                "estado": "PENDENTE-DE-DECISAO-CURATORIAL",
                "limite": "Sinal automático literal; não autoriza pérola, ficha, relação, ciclo ou alteração da Base.",
            }
        )

    fontes_preparadas = []
    for fonte in fontes:
        documento = por_ingresso[fonte["ingresso_id"]]
        fontes_preparadas.append(
            {
                "ingresso_id": documento.ingresso_id,
                "arquivo_derivado": documento.caminho_derivado,
                "sha256_derivado": documento.sha256_derivado,
                "titulo": documento.titulo,
                "data_publicacao_original": documento.data_publicacao_original,
                "id_youtube": documento.id_youtube,
                "duracao": documento.duracao_texto,
            }
        )

    resumo = {
        "lote_id": lote["lote_id"],
        "gerado_em": DATA_GERACAO,
        "estado": "AGUARDANDO-DESPACHO-CURATORIAL",
        "escopo": "Dossiê de triagem; nenhuma mutação na Base",
        "entrada_operacional": "somente normalizados_stt_lote_2026-10/",
        "fontes_brutas_abertas": 0,
        "tema": lote["tema_primario"],
        "duracao_estimada": lote["duracao_estimada"],
        "fontes": len(fontes_preparadas),
        "candidatos": len(candidatos_preparados),
        "ocorrencias_literais": len(ocorrencias_saida),
        "max_candidatos": MAX_CANDIDATOS,
        "max_evidencias_representativas_por_candidato": MAX_EVIDENCIAS_POR_CANDIDATO,
        "integridade_fase0": integridade,
        "hashes_de_entrada": {
            "lotes-planejados.json": sha256_arquivo(PLANEJAMENTO),
            "registro-mestre.jsonl": sha256_arquivo(REGISTRO),
            "indice-termos-base.jsonl": sha256_arquivo(INDICE),
            "dados_termos.py": sha256_arquivo(DADOS_TERMOS),
            **hashes_fase0,
        },
        "mutacoes": {
            "ciclos_criados": 0,
            "fichas_criadas": 0,
            "termos_criados": 0,
            "relacoes_criadas": 0,
            "apostilas_criadas": 0,
            "dados_termos_alterado": False,
        },
    }
    return resumo, fontes_preparadas, candidatos_preparados, {"ocorrencias": ocorrencias_saida}


def montar_despacho_template(resumo: dict, candidatos: list[dict]) -> dict:
    return {
        "meta": {
            "artefato": "Template de despacho curatorial — triagem STT em lote",
            "lote_id": resumo["lote_id"],
            "gerado_em": DATA_GERACAO,
            "estado": "PENDENTE-CURADOR",
            "fonte_operacional": "somente derivados normalizados; o STT bruto não foi aberto",
            "efeito_atual": "nenhum: não cria ciclo nem altera a Base",
            "instrucoes": [
                "Decidir o conjunto do lote, não vídeo a vídeo.",
                "Sinal literal não prova conceito, interpretação nem citação apta.",
                "AUTORIZAR-COTEJO é apenas permissão para aprofundar a evidência no derivado.",
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


def escapar_tabela(texto: str) -> str:
    return " ".join(texto.replace("|", "\\|").split())


def montar_dossie(resumo: dict, fontes: list[dict], candidatos: list[dict]) -> str:
    tabela_fontes = "\n".join(
        f"| `{fonte['ingresso_id']}` | {escapar_tabela(fonte['titulo'])} | {fonte['duracao'] or '—'} | "
        f"`{fonte['sha256_derivado']}` |"
        for fonte in fontes
    )
    blocos = []
    for candidato in candidatos:
        blocos.append(
            f"### `{candidato['codigo']}` — {candidato['nome']}\n\n"
            f"- categoria: {candidato['categoria']} · {candidato['subcategoria']};\n"
            f"- sinais literais: **{candidato['sinais_exatos']}** em "
            f"**{candidato['fontes_com_sinal']}** fonte(s) deste lote;\n"
            f"- estado: **PENDENTE-DE-DECISAO-CURATORIAL**.\n\n"
            "| Evidência | Endereço no derivado | Grafia encontrada | Excerto literal de triagem |\n"
            "|---|---|---|---|\n"
            + "\n".join(
                f"| `{evidencia['evidencia_id']}` | `{evidencia['ingresso_id']}` · "
                f"`{evidencia['unidade']}` (linha {evidencia['linha']}) | "
                f"`{evidencia['grafia_encontrada']}` | {escapar_tabela(evidencia['excerto'])} |"
                for evidencia in candidato["evidencias_representativas"]
            )
            + "\n\n"
        )
    return f"""# Dossiê curatorial — {resumo['lote_id']}

**Data de geração:** {DATA_GERACAO}

**Tema:** {resumo['tema']['nome']} (`{resumo['tema']['codigo']}`)
**Duração estimada:** {resumo['duracao_estimada']}
**Estado:** **AGUARDANDO-DESPACHO-CURATORIAL**

## Escopo e trava

Este é um dossiê consolidado de triagem para **{resumo['fontes']}** fontes
normalizadas e **{resumo['candidatos']}** candidatos de cotejo. A entrada é
exclusivamente `normalizados_stt_lote_2026-10/`; conteúdos de STT bruto abertos
nesta etapa: **0**.

Uma ocorrência abaixo é somente um sinal literal de uma grafia canônica já
existente na Base. O excerto é literal do **derivado**, não uma confirmação da
fala em áudio e não uma citação pronta. Este dossiê não criou ciclo, ficha,
termo, relação ou apostila e não alterou `dados_termos.py`.

O arquivo `DESPACHO-CURATORIAL-TEMPLATE.json` é a única peça de decisão a
preencher. Mesmo uma opção `AUTORIZAR-COTEJO-AMPLIADO` não autoriza o Motor; um
ciclo só poderá ser aberto por despacho posterior, com fonte derivada e âncoras
específicas.

## Fontes do lote

| Ingresso | Título | Duração | SHA-256 do derivado |
|---|---|---:|---|
{tabela_fontes}

## Candidatos de cotejo — máximo 25

{''.join(blocos)}

## Leitura do despacho

1. Deliberar cada candidato no template, em bloco.
2. Os itens mantidos para cotejo ampliado ainda exigem seleção humana de
   evidência e contexto; frequência não é prioridade editorial.
3. Sem `autorizacao_para_abrir_ciclo: true` em despacho posterior, nenhum
   `ciclo.toml` será criado e o `motor.py` não será chamado.
"""


def montar_readme() -> str:
    """Mapa recuperável dos dossiês já preparados, sem inferir decisão alguma."""
    linhas = []
    for pasta in sorted(SAIDA.glob("STT26-*")):
        resumo = pasta / "resumo-triagem.json"
        if not resumo.is_file():
            continue
        try:
            dados = json.loads(resumo.read_text(encoding="utf-8"))
        except json.JSONDecodeError as erro:
            raise FalhaTriagem(f"Resumo inválido em {resumo.relative_to(RAIZ)}") from erro
        linhas.append(
            f"| `{dados['lote_id']}` | {dados['tema']['nome']} | {dados['duracao_estimada']} | "
            f"{dados['fontes']} | {dados['candidatos']} | `{dados['estado']}` |"
        )
    tabela = "\n".join(linhas) if linhas else "| — | — | — | — | — | — |"
    return f"""# Triagens curatoriais — lote STT 2026-10

Cada subdiretório é uma devolutiva de **triagem consolidada por lote**. A
entrada operacional continua sendo exclusivamente as cópias em
`normalizados_stt_lote_2026-10/`; nenhuma ferramenta desta etapa abre os STT
brutos. Um dossiê não altera a Base e não equivale a um ciclo do Motor.

## Dossiês preparados

| Lote | Tema | Duração | Fontes | Candidatos | Estado |
|---|---|---:|---:|---:|---|
{tabela}

Para preparar o próximo lote planejado, após o anterior ser recebido:

```bash
python3 ferramentas/triagem_stt_lotes_2026_10.py --proximo
```

A preparação é recuperável: `--force` refaz somente o diretório do lote pedido,
depois de validar todos os hashes e endereços de sua entrada.
"""


def publicar(lote: dict, resumo: dict, fontes: list[dict], candidatos: list[dict], ocorrencias: list[dict], force: bool) -> None:
    SAIDA.mkdir(exist_ok=True)
    destino = SAIDA / lote["lote_id"]
    if destino.exists() and not force:
        raise FileExistsError(
            f"Dossiê já existe: {destino.relative_to(RAIZ)}/. Use --force para regenerar somente este lote."
        )
    if destino.parent.resolve() != SAIDA.resolve() or not lote["lote_id"].startswith("STT26-"):
        raise FalhaTriagem("Destino de triagem inválido")

    with tempfile.TemporaryDirectory(prefix=f".{lote['lote_id']}-", dir=SAIDA) as temporario:
        estagio = Path(temporario) / lote["lote_id"]
        estagio.mkdir()
        (estagio / "DOSSIE-CURATORIAL.md").write_text(
            montar_dossie(resumo, fontes, candidatos), encoding="utf-8", newline="\n"
        )
        (estagio / "candidatos-cotejo.json").write_text(
            json.dumps(candidatos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        escrever_jsonl(estagio / "ocorrencias-candidatos.jsonl", ocorrencias)
        (estagio / "DESPACHO-CURATORIAL-TEMPLATE.json").write_text(
            json.dumps(montar_despacho_template(resumo, candidatos), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (estagio / "resumo-triagem.json").write_text(
            json.dumps(resumo, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )

        anterior = SAIDA / f".{lote['lote_id']}-anterior"
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

    readme = SAIDA / "README.md"
    readme_tmp = SAIDA / ".README.md.tmp"
    readme_tmp.write_text(montar_readme(), encoding="utf-8", newline="\n")
    os.replace(readme_tmp, readme)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--lote", metavar="STT26-XX", help="lote planejado para preparar")
    grupo.add_argument("--proximo", action="store_true", help="primeiro lote ainda sem dossiê")
    parser.add_argument("--force", action="store_true", help="regenera somente o diretório do lote selecionado")
    args = parser.parse_args()
    try:
        lotes = carregar_lotes()
        lote = escolher_lote(lotes, args.lote, args.proximo)
        resumo, fontes, candidatos, dados = preparar(lote)
        publicar(lote, resumo, fontes, candidatos, dados["ocorrencias"], args.force)
        print(
            f"Triagem {lote['lote_id']} concluída: {len(fontes)} fontes, "
            f"{len(candidatos)} candidatos, {len(dados['ocorrencias'])} sinais literais."
        )
        return 0
    except (FalhaTriagem, FileExistsError) as erro:
        print(f"Triagem abortada: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
