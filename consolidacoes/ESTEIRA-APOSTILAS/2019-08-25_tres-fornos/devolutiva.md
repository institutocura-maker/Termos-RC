# DEVOLUTIVA — RECORTE/FORMATO · Apostila 2019-08-25 · Os Três Fornos Replicadores do Projeto Talm

**Data:** 03/09/2026 · **Branch:** `arena/01a06429-termos-rc` · **Processo:** Esteira de Consolidação sobre apostilas refatoradas (Lote 1)
> **Natureza:** este documento é um **EXEMPLAR DE FORMATO** da devolutiva, produzido sobre 1 apostila
> (2019-08-25) para validação pelo curador **antes** de aplicar o mesmo fluxo ao Lote 1 inteiro.
> **Nenhuma alteração na base** foi feita. Fonte copiada: `fonte.txt` (SHA `faf0d693…`).

---

## 1. O que foi feito (levantamento)
- Copiada a fonte (`fonte.txt`) e computado SHA/bytes.
- Gerado `mapeamento.md` mapeando **24 entidades** nomeadas pela apostila → códigos RC canônicos.
- Cruzado com `dados_termos.py` (fonte do cadastro) e com as fichas `termos/RC-*.md`.
- Registradas **3 divergências (V-1..V-3)** no ledger — todas abertas.

## 2. Principais achados
1. **Apostila já parcialmente integrada.** RC-836 (Awayen) e RC-837 (Awaylengan) foram **criados a partir de
   P2019-08-25** e já a citam. Para esta apostila a esteira é essencialmente **auditoria**, não mineração nova.
2. **Gap de fonte (V-1) — descoberta estrutural.** As fichas **RC-035, RC-499, RC-828** contêm uma seção narrativa
   "## Ampliação — P2019-08-25" afirmando a fonte oral fundadora de 2019, **mas** a lista de fontes em
   `dados_termos.py` desses códigos **não inclui P2019-08-25**. Há, portanto, uma **inconsistência** entre a
   ampliação documentada na ficha e o cadastro (autoridade da fonte). Não resolvida aqui — precisa decisão.
3. **Awaymaion (RC-499)** é descrito na apostila (terceiro forno, 2º a funcionar), mas a fonte mais antiga no
   cadastro é P2021-05-15 — a fonte fundadora de 2019 não está registrada (V-2). Candidato a recebê-la, com citação.
4. **RC-826/834/835** são tratados na apostila sem registro de P2019-08-25 em ficha nem cadastro (V-3).
5. **Sem termos genuinamente novos** — os ~24 referentes casam com RC existentes (decisão G3 respeitada).

## 3. O que proponho (aguardando aprovação)
### A) Formato desta devolutiva (objetivo do recorte)
Validar se a estrutura acima (fonte→mapa→achados→proposta→perguntas) é o padrão a replicar no **Lote 1 inteiro**
(4 apostilas v3.1). Ajustes de formato pedidos aqui são aplicados antes de processar as demais.

### B) Elevação de STATUS
**Nenhuma proposta de elevação** nesta rodada — coerentemente com a decisão G1 (apostila P = auditoria; elevar só
com obra primária B031/B060/B050 + curadoria). A apostila só ajudaria a *confirmar leitura*, nunca a promover sózinha.

### C) Divergências do ledger (V-1..V-3)
Permaneceriam **abertas** nesta rodada de formato. V-1 (ficha Ampliação vs cadastro) é a mais importante e
transcende esta apostila: **recomendo** uma checagem sistemática no Lote 1 — se o padrão se repete, tratamos como
decisão de política (a fonte do cadastro é a autoridade; ampliações narrativas de ficha sem registro no cadastro
devem ser regularizadas OU consideradas meramente editoriais).

---

## 4. Decisões solicitadas ao curador
| # | Pergunta | Opções sugeridas |
|---|---|---|
| Q-formato | **Este formato de devolutiva serve** para replicar no Lote 1? (ajustar: mais/menos seções, tabelas, profundidade) | Sim / ajustar (indicar) |
| Q-V1 | **V-1 (Ampliação na ficha ≠ fonte no cadastro):** o cadastro `dados_termos.py` é a autoridade de fontes? Ampliações de ficha sem registro no cadastro devem ser (a) regularizadas acrescentando a fonte, (b) consideradas apenas editoriais, ou (c) investigadas caso a caso? | a / b / c |
| Q-lote | Após validar o formato, confirmo prosseguir com o **Lote 1 completo** (4 apostilas v3.1) na mesma estrutura `ESTEIRA-APOSTILAS/`? | Sim / revisar antes |
