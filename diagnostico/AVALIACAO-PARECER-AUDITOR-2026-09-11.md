# Avaliação do Parecer de Auditoria — 11/09/2026

**Objeto:** `uploads_recepcao/📋 Parecer de Auditoria.docx` (primeira conversa Curador ↔ Assistente Auditor).
**Método:** extração integral do texto (92 parágrafos + 2 tabelas) + checagem de cada afirmação factual contra o repositório + avaliação técnica de cada recomendação **sob as restrições reais desta plataforma** (sandbox sem serviços persistentes, só-stdlib, Curador baixa espelhos pelo GitHub).
**Veredito em uma frase:** parecer bem estruturado e com ~80% de convergência com nosso §9 — mas com **3 erros factuais** que distorcem prioridades, e recomendações que precisam de adaptação à plataforma antes de executar.

---

## A. Checagem factual (afirmação → valor real → veredito)

| # | Afirmação do auditor | Valor verificado no repo | Veredito |
|---|---|---|---|
| 1 | "~797 commits" (citado 3×) | **131 commits** (`git log --oneline \| wc -l`) | ❌ ERRO GRAVE — contamina o risco #4 |
| 2 | Binários acumularam "dezenas ou centenas de MB" no histórico | **16,3 MB** (xlsx+docx em 57 commits, sem compressão; `.git` total = 210 MB) | ❌ Ordem de grandeza errada |
| 3 | Maior bloat = diffs binários dos espelhos | Maiores blobs: `backups/pacotes/*.txt` (5,2 MB), PDFs B050/B031 (~4 MB cada) | ❌ Mira errada — o bloat real é `backups/` + PDFs |
| 4 | README mostra 760 termos (ago/2026), desatualizado | Confirmado (760 termos, 340 fichas) | ✅ Correto… |
| 5 | …mas ignora que o README está marcado | Linha 3: "**⚠️ ARQUIVO HISTÓRICO** (revisão 2026-08-25)" | ⚠️ Nuance perdida — problema real é a *ausência* de README vivo, não desinformação ativa |
| 6 | README referencia branch `arena/01a07777` | `grep -c` = **0 ocorrências** | ❌ Não existe neste estado do repo |
| 7 | "649 verbetes" | **659** arquivos `.md` na enciclopédia | ⚠️ ~1,5% off — irrelevante |
| 8 | Recomenda `.gitignore` p/ binários (assume inexistente) | `.gitignore` **existe**, com `*.docx/*.xlsx` *deliberadamente comentados* ("deixe comentado") | ❌ Ignora decisão consciente + workflow do Curador |
| 9 | 100 vídeos × 20 min ≈ 33h | 2.000 min = 33,3h | ✅ Correto |

**Origem provável do "797":** desconhecida (não corresponde a commits, fichas, arquivos ou linhas de nenhum artefato óbvio). Ponto a devolver ao auditor.

## B. Avaliação dos 10 riscos (com severidade recalibrada)

**R1. `dados_termos.py` como BD — CRÍTICO → ✅ MANTIDO.** Diagnóstico correto nos 4 subproblemas (tupla posicional, escrita por regex, sem FK, sem consultas). **Ressalva de plataforma no plano F1–F5:** F1 (JSON Schema) pressupõe a lib `jsonschema`, que **não é stdlib** — `pip install` some entre turnos aqui, então o validador teria de ser hand-rolled. Alternativa nativa: SQLite (stdlib, testado: 3.40.1) com `CHECK`/`UNIQUE`/FKs — ou seja, o F5 do auditor antes do F1. F2 (exportador JSON) ✅ zero-risco, consensual. F3–F4 sensatos como transição.

**R2. README desatualizado — ALTO → ⬇️ MÉDIO.** É arquivo histórico sinalizado; ninguém é enganado ativamente. Mas a recomendação é ótima: **README vivo gerado do STATE-MIRROR** ✅ (entra nos quick wins).

**R3. Status duplicado — ALTO → ✅ MANTIDO, com refinamento.** "Status lido, não escrito" é o ideal final — mas a badge hardcoded tem função *hoje*: o Curador lê fichas standalone no GitHub. Remoção pura piora a leitura humana. Refinamento: manter badge + **teste de consistência como portão** (censo: hoje 100% sincronizado — o teste só impede regressão), migrando para injeção em build quando houver frontmatter.

**R4. Binários no git — MÉDIO-ALTO → ⬇️ BAIXO-MÉDIO.** 16 MB não é crise; o bloat real (`.git` 210 MB) vem de `backups/pacotes/` + PDFs. E `gitignore` sem substituto **quebra o workflow do Curador** (ele baixa os espelhos pelo repo). Sequência correta: (1) canal alternativo de distribuição (Release/Actions — a se montar); (2) só então ignorar; (3) antes de tudo, política de retenção p/ `backups/` (o txt de 5,2 MB sozinho pesa 1/3 de todo o histórico dos espelhos).

**R5. Rebuilds totais — MÉDIO → ✅ MANTIDO, com ceticismo de timing.** Hoje ~1 min; incremental com hash-store = complexidade + estado novo para ganho futuro. Proposta: definir **gatilho objetivo** (ex.: rebuild > 3 min) e só então implementar. Medir antes de otimizar.

**R6. Sem testes — MÉDIO → ⬆️ P1/QUICK WIN.** É o item mais barato e mais protetivo contra o R1 *hoje*, 100% stdlib (`unittest`). Os 5 checks propostos estão corretos; acrescentar: (6) badge↔cadastro; (7) tabela `## Fontes` bemformada (censo: **27,4% quebradas**); (8) `ficha=True` sem seções mínimas. Deveria ser o primeiro commit pós-auditoria.

