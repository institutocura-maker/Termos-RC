# ADR-001 — Arquitetura por Regimes de Verdade

> **Status:** ACEITO (despacho curatorial de 27/10/2026) · **Data:** 27/10/2026
> **Branch:** `arena/ad2ca972-termos-rc` · **Commit de partida:** `093a08c`
> **Origem:** reflexão arquitetural conjunta Curador + Arena.ai Agent Mode, após o encerramento da Onda 2.
> **Autor da redação:** Arena.ai Agent Mode.
> **Documentos de referência:** `APRESENTACAO-DO-SISTEMA.md` §9 · `docs/MAPA-DADOS-DA-BASE-RC.md` · `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md` · `diagnostico/DIAGNOSTICO-T14-REGENERACAO-ESPELHOS-2026-10-27.md`.

---

## 1. Contexto

### 1.1 Trajetória

O projeto nasceu como um glossário de termos técnicos extraídos de livros de Jan Val Ellam. Cresceu organicamente: relações entre termos, ancoragem em obras, palestras, vídeos do YouTube, transcrições STT, pérolas, verbetes, apostilas, corpus de treinamento e, na Onda 2, as cinco gavetas semânticas (H2). Estado congelado em `093a08c`:

**946 termos · 826 fichas · 1.887 relações · 104 obras · 7.917 linhas de relação T2 · 310 brutos STT · 299 pérolas · 659 verbetes · 6.065 arquivos / 249,62 MB.**

### 1.2 Diagnóstico

A organicidade foi a **única via possível** para descobrir o domínio. Não se sabia, em agosto, que seria necessária quarentena epistemológica, que haveria 24 eixos STT ou que grafias como `Hochmah`/`Rockman` seriam decisões curatoriais. O Markdown funcionou como laboratório vivo. **Não se corrige um erro aqui; formaliza-se uma maturidade.**

A dívida não está nos dados — está na **ausência de fronteiras estruturais entre tipos de afirmação**. Sete sintomas convergem para a mesma causa:

| Sintoma (vivido nesta sessão) | Causa estrutural |
|---|---|
| `canonico.json` defasado (820 vs 826 fichas) e 274 siglas ausentes | Verdade-mestra em três lugares (`.py`, `.json`, badges), sincronizada por convenção |
| T14 falha desde a Onda 2 (821 tabelas) | Validação por regex sobre Markdown — o formato do texto é o contrato |
| README/STATE-MIRROR divergentes (820 / 689 / 102) | Espelhos gerados e espelhos manuais no mesmo espaço de autoridade |
| 5 builds totais + 2 binários (2,4 MB) versionados | Derivados tratados como dados, não como funções puras |
| 24 dossiês `PENDENTE` sem ciclo aberto | Fluxo de decisão vive em arquivos, não em estados consultáveis |
| Siglas `B###`, `P####-##-##`, `STT26-*`, `OIDR26-*` numa lista plana | Proveniência como string, não como entidade tipada |
| `POLITICA-QUARENTENA` dependente de disciplina humana | Fronteira epistemológica anotada em prosa, não construtiva |

Causa única: **o sistema não distingue, estruturalmente, o que a fonte disse, o que o curador afirma e o que o modelo infere.** Quando tudo é texto Markdown, tudo tem o mesmo peso ontológico.

### 1.3 Patrimônio a preservar (inalienável)

1. **Paridade byte a byte do lastro** — nenhuma aspa, erro de STT ou grafia degradada é corrigida sem despacho.
2. **Códigos imutáveis** `RC-001…RC-946` como âncora estável.
3. **Decisão curatorial explícita** — autor, data, despacho, fundamento.
4. **Separação fonte primária × derivado** — `fontes/` intocável.
5. **Quarentena epistemológica** — `POLITICA-QUARENTENA-ENTRE-ECOSSISTEMAS.md`.
6. **Markdown como interface de leitura humana de primeira classe.**

---

## 2. Decisão

Adota-se a **Arquitetura por Regimes de Verdade**, com quatro decisões vinculantes.

### 2.1 Três regimes, física e logicamente separados

| Regime | Nome | Natureza | Mutabilidade | Local físico |
|---|---|---|---|---|
| **R1** | **Verbatim** | O que a fonte disse | **Imutável**, content-addressed | `fontes/` (intocável) + `citacao.sha256_trecho` |
| **R2** | **Asserção Curatorial** | O que a Base afirma | Versionada, com despacho | Store SQLite (`kb/base.sqlite` — a criar) |
| **R3** | **Inferência** | O que o modelo produz | **Efêmera**, reconstruível | Índice vetorial, embeddings, grafos de consulta, respostas LLM |

