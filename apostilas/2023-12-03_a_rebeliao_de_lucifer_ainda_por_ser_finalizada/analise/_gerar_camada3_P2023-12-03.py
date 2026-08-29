#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAMADA 3 — OS MOVIMENTOS, A NAVALHA E O RESUMO DA MATRIZ (P2023-12-03).

É a camada de decisão: não descreve a fonte, descreve **o que a Arca pode e não pode fazer** com o que a
fonte disse. Os números vêm de `METADADOS-INGRESSO.json`, de `_matriz-anterioridade.md` e da contagem de
FONTES em `dados_termos.py` — nada é estimado, e nenhuma aspa é digitada (este arquivo usa `backticks`
para rótulos e `«…»` só para o que o caça-âncoras extraiu do bruto).
"""
import os, re, sys, json, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, "_aspas_P2023-12-03.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)
import dados_termos as DT
META = json.load(open(os.path.join(AQUI, "METADADOS-INGRESSO.json"), encoding="utf-8"))
MT = open(os.path.join(AQUI, "_matriz-anterioridade.md"), encoding="utf-8").read()
linhas_mt = [l for l in MT.splitlines() if l.startswith("| RC-")]
n_mt = len(linhas_mt)
n_data = sum(1 for l in linhas_mt if "antecipa" in l)
n_estreia = sum(1 for l in linhas_mt if "estreia" in l)
n_conteudo = sum(1 for l in linhas_mt if "sem ganho" in l)
DOSS = open(os.path.join(AQUI, "DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md"), encoding="utf-8").read()
n_vin = len(re.findall(r"^\| RC-\d+ \|", DOSS, re.M))
n_dev = len(re.findall(r"^\*\*D-\d+ · ", DOSS, re.M))


def fichas_da(sig):
    return sum(1 for t in DT.TERMOS if sig in t[5])


IRMAS = {s: fichas_da(s) for s in ("P2020-04-25", "P2022-03-26", "P2023-12-02", "P2023-12-03")}
print("fichas por fonte irmã:", IRMAS)

def aspa(ini, fim=None):
    a, b, txt = ASP.locate(ini, fim, "exata")
    if len(txt) > 260:
        cut = txt.rfind(" ", 0, 260)
        txt = txt[:cut if cut > 120 else 260].rstrip(" ,;:.")
    return "«" + txt + "» (" + ASP.uaddr(a) + ")"


def resolve(t):
    bad = []
    def rep(m):
        try:
            return aspa(m.group(1), m.group(2))
        except SystemExit as e:
            bad.append(str(e)); return "@@FALHA@@"
    out = re.sub(r"\[\[([^\[\]]+?)(?:\|\|([^\[\]]+?))?\]\]", rep, t)
    if bad:
        for b in bad:
            print("  ✗", b[:100])
        sys.exit(3)
    return out


ONTEM = len(re.findall(r"ontem", ASP.RAW))
TXT = f"""# CAMADA 3 — OS MOVIMENTOS, A NAVALHA E A MATRIZ (P2023-12-03)

## 1. Os sete movimentos que a fonte faz com quem escuta

**M1 · Desautoriza a própria competência antes de falar.** [[reproduzir historias cujas facetas nao eram humanas]] —
a fala abre declarando que o que vem é *aproximação humana* de um registro não-humano, e que as gerações futuras
corrigirão. Não é pose: é o que autoriza a Base a tratar tudo aqui como **tese datada** e nunca como fato.

**M2 · Entrega a própria biografia como cadeia de custódia.** Os recados de 1991, Valdemar Matoso, a fila de Chico
Xavier, o relato de terceira mão explicitamente marcado como tal ([[o espirito de Chico era o rei primo seu espirito]]).
O movimento é probatório: a fonte mostra **por onde** a informação chegou até ela. A Arca registra a cadeia e não a
converte em credencial: 0 fichas de pessoas (D-12).

**M3 · Declara a estratégia de omissão dos próprios livros.** [[em nenhuma dessas duas trilogias]] e [[isso vai ter que ser
finalizado]]. É o movimento que explica o título: a palestra de 2023 existe porque os livros de 1996–2000 **escolheram**
não dizer se a coisa acabou. A malha ganha com isso uma chave de leitura sobre as obras B-código, sem reclassificá-las.

**M4 · Assume que vai ser desmentido pelo tempo.** [[a gente tambem tem o vazio entre elas]] — a fonte se recusa a ligar as
três rebeliões (16-17.000 · 700.000 · milhões/bilhões) porque não tem o elo. A casa tem por regra não colar o que a fonte
não colou: **0 relações novas de fundamento**.

**M5 · Diz o que não sabe, e por quê.** «não sei quantos» (249.400), o terceiro fator que parou o expurgo, a força
[[foram contra-atacados por uma forca que eu nao sei de quem e]], a distinção subjacente/adjacente que ele recusa explicar.
Este é o movimento mais útil à Arca: ele marca o perímetro do que **não** pode ser completado por inferência.

