# PLANO — Corpus de Treinamento da IA Local (Especialista em RC)

> **Documento-mestre do processo futuro.** Registra a decisão de pausa na geração de
> apostilas-como-corpus e o redirecionamento para o garimpo estruturado de termos e
> relações — o caminho que alimenta a Base e, dela, o corpus de treinamento da IA Local.
>
> **Status:** VIGENTE (2026-08-31) · **Origem:** decisão do Curador, sessão 2026-08-31.
> **Autor:** Arena.ai Agent Mode (MiniMax-M3).

---

## 1 · A decisão do Curador (contexto e motivação)

O Curador interrompeu o uso das apostilas v3.1-MP como produto de treinamento de IA e
redirecionou o esforço:

1. **Pausa na geração de apostilas** como corpus de treinamento — as apostilas seguem
   existindo como **arquivo histórico da fala** (leitura humana), mas **não se investe
   mais nelas** para treinar a IA.
2. **Foco novo: garimpar termos e relacionamentos.** Há ~150 palestras ainda não
   processadas. O objetivo passa a ser extrair delas **termos novos** (pérolas) e
   **relações tipadas** que enriqueçam a Base Terminológica.
3. **Motivação de fundo:** perpetuar a fala do Ellam (cuja passagem, segundo ele, está
   próxima). Já existe grande volume de conteúdo registrado; o investimento agora é em
   **qualidade da KB** (Knowledge Base) e em seu aprimoramento contínuo.
4. **Destino final:** quando a Base estiver consagrada (termos + relações estabilizadas),
   abre-se um **processo exclusivo** para gerar o conteúdo de treinamento da IA Local —
   derivado da Base, não das apostilas.
5. **Pausa técnica (conclusão da sessão):** congelar **qualquer criação de scripts,
   esqueletos de código (como o `gerar_corpus.py`) ou formatação de apostilas** — tudo
   isso fica para o **Agente exclusivo** que o Curador criará no futuro. O foco atual é
   **exclusivamente o garimpo bruto de termos e a expansão da malha da KB**; o repositório
   está **em standby**, aguardando o envio do próximo TXT.
6. **Sub-decisão das relações (anotada, não resolvida agora):** a questão dos tipos de
   relação antigos × novos fica **apenas registrada** no plano (§6) — será tratada pelo
   Agente exclusivo, não nesta fase.

> **Nota do agente:** a decisão é tecnicamente correta. As apostilas e o corpus de
> treinamento são **dois produtos diferentes** que vinham sendo forçados a conviver num
> artefato só (ver §2). Separar os dois destrava o garimpo sem o custo do verbatim
> integral em prosa.

---

## 2 · Por que a separação é necessária (diagnóstico)

| Objetivo | O que precisa | Artefato ideal | Estado |
|---|---|---|---|
| **Arquivo histórico** (a fala do Ellam) | verbatim, prosa, quarentenas | apostila v3.1-MP | **81 concluídas** — pausado como corpus, segue como arquivo |
| **Corpus de treinamento** (IA Local) | grafo estruturado, grafias canônicas, relações tipadas, zero ruído | **a Base Terminológica** | já ~90% pronto (ver §3) |

O problema que os ciclos recentes expuseram (erros de termo, portão de verbatim, retrabalho,
ambiguidades dependentes de contexto) é o sintoma de **forçar a apostila a ser corpus**:

- a apostila mistura **prosa editorial + verbatim bruto** (erros de STT em palavras comuns,
  não só em nomes próprios);
- o verbatim tem **ambiguidades contextuais** sem solução determinística (`Deus` = Criador ×
  Zeus; `aia` = Aya e/ou Aye; `Pel` = fragmento de "pele" × Pirra; `birra` = teimosia × Pirra);
- gerar à mão produz **retrabalho a cada ciclo** (o caso P2019-08-25: normalização pós-hoc).

A Base terminológica **não tem nenhum desses defeitos**: é estruturada, normalizada, com
relações explícitas e grafias canônicas já mapeadas. É dela que o corpus deve nascer.

---

## 3 · Inventário do que já existe (aproveitável para o corpus)

