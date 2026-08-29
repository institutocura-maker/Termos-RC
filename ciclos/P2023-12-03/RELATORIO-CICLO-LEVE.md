# RELATÓRIO DO CICLO ZERO — esteira LEVE · `P2023-12-03`

**Data de execução:** 29/08/2026 · **Agente:** Arena (ramo `arena/01a04969-termos-rc`)
**Instrumento:** `ferramentas/motor.py` — Motor Único, 976 linhas · 52.312 B, nascido neste ciclo
**Configuração deste ciclo:** `ciclos/P2023-12-03/ciclo.toml` (toda a curadoria mora aí; o motor não contém alvo, âncora, rótulo nem juízo)
**Baseline do portão D:** `f0baedc` (o BLOCO B do ciclo pesado, que fechou esta mesma palestra)

> Este ciclo não é uma palestra nova. É o **ciclo zero**: a mesma fonte que a esteira pesada
> já fechou (`A Rebelião de Lúcifer ainda por ser Finalizada`, 03/12/2023), reprocedida no
> formato novo, para que a comparação entre os dois rites seja possível com números e não
> com impressão. O critério de aceite combinado com o Curador foi este: **se o garimpo leve
> perdeu alguma coisa que o ciclo pesado achou, a reforma falhou** — por mais leve que tenha
> ficado.

---

## 1 · Veredicto do aceite — medido

| Grandeza | Ciclo pesado (registro fechado) | Ciclo zero (este) | Veredicto |
|---|---|---|---|
| Citações verificadas byte a byte no bruto | 147 | **147** | igual, sem perda |
| Candidatas do caderno achadas pelo garimpo | (147 no pacote) | **147** | o motor achou exatamente as mesmas |
| Spans retidos por trava | 3 | **3 spans em 2 códigos** | igual; a régua nova diz as duas unidades |
| Fichas com `## Ampliação — P2023-12-03` | 107 | **113** (107 + 6) | as 6 ordens órfãs entraram |
| Termos novos · relações novas · obras novas | 0 · 0 · 0 | **0 · 0 · 0** | preservado |
| Teto `RC-778` | intocado | **intocado** | 0 cadências consumidas |
| Estado absoluto da Base | 777 · 1.856 · 460 arquivos · 459 `ficha=True` | **777 · 1.856 · 466 · 465** | delta = exatamente o mandado (ver §4) |
| Bytes escritos pelo ciclo | 1.133.595 (pasta inteira do ciclo) | **140.346** | **8,1× menos**; 7,3× retirado o `original.txt`, que a esteira leve também preserva |
| Portões | A · B · C · D · E + cobertura | **A · B · C · D** | os três essenciais + o de contadores; ver §5 |
| `selftest` | (não existia) | **7/7** | 5 casos no ciclo zero + 2 no §8 |

**Nada do garimpo pesado se perdeu.** O caderno leve tem 25 pérolas de 147 candidatas, e o
livro-razão guarda as **122 recusadas com motivo** — que é a peça que permite responder,
para qualquer span da fonte, por que ele não virou ficha. Sem o livro-razão, "não
transcrevemos a apostila inteira" significaria "não podemos dizer o que ficou de fora".

## 2 · O que este ciclo entregou

1. **Catálogo sistemático** — entrada limpa selada: `original.txt` 105.859 B, SHA-256
   `41b3f914befb…4e1021` conferido contra a ficha de ingresso, **0 caracteres de
   controle**, 25 unidades com fala, endereço de span em `U####` + offset de caracteres.
2. **Consistência terminológica** — as 6 fichas das ordens que o despacho de fechamento do
   ciclo pesado nomeou sem destino (`RC-093`, `RC-189`, `RC-280`, `RC-035`, `RC-375`,
   `RC-344`) foram **materializadas** com o conteúdo já aprovado do pacote, e o cadastro
   virou `ficha=True` nas 6 linhas correspondentes. `RELACOES` não foi tocada (delta 0):
   neste ciclo nenhuma aresta tinha evidência para nascer.
