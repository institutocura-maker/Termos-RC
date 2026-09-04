# VERIFICAÇÃO DE COBERTURA — LISTA SIMPLES DE TERMOS-CHAVE DA RC (2026-09-04)

> **Objetivo:** conferir se algum termo da relação antiga `uploads_recepcao/LISTA SIMPLES DE
> TERMOS CHAVE DA RC.txt` (preparada por um Assistente, ordem alfabética A–Z) **não está
> contemplado** pela base de termos da RC.
>
> **Base de referência:** `ferramentas/dados_termos.py` (TERMOS — 929 códigos RC + RELACOES) +
> fichas em `termos/RC-*.md` + catálogo de obras primárias `BIBLIO` (`ferramentas/build_xlsx.py`).
>
> **Branch:** `arena/01a06429-termos-rc` · **HEAD:** `97db35b` · **Data:** 04/09/2026.
> **Método:** correspondência termo-a-termo por (1) nome canônico exato, (2) grafia/variante
> normalizada, (3) título de obra primária, (4) presença em ficha (nome de arquivo e conteúdo).
> Itens restantes foram verificados manualmente contra o corpus. **Nada na base foi alterado.**

---

## 1 · Síntese

A lista contém **~197 linhas de itens** (as duas primeiras são cabeçalho/nota do Assistente;
o restante são termos/conceitos/títulos em ordem alfabética). Resultado da auditoria:

