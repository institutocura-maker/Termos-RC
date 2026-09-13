# Certidão Onda 2.5 — tabelas `Termos Relacionados` geradas do cadastro (M3) · 12/09/2026

**Despacho do Curador (12/09)**: desenho **M3** (duas camadas: RELACOES tipadas + espelho t[6]; tabelas viram espelho 100% derivado) e destino das órfãs = **promover as 233 ao espelho** em despacho único (lista nominal na MESA deste dia, lavrada ANTES do APPLY).

## O que mudou
1. **Cadastro (`ferramentas/dados_termos.py`)**: +465 entradas no espelho t[6] de 259 termos (233 pares órfãos, inseridos nos dois polos, listas reordenadas canonicamente). **RELACOES intocado: 1.887 arestas · 946 termos · 102 obras.**
2. **Fichas**: tabelas geradas pela função canônica `esperado(X) = t6[X] ∪ {Y: X∈t6[Y]} ∪ polos de RELACOES`, rótulo por hierarquia (tipo da aresta como sujeito → ← tipo como objeto → rótulo editorial da própria linha → `associado`). **540 atualizadas · 122 seções criadas · 4 já canônicas.** Os 57 `## Termos Relacionados` preservaram **verbatim** linhas-candidato/auto/sem-código (linhas de tabela com alvo morto ou candidato não somem: ficam sob a tabela, e o T14 as ignora no match).
3. **Suíte**: novo **T14** — `tabela == f(cadastro)` para as 671 fichas, para sempre. (cabeçalho da suite: 14 checks; testes totais sobem p/ 20 no contador do unittest.)

## Verdes (pós-APPLY)
T14 divergentes: **0** · verificador: `OK — todo verbatim confere byte a byte` · `Base intacta: 946 · 671 · 1887` · JSON canônico `OK: 946 termos, 1887 relações` · docx/xlsx/README regenerados, sem vazamento de frontmatter, tabelas completas visíveis no espelho de leitura.

## Efeitos colaterais assumidos (e por quê)
- **Simetria**: pares antes listados por uma só ponta agora aparecem nas duas (regra aprovada "lê dos dois polos") — é a definição operacional de 0-divergências.
- **Hub Javé**: RC-001 passa a listar 145 linhas (era 0 linhas na carta: a seção não existia — criada); é o reflexo fiel do que o cadastro declara como associado a Javé. Nenhum rótulo inventado: onde não há aresta, a label vem da própria tabela ou é `associado`.
- **Aviso de baseline da suite** (`fantasmas: RC-448:B072 sanados`) — atualização do `test_baseline.json` fica lavrada para o **despacho 2.6** (rito: baseline só com visto).

## Porta do plano
`0 divergências tabela×cadastro` — cumprida e **travada** por T14. Reversão: `git revert` do commit da unidade devolve tabelas+cadastro ao estado anterior em um golpe (mudança contida num commit).
