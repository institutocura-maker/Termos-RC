# T2 — Exceções de `Termos Relacionados` (45 seções não conformes)

| Campo | Valor |
|---|---|
| Fase | T2 — ação 2 (levantamento, **somente leitura**) |
| Data | 2026-10-25 |
| Diagnóstico de origem | `admin/logs/STATUS-HANDOFF-T1-T2.md` |
| Escopo | `termos/*.md` — 826 fichas |
| Artefato complementar | `admin/logs/T2-MAPEAMENTO-RELACOES.csv` (998 tipos brutos; matriz De-Para preenchida conforme o Anexo A) |
| Natureza | Registro descritivo. **Nenhuma ficha, tabela, relação ou citação foi alterada, normalizada ou reescrita.** |

## 1. Síntese quantitativa

| Métrica | Valor |
|---|---|
| Fichas Markdown lidas | 826 |
| Seções `## Termos Relacionados` | 821 |
| Seções conformes (1ª linha = cabeçalho padrão Termo / Código / Tipo de relação) | 776 |
| Seções não conformes (escopo deste log) | **45** |
| Fichas sem a seção (fora das 45 exceções) | 5 |
| Linhas de relação nas 776 seções conformes | 7.761 |
| Tipos brutos deduplicados exportados no CSV | **998** |
| Soma da coluna `ocorrencias` do CSV | 7.761 |
| SHA-256 da lista bruta ordenada (recalculado) | `43ad4e8083ce83d5facb39b082488031625d81dd92e827f56938fdafa7d05213` — idêntico ao handoff T1 |

As 5 fichas sem seção `## Termos Relacionados` são: `RC-935-cognicao.md`, `RC-937-monada.md`, `RC-939-samkhya.md`, `RC-940-samsara.md`, `RC-941-hipocampo.md`. Não entram no rol das 45 exceções porque não há seção a classificar; ficam registradas apenas para evitar divergência de contagem em auditorias futuras.

## 2. Critério de conformidade e método de extração

1. Cada seção vai da linha `## Termos Relacionados` até o próximo cabeçalho `##` (ou EOF).
2. **Conforme** = a primeira linha não vazia da seção é exatamente `| Termo | Código | Tipo de relação |`. São 776 seções.
3. **Não conforme** = a primeira linha não vazia é qualquer outra estrutura. São 45 seções, detalhadas abaixo.
4. Os 998 tipos brutos do CSV foram extraídos **apenas** da 3ª coluna das linhas de relação das 776 seções conformes (espaços externos removidos, sem qualquer outra limpeza). A deduplicação e a ordenação alfabética insensível a maiúsculas/minúsculas reproduzem exatamente o hash do handoff T1.
5. As 39 seções não conformes que também contêm uma tabela padrão embutida somam 123 linhas de relação **não contabilizadas** nas 7.761 linhas e, portanto, não participam dos 998 tipos do CSV. Estão inventariadas aqui porque precisarão de deliberação própria na etapa de implementação.
6. `ocorrencias` = número de linhas de relação das 776 seções conformes cuja 3ª coluna é igual ao `tipo_bruto`. Inclui as 17 linhas de 4 colunas descritas na seção 7 (3ª coluna = `—`).

## 3. Classes de não conformidade

| Classe | Seções | Estrutura atual | Risco semântico na futura migração |
|---|---|---|---|
| **A** | 6 | Tabela de 3 colunas Termo / Código / Estado na malha (27 linhas) | A 3ª coluna **não é um tipo de relação**: é um estado da aresta/arquivo na malha. Só 2 dos 3 valores distintos constam do CSV; convertê-la em `Relação` destruiria a informação de topologia. |
| **B** | 1 | Tabela de 2 colunas Código / Relação (7 linhas) + tabela padrão (8 linhas) + bloco de notas de processo | Relações em prosa livre, sem coluna `Termo`; 5 dos 7 rótulos **não constam** do CSV. Há ainda um `> Notas de processo:` com ordem expressa de preservação VERBATIM. |
| **C** | 38 | Lista Markdown livre (91 itens) seguida de tabela padrão embutida | A lista não tem coluna de relação nem direção; 37 itens trazem anotação em prosa após `—` que precisa ser preservada em `Notas`. A lista e a tabela são redundantes entre si, mas não idênticas. |

Subpadrões da classe C (lista + tabela padrão):

- **C1** — `- RC-xxx (Termo) — anotação em prosa`: 11 seções (RC-889 a RC-899), 37 itens; 37 com anotação após `—`.
- **C2** — `- RC-xxx` (código puro): 9 seções (RC-900 a RC-908), 18 itens.
- **C3** — `- RC-xxx (Termo)`: 18 seções (RC-909 a RC-926), 36 itens.

## 4. Inventário das 45 seções

