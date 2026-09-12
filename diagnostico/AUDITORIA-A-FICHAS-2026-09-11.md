# Auditoria Interna — Frente A: Fichas (conteúdo) — 11/09/2026

Leitura pura. Universo: 671 fichas. Complementa o censo quantitativo com 5 testes de coerência interna.

## A1. Mesma fonte em 2+ blocos da mesma ficha: **19 fichas**
Casos: RC-001 (67 blocos, repete ['P2022-12-17']); RC-009 (65 blocos, repete ['P2021-12-04']); RC-395 (21 blocos, repete ['P2025-02-16']); RC-091 (18 blocos, repete ['P2025-03-15']); RC-152 (17 blocos, repete ['P2021-12-04']); RC-161 (17 blocos, repete ['P2025-03-15', 'P2024-11-09']); RC-604 (15 blocos, repete ['P2025-02-16']); RC-378 (11 blocos, repete ['P2025-03-15']); RC-612 (10 blocos, repete ['P2025-03-15']); RC-655 (10 blocos, repete ['P2024-11-30'])

Leitura: volume baixo, mas concentrado nos dossiês gigantes (001, 009). Cada repetição é um candidato a fusão de blocos — sobreposição de conteúdo provável, não provada (exige leitura humana).

## A2. Blocos fora de ordem cronológica: **255 fichas (38,0%)**, 806 inversões
Leitura: confirma o diagnóstico do RC-009 como sistêmico — a ordem dos blocos é a ordem de *processamento dos ciclos*, não a cronologia das fontes. Não é corrupção, é ausência de convenção. Proposta: ordenar blocos por data da fonte (B antes de P? ou tudo cronológico?) como passo da Onda 2.

## A3. Citações fora de `## Citações-chave`: **412 fichas (61,4%)**; 2925/2955 citações (99.0%) fora da seção; 249 fichas sequer têm a seção
Leitura: a seção `Citações-chave` não é o repositório das citações — os blocos são. Duas normalizações possíveis: (a) esvaziar o conceito (citação mora no bloco-fonte, seção some do modelo); (b) curar a seção como 'melhores citações' (índice, não arquivo). Recomendo (b) para fichas 🟢, (a) para as demais.

## A4. Divergência relacionados tabela×cadastro: **544 fichas (81,1%)** — 2665 relações só-na-tabela, 6578 só-no-cadastro
Leitura: **o achado mais grave da Frente A**. Há duas listas de relações por termo que divergiram em 4 de cada 5 fichas. Causa provável: a tabela evolui por edição editorial, o cadastro por script de leva — sem reconciliação. Proposta: declarar o cadastro como verdade-mestra, gerar a tabela a partir dele (Onda 1), e auditar as 2665 relações só-na-tabela antes (podem conter conhecimento real a incorporar).

## A5. Fichas 🟢 sem `## Citações-chave`: **163 (34,0% das 479 verificadas)**
Leitura: 1 em cada 3 fichas verificadas não tem seção de citações — o selo 🟢 hoje atesta *revisão do cadastro*, não *lastro citacional visível*. Proposta: tornar 'Citações-chave presente' (ou 'lastro explícito nos blocos') critério de 🟢 daqui em diante; as 163 entram numa fila de complementação, sem perder o selo (não-retroatividade).

## Síntese da Frente A
As fichas têm **4 verdades paralelas**: blocos (conteúdo real), tabela de Fontes (27% quebrada), tabela de Relacionados (81% divergente do cadastro) e seção de Citações (61% esvaziada). Nenhuma está errada isoladamente — o problema é a ausência de hierarquia declarada entre elas. Recomendação central: **declarar a hierarquia** (cadastro > blocos > tabelas/seções derivadas) e derivar o resto por script.