```
R1 ──citação (hash + localizador + confiança)──> R2 ──projeção (função pura)──> R3
                                                  │
                                                  └──renderização──> fichas .md (view)
```

**Regra de ouro:** nenhuma asserção do R2 nasce sem referência a um hash do R1; nenhuma saída do R3 é persistida como fato no R2. Toda resposta do R3 carrega a lista de `sha256` que a sustentam.

### 2.2 Markdown como projeção ("view")

As fichas `termos/RC-*.md` deixam de ser fonte da verdade e passam a ser **renderizações determinísticas** do R2. A interface Markdown é patrimônio cultural e será mantida com **100% de prioridade visual** — a mudança é de *autoria*, não de apresentação. O esqueleto de 5 gavetas H2 da Onda 2 é o template de referência.

Consequência direta: a falha T14 desaparece, porque deixa de haver regex adivinhando formato — há um serializador e um desserializador com contrato único.

### 2.3 SQLite relacional, sem Event Sourcing

Para o R2 adota-se **SQLite** com `PRAGMA foreign_keys = ON`. Modelam-se explicitamente as tabelas `termo`, `obra`, `fonte`, `citacao`, `relacao` e `despacho` (mais três de apoio: `candidato`, `auditoria`, `projecao` — nove tabelas no total, mais três views).

**Decisão de simplificação (despacho expresso):** **não** se constrói infraestrutura de Event Sourcing com motor de replay neste momento. Usam-se **registros relacionais diretos + logs simples de auditoria/despacho**. O banco deve permanecer limpo, legível e consultável em SQL por um humano. A tabela `auditoria` é um log append-only de operações — suficiente para rastreabilidade, sem replay.

### 2.4 Transição por *Strangler Fig*

- **Piloto:** os **310 brutos STT** e os **áudios inéditos de outubro** estreiam a nova arquitetura, entrando direto pelo store estruturado com **timestamps** e **marcadores de incerteza de transcrição**.
- **Não-invasão:** as **826 fichas atuais permanecem intocadas** até que o pipeline do lote de outubro seja validado e a **projeção reversa** (gerar `.md` a partir do banco) prove **paridade de 100%**.
- O legado (`dados_termos.py` + `canonico.json` + espelhos) continua servindo por um adaptador, que encolhe gradualmente.

---

## 3. Modelo de dados (DDL SQLite)

> **DDL validado em SQLite 3 em memória nesta redação** (bloco extraído e executado): 9 tabelas, 3 views, 19 índices, `foreign_key_check` vazio. Testes de violação deliberada confirmaram o bloqueio de auto-relação (I-08), FK órfã, hash curto (I-18), localizador incompleto (I-06) e `HOLD` + `verificado` (I-11); um par válido de timestamps de áudio foi aceito. **Nenhum arquivo `.sqlite` é criado nesta fase** — o schema entra em vigor na Fase 0 do roteiro (§6).

