# Despacho único — expansão controlada da normalização STT

**Data:** 20/10/2026

**Lote:** `uploads_recepcao/stt-lote-2026-10/` — 309 transcrições Markdown

**Estado:** despacho aprovado e executado; as contagens desta página preservam a projeção de despacho. O resultado efetivo está em `diagnostico/RELATORIO-NORMALIZACAO-STT-LOTE-2026-10-20.md`. **Nenhum bruto foi alterado.**

> **Decisão pedida ao Curador:** aprovar, ajustar ou vetar os três blocos de regras abaixo em uma única resposta. Após o despacho, a esteira produzirá somente cópias derivadas identificadas como **transcrição STT normalizada (não verbatim)**, com manifesto SHA-256, registro `antes → depois`, fila de pendências e verificação de idempotência. Os 309 brutos permanecerão byte a byte intactos.

---

## 1. Base da decisão e método de contagem

- Foram relidos os 309 brutos do lote. A contagem abaixo considera **somente o corpo da transcrição depois do frontmatter**; títulos, URLs, datas e demais metadados não entram nas regras.
- Toda ocorrência foi procurada como token/expressão inteira, com fronteiras Unicode; não há troca de fragmentos dentro de outra palavra.
- Foram conferidas a forma canônica e a evidência explícita em `base/canonico.json` e/ou nas fichas citadas. A lista de formas da ficha é prova de grafia, não autorização para inferir automaticamente um alvo pelo título de qualquer ficha.
- As **oito regras lexicais já aprovadas** permanecem fora deste despacho e serão aplicadas: projeção atual de **405 trocas em 87/309 arquivos** (`Thoth` 136; `Vishnu` 104; `Trimurti` 57; `Tirthankaras` 35; `Mohen So` 31; `Tikun` 23; `Pashupati` 10; `Anunnaki` 9).
- A regra já aprovada `Sofia`/`Sofio` → `Sophia` continua **contextual**. Há 959 candidatos em 78 arquivos; com a trava previamente publicada (no mesmo parágrafo, ao menos uma âncora RC como `Javé`, `Jesus`, `Trimurti`, `Vishnu`, `Brahma`, `avatar`, `Cristo Cósmico` ou `reintegração`), **502** ficam aptos e **457** permanecem na fila, sem alteração.

Os números são estimativas de aplicação, não edição já realizada.

---

## 2. Bloco D1 — novas equivalências lexicais recomendadas

**Recomendação:** aprovar integralmente. As formas de origem são foneticamente marcadas ou raras no português corrente e possuem resolução explícita na Base. Aplicação global no **corpo** dos derivados, preservando maiúscula inicial quando houver.

