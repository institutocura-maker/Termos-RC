# Diagnóstico do processo — Base Terminológica RC

**Estado da esteira em 2026-08-29, ao fechar o ciclo `P2023-12-03` · AGENTE 14 · documento de radiografia, não de reforma.**

> **O que este arquivo é:** a medição detalhada do processo como ele está hoje — as etapas, o custo de cada uma, onde o esforço nasce, por que ele cresceu, o que o processo garante e o que ele **não** garante. Foi escrito para que qualquer mudança seja discutida contra números, não contra impressão de cansaço.
> **O que este arquivo não é:** não é proposta aprovada, não é mudança de rite, não é ordem de serviço. **Nada aqui foi executado.** Cada sugestão está escrita como opção com custo e risco declarados; a decisão é do Curador, e só dele.
> **Reprodutibilidade:** todas as grandezas vêm de `diagnostico/medir_processo.py`, que lê o repositório e grava `diagnostico/medicoes.json`. Rodar `python3 diagnostico/medir_processo.py` reconstitui os números. Nenhum valor foi digitado à mão — a regra que vale para aspas de fonte vale aqui para números.
> **Zero aspas de citação neste arquivo** (contagem de U+00AB: 0). Documento que não cita fonte não tem direito a aspa de fonte: rótulos, nomes de campo e de arquivo vão em `backticks` ou itálico. É a regra da casa aplicada contra o próprio autor do documento.

---

## 1. O corpo da coisa hoje

| grandeza | medida | de onde se lê |
|---|---|---|
| termos na malha | **777** | `python3 ferramentas/dados_termos.py` → `OK: 777 termos, 1856 relações — dados válidos.` |
| relações | **1.856** | idem |
| arquivos de ficha | **460** em `termos/*.md` | `medicoes.json → cadastro.fichas_arquivo` |
| fichas com `ficha=True` | **459** | cadastro |
| termos **sem** arquivo de ficha | **317** (40,8% do cadastro) | índice mestre × `termos/` |
| seções de ampliação nas fichas | **1.109**, de **55** ciclos | `grep -h '^## Ampliação —' termos/*.md` |
| ciclos engavetados | **71** em `apostilas/CONCLUIDAS/` | diretório |
| ciclos com despacho formal gravado | **5** (têm `DECISAO-DO-CURADOR.md`) | `medicoes.json → corpo.comparativo` |
| ciclos com relatório de ciclo | **47** | idem |
| apostilas | **4,52 MB** · mediana **41.757 B** · maior **220.017 B** | idem |
| brutos de fonte oral | **8,69 MB** · mediana ~**121 kB** | idem |
| docs de aparato (`analise/`) | **13,71 MB** = **3,03×** o produto | idem |
| pacotes de aplicação (`_ampliacoes*`) | **1,36 MB** em 54 arquivos | idem |
| Python já escrito para a esteira | **22.533 linhas** em 158 scripts | idem |
| obras físicas em `livros/CONCLUIDOS/` | **44** (catálogo de obras: 102) | diretório |
| TXT em `uploads_recepcao/` | **34** arquivos · 4,11 MB · **0** sem ciclo engavetado | `medicoes.json → cadastro` |

**Leitura da tabela.** Por palestra processada, a Arca consome hoje ~122 kB de bruto e entrega ~64 kB de apostila — depois de produzir **~193 kB de aparato de análise**. O aparato é **três vezes o produto**. Não é anomalia de um ciclo: é a forma que o rite atual tem.

---

## 2. A anatomia do rite, etapa por etapa

O rite de um ciclo tem **7 fases, 16 instrumentos encadeados e 5 portões**. As massas abaixo são do ciclo mais recente (`P2023-12-03`), que é o **pior caso medido**, não a média.

| # | fase | instrumento | o que produz | custo medido |
|---|---|---|---|---|
| 0 | **Ingresso** | `cp` + `cmp` + SHA-256 + `ficha_ingresso.md` | bruto imutável com hash selado | 531 linhas de metadados JSON |
| 1 | **Leitura integral** | `_gerar_textos_e_dossie`, `LEITURA-1`, `leitura-segmentada.txt` | cobertura provada por igualdade de texto, não por soma | 719 linhas de script · 8,9 kB de docs |
| 2 | **Camadas de leitura** | `_gerar_camadas`, `_gerar_camada3` | camada 0 (endereços) · 1 (tese) · 2 (padrões e dicionário STT) · 3 (movimentos e navalha) | 716 linhas · 65,7 kB de `.txt` |
| 3 | **Dossiê + matriz** | fase 3 dos geradores | **127 vínculos-proposta** e matriz de anterioridade sobre **366** códigos na mira | 59,7 kB + 56,1 kB |
| 4 | **Pacote → despacho** | `_gerar_ampliacoes` | `_ampliacoes_<sigla>.txt` com BLOCO 1..5: citações com endereço, retidos, divergências, cruzamentos | **654 linhas · 89,8 kB** |
| 4b | *(pausa)* | — | **devolutiva do Curador, gravada verbatim em `DECISAO-DO-CURADOR.md`** | — |
| 5a | **BLOCO A (Base)** | `_aplicar_ampliacoes --refazer`, `_vincular_fonte`, `_gerar_fichas_*` | FONTES na malha, `## Ampliação` nas fichas, materializações | 110 + 94 + 267 linhas |
| 5b | **BLOCO B (produto)** | `_gerar_apostila` | apostila de 684 linhas · 173,5 kB · 79 blocos · 25 notas · glossário A–D | **683 linhas** |
| 6 | **Portões** | `_verificar_verbatim`, `_portao_c`, `_portao_d`, `_cobertura_apostila`, `_aspas` | A verbatim · B aspas contra o bruto · C ficha a ficha · D contadores e travas · E cobertura e trânsito | 674 linhas · **5 portões** |
| 7 | **Documento e arquivo** | `ferramentas/build_apostila.py`, relatório, `git mv`, governança | DOCX (100,4 kB), `RELATORIO-DE-CICLO.md` (186 linhas), engavetamento, 3 arquivos de governança | ~40 kB de prosa nova |

