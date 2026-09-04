# DIVERGENCE LEDGER — F029 · 29-PERSONAGENS DA REVELAÇÃO CÓSMICA

**Data:** 04/09/2026 · **Processo:** Esteira de Consolidação (F029) · **Estado:** ledger ativo — cada entrada marca (aberta | resolvida | não-propagada)

---

## DIVERGÊNCIA D-1 — Linhagem Sai: Shiva × Krishna (RESOLVIDA pelo curador 04/09/2026)

**Status:** ✅ **RESOLVIDA — Sai ancorada em Shiva (RC-102). Leitura do 29 não propagada.**

**Situação (verificada byte a byte):**
- **B060 (referência/base):** linhagem Sai **sob SHIVA (Savna)** → avatares: *Prima Sai*, Sai Baba de Shirdi/Shirdi Sai Baba (1838?–1918), **Sathya Sai Baba (1926–2011, Sathyanarayana Raju)**. Base atual: `RC-927/928/929 -encarnação-de-> RC-102 Shiva` (B060/B031).
- **29-PERSONAGENS v1.4:** mesma linhagem **sob KRISHNA** → Baba de Shirdi, Sai Baba (1838?–1918), **Prema Sai (atual encarnação)**. **OMITE Sathya Sai Baba.** Oscila Prima/Prema internamente.

**Decisão do curador (04/09/2026):**
- **MANTER** RC-927/928/929 ancorados em **RC-102 Shiva** (coerente com B060/B031 e com o trabalho já commitado).
- Registrar a leitura do 29 (Sai sob Krishna) como **divergência de terceiros — não propagada** à base.
- Não criar alteração estrutural nas relações Sai decorrentes deste documento.

**Nota técnica:** a leitura "Sai sob Krishna" do 29 guarda semelhança com uma nota já existente na ficha RC-414 (Krishna): "Krishna foi o único avatar que começou a produzir avatares dele mesmo... Sai Baba [Sathya Sai Baba] como 'continuação' — leitura do autor". Ou seja, há nas **próprias fontes RC** um fio que liga Krishna a Sathya Sai como *avatares produzidos por Krishna*, distinto da ancoragem de *encarnação da consciência Shiva*. Isso é registrado, **não** auto-resolvido.

---

## DIVERGÊNCIA D-1_krishna — Reancoragem de Krishna: aresta estrutural Shiva + aresta teológica Vishnu (RESOLVIDA pelo curador 04/09/2026)

**Status:** ✅ **RESOLVIDA (decisão) — aplicação à base PENDENTE (aguarda fase APLICACAO). Base NÃO alterada nesta fase (LEVANTAMENTO / `altera_base=false`).**

**Decisão do curador (04/09/2026):** bifurcar a ancoragem de Krishna (RC-414) em **dois planos**, separando a **linhagem estrutural** (origem/criação) da **atribuição teológico-mitológica** (registro hindu):

1. **ARESTA ESTRUTURAL — NOVA (criação):** `RC-414 --criado-por--> RC-102 (Shiva)` · fonte **P2021-04-10**.
2. **ARESTA TEOLÓGICA — RE-TIPADA:** `RC-414 --atribuído-em-teologia-comparada-a--> RC-135 (Vishnu)` · fonte **B051** (mantém a fonte primária que registra a atribuição de Krishna como avatar de Vishnu **no plano do mito/teologia**).
3. **Sem fusão com RC-425** (pretenso Keshava) e sem criar rótulo/código novo: reusa-se o predicado já existente na base `atribuído-em-teologia-comparada-a` (usado p.ex. `RC-486 --atribuído-em-teologia-comparada-a--> RC-325` [P2024-11-09]).
4. **Fontes:** incluir `P2021-04-10` na lista de fontes de RC-414 (a ficha RC-102 já o possui). Ficha RC-414 deve receber ampliação com a citação byte-exata abaixo.

**Fundamento — evidência byte-exata (verificada):**
- **Pérola `PER-2021-04-10-005`** (dossiê `ciclos/P2021-04-10/DOSSIE-RAG_P2021-04-10.md`, U0006, chars 30662–30883, status `candidata`, cruza RC-414), fala de Shiva:
  > «Então assim, Shiv, ele me disse que ele criou Krishna e Saibaba porque estes olhavam pros seres humanos com o carinho, a ternura que ele enquanto Shiva à moda desses três tipos de consciência, ele não conseguia olhar, né?»
