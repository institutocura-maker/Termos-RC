# Auditoria da salvaguarda de checkout

**Data:** 23/10/2026
**Método:** somente leitura da `stash@{0}` criada antes da restauração do checkout; nenhum arquivo foi aplicado, removido ou incorporado ao branch.

## Origem e integridade

- Base da stash: `41cfedbcbd3ee632e7e582fffc28926a912d0fac`.
- HEAD publicado comparado: `5a9b68b7231086d0e8dfd797c16a6167ae02e3dc`.
- Inventário completo: [`INVENTARIO-SALVAGUARDA-CHECKOUT-2026-10-23.csv`](INVENTARIO-SALVAGUARDA-CHECKOUT-2026-10-23.csv) — 1179 entradas, SHA-256 `fe17424e1ed0439efdc0f56c56aafa02a4a487f4cc1ae9f493b9371eb282c577`.

## Resultado

| Medida | Quantidade |
|---|---:|
| Arquivos rastreados modificados na stash | 90 |
| Arquivos não rastreados preservados na stash | 1089 |
| Conteúdos já idênticos ao HEAD publicado | 1140 |
| Conteúdos divergentes do HEAD publicado | 39 |
| Caminhos ausentes no HEAD publicado | 0 |

A salvaguarda contém majoritariamente material que já está idêntico ao branch publicado. Ela **não deve ser descartada**, pois ainda retém 39 conteúdos divergentes: `termos/` (36), `ferramentas/` (2) e `.gitattributes` (1). Todos esses caminhos existem no HEAD; portanto uma aplicação cega da stash pode sobrescrever conteúdo publicado.

## Itens que exigem reconciliação explícita

- `.gitattributes`
- `termos/RC-254-dominacao-premissa-dos-tres-primeiros-logos.md`
- `termos/RC-306-apolo.md`
- `termos/RC-839-oxitocina-hormonio-do-bem-base-bioquimica-da-karuna.md`
- `ferramentas/dados_termos.py`
- `ferramentas/motor.py`
- `termos/RC-002-rebeliao-de-lucifer.md`
- `termos/RC-003-reintegracao-cosmica.md`
- `termos/RC-024-anunnaki.md`
- `termos/RC-034-big-bang.md`
- `termos/RC-036-biodemos.md`
- `termos/RC-037-brahma-brajna.md`
- `termos/RC-039-capela-sistema.md`
- `termos/RC-056-especiacao.md`
- `termos/RC-061-espiritualidade-laboratorial.md`
- `termos/RC-078-lucifer-yel-luzbel.md`
- `termos/RC-081-mohen-so-avatar-keshava-de-vishnu.md`
- `termos/RC-086-pandora.md`
- `termos/RC-094-revelacao-cosmica-conceito.md`
- `termos/RC-097-seres-extrafisicos.md`
- `termos/RC-102-shiva-savna.md`
- `termos/RC-104-trimurti.md`
- `termos/RC-106-universo-antimaterial-brahmaloka-universo-paralelo.md`
- `termos/RC-135-vishnu-mavatna.md`
- `termos/RC-162-eletrons.md`
- `termos/RC-166-mentalma.md`
- `termos/RC-301-prometeu-tita.md`
- `termos/RC-302-epimeteu-tita.md`
- `termos/RC-414-krishna-avatar-de-vishnu-shiva.md`
- `termos/RC-487-enlil-deus-sumerio-par-de-enki.md`
- `termos/RC-489-enoque-setimo-patriarca-levado-por-jave.md`
- `termos/RC-528-mergulho.md`
- `termos/RC-529-ressonancia-limbica-emocoes-como-tecnologia-cosmica.md`
- `termos/RC-553-eu-profundo-nivel-espiritual-do-eu.md`
- `termos/RC-585-vyasa.md`
- `termos/RC-593-mahabharata.md`
- `termos/RC-623-corpo-atmico.md`
- `termos/RC-624-corpo-budico.md`
- `termos/RC-841-cronos-tita.md`

## Decisão operacional

1. Manter `stash@{0}` intacta e fora do índice.
2. Não executar `git stash pop` nem `git stash drop`.
3. Os 1.140 itens idênticos são duplicatas recuperáveis; os 39 divergentes devem ser comparados por conteúdo e submetidos a uma onda própria, sem serem misturados à migração de fontes.
4. O patch da Fase 1C não inclui nenhum arquivo da stash.