**A cadeia de dependência.** 15 dos 16 scripts do ciclo leem artefato de etapa anterior (mediana de 4 a 5 leituras por script). Consequência mecânica: **mexer num elo a montante invalida tudo a jusante.** Neste ciclo isso aconteceu duas vezes por motivo banal — uma string `"Lemi\b"` que injetou byte de controle no `camada-2.txt` e um rodapé estático na matriz que dizia `0 escrita na Base` depois de aplicada — e cada vez foi preciso rodar de novo: camadas → pós-aplicação → apostila → DOCX → cobertura → verbatim → portões C e D.

**Onde o tempo vai.** Não na escrita da apostila. Vai em (i) ler o bruto inteiro com endereço, (ii) reconciliar a proposta com a Base que já existe, (iii) consertar instrumento, (iv) reexecutar a cadeia depois de (iii). Os itens (iii) e (iv) são 100% evitáveis; (i) e (ii) são o trabalho.

---

## 3. A curva do esforço — medida, não sentida

Recorte: os **5 ciclos com despacho formal** (a nova fase) contra os **66 ciclos** anteriores do mesmo acervo.

| grandeza (mediana por ciclo) | legado (66) | nova fase (5) | fator |
|---|---|---|---|
| scripts `.py` | 2 | **11** | **×5,5** |
| linhas de `.py` | 150 | **2.331** | **×15,5** |
| portões | 0 | **5** | — |
| pacote de aplicação | 14.456 B | **69.466 B** | **×4,8** |
| docs de aparato | 153 kB | **361 kB** | **×2,4** |
| apostila | 39.756 B | **173.540 B** | **×4,4** |
| bruto | 121.428 B | 119.175 B | ×1,0 |
| **apostila ÷ bruto** | **0,33** | **1,46** | **×4,4** |

**Três leituras que os números obrigam:**

1. **A fonte não mudou de tamanho; mudou o destino dado a ela.** Bruto igual, produto 4,4× maior. A razão 0,33 do legado diz a verdade incômoda: a apostila inteira do legado media um terço do bruto — *com aparato dentro* —, de modo que a fala transcrita era **bem menos de um terço**. A razão 1,46 de hoje significa que a apostila contém a fala inteira mais o aparato, com cobertura provada por igualdade de texto e meta explícita de **0 cortes**. Boa parte do esforço extra é **preço de uma promessa nova**, não inércia.
2. **O código de esteira é o item que explode.** ×15,5 contra ×4,4 do produto. Nos 5 ciclos da nova fase foram escritas **13.438 linhas de Python — 59,6% de todo o código que a Arca já viu, em 7% dos ciclos.** Este é o único número do diagnóstico que aponta com força para desperdício estrutural (§4.3).
3. **Não é exponencial no sentido matemático — e isso é boa notícia.** Por ciclo, o crescimento é ~linear em código reescrito e ~quadrático na reconciliação com a Base. A sensação de exponencial vem de compor os dois. Precisar importa para decidir: **linear reescrevível** se conserta com ferramenta, uma vez só; **quadrático** exige mudança de regra, não de script.

---

## 4. As quatro causas do custo — cada uma com remédio e risco

### 4.1 Causa estrutural: a superfície de reconciliação cresce quadrática

Distribuição de ciclos que tocam a mesma ficha (`medicoes.json → superficie`):

| ciclos na ficha | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 13 | 14 | 15 | 17 | 18 | 23 | 24 | 27 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fichas | 133 | 107 | 83 | 49 | 20 | 17 | 13 | 6 | 8 | 5 | 3 | 5 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |

- Média **2,41** ciclos por ficha; **3.746 pares** de ciclos a reconciliar dentro de fichas; pior caso **31 ciclos na mesma ficha**.
- A matriz de anterioridade deste ciclo mirou **366** códigos e aplicou em **126**; a diferença (240) é a **curadoria de contato**: código já resolvido por outro ciclo, citado sem arquivo, ou fora do escopo. Errei a régua **duas vezes antes** de usar a Mira certa — e só o arquivo relido depois diz o número certo.

