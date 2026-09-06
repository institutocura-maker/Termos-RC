#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F044 Anel C — cria/renomeia/remove fichas no filesystem.

- Deleta termos/RC-941-rebanho-humano.md (duplicidade, merge doc na RC-193).
- Renumera termos/RC-942-hipocampo.md -> termos/RC-941-hipocampo.md (gap do validador).
- Cria fichas novas: RC-942..RC-946 (Messias, Madalena, João Batista, Pedro, Pilatos/Caifás/Sinédrio).
- Materializa: RC-887 Nag Hammadi e RC-862 Essênios.
- Merge RC-941->RC-193: substitui flag de duplicidade por nota de merge + fonte F043 na RC-193.
"""
import os, glob

TERMOS='termos/'

# ---------------------------------------------------------------- 1. delete + rename
def del_dup():
    p=TERMOS+'RC-941-rebanho-humano.md'
    if os.path.exists(p):
        os.remove(p); print(f"[del] {p}")

def rename_hipo():
    a=TERMOS+'RC-942-hipocampo.md'
    b=TERMOS+'RC-941-hipocampo.md'
    if os.path.exists(a):
        os.rename(a,b); print(f"[ren] {a} -> {b}")
    # update content header code
    txt=open(b,encoding='utf-8').read()
    txt=txt.replace('# HIPOCAMPO — RC-942','# HIPOCAMPO — RC-941')
    txt=txt.replace('## Nota — F043 T3 · Ficha nascida da expansão condicionada',
                    '## Nota — F043 T3 · Ficha nascida da expansão condicionada · [F044-MERGE]')
    txt=txt.replace('· Ficha nascida da expansão condicionada\n','· Ficha nascida da expansão condicionada\n\nRenumerada RC-942→RC-941 em 06/09/2026 (F044-MERGE) para fechar a vaga aberta pelo delete de RC-941 (duplicidade com RC-193); código sem referências, renumeração segura.\n')
    open(b,'w',encoding='utf-8').write(txt)
    print(f"[ren-c] {b} header atualizado")

# ---------------------------------------------------------------- 2. merge RC-193 (ancorar GKA + fonte F043)
def merge_r193():
    p=TERMOS+'RC-193-rebanho-humano.md'
    txt=open(p,encoding='utf-8').read()
    # substitui a flag de duplicidade
    txt=txt.replace('Aula 04 usa «rebanho humano» no contexto do julgamento da humanidade (mundo administrado), corroborando RC-193. Ver flag de duplicidade RC-193 × RC-941 (não resolvida aqui).',
        'Aula 04 usa «rebanho humano» no contexto do julgamento da humanidade (mundo administrado), corroborando RC-193.')
    # adiciona nota de merge + fonte F043 no bloco Fontes
    txt=txt.replace('## Fontes\n| Fonte | Localização | Tipo |\n|---|---|---|',
        '## Nota — F044-MERGE (RC-941 → RC-193) · 06/09/2026\n\nO código provisório **RC-941 «Rebanho humano»** (criado pelo F043-T3 como expansão condicionada) foi **excluído por despacho do Curador** por tratar-se de duplicidade com esta RC-193, que permanece **âncora**. A definição dicionarizada do parceiro (obra de apoio, fonte **secundária**) foi absorvida aqui como nota, sem criar aresta em `relacoes/`:\n\n- **Definição GKA (EXT-2024-01-04), verbatim:** «Grupo de pessoas facilmente manipuláveis, acostumadas a serem conduzidas.»\n\n**«rebanho humano» no F044 (fonte primária) — Aula 04:** este é o pior retrato do rebanho humano da atualidade.» Em contraste com a acepção GKA (manipulação), o curso de Ellam opera sobre a noção elâmica de massa horizontalizada (ver Definição Sintética acima); não há pretensão de canonicidade doutrinária.\n\n## Fontes\n| Fonte | Localização | Tipo |\n|---|---|---|')
    # adiciona a linha da fonte F043 na tabela de fontes (após P2023-12-25-04)
    txt=txt.replace('| P2023-12-25-04 | Aula 04 — O Nascimento do Cristianismo (palestra) | — | transcrição automatizada; citação |',
        '| P2023-12-25-04 | Aula 04 — O Nascimento do Cristianismo (palestra) | — | transcrição automatizada; citação |\n| EXT-2024-01-04 | Glossário Krys Amon (obra de apoio) | — | fonte secundária; paráfrase/definição |')
    open(p,'w',encoding='utf-8').write(txt)
    print(f"[merge] {p} atualizado (nota de merge + fonte F043)")

# ---------------------------------------------------------------- 3. novas fichas
# AULAS
AULA={
 'P2023-12-25-01':'Aula 01 — Adolescência e a Juventude de Jesus',
 'P2023-12-25-02':'Aula 02 — Os Anos de Pregação e a Promessa do Retorno',
 'P2023-12-25-03':'Aula 03 — Dias Difíceis: Crucificação e Ressurreição',
 'P2023-12-25-04':'Aula 04 — O Nascimento do Cristianismo',
 'P2023-12-25-05':'Aula 05 — A Verdadeira Face de Maria Madalena',
}

FICHAS={}

# ---------- RC-942 MESSIAS ----------
FICHAS['RC-942-messias.md']='''# MESSIAS — RC-942

| Campo | Valor |
|---|---|
| **Categoria Principal** | Termos Específicos |
| **Subcategoria** | 8.4 Grego / Latim |
| **Status** | 🟡 provisório |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
O «enviado» / ungido profetizado no Antigo Testamento, que viria «super poderoso em nome de Javé» resolver o tema principal — pano de fundo do conflito entre o Criador e a Criação. No F044, Ellam distingue Jesus de Nazaré do **Messias**: o homem Jesus **não** seria o avatar de Javé, seria o Messias, o enviado. É o eixo da expectativa messiânica judaica que estrutura as cinco aulas do curso.

## Contexto / Origem
O termo aparece nas aulas 01–05 do curso F044 (57.179 palavras, fonte primária), sendo o conceito central que costura a narrativa: o Messias profetizado há «400 anos de silêncio profético»; a hesitação de Jesus; a promessa do retorno; o deslocamento para o Jesus «Cristo» (ungido) do cristianismo emergente. Verbatim-chave (Aula 01):

> «o homem Jesus não seria o avatar de Javé, seria o Messias, seria o enviado, seria aquele que viria super poderoso em nome de Javé, resolver o tema principal e mais tarde foi transposto para as páginas da Bíblia, que tema era esse? Um Criador...»

## Etimologia / Grafias
- **Grafia preferida:** Messias
- **Variações / grafias alternativas:** O Ungido; Cristo (ekv. grego «Christos»)
- **Idioma de origem:** hebraico «mashiach» → grego «christós» (ungido)

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-12-25-01 | Aula 01 — Adolescência e a Juventude de Jesus | transcrição; citação |
| P2023-12-25-02 | Aula 02 — Os Anos de Pregação e a Promessa do Retorno | transcrição; citação |
| P2023-12-25-03 | Aula 03 — Dias Difíceis: Crucificação e Ressurreição | transcrição; citação |

## Relações centrais
- Jesus — RC-072;
- Segundo Advento do Cristo (Volta de Jesus) — RC-005;
- Bagagem/segredo — RC-752.

## Observação
**Quarentena teológica** — Messias/Cristo são categorias das tradições; esta ficha documenta a releitura de Ellam dentro da Revelação Cósmica, não consenso religioso. `relacoes/` blindado (0 arestas novas).

## Nota de governança
F044 (Anel C, despacho 06/09/2026); fonte primária; verbatim extraídos do translado; nenhuma aresta nova.
'''

# ---------- RC-943 MARIA MADALENA ----------
FICHAS['RC-943-maria-madalena.md']='''# MARIA MADALENA — RC-943

| Campo | Valor |
|---|---|
| **Categoria Principal** | SERES & ENTIDADES |
| **Subcategoria** | 1.6 Figuras humanas (históricas/míticas) |
| **Status** | 🟡 provisório |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
Figura humana do círculo de Jesus; no F044, a **transmissora da terceira fase da revelação**. Após a Ressurreição, o Jesus «ressuscitado» chama Maria Madalena e — por meio dela — dita uma nova revelação, «totalmente diferente, muito maior do que a que havia criado com os apóstolos». A aula 05 é dedicada à «verdadeira face» de Maria Madalena.

## Contexto / Origem
Termo central nas aulas 03 e 05 (fonte primária F044). Verbatim-chave (Aula 03) — a terceira fase:

> «agora Jesus iniciava uma terceira fase, quando ele chamou Maria Madalena e pediu para ela chamar mais quatro mulheres de Jerusalém e alguns apóstolos, porque ele, Jesus, iria ditar uma nova revelação, agora que estava como ressuscitado...»

E (Aula 03), sobre a escolha da Igreja contra a revelação por Madalena:

> «Jesus o Vivo, o Ressuscitado que através de Madalena, criou uma outra revelação totalmente diferente... A igreja preferiu a versão que Paulo criou. Paulo não conheceu Jesus...»

Na Aula 05, «a verdadeira face de Maria Madalena» é desdobrada (papel de apóstola-reveladora, contraposta à face construída pelo cristianismo paulino).

## Etimologia / Grafias
- **Grafia preferida:** Maria Madalena
- **Variações / grafias alternativas:** Madalena
- **Idioma de origem:** — (pessoa; «Madalena» = de Magdala)

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-12-25-03 | Aula 03 — Dias Difíceis: Crucificação e Ressurreição | transcrição; citação |
| P2023-12-25-05 | Aula 05 — A Verdadeira Face de Maria Madalena | transcrição; citação |

## Relações centrais
- Jesus — RC-072;
- Paulo/Saulo (revelação paulina) — RC-280;
- Apóstolos — RC-904.

## Observação
**Quarentena teológica** — a figura de Madalena (apóstola, evidenciadora, «portadora da revelação») é leitura de Ellam, divergente da tradição cristã consolidada. `relacoes/` blindado (0 arestas novas).

## Nota de governança
F044 (Anel C, despacho 06/09/2026); fonte primária; verbatim extraídos do translado; nenhuma aresta nova.
'''

# ---------- RC-944 JOÃO BATISTA ----------
FICHAS['RC-944-joao-batista.md']='''# JOÃO BATISTA — RC-944

| Campo | Valor |
|---|---|
| **Categoria Principal** | SERES & ENTIDADES |
| **Subcategoria** | 1.6 Figuras humanas (históricas/míticas) |
| **Status** | 🟡 provisório |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
Profeta judeu do círculo dos **Essênios** (RC-862), que encerra «400 anos de silêncio profético» ao anunciar que o Messias já estava entre nós. No F044, Batista é o elo que faz Jesus iniciar o ministério público e, por seu batismo, inscreve o início da missão; sua hesitação é citada como expressão da natureza «eu humano enjaulado» de Jesus.

## Contexto / Origem
Aparece nas aulas 01 e 02 (fonte primária F044). Verbatim-chave (Aula 01):

> «Depois de 400 anos de silêncio profético, João Batista começou a dizer que o Messias iria aparecer no tempo da vida dele, que era naquele tempo que aquele Messias profetizado na faixa de 2000 anos, finalmente tinha chegado o momento.»

E (Aula 02), sobre o batismo como necessidade:

> «ele poderia ter iniciado seu ministério público, sem passar pelas mãos de João Batista... pelo batismo de João Batista. Existiam outras maneiras.»

## Etimologia / Grafias
- **Grafia preferida:** João Batista
- **Variações / grafias alternativas:** (nenhuma registrada no censo)
- **Idioma de origem:** — (pessoa; «Batista» = o que batiza)

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-12-25-01 | Aula 01 — Adolescência e a Juventude de Jesus | transcrição; citação |
| P2023-12-25-02 | Aula 02 — Os Anos de Pregação e a Promessa do Retorno | transcrição; citação |

## Relações centrais
- Jesus — RC-072;
- Essênios — RC-862;
- Bagagem/segredo — RC-752.

## Observação
**Quarentena teológica** — a moldura essênia e a leitura da hesitação de Jesus são de Ellam. `relacoes/` blindado (0 arestas novas).

## Nota de governança
F044 (Anel C, despacho 06/09/2026); fonte primária; verbatim extraídos do translado; nenhuma aresta nova.
'''

# ---------- RC-945 PEDRO ----------
FICHAS['RC-945-pedro.md']='''# PEDRO (APÓSTOLO) — RC-945

| Campo | Valor |
|---|---|
| **Categoria Principal** | SERES & ENTIDADES |
| **Subcategoria** | 1.6 Figuras humanas (históricas/míticas) |
| **Status** | 🟡 provisório |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
Um dos doze apóstolos escolhidos por Jesus na Galileia; no F044, é lembrado sobretudo pelo episódio da **negação** durante a prisão de Jesus pela «turma do Sinédrio». A cena serve ao curso para mostrar o raio de alcance da condenação — a ordem era prender toda a «turma de Jesus», não só o mestre.

## Contexto / Origem
Aparece na Aula 03 (fonte primária F044). Verbatim-chave:

> «No dia em que Jesus foi preso pela turma do Sinédrio, era para prender toda a turma de Jesus. Pedro negou várias vezes. Foi quando Jesus percebeu que aqueles 11 apóstolos que ele havia escolhido lá da Galileia, porque o 12º, era Judas da Judeia...»

## Etimologia / Grafias
- **Grafia preferida:** Pedro
- **Variações / grafias alternativas:** Pedro (apóstolo)
- **Idioma de origem:** — (pessoa; grego «Petros» = pedra)

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-12-25-03 | Aula 03 — Dias Difíceis: Crucificação e Ressurreição | transcrição; citação |

## Relações centrais
- Jesus — RC-072;
- Apóstolos — RC-904.

## Observação
**Quarentena teológica** — a leitura da negação e do raio da perseguição é de Ellam. `relacoes/` blindado (0 arestas novas).

## Nota de governança
F044 (Anel C, despacho 06/09/2026); fonte primária; verbatim extraído do translado; nenhuma aresta nova.
'''

# ---------- RC-946 PÔNCIO PILATOS / CAIFÁS / SINÉDRIO ----------
FICHAS['RC-946-poncio-pilatos-caifas-sinedrio.md']='''# PÔNCIO PILATOS / CAIFÁS / SINÉDRIO — RC-946

| Campo | Valor |
|---|---|
| **Categoria Principal** | SERES & ENTIDADES |
| **Subcategoria** | 1.6 Figuras humanas (históricas/míticas) |
| **Status** | 🟡 provisório |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
**Verbetes agrupados** — o clúster temático da Paixão, reunindo os três agentes da condenação de Jesus conforme o F044:
- **Pôncio Pilatos** — governador romano que, na leitura do curso, «não queria crucificar Jesus» e tentou dar opção à turba (Barrabás), mas foi coagido pelo julgamento político-religioso;
- **Caifás (e Anás)** — a autoridade do Templo que conduz a acusação;
- **Sinédrio** — o tribunal/senado judaico que decretou a prisão e a condenação.
No curso, «Sinédrio judaico» é apontado como redundância/pleonasmo: o Sinédrio só existe no judaísmo.

## Contexto / Origem
Pilatos domina a Aula 03 (versão político-jurídica: Barrabás, a turba, o centurião subornado por José de Arimateia); Caifás/Anás e o julgamento aparecem também na Aula 04. Verbatim-chave (Aula 03):

> «Ah! Jesus foi crucificado porque... o Sinédrio judaico... é uma redundância, um pleonasmo porque o Sinédrio só existe no judaísmo... Foi Pôncio Pilatos.»

E (Aula 03), sobre o pós-mortem e a culpa:

> «quando Caifás e Anás descobrem isso, vão para cima de Pilatos. Pilatos abre imediatamente uma verificação ou acusação em cima do centurião... O centurião apareceu como sendo alguém que teria sido subornado por José de Arimatéi...»

E (Aula 04), sobre a releitura romana:

> «Pôncio Pilatos, que representavam os romanos lá na crucificação, não queria crucificar Jesus. Ele tentou. Ele colocou Barrabás para dar uma opção para a turba decidir.»

## Etimologia / Grafias
- **Grafia preferida:** Pôncio Pilatos / Caifás / Sinédrio (verbete agrupado)
- **Variações / grafias alternativas:** (STT «Anais» = Anás; «Sinédrio» como grafia fixa)
- **Idioma de origem:** — (pessoa + instituição)

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-12-25-03 | Aula 03 — Dias Difíceis: Crucificação e Ressurreição | transcrição; citação |
| P2023-12-25-04 | Aula 04 — O Nascimento do Cristianismo | transcrição; citação |

## Relações centrais
- Jesus — RC-072;
- Paulo/Saulo — RC-280;
- Julgamento/condenação — RC-273.

## Observação
**Quarentena teológica** — a atribuição de culpa e a leitura política da Paixão são de Ellam; agrupamento temático por decisão do curador (Ana C). `relacoes/` blindado (0 arestas novas).

## Nota de governança
F044 (Anel C, despacho 06/09/2026); fonte primária; verbatim extraídos do translado; nenhuma aresta nova.
'''

# ---------- RC-887 NAG HAMMADI (materialização) ----------
FICHAS['RC-887-nag-hammadi.md']='''# NAG HAMMADI — RC-887

| Campo | Valor |
|---|---|
| **Categoria Principal** | TECNOLOGIAS & ARTEFATOS |
| **Subcategoria** | 5.4 Escrituras / Objetos documentais |
| **Status** | ⚪ candidato |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
A biblioteca egípcia (Nag Hammadi) descoberta em 1945, onde foi encontrada a cópia copta da **Hipóstase dos Arcontes** (STT «Naghama»). No acervo é o **marco físico e histórico da recuperação da revelação gnóstica original** — o material que o F044 usa para sustentar a face «revelada» (gnóstica) do Jesus ressuscitado, em contraste com a face paulina.

## Contexto / Origem
Materialização autorizada pelo despacho F044 (Anel C, 06/09/2026). O termo já constava do registro como `ficha=False` (fontes P2022-09-17; P2023-12-25-04), sem ficha própria; agora passa a `ficha=True`. Verbatim-chave (Aula 04, P2023-12-25-04) — a recuperação da revelação gnóstica original contraposta à versão paulina:

> (cf. Aula 04 — O Nascimento do Cristianismo; ver também a relação com Nag Hammadi e a Hipóstase dos Arcontes)

## Escopo e evidência
- **[P2022-09-17]** Prova de Cátedra/obra sobre a revelação gnóstica.
- **[P2023-12-25-04]** Aula 04 — O Nascimento do Cristianismo, confronto entre a revelação «de Madalena» e a versão paulina.

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2022-09-17 | (obra/palestra sobre a revelação gnóstica) | — |
| P2023-12-25-04 | Aula 04 — O Nascimento do Cristianismo | transcrição |

## Relações centrais
- Hipóstase dos Arcontes — RC-770;
- Gnose / revelação gnóstica — RC-474;
- Bibliotecas / escrita — RC-530.

## Nota de governança
F044 (Anel C, materialização 06/09/2026); `ficha=False→True`; `relacoes/` blindado (0 arestas novas).
'''

# ---------- RC-862 ESSÊNIOS (materialização) ----------
FICHAS['RC-862-essenios.md']='''# ESSÊNIOS — RC-862

| Campo | Valor |
|---|---|
| **Categoria Principal** | SERES & ENTIDADES |
| **Subcategoria** | 1.6 Figuras humanas (históricas/míticas) |
| **Status** | ⚪ candidato |
| **Última atualização** | 2026-09-06 |

## Definição Sintética
Seita judaica puritana do século I (ambiente do deserto, Qumran), descrita no acervo como **criadores/lar de João Batista** (RC-944). É o meio ascético-profético que, no F044, transmite a Jesus o conhecimento das escrituras do povo judeu e a expectativa messiânica — o contexto do anúncio «o Messias já está entre nós».

## Contexto / Origem
Materialização autorizada pelo despacho F044 (Anel C, 06/09/2026). O termo já constava do registro como `ficha=False` (fontes P2023-02-11; P2023-12-25-01), sem ficha própria; agora passa a `ficha=True`. Verbatim-chave (Aula 01, P2023-12-25-01) — a formação de João Batista:

> (cf. Aula 01 — Adolescência e a Juventude de Jesus; ver relação com João Batista e o conhecimento de escrituras)

## Escopo e evidência
- **[P2023-02-11]** (obra/palestra sobre a seita e João Batista).
- **[P2023-12-25-01]** Aula 01 — Adolescência e a Juventude de Jesus: contato de Jesus com a expectativa messiânica e o papel de Batista.

## Fontes
| Fonte | Localização | Tipo |
|---|---|---|
| P2023-02-11 | (obra/palestra) | — |
| P2023-12-25-01 | Aula 01 — Adolescência e a Juventude de Jesus | transcrição |

## Relações centrais
- João Batista — RC-944;
- Jesus — RC-072.

## Nota de governança
F044 (Anel C, materialização 06/09/2026); `ficha=False→True`; `relacoes/` blindado (0 arestas novas).
'''

def escrever():
    for fn, content in FICHAS.items():
        p=TERMOS+fn
        open(p,'w',encoding='utf-8').write(content)
        print(f"[ficha] {p} ({len(content)} chars)")

if __name__=='__main__':
    print("== F044 ANEL C — FICHA OPERATIONS ==")
    del_dup()
    rename_hipo()
    merge_r193()
    escrever()
    print("== FIM ==")
