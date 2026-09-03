# DIVERGENCE LEDGER — F022 · 22-GLOSSÁRIO

**Processo:** Esteira de Consolidação · **Fase:** LEVANTAMENTO (03/09/2026) · **Branch:** `arena/01a06429-termos-rc`
**Regra:** divergência **aberta** nunca eleva STATUS nem vira citação. Só é resolvida por **cotejo com
fonte primária** ou decisão do curador.

| # | Item F022 | Afirmação no 22-GLOSSÁRIO (local) | Contradiz / ambiguidade c/ base | Origem primária presumida | Análise | Decisão proposta | Status |
|---|---|---|---|---|---|---|---|
| V1 | Brajna (nome pré-queda de Brahma) | Parte 2 (L160), Parte 5 | Base usa **Prabrajna** (RC-152); tríade canônica Prabrajna/Savna/Mavatna (RC-152/RC-102/RC-135); ver RC-037 Brahma(Brajna), RC-310/RC-410 | obra B031 e diagramas | Grafia divergente de mesmo referente; provável simplificação do refatorado | registrar como `variação`/`sinônimo` (Brajna→Prabrajna), não termo novo | aberto |
| V2 | Cronologia: unidade temporal | Parte 4 (vários) | "Mil Milhões de Anos" e contradição mil×milhões (599 mil vs 599 milhões; Zeus 300 "mil milhões" vs 300 "mil") | corpus primário (B/P) | Erro de refatoração/edição; cronologia numérica não-confiável | **rejeitar** adoção de datas; usar só ordem relativa; conferir número a número | aberto |
| V3 | "Prima Sai" | Parte 4, Parte 5 | Sem correspondente na base; base tem Sai Baba (RC-797, RC-801) | P2012-02-19 (P), B031 (ref.) | **RESOLVIDA (03/09):** "Prima Sai" = **Prem Sai** (STT fonético), 3ª manifestação da linhagem de Shiva (Shirdi → Sathya Sai Baba → Prem Sai); já **absorvida em RC-801** (seção Ampliação P2012-02-19); não gera código novo; grafia registrada na ficha RC-801 | **resolvida** — nenhum termo novo; enriquecida ficha RC-801 | resolvida |
| V4 | Enquadramento Universo Antimaterial | Parte 1 verbete "Universo Antimaterial" | ≈ Brahmaloka (RC-038) e/ou Universo Paralelo (RC-108); base RC-107 = Universo Material(Bhuloka) | B031 etc. | Terminologia ambígua entre antimaterial/paralelo | padronizar sinônimos/variação entre RC-038/RC-108 | aberto |
| V5 | Sophia — vínculo com Jesus | Parte 5 | Glossário: Sophia=avatar de Mohen So/Vishnu; "pai biológico" de Jesus por inseminação (RC-009, RC-072) | B016/B042/B014 | Conferir genealogia Sophia→Mohen So→Vishnu→Jesus | cotejo primário; possivelmente só reforça RC-009 | aberto |
| V6 | Trimurti "triunvirato demo" | Parte 5 | RC-104 Trimurti (Brahma/Vishnu/Shiva) | B031/B060 | Termo "triunvirato demo" atípico | cotejar; manter como nota, não alterar definição sem fonte | aberto |
| V7 | Val El ↔ Yel Am → Yel Liam | Partes 2/3/5 | Descrições ambíguas sobre quem é Val El/Val Ellam vs Yel Am/Yel Liam; fusão de códigos | B061/B031 | Redundância e duplicata RC-138/RC-140; narrativa confusa no refatorado | cotejar; consolidar Val/Yel (D3/D4) | aberto |
| V8 | Exilados de Capela — origem do termo | Parte 4 | Glossário: termo surge com "A Caminho da Luz" (Chico Xavier/Emmanuel) | obra de Chico Xavier (externo) | Nota histórica/externa, não da RC | registrar como nota contextual em RC-007; não elevar status | aberto |
| V9 | Lúcifer na Vulgata/São Jerônimo | Parte 4 | Glossário atribui a São Jerônimo o nome Lúcifer (séc. IV) | histórico externo | Afirmação de história religiosa; verificar veracidade | nota de contexto (RC-078), não é dado RC | aberto |
| V10 | Nave "maior" (Espherian) vs "mais requintada" (Asphezian) | Parte 1 vs Parte 4 | RC-057 (Espherian), RC-025 (Asphezian) | B031 | Descrições levemente inconsistentes entre partes | cotejar; harmonizar glosas | aberto |

