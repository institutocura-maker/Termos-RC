# Dossiê do gap «termos sem ficha» — censo 2026-09-13 (U38, leitura; zero mudança na Base)

**Pedido do Curador (13/09, ao devolver a P7m):** «depois precisamos explorar melhor o fato dos termos
não terem fichas». Executado como dossiê exploratório — nenhum byte da Base alterado; decisão de rota fica
com o senhor.

## Método (reproduzível)
Varredura invertida do corpus processado (251 arquivos: `livros/*/original.txt`, `apostilas/CONCLUIDAS/*`,
`ciclos/*/original.txt` e `translado/*.txt`), chave = nome canônico sem parênteses/barras/apelidos,
sem acentos, case-insensitive. Para cada um dos **273 códigos com `ficha=False`**: nº de ocorrências,
comprimento da maior linha portadora (prosa real ≥ 90 chars vs. lista/sumário), e se a ocorrência está
na FONTE DECLARADA no cadastro. Máquina-legível: `CENSO-GAP-FICHAS-2026-09-13.json`.

## Famílias
| Família | n | Significado | Remédio natural |
|---|---|---|---|
| A. alias-variação | 6 | sombra de duplicata com aresta `variação` para ficha existente | baixa administrativa (fechar como alias, sem ficha) |
| B. prosa citável na fonte declarada | 71 | o termo vive em prosa na própria fonte — a ficha não nasceu por falta de lastro, e sim de processo | materialização com verbatim (precedente U30) |
| C. prosa fora das fontes declaradas | 41 | existe prosa, mas em obra não listada no cadastro | retificar `fontes` (despacho) e promover a B |
| D. só estrutural / hard-wrap | 104 | só listas/sumários — OU prosa fraturada em linhas curtas (a doença do RC-367 na U30: real, mas não-citável intra-linha) | refinamento: reconstruir parágrafos e separar «lista de verdade» de «prosa fraturada» |
| E. não achado no corpus | 40 | o nome não ocorre em NENHUM arquivo processado | auditoria de atribuição (fonte não processada? tradução alternativa? fantasma do censo B031?) |
| F. nome ambíguo | 11 | chave curta/genericamente frequente (>300 occ) | qualificar o nome canônico ANTES de qualquer ficha |

## Onde o gap mora (top-10 subcategorias)

- 1.3 Extraterrestres / Raças cósmicas: **32**
- 2.2 Leis e princípios cósmicos: **22**
- 2.6 Ética / Carma / Compromissos: **22**
- 2.5 Propósitos / Destinos: **16**
- 1.6 Figuras humanas (históricas/míticas): **15**
- 3.3 Localidades terrestres: **14**
- 7.2 Eras / Épocas / Ciclos: **14**
- 4.1 Processos biológicos / genéticos: **12**
- 2.4 Espiritualidade / Doutrina: **11**
- 6.3 Dinastias extraterrestres: **10**

## Os 18 suspensos das levas m/n (V chancelado, ficha pendente) — recorte imediato