**Por que dói:** cada ciclo novo precisa saber o que 55 ciclos já disseram sobre o mesmo termo. É o preço de a Base ser *viva* — e é o que impede erro de anterioridade, a qualidade mais difícil de falsificar que a Arca tem.

**Remédio (opção, não ordem):** transformar a superfície em **consulta mecânica**, não em leitura. Já existem `ferramentas/_auditoria_lacunas.py` e o índice mestre; falta um **`ferramentas/contato.py`**: dado um código, devolve em ~20 linhas as fichas existentes, os ciclos que o tocam, as datas-fonte e se o novo ciclo *antecipa, estreita ou contradiz*. Corta o tempo da etapa 3 sem cortar verificação alguma. **Custo:** um script de ~300 linhas, uma vez. **Risco:** baixo — leitura só, sem escrita.

### 4.2 Causa escolhida: transcrição integral e moldura no lugar de corte

Medido no último ciclo: 79 blocos, **cobertura 100,00%** (102.610/102.610), **0 bloqueios**, 25 notas editoriais, 4 molduras (D-1 a D-4) posicionadas em bloco exato, o quiasma da D-2 provado dentro de um só bloco, 13 quarentenas, **3 spans retidos**.

Custo: o auditor de cobertura virou um programa de 195 linhas; a moldura virou código no gerador; a trava do despacho virou **duas** implementações (gerador **e** portão com léxico próprio, porque portão que importa a regra do gerador é eco).

**Juízo crítico: é a parte que uma reforma de agilidade não deve tocar.** Foi ela que impediu, neste ciclo, dois erros irreversíveis: inventar o aforismo político que a devolutiva citava mas que **não existe** no bruto (0× `mediocri*`, 0× `cara dela`), e apartar as duas frases que o Curador mandou manter juntas. Trocar isso por velocidade não é reforma de processo: é troca de produto — e aí tem de ser o Curador a dizer que quer outro produto, com todas as letras.

### 4.3 Causa de desperdício: a máquina é reescrita a cada ciclo

Similaridade entre as cópias do mesmo script nos 5 ciclos com despacho (código normalizado, data substituída, comentários fora):

| família | cópias | igualdade 1º×2º | natureza |
|---|---|---|---|
| `_verificar_verbatim.py` (portão B) | 5 | **99%** | **máquina pura** — só muda a sigla |
| `_portao_c_fichas.py` | 5 | **97%** | máquina pura |
| `_aspas.py` | 3 | **89%** | máquina pura |
| `_aplicar_ampliacoes.py` | 5 | **85%** | máquina + 1 escolha de formato |
| `_portao_d_contadores.py` | 4 | **75%** | máquina + contadores do ciclo |
| `_vincular_fonte.py` | 5 | **48%** | máquina com meia dúzia de exceções por ciclo |
| `_cobertura_apostila.py` | 5 | **15%** | **arquitetura repetida, código novo** |
| `_gerar_apostila.py` | 5 | **12%** | idem |
| `_gerar_camadas.py` / `_gerar_dossie.py` | 2 | **4%** / **3%** | idem |
| `_gerar_ampliacoes.py` | 5 | **2%** | idem |

E dentro dos geradores, o peso do dado: **624 das 4.273 linhas** do ciclo são decisão curatorial escrita dentro do código (alvos, âncoras, notas, rótulos) — 15%. Os outros **85% são motor**. Como os geradores de ciclos consecutivos são 2–12% idênticos **apesar de a arquitetura ser a mesma**, o que se paga a cada ciclo não é só o motor: é o motor *disfarçado de conteúdo*, que não pode ser reusado sem ser relido e re-testado.

**Consequência direta, e V.Sa. já a sentiu: a taxa de defeito de instrumento.** Os 5 ciclos somam **2.385 linhas só de portões**, e o histórico de correções é constante: **11 retificações declaradas no relatório deste último ciclo** (cedilha no caça-âncoras, índice de meses da anterioridade, portão C que não lia aspas angulares, trânsito medindo a ficha inteira em vez da seção do ciclo, rótulo de `RC-071`, byte de controle que derrubou o DOCX, rodapé estático que mentia depois da aplicação, e mais quatro de menor porte). Cada uma força reexecução (§2) e gasta um ciclo de atenção que não produz conteúdo.

**Remédio (o de maior retorno mensurável): separar motor de configuração.**
- `ferramentas/` passa a ter `portoes.py` (A–E parametrizados por `--ciclo`), `cobertura.py`, `aplicar_ampliacoes.py`, `apostila_do_ciclo.py` e `contato.py` — tudo o que já se provou 75–99% invariante.
- O ciclo passa a ser **um pacote declarativo** (o `_ampliacoes_<sigla>.txt`, que já existe e já é a interface entre despacho e Base) **mais** um `_config_<sigla>.toml` pequeno: alvo de fatiamento, molduras, quarentenas, códigos `ficha=False`, vetos de trânsito.
- O portão lê o `toml` (regra) e o pacote (conteúdo), em vez de cada ciclo embutir os dois no próprio código.

