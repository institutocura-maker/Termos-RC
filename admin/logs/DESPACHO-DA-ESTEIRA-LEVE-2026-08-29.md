# DESPACHO DA ESTEIRA LEVE — 29/08/2026

**Registro normativo da reforma do processo.** Este arquivo é a peça que os próximos ~150
ciclos leem antes de tocar em qualquer coisa. O parecer crítico do agente está em
`../../diagnostico/DIAGNOSTICO-DO-PROCESSO-2026-08-29.md`; a prova de que a reforma funciona, em
`ciclos/P2023-12-03/RELATORIO-CICLO-LEVE.md`.

> ⚠️ **Aviso sobre verbatim, declarado e não resolvido por conta própria.** O despacho foi
> recebido no chat da sessão de 29/08/2026. A praxe da casa (`DECISAO-DO-CURADOR.md`) é
> gravar a palavra do Curador **ipsis litteris**, e o texto integral não ficou disponível em
> arquivo para este registro. O que segue é o **conteúdo normativo tal como foi aplicado**,
> item por item. Onde a redação literal importar (para citação futura), basta V.Sa. colar o
> despacho aqui nesta sessão que o arquivo é substituído pela transcrição integral, sem mais
> nada mudar.

---

## 1 · O despacho, nos seus quatro atos

**Ato 1 — Fim do teto rígido, com cadência.** `RC-778+` deixa de ser reserva intocável e
passa a ser **consequência**: um código novo só nasce quando uma **pérola aprovada** o exigir.
Cada materialização tem de aparecer listada na §4 do dossiê do ciclo. O contador global passa
a ser **reportado, não respeitado**. Proibida criação em lote silenciosa — o que se proíbe é
o lote sem destinação, não o crescimento.

**Ato 2 — Portão de aprovação da pérola.** Toda pérola nasce `status: candidata`. O RAG
exporta **só `aprovada`**. Rejeitada continua no arquivo, com o motivo. Quem marca a
aprovação é o Curador; o motor não se auto-carimba.

**Ato 3 — Livro-razão de âncoras.** Obrigatório no ciclo leve: todos os spans que o motor
classificou, escolhidos **e recusados, com motivo**. É a contrapartida da fim-da-transcrição-
integral: sem apostila volumosa, a garantia de que nada se perdeu silenciosamente tem de vir
de um registro contábil, não de um texto que reproduz tudo.

**Ato 4 — Pendências da esteira pesada.** Migram **só as 6 ordens órfãs** (materializar com
o conteúdo já aprovado do pacote: `RC-093`, `RC-189`, `RC-280`, `RC-035`, `RC-375`, `RC-344`).
A reauditoria dos ciclos anteriores pelo defeito do `ç` no caça-âncoras e o micro-ciclo das
duas emendas em `P2023-12-02` ficam **declarados como encerrados** na esteira pesada — não se
abrem por aqui.

## 2 · As quatro respostas que fecharam as perguntas do agente

1. **Teto:** suspenso com cadência, no regime do Ato 1 (não abolido: cada consumo tem de ter
   pérola aprovada por trás e linha no §4 do dossiê).
2. **Aprovação:** o carimbo é do Curador; o exportador do RAG obedece ao `status`.
3. **Pendências:** só as 6 ordens órfãs; as duas outras dívidas ficam declaradas e encerradas.
4. **`RELACOES`:** o despacho **reabre** a atualização contínua da malha — «e suas relações»
   voltou a ser obrigação do ciclo, não do curador sozinho.

## 3 · A regra que o agente propôs para a malha reaberta (aceita como modo de execução)

Nenhuma aresta entra sem as três peças:

- **tipada** — `fundamenta` · `contradiz` · `antecipa` · `exemplifica` (nada de "relaciona-se");
- **com evidência** — o span que a sustenta, com endereço de unidade e faixa de caracteres;
- **selo datado** — o ciclo que a abriu; divergência se registra, não se harmoniza (D-9).

Proibida aresta entre termos **sem arquivo** (a Base tem 317 termos do índice sem ficha; uma
aresta entre fantasmas é relação que nenhum leitor pode auditar). Sem as três peças, o ciclo
entrega **delta 0 em `RELACOES`** e declara isso — como fez o ciclo zero.

## 4 · O rito leve vigente — o que cada ciclo entrega

**Produto: estritamente três coisas.**
1. **Catalogação sistemática** — entrada limpa, fonte selada por SHA-256, termos abordados.
2. **Consistência terminológica** — a Base e suas relações, nos termos do §3 acima.
3. **Garimpo de pérolas** — os trechos que fecham lacunas da Base, na íntegra, endereçados.

**Formato do produto: dossiê `.md` enxuto, quatro seções.**
`§1` cabeçalho de metadados (sigla, data, hash, termos tocados) · `§2` resumo executivo da
tese · `§3` caderno de pérolas (verbatim, com bloco/tempo) · `§4` atualizações para a Base.

