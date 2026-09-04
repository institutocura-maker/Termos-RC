# Política de Quarentena entre Ecossistemas — RC × (Jyotish · Ifá · tradições correlacionais externas)

> **Natureza:** política transversal de governança da Base Terminológica RC e do futuro
> corpus de treinamento da IA Local. Não altera `dados_termos.py` por si só; define o que
> **pode** e o que **não pode** entrar na base.
>
> **Status:** VIGENTE (2026-09-04) · **Origem:** recomendação do Agente acatada pelo Curador
> na esteira do ciclo **F029** (Q-F029-D) · **Autor da redação:** Arena.ai Agent Mode.
> **Princípio de base (regra de ouro da esteira):** *não materializar termos fantasmas* —
> nenhuma figura/relação entra sem **ancoragem estrutural em fonte primária** do corpus RC.

---

## 1 · Escopo

Esta política regula a fronteira entre **dois ecossistemas de conhecimento** que convivem no
mesmo repositório e no mesmo computador, mas que **não devem se contaminar**:

| Ecossistema | O que é | Autoridade de fonte |
|---|---|---|
| **RC (Revelação Cósmica)** | Base Terminológica (`dados_termos.py` + `termos/`), grafo de relações, corpus de treinamento da IA Local | **fonte primária RC**: obras/palestras de Jan Val Ellam (autoridade máxima); B031/B060 como fontes secundárias |
| **Tradições correlacionais externas** | Jyotish (astrologia védica), Ifá/256 Odus, mitologias clássicas, simbolismos planetários — domínios de estudo do próprio Curador | corpus **externo**, tradição correlacional; **não é** fonte RC |

O caso motivador concreto foi: figuras mitológicas clássicas (Afrodite, Ártemis, Poseidon,
Vishnu, Krishna…) e arquétipos divinos possuem correspondências **planetárias bem definidas**
na astrologia védica (navagraha etc.). Como o Curador também treina IA local em Jyotish, a
pergunta é se essas correlações devem (a) entrar na base RC, (b) viver num ambiente isolado,
ou (c) permanecer sob quarentena absoluta.

**Resposta adotada: quarentena absoluta na base**, com espaço isolado e explicitamente
não-canônico para exploração hipotética (ver §4).

---

## 2 · A decisão — quarentena absoluta na base

1. **Nenhum código RC, nenhuma aresta, nenhum campo de equivalência é criado ou preenchido
   a partir de Jyotish, Ifá ou de qualquer tradição correlacional externa.** Isso vale mesmo
   quando a correspondência é "bem estabelecida" e secularmente calibrada (ex. Mangala ↔ Marte,
   Brhaspati ↔ Júpiter/guru). Para o motor de inferência, uma equivalência **não deixa de ser
   inventada** por ter rótulo vindo de outra tradição: ela continua **sem fonte primária RC**.

2. **A correspondência astrológica não é prova** — é, no máximo, **hipótese de busca interna**
   (ver §4). Nunca entra no artefato curado como fato, variação ou nota de equivalência.

3. **Isso generaliza a regra da navalha já fixada no ciclo F029 (Q-F029-D):** figuras míticas
   sem ancoragem estrutural primária permanecem **variações míticas não-codificadas** (contexto
   dentro de códigos guarda-chuva como Arcontes/famílias estelares), **sem código RC próprio** e
   **sem forçar simetrias** que o próprio autor não cravou.

4. **Precedente já vigente, agora elevado a política transversal:** a *Nota de confinamento O-4*
   registrada na ficha **RC-092** vedava o cruzamento da taxonomia hindu (Kapila/Samkhya, três
   karmas) com as bases de Jyotish — *"escopos isolados do ecossistema local"*. Esta política
   estende essa vedação a **toda e qualquer tradição correlacional externa** e a **todo** termo,
   não apenas ao caso Kapila. A regra segue o mesmo princípio da nota O-4 e o torna recorrente.

---

## 3 · Epistemologias incompatíveis (fundamento)

A vedação não é purismo — é adequação de objeto:

- **RC é uma ontologia interna** com autoridade única e bem definida: a fala/obra primária de
  Ellam. Sua taxonomia hindu (Vishnu, Shiva, Brahma, Krishna…) é **mecânica filosófica interna**:
  refere-se à geopolítica cósmica e à rebelião, **não** ao panteão religioso terrestre.
- **Jyotish/Ifá são tradições correlacionais externas**, com lógica própria e sem vínculo de
  autoridade com o corpus RC.

Merging das duas produz exatamente o **"romantismo terrestre"** que a regra de ouro da esteira
existe para barrar: falsas simetrias, relações que o autor não cravou e **pseudo-confirmação**
(a equivalência "parece calibrada" só porque é secular). A proteção maior é contra o motor RAG
"inventar" uma correspondência e tratá-la como âncora — o mesmo risco que a navalha do F029 quis
eliminar ao não codificar Poseidon/Afrodite/Ártemis.

---

## 4 · O único caminho de uso: hipótese de busca, em espaço isolado

Se a matriz externa tiver valor, é **heurístico, nunca probatório**:

1. A correspondência planetária pode **apontar candidaturas a investigar dentro do próprio
   corpus RC** — ex.: "se a matriz sugere que um ser RC governa um domínio X, procurar na fonte
   primária onde esse ser é ancorado".
2. Qualquer exploração assim vive num **espaço isolado e explicitamente etiquetado** —
   **não-canônico, sem write na base, reversível** (planilha/nota `hipóteses <Tradição> × RC — NÃO é fonte`).
3. Só se torna **candidata a código (BLOCO 2 / fila aberta)** quando houver **pérola de fonte
   primária** confirmando a função cósmica/DNA do ser — **nunca** a tabela externa por si só.

---

## 5 · Regras operacionais (resumo executável)

- [ ] Não criar código RC, aresta ou equivalência com origem em Jyotish/Ifá/tradição externa.
- [ ] Não gravar correspondência planetária como nota de equivalência em ficha canônica.
- [ ] Manter quarentena **mesmo entre os dois corpora de treinamento da IA Local** — RC e Jyotish
      são escopos isolados do ecossistema local (herança da nota O-4).
- [ ] Se uma figura cruzar os dois mundos, registrar **separadamente e sem propagação**: lado RC
      apenas com fonte primária; lado externo fora da base.
- [ ] Exploração especulativa permitida apenas em artefato isolado etiquetado NÃO-canônico.

---

## 6 · Referências

- **Ciclo F029** (`consolidacoes/29-PERSONAGENS/`): decisão **Q-F029-D** (panteões sem RC = variações
  míticas não-codificadas) e decisões D-1/D-1_krishna.
- **RC-092** (Quarto Logos / Olm): *Nota de confinamento O-4* (precedente Jyotish) — linha ~100.
- **Regra de ouro da esteira**: *não materializar termos fantasmas*; anti-fabricação,
  anti-pseudo-confirmação, cotejo com fonte primária (G1/G3).
- **`PLANO-CORPUS-TREINAMENTO-IA-LOCAL.md`**: a IA Local deriva o corpus da Base consagrada;
  logo, a quarentena aqui defendida protege automaticamente o futuro corpus de treinamento.
