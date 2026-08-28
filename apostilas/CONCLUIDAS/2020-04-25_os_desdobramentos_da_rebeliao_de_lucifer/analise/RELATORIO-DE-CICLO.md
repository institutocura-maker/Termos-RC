# RELATÓRIO DE CICLO — P2020-04-25 *Os Desdobramentos da Rebelião de Lúcifer*

**Tema aberto pelo Curador:** **Yel Luzbel ou Lúcifer**, em 28/08/2026 · **bruto recebido** por upload na branch
(`3e642e1`) · **etapa 1** (leitura + dossiê) fechada em `82a9107` · **devolutiva D-1…D-14 registrada verbatim** ·
**BLOCO A** em `5cc6b29` · **BLOCO B** neste commit. Ciclo conduzido pelo AGENTE 13, **na mesma sessão de trabalho**
em que o arquivo chegou — o menor tempo de curadoria da Arca até aqui.

---

## 1. O percurso

| etapa | o que foi feito | prova |
|---|---|---|
| custódia | o TXT **existia no remoto e não no disco** (workspace re-materializado de clone anterior). Detectado por `git diff FETCH_HEAD HEAD` e recuperado com `git checkout FETCH_HEAD -- <arquivo>`; o commit do agente foi **refeito sobre o topo remoto** para não apagar o upload | nenhum `force-push`; o commit do Curador segue na história |
| ingresso | `cp` byte a byte → `original.txt`; `cmp` mudo; SHA-256 `1e8091e1…a7b3a` idêntico nos dois lados; CRLF e as 14 linhas preservados | `ficha_ingresso.md`; `git diff HEAD -- original.txt` = **vazio** ao fechar |
| leitura | **integral**: 8 chunks `⟦Uxxxx⟧` (~16.000 c cada) + `leitura-segmentada.txt`; `camada-0` endereça **43 seções de U0006** por offset medido + as 4 falas de Q&A | a megalinha U0006 tem 95.268 c = **82,7% da fala** |
| camadas | `camada-1` (a tese), `camada-2` (dicionário medido), `camada-3` (M1…M13, matriz de anterioridade, navalha, radar) | 12 fichas auditas uma a uma contra o cadastro |
| dossiê | `DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md` **gerado por script** (O-1…O-8, D-1…D-14, 42 vínculos-proposta, 89 âncoras resolvidas) | `_gerar_dossie_P2020-04-25.py` |
| devolutiva | 14 respostas do Curador, registradas verbatim antes de qualquer toque na Base | `DECISAO-DO-CURADOR.md` §1 |
| BLOCO A | pacote de ampliações → vínculo na malha → aplicação em fichas → materialização de RC-020 → portões C e D → builds | `5cc6b29` |
| BLOCO B | apostila gerada (54 blocos, 2 bloqueios declarativos, aparato espelhado, Apêndice do dicionário, glossário em 4 seções) + DOCX + este relatório + `git mv` para `CONCLUIDAS/` | `_cobertura_apostila.py`: **TRANSCRIÇÃO ÍNTEGRA, FIEL E BLOQUEIOS HONRADOS ✓** |

## 2. O que a palestra entregou (as joias do ciclo)

1. **O abismo recíproco.** A fonte cita Nietzsche para **negar sua literalidade** e depois o materializa em outro
   plano: não é Javé que olha para o abismo — **nós somos o abismo para ele**. É a inversão que a devolutiva
   registrou como reconstrução da ontologia documentada pela malha.
2. **A rebelião como infecção, não como insight.** A queda não foi olhar para o abismo: foi o **vírus**, «um
   coronavírus da época» (D-2 retida como analogia estrutural). O eu de Javé passa a ter definição **material** na
   Base: agregado de vírus que nunca chegou a ser célula, dependente de hospedagem sináptica — substrato
   indiferente, «de sílica ou de carbono».
3. **O processador Val e o campo mórfico.** Da resposta a uma pergunta da plateia (U0007→U0008) sai a equação que a
   malha não tinha em 2020: cada espécie biodêmica tem **um processador ligado ao cérebro de Sofia**; o ser humano
   **não tem** — tem o **campo mórfico da espécie**, que faz exatamente o que o processador faz, nas palavras dela. ⭐ Antecipa
   **3,5 anos** a fonte oral mais antiga de RC-381.
4. **A linha do tempo das chegadas, em versão oral datada:** 620 mil (única data que **bate** com B057) · 21 mil na
   nave · QG em 100/99 mil (vs 98 mil do livro) · o QG se teletransporta há 64 mil · cisão de 22 mil com 1.641 → 936
   → «900Q» · família Val em 736. Tudo **listado com endereço**, nenhum número harmonizado (D-10).
5. **O neologismo confessado ao vivo.** O nome da nova família não é citação de tradição: a fonte conta que
   **pediram que ela o inventasse** — `velo Shanai`/`Chanai`/`Shanai`, etimologia declarada (Chan + Vol + Yel). Entrou
   como **termo-observação**, sem código (D-5): o teto de 777 permanece.
