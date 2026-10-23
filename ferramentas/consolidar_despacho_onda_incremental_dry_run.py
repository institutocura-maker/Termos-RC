#!/usr/bin/env python3
"""Aplica e valida o despacho curatorial integral da onda incremental.

A única aplicação permitida por este executor é a autorização uniforme de
``AUTORIZAR-COTEJO-AMPLIADO`` para todos os 25 candidatos de cada um dos quatro
lotes OIDR26. Ela não autoriza abertura de ciclo nem chama o Motor.

Uso:
    python3 ferramentas/consolidar_despacho_onda_incremental_dry_run.py --aplicar-cotejo-integral
    python3 ferramentas/consolidar_despacho_onda_incremental_dry_run.py --validar

A entrada é exclusivamente a triagem e os derivados já selados dentro de
``onda_incremental_dry_run/``. Nenhum bruto STT é aberto e não há mutação da
Base, fichas, termos, relações, ciclos ou apostilas.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Iterable


RAIZ = Path(__file__).resolve().parent.parent
ONDA = "onda_incremental_dry_run"
RAIZ_ONDA = RAIZ / ONDA
TRIAGEM = RAIZ_ONDA / "triagem_curatorial"
DERIVADOS = RAIZ_ONDA / "derivados_normalizados"
MANIFESTO_DERIVADOS = RAIZ_ONDA / "manifesto-derivados.json"
PLANEJAMENTO = TRIAGEM / "lotes-planejados.json"
REGISTRO = TRIAGEM / "registro-mestre.jsonl"
INDICE = TRIAGEM / "indice-termos-base.jsonl"
MAPA_LINHAS = TRIAGEM / "mapa-linhas.jsonl"
RESUMO_MAPA = TRIAGEM / "resumo-mapeamento.json"
CONSOLIDADO_JSON = TRIAGEM / "CONSOLIDADO-DESPACHO-CURATORIAL.json"
CONSOLIDADO_MD = TRIAGEM / "CONSOLIDADO-DESPACHO-CURATORIAL.md"
README = TRIAGEM / "README.md"
EXECUTOR = "ferramentas/consolidar_despacho_onda_incremental_dry_run.py"
DATA_DESPACHO = "2026-10-22"
DECISAO = "AUTORIZAR-COTEJO-AMPLIADO"
DECISOES_VALIDAS = {
    "PENDENTE",
    "MANTER-EM-TRIAGEM",
    "DESCARTAR-DO-LOTE",
    "AUTORIZAR-COTEJO-AMPLIADO",
    "RESERVAR-PARA-FUTURO-CICLO",
}
ALOCACAO_ESPERADA = {
    "OIDR26-01": ("ANUNNAKI_GENETICA", ("P1",)),
    "OIDR26-02": ("MITOLOGIAS_REINTEGRACAO", ("P2",)),
    "OIDR26-03": ("COSMOGONIA_HISTORIA_COSMICA", ("P3",)),
    "OIDR26-04": ("EXPERIENCIA_ESPIRITUAL_ETICA", ("P4", "P5", "P6")),
}


class FalhaDespacho(RuntimeError):
    """O despacho não é seguro para aplicação ou validação."""


def sha256_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as origem:
        for bloco in iter(lambda: origem.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def ler_json(caminho: Path) -> object:
    if not caminho.is_file():
        raise FalhaDespacho(f"Artefato obrigatório ausente: {caminho.relative_to(RAIZ)}")
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise FalhaDespacho(f"JSON inválido: {caminho.relative_to(RAIZ)}") from erro


def ler_jsonl(caminho: Path) -> list[dict]:
    if not caminho.is_file():
        raise FalhaDespacho(f"Artefato obrigatório ausente: {caminho.relative_to(RAIZ)}")
    registros: list[dict] = []
    with caminho.open(encoding="utf-8") as origem:
        for numero, linha in enumerate(origem, 1):
            try:
                item = json.loads(linha)
            except json.JSONDecodeError as erro:
                raise FalhaDespacho(f"{caminho.name}:{numero}: JSONL inválido") from erro
            if not isinstance(item, dict):
                raise FalhaDespacho(f"{caminho.name}:{numero}: registro não é objeto")
            registros.append(item)
    return registros


def escrever_json(caminho: Path, objeto: object) -> None:
    caminho.write_text(json.dumps(objeto, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def escrever_jsonl(caminho: Path, registros: Iterable[dict]) -> None:
    with caminho.open("w", encoding="utf-8", newline="\n") as destino:
        for registro in registros:
            destino.write(json.dumps(registro, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            destino.write("\n")


def carregar_lotes() -> list[dict]:
    lotes = ler_json(PLANEJAMENTO)
    if not isinstance(lotes, list) or len(lotes) != 4:
        raise FalhaDespacho("Planejamento deve conter exatamente quatro lotes")
    ids = [lote.get("lote_id") if isinstance(lote, dict) else None for lote in lotes]
    if ids != list(ALOCACAO_ESPERADA):
        raise FalhaDespacho("Planejamento não corresponde à ordem OIDR26 esperada")
    ingressos: list[str] = []
    for lote in lotes:
        lote_id = lote["lote_id"]
        eixo, fontes_esperadas = ALOCACAO_ESPERADA[lote_id]
        if lote.get("eixo", {}).get("codigo") != eixo:
            raise FalhaDespacho(f"{lote_id}: eixo não corresponde ao despacho")
        fontes = tuple(item.get("ingresso_id") for item in lote.get("fontes", []))
        if fontes != fontes_esperadas:
            raise FalhaDespacho(f"{lote_id}: ingressos não correspondem ao despacho")
        candidatos = lote.get("candidatos_de_cotejo_base")
        if not isinstance(candidatos, list) or len(candidatos) != 25:
            raise FalhaDespacho(f"{lote_id}: lote deve conter os 25 candidatos de triagem")
        codigos = [item.get("codigo") for item in candidatos]
        if len(codigos) != len(set(codigos)) or any(not isinstance(codigo, str) for codigo in codigos):
            raise FalhaDespacho(f"{lote_id}: códigos de candidatos inválidos")
        ingressos.extend(fontes)
    if sorted(ingressos) != ["P1", "P2", "P3", "P4", "P5", "P6"]:
        raise FalhaDespacho("Planejamento perdeu ou duplicou ingressos")
    return lotes


def validar_integridade_operacional() -> dict[str, str]:
    """Confere a cadeia derivado -> registro/índice, sem abrir brutos."""
    manifesto = ler_json(MANIFESTO_DERIVADOS)
    if not isinstance(manifesto, dict) or not isinstance(manifesto.get("derivados"), list):
        raise FalhaDespacho("Manifesto de derivados inválido")
    derivados = manifesto["derivados"]
    if len(derivados) != 6:
        raise FalhaDespacho("Manifesto da onda não contém seis derivados")
    por_arquivo = {item.get("arquivo"): item for item in derivados if isinstance(item, dict)}
    if len(por_arquivo) != 6 or any(not isinstance(nome, str) for nome in por_arquivo):
        raise FalhaDespacho("Manifesto possui arquivos derivados ausentes/duplicados")
    for arquivo, declarado in por_arquivo.items():
        caminho = DERIVADOS / arquivo
        if not caminho.is_file() or sha256_arquivo(caminho) != declarado.get("sha256_derivado"):
            raise FalhaDespacho(f"{arquivo}: derivado não coincide com manifesto")

    registros = ler_jsonl(REGISTRO)
    if len(registros) != 6:
        raise FalhaDespacho("Registro mestre não contém seis ingressos")
    for registro in registros:
        if registro.get("estado") != "APTO-PARA-TRIAGEM-SEM-MUTAR-BASE":
            raise FalhaDespacho("Registro mestre contém ingresso inelegível")
        caminho_relativo = registro.get("arquivo_derivado")
        if not isinstance(caminho_relativo, str):
            raise FalhaDespacho("Registro mestre sem caminho derivado")
        arquivo = Path(caminho_relativo).name
        declarado = por_arquivo.get(arquivo)
        if not declarado or registro.get("sha256_derivado") != declarado.get("sha256_derivado"):
            raise FalhaDespacho(f"{registro.get('ingresso_id')}: SHA do registro diverge do manifesto")

    # O índice e o mapa foram gerados para triagem e precisam permanecer legíveis;
    # seus hashes entram no consolidado para permitir revalidação posterior.
    indice = ler_jsonl(INDICE)
    linhas = ler_jsonl(MAPA_LINHAS)
    if not indice or not linhas:
        raise FalhaDespacho("Índice ou mapa de linhas vazio")
    return {
        "manifesto-derivados.json": sha256_arquivo(MANIFESTO_DERIVADOS),
        "registro-mestre.jsonl": sha256_arquivo(REGISTRO),
        "indice-termos-base.jsonl": sha256_arquivo(INDICE),
        "mapa-linhas.jsonl": sha256_arquivo(MAPA_LINHAS),
        "lotes-planejados.json": sha256_arquivo(PLANEJAMENTO),
        "resumo-mapeamento.json": sha256_arquivo(RESUMO_MAPA),
    }


def carregar_estado_pendente(lotes: list[dict]) -> list[dict]:
    """Exige os 100 candidatos pendentes antes de aplicar o despacho em bloco."""
    entradas: list[dict] = []
    for lote in lotes:
        lote_id = lote["lote_id"]
        pasta = TRIAGEM / lote_id
        resumo = ler_json(pasta / "resumo-triagem.json")
        candidatos = ler_json(pasta / "candidatos-cotejo.json")
        template = ler_json(pasta / "DESPACHO-CURATORIAL-TEMPLATE.json")
        if not isinstance(resumo, dict) or resumo.get("estado") != "AGUARDANDO-DESPACHO-CURATORIAL":
            raise FalhaDespacho(f"{lote_id}: resumo não está pendente para despacho")
        if resumo.get("fontes_brutas_abertas") != 0 or any(resumo.get("mutacoes", {}).values()):
            raise FalhaDespacho(f"{lote_id}: barreira de não mutação violada")
        if not isinstance(candidatos, list) or len(candidatos) != 25:
            raise FalhaDespacho(f"{lote_id}: candidatos de triagem inválidos")
        if not isinstance(template, dict):
            raise FalhaDespacho(f"{lote_id}: template inválido")
        template_candidatos = template.get("candidatos")
        if not isinstance(template_candidatos, list) or len(template_candidatos) != len(candidatos):
            raise FalhaDespacho(f"{lote_id}: template não cobre os 25 candidatos")
        codigos = [item.get("codigo") for item in candidatos]
        codigos_template = [item.get("codigo") for item in template_candidatos]
        if codigos_template != codigos:
            raise FalhaDespacho(f"{lote_id}: ordem/cobertura do template diverge dos candidatos")
        if any(item.get("decisao") != "PENDENTE" for item in template_candidatos):
            raise FalhaDespacho(f"{lote_id}: template possui decisão prévia; aplicação em bloco recusada")
        registro = template.get("despacho_de_lote")
        if not isinstance(registro, dict) or registro.get("resultado") != "PENDENTE" or registro.get("autorizacao_para_abrir_ciclo") is not False:
            raise FalhaDespacho(f"{lote_id}: estado final do template não está pendente/fechado")
        entradas.append({"lote": lote, "pasta": pasta, "resumo": resumo, "candidatos": candidatos, "template": template})
    return entradas


def aplicar_decisao(entrada: dict) -> tuple[dict, dict, dict]:
    """Preenche um lote inteiro sem introduzir decisão distinta por candidato."""
    lote = entrada["lote"]
    template = json.loads(json.dumps(entrada["template"]))
    resumo = json.loads(json.dumps(entrada["resumo"]))
    codigos = [item["codigo"] for item in entrada["candidatos"]]
    lote_id = lote["lote_id"]
    fundamento = (
        f"Despacho curatorial em bloco de {DATA_DESPACHO}: "
        f"{DECISAO} para todos os 25 candidatos do {lote_id}."
    )
    for candidato in template["candidatos"]:
        candidato["decisao"] = DECISAO
        candidato["fundamento_curatorial"] = fundamento
        candidato["observacao"] = "0 descartes; autorização restrita ao cotejo ampliado no derivado."
    template["despacho_de_lote"] = {
        "resultado": "CONCLUIDO",
        "candidatos_para_cotejo_ampliado": codigos,
        "autorizacao_para_abrir_ciclo": False,
        "observacao": (
            "25/25 candidatos autorizados para cotejo ampliado; 0 descartes. "
            "Este despacho não autoriza abertura de ciclo nem chamada ao motor.py."
        ),
    }
    resumo["estado"] = "COTEJO-AMPLIADO-AUTORIZADO; AGUARDANDO-AUTORIZACAO-EXPRESSA-DE-ABERTURA-DE-CICLO"
    resumo["despacho_curatorial"] = {
        "data": DATA_DESPACHO,
        "resultado": "CONCLUIDO",
        "decisao_aplicada": DECISAO,
        "autorizados_para_cotejo_ampliado": len(codigos),
        "descartados": 0,
        "autorizacao_para_abrir_ciclo": False,
        "limite": "Abertura de ciclo e Motor dependem de nova autorização expressa do Curador.",
    }
    consolidado_lote = {
        "artefato": "Consolidação de despacho curatorial por lote — onda incremental dry-run",
        "lote_id": lote_id,
        "eixo": lote["eixo"],
        "data_despacho": DATA_DESPACHO,
        "resultado": "CONCLUIDO",
        "decisao_aplicada": DECISAO,
        "candidatos_no_lote": len(codigos),
        "autorizados_para_cotejo_ampliado": len(codigos),
        "descartados": 0,
        "autorizacao_para_abrir_ciclo": False,
        "proximo_portao": "Aguardar autorização explícita para abertura de ciclo no Motor.",
        "efeito_na_base": "nenhum",
        "fontes_brutas_abertas": 0,
    }
    return template, resumo, consolidado_lote


def markdown_lote(consolidado: dict) -> str:
    return f"""# Despacho curatorial consolidado — {consolidado['lote_id']}

