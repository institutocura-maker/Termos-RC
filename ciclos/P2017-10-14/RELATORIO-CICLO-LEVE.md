# RELATÓRIO DO CICLO LEVE — `P2017-10-14` · Da Base Atlan ao Colégio Druídico

**Data de execução:** 31/08/2026 · **Agente:** Arena (ramo `arena/01a05591-termos-rc`)
**Instrumento:** `ferramentas/motor.py` — Motor Único da esteira leve
**Configuração do ciclo:** `ciclos/P2017-10-14/ciclo.toml`
**Fonte:** `uploads_recepcao/2017-10-14 Da Base Atlan ao Colégio Druídico.txt` → `original.txt` (134.307 B · SHA-256 `fb7619e419…af5694d` · 113 unidades com fala)
**Baseline do portão D:** `14fb99e` (commit que adiciona o TXT)

> 1ª palestra da série que complementa a **Trilogia Terra Atlantis**; par da palestra de
> 16/10/2017. Tema: o percurso da base Atlan (Alt´Lam) até o Colégio Druídico — a recriação,
> na Terra, da escola que o Codificador fundou em Capela há ~4 milhões de anos. Fonte STT
> bruta, longa (~22.957 palavras), com forte distorção de áudio nos nomes próprios.

---

## 1 · Veredicto — medido

| Grandeza | Valor |
|---|---|
| Citações verificadas byte a byte | **17 / 17** (portão B) |
| Fichas com `## Ampliação — P2017-10-14` | **9** (portão C em paridade) |
| Códigos tocados sem arquivo (fila) | **8** |
| Termos novos | **2** (RC-841 · RC-842) |
| Relações novas | **0** |
| Obras novas | **0** |
| Materializações | **0** (nenhuma ordem do Curador neste ciclo) |
| Vínculos (códigos carregando a sigla) | **17** |
| Portões | **A ✓ · B ✓ · C ✓ · D ✓** |

**Delta do portão D:** `arquivos 0 · ficha_true 0 · termos +2 · relacoes 0 · vinculos +17`
— exatamente o declarado no `.toml`. Base: **842 termos · 1.856 relações**.

---

## 2 · O que este ciclo entregou

1. **Catálogo sistemático** — entrada selada por SHA-256, 0 caracteres de controle,
   endereço de span em `U####` + faixa de caracteres (livro-razão
   `ancorario_P2017-10-14.json`: 17 spans verificados, 0 recusados).
2. **Consistência terminológica** — 9 fichas ampliadas com a seção do ciclo; 8 códigos
   vinculados e deixados em fila declarada (sem arquivo); 2 termos novos no cadastro,
   todos `status: candidato` (`ficha=False`), aguardando carimbo do Curador.
3. **Caderno de pérolas** — `DOSSIE-RAG_P2017-10-14.md`, 17 pérolas de 17 candidatas,
   nas 4 seções do formato leve, cada aspa recortada do bruto pelo índice de âncoras.
4. **Corpus RAG** — 0 cards (`exportar_candidatas = false`): o portão de consumo é
   `aprovada`, e o carimbo é do Curador.

---

## 3 · A tese do ciclo

O **Colégio Druídico** é a recriação terrena da escola de Capela (RC-403 ↔ RC-092): a 1ª
transferência do conhecimento do Codificador a humanos livres, transmitida pelos povos
celtas/gaélicos até a Grécia (a filosofia de Pitágoras/Tales como herança druídica) e depois
distorcida por Roma e pelo cristianismo. O **ser humano** é o "protótipo que deu certo" — a
união dos dois fornos replicadores (RC-771: a banda sensata dos biodemos + a banda emocional
da animalidade), o que explica os dois hemisférios cerebrais. A **rebelião de Lúcifer**
(RC-002) trouxe o quartel-general à Terra há ~97.000 anos; na base Atlan (RC-017) reencontrou
a família Val (RC-109) e retomou a tese da "realidade doente". A **mitologia grega e
irlandesa** (Caos = Javé · Têmis · Cronos→Zeus · Thuata de Dannan · Milésios) são ecos
distorcidos dessa história biodêmica.

---

## 4 · Garimpo: o que a fonte nomeia e como foi mapeado

### 4.1 — Grafias STT → canônicas (as pérolas já carregam a forma canônica no rótulo)

