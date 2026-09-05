# uploads_recepcao/ — o canal de recepção bruto

**Política (instituída em 2026-08-26 por ordem do curador):** esta pasta é o
**caixa de entrada** de material bruto (PDFs, TXTs de palestras, etc.) subido
pelo curador — o canal que sempre funcionou.

## O ciclo de vida de um arquivo recebido

1. O arquivo chega aqui (upload do curador na branch da sessão);
2. O ciclo da obra/palestra o processa e **copia byte a byte** para
   `livros/B0NN_slug/original.pdf|.txt`, `livros/AMOSTRAS/...` ou
   `apostilas/CONCLUIDAS/AAAA-MM-DD_slug/original.txt|original.pdf`
   (com SHA-256 registrado na ficha de ingresso);
3. Comprovada a cópia idêntica (SHA a SHA), **o bruto pode ser removido daqui**.

## Limpezas

- **2026-08-26 (limpeza nº 1):** 45 arquivos (79,7 MB) removidos após auditoria
  SHA a SHA — **45/45 com cópia idêntica versionada** em seus destinos
  (41 ciclos de livros + 2 amostras + 1 apostila P2024-05-04 + o mapa B050 +
  o B060...; o PDF do Prabrajna foi copiado para a pasta da apostila antes da
  remoção, cumprindo o padrão `original.pdf` + `original.txt`).
- **2026-08-30 (limpeza nº 2):** 36 arquivos de palestras (4,11 MB) removidos
  para iniciar a **Nova Fase** (após a operação v3.1-MP completar 73/73
  apostilas). Auditoria SHA-a-SHA revelou **37 divergências** entre a versão
  em `uploads_recepcao/` (HEAD remoto) e a cópia local em
  `apostilas/CONCLUIDAS/*/original.txt` — as versões locais foram copiadas de
  uma versão intermediária, depois o remoto foi sobrescrito. Por decisão do
  curador (2026-08-30), os arquivos do remoto foram removidos mesmo com
  divergência — as versões do remoto permanecem **recuperáveis via histórico
  Git** (nada se perde irreversivelmente). Registro completo em
  [`REGISTRO-LIMPEZA-2026-08-30.json`](./REGISTRO-LIMPEZA-2026-08-30.json)
  (SHA-256, bytes e nomes de todos os 36 arquivos removidos).
- Os arquivos removidos **permanecem recuperáveis no histórico Git** (nada se
  perde irreversivelmente).
- **2026-08-30 (limpeza nº 3):** palestra `2019-05-11 - Pandora e os
  Desacertos dos Pactos de Javé.txt` (129KB) foi processada para v3.1-MP
  em `apostilas/CONCLUIDAS/2019-05-11_pandora_e_os_desacertos_dos_pactos_de_jave/`
  e removida daqui. Causa-raiz do desencontro: commit `7140ad5` no remoto só
  foi capturado pelo `git fetch` local após 3+ horas — recomenda-se
  `git fetch origin arena/01a04eee-termos-rc` explícito em vez de assumir
  que `git fetch` genérico já trouxe tudo. Registro completo em
  [`REGISTRO-LIMPEZA-2026-08-30-3.json`](./REGISTRO-LIMPEZA-2026-08-30-3.json).
- **2026-08-30 (limpeza nº 4):** palestra `2023-11-11 - De Pandora a Eva e
  a Rebelião de Lilith.txt` (89KB) foi processada para v3.1-MP em
  `apostilas/CONCLUIDAS/2023-11-11_de_pandora_a_eva_e_a_rebeliao_de_lilith/`
  e removida daqui. **WORKAROUND CONFIRMADO:** o `git fetch origin
  refs/heads/arena/01a04eee-termos-rc:refs/remotes/origin/arena/01a04eee-termos-rc`
  explícito capturou o commit `168b4ef` imediatamente — o `git fetch origin`
  genérico não traz refs novos. Registro completo em
  [`REGISTRO-LIMPEZA-2026-08-30-4.json`](./REGISTRO-LIMPEZA-2026-08-30-4.json).

## Quarentena de divergências SHA (limpeza nº 2)

⚠️ **37 palestras** têm SHA-256 diferente entre a versão em
`apostilas/CONCLUIDAS/*/original.txt` (local) e a versão correspondente que
estava em `uploads_recepcao/` (remoto, antes da limpeza nº 2). Lista
completa em `REGISTRO-LIMPEZA-2026-08-30.json`. Se alguma palestra tiver
problemas de grafia/typo na versão local, a versão "oficial" do remoto pode
ser recuperada com:

```bash
# Exemplo: recuperar a versão do remoto de uma palestra específica
git show 74a8fc4:uploads_recepcao/2020-04-18\ -\ Terra\ em\ Disputa\ o\ marco\ zero\ de\ Sophia.txt > /tmp/recuperado.txt
diff /tmp/recuperado.txt apostilas/CONCLUIDAS/2020-04-18_terra_em_disputa_o_marco_zero_de_sophia/original.txt
```

Se a versão do remoto for considerada "correta", sobrescrever o local com:

```bash
git show 74a8fc4:uploads_recepcao/<caminho-com-aspas> > apostilas/CONCLUIDAS/<pasta-local>/original.txt
```

## Estado atual

**PASTA LIMPA** — pronta para receber o material da **Nova Fase** (próxima
palestra do tema Pandora). Apenas arquivos de metadados restam:

- `README.md` (este arquivo — política institucional)
- `REGISTRO-LIMPEZA-2026-08-30.json` (auditoria da limpeza nº 1)
- `REGISTRO-LIMPEZA-2026-08-30-3.json` (auditoria da limpeza nº 3)
- `REGISTRO-LIMPEZA-2026-08-30-4.json` (auditoria da limpeza nº 4)
- `REGISTRO-LIMPEZA-2026-08-30-5.json` … `-9.json` (auditoria das limpezas nº 5 a 9)
- `REGISTRO-LIMPEZA-2026-08-30-10.json` (auditoria da limpeza nº 10)
- `REGISTRO-LIMPEZA-2026-08-31-11.json` (auditoria da limpeza nº 11 — esvaziamento integral)

## Limpeza nº 11 (2026-08-31 — esvaziamento integral)

Por ordem do curador, os **43 .txt** restantes foram removidos — todos com
cópia **byte-idêntica (SHA-256)** em `apostilas/CONCLUIDAS/<pasta>/original.txt`
e recuperáveis no histórico Git. Registro completo (SHA, bytes, destino) em
[`REGISTRO-LIMPEZA-2026-08-31-11.json`](./REGISTRO-LIMPEZA-2026-08-31-11.json).
A caixa de entrada está **zerada** e pronta para a próxima palestra.

## Limpeza nº 12 (2026-09-02 — esvaziamento dos .txt de palestras já processadas)

Auditoria **SHA-256 byte-a-byte** de todos os `.txt` desta pasta contra os `original.txt`
versionados em `ciclos/*/`, `apostilas/CONCLUIDAS/*/` e `livros/**/`. Resultado:

- **34 .txt removidos** — cada um com cópia **byte-idêntica (SHA-256)** já versionada no
  repositório (destinos registrados um a um). Total de **4.033.557 bytes** liberados.
  Registro completo em [`backups/REGISTRO-LIMPEZA-2026-09-02.json`](../backups/REGISTRO-LIMPEZA-2026-09-02.json).
- **2 .txt RETIDOS** (sem cópia byte-idêntica no repositório → não removidos, conforme política):
  1. `2024-03-02 - O Drama Espiritual de Jesus.txt` (109.709 B) — **versão divergente** do
     `original.txt` de `ciclos/P2024-03-02` (111.154 B). Requer decisão do curador
     (qual é a versão canônica / se a versão desta pasta deve ser versionada antes de remover).
  2. `2025-06-14 - PALESTRA SOBRE A QUEDA DO CRIADOR.txt` (13.180 B) — **fragmento cru** (título +
     um trecho) do conteúdo já processado na versão "-Refatorada" (`ciclos/P2025-06-14`).
     Conteúdo não-idêntico à versão versionada; requer decisão do curador.

- **2 .txt retidos na limpeza nº 12** foram, em 02/09/2026, **descartados por decisão do
  curador** (conteúdo já processado; versões divergentes/fragmentos sem valor de preservação):
  `2024-03-02 - O Drama Espiritual de Jesus.txt` e
  `2025-06-14 - PALESTRA SOBRE A QUEDA DO CRIADOR.txt`. Ambos **recuperáveis no histórico git**
  (estavam versionados em `uploads_recepcao/`). Registro em
  [`backups/REGISTRO-LIMPEZA-2026-09-02-DESCARTE-CURADOR.json`](../backups/REGISTRO-LIMPEZA-2026-09-02-DESCARTE-CURADOR.json).

