# PROMPT DE CONTINUIDADE — Sessão Arena.ai 07/09/2026 (fase pedagógica top-down)

**Repositório:** `institutocura-maker/Termos-RC`
**Branch da sessão:** `arena/01a07777-termos-rc` · **HEAD `ec62a83`** (pushado, árvore limpa)
**Agente entrante:** a sessão nova nascerá branchada deste head — não há nada NÃO-commitado por trás.

---

## 0. Bootstrap de leitura (nesta ordem, e só depois fale com o Curador)

1. `../admin/logs/STATE-MIRROR.md` (raiz, versionado) — números oficiais, proteções, doutrinas, fila.
2. **`PROMPT-CONTINUIDADE-2026-09-07-PEDAGOGIA-TOP-DOWN.md`** (este arquivo) — o estado da fase pedagógica.
3. `pedagogico/top-down/README.md` — o índice completo das 10 apostilas publicadas (verificado).
4. Validação de partida: `python3 ferramentas/dados_termos.py` → deve imprimir **OK: 946 termos, 1898 relações**. Se divergir, PARE e audite antes de tocar em qualquer coisa.

---

## 1. MISSÃO — Fase pedagógica top-down (concluída neste ciclo)

**Escopo:** aplicar o método top-down (Analista de Sistemas de IBM) ao curso da Revelação Cósmica,
produzindo **apostilas de estudo** que são **síntese de leitura** — NÃO alteram a Base
(`termos/`, `relacoes/`, `ferramentas/dados_termos.py`). Todo material vai para `pedagogico/top-down/`.

**O que foi entregue (10 apostilas publicadas + README + Making-Of):**
- 1ª **A Queda** (`c555afa`) — cronologia da crise, 12 PARTES, 100 RC-###.
- 2ª **Javé — o Buraco Negro** (`f15e354`) — biografia cósmica de RC-001, 12 PARTES, 99 RC-###.
- 3ª **O Lado de Fora do Universo** (`b4d5a33`) — 13 PARTES, 72 RC-###.
- 4ª **O Mapa dos Mundos e Lokas** (`b3144fc`) — 12 PARTES, 79 RC-###.
- 5ª **Céu Tradicional × Paraíso das RC** (`247189e`) — 12 PARTES, 61 RC-###.
- 6ª **Arqueologia dos Termos** (`7d4eb36`) — 12 PARTES, 86 RC-###.
- 7ª **Thot e Hermes** (`fd1ec16`) — 10 PARTES, 50 RC-###.
- 8ª **Pilotando o Cérebro no Caos** (`0045383`) — 12 PARTES, 57 RC-###.
- 9ª **Carbono × Sílica** (`c16ca12`) — 12 PARTES, 36 RC-###.
- 10ª **Os Tratados** (`85a1859`) — 12 PARTES, 27 RC-###.
- **README.md da pasta** (`595c369`) — índice completo + mapeamento em fases.
- **Making-Of do Agente** (`ec62a83`) — MD + DOCX lilás em `pedagogico/`.

**Regra usada em todas:** cabeçalho `@` (titulo/autor/data/local/subtitulo/nota_editor) →
`# PARTE` → glossário → caderno de incertezas → `FIM`. DOCX gerado por `ferramentas/build_apostila.py`.
**Validação antes de publicar:** remissões RC-### únicas e existentes (nenhuma órfã), contagem de
PARTES, campos `@`, término em `FIM` — via `python3` inline.

---

## 2. Do que depende a continuidade (não repetir)

- **Base intacta:** `OK: 946 termos, 1898 relações` (tudo foi síntese; nada alterado).
- **Formato de cada apostila** e o **gancho conceitual** (o "avanço-chave") já estão em cada MD.
- **Proposta original:** `pedagogico/top-down/PROPOSTA-PEDAGOGICA-TOP-DOWN.md` — define 4+1 níveis (N0→N4)
  e o Caminho de Leitura em 5 fases; o README atual já reflete o fechamento das 10 apostilas.

---

