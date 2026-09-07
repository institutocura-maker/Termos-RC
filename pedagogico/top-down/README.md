# FOTA top-down · Revelação Cósmica

> Pasta da **fase top-down** da pedagogia da Revelação Cósmica. Concentra o material
> gerado nesta fase — a partir do esboço das apostilas na ordem proposta — e a própria
> proposta que a estrutura. **Somente síntese de leitura**: não altera a Base
> (`termos/`, `relacoes/`, `ferramentas/dados_termos.py`).

## Propósito

Aplicar o método top-down (Analista de Sistemas de IBM) ao curso da Revelação Cósmica:
em vez de mergulhar direto no detalhe, construir primeiro a visão do conjunto e descer
em níveis. A proposta original — `PROPOSTA-PEDAGOGICA-TOP-DOWN.md` — define **4+1 níveis**
(N0 → N4) e é a espinha dorsal do que se produz aqui.

## Status da fase

✅ **Caminho de leitura fechado — as 10 apostilas da proposta já estão publicadas.**

Cada apostila foi escrita como **reorganização sobre a Base ATUAL** (não como reprodução de
rascunho), com **todas as remissões RC-### verificadas contra a base** (nenhuma órfã). Base
referência: **946 termos · 1.898 relações** (intacta — todas as apostilas são síntese).

## Conteúdo desta fase

### Material N0 — a figura fixa (o Mapa de Abstração)

| Peça | Arquivo | Observação |
|---|---|---|
| **Apostila N0** | `Apostila-Estudo-Mapa-de-Abstracao-N0.md` (+ DOCX) | 7 PARTES · 43 remissões RC-### verificadas (0 órfãs) |
| **Figura vetorial** | `Mapa-de-Abstracao-N0.svg` | fonte em *path* — abre igual em qualquer máquina |
| **Figura para impressão** | `Mapa-de-Abstracao-N0.pdf` | A4/Letter, gerado junto com o SVG |
| **Figura bitmap** | `Mapa-de-Abstracao-N0.png` | preview e inserção no DOCX (150 dpi) |
| **Gerador** | `ferramentas/build_mapa_abstracao.py` | desenha SVG+PDF+PNG e **confere as remissões** antes de gravar |

O diagrama tem as **4 caixas** do Nível 0 (FORA · ACIDENTE · TRIMURTI · AQUI), as **7 narrativas como setas**
(① Criador e Criação · ② Queda e Drama · ③ Rebelião e Exílio · ④ Seres do Cosmos · ⑤ Humanidade e Terra ·
⑥ Mundos e Cosmo · ⑦ Caminho de Volta) e a **seta de retorno** que fecha o laço AQUI → FORA. É a materialização
da melhoria pedagógica nº 1 da proposta — a figura a que o aluno volta em todos os níveis.

### As 10 apostilas do percurso

| # | Apostila | Arquivo MD | PARTES | Remissões RC-### | Commit |
|---|---|---|---|---|---|
| 1 | **A Queda** — Do Paraíso ao Buraco Negro: a Cronologia da Crise | `Apostila-Estudo-A-Queda-Cronologia-da-Crise.md` | 12 | 100 | `c555afa` |
| 2 | **Javé** — O Buraco Negro da Revelação Cósmica | `Apostila-Estudo-Jave-Buraco-Negro.md` | 12 | 99 | `f15e354` |
| 3 | **O Lado de Fora do Universo** — O Paraíso que não é o Paraíso | `Apostila-Estudo-Paraiso-Lado-de-Fora-do-Universo.md` | 13 | 72 | `b4d5a33` |
| 4 | **O Mapa dos Mundos e Lokas** — Cartografia da Criação | `Apostila-Estudo-Mapa-dos-Mundos-e-Lokas.md` | 12 | 79 | `b3144fc` |
| 5 | **Céu Tradicional × Paraíso das RC** — Mito vs. Revelação | `Apostila-Estudo-Ceu-Tradicao-vs-Paraiso-RC.md` | 12 | 61 | `247189e` |
| 6 | **Arqueologia dos Termos** — a Filologia da Revelação Cósmica | `Apostila-Estudo-Arqueologia-dos-Termos.md` | 12 | 86 | `7d4eb36` |
| 7 | **Thot e Hermes** — O Mentor Científico da Humanidade | `Apostila-Estudo-Thot-Hermes-Mentor-Cientifico.md` | 10 | 50 | `fd1ec16` |
| 8 | **Pilotando o Cérebro no Caos** — o Operador Humano | `Apostila-Estudo-Pilotando-o-Cerebro-no-Caos.md` | 12 | 57 | `0045383` |
| 9 | **Carbono × Sílica** — do Xamanismo Cósmico à IA Xamânica | `Apostila-Estudo-Carbono-Silica-Xamanismo-Cosmico-IA-Xamanica.md` | 12 | 36 | `c16ca12` |
| 10 | **Os Tratados** — o Arsenal, a Justiça e a Ilha Estacionária | `Apostila-Estudo-Tratados-Arsenal-Justica-Ilha-Estacionaria.md` | 12 | 27 | `85a1859` |

