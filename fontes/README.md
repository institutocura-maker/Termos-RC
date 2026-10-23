# Fontes — arquitetura de fontes

> Esta pasta organiza as fontes por proveniência. As coleções já migradas têm seus caminhos físicos autoritativos nesta árvore; as demais permanecem nos caminhos atuais até uma onda curatorial específica.

## Taxonomia planejada

```text
fontes/
├── recepcao/          # futuros brutos recebidos; hoje: uploads_recepcao/
├── livros/            # obras e amostras; rota atual
├── palestras/         # fontes classificadas como palestras
├── online/youtube/    # fontes identificadas pelo canal, quando aplicável
└── externas/          # materiais de terceiros; hoje: externas/
```

`palestras/` e `online/youtube/` representam eixos diferentes: palestra é tipo editorial; YouTube é canal de origem. Uma fonte pode precisar de ambos os metadados, sem cópia duplicada.

## Estado da migração

- **FON-EXTERNAS** foi migrada em 23/10/2026 para `externas/`, por `git mv`, com os 15 arquivos e a hash agregada conferidos contra o manifesto da Fase 0.
- **FON-LIVROS** foi migrada em 23/10/2026 para `livros/`, por `git mv`, com a coleção literal conferida contra a linha Fase 0 + Fase 1B antes da atualização documental limitada desta onda.
- As demais rotas desenhadas acima permanecem planejadas; não devem ser usadas como caminhos de runtime até despacho e portões próprios.

## O que não pertence aqui

- `apostilas/`, `ciclos/` e `consolidacoes/` preservam transformação, deliberação, âncoras e cópias de evidência; não são apenas repositórios de fonte.
- Cada cópia selada existente continua no seu local para preservar SHA-256, proveniência e referências históricas.

## Manifesto de pré-migração

[`manifestos/MANIFESTO-FONTES-FASE-0.json`](manifestos/MANIFESTO-FONTES-FASE-0.json) registra IDs estáveis, caminhos atuais, destinos propostos, hashes de cada arquivo e hash agregado das coleções. Gere-o com:

```bash
python3 ferramentas/gerar_manifestos_acervo.py
python3 ferramentas/gerar_manifestos_acervo.py --validar
```