**Custo:** extração estimada em ~1.500–2.000 linhas de engenharia, **uma vez**. **Economia projetada:** dos ~2.300–4.300 linhas de Python por ciclo sobram como trabalho real as ~230–620 linhas de decisão (faixa medida de `dados_em_codigo`). Ou seja: **o custo de instrumentação por ciclo voltaria de ×15,5 para perto de ×1 do legado**, sem tocar em cobertura, verbatim, tetos nem poderes. **Risco:** motor único **concentra** defeitos — um bug no motor contamina todos os ciclos futuros. Mitigação obrigatória: o motor só entra em uso depois de **re-rodar os 5 ciclos com despacho contra ele e exigir resultado idêntico ao gravado** (é a mesma técnica desta sessão: mexe-se no gerador, nunca no produto; rollback por `git checkout <commit> -- termos/`).

### 4.4 Causa de overhead: o imposto de governança e de re-leitura

| item | tamanho | crescimento |
|---|---|---|
| `CONTINUIDADE.md` | **337.128 B** · 463 blocos · ~728 B por bloco | +1 bloco denso por fase de ciclo |
| `PROMPT-PROXIMA-SESSAO.md` | **52.856 B** | +1 atualização por sessão (a 10ª foi escrita na última) |
| `INDICE-PALESTRAS.md` (raiz) | **34.794 B** · 38 linhas, uma por ciclo | a linha do ciclo atual passou de ~2,6 kB para ~3,1 kB |
| `apostilas/INDICE-PALESTRAS.md` | **91.411 B** | congelado (intocável) |
| GUIA-MESTRE + convenções | **34.052 B** | estável |
| **leitura obrigatória antes de tocar em qualquer coisa** | **550.241 B** | cresce com o acervo |

**Leitura crítica:** ~550 kB de documentos de governo são lidos a cada abertura de sessão antes do trabalho produtivo. Não é desperdício puro — é o preço de um processo sem memória própria; mas é um preço que sobe a cada ciclo e cuja subida não compra nada. O ponto que dói é o `CONTINUIDADE.md`: diário é ótimo como arquivo e ruim como pré-requisito. Duas opções baratas, sem perda histórica: (a) o cabeçalho vir **o estado** (as 4 primeiras linhas já somam 4,9 kB e respondem ao que a sessão precisa) e o corpo passar a ser lido **por endereço**, não por dever; (b) mover o corpo dos ciclos fechados para `diario/` fatiado, deixando no mestre só o que governa. **Custo:** meia sessão de organização. **Risco:** baixo, se o `git mv` preservar histórico e os índices apontarem para o novo endereço.

---

## 5. O que o processo garante hoje — e que uma reforma tende a quebrar

Reforma de processo costuma cortar o que é caro, e nem sempre o caro é dispensável. Em ordem de valor, com a evidência do último ciclo:

| garantia | como se prova | se for cortada |
|---|---|---|
| **Fonte imutável** | `original.txt` com o mesmo SHA-256 do ingresso (`41b3f914befb…4e1021`); movimento só por `git mv` como renomeio puro | perde-se a capacidade de reprocessar e de acusar o STT em vez do curador |
| **Cobertura por igualdade de texto** | 102.610/102.610 = **100,00%**, 0 bloqueios, medido por auditor estrutural | volta-se ao 0,33: resumir é cortar sem dizer |
| **Verbatim endereçado** | portões A e B sobre **473 fragmentos**, 0 divergências; nenhuma aspa digitada à mão, nem em nota editorial | a citação ganha vida própria — o pior defeito possível numa base terminológica |
| **Travas do despacho viram código** | D-1 a D-4, D-8, D-10, D-12, D-13 implementadas; os **3 spans retidos** provam que mordem | vira promessa de boa intenção, e boa intenção falha em silêncio |
| **Veto de trânsito** | 0 vazamentos em 72.764 chars de 107 seções; nada de gênero ou política entra em ficha que nomeia gente | dano reputacional e ontológico — o único item da lista sem volta |
| **Contadores inviolados** | 777 termos · 1.856 relações · 102 obras preservados; `RC-778` intacto; `RELACOES` intocada | perde-se a arqueologia do acervo |
| **Divergência sem harmonização** | 7 divergências seladas com data; prazo 2049-2052 **vencido e declarado, não corrigido** | a Base passa a concordar consigo mesma por edição — falsidade |
| **Silêncio não é opção** | 11 retificações no relatório; **6 ordens do despacho sem destino nomeadas**, declaradas | dívida vira invisível |

**Ponto cego que a medição revelou e que nenhum portão cobre:** nada desse aparato toca o **estado verificativo do termo**. No índice mestre, dos 777 termos, **0 carregam 🟢 verificado** (492 🟡 provisório · 285 ⚪ candidato). A esteira certifica o *texto de cada ciclo* com cinco portões e nunca promove o *termo* na coluna `Status`. Na minha leitura, é **a maior ineficiência real do processo** — não de custo, de **valor**: a verificação foi feita e não está registrada onde o leitor procura.

---

## 6. Dívidas e pendências abertas (estado exato, sem eufemismo)