- Corrobora a tese de linhagem por Shiva o próprio corpo das fichas RC: P2024-03-02 (Krishna "pendeu pro lado de Shiva"), P2022-07-16 (Mahâbhârata = "definitiva transferência do poder trimurtiano ancestral" — já fonte de RC-414), P2021-04-10-005 acima.
- O vínculo com **Vishnu** permanece registrado (B051, RC-135) — como atribuição **teológica/comparativa do mito**, não como origem estrutural.

**Motivo de re-tipar (não apenas adicionar):** a aresta atual `RC-414 --é-um--> RC-135` (Vishnu) codifica o vínculo de Vishnu como *linhagem real*; com a decisão, Vishnu deixa de ser a origem estrutural de Krishna e passa a ser leitura teológica. Re-tipar para `atribuído-em-teologia-comparada-a` preserva o registro e isola o plano, permitindo que o filtro RAG separe "linhagem real" (criado-por Shiva) de "embalagem cultural" (Vishnu).

**PATCH DE APLICACAO (pronto, NÃO aplicado):** quando o ciclo transitar para **APLICACAO** (`altera_base=true`):
- `ferramentas/dados_termos.py` `RELACOES`: linha 1453 `("RC-414","é-um","RC-135","B051")` → `("RC-414","atribuído-em-teologia-comparada-a","RC-135","B051")`; adicionar `("RC-414","criado-por","RC-102","P2021-04-10")`.
- `ferramentas/dados_termos.py` `TERMOS` (RC-414, linha 547): acrescentar `'P2021-04-10'` à lista de fontes.
- `termos/RC-414-*.md`: adicionar seção `## Ampliação — P2021-04-10` com a citação byte-exata acima e a referência a RC-102.

---

## DIVERGÊNCIA D-2 — Krishna "predominância Shiva" vs RC-414 "avatar de Vishnu/Shiva"
**Status:** ✅ **RESOLVIDA** — subsumida à **D-1_krishna** (decisão 04/09/2026): a "predominância Shiva" / DNA-trimurti vira **aresta estrutural `criado-por Shiva`**; o vínculo "avatar de Vishnu" vira **atribuição teológico-mitológica** (`atribuído-em-teologia-comparada-a Vishnu`). Leitura do 29 não é propagada como autoridade; o patch (acima) aguarda fase APLICACAO.

## DIVERGÊNCIA D-3 — Kalil Kadmon (enriquecimento, não contradição)
**Status:** aberta (baixa). 29: Kalil Kadmon = "Olimpiano filho de Zeus e Têmis, genética da liberdade encomendada por Moros através das Moiras" + "ver Pandora". Base RC-299 já consolida "Kalil Kadmon = nome demo de Pandora"; RC-815 Têmis co-clonadora; Moros/Moiras presentes. Verificar se RC-299 cita Moros/Moiras/Têmis; se não, ampliar com citação (pós-cotejo).

## DIVERGÊNCIA D-4 — Jesus/Sophia/Issa no elenco de Vishnu
**Status:** aberta (baixa). Consistente com base (Sophia=RC-009 é-um Vishnu RC-135; Jesus RC-072). "Issa" como item de Vishnu a conferir (RC-253/254?).

## DIVERGÊNCIA D-5 — Cadeias de reencarnação de figuras históricas (conteúdo novo)
**Status:** aberta — aguarda **cotejo com fonte primária** (decisão G1: fonte P de terceiros não eleva/não cria sem cotejo). Várias sem ficha (Akhenaton, Chico Xavier, Blavatsky, Shelley, Hercílio Maes, Pestalozzi, Waldemar…); várias históricas sem nome (não criar). Ver PARTE D do `mapeamento.md`.

## DIVERGÊNCIA D-6 — Variações/omissões do próprio 29 vs B060
**Status:** registrada. O 29 **omite Sathya Sai Baba** (presente no B060) e corrige/desloca grafias (Viracocha "Quechua" vs "Inca" do B060; Zeus "filho de Cronos e Reis"). **A base segue B060/B031** onde divergir (autoridade: obras/palestras primárias).
