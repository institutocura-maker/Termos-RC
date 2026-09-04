# 📑 ÍNDICE DE ARQUIVOS DA RAIZ — Termos-RC (2026-08-31)

> **Documento de handoff — Tabela de ponteiros.** Este é o **"mapa do mapa"**: para cada arquivo `.md`/`.json` da raiz, diz **o que é, quando foi atualizado, e quando o agente novo precisa lê-lo**. Use Ctrl+F no nome do arquivo.
>
> **Curado por:** Arena.ai Agent Mode (MiniMax-M3) em 2026-08-31.
> **Branch:** `arena/01a06429-termos-rc` · **HEAD:** `22eaeef` · **Working tree:** LIMPO (atualizado 2026-09-04).
> **Cabe em qualquer janela de contexto** (~10KB).

---

## 🗺️ Como usar este índice

1. **O agente novo chegou ao repo.** Qual arquivo ler PRIMEIRO?
   → Leia `PROMPT-PROXIMA-SESSAO.md` (item 1 abaixo).
2. **O agente precisa entender o que JÁ foi feito?**
   → Leia `STATUS-HANDOFF-2026-08-31.md` (item 2).
3. **O agente precisa da lista de todas as RC?**
   → Leia `GLOSSARIO-CANONICO-2026-08-31.md` (item 3) OU `indice-mestre.md` (item 4).
4. **O agente precisa do histórico completo?**
   → Leia `CONTINUIDADE.md` por CHUNK (item 5).
5. **O agente precisa do DNA/fundamento do projeto?**
   → Leia `GUIA-MESTRE-RC-APOSTILA-v1.1.md` (item 6).

---

## 🟢 GRUPO 1 — VIGENTES (ler quando relevante)

Estes arquivos são a **fonte de verdade operacional** em 2026-08-31.

| # | Arquivo | Tam | Última atualização | Quando ler |
|---|---|---|---|---|
| 1 | **`PROMPT-COMPLETO-2026-08-31.md`** | ~12 KB | 2026-08-31 (T+0:25) | **NOVO** — Prompt consolidado para colar no início da próxima sessão (compila STATUS + PROXIMA-SESSAO + GLOSSARIO + workflow) |
| 2 | **`PROMPT-PROXIMA-SESSAO.md`** | 57.2 KB · 264 linhas | 2026-08-28 (AGENTE 13/14) | **SEMPRE primeiro** — define a persona, o rito (esteira leve), os 7 capacidades, o Despacho vigente |
| 3 | **`STATUS-HANDOFF-2026-08-31.md`** | 10.6 KB · 277 linhas | 2026-08-31 (T+0:04) | Quando o agente novo precisa saber ONDE ESTAMOS e QUAIS REGRAS seguir |
| 4 | **`GLOSSARIO-CANONICO-2026-08-31.md`** | 51.1 KB · 702 linhas | 2026-08-31 (T+0:08) | Quando o agente precisa listar 524 RC canônicas + 80 pastas CONCLUIDAS |
| 4 | **`indice-mestre.md`** | 181.0 KB · 793 linhas | **(gerado automaticamente)** | Quando precisa da TABELA MESTRA de todos os 777 termos da Base (NÃO cabe em 1 chat; ler por chunk) |
| 5 | **`CONTINUIDADE.md`** | 343.6 KB · 1613 linhas | 2026-08-29 (AGENTE 14) | Log histórico das 14 sessões (NÃO cabe em 1 chat; ler por chunk) |
| 6 | **`GUIA-MESTRE-RC-APOSTILA-v1.1.md`** | 29.4 KB · 502 linhas | v1.1 (2026) | Quando precisa do DNA/fundamento/pipeline do projeto |
| 7 | **`INDICE-PALESTRAS.md`** | 45.9 KB · 51 linhas | 2026-08-31 (T+0:15) | Quando precisa do estado individual de cada uma das 51 palestras/livros |
| 8 | **`INVENTARIO-APOSTILAS.json`** | 12.5 KB | 2026-08-31 (T+0:01) | Fonte canônica estruturada (JSON) das 80 pastas CONCLUIDAS |
| 9 | **`INVENTARIO-COMPACTO-2026-08-31.md`** | 9.7 KB · 139 linhas | 2026-08-31 (T+0:10) | Versão legível (markdown) do `INVENTARIO-APOSTILAS.json` |
| 10 | **`DIAGNOSTICO-DO-PROCESSO-2026-08-29.md`** | 37.6 KB · 299 linhas | 2026-08-29 (AGENTE 14) | Análise técnica do rito (causas do custo, garantias, reforma) |
| 11 | **`DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md`** | 8.9 KB | 2026-08-29 (Curador) | A NORMA vigente da esteira leve (ato normativo do curador) |
| 12 | **`REGISTRO-ANOMALIA-REBASE-2026-08-31.md`** | 6.6 KB | 2026-08-31 (T+0:50) | Anomalia de rebase documentada HOJE (3 órfãs recuperadas) |
| 13 | **`README.md`** | 8.6 KB · 137 linhas | 2026-08-17 | Visão geral + comandos de validação (primeira leitura) |
| 14 | **`01-ficha-modelo.md`** | 2.9 KB | 2026 | **SEMPRE** — modelo de ficha canônica (criar/atualizar fichas) |
| 15 | **`02-vocabulario-controlado.md`** | 4.4 KB | 2026 | Quando precisa da lista de grafias canônicas |
| 16 | **`convencoes-editoriais-rc.md`** | 4.6 KB | 2026 | **SEMPRE** — regras de estilo editorial (aspas, negrito, verbatim) |
| 17 | **`VERIFICACAO-DE-COBERTURA-2026-08-26.md`** | 5.2 KB | 2026-08-26 | Como auditar cobertura de uma apostila (portão D) |
| 18 | **`PLANO-MIGRACAO-DE-CHAT.md`** | 6.9 KB | 2026-08-18 | Como migrar entre chats (pré-esteira-leve) |
| 19 | **`PACOTE-MIGRACAO-CHAT-2026-08-18.md`** | 9.0 KB | 2026-08-18 | Pacote de migração (estado pré-esteira-leve) |
| 20 | **`POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`** | 6.7 KB · 111 linhas | 2026-09-04 | **Política transversal** — quarentena absoluta entre a Base RC e tradições correlacionais externas (Jyotish/Ifá/mitologias); eleva a "Nota de confinamento O-4" (RC-092) a política recorrente. Ler quando qualquer proposta tocar fronteira com ecossistema externo |