| Insumo | Onde | Conteúdo | Valor para o corpus |
|---|---|---|---|
| **Cadastro autoritativo** | `ferramentas/dados_termos.py` | **777 termos** × 8 campos (código, nome, categoria, subcategoria, status, fontes, relacionados, ficha) + **1.856 relações** + **102 obras** | grafo de conhecimento já normalizado — o coração do corpus |
| **Fichas RC** | `termos/RC-XXX-*.md` (526 arquivos) | definição sintética, etimologia, citações-chave, termos relacionados, observações | contexto rico por termo |
| **Glossário canônico** | `GLOSSARIO-CANONICO-2026-08-31.md` | 524 fichas + 80 pastas + **regras de grafia** (canônica × rejeitada) | mapa de normalização pronto |
| **Convenções editoriais** | `convencoes-editoriais-rc.md` | regras de edição, hierarquia de referências, §13 (normalização) | governança |
| **Vocabulário controlado** | `02-vocabulario-controlado.md` | 8 categorias principais × subcategorias | taxonomia do corpus |
| **Esteira leve** | `admin/logs/DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md` + `ferramentas/motor.py` (selftest 9/9) | o processo de **garimpo** já pronto: pérolas (status candidata → aprovada), livro-razão de âncoras, arestas tipadas | **o instrumento do garimpo** |
| **Ciclos leves já rodados** | `ciclos/P2023-12-03/`, `ciclos/P2023-12-17/` | provas de conceito do rito leve (P2023-12-03 = ciclo zero verde) | referência de formato |

**Conclusão:** o insumo de treinamento já está ~90% pronto e normalizado. O que faltou foi
parar de tentar fazer as apostilas serem esse insumo.

---

## 4 · O pipeline de garimpo (o caminho para alimentar a KB)

Este é o processo **atual** para as ~150 palestras restantes — já operacional, não precisa
ser inventado:

1. **Ingresso** — `motor.py novo <arquivo>`: copia o TXT byte a byte, sela com SHA-256,
   recusa sobrescrever fonte já selada, escreve `ciclo.toml` + `pacote` vazios (ausência
   visível, não zero disfarçado).
2. **Leitura** — `fatias` (leitura integral com concatenação asserida) e `busca "<âncora>"`
   (período verbatim com `U####` e faixa de caracteres; **nenhuma aspa digitada à mão**).
3. **Garimpo** — edição do `ciclo.toml`: pérolas (termos candidatos novos) com âncora,
   spans aceitos/recusados (livro-razão, com motivo), relações propostas.
4. **Portões** — `portoes` / `tudo`: A (integridade da fonte), B (verbatim byte a byte),
   C (paridade ficha ↔ pacote + veto de trânsito), D (DELTA contra o commit-base).
5. **Aprovação** — o **Curador** carimba cada pérola (`candidata` → `aprovada`); o RAG
   exporta **só `aprovada`**. O motor não se auto-carimba.
6. **Materialização** — só quando uma pérola aprovada o exigir (`RC-778+` é consequência,
   não reserva). Relações entram **tipadas** (`fundamenta`/`contradiz`/`antecipa`/
   `exemplifica`), com evidência (span + endereço) e selo datado. Aresta proibida entre
   termos sem arquivo.

**Regra de custo já provada:** o ciclo zero leve escreveu 140.346 B contra 1.133.595 B do
rito pesado (**8,1× menos**), sem perder nenhuma das 147 citações.

---

## 5 · O pipeline de treinamento futuro (a abrir quando a Base estiver consagrada)

Este é o processo **exclusivo** que o Curador descreveu — ainda **não iniciado** e
**atribuído ao Agente exclusivo futuro** (nada aqui será criado nesta fase — ver §1,
item 5). Fica registrado aqui para a próxima fase:

1. **Congelar a Base** — termos + relações + fichas auditadas (consagração).
2. **Exportar o corpus** — script determinístico (`ferramentas/gerar_corpus.py`, a criar
   pelo Agente exclusivo) que converte `dados_termos.py` + fichas + glossário em
   `corpus.jsonl` versionável:
   - cada termo = 1 registro com código, nome canônico, categoria/subcategoria, status,
     definição, fontes, relações tipadas, grafias rejeitadas;
   - relações expandidas em arestas `(termo_A, tipo, termo_B)` com evidência;
   - separação explícita de **fato** (científico) × **leitura do autor** × **quarentena**,
     para o corpus não ensinar leitura como doutrina.
3. **Validar o corpus** — dedupe, consistência de códigos (imutáveis), grafias canônicas.
4. **Treinar** — fine-tuning da IA Local com o corpus (estratégia de chunking e formato
   de prompt a definir no processo exclusivo).

---

## 6 · Decisões de formato FECHADAS (2026-08-31)

Fechadas pelo Curador nesta sessão. São as cinco do §6 original + o default técnico de
chunking, validado em bloco:

