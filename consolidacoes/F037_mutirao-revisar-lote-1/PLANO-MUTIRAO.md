# PLANO DO MUTIRÃO REVISAR — o novo core do motor

> Ordem: «liquidar o máximo das flags [REVISAR] vivas, usando fontes primárias (livros e originais) para fechar o que for resolvível e cravar a chancela de 'tensão insolúvel' no que as próprias fontes não resolvem» (DESPACHO DE PAUSA, 05/09/2026).

## Censo de partida (05/09/2026, ferramenta: varredura linha a linha de `termos/*.md`)

- **286 linhas-âncora com REVISAR** em **187 fichas** · 283 VIVAS (3 já são verbetes de adjudicação passada: RC-102 etc.).
- Distribuição por lote temático (classificação automática; reclassificação linha a linha é parte da execução de cada lote):

| Lote | Tema | Flags | Fontes primárias | Predição |
|---|---|---|---|---|
| **L1** (F037) | Cronologia — B050 e datas EC | 38 (35 reais; 2 meta-linhas do F036 excluídas, 1 protegida por despacho) | B050 completo no repo + livros B0xx | ~15–20 fecháveis · ~10 chanceláveis · ~10 reclassificáveis |
| L2 | Grafia & taxonomia (sânscrito/grego) | 21 | livros (B051/B064/B083…), dicionários internos do corpus | mix; grafia de palestra não se corrige — chancela de grafia variante |
| L3 | STT & áudio | 111 | só os originais.txt (que SÃO o STT) | maior bloco de chancela: «depende de áudio que a esteira não possui» — mas candidatas a fechar quando livro irmão crava a grafia/número |
| L4 | Tensão intra-corpus | 8 | duas fontes divergentes | chancela canônica do tipo «tensão insolúvel» |
| L5 | Outros/provisórios | 105 | variada | sub-categorizar na abertura do lote (inclui «provisoriamente», «nome ??», aguardos de B0xx) |

- Concentrações top: RC-009 (9) · RC-102 (7, pós-encerramento) · RC-104 (7) · RC-072 (6) · RC-091 (6) · RC-024/RC-414/RC-489/RC-777 (5).

## Máquina de estados da flag (por adjudicação, lavrada na ficha)

1. **ENCERRADO-F037-Ln** — âncora primária byte-a-byte disponível: nota ao fim da ficha no modelo RC-102 (cita a fonte verbatim) + inline «[REVISAR → ENCERRADO dd/mm/aaaa · F037-Ln: ver nota]».
2. **TENSÃO-INSOLÚVEL-F037-Ln** — fontes conferidas e divergentes/silentes: inline «[REVISAR → CHANCELA dd/mm/aaaa · F037-Ln: B050 silente; molduras registradas na nota]» + nota ao fim da ficha arrolando as molduras. A flag deixa de contar como aberta; fica visível como tese viva documentada.
3. **RECLASSIFICADO-Lm** — o censo automático errou o lote; a linha migra de roster sem tocar a ficha.
4. **PROTEGIDA** — flag mantida por despacho expresso anterior (ex.: RC-091 l. 65, F036-Q-B): o mutirão NÃO a encerra nem a chancela; apenas a exclui do roster.
5. (L3 específico) **AGUARDA-ÁUDIO** — chancela de impossibilidade estrutural, com a grafia variante registrada para o dia do áudio.

## Governança

Um lote = um ciclo: DEVOLUTIVA com adjudicação linha a linha (âncora verbatim ou veredito de chancela) → despacho único do curador (lista aprovada, com desvios marcados) → APLICAÇÃO em commit único → espelhos consolidados ao FIM do lote (não por ficha). Métrica de continuação: lote com <15% de fecháveis + chancelas úteis aciona reordenação. O mutirão encerra quando o censo chegar a zero VIVAS ou quando só restarem AGUARDA-ÁUDIO/PROTEGIDA — e aí sim a esteira poderá repousar de vez.

## Correção de alçada descoberta na abertura (integridade)

O cotejo F036/V-4 negara jurisdição do B050 sobre datas da era comum. O censo do mutirão provou o contrário: o mapa tem **Trilha D** — l. 203: «[14 a.p.] Fim do fechamento dos portais. (2012 d.C.)» e l. 204: «[11 a.p.] 2.000 A.P / 2.000 D.C. / Fim da Lila/Trimurti. (2015 d.C.)» — além de l. 87 («Surge Sophia, o primeiro biodemo», 5 bi a.p.) e ll. 46/64 (Era da Solidão = 13,8–13,3 bi ≡ os «500 milhões» do RC-808). Averbação lavrada no mapeamento do F037; as fichas afetadas serão adjudicadas pelo L1 com esses versos.
