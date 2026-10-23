# Plano — arquitetura Fontes e KB (Fase 0)

## Objetivo

Preparar uma futura organização física em `fontes/` e `kb/` sem mover, renomear, copiar ou reescrever qualquer fonte, ficha, cadastro ou evidência nesta fase.

## Diagnóstico de risco

O repositório atual separa, corretamente, mais de uma dimensão:

1. **origem/tipo:** livros, palestras, materiais externos e vídeos;
2. **ciclo de vida:** recepção bruta em `uploads_recepcao/`, processamento e evidência em `ciclos/`, `apostilas/` e `consolidacoes/`;
3. **conhecimento canônico:** `base/`, `termos/`, `rag/` e o registro executável em `ferramentas/dados_termos.py`.

Não é seguro colapsar essas dimensões em uma simples árvore de diretórios. Em especial, YouTube é canal de origem, não sinônimo de palestra; e cópias em ciclos/apostilas são prova de proveniência, não duplicação a eliminar.

## Entregas da Fase 0

- `ferramentas/caminhos_acervo.py`: mapa único de caminhos atuais e destinos planejados;
- `ferramentas/gerar_manifestos_acervo.py`: geração e validação determinística dos manifestos;
- `fontes/manifestos/MANIFESTO-FONTES-FASE-0.json`: inventário SHA-256 das fontes e evidências relacionadas;
- `kb/manifestos/MANIFESTO-KB-FASE-0.json`: inventário SHA-256 da camada canônica e RAG;
- `fontes/README.md` e `kb/README.md`: contratos que deixam explícito que não houve migração física.

## Portões para qualquer migração posterior

1. Validar os manifestos antes do movimento.
2. Declarar uma única coleção-piloto e o conjunto completo de consumidores a atualizar.
3. Substituir caminhos de runtime ativos pela camada `caminhos_acervo.py` antes de alterar o local físico.
4. Executar verificador de referências Markdown/JSON/TOML/Python relativo a essa coleção.
5. Garantir igualdade de hashes por arquivo e por coleção após o movimento.
6. Rodar os builders, `ferramentas/test_suite.py`, `ferramentas/motor.py selftest` e testes específicos do piloto.
7. Não modificar diretórios consolidados sem despacho explícito; referências neles são bloqueios, não convites a reescrita.
8. Só então apresentar relatório/tree para validação curatorial e, após aceite, commitar.

## Ordem recomendada de ondas futuras

1. **Piloto de taxonomia/metadata, sem dados:** concluído nesta Fase 0.
2. **Piloto físico eventual:** avaliar `materiais_externos/`, após mapear inclusive referências em acervo consolidado; não há consumidores Python diretos conhecidos.
3. **Fontes primárias:** `livros/`, somente após adaptação e testes dos consumidores ativos.
4. **Recepção e palestras:** `uploads_recepcao/` e seu contrato de SHA-256, sem mover apostilas/ciclos junto.
5. **KB:** `base/`, `termos/` e `rag/` em onda exclusiva; nunca junto da migração de fontes.

## Fora de escopo

Esta Fase 0 não muda caminhos de runtime, não abre ciclos, não altera Base, não reorganiza apostilas/ciclos/consolidações e não classifica retroativamente cada vídeo do YouTube como palestra.