| # | Decisão | Fechada como | Nota |
|---|---|---|---|
| 1 | **Estratégia de treino** | **Híbrido** — RAG como fonte de verdade + fine-tuning leve para o estilo curatorial | respostas ancoradas + sotaque de curadoria |
| 2 | **Formato do corpus-base** | **JSONL** — 1 registro por termo + 1 por relação + 1 por par de grafia | fonte de verdade neutra; transformável em Q&A/RAG/markdown por script |
| 3 | **Quarentenas no corpus** | **Rotuladas** com campo explícito, **nunca como doutrina** | o termo entra, marcado como leitura/alegação |
| 4 | **Fato × leitura do autor** | **Campo obrigatório** `epistemologia` por asserção/relação | impede a IA de ensinar cosmologia do autor como ciência |
| 5 | **Camada de grafia STT→canônico** | **Pares supervisionados** da SEÇÃO 1 do `GLOSSARIO-CANONICO` | determinístico e auditável |
| 6 | **Chunking** (default técnico) | **Por unidade lógica** (seção da ficha), com metadados — nunca por caractere fixo | valida junto ao fechamento do processo exclusivo |

> **Sub-decisão emergente (anotada, não bloqueante):** as fichas antigas usam **tipos de
> relação livres** ("é-família-de", "é-paralelo-com", "é-vigiada-por"…), enquanto a esteira
> leve canoniza **4 tipos** (`fundamenta`/`contradiz`/`antecipa`/`exemplifica`). O corpus
> precisa de um **vocabulário controlado de relações**: as 4 da esteira são o núcleo; os
> tipos livres serão **mapeados/normalizados** (ou mantidos como `relaciona` genérico) no
> momento da exportação. Registrar como item do processo exclusivo, não do garimpo.

---

## 7 · Schema do corpus JSONL (especificação v1.0)

O `corpus.jsonl` terá **4 tipos de registro** (um objeto JSON por linha). Campos marcados
`*` são obrigatórios. Este schema é o contrato que o `gerar_corpus.py` (a criar no processo
exclusivo) deverá cumprir.

### 7.1 — Registro `meta` (cabeçalho, 1ª linha)

```json
{
  "tipo": "meta",
  "schema_versao": "1.0",
  "gerado_em": "AAAA-MM-DD",
  "fontes": ["ferramentas/dados_termos.py", "termos/RC-*.md", "GLOSSARIO-CANONICO-*.md"],
  "contadores": {"termos": 777, "relacoes": 1856, "fichas": 526, "grafias": "N"}
}
```

### 7.2 — Registro `termo` (1 por termo)

```json
{
  "tipo": "termo",
  "codigo": "RC-009",
  "nome": "Sophia (Cristo Cósmico)",
  "categoria": "Seres & Entidades",
  "subcategoria": "1.8 Consciências coletivas / Logos",
  "status": "verificado",
  "ficha": true,
  "definicao": "…(Definição Sintética)…",
  "etimologia": "…(Etimologia / Grafias)…",
  "fontes": ["B031", "P2023-12-17"],
  "grafias": {"canonica": "Sophia", "rejeitadas": ["Sofia"]},
  "quarentena": [],
  "epistemologia": "leitura_do_autor",
  "citacoes_chave": ["…"],
  "observacoes": ["…"]
}
```

### 7.3 — Registro `relacao` (1 por aresta)

```json
{
  "tipo": "relacao",
  "origem": "RC-009",
  "relacao": "fundamenta",
  "destino": "RC-072",
  "evidencia": {"fonte": "P2023-12-17", "unidade": "U0002", "faixa": "1234-1456"},
  "selo": "P2023-12-17",
  "epistemologia": "leitura_do_autor"
}
```

### 7.4 — Registro `grafia` (1 por par bruto→canônico; decisão §6-5)

```json
{
  "tipo": "grafia",
  "bruto": "Sofia",
  "canonico": "Sophia",
  "codigo": "RC-009",
  "origem": "GLOSSARIO-CANONICO §1"
}
```

### 7.5 — Enums (vocabulários controlados do corpus)

| Campo | Valores |
|---|---|
| `status` | `candidato` · `provisório` · `em análise` · `verificado` |
| `epistemologia` | `fato` · `leitura_do_autor` · `alegacao` · `quarentena` |
| `quarentena` | `teologica` · `ufologica` · `clinica` · `politica` · `genero` · `biomediunica` · `institucional` · `biografica` |
| `relacao` (núcleo) | `fundamenta` · `contradiz` · `antecipa` · `exemplifica` (+ tipos livres das fichas, a normalizar — ver §6) |

