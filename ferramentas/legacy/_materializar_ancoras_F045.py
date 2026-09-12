#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F045 — MATERIALIZAÇÃO DAS 12 ÂNCORAS ESTRUTURAIS DA ENCICLOPÉDIA.

Despacho do Curador (07/09/2026): criar as fichas estruturais ausentes na
Base, com prioridade para as três espiritualidades (RC-059/060/061).

O que este script faz:
  1. Grava `termos/RC-XXX-slug.md` para cada um dos 12 códigos, com
     Definição / Contexto / Etimologia / Observação curadas à mão e as
     seções **Fontes** e **Relações centrais** geradas AUTOMATICAMENTE a
     partir do registro-mestre (garantia de consistência com a Base).
  2. Liga `ficha=True` no registro-mestre para os mesmos 12 códigos.

O que este script NÃO faz:
  - não cria nenhuma aresta (relacoes/ intacto);
  - não altera nomes, categorias, status, fontes ou relações de nada;
  - não mexe em nenhum outro código.

Asserts ao final: contagem de fichas, matcher ficha<->arquivo,
contiguidade dos códigos e integridade de relacoes/.

Uso:  python3 ferramentas/_materializar_ancoras_F045.py
"""
import os
import re
import sys
import glob

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dados_termos as BASE  # noqa: E402

REG = os.path.join(RAIZ, "ferramentas", "dados_termos.py")
DIR_T = os.path.join(RAIZ, "termos")
DATA = "2026-09-07"

# ------------------------------------------------------------------ conteúdo
# curadoria: (slug, definição, contexto, etimologia[], observação, revisar)
CONTEUDO = {
    "RC-059": (
        "espiritualidade-superior",
        "O nível mais alto dos três em que a Revelação Cósmica divide a realidade não caída: "
        "o «todo» que contém tudo — inclusive a Criação Indevida, que nela existe como uma "
        "«cabeça de alfinete» blindada. É a condição dos Seres Originais (RC-600), que vivem "
        "sob os Protocolos / Algoritmos da Perfeição (RC-606), sem tempo, sem distância e sem "
        "mérito. Corresponde, na leitura de Ellam, ao «Paraíso» e ao que a tradição gnóstica "
        "chamou de Pleroma.",
        "A Espiritualidade Superior é o «lado de fora» do universo: o que não é acidente, não "
        "caiu e não precisa de conserto. É dela que partem as mônadas que estruturam os seres "
        "da criação caída — «a Espiritualidade Superior, vendo o drama do Criador caído, deu de "
        "si mônadas para estruturar os clones que Brahma criava». A Departamentalização da Vida "
        "(RC-601) e os corpos búdico (RC-060) e manásico (RC-061) são desdobramentos "
        "experimentais a partir deste nível. Distingue-se do Deus Incognoscível / Deidade "
        "(RC-052), que não é um nível e sim a Fonte.",
        ["Grafia preferida: Espiritualidade Superior",
         "Variações: o Todo; o Paraíso; Pleroma (correspondência aproximada, [REVISAR])",
         "Uso na Base: nível 1 de 3 (Superior → Operacional → Laboratorial)"],
        "Nível de referência de toda a cosmografia da RC — eixo do Volume II da Enciclopédia e "
        "caixa «O FORA» do Mapa de Abstração (N0). A correspondência com Pleroma é leitura "
        "comparada, não identidade declarada pelo autor.",
        False,
    ),
    "RC-060": (
        "espiritualidade-operacional",
        "O primeiro desdobramento da Espiritualidade Superior (RC-059): o nível criado para que "
        "os seres puros pudessem experimentar a imperfeição por meio de uma «vestimenta "
        "espiritual» — o corpo búdico. É o degrau intermediário entre a perfeição obrigatória e "
        "a Espiritualidade Laboratorial (RC-061).",
        "Na sequência descrita por Ellam, a experiência da incompletude exigiu sucessivas "
        "vestimentas: «surgiu o corpo búdico, permitindo a experiência na Espiritualidade "
        "Operacional. Posteriormente, foi concebido o corpo manásico, que possibilitou a "
        "existência no nível da Espiritualidade Laboratorial». A Departamentalização da Vida "
        "(RC-601) envolve os três níveis, e os Seres Originais (RC-600) são descritos como "
        "criadores das condições desse desdobramento.",
        ["Grafia preferida: Espiritualidade Operacional",
         "Variações: Espiritualidade Operativa (grafia encontrada em fichas da Base)",
         "Corpo associado: corpo búdico"],
        "Materialização de âncora estrutural: sem este verbete, a sequência «Superior → "
        "Operacional → Laboratorial» — repetida em praticamente toda a cosmografia — ficava sem "
        "o elo do meio.",
        False,
    ),
    "RC-061": (
        "espiritualidade-laboratorial",
        "O terceiro e mais denso dos três níveis: a região da «Experiência Laboratorial» onde "
        "se deu o projeto que saiu errado. Abriga Ereon (RC-496) e os seus cinco Archeons "
        "(RC-596) — Antérion, Danérion, Mermérion, Perpérion (RC-087) e Tempérion (RC-472) — e "
        "é o nível do corpo manásico. Dela partiu a projeção de Prabrajna (RC-152) que gerou a "
        "Criação Indevida (RC-167).",
        "É o «laboratório» no sentido literal: o nível em que consciências experimentam criar. "
        "Em Perpérion residiam as 147 consciências do Gênero Adhy (RC-411), das quais 43 "
        "compunham a espécie Pashvnaj (RC-455) — o ambiente de onde sai o impulso de Prabrajna. "
        "Após o colapso, a Espiritualidade Laboratorial se reorganiza no Conclave (RC-635), e a "
        "faixa da Errática (RC-513) é descrita como a quarta faixa manifestada, abaixo dela.",
        ["Grafia preferida: Espiritualidade Laboratorial",
         "Variações: Laboratorial; nível laboratorial",
         "Corpo associado: corpo manásico",
         "Subdivisões: cinco Archeons de Ereon (RC-596)"],
        "O elo mais citado e menos documentado da cosmografia — materializado por exigência da "
        "estrutura da Enciclopédia (Volume II, seção II.7.2).",
        False,
    ),
    "RC-099": (
        "seres-terrenos",
        "A espécie humana na leitura da Revelação Cósmica: o ser terreno atual (Homo sapiens), "
        "habitante do Universo Material (RC-107) e portador do DNA como projeção holográfica do "
        "psiquismo do Criador (RC-217). Não é apresentado como produto de evolução darwiniana "
        "nem de criação divina direta, mas como resultado de sucessivas levas genéticas e de um "
        "projeto de semeadura, e como candidato à especiação (RC-056) que produz a Criatura "
        "Universal (RC-042).",
        "O termo é o «nós» da narrativa: aparece em 21 fontes do censo, o que o torna um dos "
        "nós mais densos da Base. A RC trata o humano simultaneamente como criatura-ferramenta "
        "(RC-164) da Criação Indevida e como o agente do Tikun — a criatura capaz de produzir, "
        "com a sua própria experiência no caos, as informações que faltam ao Criador para se "
        "recompor. O Fim do Experimento Humano (RC-578) é o risco que paira sobre a espécie.",
        ["Grafia preferida: Seres Terrenos",
         "Variações: Homo sapiens; humano; humanidade terrestre",
         "Uso na Base: 1.6 Figuras humanas (espécie, não indivíduo)"],
        "Materialização de âncora estrutural do Volume IV (Antropogênese). Quarentena: a "
        "antropogênese da RC é leitura de Ellam e não substitui nem a biologia evolutiva nem a "
        "teologia das religiões.",
        False,
    ),
    "RC-118": (
        "val-dimon",
        "Nome demo de Pandora (RC-086): a identidade de Pandora antes da humanização, na "
        "condição de biodemo da família Val (RC-109). Integra a cadeia de identidades que a RC "
        "atribui à mesma figura — Kalil Kadmon (RC-299) → Adam Kadmon → Val Dimon → Pandora — e "
        "que a proposta pedagógica resume como «Pandora = Val Dimon = Kalil Kadmon = serpente do "
        "Éden».",
        "A ficha de Pandora (RC-086) registra a identidade-val, e a de Kalil Kadmon (RC-299) "
        "narra a cadeia de dignificação que culmina no «sorriso de Pandora». O fechamento do "
        "triângulo documental vem de B020 (Pandora = Val Dimon) e B060 (Kalil Kadmon = Val "
        "Dimon), já averbados em relacoes/.",
        ["Grafia preferida: Val Dimon",
         "Variações: Val Dimon (biodemo) → Pandora (humanizada)",
         "Família: Val (RC-109)"],
        "Verbete exigido pela seção IV.17.4 da Enciclopédia (Pandora, o Éden e as hibridações). "
        "As identidades sobrepostas de Pandora são uma das «identidades que se confundem» que o "
        "percurso top-down manda destravar no N2.",
        False,
    ),
    "RC-120": (
        "val-el",
        "Nome composto «Val El / Val Ellam»: a forma pela qual o codificador das Revelações "
        "Cósmicas, Jan Val Ellam (RC-071), é designado na economia interna da própria obra — o "
        "nome civil acrescido do prefixo «Val», que na RC identifica a família biodêmica Val "
        "(RC-109).",
        "Registrado com uma única fonte (B031), o verbete tem valor sobretudo prosopográfico e "
        "de aparato: é o ponto de encontro entre o autor empírico (RC-071) e a sua "
        "caracterização dentro da narrativa cósmica. As relações apontam para a família Val "
        "(RC-109), para o próprio Jan Val Ellam (RC-071) e para os códigos RC-140, RC-068 e "
        "RC-083.",
        ["Grafia preferida: Val El / Val Ellam",
         "Variações: Val El; Val Ellam",
         "Família: Val (RC-109) · Autor: Jan Val Ellam (RC-071)"],
        "Fonte única (B031) — manter sob [REVISAR] até nova evidência. Verbete de aparato, "
        "necessário à seção I.1.1 da Enciclopédia (o autor e a sua voz).",
        True,
    ),
    "RC-163": (
        "mente-universal-emergente",
        "A «Mente Universal» (também chamada Biocosmos): a mente coletiva que emerge da "
        "recomposição da criação — o resultado da integração das consciências particularizadas "
        "depois do Tikun (RC-514). Não é uma divindade nem uma soma de indivíduos: é a nova "
        "instância de consciência que a obra descreve como o destino do conjunto.",
        "O conceito fecha o arco da apostila «A Queda»: a crise culmina na construção do Paraíso "
        "B (RC-612) — a nova espiritualidade que incorpora o aprendizado do caos — e na formação "
        "da Mente Universal Emergente (RC-163). As criaturas-ferramenta (RC-164) são, na leitura "
        "de Ellam, as produtoras das informações que permitem a «emergência de uma Mente-una».",
        ["Grafia preferida: Mente Universal (Emergente)",
         "Variações: Mente Universal; Biocosmos; Mente-una",
         "Par declarado pela fonte: RC-879 (variação)"],
        "Destino final do Volume V da Enciclopédia (V.22.4). Quarentena cosmológica: não há "
        "correspondência com qualquer conceito da física ou da neurociência acadêmicas.",
        False,
    ),
    "RC-196": (
        "criador-refem-das-proprias-criaturas",
        "A condição do Criador depois da queda: preso à própria obra, dependente das criaturas "
        "que gerou. É o inverso da onipotência — o deus que não pode sair do lugar nem desfazer "
        "o que fez, e cuja recomposição depende do que as suas criaturas produzirem.",
        "A Base aproxima este verbete de dois outros: a Simbiose Quântica (RC-195), a "
        "interconexão não-local entre todos os seres gerados a partir da energia do criador "
        "caído, e o Modelo Colmeia (RC-176), o modo de operação em que todas as criaturas "
        "existem para servir a «abelha-rainha». A condição do Criador (RC-041) é, portanto, a de "
        "um refém que precisa das suas próprias ferramentas (RC-164) para se reerguer — é esse "
        "o motor ético do Tikun.",
        ["Grafia preferida: Criador refém das próprias criaturas",
         "Variações: criador refém; refém da própria obra",
         "Condição conexa: Demência do Criador (RC-526)"],
        "Nó ético e dramático do Volume III da Enciclopédia (III.9.4). A imagem do «refém» é "
        "leitura de Ellam, não categoria teológica das religiões.",
        False,
    ),
    "RC-281": (
        "agentes-do-quarto-logos",
        "Os agentes do Quarto Logos — Olm, o Codificador de Zian (RC-092 / RC-252) — : as "
        "consciências encarregadas de levar adiante a «estratégia esclarecedora» do Logos que "
        "mergulhou diretamente no universo biológico sem passar pelo antimaterial. Na RC, o "
        "próprio Jan Val Ellam (RC-071) é tratado como um desses agentes.",
        "Fonte única (B014). O Quarto Logos é o único dos quatro que não mergulhou no "
        "Brahmaloka, podendo por isso criar um CFD próprio — daí a função de «codificador». A "
        "Escola dos Agentes Esclarecidos da Busca da Verdade (RC-256) aparece como a instância "
        "de formação desses agentes.",
        ["Grafia preferida: Agentes do Quarto Logos",
         "Variações: agentes de Olm; esclarecedores",
         "Logos: Quarto Logos / Olm (RC-092, RC-252)"],
        "Fonte única (B014) — manter sob [REVISAR] até nova evidência. Verbete de apoio à seção "
        "III.13.5 (Consciências coletivas e Logos).",
        True,
    ),
    "RC-331": (
        "ra-atom",
        "Designação do Criador nas obras: «Ra-Atom / Og-mi». Integra a série de nomes que a RC "
        "atribui ao mesmo ser — Javé (RC-001), Brahma (RC-037), Caos (RC-284), Ialdabaoth "
        "(RC-482), Alá — recolhidos na correspondência estabelecida em «O Sorriso de Pandora» "
        "(B020).",
        "O verbete funciona como entrada filológica: é pela multiplicidade de nomes que a "
        "pedagogia top-down destrava a confusão número 1 do iniciante («afinal, Javé e Brahma são "
        "a mesma coisa?»). A relação com RC-284 (Caos = Brahma = Javé) e com RC-001 (Javé) está "
        "averbada na malha de relações, e o seu enquadramento geral é a Revelação Cósmica "
        "(RC-094).",
        ["Grafia preferida: Ra-Atom / Og-mi",
         "Variações: Ra-Atom; Og-mi",
         "Série onomástica: Javé · Brahma · Caos · Ialdabaoth · Alá"],
        "Verbete de filologia (Volume I, seção I.3 — a linguagem da RC). A equivalência entre "
        "nomes de tradições distintas é leitura comparada de Ellam.",
        False,
    ),
    "RC-410": (
        "adhyprabraja",
        "Grafia do diagrama para o nome do Criador antes da queda: ADHYPRABRAJNA. É a forma "
        "usada nos quadros e diagramas das obras (B051, B060, B061) para Adhyshprabrajna "
        "(RC-310) — o ser da condição Adhyatman que, após a queda, passa a ser chamado "
        "Prabrajna (RC-152) e, depois, Brahma / Javé (RC-037 / RC-001).",
        "A ficha de RC-310 registra o uso em «Inquisição Trimurtiana» (B022, Introdução): a "
        "Criação Universal indevida «foi procedida por Adhyshprabrajna, na sua expressão "
        "Adhyatman». A grafia do diagrama é a mesma entidade, com a grafia normalizada dos "
        "quadros. A relação com o Fatiamento de Consciência (RC-604) vem de P2021-12-04.",
        ["Grafia preferida: ADHYPRABRAJNA (grafia do diagrama)",
         "Variações: Adhyshprabrajna (RC-310); Prabrajna (RC-152); Prajapati (tradição védica)",
         "Condição: Adhyatman"],
        "Verbete-ponte entre a filologia (Volume I) e a cadeia do Criador (Volume III). A Base "
        "mantém as três grafias em códigos distintos de propósito: são entradas diferentes da "
        "mesma identidade, e é isso que o estudante precisa ver.",
        False,
    ),
    "RC-528": (
        "mergulho",
        "A designação ellâmica da queda: «mergulho», não «queda». O termo desloca o sentido "
        "teológico da culpa para o de uma descida voluntária — ainda que malcalculada — para "
        "dentro da própria criação, da qual o ser não consegue mais sair.",
        "O vocabulário importa: na RC, «mergulhar» é o que fazem os Logos e as cocriadoras "
        "quando descem aos níveis inferiores (o Quarto Logos, RC-092, «mergulhou» diretamente no "
        "universo biológico). A queda de Prabrajna (RC-152) é, nessa chave, o mergulho que deu "
        "errado e produziu a Criação Indevida (RC-167) — donde a proximidade com o acidente "
        "cosmogônico (RC-515).",
        ["Grafia preferida: Mergulho (designação ellâmica da queda)",
         "Variações: mergulho; a descida",
         "Uso oposto: «queda» (a leitura tradicional)"],
        "Status mantido em ⚪ candidato (como estava no registro-mestre) até revisão cruzada "
        "com as obras primárias. Verbete-chave do Volume II (II.6.3).",
        False,
    ),
}


# ------------------------------------------------------------------ helpers
def slugify(nome):
    n = nome.lower()
    for a, b in (("ç", "c"), ("ã", "a"), ("á", "a"), ("à", "a"), ("â", "a"),
                 ("é", "e"), ("ê", "e"), ("í", "i"), ("ó", "o"), ("õ", "o"),
                 ("ô", "o"), ("ú", "u"), ("ü", "u")):
        n = n.replace(a, b)
    n = re.sub(r"[^a-z0-9]+", "-", n).strip("-")
    return n


STATUS_EMOJI = {"candidato": "⚪", "provisório": "🟡", "em análise": "🟠",
                "verificado": "🟢"}


def montar_ficha(cod, termo):
    slug, definicao, contexto, etim, obs, revisar = CONTEUDO[cod]
    _c, nome, area, sub, status, fontes, relac, _f = termo
    emoji = STATUS_EMOJI.get(status, "⚪")
    L = []
    L.append(f"# {nome} — {cod}")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append(f"| **Categoria Principal** | {area.upper()} |")
    L.append(f"| **Subcategoria** | {sub} |")
    L.append(f"| **Status** | {emoji} {status.capitalize()} |")
    L.append(f"| **Última atualização** | {DATA} |")
    L.append("")
    L.append("## Definição Sintética")
    L.append(definicao)
    L.append("")
    L.append("## Contexto / Origem")
    L.append(contexto)
    L.append("")
    L.append("## Etimologia / Grafias")
    for e in etim:
        L.append(f"- {e}")
    L.append("")
    L.append("## Fontes")
    L.append("| Obra/palestra | Localização | Tipo |")
    L.append("|---|---|---|")
    if fontes:
        for f in fontes:
            L.append(f"| {f} | — | registro-mestre (fonte censada) |")
    else:
        L.append("| — | — | sem fonte censada |")
    L.append("")
    L.append("## Relações centrais")
    if relac and relac.strip() and relac.strip() != "—":
        for r in [x.strip() for x in relac.split(";") if x.strip()]:
            L.append(f"- {r} — ver ficha correspondente")
    else:
        L.append("- *(nenhuma relação registrada no registro-mestre)*")
    L.append("")
    L.append("## Observação")
    L.append(obs)
    if revisar:
        L.append("")
        L.append("**[REVISAR]** — fonte única; ampliar com revisão cruzada antes de promover o status.")
    L.append("")
    L.append("## Nota de governança")
    L.append(f"F045 (despacho 07/09/2026) — materialização de âncora estrutural da Enciclopédia ")
    L.append(f"(Apêndice D do `pedagogico/enciclopedia/INDICE-ENCICLOPEDIA-RC.md`). Síntese de ")
    L.append(f"leitura construída sobre o acervo; nenhuma aresta nova em `relacoes/`.")
    L.append("")
    return "\n".join(L), f"{cod}-{slug}.md"


def ligar_ficha_no_registro(codigos):
    """Troca o flag ficha de False -> True, só nas linhas dos códigos dados."""
    src = open(REG, encoding="utf-8").read()
    linhas = src.split("\n")
    # IMPORTANTE: o bloco RELACOES tambem tem linhas comecando por ("RC-xxx", —
    # a edicao vale SOMENTE para o bloco TERMOS.
    fim_termos = next((i for i, l in enumerate(linhas) if l.startswith("RELACOES")), None)
    assert fim_termos is not None, "nao achei o inicio do bloco RELACOES"
    alteradas = []
    for i, ln in enumerate(linhas[:fim_termos]):
        for c in codigos:
            if ln.lstrip().startswith(f'("{c}",'):
                novo, n = re.subn(r",\s*False\s*\)(?=\s*,?\s*(?:#|$))", ", True)", ln, count=1)
                if n != 1:
                    raise SystemExit(f"FALHA ao ligar ficha de {c}: padrão não encontrado")
                if novo != ln:
                    linhas[i] = novo
                    alteradas.append(c)
                break
    if len(alteradas) != len(codigos):
        faltando = [c for c in codigos if c not in alteradas]
        raise SystemExit(f"FALHA: nem todos os códigos foram ligados: {faltando}")
    open(REG, "w", encoding="utf-8").write("\n".join(linhas))
    return alteradas


# ------------------------------------------------------------------ execução
def main():
    mapa = {t[0]: t for t in BASE.TERMOS}
    codigos = list(CONTEUDO.keys())
    for c in codigos:
        assert c in mapa, f"{c} não existe no registro-mestre"
        assert mapa[c][7] is False, f"{c} já tem ficha=True (esperado False)"

    fichas_antes = sum(1 for t in BASE.TERMOS if t[7])
    rel_antes = len(BASE.RELACOES)
    print(f"ANTES: {len(BASE.TERMOS)} termos · {fichas_antes} fichas · {rel_antes} relações")

    # 1) gravar as fichas
    gravados = []
    for c in codigos:
        texto, nome_arq = montar_ficha(c, mapa[c])
        caminho = os.path.join(DIR_T, nome_arq)
        assert not os.path.exists(caminho), f"arquivo já existe: {caminho}"
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)
        gravados.append(caminho)
        print(f"  ficha gravada: termos/{nome_arq}")

    # 2) ligar ficha=True no registro-mestre
    alteradas = ligar_ficha_no_registro(codigos)
    print(f"  registro-mestre: {len(alteradas)} flags ficha False -> True")

    # 3) revalidar
    os.execv(sys.executable, [sys.executable, "-c", """
import sys, os, glob
sys.path.insert(0, os.path.join(os.getcwd(), "ferramentas"))
import dados_termos as d
d.validar()
fichas = [t for t in d.TERMOS if t[7]]
arqs = glob.glob("termos/*.md")
sem_arq = [t[0] for t in fichas if not glob.glob(f"termos/{t[0]}-*.md")]
orfos = [a for a in arqs if a.split("/")[-1][:6] not in {t[0] for t in d.TERMOS}]
print(f"fichas=True: {len(fichas)} | arquivos .md: {len(arqs)}")
print(f"ficha sem arquivo: {sem_arq}")
print(f"arquivo sem codigo na base: {orfos}")
assert not sem_arq and not orfos, "MATCHER QUEBRADO"
print("MATCHER OK")
"""])


if __name__ == "__main__":
    main()