| # | pendência | natureza | o que falta |
|---|---|---|---|
| 1 | **317 termos sem arquivo de ficha** (40,8% do cadastro) | estoque | materialização em lote, ou decisão de que ⚪ nunca terá ficha |
| 2 | **0 termos com selo 🟢** | registro | derivar o selo dos ciclos fechados (§7.2.3) |
| 3 | **6 ordens do despacho `P2023-12-03` nomeando fichas que não existem**: `RC-093`, `RC-189`, `RC-280`, `RC-035`, `RC-375`, `RC-344` | descompasso despacho × cadastro | uma ordem nova; o materializador é genérico (`_gerar_fichas_RC018_RC040_P2023-12-03.py` é copiado com dois nomes) |
| 4 | **19 códigos `ficha=False` citados no pacote e sem arquivo** + termos-observação fora da malha (Rockmar/Rockma/Rockban, teia de Orlo, horlogus/orlog, Job Misso, Enócrita, Z Geist, Patangel, Satanail, 4 grafas de Alto Longron, 5 de Túatha, comaranda, niroda, cita, fenvan, trouidaram) | fila de ontologia | decisão do Curador — nunca do aplicador |
| 5 | **Reauditoria dos ciclos anteriores pelo defeito do `ç`** no caça-âncoras herdado | higiene de instrumento | ordem de executar; o mapa `_EXTRA` corrigido vale só para ciclos novos |
| 6 | **Micro-ciclo das 2 emendas silenciosas** em `apostilas/CONCLUIDAS/2023-12-02_thot_enigmatico_hermes_trimegisto/` | pendência não despachada | despacho (foi levantada e devolvida sem ordem) |
| 7 | **`RC-017` sem arquivo** | resíduo conhecido | idem item 4 |
| 8 | **Fila de obras**: 102 no catálogo, 44 físicas em `livros/CONCLUIDOS/` | paralelo | fora do escopo deste rite |
| 9 | **Radar datado** de 4 promessas da fonte (D-11) e o prazo 2049-2052 vencido | vigília | só o relatório; nada a executar |

As linhas 3 a 6 provam que a esteira **não improvisa**: parou na fronteira da ordem. Qualquer reforma precisa preservar esse comportamento — custa menos um despacho de uma linha do que uma materialização não autorizada a desfazer.

---

## 7. Análise crítica do pedido — e o que eu sugiro

V.Sa. colocou três premissas. Não são igualmente verdadeiras, e a reforma fica muito mais fácil quando elas são separadas.

**Premissa 1 — *a Base e as Relações estão muito estáveis*.** Correta, e mais do que foi formulado: **1.856 relações intocadas em cinco ciclos consecutivos**, com D-6 e D-8 negando expressamente a criação de relação de fundamento. O cadastro é hoje *consumido*, não *escrito*, pela esteira de palestras. Consequência: a parte mais cara do rite (vínculo, anterioridade, contato com o passado) defende um perímetro que **não se move mais por si**. É daí que sai a maior economia legítima da reforma — não de cortar verificação.

**Premissa 2 — *o esforço de checagem aumenta exponencialmente*.** Parcialmente correta, e a correção importa para a decisão:
- o que cresce **quadrático** é a superfície de reconciliação (§4.1) — real e medido (3.746 pares, pior caso 31 ciclos/ficha), e **só** no eixo *o que os ciclos anteriores já disseram*;
- o que cresce **linear com coeficiente brutal** é a reescrita da máquina (§4.3): ×15,5 por ciclo, com 60% de todo o Python da Arca gasto em 7% dos ciclos. **Isto não é custo de checagem: é custo de ferramenta jogada fora a cada ciclo.** Não é exponencial — e é o item mais barato de resolver;
- o esforço de checagem *estrita* (portões) é o **menor** dos três: 212–674 linhas por ciclo, quase todo ele idêntico entre ciclos. Reduzir portões economiza pouco e custa caro.

**Premissa 3 — *o volume a catalogar é grande*.** Verdadeira, mas **o repositório não a enxerga**: `uploads_recepcao/` tem 34 TXTs e todos já têm ciclo engavetado. O backlog está com V.Sa., fora da Arca — e essa é exatamente a informação que falta para dimensionar a reforma (primeira pergunta do §8). Sem saber se restam 20 ou 200 palestras, a escolha certa muda: para dezenas, vale reformar o motor; para centenas, vale **criar uma classe de ciclo que hoje não existe** (§7.3, modelo C).

### 7.1 Onde eu discordo

**Da direção “objetivo”, se significar encurtar o produto.** O ativo da Arca não é a elegância da apostila: é um texto-fonte tratado byte a byte com honestidade, em que nada foi sumariado por cansaço. O legado com ratio 0,33 é um acervo de apostilas que largaram fora boa parte da fala do autor — e o custo disso já apareceu: as **re-curadorias** de `P2021-12-04`, `P2022-12-17` e `P2020-04-25` foram exatamente ciclos abertos para pagar essa conta anos depois. Agilidade tem de vir do **motor e do aparato**, nunca do produto.

