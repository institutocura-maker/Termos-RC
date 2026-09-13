# Política de Citações-chave — Onda 2.3 (12/09/2026)

Decisão-mãe (censo A3, adotada como plano): **`## Citações-chave` é índice curado (opção b) só para 🟢**; para as demais status a seção some do modelo (opção a) — o arquivo das citações é o bloco-fonte; transcrição literal sempre (G2.4: nada de paráfrase).

## Censo re-rodado hoje (regra dupla: blocos `> ` ≥180c ∪ citações `«…»` 150–1500c)
- 🟢 sem `## Citações-chave`: **163** (reconcilia com A5 de 11/09 — número que não reconcilia não publica: publicou).
- **81 fichas ganham índice mecânico** (U14): até 3 itens, seleção determinística pela citação mais longa **dentro de seções de conteúdo** (`Ampliação`/`Contexto / Origem`/`Etimologia`) — meta-citações (citações da própria ficha vivas em `Nota`/`Atualização`/`Observações`/`Definição`/`Fontes`) ficam de fora; cada item = trecho literal de abertura (≤300c, prefixo verbatim) + âncora `U####`/`p.` quando existente no entorno + ponteiro para a seção-fonte (`ver em ## …`). A seção nova é **aditiva**: removida byte a byte, a carta volta ao original — gate do script.
- **82 ficam na fila A5** (58 sem nenhuma das duas sintaxes + 24 onde as únicas citações localizadas eram meta-citações) — complementação é curadoria humana, item a item, sem perder o selo (não-retroatividade). Lista:
  RC-014, RC-015, RC-016, RC-024, RC-033, RC-038, RC-063, RC-075, RC-098, RC-099, RC-118, RC-153, RC-163, RC-164, RC-175, RC-176, RC-196, RC-239, RC-253, RC-266, RC-267, RC-268, RC-287, RC-302, RC-376, RC-385, RC-410, RC-425, RC-426, RC-432, RC-436, RC-449, RC-460, RC-461, RC-470, RC-477, RC-483, RC-487, RC-490, RC-506, RC-526, RC-530, RC-541, RC-545, RC-556, RC-563, RC-565, RC-705, RC-721, RC-723, RC-724, RC-726, RC-728, RC-729, RC-731, RC-732, RC-733, RC-735, RC-738, RC-739, RC-743, RC-746, RC-747, RC-751, RC-752, RC-754, RC-756, RC-758, RC-759, RC-760, RC-761, RC-762, RC-763, RC-764, RC-766, RC-767, RC-843, RC-845, RC-849, RC-852, RC-856, RC-872.
- Observação honesta: a regra-antiga (só `> `) deixava **as 4 gigantes na fila**; com a regra dupla **todas as 4 entraram no quadro** (citações em «» de 120–855c). Duas revisões determinísticas ocorreram no dry-run: (1) união das sintaxes `> ` ∪ `«…»` (163→105 com lastro); (2) exclusão de meta-citações por seção-âncora (105→81). A fila cresceu de 58→82 e é, agora, a lista honesta do que carece de curadoria humana.

## Modelo
`01-ficha-modelo.md` §7 atualizado (política declarada no próprio modelo; seção "some do modelo" das não-🟢 = não criar, não apagar o que existe — apagar é perda).

## Portões da unidade
Aditivo puro (gate de restauração byte a byte por remoção da seção); trecho-cita é substring da carta (anti-paráfrase); frontmatter TOML intocado nos pilotos; suíte + verificador + builds verdes antes do commit.
