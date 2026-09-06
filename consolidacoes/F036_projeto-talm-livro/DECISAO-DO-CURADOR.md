# DECISÃO DO CURADOR — CICLO F036

**Data**: 05/09/2026 · **Documento-sujeito**: «Projeto TALM – O Livro» (SHA-256 `b9ad623e3b6fd27e9057c1cf04c63a4f085b9fb802b12fae1c4193eae8f7857e`) · **Ciclo**: F036 · **Fase**: APLICAÇÃO (concluída no mesmo ato)

## Despacho (verbatim dos pontos deliberativos)

> A análise cirúrgica deste ciclo revela o quão lapidada a sua esteira se tornou. Constatar que o documento F036 tem 100% das suas linhas longas e 100% de suas citações ancoradas verbatim no corpus (sendo o corpo byte a byte o `original.txt` de P2025-08-02) comprova a precisão do seu processo curatorial anterior. O documento não postula falsas identidades nem adiciona ruído, atuando como uma janela de verificação cristalina.
>
> O ganho real deste ciclo foi o cotejo cronológico contra o B050, que cravou o início do TALM em 7,7 bilhões a.p. e revalidou as âncoras para Nidana e Fenvans.
>
> Transite o ciclo F036 para a fase `APLICACAO` (`altera_base=true`). O documento é confirmado como FONTE do cluster P2025-08-02, com saldo doutrinário zero. Nenhum novo termo ou relação será criado. Execute os fechamentos no ledger e aplique a única modificação de ficha autorizada abaixo.
>
> **Q-F036-A (Homologação):** ✅ Aprovado. Homologo a sigla F036 como documento-FONTE (ciclo de VERIFICAÇÃO). A citabilidade do material segue a do ART-2025-08-02.
>
> **Q-F036-B (Averbação na Ficha RC-091):** ✅ Aprovado. Insira a nota na ficha RC-091 (sem blindagem), registrando o terceiro ponto cronológico encontrado no B050 (l. 82: «[ 7,700,000,000 a.p.] (trilha A, y=1724) "Início" do projeto Talm. (7,7 bilhões a.p.)»). **Mantenha o** `[REVISAR]` **aberto** para que a discrepância interna dos capítulos do B024 continue evidente para futuros pesquisadores.
>
> **Q-F036-C (RC-092 / Olm 6-7 bi):** Flag mantida. Como B050 é silente sobre Olm, a tensão temporal persiste no corpus. Não aplique nenhuma nota adicional na ficha; mantenha a flag `[REVISAR]` original da l. 51.
>
> **Q-F036-D (Encerramentos de Ledger):** Averbado. Declare como fechadas no ledger as pendências sobre os biodemos (~900 mi) e as datas da era comum (2012/2015-2018), pois estão ancoradas em fontes distintas do mapa das eras (P2022-03-26, B057, e material curado). Nenhuma ficha adicional será movida por estes itens.
>
> **Q-F036-E (Supressões Editoriais):** Averbado. Registre no ledger que a exclusão das 47 linhas "pedagógicas" do texto original pela curadoria foi uma decisão de formato, não uma censura doutrinária, para orientar futuras auditorias. A taxonomia (Nidana ≠ TALM) mantém-se rigorosamente como está.
>
> **Q-F036-F (Limpeza da Caixa):** Autorizado. Emita o Registro nº 19 declarando o F036 como o 9º apto da Família F. Realize a conferência tripla do SHA, assegurando-se de utilizar o travessão no nome («TALM – O Livro»), e execute o `git rm` do bruto nº 14 da caixa de recepção.
>
> O ciclo está liberado para `APLICACAO`. Com a conclusão desta verificação, encerramos mais um lote garantindo a pureza do `dados_termos.py`.

## Execução (agente: aplicação imediata do assinado — nada além)

| Item | O que entrou | Fonte gravada |
|---|---|---|
| Q-B | `RC-091`, nota ao fim da ficha: «Nota — terceiro ponto cronológico em B050: `[REVISAR]` da l. 65 MANTIDO — F036 aplicação (05/09/2026)», com a âncora de B050 l. 82 grafada byte a byte (assert programático de igualdade com o arquivo-fonte executado antes da gravação) e a declaração expressa de que o `[REVISAR]` da l. 65 permanece aberto por decisão do despacho | B050 original.txt l. 82 |
| Q-C | Nada. RC-092 intocada; flag da l. 51 permanece exatamente como estava | — |
| Q-D | Nada nas fichas; fechamentos de biodemos (~900 mi) e datas EC (2012/2015–2018/2017–2018) averbados no ledger F036 (V-4/V-5 atualizados pelo encerramento) | P2022-03-26 · P2020-04-25 · B057 p. 21 (RC-009/RC-442) · material ART |
| Q-E | Nada nas fichas; averbação de formato no ledger (as 47 linhas do andaime pedagógico = supressão editorial, não censura); taxonomia Nidana ≠ TALM intacta em RC-154/RC-091 | — |
| Q-F | `backups/REGISTRO-LIMPEZA-2026-09-05-19.json` (F036 = **9º apto da Família F**); conferência tripla do SHA (sha256sum do bruto · hashlib da cópia canônica · stream em blocos do bruto, 121.388 B — nome do bruto grafado com travessão «TALM – O Livro»); `git rm` do bruto nº 14; README: linha F036 na tabela + seção «Limpeza nº 19» | SHA `b9ad623e…` idêntico nas três vias |
| Saldo | **termos 933 (inalterado) · relações 1898 (inalterado) · fichas tocadas: 1 (RC-091, só a nota de averbação) — nenhuma definição, categoria ou status movido** · ledger F036 encerrado 0 abertas · validador OK · espelhos (indice-mestre · xlsx · docx) consolidados | — |

## Encerramento

F036 encerra como o ciclo-espelho de F035 com sinal invertido: lá, a fonte revelou uma pendência centenária do cluster (a data de Shiva, hoje encerrada em RC-102); aqui, a fonte **confirmou a sanidade do que fora lavrado** — 100% das linhas longas, 100% das citações, zero ruído — e a repassada de 2026 pôde transformar a lista de incertezas do DOSSIE de 2025 em três fechamentos (TALM via B050 l. 82; biodemos e datas EC via fontes próprias) e duas certidões de mantença (Olm/RC-092; «autor do Apocalipse»/F034-Q-C). A única mão na base foi a nota de RC-091, que documenta o terceiro ponto cronológico sem fechar a discrepância do B024 — porque a decisão assinada quis que a divergância continuasse visível aos pesquisadores. Caixa fechada no Registro nº 19; `dados_termos.py` puro, como pedido.