3. **Caderno de pérolas** — `ciclos/P2023-12-03/DOSSIE-RAG_P2023-12-03.md`, 607 linhas ·
   13.939 B, nas quatro seções do formato novo (metadados · resumo executivo da tese ·
   caderno · atualizações para a Base), cada aspa com endereço de unidade e faixa de
   caracteres.
4. **Corpus RAG** — `rag/perolas/` com **25 cards atômicos** (1 card por pérola,
   front-matter com `id`, `ciclo`, `sha256_fonte`, `unidade`, `chars`, `termo`, `status`,
   `trava`, `lacuna`) + `rag/MANIFESTO-P2023-12-03.json` com o SHA-256 de cada card.
   ⚠️ **Estado político:** todos os 25 saem com `status: candidata`. O exportador foi
   exercitado sob a chave `exportar_candidatas = true`, declarada no `.toml` e registrada no
   manifesto como **ensaio do ciclo zero** — para a esteira não nascer com um passo não
   testado. **O portão real de consumo continua sendo `aprovada`**, e o corpus não deve ser
   indexado enquanto o Curador não marcar a aprovação no dossiê. Sem o ensaio, o número de
   cards aptos a entrar hoje é **0**.

## 3 · Emendas declaradas no material do ciclo engavetado

Duas correções foram feitas **no material do ciclo fechado**, não no bruto. Cada uma está
anotada no próprio arquivo, com carimbo da data e da origem:

1. **Má-citação em `BLOCO 4` do pacote (`_ampliacoes_P2023-12-03.txt`) e no
   `RELATORIO-DE-CICLO.md`.** O texto dizia que a fonte nunca teve «coragem nem saco» de
   fazer a palestra sobre a gênese da hibridagem. O bruto diz **`nem coragem, nem saco de
   fazer`** — faltavam o `nem` inicial e a vírgula. A aspa foi reposta byte a byte contra o
   `original.txt`; a frase ao redor foi ajustada só no verbo de elocução («disse nunca ter
   tido»). Nada mais nos dois blocos mudou. *Como se descobriu:* o portão B do motor novo
   cobrou do pacote a mesma régua que cobra das fichas, e a aspa não passou. *Onde ainda
   existe a supressão:* `analise/camada-0.txt` (linha 191 da tabela de candidatas) — é
   intermediário gerado, fala em `backticks` e não em aspas, e por isso **não** é citação;
   fica como está, declarado aqui.
2. **Aspa de glosa rebaixada no `BLOCO 1` (`RC-189`).** O bloco citava `«Depois que Eva
   disse…»` entre aspas angulares, sendo a referência elíptica a um span **retido** por
   máscara do STT (BLOCO 5) — logo, um span que não verifica. Pela regra da casa, aspa é
   reserva de citação conferível: a referência passou a `backticks` no próprio material.
   A partir daí o motor não precisou rebaixar nada na materialização (0 ocorrências), e a
   paridade ficha ↔ pacote fechou limpa.

**Reexecução dos portões do próprio ciclo engavetado, depois das emendas:**
`_verificar_verbatim_P2023-12-03.py` → *CITAÇÕES FIEL À FONTE ✓* (paridade de aspas 0
problemas; verbatim 0 divergências; portão E 315 endereços, 0 divergência) ·
`_portao_c_fichas_P2023-12-03.py` → *FICHA A FICHA, TUDO FIEL À FONTE ✓* (113 fichas,
111 citações verificadas, 0 divergentes) · `_portao_d_contadores_P2023-12-03.py` →
**REVISAR ⚠️ (2)**, as duas únicas linhas vermelhas sendo `arquivos = 466 ≠ 460` e
`ficha=True = 465 ≠ 459`. **Não foram consertadas**: o portão D do rite pesado fixa estado
**absoluto** na data do seu próprio fechamento, e por construção acusa qualquer ciclo
posterior. O vermelho é a prova de que aquele instrumento apodrece — é a razão de o motor
novo medir **delta** (§4). Editar o portão antigo para o vermelho sumir está proibido.