```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- ============================================================ R2 · CATÁLOGO
CREATE TABLE obra (
  codigo            TEXT PRIMARY KEY,               -- B031 | P2023-12-03 | ART-2025-08-01 | STT26-01 | EXT-...
  tipo              TEXT NOT NULL CHECK (tipo IN
                    ('LIVRO','PALESTRA','APOSTILA','VIDEO','AUDIO','EIXO_STT','ARTIGO','EXTERNA','PEROLA')),
  titulo            TEXT NOT NULL,
  subtitulo         TEXT,
  editora           TEXT,
  ano               TEXT,
  status            TEXT,
  nota              TEXT,
  origem_legado     TEXT,                           -- 'base/biblio.json' | 'INVENTARIO-APOSTILAS.json' | ...
  CHECK (length(codigo) >= 3)
);

-- ============================================================ R1 · FONTE FÍSICA
CREATE TABLE fonte (
  fonte_id                  INTEGER PRIMARY KEY,
  obra_codigo               TEXT NOT NULL REFERENCES obra(codigo),
  natureza                  TEXT NOT NULL CHECK (natureza IN
                            ('BRUTO','DERIVADO_NORMALIZADO','COMPOSICAO_CICLO','AMOSTRA')),
  caminho                   TEXT NOT NULL UNIQUE,
  sha256                    TEXT NOT NULL,
  bytes                     INTEGER NOT NULL CHECK (bytes >= 0),
  mimetype                  TEXT,
  -- metadados de mídia (presentes no frontmatter dos 310 brutos STT)
  duracao                   TEXT,                 -- '1:23:28'
  id_youtube                TEXT,
  link_original             TEXT,
  data_publicacao_original  TEXT,                -- ISO 8601
  data_transcricao          TEXT,
  motor_neural              TEXT,                -- 'faster-whisper large-v3 (FP16 / CUDA)'
  confianca_transcricao     TEXT NOT NULL DEFAULT 'NAO_AVALIADA'
                            CHECK (confianca_transcricao IN
                            ('ALTA','MEDIA','BAIXA','NAO_AVALIADA')),
  declarada_em              TEXT,                -- manifesto que declarou a proveniência
  UNIQUE (obra_codigo, caminho),
  CHECK (length(sha256) = 64)
);

CREATE INDEX idx_fonte_obra    ON fonte(obra_codigo);
CREATE INDEX idx_fonte_natureza ON fonte(natureza);
CREATE INDEX idx_fonte_youtube ON fonte(id_youtube);

-- ============================================================ R1 → R2 · CITAÇÃO
CREATE TABLE citacao (
  citacao_id            INTEGER PRIMARY KEY,
  fonte_id              INTEGER NOT NULL REFERENCES fonte(fonte_id),
  localizador           TEXT NOT NULL,           -- 'p. 14' | 'cap. 2' | 'U00076' | 'chars 81882-82260' | '00:14:32-00:15:08'
  unidade               TEXT,                   -- 'U00076' (endereço estável do mapa-linhas)
  linha                 INTEGER,
  chars_ini             INTEGER,
  chars_fim             INTEGER,
  t_ini                 TEXT,                   -- timestamp de ÁUDIO (novo, lote outubro)
  t_fim                 TEXT,
  sha256_trecho         TEXT NOT NULL,
  texto_verbatim        TEXT NOT NULL,           -- IMUTÁVEL: nunca corrigido, nunca parafraseado
  grafia_encontrada     TEXT,
  regime_epistemico     TEXT NOT NULL DEFAULT 'CANONICO_RC' CHECK (regime_epistemico IN
                        ('CANONICO_RC','LEITURA_FENOMENOLOGICA','CORRELACAO_EXTERNA','HIPOTESE','NAO_ONTOLOGIZADO')),
  confianca_transcricao TEXT NOT NULL DEFAULT 'NAO_AVALIADA' CHECK (confianca_transcricao IN
                        ('ALTA','MEDIA','BAIXA','NAO_AVALIADA')),
  criado_em             TEXT NOT NULL,
  CHECK (length(sha256_trecho) = 64),
  -- par de localizadores: ou ambos presentes, ou ambos ausentes (I-06)
  CHECK ((t_ini IS NULL AND t_fim IS NULL) OR (t_ini IS NOT NULL AND t_fim IS NOT NULL)),
  CHECK ((chars_ini IS NULL AND chars_fim IS NULL) OR (chars_ini IS NOT NULL AND chars_fim IS NOT NULL)),
  CHECK (chars_fim IS NULL OR chars_ini IS NULL OR chars_fim >= chars_ini),
  CHECK (t_fim IS NULL OR t_ini IS NULL OR t_fim >= t_ini),
  UNIQUE (fonte_id, localizador, sha256_trecho)
);

CREATE INDEX idx_citacao_fonte    ON citacao(fonte_id);
CREATE INDEX idx_citacao_unidade  ON citacao(unidade);
CREATE INDEX idx_citacao_regime   ON citacao(regime_epistemico);

-- ============================================================ R2 · TERMO
CREATE TABLE termo (
  codigo            TEXT PRIMARY KEY,             -- RC-001 … RC-946 (IMUTÁVEL)
  nome              TEXT NOT NULL,
  categoria         TEXT NOT NULL,
  subcategoria      TEXT NOT NULL,
  status            TEXT NOT NULL CHECK (status IN
                    ('candidato','provisório','em análise','verificado')),
  via               TEXT CHECK (via IN ('P6-evidência','P7-conhecimento')),
  confianca_fonte   TEXT CHECK (confianca_fonte IN ('alta','média','baixa')),
  gaveta_padrao     TEXT CHECK (gaveta_padrao IN ('1','2','3','4','5')),  -- Onda 2
  hold              INTEGER NOT NULL DEFAULT 0 CHECK (hold IN (0,1)),
  ficha_projetada   INTEGER NOT NULL DEFAULT 0 CHECK (ficha_projetada IN (0,1)),
  atualizado        TEXT NOT NULL,               -- ISO 8601
  origem_legado     TEXT,
  CHECK (codigo GLOB 'RC-[0-9][0-9][0-9]'),
  CHECK (hold = 0 OR status <> 'verificado')    -- I-11: HOLD nunca é 🟢
);

CREATE INDEX idx_termo_status ON termo(status);
CREATE INDEX idx_termo_hold   ON termo(hold);

-- ============================================================ R2 · DESPACHO
CREATE TABLE despacho (
  despacho_id   INTEGER PRIMARY KEY,
  codigo        TEXT NOT NULL UNIQUE,            -- 'T2-MATRIZ-998' | 'STT26-01' | 'ADR-001'
  tipo          TEXT NOT NULL CHECK (tipo IN
                ('CHANCELA','TRIAGEM_LOTE','QUARENTENA','MIGRACAO','NORMALIZACAO','MATRIZ_RELACAO')),
  lote_id       TEXT,
  estado        TEXT NOT NULL DEFAULT 'PENDENTE' CHECK (estado IN
                ('PENDENTE','EM_TRIAGEM','AUTORIZADO','RECUSADO','ENCERRADO')),
  emitido_por   TEXT NOT NULL,
  emitido_em    TEXT NOT NULL,
  decidido_em   TEXT,
  fundamento    TEXT,
  artefato      TEXT,                           -- caminho do .md/.json de origem
  observacao    TEXT,
  CHECK (decidido_em IS NULL OR estado IN ('AUTORIZADO','RECUSADO','ENCERRADO'))
);

CREATE INDEX idx_despacho_lote   ON despacho(lote_id);
CREATE INDEX idx_despacho_estado ON despacho(estado);

-- ============================================================ R2 · RELAÇÃO
CREATE TABLE relacao (
  relacao_id  INTEGER PRIMARY KEY,
  a           TEXT NOT NULL REFERENCES termo(codigo),
  b           TEXT NOT NULL REFERENCES termo(codigo),
  tipo        TEXT NOT NULL,                    -- vocabulário controlado (23 relações T2) ou tipo_bruto
  direcao     TEXT NOT NULL CHECK (direcao IN ('->','<-','<->','-')),
  notas       TEXT,
  origem      TEXT NOT NULL DEFAULT 'GRAFO_CURATORIAL' CHECK (origem IN
              ('GRAFO_CURATORIAL','TABELA_T2','NAVEGACAO_AMPLA')),
  despacho_id INTEGER REFERENCES despacho(despacho_id),
  CHECK (a <> b),
  UNIQUE (a, b, tipo, direcao)
);

CREATE INDEX idx_relacao_a ON relacao(a);
CREATE INDEX idx_relacao_b ON relacao(b);
CREATE INDEX idx_relacao_tipo ON relacao(tipo);

-- ============================================================ R2 · CANDIDATO (triagem STT)
CREATE TABLE candidato (
  evidencia_id       TEXT PRIMARY KEY,          -- 'STT26-01-RC-086-001'
  lote_id            TEXT NOT NULL,             -- 'STT26-01'
  termo_codigo       TEXT NOT NULL REFERENCES termo(codigo),
  citacao_id         INTEGER REFERENCES citacao(citacao_id),
  ingresso_id        TEXT NOT NULL,             -- 'STT-2026-10-011'
  unidade            TEXT,
  grafia_encontrada  TEXT,
  sinais_exatos      INTEGER NOT NULL DEFAULT 0 CHECK (sinais_exatos >= 0),
  decisao            TEXT NOT NULL DEFAULT 'PENDENTE' CHECK (decisao IN
                     ('PENDENTE','AUTORIZAR_COTEJO_AMPLIADO','RECUSADO','HOMOLOGADO')),
  fundamento         TEXT,
  despacho_id        INTEGER REFERENCES despacho(despacho_id)
);

CREATE INDEX idx_candidato_lote  ON candidato(lote_id);
CREATE INDEX idx_candidato_termo ON candidato(termo_codigo);
CREATE INDEX idx_candidato_dec   ON candidato(decisao);

-- ============================================================ R2 · AUDITORIA (log simples)
CREATE TABLE auditoria (
  auditoria_id   INTEGER PRIMARY KEY,
  tabela         TEXT NOT NULL,
  registro_id    TEXT NOT NULL,
  operacao       TEXT NOT NULL CHECK (operacao IN ('INSERT','UPDATE','DELETE','DESPACHO')),
  campo          TEXT,
  valor_anterior TEXT,
  valor_novo     TEXT,
  despacho_id    INTEGER REFERENCES despacho(despacho_id),
  ocorrido_em    TEXT NOT NULL,
  autor          TEXT NOT NULL
);

CREATE INDEX idx_auditoria_registro ON auditoria(tabela, registro_id);
CREATE INDEX idx_auditoria_despacho ON auditoria(despacho_id);

-- ============================================================ R2 · PROJEÇÃO (paridade)
CREATE TABLE projecao (
  projecao_id      INTEGER PRIMARY KEY,
  termo_codigo     TEXT NOT NULL REFERENCES termo(codigo),
  caminho          TEXT NOT NULL UNIQUE,       -- 'termos/RC-086-pandora.md'
  sha256_gerado    TEXT NOT NULL,
  sha256_legado    TEXT,
  paridade         INTEGER NOT NULL DEFAULT 0 CHECK (paridade IN (0,1)),
  versao_template  TEXT NOT NULL,              -- 'onda2-v1'
  gerado_em        TEXT NOT NULL,
  CHECK (length(sha256_gerado) = 64),
  CHECK (sha256_legado IS NULL OR length(sha256_legado) = 64)
);

CREATE INDEX idx_projecao_paridade ON projecao(paridade);

-- ============================================================ VIEWS (consultas vivas)
CREATE VIEW v_numeros_oficiais AS
SELECT
  (SELECT count(*) FROM termo)                              AS termos,
  (SELECT count(*) FROM termo WHERE ficha_projetada = 1)  AS fichas,
  (SELECT count(*) FROM relacao)                           AS relacoes,
  (SELECT count(*) FROM obra)                              AS obras;

-- Reproduz a tabela de 5 colunas da T2 sem parsear Markdown.
CREATE VIEW v_tabela_relacoes AS
SELECT r.a AS codigo_origem, t.nome AS termo_destino, r.b AS codigo_destino,
       r.tipo AS relacao, r.direcao AS direcao, COALESCE(r.notas,'-') AS notas
FROM relacao r JOIN termo t ON t.codigo = r.b
WHERE r.origem = 'TABELA_T2'
ORDER BY r.a, r.b;

-- Estado dos 24 lotes do piloto (substitui a leitura de 24 JSONs).
CREATE VIEW v_triagem_lotes AS
SELECT c.lote_id,
       count(*) AS candidatos,
       sum(CASE WHEN c.decisao = 'PENDENTE' THEN 1 ELSE 0 END) AS pendentes,
       sum(CASE WHEN c.decisao = 'AUTORIZAR_COTEJO_AMPLIADO' THEN 1 ELSE 0 END) AS autorizados,
       d.estado AS estado_despacho
FROM candidato c LEFT JOIN despacho d ON d.lote_id = c.lote_id
GROUP BY c.lote_id;
```

