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
| **Esteira leve** | `DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md` + `ferramentas/motor.py` (selftest 9/9) | o processo de **garimpo** já pronto: pérolas (status candidata → aprovada), livro-razão de âncoras, arestas tipadas | **o instrumento do garimpo** |
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

Este é o processo **exclusivo** que o Curador descreveu — ainda **não iniciado**. Fica
registrado aqui para a próxima fase:

1. **Congelar a Base** — termos + relações + fichas auditadas (consagração).
2. **Exportar o corpus** — script determinístico (`ferramentas/gerar_corpus.py`, a criar)
   que converte `dados_termos.py` + fichas + glossário em `corpus.jsonl` versionável:
   - cada termo = 1 registro com código, nome canônico, categoria/subcategoria, status,
     definição, fontes, relações tipadas, grafias rejeitadas;
   - relações expandidas em arestas `(termo_A, tipo, termo_B)` com evidência;
   - separação explícita de **fato** (científico) × **leitura do autor** × **quarentena**,
     para o corpus não ensinar leitura como doutrina.
3. **Validar o corpus** — dedupe, consistência de códigos (imutáveis), grafias canônicas.
4. **Treinar** — fine-tuning da IA Local com o corpus (estratégia de chunking e formato
   de prompt a definir no processo exclusivo).

---

## 6 · Decisões de formato pendentes (para o processo exclusivo futuro)

Estas decisões **não bloqueiam o garimpo** (que já roda), mas precisam ser fechadas antes
de abrir o treinamento:

- [ ] **Formato do corpus:** JSONL (um registro por termo + um por aresta) vs. pares
      pergunta-resposta vs. markdown estruturado. Recomendação inicial: JSONL.
- [ ] **Estratégia de chunking:** como fatiar fichas longas para a janela de contexto do
      modelo local.
- [ ] **Tratamento das quarentenas no corpus:** os termos sob quarentena (teológica,
      ufológica, clínica, política, gênero) entram **rotulados**, nunca como doutrina.
- [ ] **Separar fato × leitura:** campo explícito de "status epistemológico" (a Base já
      tem insumo para isso nas apostilas, via `@autoridade_leitura`).
- [ ] **Camada de grafia:** como ensinar o modelo a corrigir STT → canônico (o
      `GLOSSARIO-CANONICO` SEÇÃO 1 é o ponto de partida).

---

## 7 · Lições aprendidas (para não repetir)

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

## 8 · Estado atual (fechamento da sessão 2026-08-31)

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

## 9 · Próximos passos

1. **Registrar a decisão** no `CONTINUIDADE.md` e no `PROMPT-PROXIMA-SESSAO.md` (feito
   nesta sessão) para a próxima sessão abrir já no foco certo.
2. **Retomar o garimpo** assim que o Curador nomear a próxima palestra (fila em
   `uploads_recepcao/`; os ~150 TXT restantes ainda precisam ser enviados/recuperados).
3. **Aprovar pérolas candidatas** pendentes (25 do ciclo zero P2023-12-03 aguardam o
   carimbo do Curador).
4. **Quando a Base estiver consagrada**, abrir o processo exclusivo de corpus (§5–§6).

---

## 10 · Referências

- `DESPACHO-DA-ESTEIRA-LEVE-2026-08-29.md` — norma da esteira leve (rito de garimpo).
- `ferramentas/motor.py` — Motor Único (selftest 9/9).
- `ferramentas/dados_termos.py` — cadastro autoritativo (777/1.856/102).
- `GLOSSARIO-CANONICO-2026-08-31.md` — grafias canônicas × rejeitadas.
- `convencoes-editoriais-rc.md` — convenções (incl. §13, normalização terminológica).
- `ciclos/P2023-12-03/RELATORIO-CICLO-LEVE.md` — prova de conceito do rito leve.
- `DIAGNOSTICO-DO-PROCESSO-2026-08-29.md` — parecer que motivou a reforma.
