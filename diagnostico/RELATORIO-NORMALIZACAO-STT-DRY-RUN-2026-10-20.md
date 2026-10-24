# Relatório de normalização STT — dry-run

**Data de geração:** 20/10/2026

**Executor:** `ferramentas/normalizar_stt_dry_run.py`

**Tabela aplicada:** `diagnostico/TABELA-NORMALIZACAO-STT-2026-10-20.md`

**Modo:** cópia derivada; **0 arquivos brutos alterados**.

## Escopo e guarda

Foram lidas as seis amostras Markdown de `uploads_recepcao/` e escritas cópias
em `normalizados_stt_dry_run/`. O processo usa apenas as oito regras
**AUTOMÁTICA** da seção 2.1 da tabela. Ele não aplica `Sophia` por contexto,
nem qualquer item de `REVISAR` ou `PRESERVAR / PENDENTE`.

- fontes brutas: **6**;
- cópias derivadas: **6**;
- substituições: **52**;
- alteração em `uploads_recepcao/`: **0**;
- idempotência das cópias geradas: **conferida**.

## Censo por regra

| Regra | DE | PARA | Ocorrências | Âncora oficial |
|---|---|---|---:|---|
| `STT-A01` | `anunaki` | **Anunnaki** | 6 | RC-024 — Anunnaki |
| `STT-A02` | `trimurte` / `trimurto` | **Trimurti** | 9 | RC-104 — Trimurti |
| `STT-A03` | `vismo` / `visma` / `vizno` | **Vishnu** | 20 | RC-135 — Vishnu (Mavatna) |
| `STT-A04` | `pachupati` / `pachupato` | **Pashupati** | 4 | RC-669 — Pashupati |
| `STT-A05` | `tikkun` | **Tikun** | 4 | RC-514 — Tikun Cósmico |
| `STT-A06` | `mohensof` / `mohenso` | **Mohen So** | 5 | RC-081 — Mohen So |
| `STT-A07` | `tirtankaras` | **Tirthankaras** | 1 | RC-397 — Tirthankaras |
| `STT-A08` | `tote` / `toth` | **Thoth** | 3 | RC-463/RC-534 — Thoth |

**Censo:** OK — coincide com o censo da tabela inicial (52 ocorrências).

## Manifesto de arquivos

| Fonte bruta | Linhas | SHA-256 original | SHA-256 cópia | Mudanças |
|---|---:|---|---|---:|
| `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 511 | 335a1b24cdcad1adb707e585c617a50dd277f550310abbbb35c328cf00d33134 | 74db4bc550f396607b06e586c3eefdd0ec591a95b05a03cafe230b4fe2b685f2 | 11 |
| `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 883 | d501d087d9113c91ee1cdf21b2ec7c1514252bc0acf69bf5881e988405f274fb | 954dfba1d95dec7ec9116b50eff7c638b87d4694bbfef492c354dcc4f07a0f75 | 23 |
| `2025-07_002_lS8Bw-eaFYQ_A_Falencia_dos_Deuses_e_a_Destinacao_do_Lobo_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` | 891 | 260115a68f01c5c5d7a7669b8756624d0f0c74af28a47f42b998d6a67ba5b812 | 1153163ad88e48634165361f041e21ae9d40a4d90b42e2634e3f13727d531ab8 | 15 |
| `2025-07_035_JDaxXjYGyu0_Direitos_e_Deveres_Espirituais_VSC_10.md` | 292 | 4d6b32ef39504d28291d2e73f458c4af5a7fceaa220a74f037b11092dd4ca649 | 9083e18b80c67bd1fa6401152ebe3e3e3ea1918be2c016273dcb34894af55a35 | 1 |
| `2025-09_029_SzZtXArSltg_O_Quarto_Caminho_de_Gurdjieff_VSC_16.md` | 343 | 8656437f5b36dbb7e12b947584dacb8690d0d96415cfd6312fe87b8825fb3246 | 9bc6358bd93b44eb846e599a1d2a9dd657c858b3021162266aca49a9b71aa37d | 1 |
| `2026-02_019_E2fBs7aocgU_O_Grande_Caminho_VSC_26.md` | 358 | 9d7e52325e556d5508f930ac4be32967bd3acbf9bfec1ed82f7c3892a323c33f | a68c477815c157e108fa960e4a9456435bbd4c890e701098455e98461a114173 | 1 |