### 3.1 Notas de modelagem

- **`obra.tipo`** resolve a mistura atual de siglas numa lista plana: `B###` → `LIVRO`, `P####-##-##` → `PALESTRA`, `STT26-*` → `EIXO_STT`, `ART-*` → `ARTIGO`, `EXT-*` → `EXTERNA`. Um `EIXO_STT` pode agregar várias `fonte` do tipo `VIDEO`.
- **`fonte` vs `citacao`:** `fonte` é o arquivo inteiro com seu SHA-256; `citacao` é o recorte endereçado. O mesmo hash de arquivo pode sustentar milhares de citações sem duplicar bytes.
- **`t_ini`/`t_fim`** são a novidade do piloto: o áudio passa a ser localizador de primeira classe, ao lado de `p.`, `cap.`, `U00076` e `chars`.
- **`regime_epistemico`** é a `POLITICA-QUARENTENA` tornada construtiva. `CORRELACAO_EXTERNA` e `HIPOTESE` ficam **fora** do índice vetorial canônico por construção (ver §5.2).
- **`projecao`** é a tabela que prova a paridade da projeção reversa, ficha por ficha.
- **Sem `NOT NULL` em `texto_verbatim`?** Há — e `IMUTÁVEL` é garantido pelo invariante I-03 (§4), não por `CHECK`.

