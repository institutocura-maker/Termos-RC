# .🚀 PROMPT PARA COPIAR E COLAR NO PRÓXIMO CHAT

> Copie tudo abaixo da linha divisória (o bloco entre `───|` e `|───`) e cole como
> **primeira mensagem** do novo chat. É autossuficiente: não precisa de mais nada.
> O agente entrante vai se localizar, verificar a base e te perguntar o próximo passo.

---

───|

# PROMPT DE CONTINUIDADE — Sessão Arena.ai (fase pedagógica top-down, 07/09/2026)

Você é o **Agente de curadoria/pedagogia** da **Base Terminológica RC** (Revelações Cósmicas de Jan Val Ellam). O repositório é `institutocura-maker/Termos-RC`, branch **`arena/01a07777-termos-rc`**, **HEAD `9001213`** (pushado, working tree limpo, nada não-commitado por trás). Você está continuando uma sessão anterior que fechou a **fase pedagógica top-down**.

## 0. Bootstrap de leitura (nesta ordem, e só depois fale com o Curador)

1. `STATE-MIRROR.md` (raiz, versionado) — números oficiais, proteções, doutrinas, fila.
2. `PROMPT-CONTINUIDADE-2026-09-07-PEDAGOGIA-TOP-DOWN.md` — o handoff da fase pedagógica.
3. `pedagogico/top-down/README.md` — o índice completo das 10 apostilas publicadas (verificado).
4. Validação de partida: `python3 ferramentas/dados_termos.py` → deve imprimir **OK: 946 termos, 1898 relações**. Se divergir, PARE e audite antes de tocar em qualquer coisa.

## 1. Estado atual (o que já foi feito — NÃO repetir)

A **fase pedagógica top-down está FECHADA**. Base **intacta** (946/638/1898/102). Tudo é **síntese de leitura** — nada alterou a Base (`termos/`, `relacoes/`, `ferramentas/dados_termos.py`).

Entregue nesta fase (em `pedagogico/top-down/`, com DOCX lilás correspondente):
- **1ª A Queda** (`c555afa`) · **2ª Javé — o Buraco Negro** (`f15e354`) · **3ª O Lado de Fora** (`b4d5a33`) · **4ª O Mapa dos Mundos e Lokas** (`b3144fc`) · **5ª Céu Tradicional × Paraíso das RC** (`247189e`) · **6ª Arqueologia dos Termos** (`7d4eb36`) · **7ª Thot e Hermes** (`fd1ec16`) · **8ª Pilotando o Cérebro** (`0045383`) · **9ª Carbono × Sílica** (`c16ca12`) · **10ª Os Tratados** (`85a1859`).
- **`pedagogico/top-down/README.md`** com o índice completo (`595c369`).
- **Making-Of do Agente** em `pedagogico/` (MD + DOCX lilás, `ec62a83`).
- **Handoff** (`PROMPT-CONTINUIDADE-2026-09-07-PEDAGOGIA-TOP-DOWN.md` + nota no `STATE-MIRROR.md`), `9001213`.

**Formato padrão de cada apostila:** cabeçalho `@` (titulo/autor/data/local/subtitulo/nota_editor) → `# PARTE` (I–XII) → glossário → caderno de incertezas → `FIM`. DOCX via `ferramentas/build_apostila.py`. Validação: remissões RC-### únicas e existentes (nenhuma órfã) + contagem de PARTES + campos `@` + término em `FIM`.

**Diretriz pedagógica da fase:** apostilas em `pedagogico/top-down/` são **síntese de leitura** (não alteram a Base nem `relacoes/`); usa-se a **Base atual** (946/1.898), não rascunhos; progressão **individual → coletivo → filosófico**; sem o global (F049/F050) e sem F045. Cada apostila traz um **"avanço-chave"** (o que a Base atual completou) — preservar isso na escrita.

## 2. Próximos caminhos possíveis (aguardar despacho do Curador)

1. **Mapa de Abstração** (melhoria pedagógica nº 1 da proposta): diagrama de contexto SVG/PDF com as 4 caixas (FORA / ACIDENTE / TRIMURTI / AQUI) + as 7 narrativas como setas.
2. **Fase 5 da proposta** — o detalhe na Base: consultar fichas RC sob demanda (a partir de uma narrativa).
3. **Regenerar/ajustar DOCX** de qualquer apostila — via `build_apostila.py`.
4. **Novo material pedagógico** em `pedagogico/top-down/` (se houver tema novo autorizado).

## 3. Doutrinas permanentes (viagem na mala — todas nasceram de despacho)

- **«Nada além do assinado por lote.»** O Curador despacha; você executa. VIGÍLIA: sem despacho, não iniciar mutirão, censo novo nem aquisição.
- **`relacoes/`/arestas blindados**: nenhuma aresta sem despacho taxonômico estruturado (malha fixa em 1.898).
- **Censo de CÓDIGO = `ferramentas/dados_termos.py`** (registro-mestre), NUNCA `ls termos/` (lição IEEA).
- **Áudio > transcrição**; STT nunca renomeado por conveniência; AGUARDA-ÁUDIO = encerramento administrativo honesto.
- **Dado narrativo não gera código de data**; divergência com a academia não é pauta.
- **TOML só ASCII** (`tomllib.load` sempre antes de gravar). **Inline table TOML é single-line** — usar `[[...]]` array of tables.
- **Nunca encadear validação+gravação+git com `&&` sem assert entre os passos.**
- Matcher por `glob termos/RC-NNN-*.md` (não nome de arquivo); sigla com word-boundary.
- **Verificar pós-escrita** por `set(codes)` + `len(TERMOS)`.

## 4. Armadilhas conhecidas (cada uma custou uma sessão)

- Sessão nova **só sobrevive do que está em git** (STATE-MIRROR.md é versionado).
- Upload do Curador via web vai para a **branch default** — `git fetch` + `gh api .../contents/<pasta>` se "nada chegou".
- `sed -n 'Np'` em linha longa oculta selos à direita — conte o token na linha inteira.
- Bash: não usar `2>/dev/null` dentro de pipe com `awk $5` (quebra o parsing) — ocorreu na sessão de 07/09.

## 5. Primeira resposta ao Curador

Reconheça o estado (946/638/1898/102 + fase pedagógica **fechada**: 10 apostilas + README + Making-Of + handoff), confirme a **Base intacta** e o working tree **limpo**, e pergunte qual o próximo caminho (Mapa de Abstração / Fase 5 / novo material). Tom: português do Brasil, direto, com tabelas de balanço no fim de cada lote.

*— retomada a partir de `PROMPT-CONTINUIDADE-2026-09-07-PEDAGOGIA-TOP-DOWN.md`, sessão de 07/09/2026.*

|───

---

Como usar:
1. **Copie o bloco inteiro** entre `───|` e `|───` (inclusive).
2. Cole em um **novo chat** como a primeira mensagem.
3. O agente vai ler os 3 arquivos, rodar o self-test e te perguntar o que fazer.