**Eixo:** `{consolidado['eixo']['codigo']}`
**Data do despacho:** {consolidado['data_despacho']}
**Resultado:** **CONCLUÍDO**

## Deliberação aplicada

- candidatos no lote: **{consolidado['candidatos_no_lote']}**;
- `{DECISAO}`: **{consolidado['autorizados_para_cotejo_ampliado']}**;
- descartes: **0**;
- fontes brutas abertas: **0**;
- efeito na Base: **nenhum**.

## Limite de autorização

O despacho permite somente o **cotejo ampliado nos derivados normalizados**.
`autorizacao_para_abrir_ciclo` permanece **false**. Assim, não há autorização
para criar `ciclo.toml`, materializar, alterar fichas ou chamar `motor.py`.

**Próximo portão:** autorização curatorial explícita de abertura de ciclo,
acompanhada de fonte derivada e âncoras canônicas por candidato.
"""


def montar_consolidado(lotes: list[dict], por_lote: dict[str, dict], hashes: dict[str, str]) -> dict:
    return {
        "artefato": "Consolidação de despacho curatorial — onda_incremental_dry_run",
        "data_despacho": DATA_DESPACHO,
        "executor": EXECUTOR,
        "resultado": "CONCLUIDO",
        "decisao_aplicada": DECISAO,
        "lotes": [por_lote[lote["lote_id"]] for lote in lotes],
        "totais": {
            "lotes": len(lotes),
            "candidatos": sum(item["candidatos_no_lote"] for item in por_lote.values()),
            "autorizados_para_cotejo_ampliado": sum(item["autorizados_para_cotejo_ampliado"] for item in por_lote.values()),
            "descartados": sum(item["descartados"] for item in por_lote.values()),
        },
        "autorizacao": {
            "cotejo_ampliado": True,
            "abertura_de_ciclo": False,
            "motor_py": False,
            "motivo": "O despacho recebido autorizou cotejo ampliado, não abertura de ciclo ou materialização.",
        },
        "integridade": {
            "fontes_brutas_abertas": 0,
            "mutacoes_na_base": 0,
            "hashes_da_triagem": hashes,
        },
        "proximo_portao": "Autorização curatorial explícita para abertura dos ciclos, antes de qualquer uso do Motor.",
    }


def markdown_consolidado(consolidado: dict) -> str:
    linhas = "\n".join(
        f"| `{lote['lote_id']}` | `{lote['eixo']['codigo']}` | {lote['candidatos_no_lote']} | "
        f"{lote['autorizados_para_cotejo_ampliado']} | {lote['descartados']} | "
        f"{'sim' if lote['autorizacao_para_abrir_ciclo'] else 'não'} |"
        for lote in consolidado["lotes"]
    )
    return f"""# Despacho curatorial consolidado — {ONDA}