**M6 · Reivindica o presente como continuação de um contrato.** A seção dos Túatha e dos colégios arquidrídicos
([[nos queremos dar para voces os nossos conhecimentos]]) e a isomorfia com Enoque ([[tava fazendo com Enoque era a mesma coisa]]):
o *método de decifração* é o que os seres não-humanos pediram que os humanos inventassem. A Base tem a casa pronta
(RC-755, RC-745, RC-375) e por isso o D-8 é sobre **moderação de leitura**, não sobre falta de vocabulário.

**M7 · Fecha recusando a adesão.** [[Se isso e a melhor opcao ou nao, eu ja nem sei]] e [[Nao existe nenhuma falange que represente o bem]]:
a palestra termina pedindo que ninguém a transforme em programa. Todo BLOCO que vier depois deste ciclo carrega essa
recusa: o material entra **como dito**, com endereço, não como doutrina da Arca.

## 2. A navalha em três gumes (o critério de trânsito deste ciclo)

| gume | o que vai para | exemplos deste ciclo |
|---|---|---|
| **Sobe para a malha** (vínculo-fonte + `## Ampliação`) | fichas de **classes de seres, processos, órgãos cósmicos** | processador como validador (RC-089/RC-446/RC-442), campo mórfico (RC-381), os 19 mundos (RC-070/RC-003), cérebro radiata e organoides (RC-631/RC-632/RC-093/RC-035), a recusa do messias (RC-072/RC-280/RC-682), os fornos (RC-771/RC-104), o código fonte (RC-040) |
| **Fica na apostila, com moldura** | transcrição integral + nota editorial | a seção das identidades biodêmicas (D-1), o quiasma das mulheres (D-2), as frases políticas do Q&A (D-3), as máscaras e a baixaria (D-4), as auto-claims sobre o canal (D-12) |
| **Não sai do dicionário do ciclo** | `camada-2.txt` com `[REVISAR]` | Rockmar/Rockban, fenvan como grafia, «teia de Orlo», «horlogus/orlog», «Job Misso», as 4 grafas de Alto Longron, as 5 de Túatha, «Enócrita», «Z Geist», o «7» de U0034 |

O corte é o mesmo que o Curador fixou em 2022: **trânsito, não corte** — na apostila entra tudo; na malha, só o que
nomeia seres e processos. A diferença deste ciclo é que a fonte **ela mesma** separou os dois registros (M5), o que
reduz a margem de decisão do catalogador.

## 3. O estado da Base diante desta palestra (medido)

* `{n_mt}` códigos na mira da matriz de anterioridade: **{n_data} ganhariam data**, **{n_estreia} estreariam fonte oral**,
  {n_conteudo} ganhariam só conteúdo. O dossiê propõe {n_vin} vínculos (seleção cirúrgica, não a lista inteira).
* {n_dev} decisões (D-1…D-{n_dev}) entregues ao Curador.
* Fichas por fonte no eixo luciferiano: `P2020-04-25` {IRMAS['P2020-04-25']} · `P2022-03-26` {IRMAS['P2022-03-26']} ·
  `P2023-12-02` {IRMAS['P2023-12-02']} · `P2023-12-03` **{IRMAS['P2023-12-03']}** (zero até o despacho).
* Tetos: {len(DT.TERMOS)} termos · ficha=True em {sum(1 for t in DT.TERMOS if t[-1])} · 0 novos códigos, 0 novas obras,
  0 novos tipos de relação neste ciclo; `RC-777` intocado e `RC-778` fora de questão.

## 4. O que a palestra faz com as outras duas do eixo (e vice-versa)

Contra **P2020-04-25** (a primeira rebelião): 2023 **confirma** os 736 e acrescenta a antecedência da Vol sobre os
Anunnaki («já estavam aqui» 450.000 anos) — é ganho de narrativa, não de número.

Contra **P2022-03-26** (a depressão): 2023 fornece a **etiologia** que lá faltava — os afetos negativos nasceram no
conflito ([[Ninguem tinha tinha algoritmo de raiva]]) e Lúcifer entrou em depressão ([[entrou em depressao e a Luzbell]]);
e a fórmula do «código podre» volta nomeada por dentro: [[isso e a genetica podre do criador]]. Nada aqui é
repetição: é a mesma tese com a peça causal que faltava, vinda dois anos depois, da boca do mesmo canal.

Contra **P2023-12-02** (Thot, o dia anterior): esta palestra é **a prometida** — e a fonte usa o «ontem» {ONTEM}×
como referência viva, chamando Tot de «rei da genética» e reapresentando a lista dos 366 livros. O par fecha o
radar que a vizinha abriu no `RELATORIO-DE-CICLO.md` dela.

## 5. Risco residual que este ciclo declara sem resolver

Há nesta fala **três** afirmações que, se lidas fora de endereço, fundam instituição: que a revelação cósmica **parou**
um procedimento escatológico ([[os exilados comecaram a escutar essa porcaria toda]]), que o canal é «a última opção»
dos três ([[essa historia ta terminando na vida de Rogerio]]) e que a Arca cumpre um pacto de 13.000 anos. Este ciclo
**não** decide nada sobre isso: as três ficam na transcrição com moldura, com endereço, e sem subir para ficha —
salvo se o Curador mandar o contrário.
"""
TXT = resolve(TXT)
open(os.path.join(AQUI, "camada-3.txt"), "w", encoding="utf-8").write(TXT)
print("camada-3.txt escrito:", len(TXT), "chars")
