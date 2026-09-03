# MAPEAMENTO — ESTEIRA-APOSTILAS · 2019-08-25 · Os Três Fornos Replicadores do Projeto Talm

**Data:** 03/09/2026 · **Processo:** Esteira de Consolidação sobre apostilas refatoradas (Lote 1 — recorte/formato) · **Fonte:** `fonte.txt` (SHA `faf0d693…`, 22.606 B) · **Estado:** LEVANTAMENTO (não altera a base)
> Objetivo: validar o **formato** da devolutiva com 1 apostila antes de aplicar ao Lote 1 inteiro.
> Esta apostila (v3.1, P2019-08-25) é **fonte oral fundadora** do cluster Fornos/Projeto Talm e já está
> parcialmente integrada na base — portanto o recorte demonstra a trilha de **AUDITORIA**.

## Natureza da fonte (para elevação — decisão G1)
A apostila é fonte **P (palestra)**, normalizada a partir de `original.txt` (STT). Pela decisão G1, **não eleva status por si só**; funciona como **auditoria/confirmação de leitura**. Origem primária real: `P2019-08-25` (STT).

## Legenda de decisão
| Sigla | Significado |
|---|---|
| ok | entidade casa com RC existente (referente correto) |
| gap | RC existente **não lista `P2019-08-25`** em `dados_termos.py`, embora o texto a descreva (auditoria) |
| fech | RC foi **criado a partir desta fonte** e já a cita (RC-836/837) |
| var | variação de grafia / enquadramento a estudar |
| sem | sem correspondente direto na base (não criar à toa) |

## Entidades mapeadas
| # | Entidade (apostila) | RC canônico | Decisão | Observação |
|---|---|---|---|---|
| 1 | Brahma / Brajna | RC-037 | ok/gap | apostila o descreve como 1º Logos, doença da supremacia; RC-037 não cita P2019-08-25 |
| 2 | Shiva (Savna) | RC-102 | ok/gap | 2º Logos, pai dos demos, linhagem do fogo; não cita P2019-08-25 |
| 3 | Vishnu / Mavatna (Adhymavatana) | RC-408 | ok/gap | 3º Logos, propôs Trimurti/Lila; não cita P2019-08-25 |
| 4 | Moros (Elm) | RC-454 | ok | origem de Tempérion (Q&A André); grafia STT Morus; não cita P2019-08-25 |
| 5 | Morren So (Mohen So) | RC-081 | ok/gap | avatar de Vishnu que engendra Sophia; não cita P2019-08-25 |
| 6 | Sophia (Cristo Cósmico) | RC-009 | ok/gap | engendrada com "bomba" de Brahma; não cita P2019-08-25 |
| 7 | Lúcifer / Rebelião de Lúcifer | RC-002 | ok | destravou lacre da família Yel; não cita P2019-08-25 |
| 8 | Família Aya | RC-834 | ok | assessoras de Sophia (São Gabriel/Rafael/Miguel); ficha só cita P2023-12-17 |
| 9 | Família Aye | RC-835 | ok | idem Aya; ficha só cita P2023-12-17 |
| 10 | Zian (Zion) | RC-146 | ok | codificador; não cita P2019-08-25 |
| 11 | Trimurti | RC-104 | ok/gap | + Lila como "constituição/geopolítica da Trimurti"; não cita P2019-08-25 |
| 12 | Lila | (Lila é qualificadora de RC-104) | sem | sem ficha própria; tratada como aspecto de RC-104 |
| 13 | Projeto Talm | RC-091 | ok/gap | Mensagem Talm/Nidana; não cita P2019-08-25 |
| 14 | Nidana / Nidana B | (via RC-091) | var | Nidana B (ovo cósmico) = qualificador; ver se merece nota em RC-091 |
| 15 | Fornos Replicadores | RC-771 | ok/gap | "casulo vibratório"; não cita P2019-08-25 (só P2021-05-15+ em diante) |
| 16 | Forno de Awayen | RC-836 | fech | **criado desta fonte**; cita P2019-08-25 ✓ |
| 17 | Forno de Awaylengan | RC-837 | fech | **criado desta fonte**; cita P2019-08-25 ✓ |
| 18 | Forno de Awaymaion | RC-499 | gap | apostila o descreve (2º a funcionar, biodemos); **RC-499 não cita P2019-08-25** |
| 19 | Bilatérios | RC-035 | gap | ficha tem "## Ampliação — P2019-08-25"; **dados_termos.py não lista P2019-08-25** |
| 20 | Radiatas | RC-093 | ok/gap | contraposição aos bilatérios; não cita P2019-08-25 |
| 21 | Sistema Arcaico Mental | RC-828 | gap | ficha tem "Ampliação — P2019-08-25"; **dados_termos.py não lista P2019-08-25** |
| 22 | Rebelião dos Elétrons | RC-826 | ok | apostila como fundadora (Q&A); ficha não carrega Ampliação P2019-08-25 |
| 23 | Quarto Logos (Olm/Codificador de Zian) | RC-092 | ok/gap | "semeador de escolas"; não cita P2019-08-25 |
| 24 | Javé | RC-001 | ok/gap | = Brahma = Atum; "abelha-rainha"; não cita P2019-08-25 |

## Principais achados (recorte)
1. **Já integrada em ~2 códigos:** RC-836 (Awayen) e RC-837 (Awaylengan) foram **criados a partir de P2019-08-25** e a citam no cadastro. A esteira aqui é **auditoria**, não mineração primária.
2. **Gap de fonte recorrente (divergência estrutural):** fichas RC-035, RC-499, RC-828 contêm seção narrativa **"## Ampliação — P2019-08-25"** (declarando a fonte fundadora de 2019), mas a lista de fontes em `dados_termos.py` **não inclui `P2019-08-25`** para esses códigos. RC-826/834/835 são descritos nesta apostila mas nem a ficha nem o cadastro registram P2019-08-25. → a consistência "ampliação-narrativa ↔ fonte no cadastro" está quebrada e deve ser auditada no Lote (V-1).
3. **Awaymaion (RC-499)** é o terceiro forno descrito na apostila, mas o cadastro não a associa a P2019-08-25 (fonte mais antiga lá: P2021-05-15). Candidato a receber a fonte fundadora — conferir primário (V-2).
4. **Sem termos genuinamente novos:** todos os ~24 referentes casam com RC existentes; nada a criar (decisão G3).

## Divergências abertas (ledger deste recorte)
| ID | Descrição | Tipo | Impacto |
|---|---|---|---|
| V-1 | Ampliação P2019-08-25 narrada em fichas (RC-035/499/828) sem correspondência na fonte do cadastro | consistência ficha↔cadastro | alto — precisa reconciliar (qual é a autoridade?) |
| V-2 | Awaymaion (RC-499) não recebe a fonte oral fundadora de 2019 | lacuna de fonte | médio — conferir citação primária |
| V-3 | RC-826/834/835 descritos na apostila mas sem P2019-08-25 registrado (nem ficha nem cadastro) | lacuna de fonte | médio — conferir relevância/citação |
