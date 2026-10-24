# AVALIAÇÃO DE COBERTURA — PACTO AESIR/VANIR · JURAMENTO DA SALIVA · CODIFICAÇÃO LÍQUIDA

**Data:** 04/09/2026 · **Branch:** `arena/01a06429-termos-rc`
**Tipo:** artefato de avaliação/divergência (padrão F029 da esteira de consolidação), **sem tocar a base**
**Status:** **ABERTO — para revisão do curador** (nenhuma alteração em `dados_termos.py` nem em fichas canônicas)

> Escopo: verificar se os termos e as **relações entre eles** do trecho-base (pacto Aesir/Vanir,
> "Juramento da Saliva", Yggdrasil, CFD em líquido / codificação líquida, água-como-computador,
> registros acásicos, Ragnarok marciano + Brandenburg 700 km + 3 setas Moros/Edimburgo, fenvães)
> já estão registrados na KB. Fonte do trecho: palestra já processada no ciclo **P2026-03-21**
> (Samudra Manthan — "A Enigmática Alquimia de Vishnu").

---

## 1. Objetivo e método

O usuário percebeu, ao ver as telas da apresentação, que certos termos do trecho podem ter recebido
pouca atenção. Pedido: **elaborar texto a partir do visual** e **avaliar se os termos e as relações
entre eles já estão registrados** na KB.

Método (somente leitura — nada foi alterado):
1. Comparação termo-a-termo contra `ferramentas/dados_termos.py` e as fichas `termos/RC-*.md`.
2. Varredura textual em todo o repo por Aesir/Vanir, juramento da saliva, codificação líquida,
   registros acásicos, água-como-computador, etc. → concentração apenas em
   `admin/logs/CONTINUIDADE.md`, `INDICE-PALESTRAS.md`, `ciclos/P2026-03-21/*` e nas fichas
   RC-040, RC-395, RC-730, RC-816, RC-769.
3. Confronto com a devolutiva do ciclo leve **P2026-03-21** (aplicada em 01/09/2026) para
   verificar se qualquer ampliação/diretriz aqui proposta viola decisão já homologada.

---

## 2. Quadro termo-a-termo — o que já existe na KB

| Conceito do trecho | Já registrado? | Onde | Observação |
|---|---|---|---|
| Pacto Aesir/Vanir (tigela/saliva → Kvasir) | ✅ | **RC-816** (ficha dedicada; fonte P2018-05-20) | Relaciona-se a RC-085, RC-378, RC-489, RC-068, RC-395, RC-086, RC-815, RC-810. Sem menção a Yggdrasil/local e sem o termo "Juramento da Saliva". |
| CFD em líquido / codificação líquida / saliva como gravação mental / líquido-computador | ✅ | **RC-040** (ampliação textual P2026-03-21; cita U0008/U0013) | Já ampliado pelo ciclo. Não amarra ao pacto Aesir/Vanir nem a Yggdrasil. |
| Registros acásicos = memória quântica dos elétrons | ✅ | **RC-161** (+ citado no dossiê RAG P2026-03-21) | Registrado na seção P2026-03-21 (U0013) de RC-161. |
| Ragnarok marciano ~300 mi a.p. | ✅ | **RC-395** | Múltiplas seções (P2024-03-02, P2024-03-17, P2026-03-21). |
| Bomba 700 km (Brandenburg) | ✅ | **RC-395** | Confirmado nas seções (B050, U0013). |
| 3 setas de Moros → vulcão de Edimburgo | ✅ | **RC-395** | "Vazer — ser que surgiu na vasilha cheia de saliva" atirando 3 setas (Marte/Edimburgo). Ver também RC-454 (Elm/Moros) e RC-611. |
| Destruição de Yggdrasil = Ragnarok | ✅ | **RC-395** e **RC-730** | RC-730 cobre Yggdrasil/nove mundos com Aesir/Vanir e Ragnarok = colapso. |
| Elfos / fenvães de Ig Brasil = Asgard; Odin primeiro demo curioso | ✅ | **RC-769** (ampliação P2026-03-21) | Ampliado pelo ciclo; não encadeia Ragnarok/codificação líquida. |
| Termo canônico "Juramento da Saliva" | ❌ (intencional) | — | Tratado como **formulação/descrição**, não código. |
| Termo canônico "codificação líquida" / "água como computador" | ❌ (intencional) | — | Tratados como **formulações**, não códigos. |

