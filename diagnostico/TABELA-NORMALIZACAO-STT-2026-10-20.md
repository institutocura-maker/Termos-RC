# Tabela inicial de normalização STT — «DE → PARA»

**Data:** 20/10/2026

**Natureza:** diagnóstico lexical derivado de seis transcrições brutas do fast-whisper; não é revisão de fonte, nem cotejo de áudio.

**Escopo:** primeiro léxico para a recepção STT de vídeos de Jan Val Ellam. Nenhuma das seis transcrições foi modificada.

> **Regra de procedência.** A saída do fast-whisper permanece um bruto. Uma cópia que receba as regras desta tabela deve chamar-se **transcrição STT normalizada**, nunca *verbatim bruto*. A fonte bruta não deve ser regravada: a política da casa já refutou normalizações que alterem a fonte (`diagnostico/U97-REFUTACAO-NORMALIZACAO-FONTES.md`, §§5–7).

---

## 1. Amostra examinada

Foram lidos **6 arquivos** (`3.278` linhas; `626.715` bytes), todos declarados em seu cabeçalho como `faster-whisper large-v3 (FP16 / CUDA)` e transcritos em 17–18/10/2026.

| Rótulo | Arquivo bruto em `uploads_recepcao/` | Vídeo | Linhas |
|---|---|---|---:|
| F1 | `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | `L90vP0VFSTc` | 511 |
| F2 | `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | `EbK2RfETyEM` | 883 |
| F3 | `2025-07_002_lS8Bw-eaFYQ_A_Falencia_dos_Deuses_e_a_Destinacao_do_Lobo_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | `lS8Bw-eaFYQ` | 891 |
| F4 | `2025-07_035_JDaxXjYGyu0_Direitos_e_Deveres_Espirituais_VSC_10.md` | `JDaxXjYGyu0` | 292 |
| F5 | `2025-09_029_SzZtXArSltg_O_Quarto_Caminho_de_Gurdjieff_VSC_16.md` | `SzZtXArSltg` | 343 |
| F6 | `2026-02_019_E2fBs7aocgU_O_Grande_Caminho_VSC_26.md` | `E2fBs7aocgU` | 358 |

### Como ler os regimes

- **AUTOMÁTICA** — forma STT incomum, mapeamento inequívoco no vocabulário do acervo; aplicar somente a palavra/expressão inteira, nunca como substring.
- **AUTOMÁTICA-CONTEXTO** — a troca é forte nesta amostra, mas a forma de origem também pode existir fora do vocabulário RC; requer ao menos uma âncora temática no mesmo parágrafo.
- **REVISAR** — há alvo provável, mas a forma pode representar mais de uma coisa, conter uma palavra colada ou conflitar com outra grafia canônica. Produzir fila, não trocar em lote.
- **PRESERVAR / PENDENTE** — a Base já determinou que a grafia STT fique registrada, ou não há forma canônica suficientemente demonstrada. Não normalizar.

As ocorrências são contagens literais na amostra F1–F6. A coluna **âncora** identifica a forma canônica no acervo; não cria código, termo, ficha ou relação nova.

---

## 2. Regras aprováveis de normalização

### 2.1 Automáticas — token exclusivo

Estas regras somam **52 ocorrências** na amostra. A aplicação futura deve respeitar fronteiras de palavra e conservar o bruto sem alteração.

| DE — forma literal STT | PARA — forma canônica | Classe | Ocorrências | Evidência na amostra | Âncora canônica |
|---|---|---|---:|---|---|
| `anunaki` | **Anunnaki** | entidade | 6 | F1 L255/L271/L393/L455/L457; F2 L91 | RC-024 — *Anunnaki* |
| `Trimurte`, `trimurto` | **Trimurti** | conceito/entidade | 9 | F1 L209; F2 L367/L369; F3 L203/L511/L727 | RC-104 — *Trimurti* |
| `Vismo`, `Visma`, `Vizno` | **Vishnu** | entidade | 20 | F1 L451; F2 L129/L131/L133/L137/L139; F3 L195/L395/L427/L773 | RC-135 — *Vishnu (Mavatna)*; as deformações de fala de Vishnu já são documentadas no acervo |
| `Pachupati`, `Pachupato` | **Pashupati** | entidade | 4 | F2 L189/L191; F3 L787 | RC-669 — *Pashupati* |
| `Tikkun` | **Tikun** | conceito | 4 | F1 L433; F2 L733; F3 L875; F6 L252 | RC-514 — *Tikun Cósmico* |
| `Mohenso`, `Mohensof` | **Mohen So** | entidade | 5 | F3 L205/L207/L209/L229/L257 | RC-081 — *Mohen So*; `GLOSSARIO-CANONICO-2026-08-31.md` registra explicitamente `Mohenso` |
| `Tirtankaras` | **Tirthankaras** | tradição/figura coletiva | 1 | F4 L144 | RC-397 — *Tirthankaras* |
| `Tote`, `Toth` | **Thoth** | entidade histórica/mítica | 3 | F1 L473; F5 L161 | RC-463/RC-534 usam a grafia *Thoth* |

### 2.2 Automática somente com âncora contextual

Esta regra responde por **47 ocorrências**. Não deve ser disparada por uma busca global simples: `Sofia` também pode designar uma pessoa fora do domínio da Revelação Cósmica.

| DE — forma literal STT | PARA — forma canônica | Condição mínima de contexto | Ocorrências | Evidência | Âncora canônica |
|---|---|---|---:|---|---|
| `Sofia`, `Sofio` | **Sophia** | no mesmo parágrafo, ao menos uma âncora como `Javé`, `Jesus`, `Trimurti`, `Vishnu`, `Brahma`, `avatar`, `Cristo Cósmico` ou `reintegração` | 47 | F1: 17; F2: 13; F4: 17 — p.ex. F1 L89/L451, F2 L367/L369, F4 L270/L272 | RC-009 — *Sophia (Cristo Cósmico)* |

**Saldo apto a normalização controlada nesta amostra:** **99 ocorrências** (`52` lexicais exclusivas + `47` com âncora contextual). Isto não significa que 99 palavras foram alteradas: nesta fase nenhuma transcrição foi reescrita.

---

## 3. Fila de revisão humana — alvo provável, mas não automático

| DE — forma literal STT | PARA provável / forma oficial | Motivo para revisão | Ocorrências | Evidência | Referência interna |
|---|---|---|---:|---|---|
| `Morrenso`, `Morrenson`, `Morressor` | **Morren So** *ou* **Moros**, conforme o trecho | A Base registra simultaneamente o epíteto oficial **Morren So** e variantes STT próximas que, em outro contexto, foram resolvidas como **Moros**. Não fundir os dois nomes sem ouvir ou ler o contexto semântico. | 5 | F2 L501; F3 L205/L229/L749/L773 | RC-454, nota de grafia oficial de *Morren So*; RC-530, lista contextual de variantes |
| `UERD`, `WERD` | **Wyrd / Urd** | A ficha canônica preserva as duas formas do nome. A saída deve escolher a grafia dita, não inserir automaticamente uma barra no corpo de uma fala. | 9 | F2 L531/L533/L535/L545/L559/L807; F3 L217 | RC-560 / RC-658 — *Wyrd / Urd* |
| `Elio` | **Enlil** | No conjunto F1 os contextos são de Enki/Anu/clãs anunnaki e a hipótese é forte; porém “Élio/Elio” também é nome pessoal. Exigir contexto anunnaki. | 16 | F1 L153/L157/L183/L253/L273/L277… | RC-487 — *Enlil*; precedente interno registra STT `Eli` por Enlil |
| `Enck`, `Enke`, `Enkel`, `Yenck`, `Dienke`, `Bienque`, `Enquil` | **Enki** ou **de Enki** | Há perda e fusão de segmentação. `Dienke`/`Bienque` podem conter preposição e não devem ser substituídos por uma única palavra às cegas. | 17 | F1 L253/L275/L277/L287/L301/L307/L309…; F3 L773 | RC-486 — *Enki* |
| `Virgium`, `Virgo`, `Bhishma`, `Vista` (somente F2 L181), `Vigna`, `Vigno`, `Vísgno`, `Vísneo`, `Vísnulo` | **Vishnu** | A vizinhança textual dos 20 casos aponta para a tríade Brahma–Vishnu–Shiva, mas algumas formas (`Vista`, `Virgo`, `Bhishma`) existem autonomamente em outros contextos. | 20 casos contextuais | F2 L137/L145/L149/L181/L363; F3 L395/L425/L427/L749/L751/L773/L787 | RC-135; variantes históricas `Virgno/Vno` documentadas em RC-135 e RC-530 |
| `Morrejodaro`, `Morrejo` | **Mohenjo-Daro** | A própria amostra alterna formas e o acervo usa `Mohenjo-Daro`; a correção é forte, mas é topônimo/história em quarentena, fora do núcleo terminológico. | 4 | F1 L221/L251/L253/L413 | RC-329 e RC-588 |
| `Arapa` | **Harapa** | Há forma interna `Harapa`, mas a grafia histórica também aparece de outras maneiras fora do acervo. Aplicar somente no mesmo bloco que trate de Mohenjo-Daro/vale do Indo. | 6 | F1 L221/L225/L251/L253/L413 | RC-329 |
| `Pesco`, `Péssico` na expressão `Golfo …` | **Golfo Pérsico** | Correção geográfica evidente no contexto, mas não é termo canônico RC e não deve virar substituição global de `pesco`. | 10 | F1 L233/L235/L245/L251/L339/L407 | pendência lexical geral; sem ficha RC dedicada |

---

## 4. Formas que não devem entrar em substituição automática

| Forma vista na amostra | Ocorrências | Decisão | Motivo / fonte |
|---|---:|---|---|
| `Pularra` | 16 | **PRESERVAR / PENDENTE** | A própria RC-743 lista `Pularra/Prara/Pharara/Porularra/Pulra` e determina **[REVISAR → AGUARDA-ÁUDIO]**. Não escolher grafia nova. |
| `Lémion`, `Lénion`, `Lemion` | 10 | **PRESERVAR** | A Base registra *Len Mion (Satã)*, mas também conserva `Lemion` como grafia STT datada. Não converter retroativamente sem regra específica aprovada. |
| `Anunnakis` | 80 | **PRESERVAR** | É plural usado na fala; trocá-lo por o lema singular canônico `Anunnaki` apagaria número gramatical. |
| `Brama` | 7 | **PRESERVAR** | O próprio acervo admite `Brama` em títulos/expressões, embora também use `Brahma`. Não é erro STT demonstrado. |
| `Nephilim` | 1 | **PRESERVAR** | Há grafia canônica *Nefilim*, mas `Nephilim` é transliteração corrente; não há razão suficiente para reescrita verbal. |
| `Parvati` | 1 | **PRESERVAR** | A Base usa *Parvathi*, mas `Parvati` é variante transliterativa; tratar como escolha editorial, não como ruído STT. |
| `Capella` | 1 | **PRESERVAR** | O acervo usa *Capela*, mas `Capella` é forma externa legítima; falta critério editorial específico. |
| `Gauzu` | 8 | **PRESERVAR** | Não é ruído demonstrado: o próprio acervo registra `Gauzu` em contexto de fonte. |

---

## 5. Regras de implementação para o lote de 300+ vídeos

1. **Nunca sobrescrever o bruto.** Guardar `raw/` (saída original do STT), gerar `normalizado/` como cópia e manter um log `antes → depois`, regra usada, arquivo e linha/parágrafo.
2. **Começar somente pela seção 2.1.** Usar substituições literais com fronteiras de palavra, sem regexes permissivas, sem trocar fragmentos dentro de palavras e sem alterar URLs/metadados.
3. **Aplicar 2.2 por contexto verificável.** Caso a condição não seja satisfeita, a ocorrência entra na fila de revisão.
4. **Seção 3 vira fila, não corretor.** O sistema pode destacá-la, mas não deve editar automaticamente.
5. **Seção 4 é bloqueio explícito.** Uma futura regra para qualquer uma dessas formas requer prova de áudio ou despacho editorial.
6. **A cada lote:** emitir contagem por regra, lista de mudanças, lista de candidatos não resolvidos e amostra de auditoria. Uma regra nova só entra após ao menos uma evidência textual e uma âncora canônica — nunca por aproximação fonética isolada.

## 6. Fecho da apreciação inicial

A amostra não recomenda um corretor geral de “português”: o ruído principal é **terminológico, onomástico e fonético**, com muitas palavras que se parecem com nomes comuns. O ganho seguro está em um léxico pequeno e governado.

O primeiro núcleo utilizável contém **8 regras lexicais exclusivas**, uma regra contextual de alta incidência e uma fila explícita de ambiguidades. A Base terminológica, as relações e os seis brutos de recepção permaneceram intocados.
