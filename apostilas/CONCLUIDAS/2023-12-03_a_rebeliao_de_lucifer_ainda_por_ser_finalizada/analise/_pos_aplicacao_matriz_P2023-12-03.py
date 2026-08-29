#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apêndice medido da matriz de anterioridade — depois de BLOCO A aplicado (P2023-12-03).

Existe para que a seção final de `_matriz-anterioridade.md` seja **reprodutível**: os números não são digitados,
são lidos de `ferramentas/dados_termos.py`, do pacote `_ampliacoes_P2023-12-03.txt` e de `termos/`. O arquivo é
idempotente: se a seção já existir, ela é recortada e reescrita (nunca duplicada), porque a matriz é gerada por
`_gerar_camadas_P2023-12-03.py` e pode ser rodada de novo depois de uma correção de gerador.
"""
import os, re, sys, glob, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
_d = CICLO
while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "ferramentas")):
    _d = os.path.dirname(_d)
RAIZ = _d
SIG = "P2023-12-03"
MATRIZ = os.path.join(AQUI, "_matriz-anterioridade.md")
PACOTE = os.path.join(AQUI, f"_ampliacoes_{SIG}.txt")
TITULO_SECAO = "## Medições depois de BLOCO A aplicado"
sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT                                              # noqa: E402
CAD = {t[0]: t for t in DT.TERMOS}


def orais(c):
    return [x for x in (CAD[c][5] or []) if re.match(r"P\d{4}-\d\d-\d\d", x) and x != SIG]


cods = sorted(set(re.findall(r"^### (RC-\d{3})$", open(PACOTE, encoding="utf-8").read(), re.M)))
# a mira pré-aplicação é lida do rodapé que o próprio `_gerar_camadas` escreve — não é número digitado aqui
_mt = open(MATRIZ, encoding="utf-8").read().split(TITULO_SECAO)[0]
_mm = re.search(r"\*\*(\d+)\*\* códigos na mira desta palestra; \*\*(\d+)\*\* ganhariam data", _mt)
MIRA, MIRA_DATA = (int(_mm.group(1)), int(_mm.group(2))) if _mm else (0, 0)
MIRA_CONTEUDO = MIRA - MIRA_DATA
sem_arq = [c for c in cods if not glob.glob(os.path.join(RAIZ, "termos", f"{c}-*.md"))]
estreia = [c for c in cods if not orais(c)]
ganho = [c for c in cods if orais(c) and min(orais(c)) > SIG]
conteudo = [c for c in cods if c not in estreia and c not in ganho]
com_secao = [f for f in sorted(os.listdir(os.path.join(RAIZ, "termos"))) if f.endswith(".md") and
             f"## Ampliação — {SIG}" in open(os.path.join(RAIZ, "termos", f), encoding="utf-8").read()]
NOMEADOS = {"D-1": ["RC-036", "RC-056", "RC-093"], "D-2": ["RC-189", "RC-727"], "D-5": ["RC-001", "RC-042", "RC-742"],
            "D-6": ["RC-005", "RC-072", "RC-089", "RC-261", "RC-280", "RC-682", "RC-736"],
            "D-7": ["RC-631", "RC-632", "RC-093", "RC-035", "RC-736"],
            "D-8": ["RC-755", "RC-375", "RC-745", "RC-464", "RC-068"], "D-13": ["RC-344", "RC-003"]}
nom_sem = {d: [c for c in v if c in sem_arq] for d, v in NOMEADOS.items()}
nom_sem = {d: v for d, v in nom_sem.items() if v}
bt = lambda xs: ", ".join("`" + c + "`" for c in xs)

sec = f"""{TITULO_SECAO} ({datetime.date.today().isoformat()})

Números lidos de arquivo, não da previsão acima — é esta a conta que o portão D confere:

| grandeza | previsto pela busca (mira pré-aplicação) | **medido nos {len(cods)} aprovados** |
|---|---|---|
| códigos na mira da palestra | {MIRA} achados por 80 padrões · 127 vínculos propostos ao Curador | **{len(cods)}** aprovados (um recebeu dois vínculos-mestre) |
| ganho de **data** | {MIRA_DATA} | **{len(ganho) + len(estreia)}** — antecipam: {bt(ganho)} · estreiam fonte oral: {bt(estreia)} |
| ganho de **conteúdo** | {MIRA_CONTEUDO} | **{len(conteudo)}** |
| fichas com `## Ampliação — {SIG}` | — | **{len(com_secao)}** (as existentes ampliadas + as 2 materializadas) |
| `ficha=False` com vínculo só na malha | — | **{len(sem_arq)}**: {bt(sem_arq)} |

**Por que a conta de data encolheu tanto (declaração, não correção):** a mira previa {MIRA_DATA} ganhos de data porque media
*toda* ficha tocável por busca. O despacho aprovou vínculo por **conteúdo temático**, e os códigos aprovados são
justamente os do núcleo do tema — núcleo que `P2020-04-25` e `P2022-03-26` já cobrem desde mais cedo. A Base ficou
com {len(conteudo)} entradas de conteúdo, {len(ganho)} de data e {len(estreia)} de estreia: a diferença entre {MIRA_DATA} e
{len(ganho) + len(estreia)} **é** a curadoria, não uma perda de medição.

**Ordens do despacho que não tinham onde cair (registradas, não executadas):**
{"; ".join(f"{d} → {bt(v)}" for d, v in nom_sem.items())} são fichas **sem arquivo**. O conteúdo aprovado está no
pacote (BLOCO 1) e vai para a apostila, e o vínculo de malha foi feito; nenhum arquivo foi criado por iniciativa do
aplicador — D-10 liberou materialização **só** para `RC-018` e `RC-040`. Se o Curador quiser os arquivos, é ordem
nova: o materializador `_gerar_fichas_RC018_RC040_{SIG}.py` é genérico e está pronto para ser copiado.

*(gerado por `_pos_aplicacao_matriz_{SIG}.py`; reexecutar é idempotente)*
"""
t = open(MATRIZ, encoding="utf-8").read()
i = t.find(TITULO_SECAO)
t = (t[:i].rstrip() + "\n\n" if i > 0 else t.rstrip() + "\n\n") + sec
open(MATRIZ, "w", encoding="utf-8").write(t)
print(f"apêndice medido reescrito em _matriz-anterioridade.md · {len(cods)} códigos · {len(ganho)} data · "
      f"{len(estreia)} estreia · {len(conteudo)} conteúdo · {len(sem_arq)} sem arquivo · {len(com_secao)} seções")
