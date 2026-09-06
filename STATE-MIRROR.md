# ESTADO-MIRROR · Termos-RC — espelho de continuidade (arquivo VISIONADO, em git)
> Regra de sobrevivência entre sessões: **só o que está em git sobrevive ao clone**. Este espelho substitui o antigo STATE-MIRROR fora do repositório (perdido na migração 2026-09). Sessão nova: ler este arquivo + `.arena/SESSION-NOTES.md` + o último `consolidacoes/F0NN_*/`.

## 0. Identidade operacional (2026-09-06)
- Sessão = repositório = **branch `arena/01a071c8-termos-rc`** (head pushado `f0d5ddb3e5`). A branch `main` é obsoleta. Agente = **Agente 20**; curador humano despacha, agente executa sob autorização expressa ("nada além do assinado por lote").
- Validador/self-test: `python3 ferramentas/dados_termos.py` → hoje: **OK: 942 termos, 1898 relações**.

## 1. Números oficiais
- Base: **942 termos · 632 fichas · 1898 relações · 102 obras** (espelhos `indice-mestre.md`, xlsx/docx reconstruídos em 06/09/2026 — a cada turno de espelho: `pip install -q --user --break-system-packages openpyxl python-docx`).
- Censo de CÓDIGO = `ferramentas/dados_termos.py` (registro-mestre), NUNCA nomes de `termos/` (lição IEEA: fichas paravam em RC-929, registro ia a 933; F043 quase duplicou código).
- Ledger do Curador: **47 resíduos chancelados** (F041: 33 + F042: 14) · régua BRUTA = **4** (menções literais em 3 fichas-meta + 1 já averbada na reabertura RC-047) · "perdoado até novas evidências", reabertura só por portão.
- `uploads_recepcao/`: só README + .gitkeep + 8 registros-antigos na raiz (contabilidade histórica, intocável). Caixa canônica de expurgo = `backups/REGISTRO-LIMPEZA-*.json`, último **nº 21**.

## 2. Proteções inegociáveis
- **RC-091 · linha 65** intocável (assert `80ec9a033914...`); **RC-047 · linha 65** decisão (assert `95cf6f5f5f...`); l.70 da RC-047 = chancela AGUARDA-ÁUDIO convertida em **averbação definitiva Perpérion** (06/09/2026, F043-T3).
- `relacoes/`/espelho de relações **blindado**: nenhuma aresta sem despacho taxonômico estruturado. Áudio ⟶ **prioridade sobre transcrição**; STT nunca renomeado por conveniência; AGUARDA-ÁUDIO = encerramento administrativo honesto.
- Citações verbatim só intra-linha; toda âncora com assert de hash; divergência com a academia NÃO é pauta; dado narrativo não gera código de data.
- VIGÍLIA: sem despacho, não iniciar mutirão/censo/aquisição nova; "um censo furado não autoriza ações autônomas".

## 3. Fontes externas e obras de apoio (precedente F043)
- Padrão de ingresso: cópia byte a byte em `materiais_externos/AAAA-MM-DD_slug/` (original.txt + traslado limpo + ficha_ingresso.md EXT-… + analise/PARECER) → **REGISTRO-LIMPEZA nº N** em `backups/` → expurgo do bruto da caixa → ficha-pessoa do autor se não cadastrada (censo estrito antes!).
- **GKA (Glossário Krys Amon, EXT-2024-01-04, autor RC-934) = Obra de Apoio, fonte SECUNDÁRIA, nunca co-autoria.** Anéis A (10) e B (6+costura RC-160) notificados "GKA corrobora"; Anel C = 8 fichas RC-935..942; **Anel D guardado na fonte sem códigos** (Éon, Agam Karan, …). Ficha RC-150 = TENSÃO NÃO-RESOLVÍVEL (guarda histórica, sem edição).

## 4. Missões encerradas
- **F041** (33 chancelas) e **F042** (14 chancelas) — dossiês em `consolidacoes/`.
- **F043** Glossário Krys Amon — T1 canônica, T2 16 notas, T3 8 fichas + reabertura averbada; **CONCLUÍDO** 06/09/2026; dossiê `consolidacoes/F043_glossario-krys-amon/` (ciclo.toml status concluido; DECISAO com adenda de execução).

## 5. Fila / próximo despacho esperado
- **F044 · "Os Mistérios da Vida de Jesus" (curso amplo de Ellam)** — anunciado pelo Curador em 06/09/2026 para SESSÃO NOVA; nada chegou à caixa ainda. Cluster a expandir (NÃO substituir): RC-072 (54 fontes), RC-005, RC-280; obras B014/B003/B025/B043 etc. já no roster de obras. Protocolo sugerido de abertura: recepção do bruto → ficha de ingresso/registro (se material externo) → traslado/STT → mapeamento com censo → dossiê F044 com anéis → execução só por despacho.
- Pendências de portão: 12+4 transcrições a re-odiar (decisão de renomeio só com áudio); Anel D à espera de chancela do Ellam.