**Engenharia.** Fim da reescrita de código por ciclo. Aparato unificado no Motor Único
`ferramentas/motor.py`; operação por config declarativa `ciclos/<SIGLA>/ciclo.toml`. Os
portões essenciais permanecem: **A** integridade da fonte · **B** verbatim · **C** paridade
ficha ↔ pacote e veto de trânsito · **D** contadores como *delta* contra o commit-base, com a
validação autoritativa do cadastro. `selftest` tem de dar 8/8; se der menos, o motor está
inapto e nenhum ciclo abre com ele.

**Autoria do ciclo, com o cortador na mão — os três comandos que faltavam para abrir um ciclo
novo (até aqui o motor só reprocedia ciclo fechado): `novo` copia o TXT byte a byte para
`ciclos/<SIGLA>/original.txt`, sela com SHA-256 e escreve o andaime (`ciclo.toml` + `pacote` com os
campos vazios, para que a ausência seja visível, não um zero disfarçado de resultado) — e
**recusa** sobrescrever fonte já selada cujo conteúdo difere; `busca "<âncora>"` devolve o
período verbatim com `U####` e faixa de caracteres, pronto para colar, porque *nenhuma aspa
digitada à mão* quer dizer isto e não *prometo transcrever certo*; `fatias` é a leitura integral
com prova de cobertura (a concatenação das fatias é o arquivo, asserido) — a esteira leve não
reemite a transcrição, mas quem escolhe as pérolas tem de ter lido tudo.

**Pousar na Base, sem reescrever história.** Dois passos fecham o ciclo: `ampliar` insere (ou substitui, só quando o conteúdo é o que o motor escreveria) a seção `## Ampliação — <SIGLA>` nas fichas que já existem, sem tocar em mais nada do arquivo — e **recusa** sobrescrever uma seção escrita à mão, declarando quantas; `vincular` acrescenta a sigla do ciclo à lista de fontes do cadastro, idempotente, porque ampliação sem vínculo existe na ficha e não existe na malha. `materializar`, por sua vez, aborta em ficha que existe e não foi escrita por ele — criar ficha é ordem, não conveniência de formatar.

## 5 · O que a leveza NÃO toca (invioláveis, com o motivo)

- **Nenhuma aspa digitada à mão.** Com a apostila integral fora, o portão de verbatim passou a
  ser a **única** defesa contra paráfrase vestida de citação — e por isso ele agora cobra o
  pacote, o dossiê **e** a seção do ciclo em cada ficha. O resumo executivo (que não é span)
  sai em prosa **sem aspas angulares**.
- **Aspas bloqueadas não transitam** (D-1…D-5 do regime de moldura): as de gênero, de baixa
  interioridade, de política conjuntural e as que atravessam máscara do STT ficam na fonte e
  no livro-razão, nunca em ficha de pessoa, paciente ou grupo humano.
- **Nada de harmonizar números** (D-9): divergência coexiste com selo datado.
- **Consertar o gerador, nunca o produto.** Vermelho de portão se resolve no instrumento; o
  número que não bate é informação, não erro de digitação.
- **Config validada é config lida:** chave não usada no `.toml` é erro de ciclo.
- **Fonte intocada:** `original.txt` é preservado byte a byte; fim da reemissão de transcrição
  não é licença para reescrever o que existe. Preservação = arquivo + hash na entrada.
- **Idempotência:** rodar o passo duas vezes tem de ser neutro (o sandbox reverte; o rito tem
  de poder recomeçar do meio).

## 6 · Onde está cada peça

| Peça | Caminho |
|---|---|
| Motor Único (o instrumento de todos os ciclos) | `ferramentas/motor.py` |
| Config declarativa do ciclo | `ciclos/<SIGLA>/ciclo.toml` |
| Pacote de ampliação (o que entra em ficha, o que fica retido) | `ciclos/<SIGLA>/pacote_<SIGLA>.txt` |
| Fonte selada do ciclo leve | `ciclos/<SIGLA>/original.txt` |
| Livro-razão de âncoras | `ciclos/<SIGLA>/ancorario_<SIGLA>.json` |
| Dossiê RAG (as 4 seções) | `ciclos/<SIGLA>/DOSSIE-RAG_<SIGLA>.md` |
| Relatório do ciclo | `ciclos/<SIGLA>/RELATORIO-CICLO-LEVE.md` |
| Cards atômicos do corpus | `rag/perolas/PER-<data>-<n>.md` |
| Manifesto do corpus (com o hash de cada card) | `rag/MANIFESTO-<SIGLA>.json` |
| Cadastro autoritativo da Base | `ferramentas/dados_termos.py` |
| Ciclos pesados concluídos (legado, não se regenera) | `apostilas/CONCLUIDAS/` |

## 7 · Estado das contagens a partir deste despacho

Base: **777 termos · 1.856 relações · 102 obras · 466 arquivos de ficha · 465 `ficha=True`**
(delta do ciclo zero: +6 arquivos, +6 fichas vivas, 0 termos, 0 relações, 0 obras). Teto
reportado, não respeitado: nenhuma cadência consumida até aqui. Fila: `uploads_recepcao/` com
34 TXT · 4,11 MB, e ~150 palestras restantes no formato leve.
