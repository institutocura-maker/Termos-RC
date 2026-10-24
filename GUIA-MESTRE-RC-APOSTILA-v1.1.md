# GUIA-MESTRE DA BASE TERMINOLÓGICA RC
## Revelações Cósmicas — Jan Val Ellam · Documento de Reconstrução e Trabalho
### Versão 1.1 · 2026-08-19

**Para qualquer agente que inicie uma nova sessão:** leia este guia e monte o workspace.

---

## Instrução de retomada (para o curador)

Anexe este arquivo (ou o `GUIA-MESTRE-RC-APOSTILA.txt` v1.1) numa nova conversa **junto com o `prompts/PROMPT-INICIAL-DO-AGENTE.md`** e escreva:
*"Leia o Guia-Mestre da RC e o Prompt Inicial, monte o workspace, valide a base e me apresente o estado + próximo passo."*

**Curador:** analista de sistemas, programador, Pajé (tradição Rubens Saraceni), 14+ anos de estudo das RC, estudioso de Jyotish/Ifá.

---

## SUMÁRIO

1. Sobre o projeto e o curador — contexto, filosofia, decisões canônicas
2. O que é a Revelação Cósmica (RC) — tese central, 7 narrativas, cadeias canônicas, glossário mínimo
3. A Base Terminológica — estrutura, dados atuais (2026-08-19), como regenerar
4. **Fluxo Operacional em 2 Ciclos** — Curadoria (Base-first) + Apostilas em Lote (novo)
5. **GitHub como Espelhamento** (novo)
6. Convenções Editoriais RC (v2, canônica) — público, fala, notas, formato, glossário, marcadores, kardecismo, grafias
7. DNA do Estilo Ellam — livros × palestras (e o que isso significa para as apostilas)
8. Pipeline de Produção de Apostilas — fluxo, convenção de nomes, estrutura de pastas, ficha v2.0
9. Exemplo de Apostila — "As Faces de Javé — O Senhor Parameshthi" (estrutura e lições)
10. Histórico do que foi feito — livros, enciclopédia, DNA, apostilas, pedagogia
11. Pendências e Próximos Passos — palestras, livros, divergências, grafias, curadoria
12. Instruções para o Novo Agente — Prompt Inicial, ordem de leitura, regras de ouro

---

# PARTE 1 — SOBRE O PROJETO E O CURADOR

## 1.1 Visão geral

Este projeto sistematiza o corpus de **Jan Val Ellam** — as Revelações Cósmicas (RC) — numa **Base Terminológica** (termos, relações, fichas, obras) e produz **Apostilas de estudo para humanos** a partir de palestras. É parte de um acervo multi-domínio off-grid do curador (a "Arca de Noé Digital"), preparado para cenário sem internet.

O curador: veterano de IBM Brasil (25 anos), Pajé com Pai de Santo (tradição Rubens Saraceni), estudioso full-time de Jyotish (astrologia védica) e Ifá/256 Odus, programador sênior (Python, RAG, LoRA, fine-tuning), agricultor/sobrevivencialista. Hardware local: 32 GB RAM + 12 GB VRAM (Mistral Nemo 12B + Hermes como modelo base; adaptadores LoRA por domínio).

## 1.2 Filosofia operacional (princípios inegociáveis)

1. O curador é a autoridade. A IA é a ferramenta. Hierarquia inegociável.
2. Preservação > velocidade. Qualidade importa mais que velocidade.
3. Cada entrada bem feita é uma semente para a IA que continuará o trabalho.
4. A IA local é o destino (Professora de RC — agente pedagógico com anamnese de alunos).
5. Não inventar, não completar, não interpolar. Se falta fonte, marca-se `[REVISAR]`/`[TEXTO INCOMPLETO]`.
6. A voz do autor é maior que a do editor. Preservar a fala do Ellam (marcadores, humor, digressões).
7. **Fluxo é lei:** cada ciclo termina com `gerar_pacotes.py` e atualização do `admin/logs/CONTINUIDADE.md`.

## 1.3 Decisões canônicas (registradas)

- A Base Terminológica deste projeto é a referência canônica para grafias e termos (decisão do curador, 2026-08-13). Documentos de um acervo anterior (que usava "Brama", "Tikkun", "Sofia") são fonte de insights editoriais, não autoridade terminológica.
- Voz do Ellam prevalece sobre interpretações de terceiros (inclusive o Glossário Raquyel, B031).
- **Compactação (Navalha de Ockham):** preferir absorver candidatos em fichas existentes a criar códigos novos; proteger o RAG local (RTX 3060 / Llama 3) de inchaço de vocabulário.
- **Quarentenas rígidas:** clínico/científico, político/geopolítico, ufológico, teológico, STT duvidoso — leitura do autor, não fato.
- **Falas da plateia:** sempre isoladas, nunca viram ontologia.

