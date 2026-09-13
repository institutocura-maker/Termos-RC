# CERTIDÃO — P2026-02-28 MATERIALIZADA (U19) — 2026-09-12

**Objeto:** recepção e canonização da apostila revisada de «Os Desafios da Transição Planetária — Aprofundamento» (Braga, 28/02/2026), encerrando a pendência "DOCX aguardando revisão" herdada da Onda 2.2.

## Despacho e entrega
- Curador (12/09): "Subi o DOCX revisado e ele não tem alteração. Está ok." — entrega via GitHub na branch (commit `c104f4b`, "Add files via upload"): `Apostila_2.2 - …(Aprofundamento).docx` (48.367 B) + `apostila.md` (24.726 B).
- O anexo prometido no chat não havia chegado ao sandbox; a entrega pelo git foi confirmada com o Curador antes de qualquer medida (nenhum placeholder de pasta foi criado — o T8 reconhece obras pelo NOME da pasta e pasta vazia falsificaria o censo).

## Prova de "não tem alteração"
- Dif formato-independente (canone alfanumérico) DOCX↔MD: similaridade 0,94; as divergências são reflow de listas/numeração, cabeçalhos e 14+17 linhas de rótulo — **nenhum fato novo**; itens exclusivos do MD verificados como reformatação do mesmo conteúdo.
- Consequência: as 4 fichas-âncora **RC-667, RC-668, RC-669, RC-670 ficaram INTACTAS** (zero byte); nenhum `## Fontes` novo; corpus TOML intacto (671 fichas).

## Canonização (convenção da casa)
- Pasta `apostilas/CONCLUIDAS/2026-02-28_os_desafios_da_transicao_planetaria_aprofundamento/`: cópia byte a byte dos 2 artefatos (sha256 `70066067d059…` docx / `945e262cb509…` md, conferidos no ato) + `ficha_ingresso.md` (origem, chancela, shas, vínculos B061/RC-667..670).
- **Base externa declarada:** o `original.txt` (STT bruta) referenciado pelo cabeçalho da apostila — SHA declarado `4e3ed5f254d3df0156…` — NÃO integra o git; os localizadores `L##` da apostila referem-se a ele. Fica à mesa do Curador eventual canonização do bruto; nada foi inventado nem renomeado.
- Índice-mestre: linha 28/02/2026 atualizada em `INDICE-PALESTRAS.md` (raiz) E `apostilas/INDICE-PALESTRAS.md` (a "to-do" que o próprio MD trazia, cumprida).
- **Expurgo nº 23** (`backups/REGISTRO-LIMPEZA-2026-09-12-23.json`): os 2 brutos saem da caixa só após sha conferido contra o destino canônico; os originais vivem também no histórico do commit `c104f4b`.

## Efeito no baseline e portas
- `test_baseline.json`: 127 → **123** fantasmas (removidos EXATAMENTE `ficha:RC-667..670:P2026-02-28`; 7 B072 remanescentes intactos); nota de levantação lavrada.
- Suíte: 20 testes verdes (T8 varre a pasta nova; sem sanção). Verificador: base intacta 946/671/1887. README reconstruído (946/671/1887/102). DOCX/XLSX do corpus NÃO regenerados — zero mudança em `termos/` (paridade declarada).
- Portões G1 (verbatim), G2 (RAG ≤6k), G3 (metadado só no TOML): intocados — a apostila é documento-fonte, não ficha.

## Pendências do diário (estado após U19)
1. **P7 — PAUSADO** (ordem do Curador); pendência técnica lavrada: `motor.py` ainda EMITE envelope — ao reabrir deve gerar o bloco `+++` canônico (molde: `fm_de` da expansão 2.1-B).
2. **Fila A5** — 82 fichas sem citação.
3. **B061** — v3.0 (materializada 1.3) × v1.0 (arquivo físico).
4. Opcional à mesa: canonizar a STT bruta `original.txt` (4e3ed5f2) se o Curador desejar âncora local dos localizadores L##.
