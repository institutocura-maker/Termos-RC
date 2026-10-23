# Relatório — Fase 1B · preparação de FON-LIVROS

**Data:** 23/10/2026
**Estado:** preparação concluída; sem migração física, renomeação ou alteração em `livros/`.
**Decisão:** relatório validado pelo Curador para consolidação e publicação.

## Escopo executado

A Fase 1B prepara a futura rota `livros/ → fontes/livros/`, sem a acionar:

1. auditoria das referências ao caminho de livros;
2. parametrização dos quatro consumidores Python ativos pelo mapa central `fonte.livros`;
3. generalização do verificador por ID estável de coleção;
4. registro verificável do único delta documental ocorrido após o manifesto imutável da Fase 0;
5. validações de integridade, builders, suíte e Motor.

Não foram movidos, editados ou regenerados arquivos sob `livros/`. Base, Termos, RAG, apostilas, ciclos, consolidações e recepção permanecem fora do patch.

## Linha de base e averbação

O manifesto imutável `fontes/manifestos/MANIFESTO-FONTES-FASE-0.json` declara para **FON-LIVROS**:

| Campo | Valor |
|---|---|
| Rota atual | `livros/` |
| Destino apenas planejado | `fontes/livros/` |
| Arquivos | 577 |
| Bytes | 100.540.340 |
| SHA-256 agregado da Fase 0 | `64d8aed02b3d46f02ad17b80710a5b831289e8e7c5a20d48987d0dd2d6a8d88c` |

A verificação estrita da Fase 0 localiza exatamente um delta posterior: `livros/README.md`. Os demais **576 arquivos** coincidem literalmente com o manifesto, por caminho relativo, bytes e SHA-256.

O README foi alterado no commit publicado `0e56c1b`, unicamente para atualizar a documentação de materiais de terceiros para `../fontes/externas/` no piloto FON-EXTERNAS. Mantém 16.950 bytes, mas seu SHA-256 mudou; não foi tocado nesta fase.

Para não regenerar o manifesto imutável, o delta foi averbado em:

```text
fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1B.json
```

A averbação exige o hash da Fase 0 e fixa o hash atual desse README. A linha pré-migração resultante é:

```text
06098a1590654708a6e0145502cf0147066e2048b16ed8b8a0dcd15d612c66d5
```

Ela é prova de proveniência; não autoriza movimento físico e não altera o manifesto-base.

## Auditoria de referências

A varredura inicial de `livros/` identificou **380 ocorrências em 238 arquivos**:

| Classe | Ocorrências | Arquivos | Tratamento |
|---|---:|---:|---|
| Fonte interna de `livros/` | 159 | 147 | Selada; preservar literalmente. |
| Apostilas concluídas | 33 | 19 | Evidência consolidada; não alterar sem autorização contextual. |
| Consolidações | 16 | 16 | Deliberação/registro; não alterar sem autorização contextual. |
| Ficha canônica em `termos/` | 1 | 1 | Fora de escopo. |
| Documentação/operação fora das classes acima | 158 | 51 | Classificar por contexto em proposta física futura. |
| Consumidores Python ativos | 13 | 4 | Desacoplados da literal de rota nesta fase. |

Os 158 usos documentais/operacionais incluem `admin/` (83), `pedagogico/` (36), `diagnostico/` (16), `prompts/` (8), `.arena/` (6), raiz (2), `notas/` (2), `fontes/` (2), `uploads_recepcao/` (2) e `docs/` (1). Eles não foram tratados como caminhos de runtime por simples busca textual.

Portanto, os quatro consumidores ativos já não dependem de `livros/`, mas uma futura proposta de `git mv livros/ fontes/livros/` ainda deverá classificar os registros documentais e solicitar autorização individual para qualquer averbamento de apostila, consolidação ou ficha canônica.

## Preparação técnica

`ferramentas/caminhos_acervo.py` continua autoritativo nesta fase:

```text
fonte.livros = livros/
destino planejado = fontes/livros/
```

Os consumidores abaixo passaram a consultar `caminho_atual("fonte.livros")`:

- `ferramentas/censo_gap_v2.py`;
- `ferramentas/materializar_lote.py`;
- `ferramentas/test_suite.py`;
- `ferramentas/u41_materializar_r1.py`.

O censo carregou 174 obras pela rota mapeada; B003 no materializador e os oito localizadores de livro da U41 também foram conferidos.

`ferramentas/verificar_migracao_fontes.py` agora aceita `--colecao FON-LIVROS` e preserva o atalho publicado `--piloto externas`. A comparação crua diagnostica somente `README.md`; a verificação da linha pré-migração averbada é explícita:

```bash
python3 ferramentas/verificar_migracao_fontes.py \
  --colecao FON-LIVROS \
  --averbacao fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1B.json
```

## Portões executados

| Verificação | Resultado |
|---|---|
| `py_compile` dos seis módulos envolvidos | OK |
| FON-LIVROS contra Fase 0 estrita | Divergência esperada: somente `README.md` |
| FON-LIVROS com averbação | OK — 577 arquivos, 100.540.340 bytes, hash `06098a…c66d5` |
| FON-EXTERNAS pós-piloto | OK — 15 arquivos, 146.373 bytes, hash `144847…f6488` |
| Integração dos consumidores mapeados | OK — censo com 174 obras e localizadores conferidos |
| `ferramentas/test_suite.py` | OK — 21 testes |
| `ferramentas/motor.py selftest` | OK — 10/10 |
| `ferramentas/build_readme.py` | OK — `946/820/1887/104` |
| `ferramentas/build_indice.py` | OK — 946 linhas |
| `git diff --check` | OK |

A suíte emitiu somente `ResourceWarning` herdados por leituras sem fechamento explícito e encerrou com `OK`.

## Árvore consolidada

Não há árvore movida nesta fase. O patch contém somente:

```text
admin/logs/RELATORIO-FASE-1B-FON-LIVROS-2026-10-23.md
ferramentas/censo_gap_v2.py
ferramentas/materializar_lote.py
ferramentas/test_suite.py
ferramentas/u41_materializar_r1.py
ferramentas/verificar_migracao_fontes.py
fontes/manifestos/averbacoes/AVERBACAO-FON-LIVROS-FASE-1B.json
```

## Próxima decisão arquitetural

A preparação torna possível abrir uma proposta separada de migração física FON-LIVROS, sem a executar automaticamente. Até novo despacho, `livros/` continua a única rota física autorizada para o runtime.