---

# PARTE 2 — O QUE É A REVELAÇÃO CÓSMICA (RC)

## 2.1 Tese central (em 1 parágrafo)

A Revelação Cósmica (RC-094) é um sistema de conhecimento espiritual-cósmico divulgado por Jan Val Ellam (pseudônimo de Rogério de Almeida Freitas) em livros e palestras. Sua tese: este universo é uma "Criação Indevida" (RC-167). O Criador (RC-001 — Javé, Brahma, Alá...) é, na verdade, um ser de altíssima hierarquia chamado Prabrajna (RC-152) que, ao tentar projetar um novo universo, sofreu um colapso psíquico, "caiu" na própria criação e ficou doente e refém (RC-196). Os seres criados (biodemos, RC-036, e a humanidade, RC-099) herdaram os defeitos do "código-fonte" (CFD, RC-040). A história é o drama da rebelião (RC-002), do isolamento da Terra (RC-070, a "quarentena sideral") e da Reintegração Cósmica (RC-003): as criaturas, como agentes da vida (RC-148), ajudam a curar o Criador (RC-332) e a consertar a Obra (Tikun, RC-514).

Em uma frase: *"Um deus imperfeito caiu na própria criação, e somos nós — suas criaturas — que podemos ajudá-lo a se curar."*

## 2.2 As 7 Narrativas (o esqueleto)

| # | Narrativa | Pergunta-guia | Conceitos-âncora |
|---|---|---|---|
| 1 | O Criador e a Criação | Quem criou? Como? | Javé (RC-001), Prabrajna (RC-152), Criação Indevida (RC-167), CFD (RC-040), Eras (RC-155) |
| 2 | A Queda e o Drama | O que deu errado? | Demência do Criador (RC-526), Criador refém (RC-196), Mergulho (RC-528), Khaos (RC-294) |
| 3 | A Rebelião e o Exílio | O que partiu a harmonia? | Rebelião de Lúcifer (RC-002), Yel Luzbel (RC-142/078), Exilados de Capela (RC-007), Isolamento (RC-070), Revolta Capelina (RC-450) |
| 4 | Os Seres do Cosmos | Quem habita a criação? | Biodemos (RC-036), Demos (RC-049), Anunnakis (RC-024), Trimurti (RC-104), Sophia (RC-009), Jesus (RC-072) |
| 5 | A Humanidade e a Terra | Quem somos nós? | Homo sapiens (RC-099), Pandora (RC-086/283), Éden (RC-242), DNA holográfico (RC-217), Agentes da Vida (RC-148) |
| 6 | Os Mundos e o Cosmo | Onde tudo acontece? | Universo Material (RC-107), Antimaterial (RC-106), Espiritualidades (RC-059/060/061), Perpérion (RC-087) × Tempérion (RC-472) |
| 7 | O Caminho de Volta | Como se conserta? | Reintegração (RC-003), Tikun (RC-514), Favor Divino (RC-332), Mentalma (RC-166), Cidadão Cósmico (RC-226) |

## 2.3 Cadeias canônicas (quem é quem)

**Cadeia do Criador:**
Adhy (RC-310) → Adhyatman → ADHYPRABRAJNA (RC-410) → Prabrajna (RC-152) → Brahma/Javé/Alá (RC-037/001) → Kether (RC-261) → Caos (RC-284) → Ra-Atom/Og-mi (RC-331) → Demiurgo/Ialdabaoth (RC-482)
→ Vishnu/ADHYMAVATANA (RC-135/408) → Mohen So (RC-081) → Sophia (RC-009) → Jesus (RC-072)
→ Shiva/ADHYSAVNA (RC-102/409) → Hara (RC-413)/Krishna (RC-414)/Sai Baba

**Cadeia da Rebelião:**
Yel Luzbel/Lúcifer (RC-142/078) → Rebelião de Lúcifer (RC-002) → Isolamento Cósmico (RC-070) → Família Yel (RC-442) → Capela (RC-039) / Len Mion/Satã (RC-074) → Família Mion (RC-443) → Exilados de Capela (RC-007) → Quarentena (RC-342) → Revolta Capelina (RC-450)

