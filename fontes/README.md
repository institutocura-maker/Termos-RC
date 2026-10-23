# Fontes — arquitetura em Fase 0

> Esta pasta inicia a organização lógica das fontes. **Nenhum bruto foi movido para cá nesta fase**: os caminhos físicos atuais permanecem autoritativos até uma onda curatorial específica de migração.

## Taxonomia planejada

```text
fontes/
├── recepcao/          # futuros brutos recebidos; hoje: uploads_recepcao/
├── livros/            # obras e amostras; hoje: livros/
├── palestras/         # fontes classificadas como palestras
├── online/youtube/    # fontes identificadas pelo canal, quando aplicável
└── externas/          # materiais de terceiros; hoje: externas/
```

`palestras/` e `online/youtube/` representam eixos diferentes: palestra é tipo editorial; YouTube é canal de origem. Uma fonte pode precisar de ambos os metadados, sem cópia duplicada.

## Estado da migração

- **FON-EXTERNAS** foi migrada em 23/10/2026 para `externas/`, por `git mv`, com os 15 arquivos e a hash agregada conferidos contra o manifesto da Fase 0.
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
