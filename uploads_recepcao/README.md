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
| `11 - Mohen So – O Livro.txt` | **F033** (CONCLUÍDO 05/09/2026 — aplicação do despacho Q-F033-A…F: seis notas de ficha estritas às âncoras (RC-081/092/154/454/535/282) + aresta RC-081→gera→RC-064; 36/36 núcleo-alegações ancoradas; **removido no registro nº 16**) | `consolidacoes/F033_mohen-so-livro/fonte.txt` · SHA `5e1c599c…` |
| `12 - Fenvans - A Gênese Nanotecnológica e o Sacrifício Cósmico.txt` | **F034** (CONCLUÍDO 05/09/2026 — homologado **documento-espelho**: 100% verbatim ao corpus (299/299 linhas; 292/299 na apostila-mãe P2025-08-03), 52/52 sondas ancoradas, saldo 0 termos/0 relações; aplicação: retificação D-5 do ledger F032 + nota sem blindagem só na RC-658 («teia ~9 bi», apostila ll. 826/882); REVISAR «autora do Apocalipse» mantido; **removido no registro nº 17**) | `consolidacoes/F034_fenvans-livro/fonte.txt` · SHA `b7d084bd…` |
| `13 - Fornos Replicadores-Refatorado.txt` | **F035** (CONCLUÍDO 05/09/2026 — homologado **documento-fonte da série refatorada**: 63/63 linhas verbatim no original.txt do cluster P2025-08-01; ciclo de VERIFICAÇÃO com saldo 0 termos/0 relações; aplicação: [REVISAR B050] ENCERRADO na RC-102 (mergulho ~12,17 bi + corte da cabeça 11,6 bi a.p., B050 ll. 67/69 verbatim) e nota de amarração no RC-408 (Eros · Terceiro Logos · período 9,7–9,5 bi a.p.); supressão «Talm=Nidana» mantida; **removido no registro nº 18**) | `consolidacoes/F035_fornos-replicadores-refatorado/fonte.txt` · SHA `f1c9926c…` |
| `14 - Projeto TALM – O Livro.txt` | **F036** (CONCLUÍDO 05/09/2026 — homologado **documento-FONTE do cluster P2025-08-02**: corpo byte-a-byte igual ao `original.txt` da apostila, diff = só o wrapper de cabeçalho; 250/250 linhas ≥80c e 393/393 citações verbatim — recorde da série; ciclo de VERIFICAÇÃO com saldo 0 termos/0 relações; cotejo B050 homologou TALM 7,7 bi (nota única na RC-091, `[REVISAR]` da l. 65 mantido por decisão expressa), revalidou Mohen So 7,8 bi e Nidana 3,8 bi, certificou Olm 6–7 bi como não-encerrável (RC-092 intocada); supressões do andaime pedagógico averbadas como formato; **removido no registro nº 19**) | `consolidacoes/F036_projeto-talm-livro/fonte.txt` · SHA `b9ad623e…` |

- **Limpeza nº 13 PREPARATORADA (despacho F030/Q-F030-F, 05/09/2026):** auditoria SHA-a-SHA da Família F em [`backups/REGISTRO-LIMPEZA-2026-09-05-13.json`](../backups/REGISTRO-LIMPEZA-2026-09-05-13.json) — nenhum arquivo removido na época; 3 aptos + 1 não-apto.
- **Limpeza nº 14 EXECUTADA (despacho F031/Q-F031-G, 05/09/2026):** [`backups/REGISTRO-LIMPEZA-2026-09-05-14.json`](../backups/REGISTRO-LIMPEZA-2026-09-05-14.json) — SHA-256 re-conferido imediatamente antes do `rm`; **4 removidos · 0 divergências**; `LISTA SIMPLES` preservada. A política segue: **nenhum bruto sai daqui sem cópia versionada byte-idêntica + comando final do curador.** Executada em 05/09/2026 pelo Q-F032-F (registro nº 15: 1 removido, SHA re-conferido byte a byte antes do `rm`).

## Limpeza nº 16 (2026-09-05 — F033 · «Mohen So – O Livro»)