Os SHA-256 são deliberadamente diferentes quando a cópia recebeu uma troca; a
proveniência fica verificável pelo diff e pelas linhas abaixo.

## Registro `antes → depois`

### `2024-07_005_L90vP0VFSTc_Enki_Enlil_e_o_Fim_Subito_da_Babilonia_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` — 11 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 255 | `STT-A01` | `Anunaki` | **Anunnaki** | …linguagem bíblica, essas duas expressões, Anakins e Enansins, é a mesma coisa que Anunaki e Neflin. O que é que eu estou querendo dizer? Que nessa Nesse período aí, a t… | …linguagem bíblica, essas duas expressões, Anakins e Enansins, é a mesma coisa que Anunnaki e Neflin. O que é que eu estou querendo dizer? Que nessa Nesse período aí, a t… |
| 271 | `STT-A01` | `anunaki` | **Anunnaki** | …e de lugarejos, de pequenas vilas, de povos nômades do deserto, que tinham sangue anunaki, da primeira investida deles antes do dilúvio. Mas que também, no período pós-… | …e de lugarejos, de pequenas vilas, de povos nômades do deserto, que tinham sangue Anunnaki, da primeira investida deles antes do dilúvio. Mas que também, no período pós-… |
| 393 | `STT-A01` | `Anunaki` | **Anunnaki** | …por Javé estavam fazendo com Abraão e Sara a mesma coisa que Anu na imbecilidade Anunaki fez com a irmã, não, isso aqui é sangue azul mas ali era uma regra monástica no c… | …por Javé estavam fazendo com Abraão e Sara a mesma coisa que Anu na imbecilidade Anunnaki fez com a irmã, não, isso aqui é sangue azul mas ali era uma regra monástica no c… |
| 455 | `STT-A01` | `anunaki` | **Anunnaki** | …o, tudo é o mais forte pegando o mais fraco. Então foi feita uma operação para um anunaki, fêmea, ter inserido na história lá deles um tipo de relação, mas aí foge o nosso… | …o, tudo é o mais forte pegando o mais fraco. Então foi feita uma operação para um Anunnaki, fêmea, ter inserido na história lá deles um tipo de relação, mas aí foge o nosso… |
| 457 | `STT-A01` | `anunaki` | **Anunnaki** | …í foge o nosso padrão humano. Essa raça é uma raça meio que biônica. Enfim, um anunaki engravidou e gauzu nasceu desse toque. sendo que essa raça biônica ia transferir… | …í foge o nosso padrão humano. Essa raça é uma raça meio que biônica. Enfim, um Anunnaki engravidou e gauzu nasceu desse toque. sendo que essa raça biônica ia transferir… |
| 209 | `STT-A02` | `Trimurte` | **Trimurti** | …tras locas também. Então era um período em que o conglomerado de realidades, a Trimurte, brigava com a geração de Zeus, que havia derrotado os titãs e que havia posto a… | …tras locas também. Então era um período em que o conglomerado de realidades, a Trimurti, brigava com a geração de Zeus, que havia derrotado os titãs e que havia posto a… |
| 209 | `STT-A02` | `Trimurte` | **Trimurti** | …a com a geração de Zeus, que havia derrotado os titãs e que havia posto a própria Trimurte de castigo, vamos assim dizer. Se tinha essas brigas entre os seres extrafísic… | …a com a geração de Zeus, que havia derrotado os titãs e que havia posto a própria Trimurti de castigo, vamos assim dizer. Se tinha essas brigas entre os seres extrafísic… |
| 451 | `STT-A03` | `Visma` | **Vishnu** | …na. e resolvendo assim a questão de como produzir um avatar humano da linhagem de Visma e de Sofia entre os humanos da história da Arca da Aliança que um dia eu vou cont… | …na. e resolvendo assim a questão de como produzir um avatar humano da linhagem de Vishnu e de Sofia entre os humanos da história da Arca da Aliança que um dia eu vou cont… |
| 433 | `STT-A05` | `Tikkun` | **Tikun** | …rspectiva de que nos é dado conhecer, passamos um dia a consertar. É o chamado Tikkun, que eu falo no livro Tzintzum, o exílio forçado e a endividade, que seria o cons… | …rspectiva de que nos é dado conhecer, passamos um dia a consertar. É o chamado Tikun, que eu falo no livro Tzintzum, o exílio forçado e a endividade, que seria o cons… |
| 473 | `STT-A08` | `Toth` | **Thoth** | …am entre os Anunnakis no Egito e na Suméria entre os clãs, o Ninji Gizida que é o Toth que é o Hermes primegisto, ou seja é o mesmo ser, se observado pelo nome sumério… | …am entre os Anunnakis no Egito e na Suméria entre os clãs, o Ninji Gizida que é o Thoth que é o Hermes primegisto, ou seja é o mesmo ser, se observado pelo nome sumério… |
| 473 | `STT-A08` | `Tote` | **Thoth** | …ervado pelo nome sumério você chama Ninji Gizida se você olha pelo nome egípcio é Tote, e se você olha pela tradição hermética esse ser é Hermes primegisto é difícil, m… | …ervado pelo nome sumério você chama Ninji Gizida se você olha pelo nome egípcio é Thoth, e se você olha pela tradição hermética esse ser é Hermes primegisto é difícil, m… |