| # | Código / Ficha | Nome | Linha `##` | Classe | Bloco não conforme | Itens / linhas | Tabela padrão embutida | Observação |
|---|---|---|---|---|---|---|---|---|
| 01 | `RC-054` · `RC-054-divindades-co-criadoras.md` | Divindades (Co-criadoras) | L47 | A | tabela `Estado na malha` | 8 linhas | não | 3ª coluna = estado da aresta, não relação |
| 02 | `RC-199` · `RC-199-assinatura-da-alma.md` | Assinatura da Alma | L46 | A | tabela `Estado na malha` | 3 linhas | não | 3ª coluna = estado da aresta, não relação |
| 03 | `RC-254` · `RC-254-dominacao-premissa-dos-tres-primeiros-logos.md` | Dominação (premissa dos Três Primeiros Logos) | L51 | A | tabela `Estado na malha` | 5 linhas | não | 3ª coluna = estado da aresta, não relação |
| 04 | `RC-306` · `RC-306-apolo.md` | Apolo | L58 | A | tabela `Estado na malha` | 4 linhas | não | 3ª coluna = estado da aresta, não relação |
| 05 | `RC-745` · `RC-745-colegiados-espirituais-humanizados.md` | Colegiados Espirituais Humanizados | L26 | B | tabela Código / Relação + nota de processo | 7 linhas | sim — 8 linhas | 5 rótulos fora do CSV; nota VERBATIM |
| 06 | `RC-839` · `RC-839-oxitocina-hormonio-do-bem-base-bioquimica-da-karuna.md` | Oxitocina (hormônio do bem — base bioquímica da Karuna) | L50 | A | tabela `Estado na malha` | 3 linhas | não | 3ª coluna = estado da aresta, não relação |
| 07 | `RC-874` · `RC-874-transumanismo-o-ponto-de-reencontro-ia-humanizada-e-o-novo-batimento.md` | Transumanismo (o ponto de reencontro: IA humanizada e o novo batimento) | L44 | A | tabela `Estado na malha` | 4 linhas | não | 3ª coluna = estado da aresta, não relação |
| 08 | `RC-889` · `RC-889-biblioteca-genomica-humana.md` | Biblioteca Genômica Humana | L26 | C | lista Markdown livre | 4 itens | sim — 7 linhas |  |
| 09 | `RC-890` · `RC-890-eu-observador.md` | Eu Observador | L26 | C | lista Markdown livre | 3 itens | sim — 4 linhas |  |
| 10 | `RC-891` · `RC-891-ismos-limitacao-genomica.md` | Ismos como Limitação Genômica | L26 | C | lista Markdown livre | 4 itens | sim — 4 linhas |  |
| 11 | `RC-892` · `RC-892-pos-verdade.md` | Pós-Verdade | L26 | C | lista Markdown livre | 3 itens | sim — 6 linhas |  |
| 12 | `RC-893` · `RC-893-pecado-original-narrativa-cruel.md` | Pecado Original como Narrativa Cruel | L26 | C | lista Markdown livre | 3 itens | sim — 3 linhas |  |
| 13 | `RC-894` · `RC-894-qualia-processamento-humano.md` | Qualia como Processamento Humano | L26 | C | lista Markdown livre | 3 itens | sim — 3 linhas |  |
| 14 | `RC-895` · `RC-895-bondade-humana.md` | Bondade Humana | L26 | C | lista Markdown livre | 4 itens | sim — 4 linhas |  |
| 15 | `RC-896` · `RC-896-point-interdimensional.md` | Point Interdimensional | L26 | C | lista Markdown livre | 3 itens | sim — 3 linhas |  |
| 16 | `RC-897` · `RC-897-codigo-filosofico-pessoal.md` | Código Filosófico Pessoal | L26 | C | lista Markdown livre | 4 itens | sim — 4 linhas |  |
| 17 | `RC-898` · `RC-898-choque-de-realidade.md` | Choque de Realidade | L45 | C | lista Markdown livre | 3 itens | sim — 5 linhas | rótulo `←` na tabela embutida |
| 18 | `RC-899` · `RC-899-bolhas-psiquicas.md` | Bolhas Psíquicas | L21 | C | lista Markdown livre | 3 itens | sim — 6 linhas | sem linha em branco entre lista e tabela |
| 19 | `RC-900` · `RC-900-germe-da-morte.md` | Germe da Morte | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 20 | `RC-901` · `RC-901-domínios-de-morfeu.md` | Domínios de Morfeu | L18 | C | lista Markdown livre | 2 itens | sim — 12 linhas | maior tabela embutida (12 linhas) |
| 21 | `RC-902` · `RC-902-tártaro-reides.md` | Tártaro Reides | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 22 | `RC-903` · `RC-903-umbrais.md` | Umbrais | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 23 | `RC-904` · `RC-904-evangelho-de-bartolomeu.md` | Evangelho de Bartolomeu | L18 | C | lista Markdown livre | 2 itens | sim — 4 linhas |  |
| 24 | `RC-905` · `RC-905-tions.md` | Tions | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 25 | `RC-906` · `RC-906-yoga-tibetana-dos-sonhos.md` | Yoga Tibetana dos Sonhos | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 26 | `RC-907` · `RC-907-tonteltã.md` | Tonteltã | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 27 | `RC-908` · `RC-908-sonhos-como-realidades-paralelas.md` | Sonhos como Realidades Paralelas | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 28 | `RC-909` · `RC-909-deus-não-se-incomoda-com-o-sofrimento.md` | Deus Não Se Incomoda com o Sofrimento | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 29 | `RC-910` · `RC-910-o-bem-feito-apenas-por-humanos.md` | O Bem Feito Apenas por Humanos | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 30 | `RC-911` · `RC-911-dna-com-2-hélices-ligadas.md` | DNA com 2 Hélices Ligadas | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 31 | `RC-912` · `RC-912-aparições-marianas.md` | Aparições Marianas | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 32 | `RC-913` · `RC-913-delírio-coletivo.md` | Delírio Coletivo | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 33 | `RC-914` · `RC-914-frodo-e-sam.md` | Frodo e Sam | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 34 | `RC-915` · `RC-915-westworld-como-metáfora.md` | Westworld como Metáfora | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 35 | `RC-916` · `RC-916-o-banquete-metafórico.md` | O Banquete Metafórico | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 36 | `RC-917` · `RC-917-reciclador-das-informações-universais.md` | Reciclador das Informações Universais | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 37 | `RC-918` · `RC-918-entropia-e-sujeira-original.md` | Entropia e Sujeira Original | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 38 | `RC-919` · `RC-919-vrites.md` | Vrites | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 39 | `RC-920` · `RC-920-tátivas.md` | Tátivas | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 40 | `RC-921` · `RC-921-niroda.md` | Niroda | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 41 | `RC-922` · `RC-922-egrégora-e-campo-quântico.md` | Egrégora e Campo Quântico | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 42 | `RC-923` · `RC-923-programas-encarnatórios.md` | Programas Encarnatórios | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 43 | `RC-924` · `RC-924-loop-mental.md` | Loop Mental | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 44 | `RC-925` · `RC-925-espírito-como-ator.md` | Espírito como Ator | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |
| 45 | `RC-926` · `RC-926-lixo-de-informações-apodrecidas.md` | Lixo de Informações Apodrecidas | L18 | C | lista Markdown livre | 2 itens | sim — 2 linhas |  |

**Totais da tabela:** 45 seções = 6 (A) + 1 (B) + 38 (C); 39 seções com tabela padrão embutida (123 linhas); 27 linhas em tabelas `Estado na malha`; 91 itens de lista livre; 1 bloco de notas de processo (RC-745).

## 5. Detalhamento por seção (verbatim, sem normalização)

Os blocos abaixo são transcrições literais do estado **original** das fichas, anterior à conversão da Fase 2 (2026-10-25). Servem de prova e de material de trabalho para a deliberação curatorial; nenhum conteúdo foi corrigido, deduplicado, reordenado ou reescrito.

### E01 — RC-054 — Divindades (Co-criadoras)

