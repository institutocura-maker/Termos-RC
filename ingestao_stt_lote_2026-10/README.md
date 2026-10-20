# Fase 0 — ingresso STT normalizado (lote 2026-10)

> **Estado:** registro, integridade e triagem. Não é um ciclo do Motor e não altera a Base.

## Regra de fonte

A entrada operacional é exclusivamente `normalizados_stt_lote_2026-10/`. Os
caminhos e SHA-256 dos STT brutos aparecem como proveniência declarada pelos
manifestos da normalização; a Fase 0 não abriu, pesquisou nem transcreveu os
brutos em `uploads_recepcao/`.

## Resultado desta geração

- registros mestre: **309**;
- pares fonte declarada ↔ derivado: **309**;
- duração total informada: **245:56:52**;
- lotes temáticos planejados: **24**;
- sinais exatos da Base indexados: **11542**;
- mutações em `dados_termos.py`, fichas, relações, ciclos e apostilas: **0**.

## Artefatos

| Arquivo | Finalidade |
|---|---|
| `registro-mestre.jsonl` | Um registro por derivado, sua proveniência declarada, hashes e metadados. |
| `mapa-linhas.jsonl` | Endereço estável `Uxxxxx` e hash de cada linha textual do derivado. |
| `indice-termos-base.jsonl` | Ocorrências exatas e não ambíguas de grafias da Base; é sinal de triagem, não citação. |
| `mapa-tematico.jsonl` | Eixos temáticos e palavras-sinal por fonte. |
| `lotes-planejados.json` | Lotes sem sobreposição, capacidade estimada e no máximo 25 candidatos de cotejo por lote. |
| `resumo-triagem.json` | Contadores, hashes de entrada e barreiras de escopo. |

## Consulta reproduzível

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --buscar Sophia
```

A busca lê apenas os derivados e devolve endereços de linha. Para regenerar a
Fase 0 com segurança, use `--force`: o diretório é construído em estágio e só
substitui a geração anterior depois de todas as verificações passarem.

## Próxima fronteira

Cada lote permanece em `AGUARDANDO-DESPACHO-CURATORIAL`. O limite de 25 é um
teto para **candidatos de cotejo**; ele não cria pérolas nem autoriza ampliação.
Somente um despacho consolidado poderá selecionar candidatos e abrir um
`ciclo.toml` para o `motor.py`.