Por despacho Q-F033-F, o bruto `11 - Mohen So – O Livro.txt` foi **removido** após re-conferência byte a byte do SHA-256 (`5e1c599c…`) contra `consolidacoes/F033_mohen-so-livro/fonte.txt`. Registro completo em `backups/REGISTRO-LIMPEZA-2026-09-05-16.json`. F033 é o **6º arquivo apto** da Família F. A caixa retorna ao regime de entrada bruta; `LISTA SIMPLES` permanece, não-apta. O alerta contra preenchimento de «nome ??» mantém-se vigente — e, nota histórica: foi a primeira vez que um volume da série «O Livro» passou nele limpo.

## Limpeza nº 17 (2026-09-05 — F034 · «Fenvans - A Gênese Nanotecnológica e o Sacrifício Cósmico»)

Por despacho Q-F034-E, o bruto `12 - Fenvans - A Gênese Nanotecnológica e o Sacrifício Cósmico.txt` foi **removido** após **re-conferência tripla** do SHA-256 (`b7d084bd…`) — `sha256sum` do bruto × `hashlib` da cópia canônica × hash de stream em blocos do bruto, os três idênticos a 141.502 B — contra `consolidacoes/F034_fenvans-livro/fonte.txt`. Registro completo em `backups/REGISTRO-LIMPEZA-2026-09-05-17.json`. F034 é o **7º arquivo apto** da Família F e o **primeiro da série «— O Livro» encerrado com saldo zero na base**: o documento era um espelho literal do cluster 2025-08 (299/299 linhas verbatim), e o único movimento de conteúdo que produziu foi a retificação Q-B (cifra «Wyrd ≈ 9 bi» restaurada no ledger F032, averbada na RC-658). A caixa retorna ao regime de entrada bruta; `LISTA SIMPLES` permanece, não-apta. O alerta contra preenchimento de «nome ??» mantém-se vigente.

## Limpeza nº 18 (2026-09-05 — F035 · «Fornos Replicadores-Refatorado»)

Por despacho Q-F035-F, o bruto `13 - Fornos Replicadores-Refatorado.txt` foi **removido** após **re-conferência tripla** do SHA-256 (`f1c9926c…` — `sha256sum` do bruto × `hashlib` da cópia canônica × hash de stream em blocos do bruto, os três idênticos a 25.845 B) contra `consolidacoes/F035_fornos-replicadores-refatorado/fonte.txt`. Registro completo em `backups/REGISTRO-LIMPEZA-2026-09-05-18.json`. F035 é o **8º arquivo apto** da Família F e o primeiro homologado como **documento-fonte** (e não reciclagem, como o F034): as 63 linhas batem 100% com o `original.txt` da apostila P2025-08-01, e o saldo do ciclo foi de VERIFICAÇÃO — o «[REVISAR — conferir B050]» que a ficha RC-102 carregava desde 2025 foi oficialmente encerrado com a data cravada na fonte (l. 67), e o alias Eros amarrado no RC-408. A caixa retorna ao regime de entrada bruta; `LISTA SIMPLES` permanece, não-apta. O alerta contra preenchimento de «nome ??» mantém-se vigente.

## Limpeza nº 19 (2026-09-05 — F036 · «Projeto TALM – O Livro»)

Por despacho Q-F036-F, o bruto `14 - Projeto TALM – O Livro.txt` — nome grafado com **travessão** («TALM – O Livro»), distinto do hífen do nº 13 — foi **removido** após **re-conferência tripla** do SHA-256 (`b9ad623e…` — `sha256sum` do bruto × `hashlib` da cópia canônica × hash de stream em blocos do bruto, os três idênticos a 121.388 B) contra `consolidacoes/F036_projeto-talm-livro/fonte.txt`. Registro completo em `backups/REGISTRO-LIMPEZA-2026-09-05-19.json`. F036 é o **9º arquivo apto** da Família F e o segundo homologado como **documento-FONTE**: o corpo bate 100% com o `original.txt` da apostila P2025-08-02 (6 linhas de diff, todas o cabeçalho), e o saldo foi de VERIFICAÇÃO — o cotejo B050 que o DOSSIE de 2025 pedira fechou o TALM em 7,7 bi a.p. (nota averbada na RC-091 sem encerrar a discrepância interna do B024, que o despacho quis manter evidente), certificou Olm como tensão própria do corpus (flag da RC-092 mantida) e devolveu biodemos e datas EC às suas fontes próprias. A caixa retorna ao regime de entrada bruta; `LISTA SIMPLES` permanece, não-apta. O alerta contra preenchimento de «nome ??» mantém-se vigente.
