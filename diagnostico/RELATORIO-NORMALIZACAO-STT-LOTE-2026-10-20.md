# Relatório de normalização STT — lote 2026-10

**Data de geração:** 20/10/2026

**Executor:** `ferramentas/normalizar_stt_lote_2026_10.py`

**Fonte:** `uploads_recepcao/stt-lote-2026-10/`

**Saída:** `normalizados_stt_lote_2026-10/`

**Despacho aplicado:** D1 e D2 aprovados; D3 preservado.

> **Resultado derivado, não verbatim.** Os 309 brutos permaneceram
> inalterados; as cópias normalizadas têm manifesto SHA-256 e rastreio completo.

## Resultado geral

| Item | Resultado |
|---|---:|
| Fontes brutas lidas | 309 |
| Cópias derivadas escritas | 309 |
| Arquivos com ao menos uma troca | 134 |
| Arquivos sem troca | 175 |
| Substituições aplicadas | 1306 |
| Contextuais preservados por falta de âncora | 476 |
| Ocorrências D3/pendentes preservadas | 3314 |
| Fontes brutas alteradas | **0** |
| Idempotência do produto | **OK** |

## Censo das regras executadas

| Regra | DE | PARA | Trocas | Arquivos | Âncora | Regime |
|---|---|---|---:|---:|---|---|
| `STT-A01` | `anunaki` | **Anunnaki** | 9 | 6 | RC-024 — Anunnaki | automática |
| `STT-A02` | `trimurte` / `trimurto` | **Trimurti** | 57 | 39 | RC-104 — Trimurti | automática |
| `STT-A03` | `vismo` / `visma` / `vizno` | **Vishnu** | 104 | 40 | RC-135 — Vishnu (Mavatna) | automática |
| `STT-A04` | `pachupati` / `pachupato` | **Pashupati** | 10 | 7 | RC-669 — Pashupati | automática |
| `STT-A05` | `tikkun` | **Tikun** | 23 | 9 | RC-514 — Tikun Cósmico | automática |
| `STT-A06` | `mohensof` / `mohenso` | **Mohen So** | 31 | 12 | RC-081 — Mohen So | automática |
| `STT-A07` | `tirtankaras` | **Tirthankaras** | 35 | 15 | RC-397 — Tirthankaras | automática |
| `STT-A08` | `tote` / `toth` | **Thoth** | 135 | 5 | RC-463/RC-534 — Thoth | automática |
| `STT-D1.01` | `rockman` | **Hochmah** | 67 | 17 | RC-565 — Hochmah; RC-009 | automática |
| `STT-D1.02` | `uerd` / `werd` / `erd` | **Wyrd** | 133 | 22 | RC-658/RC-560 — Wyrd / Urd | automática |
| `STT-D1.03` | `ticum` | **Tikun** | 38 | 14 | RC-514 — Tikun Cósmico | automática |
| `STT-D1.04` | `javer` | **Javé** | 16 | 13 | RC-001; RC-040 | automática |
| `STT-D1.05` | `sávina` | **Savna** | 14 | 8 | RC-102 — Shiva (Savna) | automática |
| `STT-D1.06` | `vaicunta` | **Vaikuntha** | 9 | 4 | RC-414 | automática |
| `STT-D1.07` | `rabarata` / `marra barata` | **Mahabharata** | 18 | 14 | RC-593 — Mahabharata | automática |
| `STT-D1.08` | `morus` | **Moros** | 6 | 4 | RC-454; RC-533 | automática |
| `STT-D1.09` | `viaza` | **Vyasa** | 5 | 2 | RC-585 — Vyasa | automática |
| `STT-D1.10` | `silênio` | **Sileno** | 5 | 3 | RC-228 — Sileno | automática |
| `STT-D1.11` | `horlogue` | **Orlog** | 3 | 2 | RC-658 — Wyrd / Urd | automática |
| `STT-D1.12a` | `aia` | **Aya** | 2 | 2 | RC-834 — Família Aya | automática |
| `STT-D1.12b` | `aie` | **Aye** | 1 | 1 | RC-835 — Família Aye | automática |
| `STT-D1.13` | `chiva` | **Shiva** | 3 | 3 | RC-102; RC-135 | automática |
| `STT-D1.14` | `pimeteu` | **Epimeteu** | 3 | 3 | Glossário canônico; RC-302 | automática |
| `STT-D1.15` | `riches` | **Rishis** | 2 | 1 | RC-586 — Rishis | automática |
| `STT-D1.16` | `fanis` | **Phanes** | 2 | 2 | RC-565; RC-282 | automática |
| `STT-C01` | `sofia` / `sofio` | **Sophia** | 514 | 67 | RC-009 — Sophia (Cristo Cósmico) | automática-contexto |
| `STT-D2.01` | `elio` | **Enlil** | 9 | 4 | RC-487 — Enlil | automática-contexto |
| `STT-D2.02` | `enke` / `enck` / `enk` | **Enki** | 18 | 11 | RC-487 — Enlil; RC-486 — Enki | automática-contexto |
| `STT-D2.03` | `vigno` / `vigna` / `virgo` / `vísgno` | **Vishnu** | 26 | 12 | RC-135 — Vishnu (Mavatna) | automática-contexto |
| `STT-D2.04` | `arapa` | **Harapa** | 5 | 5 | RC-329 — Kumari Kandam | automática-contexto |
| `STT-D2.05` | `buloca` | **Bhuloka** | 3 | 3 | RC-033 — Bhuloka | automática-contexto |
| `STT-D2.06` | `anã` | **Ananque** | 0 | 0 | RC-777 — Ananque | automática-contexto |