---

## 🟡 GRUPO 2 — HISTÓRICOS (NÃO usar como estado vigente)

Estes arquivos se **declaram** desatualizados. Não usar para tomar decisão, apenas para contexto histórico se o curador pedir.

| # | Arquivo | Tam | Status oficial |
|---|---|---|---|
| 21 | **`PROMPT-INICIAL-DO-AGENTE.md`** | 4.6 KB | **DECLARA-SE HISTÓRICO** (linha 3): "⚠️ não usar — prevalece `PROMPT-PROXIMA-SESSAO.md`" |
| 22 | **`CHECKPOINT-SESSAO-2026-08-21.md`** | 12.3 KB | **DECLARA-SE VELHO** (linha 3): "Contagens 1849 relações / HEAD e91552d estão **velhas**. Vigente em 2026-08-25: 777 termos / 1.852 relações · HEAD `3fa96c1`" |
| 23 | **`STATUS-RESTAURACAO.md`** | 5.4 KB | Status de uma restauração antiga (provavelmente 2026-08-17) |
| 24 | **`PREPARACAO-DE-TEMA-2020-04-25-YEL-LUZBEL.md`** | 9.3 KB | Preparação específica de uma palestra antiga (não usar como template) |

---

## 🔴 GRUPO 3 — ARQUIVOS GRANDES (ler por chunk; NÃO cabem em 1 chat)

Estes arquivos **estouram qualquer janela de contexto razoável** e devem ser lidos em partes (ou só sob demanda).

| # | Arquivo | Tam | % de janela 200K | % de janela 1M | Estratégia de leitura |
|---|---|---|---|---|---|
| 4 | `indice-mestre.md` | 181.0 KB | **350%** ⚠️ | 70% | Ler por **palavras-chave** com `grep -A 5 "termo" indice-mestre.md` |
| 5 | `CONTINUIDADE.md` | 343.6 KB | **650%** ⚠️ | 130% | Ler por **ciclo** com `grep -A 30 "Ciclo — P2023-12-03" CONTINUIDADE.md` |

> **REGRA**: NUNCA tente ler esses 2 arquivos inteiros de uma vez. Use `head`, `tail`, `grep -A`, ou `sed -n '100,150p'`.

---

## 📊 Resumo Estatístico

| Categoria | Qtd | Soma (KB) | % da raiz |
|---|---|---|---|
| GRUPO 1 — VIGENTES | 20 arquivos | ~832 KB | ~63% |
| GRUPO 2 — HISTÓRICOS | 4 arquivos | ~32 KB | ~2% |
| GRUPO 3 — GRANDES | 2 arquivos | ~525 KB | ~40% (mas NÃO cabem em 1 chat) |
| **TOTAL MD/JSON** | **26 arquivos** | **~1.31 MB** | **100%** |

> **Nota**: Os 2 arquivos grandes (indice-mestre + CONTINUIDADE) sozinhos somam **525 KB** = 40% da raiz.