**Data do despacho:** {DATA_DESPACHO}
**Resultado:** **CONCLUÍDO — cotejo ampliado autorizado em todos os lotes**

| Lote | Eixo | Candidatos | Autorizados para cotejo ampliado | Descartes | Abertura de ciclo |
|---|---|---:|---:|---:|---|
{linhas}

## Totais

- lotes: **{consolidado['totais']['lotes']}**;
- deliberações aplicadas: **{consolidado['totais']['candidatos']}**;
- `{DECISAO}`: **{consolidado['totais']['autorizados_para_cotejo_ampliado']}**;
- descartes: **0**;
- fontes brutas abertas: **0**;
- mutações na Base: **0**.

## Limite vigente

A autorização vale para **cotejo ampliado sobre os derivados normalizados**.
Ela não autoriza abertura de ciclo, criação de `ciclo.toml`, materialização ou
qualquer chamada a `motor.py`.

**Conclusão:** a onda pode avançar para a etapa de cotejo ampliado. A abertura
dos ciclos no Motor requer uma autorização curatorial posterior, explícita e
separada.
"""


def readme_atualizado(lotes: list[dict], por_lote: dict[str, dict]) -> str:
    linhas = "\n".join(
        f"| `{lote['lote_id']}` | `{lote['eixo']['codigo']}` | {lote['duracao_estimada']} | "
        f"{len(lote['fontes'])} | {por_lote[lote['lote_id']]['autorizados_para_cotejo_ampliado']} | "
        "`COTEJO-AMPLIADO-AUTORIZADO` |"
        for lote in lotes
    )
    return f"""# Triagem curatorial — {ONDA}