| Código | Termo | Família | Ocorrências | Nota |
|---|---|---|---|---|
| RC-027 | Astréia | B | 28 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-030 | Atlantes | B | 84 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-050 | Demônios | B | 199 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-051 | Despina | B | 38 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-053 | Deuses (os dois tipos) | F | 1814 | nome precisa de qualificador (ex.: «Deuses (os dois tipos)» é categoria, não termo) |
| RC-076 | Logos / Logos Criadores | F | 1448 | nome precisa de qualificador (ex.: «Deuses (os dois tipos)» é categoria, não termo) |
| RC-097 | Seres Extrafísicos | B | 105 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-100 | Seres Espirituais | B | 31 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-214 | Agente do Mais Alto | D | 8 | remédio A5: nota estrutural ou ditado livre |
| RC-215 | Emissários da Espiritualidade Maior | D | 6 | remédio A5: nota estrutural ou ditado livre |
| RC-222 | Filhos das Estrelas | D | 8 | remédio A5: nota estrutural ou ditado livre |
| RC-246 | Dez Sagrados (primeira geração do Criador) | D | 2 | remédio A5: nota estrutural ou ditado livre |
| RC-248 | Viajores da Rebelião | D | 1 | remédio A5: nota estrutural ou ditado livre |
| RC-304 | Deucalião | B | 34 | materializável já (garimpo de citação intra-linha na fonte declarada) |
| RC-306 | Apolo | F | 378 | nome precisa de qualificador (ex.: «Deuses (os dois tipos)» é categoria, não termo) |
| RC-309 | Ordem dos Indecifráveis | D | 1 | remédio A5: nota estrutural ou ditado livre |
| RC-368 | Assessoria Cósmica (equipes espirituais de Jesus | D | 5 | remédio A5: nota estrutural ou ditado livre |
| RC-390 | Espíritos comunicantes do Grupo Atlan | E | 0 | auditar atribuição antes |

**Leitura do caso RC-053/RC-076/RC-306 (F):** «Deuses», «Logos», «Apolo» batem centenas de vezes porque
são palavras do idioma, não rótulos de conceito único — o censo B031 os registrou como termos, e sem
qualificador canônico uma ficha seria verbete-dicionário. Proposta: fila de qualificação no ditado.

## B — amostra das 71 prontas (top-15 por ocorrência)

| Código | Termo | Fontes | Occ |
|---|---|---|---|
| RC-065 | Frota Norte | B031,B017,B018 | 208 |
| RC-050 | Demônios | B031,P2025-06-26 | 199 |
| RC-066 | Genos | B031 | 152 |
| RC-077 | Lokas | B031,B021,B060 | 134 |
| RC-044 | Cultura Demo | B031,B044 | 116 |
| RC-032 | Benem | B031,B017,B018 | 97 |
| RC-048 | Demiurgo | B031 | 89 |
| RC-030 | Atlantes | B031 | 84 |
| RC-073 | Keshava | B031,P2026-04-02 | 78 |
| RC-051 | Despina | B031,B060,B089 | 38 |
| RC-022 | Antlar | B031 | 34 |
| RC-027 | Astréia | B031,B060,P2023-05-21 | 28 |
| RC-045 | Daemon | B031 | 16 |
| RC-082 | Nephilins | B031,B017,B018 | 12 |
| RC-069 | Ion Crom | B031 | 3 |

## Limitações honestas do censo
1. **D não separa lista real de prosa fraturada** (hard-wrap tipo B011) — exige passe de reconstrução de
   parágrafos; estimado que uma fração relevante dos 104 migre para B materializável.
2. Ocorrência ≠ definição: família B garante que HÁ prosa citável, não que o autor DEFINE o termo ali —
   cada materialização passa pelo mesmo crivo da U30 (sentença completa intra-linha + declaração).
3. Linha ≥90 chars em arquivos de linha única (alguns `original.txt` de apostila são um blob só) é
   fraqueza do detector a favor de B; a verificação manual por ficha corrige.
4. E=40 inclui nomes com variantes ortográficas (STT degradou «Maré» a «Mar é» no caso U30; aqui o
   detector usa só a grafia canônica) — auditoria de grafia é o passo seguinte dessa família.

## Rotas sugeridas (cada uma = 1 unidade, 1 despacho seu)
- **R1 · Piloto suspenso-B:** materializar as 7 fichas dos suspensos em B (RC-027 Astréia, RC-030 Atlantes,
  RC-050 Demônios, RC-051 Despina, RC-097 Seres Extrafísicos, RC-100 Seres Espirituais, RC-304 Deucalião)
  com o V já chancelado — fecha o capítulo HOLD das levas m/n na parte citável e calibra o método.
- **R2 · Refinamento D:** reconstrução de parágrafos e recorte lista-de-verdade × prosa-fraturada.
- **R3 · Auditoria E:** 40 nomes fora do corpus — retificar fontes/gramas ou assumir fantasma (nota na
  ficha do censo B031, sem deletar).
- **R4 · Fechar A:** 6 aliases-variação baixados administrativamente (canônico citável, código imutável).
