# PROMPT DE CONTINUAÇÃO — FASE 1 · B019 *Nem Deus, nem Javé, nem Darwin* (A Evolução Possível)

**Gerado em:** 2026-08-23 · Agente RC (Arena) · Branch de sessão: `arena/01a02a88-termos-rc`
**Para:** qualquer nova sessão do Agente Base-first (ou o Assistente do curador) retomar o reprocessamento do B019 exatamente de onde ele parou, sem depender de janela de contexto anterior.

> **Leia primeiro:** `CHECKPOINT-SESSAO-2026-08-21.md` (seção "ATUALIZAÇÃO 2026-08-22/23 — FASE 1 B019") + seção "Fase 1 — B019" do `CONTINUIDADE.md` + `livros/B019_nem-deus-nem-jave-nem-darwin/analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`.

---

## 1. ESTADO CANÔNICO (validar ao retomar)

```text
Base: 777 termos (RC-001–RC-777) · 1.852 relações · 428 fichas físicas (427 canônicas + RC-004)
Próximo código disponível: RC-778
Obras: 86 (B001–B083 + ART-2025-08-01/02/03) · 37 apostilas em CONCLUIDAS
B019: PDF byte a byte + texto_integral + camadas 0–3 + 52 chunks + LEITURA-1 + LEITURA-2 + DOSSIE v1 — TUDO COMMITADO
KB INTOCADA pela FASE 1 até a Devolutiva (regra de ouro).
Validação: python3 ferramentas/dados_termos.py → "OK: 777 termos, 1852 relações — dados válidos."
```

## 2. O QUE JÁ FOI FEITO (FASE 1 B019 — cronologia de commits)

| Commit | Ciclo |
|---|---|
| `6b3b72c` | INGRESSO: PDF do curador (GitHub `d197e1c`) → `livros/B019_.../original.pdf` (1.808.075 b · SHA `0fa27f54…de583051`) · 238 págs · nascido-digital · `analise/texto_integral.txt` (502.610 chars · 80.493 palavras) · mapa 18 capítulos + posfácio + 60+ notas · gerador de pacotes BINÁRIO-SEGURO + pacote cobre `livros/` |
| `e9faedf` | LACUNA 2024-05-04 FECHADA: `original.pdf` da Prabrajna em Perpérion corrompido na migração antiga (142.138 U+FFFD) → re-anexado pelo curador (GitHub `6a95cdf`) → substituído byte a byte (368.728 b · SHA `cee4ef97…dd596` · 38/38 págs idênticas ao backup textual + round-trip 0 U+FFFD) |
| `31789cc` + `9d09a46` | **LEITURA-1-MACROESTRUTURA.md COMPLETA (p. 1–238)**: TESE GERAL DO LIVRO no topo (8 etapas do "reparo de baixo para cima") + 60+ notas por capítulo com páginas verificadas (RC: 3 estágios; Daath="Abismo de Luz"; Quarto Logos=Olm; Reintegração Cósmica="apresentação oficial de Sophia com suas naves"; Biocosmos Inteligente=Gardner [externo]; Espíritos Codificadores=kardecista; buraco branco→Big Bang; Mentalma VI/VII; 28.869 genes; B040 sob nome real; bibliográfico Conectar/Natal) |
| `14817c4` + `31b48da` | **LEITURA-2-TERMINOLOGICA.md** (seções A–H: 20 citações auditadas; ~50 termos corroborados; 40 candidatos a novo termo [10 alta/20 média/10 Ockham]; 20 variações de grafia; 9 quarentenas; 11 itens bibliográficos; 20 inconsistências internas; 20 pontos sensíveis) com **47 correções de página verificadas no livro** + **DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md** (O-1..O-10 + N1..N18) + camadas 0–3 + 52 chunks |
| `b3e8ba8` | Typo fix (`alicerccar`→`alicerçar`) + pacotes **BINÁRIO-SEGURO round-trip 568/568 100% fiéis** + LACUNA 2024-05-04 nos pacotes/backup |

**Artefatos B019 (todos em `livros/B019_nem-deus-nem-jave-nem-darwin/`):** `original.pdf` · `ficha_ingresso.md` · `analise/{texto_integral.txt, METADADOS-INGRESSO.json, camada-0..3.txt, leitura/chunk-01..52.txt, LEITURA-1-MACROESTRUTURA.md, LEITURA-2-TERMINOLOGICA.md, DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md, _corrigir_leitura2_2026-08-22.py}`.