## 4 · Portões deste ciclo — o que verde quer dizer

```
PORTÃO A ✓ SHA-256 confere · 0 bytes de controle · 105.859 B · 25 unidades com fala
PORTÃO B ✓ 147/147 citações do pacote conferidas byte a byte no bruto
         ✓ 25 aspas do dossiê conferidas · 113 fichas com a seção do ciclo conferida
         · aspas de glosa: 11 de 11 são span verificado (nenhuma precisou ser rebaixada)
PORTÃO C ✓ 113 fichas em paridade com o pacote · 0 vazamentos do léxico vetado (4 marcas)
         · 7 fichas que nomeiam grupo humano sob vigilância: caderno delas é fechado
PORTÃO D ✓ Δ arquivos = 6 · Δ ficha_true = 6 · Δ termos = 0 · Δ relacoes = 0
         ✓ teto suspenso-com-cadência: 0 termo novo ≤ 0 autorizado
         ✓ cadastro válido: OK: 777 termos, 1856 relações — dados válidos
SELFTEST ✓ 5/5 anomalias plantadas detectadas na data deste fechamento (âncora inexistente ·
           âncora ambígua · byte de controle DOCX · paráfrase vestida de citação · cedilha na
           normalização); o motor está hoje em 7/7 — ver §8
```

A paridade do portão C é aferida **depois** da normalização de aspas de glosa, aplicada aos
dois lados. Assim a regra continua sendo teste real — e não o motor apagando o que não lhe
convém, nem a divergência virar norma do arquivo.

## 5 · As lições deste ciclo zero — 14 consertos no instrumento, 0 no produto

Nenhuma linha vermelha deste ciclo foi resolvida mudando texto para caber na régua. Todas
as 14 correções abaixo foram no motor, e cada uma é o tipo de erro que **produziria um
número plausível e errado**:

1. **`BLOCO 1` engolia os blocos 2–5.** O parser cortava só em `^### RC-\d{3}$`, então o
   corpo do último código do bloco carregava as notas editoriais dos blocos seguintes — e o
   portão cobrava-as como citação: 173 "citações" contra as 147 reais. O fim do bloco agora
   é casado também em `### BLOCO 2`.
2. **O rodapé `---` da ficha entrava na seção medida.** A extração parava no próximo `## `,
   então a régua "corpo divergente do pacote" acusava as 113 fichas por 4 caracteres de
   separador. Há um extrator único, `secao_da_ficha`, que para em `## ` e em `---`.
3. **`git ls-tree` cita nomes com byte não-ASCII.** `RC-572 (×)`, `RC-657 (×)`,
   `RC-706 (ṅ)` somem de uma âncora `.md$` — 460 fichas lidas como 457, delta **9** em vez
   de 6. O padrão agora tolera a aspa final do caminho escapado.
4. **Contar `RELACOES` por regex de linha perde aresta** (há soma fora do bloco principal):
   1.855 vs 1.856. A régua autoritativa passou a ser **executar o texto medido**
   (`medir_codigo`), com fallback de regex declarado; e o motor compara a própria contagem
   com a validação do cadastro — se divergir, ele diz que **o instrumento** está errado.
5. **Duas réguas para a mesma coisa.** `agora()` media por um caminho e `no_commit()` por
   outro; o delta nascia falso.Baseline e hoje usam a mesma função, e a diferença de unidades
   fica impressa (spans × códigos).
6. **Aspas simples e duplas convivem no cadastro** por herança de ciclos. A linha de termo e
   a linha de virada do `ficha` precisaram aceitar os dois estilos — com aspas só duplas no
   padrão, o aplicador não achava as 6 linhas `ficha=False`.
7. **Rodar duas vezes tinha de ser neutro.** `virar_ficha` agora reporta "6 já viradas" em
   vez de abortar; materializar reescreve a seção, não emenda duplicada.