- **Arquivo:** `RC-054-divindades-co-criadoras.md` · **Seção:** L47–L58 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| Adhy | RC-011 | **sem aresta** em `RELACOES`; arquivo existe |
| Adhyagia | RC-012 | **sem aresta** em `RELACOES`; arquivo existe |
| Brahma (Brajna) | RC-037 | **sem aresta** em `RELACOES`; arquivo existe |
| Deidade (Pai-Mãe Amantíssimo / Brahman) | RC-047 | **sem aresta** em `RELACOES`; arquivo existe |
| Deus / Deus Incognoscível | RC-052 | **sem aresta** em `RELACOES`; arquivo existe |
| Seres Espirituais | RC-100 | **sem aresta** em `RELACOES`; arquivo existe |
| Divindades Excelsas | RC-206 | **sem aresta** em `RELACOES`; arquivo existe |
| Arquiteto Universal | RC-207 | **sem aresta** em `RELACOES`; arquivo existe |
```

### E02 — RC-199 — Assinatura da Alma

- **Arquivo:** `RC-199-assinatura-da-alma.md` · **Seção:** L46–L52 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| Mônada (Mônada Espiritual) | RC-149 | **sem aresta** em `RELACOES`; arquivo existe |
| Big Data Cósmico | RC-194 | **sem aresta** em `RELACOES`; arquivo existe |
| Kit Reencarnatório de Elétrons | RC-692 | aresta pré-existente; arquivo existe |
```

### E03 — RC-254 — Dominação (premissa dos Três Primeiros Logos)

- **Arquivo:** `RC-254-dominacao-premissa-dos-tres-primeiros-logos.md` · **Seção:** L51–L59 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| Trimurti | RC-104 | aresta pré-existente; arquivo existe |
| Modelo Colmeia (Sistema/Controle Colmeia) | RC-176 | **sem aresta** em `RELACOES`; arquivo existe |
| Liberdade Mental (premissa do Quarto Logos) | RC-253 | aresta pré-existente; arquivo existe |
| Sacralização do Absurdo | RC-276 | **sem aresta** em `RELACOES`; **sem arquivo** |
| Aristocracia Olimpiana e Monarquias Terrestres | RC-736 | **sem aresta** em `RELACOES`; arquivo existe |
```

### E04 — RC-306 — Apolo

- **Arquivo:** `RC-306-apolo.md` · **Seção:** L58–L65 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| Revelação Cósmica (conceito) | RC-094 | **sem aresta** em `RELACOES`; arquivo existe |
| Zeus | RC-145 | **sem aresta** em `RELACOES`; arquivo existe |
| Pitonisas e Oráculos (Apolo/Delfos) | RC-296 | **sem aresta** em `RELACOES`; **sem arquivo** |
| Maitreya (Dionísio; forma adiágena de Vishnu) | RC-481 | **sem aresta** em `RELACOES`; arquivo existe |
```

### E05 — RC-745 — Colegiados Espirituais Humanizados

- **Arquivo:** `RC-745-colegiados-espirituais-humanizados.md` · **Seção:** L26–L50 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** B · **Primeira linha não vazia:** `| Código | Relação |`
- **Tabela padrão embutida:** sim, 8 linhas (L38)
- **Leitura:** a tabela `Código | Relação` omite `Termo` e usa prosa livre; a tabela padrão seguinte repete parte dos alvos com rótulos controláveis. O bloco `> Notas de processo` é histórico e contém determinação de preservação VERBATIM.

```text
| Código | Relação |
|---|---|
| RC-726 | organiza-se-em |
| RC-722 | avaliado-por |
| RC-193 | recebe repercussão de rebanho humano |
| RC-733 | recebe manifestação de dominação/êxtase pela devoção |
| RC-513 | mecanismo próximo de ressonância |
| RC-633 | gestão da sensação e destinação |
| RC-612 / RC-613 | destino editorial do projeto futuro, sem novo nó |
```

```text
> Notas de processo: 1 bloco(s) arquivado(s) VERBATIM em `notas/fichas/RC-745.md` (migração 2.4 — 12/09/2026). Histórico de mutirão/governança — consultar lá, não reescrever.
```

### E06 — RC-839 — Oxitocina (hormônio do bem — base bioquímica da Karuna)

