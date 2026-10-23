# DESPACHO — ESTEIRA DE CONSOLIDAÇÃO DA BASE TERMINOLÓGICA RC (rascunho p/ aprovação do curador)

**Data:** 03/09/2026 · **Branch:** `arena/01a06429-termos-rc`
**Status:** RASCUNHO para revisão do curador — nada executado ainda.

> Este documento operacionaliza a proposta de "revisar e consolidar a KB" usando uma **nova
> categoria de fonte** (material refatorado/revisado derivado de Ellam). É gêmeo do
> `DIAGNOSTICO-BASELINE-KB-2026-09-03.md` e do `ANALISE-PROPOSTA-CONSOLIDACAO-E-22-GLOSSARIO-2026-09-03.md`.

---

## 1. Princípios (não negociáveis)

1. **Fonte refatorada ≠ fonte primária.** Todo dado do refatorado deve ser **cotejado** com uma
   fonte primária (B/P) antes de alterar a base. Sem âncora primária → **divergência em aberto**.
2. **Anti-fabricação.** Nada de inventar citação, número, data, grafia ou termo. Se não houver
   fonte, marca `[REVISAR]` / `[TEXTO INCOMPLETO]`.
3. **Anti-pseudoconfirmação.** *Coincidência entre o refatorado e a base que derivam da mesma
   fonte raiz NÃO é corroboração independente.* Só eleva STATUS a corroboração por fonte
   independente ou por revisão explícita do curador.
4. **Anti-duplicação.** Antes de criar QUALQUER código novo, checar nome-base + sinônimos + `variação`
   contra os 926 termos.
5. **Códigos imutáveis.** Não reutilizar RC; duplicatas resolvem-se por *alias/merge documentado*,
   nunca apagando.

---

## 2. Nova categoria de fonte — "Família F"

| Prefixo | Significado | Exemplo |
|---|---|---|
| `B###` | obra primária | B031 |
| `P####-##-##` | palestra (STT) | P2024-03-17 |
| `ART-*` | artigo | ART-2025-08-01 |
| **`F###`** | **documento refatorado/revisado (novo)** | F022 → 22-GLOSSÁRIO |

Registro por documento (como as obras): `F022 · 22-GLOSSÁRIO · refatorado (origem Ellam) ·
SHA 8968eab…792a · 76.695 B`. Cada afirmação carrega `F022` + localização (parte/item) + campo
`origem_primaria_presumida`.

---

## 3. Estrutura de um ciclo de consolidação

`consolidacoes/F022_22-glossario/`
```
ciclo.toml          # metadata: sigla_fonte=F022, sha, data, escopo
fonte.txt           # cópia do refatorado (byte-a-byte)  [F022]
mapeamento.md       # verbete/item  →  código(s) RC  →  decisão (já existente/variação/novo?/duplicata)
divergencias.md     # DIVERGENCE LEDGER (tabela abaixo)
ampliacoes.md       # citações/adendos validados p/ inserir nas fichas
devolutiva.md       # resumo p/ aprovação do curador
```

### 3.1 Divergence Ledger (formato)
```markdown
| # | Item F022 | Afirmação (local) | Contradiz/ambíguo c/ | Origem primária presumida | Análise | Decisão | Status |
```
Status: `aberto → em_estudo → resolvida | rejeitada | arquivada`. **Divergência aberta nunca
eleva STATUS nem vira citação.**

---

## 4. Regras de elevação de STATUS (dois eixos → 4 níveis atuais)

Manter os 4 níveis legíveis por ferramentas (`candidato/provisório/em análise/verificado`), mas
avaliar por **2 eixos**:

| Elevação | Requisito mínimo |
|---|---|
| candidato → provisório | ficha + ≥1 fonte primária ancorada (B com ref, ou P com citação) |
| provisório → em análise | ≥2 fontes **independentes** convergentes **OU** 1 primária + revisão do curador |
| em análise → verificado | curadoria explícita + referência primária obra+capítulo/página |

**Elevação via F (refatorado) — só nos casos:** (a) F aponta e *reforça* item já com primária, e a
F deriva de **fonte raiz distinta**; ou (b) F explicita divergência já conhecida e ela foi
resolvida por cotejo primário. Nunca por simples concordância F↔base do mesmo corpus.

---

## 5. Fluxo típico do piloto (22-GLOSSÁRIO)

1. **Carregar fonte:** copiar `uploads_recepcao/22-GLOSSÁRIO.txt` → `consolidacoes/F022.../fonte.txt`
   (SHA confere); registrar `F022`.
2. **Mapear:** 137 verbetes da Parte 1 (+ Partes 2–5) → código(s) RC. Preencher `mapeamento.md`.
3. **Anti-duplicar:** conferir os 6 grupos de nome-base do baseline; recomendar merge/alias.
4. **Divergir:** registrar as do §4 da análise (Brajna/Prabrajna; unidades mil×milhões; Prima Sai;
   Yel Liam; contagens) no ledger, com origem primária presumida.
5. **Ampliar com segurança:** onde F **reforça** conteúdo já primário e não conflita → inserir
   seção `## Ampliação — F022` na ficha existente (sem elevar status ainda, salvo regra §4).
6. **Devolutiva ao curador** antes de aplicar elevações e merges.
7. **Aplicar** após aprovação; registrar Δ; regenerar espelhos; atualizar docs.

---

## 6. Critérios de aproveitamento PARCIAL

Um item do refatorado pode ser aproveitado **parcialmente** se:
- a **parte aproveitada** tem ancoragem primária (o restante, sem âncora, vai ao ledger);
- a parte aproveitada **não** contradiz fonte primária já catalogada;
- **erros óbvios** (ex.: unidades) são excluídos do aproveitamento e apenas registrados;
- **variações de grafia** entram como `variação`/`sinônimo` (não como termo novo).

---

## 7. Não escopo desta esteira (p/ evitar sobreposição)

- Não substitui a **Esteira Leve** (citação byte-exata de palestras novas).
- Não cria fichas novas por capricho a partir de refatorado duplicado.
- Não altera `dados_termos.py` sem passar pela devolutiva e sem revalidar (`python3 ferramentas/dados_termos.py`).

---

## 8. Produtos mínimos ao final do piloto

- `mapeamento.md` com % de sobreposição e lista de "sem correspondente".
- `divergencias.md` com ledger populado.
- Lista de **elevações seguras** e de **merges de duplicata** propostos (aguardando curador).
- Se aprovado: aplicação, regeneração de espelhos, atualização de `DIAGNOSTICO-BASELINE-KB` e docs.

---

*Aguardando aprovação do curador para iniciar o piloto F022 (itens 1–4 do fluxo = levantamento,
não alteram a base; itens 5–7 alteram a base e aguardam devolutiva).*