**Outras identidades-chave:**
- Pandora (RC-086) = Val Dimon (RC-118) = Kalil Kadmon (RC-299) = serpente do Éden (RC-283);
- Judas = Yel Am/Yel Liam (RC-138); Lúcifer = Yel Luzbel (RC-078/142); Val El = Jan Val Ellam (RC-071);
- Rochester (Grupo Atlan) = Val Pen (RC-129);
- Perpérion (RC-087) ≠ Tempérion (RC-472) — setores distintos da Espiritualidade Laboratorial;
- Hochmah (RC-565) = 2ª Sefirah (Sabedoria) = epíteto hebraico de Sophia (RC-009);
- **Wyrd/Urd (RC-658)** — fusão do antigo WD (RC-560 é remissão histórica);
- **Mohen So = Phanes/Protogonos** (RC-282) — Mohen So NÃO é Moros.

## 2.4 Glossário mínimo (18 termos)

| Termo | Código | Significado |
|---|---|---|
| Revelação Cósmica | RC-094 | O corpus de conhecimento do Ellam |
| Criação Indevida | RC-167 | O universo como "acidente" da queda de Prabrajna |
| CFD / CFDP | RC-040/153 | Código Fonte Definidor (e Pessoal) — o "software" de cada ser |
| Biodemos | RC-036 | Seres do universo antimaterial com biologia não convencional |
| Demos | RC-049 | Seres do universo antimaterial ("de lá") |
| Anunnakis | RC-024 | Civilização extraterrestre reinterpretada |
| Trimurti | RC-104 | Brahma, Vishnu, Shiva como expressões do drama cósmico |
| Sophia | RC-009 | Avatar de Mohen So (Vishnu); o "Cristo Cósmico" |
| Isolamento Cósmico / Quarentena | RC-070/342 | O "cárcere" da Terra |
| Reintegração Cósmica | RC-003 | O retorno da Terra à convivência cósmica |
| Tikun | RC-514 | O "conserto" da Criação e a recuperação do Criador |
| Favor Divino | RC-332 | Invertido: nós curamos Deus |
| Mentalma | RC-166 | Método prático (yoga mental) do Ellam |
| Cidadão Cósmico | RC-226 | A identidade plena do ser consciente |
| Espiritualidade Laboratorial | RC-061 | Estrato onde divindades cocriadoras projetam universos |
| Criatura Universal | RC-042 | O ser futuro que conduzirá a Criação ao equilíbrio |
| Criaturas-ferramenta | RC-449 | Seres criados como instrumentos do Criador caído |
| Teia quântica / Wyrd | RC-559/658 | O princípio "o que sai volta" / a Teia do Destino |

---

# PARTE 3 — A BASE TERMINOLÓGICA

## 3.1 O que é e como está estruturada

A Base é um projeto orientado a dados: um arquivo Python é a fonte única de verdade e vários builders geram os artefatos.

```
rc-terminologia/
├── README.md · admin/logs/CONTINUIDADE.md · convencoes-editoriais-rc.md
├── GUIA-MESTRE-RC-APOSTILA.txt (v1.1) · prompts/PROMPT-INICIAL-DO-AGENTE.md
├── admin/logs/PACOTE-MIGRACAO-CHAT-2026-08-18.md · PLANO-MIGRACAO-DE-CHAT.md
├── indice-mestre.md · base-terminologica.xlsx · base-terminologica-leitura.docx
├── ferramentas/
│   ├── dados_termos.py ← TABELA-MESTRA (TERMOS + RELACOES) — FONTE ÚNICA
│   ├── build_xlsx.py · build_indice.py · build_word.py · build_apostila.py
│   ├── criar_pasta_palestra.py · gerar_pacotes.py · restaurar_pacotes.py
├── termos/ ← 378 fichas detalhadas (RC-###-nome.md)
├── apostilas/CONCLUIDAS/ ← 13 apostilas concluídas (pasta YYYY-MM-DD_slug/)
├── pedagogico/ ← temáticas (Javé, Thot) + mapa
├── reconstrucao/pacotes/ ← pacotes de reconstrução (TXT)
└── reconstrucao/backups/ ← backups pré-ciclo do dados_termos.py
```

## 3.2 Dados atuais (2026-08-19)

| Item | Valor |
|---|---|
| Termos | **767** (RC-001 a RC-767) |
| Relações tipadas | **1.531** |
| Fichas detalhadas | **378** (377 canônicas + RC-004 Elohim investigação) |
| Obras cadastradas | 79 (B001–B079) |
| Próximo código | **RC-768** |
| Apostilas concluídas | **13** (em apostilas/CONCLUIDAS/) |
| Temáticas pedagógicas | **2** (Javé; Thot) + mapa Buraco Negro Javé |
| Fidelidade dos pacotes | **435/435 arquivos** (pacote == manifesto == workspace) |
| Checksum dados_termos.py | `7a95c8dd5bdb9b981b55f43e9dd1e34229f155be548e232870b27d9e69d028ac` |