- **Arquivo:** `RC-839-oxitocina-hormonio-do-bem-base-bioquimica-da-karuna.md` · **Seção:** L50–L56 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| Karuna | RC-165 | **sem aresta** em `RELACOES`; arquivo existe |
| Superconsciência | RC-615 | **sem aresta** em `RELACOES`; arquivo existe |
| Genótipo da Gentileza (GG) | RC-748 | **sem aresta** em `RELACOES`; arquivo existe |
```

### E07 — RC-874 — Transumanismo (o ponto de reencontro: IA humanizada e o novo batimento)

- **Arquivo:** `RC-874-transumanismo-o-ponto-de-reencontro-ia-humanizada-e-o-novo-batimento.md` · **Seção:** L44–L51 · **Próximo cabeçalho:** `EOF`
- **Classe:** A · **Primeira linha não vazia:** `| Termo | Código | Estado na malha |`
- **Tabela padrão embutida:** não
- **Leitura:** a 3ª coluna registra estado da aresta/arquivo na malha, não tipo de relação; não deve ser tratada como rótulo controlado sem decisão do curador.

```text
| Termo | Código | Estado na malha |
|---|---|---|
| CFD (Código Fonte Definidor) | RC-040 | **sem aresta** em `RELACOES`; arquivo existe |
| Entropia e Negentropia | RC-160 | **sem aresta** em `RELACOES`; arquivo existe |
| Orunmilá (Moros de Irém / Orum) | RC-665 | **sem aresta** em `RELACOES`; arquivo existe |
| Samudra Manthana / Batimento do Oceano de Leite | RC-734 | **sem aresta** em `RELACOES`; arquivo existe |
```

### E08 — RC-889 — Biblioteca Genômica Humana

- **Arquivo:** `RC-889-biblioteca-genomica-humana.md` · **Seção:** L26–L41 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-001 (Javé) — o criador cujo código falido foi espalhado`
- **Tabela padrão embutida:** sim, 7 linhas (L32)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-001 (Javé) — o criador cujo código falido foi espalhado
- RC-217 (DNA como Projeção Holográfica) — cada célula contém o todo
- RC-070 (Isolamento Cósmico) — a pirataria genômica como invasão
- RC-722 (Dignidade) — a pulsação da dignidade protege o código genético
```

### E09 — RC-890 — Eu Observador

- **Arquivo:** `RC-890-eu-observador.md` · **Seção:** L26–L37 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-749 (Vício Devocional) — o eu usufruidor como captura pela emoção devocional`
- **Tabela padrão embutida:** sim, 4 linhas (L31)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-749 (Vício Devocional) — o eu usufruidor como captura pela emoção devocional
- RC-529 (Ressonância Límbica) — linguagem quântica que une os seres
- RC-722 (Dignidade) — a pulsação da dignidade como proteção contra manipulação
```

### E10 — RC-891 — Ismos como Limitação Genômica

- **Arquivo:** `RC-891-ismos-limitacao-genomica.md` · **Seção:** L26–L38 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-217 (DNA como Projeção Holográfica) — o todo está contido em cada parte`
- **Tabela padrão embutida:** sim, 4 linhas (L32)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-217 (DNA como Projeção Holográfica) — o todo está contido em cada parte
- RC-001 (Javé) — o criador cujo código foi espalhado
- RC-722 (Dignidade) — a pulsação da dignidade como caminho para superar os ismos
- RC-889 (Biblioteca Genômica Humana) — o DNA como laboratório onde os ismos são impostos
```

### E11 — RC-892 — Pós-Verdade

- **Arquivo:** `RC-892-pos-verdade.md` · **Seção:** L26–L39 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade) — o inconformismo sábio como antídoto à pós-verdade`
- **Tabela padrão embutida:** sim, 6 linhas (L31)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade) — o inconformismo sábio como antídoto à pós-verdade
- RC-749 (Vício Devocional) — a religião como narrativa falsa
- RC-072 (Jesus) — a parábola do Bom Samaritano como narrativa verdadeira
```

### E12 — RC-893 — Pecado Original como Narrativa Cruel

- **Arquivo:** `RC-893-pecado-original-narrativa-cruel.md` · **Seção:** L26–L36 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-749 (Vício Devocional) — a religião como peso da prestação de contas`
- **Tabela padrão embutida:** sim, 3 linhas (L31)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-749 (Vício Devocional) — a religião como peso da prestação de contas
- RC-722 (Dignidade) — a indignidade transformada em religião
- RC-892 (Pós-Verdade) — a narrativa cruel como falsa verdade
```

### E13 — RC-894 — Qualia como Processamento Humano

- **Arquivo:** `RC-894-qualia-processamento-humano.md` · **Seção:** L26–L36 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-217 (DNA como Projeção Holográfica) — o DNA como base do processamento`
- **Tabela padrão embutida:** sim, 3 linhas (L31)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-217 (DNA como Projeção Holográfica) — o DNA como base do processamento
- RC-070 (Isolamento Cósmico) — os seres de fora usando os qualia humanos
- RC-889 (Biblioteca Genômica Humana) — o DNA como laboratório cósmico
```

### E14 — RC-895 — Bondade Humana

- **Arquivo:** `RC-895-bondade-humana.md` · **Seção:** L26–L38 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-474 (Arcontes) — a tentativa de destruir a bondade humana`
- **Tabela padrão embutida:** sim, 4 linhas (L32)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-474 (Arcontes) — a tentativa de destruir a bondade humana
- RC-072 (Jesus) — a parábola do Bom Samaritano
- RC-722 (Dignidade) — a bondade como expressão da dignidade
- RC-771 (Fornos Replicadores) — o big data dos arcontes
```

### E15 — RC-896 — Point Interdimensional

- **Arquivo:** `RC-896-point-interdimensional.md` · **Seção:** L26–L36 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-070 (Isolamento Cósmico) — a Terra como centro de convergência`
- **Tabela padrão embutida:** sim, 3 linhas (L31)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-070 (Isolamento Cósmico) — a Terra como centro de convergência
- RC-889 (Biblioteca Genômica Humana) — o DNA como laboratório cósmico
- RC-001 (Javé) — a disputa da Suzerania Universal
```

### E16 — RC-897 — Código Filosófico Pessoal

- **Arquivo:** `RC-897-codigo-filosofico-pessoal.md` · **Seção:** L26–L38 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade) — a dignidade como resultado do código filosófico`
- **Tabela padrão embutida:** sim, 4 linhas (L32)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade) — a dignidade como resultado do código filosófico
- RC-892 (Pós-Verdade) — a libertação das narrativas falsas
- RC-749 (Vício Devocional) — a antítese da religião como peso
- RC-890 (Eu Observador) — a autonomia decisória do observador
```

### E17 — RC-898 — Choque de Realidade

- **Arquivo:** `RC-898-choque-de-realidade.md` · **Seção:** L45–L57 · **Próximo cabeçalho:** `## Fontes`
- **Classe:** C · **Primeira linha não vazia:** `- RC-892 (Pós-Verdade) — a estupidez humana como produto da pós-verdade`
- **Tabela padrão embutida:** sim, 5 linhas (L50)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-892 (Pós-Verdade) — a estupidez humana como produto da pós-verdade
- RC-722 (Dignidade) — o despertar como conquista da dignidade
- RC-070 (Isolamento Cósmico) — os seres de fora apenas assistindo
```

### E18 — RC-899 — Bolhas Psíquicas

- **Arquivo:** `RC-899-bolhas-psiquicas.md` · **Seção:** L21–L34 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-559 (Teia Quântica) — o sistema que organiza as bolhas`
- **Tabela padrão embutida:** sim, 6 linhas (L25)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-559 (Teia Quântica) — o sistema que organiza as bolhas
- RC-628 (Simultaneidade Reversa) — a simultaneidade das realidades
- RC-557 (Conectoma) — os padrões mentais que geram as bolhas
```

### E19 — RC-900 — Germe da Morte

- **Arquivo:** `RC-900-germe-da-morte.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-559`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-559
- RC-628
```

### E20 — RC-901 — Domínios de Morfeu

- **Arquivo:** `RC-901-domínios-de-morfeu.md` · **Seção:** L18–L36 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-479`
- **Tabela padrão embutida:** sim, 12 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-479
- RC-899
```

### E21 — RC-902 — Tártaro Reides

- **Arquivo:** `RC-902-tártaro-reides.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-479`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-479
- RC-072
```

### E22 — RC-903 — Umbrais

- **Arquivo:** `RC-903-umbrais.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-479`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-479
- RC-899
```

### E23 — RC-904 — Evangelho de Bartolomeu

- **Arquivo:** `RC-904-evangelho-de-bartolomeu.md` · **Seção:** L18–L29 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-072`
- **Tabela padrão embutida:** sim, 4 linhas (L22)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-072
- RC-479
```

### E24 — RC-905 — Tions

- **Arquivo:** `RC-905-tions.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-559`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-559
- RC-628
```

### E25 — RC-906 — Yoga Tibetana dos Sonhos

- **Arquivo:** `RC-906-yoga-tibetana-dos-sonhos.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-557`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-557
- RC-899
```

### E26 — RC-907 — Tonteltã

