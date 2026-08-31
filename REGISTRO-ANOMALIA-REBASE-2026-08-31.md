# REGISTRO DE ANOMALIA — REBASE DE 2026-08-31 (LIMPEZA Nº 10 PENDENTE)

**Data:** 2026-08-31
**Operador:** Arena.ai Agent Mode (MiniMax-M3)
**Branch:** `arena/01a04eee-termos-rc`
**Status:** DOCUMENTADO, NÃO RESOLVIDO

---

## Resumo

Em 2026-08-31, durante o processamento de 4 palestras consecutivas (P2017-05-14, P2018-05-20, P2019-04-14 e a auditoria), foi detectado que a pasta `uploads_recepcao/` continha **42 arquivos .txt** que deveriam ter sido deletados pelos commits `c2d838dd` (P2019-05-11) e `c11976e` (P2023-11-11) — commits esses que ficaram em estado "unreachable" no `.git/objects` do sandbox após múltiplos rebases do branch remoto upstream.

## Causa Raiz

1. **O branch remoto foi reescrito 4 vezes** entre 30/08 18h e 31/08 00h (cada `git push --force` invalidou commits anteriores).
2. **O curador anterior** (outra instância do agente) processou P2019-05-11 e P2023-11-11 em 30/08 22h22 e 22h26, fazendo **limpezas massivas** (36+36 arquivos removidos do `uploads_recepcao/`).
3. **Esses commits de limpeza ficaram em "unreachable"** porque o branch upstream continuou sendo reescrito.
4. **Quando o agente atual fez `git pull --rebase`** no início da sessão, o git moveu o commit do agente (P2017-05-14) para DEPOIS do commit de upload (78fd3cb), mas **NÃO reaplicou as deleções dos commits unreachable** (porque elas não faziam parte do branch puxado).
5. **Resultado:** os 42 arquivos .txt voltaram para `uploads_recepcao/`, mesmo já existindo cópias idênticas (SHA-256) em `apostilas/CONCLUIDAS/`.

## Estado atual

| Item | Valor |
|---|---|
| **HEAD remoto** | `d889068` |
| **Pastas em CONCLUIDAS** | 79 (todas com SHA-256 verificado) |
| **Pastas no INVENTARIO** | 79 (sincronizado) |
| **Arquivos em `uploads_recepcao/`** | 42 .txt + 7 .json + 1 README + 1 .gitkeep = **51 arquivos** |
| **Arquivos em `uploads_recepcao/` que DEVERIAM ter sido deletados** | 41 (todos com SHA-256 idêntico ao `original.txt` em CONCLUIDAS) |
| **Arquivo em `uploads_recepcao/` que DEVE FICAR** | `2023-12-17 Lúcifer e a Rebelião dos Elétrons.txt` (fonte do ciclo leve `ciclos/P2023-12-17/`) |

## Diagnóstico verificado

- `git fsck --unreachable` confirmou que `c2d838dd` e `c11976e` (as limpezas massivas) estão em `.git/objects/` mas não no branch
- `git show c2d838dd -- uploads_recepcao/` mostrou que ele removeu 36 arquivos de uma vez
- `git show c11976e -- uploads_recepcao/` mostrou que ele removeu outros 36
- O branch atual (`d889068`) tem 51 arquivos em `uploads_recepcao/`, mas o curador anterior pretendia deixar apenas 5-7

## Decisão (Opção C)

Por instrução do usuário em 2026-08-31, foi escolhida a **Opção C**: **apenas documentar** e seguir o fluxo de processamento das palestras pendentes, deixando a limpeza massiva para uma sessão futura (talvez em uma janela de manutenção).

## Consequências conhecidas

- O repositório tem 41 arquivos "duplicados" (no `uploads_recepcao/` e em `apostilas/CONCLUIDAS/*/original.txt`)
- O `uploads_recepcao/` está com **~9 MB** de espaço desperdiçado (estimativa)
- O comportamento do agente durante o fluxo (puxar a próxima palestra) **NÃO** é afetado — o agente sempre busca a palestra em `uploads_recepcao/`, processa e tenta deletá-la
- Cada palestra que o agente processar DEVE deletar seu próprio upload (mas o problema é que o agente não sabe que DEVERIA deletar também os outros 41)

## Recomendações para próxima janela de manutenção

1. **Fazer a limpeza massiva** (Opção A) — `git rm` os 41 arquivos duplicados
2. **Adicionar regra no fluxo do agente:** ao processar a 1ª palestra de uma sessão, SEMPRE fazer `git pull --rebase` antes, e verificar se há inconsistências em `uploads_recepcao/`
3. **Considerar `.gitignore`** em `uploads_recepcao/*.txt` para evitar que o curador humano adicione arquivos lá sem querer

## Anexo: Lista dos 41 arquivos que DEVERIAM ter sido deletados