As regras `STT-A01` a `STT-A08` são as oito equivalências já aprovadas. `STT-C01`
corresponde a Sophia/Sofio com a trava contextual original. `STT-D1.*` e
`STT-D2.*` executam exatamente os blocos autorizados no despacho consolidado.

> **Reconciliação do pré-censo.** A projeção exploratória de 405 trocas para as
> oito regras legadas contou uma ocorrência de `Toth` no frontmatter. Como o
> executor protege o frontmatter por desenho, o censo aplicado dessas regras é
> **404**. A regra Sophia sobe de 502 candidatos contextualmente aptos no
> pré-censo para **514** porque o ponto fixo avalia o contexto depois das trocas
> lexicais autorizadas (por exemplo, `Javer` → `Javé`), sem tocar o YAML.

## Contextuais não aplicados

Uma ocorrência contextual só foi trocada com ao menos uma âncora no mesmo
parágrafo. O detalhe por linha está em
`normalizados_stt_lote_2026-10/pendentes-contexto.jsonl`.

| Regra contextual | Mantidos sem troca | Mapeamento |
|---|---:|---|
| `STT-C01` | 445 | `sofia` / `sofio` → **Sophia** |
| `STT-D2.01` | 5 | `elio` → **Enlil** |
| `STT-D2.02` | 4 | `enke` / `enck` / `enk` → **Enki** |
| `STT-D2.03` | 13 | `vigno` / `vigna` / `virgo` / `vísgno` → **Vishnu** |
| `STT-D2.04` | 3 | `arapa` → **Harapa** |
| `STT-D2.05` | 1 | `buloca` → **Bhuloka** |
| `STT-D2.06` | 5 | `anã` → **Ananque** |

## Formas preservadas (D3 e travas antigas)