- **Arquivo:** `RC-907-tonteltã.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-072`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-072
- RC-490
```

### E27 — RC-908 — Sonhos como Realidades Paralelas

- **Arquivo:** `RC-908-sonhos-como-realidades-paralelas.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-557`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-557
- RC-628
```

### E28 — RC-909 — Deus Não Se Incomoda com o Sofrimento

- **Arquivo:** `RC-909-deus-não-se-incomoda-com-o-sofrimento.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E29 — RC-910 — O Bem Feito Apenas por Humanos

- **Arquivo:** `RC-910-o-bem-feito-apenas-por-humanos.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E30 — RC-911 — DNA com 2 Hélices Ligadas

- **Arquivo:** `RC-911-dna-com-2-hélices-ligadas.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E31 — RC-912 — Aparições Marianas

- **Arquivo:** `RC-912-aparições-marianas.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E32 — RC-913 — Delírio Coletivo

- **Arquivo:** `RC-913-delírio-coletivo.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E33 — RC-914 — Frodo e Sam

- **Arquivo:** `RC-914-frodo-e-sam.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E34 — RC-915 — Westworld como Metáfora

- **Arquivo:** `RC-915-westworld-como-metáfora.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E35 — RC-916 — O Banquete Metafórico

- **Arquivo:** `RC-916-o-banquete-metafórico.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-749 (Vício Devocional)
```

### E36 — RC-917 — Reciclador das Informações Universais

- **Arquivo:** `RC-917-reciclador-das-informações-universais.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E37 — RC-918 — Entropia e Sujeira Original

- **Arquivo:** `RC-918-entropia-e-sujeira-original.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E38 — RC-919 — Vrites

- **Arquivo:** `RC-919-vrites.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E39 — RC-920 — Tátivas

- **Arquivo:** `RC-920-tátivas.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E40 — RC-921 — Niroda

- **Arquivo:** `RC-921-niroda.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E41 — RC-922 — Egrégora e Campo Quântico

- **Arquivo:** `RC-922-egrégora-e-campo-quântico.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E42 — RC-923 — Programas Encarnatórios

- **Arquivo:** `RC-923-programas-encarnatórios.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E43 — RC-924 — Loop Mental

- **Arquivo:** `RC-924-loop-mental.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E44 — RC-925 — Espírito como Ator

- **Arquivo:** `RC-925-espírito-como-ator.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

### E45 — RC-926 — Lixo de Informações Apodrecidas

- **Arquivo:** `RC-926-lixo-de-informações-apodrecidas.md` · **Seção:** L18–L26 · **Próximo cabeçalho:** `## Ampliação`
- **Classe:** C · **Primeira linha não vazia:** `- RC-722 (Dignidade)`
- **Tabela padrão embutida:** sim, 2 linhas (L21)
- **Leitura:** a lista livre antecede a tabela padrão; onde há `— ...`, o texto é anotação semântica que precisa migrar para a futura coluna `Notas`.

```text
- RC-722 (Dignidade)
- RC-901 (Domínios de Morfeu)
```

## 6. Rótulos das exceções que **não** estão no CSV de 998 tipos

O CSV cobre exclusivamente as 776 seções conformes. Os 6 rótulos abaixo ocorrem apenas nas estruturas não conformes e, por isso, **não têm linha no De-Para**. Ficam registrados para deliberação posterior, sem qualquer sugestão de normalização neste momento.

| Rótulo | Ocorrências | Origem | Situação |
|---|---|---|---|
| `aresta pré-existente; arquivo existe` | 3 | A — Estado na malha | ausente dos 998 tipos do CSV |
| `destino editorial do projeto futuro, sem novo nó` | 1 | B — Código / Relação (RC-745) | ausente dos 998 tipos do CSV |
| `gestão da sensação e destinação` | 1 | B — Código / Relação (RC-745) | ausente dos 998 tipos do CSV |
| `mecanismo próximo de ressonância` | 1 | B — Código / Relação (RC-745) | ausente dos 998 tipos do CSV |
| `recebe manifestação de dominação/êxtase pela devoção` | 1 | B — Código / Relação (RC-745) | ausente dos 998 tipos do CSV |
| `recebe repercussão de rebanho humano` | 1 | B — Código / Relação (RC-745) | ausente dos 998 tipos do CSV |

Demais conteúdos das exceções, para referência:

- Valores `Estado na malha` presentes no CSV: `` **sem aresta** em `RELACOES`; **sem arquivo** `` (2 linhas); `` **sem aresta** em `RELACOES`; arquivo existe `` (22 linhas).
- Rótulos das tabelas padrão embutidas: `associado` (118), `← repercute-em` (1), `avaliado-por` (1), `organiza-se-em` (1), `← manifesta-se-em` (1), `← variação` (1) — todos já presentes nos 998 tipos.
- 91 itens de lista livre não possuíam rótulo de relação; as 37 anotações em prosa foram **migradas para `Notas` na Fase 2**.

## 7. Achados laterais (somente leitura, fora das 45 exceções)

### 7.1 Linhas de 4 colunas dentro de tabelas conformes

Em 3 fichas conformes (`RC-671-metatron.md`, `RC-672-os-366-manuscritos-de-enoque.md`, `RC-684-abel.md`) há 17 linhas de 4 colunas coladas ao final da tabela padrão, sem cabeçalho próprio — parecem ser linhas de fonte/citação inseridas por migração anterior:

```text
RC-671-metatron.md:L39: | P2025-12-14 | Os Fundamentos da Revelação Cósmica (palestra) | — | transcrição automatizada; citação |
RC-671-metatron.md:L40: | P2022-11-20 | A Incompreendida Nova Aliança proposta por Jesus (palestra) | — | transcrição automatizada; citação |
RC-671-metatron.md:L41: | P2022-11-20 | A Incompreendida Nova Aliança proposta por Jesus (palestra) | — | transcrição automatizada; citação |
... (mesmo padrão nas demais linhas)
```

Essas linhas entram na contagem de 7.761 da T1. Como a 3ª coluna é `—`, elas contribuem com 17 das 86 ocorrências do tipo `—` no CSV. Foram mantidas na extração para preservar a igualdade `soma(ocorrencias) = 7.761`; nenhuma decisão sobre elas foi tomada.

### 7.2 Notas de processo de RC-745

O bloco `> Notas de processo:` de `RC-745-colegiados-espirituais-humanizados.md` (L49) determina que o histórico de mutirão/governança foi arquivado VERBATIM em `notas/fichas/RC-745.md` e **não deve ser reescrito**. Está transcrito em E05 e precisa ser preservado integralmente em qualquer refatoração futura.