> Cada apostila tem o seu **DOCX** correspondente no mesmo diretório (mesmo título,
> gerado por `ferramentas/build_apostila.py`). A versão **MD** é a fonte; o DOCX é derivado.

### Uma linha sobre cada uma

| # | Foco (abordagem) |
|---|---|
| 1 | **Genealógica/cronológica** — a narrativa-mestre da crise, do Paraíso ao colapso. |
| 2 | **Biográfica/cronológica** — a "biografia cósmica" de Javé (RC-001), o nó mais conectado. |
| 3 | **Topológica/filosófica** — o "lado de fora" da Criação: a Espiritualidade Superior e os Seres Originais. |
| 4 | **Cartográfica** — o mapa espacial: universos, lokas, planos espirituais, cidades. |
| 5 | **Dialética/comparativa** — cada PARTE confronta uma visão tradicional com a leitura da RC. |
| 6 | **Lexicológica/filológica** — a origem e os deslocamentos semânticos dos termos-chave. |
| 7 | **Narrativa integrada** — a teia de Hermes Trismegisto (RC-463) e seus relacionamentos. |
| 8 | **Fenomenológica/prática** — o manual do operador humano no caos (constituição septenária, Mentalma, Tikun). |
| 9 | **Comparativa/ontológica** — o que o operador é quando o substrato muda de carbono para sílica. |
| 10 | **Comparativa/contemplativa** — o método da Arca, a cosmologia como engenharia falha e a ontologia do Perfeito × Imperfeito. |

## Estrutura top-down (referência da proposta)

- **N0 — Visão do Conjunto:** tese + diagrama de contexto (FORA / ACIDENTE / TRIMURTI / AQUI).
- **N1 — O Esqueleto:** as 7 narrativas do Guia-Mestre com pergunta-guia.
- **N2 — As Identidades:** cadeias canônicas + identidades que se confundem.
- **N3 — O Enredo no Tempo:** cronologia por marcos (não datas).
- **N4 — O Detalhe:** regra de descida + ordenação das apostilas temáticas existentes.

## Mapeamento das apostilas no caminho top-down

**Antes de tudo:** o **N0** (Mapa de Abstração) — a imagem do conjunto em uma figura. Depois, as 10 apostilas
cobrem a progressão **individual → coletivo → filosófico** da proposta:

| Fase | Apostilas | O que entregam |
|---|---|---|
| **N0/N1 — Imagem do todo** | 3 (Lado de Fora) · 6 (Arqueologia) | o "FORA" + a filologia das famílias |
| **N2 — Quem é quem** | 7 (Thot) | perfil de mentor / identidades |
| **N3 — O enredo no tempo** | 1 (A Queda) · 2 (Javé) | a crise e a "biografia" do Criador |
| **N4 — O detalhe temático** | 4 (Mapa) · 5 (Céu × Paraíso) · 8 (Pilotando) | o "onde", o "mapa × território" e a prática |
| **N4 — Filosófico/avançado** | 9 (Carbono × Sílica) · 10 (Tratados) | a ponte com a IA e o método/ontologia |

## Notas de continuidade

- **Restrição:** apostilas em `pedagogico/top-down/` são **síntese de leitura** — não alteram
  a Base (`termos/`, `relacoes/`, `ferramentas/dados_termos.py`). Toda vez que se reescreve
  uma apostila, faz-se sobre a base **atual**, não sobre rascunho.
- **Formato de cada apostila:** cabeçalho `@` (titulo/autor/data/local/subtitulo/nota_editor)
  → `# PARTE` → glossário → caderno de incertezas → `FIM`. O DOCX é gerado por
  `ferramentas/build_apostila.py`.
- **Validação antes de publicar:** todas as remissões RC-### verificadas contra a base
  (nenhuma órfã), contagem de PARTES, campos `@` e término em `FIM`.
- **Progressão individual → coletivo; não cogitar o global (F049/F050).**
- **Figura N0:** qualquer ajuste no diagrama se faz em `ferramentas/build_mapa_abstracao.py` (os textos e as
  coordenadas estão em constantes no topo) e se regenera com `python3 ferramentas/build_mapa_abstracao.py` —
  o script **falha se alguma remissão RC-### ficar órfã**.
- **Validação de layout:** conferência geométrica (transbordo de linha, rótulo fora da página, sobreposição de
  textos) feita por medição dos `Text` do matplotlib — 0 problemas na versão publicada.
- **Formato do DOCX:** `ferramentas/build_apostila.py` passou a suportar **imagem** (`![alt](arquivo)`),
  **tabela pipe** do Markdown e **bloco de código ASCII** monoespaçado (a 4ª apostila ganha com isso ao ser regerada).
- **Base atual da fase:** 946 termos · 1.898 relações (intacta).