6. **O fecho, que é o mais inédito de tudo:** a nova família será **bilatéria** e **não receberá espíritos humanos**
   — «retrogradação espiritual» —, e a decisão é apresentada como ato de **decência** em relação a Lemion
   [REVISAR: Len Mion]. Isso **contradiz** as fichas de exilados; a contradição foi registrada como divergência
   datada, não corrigida.

## 3. As quarentenas e os bloqueios (itens D-1 a D-4)

- **D-1 · bloqueio sumário — 16.523 caracteres.** O bloco de política nacional que **abre** a fala, na voz do
  próprio autor. Medição do recorte: começa no offset **949** de U0006 (logo depois de a fonte anunciar quanto vai
  gastar com aquilo) e termina no **17.472**, na frase imediatamente anterior ao pedido de desculpas. **Preservados
  por ordem expressa:** o gancho (U0003, o pedido de comentário) + o anúncio do desvio + a desculpa, dita duas vezes
  (fim de U0006 e fim de U0013). O teor cortado **não** é ecoado em lugar algum — nem na declaração de bloqueio, nem
  no dicionário STT, nem nas fichas (regra R-6 do ciclo anterior, aqui aplicada com o dobro de cuidado porque o
  bloco é 3× maior).
- **D-4 · bloqueio sumário — 237 caracteres.** A doença de 2009 e o pedido de silêncio, no offset **51.714** —
  **dentro** do corpo doutrinário, não contíguo à digressão. É a razão de esta apostila ter **dois** spans, e o
  portão D conferir os dois.
- **D-3 · manutenção com moldura.** Mulheres, homoafetivos e «cobaias» ficam na transcrição, com nota editorial, e
  **nenhuma** dessas aspas transitou para ficha: o gerador do pacote carrega `VETADAS` e **aborta** se alguma aparecer
  em citação. O portão D reconfere no material aplicado (0 vazamento).
- **D-2 · retenção seletiva.** A analogia viral está nas fichas; o juízo sobre conduta pública de saúde estava dentro
  do bloco bloqueado e não circula.
- **Cobertura resultante: 85,45%** (98.394 de 115.151 caracteres) — **a menor da Arca, e ela é decidida**: 14,6% do
  texto falado é um bloco que a própria fonte classifica como extratema.

## 4. A contabilidade da fase (medida por script, não lembrada)

| grandeza | antes | depois |
|---|---|---|
| termos no cadastro | 777 | **777** (teto curatorial; `RC-778` intocado) |
| relações na malha | 1.856 | **1.856** (0 arestas criadas) |
| obras (BIBLIO) | 102 | **102** (nenhum arquivo em `livros/` tocado) |
| arquivos de ficha em `termos/` | 456 | **457** (a única materialização: `RC-020-anjos-caidos.md`) |
| linhas `ficha=True` | 455 | **456** |
| fichas com seção `## Ampliação — P2020-04-25` | 0 | **45** |
| códigos com a sigla na malha | 0 | **56** (42 vínculos do dossiê, expandidos nos blocos compostos) |
| códigos sem arquivo, vínculo só na malha | — | **11** (RC-017/018/035/089/093/109/136/154/291/444/491) |
| pacote de ampliações | — | 56 códigos · 91 blocos · **132 citações** · 54.436 chars |
| apostila | — | 142.724 chars · 444 linhas · **54 blocos** · 2 bloqueios · DOCX 93.170 B |
| portões | — | **A 0 · B 0** (173 fragmentos longos; 1 aspa conferida no 2º corpus = a devolutiva) · **C 0** (99 citações em 45 fichas) · **D** paridade estrutural + travas **✓** |
| builds | — | `indice-mestre.md` 777 · `base-terminologica.xlsx` 7 abas (777 · 456 · 1.856 · 102) · `base-terminologica-leitura.docx` (457 fichas) |

**Anterioridades calculadas** (R-6: o gerador lê `dados_termos.py`, nunca a memória): **54** notas de antecipação
nos códigos do pacote — 21 ganham **13 meses**, 5 ganham 32, 5 ganham 11, 3 ganham **3,5 anos** (RC-381), 2 ganham
**14 dias** (RC-001), e há ganhos de 3,0 a 6,3 anos no bloco Mentalma/livros; **11** fichas passam a ter **a
primeira fonte oral da sua história**; e **2** fichas (RC-089, RC-154) ouvem o agente dizer **sem ganho de
anterioridade**, porque já tinham fala anterior — declarado na ficha, em vez de fingir primazia.

## 5. As retificações encontradas no portão de âncoras (a lição do ciclo)

Seis correções medidas entre a proposta e o aplicado, todas em `DECISAO-DO-CURADOR.md` §5. As três que importam para o
**método**, não só para este arquivo:

1. **R-2 — doze aspas digitadas de memória em prosa de aparato.** Nenhuma batia byte a byte; duas trocavam só a
   caixa inicial; três eram **ênfase** escrita com aspas angulares. Correção: toda aspa ≥ 25 caracteres agora sai de
   `span()`, e ênfase passou a ser `**negrito**`. O auditor foi quem pegou — ele existe para isso.
2. **R-1 — a camada 0 publicava *extensão* no lugar de *offset*, e três rótulos dados por certos:** «Sarney» (o
   bruto grafa **`Sarnei` 8×** e `Sarneio` 1×), «foro privilegiado» (**0** ocorrências) e «venda de mandato» (**0**).
   A tabela foi **regenerada por script** âncora a âncora; a descrição do bloco Q-1 no dossiê foi reescrita com a
   lista medida e a negativa explícita dos termos inexistentes.
3. **R-3 — quatro grafas de dicionário que eu havia «lembrado» não existem** (`Jaela`, `Javella`, `janhu`, `Lusbel`,
   `biodeemo` = 0 ocorrências). O dicionário do ciclo passou a ser feito **só** de contagem medida. Se o portão B não
   existisse, isso teria virado **fato de Base** — é exatamente o tipo de dano que a esteira foi construída para
   impedir.

Nota de processo, registrada sem eufemismo: o BLOCO A foi aplicado, o pacote mudou (uma nota de RC-755) e foi preciso
**reverter e reaplicar** — `git checkout <commit anterior> -- termos/ ferramentas/dados_termos.py`, não `git
checkout -- termos/` (que restauraria o próprio estado aplicado). A reaplicação passou limpa por C e D; o custo foi
de uma rodada, e o ganho é que **ficha e pacote são byte a byte a mesma coisa**.

## 6. Pendências carregadas (o radar da Operação)

1. **RC-020** foi materializada **sem** abrir arestas: os quatro `relacionados` do cadastro (RC-007, RC-078, RC-024,
   RC-082) continuam **sem aresta** em `RELACOES`, declarado na ficha. Se o Curador quiser ligar, é decisão dele.
2. **Onze códigos continuam `ficha=False`** e agora têm vínculo desta fonte na malha — RC-089 (Processador Val) é o
   caso mais gritante: a palestra é **a** definição canônica da função, e a ficha não existe. Materializar = nova
   ordem.
3. **A fila de livros** (gênese de *Terra Atlantis*, os evangelhos gnósticos em tradução, o «mergulho na escuridão»
   escrito com o próprio Javé, o 2º volume da série anunciada) ficou **no radar datado**, sem registro — como mandou
   D-11.
4. **Cinco divergências internas desta fonte** seguem herdadas sem resolução, por decisão (O-6): as três contagens de
   famílias, a contradição a oscilação entre engenhosidade máxima e confiança zero, as duas faces de Javé (dependente e tirano), a filologia
   improvável de «Omério»/«Esildo», e «Hipergória» convivendo com Alto Langron.
5. **`INDICE-PALESTRAS.md`** ganhou a linha de 25/04/2020, mas o acervo **P2020 inteiro** continua com buracos de
   catálogo (ex.: 18/04/2020 e 09/05/2020, que já têm fonte na malha, seguem sem linha no índice). É tarefa de
   catálogo, não de ciclo.
6. **`DECISAO-DO-CURADOR.md` do ciclo P2021-05-15** mantém a `DECLARAÇÃO DE ESTADO` sem verbatim da devolutiva que a
   originou (registra-se, não se reconstitui de memória — regra da casa).

## 7. Posição do agente ao fechar o ciclo

O ciclo **não** inventou termo, **não** harmonizou cronologia, **não** corrigiu grafia em silêncio e **não** tocou
uma linha de obra. Ele fez o que a esteira permite: **desceu a data de 12 fichas** (a mais antiga fala do acervo com
conteúdo estruturante desde P2020-04-18), **materializou um cadastro órfão** com a definição vinda da fonte que o
Curador indicou, e **enterrou 16,5 mil caracteres de política nacional** a pedido do próprio autor e por decisão do
Curador — com o gancho e a desculpa **no lugar**, para que o leitor saiba que o corte existe e por quê.

Se alguma aspa deste ciclo estiver errada, o erro é **do método que a produziu**, não da memória de quem escreveu:
todas elas foram recortadas de `original.txt` por um caça-âncoras que se recusa a escrever o arquivo quando a âncora
não bate exatamente uma vez. É incômodo de ler e é por isso que ele fica.

*Ferramentas do ciclo (todas reexecutáveis):* `_aspas_P2020-04-25.py` (caça-âncoras) ·
`_gerar_dossie_P2020-04-25.py` · `_gerar_ampliacoes_P2020-04-25.py` · `_gerar_ficha_RC020_P2020-04-25.py` ·
`_vincular_fonte_P2020-04-25.py` · `_aplicar_ampliacoes_P2020-04-25.py` · `_portao_c_fichas.py` ·
`_portao_d_contadores.py` · `_verificar_verbatim_P2020-04-25.py` · `_gerar_apostila_P2020-04-25.py` ·
`_cobertura_apostila.py`.
