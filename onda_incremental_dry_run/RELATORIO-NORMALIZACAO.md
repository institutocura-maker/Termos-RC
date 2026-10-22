# Relatório de normalização — onda_incremental_dry_run

**Data de geração:** 2026-10-22
**Executor:** `ferramentas/normalizar_onda_incremental_dry_run.py`
**Entrada:** `uploads_recepcao/` (os seis brutos selados do piloto)
**Saída exclusiva:** `onda_incremental_dry_run/`

> **CONFIRMADO — normalização concluída com proveniência limpa.**
> Foram lidas seis fontes previamente inventariadas, escritas seis cópias
> derivadas e preservadas integralmente as fontes brutas.

## Resultado

| Verificação | Resultado |
|---|---:|
| Fontes brutas inventariadas | 6 |
| Hashes do piloto confirmados | 6/6 |
| Derivados normalizados escritos | 6 |
| Substituições rastreadas | 52 |
| Regras contextuais executadas | 0 |
| Itens de revisão/preservação executados | 0 |
| Alterações em `uploads_recepcao/` | **0** |
| Frontmatters preservados byte a byte | **6/6** |
| URLs preservadas | **6/6** |
| Idempotência do produto | **6/6** |
| Uso ou escrita em `normalizados_stt_dry_run/` | **0** |

## Censo das regras autorizadas

| Regra | DE | PARA | Trocas | Âncora canônica |
|---|---|---|---:|---|
| `STT-A01` | `anunaki` | **Anunnaki** | 6 | RC-024 — Anunnaki |
| `STT-A02` | `trimurte` / `trimurto` | **Trimurti** | 9 | RC-104 — Trimurti |
| `STT-A03` | `vismo` / `visma` / `vizno` | **Vishnu** | 20 | RC-135 — Vishnu (Mavatna) |
| `STT-A04` | `pachupati` / `pachupato` | **Pashupati** | 4 | RC-669 — Pashupati |
| `STT-A05` | `tikkun` | **Tikun** | 4 | RC-514 — Tikun Cósmico |
| `STT-A06` | `mohensof` / `mohenso` | **Mohen So** | 5 | RC-081 — Mohen So |
| `STT-A07` | `tirtankaras` | **Tirthankaras** | 1 | RC-397 — Tirthankaras |
| `STT-A08` | `tote` / `toth` | **Thoth** | 3 | RC-463/RC-534 — Thoth |

O censo de **52** coincide com a linha de base do piloto (52). Nenhuma
regra foi ampliada, nem foi inferida a partir de semelhança fonética.

## Manifesto de proveniência

| Derivado | Trocas | SHA-256 bruto | SHA-256 derivado |
|---|---:|---|---|
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 11 | `335a1b24cdcad1adb707e585c617a50dd277f550310abbbb35c328cf00d33134` | `74db4bc550f396607b06e586c3eefdd0ec591a95b05a03cafe230b4fe2b685f2` |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 23 | `d501d087d9113c91ee1cdf21b2ec7c1514252bc0acf69bf5881e988405f274fb` | `954dfba1d95dec7ec9116b50eff7c638b87d4694bbfef492c354dcc4f07a0f75` |
| `2025-07_002_lS8Bw-eaFYQ_A_Falencia_dos_Deuses_e_a_Destinacao_do_Lobo_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 15 | `260115a68f01c5c5d7a7669b8756624d0f0c74af28a47f42b998d6a67ba5b812` | `1153163ad88e48634165361f041e21ae9d40a4d90b42e2634e3f13727d531ab8` |
| `2025-07_035_JDaxXjYGyu0_Direitos_e_Deveres_Espirituais_VSC_10.md` | 1 | `4d6b32ef39504d28291d2e73f458c4af5a7fceaa220a74f037b11092dd4ca649` | `9083e18b80c67bd1fa6401152ebe3e3e3ea1918be2c016273dcb34894af55a35` |
| `2025-09_029_SzZtXArSltg_O_Quarto_Caminho_de_Gurdjieff_VSC_16.md` | 1 | `8656437f5b36dbb7e12b947584dacb8690d0d96415cfd6312fe87b8825fb3246` | `9bc6358bd93b44eb846e599a1d2a9dd657c858b3021162266aca49a9b71aa37d` |
| `2026-02_019_E2fBs7aocgU_O_Grande_Caminho_VSC_26.md` | 1 | `9d7e52325e556d5508f930ac4be32967bd3acbf9bfec1ed82f7c3892a323c33f` | `a68c477815c157e108fa960e4a9456435bbd4c890e701098455e98461a114173` |

Cada linha de `rastreio-antes-depois.jsonl` carrega o SHA da fonte, a posição
original (linha, coluna e offset), a regra, a âncora canônica e os contextos
antes/depois. Assim, a cópia derivada é auditável sem consultar o diretório
histórico de testes.

## Amostra do rastreio

| Arquivo | Posição no bruto | Regra | Antes | Depois |
|---|---|---|---|---|
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 209:61 | `STT-A02` | `Trimurte` | **Trimurti** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 209:159 | `STT-A02` | `Trimurte` | **Trimurti** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 255:559 | `STT-A01` | `Anunaki` | **Anunnaki** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 271:996 | `STT-A01` | `anunaki` | **Anunnaki** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 393:3508 | `STT-A01` | `Anunaki` | **Anunnaki** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 433:13 | `STT-A05` | `Tikkun` | **Tikun** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 451:594 | `STT-A03` | `Visma` | **Vishnu** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 455:263 | `STT-A01` | `anunaki` | **Anunnaki** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 457:50 | `STT-A01` | `anunaki` | **Anunnaki** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 473:2013 | `STT-A08` | `Toth` | **Thoth** |
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 473:2156 | `STT-A08` | `Tote` | **Thoth** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 91:69 | `STT-A01` | `anunaki` | **Anunnaki** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 129:8 | `STT-A03` | `Vizno` | **Vishnu** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 131:87 | `STT-A03` | `Visma` | **Vishnu** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 133:8 | `STT-A03` | `Visma` | **Vishnu** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 137:519 | `STT-A03` | `Vismo` | **Vishnu** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 139:28 | `STT-A03` | `Vismo` | **Vishnu** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 189:47 | `STT-A04` | `Pachupati` | **Pashupati** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 189:60 | `STT-A04` | `Pachupati` | **Pashupati** |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 191:166 | `STT-A04` | `Pachupato` | **Pashupati** |

## Limites vigentes antes do mapeamento temático

- Este resultado não é um cotejo com áudio e não altera o bruto STT.
- Somente as oito regras lexicais automáticas foram usadas.
- Sophia/Sofio por contexto, ambiguidades e itens preservados continuam fora do
  produto, sem decisão implícita.
- Não foram criados termos, relações, fichas, candidatos ou eixos.

**Próximo portão:** mapeamento dos eixos temáticos a partir destes derivados,
mediante orientação do Curador.
