# DIAGNÓSTICO DE BASELINE DA BASE TERMINOLÓGICA RC — 03/09/2026

> **Finalidade:** linha de base mensurável da Base de Conhecimento (KB) antes de iniciar a
> **Esteira de Consolidação**. Serve para (a) dimensionar o trabalho, (b) monitorar progresso e
> (c) detectar regressões. Números reproduzíveis via `ferramentas/dados_termos.py`.

**Branch:** `arena/01a06429-termos-rc` · **HEAD do diagnóstico:** `40cef9c` (após integração do
`22-GLOSSÁRIO.txt`). Fonte dos dados: `dados_termos.py` (TERMOS + RELACOES).

---

## 1. Volumes globais

| Métrica | Valor |
|---|---|
| Termos (códigos RC-001…RC-926, sem lacunas) | **926** |
| Fichas materializadas em `termos/` (`ficha=True`) | **620** |
| Sem ficha (`ficha=False` — fila de materialização) | **306** |
| Relações (RELACOES) | **1.869** |
| Tipos de relação distintos **em uso** | **279** |
| Obras/fontes (contagem declarada nos espelhos) | 102 |

---

## 2. Distribuição de STATUS

| Status | Total | com ficha | sem ficha |
|---|---|---|---|
| ⚪ candidato | **396** | 336 | 60 |
| 🟡 provisório | **530** | 284 | 246 |
| 🟠 em análise | 0 | 0 | 0 |
| 🟢 verificado | 0 | 0 | 0 |

**Leitura crítica (achados):**
1. **Nenhum termo passou de `provisório`.** Os níveis `em análise` e `verificado` nunca foram
   utilizados na tabela-mestra — o "ciclo de maturação" está, na prática, desativado.
2. **`candidato` perdeu o significado canônico.** O `01-ficha-modelo.md` define candidato como
   "só aparece no índice; sem ficha ainda" — porém **336 candidatos têm ficha**. Na prática,
   candidato virou sinônimo de "baixa confiança / adicionado recentemente". É preciso redefinir
   (ou tolerar) essa semântica antes de qualquer elevação.

---

## 3. Relações — saúde do vocabulário

- **279 tipos de relação distintos**, mas a distribuição é muito concentrada e um tipo é um
  "guarda-chuva" de baixa informação:
  | Tipo | ocorrências |
  |---|---|
  | `relaciona-se-a` | **885 (47%)** |
  | `é-um` | 117 |
  | `envolve` | 102 |
  | `variação` | 70 |
  | `inclui` | 64 |
  | `associado-a` | 40 |
  | … (~273 tipos restantes) | ~1 cada |
- O vocabulário controlado (`02-vocabulario-controlado.md`) lista ~11 tipos; a base real usa 279.
- **Recomendação de baseline:** fixar `relaciona-se-a` em ~885 e os tipos singulares em ~273 como
  *dívida estrutural* a reduzir (ver despacho), não como algo a aceitar permanentemente.

---

## 4. Fontes (ocorrências totais nos campos `fontes`)

| Família | ocorrências |
|---|---|
| `B###` (livros originais) | 1.220 |
| `P####-##-##` (palestras/STT) | 3.111 |
| `ART-*` | 22 |
| **Família F (refatoradas) — proposta** | **0** (a criar) |

**Achado:** não existe hoje nenhum mecanismo (sigla/taxonomia) para **fontes refatoradas** —
exatamente o tipo de material que o novo processo quer usar. Sem ele, não há rastreabilidade.

---

## 5. Duplicações de nome-base detectadas (candidatas a consolidação)

Agrupando por nome-base (antes do primeiro parêntese), há **6 grupos com ≥2 códigos**. Cada grupo
exige triagem (mergir vs. manter como nuances distintas vs. um é variação):

| Nome-base | Códigos | Leitura preliminar |
|---|---|---|
| Conselho dos Cinco | RC-043 (prov., ficha=False, B031) · RC-501 (cand., ficha=False, B061) | provável duplicata → consolidar |
| Val Aten | RC-115 (prov., ficha=False, B031) · RC-502 (cand., ficha=False, B061) | provável duplicata → consolidar |
| Choque de Realidade | RC-867 (cand., ficha=False, P2022-11-26) · RC-898 (prov., ficha=True, P2023-10-15/18) | **RC-898 criado em 02/09** duplica RC-867 → consolidar |
| Criaturas-ferramenta | RC-164 (prov., ficha=True) · RC-449 (prov., ficha=True) | investigar se mesma coisa |
| Fenômenos Denunciadores do Fim | RC-203 (cand., ficha=False) · RC-314 (prov., ficha=True) | provável duplicata |
| Favor Divino | RC-063 (prov.) · RC-332 "Favor Divino (conceito invertido)" (prov.) | possível nuance legítima |

> Estas duplicatas surgem porque a adição de novos termos (RC-889…RC-926, e antes RC-857…RC-888)
> não checou automaticamente contra o nome-base já existente. A **Esteira de Consolidação deve
> incluir um passo obrigatório de "anti-duplicação"** (busca por nome-base/sinônimos antes de
> criar código novo).

---

## 6. Indicadores recomendados para acompanhamento

| Indicador | Hoje | Meta (tendência) |
|---|---|---|
| `em análise` + `verificado` | 0 | subir |
| `relaciona-se-a` (%) | 47% | descer |
| grupos de nome duplicado | 6 | descer |
| fontes com sigla de origem (rastreáveis) | 100% (B/P/ART) | manter 100% + incluir F |
| divergências abertas (ledger) | não mensurado | criar e manter ≤ X abertas |
| fichas `candidato` com ficha | 336 | reclassificar ou redefinir status |

---

## 7. Como re-rodar

```bash
cd /home/user/Termos-RC
python3 - <<'PY'
import sys,collections,re
sys.path.insert(0,'ferramentas'); import dados_termos as D
T=D.TERMOS
print(collections.Counter(t[4] for t in T))
print(collections.Counter(t[4] for t in T if t[7]))
print(collections.Counter(r[1] for r in D.RELACOES).most_common(6))
PY
```

**Nota:** este diagnóstico é um *retrato*, não um veredito. Duplicatas e "problemas" aqui listados
devem ser **confirmados caso a caso** (conferindo fichas e fontes) antes de qualquer alteração —
nunca mesclados às cegas.
