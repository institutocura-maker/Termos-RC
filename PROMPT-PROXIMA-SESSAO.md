# PROMPT DA PRÓXIMA SESSÃO — Base Terminológica RC

> **Ritual de continuidade.** Este arquivo é o prompt a colar (ou anexar) no chat seguinte.
>
> **Última atualização:** 2026-08-25 · AGENTE 11 · **CICLOS B057, B058 (YEL LUZBEL) E B087–B088 (PANDORA 1–2) FECHADOS** (Devolutivas O-1..O-8 aplicadas; **0 códigos em todos**; B087/B088 = fontes novas vinculadas ao cluster Pandora/Olimpo — 26 vínculos e 4 fichas materializadas no total; 777/1.852 invariantes) · branch **`arena/01a03ad8-termos-rc`** (esteira 11; trouxe o tip `0d76442` da esteira 10 via fetch+reset). **Ocorrência operacional: 2ª reversão do sandbox entre turnos — recuperada via fetch+reset (ver CONTINUIDADE, ciclo B088).**
>
> **Tarefa da sessão nova:** o curador decide — o piloto do **B089** *Os Anunnaki e a Disputa pela Genética de Pandora* (PDF já em `uploads_recepcao/`; **fecha a trilogia Pandora**), ou outra ordem. **A ordem é do curador.** Não abrir ciclo sem a obra nomeada.

---

## Como usar

1. Anexe **este arquivo primeiro** no chat novo.
2. Em seguida, se precisar de fundo: `CONTINUIDADE.md` (diário; cabeçalho prevalece) → `convencoes-editoriais-rc.md` → `GUIA-MESTRE-RC-APOSTILA-v1.1.md` → arquivos HISTÓRICOS (com banner ⚠️; só como história): `CHECKPOINT-SESSAO-2026-08-21.md` · `PROMPT-INICIAL-DO-AGENTE.md` · `README.md` · `PLANO-MIGRACAO-DE-CHAT.md` · `PACOTE-MIGRACAO-CHAT-2026-08-18.md`.
3. Diga: *leia `PROMPT-PROXIMA-SESSAO.md`, monte o ambiente e apresente o estado.*

**Este arquivo prevalece** para o estado vigente (ver tabela "Mapa da vigência").

---

## PROMPT PARA COLAR NO NOVO CHAT

