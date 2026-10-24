# PROMPT DE CONTINUIDADE — Sessão Arena.ai 06/09/2026 (abertura do F044)

**Repositório:** `institutocura-maker/Termos-RC`
**Branch da sessão anterior:** `arena/01a071c8-termos-rc` · **HEAD `aa38e6b2c`** (pushado, árvore limpa)
**Agente entrante:** a sessão nova nascerá branchada deste head — não há nada NÃO-commitado por trás.

---

## 0. Bootstrap de leitura (nesta ordem, e só depois fale com o Curador)

1. `../admin/logs/STATE-MIRROR.md` (raiz, versionado) — números oficiais, proteções, doutrinas, fila.
2. `.arena/SESSION-NOTES.md` — diário da era F033→F044.
3. `ciclos/F044_misterios-da-vida-de-jesus/ficha_ingresso.md` + `ciclo.toml` — o material da missão atual.
4. `consolidacoes/F043_glossario-krys-amon/` (ciclo concluído; precedente de material externo) e, se precisar de jurisprudência, os dossiês F041/F042.
5. Validação de partida: `python3 ferramentas/dados_termos.py` → deve imprimir **OK: 942 termos, 1898 relações**. Se divergir, PARE e audite antes de tocar em qualquer coisa.

## 1. MISSÃO — F044 · «Os Mistérios da Vida de Jesus» (curso Ellam, 5 aulas)

**Já feito (não repetir):** a receção. 5 `.docx` (57.179 palavras) chegaram por upload web na branch, foram canonizados **byte a byte** em `ciclos/F044_misterios-da-vida-de-jesus/brutos/`, com traslado fiel em `translado/*.txt`, ficha de ingresso, `ciclo.toml` (fase RECEPCAO), `inventario_sha.json` e **REGISTRO-LIMPEZA nº 22**. A caixa `uploads_recepcao/` está zerada de brutos.

**Características da fonte (importantes para o plano):**
- Transcrição automática **revisada linha a linha pelo Curador contra o áudio** — qualidade superior ao STT bruto histórico; marcação `Speaker N [hh:mm:ss]` preservada.
- Terminologia **NÃO padronizada** pela Arca («na época muitos termos ainda não estavam padronizados») — o dicionário de termos/correções é trabalho do ciclo.
- Varredura lexical (06/09/2026): Jesus 996 · Javé 185 · Judas 68 · Maria Madalena 63 · Evangelho 52 · Sophia 44 · Pedro 38 · Cristo 33 · Shiva 28 · Trimurti 5 · Essênios 13 · gnóstic* 25 · Pilatos 21 · Herodes 1 — e **zero** ocorrências de Reb. dos Elétrons / conectoma / Perpérion / negentropia. O curso dialoga com **RC-072 (54 fontes), RC-005, RC-280** — cluster para EXPANDIR, não substituir.
- Metadatas dos docx (25 e 31/12/2023; 27/04/2015×3) são datas de **salvação da revisão/conversão, não do evento**. Dado narrativo não gera código de data.

**Protocolo proposto (cada passo executado só com despacho do Curador):**
1. **Despacho de datas** → códigos `P20XX-XX-XX` para as 5 aulas (ou código provisório assinado).
2. **Mapeamento integral**: leitura integral do traslado (57k palavras em chunks) + censo de todo termo/nome/evento **contra `ferramentas/dados_termos.py` e `termos/`** — censo estrito NO registro-mestre antes de propor código (lição IEEA: `ls termos/` PARA DE CONTAR; o censo de código é dados_termos.py ∩ ausência de ficha, checado em python).
3. **Dossiê com anéis** (padrão F043: quem já tem ficha e só é corroborado; quem merece ampliação; quem merece código novo; o que fica guardado aguardando) em `consolidacoes/F044_.../`.
4. **Execução por lote assinado**: ampliações de fichas, vínculos na tabela FONTES, notas de anterioridade sem retrodatação; **1 novo código por ficha nova**; relacoes/ blindado.
5. **Fecho**: `python3 ferramentas/dados_termos.py` → rebuild de espelhos (`pip install -q --user --break-system-packages openpyxl python-docx && python3 ferramentas/build_indice.py && python3 ferramentas/build_xlsx.py && python3 ferramentas/build_word.py`) → STATE-MIRROR + notes + ciclo.toml atualizados → commit+push.

## 2. Doutrinas permanentes (viagem na mala — todas nasceram de despacho, não de preferência)

- **«Nada além do assinado por lote.»** O Curador despacha; você executa o despacho. VIGÍLIA: sem despacho, não iniciar mutirão, censo novo nem aquisição.
- **Âncoras verbatim** com assert de hash na gravação; citações só intra-linha; F033-QB vivo.
- **Proteções inegociáveis:** RC-091 l.65 intocável (assert prefixo `80ec9a033914…`); RC-047 l.65 (assert `95cf6f5f5f…`) — a l.70 da RC-047 já foi convertida em **averbação definitiva Perpérion** (06/09/2026), não reabrir sem despacho novo.
- **Áudio > transcrição**; STT nunca renomeado por conveniência; AGUARDA-ÁUDIO = encerramento administrativo honesto; 12+4 transcrições aguardam re-odiamento (renomeio só com áudio).
- **`relacoes/`/arestas blindados**: nenhuma aresta sem despacho taxonômico estruturado (a malha está em 1.898 desde sempre; mutirões de fonte nunca criaram arestas).
- **Fontes externas** seguem o precedente F043: canonização byte a byte + ficha de ingresso + REGISTRO-LIMPEZA (próximo nº: **23**) + expurgo da caixa (regra EXPURGAR-SÓ-CANONIZADO, verificação sha antes de deletar). Obra de apoio de parceiro humano = **fonte secundária nunca co-autoria** (caso GKA/RC-934; Anel D do GKA continua guardado na fonte sem códigos, à espera do Ellam).
- **Ledger do Curador**: 47 resíduos chancelados; régua bruta = 4 menções literais; dívida «perdoada até novas evidências»; reabertura só por portão.
- Divergência com a academia NÃO é pauta; menção literal ≠ flag; ficha nova limpa não mexe na régua.

## 3. Armadilhas conhecidas (cada uma custou uma sessão)

- **TOML só ASCII** (chave acentuada quebrou commit em 06/09; `tomllib.load` sempre antes de gravar).
- **Nunca encadear validação+gravação+git com `&&` único sem assert entre os passos** (o split feio da receção F044 veio daí).
- Matcher por **nome de arquivo** perde hifenizados — resolva por `glob termos/RC-NNN-*.md`.
- **Sigla curta sem word-boundary** encharca falso-positivo (caso «adhy»).
- `sed -n 'Np'` de linha longa oculta selos à direita — conte ocorrências do token na linha inteira.
- Cadastro em replace: verificar **pós-escrita** por `set(codes)` + `len(TERMOS)`, nunca por «o código existe».
- Upload do Curador via **web vai para a branch default** (não a main!) — quando «não chegar nada na caixa», `git fetch` + `gh api .../contents/uploads_recepcao` primeiro.
- Sessão nova **só sobrevive do que está em git**: nada de espelho fora do repositório; ../admin/logs/STATE-MIRROR.md é versionado agora.

## 4. Primeira resposta ao Curador

Reconheça o estado (942/632/1898/102 + F044 RECEPCAO concluída), confirme os itens do despacho que ele precisa dar — **datas reais das 5 aulas** e alcance do mapeamento — e só então abra a leitura integral. Tom: português do Brasil, direto, com tabelas de balanco no fim de cada lote.

*— ditado na sessão de Agente 20, 06/09/2026, ao fechar o F043 e receber o F044.*
