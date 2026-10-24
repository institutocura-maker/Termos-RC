#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Materializa as DUAS fichas autorizadas pelo despacho de 29/08/2026 (D-10).

`RC-018 Alt´Lam Gron` e `RC-040 CFD (Código Fonte Definidor)` viviam **só no cadastro** — linha em
`ferramentas/dados_termos.py` sem arquivo em `termos/`, `ficha=False`. O Curador autorizou a virada
`ficha=False → ficha=True` para estas duas e **somente** estas duas (a `RC-444 Família Cromon` foi
nominalmente mantida em `ficha=False`).

Regras observadas (espelho de `_gerar_ficha_RC089_P2022-03-26.py`, que é espelho do que foi feito com
`RC-020` em P2020-04-25):

 * a seção `## Ampliação — P2023-12-03` é **copiada byte a byte do pacote** `_ampliacoes_P2023-12-03.txt`
   — mesma fonte do aplicador, portanto a paridade exigida pelo portão D é automática;
 * **nenhuma aspa desta ficha foi digitada de memória**: as citações vêm do pacote, e o pacote só contém
   span verificado pelo caça-âncoras `_aspas_P2023-12-03.py`;
 * `RELACOES` **não é tocada**: a ficha reproduz o estado do cadastro e **não** abre aresta; onde o cadastro
   lista `relacionados` sem aresta correspondente, a ficha **declara a lacuna** em vez de fingir que resolveu;
 * o cadastro é virado por `_vincular_fonte_P2023-12-03.py`, não aqui.
"""
import os, re, sys, glob, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SIGLA = "P2023-12-03"
TITULO = "A Rebelião de Lúcifer ainda por ser Finalizada"
DATA = "2026-08-29"
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIGLA}.txt")
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                                             # noqa: E402
CAD = {t[0]: t for t in DT.TERMOS}

pac = open(PACOTE, encoding="utf-8").read()


def bloco_de(cod):
    b = pac.split(f"### {cod}\n", 1)[1]
    m = re.search(r"^(?:## |### )", b, re.M)
    if m:
        b = b[:m.start()]
    b = b.strip()
    assert b.startswith("- **["), f"bloco {cod} vazio ou mal formado"
    return b


def slug(nome):
    x = unicodedata.normalize("NFKD", nome.replace("´", " ")).encode("ascii", "ignore").decode()
    x = re.sub(r"[^A-Za-z0-9]+", "-", x).strip("-").lower()
    return re.sub(r"-{2,}", "-", x)


def arquivo_de(cod):
    got = glob.glob(os.path.join(RAIZ, "termos", f"{cod}-*.md"))
    return got[0] if got else os.path.join(RAIZ, "termos", f"{cod}-{slug(CAD[cod][1])}.md")


def arestas_de(cod):
    return [r for r in DT.RELACOES if r[0] == cod or r[2] == cod]


def tabela_rel(cod, linhas_extra):
    lin = CAD[cod]
    rel = [x.strip() for x in (lin[6] or "").split(";") if x.strip()]
    out = ["| Termo | Código | Tipo de relação |", "|---|---|---|"]
    for r in rel:
        nome = CAD.get(r, ["", "— (sem linha no cadastro)"])[1]
        arq = "arquivo existe" if glob.glob(os.path.join(RAIZ, "termos", f"{r}-*.md")) else "**sem arquivo**"
        aresta = next((a for a in arestas_de(cod) if r in (a[0], a[2])), None)
        tipo = (f"`{aresta[1]}` (aresta em `RELACOES`, fonte {aresta[3]})" if aresta
                else f"listado no cadastro como relacionados, **sem aresta** em `RELACOES`; {arq}")
        out.append(f"| {nome} | {r} | {tipo} |")
    out += linhas_extra
    return "\n".join(out)


def fontes_tabela(cod):
    fs = [f for f in (CAD[cod][5] or []) if f != SIGLA]
    orais = [f for f in fs if f.startswith("P")]
    obras = [f for f in fs if not f.startswith("P")]
    ln = ["| Obra (sigla) | Capítulo | Página | Tipo (citação/paráfrase) |", "|---|---|---|---|",
          f"| {SIGLA} | {TITULO} (palestra) | — | transcrição automatizada; citação |"]
    for b in obras:
        ln.append(f"| {b} | a preencher | — | paráfrase (vínculo pré-existente do cadastro) |")
    if orais:
        ln.append(f"| {' · '.join(orais)} | — | — | fontes orais já registradas no cadastro antes deste ciclo |")
    return "\n".join(ln)


# ══════════════════════════════ RC-018 ══════════════════════════════
lin = CAD["RC-018"]
n_arestas = len(arestas_de("RC-018"))
RC018 = f"""# Alt´Lam Gron — RC-018

