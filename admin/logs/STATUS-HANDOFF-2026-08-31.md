# STATUS-HANDOFF — Termos-RC (2026-08-31)

> **Documento de handoff para continuação em outro chat.**
> **Curado por:** Arena.ai Agent Mode (MiniMax-M3)
> **Data:** 2026-08-31
> **HEAD do branch:** `27ad59f`
> **Tamanho do repo:** 27.2 MB / ~7.1M tokens (NÃO cabe em uma única janela de contexto)

---

## 🎯 Onde Estamos

**Branch:** `arena/01a04eee-termos-rc`
**HEAD:** `27ad59f` (sincronizado com `origin/arena/01a04eee-termos-rc`)
**Working tree:** LIMPO (nenhuma modificação pendente)

**Repositório:** [institutocura-maker/Termos-RC](https://github.com/institutocura-maker/Termos-RC)
**Plataforma:** GitHub
**Workflow:** o usuário sobe arquivos de palestra no `uploads_recepcao/`, o agente processa para `apostilas/CONCLUIDAS/`, cria fichas em `termos/`, atualiza `INVENTARIO-APOSTILAS.json` e `INDICE-PALESTRAS.md`, commita + push.

---

## 📊 Números Atuais (2026-08-31)

| Item | Valor |
|---|---|
| **Pastas v3.1-MP em CONCLUIDAS** | **80** |
| **Total de termos (RC)** | **524 arquivos .md** (RC-001 a RC-835) |
| **Uploads em `uploads_recepcao/`** | 42 .txt + 11 metadados = 53 arquivos |
| **Limpezas registradas** | 10 (REGISTRO-LIMPEZA-2026-08-30-{1..10}.json) |
| **Tamanho total (working tree, sem .git)** | 27.2 MB |
| **Estimativa de tokens** | ~7.1M tokens |

---

## 🏛️ Arquitetura do Repositório

```
/home/user/Termos-RC/
├── apostilas/
│   └── CONCLUIDAS/                          # 80 pastas, uma por palestra
│       ├── AAAA-MM-DD_slug/
│       │   ├── apostila.md                  # Apostila v3.1-MP (~30KB, RAG-optimal)
│       │   ├── README.md                    # Metadata da palestra
│       │   └── original.txt                 # STT bruto (preservado, NÃO modificar)
│       └── ...
├── termos/                                  # 524 fichas RC (.md)
│   ├── RC-001-jave.md                       # Javé (Brama)
│   ├── RC-002-rebeliao-de-lucifer.md        # Lúcifer
│   ├── ...
│   ├── RC-009-sophia-cristo-cosmico.md      # Sophia (grafia CANÔNICA)
│   ├── RC-037-brahma-brajna.md              # Brahma (grafia CANÔNICA)
│   ├── RC-078-lucifer-yel-luzbel.md         # Lúcifer / Yel Luzbel
│   ├── RC-142-yel-luzbel.md                 # Yel Luzbel (remissão)
│   ├── RC-806-desvio-de-rota-de-pandora.md
│   ├── ...
│   └── RC-835-familia-aye.md                # Aye (recém-criada 2026-08-31)
├── uploads_recepcao/                        # Canal de entrada de palestras
│   ├── 2023-12-17 Lúcifer e a Rebelião dos Elétrons.txt
│   ├── ... (42 arquivos .txt)
│   ├── README.md                            # Política de uso
│   └── REGISTRO-LIMPEZA-2026-08-30-{1..10}.json
├── ciclos/                                  # Sistema paralelo de ciclos leves
│   ├── P2023-12-03/
│   │   ├── ciclo.toml
│   │   ├── original.txt
│   │   └── pacote_P2023-12-03.txt
│   └── P2023-12-17/                         # ⚠️ ciclo leve, mas REPROCESSADO
│       ├── ciclo.toml
│       ├── original.txt
│       └── pacote_P2023-12-17.txt
├── ferramentas/
│   └── motor.py                             # Sistema de andaime (ciclos)
├── INVENTARIO-APOSTILAS.json                # 80 pastas + metadados (md_size, orig_size, n_rc, is_v31_mp)
├── INDICE-PALESTRAS.md                      # 51 linhas, lista de todas as palestras processadas
├── README.md                                # README raiz
├── REGISTRO-ANOMALIA-REBASE-2026-08-31.md   # ⚠️ Documenta anomalia de rebase do dia 31/08
└── STATUS-HANDOFF-2026-08-31.md             # ESTE ARQUIVO
```

---

## 📐 Regras do Agente (LEIA ANTES DE PROCESSAR)

### 1. **TERMINOLOGIA CANÔNICA** (regra crítica — aprendida em 2026-08-31)

**SEMPRE** use as grafias canônicas das fichas existentes. **NUNCA** use variantes informais.

| Termo canônico | Variações REJEITADAS | RC canônica |
|---|---|---|
| **Sophia** | "Sofia" | RC-009 |
| **Yel Luzbel** | "Luzbel" sozinho, "Yosbel", "Luzbell" | RC-078/RC-142 |
| **Brahma** | "Brama" | RC-037 |
| **Aya** | "Aia" | RC-834 (remissão) |
| **Aye** | "Aie" | RC-835 (remissão) |
| **Pirra** | "Pirra" (RC-303), "Birra" (STT) | RC-303 |
| **Epimeteu** | "Pimeteu" (STT) | RC-271 |
| **Prometeu** | "Prometeu" | RC-270 |

**Ao processar uma nova palestra:**
1. Ler o `original.txt` extraído via `git cat-file -p <blob>`
2. Listar entidades mencionadas
3. Para cada entidade, verificar a grafia canônica em `termos/RC-XXX-*.md`
4. Se não existir ficha canônica, criar como "remissão" para a palestra canônica
5. Adicionar seção "Quarentena Terminológica" em cada ficha nova

### 2. **WORKFLOW DE PROCESSAMENTO**

```bash
# 1. Fetch
git fetch origin refs/heads/arena/01a04eee-termos-rc:refs/remotes/origin/arena/01a04eee-termos-rc

# 2. Localizar o blob da palestra no commit de upload
git ls-tree origin/arena/01a04eee-termos-rc --name-only | grep "uploads_recepcao/AAA-MM-DD"

# 3. Pull --rebase
git pull --rebase origin arena/01a04eee-termos-rc

# 4. Criar pasta
mkdir -p "apostilas/CONCLUIDAS/AAAA-MM-DD_slug"

# 5. Extrair original.txt
git cat-file -p <blob> > "apostilas/CONCLUIDAS/AAAA-MM-DD_slug/original.txt"

# 6. Análise estrutural (5 PARTES, U0001..U0005)

# 7. Dedup dos conceitos novos contra 524 RC

# 8. write_file apostila.md (v3.1-MP, ~30KB)

# 9. write_file README.md da pasta

# 10. Atualizar INVENTARIO-APOSTILAS.json (Python script)

# 11. Atualizar INDICE-PALESTRAS.md (cat >>)

# 12. write_file das fichas novas em termos/RC-XXX-*.md

# 13. REGISTRO-LIMPEZA-N.json em uploads_recepcao/

# 14. git add paths explícitos + commit + push (NUNCA `git stash -u`!)
```

### 3. **FORMATO v3.1-MP (RAG-optimal, machine-parseable)**

Toda `apostila.md` deve ter estas seções:

```markdown
# Título da Palestra — PAAMM-DD (v3.1-MP)

> [Metadados básicos]

## @metadata          # ID, data, título, duração, companions, n_conceitos, RC referenciadas
## @tese              # Tese central (1-2 parágrafos)
## @datas             # Tabela cronológica
## @autoridade_leitura  # Fato vs leitura do autor
## @glossario         # Personagens, conceitos, lugares, eventos, espécies
## @spans (5 PARTES)  # U0001 a U0005
## @conceitos_novos   # C-1 a C-N (cada um com definição, fontes, RC, observações)
## @quarentenas       # Crítica, demonológica, teológica, social, metodológica
## @estrutura_palestra  # Duração, gênero, tom
## @conexoes_outras_palestras
## @observacoes_curatoria
## @proximos_passos
## @quarentena_terminologica  # ← SEMPRE incluir (fix 2026-08-31)
```

### 4. **FORMATO DE FICHA RC**

```markdown
# Título Canônico — RC-XXX

| Campo | Valor |
|---|---|
| Categoria Principal | [SERES & ENTIDADES / EVENTOS & ERAS / etc] |
| Subcategoria | [...] |
| Status | [⚪ candidato / 🟡 Provisório / 🟢 Definitivo] |
| Última atualização | AAAA-MM-DD |

## Definição Sintética
[1-2 parágrafos]

## Contexto / Origem
[Aparece em qual palestra, qual span]

## Etimologia / Grafias
- Grafia preferida: [CANÔNICA]
- Variações STT capturadas: [...]
- Idioma de origem: [...]

## Fontes
| Obra | Capítulo | Página | Tipo |
|---|---|---|---|

## Citações-chave
> [aspas literais da palestra]

## Termos Relacionados
| Termo | Código | Tipo de relação |
|---|---|---|

## Seres Associados
- [quem]

## Observações
- [REVISAR se algo precisa revisão]
- Quarentena: [...]

## Quarentena Terminológica
[Lista de grafias canônicas — SEMPRE incluir]
```

### 5. **PROMESSA: SEMPRE DELETAR O UPLOAD PROCESSADO**

Ao processar uma palestra, **SEMPRE deletar o arquivo correspondente em `uploads_recepcao/`** (mas só esse, não os outros). Isso é feito via `git rm` + commit.

**ANOMALIA CONHECIDA (2026-08-31):** o branch atual tem **41 duplicatas** em `uploads_recepcao/` que **deveriam ter sido deletadas** pelos commits `c2d838dd` (P2019-05-11) e `c11976e` (P2023-11-11) do curador anterior, mas ficaram em "unreachable" após rebase. Ver `REGISTRO-ANOMALIA-REBASE-2026-08-31.md`. **NÃO** deletar essas 41 (opção C do usuário — documentar e seguir).

---

## 🎯 Tarefas Pendentes / Próximas Ações

### Pendências Imediatas
- [ ] **PROCESSAR próxima palestra** que o usuário subir no `uploads_recepcao/`
- [ ] Aguardar o usuário dizer qual palestra processar

### Backlog de Manutenção (NÃO é para fazer agora — só se o usuário pedir)
- [ ] Limpar 41 duplicatas em `uploads_recepcao/` (Opção A da anomalia — bloqueada pelo usuário)
- [ ] Renomear outros arquivos com grafias erradas (ver `REGISTRO-ANOMALIA-REBASE-2026-08-31.md`)

### Tarefas de Longo Prazo
- [ ] Processar as 41 palestras "duplicadas" (que JÁ estão em CONCLUIDAS, mas que aparecem também em uploads_recepcao/) — não há o que fazer, só documentar

---

## 📚 Como Continuar em Outro Chat

Para retomar o trabalho em outra sessão:

1. **Abra um novo chat** com o agente (Arena.ai Agent Mode / MiniMax-M3)
2. **Copie e cole** este documento inteiro (`STATUS-HANDOFF-2026-08-31.md`)
3. **Mencione o branch:** `arena/01a04eee-termos-rc`
4. **Mencione o HEAD:** `27ad59f`
5. **Peça a próxima ação** (ex: "processe a próxima palestra que eu subir")

O agente deve:
1. Verificar que está no branch certo
2. Verificar que o HEAD local = HEAD remoto
3. Pedir o nome do arquivo que você quer processar
4. Aplicar o workflow da seção "WORKFLOW DE PROCESSAMENTO"

---

## 🗓️ Histórico Recente (últimos 5 commits)

```
27ad59f fix(P2023-12-17): TERMINOLOGIA CANONICA - 158 substituicoes + 2 RC remissoes (Aya/Aye)
d21f0bb docs: REGISTRO-ANOMALIA-REBASE-2026-08-31 — uploads_recepcao/ com 41 duplicatas
9c02f5d feat(P2023-12-17): Lúcifer e a Rebelião dos Elétrons (REPROCESSADO como apostila)
4dab46d feat(P2019-04-14): Javé versus Pandora A Prole sem Face — 7 RC-819 a RC-825
b4c4559 feat(P2018-05-20): De Pandora a Eva e o Culto a Lilith — 6 RC-813 a RC-818
```

---

## 🔍 Arquivos Auxiliares (junto com este)

1. **`GLOSSARIO-CANONICO-2026-08-31.md`** — Lista de TODAS as 524 RC + 80 pastas com grafias canônicas (~30KB)
2. **`../../docs/historico/INVENTARIO-COMPACTO-2026-08-31.md`** — Versão compacta do INVENTARIO-APOSTILAS.json (~12KB)
3. **`../../docs/historico/INDICE-ARQUIVOS-RAIZ-2026-08-31.md`** — Ponteiro "qual arquivo usar pra quê" (~10KB) — resolve a pergunta sobre CONTINUIDADE.md (343KB) e ../../prompts/PROMPT-INICIAL-DO-AGENTE.md (4.6KB, histórico)

Todos estão commitados no branch `arena/01a04eee-termos-rc` na raiz do repositório.

---

**Curador:** Arena.ai Agent Mode (MiniMax-M3)
**Última atualização:** 2026-08-31
**Versão do schema:** 3.1-MP (RAG-optimal, machine-parseable)