---

## 🎯 Recomendação de leitura para um agente novo

### 1ª Turn (mínima viável — ~80KB total)
1. `STATUS-HANDOFF-2026-08-31.md` (10.6 KB) — onde estamos
2. `PROMPT-PROXIMA-SESSAO.md` (57.2 KB) — rito vigente
3. `convencoes-editoriais-rc.md` (4.6 KB) — estilo
4. `01-ficha-modelo.md` (2.9 KB) — modelo de ficha
5. `INDICE-PALESTRAS.md` (45.9 KB) — estado por palestra

### 2ª Turn (se for processar uma palestra nova — +60KB)
6. `GLOSSARIO-CANONICO-2026-08-31.md` (51.1 KB) — RC canônicas
7. `DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md` (8.9 KB) — norma da esteira

### 3ª Turn (se for auditar/reformar — +200KB)
8. `DIAGNOSTICO-DO-PROCESSO-2026-08-29.md` (37.6 KB) — análise do rito
9. `GUIA-MESTRE-RC-APOSTILA-v1.1.md` (29.4 KB) — DNA
10. `CONTINUIDADE.md` (343.6 KB) — **POR CHUNK** (usar `grep -A 30 "Ciclo — P????-??-??"`)

### 4ª Turn (se for mexer na Base — +180KB)
11. `indice-mestre.md` (181.0 KB) — **POR CHUNK** (usar `grep -A 5 "^| RC-XXX"`)

---

## 🔗 Relações entre arquivos

```
STATUS-HANDOFF ──► Workflow resumido ──► aponta para PROMPT-PROXIMA-SESSAO
GLOSSARIO-CANONICO ──► Lista das 524 RC + 80 pastas ──► aponta para termos/, apostilas/CONCLUIDAS/
INVENTARIO-COMPACTO ──► Tabela das 80 pastas ──► aponta para INVENTARIO-APOSTILAS.json
INDICE-ARQUIVOS-RAIZ (este) ──► Tabela de ponteiros ──► aponta para TODOS acima

PROMPT-PROXIMA-SESSAO ──► Persona + rito vigente ──► prevalece sobre PROMPT-INICIAL
DESPACHO-DA-ESTEIRA-LEVE ──► Norma da esteira leve (ato do curador) ──► prevalece sobre rite pesado
DIAGNOSTICO-DO-PROCESSO ──► Análise técnica do rito ──► base do DESPACHO
GUIA-MESTRE ──► DNA/fundamento ──► v1.1 estável
CONTINUIDADE ──► Log histórico ──► NÃO é estado vigente
indice-mestre ──► Tabela gerada ──► regenerar com ferramentas/gerar_pacotes.py
```

---

## 📋 Arquivos auxiliares (não-md/json)

A raiz também tem:

| Arquivo | Tam | Função |
|---|---|---|
| `base-terminologica-leitura.docx` | 1.28 MB | DOCX da base (gerado por `ferramentas/build_apostila.py`) |
| `base-terminologica.xlsx` | 252.9 KB | XLSX da base (gerado por `ferramentas/gerar_pacotes.py`) |
| `GUIA-MESTRE-RC-APOSTILA.txt` | 29.4 KB | Cópia `.txt` do GUIA-MESTRE (v1.1) |
| `2026-08-04 - O QUE NÃO TE CONTARAM SOBRE ALIENÍGENAS E A BÍBLIA.txt` | 96.5 KB | TXT de palestra avulsa na raiz (verificar se deve ir para `uploads_recepcao/`) |
| `.gitignore` | 765 B | Padrões de ignore do Git |

> **Nota (2026-08-31, T+0:25)**: O TXT `2026-08-04 - O QUE NÃO TE CONTARAM SOBRE ALIENÍGENAS E A BÍBLIA.txt` (96.5 KB) que estava solto na raiz foi **movido para `uploads_recepcao/`** via `git mv` (rename preservado). A raiz agora tem 27 arquivos, sem arquivos avulsos.

---

## 📜 Histórico deste índice

- **2026-08-31 (T+0:21)**: Criado em resposta à pergunta do curador sobre `CONTINUIDADE.md` e `PROMPT-INICIAL-DO-AGENTE.md`. Decideuse criar 1 doc de ponteiros (em vez de mini-resumo de cada um) para preservar o conteúdo original intacto.
- **2026-09-04**: Registrado `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md` como item 20 do GRUPO 1 (VIGENTES); GRUPO 2 renumerado (20–23 → 21–24); total MD/JSON 25 → 26. Branch `arena/01a06429-termos-rc` · HEAD `22eaeef`.
- Commit: (ver `git log` — a fazer)

---

**FIM DO ÍNDICE — Total: ~10KB, cabe em qq chat.**