| Campo | Valor |
|---|---|
| **Categoria Principal** | {lin[2].title()} |
| **Subcategoria** | {lin[3]} |
| **Status** | 🟡 {lin[4].capitalize()} |
| **Última atualização** | {DATA} |

## Definição Sintética

**Alt´Lam Gron** é, nas obras do acervo, a nave-entidade vinculada ao sistema de Alt´Lam (`RC-017`) — a estrutura
que hospeda os coletivos rebeldes fora do planeta. Esta ficha existia **só no cadastro** (`dados_termos.py`) desde a
migração: não havia arquivo, e por isso não havia definição. Passa a tê-la, e a definição é a que a fonte oral de
**03/12/2023** entrega: na palestra, a nave é dita **pequenininha**, é o lugar onde uma turma **se astralizou**
depois de «fazer a experiência», e é o ponto onde estão, ao mesmo tempo, os efetivos de uma família, o
processador dela e **uma visita datada** (Sofia, nos anos 2018-19). A Base ganha, com isso, o que nenhuma obra
dava: um endereço funcional para o nome.

## Contexto / Origem

**Materialização (não é criação).** O código RC-018 vivia só no cadastro — linha `("{lin[0]}", "{lin[1]}", {lin[2]},
{lin[3]}…, {", ".join(f"`{x}`" for x in (lin[5] or []))}, {lin[6]}, False)` — sem arquivo em `termos/`. A
**Devolutiva do Curador de 29/08/2026 (D-10)** autorizou a virada `ficha=False → ficha=True` «com as 4 grafas e o
censo», dada a quantidade de dado técnico que a fonte entrega sobre o objeto. É uma de **duas** materializações
deste ciclo (a outra é `RC-040`); `RC-444 Família Cromon` foi nominalmente mantida em `ficha=False`.

Com isso:

- a Base passa de **458 para 460 arquivos de ficha** e o cadastro de **457 para 459** linhas `ficha=True`;
- o cadastro continua em **777 termos** (teto curatorial; `RC-778` não consumido) e as **1.856 relações
  permanecem intactas**: {n_arestas} aresta(s) tocam RC-018 hoje em `RELACOES` — a rede deste termo é só a que o
  cadastro já registrava, e nenhuma linha foi acrescentada;
- o cadastro lista em `relacionados` os códigos {", ".join(f"`{x.strip()}`" for x in (lin[6] or "").split(";") if x.strip())}:
  **não há arestas correspondentes** para eles, e três deles nem arquivo têm. Abrir essas arestas é decisão
  curatorial e continua pendente — a ficha declara a lacuna em vez de preenchê-la.

**O que a fonte muda e o que não muda (D-9, sem harmonização):** a fala de 2023 dá **um censo próprio** para o que
está a bordo — `cerca de 900, quase 1000` corrigido em seguida para `938 figuras` — e é a mesma grandeza que os
ciclos anteriores registraram para a **família** (936 em P2022-03-26; 900Q; 13 membros em `RC-491`). As quatro
magnitudes coexistem, cada uma com sua fonte e data; nada é médio, nada é arredondado, e `RC-491` **não** foi
editada por este ciclo.

**Origem do conteúdo da ampliação:** palestra `{SIGLA} — {TITULO}` (na sala, 03/12/2023), blocos U0004 e U0016 do
`original.txt` — transcrição automatizada, **não conferida com o áudio**. Cada aspa foi recortada byte a byte por
`_gerar_ampliacoes_{SIGLA}.py` sobre o caça-âncoras `_aspas_{SIGLA}.py`; nada foi digitado de memória.

## Etimologia / Grafias

- **Canônico da Base:** *Alt´Lam Gron* — com **acento agudo** (`´`, U+00B4), não crase, não cedilha: é a grafia do
  cadastro e ela preside o nome da ficha.
