# U48 — R1 · lote 5 · os 14 restantes do glossário da B031

Safra 2026-09-13 · despachos: `DESPACHO-ROTAS-POS-V2-2026-09-13.md` e
`DESPACHO-DIVERGENCIAS-CROSSREF-E-GRAFIA-2026-09-13.md`.

## 1. As 14 fichas (fecha o glossário da B031)

| Código | Nome | Ficha | Fragmentos |
|---|---|---|---:|
| RC-022 | Antlar | `termos/RC-022-antlar.md` | 3 |
| RC-023 | Antlartes | `termos/RC-023-antlartes.md` | 2 |
| RC-026 | Astralização dos Biodemos | `termos/RC-026-astralizacao-dos-biodemos.md` | 5 |
| RC-029 | Atlans | `termos/RC-029-atlans.md` | 3 |
| RC-043 | Conselho dos Cinco | `termos/RC-043-conselho-dos-cinco.md` | 3 |
| RC-045 | Daemon | `termos/RC-045-daemon.md` | 5 |
| RC-067 | Gron Mion | `termos/RC-067-gron-mion.md` | 4 |
| RC-069 | Ion Crom | `termos/RC-069-ion-crom.md` | 3 |
| RC-082 | Nephilins | `termos/RC-082-nephilins.md` | 5 |
| RC-083 | Norte Divino | `termos/RC-083-norte-divino.md` | 3 |
| RC-088 | Portlan e Portlon | `termos/RC-088-portlan-e-portlon.md` | 4 |
| RC-127 | Val-Ha | `termos/RC-127-val-ha.md` | 6 |
| RC-134 | Viajores | `termos/RC-134-viajores.md` | 3 |
| RC-144 | Zeitgeist | `termos/RC-144-zeitgeist.md` | 4 |

**53 fragmentos** verbatim intra-linha, conferidos byte a byte — **0 falhas**.
Fontes: **B031** (13 fichas) e **B031 + B015** (RC-134 Viajores, que usa as duas).

## 2. Os três despachos curatoriais, aplicados

### 2.1 Divergência Val Bon × Val Dimon — etiquetada e cruzada

Gaveta `## 6. Histórico Curatorial e Auditoria` criada em **RC-116** e **RC-118**,
cada uma com a etiqueta `[⚠️ DIVERGÊNCIA INTERNA DA FONTE]` e o cruzamento do
verbete alheio: L3926–L3929 (Astréia) contra L3939–L3941 (Pandora). As duas
afirmações permanecem, sem conciliação — a contradição é da obra, não da extração.

### 2.2 Códigos duplos Yel Am × Yel Liam — preservados e conectados

Sem fusão, sem lápide, sem aresta nova em `relacoes/`. Conexão feita no corpo
das fichas: **RC-138 → RC-140** (evolução, pós-fusão com Val El) e
**RC-140 ← RC-138** (origem, pré-fusão).

### 2.3 Grafia — paridade verbatim absoluta

Nenhuma grafia foi normalizada. A variação fica declarada na **Definição Sintética**
de RC-121 («Val Elliah» L3983 × «Val Eliah» L3255), RC-122 («Val Ellieh» L3986 ×
«Val Elieh» L3255) e RC-043 (Conselho dos Cinco, que cita os dois de um só «l»).
Caso-limite preservado neste lote: o verbete «Gron Mion» (B031 L3497) é grafado com
**dois espaços** depois dos dois-pontos — a ficha conserva os dois.

## 3. Efeito na Base

- **+14 fichas** (732 → 746).
- Status **inalterado**: as 14 já eram `provisório` — 572🟢 · 212🟡 · 102🟠 · 60⚪.
- Gap de fichas: 214 → **200**. Poço da família B (censo v2): 107 → **93 restantes**.
- Nenhuma aresta criada em `relacoes/` (1887) · nenhum HOLD tocado.

## 4. Instrumento

`ferramentas/materializar_lote.py` passa a aceitar o campo opcional `historico` por
ficha, que gera a gaveta `## 6. Histórico Curatorial e Auditoria`. As gavetas de
RC-116, RC-138 e RC-140 foram **regeneradas pelo driver** a partir do JSON do lote 4,
que foi atualizado para reproduzi-las — prova de regeneração conferida (o JSON volta
a gerar o arquivo byte a byte).

## 5. Incidente de ambiente

No meio do turno o sandbox perdeu `openpyxl` e `python-docx` (incidente conhecido da
U39). Os builds de xlsx e word falharam na primeira passada; as libs foram reinstaladas
e os dois builds refeitos antes da suíte, que fechou verde.

## 6. Verificação

Suíte 21/21 (T13 746 · T14 0 divergentes · T15 746/0) · verificador 946/746/1887 ·
5 builds na ordem (indice → exportar_json → xlsx → word → readme).