## 3. O QUE FALTA (o ÚNICO pendente do fluxo FASE-1)

**DEVOLUTIVA DO CURADOR** sobre o DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1 (documentos: "nenhuma decisão ontológica aqui — nada é consumido antes da devolutiva"):

1. **O-1..O-10** (Seção 5 do DOSSIE — tensões/itens sensíveis): harmonizar RC-604 × B019 p. 198 ("2 Espíritos × 3 Seres" vs. "fatiamento = um espírito"); Mente Cósmica (novo código ou fundição RC-163/RC-615); Espíritos Codificadores (novo ou anotação em RC-190); RC-216 (enquadramento "homenagem frustrada à Deidade"); figuras Kapila/Buda/Pan Ku/Patanjali (termo-figura ou referência externa?); grafia canônica "Consórcio de Mundos × Consórcio Cósmico" (RC-538) e "Cúpula Diretiva Universal × Cúpula Governamental"; 28.869 genes (atualizar Colecionar Incertezas); novas grafias do livro; "Projeto Talm" = RC-091/B045; "Código digitalizado" (variação de CFD/CFDP/TALM?);
2. **N1..N18** (Seção 4 — candidatos a NOVO CÓDIGO, a partir de RC-778): 10 prioridade alta (Buraco Branco; Ponte Quântica; Causação Descendente; Mente Cósmica; Espíritos Codificadores; Revelação em 3 Estágios; Semeadores; Cúpula Diretiva Universal; Coração Espiritual; Hibernação Vibratória) + 8 média (Kapila; Sidarta/Buda; Pan Ku; Patanjali; Código Digitalizado; Síndrome de Estrangeiro; Seres-cientistas; "Jogo da Vida"/"Jogo das Mutações") — cada um com página(s) e cruzamentos no DOSSIE;
3. **Ampliações dos 20 termos existentes que citam B019** (Seção 2 — bloco RC-538–547 + 12 pré-existentes) com as páginas verificadas do livro;
4. **11 itens bibliográficos** (LEITURA-2 §F): editora Conectar/Natal + anos (B001 2010/B002 2011/B033 2012/B048 2013/B016 2017/B041 2019/B049 2019/B024 2020); Mentalma VI/VII; obras ausentes (Big Data do Criador/Nos Céus da Grécia); B040 sob nome real; B030 coautoria José Renan de Medeiros; Manifestos Orbum/Onda Vírus [quarentena política];
5. **15 itens Colecionar Incertezas** (Seção 7) — registro, não ontologia.

## 4. PLANO DE EXECUÇÃO (quando a Devolutiva chegar)

1. Registrar a Devolutiva em `CONTINUIDADE.md` (seção FASE 1 B019) — transcrever as decisões O-1..O-10/N1..N18;
2. **Ampliações** dos 20 termos (Seção 2 do DOSSIE) + os termos corroborados que o curador aprovar → método padrão: `_ampliacoes_B019_<data>.txt` + `_aplicar_ampliacoes_B019_<data>.py` (ou edição manual das fichas, padrão das re-curadorias);
3. **Novos códigos** (se aprovados): a partir de **RC-778**, com ficha física (padrão `01-ficha-modelo.md`) + categoria do vocabulário controlado;
4. **Relações novas** na tabela-mestra (`ferramentas/dados_termos.py` — fonte única; backup pré-ciclo em `reconstrucao/backups/`);
5. **Regenerar artefatos:** `python3 ferramentas/build_indice.py` → `build_xlsx.py` → `build_word.py`;
6. **Pacotes + backup:** `python3 ferramentas/gerar_pacotes.py` → verificação de fidelidade `python3 ferramentas/verificar_pacotes.py` (não-destrutiva; 569 arquivos) → atualizar `backups/pacotes/`;
7. **Documentar:** CONTINUIDADE (seção do ciclo) + CHECKPOINT-SESSAO (cronologia + estado canônico) + índices;
8. **Commit + push** em `arena/01a02a88-termos-rc` (mensagens no padrão do projeto: `FASE-1 B019 <o que mudou>`);
9. **Entrega final do piloto:** a FASE 1 B019 fecha quando a Devolutiva for consumida — então o curador decide a FASE 2 (candidatas B011/B040) e se o B019 gera apostila/tratado temático.