## 3.3 Formato dos dados (para reconstruir a base)

**TERMOS** (em `dados_termos.py`): cada termo é uma tupla `(codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha)`.
- status: `candidato` ⚪ / `provisório` 🟡 / `em análise` 🟠 / `verificado` 🟢;
- fontes: lista de siglas `B###` (livros) / `P###` (palestras) / `ART-###`;
- relacionados: string `"RC-###; RC-###; ..."`;
- ficha: True/False (existe ficha em `termos/`).

**RELACOES**: cada relação é uma tupla `(termoA, tipo, termoB, fonte)`. Tipos comuns: é-um, parte-de, criado-por, envolve, ocorre-em, associado-a, opõe-se-a, sinônimo, variação, relaciona-se-a, tema-de, integra, manifesta-se-em, etc.

**Categorias**: SER_DIV a SER_LOG (Seres 1.1–1.8); COS_COG a COS_ETI (Conceitos 2.1–2.6); LOK_PLA a LOK_REG (Lokas 3.1–3.4); PRO_BIO a PRO_FIS (Processos 4.1–4.4); TEC_NAV a TEC_ESC (Tecnologias 5.1–5.4); GEN_DIV a GEN_AVO (Genealogias 6.1–6.4); EVE_GUE a EVE_MIS (Eventos 7.1–7.5); TER_SAN a TER_OUT (Termos Específicos 8.1–8.5).

## 3.4 Como regenerar os artefatos

```bash
cd /home/user/rc-terminologia
python3 ferramentas/dados_termos.py          # valida (códigos únicos, sequência, relações)
python3 ferramentas/build_indice.py          # gera indice-mestre.md
python3 ferramentas/build_xlsx.py            # gera base-terminologica.xlsx (7 abas)
python3 ferramentas/build_word.py            # gera base-terminologica-leitura.docx
python3 ferramentas/build_apostila.py apostilas/SLUG/apostila.md   # apostila DOCX
python3 ferramentas/gerar_pacotes.py         # regenera pacotes + manifesto (HÁBITO)
python3 ferramentas/restaurar_pacotes.py     # restaura a partir dos pacotes
```

> **LIÇÃO CRÍTICA:** NÃO editar programaticamente a lista `BIBLIO` dentro de `build_xlsx.py` (corrompeu o arquivo 2x). Atualizar entradas da bibliografia manualmente (ou via `repr()`).

---

# PARTE 4 — FLUXO OPERACIONAL EM 2 CICLOS (v1.1 — NOVO)

## 4.1 Ciclo de Curadoria (Base-first)

**Objetivo:** absorver uma palestra na Base (termos + relações + fichas) SEM criar a apostila.

```
TXT da palestra
  → preservar original.txt (byte a byte, SHA-256)
  → ficha_ingresso.md
  → leitura 2x (reconhecimento + terminológica)
  → camadas 0–3 + leitura segmentada + chunks (analise/)
  → DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md (candidatos, ampliações, bloqueios, STT)
  → AGUARDA DEVOLUTIVA DO CURADOR (nenhum código consumido antes!)
  → [Devolutiva aprova] consumir códigos RC-###
  → criar/ampliar fichas em termos/ + cruzar relações
  → atualizar dados_termos.py + validar
  → regenerar artefatos (índice, XLSX, DOCX)
  → atualizar admin/logs/CONTINUIDADE.md + INDICE-PALESTRAS.md
  → python3 ferramentas/gerar_pacotes.py  ← HÁBITO OBRIGATÓRIO
  → (opcional) sincronizar GitHub
```

**Entregáveis por palestra:** `original.txt`, `ficha_ingresso.md`, `analise/` (camadas, chunks, Dossiê, DECISAO-DO-CURADOR, RELATORIO-DE-CICLO).

## 4.2 Ciclo de Apostilas (em Lote)

**Objetivo:** transformar palestras com Dossiê+Devolutiva concluídos (aguardando) em apostilas.

```
Gatilho: acumular 3+ palestras com Dossiê+Devolutiva concluídos sem apostila
  → para cada palestra (ordem cronológica):
      1. apostila.md ← TRANSCRIÇÃO EDITADA INTEGRAL (~100%, NUNCA resumir; formato TOP)
      2. python3 ferramentas/build_apostila.py apostilas/SLUG/apostila.md → DOCX
      3. mover pasta para apostilas/CONCLUIDAS/
      4. atualizar índices (raiz + apostilas/INDICE-PALESTRAS.md)
  → python3 ferramentas/gerar_pacotes.py  ← HÁBITO
  → sincronizar GitHub
```