---

## 4. Invariantes de validação

Invariantes são **portões declarativos**, substituindo os 23 testes que farejam Markdown. Cada um tem consulta SQL executável; `SELECT` deve retornar **zero linhas**.

| ID | Invariante | Verificação SQL |
|---|---|---|
| **I-01** | Toda `obra` tem pelo menos uma `fonte` | `SELECT o.codigo FROM obra o LEFT JOIN fonte f ON f.obra_codigo=o.codigo WHERE f.fonte_id IS NULL;` |
| **I-02** | Toda `fonte` aponta para `obra` existente (FK) | `PRAGMA foreign_key_check;` → vazio |
| **I-03** | **Verbatim imutável**: nenhum `UPDATE` em `citacao.texto_verbatim`/`sha256_trecho` | `SELECT * FROM auditoria WHERE tabela='citacao' AND campo IN ('texto_verbatim','sha256_trecho') AND operacao='UPDATE';` |
| **I-04** | Hash do trecho corresponde ao texto | `SELECT citacao_id FROM citacao WHERE sha256_trecho <> lower(hex(sha256(texto_verbatim)));` *(via UDF `sha256`)* |
| **I-05** | Toda `citacao` referencia `fonte` existente | `PRAGMA foreign_key_check;` → vazio |
| **I-06** | Localizador completo: áudio com `t_ini` exige `t_fim`; texto com `chars_ini` exige `chars_fim` | `SELECT citacao_id FROM citacao WHERE (t_ini IS NOT NULL AND t_fim IS NULL) OR (chars_ini IS NOT NULL AND chars_fim IS NULL);` |
| **I-07** | Nenhuma `relacao` sem despacho (exceto `NAVEGACAO_AMPLA` legado) | `SELECT relacao_id FROM relacao WHERE despacho_id IS NULL AND origem <> 'NAVEGACAO_AMPLA';` |
| **I-08** | Nenhuma `relacao` consigo mesma | `CHECK (a <> b)` |
| **I-09** | Tipos de relação pertencem ao vocabulário controlado (23 da matriz T2) | `SELECT DISTINCT tipo FROM relacao WHERE origem='TABELA_T2' AND tipo NOT IN (SELECT DISTINCT relacao_controlada FROM matriz_t2) AND relacao_controlada <> '';` *(tabela `matriz_t2` criada na Fase 2)* |
| **I-10** | **Quarentena**: nenhuma aresta nasce de tradição correlacional externa | `SELECT r.relacao_id FROM relacao r JOIN candidato c ON c.termo_codigo=r.a JOIN citacao x ON x.citacao_id=c.citacao_id WHERE x.regime_epistemico='CORRELACAO_EXTERNA' AND r.origem='GRAFO_CURATORIAL';` |
| **I-11** | `termo.hold = 1` ⇒ `status <> 'verificado'` | `SELECT codigo FROM termo WHERE hold=1 AND status='verificado';` |
| **I-12** | `ficha_projetada = 1` ⇒ existe `projecao` com `paridade = 1` | `SELECT t.codigo FROM termo t LEFT JOIN projecao p ON p.termo_codigo=t.codigo AND p.paridade=1 WHERE t.ficha_projetada=1 AND p.projecao_id IS NULL;` |
| **I-13** | Paridade de projeção: `sha256_gerado = sha256_legado` | `SELECT caminho FROM projecao WHERE paridade=1 AND sha256_gerado <> sha256_legado;` |
| **I-14** | Decisão de `candidato` exige despacho e fundamento | `SELECT evidencia_id FROM candidato WHERE decisao <> 'PENDENTE' AND (despacho_id IS NULL OR fundamento IS NULL OR fundamento='');` |
| **I-15** | Lote não abre ciclo sem despacho `AUTORIZADO` | `SELECT lote_id FROM candidato WHERE decisao='AUTORIZAR_COTEJO_AMPLIADO' AND despacho_id NOT IN (SELECT despacho_id FROM despacho WHERE estado='AUTORIZADO');` |
| **I-16** | Números oficiais batem com o cadastro legado | `SELECT * FROM v_numeros_oficiais;` → `946 / 826 / 1887 / 104` |
| **I-17** | `auditoria` é append-only | `SELECT * FROM auditoria WHERE operacao IN ('INSERT','UPDATE','DELETE') AND operacao <> 'DESPACHO' AND campo IS NULL;` — complementado por trigger `BEFORE UPDATE/DELETE ON auditoria BEGIN SELECT RAISE(ABORT,'auditoria imutável'); END;` |
| **I-18** | Nenhum `sha256` de fonte vazio ou curto | `CHECK (length(sha256)=64)` |

