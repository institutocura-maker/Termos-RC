# Certidão Onda 2.2 — consolidação dos dossiês gigantes (12/09/2026)

**Escopo chancelado** (despacho `u12_u13`, Curador): mapeamento aprovado com re-síntese nominal das Definições de RC-001 e RC-009; execução bifurcada em duas unidades.

## O1 · Quitação do "A1" (fusão de duplicatas)
Censo em três granularidades (título de seção exato · bloco ≥200c com similaridade >0.85 via difflib · parágrafo ≥180c exato/quase-exato) nas 4 cartas: **zero duplicatas**. O item do plano está extinto pelos mutirões F036–F042 e remapeamentos P5b — nada foi fundido porque nada restava a fundir.

## O2+O4 · U12 (`2a2e5ce`) — mecânica pura
- Ordenação canônica imposta: Definição → Contexto/Origem → Etimologia → (Citações-chave) → Termos Relacionados → Seres Associados → **Fontes** → Ampliações (**B por número, depois P por data cronológica crescente**, extras depois) → Atualizações/Observações → Notas (intocadas; competência da 2.4).
- Reparo estrutural: as 2 `Ampliação` órfãs da RC-001 (P2024-03-17, P2024-02-04) voltaram do pós-Fontes para o bloco de ampliações.
- Quebras RAG: `Ampliação — P2025-02-22` de RC-009 (7.585c) e RC-072 (6.250c) cortadas em fronteiras de linha com `### Parte N` neutro. **Gate G2.2 re-rodado: zero bloco >6.000c em qualquer uma das 4 cartas, Fontes incluído.**
- Prova de verbatimidade: cada bloco final, com os marcadores removidos, restaura **byte a byte** o bloco original (assert por título); permuta validada por multiconjunto de blocos; normalização de linhas em branco declarada (Δ −29…−43c/ficha, só espaçamento).
- Suíte 19 OK · verificador 649/8.540/8.250/0 (todo verbatim confere) · docx/xlsx/README regenerados, sem vazamento de frontmatter.

## O3 · U13 — re-síntese curatorial (este commit)
- **RC-001** Definição: 519c → 284c. Nota obsoleta *"(Definição preliminar baseada em B031; a refinar com as obras primárias.)"* saiu do corpo da definição; a definição inteira anterior foi **arquivada verbatim** em `## Observações → ### Definição anterior a 2.2 U13`.
- **RC-009** Definição: 577c → 500c (compressão sem fato novo; todos os nomes/códigos citados — Orbum, Capela, biodemo, radiata, Mohen So, Mavatna, Aya/Aye, B031 — verificados presentes na carta no dry-run).
- RC-072 (385c) e RC-104 (205c): mantidas — já eram sínteses; só o layout do U12 as alcançou.
- Gates: definição antiga sobrevive verbatim no arquivo; frontmatter byte-intacto; contagem de linhas auditada; suíte OK, verificador "Base intacta", builds regenerados.

## Incólume
Registro (`dados_termos.py`), RELACOES, `relacoes/`, JSON canônico (conteúdo de carta fora do registro), fichas não-gigantes (667) e as 6 fichas-piloto não-gigantes. Onda 2 continua: 2.3 citações-chave · 2.4 notas de processo · 2.5 tabela gerada · 2.6 despachos pontuais · expansão TOML (pausa do Curador) · P7 (pausado).
