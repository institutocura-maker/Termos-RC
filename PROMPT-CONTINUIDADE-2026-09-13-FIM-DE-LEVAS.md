# PROMPT DE CONTINUIDADE — Sessão Arena.ai 13/09/2026 (P7 concluído · gap de fichas em aberto)

**Repositório:** `institutocura-maker/Termos-RC`
**Branch da sessão:** `arena/01a0960b-termos-rc` · **HEAD `f26dfe2`** (U39, pushado, árvore limpa)
**Agente entrante:** a sessão nova nascerá branchada deste head — não há nada NÃO-commitado por trás.

---

## 0. Bootstrap de leitura (nesta ordem, e só depois fale com o Curador)

1. `STATE-MIRROR.md` (raiz, versionado) — números oficiais, proteções, doutrinas, fila. Linha-9 é o resumo autoritativo.
2. Este arquivo — o estado da fase P7/gap.
3. `diagnostico/CENSO-GAP-FICHAS-2026-09-13.md` + `.json` — o dossiê do gap (rota aberta pelo Curador).
4. Validação de partida: `python3 ferramentas/verificar_verbetes.py` → deve imprimir **Base intacta: 946 termos · 673 fichas · 1887 relacoes**.

---

## 1. ONDE PARAMOS — a esteira de chancela P7 terminou a fila de temas

- **Levas aplicadas (unidades U25–U39, todas com certidão em `diagnostico/`):**
  - U25 · motor `fm_toml` (pendência 2.1B cumprida) + T15 na suíte (guarda byte a byte do frontmatter das 671→673 fichas).
  - U26 · resíduo dos retornos P7a–j sanado (148 V; RC-833 HOLD mantido por despacho; RC-769 fundido→RC-064 por remissiva-lápide; RC-024 averbada).
  - U27/U29/U34/U36/U39 · as levas novas no ciclo «agente gera planilha → Curador devolve V/X/?»: **P7k** (4.4, 27 V) · **P7l** (4.4-2, 13+2) · **P7m** (1.5, 9+9) · **P7n** (1.8, 8+9) · **P7o** (7.5, 9+7). Planilhas e retornos canonizados em `chancela/P7-*.csv`/`*_retorno.csv` (10 pares antigos + 5 novos ciclos).
  - U30 · materialização despachada de RC-367/RC-537 (precedente vivo do remédio da família B — citação verbatim intra-linha + declaração).
  - U32 · **reparo de integridade**: 9 termos do cadastro carregavam rel colado dentro de `fontes` (herança pré-TOML); limpos, órfãs realocadas ao espelho `t[6]` com propagação M3. Se mexer em linha de `dados_termos.py`, **ancore sempre na região `TERMOS = [ … ]`** — as linhas RELACOES começam igual.
- **Estado numérico:** base **946 termos · 673 fichas · 1887 relações · 102 obras**; status **60⚪ · 236🟡 · 102🟠 · 548🟢**; baseline `[REVISAR]` **123**; suíte `ferramentas/test_suite.py` **21 testes** (rodar SOLA com `; echo EXIT=$?` — pipe engole FAIL).
- **HOLD atual (`chancela/HOLD.csv`):** 40 linhas-parse, sendo **25 termos com V chancelado e suspenso** (9+9+7 das levas m/n/o) à espera da exploração do gap — o V deles NÃO se perdeu; está guardado aqui com a pauta do Curador lavrada no `motivo`.

## 2. A ÚNICA FILA VIVA — o gap «273 termos sem ficha»

Dossiê U38 (`diagnostico/CENSO-GAP-FICHAS-2026-09-13.md`) classifica com método reproduzível e json máquina-legível:
- **A · alias-variação: 6** → baixa administrativa (R4).
- **B · prosa citável na fonte declarada: 71** → materialização com verbatim intra-linha (precedente U30). **R1 · piloto:** os suspensos que caem em B = **8** (RC-027, RC-030, RC-050, RC-051, RC-097, RC-100, RC-304 + RC-090 da P7o) — V já chancelado, só falta a ficha nascer.
- **C · prosa fora das fontes declaradas: 41** → retificar `fontes` (despacho) e promover a B.
- **D · só-estrutural/hard-wrap: 104** → refinamento R2 (separar lista-real de prosa-fraturada por reconstrução de parágrafos); suspenso-B não resolve D — D pede nota estrutural (padrão das 8 da A5) ou ditado livre.
- **E · não-achados no corpus: 40** → R3 auditoria de atribuição/grafia (ex.: «Mar é Cósmica» era STT degradado).
- **F · nomes ambíguos: 11** (Deuses/Logos/Apolo…) → qualificar o nome canônico antes de qualquer ficha.

**Regra de ouro da materialização (herança U30 + pacto):** o motor não inventa conteúdo; citação só **verbatim intra-linha** conferida byte a byte contra o `original.txt`; frontmatter SEMPRE regerado por `motor.fm_toml` (nunca à mão); ficha nasce com «Materialização (não é criação)» + Escopo e evidência + tabela Termos Relacionados (espelho ∪ arestas, dos dois polos — T14 cobra).

## 3. Pendência menor e opcional

- Canonização da STT bruta 2026-02-28 (declarada EXTERNA ao git na ficha de ingresso; `apostilas/CONCLUIDAS/2026-02-28_…/` tem a canonização parcial). Só se o Curador pedir.

## 4. RITO (inadiável — o Curador cobra)

- 1 unidade = 1 commit + push na branch da sessão; **nunca `--amend`** (acréscimos viram adendos com a história do erro contada).
- ask_user com ≥2 opções para despacho; despacho = 1 pergunta redonda.
- Suite sola verde ANTES de commit de dados; `verificar_verbetes` idem.
- `pip install -q --user --break-system-packages openpyxl python-docx` **a cada rebuild** (o sandbox some e leva as libs — incidente U39).
- Builds na ordem: `build_indice` → `exportar_json` → `build_xlsx` → `build_word` → `build_readme` (README é produto do espelho, 0.4).
- CSVs: `;` + utf-8-sig + CRLF; **OBS/termo/fontes nunca com `;` interno**; assert de 9 colunas E de conteúdo (forma sem conteúdo não é guarda — lição U35).
- `relacoes/` blindado; nada de aresta nova sem despacho; nada deleta memória (lápides, desfechos no HOLD).
- **Sandbox recriado é esperado (aconteceu 4× nesta sessão):** se `git status` inflar ou o push reclamar, NÃO confiar no HEAD local → `git fetch` + `update-ref` ao ramo remoto + `git reset -q`; o ramo remoto é a fonte de verdade. Commit perdido se refaz contra `git diff` de verificação (os ARQUIVOS sobrevivem; os OBJETOS não — caso U38).
- Token GitHub expira entre turnos (`could not read Username` / `commit_refs`): tentar 1×, se falhar avisar o Curador para reconectar na Arena e seguir trabalhando localmente (nada se perde; pusha no turno seguinte).
- Encadeamentos `cmd && python <<EOF` podem commitar mesmo com o python quebrado — checar a saída ANTES do `git add`; e `assert`s de contagem devem usar o número REAL (lição U36: eu esperei 24 onde havia 33).

## 5. PRÓXIMO TURNO — sugestão de abertura

Perguntar ao Curador: «R1 (piloto dos 8 suspenso-B), R2 (refinamento D), R3 (auditoria E), R4 (baixa A) — qual abre?» Cada rota é 1 unidade 1 commit; R1 é o caminho que já tem precedente (U30) e V chancelado.