- **Na fonte oral (P2023-12-03)** o nome aparece **degradação a baixo pelo STT em três formas** —
  `Alto Longró`, `Alto Langron`, `Alto Longron` — nunca como o par `Alt´Lam` + `Gron` do cadastro. `[REVISAR]`:
  nenhuma delas promotiona a grafia canônica, e nenhuma hipótese etimológica é feita a partir do TXT.
- **Vetado** (devolutiva de 29/08/2026, D-4): nenhuma das máscaras do STT (`p****`, `m****`, `b******`, `e******`)
  transita para esta ficha. As nove ocorrências ficam na apostila, com a moldura, onde o leitor vê que são máscara.

## Ampliação — {SIGLA} ({TITULO})

{bloco_de("RC-018")}

## Fontes
{fontes_tabela("RC-018")}

## Termos Relacionados
{tabela_rel("RC-018", [
 "| Alt´Lam | RC-017 | par nomeador — `RC-017` também está **sem arquivo**; nenhum dos dois recebeu materialização |",
 "| Processador Val | RC-089 | a fala põe o processador da família **dentro** da nave: mesma cena, duas fichas |",
])}

## Observações

* **[REVISAR] — o censo é da fala, não da Base.** «938 figuras» e «uns 600 e poucos» na Terra pertencem a um só
  fôlego de 03/12/2023 e não foram reconciliados com os 936/900Q dos ciclos anteriores nem com os 13 membros de
  `RC-491`. Registrar a divergência datada é o serviço desta ficha; resolvê-la é decisão curatorial.
* **[REVISAR] — evento datado.** A visita («Sofia esteve aqui nos anos 2018, 19») é a única data *recente* que esta
  fonte aplica a um objeto da malha; não virou relação, não virou cronologia da ficha e não foi confrontada com as
  datas de aparição já registradas em outras fichas.
* Esta ficha **não** afirma que a nave exista fisicamente no Atlântico Norte: transcreve, com endereço, a afirmação
  de que ela «pulou umita para cima e continuou flutuando» como a fonte a disse, em 2023.
"""

# ══════════════════════════════ RC-040 ══════════════════════════════
lin = CAD["RC-040"]
ar = arestas_de("RC-040")
RC040 = f"""# CFD (Código Fonte Definidor) — RC-040

| Campo | Valor |
|---|---|
| **Categoria Principal** | {lin[2].title()} |
| **Subcategoria** | {lin[3]} |
| **Status** | 🟡 {lin[4].capitalize()} |
| **Última atualização** | {DATA} |

## Definição Sintética

**CFD — Código Fonte Definidor** é o princípio pelo qual a criação biológica tem uma definição de si escrita antes
de qualquer experiência: o código que **define** o que um ser pode vir a ser, e que por isso pode ser corrompido,
organizado, reciclado. Esta ficha existia **só no cadastro** — `ficha=False`, sem arquivo — embora fosse um dos
códigos com **mais obras apontando para ele** ({len([f for f in (lin[5] or []) if not f.startswith('P')])} B-códigos)
e um dos poucos com arestas de verdade na rede ({len(ar)}). A fonte oral de **03/12/2023** é a primeira que diz
para que serve a organização desse código: «ou isso aqui fica organizado ou jamais esse ser aqui terá paz» — ou
seja, o CFD não é metáfora de destino, é **condição de habitabilidade psíquica** do criador.

## Contexto / Origem

**Materialização (não é criação).** A **Devolutiva do Curador de 29/08/2026 (D-10)** autorizou a virada
`ficha=False → ficha=True` «dada a robustez técnica apresentada pela fonte»: o CFD é um dos três códigos que esta
palestra ilumina sem ter arquivo, e um dos dois que o Curador materializou. `RC-444 Família Cromon`, o terceiro
candidato, foi nominalmente recusado e segue `ficha=False`.

Com isso:

- a Base passa de **458 para 460 arquivos de ficha** e o cadastro de **457 para 459** linhas `ficha=True`;
- o cadastro continua em **777 termos** (teto curatorial; `RC-778` não consumido) e as **1.856 relações
  permanecem intactas**: as {len(ar)} arestas que tocam RC-040 são todas pré-existentes — nenhuma foi aberta,
  fechada ou reetiquetada por este ciclo;
