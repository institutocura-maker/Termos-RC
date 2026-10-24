# Transcrições STT normalizadas — lote 2026-10

> **Natureza:** cópias derivadas e auditáveis; **não são verbatim bruto**.
>
> **Fontes imutáveis:** `uploads_recepcao/stt-lote-2026-10/`
>
> **Executor:** `ferramentas/normalizar_stt_lote_2026_10.py`
>
> **Política inicial:** `diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md`
>
> **Despacho autorizado:** `diagnostico/DESPACHO-NORMALIZACAO-STT-LOTE-2026-10-20.md`

Este diretório contém uma cópia de cada uma das 309 transcrições do lote,
com as regras já aprovadas e os blocos D1/D2 autorizados pelo Curador em
20/10/2026. O frontmatter, URLs e dados de origem foram preservados; somente o
corpo da transcrição recebeu as trocas auditadas abaixo.

## Resultado

- cópias derivadas: **309**;
- substituições rastreadas: **1306**;
- candidatos contextuais não alterados: **476**;
- itens D3 e pendências antigas: ver `preservados-d3.jsonl`;
- fontes alteradas: **0**;
- idempotência: **verificada**.

## Censo por regra executada

| Regra | DE | PARA | Trocas | Arquivos | Regime |
|---|---|---|---:|---:|---|
| `STT-A01` | `anunaki` | **Anunnaki** | 9 | 6 | automática |
| `STT-A02` | `trimurte` / `trimurto` | **Trimurti** | 57 | 39 | automática |
| `STT-A03` | `vismo` / `visma` / `vizno` | **Vishnu** | 104 | 40 | automática |
| `STT-A04` | `pachupati` / `pachupato` | **Pashupati** | 10 | 7 | automática |
| `STT-A05` | `tikkun` | **Tikun** | 23 | 9 | automática |
| `STT-A06` | `mohensof` / `mohenso` | **Mohen So** | 31 | 12 | automática |
| `STT-A07` | `tirtankaras` | **Tirthankaras** | 35 | 15 | automática |
| `STT-A08` | `tote` / `toth` | **Thoth** | 135 | 5 | automática |
| `STT-D1.01` | `rockman` | **Hochmah** | 67 | 17 | automática |
| `STT-D1.02` | `uerd` / `werd` / `erd` | **Wyrd** | 133 | 22 | automática |
| `STT-D1.03` | `ticum` | **Tikun** | 38 | 14 | automática |
| `STT-D1.04` | `javer` | **Javé** | 16 | 13 | automática |
| `STT-D1.05` | `sávina` | **Savna** | 14 | 8 | automática |
| `STT-D1.06` | `vaicunta` | **Vaikuntha** | 9 | 4 | automática |
| `STT-D1.07` | `rabarata` / `marra barata` | **Mahabharata** | 18 | 14 | automática |
| `STT-D1.08` | `morus` | **Moros** | 6 | 4 | automática |
| `STT-D1.09` | `viaza` | **Vyasa** | 5 | 2 | automática |
| `STT-D1.10` | `silênio` | **Sileno** | 5 | 3 | automática |
| `STT-D1.11` | `horlogue` | **Orlog** | 3 | 2 | automática |
| `STT-D1.12a` | `aia` | **Aya** | 2 | 2 | automática |
| `STT-D1.12b` | `aie` | **Aye** | 1 | 1 | automática |
| `STT-D1.13` | `chiva` | **Shiva** | 3 | 3 | automática |
| `STT-D1.14` | `pimeteu` | **Epimeteu** | 3 | 3 | automática |
| `STT-D1.15` | `riches` | **Rishis** | 2 | 1 | automática |
| `STT-D1.16` | `fanis` | **Phanes** | 2 | 2 | automática |
| `STT-C01` | `sofia` / `sofio` | **Sophia** | 514 | 67 | automática-contexto |
| `STT-D2.01` | `elio` | **Enlil** | 9 | 4 | automática-contexto |
| `STT-D2.02` | `enke` / `enck` / `enk` | **Enki** | 18 | 11 | automática-contexto |
| `STT-D2.03` | `vigno` / `vigna` / `virgo` / `vísgno` | **Vishnu** | 26 | 12 | automática-contexto |
| `STT-D2.04` | `arapa` | **Harapa** | 5 | 5 | automática-contexto |
| `STT-D2.05` | `buloca` | **Bhuloka** | 3 | 3 | automática-contexto |
| `STT-D2.06` | `anã` | **Ananque** | 0 | 0 | automática-contexto |

## Artefatos de auditoria

| Arquivo | Conteúdo |
|---|---|
| `manifesto-fontes-sha256.tsv` | caminho, bytes e SHA-256 de cada bruto usado |
| `manifesto-derivados-sha256.tsv` | SHA-256 de cada derivado, SHA da origem e número de trocas |
| `rastreio-antes-depois.jsonl` | cada troca com regra, linha, parágrafo e excertos |
| `pendentes-contexto.jsonl` | candidatos de regras contextuais sem âncora suficiente |
| `preservados-d3.jsonl` | formas bloqueadas/preservadas, sem alteração |
| `diagnostico/RELATORIO-NORMALIZACAO-STT-LOTE-2026-10-20.md` | síntese humana, censo e verificações |

A execução nunca regrava os arquivos em `uploads_recepcao/`. Para repetir a
geração, use o executor com `--force`; ele só remove este diretório derivado e
os relatórios derivados associados.