**De mexer no rite de dois blocos com devolutiva.** O §4.3 localiza o desperdício fora dessa etapa, e é ela que impede o erro irreversível. É o único ponto em que eu diria “não mexa, mesmo que custe” — inclusive porque a devolutiva é onde V.Sa. é, de longe, o componente mais rápido da esteira: o despacho atual resolveu 14 itens estruturais numa passada, e três deles (D-1, D-10, D-13) impediram escrita errada em 100+ fichas.

### 7.2 Sugestões, em ordem de retorno/risco

1. **Congelar rite e produto; reformar só o instrumento.** Meta declarada: linhas de Python por ciclo de ~2.300–4.300 para **< 700**, com todos os portões intactos e cobertura ainda em 100,00%. Se a reforma não baixar esse número, ela não pegou o problema.
2. **Extrair o motor para `ferramentas/`** (§4.3), com pacote + `toml` como **única escrita por ciclo**. Pré-requisito de aceite: reproduzir os 5 ciclos com despacho bit a bit rodando pelo motor novo. É verificável hoje e impede reforma que quebra.
3. **Promover o selo 🟢 por derivação, com despacho.** Proposta: o termo sobe para *verificado por fonte oral* quando (i) tem arquivo, (ii) tem ≥1 seção de ampliação de ciclo engavetado **com portões verdes** e (iii) o ciclo tem relatório. 100% mecânico, não nomeia, não relaciona, não reinterpreta. Escopo imediato medido: **336 seções** dos 5 ciclos com despacho, sobre **166 fichas únicas** — a verificação dessas fichas já foi feita; só não está registrada onde o leitor procura. Custo: ~80 linhas em `build_indice.py`.
4. **Criar o “ciclo leve” como classe oficial, com porta fechada por V.Sa.** Descrição honesta do que ele **não** faz: não produz apostila de transcrição integral. O que ele produz: ingresso com hash, leitura integral **com cobertura provada** (o que dá o direito de dizer que não cortou) e um relatório de **materialidade** de uma página — termos novos, termos tocados, divergências, trechos que exigiriam moldura. A decisão vai para o despacho, que é o lugar onde V.Sa. já decide mais rápido que qualquer máquina. **Inviolável mesmo no ciclo leve:** SHA do bruto, verbatim com endereço, veto de trânsito, tetos, dois commits, devolutiva. **Abdica-se de:** dossiê, camadas 1–3, matriz de anterioridade, glossário. Estimativa: ~25% do custo atual por palestra com ~90% da informação que o despacho usa.
5. **Reconciliação virar tabela gerada uma vez por safra.** `analise/CONTATO-GERAL-<data>.md` com os 3.746 pares e as colisões de anterioridade; o ciclo lê só as linhas dos seus códigos. Transforma o quadrático (§4.1) em O(1) por ciclo sem mudar regra nenhuma.
6. **Pôr o `RELATORIO-DE-CICLO.md` para trabalhar fora do ciclo.** É hoje o arquivo mais denso em decisão e o menos reutilizado. Dois blocos fixos: `PRÓXIMO CICLO` (as ordens que faltaram — foi assim que as linhas 3 a 6 do §6 ficaram visíveis) e `PARA LER ANTES` (termos-observação ainda fora da malha). Custo zero.
7. **Regra anti-retificação: defeito de instrumento só morre com teste.** As 11 retificações deste ciclo teriam morrido no nascimento com ~6 linhas de teste por portão (âncora que não existe no bruto, byte de controle, rodapé estático, portão que não lê aspas angulares). Sugestão: `diagnostico/teste_portoes.py` — um bruto falso de ~40 linhas com **5 anomalias canônicas plantadas** — rodado antes de qualquer ciclo; se um portão não acusar as cinco, o ciclo não abre. **É isto que separa “mais ágil” de “mais frágil”.**
8. **Governança em duas velocidades** (§4.4): cabeçalho = estado, corpo = arquivo; linha curta no índice e o detalhe (hoje 3,1 kB na linha 38) morando no ciclo, onde já existe.
9. **Decidir §8.1 antes de desenhar qualquer coisa.** Sem o tamanho do backlog e sem o critério de materialidade, a reforma seria desenhada para um ciclo médio que não existe: nos 71 ciclos, brutos de **26 kB a 183 kB**, pacotes de **6,9 kB a 89,8 kB**, apostilas de **33 kB a 220 kB**.

### 7.3 Três modelos candidatos, para escolher qual merece protótipo

| | **A. Motor único** (recomendado) | **B. Ciclo em dois andares** | **C. Triagem em lote** |
|---|---|---|---|
| mexe em | instrumento (`ferramentas/`) | rite (porta de entrada nova) | rite (fase 0 nova) |
| economiza por ciclo | ~70% do código · **0% da verificação** | 45–55% nos ciclos de baixa materialidade | ~90% nos ciclos que não merecem rite |
| risco | defeito concentrado no motor | ciclo leve virar default por inércia | falso negativo: palestra subestimada |
| mitigação | teste de paridade nos 5 ciclos com despacho | **só o Curador** baixa um ciclo de andar | materialidade revisável por V.Sa.; fila leve→cheio custa zero (o pacote é o mesmo) |
| preserva | tudo | tudo menos aparato opcional | o produto integral nos que entrarem no rite |
| custo de implantar | 1 sessão longa de extração + testes | meia sessão de regra + 1 script | 1 script de lote + 1 página de critério |
| o que **não** muda | cobertura 100%, verbatim, travas, tetos, 2 commits, devolutiva | idem | idem para os admitidos no rite |