## 3. Próximos caminhos possíveis (aguardar despacho do Curador)

1. **Mapa de Abstração** (sugestão de melhoria pedagógica nº 1 da proposta): um diagrama de contexto
   SVG/PDF com as 4 caixas (FORA / ACIDENTE / TRIMURTI / AQUI) + as 7 narrativas como setas.
2. **Fase 5 da proposta** — o detalhe na Base: consultar fichas RC sob demanda (a partir de uma narrativa).
3. **DOCX de qualquer apostila que precise ser regerado/ajustado** — via `build_apostila.py`.
4. **Novo material pedagógico** em `pedagogico/top-down/` (se houver tema novo autorizado).

---

## 4. Avaliação de ocupação de contexto (07/09/2026)

Metodologia: **por peso de arquivo lido/gerado** nesta sessão (aproximação honesta; o contexto real
inclui também o diálogo, o system prompt e as saídas de ferramentas, não só arquivos).

**Volumes lidos/processados nesta sessão (bytes):**
- Tratados-base e fichas-âncora (fontes da 9ª/10ª): ~130 KB (3 Tratados + ~15 fichas RC-###).
- 10 apostilas top-down (MD) re-verificadas: ~225 KB (soma dos `.md`).
- Transições/cabeçalhos/`@` e metadados: n/a (embutidos nos MD).

**Estimativa de contexto consumido (fase pedagógica):** a maior carga não veio dos arquivos
**em si**, mas das **janelas grandes de leitura** (3 Tratados com 22–32 KB cada, fichas, a 8ª apostila
inteira de 18 KB) somadas às **sínteses longas re-escritas** (cada apostila 13–31 KB). Aproximadamente
**350–450 KB de texto** atravessaram a janela nesta fase, incluindo as idas-e-vindas de validação.
*Ressalva:* a janela real de um modelo não é soma de bytes (tokens); este número serve como **indicador
de peso relativo**, não como medida de tokens. O ponto prático: **a fase top-down já está fechada no git**,
então um novo chat **não precisa re-carregar** as apostilas nem os tratados — basta o README + este prompt.

**Recomendação:** para a nova sessão, carregar **pouco** (STATE-MIRROR + README + este prompt) e ler
arquivos **sob demanda**. Como a fase está commitada, o contexto máximo necessário é baixo.

---

## 5. Armadilhas conhecidas (herdadas — cada uma custou uma sessão)

- **TOML só ASCII** (chave acentuada quebrou commit; `tomllib.load` sempre antes de gravar).
- **Nunca encadear validação+gravação+git com `&&` único sem assert entre os passos.**
- **Censo de CÓDIGO = `ferramentas/dados_termos.py`** (registro-mestre), NUNCA `ls termos/` (lição IEEA).
- **`relacoes/`/arestas blindados**: nenhuma aresta sem despacho taxonômico estruturado (malha fixa em 1.898).
- **Matcher por nome de arquivo** perde hifenizados — use `glob termos/RC-NNN-*.md`.
- **Sigla curta sem word-boundary** encharca falso-positivo (caso «adhy»).
- **Verificar pós-escrita** por `set(codes)` + `len(TERMOS)`; **STT nunca renomeado por conveniência**.
- **Áudio > transcrição**; AGUARDA-ÁUDIO = encerramento administrativo honesto.
- **Dado narrativo não gera código de data**; divergência com a academia não é pauta.
- Sintaxe bash: não usar `2>/dev/null` dentro de pipe com `awk $5` (quebra o parsing — ocorreu nesta sessão).

---

## 6. Primeira resposta ao Curador na nova sessão

Reconheça o estado (946/638/1898/102 + fase pedagógica top-down **fechada**: 10 apostilas + README +
Making-Of), confirme que a **Base está intacta** e o working tree **limpo**, e pergunte qual o próximo
caminho (Mapa de Abstração / Fase 5 / novo material). Tom: português do Brasil, direto, com tabelas.

*— ditado na sessão de Agente, 07/09/2026, ao fechar a fase pedagógica top-down.*