| Classe | Qtd | Significado |
|---|---|---|
| 🟢 **COBERTO** (código RC próprio) | ~90 | Já existe termo canônico que representa o item |
| 📘 **OBRA primária** (título de livro B###) | ~21 | Não é termo; é obra já catalogada na BIBLIO |
| 🟡 **COBERTURA POR VARIANTE / MENÇÃO** | ~40 | Sem código próprio, mas coberto por uma ficha vizinha (variação, sinônimo, contexto) |
| 🔴 **NÃO CONTEMPLADO / LACUNA** | ~20 | Sem código próprio e sem ficha que o represente (candidatos reais) |
| ⚪ Genérico (física/instituição) | ~6 | Termo de ciência geral/sigla, não é neologismo RC |

**Conclusão principal:** a esmagadora maioria da lista já é contemplada. As lacunas genuínas
estão concentradas em **3 famílias**: (a) tipologias "homo …" (consumus/corruptus/nervosus/
religiosus), (b) termos cabalísticos periféricos (Ain Soph/Ein Sof, Klippoth, Shevirah), e
(c) alguns conceitos/expressões soltos (Vírus mental, Personificação da Condição Mental,
Guarida preciosa, Suserano Universal etc.). Veja §3.

---

## 2 · Aviso importante sobre a natureza do documento

1. A lista mistura **termos** com **títulos de livros do próprio Ellam** (ex.: "O Drama Cósmico
   de Javé", "Cartas a Javé", "Carma e Compromisso", "Jesus e Nietzsche", "O Sorriso de Pandora",
   "Terra Atlantis", "Revelação Cósmica"). Esses **não são termos a criar** — são obras primárias
   já registradas na BIBLIO (B001, B002, B011, B016, B020, B023, B025, B026, B029, B033, B034, B035,
   B037, B043, B044, B046, B048, B049, B052, B003, B005, B012, B013, B015, B022).
2. A lista também traz **termos de física/cosmologia geral** (Antimatéria, Buracos de minhoca,
   Energia escura, Entropia, Glúons, Quark, Matéria escura, Matriz de Planck, Quarta Dimensão,
   Túneis quânticos) — na RC eles aparecem **como referência/contexto** dentro de fichas, não
   como termos próprios da Revelação. Não devem virar código sem fonte primária que os ancore
   (regra G1).

---

## 3 · LACUNAS E CANDIDATOS (o que o curador procura)

### 3.1 — Tipologias "homo …" (familia consumus/corruptus/nervosus/religiosus)
**Status: NÃO CONTEMPLADAS — e JÁ ANOTADAS como deliberadamente não materializadas.**
A CONTINUIDADE.md (ciclo do livro **B040**) registra explicitamente: *"O-3: zero códigos;
RC-040/099/431/432/244/540 não materializadas; **'homo consumus' sem código**"*. Ou seja, as
tipologias `Homo consumus`, `Homo corruptus`, `Homo nervosus`, `Homo religiosus` da lista **foram
identificadas no corpus mas deliberadamente NÃO criadas** (decisão O-3/O-4 — material apenas como
leitura de B040, sem código). A lista antiga as inclui, mas a base atual **as omite de propósito**.

### 3.2 — Termos cabalísticos periféricos
A base tem um **cluster Cabala** rico (RC-261 Kether, RC-262 Daath, RC-263 Sefirot, RC-264
Atziluth/Briah/Yetzirah/Assiah, RC-265 Zohar/270 mundos, RC-266 Sepher ha-Zohar, RC-267 Isaac
Luria/Tzimtzum, RC-268 Gnosticismo). A lista traz alguns que **caem nesse cluster mas sem ficha
própria**:
- **Ain Soph (Ein Sof)** → citado no contexto de Tzimtzum (RC-001/RC-008); **sem ficha dedicada**
  no cluster Cabala. *Candidato a variação dentro de RC-264/RC-267, não código novo.*
- **Klippoth (Qliphoth)** → **ausente** das fichas. *Item do cluster Cabala a considerar.*
- **Shevirah** (quebra dos vasos, luriano) → **ausente**; vizinho de RC-267 (Isaac Luria).
- **Sefiroth / Sefirot** → **já coberto** por RC-263.
- **Daath / Zohar / Tzimtzum / Atziluth** → **já cobertos** (RC-262/266/008+B013/264).

### 3.3 — Conceitos/expressões soltos (possíveis lacunas, verificar fonte primária)
Sem código próprio e sem ficha dedicada clara — exigem curadoria antes de qualquer criação:
- **Vírus mental** / **Onda Vírus** → "vírus mental" aparece como menção em RC-036/078/450;
  não há ficha própria de "vírus mental"/"onda-vírus". Verificar se é variação de vírus de
  programação mental (candidato de baixa prioridade).
- **Personificação da Condição Mental** → provável referência ao conceito de Mavatna/Mavat
  (RC-503) ou à mecânica de encarnação de condição; sem ficha dedicada.
- **Personificação da Sabedoria** → próximo de Hochmah (RC-565) e do Quarto Cérebro (RC-758);
  sem ficha dedicada.
- **Guarida preciosa** → expressão da OC; aparece em 3 arquivos, sem ficha dedicada.
- **Suserano Universal (Celeste)** → epíteto de Sophia/RC-009 (Suserano Cósmico); variação, não
  código novo.
- **Semente única da vida** → RC-525 (Semente da Racionalidade) é vizinho; verificar relação.
- **DNA Homo Terráqueo** → RC-231/RC-107 cobrem DNA/terráqueos; sem ficha dedicada.
- **Clonagem necessária** / **Elétron de Deus** / **Estirpes cósmicas** / **Gêneros universais** /
  **Cabalistas** / **Grupo da Epistemologia Val** / **Impulso ao progresso** → presentes apenas
  como menção/contexto; sem código próprio.

### 3.4 — Institucional/real
- **IEEA** → sigla de instituição real (citada em 287 arquivos). Não é neologismo RC; não criar.
- **Capelinos** → seres/originários de Capela; coberto por RC-039 (Sistema de Capela) e RC-450
  (Revolta Capelina) / RC-447. Variação, não código novo.
- **Cabalistas** → seguidores da Cabala; cluster RC-261-268 cobre o fenômeno; não código novo.

---

## 4 · Referência rápida das principais correspondências (COBERTO)

Lista parcial dos itens já contemplados por código, para conferência rápida:

| Item da lista | Código/obra |
|---|---|
| Javé | RC-001 |
| Rebelião de Lúcifer / Lúcifer | RC-002 / RC-078 |
| Reintegração Cósmica | RC-003 (e B003) |
| Sophia / Cristo Cósmico / Suserano Cósmico | RC-009 |
| Terra Atlantis | RC-010 (+ obras B017/B018/B039) |
| Frota Norte (Terra Atlantis) | RC-065 |
| Adhyatman | RC-013 |
| Alt'Lam Gron | RC-018 |
| Anjo-clone | RC-019/RC-651 |
| Asphezian | RC-025 |
| Benem | RC-032 |
| Bhuloka / Brahmaloka / Universo antimaterial | RC-033/RC-038/RC-106 |
| CFD (Código-fonte Definidor de Vida) | RC-040 |
| Demiurgo / Criador | RC-048/RC-041 |
| Cultura demo / Demos / Biodemos / Biodemol | RC-044/RC-049/RC-036/RC-186 |
| En Drel | RC-055 |
| Espherian / Espheron | RC-057/RC-058 |
| Espiritualidade Superior | RC-059 |
| Fenvam(s) | RC-064 (variação) |
| Morus | Moros → RC-454 (grafia/variação) |
| Genos | RC-066 |
| Grupo Atlan | RC-388 |
| Holograma universal | RC-218 |
| Homo sapiens | RC-099/RC-544 |
| Lila / Lokas / Logos Criadores | RC-075/RC-077/RC-076 |
| Mastlans | RC-079 |
| Mensagem Talm / Projeto Talm / Processador Val | RC-080/RC-091/RC-089 |
| Nidana / Orbum / Perpérion / Prabrajna | RC-154/RC-085/RC-087/RC-152 |
| Shamb-Aha / Trimurti / Xadrez Cósmico / Yel Luzbel | RC-101/RC-104/RC-150/RC-142 |
| Val (família) / Yel (família) | RC-109 / RC-136 |
| Atziluth / Daath / Sefirot / Zohar | RC-264/RC-262/RC-263/RC-265-266 |
| Codificador de Zion | RC-252/RC-255 |
| Consciência Cósmica | RC-721 |
| DNA-lixo (Ex-DNA-lixo) | RC-542 |
| Força rajas / tamásica / Sattva | RC-151 (Gunas) |
| Elétrons / Rebelião dos Elétrons / Elétron de Deus | RC-161/RC-162/RC-378/RC-826 |
| Entropia | RC-160/RC-725 |
| Eras da Criação / Era Sapiens | RC-155 / RC-238 |
| Khaos (Caos) | RC-284/RC-294 |
| Antimatéria / Matéria escura / Energia escura | RC-527/RC-106 (contexto) |
| Memórias de Javé / Cartas a Javé | RC-421 / RC-416 |
| Molécula-mãe / Mônada espiritual | RC-540 / RC-149 |
| Portais (seres dos) / Fechamento dos portais | RC-241 / RC-295 |
| Reencarnação / Revelação Espiritual / Ressonância mórfica | RC-407 / RC-190 / RC-381 |
| Semente | RC-525 |
| Sinal de Land's End | RC-237 |
| Varna / Dharma / Castas | RC-319/RC-321/RC-322 |
| Espirituais / Seres dos Portais | RC-100 / RC-241 |

> A íntegra do cruzamento (os ~197 itens um a um) não é reproduzida aqui por economia; este
> relatório foca as lacunas (§3) que respondem diretamente à pergunta do curador. Se desejar,
> posso gerar o **mapeamento completo linha-a-linha** (item → classe → código/obra/justificativa)
> como segundo artefato.

---

## 5 · Recomendação

1. **Não criar código novo** para os itens já cobertos por variação (Capelinos, Suserano,
   Semente única, Varna, Tikkun→RC-514, Fenvam, Morus→Moros RC-454 etc.) — evitariam duplicação.
2. **Tipologias "homo …":** manter a decisão já registrada (não materializar). Se o curador quiser,
   reabrir em ciclo próprio com fonte B040.
3. **Cabalísticos periféricos (Ain Soph, Klippoth, Shevirah):** avaliar como **variações do cluster
   Cabala** (RC-264/RC-267) — apenas se houver fonte primária, jamais por catálogo externo (regra de
   quarentena entre ecossistemas).
4. **Conceitos soltos (§3.3):** só tratar se houver fonte primária que os ancore; caso contrário,
   permanecem menção de contexto (regra G1/G3).