**R7. Raiz com ~50 docs — MÉDIO → ✅ MANTIDO.** Direção correta (`docs/historico/`); pré-requisito: **inventário de links cruzados** antes de mover (docs se referenciam; `INDICE-ARQUIVOS-RAIZ` precisa migrar junto). Caso contrário, move-se o caos com links quebrados.

**R8. Parsing por regex — MÉDIO → ✅ MANTIDO, com troca de dependência.** `mistune`/`markdown-it` = pip = frágil aqui; YAML frontmatter = `pyyaml` = pip também. Alternativa nativa: **frontmatter TOML** (`tomllib` é stdlib desde 3.11; sandbox roda 3.11.2 ✅). Mesma arquitetura, zero dependência.

**R9. STT como fonte — BAIXO-MÉDIO → ✅ MANTIDO.** `confianca_fonte` (alto/médio/baixo) é excelente ideia — e é, ironicamente, **mais um argumento pelo R1**: campo novo exige schema, que exige a migração. Ínterim viável: convenção em `## Observações` até o schema existir.

**R10. Legados/retenção — BAIXO → ✅ MANTIDO.** `ferramentas/legacy/` + README ✅; retenção 90 dias p/ backups ✅ (e resolve parte do R4 real).

## C. Plano YouTube (100 vídeos) — avaliação

Pipeline proposto (transcrição → pré-filtro → lotes de 10–15 → CSV de chancela) é **sólido e compatível** com o Anel A/B/C; o mapeamento A=fonte/B=verbatim/C=códigos-novos com sigla `V`/`Y` é elegante. Quatro ressalvas:

1. **"Posso acessar transcrições do YouTube"** é afirmação sobre a plataforma *dele* — não verificável daqui. Nesta plataforma, precisaríamos de links + teste de transcrição antes de assumir.
2. **Sigla nova (`V`/`Y`) é decisão canônica**, não detalhe: propaga para `02-vocabulario-controlado.md`, parsers (`[BP]` regex no P6a!), builders e STATE-MIRROR. Exige despacho formal.
3. **Onde moram os vídeos?** O repo não comporta 33h de mídia — só transcrições + metadados + links. Precisa de política de armazenamento externo.
4. `confianca_fonte=baixo` default ✅ — coerente com R9.

## D. Ideias de futuro — triagem por viabilidade nesta plataforma

| Ideia | Viabilidade aqui | Comentário |
|---|---|---|
| API FastAPI/Flask | ❌ Sandbox / ✅ Curador local | Sem serviços persistentes entre sessões; só como projeto local do Curador |
| Grafo D3.js das 1.898 relações | ✅ Alta | HTML estático gerado pelo build — entrega real sem servidor |
| Busca full-text (SQLite FTS5) | ✅ Alta — **quick win oculto** | Testado: **FTS5 funciona na stdlib daqui**. Indexar 671 fichas + 659 verbetes é um script só |
| Versionamento semântico | ✅ Processo | Convive com P6/P7 (fases ≠ releases); changelog gerado das levas é trivial |
| CI (GitHub Action) | ✅ Alta | Validador + suite pós-push como alarme; barato e independente de plataforma |

## E. O que o auditor NÃO viu (nossos achados exclusivos)

1. **Censo das fichas** (`diagnostico/CENSO-CONFORMIDADE-FICHAS-2026-09-11.md`): modelo v2 é ficção normativa (47% sem Citações-chave), 27% das Fontes quebradas, 2.323 blocos acumulados, conteúdo que nenhum build consome — ele auditou o cadastro, não as fichas.
2. O `.gitignore` consciente e o workflow de distribuição dos espelhos.
3. O bloat real (`backups/` + PDFs) vs. o bloat imaginado (espelhos).
4. Restrições da plataforma de execução (só-stdlib) — natural, ele audita o repo, não o sandbox.

## F. Encaminhamento recomendado

1. **Devolver ao auditor** os 3 erros factuais (797 commits, MBs binários, branch/README) + nosso censo de fichas — ele merece auditar as fichas também.
2. **Quick wins consensuais** (pós-alinhamento): test-suite P1 (#6+7 checks) → README vivo gerado → exportador JSON F2 → FTS5 experimental.
3. **Decisões que só o Curador toma:** JSON-primeiro (auditor) × SQLite-primeiro (nossa contraproposta) — tecnicamente empatados, desempatam por manutenção; sigla `V`/`Y`; canal de distribuição dos espelhos.
4. **Não executar ainda:** F3–F5, builds incrementais, remoção de badges, `gitignore` em binários.

---

*Parecer sobre o parecer, lavrado pelo agente de engenharia em 11/09/2026. Tom propositalmente simétrico ao do auditor: pontos fortes primeiro, riscos depois, prioridades por fim.*

## Adendo (Onda 0.4, 12/09/2026)
- Item A-6 ("branch 01a07777 não existe no README"): origem localizada — a string está no **STATE-MIRROR §0** (outra linhagem de sessão), não no README. O auditor leu o arquivo certo com o nome errado; o ponto continua válido como "referência de branch obsoleta", só muda o endereço.
- Item B-R2 (README): resolvido — README vivo gerado (`ferramentas/build_readme.py`), histórico arquivado em `docs/historico/README-2026-08-17.md` com placa.
