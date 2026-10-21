# Triagens curatoriais — lote STT 2026-10

Cada subdiretório é uma devolutiva de **triagem consolidada por lote**. A
entrada operacional continua sendo exclusivamente as cópias em
`normalizados_stt_lote_2026-10/`; nenhuma ferramenta desta etapa abre os STT
brutos. Um dossiê não altera a Base e não equivale a um ciclo do Motor.

## Dossiês preparados

| Lote | Tema | Duração | Fontes | Candidatos | Estado |
|---|---|---:|---:|---:|---|
| `STT26-01` | Anunnaki, genética e humanidade | 9:51:16 | 11 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-02` | Anunnaki, genética e humanidade | 10:28:02 | 20 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-03` | Cosmogonia, quedas e história cósmica | 10:11:02 | 10 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-04` | Cosmogonia, quedas e história cósmica | 9:51:24 | 11 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-05` | Cosmogonia, quedas e história cósmica | 9:18:16 | 9 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-06` | Cosmogonia, quedas e história cósmica | 9:56:41 | 18 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-07` | Extraterrestres, tecnologia e cosmos | 11:45:46 | 19 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-08` | Experiência espiritual, morte e ética evolutiva | 10:03:19 | 5 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-09` | Experiência espiritual, morte e ética evolutiva | 10:54:10 | 17 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-10` | Experiência espiritual, morte e ética evolutiva | 11:06:11 | 22 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-11` | Experiência espiritual, morte e ética evolutiva | 10:42:07 | 20 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-12` | Experiência espiritual, morte e ética evolutiva | 11:23:12 | 22 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-13` | Mitologias, tradições e eixo de reintegração | 10:00:17 | 8 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-14` | Mitologias, tradições e eixo de reintegração | 10:38:06 | 10 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-15` | Mitologias, tradições e eixo de reintegração | 10:56:31 | 10 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-16` | Mitologias, tradições e eixo de reintegração | 10:18:10 | 14 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-17` | Mitologias, tradições e eixo de reintegração | 10:55:18 | 8 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-18` | Mitologias, tradições e eixo de reintegração | 10:07:17 | 11 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-19` | Sociedade, comportamento e atualidades | 10:31:38 | 5 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-20` | Sociedade, comportamento e atualidades | 9:16:02 | 11 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-21` | Sociedade, comportamento e atualidades | 9:17:23 | 21 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-22` | Sociedade, comportamento e atualidades | 8:31:14 | 9 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-23` | Sociedade, comportamento e atualidades | 9:50:33 | 9 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |
| `STT26-24` | Sociedade, comportamento e atualidades | 10:02:57 | 9 | 25 | `AGUARDANDO-DESPACHO-CURATORIAL` |

Para preparar o próximo lote planejado, após o anterior ser recebido:

```bash
python3 ferramentas/triagem_stt_lotes_2026_10.py --proximo
```

A preparação é recuperável: `--force` refaz somente o diretório do lote pedido,
depois de validar todos os hashes e endereços de sua entrada.