### `2024-09_003_EbK2RfETyEM_Conspiracao_Demodharmica_-_Krishna_Jesus_e_Sai_Baba_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` — 23 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 91 | `STT-A01` | `anunaki` | **Anunnaki** | …erísticas. Mas uma mulher que era, entre aspas, obrigada a ter relações com um anunaki, um ijiji, um ser de fora, seja lá quem fosse, Zeus, esse ser que nascia dessa re… | …erísticas. Mas uma mulher que era, entre aspas, obrigada a ter relações com um Anunnaki, um ijiji, um ser de fora, seja lá quem fosse, Zeus, esse ser que nascia dessa re… |
| 367 | `STT-A02` | `Trimurte` | **Trimurti** | …essias violentos e levar os humanos pela violência para o controle de Braga. A Trimurte que havia criado Sofia como sendo representante da Trimurte e herdeiro das épocas… | …essias violentos e levar os humanos pela violência para o controle de Braga. A Trimurti que havia criado Sofia como sendo representante da Trimurte e herdeiro das épocas… |
| 367 | `STT-A02` | `Trimurte` | **Trimurti** | …ntrole de Braga. A Trimurte que havia criado Sofia como sendo representante da Trimurte e herdeiro das épocas porque era o único ser condenado à Trimurte título de prepo… | …ntrole de Braga. A Trimurte que havia criado Sofia como sendo representante da Trimurti e herdeiro das épocas porque era o único ser condenado à Trimurte título de prepo… |
| 367 | `STT-A02` | `Trimurte` | **Trimurti** | …epresentante da Trimurte e herdeiro das épocas porque era o único ser condenado à Trimurte título de preposto nesse universo biológico. O resto todo está lá. Depois do p… | …epresentante da Trimurte e herdeiro das épocas porque era o único ser condenado à Trimurti título de preposto nesse universo biológico. O resto todo está lá. Depois do p… |
| 369 | `STT-A02` | `Trimurte` | **Trimurti** | …nesse universo biológico. O resto todo está lá. Depois do problema de Jesus, a Trimurte não mais reconheceu Sofia a autoridade de suzerania que até então ele sempre exer… | …nesse universo biológico. O resto todo está lá. Depois do problema de Jesus, a Trimurti não mais reconheceu Sofia a autoridade de suzerania que até então ele sempre exer… |
| 129 | `STT-A03` | `Vizno` | **Vishnu** | …essas as duas teses centrais, não é só da mitologia ariana, são várias. Só que Vizno nunca brigou com Brahma disputando poder e também nunca brigou com Shiva disputan… | …essas as duas teses centrais, não é só da mitologia ariana, são várias. Só que Vishnu nunca brigou com Brahma disputando poder e também nunca brigou com Shiva disputan… |
| 131 | `STT-A03` | `Visma` | **Vishnu** | …o, mais uma vez, estava Shiva mantendo Brahma vivo, fazendo esse tipo de ardil. E Visma, então, diz para Brahma, olha, a China já está semeando no meio do DNA humano os… | …o, mais uma vez, estava Shiva mantendo Brahma vivo, fazendo esse tipo de ardil. E Vishnu, então, diz para Brahma, olha, a China já está semeando no meio do DNA humano os… |
| 133 | `STT-A03` | `Visma` | **Vishnu** | …humanas terão a marca de China. Aí Brahma disse, eu vou fazer o mesmo. Mas aí Visma disse, é só que você tem um problema, você é desalmado. A gente vai ver isso daqu… | …humanas terão a marca de China. Aí Brahma disse, eu vou fazer o mesmo. Mas aí Vishnu disse, é só que você tem um problema, você é desalmado. A gente vai ver isso daqu… |
| 137 | `STT-A03` | `Vismo` | **Vishnu** | …ramento Aí viram disse, já que o problema com o Enoque você não vai resolver, eu, Vismo, me ofereço para produzir um avatar seu. E foi assim que a ideia de Vismo prod… | …ramento Aí viram disse, já que o problema com o Enoque você não vai resolver, eu, Vishnu, me ofereço para produzir um avatar seu. E foi assim que a ideia de Vismo prod… |
| 139 | `STT-A03` | `Vismo` | **Vishnu** | …eu, Vismo, me ofereço para produzir um avatar seu. E foi assim que a ideia de Vismo produzir um avatar para ser usado a serviço de Jamel surgiu. Essa história, usand… | …eu, Vismo, me ofereço para produzir um avatar seu. E foi assim que a ideia de Vishnu produzir um avatar para ser usado a serviço de Jamel surgiu. Essa história, usand… |
| 197 | `STT-A03` | `Vismo` | **Vishnu** | …mais louvado pelos dravidianos que depois seriam os hindus que conhecemos um dia Vismo foi o ser mais louvado um dia Shiva foi o mais louvado hoje é Cristo hoje, nos úl… | …mais louvado pelos dravidianos que depois seriam os hindus que conhecemos um dia Vishnu foi o ser mais louvado um dia Shiva foi o mais louvado hoje é Cristo hoje, nos úl… |
| 199 | `STT-A03` | `Visma` | **Vishnu** | …ue ninguém reza mais para Brahma. Todo mundo reza para Cristo. Nem Brahma, nem Visma, nem Shiva nunca gostaram disso. Mas Cristo se estabeleceu como o Senhor Supremo… | …ue ninguém reza mais para Brahma. Todo mundo reza para Cristo. Nem Brahma, nem Vishnu, nem Shiva nunca gostaram disso. Mas Cristo se estabeleceu como o Senhor Supremo… |
| 201 | `STT-A03` | `Vismo` | **Vishnu** | …és de várias atitudes, Cristo cuida de cada um deles. Vaicunta é o nome do céu de Vismo que Cristo basicamente roubou para ele desde que Vismo se desconstituiu e como el… | …és de várias atitudes, Cristo cuida de cada um deles. Vaicunta é o nome do céu de Vishnu que Cristo basicamente roubou para ele desde que Vismo se desconstituiu e como el… |
| 201 | `STT-A03` | `Vismo` | **Vishnu** | …aicunta é o nome do céu de Vismo que Cristo basicamente roubou para ele desde que Vismo se desconstituiu e como ele é um filho de Vismo porque ele é uma bataca-chave, en… | …aicunta é o nome do céu de Vismo que Cristo basicamente roubou para ele desde que Vishnu se desconstituiu e como ele é um filho de Vismo porque ele é uma bataca-chave, en… |
| 201 | `STT-A03` | `Vismo` | **Vishnu** | …camente roubou para ele desde que Vismo se desconstituiu e como ele é um filho de Vismo porque ele é uma bataca-chave, então primeiro os EMAs ou os códigos fortes dos tr… | …camente roubou para ele desde que Vismo se desconstituiu e como ele é um filho de Vishnu porque ele é uma bataca-chave, então primeiro os EMAs ou os códigos fortes dos tr… |
| 497 | `STT-A03` | `Vismo` | **Vishnu** | …il expressões avatálicas do espírito dele, da condição a que agia dele, Shiva. Vismo não pode ter isso Porque vismo O espírito dele teve problema Que problema? O e… | …il expressões avatálicas do espírito dele, da condição a que agia dele, Shiva. Vishnu não pode ter isso Porque vismo O espírito dele teve problema Que problema? O e… |
| 497 | `STT-A03` | `vismo` | **Vishnu** | …írito dele, da condição a que agia dele, Shiva. Vismo não pode ter isso Porque vismo O espírito dele teve problema Que problema? O espírito dele perdeu o corpo hum… | …írito dele, da condição a que agia dele, Shiva. Vismo não pode ter isso Porque Vishnu O espírito dele teve problema Que problema? O espírito dele perdeu o corpo hum… |
| 501 | `STT-A03` | `Vismo` | **Vishnu** | …a dar conta Porque na época que Jesus nasceu Ainda existia ligado a esse espírito Vismo, morressor, Sofia Ou seja, vários seres todos ligados a um Espírito. No início, i… | …a dar conta Porque na época que Jesus nasceu Ainda existia ligado a esse espírito Vishnu, morressor, Sofia Ou seja, vários seres todos ligados a um Espírito. No início, i… |
| 703 | `STT-A03` | `Vismo` | **Vishnu** | …om a definição do Senhor Supremo assumida por Cristo. Nem Cristo, nem Brahma, nem Vismo gostaram da opção psíquica adotada por Saibaba, ainda que esta tenha sido apoiada… | …om a definição do Senhor Supremo assumida por Cristo. Nem Cristo, nem Brahma, nem Vishnu gostaram da opção psíquica adotada por Saibaba, ainda que esta tenha sido apoiada… |
| 189 | `STT-A04` | `Pachupati` | **Pashupati** | …partir do seu próprio genérico. Então, o senhor Shiva criou um senhor chamado Pachupati. E Pachupati gerou todos os animais que a gente conhece nesse universo vizinho, q… | …partir do seu próprio genérico. Então, o senhor Shiva criou um senhor chamado Pashupati. E Pachupati gerou todos os animais que a gente conhece nesse universo vizinho, q… |
| 189 | `STT-A04` | `Pachupati` | **Pashupati** | …u próprio genérico. Então, o senhor Shiva criou um senhor chamado Pachupati. E Pachupati gerou todos os animais que a gente conhece nesse universo vizinho, que depois...… | …u próprio genérico. Então, o senhor Shiva criou um senhor chamado Pachupati. E Pashupati gerou todos os animais que a gente conhece nesse universo vizinho, que depois...… |
| 191 | `STT-A04` | `Pachupato` | **Pashupati** | …m desse universo vizinho, E isso tudo é contado no Mahabharata, pois que o senhor Pachupato, junto com os seis filhos da geração regenerada de Brahma, criaram os animais que… | …m desse universo vizinho, E isso tudo é contado no Mahabharata, pois que o senhor Pashupati, junto com os seis filhos da geração regenerada de Brahma, criaram os animais que… |
| 733 | `STT-A05` | `Tikkun` | **Tikun** | …imon Bar Yashai, quando ele reconhecia que os humanos é que teriam que realizar o Tikkun, que é uma expressão kabbalística que chama-se reparo na obra e no Criador caído… | …imon Bar Yashai, quando ele reconhecia que os humanos é que teriam que realizar o Tikun, que é uma expressão kabbalística que chama-se reparo na obra e no Criador caído… |