```
Continue o projeto Base Terminológica RC — as Revelações Cósmicas de Jan Val Ellam. Esta é uma sessão de continuidade. A esteira 10 fechou a revisão de continuidade e os ciclos B074/B075 Mentalma; a esteira 11 (branch arena/01a03ad8-termos-rc) fechou o ciclo B057 A Revolta do Anjo Decaído (10 ampliadas + 7 criadas; RC-142 = remissão; B086–B090 cadastradas; 0 códigos), o ciclo B058 O Início da Revolta Capelina (15 ampliadas + 6 criadas; 0 códigos) e os ciclos B087–B088 Os Livros da Vida de Pandora 1–2 (FONTES NOVAS: 21 fichas do cluster ampliadas + 4 materializadas — Zeus, Prometeu, Pirra, Hefesto — + 26 vínculos de fonte; status 'trabalhada' em ambos; 0 códigos; o título interno do B088 foi alterado na ed. 2022 — registrado como nota). Trilogia Pandora ⅔ fechada — próximo B089 (PDF recebido), na ordem do curador.

AUTORIDADE: o curador (Edson Cella Mendes) é a autoridade máxima. Você organiza, cruza, edita e audita. Nunca decida ontologia sem autorização. Conclusões são sempre sugestões.

PRIMEIRA AÇÃO (antes de qualquer edição):
1. O clone já vem na raiz (main, b420f14). O trabalho da esteira está na branch arena/01a03ad8-termos-rc (esteira 11). Se HEAD local for só b420f14 (main) e o working tree estiver limpo: git fetch origin arena/01a03ad8-termos-rc && git reset --hard FETCH_HEAD. Esperado: o tip da esteira 11 (B057/B058/B087/B088 aplicados; nenhum ciclo ativo — próximo B089). Conferir TODAS as branches (o curador pode subir arquivos em qualquer uma): git ls-remote --heads origin — se houver upload novo em outra branch (ex.: arena/01a03913-termos-rc), fetch + cherry-pick/merge ANTES de editar.
2. SE O WORKSPACE PARECER ANTIGO (ex.: sem livros/CONCLUIDOS/B057, ou HEAD em b420f14 depois de já ter trabalhado): o sandbox reverteu o workspace — refaça fetch + reset ANTES de editar. O store durável é a branch no GitHub; commit + push ao fim de cada turno.
3. pip install --break-system-packages markdown openpyxl python-docx pypdf
4. python3 ferramentas/dados_termos.py → deve retornar exatamente: OK: 777 termos, 1852 relações — dados válidos.
5. Leia PROMPT-PROXIMA-SESSAO.md (este) por inteiro — inclusive as seções Workspace × GitHub e Patrimônio da KB.
6. Resuma o estado e aguarde confirmação do curador. NÃO abrir PR.

ESTADO CANÔNICO: 777 termos (RC-001–RC-777) · 1.852 relações · próximo RC-778 · 449 fichas físicas (448 ficha=True + RC-004 investigação False) · 93 obras (B001–B090 + ART-2025-08-01/02/03) · 37 apostilas em apostilas/CONCLUIDAS/ · 40 livros em livros/CONCLUIDOS/ · 2 amostras em livros/AMOSTRAS/ (B027, B035) · nenhum ciclo em andamento (próximo: B089 — fecha a trilogia Pandora).

FONTE DA VERDADE: o GitHub (branch da sessão: arena/01a03ad8-termos-rc). O Workspace da Arena é sandbox efêmero — o curador trabalha pelo GitHub, não pelo painel de arquivos da Arena. (Decisão do curador, 2026-08-25: sem investimento no Workspace.)

ARTEFATOS DE LEITURA: base-terminologica.xlsx e base-terminologica-leitura.docx estão no GitHub (decisão do curador, 2026-08-25: cópia para download). Regenerar sempre com python3 ferramentas/build_indice.py && python3 ferramentas/build_xlsx.py && python3 ferramentas/build_word.py antes de qualquer commit que mude a base (são espelho; a fonte é dados_termos.py + Markdown).

TAREFA DESTA SESSÃO: abrir o piloto B089 Os Anunnaki e a Disputa pela Genética de Pandora (PDF em uploads_recepcao/ — fecha a trilogia Pandora) e entregar o dossiê enxuto O-1..O-8 — ou a ordem que o curador der. Pendências de fundo: B059 (sem PDF — só físico); obras completas B027/B035; B076–B078 Mentalma III–V (sem PDF); B085/B086/B090 (sem PDF). Não começar nada sem a obra nomeada.

MÉTODO DO CICLO DE LIVRO (padrão B019..B022, B074, B075, B057): PDF em livros/B0NN_slug/ (original.pdf + original.txt paginado, SHA-256) + ficha_ingresso.md + analise/ (camadas 0–3, LEITURA-1, DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md com O-1..O-8) → AGUARDA DEVOLUTIVA (0 códigos) → [aprovada] ampliações via analise/_ampliacoes_B0NN.txt + _aplicar_ampliacoes_B0NN.py (seção ## Ampliação — B0NN antes de ## Fontes) → validar → artefatos (índice, xlsx, docx) → DECISAO-DO-CURADOR.md + RELATORIO-DE-CICLO.md → mover para livros/CONCLUIDOS/ → atualizar CONTINUIDADE + livros/README.md + PROMPT-PROXIMA → push.

REGRAS DE OURO: não inventar / [REVISAR] / [TEXTO INCOMPLETO]; plateia e cartas isoladas; Navalha de Ockham (quase sempre zero códigos — veto absoluto); nada antes da Devolutiva O-1..O-8; quarentenas (mediumística, clínica, política, ufológica, teológica, biográfica, institucional — p. 215 de B074: Hitler/biodemos BANIDO da malha); grafias canônicas (Brahma, Tikun, Sophia, Nefilins, Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo, Wyrd/Urd, Kapila, Vaishnavismo, Hochmah, Moros, Malkuth=Hochmah=Sophia, Orlog=Moros, Awayen/Awaylengan/Awaymaion, Morlens, Ginnungagap, Orunmilá, Obatalá, En Ma, Deva/Aurora, Mohen So, Shanlung); jamais editar BIBLIO de build_xlsx.py programaticamente; nunca colar token/PAT.

LIÇÃO DA SESSÃO 8: push ANTES de abrir PR; PR por último e só se o curador pedir.
LIÇÃO DA SESSÃO 10: o workspace Arena reverte entre turnos sem aviso — o único store durável é o push na branch; re-fetch/re-reset se o tree parecer antigo; commit + push ao fim de cada turno. O curador pode subir arquivos em QUALQUER branch — conferir as branches antes de editar.
LIÇÃO DA SESSÃO 11: o prompt que o curador cola pode estar DEFASADO em relação à branch (visto em 2026-08-25: dizia B074/B075 pendentes quando a branch já os tinha fechado e aberto o piloto B057). O PROMPT-PROXIMA-SESSAO.md da branch prevalece; conferir sempre o estado real da árvore (ciclo ativo em livros/, últimos commits) antes de agir.

Comece agora: valide a base, leia este arquivo e apresente o estado. Aguarde confirmação.
```

