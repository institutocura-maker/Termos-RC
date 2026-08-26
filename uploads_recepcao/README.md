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
- Os arquivos removidos **permanecem recuperáveis no histórico Git** (nada se
  perde irreversivelmente).

## Estado atual

**PASTA LIMPA** — pronta para receber o material da nova fase (Palestras e
Apostilas). A primeira da fila: **P2023-11-19 — *A Máquina da Criação: O
Desmonte do Mundo*** (a ser subida pelo curador).