### `2025-07_002_lS8Bw-eaFYQ_A_Falencia_dos_Deuses_e_a_Destinacao_do_Lobo_-_PALESTRA_COMPLETA_Jan_Val_Ellam.md` — 15 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 203 | `STT-A02` | `trimurte` | **Trimurti** | …ês seres nunca conseguiram matar uns aos outros, eles criaram um triunvirato, uma trimurte, uma tríade, uma trindade, porque eles eram os mais fortes mas Brahma não consegu… | …ês seres nunca conseguiram matar uns aos outros, eles criaram um triunvirato, uma Trimurti, uma tríade, uma trindade, porque eles eram os mais fortes mas Brahma não consegu… |
| 511 | `STT-A02` | `trimurte` | **Trimurti** | …Os lobos são mamíferos. É um desenvolvimento. A gente quer. Porque o sonho da trimurte e da descendência é um dia ter um era, um dia ter um nível de vida entre eles, qu… | …Os lobos são mamíferos. É um desenvolvimento. A gente quer. Porque o sonho da Trimurti e da descendência é um dia ter um era, um dia ter um nível de vida entre eles, qu… |
| 727 | `STT-A02` | `Trimurto` | **Trimurti** | …outros de uma forma muito superior ao padrão que antes havia encantado a própria Trimurto, quando percebeu que os mamíferos existiam, ele se encheu de alegria, mas a invej… | …outros de uma forma muito superior ao padrão que antes havia encantado a própria Trimurti, quando percebeu que os mamíferos existiam, ele se encheu de alegria, mas a invej… |
| 195 | `STT-A03` | `Vizno` | **Vishnu** | …nte vai precisar tomar para entender o resto, Quando foi decretada essa falência, Vizno, Shiva e Brahma se reuniram. Isso eu já contei em várias outras palestras e vamos… | …nte vai precisar tomar para entender o resto, Quando foi decretada essa falência, Vishnu, Shiva e Brahma se reuniram. Isso eu já contei em várias outras palestras e vamos… |
| 395 | `STT-A03` | `Vizno` | **Vishnu** | …efanta estava sentindo, o que é isso? Ou seja, quando os mamíferos surgiram, e Vizno e algumas expressões avatáricas que ele criou propositadamente para mexer na evol… | …efanta estava sentindo, o que é isso? Ou seja, quando os mamíferos surgiram, e Vishnu e algumas expressões avatáricas que ele criou propositadamente para mexer na evol… |
| 427 | `STT-A03` | `Vizno` | **Vishnu** | …e o vísgno e pediram para ele destruir os raksasas e organizar os sacrifícios. aí Vizno conversou com Shiva e os dois produziram um avatar à moda de Vizno mas com genéti… | …e o vísgno e pediram para ele destruir os raksasas e organizar os sacrifícios. aí Vishnu conversou com Shiva e os dois produziram um avatar à moda de Vizno mas com genéti… |
| 427 | `STT-A03` | `Vizno` | **Vishnu** | …acrifícios. aí Vizno conversou com Shiva e os dois produziram um avatar à moda de Vizno mas com genética dos dois chamado Rama Rama surge nessa cidade de Ayodhya que vai… | …acrifícios. aí Vizno conversou com Shiva e os dois produziram um avatar à moda de Vishnu mas com genética dos dois chamado Rama Rama surge nessa cidade de Ayodhya que vai… |
| 773 | `STT-A03` | `vizno` | **Vishnu** | …á fora observando. Quem mudou o divisor de águas dessa história foi o vísnulo. vizno quando mergulhou ele percebeu o problema só que ele não pôde fazer nada ele teve… | …á fora observando. Quem mudou o divisor de águas dessa história foi o vísnulo. Vishnu quando mergulhou ele percebeu o problema só que ele não pôde fazer nada ele teve… |
| 787 | `STT-A04` | `Pachupati` | **Pashupati** | …uros já macho e feio esse trabalho foi de Shiva Shiva que fez essa polaridade via Pachupati e via depois a geração regenerada de Brahma, pegou tudo que é animal que existe.… | …uros já macho e feio esse trabalho foi de Shiva Shiva que fez essa polaridade via Pashupati e via depois a geração regenerada de Brahma, pegou tudo que é animal que existe.… |
| 875 | `STT-A05` | `Tikkun` | **Tikun** | …am com seus próprios irmãos. E ele sempre quis comandar esse processo, que é o Tikkun, que é o nome cabalístico de reparo do DNA dele. Mas, nessa época, era muito clar… | …am com seus próprios irmãos. E ele sempre quis comandar esse processo, que é o Tikun, que é o nome cabalístico de reparo do DNA dele. Mas, nessa época, era muito clar… |
| 205 | `STT-A06` | `Mohenso` | **Mohen So** | …onde eu posso jogar esses códigos para lá e criar vida biológica. E foi daqui que Mohenso disse que iria criar mais um tipo de espécie de seres demos, só do tipo fenvã, e… | …onde eu posso jogar esses códigos para lá e criar vida biológica. E foi daqui que Mohen So disse que iria criar mais um tipo de espécie de seres demos, só do tipo fenvã, e… |
| 207 | `STT-A06` | `Mohenso` | **Mohen So** | …conglomerado de Yggdrasil, nesse universo vizinho, com o novo código genético que Mohenso conseguiu criar a partir da podridão de todos os códigos que ele rejuntou no mesm… | …conglomerado de Yggdrasil, nesse universo vizinho, com o novo código genético que Mohen So conseguiu criar a partir da podridão de todos os códigos que ele rejuntou no mesm… |
| 209 | `STT-A06` | `Mohenso` | **Mohen So** | …para a semeadura da vida biológica e a vida que hoje nós vemos é resultado do que Mohenso fez há cerca de 8, 7 bilhões de anos atrás. Qual o detalhe? Essa história aqui… | …para a semeadura da vida biológica e a vida que hoje nós vemos é resultado do que Mohen So fez há cerca de 8, 7 bilhões de anos atrás. Qual o detalhe? Essa história aqui… |
| 229 | `STT-A06` | `Mohensof` | **Mohen So** | …o nosso universo o universo biológico, o código dele veio pra cá, transferido por Mohensof, quando essa coisa se deu, que coisa a falência total de todos os planos de todos… | …o nosso universo o universo biológico, o código dele veio pra cá, transferido por Mohen So, quando essa coisa se deu, que coisa a falência total de todos os planos de todos… |
| 257 | `STT-A06` | `Mohenso` | **Mohen So** | …giu por acaso. Mas isso foi resultado da semeadura do projeto TALM do nosso amigo Mohenso, que mandou do universo vizinho de lá esse código para cá. E aqui na Terra, esse… | …giu por acaso. Mas isso foi resultado da semeadura do projeto TALM do nosso amigo Mohen So, que mandou do universo vizinho de lá esse código para cá. E aqui na Terra, esse… |