8. **Aspa de glosa ≠ citação.** Um defeito que já estava no material fechado (§3.2) e que o
   motor agora trata por regra declarada, com log impresso de cada substituição.
9. **Motivo de recusa não é pontuação.** O livro-razão agora lista `recusada_por` ("ficou fora
   do teto de 25 por pontuação (3 pt(s), a #26 do ranque)") separado de `sinais`, que é o
   cômputo. 114 recusas por teto, 8 por pontuação negativa.
10. **Retidos: spans (3) ≠ códigos (2).** O rite pesado contava spans; um contador de códigos
    diria "2" e pareceria contradição com o arquivo de fechamento.
11. **Chave não usada no `.toml` é erro.** Config validada é a que o ciclo leu de fato;
    mantida do rite pesado, e foi ela que impediu a chave nova do exportador de virar
    decoração.
12. **O RAG só consome `aprovada`.** O ensaio deste ciclo foi explícito no manifesto; sem a
    chave, a esteira exportaria 0 cards — e 0 é o estado político correto hoje.
13. **`[tese]` é mesa, não lista.** Lida como lista, o `## 2` do dossiê saiu com um único item
    chamado "pontos" — um resumo executivo que não resume é exatamente o que o despacho veio
    impedir, e a esteira o teria exportado para a IA local sem que ninguém lesse.
14. **A validação de config passou a valer dentro das mesas.** Subchave que o motor não lê é
    erro, e código nomeado no `.toml` que não existe no cadastro é **ordem órfã fabricada em
    config**. As duas guardas foram testadas com anomalia plantada (`RC-999` em
    `[definicoes]`, `fora_do_contrato` em `[tese]`, chave raiz desconhecida) — as três mordem.

## 6 · O que fica aberto, por decisão — não por descuido

- **Aprovações pendentes do Curador.** 25 pérolas `candidatas`; nenhuma `aprovada`. O corpus
  real do RAG local cresce na cadência do carimbo, não na do motor.
- **`RELACOES` reaberta pelo despacho, sem aresta nova neste ciclo.** A regra aceita está
  escrita no motor do próximo: aresta **tipada** (`fundamenta`/`contradiz`/`antecipa`/
  `exemplifica`), **com evidência** (span + endereço) e **selo datado**; proibida aresta entre
  termos sem arquivo. Como nenhuma das 147 citações deste ciclo sustentou aresta com essa
  cara, o delta foi 0 — declarado, não adiado em silêncio.
- **Portão D do ciclo pesado:** 2 vermelhos estruturais (contadores absolutos), congelados
  por regra. Qualquer ciclo novo da casa acende os mesmos dois; é o preço de o instrumento
  antigo medir estado em vez de variação.
- **Duas pendências da esteira pesada encerradas por despacho** (reauditoria do `ç` no
  caça-âncoras herdado; micro-ciclo das duas emendas em `P2023-12-02`): ficam **declaradas
  como encerradas na esteira velha** e não foram abertas aqui. O defeito do `ç` está
  corrigido no instrumento novo (selftest nº 5 o prova) e por isso não migra como dívida.
- **Fila que a cadência do teto tem de resolver primeiro.** `RC-184` (*Trava-demo*) tem aresta em `RELACOES` (`RC-086 → rompe → RC-184`), quatro fichas apontando para ela, e **não tem arquivo**: é o tipo exato de lacuna que a pérola aprovada passa a ter autoridade para fechar, sem lote silencioso. O ciclo zero não a tocou porque nenhuma das 147 citações a nomeou.
- **Próximas palestras (~150):** cada uma passa a ser um diretório `ciclos/<SIGLA>/` com um
  `ciclo.toml`. A fileira em `uploads_recepcao/` tem 34 TXT · 4,11 MB aguardando.

## 7 · Como se roda um ciclo leve (a receita, para conferir esta reforma)

```bash
python3 ferramentas/motor.py selftest                 # 5/5, senão o motor está inapto
python3 ferramentas/motor.py --ciclo P<SIGLA> status        # só lê: o que o .toml manda
python3 ferramentas/motor.py --ciclo P<SIGLA> entrada       # cp + sha256 + bytes de controle
python3 ferramentas/motor.py --ciclo P<SIGLA> ancorario     # livro-razão de spans
python3 ferramentas/motor.py --ciclo P<SIGLA> dossier       # as 4 seções do formato novo
python3 ferramentas/motor.py --ciclo P<SIGLA> rag           # cards só de `aprovada`
python3 ferramentas/motor.py --ciclo P<SIGLA> tudo           # os quatro portões no fim
```

O ciclo leve escreve, no máximo: `ciclos/<SIGLA>/{ciclo.toml, ancorario_*.json,
DOSSIE-RAG_*.md, RELATORIO-CICLO-LEVE.md}`, `termos/RC-*.md` das materializações listadas na
§4 do dossiê, as linhas `ficha`/`FONTES`/`RELACOES` do cadastro que o `.toml` mandou, e
`rag/perolas/*.md`. **Nenhuma linha de `.py` é escrita por ciclo** — o instrumento é um só, e
o que muda entre ciclos é declaração.

---

## 8 · Depois deste fechamento: o motor aprendeu a **abrir** ciclo (não só reproceder)

Este relatório documenta o ciclo zero, que testou a esteira reprocedendo um ciclo **fechado**. Quando o
Curador nomeou a primeira palestra nova para o formato leve, apareceram três lacunas de autoria que o
ciclo zero não podia revelar — e o remédio foi no instrumento, não no produto:

1. **`motor.py novo <TXT>`** — a abertura: cópia byte a byte para `ciclos/<SIGLA>/original.txt`, SHA-256
   selado, e andaime (`ciclo.toml` + `pacote_<SIGLA>.txt`) com os campos de curadoria **vazios**, para que
   a ausência seja visível em vez de um zero disfarçado de resultado. Recusa sobrescrever um
   `original.txt` já selado cujo conteúdo difere: fonte preservada não se reescreve.
2. **`motor.py --ciclo <SIGLA> busca "<âncora>"`** — o cortador: devolve o período verbatim do bruto com
   `U####` e faixa de caracteres, pronto para colar no pacote. É a materialização da regra *nenhuma aspa
   digitada à mão*: quem garimpa não transcreve de memória.
3. **`motor.py --ciclo <SIGLA> fatias [largura]`** — a leitura integral com prova: corta em fronteira de
   período e fecha asserindo que a concatenação das fatias **é** o arquivo. A esteira leve não reemite a
   transcrição, mas quem escolhe as pérolas tem de ter lido tudo; cobertura continua sendo igualdade de
   texto, não promessa.

O `selftest` ganhou os dois casos que essas funções exigem e passou de **5/5 a 7/7**: o recorte devolvido
tem de verificar no bruto (senão o ciclo nasceria com citação falsa) e a abertura tem de recusar o
`original.txt` divergente (senão a preservação acabaria ali). Testado de ponta a ponta num andaime
temporário — `novo` → `entrada` ✓ contra o hash que ele mesmo gravou → `busca` com 22 ocorrências todas
✓ → `fatias` com cobertura provada — e o caso decisivo: **roda-se `tudo` num andaime vazio e ele aborta
vermelho** ("o pacote não tem uma aspa sequer"), porque ciclo não fecha por omissão.

Nenhum produto foi escrito nesse teste, a Base continua em 777 · 1.856 · 102 (466 arquivos, 465
`ficha=True`), e o andaime do ensaio foi apagado. O primeiro ciclo leve de palestra nova está **pronto para
rodar no minuto em que o TXT chegar** — a palestra nomeada (`2023-12-17 Lúcifer e a Rebelião dos Elétrons`)
não estava no sandbox quando esta rodada foi fechada.