- a definição acima **não** é uma síntese doutrinal nova: é a leitura do que já estava nas obras vinculadas,
  ladeada pelo que a fala de 2023 acrescenta, cada parte com sua fonte.

**Tensão a não escondar (sem harmonização):** a fala de 03/12/2023 diz que o código fonte definidor **é o código de
Javé** («tudo é feito a partir do código fonte definidor do criador, ou seja, do código de Javer»). Isso não é
identicamente o que as obras catalogadas sustentam sobre o CFD, e a Base **não** unifica as duas formulações: a
aspa fica datada aqui, e a eventual revisão do verbete nas obras continua pendente. `RC-424` (inserido-em) e
`RC-742` (é-falência-de) mantêm as arestas que já tinham, exatamente como estavam.

**Origem do conteúdo da ampliação:** palestra `{SIGLA} — {TITULO}` (na sala, 03/12/2023), bloco U0004 do
`original.txt` — transcrição automatizada, **não conferida com o áudio**. Cada aspa foi recortada byte a byte por
`_gerar_ampliacoes_{SIGLA}.py` sobre o caça-âncoras `_aspas_{SIGLA}.py`; nada foi digitado de memória.

## Etimologia / Grafias

- **Canônico da Base:** *CFD (Código Fonte Definidor)* — a sigla é do cadastro e das obras; **a sigla não é dita**:
  no `original.txt` de 2023 a forma `CFD` tem **0 ocorrências**, e o que se ouve é a expressão por extenso
  (`código fonte definidor`, 2×, sempre seguida de `do criador`).
- **Na fonte oral (P2023-12-03):** o STT grafa `padroes arquétipos` e degrada o nome de Javé para `Javer` na
  segunda ocorrência. `[REVISAR]` — as formas entram como vieram, sem emenda.
- **Vetado** (devolutiva de 29/08/2026, D-4/D-5): nenhuma máscara do STT entra nesta ficha, e a frase que associa o
  CFD ao «criador» não é lida como negação de Deus — a cláusula «desloca o título de Deus do criador da obra» mora
  em `RC-001`/`RC-042`/`RC-742`, onde o despacho a exigiu.

## Ampliação — {SIGLA} ({TITULO})

{bloco_de("RC-040")}

## Fontes
{fontes_tabela("RC-040")}

## Termos Relacionados
{tabela_rel("RC-040", [
 "| Criação do universo biológico (três fornos) | RC-104 | o ato de replicação cuja definição é o CFD — aresta só se o cadastro já a tivesse |",
 "| Falência dos deuses | RC-742 | aresta `é-falência-de` (P2024-08-03) já registrada; este ciclo **não** a reforça |",
])}

## Observações

* **[REVISAR] — estado das arestas.** Dos cinco códigos listados em `relacionados`, só {len([r for r in (lin[6] or '').split(';') if r.strip() and any(a[0]=='RC-040' or a[2]==r.strip() for a in ar)])}
  tem aresta correspondente em `RELACOES`. A desproporção (muita obra, pouco grafo) é o motivo pelo qual este
  código era candidato a materialização **sem** ser candidato a relação nova: a Base ganha o arquivo, não ganha
  rede.
* Esta ficha **não** converte o CFD em termo operacional de nada: não há código de procedimento, não há uso
  computacional, não há paralelo com «código-fonte» em engenharia de software. O sentido é o das obras vinculadas
  (definição escrita da vida biológica) mais o que a fala de 2023 acrescenta sobre organização e paz.
"""

for cod, corpo in (("RC-018", RC018), ("RC-040", RC040)):
    alvo = arquivo_de(cod)
    novo = not os.path.exists(alvo)
    open(alvo, "w", encoding="utf-8").write(corpo)
    print(f"{'criada' if novo else 'REESCRITA'}: {os.path.relpath(alvo, RAIZ)} · {len(corpo):,} chars".replace(",", "."))
    assert f"## Ampliação — {SIGLA}" in corpo
print(f"arestas tocando RC-040: {len(arestas_de('RC-040'))} (pré-existentes) · RC-018: {len(arestas_de('RC-018'))}")