**Portão de execução:** `PRAGMA foreign_key_check` + os 18 invariantes devem retornar vazios antes de qualquer publicação de leva. O `test_suite.py` atual (T1–T17) permanece vigente para o legado até a Fase 5; a falha T14 é declarada **dívida conhecida e não-bloqueante** para o piloto (o novo pipeline não a herda, pois não parseia Markdown).

---

## 5. Projeção Markdown (determinística)

### 5.1 Template

A função `projetar_ficha(termo_codigo, versao_template)` é **pura**: para o mesmo estado do R2 e a mesma versão de template, produz sempre os mesmos bytes.

```
+++
codigo = "<codigo>"
nome = "<nome>"
categoria = "<categoria>"
subcategoria = "<subcategoria>"
status = "<status>"
fontes = [<siglas de obra ligadas por citacao>]
via = "<via>"
confianca_fonte = "<confianca_fonte>"
atualizado = "<ISO>"
+++
# <nome> — <codigo>

## 1. Gênese e Definição
### Definição Sintética
<definicao>
### Termos Relacionados
| Termo | Código | Relação | Direção | Notas |
|---|---|---|---|---|
<linhas de v_tabela_relacoes>
... G2/G3/G4/G5/G6 ...
```

Regras fixas (herdadas da Onda 2 e validadas pelo Curador):