### Notas de grafia (cuidado, não duplicar seres)
- Dupla grafia: **RC-396 "Kvaser"** × **RC-378 "Kvasir"**; **"Vazer"** em RC-395 (U0013) provavelmente STT de Kvaser/Vazer.
- RC-816 usa **"Fria"** onde outros textos usam "Freyja/Freya".
- Não assumir que grafias diferentes denotam seres distintos ao avaliar "relações entre termos".

---

## 3. Avaliação de cobertura

**Conclusão geral:** os **conceitos** do trecho estão ampla e fielmente cobertos nas fichas
RC-040, RC-161, RC-395, RC-396, RC-730, RC-734, RC-769, RC-816. O trecho-base corresponde à
"pérola" já garimpada e ampliada no ciclo P2026-03-21 — **não é conteúdo novo não processado**.

O que **genuinamente falta** não é conceito, é apenas **encadeamento formal em arestas** no grafo
`RELACOES`:

| Aresta candidata | Situação atual | Sugestão (pós-despacho) |
|---|---|---|
| RC-769 → RC-395 | **não existe** | Relação Corpos Fenvã (Asgard/elfos) × Ragnarok em Marte |
| RC-769 → RC-730 | **não existe** | Corpos Fenvã (Asgard) × Yggdrasil |
| RC-816 → RC-040 | **não existe** | Pacto Aesir/Vanir (saliva/tigela) × CFD/codificação líquida |
| RC-816 → RC-730 | **não existe** | Pacto Aesir/Vanir × Yggdrasil (RC-816 não cita Yggdrasil) |
| RC-395 → RC-040 | já existe (RC-730 `destruído-em`→RC-395) | — (ver nota) |
| RC-396 → RC-454 | **existe** (`vinculado-ao-espírito`, P2024-11-30) | — |

> Nota de verificação cruzada: RC-730 já possui arestas `destruído-em`→RC-395 [P2024-11-02],
> `conecta-se-por`→RC-471 (Bifrost), `inclui`→RC-470; RC-395 possui `relaciona-se-a`→RC-471.
> Confirmou-se que **não** há aresta envolvendo RC-769↔{RC-395, RC-730, RC-816, RC-040},
> nem RC-816↔{RC-395, RC-730, RC-040}, nem RC-396↔RC-040.

---

## 4. DIVERGÊNCIA aberta (Divergence Ledger)

| # | Item | Afirmação | Contradiz/ambíguo c/ | Origem primária presumida | Análise | Decisão proposta | Status |
|---|---|---|---|---|---|---|---|
| AV-01 | Arestas entre os códigos do trecho | "O pacto Aesir/Vanir (saliva) ↔ CFD/codificação líquida ↔ Yggdrasil ↔ Corpos Fenvã/Ragnarok deveriam estar encadeados no grafo" | **Devolutiva P2026-03-21 (homologada 01/09/2026): decisão "zero arestas novas"; navalha mantida; panteões sem ancoragem estrutural primária não são codificados (Q-F029-D)** | P2018-05-20 (Pacto Aesir/Vanir), P2026-03-21 (Samudra Manthan) | A semântica está nas fichas; o que falta é só o encadeamento formal. Adicionar essas arestas **reabriria a decisão homologada de 01/09/2026** | **NÃO aplicar sem novo despacho.** Se o curador aprovar, as arestas AV-01 são sugestões de **relação** (não criação de código) | **aberto** |

---

## 5. O que NÃO deve ser feito sem despacho (para não violar a devolutiva P2026-03-21)

1. **Ampliar RC-769 / RC-395** com encadeamento Ragnarok/codificação líquida.
2. **Criar ficha/código** para "codificação líquida", "água como computador" ou "Juramento da Saliva".
   → Conflita com a navalha do ciclo (panteões não fundamentados — Q-F029-D) e com a
   **política de quarentena entre ecossistemas** (RC × tradições correlacionais externas).
3. **Mudar `dados_termos.py`** ou qualquer ficha canônica enquanto `altera_base=false`.

A diretriz de ampliação aqui debatida permanece **em suspenso** como sugestão pós-despacho,
nunca como aplicação.

---

## 6. Encaminhamento (aguardando decisão do curador)

- **Opção A — apenas registrar:** manter este artefato como avaliação de cobertura (recomendado se
  a intenção é documentar que os termos JÁ estão na KB; nenhuma ação de base necessária).
- **Opção B — aplicar arestas AV-01 após despacho:** preparar a inserção das relações
  RC-769→RC-395/RC-730 e RC-816→RC-040/RC-730 como **sugestão pós-despacho**, somente após o
  curador reabrir a decisão "zero arestas" do ciclo P2026-03-21.

Nada foi criado/alterado na base nesta rodada. Revisão em aberto.