Minha recomendação, se me é permitido: **A + G agora, B como segundo passo** — motor único e o `teste_portoes` primeiro; o ciclo leve só depois que V.Sa. tiver visto dois ou três relatórios de materialidade e puder dizer o que os separa. Começar por B é a tentação natural de quem está cansado, e é onde eu teria mais medo de errar o corte.

---

## 8. O que precisa de despacho antes de qualquer coisa

1. **Tamanho e textura do backlog:** quantas palestras restam, com que tamanho típico de bruto, quantas têm conteúdo que exija moldura (política, gênero, nomes de pessoas/grupos), quantas são Q&A ou fala corrida.
2. **Hierarquia declarada:** entre *cobertura integral da fonte* e *custo por ciclo*, a primeira continua intocável? (Recomendação: sim — e a economia vem dos itens 1, 2, 5 e 7 do §7.2.)
3. **O selo 🟢:** derivar como proposto, criar rótulo novo (p. ex. *verificado por fonte oral*, diferente de 🟢 a seco), ou deixar a coluna como está?
4. **Materialidade:** V.Sa. quer critério objetivo para o ciclo leve (por exemplo: 0 termos novos e 0 divergências ⇒ leve; qualquer moldura necessária ⇒ cheio), ou prefere continuar nomeando palestra a palestra?
5. **As 6 ordens órfãs** do despacho `P2023-12-03`: materializar, manter declaradas, ou reverter a decisão de conteúdo?
6. **Reauditoria do `ç`:** roda nos ciclos anteriores ou fica como defeito conhecido e documentado?
7. **Fronteira de autoridade na reforma:** posso propor e escrever scripts/motor em `ferramentas/` sem despacho, ou o instrumento só entra depois de aprovado? (Muda meu comportamento a partir da próxima sessão; é a única pergunta daqui que me afeta diretamente.)

---

## 9. Como saber se a reforma funcionou — medidores que já existem

Propor mudança sem dizer como se mede o sucesso é como propor corte sem dizer o que fica protegido. Os indicadores abaixo já são produzidos por `diagnostico/medir_processo.py` e podem ser lidos a cada fechamento de ciclo:

| indicador | hoje (mediana nova fase) | meta | campo no JSON |
|---|---|---|---|
| linhas de `.py` por ciclo | 2.331 | **< 700** | `corpo.comparativo.nova_fase.linhas_py` |
| linhas de decisão (dado curatorial) | 231–624 | manter — é o trabalho real | `linhas_dado` |
| similaridade entre versões do mesmo portão | 75–99% já; 12–15% nos geradores | **tudo > 95%** | `motor.familias` |
| retificações de instrumento por ciclo | 5 a 11 declaradas | **0 novas** (só defeito de conteúdo) | §5 dos relatórios |
| ciclos por ficha (superfície) | média 2,41 · máx 31 | crescer sem custo novo, com `contato.py` cobrindo | `superficie` |
| cobertura de apostila | 100,00% | **100,00% inegociável** | portão E |
| divergências verbatim | 0 | 0 | portões A e B |
| termos com 🟢 | 0 / 777 | subir sem escrever ontologia nova | `cadastro.status` |
| leitura de início de sessão | 550.241 B | < 250 kB | `governanca.leitura_obrigatoria_bytes` |
| ordens de despacho sem destino | 6 | 0 (materializar ou reverter) | §5 do despacho |

Se ao fim de um ciclo piloto com o processo reformado a linha **cobertura** ou a linha **divergências verbatim** tiver piorado, a reforma falhou **independentemente** das linhas economizadas. Sugiro gravar essa frase como condição de aceite.

---

## 10. Parecer em uma página

1. **A pausa é a decisão correta para este dia.** Cinco ciclos seguidos com despacho é um laboratório excelente e uma fadiga igualmente excelente para decidir reforma. A esteira está fechada no verde, a Base está limpa, nada se perde enquanto V.Sa. pensa: o acervo não é volátil e ciclo não vence.
2. **O diagnóstico confirma o sintoma e corrige o nome dele.** Não é que a checagem ficou cara: é que a *ferramenta de checagem* está sendo comprada de novo a cada ciclo (×15,5) e que a *reconciliação com o passado* cresce de verdade (quadrática). A primeira se resolve com uma sessão de engenharia e custo de qualidade zero; a segunda, com um índice, não com regra mais frouxa.
3. **Onde mora a agilidade legítima:** motor único, reconciliação virando consulta, governança em duas velocidades e uma classe nova de ciclo para palestra de baixa materialidade. Somando os quatro, minha estimativa honesta pelos números medidos é **40% a 60% de redução de custo por ciclo com perda zero de garantia** — não 90%, que só aparece quando se corta produto ou portão.
4. **Onde mora o perigo:** a mesma reforma que economiza 50% pode devolver a esteira ao estado do legado (ratio 0,33), e essa perda não aparece na planilha do dia em que se decide — aparece dois anos depois, quando alguém precisa da frase que alguém resumiu. Por isso eu pediria que a primeira linha do rite novo, seja qual for o modelo, fosse uma frase de inviolabilidade: cobertura 100% provada por igualdade de texto, verbatim com endereço, trava com dente, teto, dois commits. O resto é negociável — camadas, tamanho de glossário, se o DOCX sai no mesmo commit.
5. **Um ganho gratuito ainda não colhido:** 336 seções de 166 fichas passaram por cinco portões e a coluna `Status` do índice mestre não registra nada; 🟢 está em **0/777**. Converter isso em selo derivado (§7.2.3) é provavelmente o melhor custo/benefício do acervo hoje — o único item da lista que **aumenta** o valor da Base sem gastar um minuto a mais por ciclo.