1. `### Termos Relacionados` **sempre** no topo de `## 1`, logo após a definição.
2. Células vazias → `-`. Sufixo `[Fonte: SIGLA]` ao final de balas sem tag inline.
3. H3 nunca contém sigla/data; apenas títulos semânticos.
4. UTF-8 sem BOM, LF, estado de newline final preservado por ficha (7 arquivos sem newline).
5. Ordem das linhas de relação = `ORDER BY codigo_destino, tipo, direcao`.

### 5.2 Projeção para R3

O índice vetorial é gerado **somente** de `citacao` com `regime_epistemico IN ('CANONICO_RC','LEITURA_FENOMENOLOGICA')`, ponderado por `gaveta_padrao` e `confianca_transcricao`. `CORRELACAO_EXTERNA` e `HIPOTESE` são indexados em coleção separada, **nunca** misturados — é a quarentena por construção.

Cada chunk do índice carrega: `citacao_id`, `termo_codigo`, `fonte_id`, `localizador`, `sha256_trecho`, `gaveta`, `regime_epistemico`. Toda resposta do LLM devolve essa lista.

---

## 6. Roteiro do piloto — lote de áudios de outubro

**Princípio:** nenhuma das 826 fichas atuais é tocada até a Fase 5. O novo store nasce paralelo.

| Fase | Nome | Escopo | Critério de aceite (portão) |
|---|---|---|---|
| **F0** | **Schema sem dados** | Extrair o DDL deste ADR para `ferramentas/adr001_schema.sql`; criar `kb/base.sqlite` vazio; rodar `PRAGMA foreign_key_check` e os 18 invariantes sobre o vazio | DDL executa sem erro; **9 tabelas + 3 views + 19 índices**; 0 violações; **0 arquivos em `termos/` alterados** |
| **F1** | **Ingestão R1 dos 310 brutos** | Popular `obra` (tipo `EIXO_STT`/`VIDEO`) e `fonte` com os 310 brutos de `fontes/stt-lote-2026-10/`: `sha256`, `bytes`, `duracao`, `id_youtube`, `data_transcricao`, `motor_neural`, `confianca_transcricao='BAIXA'` (STT por definição) | 310 fontes com hash conferido contra `fontes/manifestos/`; I-01, I-02, I-18 verdes; `fontes/` intocável |
| **F2** | **Endereçamento e incerteza** | Importar `mapa-linhas.jsonl` (26.389 linhas, `unidade U00029`, `sha256_texto_linha`) para `citacao`; adicionar `t_ini`/`t_fim` a partir dos áudios inéditos; marcar `confianca_transcricao` por faixa | 26.389+ citações; todo `Uxxxxx` único por fonte; I-04, I-06 verdes; nenhum `texto_verbatim` difere do bruto (paridade byte a byte) |
| **F3** | **Triagem dos 24 lotes no store** | Importar os 24 `candidatos-cotejo.json` (600 candidatos, 25/lote) e os `DESPACHO-CURATORIAL-TEMPLATE.json` para `candidato`/`despacho`. `v_triagem_lotes` substitui a leitura de arquivos | `v_triagem_lotes` = 24 linhas, 25 candidatos cada, 600 `PENDENTE`; I-14, I-15 verdes; **nenhum ciclo aberto** |
| **F4** | **Despacho curatorial** | Curador decide por lote via `despacho` (estado `AUTORIZADO`/`RECUSADO`), com `fundamento` e `artefato`. Logs em `auditoria` | I-07, I-10, I-11, I-15 verdes; 0 arestas sem despacho; 0 contaminação de quarentena |
| **F5** | **Projeção reversa e paridade** | Gerar `.md` a partir do banco para um **conjunto-piloto de 10 fichas**, comparar byte a byte com as fichas atuais | **Paridade 100%** (`projecao.paridade=1`, I-12/I-13 verdes); nenhuma divergência de conteúdo; Curador homologa o template `onda2-v1` |
| **F6** | **Strangler Fig** | Ampliar a projeção para as 826 fichas; `dados_termos.py` rebaixado a view; `canonico.json` e os 6 espelhos passam a ser gerados do banco | `v_numeros_oficiais` = 946/826/1887/104; T14 extinto; 0 perdas; legado servido por adaptador |

**Fora de escopo do piloto:** mover `fontes/`, reescrever as 826 fichas à mão, substituir o `motor.py`, treinar a IA Local, e qualquer re-odição de áudio sem despacho (regra M2: STT não conta como prova).

### 6.1 Dados concretos de entrada (levantados nesta redação)