## 5. COMO RETOMAR (procedimento padrão)

1. `cd /tmp && git clone https://x-access-token:${GH_TOKEN}@github.com/institutocura-maker/Termos-RC.git` (token no ambiente; nunca salvar em arquivo) **OU** usar o workspace já clonado (branch `arena/01a02a88-termos-rc` já contém tudo);
2. `python3 ferramentas/dados_termos.py` → esperar `OK: 777 termos, 1852 relações — dados válidos.`;
3. Ler: `CHECKPOINT-SESSAO-2026-08-21.md` → este prompt → seção "Fase 1 — B019" do `CONTINUIDADE.md` → `DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`;
4. Verificar o upload do curador em `main` (novos PDFs/decisões chegam por lá: `git fetch origin main && git log HEAD..origin/main --oneline`);
5. **NÃO tocar na KB (dados_termos.py) antes da Devolutiva.**

## 6. REGRAS DE OURO (recordatório)

- Curador = autoridade máxima; nada é consumido sem Devolutiva; quase sempre ZERO códigos novos (Navalha de Ockham) — exceções só com aprovação explícita;
- Não inventar/não completar/não interpolar → `[REVISAR]`/`[NÃO REVELADO]`; falas da plateia nunca viram ontologia;
- Quarentenas ativas no B019 (DOSSIE §6): externa/filosófica (Heidegger, Nietzsche, Kant...); externa/científica (Goswami, Sheldrake, Diamond, Sattinover, Gardner...); clínica/biológica (CMV, metilação, Tay-Sachs, oxitocina, 28.869 genes, 97/3/2%); teológica; ufológica; política (Orbum/IEPP); gênero; histórico/alternativo; parapsicologia — tudo "leitura de Ellam", nunca ontologia;
- A cada ciclo: validar → executar → regenerar artefatos → pacotes + `backups/pacotes/` → CONTINUIDADE/CHECKPOINT → push;
- Grafias canônicas vigem (Brahma, Tikun, Sophia, Javé, Vishnu, Olm, Moros, Kapila, Patanjali, Prabrajna, Mavatma...).

## 7. ARQUIVOS-CHAVE

| Arquivo | Função |
|---|---|
| `livros/B019_nem-deus-nem-jave-nem-darwin/analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md` | **O documento que aguarda a Devolutiva** (O-1..O-10 + N1..N18) |
| `livros/B019_nem-deus-nem-jave-nem-darwin/analise/LEITURA-1-MACROESTRUTURA.md` | Leitura integral p. 1–238 (TESE GERAL + 60+ notas paginadas) |
| `livros/B019_nem-deus-nem-jave-nem-darwin/analise/LEITURA-2-TERMINOLOGICA.md` | Cruzamento termo a termo (seções A–H, 47 correções de página) |
| `livros/B019_nem-deus-nem-jave-nem-darwin/analise/texto_integral.txt` | Texto do livro com marcadores `=== PAG N ===` (fonte para reler qualquer citação) |
| `livros/B019_nem-deus-nem-jave-nem-darwin/analise/leitura/chunk-01..52.txt` | Chunks da leitura (faixas ~9.000 chars) |
| `ferramentas/dados_termos.py` | Tabela-mestra — fonte única de verdade (NÃO tocar antes da Devolutiva) |
| `ferramentas/gerar_pacotes.py` / `restaurar_pacotes.py` / `verificar_pacotes.py` | Pacotes binário-seguros (verificação não-destrutiva 569/569) |
| `CHECKPOINT-SESSAO-2026-08-21.md` / `CONTINUIDADE.md` | Estado canônico + histórico |
| `backups/pacotes/` | Cópia versionada dos pacotes (atualizar a cada ciclo) |
| `pedagogico/DOSSIE-AUDITORIA-LACUNAS-FASE-0.md` | Dossiê da FASE 0 (lista de obras para a FASE 2) |

---

**Resumo em uma frase:** *FASE 1 B019 está com toda a matéria-prima e as duas leituras + dossiê prontos e commitados; a base segue em 777/1.852 intacta; o fluxo está travado apenas na Devolutiva do curador (O-1..O-10 + N1..N18) — quando ela chegar, executar o plano da seção 4 e fechar o piloto.*
