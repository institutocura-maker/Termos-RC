# Pacto de arquitetura — Onda 2 (Fichas) · 12/09/2026

> Despacho do Curador que abre a Onda 2, com três pontos de atenção arquitetural. Este documento os **cristaliza em portões mecânicos** — valem para TODA unidade da Onda 2 e serão cobrados por script, não por boa vontade.

## 1. A "Guilhotina" — injeção cirúrgica em prosa

Todo script que tocar `.md` de ficha nasce morto; só escreve disco se provar, por ficheiro:

- **G1.1 — corte contíguo:** a mutação é uma *splicing* de blocos exatos (o texto novo tem de ser `cabeçalho + corpo_original_sem_bloco`, com o bloco removido casando byte a byte na posição);
- **G1.2 — paridade literal do resto:** todo byte que NÃO é o bloco declarado permanece verbatim, contíguo, no arquivo reescrito (assert de substring + posições);
- **G1.3 — dry-run obrigatório:** o relatório seco lista, por ficha: bloco removido (com as linhas), tamanho antes/depois, gates; APPLY só com tudo verde;
- **G1.4 — backup pré-escrita** (/tmp, efêmero, como no P5b/1.4) + git é a cápsula do tempo: 1 família de fichas = 1 commit;
- **G1.5 — Unicode preservado:** nenhuma normalização silenciosa (sem NFC/NFD, sem strip de aspas curvas, sem tocar em ⟶/⚠/emojis); o script opera em str com encoding declarado `utf-8` e nunca re-renderiza o corpo — só concatena.

## 2. Chunking RAG — os dossiês gigantes (2.2)

Consolidação de 001/009/072/104 sem "amnésia de meio de texto":

- **G2.1 — marcação semântica rígida é obrigatória:** hierarquia `##`/`###` preservada e, onde o bloco fundido perder subtítulo, ele é REINSERIDO (nunca removido);
- **G2.2 — porta do tamanho:** nenhum trecho contínuo de prosa > **6.000 caracteres** sem um subtítulo; métrica lavrada em certidão antes/depois por dossiê;
- **G2.3 — pontos de quebra naturais:** seções canônicas (`Definição Sintética`, `Contexto / Origem`, `Citações-chave`, `Ampliação`, `Fontes`, `Termos Relacionados`, `Observações`) viram as bordas dos chunks; nomes NÃO mudam (o verificador de verbetes e o RAG futuro dependem deles);
- **G2.4 — fusão sem reescrita:** consolidar = mover/deduplicar blocos inteiros verbatim + ordenar; nada de parafrasear (regra-mãe: o ouro é o texto lapidado).

## 3. Envelope × Carta — redundância para o TOML, nunca os dois

- **G3.1 — metadado mora no TOML, um só lugar:** `codigo, nome, categoria, subcategoria, status, fontes (siglas), via, confianca_fonte, atualizado` — valores **do registro** (fonte de verdade), não do que a ficha digito-grafava;
- **G3.2 — remoção enumerada:** o script remove do corpo apenas o `| Campo | Valor |` (e o que mais o Curador enumerar), linha a linha, com assert de que nenhuma linha removida é citada verbatim em verbete (côtejo automático) nem reaparece em outro ponto da ficha;
- **G3.3 — invariante xor:** uma ficha tem status OU no frontmatter OU na tabela — nunca em ambos (guarda na suite, T6/T13);
- **G3.4 — `## Fontes` fica na carta:** a tabela de fontes com âncoras U####/p. é aparato de citação (último selo da lapidação), não envelope — só migra se o Curador um dia o enumerar;
- **G3.5 — consumers adaptados no MESMO commit:** suite (T6 aware; novo teste de frontmatter) e `build_word` (strip do bloco `+++` — o docx nunca vê TOML cru).

## Domínio de aplicação (2.1 piloto)

10 fichas: os 4 gigantes de 2.2 (RC-001/009/072/104 — o frontmatter já nasce testado onde doerá) + 6 de formas variadas (RC-167 verbo-modelo · RC-454/499/714 hubs com tabelas-tipadas · RC-592/611 padrão pequeno). Decisão de expandir p/ as 661 restantes sai do piloto + "decisão expandir" do plano (2.1), com certidão própria.

*Nada aqui toca `relacoes/`, o registro-mestre ou os espelhos além do regenerado de praxe. Suite verde (agora 13 checks) é portão de cada commit.*