**Formato TOP da apostila:** capa (título, autor, data, local, subtítulo, nota do editor) → PARTES roxas (`# PARTE I — ...`) → capítulos (`## ...`) → citações em bloco (`> "..." — fonte`) → notas editoriais verdes (`Nota do editor: ...`) → glossário local A–D com remissões RC-### → TOC (campo Word; atualizar com Ctrl+A+F9).

## 4.3 Quando NÃO fazer

- Nunca criar apostila antes da Devolutiva do curador;
- Nunca consumir código sem Devolutiva;
- Nunca misturar falas da plateia na ontologia.

---

# PARTE 5 — GITHUB COMO ESPELHAMENTO (v1.1 — NOVO)

## 5.1 O repositório

- **URL:** `https://github.com/institutocura-maker/Termos-RC` (PRIVADO — requer token);
- **Branch:** `main`;
- **Natureza:** espelho/backup do estado canônico — o workspace local (`/home/user/rc-terminologia`) é a fonte primária de trabalho.

## 5.2 O que vai / não vai para o GitHub

| Vai | Não vai |
|---|---|
| `dados_termos.py` + builders | DOCX/XLSX (regeneráveis) |
| `termos/*.md` (fichas) | `reconstrucao/` (pacotes/backups — viajam nos TXT) |
| `apostilas/CONCLUIDAS/*/apostila.md` + `analise/` | `__pycache__` |
| `pedagogico/*.md` + mapa SVG | arquivos temporários |
| Docs: GUIA-MESTRE, PROMPT-INICIAL, PACOTE-MIGRACAO, PLANO, README, CONTINUIDADE | — |

## 5.3 Como sincronizar (2 momentos)

1. **Ao fim de cada Ciclo de Curadoria** → subir `dados_termos.py` + fichas novas + docs (núcleo muda a cada palestra);
2. **Ao fim de cada Lote de Apostilas** → subir `apostila.md` + `analise/` + temáticas.

**Comando (token via variável de ambiente, NUNCA em arquivo):**
```bash
export GH_TOKEN='...'
cd /tmp && rm -rf Termos-RC
git clone https://x-access-token:${GH_TOKEN}@github.com/institutocura-maker/Termos-RC.git
# copiar arquivos atualizados do workspace → repo
cd Termos-RC && git add -A && git commit -m "sync: estado canônico" && git push
```

---

# PARTE 6 — CONVENÇÕES EDITORIAIS RC (v2, CANÔNICA)

Resumo consolidado. O documento completo está em `convencoes-editoriais-rc.md`.

## 6.1 Hierarquia de referências
1. Base Terminológica RC (termos, grafias, relações) — CANÔNICA;
2. Convenções Editoriais RC v2 — CANÔNICA;
3. Obras primárias de Jan Val Ellam — fonte primária;
4. Dossiê do estilo (palestras) — insights editoriais;
5. Convenções v1 / Glossário Mestre do acervo anterior — NÃO canônico;
6. Glossário Raquyel (B031) — referência secundária valiosa.

## 6.2 Sobre o público
- Público indefinido/heterogêneo (kardecistas, curiosos, estudiosos); sem "plateia cativa";
- Notas didáticas e acessíveis; termos técnicos com referência cruzada na 1ª ocorrência; cross-reference com kardecismo bem-vindo (sem endosso); cada apostila é "primeira leitura possível".

## 6.3 Sobre a preservação da fala do Ellam
- Preservar vocabulário, ritmo, marcadores orais, digressões, autocorreções, humor, anedotas. Não domesticar;
- Erros de STT: corrigir com nota na 1ª ocorrência (nunca eliminar silenciosamente);
- Repetições 1–3: reduzir; repetições 4–5+: manter (ênfase);
- Frases truncadas: manter, marcar `[frase truncada]` se necessário;
- Fala da plateia: separar com "Intervenção da plateia (nome)";
- Nunca inventar, completar ou interpolar.

## 6.4 Sobre os objetivos editoriais
- Primário: grupos de estudo (autocontida, sem depender da palestra);
- Secundário: treinamento da Professora de RC (IA pessoal) — material ingerível.

## 6.5 Sobre as notas editoriais
- Contextuais, não avaliativas (nunca dizer se o Ellam está certo ou errado);
- Quando colocar: termo técnico na 1ª vez; referência histórica/mitológica; uso próprio do autor; cross-reference esclarecedor;
- Quando NÃO colocar: o Ellam já explica; termo autoexplicativo; redundante com glossário.

