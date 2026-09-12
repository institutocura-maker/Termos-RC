# Mapeamento 2.2 — dossiês gigantes 001/009/072/104 (proposta p/ bisturi do Curador · 12/09/2026)

Censo completo em anexo (números de hoje, scripts do turno): **72–74 seções por ficha · 51–107KB de carta · ZERO duplicatas** (título exato, bloco >0.85 e parágrafo exato/quase-exato). O item "fusão dos blocos repetidos (A1)" do plano está **extinto pelos antecessores** (mutirões F036–F042 + remapeamentos P5b) — nada a fundir; o plano recebe aqui a sua **certidão de quitação**.

O que os dados mostram de fato, e vira operação proposta:

## O1 — Quitação do "A1" (0 mutações)
Registro do achado para a história: duplicação em bloco não existe mais nas 4 cartas. Aceite do plano ("4 fichas com blocos únicos") já satisfeito.

## O2 — Ordenação canônica (movimento de blocos inteiros, verbatim)
Regra-proposta (determinística; Curador pode alterar antes da execução):

1. **Ordem das seções-padrão:** `Definição Sintética` → `Contexto / Origem` → `Etimologia / Grafias` → (`Citações-chave` se houver) → `Termos Relacionados` → `Seres Associados` → `Fontes` → **`Ampliação — *`** → `Observações` → `Nota — *` (Notas de processo ficam onde estão: competência da 2.4, não se movem agora).
2. **Dentro das Amplações:** livros primeiro (por sigla `B###` ascendente — a impressa é o lastro), depois palestras (`PAAAA-MM-DD` cronológico crescente — "enredo no tempo", N3 da pedagogia), por último `ART-*`/extras.
3. **Reparos pontuais:** RC-001 tem 2 `Ampliação` (P2024-03-17, P2024-02-04) **depois de `## Fontes`** → voltam para o bloco de ampliações; RC-072/RC-104 têm linha em branco após o título da seção (`## Definição Sintética\n\nFigura...`) → normaliza (única mutação de *layout* aceita fora de movimento).

Mecânica segura (G1.1/G1.2): ordenar = permuta de blocos de seção **byte-íntegros**; gate = multiconjunto de blocos idêntico antes/depois + tamanho total igual (exceto as 2 trocas de linha em branco declaradas). Dry-run imprime a nova TOC de cada ficha antes de escrever.

## O3 — Re-síntese das Definições (prosa nova SÓ aqui, frase a frase lastreada)
- **RC-001 (519c → ~340c):** REMOVE do fim a nota de processo obsoleta *"(Definição preliminar baseada em B031; a refinar com as obras primárias.)"* — a refinação aconteceu (72 seções, B001/B002/B033/B034/B036 no lastro); a frase removida migra verbatim para `## Observações` (nada se perde; G1). Proposta de corpo:
  > Nas RC, Javé é o Deus bíblico do Antigo Testamento — Jeová/Yahweh, Alá, Brahma, Caos, Pangu e Atom nas outras tradições (B031). É o **Criador "caído"**, e por isso chamado Criador e não Deus: o protagonista do drama cósmico que ele mesmo gerou, do isolamento prometido à reintegração.
- **RC-009 (577c → ~400c):** compressão sem fato novo: Cristo Cósmico + Suserano deste universo; biodemo/radiata governando de Orbum (Capela); avatar de Mohen So, avatar de Vishnu, mesmo espírito de Jesus; "pai biológico" de Jesus pelo DNA cedido às Famílias Aya/Aye (B031).
- **RC-072 (385c) e RC-104 (205c):** **manter** — já são sínteses; só o layout (O2.3).

Aceite de conteúdo é curatorial: as duas reescritas acima só entram com visto nominal do Curador (código executa `old→new` com assert de que cada nome/código citado existe na carta).

## O4 — Quebras RAG (>6k sem subtítulo)
- `RC-009 / Ampliação — P2025-02-22` (7585c) e `RC-072 / Ampliação — P2025-02-22` (6250c): inserir `### Parte 2` (e `### Parte 3` se necessário) no parágrafo que seguir a ~5.000c, **sem mover nem reescrever prosa** (corte em fronteira de parágrafo; marcador neutro, não-editorial). Gate G2.2 re-rodado pós-edição: nenhum bloco >6.000c.

## Efeito somado
4 fichas com TOC canônica, ampliações em tempo cronológico, zero >6k, definições sínteses com a nota de processo arquivada em Observações; RELACOES/canônico/registro **intactos** (2.2 é operação de carta); builds regenerados (docx/xlsx/README) e suite 19 verde em cada commit. Execução em **2 unidades**: U12 = O2+O4 (mecânica pura, sem texto novo); U13 = O3 (prosa curatorial, só com visto nominal).