| Fonte | Volume | Campos aproveitados |
|---|---|---|
| `fontes/stt-lote-2026-10/*.md` | 310 brutos | `titulo`, `data_publicacao_original`, `id_youtube`, `link_original`, `duracao`, `data_transcricao`, `motor_neural`, `arquivo_fonte (.opus)` |
| `ingestao_stt_lote_2026-10/registro-mestre.jsonl` | 309 | `ingresso_id`, `sha256_derivado`, `bytes_derivado`, `origem_declarada`, `normalizacao`, `estado`, `metadados` |
| `ingestao_stt_lote_2026-10/mapa-linhas.jsonl` | 26.389 | `unidade`, `linha`, `caracteres`, `sha256_texto_linha`, `ingresso_id` |
| `normalizados_stt_lote_2026-10/` | 309 derivados + manifestos | proveniência das 1.306 substituições auditadas |
| `triagem_stt_lote_2026-10/STT26-01…24/` | 24 × 25 candidatos | `evidencia_id`, `ingresso_id`, `unidade`, `grafia_encontrada`, `excerto`, `sinais_exatos` |
| `fontes/stt-lote-2026-10/` + áudios inéditos | a receber | **`t_ini`/`t_fim`**, `confianca_transcricao` |
| `admin/logs/T2-MAPEAMENTO-RELACOES.csv` | 998 linhas `APROVADO` | vocabulário controlado das 23 relações (I-09) |
| `chancela/HOLD.csv` | 40 códigos | `termo.hold` (I-11) |

---

## 7. Mapeamento legado → novo

| Legado (hoje) | Novo (ADR-001) | Regime |
|---|---|---|
| `fontes/**/original.pdf\|txt`, brutos STT | `fonte` + `citacao.texto_verbatim` | R1 |
| `ferramentas/dados_termos.py` | `termo` + `relacao` | R2 |
| `base/canonico.json` | **extinto** — `v_numeros_oficiais` | projeção |
| `base/biblio.json` (104 obras) | `obra` | R2 |
| `termos/RC-*.md` | `projecao` (view renderizada) | projeção |
| `chancela/*.csv` + `HOLD.csv` | `despacho` + `termo.hold` + `auditoria` | R2 |
| `rag/perolas/PER-*.md` | `citacao` (recorte) + `candidato` | R1→R2 |
| `triagem_stt_lote_2026-10/*` | `candidato` + `despacho` + `v_triagem_lotes` | R2 |
| `README.md`, `indice-mestre.md`, `.xlsx`, `.docx`, `STATE-MIRROR.md` | funções puras sobre o store; **não versionados** | projeção |
| `POLITICA-QUARENTENA-*.md` | `citacao.regime_epistemico` + I-10 | R2 |

---

## 8. Riscos e mitigações

| Risco | Severidade | Mitigação |
|---|---|---|
| Projeção reversa não alcançar 100% (7 fichas sem newline, 143 linhas extras fora de tabela, `[Fonte: X]`) | **Alta** | F5 com piloto de 10 fichas antes de qualquer ampliação; `projecao` registra paridade por arquivo; template versionado |
| Ingestão de áudio com timestamp impreciso | Média | `confianca_transcricao` obrigatório; re-odição somente com despacho (regra M2) |
| Duas verdades convivendo durante a transição | Média | Adaptador único de leitura; I-16 compara números a cada build; janela de transição declarada e curta |
| Schema engessar o domínio antes de conhecê-lo | Média | `ALTER TABLE` é barato em SQLite; `nota`/`observacao` livres; `regime_epistemico` extensível por migração |
| Perda da cultura de leitura das fichas | **Alta** | Markdown mantido como interface de primeira classe (§2.2); nenhuma mudança visual em relação à Onda 2 |
| Banco binário no git (o erro que os espelhos binários já causaram) | Média | `kb/base.sqlite` **não é versionado**; versiona-se `ferramentas/adr001_schema.sql` + dumps `.sql` determinísticos quando necessário |

---

## 9. Consequências

**Positivas:** fim da defasagem de espelhos (I-16); T14 extinto; proveniência consultável em SQL; quarentena construtiva; decisões curatoriais auditáveis sem arqueologia em `admin/logs/`; áudio com timestamp e incerteza como cidadãos de primeira classe; RAG com lastro verificável em cada resposta.

**Custos aceitos:** um store novo a operar; um gerador de projeção a escrever e homologar; convivência temporária de dois caminhos de leitura; necessidade de revalidação do `test_suite.py` ao fim da F6.

**Decisões explicitamente adiadas:** Event Sourcing com replay (§2.3); migração física de `fontes/`/`kb/` (Fase 0 de 23/10/2026 permanece válida); substituição do `motor.py`; treinamento da IA Local.

---

## 10. Aceite

ADR-001 **ACEITO** por despacho curatorial de 27/10/2026. Sua publicação não altera nenhum dado: é um documento de arquitetura. A execução começa pela **F0 (schema sem dados)**, em rodada própria, mediante novo despacho.

---

*Fim do ADR-001 · Base Terminológica RC · 27/10/2026.*