```
2017-14-05 - O Desvio de Rota de Pandora e o Quarto Logos Universal.txt  (data STT corrompida)
2018-02-24 - Pandora e a Estratégia dos Avatares.txt
2018-05-20 - De Pandora a Eva e o culto a Lilith.txt
2018-10-06 - Humanidade em Disputa a Descendência de Pandora.txt
2019-04-14 - Javé versus Pandora A Prole sem Face.txt
2019-05-11 - Pandora e os Desacertos dos Pactos de Javé.txt
2020-04-18 - Terra em Disputa o marco zero de Sophia.txt
2020-04-25 - Os Desdobramentos da Rebelião de Lúcifer.txt
2020-05-09 - Sophia e o Juizo Final.txt
2020-07-04 – A Hierarquia Fraturada dos Anjos do Criador, as Hostes de Sophia.txt
2020-08-08 - Sophia e o Alinhamento Interdimensional do Moscoviano Tempos anteriores ao de Capela.txt
2020-09-19 - Sophia e o Impasse do Juízo Final.txt
2021-03-13 - Sophia e o Ragnarok.txt
2021-05-08 - As Convenções Mentais de Sophia.txt
2021-05-15 - As Etnias Hiperboreas e os Anunnakis.txt
2021-07-24 - Sophia, Ananque e as Necessidades Cósmicas.txt
2021-09-04 - Sophia e as Demais Singularidades da Criação.txt
2022-03-26 A Rebelião de Lúcifer e a Depressão Mental dos Seres.txt
2022-09-24 - Sophia, os Arcontes e a Disputa pela Suzerania Universal.txt
2023-04-01 - O Quarto Logos e seus agentes.txt
2023-04-01 - Reintegração Cósmica Tempo de Ruptura.txt
2023-04-15 - Desafio Crucial O Alinhamento do Espírito de Jesus.txt
2023-04-29 - Jesus Sophia e Javé as Responsabilidades de um mesmo Ser.txt
2023-04-30 - O Senhor Krishna e as Expressões do Ser.txt
2023-05-20 - As Batalhas do Final dos Tempos.txt
2023-05-21 - A Hebdômoda de Apolo_O Ultraje Humano.txt
2023-06-03 - Os Bastidores da Ressureição de Jesus.txt
2023-06-17 - O Paradoxo Divino.txt
2023-06-24 - O Buraco Negro Mental e o Estacionamento Coletivo.txt
2023-06-25 - A Proposta de Salvação do Senhor Krishna.txt
2023-07-05 - O Despertar dos Potenciais da Consciência Pessoal.txt
2023-07-30 - A Leitura Adulta da Realidade.txt
2023-08-05 - O Velho Sonho de Ares.txt
2023-09-09 -O Colapso da Trimurte e Suas Consequências.txt
2023-10-14 - A Esquecida Honra dos Anunnaki.txt
2023-11-11 - De Pandora a Eva e a Rebelião de Lilith.txt
2023-11-19 - A Máquina da Criação O Desmonte do Mundo.txt
2023-12-03 - A Rebelião de Lúcifer ainda por ser Finalizada.txt
2024-11-03 - Apolônio de Tiana e o Quarto Logos.txt
2025-02-22 - A Vinda de Sophia e o Equilíbrio Universal.txt
2025-07-18 - Javé, Sophia e as Sincronicidades Profetizáveis.txt
```

**Arquivo que DEVE FICAR (fonte do ciclo leve):**
```
2023-12-17 Lúcifer e a Rebelião dos Elétrons.txt  →  ciclos/P2023-12-17/original.txt
```

---

---

## ⚠️ SUPERAÇÃO (2026-08-31, AGENTE 15)

A **"Opção C"** (documentar e manter os 42 .txt) foi **superada por ordem do curador** na sessão seguinte (AGENTE 15, branch `arena/01a05591-termos-rc`):

- O curador pediu **limpeza total** de `uploads_recepcao/` antes de subir a próxima palestra.
- Verificação prévia: os **43 .txt** presentes tinham, **cada um**, uma pasta correspondente em `apostilas/CONCLUIDAS/` com `original.txt` **SHA-256 idêntico** (0 órfãos, 0 divergências).
- Inclui o `2026-08-04 - O QUE NÃO TE CONTARAM SOBRE ALIENÍGENAS E A BÍBLIA.txt`, que chegou à pasta por engano (ficou solto na raiz e foi movido por `git mv` no commit anterior) — já estava processado na pasta `2026-08-04_irmaos-dias-podcast_aliens_biblia`.
- O ciclo leve `P2023-12-17` **não é afetado**: a fonte permanece preservada em `ciclos/P2023-12-17/original.txt` (e a cópia da apostila em `apostilas/CONCLUIDAS/2023-12-17_lucifer_e_a_rebeliao_dos_eletrons/original.txt` é SHA-idêntica).
- Resultado: **43/43 removidos** via `git rm` + commit; nada se perde irreversivelmente (cópias versionadas + histórico Git).
- Registro da operação: `uploads_recepcao/REGISTRO-LIMPEZA-2026-08-31-11.json` (SHA-256 e bytes computados, 43/43 com `copia_identica: true`).

**Curadoria:** Arena.ai Agent Mode (MiniMax-M3)
**Versão:** 1.0