---

## Resumo do levantamento

- **137 verbetes** da Parte 1 → quase todos casam com RC existente (bloco alfabético RC-001–152).
- **Duplicatas de nome-base evidenciadas:** D1–D4 (Conselho dos Cinco, Val Aten, Yel Liam, Jan Val Ellam) + reforço de D5–D9.
- **Divergências registradas:** V1–V10 (nenhuma auto-resolvida; todas `aberto`, aguardando cotejo primário).
- **Termos potencialmente "novos" no refatorado:** nenhum se mostrou genuinamente novo; todos são variações/duplicatas
  de RC existentes → **não recomendamos criar código novo a partir do F022** (princípio anti-duplicação + anti-pseudoconfirmação).

*Aguardando devolutiva do curador para avançar à fase de APLICAÇÃO (elevações seguras + merges D1–D4, mediante cotejo primário).*

---

## REGISTRO DE APLICAÇÃO — merges D1–D4 (03/09/2026, após aprovação do curador)

Referências máximas confirmadas pelo curador: **B031** (maioria dos termos), **B060** (personagens), **B050** (períodos/datas/eras).

| Merge | Ação | Estado |
|---|---|---|
| D1 Conselho dos Cinco | `RC-501 --variação--> RC-043` (canônico RC-043/B031) | ✅ aplicado |
| D2 Val Aten | `RC-502 --variação--> RC-115` (canônico RC-115/B031) | ✅ aplicado |
| D3 Yel Liam | `RC-140 --variação--> RC-138` (Yel Am/Yel Liam) | ✅ aplicado |
| D4 Jan Val Ellam/Rogério | relação `RC-071 --variação--> RC-095` **já existia** | ✅ já resolvido na base |

- Nenhum código foi apagado (imutáveis); duplicatas canonizadas por relação de `variação` (padrão casa, cf. RC-071/095 e RC-503/408).
- D5–D9 (Favor Divino, Choque de Realidade, Criaturas-ferramenta, Fenômenos Denunciadores, Val dos Corpos Perdidos) → **adiadas** para etapa de cotejo (Q2 do curador).
- **ELEVAÇÃO DE STATUS: nenhuma aplicada nesta rodada** (Q3) — fica para a fase de cotejo com fontes primárias B031/B060/B050.

**Validação pós-aplicação:** `OK: 926 termos, 1872 relações — dados válidos.`

---

## REGISTRO DE APLICAÇÃO — cotejo B031/B060/B050 (03/09/2026, aprovado pelo curador)

**Referências validadas por equipe avançada da RC + Ellam:** B031 (termos), B060 (personagens), B050 (eras/datas).

### Merges D5–D9
| Merge | Ação | Estado |
|---|---|---|
| D5 Favor Divino (RC-063 × RC-332) | par deliberado obra-título × conceito (documentado na ficha RC-332) | ✅ **sem merge** |
| D6 Choque de Realidade | `RC-867 --variação--> RC-898` | ✅ aplicado |
| D7 Criaturas-ferramenta | `RC-449 --variação--> RC-164` (conteúdo B057/B058 preservado em RC-449) | ✅ aplicado |
| D8 Fenômenos Denunciadores do Fim | `RC-203 --variação--> RC-314` | ✅ aplicado |
| D9 Val dos Corpos Perdidos | `RC-493 --variação--> RC-133` | ✅ aplicado |

### Elevação de STATUS (Opção B)
Conjunto elegível = `provisório + ficha=True + cita ≥1 obra revisada (B031/B060/B050)` = **97 termos**.
- **22 → `verificado`** (🟢): citam **≥2** obras revisadas (corroboração cruzada entre volumes curados).
  Lista: RC-001, 009, 036, 037, 049, 071, 074, 078, 087, 092, 094, 102, 104, 106, 107, 135, 142, 145, 299, 395, 396, 398.
- **75 → `em análise`** (🟠): citam 1 obra revisada.
- Tabela-mestra + 96 fichas atualizadas (RC-396 é ficha-stub sem cabeçalho de Status — atualizada só na tabela-mestra).
- Fichas sem alteração de conteúdo; apenas campo **Status** promovido.
- **Validator pós:** `OK: 926 termos, 1876 relações`. Distribuição: verificado 22 · em análise 75 · provisório 433 · candidato 396.