| Regra | Formas inventariadas | Ocorrências mantidas | Motivo |
|---|---|---:|---|
| `STT-P01` | `morrenso` / `morrensor` / `morrenson` | 41 | colisão Morren So × Morlens × Moros; sem alvo global seguro |
| `STT-P02` | `luzbel` | 36 | pode ser Yel Luzbel ou Lúcifer conforme o contexto |
| `STT-P03` | `brama` / `brahman` | 24 | formas com estatutos/referentes distintos |
| `STT-P04` | `temes` / `tênis` | 30 | Têmis × usos comuns, inclusive Tênis Clube Paulista |
| `STT-P05` | `deus` | 2428 | palavra portuguesa comum; nunca inferir Zeus |
| `STT-P06` | `viaja` | 3 | verbo comum; distinto de Viaza |
| `STT-P07` | `vista` / `virgem` | 180 | formas comuns; não inferir Vishnu por semelhança |
| `STT-P08` | `urdre` / `vivendre` / `scud` | 29 | componentes das Nornes; não fundir em Wyrd |
| `STT-P09` | `pularra` / `prara` / `pharara` / `porularra` / `pulra` | 2 | RC-743 aguarda áudio; não escolher grafia |
| `STT-P10` | `lémion` / `lénion` / `lemion` | 46 | grafias STT datadas de Len Mion; não converter retroativamente |
| `STT-P11` | `anunnakis` | 455 | plural oral; não apagar número gramatical |
| `STT-P12` | `nephilim` | 17 | transliteração legítima; sem troca editorial |
| `STT-P13` | `parvati` | 11 | variante transliterativa; sem troca editorial |
| `STT-P14` | `capella` | 4 | forma externa legítima; sem troca editorial |
| `STT-P15` | `gauzu` | 8 | forma registrada na Base; não é ruído demonstrado |

O inventário completo com arquivo, linha, parágrafo e excerto está em
`normalizados_stt_lote_2026-10/preservados-d3.jsonl`. Uma ocorrência aparecer
nesse inventário **não** significa erro: ela foi conscientemente deixada igual
à fonte por colisão, variante legítima ou insuficiência de contexto.

## Amostra de trilha `antes → depois`

O rastreio integral, não apenas esta amostra, está em
`normalizados_stt_lote_2026-10/rastreio-antes-depois.jsonl`.

| Arquivo | Linha | Regra | Antes | Depois | Âncora contextual |
|---|---:|---|---|---|---|
| `2015-09_006_Ci_985QlYms_PALESTRA_COMPLETA_-_A_Volta_de_Jesus.md` | 237 | `STT-D2.02` | `Enke` | **Enki** | Livro Perdido |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 224 | `STT-A02` | `Trimurte` | **Trimurti** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 60 | `STT-A03` | `vizno` | **Vishnu** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 158 | `STT-A03` | `Vizno` | **Vishnu** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 160 | `STT-A03` | `Vizno` | **Vishnu** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 626 | `STT-A03` | `Vizno` | **Vishnu** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 266 | `STT-D1.12a` | `Aia` | **Aya** | — |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 32 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 50 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 50 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 60 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 60 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 74 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 98 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 98 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 100 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 102 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 104 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 104 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 116 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 116 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 118 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 118 | `STT-C01` | `Sofia` | **Sophia** | Javé |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 160 | `STT-C01` | `Sofia` | **Sophia** | Jesus |
| `2020-04_002_Fnh_Cyoxtos_2020-04-09_-_Live_com_Jan_Val_Ellam_-_Perguntas_e_Respostas.md` | 166 | `STT-C01` | `Sofia` | **Sophia** | Jesus |

## Integridade e reprodutibilidade

1. Antes da escrita, o executor leu e reteve os bytes das 309 fontes.
2. Após a escrita, recalculou todos os SHA-256 e comprovou que cada bruto era
   idêntico ao byte originalmente lido.
3. `manifesto-fontes-sha256.tsv` e `manifesto-derivados-sha256.tsv` registram
   caminho, bytes, hash de origem, hash derivado e total de trocas por arquivo.
4. O executor rodou um segundo passe em memória sobre cada derivado; qualquer
   nova troca abortaria a execução. Nenhuma foi encontrada.
5. O YAML/frontmatter e as URLs não foram alvo de regex: a transformação atua
   apenas depois do delimitador final `---` do frontmatter.

## Limites explícitos

- Não houve cotejo com áudio nesta etapa.
- O bruto STT não foi “corrigido”: ele permanece em `uploads_recepcao/`.
- D3 não foi inferido, nem substituído. Casos com baixa segurança seguem
  listados e preservados para eventual despacho futuro.