| STT (bruto) | Canônico | Código |
|---|---|---|
| `colégio do I` / `escola druídica` / `colégio druídico` | Colegiado Druídico | RC-403 |
| `base Atla` / `Atlan` | Alt´Lam / Alt´Lam Gron | RC-017 / RC-018 |
| `três formos replicadores`; `for de Brama`; `o de China`/`virgem chiva`; `forno de Virgo` | Fornos Replicadores (Awayen / Awaylengan / Awaymaion) | RC-771 / RC-836 / RC-837 / RC-499 |
| `quificador` / `cotificador` | Codificador (Quarto Logos / Olm) | RC-092 / RC-252 |
| `família Vol` / `Família V` | Val (Família Val) | RC-109 |
| `processador da família Vol` | Processador Val | RC-089 |
| `Sileno` / `Silênio` | Sileno (Observação de Sileno) | RC-228 |
| `Temis` / `Tenes` | Têmis | RC-305 |
| `toatas de ganã` | Thuata de Dannan | RC-398 |
| `registro cástico` / `fracasso` | Memória Quântica dos Elétrons (registro cármico) | RC-161 |
| `Caos` / `Jahé` | Javé (= Brahma = Caos) | RC-001 / RC-284 |
| `anonques` / `anulax` | Anunnakis | RC-024 |
| `Fox 2` | FOXP2 (inoculado por Enki) | RC-486 |
| `Machupate` | Pashupati (avatar de Shiva) | RC-669 |
| `cronos` | Cronos (titã) — **novo** | RC-841 |
| `milesanos` | Milésios (raça da Irlanda) — **novo** | RC-842 |

### 4.2 — Termos NOVOS criados (por pérola, §4 do dossiê)

- **RC-841 · Cronos (titã)** — a genealogia titânica (Uranos → Cronos/Titãs → Zeus/Olimpianos)
  é explicitamente contada na fonte; Cronos é o elo (pai de Zeus, usurpado por ele) e faltava
  ao lado de Zeus (RC-145), Têmis (RC-305) e Prometeu (RC-301). `SER_DEC`.
- **RC-842 · Milésios (raça da Irlanda)** — a última raça a aportar na Irlanda, que herdou o
  conhecimento druídico e "fundou as primeiras origens do colégio". Pérola longa que amarra
  Milésios → Colégio Druídico → Capela. `SER_HUM`.

### 4.3 — Nomes que NÃO viraram termo (registrados para decisão do Curador)

- **`Shamba`** (U0010) — "dimensão chamada na época WH, que depois passou a ser conhecida
  como Shamba": onde os biodemos mortos ficavam presos; precursora da astralização. **Não
  criado** por ambiguidade de grafia (WH × Shamba × possível Shambhala); fica como candidato
  a novo termo sob a canônica que o Curador fixar.
- **`Família Chamon / Shamon / Chamom`** (U0005/U0008) — uma das famílias biodêmicas; **não
  criado** por não estar claro se é família distinta ou STT de `Shanlung` (RC-491) / `Cromon`
  (RC-444). Aguarda confirmação.
- **`Beltane` ("festival do deus Bel"/"veladão")** (U0167) — festival do fogo dos Thuata de
  Dannan; **não criado** por ser menção breve e sem categoria própria no cadastro.
- **`Midas`** (U0021) — rei, dentro da história de Sileno (RC-228); **não criado** — coberto
  pela pérola de RC-228.
- **`Valel` / `El Bel` / `Bauel`** — a figura biodêmica que anima o autor e nasceu como
  Enoque; **não criado** por flutuação de grafia; o vínculo Valel→Enoque ficou na pérola de
  RC-489.
- **`Uranos`** (U0135) — 1ª geração de deuses; menção breve; **não criado** (poderia ser
  termo-irmão de Cronos, se o Curador quiser).

---

## 5 · Fila aberta (8 códigos tocados sem arquivo de ficha)

`RC-403` (Colegiado Druídico) · `RC-017` (Alt´Lam) · `RC-228` (Sileno) · `RC-305` (Têmis) ·
`RC-398` (Thuata de Dannan) · `RC-109` (Val) · `RC-841` (Cronos) · `RC-842` (Milésios).

Todos carregam a sigla na lista de fontes (vínculo) e têm bloco no pacote; a criação de ficha
é `materializar`, por ordem do Curador.

---

## 6 · Observações e travas

- **Travas aplicadas:** RC-109 (quarentena social — a leitura "elitista" do percentual de
  biodemos e dos "mais habilitados" que levam a tocha da vida, U0149); RC-001 (leitura do
  autor — o tom crítico a Javé e a frase de Sileno).
- **Lacunas fechadas:** RC-403 (Colégio Druídico como 1ª transferência), RC-842 (Milésios
  herdeiros do conhecimento druídico), RC-161 (registro cármico = memória dos elétrons).
- **0 relações novas:** nenhuma aresta tipada com evidência e selo nasceu neste ciclo; a
  malha só cresce por aresta auditável (despacho §3).
- **Teto:** suspenso-com-cadência; 2 cadências consumidas (RC-841, RC-842), cada uma com
  pérola candidata por trás e linha no §4 do dossiê — o carimbo `aprovada` é do Curador,
  na devolutiva.
