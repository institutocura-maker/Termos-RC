# Despacho — presunção de V por fonte de livro (13/09/2026)

**Pergunta do Curador (13/09/2026):** «Para o bloco anterior, pode aplicar_V em todos os termos e
para o próximo também. O que você acha da ideia de considerar marcado com 'V' todo termo que teve
origem em um livro (Bxxx)? Já dei uma olhada geral neles e estão todos corretos.»

**Decisão tomada:** executada (U43) — V aplicado aos 8 do lote 1 da família B, e a regra adotada
para os lotes seguintes **como presunção com plano de exceções**, nos termos abaixo.

---

## 1. Parecer — favorável, com duas ressalvas e um plano de exceções

### O que a favorece

1. **Livro é o lastro mais forte da casa.** É a única fonte em que a citação pode ser conferida
   byte a byte contra um `original.txt` estável — ao contrário do STT, que degrada nomes (U30
   documentou «Mar é Cósmica»; RC-304 registrou «Decalião»).
2. **A própria Base já pensa assim.** A regra do loader (Onda 1.5) dá `confianca_fonte = alta`
   exatamente quando `status = verificado` **e** há fonte de livro. A presunção apenas explicita o
   que a métrica derivada já supunha.
3. **Desafoga a fila.** O processo «agente gera planilha → Curador devolve V/X/?» nasceu para
   triar o **duvidoso**. Aplicá-lo a termos cujo lastro é público e verificável consome o recurso
   mais escasso da casa — o tempo de chancela do Curador.

### Ressalva 1 · V e «ter livro» não são a mesma coisa

Na série P7, o V chancela a **identidade do termo**: nome, grafia, categoria, e as decisões de
não-fusão, não-duplicidade e não-colisão. A origem em livro garante **lastro**, não **identidade**.
A própria Base prova isso:

- **RC-053 Deuses · RC-076 Logos · RC-306 Apolo** têm B031 e foram classificados na família
  **F · nome ambíguo** — o parecer do censo é que «sem qualificador canônico uma ficha seria
  verbete-dicionário». Livro não resolve ambiguidade.
- Os **6 da família A** (alias-variação) também têm livro; o remédio deles é a baixa
  administrativa, não o V.
- Os **40 da família E** não foram achados no corpus: são candidatos naturais a erro de atribuição
  ou de grafia — é o caso que o livro *não* resolve e que a leva existe para pegar.

### Ressalva 2 · o 🟢 é também uma afirmação sobre a ficha

O ficha-modelo define 🟢 como «revisado e referenciado (obra + capítulo/página); pode ser citado
como consolidado». Se todo termo com livro virar 🟢, o badge deixa de discriminar os revisados dos
não-revisados. **Custo assumido, com remédio:** cada V presuntivo fica identificado no corpo da
ficha e na certidão do lote — se o senhor quiser re-revisar apenas os presuntivos, a Base os
entrega de uma vez.

### O que a regra não pode atropelar

- **HOLD** — retenção curatorial de outra natureza (RC-833: fonte única de STT + quarentena
  autobiográfica; RC-454 Elm/Moros; RC-822 Mahatma Magant). Vários têm livro. HOLD não se resolve
  por presunção, só por despacho.
- **Trava §7** — sem ficha, não há o que chancelar. A materialização continua sendo o portão.

---

## 2. Redação da regra (para chancela)

> **R · Presunção de V por fonte de livro.** Todo código cuja ficha nasça com citação verbatim
> conferida byte a byte em obra publicada (fonte `B###` declarada no cadastro) recebe o **V** e o
> status 🟢 **verificado**, por presunção de lastro, sem passagem por leva individual. A presunção
> **cai** — e o termo volta a 🟡 provisório, indo a leva própria — nas exceções abaixo.

| Exceção | Condição que suspende a presunção |
|---|---|
| **E1** | código com **HOLD ativo** |
| **E2** | família **F** (nome ambíguo) e família **A** (alias-variação) — até qualificação/baixa |
| **E3** | família **E** (não-achado no corpus) — até auditoria de atribuição/grafia |
| **E4** | **colisão Base×fichas viva** (verificador `checar_colisoes` no driver) |
| **E5** | termo **sem ficha** — a trava §7 continua valendo |

Mecânica: o lote declara `aplicar_V: "presuncao-livro"`; o driver aplica E1–E5 **antes** de
escrever e aborta com relatório se alguma exceção pegar. A checagem E4 é viva (não uma lista
estática): no lote 1, RC-085 e RC-066 constavam da lista de colisões da auditoria P5b e, conferidos
hoje código a código contra todas as fichas e verbetes, **mostraram uso consistente com a Base** —
o remapeamento da P5b os havia sanado. Lista estática teria barrado dois termos limpos.

## 3. Rastreabilidade

- `via = P6-evidência` · `confianca_fonte = alta` (a regra do loader, inalterada).
- Nota «**V aplicado (U43, 13/09/2026)**» no corpo de cada ficha, declarando que o 🟢 é
  **presuntivo** e reversível.
- Certidão por lote, com a lista dos chancelados e o resultado das exceções E1–E5.
- Instrumento: `ferramentas/aplicar_v.py` (aplica e regenera o frontmatter por `motor.fm_toml`).

## 4. Execução imediata (U43)

V aplicado aos 8 do lote 1 — RC-108 · RC-085 · RC-065 · RC-066 · RC-540 · RC-077 · RC-044 ·
RC-392 — após checagem E1–E5: **E1 0** (nenhum no HOLD) · **E2 0** (nenhum em F/A) · **E3 0**
(todos achados no corpus) · **E4 0** (uso consistente em fichas e verbetes) · **E5 0** (todos com
ficha desde a U42).

## 5. Reversibilidade

A regra é um despacho, não uma lei da Base: revogada, basta rebaixar os presuntivos a 🟡 — a nota
no corpo de cada ficha os identifica um a um.