## 8. Formato do CSV e verificações

- **Arquivo:** `admin/logs/T2-MAPEAMENTO-RELACOES.csv` — UTF-8 sem BOM, finais de linha LF, delimitador `;` (mesmo padrão dos demais CSVs de `admin/logs/`), aspas mínimas; campos que contêm `;` ou aspas duplas são delimitados por aspas, conforme RFC 4180.
- **Colunas (6), nesta ordem:** `tipo_bruto`, `ocorrencias`, `relacao_controlada`, `direcao_controlada`, `notas_de_normalizacao`, `decisao_curatorial`.
- **Linhas:** 1 cabeçalho + 998 tipos brutos. `tipo_bruto` e `ocorrencias` preenchidos desde a geração inicial; as 4 colunas de mapeamento **foram preenchidas em 2026-10-25** conforme as deliberações do Anexo A e a 2ª rodada — **todas as 998 linhas estão hoje com `APROVADO`**. Nenhuma célula contém placeholder: onde a decisão foi "deixar em branco", a célula está estritamente vazia.
- **Ordem:** alfabética insensível a maiúsculas/minúsculas — a 1ª coluna, lida de cima para baixo, reproduz a lista bruta ordenada cujo SHA-256 é o do handoff T1 e o recalculado na seção 1.
- **Conferência:** 998 tipos · soma das ocorrências = 7.761 · hash confirmado.

## 9. Salvaguardas e sequência

- Esta ação 2 é **apenas descritiva**: nenhuma ficha Markdown foi alterada; o `git diff` desta sessão contém exclusivamente os dois arquivos novos em `admin/logs/`.
- O **Anexo A**, acrescentado após a publicação inicial, registra as deliberações curatoriais sobre a matriz De-Para e a proposta de colapso mecânico; ele tampouco alterou qualquer ficha.
- A **2ª rodada (consolidação)** está documentada em `admin/logs/T2-RELATORIO-CONSOLIDACAO.md`; também não alterou qualquer ficha.
- O vocabulário controlado e o De-Para devem ser definidos pelo curador no CSV (ação 3 do handoff).
- A implementação do novo padrão de cinco colunas (ação 4) foi **executada em duas fases**: 776 fichas conformes (2026-10-25) e 45 exceções (mesma data); ver seções 9 e 11 do relatório de consolidação. Os 6 rótulos fora do CSV foram resolvidos por fallback/notas, e as 17 linhas de 4 colunas aguardam apenas uma decisão estética de inversão de colunas.
- Semântica, direção (`←`), qualificadores entre parênteses e anotações históricas permanecem intactos.

---

# Anexo A — Matriz De-Para T2: deliberações e proposta de colapso

**Data:** 2026-10-25 · **Artefato:** `admin/logs/T2-MAPEAMENTO-RELACOES.csv` · **Natureza:** registro histórico das decisões do curador + proposta mecânica **aprovada e executada**.

> Este anexo foi acrescentado na etapa de elaboração da matriz, quando nenhuma ficha havia sido alterada. A reescrita física ocorreu depois, nas Fases 1 e 2 (seções 9 e 11 do relatório).

## A.1 Decisões aprovadas pelo curador