| ID | DE → PARA | Censo (ocorrências / arquivos) | Âncora interna e fundamento |
|---|---|---:|---|
| D1.01 | `Rockman` → **Hochmah** | 67 / 17 | RC-565: decisão canônica: **Hochmah**, nunca `Rockman/Rockma`; RC-009 confirma o erro de STT. |
| D1.02 | `UERD`, `Werd`, `erd` → **Wyrd** | 133 / 22 | RC-658 e RC-560 unificam as formas STT da teia sob **Wyrd**; a decisão curatorial registra “somente Wyrd”. Não inclui `Urdre`, que é mantido. |
| D1.03 | `ticum` → **Tikun** | 38 / 14 | RC-514, inclusive a anotação explícita `ticum/tikum` como STT. |
| D1.04 | `Javer` → **Javé** | 16 / 13 | RC-001 identifica a forma em falas sobre Javé; RC-040 registra `Javer` como degradação STT do nome. |
| D1.05 | `Sávina` → **Savna** | 14 / 8 | RC-102 relaciona explicitamente `Sávina` e outras captações STT a **Savna**. |
| D1.06 | `vaicunta` → **Vaikuntha** | 9 / 4 | RC-414 identifica expressamente `vaicunta` como STT de **Vaikuntha**. |
| D1.07 | `rabarata`, `Marra Barata` → **Mahabharata** | 18 / 14 | RC-593 registra `Marrabarata/rabarata` como STT de **Mahabharata**. |
| D1.08 | `Morus` → **Moros** | 6 / 4 | RC-454 e RC-533 registram `Moros/Morus` como a mesma forma. Não se aplica a `Morrensor`/correlatos. |
| D1.09 | `Viaza` → **Vyasa** | 5 / 2 | RC-585 registra expressamente `Viaza` como STT de **Vyasa**. Não inclui o verbo comum `viaja`. |
| D1.10 | `Silênio` → **Sileno** | 5 / 3 | RC-228: `Sileno/Silênio = Sileno`. |
| D1.11 | `Horlogue` → **Orlog** | 3 / 2 | RC-658 documenta `horlog` como captação STT de **Orlog**; os três casos do lote estão no mesmo uso onomástico. |
| D1.12 | `Aia` → **Aya**; `Aie` → **Aye** | 3 / 2 | RC-834 e RC-835 classificam ambas como corruptelas STT e mandam preferir as grafias canônicas. |
| D1.13 | `Chiva` → **Shiva** | 3 / 3 | RC-102 e RC-135 explicitam `Chiva` como forma STT de **Shiva**. |
| D1.14 | `Pimeteu` → **Epimeteu** | 3 / 3 | Glossário canônico, linha de **Epimeteu**; alvo ancorado em RC-302. A forma paralela `Efestos` continua bloqueada (ver §4). |
| D1.15 | `riches` → **Rishis** | 2 / 1 | RC-586: “Grafia preferida: Rishis. STT: riches.” |
| D1.16 | `Fanis` → **Phanes** | 2 / 2 | RC-565 registra `funis/Fanis` como STT de **Phanes**; RC-282 ancora o termo. |

**Impacto incremental de D1:** **327 substituições candidatas** em **81 arquivos** (a soma por linha pode contar o mesmo arquivo mais de uma vez).

---

## 3. Bloco D2 — novas equivalências fortes, mas com trava de contexto

**Recomendação:** aprovar com as condições textuais abaixo. A troca só ocorre quando a forma e pelo menos uma âncora aparecem no mesmo parágrafo da transcrição. Caso contrário, o evento entra no relatório `pendentes-contexto`, sem modificação.

| ID | DE → PARA | Censo bruto | Trava de contexto proposta | Fundamentação |
|---|---|---:|---|---|
| D2.01 | `Elio` → **Enlil** | 14 / 5 | `Enki`, `Anunnaki`, `Anu`, `Ninmah`, `Ninhursag`, `FOXP2` ou `Babilônia` | RC-487 informa explicitamente: bruto `Elio` para **Enlil**. |
| D2.02 | `Enke`, `Enck`, `Enk` → **Enki** | 22 / 12 | `Enlil`, `Anunnaki`, `Anu`, `Ninmah`, `Ninhursag`, `FOXP2` ou `Livro Perdido` | RC-487 registra `enque` por **Enki**. A trava evita converter abreviação truncada fora do ciclo anunnaki. |
| D2.03 | `Vigno`, `Vigna`, `Virgo`, `Vísgno` → **Vishnu** | 39 / 19 | `Shiva`, `Brahma`, `Trimurti`, `Sophia`, `avatar`, `Krishna`, `Mavatna` ou `Javé` | RC-135 documenta `virgno/virgino/Vno` e outras captações do mesmo nome. Formas comuns como `Vista` e `Virgem` não entram. |
| D2.04 | `Arapa` → **Harapa** | 8 / 5 | `Mohenjo-Daro`, `Indo`, `Paquistão`, `dravidianos` ou `Kumari` | RC-329 usa **Harapa** no mesmo conjunto histórico. A trava exclui eventual nome próprio alheio. |
| D2.05 | `Buloca` → **Bhuloka** | 4 / 4 | `Bramaloca`, `Brahmaloka`, `universo material`, `universo biológico` ou `loka` | RC-033 fixa **Bhuloka**. Os quatro casos observados são pares de Bramaloca/Buloca. |
| D2.06 | `Anã` → **Ananque** | 5 / 4 | `Moros`, `Moiras`, `Nornes`, `necessidades`, `código` ou `Sophia` | RC-777 declara `Anã` grafia antiga superada e consagra **Ananque**; a trava evita o substantivo comum. |