---

## Mapa da vigência dos arquivos de continuidade (2026-08-25 — revisão AGENTE 10)

| Arquivo | Papel | Estado |
|---|---|---|
| `PROMPT-PROXIMA-SESSAO.md` | Estado vigente + primeira ação | **VIGENTE** |
| `convencoes-editoriais-rc.md` | Grafias, quarentenas, Navalha | **VIGENTE** |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Método (dossiê → Devolutiva → ampliação) | **VIGENTE** |
| `01-ficha-modelo.md` | Ficha Padrão v2 + guia de preenchimento | **VIGENTE** |
| `02-vocabulario-controlado.md` | Vocabulário controlado (mesmos nomes para a mesma coisa) | **VIGENTE** |
| `CONTINUIDADE.md` | Diário da jornada (cabeçalho = agora) | **VIGENTE** (diário) |
| `INDICE-PALESTRAS.md` | Índice de palestras (estado reconstruído) | **VIGENTE** (índice vivo) |
| `CHECKPOINT-SESSAO-2026-08-21.md` | Retomada antiga | HISTÓRICO (banner; sem procedimento com token) |
| `README.md` | Reconstrução de 2026-08-14 (contagens 760/1.433) | HISTÓRICO (banner) |
| `STATUS-RESTAURACAO.md` | Restauração de 2026-08-19 | HISTÓRICO (banner) |
| `PLANO-MIGRACAO-DE-CHAT.md` | Plano de migração de 2026-08-18 | HISTÓRICO (banner) |
| `PACOTE-MIGRACAO-CHAT-2026-08-18.md` | Snapshot de 2026-08-18 | HISTÓRICO (banner) |
| `PROMPT-INICIAL-DO-AGENTE.md` | Prompt da sessão original (contagens velhas) | HISTÓRICO (banner) |

Nada foi apagado — os históricos conservam a história; o banner ⚠️ no topo de cada um impede confusão com o vigente.

---

## Workspace da Arena × GitHub (2026-08-25 — DECISÃO DO CURADOR)