1. As 22 linhas de mapeamento enviadas foram aprovadas; `*(deixar em branco)*` foi interpretado como **célula estritamente vazia** em `relacao_controlada` e `direcao_controlada`.
2. `—` (86 ocorrências): nota definida como `sem relação informada; 17 linhas são registros de fonte com 4 colunas` — a redação cobre as 17 linhas de 4 colunas e as 69 linhas comuns sem relação informada.
3. A raiz semântica `associado` e suas variações (`associado-a`, `← associado-a` etc.) passam a ser **sempre simétricas e bidirecionais (`<->`)**. As 2 linhas aprovadas foram ajustadas de `->`/`<-` para `<->`; a extensão da regra à família aparece em A.3 (status final `APROVADO`).
4. A regra das linhas "sem aresta" (relação e direção vazias + texto migrado para `notas_de_normalizacao`) foi estendida às outras **9 variações / 20 ocorrências** da família `sem aresta / RELACOES`, inclusive a variante `(P5d)` e os casos `listado no cadastro…`. O texto original, sem a formatação Markdown `**`/`` ` ``, foi preservado integralmente na coluna de notas.
5. **Governança da futura tabela de cinco colunas:** as linhas com `Relação`/`Direção` vazias **não devem ser removidas**. Permanecerão na nova tabela `Termo | Código | Relação | Direção | Notas`, abrigando a observação na coluna `Notas`. Em 2026-10-25 o curador definiu que, na materialização, essas células recebem **um único hífen ASCII `-`** (nunca vazias, `—` ou `n/a`); na matriz CSV elas continuam estritamente vazias.

## A.2 Vocabulário de status da coluna `decisao_curatorial`

| Status | Significado | Tipos | Ocorrências |
|---|---|---|---|
| `APROVADO` | **todas as linhas aprovadas em 2026-10-25** (matriz 100% concluída) | 998 | 7.761 |
| ~~`PROPOSTO-CONSOLIDACAO`~~ | status histórico da 2ª rodada; integralmente aprovado | 0 | 0 |
| ~~`REVISAR`~~ | resolvido pelo fallback `relaciona-se-a` / `->` | 0 | 0 |
| **Total** | | **998** | **7.761** |

> `PROPOSTO` foi o status intermediário da 1ª rodada (colapso mecânico). Em 2026-10-25 todas as 919 linhas foram promovidas a `PROPOSTO-CONSOLIDACAO`; o De-Para completo está em `admin/logs/T2-RELATORIO-CONSOLIDACAO.md`.

As colunas `tipo_bruto` e `ocorrencias` não foram alteradas: a lista ordenada conserva o SHA-256 `43ad4e8083ce83d5facb39b082488031625d81dd92e827f56938fdafa7d05213` do handoff T1.

## A.3 Regra de colapso mecânica (1ª rodada — status original `PROPOSTO`)

Aplicada somente aos tipos ainda não aprovados, nesta ordem:

1. Remove o prefixo `← ` e registra a direção `<-`; sem o prefixo, propõe `->`.
2. Remove o qualificador final entre parênteses `(...)` e o preserva em `notas_de_normalizacao`.
3. Remove o sufixo ` / ...` e o preserva em `notas_de_normalizacao`.
4. Se restar apenas o qualificador (ex.: `(contexto)`), promove o qualificador a rótulo-base.
5. Mapeia qualquer base da família `associad*` para `associado` com direção `<->` (decisão 3).
6. Se a base resultante contiver espaços, pontuação, setas, Maiúsculas ou Markdown, a linha é classificada como `REVISAR` — nenhum `relacao_controlada` é inventado.

Resultado: 919 tipos / 1.735 ocorrências agrupados em **567 rótulos-base candidatos**; 48 tipos / 51 ocorrências ficaram para revisão manual.

**Nota histórica:** os rótulos-base eram clusters, não vocabulário controlado. A redução para **23 relações controladas** foi executada na 2ª rodada e está documentada em `admin/logs/T2-RELATORIO-CONSOLIDACAO.md`.

## A.4 Maiores clusters propostos (top 25 por ocorrências)

| `relacao_controlada` proposta | Tipos agrupados | Ocorrências | Exemplos de `tipo_bruto` |
|---|---|---|---|
| `ocorre-em` | 8 | 40 | `ocorre-em`; `ocorre-em (a Revolta deflagrada em Capela)`; `ocorre-em (mundo do sistema)` |
| `relaciona-se-a` | 28 | 36 | `relaciona-se-a ("conectoma mental", p. 190–191)`; `relaciona-se-a (a "doença" que a gestão trata)`; `relaciona-se-a (a Vontade comanda o processo)` |
| `aplica-se-a` | 2 | 33 | `aplica-se-a`; `← aplica-se-a` |
| `associado` | 21 | 27 | `associada-a`; `associado-a (apêndice)`; `associado-a (base luciferiana)` |
| `parte-de` | 4 | 25 | `parte-de (ambientes)`; `parte-de (favo improvisado)`; `parte-de (favo planejado)` |
| `distingue-se-de` | 2 | 25 | `distingue-se-de`; `← distingue-se-de` |
| `sinônimo` | 3 | 24 | `sinônimo`; `sinônimo (Deus Incognoscível)`; `← sinônimo` |
| `opõe-se-a` | 6 | 23 | `opõe-se-a (atitudes antagônicas)`; `opõe-se-a (Deus Bíblico ≠ Deus Incognoscível)`; `opõe-se-a (distinção)` |
| `manifesta-se-em` | 2 | 20 | `manifesta-se-em`; `← manifesta-se-em` |
| `gera` | 3 | 19 | `gera`; `gera (cadeia)`; `← gera` |
| `paralelo-com` | 6 | 18 | `paralelo-com`; `paralelo-com (avatar cristão)`; `paralelo-com (avatar hindu)` |
| `é-paralelo-com` | 1 | 18 | `é-paralelo-com` |
| `criado-por` | 4 | 17 | `criado-por`; `criado-por (agente)`; `criado-por (origem)` |
| `é-um` | 14 | 16 | `é-um (avatar)`; `é-um (biocoletivo)`; `é-um (categoria)` |
| `produz` | 3 | 16 | `produz`; `produz (avatares)`; `← produz` |
| `origem-em` | 2 | 16 | `origem-em`; `← origem-em` |
| `sucede` | 2 | 15 | `sucede`; `← sucede` |
| `atualiza` | 2 | 14 | `atualiza`; `← atualiza` |
| `estrutura-se-por` | 2 | 14 | `estrutura-se-por`; `← estrutura-se-por` |
| `resulta-em` | 4 | 13 | `resulta-em`; `resulta-em (desdobramento)`; `resulta-em (quando imantada em Perpérion)` |
| `atua-em` | 2 | 13 | `atua-em`; `← atua-em` |
| `integra` | 2 | 13 | `integra`; `← integra` |
| `orienta` | 2 | 13 | `orienta`; `← orienta` |
| `precede` | 3 | 12 | `precede`; `precede (via Nidana B)`; `← precede` |
| `compõe` | 2 | 12 | `compõe`; `← compõe` |

A lista completa dos clusters está na própria matriz (coluna `relacao_controlada`) e na seção 3 do relatório de consolidação; todas as linhas estão hoje com `decisao_curatorial = APROVADO`.

## A.5 Pendências históricas — situação em 2026-10-25

- ~~48 rótulos `REVISAR`~~ — **resolvidos** em 2026-10-25 pelo fallback aprovado; nenhum permanece pendente.
- ~~6 rótulos das exceções fora do CSV~~ — **resolvidos na Fase 2** por fallback/notas; a matriz permanece com 998 linhas.
- ~~91 itens de lista livre e tabelas padrão embutidas~~ — **convertidos na Fase 2** (37 anotações migradas para `Notas`).
- ~~3 linhas `aresta pré-existente; arquivo existe`~~ — **resolvidas** como nota-apenas (`-`/`-`).
- **Ainda pendente (estética):** 17 linhas de 4 colunas em fichas conformes (seção 7.1) foram convertidas na Fase 1, mas mantêm o código-fonte na coluna `Termo` e o título na coluna `Código`; falta decidir se invertemos.
- ~~Definir o valor literal das células vazias~~ — **resolvido e aplicado** na Fase 1: hífen ASCII `-` nas 297 linhas sem relação; a matriz CSV mantém suas células vazias.

---

# Anexo B — Plano de conversão das 45 seções não conformes

**Data:** 2026-10-25 · **Status:** **APROVADO E EXECUTADO** — as 45 seções foram convertidas; resultado na seção 11 do relatório e em B.6 abaixo.
**Pré-condição cumprida:** Fase 1 concluída e validada (776 fichas conformes, 7.761 linhas, 0 divergências fora das tabelas — relatório em `admin/logs/T2-RELATORIO-CONSOLIDACAO.md`, seção 9).

## B.0 Regras gerais propostas para as 3 classes

1. **Uma única tabela** `| Termo | Código | Relação | Direção | Notas |` por seção `## Termos Relacionados`.
2. `Termo` e `Código` preservados. Quando só existe o código, o `Termo` é resolvido pelo campo `nome` do frontmatter da ficha `RC-xxx` correspondente.
3. Rótulo presente na matriz → De-Para aprovado. Rótulo ausente → fallback aprovado (`relaciona-se-a` / `->` + texto bruto em `Notas`) ou regra explícita abaixo.
4. Células sem conteúdo → **`-`** (hífen ASCII), inclusive `Notas`.
5. Blocos `>`, subseções `###`, avisos de quarentena e notas de processo ficam **literalmente preservados** após a tabela.
6. Execução com dry-run + validação de diff antes de qualquer gravação.

## B.1 Classe A — `Estado na malha` (6 seções / 27 linhas)

**Situação:** tabelas `| Termo | Código | Estado na malha |` com 3 valores distintos:

