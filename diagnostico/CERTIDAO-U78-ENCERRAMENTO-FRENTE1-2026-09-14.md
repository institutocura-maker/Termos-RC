# CERTIDÃO — U78 · ENCERRAMENTO · FRENTE 1
## Reconstrução dos espelhos `.xlsx` / `.docx`

**Data:** 14/09/2026 · **Despacho:** U77 — roteiro de encerramento homologado na U60, **estritamente nesta ordem**: Frente 1 (espelhos) → Frente 2 (higienização de `fontes`) → Frente 3 (certidão final da campanha R1).
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0** · verificação dupla de HEAD

---

## 1. A dívida, medida antes de paga

Os espelhos estavam **congelados desde a U51** (despacho U52: adiados para poupar custo por rodada, com a verificação prévia de que nenhum teste da suíte os fiscaliza — T10–T15). A dívida foi **medida antes** de reconstruir, e não estimada:

| Espelho | Fichas antes | Fichas depois |
|---|---:|---:|
| `base-terminologica.xlsx` (aba *Fichas*) | **768** (769 linhas − 1 cabeçalho) | **820** (821 − 1) |
| `base-terminologica-leitura.docx` (Heading 1 «Nome — RC‑###») | **768** | **820** |

**52 fichas em dívida** — exactamente as materializadas entre a U52 e a U77.

## 2. A reconstrução

```
pip install -q --user --break-system-packages openpyxl python-docx
    (o sandbox perdeu as duas dependências pela 3.ª vez — U39, U51, U78)

python3 ferramentas/build_xlsx.py
    OK -> base-terminologica.xlsx (7 abas)
    Índice: 946 termos | Fichas-resumo: 820 | Relações: 1887 | Obras: 102

python3 ferramentas/build_word.py
    OK -> base-terminologica-leitura.docx
    Termos: 946 | Relações: 1887 | Obras: 102 | Fichas: 820
```

Ambos leem `base/canonico.json` (JSON‑primeiro, Onda 1.7‑b/c) e `termos/*.md`; o canônico estava em dia desde a U77.

## 3. Verificação dos artefatos (não só a contagem)

**XLSX** — 7 abas, todas íntegras:

| Aba | Linhas não‑vazias |
|---|---:|
| Como usar | 9 |
| Índice Mestre | 947 (946 + cabeçalho) |
| **Fichas** | **821 (820 + cabeçalho)** |
| Categorias | 41 |
| Bibliografia | 103 |
| Relações | 1888 (1887 + cabeçalho) |
| Status | 5 |

Cabeçalho da aba *Fichas*: `('Código', 'Termo', 'Categoria', 'Subcategoria')`.

**DOCX** — 820 fichas detalhadas, da primeira («Javé (Senhor Javé) — RC‑001») à última («PÔNCIO PILATOS / CAIFÁS / SINÉDRIO — RC‑946»).

**Prova de que as fichas novas entraram com CONTEÚDO, e não só com a linha:** conferiu‑se a RC‑931 no corpo do documento — título «Nuctemeron — RC‑931», Definição Sintética, Contexto/Origem, Escopo e evidência, Termos Relacionados, Fontes e as Citações‑chave («Apolônio de Tiana» L26, «APOLÔNIO DE TIANA» L6878…). Amostra de presença: **RC‑931, RC‑377, RC‑372, RC‑368, RC‑352, RC‑347, RC‑270, RC‑025 — todos True**.

## 4. O que **não** mudou

```python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 820 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 820 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 820 fichas · 1887 relacoes
```

**O delta do turno é só os dois binários.** Nenhum dado, nenhum script, nenhuma ficha tocados:

```
M base-terminologica-leitura.docx   Bin 1 964 460 -> 2 066 963 bytes
M base-terminologica.xlsx           Bin   305 976 ->   311 012 bytes
```

O canônico não foi reexportado porque nada mudou no cadastro nesta unidade — a dívida era **dos espelhos**, não da Base.

---

## 5. Estado das frentes

| Frente | Estado |
|---|---|
| **1 — Espelhos .xlsx/.docx** | ✅ **CONCLUÍDA (U78)** |
| 2 — Higienização global de `fontes` (inventário U57 + TAB→ESPAÇO da B049) | ⏳ aguardando |
| 3 — Certidão Final da Campanha R1 | ⏳ aguardando |

---

*Lavrada sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`; verificação dupla de HEAD (abertura e encerramento).*
