# Mesa Onda 2.6 — despachos pontuais (12/09/2026)

## Mesa 1 · C6 — 4 pares de nomes duplicados no cadastro

| Par | Situração (hoje) | Leitura dos fatos | Opções |
|---|---|---|---|
| RC-164 ↔ RC-449 | ambos 🟢, fichas 6.293c/3.838c, categoria idêntica (Conceitos Cosmológicos), 11×8 seções, similaridade 0.42, ref. cruzada já existente | conteúdo distinto o bastante para 2 dossiês; duplicata de *nome*, não de *ouro* | manter com remissiva · fundir |
| RC-203 ↔ RC-314 | 203 = `candidato` **sem ficha** (`ficha=False`); 314 = 🟢 6k+ seções | 203 é entrada de cadastro à espera, não duplicata material | manter como alias-remissiva ao 314 · (fundir não tem o que mover) |
| RC-581 ↔ RC-872 | 581 = 🟢 6.825c/14 seções; 872 = 🟢 1.354c/2 seções (sim 0.20); 872 estava na fila A5 e ganhou promoção de espelho no 2.5 | 872 é toco (stub) recente; fusão verbatim barata: mover o bloco de 872 p/ `## Ampliação — 2.6 (origem RC-872)` de 581 e deixar em 872 lápide-ponteiro (cadastro intocado, RELACOES/espelho preservados) | manter · **fundir 872→581** com lápide |
| RC-898 ↔ RC-936 | 898 = 🟠 em análise (3.948c); 936 = 🟡 provisório, **Anel C do GKA (RC-935..942)** | anelar GKA é regra de anel (obra de apoio, fonte secundária) — fundir contaminaria o lastro primário de 898 | manter com remissiva declarando o anel · (fundir viola precedente do Anel C) |

Recomendação do agente: **manter os 4 com remissivas padronizadas em `## Observações`** + **fusão opcional 872→581** (única onde o ouro cabe num bloco só).

## Mesa 2 · P2023-12-25 — o caso F044
17 citações `P2023-12-25-01..05` em fichas (RC-005/072/193/273/280/376/565/647/752/862/887/904/942-946), hoje sancionadas no baseline. O curso existe e está CANONE — `ciclos/F044_misterios-da-vida-de-jesus/` (5 traduzidos + brutos, registro de limpeza nº 22, transcrição revisada contra áudio) — mas `ciclo.toml` lavra: `codigos_p = "datas reais das 5 aulas (metadatas do docx NÃO valem)"`. A pasta não-datada é o único motivo do fantasma: T8 materializa por nome `P?AAAA-MM-DD`.
Opções: **(a)** as 5 aulas são de 2023-12-25 → renomear `ciclos/P2023-12-25_F044_misterios-da-vida-de-jesus` (fecha 17 fantasmas num `git mv` + limpa o baseline); **(b)** datas reais ≠ essa (o Curador detém-nas; forneo no texto do despacho, uma por aula) → corrijo siglas em fichas/registro + renomeio; **(c)** sem data confirmada ainda → mantido "aguarda-verificação-de-áudio" na contabilidade do baseline.

## Mesa 3 · P2026-02-28 (RC-667..670)
O `INDICE-PALESTRAS.md` declara: "Base e apostila concluídas · parte de B061 · DOCX aguardando revisão". A fonte-mãe B061 foi materializada na Onda 1.3, mas a apostila da data específica não tem pasta própria. 4 citações no baseline. Opções: **(a)** manter sancionado (a declaração do índice é o lastro honesto; pasta nasce quando o DOCX revisar); **(b)** materializar agora extraindo de B061 a parte correspondente para `apostilas/CONCLUIDAS/2026-02-28_os-desafios-da-transicao-planetaria/` (risco: recorte manual = curadoria de corpo — prefiro com instrução nominal); **(c)** declarar no índice o status `fontes=declaração` e seguir.

## Mesa 4 · Baseline da suíte (rito T7/T8)
Aviso atual: `fantasmas` sanados = `['ficha:RC-448:B072']` (a ficha 448 deixou de citar B072 na carta — evento legítimo das ondas). Rito: item sanado vira AVISO pedindo atualização, nunca falha silenciosa. Opções: **(a)** atualizar o `test_baseline.json` removendo SÓ o sanado (deixo 22 B072, 17+4 P como estão); **(b)** não atualizar (o aviso continua pedindo — registro vivo de que a 448 mudou). Recomendo **(a)**: baseline é fotografia com data, não fóssil; a remoção documenta a cura.

## Execução sob despacho (U17)
Mesa 1: inserir bloco de remissiva padrão nas fichas do(s) par(es) mantido(s) (aditivo, gate byte); fusão 872→581 = mover bloco verbatim (gate: multiconjunto de blocos preservado + lápide). Mesa 2(a): `git mv` da pasta + verificação T8. Mesa 4: patch cirúrgico do json (só o item sanado; `gerado_em` atualizado). Suite + verificador + builds; certidão 2.6 fecha a ONDA 2.