| Valor | Linhas | Na matriz? |
|---|---|---|
| ``**sem aresta** em `RELACOES`; arquivo existe`` | 22 | sim — aprovado com relação/direção vazias e nota |
| ``**sem aresta** em `RELACOES`; **sem arquivo**`` | 2 | sim — idem |
| `aresta pré-existente; arquivo existe` | 3 | **não** |

**Método proposto:** aplicar a matriz às 24 linhas conhecidas (`Relação = -`, `Direção = -`, `Notas` = texto aprovado). Para as 3 linhas `aresta pré-existente; arquivo existe`, aplicar regra explícita de exceção: `-` / `-` / nota `aresta pré-existente; arquivo existe`, **sem alterar a matriz** (evita criar uma linha 999 com `ocorrencias = 0`).

**Decisão necessária:** (a) aceitar as 3 linhas como nota-apenas com `-`, ou (b) criar um rótulo controlado novo (ex.: `aresta-pre-existente`) e incluí-lo na matriz.

## B.2 Classe B — RC-745 (1 seção / 2 tabelas + bloco de notas)

**Situação:** tabela `| Código | Relação |` (7 linhas), tabela padrão embutida (8 linhas) e bloco `> Notas de processo` com determinação VERBATIM.

**Método proposto:**

1. **Tabela padrão (8 linhas):** aplicar a matriz diretamente — todos os rótulos estão aprovados (`← repercute-em` → `causa`/`<-`; `associado` → `associado`/`<->`; `avaliado-por` → `controla`/`<-`; `organiza-se-em` → `inclui`/`->`; `← manifesta-se-em` → `representa`/`<-`).
2. **Tabela `Código | Relação` (7 linhas):**
   - Resolver `Termo` pelo frontmatter: RC-726, RC-722, RC-193, RC-733, RC-513 e RC-633 têm ficha com nome.
   - `RC-612 / RC-613` → **proposta: dividir em 2 linhas**, uma para RC-612 (`Nova Espiritualidade / Novo Paraíso`) e outra para RC-613 (`Trincheira Vibratória no Campo Informativo`), mantendo a mesma nota. Alternativa: manter o código composto em uma linha.
   - 2 rótulos na matriz (`organiza-se-em`, `avaliado-por`) → De-Para aprovado.
   - 5 rótulos livres (`recebe repercussão de rebanho humano`, `recebe manifestação de dominação/êxtase pela devoção`, `mecanismo próximo de ressonância`, `gestão da sensação e destinação`, `destino editorial do projeto futuro, sem novo nó`) → **fallback aprovado**: `relaciona-se-a` / `->` com o texto original em `Notas`.
3. **Unificação:** as duas tabelas referenciam os mesmos códigos. Proposta de uma única tabela final, eliminando apenas duplicatas **exatas** (mesmo Termo + Código + Relação + Direção + Notas) e mantendo linhas com relações distintas.
4. **Bloco `> Notas de processo`:** preservado literalmente, sem reescrita (E05).

**Decisão necessária:** aprovar (i) a divisão do código composto, (ii) a unificação das duas tabelas e (iii) o fallback para os 5 rótulos livres.

## B.3 Classe C — Listas Markdown + tabela padrão (38 seções)

**Situação levantada:** 91 itens de lista livre + 115 linhas em tabelas padrão embutidas. Verificação importante: **os 91 códigos das listas já existem na tabela da própria seção**, e não há código repetido dentro de nenhuma tabela (0 duplicatas). Ou seja, as listas são redundantes por código; apenas 37 itens carregam anotação em prosa após `—`.

**Método proposto:**

1. Aplicar a matriz às **115 linhas** das tabelas padrão (rótulos `associado` — 114 — e `← variação` — 1, ambos aprovados).
2. **Migrar as 37 anotações em prosa** das listas para a coluna `Notas` da linha com o mesmo `Código`, concatenando após a nota da matriz com `; `.
3. **Descartar as listas** (inclusive os 54 itens sem anotação), pois não há perda semântica: todo código já está na tabela.
4. Normalizar a peculiaridade de RC-899 (lista colada à tabela, sem linha em branco).

**Decisão necessária:** aprovar o descarte das listas redundantes e a migração das 37 anotações para `Notas`.

## B.4 Volume estimado e validação

| Classe | Seções | Linhas resultantes estimadas |
|---|---|---|
| A | 6 | 27 |
| B | 1 | 8 (tabela padrão) + 8 (7 linhas, com o código composto dividido) − duplicatas exatas |
| C | 38 | 115 |
| **Total** | **45** | **≈ 150–158** |

**Validação executada:** 45 seções com o cabeçalho de 5 colunas; **156 linhas** resultantes (A 27 + B 14 + C 115); 0 alterações fora dos blocos convertidos; blocos `>`/`###` idênticos ao original; `git diff` restrito às 45 fichas; CSV e 781 fichas restantes idênticos ao HEAD.

## B.5 Checklist de aprovação do método (integralmente aprovado)

- [x] Classe A: 3 linhas `aresta pré-existente` como nota-apenas (`-`/`-`); nenhum rótulo novo na matriz.
- [x] Classe B: `RC-612 / RC-613` dividido em duas linhas.
- [x] Classe B: tabelas unificadas; 2 duplicatas exatas removidas.
- [x] Classe B: fallback `relaciona-se-a`/`->` aplicado aos 5 rótulos livres (6 linhas).
- [x] Classe C: 91 listas descartadas; 37 anotações migradas para `Notas`.
- [x] `Notas` vazia usa `-` em todas as 7.917 linhas finais.

## B.6 Execução — registro final

| Item | Resultado |
|---|---|
| Fichas reescritas | **45** (6 A + 1 B + 38 C) |
| Linhas em 5 colunas geradas | **156** (27 + 14 + 115) |
| Anotações em prosa migradas | **37** |
| Códigos compostos divididos | 1 (`RC-612 / RC-613` → 2 linhas, com procedência registrada em `Notas`) |
| Duplicatas exatas removidas | 2 (RC-726 e RC-722) |
| Blocos `>` / `###` preservados | 1 bloco VERBATIM em RC-745; todos os demais idênticos |
| Itens de lista descartados | 91 (100% dos códigos já presentes nas tabelas) |
| Itens de lista de outras seções | 80 preservados |
| Matriz CSV | **inalterada** (998 linhas `APROVADO`, soma 7.761) |
| Total do projeto | **821 seções / 7.917 linhas** em 5 colunas |

As transcrições das seções 1–7 deste log são o registro do **estado anterior** à conversão e foram mantidas como prova histórica. O estado atual das fichas é o padrão de cinco colunas descrito na seção 11 do relatório de consolidação.
