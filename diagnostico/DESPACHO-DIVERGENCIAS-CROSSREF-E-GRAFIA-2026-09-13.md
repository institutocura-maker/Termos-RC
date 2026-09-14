# Despacho — divergências de fonte, códigos duplos e grafia (13/09/2026)

Curador: despacho proferido sobre os três achados registrados na certidão
`diagnostico/CERTIDAO-U47-R1-LOTE4-2026-09-13.md` (lote 4, os 25 Val/Yel).
Escrivão: agente da sessão `arena/01a09ca0-termos-rc`.

---

## 1. Divergência Val Bon × Val Dimon — manter ambas, com etiqueta

> «Sua atitude foi corretíssima ao não escolher e transmitir ambas. *Diretriz:*
> Mantenha a divergência registrada *verbatim* em cada respectiva ficha. Adicione
> uma nota na gaveta `## 6. Histórico Curatorial e Auditoria` de ambas as fichas,
> utilizando a tag `[⚠️ DIVERGÊNCIA INTERNA DA FONTE]`, cruzando os dois verbetes
> para que o leitor humano (ou o LLM) saiba que a contradição pertence à obra
> original (B031) e não a um erro de extração.»

Aplicação:

- **RC-116 (Val Bon)** e **RC-118 (Val Dimon)** recebem a gaveta
  `## 6. Histórico Curatorial e Auditoria`, cada uma com a etiqueta
  `[⚠️ DIVERGÊNCIA INTERNA DA FONTE]` e o cruzamento explícito do verbete alheio,
  com as linhas de cada um (L3926–L3929 e L3939–L3941).
- Nenhuma das duas fichas é alterada no seu conteúdo doutrinário: a contradição
  é da obra e fica registrada como tal.
- A gaveta passa a existir no instrumento
  (`ferramentas/materializar_lote.py`, campo opcional `historico` do lote), de
  modo que qualquer ficha futura possa recebê-la sem remendo à mão.

## 2. Códigos duplos Yel Am (RC-138) × Yel Liam (RC-140) — preservar e cruzar

> «*Diretriz:* Preserve ambos os códigos e não realize fusão de fichas. Eles
> representam estados ontológicos e temporais distintos do mesmo ser (pré e
> pós-fusão com Val El). O que faremos é conectá-los via Cross-Reference. Em
> RC-138, aponte a evolução para RC-140; em RC-140, aponte a origem em RC-138.»

Aplicação:

- Nenhuma fusão, nenhuma lápide, nenhuma aresta nova em `relacoes/` (o
  `relacoes/` segue blindado: aresta só por despacho taxonômico estruturado).
- A conexão é feita **no corpo das fichas**, por remissiva textual explícita:
  RC-138 aponta a evolução → RC-140; RC-140 aponta a origem → RC-138.

## 3. Grafia Eliah/Elieh × Elliah/Ellieh — paridade verbatim absoluta

> «*Diretriz:* O Portão de Paridade Verbatim é absoluto. É terminantemente
> proibido normalizar a grafia. Extraia e cole a palavra exatamente com a grafia
> utilizada no trecho específico da fonte, seja no corpo do texto ou no glossário.
> Onde o livro usar um "L", usamos um; onde usar dois, usamos dois. Registre a
> variação gráfica nos metadados ou na Definição Sintética.»

Aplicação:

- Cada fragmento de citação continua verbatim byte a byte, com a grafia do
  trecho de onde saiu — «Val Eliah»/«Val Elieh» onde a fonte os grafa assim
  (B031 L3255), «Val Elliah»/«Val Ellieh» onde a fonte os grafa com dois
  (B031 L3983 e L3986).
- A variação fica declarada na **Definição Sintética** de RC-121 e de RC-122,
  para que quem ler uma ficha saiba que a outra grafia existe e não é erro.
- Regra geral doravante: **não normalizar grafia, nunca**; registrar a variação.

---

## 4. Lote 5 autorizado

> «*Diretriz:* **APROVADO.** Siga com os 14 termos restantes da B031 (Antlar,
> Antlartes, Astralização dos Biodemos, Atlans, Conselho dos Cinco, Daemon,
> Gron Mion, Ion Crom, Nephilins, Norte Divino, Portlan e Portlon, Val-Ha,
> Viajores, Zeitgeist). Fechar o glossário desta obra de uma única vez consolida
> uma família inteira e limpa a área para os próximos alvos.»

Mantidas as demais condições do despacho anterior
(`DESPACHO-ROTAS-POS-V2-2026-09-13.md`): poço = família B do censo v2, **V
presuntivo revogado** (as 14 nascem 🟡), bloco único quando a fonte for a mesma.