### `2025-07_035_JDaxXjYGyu0_Direitos_e_Deveres_Espirituais_VSC_10.md` — 1 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 144 | `STT-A07` | `Tirtankaras` | **Tirthankaras** | …r É um projeto que vem Quem quiser ir a fundo nisso Tem palestras minhas sobre os Tirtankaras que são expressões da religião mais antiga da Terra, que é o Jainismo. Os Tist… | …r É um projeto que vem Quem quiser ir a fundo nisso Tem palestras minhas sobre os Tirthankaras que são expressões da religião mais antiga da Terra, que é o Jainismo. Os Tist… |

### `2025-09_029_SzZtXArSltg_O_Quarto_Caminho_de_Gurdjieff_VSC_16.md` — 1 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 161 | `STT-A08` | `Tote` | **Thoth** | …va o Egito e outras regiões ali próximas, notadamente as cidades da Suméria. E Tote chega para o faraó e diz, tive uma ideia. E o faraó, qual foi? Estou desenvolvend… | …va o Egito e outras regiões ali próximas, notadamente as cidades da Suméria. E Thoth chega para o faraó e diz, tive uma ideia. E o faraó, qual foi? Estou desenvolvend… |

### `2026-02_019_E2fBs7aocgU_O_Grande_Caminho_VSC_26.md` — 1 mudança(s)
| Linha | Regra | Antes | Depois | Contexto antes | Contexto depois |
|---:|---|---|---|---|---|
| 252 | `STT-A05` | `tikkun` | **Tikun** | …e vai ser a base do nascimento desse novo ser humano que um dia poderá realizar o tikkun, que é o conserto tanto na natureza doentia quanto no que restou do eu caído do c… | …e vai ser a base do nascimento desse novo ser humano que um dia poderá realizar o Tikun, que é o conserto tanto na natureza doentia quanto no que restou do eu caído do c… |



## Limites deste resultado

- A cópia normalizada não substitui nem corrige o bruto STT.
- O relatório não afirma cotejo com áudio; ele registra a aplicação de um
  vocabulário já ancorado na Base.
- Qualquer ampliação de regra deve primeiro entrar na tabela de normalização,
  com regime e evidência próprios.
