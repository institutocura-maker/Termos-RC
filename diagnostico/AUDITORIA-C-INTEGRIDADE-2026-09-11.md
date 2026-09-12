# Auditoria Interna — Frente C: Integridade Referencial — 11/09/2026

Leitura pura. Pergunta: os ponteiros da base (relações, fichas, fontes) apontam para coisas que existem?

## C1. Verdade dupla nas relações: `t[6]` × `RELACOES` (detalhamento do achado-bônus de A)

| Estoque | Formato | Pares únicos |
|---|---|---|
| `TERMOS[t][6]` | string `;`-separada (ex.: `"RC-002; RC-003; …"`) | 4.494 |
| `RELACOES` | tuplas `(origem, tipo, destino, fonte)` | 1.723 (em 1.898 lançamentos) |
| Só no primeiro | — | **2.939** |
| Só no segundo | — | **168** |
| Interseção | — | 1.555 |

Leitura: são dois estoques com **filosofias distintas** — `t[6]` é "ver também" (amplo, não-tipado), `RELACOES` é relação tipada (279 tipos, dos quais `relaciona-se-a` sozinho tem 896/1.898 = 47%). Nenhum dos dois está errado; o erro é **não declarar a diferença**. Quem consome `RELACOES` (xlsx) vê 1.723 pares; quem lê `t[6]` (índice-mestre) vê 4.494. Proposta: declarar (`t[6]` = navegação ampla, `RELACOES` = relações curatoriais tipadas) + reconciliar os 168 pares órfãos do segundo (toda relação tipada deveria existir como navegação) — e auditar os 9 lançamentos duplicados em `RELACOES` e os tipos hapax (cauda de 279 tipos sugere vocabulário não-controlado).

Notas positivas: **zero self-loops**, e o tipo genérico `relaciona-se-a` (47%) é honesto — melhor que tipar à força.

## C2. Códigos inexistentes referenciados: **zero**

Nem `t[6]` nem `RELACOES` apontam para códigos fora do cadastro. O `validar()` de `dados_termos.py` + o verificador seguram este portão. ✅

## C3. `ficha=True` × arquivo físico: **sincronia perfeita**

`True` sem arquivo: 0 · arquivo sem cadastro: 0 · `False` com arquivo: 0 · arquivos duplicados por código: 0. ✅ (O portão "sem-ficha" do P7 tem lastro real.)

## C4. Fontes-fantasma: siglas citadas sem pasta no disco

**Livros (B):** 46 pastas no disco; **28 siglas citadas em fichas sem pasta**, das quais **7 também no cadastro** (`fontes`): B051, B059, B061, B064, B071, B072, B073.

- Caso extremo: **B061 não existe em lugar nenhum** — sem pasta, sem entrada no BIBLIO — mas é citado como fonte no cadastro de **~65 termos** (inclui RC-004, RC-009, RC-024, RC-052). É fonte-fantasma de alta propagação: 65 termos alegam lastro numa obra que não está na base.
- B004/B007/B008/B012 constam no BIBLIO como "Aguardando PDF" — anunciadas, não processadas; citação honesta, mas o status "aguardando" deveria ser visível no cadastro (argumento extra para `confianca_fonte`).
- B027/B035 saíram da lista ao incluir `AMOSTRAS/` (falso-positivo inicial — metodologia: conferir os dois diretórios).

**Palestras (P):** 112 datas com pasta; **2 datas citadas em fichas sem pasta**: P2023-12-25 (citada nas variantes `-02` e `-04`, ex.: RC-565, RC-887) e P2026-02-28. Pastas possivelmente nunca criadas ou nomeadas fora do padrão.

Proposta: (1) criar o conceito de **fonte declarada vs. fonte materializada** (B061 é declarada; B031 é materializada); (2) portão no test-suite: toda sigla citada deve ser declarada (BIBLIO) ou materializada (pasta), nunca fantasma; (3) B061: despacho curatorial — de onde veio a sigla? (provável resquício de importação/glossário externo).

## C5. Status e sequência: **íntegros**

Status fora do enum: 0 · códigos RC-001…RC-946 sem gaps (0 furos). ✅ A sequência imutável está sã.

## C6. Títulos duplicados: **4 pares**

`criaturas-ferramenta`, `fenômenos denunciadores do fim`, `rakshasas`, `choque de realidade` — cada um em 2 códigos. Podem ser legítimos (remissivas intencionais, ex. RC-500 Almaior/Alamaior) ou duplicatas reais. Proposta: despacho caso a caso (4 itens, barato) — manter com nota de remissiva ou fundir.

## C7. Bônus metodológico: tipos inconsistentes no cadastro

` TERMS[t][5]` (fontes) é **lista**; `TERMS[t][6]` (relacionados) é **string** `;`-separada; `TERMS[t][7]` é **bool**. Três convenções de tipo numa tupla de 8 — foi o que me derrubou na Frente A (errata A4). É a prova viva do R1 do auditor: *schema implícito cobra pedágio até de quem o conhece*. Qualquer migração (JSON/SQLite) deve começar normalizando isto.

## Síntese da Frente C

O esqueleto é são (C2/C3/C5 zerados — os portões existentes funcionam), mas há **três fraturas**: (1) verdade dupla nas relações sem hierarquia declarada; (2) **fontes-fantasma**, com B061 contaminando ~65 termos; (3) schema implícito com tipos inconsistentes. Recomendação central: **portão "sem-fantasma" no test-suite (Onda 0)** + despacho sobre B061 + declaração da hierarquia `t[6]`×`RELACOES`.

## Errata 2 (Onda 1.3, 12/09/2026)
- **C4 refinado (B061)**: minha afirmação "B061 sem entrada no BIBLIO" estava errada — artefato do meu `grep` (a linha B061 quebra em várias linhas). B061 **é declarada** na BIBLIO (status `minerada`, v3.0, 5 palestras STT). O fantasma real era só-ausência-de-pasta (fechada pela materialização) + a questão aberta v1.0×v3.0 (doc 1.6, questão 1).
