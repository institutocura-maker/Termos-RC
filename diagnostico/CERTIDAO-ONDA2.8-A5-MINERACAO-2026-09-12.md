# CERTIDÃO — U21 · Fila A5: mineração de citações-chave — 2026-09-12

**Despacho:** fila A5 (82 fichas 🟢 sem `## Citações-chave`, herdada da Onda 2.3): triagem mecânica com ouro quando a fonte em disco o permite.

## Método (script determinístico, bifásico dry-run→APPLY; gates por ficha)
- Varredura das fontes do termo no registro; **só prosa organizada**: livros via `original.txt`, apostilas **apenas** via `apostila.md` — STT bruta (`original.txt` de palestra) nunca gera citação (regra lavrada após o spot-check rejeitar janelas "em tá na retaguarda" do bruto).
- Janela: termo (nome + variações da Etimologia) presente no trecho; início em maiúscula após fronteira de frase; fim obrigatório em fronteira (corte a meio da palavra = rejeição — porta lavrada após o spot-check flagar "Perperion" truncado); 170–1400c; verbatim substring da fonte (refluxo de espaços/novas linhas permitido, declarado no ledger); até 3 citações de fontes distintas.
- **Filtro de ruído** (BAD): marcas de conversão-ebook (`[PÁGINA n]`, `=====`, watermark, `***`), preâmbulos e disclaimers de apostila ("O QUE SE SABE", "não consensus/leitura de Ellam", "Alegações"), aberturas de palestra ("Boa noite…"), e **ponteirões de aparato** (`RC-\d`) — a última porta custou 9 fichas (37→28), sacrificadas deliberadamente por qualidade; aparato não é fonte.
- Inserção antes de `## Observações` (senão no fim); **gate de restauração byte a byte** (removida a seção, a carta volta ao original) + tomllib do envelope + paridade de citação-vs-fonte, por ficha.

## Resultado do censo (ledger `A5-MINERACAO-2026-09-12.json|.md`)
- **28 fichas** ganharam índice curado mecânico (ex.: RC-014 com 3 painéis de B031/B044/B016).
- **52 permanecem na fila A5** sem parágrafo-ouro em fonte organizada — curadoria humana item a item, não-retroatividade preservada (selo 🟢 intacto; nada foi preenchido à força).
- **2 lápides** (RC-449, RC-872) excluídas por política 2.1B (registro histórico não recebe índice).
- Efeito colateral honesto: os 9 candidatos RC-477..502 com `fontes=[]` (pós-guilhotina B061 U20) caem naturalmente aqui — sem fonte em disco, permanecem na fila.

## Pós-verificação
Suíte completa verde (T13 671; T14 0-divergentes; blocos ≤6k respeitados); verificador "base intacta"; rebuilds: `base/canonico.json` + índice-mestre (fichas-resumo atualizadas), XLSX, DOCX, README — 946/671/1887/102. Gold das cartas e `notas/` intocados; registro-mestre não mudou (só fichas). commit único (1 unidade).

## U23 — complemento (13/09, madrugada): delegação de integração
Despacho do Curador em três frentes: (1) aprovação nominal de 3 candidatas (RC-015, RC-506, RC-746 — nesta, o fim ditado de memória foi substituído pelo verbatim integral da fonte, diferença documentada no ledger); (2) 2 ditados novos (RC-426, RC-526) — texto-síntese inexistente nos arquivos em disco, lavrado ipsis litteris com proveniência «ditado Curador 13/09» (âncora de conferência pendente da manhã do Curador); (3) delegação: 25 fichas elegíveis receberam a janela mais aderente (1 citação/ficha). Total U23: **30 fichas**. Fila A5 remanescente: 24 (16 ditado livre + 8 cujo termo só ocorre em listas/tabelas/linhas-# das fontes — não-citáveis por política de prosa). Seleção por parágrafo (fences `>` removidas; cabeçalhos/listas fora; fim de frase obrigatório; verbatim contra o texto normalizado tipograficamente, asserção por ficha; restauração byte a byte; tomllib).

## Incidente técnico sanado na U23 (honestidade de censo)
A suíte vinha sendo lida via `tail` com pipe, o que mascarou o exit-code desde a U18. Rodada sem pipe revelou duas falhas latentes, ambas corrigidas na U23: (i) **T6 x lápides** — o xor G3.3 não conhecia a exceção histórica sancionada na certidão 2.1B; isenção lavrada em código com referência à sanção (dado intocado — o envelope-história é registro); (ii) **T12 x canonico.json** — o produtor `exportar_json.py` não rodara após a guilhotina B061, e 14 fichas portavam `confianca_fonte="alta"` que só se sustentava no B061 como livro (regra `tem_livro`): JSON reexportado + TOML das 14 alinhado à regra do loader (alta→média); suíte agora verde com exit-code 0 sem pipe. Builds finais reconstruídos sobre os dados corrigidos.