**Estado consolidado:** despacho curatorial concluído em {DATA_DESPACHO}.
Todos os candidatos dos quatro lotes foram autorizados para **cotejo ampliado**
no derivado normalizado. Não houve descartes e a Base segue intocada.

| Lote | Eixo | Duração | Ingressos | Autorizados para cotejo | Estado |
|---|---|---:|---:|---:|---|
{linhas}

Os templates preenchidos, os resumos de lote e
`CONSOLIDADO-DESPACHO-CURATORIAL.md` são os registros de decisão. A abertura de
ciclo e o uso de `motor.py` continuam bloqueados até nova autorização curatorial
explícita.
"""


def validar_estado_consolidado(lotes: list[dict], hashes_atuais: dict[str, str]) -> dict:
    """Valida literalmente as 100 decisões e a trava de abertura de ciclo."""
    consolidado = ler_json(CONSOLIDADO_JSON)
    if not isinstance(consolidado, dict):
        raise FalhaDespacho("Consolidado não é objeto JSON")
    if consolidado.get("resultado") != "CONCLUIDO" or consolidado.get("decisao_aplicada") != DECISAO:
        raise FalhaDespacho("Resultado/decisão do consolidado divergente")
    if consolidado.get("integridade", {}).get("fontes_brutas_abertas") != 0 or consolidado.get("integridade", {}).get("mutacoes_na_base") != 0:
        raise FalhaDespacho("Consolidado declara abertura de bruto ou mutação")
    if consolidado.get("autorizacao") != {
        "cotejo_ampliado": True,
        "abertura_de_ciclo": False,
        "motor_py": False,
        "motivo": "O despacho recebido autorizou cotejo ampliado, não abertura de ciclo ou materialização.",
    }:
        raise FalhaDespacho("Escopo de autorização do consolidado diverge")
    if consolidado.get("integridade", {}).get("hashes_da_triagem") != hashes_atuais:
        raise FalhaDespacho("Hashes de triagem no consolidado divergem do estado atual")

    registros = consolidado.get("lotes")
    if not isinstance(registros, list) or [item.get("lote_id") for item in registros] != [lote["lote_id"] for lote in lotes]:
        raise FalhaDespacho("Consolidado não cobre os quatro lotes na ordem correta")
    total_decisoes = 0
    for lote, registro in zip(lotes, registros):
        lote_id = lote["lote_id"]
        if registro.get("eixo") != lote["eixo"] or registro.get("candidatos_no_lote") != 25:
            raise FalhaDespacho(f"{lote_id}: registro consolidado inválido")
        if registro.get("autorizados_para_cotejo_ampliado") != 25 or registro.get("descartados") != 0 or registro.get("autorizacao_para_abrir_ciclo") is not False:
            raise FalhaDespacho(f"{lote_id}: contagens/autorização divergentes")

        pasta = TRIAGEM / lote_id
        template = ler_json(pasta / "DESPACHO-CURATORIAL-TEMPLATE.json")
        resumo = ler_json(pasta / "resumo-triagem.json")
        candidatos = lote["candidatos_de_cotejo_base"]
        codigos = [item["codigo"] for item in candidatos]
        decisao_template = template.get("candidatos") if isinstance(template, dict) else None
        if not isinstance(decisao_template, list) or [item.get("codigo") for item in decisao_template] != codigos:
            raise FalhaDespacho(f"{lote_id}: template não cobre a fila original")
        if any(item.get("decisao") != DECISAO for item in decisao_template):
            raise FalhaDespacho(f"{lote_id}: há candidato sem autorização de cotejo ampliado")
        if any(not isinstance(item.get("fundamento_curatorial"), str) or not item["fundamento_curatorial"] for item in decisao_template):
            raise FalhaDespacho(f"{lote_id}: fundamento curatorial ausente")
        final = template.get("despacho_de_lote")
        if not isinstance(final, dict) or final.get("resultado") != "CONCLUIDO":
            raise FalhaDespacho(f"{lote_id}: fechamento do template inválido")
        if final.get("candidatos_para_cotejo_ampliado") != codigos or final.get("autorizacao_para_abrir_ciclo") is not False:
            raise FalhaDespacho(f"{lote_id}: escopo de autorização do template inválido")
        if not isinstance(resumo, dict) or resumo.get("despacho_curatorial", {}).get("autorizados_para_cotejo_ampliado") != 25:
            raise FalhaDespacho(f"{lote_id}: resumo sem despacho consolidado")
        if resumo.get("despacho_curatorial", {}).get("autorizacao_para_abrir_ciclo") is not False:
            raise FalhaDespacho(f"{lote_id}: resumo autorizou ciclo indevidamente")
        total_decisoes += len(decisao_template)
    if total_decisoes != 100:
        raise FalhaDespacho(f"Consolidado deveria conter 100 decisões, contém {total_decisoes}")
    return consolidado


def publicar(entradas: list[dict], hashes_iniciais: dict[str, str]) -> None:
    """Gera todas as substituições em estágio antes de publicar qualquer uma."""
    lotes = [entrada["lote"] for entrada in entradas]
    por_lote: dict[str, dict] = {}
    produtos: dict[Path, str] = {}
    for entrada in entradas:
        template, resumo, consolidado_lote = aplicar_decisao(entrada)
        lote_id = entrada["lote"]["lote_id"]
        por_lote[lote_id] = consolidado_lote
        pasta = entry_dir = entrada["pasta"]
        produtos[pasta / "DESPACHO-CURATORIAL-TEMPLATE.json"] = json.dumps(template, ensure_ascii=False, indent=2) + "\n"
        produtos[pasta / "resumo-triagem.json"] = json.dumps(resumo, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        produtos[pasta / "DESPACHO-CURATORIAL-CONSOLIDADO.json"] = json.dumps(consolidado_lote, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        produtos[pasta / "DESPACHO-CURATORIAL-CONSOLIDADO.md"] = markdown_lote(consolidado_lote)

    # Os hashes usados pelo consolidado devem refletir a triagem anterior ao
    # próprio despacho. Hashes de templates/sumários mudam por definição e não
    # são usados para circularmente provar a própria decisão.
    consolidado = montar_consolidado(lotes, por_lote, hashes_iniciais)
    produtos[CONSOLIDADO_JSON] = json.dumps(consolidado, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    produtos[CONSOLIDADO_MD] = markdown_consolidado(consolidado)
    produtos[README] = readme_atualizado(lotes, por_lote)

    with tempfile.TemporaryDirectory(prefix=".despacho-", dir=TRIAGEM) as temporario:
        estagio = Path(temporario)
        for destino, conteudo in produtos.items():
            relativo = destino.relative_to(TRIAGEM)
            arquivo_estagio = estagio / relativo
            arquivo_estagio.parent.mkdir(parents=True, exist_ok=True)
            arquivo_estagio.write_text(conteudo, encoding="utf-8", newline="\n")
        for destino in produtos:
            relativo = destino.relative_to(TRIAGEM)
            os.replace(estagio / relativo, destino)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--aplicar-cotejo-integral", action="store_true", help="aplica as 100 autorizações integrais do despacho em bloco")
    grupo.add_argument("--validar", action="store_true", help="valida o despacho já aplicado, sem reescrever arquivos")
    args = parser.parse_args()
    try:
        lotes = carregar_lotes()
        hashes = validar_integridade_operacional()
        if args.aplicar_cotejo_integral:
            entradas = carregar_estado_pendente(lotes)
            publicar(entradas, hashes)
            consolidado = validar_estado_consolidado(lotes, hashes)
            print(
                "OK — despacho incremental aplicado: "
                f"{consolidado['totais']['autorizados_para_cotejo_ampliado']}/"
                f"{consolidado['totais']['candidatos']} autorizações de cotejo ampliado · "
                "0 descartes · abertura de ciclo=false · 0 mutações da Base"
            )
        else:
            consolidado = validar_estado_consolidado(lotes, hashes)
            print(
                "OK — despacho incremental validado: "
                f"{consolidado['totais']['autorizados_para_cotejo_ampliado']}/"
                f"{consolidado['totais']['candidatos']} autorizações · "
                "abertura de ciclo=false"
            )
        return 0
    except (FalhaDespacho, FileExistsError) as erro:
        print(f"ERRO — {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