| O quê | Papel real |
|---|---|
| **GitHub** `institutocura-maker/Termos-RC` · branch `arena/01a03ad8-termos-rc` (esteira 11) | **Fonte da verdade.** O curador sobe PDFs, baixa arquivos (incl. xlsx/docx de leitura), vê o histórico. |
| **Branches das esteiras anteriores** (`arena/01a03913-termos-rc` · `arena/01a02e74` · `arena/01a02c4e` · `arena/01a02a88`) | Histórico versionado; a esteira vigente é a 11. **O curador pode subir arquivos em qualquer branch** — conferir antes de editar. A pasta de obra em processamento fica na branch da sessão o ciclo inteiro e só move para `CONCLUIDOS/` no fechamento. |
| **`main`** | Ainda em `b420f14` (PR #2, Windows). O trabalho desta esteira **não** está no `main`. |
| **Workspace Arena** | Sandbox do agente. Some com a sessão e **reverte entre turnos**. **Decisão do curador (2026-08-25): sem investimento** — o curador não o usa; visor/preview ficam parados. |
| **Como o curador entrega PDF** | *Add files via upload* no GitHub → `uploads_recepcao/` → o agente faz `fetch`/cherry-pick. Anexos de chat **não** caem em `/home/user/uploads/`. |

Consequência operacional: **commit + push ao fim de cada turno** — o push é o que dura.

---

## Artefatos de leitura (xlsx / docx)

**Decisão do curador (2026-08-25): cópia versionada no GitHub** para download.

- `base-terminologica.xlsx` (7 abas) e `base-terminologica-leitura.docx` **estão no Git**.
- Ficam **regeneráveis**: a fonte continua sendo `dados_termos.py` + Markdown; os binários são espelho. Regenerar sempre antes de qualquer commit que mude a base:

```bash
python3 ferramentas/build_indice.py   # → indice-mestre.md
python3 ferramentas/build_xlsx.py     # → base-terminologica.xlsx (7 abas)
python3 ferramentas/build_word.py     # → base-terminologica-leitura.docx
```

`indice-mestre.md` **está** no Git (regenerado a cada ciclo). Apostilas e tratados em DOCX **estão** no Git (`apostilas/CONCLUIDAS/`, `pedagogico/`) — **coleção completa**: 10 apostilas temáticas + 2 tratados (Javé e Thot/Hermes; no nome `Apostila - Javé_ O Buraco Negro...` o `_` é o `:` do título adaptado para Windows).

---

## Patrimônio da KB — o que é canônico

Camadas, da mais dura para a mais mole:

### 1. Núcleo (se isto sumir, a Base some)

| Arquivo | O que é |
|---|---|
| `ferramentas/dados_termos.py` | **Fonte única.** 777 termos + 1.852 relações. Validar sempre. |
| `ferramentas/build_xlsx.py` | BIBLIO das 93 obras. **Edição só manual.** |
| `termos/*.md` | 449 fichas (a carne da ontologia). |
| `indice-mestre.md` | Índice gerado; versionado. |

### 2. Governança (sem isto o próximo agente se perde)

| Arquivo | O que é |
|---|---|
| `PROMPT-PROXIMA-SESSAO.md` | **Vigente.** Estado + primeira ação + mapa da vigência. |
| `convencoes-editoriais-rc.md` | Grafias, quarentenas, Navalha. |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Método (dossiê → Devolutiva → ampliação). |
| `01-ficha-modelo.md` | Ficha Padrão v2 + guia de preenchimento (norma da ficha). |
| `02-vocabulario-controlado.md` | Vocabulário controlado (norma dos nomes). |
| `CONTINUIDADE.md` | Diário da jornada (longo; cabeçalho = agora). |
| `INDICE-PALESTRAS.md` | Índice de palestras (estado reconstruído; atualizado a cada ciclo). |
| `CHECKPOINT-SESSAO-2026-08-21.md` | Retomada antiga; útil como história. **Não** usar o procedimento de clone com token. |
| `PROMPT-INICIAL-DO-AGENTE.md` | Identidade histórica (contagens velhas). |

### 3. Acervo trabalhado (a jornada)

| Pasta | Conteúdo |
|---|---|
| `livros/CONCLUIDOS/` | 40 obras integrais com PDF + extract + dossiê + ampliações (últimas: B057, B058 — Yel Luzbel ⅔ — e B087, B088 — Pandora ⅔). |
| `livros/AMOSTRAS/` | B027 e B035 (Sample; obra completa pendente). |
| `apostilas/CONCLUIDAS/` | 37 palestras/lives (original.txt + apostila.md + DOCX). |
| `pedagogico/` | 10 apostilas temáticas (todas com DOCX) + 2 tratados (com DOCX) + 2 mapas + índice temático + Guia TALM + Dossiê Fase 0 + matriz de auditoria. |
| `materiais_externos/` | EXT (terceiros; **não** toca ontologia). |
| `uploads_recepcao/` | PDFs que o curador subiu (fonte bruta). |
| `backups/pacotes/` | MANIFESTO + FICHAS + REGENERAÇÃO (seguro versionado; **manifesto de 2026-08-18 desatualizado** — ver pendências). |

### 4. Regenerável

`reconstrucao/` · `__pycache__/` · `base-terminologica.xlsx` e `base-terminologica-leitura.docx` (regeneráveis, **porém versionados por decisão do curador, 2026-08-25** — regenerar sempre antes de commitar).

### 5. Arquivos históricos — não confundir com o vigente

`README.md` (contagens 760/1433) · `STATUS-RESTAURACAO.md` · `PLANO-MIGRACAO-DE-CHAT.md` · `PACOTE-MIGRACAO-CHAT-2026-08-18.md` · `PROMPT-INICIAL-DO-AGENTE.md` — todos com banner ⚠️ no topo (revisão 2026-08-25).

---

## Ciclos da esteira — ENCERRADOS

**AGENTE 9:** B019 · B011 · B052 · B043 · B013 · B014 · B016 · B044 · B024 · B041 · B036 · B034 · B042 · B048 · B040 · B037 · B049 · B009 · B023 · B001 · B002 · B033 · B017 · B018 · B039 · B003 · B025 · B026 · B015 · B020 · B021 · B005 · B006 · **B022** · amostras B035 e B027 · Carbono.

Trilogias Dramas / Terra Atlantis / Queda e Ascensão: **ENCERRADAS.**

**AGENTE 10 (2026-08-25) — revisão de continuidade + ciclos B074–B075 *Mentalma* (zero códigos em tudo):**

- A. Higienização: banners HISTÓRICO em 5 arquivos + MAPA DA VIGÊNCIA (nada apagado).
- B. Workspace da Arena: **sem investimento** (decisão do curador) — GitHub = única interface.
- C. xlsx/docx de leitura: **versionados no GitHub** (decisão do curador); coleção `pedagogico/` completa.
- D. Mapa da KB: +3 peças; correção `pedagogico/`: **10** apostilas temáticas.
- **E. B074 *Mentalma I***: Devolutiva aplicada — 5 ampliadas + 2 criadas (RC-550, RC-553); **0 códigos**; B084 cadastrada; quarentena p. 215 banida; CIP 290 × 227 = `[REVISAR]`.
- **F. B075 *Mentalma II***: Devolutiva aplicada — 6 ampliadas + 2 criadas (RC-554, RC-555); **0 códigos**; B085 cadastrada; PKMzeta/hipnose = leitura filosófica; NDEs/Ramtha fora.
- **G. Piloto B057** (último commit da esteira 10): ingresso + dossiê enxuto, 0 códigos.

**AGENTE 11 (2026-08-25) — ciclo B057 *A Revolta do Anjo Decaído* FECHADO (zero códigos):**

- **Devolutiva O-1..O-8 100% aprovada e aplicada.** Obra secundária (psicografia de Jeane Miranda; prefácio de Ellam; ed. 2022 "Corrigida e Adaptada por Gullan Greyl", PT-PT — anotada na BIBLIO).
- **10 fichas ampliadas** (RC-002/007/009/074/078/092/252/442/443/446) + **7 criadas** (RC-036 Biodemos · RC-039 Capela · RC-046 Dan · RC-146 Zian/Zion · RC-445 Biocoletivos · RC-447 Primeiro Pesquisador · **RC-142 Yel Luzbel = remissão para RC-078** — duplicidade resolvida sem fusão de códigos).
- **B086–B090 cadastradas** (5 obras de Jeane Miranda da p. 70; `identificada`; sem PDF). **O Funeral da Evidência = já era B068** (nenhuma duplicata; nota de B061 corrigida).
- **B057 nas fontes de RC-085/RC-444/RC-491** (O-6). Grafias: "Shanlun" → Shanlung; datas 687 mil × 742 mil = variante anotada. Quarentenas: mediumística/ufológica/teológica/institucional.
- Base: **777/1.852 invariantes**; 439 fichas; 93 obras; 37 livros em `CONCLUIDOS/`.
- **Ciclo B058 *O Início da Revolta Capelina* FECHADO** (piloto + Devolutiva aplicada no mesmo dia): **15 fichas ampliadas + 6 criadas** (RC-021 Antares · RC-103 Tau Ceti · RC-448 Deslacre · RC-451 Universidade de Tau Ceti · RC-452 Grão-mestre · RC-453 Hostes de Sophia); **0 códigos**; BIBLIO de B058 com a nota da ed. 2022 + notas com fontes externas (Wikipédia/B031 — quarentena institucional); **isolamento mediúnico total** (sem prefácio de Ellam neste volume — dedicatória de Adilson Reane + notas de Yel/Jeane); "falso Criador" = leitura do ser em revolta, jamais fato ontológico; "Capella" → Capela; erro "A Revolto" registrado sem corrigir a voz; **radar limpo** (as 7 obras da autora já estavam na BIBLIO). Pasta em `CONCLUIDOS/`.
- **Ciclo B088 *Os Livros da Vida de Pandora 2* FECHADO** (piloto + Devolutiva aplicada no mesmo dia): **12 fichas do cluster ampliadas + B088 nas fontes de 13 termos** (12 + RC-465); status **`trabalhada`** + nota com **o título interno alterado da ed. 2022** ("As Poções dos Titãs e a Ameaça do Olimpo" — nota bibliográfica; o canônico se mantém); **0 códigos**; **isolamento total** (sem prefácio de Ellam — o "Manifesto de Pandora" assinado pela entidade; **Khaos=Javé** = leitura do ser; a "hipnose" = clínica; Eva e Maria de Magdala = social/gênero); erros de citação de Pessoa preservados como anomalias; cross cruciais: **Pandora em Capela** (Yel Luzbel), a humanização concluída, a profecia Pirra+filho de Prometeu (**Deucalião**), o medo da morte de Zeus (o artefato), Témis e Ares observacionais. Pasta em `CONCLUIDOS/` (40 obras).
- **Ciclo B087 *Os Livros da Vida de Pandora 1* FECHADO** (piloto + Devolutiva aplicada no mesmo dia): **FONTE NOVA** (0 termos citavam B087) — **9 fichas do cluster ampliadas + 4 materializadas** (RC-145 Zeus · RC-301 Prometeu · RC-303 Pirra · RC-307 Hefesto) + **B087 nas fontes de 13 termos**; status **`trabalhada`** + nota da ed. 2022; **0 códigos** (777/1.852); quarentena **teológica CRÍTICA — isolamento sumário padrão B001/B002** (prefácio de Ellam: Jesus/Javé); clínica (Epimeteu viciado nas "poções"); social/de gênero (a "violência mental"); divergências × B020 registradas, jamais fundidas (a caixa aberta por **Epimeteu**; a "esperança" como o último "algoritmo viral"); **Atena = registro observacional** (sem termo). Pasta em `CONCLUIDOS/` (39 obras).

HEAD: tip da branch `arena/01a03ad8-termos-rc` (esteira 11). PR **não** aberto.

Pendências de livro (quando o curador quiser): **B089** *Os Anunnaki e a Disputa pela Genética de Pandora* (**PDF recebido — fecha a trilogia Pandora**); B059 *Sinais de Guerra em Capela* (**sem PDF — somente físico**, ASIN B0GFPWXVSG; fecha a trilogia de Yel Luzbel); obras completas B027 e B035; B076–B078 *Mentalma III–V* (sem PDF); B085 *Hyren-Hyron*, B086 e B090 (sem PDF). Pendências menores: manifest versionado desatualizado (curador decide regenerar); CIP B074 `[REVISAR]`.

---

## Encerramento de sessão (checklist)

1. Última atualização (data, agente, branch, HEAD).
2. ESTADO CANÔNICO — só se `dados_termos.py` mudou.
3. Pendências de fundo — o curador escolhe a ordem.
4. Bloco *PROMPT PARA COLAR* — a sessão seguinte não depende do chat anterior.