---

## 11. O desfecho, na mesma data: despacho, motor, e o ciclo zero medido

O despacho veio no mesmo dia e autorizou a reforma nos termos do §10, com quatro atos (teto suspenso com cadência · portão de aprovação da pérola · livro-razão de âncoras obrigatório · migração só das 6 ordens órfãs) e a reabertura de `RELACOES`. O registro normativo vigente está em `DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md`; o instrumento em `ferramentas/motor.py`; a prova em `ciclos/P2023-12-03/RELATORIO-CICLO-LEVE.md`.

**As três premissas que este documento pôs à prova, agora com número:** (1) *escrever é o gargalo, não ler* — confirmado com folga: o ciclo zero escreveu **140.346 B** contra os **1.133.595 B** do mesmo ciclo no rite pesado, **8,1× menos**, e o ganho cresce a cada ciclo porque o instrumento não é mais reescrito (0 linhas de `.py` por ciclo contra os 13 scripts de `P2023-12-03`); (2) *o portão de verbatim é a única defesa que sobra quando a apostila sai* — confirmado em ambos os sentidos: o motor achou exatamente as 147 citações e, cobrando a mesma régua do pacote, descobriu **uma má-citação real no material engavetado** («coragem nem saco» contra o bruto `nem coragem, nem saco de fazer`) e **uma aspa de glosa que fingia citação** (`RC-189`) — as duas emendadas com carimbo, sem tocar o bruto; (3) *o essencial a preservar cabe em quatro portões* — confirmado, mas com ressalva medida: os portões precisam medir **delta** contra o commit-base, porque o portão D pesado, que fixa estado absoluto, hoje marca `466 ≠ 460` e `465 ≠ 459` em todo ciclo posterior. Um instrumento que apodrece a cada uso vira ruído que o Curador paga.

**O que a reforma custou, declarado:** catorze consertos no instrumento durante o ciclo zero (parser de bloco, fronteira de seção, caminhos não-ASCII do `git`, contagem de `RELACOES` por regex, dois estilos de aspa no cadastro, idempotência da virada, aspa de glosa, motivo de recusa, spans × códigos) — cada um produzindo número plausível e errado se ficasse quieto. O selftest com as cinco anomalias plantadas (âncora inexistente, âncora ambígua, byte de controle de DOCX, paráfrase vestida de citação, cedilha na normalização) ficou em **5/5** em todas as passadas; ele é a razão de o motor poder ser escrito de uma vez e confiado depois.

---

### Apêndice A — arquivos deste diagnóstico

| arquivo | o que é |
|---|---|
| `diagnostico/medir_processo.py` | o medidor (309 linhas; leitura só, escreve apenas no próprio JSON) |
| `diagnostico/medicoes.json` | todas as grandezas acima em forma máquina, geradas na execução de 2026-08-29 |

### Apêndice B — nota de integridade da sessão

Entre o fechamento do BLOCO B e a escrita deste documento o sandbox **reverteu o clone** (o `HEAD` voltou a `8eef2d9`, o ponto de ramificação, com o reflog mostrando `clone` + `checkout` novo). Os três commits do ciclo estavam salvos na branch remota e foram recuperados com `git fetch` + `git reset --hard FETCH_HEAD`; a branch está de novo em `f0baedc` (BLOCO B) com `932539a` (BLOCO A) e `3d3b8a0` (Etapa 1) por baixo. Depois da recuperação, as verificações reexecutaram verdes: `OK: 777 termos, 1856 relações — dados válidos.`, os quatro portões do ciclo sem divergência, e `original.txt` com o SHA do ingresso. **Nenhum produto foi perdido; os dois arquivos deste diagnóstico foram reescritos** porque o `reset` levou o que ainda estava no índice.

*Escrito por AGENTE 14 em 2026-08-29, ao fechar o ciclo `P2023-12-03`, sob a premissa de que nenhuma linha deste documento autoriza alteração de processo. Alteração de processo sem despacho não é agilidade: é iniciativa própria — e a casa tem nome para isso.* **Fecho do mesmo dia:** a premissa foi honrada — o despacho chegou antes de qualquer linha do motor ser escrita, a reforma foi implementada nos termos dele, e o ciclo zero fechou verde (§11).