## ⚠️ Regras da esteira (Família F — vigentes desde o F032, 05/09/2026)

> **Alerta: docs-síntese preenchem deliberadamente lacunas «nome ??» das fontes primárias com erudição externa. Validar toda lista contra B060.**
> (precedente F032 D-1: «Amenophis» sobre o sacerdote de Mernephta de B060; «Quirinius» onde o corpus grafa Longino; Ellam Yua/Yup'ik, Jan Huss, Tróia, Krsnavapalyana — todos 0 hits). A regra-mãe segue: nenhum compilador substitui a fonte primária; docs-síntese nunca são âncora de aspa, data, identidade ou STATUS.

**Estado da pasta (atualizado em 05/09/2026 — limpezas nº 14 e nº 15 EXECUTADAS):** a caixa voltou ao regime de **entrada bruta**: os quatro brutos da Família F com ciclo concluído foram **removidos** por comando final do curador (Q-F031-G), cada um previamente auditado SHA-a-SHA contra sua cópia versionada.

| Arquivo | Situação |
|---|---|
| `LISTA SIMPLES DE TERMOS CHAVE DA RC.txt` | **permanece na caixa** — auditoria de cobertura em `VERIFICACAO-DE-COBERTURA-LISTA-SIMPLES-2026-09-04.md`, mas **sem cópia byte a byte versionada**: não-apta à remoção sob a política vigente |

**Brutos removidos nos registros nº 14–15** (cópias canônicas vivem em `consolidacoes/*/fonte.txt`; histórico byte-a-byte recuperável no git — p.ex. `git show d8bb396:"uploads_recepcao/22-GLOSSÁRIO.txt"`):

| Bruto removido | Ciclo | Cópia canônica |
|---|---|---|
| `22-GLOSSÁRIO.txt` | **F022** (concluído 04/09/2026) | `consolidacoes/F022_22-glossario/fonte.txt` · SHA `8968eab3…` |
| `29-PERSONAGENS DA REVELAÇÃO CÓSMICA.txt` | **F029** (concluído) | `consolidacoes/29-PERSONAGENS/fonte.txt` · SHA `e8274acc…` |
| `Colégio Druídico — Estudo Continuad.txt` | **F030** (CONCLUÍDO 05/09/2026 — aplicação: RC-032 Benem arestado via B018; fichas RC-398/RC-068/RC-403/RC-437 ampliadas) | `consolidacoes/F030_colegio-druidico/fonte.txt` · SHA `36b35d46…` |
| `1-EDR-O Livro.txt` | **F031** (CONCLUÍDO 05/09/2026 — aplicação do despacho Q-F031-A…G: RC-930/931/932 na fila, 7 arestas, bloco QUATRO MÉTODOS na ficha RC-755, blindagem D-1 em RC-142/RC-074) | `consolidacoes/F031_edr-livro/fonte.txt` · SHA `d629befd…` |
| `10 - Moros – O Livro.txt` | **F032** (CONCLUÍDO 05/09/2026 — auditoria-pura da Rede Moros; aplicação: RC-933 «Revelação Psíquica (Kapila — Samkhya)» na fila, aresta RC-777→RC-716, Súdices no RC-467, blindagem de identidades na RC-454, RC-930 += P2024-11-30, retificação do ledger F031; **removido no registro nº 15**) | `consolidacoes/F032_moros-livro/fonte.txt` · SHA `ea856120…` |

- **Limpeza nº 13 PREPARATORADA (despacho F030/Q-F030-F, 05/09/2026):** auditoria SHA-a-SHA da Família F em [`backups/REGISTRO-LIMPEZA-2026-09-05-13.json`](../backups/REGISTRO-LIMPEZA-2026-09-05-13.json) — nenhum arquivo removido na época; 3 aptos + 1 não-apto.
- **Limpeza nº 14 EXECUTADA (despacho F031/Q-F031-G, 05/09/2026):** [`backups/REGISTRO-LIMPEZA-2026-09-05-14.json`](../backups/REGISTRO-LIMPEZA-2026-09-05-14.json) — SHA-256 re-conferido imediatamente antes do `rm`; **4 removidos · 0 divergências**; `LISTA SIMPLES` preservada. A política segue: **nenhum bruto sai daqui sem cópia versionada byte-idêntica + comando final do curador.** Executada em 05/09/2026 pelo Q-F032-F (registro nº 15: 1 removido, SHA re-conferido byte a byte antes do `rm`).
