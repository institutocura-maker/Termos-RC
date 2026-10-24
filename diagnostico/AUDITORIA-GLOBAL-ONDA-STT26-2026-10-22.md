# Auditoria global — onda STT26

**Data da auditoria:** 22/10/2026
**Escopo:** planejamento, derivados normalizados, registro mestre, rastreio, despachos por eixo e ciclos STT26 existentes.
**Modo:** somente leitura das fontes operacionais; sem abertura de STT bruto, sem mutação da Base e sem abertura de ciclo.

## Resultado

**APROVADA** — a onda STT26 está íntegra para continuidade controlada.

- lotes planejados e deliberados: **24**;
- fontes derivadas rastreáveis: **309**;
- duração planejada: **245:56:52**;
- decisões registradas: **600**;
- `AUTORIZAR-COTEJO-AMPLIADO`: **483**;
- `DESCARTAR-DO-LOTE`: **117**;
- decisões pendentes, `MANTER-EM-TRIAGEM` ou reservas: **0**;
- fontes brutas abertas pela Fase 0, triagem ou consolidação: **0**;
- mutações de Base registradas nessas etapas: **0**.

## Cadeia de proveniência

- **309** derivados Markdown conferidos byte a byte contra `normalizados_stt_lote_2026-10/manifesto-derivados-sha256.tsv`;
- os **309** derivados correspondem exatamente aos arquivos e aos ingressos do planejamento;
- `registro-mestre.jsonl`: **309** registros, um por `ingresso_id` planejado;
- `mapa-linhas.jsonl`: **26389** endereços de linha, todos vinculados a ingressos planejados;
- `rastreio-antes-depois.jsonl`: **1306** mudanças, igual às **1306** mudanças declaradas no manifesto;
- fontes operacionais verificadas: somente `normalizados_stt_lote_2026-10/`.

## Despachos por eixo

| Eixo | Lotes | Fontes | Duração | Códigos únicos | Cotejos | Descartes | Ciclo STT26 |
|---|---|---:|---:|---:|---:|---:|---|
| `ANUNNAKI_GENETICA` | STT26-01, STT26-02 | 31 | 20:19:18 | 36 | 43 | 7 | aberto e validado |
| `COSMOGONIA_HISTORIA_COSMICA` | STT26-03, STT26-04, STT26-05, STT26-06 | 48 | 39:17:23 | 53 | 85 | 15 | aberto e validado |
| `EXPERIENCIA_ESPIRITUAL_ETICA` | STT26-08, STT26-09, STT26-10, STT26-11, STT26-12 | 86 | 54:08:59 | 64 | 102 | 23 | não aberto |
| `EXTRATERRESTRES_TECNOLOGIA` | STT26-07 | 19 | 11:45:46 | 25 | 22 | 3 | não aberto |
| `MITOLOGIAS_REINTEGRACAO` | STT26-13, STT26-14, STT26-15, STT26-16, STT26-17, STT26-18 | 61 | 62:55:39 | 63 | 114 | 36 | não aberto |
| `SOCIEDADE_CONTEMPORANEA` | STT26-19, STT26-20, STT26-21, STT26-22, STT26-23, STT26-24 | 64 | 57:29:47 | 72 | 117 | 33 | não aberto |

Todos os seis despachos estão em `CONCLUIDO`, com cobertura exata de **25 decisões por lote**.

## Ciclos já publicados

- `STT26-ANUNNAKI_GENETICA` — ciclo existente e validado;
- `STT26-COSMOGONIA_HISTORIA_COSMICA` — ciclo existente e validado.

## Ciclos ainda não abertos

`EXPERIENCIA_ESPIRITUAL_ETICA`, `EXTRATERRESTRES_TECNOLOGIA`, `MITOLOGIAS_REINTEGRACAO`, `SOCIEDADE_CONTEMPORANEA`.

Estes eixos possuem despacho integral e cotejo autorizado, mas mantêm
`autorizacao_para_abrir_ciclo: false`. A auditoria **não** alterou essa
condição e não criou novos ciclos.

## Selos SHA-256 consultados

- `ingestao_stt_lote_2026-10/lotes-planejados.json`: `701ad2f1f4136c7c0ec201247189d361d5b5198f0eb8c577454bc1a72035295c`
- `normalizados_stt_lote_2026-10/manifesto-derivados-sha256.tsv`: `906d8e755d701f1dd4e8a2cedbc7f3a1fc18ef29b2cbe6da821f381c8918c501`
- `normalizados_stt_lote_2026-10/rastreio-antes-depois.jsonl`: `be67a9649240d0f9830be7f5e90f3e3c2097f1ae215ff1fad83fb107116a554a`
- `ANUNNAKI_GENETICA` — `DESPACHO-EIXO-TEMPLATE.json`: `3f1f063932451801735cfc0f38b16bf45d879d9a7ae9591d9eb955203d82b13d`
- `COSMOGONIA_HISTORIA_COSMICA` — `DESPACHO-EIXO-TEMPLATE.json`: `3af9f658fa2ba0f4eef970faffd59a01a012367302d2e5bc91e047f462424bf6`
- `EXPERIENCIA_ESPIRITUAL_ETICA` — `DESPACHO-EIXO-TEMPLATE.json`: `c61ae0309d8fd0da30e07a3d9592c5358980788afa94596d1f155b101b79e718`
- `EXTRATERRESTRES_TECNOLOGIA` — `DESPACHO-EIXO-TEMPLATE.json`: `f20415a8332780afaa40e20839898b7e7e1f7aee18e4332644efc9663c6adb80`
- `MITOLOGIAS_REINTEGRACAO` — `DESPACHO-EIXO-TEMPLATE.json`: `e9176fcfc266c8c262d19e929d44efc12577791634b078ab32605413bc1762a3`
- `SOCIEDADE_CONTEMPORANEA` — `DESPACHO-EIXO-TEMPLATE.json`: `40be6275296d8a3121ee8d188577d2ed6bcf4c551d2566071fd2aa9906123a34`

## Validações executadas fora deste relatório

1. `consolidar_despacho_eixo_stt_2026_10.py --validar-despacho` para cada um dos seis eixos;
2. `abrir_ciclo_eixo_stt_2026_10.py --validar` para os ciclos Anunnaki e Cosmogonia já existentes;
3. `ferramentas/test_suite.py` — **21 testes aprovados**.

## Próxima ação condicionada

A presente auditoria não autoriza automaticamente nenhuma abertura. Conforme a
orientação curatorial vigente, a abertura de `EXTRATERRESTRES_TECNOLOGIA` só
poderá ocorrer após aprovação explícita deste resultado.