## 6.6 Sobre o formato
- Apostila para Humanos (DOCX) = padrão. Caderno Estruturado (JSON + MD) = quando denso;
- Identidade visual: H1 roxo escuro `#331A55` · H2 roxo médio `#442266` · H3 roxo claro `#553377` · nota editorial verde `#2E7D4F` sobre `#EEF6F0` · citação em destaque roxo `#443377` sobre `#F2EFFA` · corpo Calibri 11pt.

## 6.7 Sobre o Glossário e a Enciclopédia
- Glossário Mestre = Base Terminológica (canônica). Enciclopédia = material narrativo complementar;
- Toda palestra nova → extrair termos (aspas = detector!) → cruzar com a Base → cadastrar novos (fonte P###).

## 6.8 Marcadores orais (preservar sempre)
`pô` · `pá` · `pessoal` · `ô cara` · `mano` · `nóis` · `rapaz` · `meu amigo` · `meus povos` · `M****` · `putz` · `cacete` · `bicho` · `besteira` · `zebra` · `tá` · `Pô, vi, é` · `cara pálida`.
Exceção: erros claros de STT (ex.: "Ticum"→Tikun; "H"→Olm) corrigidos com nota.

## 6.9 Conteúdo kardecista
Cross-reference frequente sem endosso. Termos a distinguir: Espírito, Perispírito, Mediunidade, Comunicação, Reencarnação, Plano espiritual, Demônio (vs. demos RC-049), Anjo (vs. anjos clones).

## 6.10 Formas canônicas (CORRIGIDAS pela Base — crítico!)

| Termo | NÃO usar | CANÔNICO |
|---|---|---|
| Criador hindu | Brama, Bramá | Brahma (Brajna) — RC-037 |
| Reparo cósmico | Tikkun, Ticum | Tikun Cósmico — RC-514 |
| Sabedoria (2ª Sefirah) | Chokmach (variação ok) | Hochmah — RC-565 |
| Sophia | Sofia | Sophia — RC-009 |
| Nefilins | Nefelins (variação ok) | Nefilins (= Anunnakis) — RC-488 |
| Xamanismo | Chamanismo, Xamanismo (sempre X) | Xamanismo — RC-577 |
| Teia do Destino | WD (antigo) | Wyrd / Urd — RC-658 (RC-560 remissão) |
| Vaishnavismo | Vixenuísmo (variação ok) | Vaishnavismo — RC-757 |
| Sábio hindu | Capila | Kapila (grafia canônica) |

---

# PARTE 7 — DNA DO ESTILO ELLAM

## 7.1 DNA dos LIVROS (quantitativo, 35 obras primárias, ~2M palavras)
- Frases longas, subordinadas; erudição teológica; tom doutrinário; neologismos constantes; referências cruzadas entre obras.

## 7.2 DNA das PALESTRAS (dossiê do acervo anterior — insights editoriais)
- Fala espontânea com marcadores; digressões frequentes; humor; repetições enfáticas; perguntas da plateia intercaladas;
- STT (transcrição automática) exige correção com nota; STTs duvidosos → Colecionar Incertezas.

## 7.3 Implicação para a Apostila
- Apostila = transcrição editada integral (~100%), organizada em PARTES temáticas, com citações literais, notas editoriais verdes e glossário local A–D com remissões RC-###;
- Nunca resumir; nunca "domesticar" a fala.

---

# PARTE 8 — PIPELINE DE PRODUÇÃO DE APOSTILAS

## 8.1 Convenção de nomes (canônica)
- Pasta: `apostilas/AAAA-MM-DD_slug_da_palestra/` (ex.: `2023-05-13_bastidores_revelacao_cosmica/`);
- Concluída: mover para `apostilas/CONCLUIDAS/AAAA-MM-DD_slug/`;
- Temática: `pedagogico/Apostila-Estudo-Slug.md`.

## 8.2 Estrutura de cada pasta
```
YYYY-MM-DD_slug/
├── original.txt          ← preservado byte a byte
├── ficha_ingresso.md     ← ficha v2.0
├── apostila.md           ← (quando gerada)
├── Apostila - Título.docx ← (quando gerada)
└── analise/
    ├── METADADOS-INGRESSO.json
    ├── camada-0.txt · camada-1.txt · camada-2.txt · camada-3.txt
    ├── leitura-segmentada.txt · leitura/chunk-NN.txt
    ├── DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md
    ├── DECISAO-DO-CURADOR.md · RELATORIO-DE-CICLO.md
```

## 8.3 Ficha de ingresso v2.0 (SIMPLIFICADA)
Campos: Palestra, Data, Local, Fonte proposta (P###), Arquivo original (bytes + SHA-256), INFORMAÇÃO DISPONÍVEL (do curador), INSTRUÇÕES ESPECIAIS, Inferências da IA (leitura 1 — pelo sumário).

## 8.4 Fluxo de produção (7 passos)
1. Criar pasta + salvar `original.txt` + ficha v2.0;
2. Leitura 2x (reconhecimento + editorial);
3. Extração de termos (aspas = detector) → cruzamento com a Base;
4. Edição da `apostila.md` — TRANSCRIÇÃO EDITADA INTEGRAL (~100%, NUNCA resumir);
5. Geração: `build_apostila.py` → DOCX;
6. Atualização: Base (termos novos com fonte P###), bibliografia, índice de palestras;
7. Revisão do curador → iteração.

## 8.5 Marcadores do Markdown da apostila
- Metadados no topo: `@titulo:`, `@autor:`, `@data:`, `@local:`, `@subtitulo:`, `@nota_editor:`;
- `# PARTE I — ...` (roxo) · `## Capítulo` (roxo médio) · `> "citação" — fonte` · `Nota do editor: ...` (verde).

## 8.6 Lições aprendidas (importante!)
- NUNCA resumir a palestra — a apostila é transcrição editada integral (~100%);
- NUNCA editar programaticamente a BIBLIO do `build_xlsx.py`;
- Sempre rodar `gerar_pacotes.py` ao fim de cada ciclo;
- Verificar fidelidade dos pacotes (pacote == manifesto == workspace) após regenerar;
- Manter os DOIS índices sincronizados: `INDICE-PALESTRAS.md` (raiz) e `apostilas/INDICE-PALESTRAS.md`.

---

# PARTE 9 — EXEMPLO DE APOSTILA ("As Faces de Javé — O Senhor Parameshthi")

> Referência histórica do formato. As apostilas recentes seguem o mesmo padrão (ver `apostilas/CONCLUIDAS/`). Estrutura-tipo: capa → nota do editor → PARTES temáticas → citações em bloco → notas verdes → glossário A–D → TOC.

**Modelos vivos (2026-08-18):**
- `apostilas/CONCLUIDAS/2023-12-02_thot_enigmatico_hermes_trimegisto/Apostila - Thot, o Enigmático Hermes Trimegisto.docx` (11 PARTES);
- `apostilas/CONCLUIDAS/2025-11-29_revelacao_ifa_destino_seres/Apostila - A Revelação de Ifá e o Destino dos Seres.docx` (11 PARTES);
- Temática: `pedagogico/Apostila - Thot e Hermes — O Mentor Científico da Humanidade.docx` (10 PARTES).

---

# PARTE 10 — HISTÓRICO DO QUE FOI FEITO

## 10.1 Livros processados (42 PDFs, extratos em ferramentas/)
Obras primárias de Ellam com extratos de texto; bibliografia consolidada em `build_xlsx.py` (BIBLIO — 79 obras B001–B079).

## 10.2 Palestras processadas (fluxo Base-first, 2026-08-18)

| Palestra | Códigos | Status |
|---|---|---|
| P2021-03-27 — Enki, Enlil e o Fim Súbito da Babilônia | RC-764/765 | Base + apostila concluída |
| P2023-05-13 — Bastidores da Revelação Cósmica | RC-761 | Base + apostila concluída |
| P2023-12-02 — Thot, o Enigmático Hermes Trimegisto | RC-762/763 | Base + apostila concluída |
| P2024-02-03 — O Jainismo e o Druidismo Ancestrais | RC-759/760 | Base + apostila concluída |
| P2024-09-28 — A Raça Inabalável dos Sethianos Emancipados | RC-766 | Base + apostila concluída |
| P2025-11-29 — A Revelação de Ifá e o Destino dos Seres | RC-767 | Base + apostila concluída |
| (mais 7 anteriores) | RC-596 a RC-760 | apostilas concluídas em CONCLUIDAS |

**13 apostilas DOCX concluídas** em `apostilas/CONCLUIDAS/`.

## 10.3 Material pedagógico
- **Temática "Javé: O Buraco Negro da Revelação Cósmica"** (Super-Nó Semântico — aprovada pelo curador);
- **Temática "Thot e Hermes — O Mentor Científico da Humanidade"** (2026-08-18);
- **Mapa SVG do Buraco Negro Javé** (SEGURADO — regenerar quando mais palestras agregadas).

## 10.4 Correções de engenharia (2026-08-18)
1. Gerador/restaurador de pacotes: fidelidade byte a byte (concatenação sem join; busca binária do FIM-ARQ); 435/435 arquivos;
2. Manifesto dinâmico: `gerar_pacotes.py` computa o estado automaticamente (antes hardcoded);
3. Duplicata órfã removida (`2024-11-02` na raiz);
4. Espelhamento GitHub (2026-08-19): repo privado sincronizado; commit `03536d8`.

---

# PARTE 11 — PENDÊNCIAS E PRÓXIMOS PASSOS

## 11.1 Urgente
1. Retomar palestras novas quando o curador fornecer material-fonte: **Faces de Javé** (P2024-02-25), **Jesus e a Dinastia das Sophias** (P2025-07-25) — ambas "material-fonte ausente";
2. Regenerar o **Mapa do Buraco Negro Javé** (SEGURADO — aguardando mais palestras);
3. Revisar apostilas concluídas com o curador.

## 11.2 Curadoria do usuário (termos candidatos ⚪)
Revisar candidatos pendentes; aprovar/rejeitar via Devolutiva.

## 11.3 Divergências de datas (resolver com fontes primárias)
- "4.261 a.C." (alfabeto de Thot); "20171" (colapso Trimurti); Kybalion (1900 × 1908); colapso de Javé (2021).

## 11.4 Livros sem PDF (aguardando)
Bibliografia completa em BIBLIO; PDFs de livros adicionais pendentes.

## 11.5 Grafias a reconciliar (Colecionar Incertezas)
- "quachadas/quechada" (= Keshava? — pista do curador); "Hen Orl"; "Prima Sai"; "Quinara"; "demo hesitante"; "Hainarok" (= Ragnarök); "Osamaro Ibier"; "Sinal de Lel" (= "O Sinal de Lemur"?); "Paul Hiller"; "Tubaral"; "imoléis"; "Vaius".

---

# PARTE 12 — INSTRUÇÕES PARA O NOVO AGENTE

## 12.1 O Prompt Inicial (materializado)

**Leia o `prompts/PROMPT-INICIAL-DO-AGENTE.md`** — contém o prompt a colar no chat + a ordem de anexação + as regras de ouro. O essencial:

> Autoridade do curador; estado canônico (767/1531/RC-768/13 apostilas); fluxo em 2 ciclos (Curadoria Base-first + Apostilas em Lote); regras de ouro (não inventar, quarentenas, grafias, voz do Ellam); fontes (GitHub ou pacotes); primeira ação (validar → ler docs → resumir → aguardar).

## 12.2 Como montar o workspace

1. **Fonte A (GitHub):** `git clone https://x-access-token:TOKEN@github.com/institutocura-maker/Termos-RC.git` (token fornecido pelo curador);
   **Fonte B (pacotes):** restaurar de `reconstrucao/pacotes/` via `restaurar_pacotes.py` (ou do ZIP `PACOTE-DE-ORIGINAIS-2026-08-18.zip.txt`);
2. Validar: `python3 ferramentas/dados_termos.py` → `OK: 767 termos, 1531 relações — dados válidos.`;
3. Ler na ordem: `GUIA-MESTRE-RC-APOSTILA.txt` (v1.1) → `prompts/PROMPT-INICIAL-DO-AGENTE.md` → `admin/logs/PACOTE-MIGRACAO-CHAT-2026-08-18.md` → `PLANO-MIGRACAO-DE-CHAT.md` → `convencoes-editoriais-rc.md`;
4. Resumir ao curador o estado + próximo passo + pendências; aguardar confirmação.

## 12.3 Por onde começar (prioridade)

1. Se o curador fornecer nova palestra TXT → Ciclo de Curadoria (Parte 4.1);
2. Se houver palestras com Dossiê+Devolutiva sem apostila → Ciclo de Apostilas em Lote (Parte 4.2);
3. Se nada disso → revisar pendências (Parte 11) e aguardar orientação.

## 12.4 Regras de ouro para o agente

1. O curador manda; você sugere;
2. Não inventar, não completar, não interpolar → `[REVISAR]`/`[TEXTO INCOMPLETO]`;
3. Falas da plateia nunca viram ontologia;
4. Quarentenas: clínico, político, ufológico, teológico, STT — leitura do autor;
5. Grafias canônicas (Parte 6.10);
6. Todo ciclo termina com `gerar_pacotes.py` + admin/logs/CONTINUIDADE.md;
7. O GitHub é espelho; o local é a fonte primária;
8. Só interrompa o curador por ambiguidade realmente impeditiva.

---

> **Fim do Guia-Mestre v1.1 (2026-08-19).** Para contagens atuais, prevalece `ferramentas/dados_termos.py`. Última sincronização GitHub: `03536d8`.