### 7.6 — Mapa de origem dos campos (o que sai de onde)

| Campo do corpus | Vem de |
|---|---|
| `codigo`, `nome`, `categoria`, `subcategoria`, `status`, `ficha`, `fontes` | `dados_termos.py` |
| `definicao`, `etimologia`, `citacoes_chave`, `observacoes`, `relacionados` | `termos/RC-*.md` |
| `grafias` (canônica × rejeitadas) | `GLOSSARIO-CANONICO` §1 |
| `relacao`, `evidencia`, `selo`, `epistemologia` | malha de relações + esteira leve |
| `quarentena` | rótulos das fichas/apostilas (campo novo a preencher na exportação) |

---

## 8 · Lições aprendidas (para não repetir)

1. **Verbatim e canônico são camadas diferentes.** O verbatim bruto mora em
   `original.txt` + `uploads_recepcao/`; o canônico mora na Base. Misturar os dois num
   arquivo de treinamento é a raiz dos erros de termo.
2. **Substituição cega corrompe.** Regras de grafia são **contextuais**: `Deus`→Zeus só
   quando é o deus grego (23 ocorrências no 1º lote eram todas o Criador); `Pel`/`birra`
   casam fragmentos de palavras comuns; `aia` não distingue Aya de Aye. Toda regra de
   grafia precisa de âncora ou contexto, nunca de replace global.
3. **O portão de verbatim é o corretivo da memória.** "Nenhuma aspa digitada à mão" e
   "âncora que bate 0 ou >1 vez ABORTA" impedem o agente de inventar citação — mantê-los
   é inegociável em qualquer rito.
4. **Dois produtos, dois ritos.** Apostila (arquivo, pesado) e garimpo (KB, leve) não
   deveriam dividir o mesmo ciclo. A esteira leve já resolve isso.
5. **O Curador carimba, o motor não se auto-carimba.** Aprovação de pérola e de relação
   é prerrogativa do Curador; o exportador do RAG obedece ao `status`.

---

## 9 · Estado atual (fechamento da sessão 2026-08-31)

| Métrica | Valor |
|---|---|
| Termos no cadastro | **777** |
| Relações | **1.856** |
| Obras | **102** |
| Fichas físicas (`termos/`) | **526** |
| Apostilas concluídas | **81** |
| Ciclos leves rodados | 2 (P2023-12-03, P2023-12-17) |
| Motor (`selftest`) | **9/9** |
| TXT na fila (`uploads_recepcao/`) | 1 (P2019-08-25, já processada) |
| Palestras restantes (estimativa) | **~150** |

**Commit-base do redirecionamento:** `be00a1a` (norma de normalização + ciclo P2019-08-25
fechado). A partir daqui, o foco migra para o **garimpo via esteira leve**.

---

## 10 · Próximos passos

1. ✅ **Registrar a decisão** no `admin/logs/CONTINUIDADE.md` e no `prompts/PROMPT-PROXIMA-SESSAO.md` (feito).
2. ✅ **Fechar as decisões de formato** (§6) e **especificar o schema** (§7) — feito nesta
   sessão; o caminho do corpus está mapeado de ponta a ponta.
3. **Standby:** aguardar o Curador enviar o próximo TXT (`uploads_recepcao/`). Foco
   exclusivo no **garimpo bruto de termos** e na **expansão da malha da KB** via esteira
   leve — sem criar scripts, esqueletos ou apostilas (pausa técnica, §1 item 5).
4. **Aprovar pérolas candidatas** pendentes (25 do ciclo zero P2023-12-03 aguardam o
   carimbo do Curador).
5. **Quando a Base estiver consagrada**, o **Agente exclusivo** abre o processo de corpus
   (§5): criar `gerar_corpus.py` segundo o schema §7, normalizar o vocabulário de relações
   (§6), validar e exportar `corpus.jsonl`.

---

## 11 · Referências

- `admin/logs/DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md` — norma da esteira leve (rito de garimpo).
- `ferramentas/motor.py` — Motor Único (selftest 9/9).
- `ferramentas/dados_termos.py` — cadastro autoritativo (777/1.856/102).
- `GLOSSARIO-CANONICO-2026-08-31.md` — grafias canônicas × rejeitadas.
- `convencoes-editoriais-rc.md` — convenções (incl. §13, normalização terminológica).
- `ciclos/P2023-12-03/RELATORIO-CICLO-LEVE.md` — prova de conceito do rito leve.
- `../../diagnostico/DIAGNOSTICO-DO-PROCESSO-2026-08-29.md` — parecer que motivou a reforma.