**Impacto máximo de D2:** **92 candidatos** em **40 arquivos**, sujeito às travas. A contagem efetiva será divulgada regra a regra no relatório da execução.

---

## 4. Bloco D3 — preservar e relatar; não normalizar agora

Estas formas foram encontradas e **não** devem ser convertidas por este despacho. A tabela é parte da guarda contra falsos positivos; elas aparecerão consolidadas no relatório final, sem revisão arquivo a arquivo.

| Forma(s) preservada(s) | Censo | Por que fica bloqueada |
|---|---:|---|
| `Morrenso`, `Morrensor`, `Morrenson` | 41 / 15 | Há colisão real: RC-454 registra famílias próximas para **Morren So**, mas RC-772 também registra `morrensor` como captação de **Morlens**; outros trechos usam **Moros**. Não há regra global segura. |
| `Luzbel` | 36 / 13 | Pode exigir **Yel Luzbel** ou **Lúcifer** conforme o paralelo; RC-078/RC-142 não autorizam uma troca cega. |
| `Brama`, `Brahman` | 24 / 17 | As formas têm estatutos e referentes distintos no próprio acervo; não reduzir a **Brahma**. |
| `Temes`, `Tênis` | 30 / 10 | Há referências a **Têmis**, mas também há, por exemplo, “Tênis Clube Paulista”; não é substituição lexical global. |
| `Deus` | 2.433 / 203 | Nunca converter para **Zeus**: trata-se de palavra portuguesa comum, apesar de haver paralelo grego em contexto específico. |
| `viaja` | 3 / 3 | Verbo comum; só `Viaza` entra em D1.09. |
| `Vista`, `Virgem` e demais grafias comuns próximas de Vishnu | 180+ | Não usar proximidade fonética como prova; permanecem fora de D2.03. |
| `Urdre`, `Vivendre`, `Scud` e demais componentes das Nornes | 29 / 12 | RC-658 manda manter a distinção dos componentes; não os fundir em **Wyrd**. |

Também ficam fora por já integrarem o conjunto previamente autorizado: `Pachupati` → **Pashupati** e `Tirtankaras` → **Tirthankaras**. Não são rediscutidos aqui.

---

## 5. Forma concisa do despacho

Uma única resposta pode autorizar a próxima fase. Exemplos:

- **`Aprovo D1 e D2; mantenha D3 preservado.`** — recomendação técnica.
- **`Aprovo somente D1; D2 fica na fila.`**
- **`Aprovo D1, D2 exceto D2.03 e D2.06; mantenha D3.`**
- **`Vetado D1.xx`** ou indicar uma alteração de alvo/regra.

**Despacho recebido:** `Aprovo D1 e D2; mantenha D3 preservado.` A execução foi então realizada uma única vez sobre o lote inteiro, sem solicitar confirmação por arquivo; consultar o relatório final para o censo aplicado e os manifestos.

---

## 6. Salvaguardas já fixadas para a execução posterior

1. Copiar cada bruto para uma árvore derivada nova; jamais sobrescrever `uploads_recepcao/stt-lote-2026-10/`.
2. Alterar apenas o corpo posterior ao frontmatter; preservar metadados e URLs literalmente.
3. Registrar cada substituição com regra, arquivo, ocorrência, linha/parágrafo, excerto antes/depois e SHA-256 de origem/derivado.
4. Produzir manifestos de 309 fontes e 309 derivados, censo por regra, lista de pendências D2/D3 e verificação de idempotência.
5. Falhar de modo seguro se a fonte mudar, se uma regra atingir texto fora do corpo ou se o censo não reproduzir o manifesto.
