# T2 — Relatório de Consolidação (De-Para Fase 2)

| Campo | Valor |
|---|---|
| Data | 2026-10-25 |
| Status | **APROVADO em 2026-10-25 — matriz 100% concluída** |
| Matriz | `admin/logs/T2-MAPEAMENTO-RELACOES.csv` |
| Log de exceções | `admin/logs/T2-EXCECOES-RELACOES.md` (Anexo A) |
| Escopo | 919 linhas `PROPOSTO` (567 rótulos-base) consolidadas; 31 `APROVADO` e 48 `REVISAR` intactas |
| Salvaguarda | **Nenhuma ficha Markdown foi alterada.** |

## 1. Síntese

| Métrica | Valor |
|---|---|
| Rótulos-base (entrada) | 567 |
| Relações controladas (saída) | **23** — 10 já aprovadas + 13 novas |
| Volume consolidado | 1.735 ocorrências |
| Volume nas 10 relações aprovadas (2ª rodada) | 953 / 1.735 (54.9%) |
| Volume nas 10 relações aprovadas (base inteira) | **6.928 / 7.761 (89.3%)** |
| Linhas com direção invertida (formas passivas) | 126 |
| Linhas forçadas a `<->` (raiz `associado`, decisão 3) | 70 |
| Linhas `REVISAR` mantidas intocadas | 48 (51 ocorrências) |

A consolidação reduz 567 clusters a 23 relações controladas. Onde não havia ganho semântico comprovado, o rótulo-base foi enviado para `relaciona-se-a` (aprovada); o rótulo original foi preservado em `notas_de_normalizacao` em todas as linhas alteradas.

## 2. Núcleo controlado proposto (23 relações)

| Relação | Origem | Definição operacional | Direção padrão | Bases | Ocorrências |
|---|---|---|---|---|---|
| `origina` | Nova | Criação, geração, procedência, genealogia, filiação ou encarnação. | `->` | 60 | 212 |
| `contexto` | Aprovada | Contexto, tema, domínio, ambiente, localização ou ocorrência. | `->` | 45 | 197 |
| `associado` | Aprovada | Vínculo genérico e simétrico; sem lado preferencial. | `<->` | 34 | 140 |
| `relaciona-se-a` | Aprovada | Vínculo genérico direcional; fallback quando nenhum outro rótulo traz ganho semântico. | `->` | 65 | 123 |
| `usa` | Aprovada | Instrumento, método, meio, operação ou execução. | `->` | 34 | 107 |
| `causa` | Nova | Causalidade, consequência, efeito, influência ou modificação. | `->` | 30 | 96 |
| `variação` | Aprovada | Sinonímia, variante, paralelo, analogia, correspondência ou equivalência. | `->` | 34 | 90 |
| `opõe-se-a` | Aprovada | Oposição, contraste, distinção, resistência ou crítica. | `->` | 16 | 85 |
| `inclui` | Aprovada | Meronomia do todo para a parte; composição, organização, estrutura. | `->` | 14 | 72 |
| `controla` | Nova | Controle, comando, liderança, gestão, regência ou tutoria. | `->` | 25 | 57 |
| `transfere` | Nova | Transferência, transporte, envio, destinação ou recebimento. | `->` | 17 | 54 |
| `envolve` | Aprovada | Participação, agência, escopo ou protagonismo. | `->` | 20 | 51 |
| `é-um` | Aprovada | Classificação, identidade, espécie, instância ou estado. | `->` | 23 | 51 |
| `representa` | Nova | Representação, expressão, manifestação ou personificação. | `->` | 18 | 49 |
| `sucede` | Nova | Posterioridade temporal, continuação, desdobramento ou encerramento. | `->` | 13 | 48 |
| `danifica` | Nova | Dano, destruição, ruptura, ataque, corrupção ou ameaça. | `->` | 28 | 47 |
| `protege` | Nova | Proteção, sustentação, apoio, nutrição, benefício ou libertação. | `->` | 19 | 45 |
| `precede` | Nova | Anterioridade temporal, início de sequência ou hierarquia superior. | `->` | 12 | 39 |
| `parte-de` | Aprovada | Meronomia inversa: a parte para o todo. | `->` | 8 | 37 |
| `explica` | Nova | Explicação, interpretação, definição, revelação ou qualificação. | `->` | 11 | 36 |
| `comunica` | Nova | Comunicação, mensagem, resposta, anúncio ou registro escrito. | `->` | 16 | 35 |
| `requer` | Nova | Dependência, necessidade, condição, premissa ou base. | `->` | 10 | 35 |
| `observa` | Nova | Observação, reconhecimento, medição, mapeamento, avaliação ou registro. | `->` | 15 | 29 |

`Direção padrão` é o valor aplicado quando o tipo bruto não traz `←`. Linhas com `← ` recebem `<-`; formas passivas/inversas têm a direção invertida; a raiz `associado` é sempre `<->`.

## 3. De-Para completo — 567 rótulos-base por relação controlada

Cada linha abaixo é um cluster da 1ª rodada. `Inv.` marca as bases cujas linhas tiveram a direção invertida para preservar a leitura da forma passiva (ex.: `criado-por` → `origina` com `<-`).

| Relação controlada | Rótulo-base (cluster) | Ocorrências | Inv. |
|---|---|---|---|
| `origina` | `gera` | 19 | — |
| `origina` | `criado-por` | 17 | sim |
| `origina` | `origem-em` | 16 | — |
| `origina` | `produz` | 16 | — |
| `origina` | `cria` | 11 | — |
| `origina` | `origem` | 11 | — |
| `origina` | `gera-linhagem-de` | 10 | — |
| `origina` | `origina-em` | 10 | — |
| `origina` | `encarnação-de` | 8 | — |
| `origina` | `encarnação-posterior-de` | 8 | — |
| `origina` | `origina` | 5 | — |
| `origina` | `deriva-de` | 4 | sim |
| `origina` | `descende-de` | 4 | sim |
| `origina` | `origina-se-em` | 4 | — |
| `origina` | `pai-de` | 4 | — |
| `origina` | `originou` | 3 | — |
| `origina` | `avatar-de` | 2 | — |
| `origina` | `descende-de-membro-de` | 2 | — |
| `origina` | `fonte` | 2 | — |
| `origina` | `fonte-em` | 2 | — |
| `origina` | `fundado-por` | 2 | sim |
| `origina` | `gerada-por` | 2 | sim |
| `origina` | `gere` | 2 | — |
| `origina` | `herdado-de` | 2 | sim |
| `origina` | `iniciador` | 2 | — |
| `origina` | `origina-de` | 2 | sim |
| `origina` | `originada-em` | 2 | sim |
| `origina` | `produzido-por` | 2 | sim |
| `origina` | `produziu-pacote-genético` | 2 | — |
| `origina` | `é-avatar-de` | 2 | — |
| `origina` | `é-clone-para-inseminação-de` | 2 | — |
| `origina` | `é-criador-de` | 2 | — |
| `origina` | `é-inseminada-por` | 2 | sim |
| `origina` | `é-obra-de` | 2 | sim |
| `origina` | `criada-por` | 1 | sim |
| `origina` | `criador` | 1 | — |
| `origina` | `criou` | 1 | — |
| `origina` | `descendente-de` | 1 | — |
| `origina` | `edificada-por` | 1 | sim |
| `origina` | `filha-de` | 1 | — |
| `origina` | `fundada-por` | 1 | sim |
| `origina` | `gatilho-de` | 1 | — |
| `origina` | `gera-com-epimeteu` | 1 | — |
| `origina` | `gerou` | 1 | — |
| `origina` | `herança` | 1 | — |
| `origina` | `originado-por` | 1 | sim |
| `origina` | `plantou-semente-em` | 1 | — |
| `origina` | `provém-de` | 1 | sim |
| `origina` | `é-descendente-de` | 1 | — |
| `origina` | `é-encarnação-posterior-de` | 1 | — |
| `origina` | `é-fonte-de` | 1 | — |
| `origina` | `é-início-de` | 1 | — |
| `origina` | `é-mãe` | 1 | — |
| `origina` | `é-mãe-de` | 1 | — |
| `origina` | `é-mãe-de-origem` | 1 | — |
| `origina` | `é-origem` | 1 | — |
| `origina` | `é-origem-de` | 1 | — |
| `origina` | `é-pai` | 1 | — |
| `origina` | `é-produto-de` | 1 | sim |
| `origina` | `é-progênie` | 1 | — |
| `contexto` | `ocorre-em` | 40 | — |
| `contexto` | `atua-em` | 13 | — |
| `contexto` | `contextualiza` | 12 | — |
| `contexto` | `é-contexto-de` | 12 | — |
| `contexto` | `ancora` | 10 | — |
| `contexto` | `tema-de` | 10 | — |
| `contexto` | `abriga` | 8 | — |
| `contexto` | `armazenado-em` | 6 | — |
| `contexto` | `atravessa` | 6 | — |
| `contexto` | `contextualizado-por` | 6 | sim |
| `contexto` | `erro-stt-de` | 4 | — |
| `contexto` | `hospeda` | 4 | — |
| `contexto` | `mergulha-em` | 4 | — |
| `contexto` | `tema` | 4 | — |
| `contexto` | `atua-sobre` | 3 | — |
| `contexto` | `habita` | 3 | — |
| `contexto` | `habitado-por` | 3 | sim |
| `contexto` | `local` | 3 | — |
| `contexto` | `surge-em` | 3 | — |
| `contexto` | `ambiente` | 2 | — |
| `contexto` | `atravessada-por` | 2 | sim |
| `contexto` | `atua-por` | 2 | — |
| `contexto` | `contexto` | 2 | — |
| `contexto` | `morada-de` | 2 | — |
| `contexto` | `ocorre-no-eixo-de` | 2 | — |
| `contexto` | `ocorreu-em` | 2 | — |
| `contexto` | `opera-em` | 2 | — |
| `contexto` | `operam-em` | 2 | — |
| `contexto` | `persiste-em` | 2 | — |
| `contexto` | `profecias-em` | 2 | — |
| `contexto` | `registradas-em` | 2 | — |
| `contexto` | `registrado-em` | 2 | — |
| `contexto` | `retratado-em` | 2 | — |
| `contexto` | `surgiu-em` | 2 | — |
| `contexto` | `trabalha-em` | 2 | — |
| `contexto` | `é-morada-de` | 2 | — |
| `contexto` | `contexto-de` | 1 | — |
| `contexto` | `desenvolvida-em` | 1 | — |
| `contexto` | `está-em` | 1 | — |
| `contexto` | `localiza-se-em` | 1 | — |
| `contexto` | `mergulhou-em` | 1 | — |
| `contexto` | `plano-original-de` | 1 | — |
| `contexto` | `refúgio` | 1 | — |
| `contexto` | `sediou` | 1 | — |
| `contexto` | `é-tema-de` | 1 | — |
| `associado` | `associado` | 27 | — |
| `associado` | `paralelo-com` | 18 | — |
| `associado` | `é-paralelo-com` | 18 | — |
| `associado` | `vinculado-ao-espírito` | 12 | — |
| `associado` | `vincula` | 6 | — |
| `associado` | `acompanha` | 5 | — |
| `associado` | `irmão-de` | 5 | — |
| `associado` | `conecta-se-por` | 4 | — |
| `associado` | `desenvolve` | 4 | — |
| `associado` | `nave-irmã` | 4 | — |
| `associado` | `contraponto` | 3 | — |
| `associado` | `interagiu` | 3 | — |
| `associado` | `pactuou-com` | 3 | — |
| `associado` | `conecta` | 2 | — |
| `associado` | `divide-com` | 2 | — |
| `associado` | `parceria-de` | 2 | — |
| `associado` | `tem-filhas-unidas-a` | 2 | — |
| `associado` | `une-se-às-filhas-de` | 2 | — |
| `associado` | `é-companheiro-de` | 2 | — |
| `associado` | `é-complemento` | 2 | — |
| `associado` | `acopla` | 1 | — |
| `associado` | `associa-se-a` | 1 | — |
| `associado` | `co-clona-com` | 1 | — |
| `associado` | `contato` | 1 | — |
| `associado` | `correlato` | 1 | — |
| `associado` | `irmã-de` | 1 | — |
| `associado` | `irmãos` | 1 | — |
| `associado` | `não-conectada-por` | 1 | — |
| `associado` | `parceiro-de-ideal` | 1 | — |
| `associado` | `vínculo-de-identidade` | 1 | — |
| `associado` | `é-complemento-a` | 1 | — |
| `associado` | `é-paralelo-a` | 1 | — |
| `associado` | `é-paralelo-formal-com` | 1 | — |
| `associado` | `é-paralelo-nórdico-com` | 1 | — |
| `relaciona-se-a` | `relaciona-se-a` | 36 | — |
| `relaciona-se-a` | `relacionado-a` | 3 | — |
| `relaciona-se-a` | `abre` | 2 | — |
| `relaciona-se-a` | `acionado-por` | 2 | — |
| `relaciona-se-a` | `bate-duro-por` | 2 | — |
| `relaciona-se-a` | `busca` | 2 | — |
| `relaciona-se-a` | `caminho-para-reacender` | 2 | — |
| `relaciona-se-a` | `cobra` | 2 | — |
| `relaciona-se-a` | `condição` | 2 | — |
| `relaciona-se-a` | `confirmada-por` | 2 | sim |
| `relaciona-se-a` | `disputada-por` | 2 | sim |
| `relaciona-se-a` | `enfrentada-por` | 2 | sim |
| `relaciona-se-a` | `evento` | 2 | — |
| `relaciona-se-a` | `fator` | 2 | — |
| `relaciona-se-a` | `humaniza-se-por` | 2 | — |
| `relaciona-se-a` | `inserido-em` | 2 | — |
| `relaciona-se-a` | `lamuriou-se` | 2 | — |
| `relaciona-se-a` | `operou-segundo` | 2 | — |
| `relaciona-se-a` | `planejada-por` | 2 | — |
| `relaciona-se-a` | `proposto-por` | 2 | sim |
| `relaciona-se-a` | `reconstrói` | 2 | — |
| `relaciona-se-a` | `sujeito` | 2 | — |
| `relaciona-se-a` | `tema-relacionado` | 2 | — |
| `relaciona-se-a` | `alvo` | 1 | — |
| `relaciona-se-a` | `alvo-do-plano` | 1 | — |
| `relaciona-se-a` | `animalizou-via` | 1 | — |
| `relaciona-se-a` | `apaixona-se-por` | 1 | — |
| `relaciona-se-a` | `ativou` | 1 | — |
| `relaciona-se-a` | `contemporâneo` | 1 | — |
| `relaciona-se-a` | `desfaz-arcanos-de` | 1 | — |
| `relaciona-se-a` | `desmaiou-aos-pés-da-cruz-de` | 1 | — |
| `relaciona-se-a` | `escapa-de` | 1 | — |
| `relaciona-se-a` | `escolhe` | 1 | — |
| `relaciona-se-a` | `estratégia` | 1 | — |
| `relaciona-se-a` | `etimologia` | 1 | — |
| `relaciona-se-a` | `finalidade` | 1 | — |
| `relaciona-se-a` | `frota-de` | 1 | — |
| `relaciona-se-a` | `hábito-de` | 1 | — |
| `relaciona-se-a` | `identidade` | 1 | — |
| `relaciona-se-a` | `institui` | 1 | — |
| `relaciona-se-a` | `jogadores` | 1 | — |
| `relaciona-se-a` | `manipula` | 1 | — |
| `relaciona-se-a` | `motivo-da-vingança` | 1 | — |
| `relaciona-se-a` | `objeto` | 1 | — |
| `relaciona-se-a` | `ouviu-em` | 1 | — |
| `relaciona-se-a` | `premissa` | 1 | — |
| `relaciona-se-a` | `premissa-de` | 1 | — |
| `relaciona-se-a` | `produtos` | 1 | — |
| `relaciona-se-a` | `promovido-por` | 1 | sim |
| `relaciona-se-a` | `racionalidade-instantânea` | 1 | — |
| `relaciona-se-a` | `racionalidade-reflexiva` | 1 | — |
| `relaciona-se-a` | `rebelou-se-contra` | 1 | — |
| `relaciona-se-a` | `recorre-a` | 1 | — |
| `relaciona-se-a` | `repertório` | 1 | — |
| `relaciona-se-a` | `resolve` | 1 | — |
| `relaciona-se-a` | `retira-sequências-de` | 1 | — |
| `relaciona-se-a` | `sacanela` | 1 | — |
| `relaciona-se-a` | `substitui` | 1 | — |
| `relaciona-se-a` | `tabuleiro` | 1 | — |
| `relaciona-se-a` | `tem-memória` | 1 | — |
| `relaciona-se-a` | `tem-pulsação` | 1 | — |
| `relaciona-se-a` | `tem-pulsação-de` | 1 | — |
| `relaciona-se-a` | `tentou-3-vezes` | 1 | — |
| `relaciona-se-a` | `unificado-ao` | 1 | — |
| `relaciona-se-a` | `é-de` | 1 | — |
| `usa` | `aplica-se-a` | 33 | — |
| `usa` | `realiza` | 12 | — |
| `usa` | `é-mecanismo-de` | 8 | — |
| `usa` | `realizada-por` | 6 | sim |
| `usa` | `cumpre` | 4 | — |
| `usa` | `instrumento` | 4 | — |
| `usa` | `processa` | 4 | — |
| `usa` | `canaliza` | 2 | — |
| `usa` | `codificado-em` | 2 | — |
| `usa` | `cumpre-se-em` | 2 | — |
| `usa` | `implementa` | 2 | — |
| `usa` | `instrumento-de` | 2 | — |
| `usa` | `processado-por` | 2 | sim |
| `usa` | `usada-em` | 2 | — |
| `usa` | `usado-por` | 2 | sim |
| `usa` | `é-cumprido-via` | 2 | sim |
| `usa` | `codifica-transmite` | 1 | — |
| `usa` | `executa` | 1 | — |
| `usa` | `executado-por` | 1 | sim |
| `usa` | `instrumentaliza` | 1 | — |
| `usa` | `instrumentalizado-por` | 1 | sim |
| `usa` | `instrumentalizado-via` | 1 | — |
| `usa` | `opera-por` | 1 | — |
| `usa` | `operacionaliza` | 1 | — |
| `usa` | `operadores` | 1 | — |
| `usa` | `pratica` | 1 | — |
| `usa` | `reativa-via` | 1 | — |
| `usa` | `recusa-usar-poderes-de` | 1 | — |
| `usa` | `usa-via` | 1 | — |
| `usa` | `é-instrumento-de` | 1 | — |
| `usa` | `é-método-de` | 1 | — |
| `usa` | `é-programação-de` | 1 | — |
| `usa` | `é-vetor-de` | 1 | — |
| `usa` | `é-veículo-de` | 1 | — |
| `causa` | `atualiza` | 14 | — |
| `causa` | `resulta-em` | 13 | — |
| `causa` | `afeta` | 11 | — |
| `causa` | `é-consequência-de` | 5 | sim |
| `causa` | `é-resultado-de` | 5 | sim |
| `causa` | `reforça` | 4 | — |
| `causa` | `resulta-de` | 4 | sim |
| `causa` | `beneficia` | 3 | — |
| `causa` | `impulsiona` | 3 | — |
| `causa` | `repercute-em` | 3 | — |
| `causa` | `ameaça` | 2 | — |
| `causa` | `favorece` | 2 | — |
| `causa` | `impulsionado-por` | 2 | sim |
| `causa` | `influencia` | 2 | — |
| `causa` | `modifica` | 2 | — |
| `causa` | `motiva` | 2 | — |
| `causa` | `motiva-recurso-a` | 2 | — |
| `causa` | `risco-de` | 2 | — |
| `causa` | `transforma` | 2 | — |
| `causa` | `viabiliza` | 2 | — |
| `causa` | `é-falência-de` | 2 | — |
| `causa` | `capacita` | 1 | — |
| `causa` | `consequência` | 1 | — |
| `causa` | `contribuiu-para` | 1 | — |
| `causa` | `efeito` | 1 | — |
| `causa` | `possibilita` | 1 | — |
| `causa` | `é-efeito-colateral-de` | 1 | sim |
| `causa` | `é-produzida-via` | 1 | sim |
| `causa` | `é-quebrada-por` | 1 | sim |
| `causa` | `é-sufocada-por` | 1 | sim |
| `variação` | `sinônimo` | 24 | — |
| `variação` | `correspondência-em-teologia-comparada-de` | 10 | — |
| `variação` | `corresponde-a` | 5 | — |
| `variação` | `serve-de-modelo-para` | 4 | — |
| `variação` | `variação` | 4 | — |
| `variação` | `atribuída-em-teologia-comparada-a` | 2 | sim |
| `variação` | `atribuído-a` | 2 | sim |
| `variação` | `atribuído-em-teologia-comparada-a` | 2 | — |
| `variação` | `compara-se-a` | 2 | — |
| `variação` | `comparado-a` | 2 | — |
| `variação` | `converte-se-em` | 2 | — |
| `variação` | `convertida-em` | 2 | — |
| `variação` | `metaforiza` | 2 | — |
| `variação` | `paralela-a` | 2 | — |
| `variação` | `paralelo` | 2 | — |
| `variação` | `sinônimo-parcial` | 2 | — |
| `variação` | `tem-como-modelo` | 2 | — |
| `variação` | `variação-posterior-de` | 2 | — |
| `variação` | `é-comparada-à-emergência-de` | 2 | — |
| `variação` | `alternativa-a` | 1 | — |
| `variação` | `analogia-de` | 1 | — |
| `variação` | `análogo` | 1 | — |
| `variação` | `equivale-em-função` | 1 | — |
| `variação` | `variante-de` | 1 | — |
| `variação` | `versão-oficial-de` | 1 | — |
| `variação` | `é-alternativa-a` | 1 | — |
| `variação` | `é-análoga-a` | 1 | — |
| `variação` | `é-análoga-babilônica` | 1 | — |
| `variação` | `é-análogo-a` | 1 | — |
| `variação` | `é-equivalente-feminino-de` | 1 | — |
| `variação` | `é-equivalente-grego` | 1 | — |
| `variação` | `é-metáfora-para` | 1 | — |
| `variação` | `é-padrão-de` | 1 | — |
| `variação` | `é-versão-moderada-de` | 1 | — |
| `opõe-se-a` | `distingue-se-de` | 25 | — |
| `opõe-se-a` | `opõe-se-a` | 23 | — |
| `opõe-se-a` | `confronta` | 6 | — |
| `opõe-se-a` | `propõe` | 5 | — |
| `opõe-se-a` | `distingue-se` | 4 | — |
| `opõe-se-a` | `critica` | 3 | — |
| `opõe-se-a` | `é-resistência-a` | 3 | — |
| `opõe-se-a` | `afronta` | 2 | — |
| `opõe-se-a` | `contrapõe-a` | 2 | — |
| `opõe-se-a` | `denuncia` | 2 | — |
| `opõe-se-a` | `inverte` | 2 | — |
| `opõe-se-a` | `resiste-a` | 2 | — |
| `opõe-se-a` | `resistido-por` | 2 | sim |
| `opõe-se-a` | `é-exceção-a` | 2 | — |
| `opõe-se-a` | `contraponto-a` | 1 | — |
| `opõe-se-a` | `crítica` | 1 | — |
| `inclui` | `estrutura-se-por` | 14 | — |
| `inclui` | `integra` | 13 | — |
| `inclui` | `compõe` | 12 | — |
| `inclui` | `inclui` | 7 | — |
| `inclui` | `organiza` | 6 | — |
| `inclui` | `divide-se-em` | 4 | — |
| `inclui` | `organiza-se-em` | 3 | — |
| `inclui` | `abrange` | 2 | — |
| `inclui` | `condensa` | 2 | — |
| `inclui` | `contêm` | 2 | — |
| `inclui` | `incluído-em` | 2 | — |
| `inclui` | `organizada-por` | 2 | sim |
| `inclui` | `organizados-por` | 2 | sim |
| `inclui` | `contém-germe-de` | 1 | — |
| `controla` | `orienta` | 13 | — |
| `controla` | `investe` | 4 | — |
| `controla` | `investido-por` | 4 | sim |
| `controla` | `avaliado-por` | 3 | sim |
| `controla` | `assessora` | 2 | — |
| `controla` | `assume-regência` | 2 | — |
| `controla` | `dita-por` | 2 | sim |
| `controla` | `dominado-por` | 2 | sim |
| `controla` | `gerida-por` | 2 | sim |
| `controla` | `impõe-se-a` | 2 | — |
| `controla` | `mentor-de` | 2 | — |
| `controla` | `rege` | 2 | — |
| `controla` | `submete` | 2 | — |
| `controla` | `submetidos-a` | 2 | sim |
| `controla` | `tutoria` | 2 | — |
| `controla` | `é-vigiada-por` | 2 | sim |
| `controla` | `comandava` | 1 | — |
| `controla` | `controla` | 1 | — |
| `controla` | `lidera` | 1 | — |
| `controla` | `mestre-de` | 1 | — |
| `controla` | `orquestra` | 1 | — |
| `controla` | `é-controlado-por` | 1 | sim |
| `controla` | `é-mantida-por` | 1 | sim |
| `controla` | `é-mantida-via` | 1 | sim |
| `controla` | `é-rainha-de` | 1 | — |
| `transfere` | `enviado-a` | 8 | — |
| `transfere` | `transfere-para` | 8 | — |
| `transfere` | `transporta` | 6 | — |
| `transfere` | `destinação-gerida-por` | 4 | — |
| `transfere` | `destino` | 4 | — |
| `transfere` | `recebe` | 4 | — |
| `transfere` | `recebida-por` | 3 | sim |
| `transfere` | `transportado-por` | 3 | sim |
| `transfere` | `destinada-a` | 2 | — |
| `transfere` | `destinado-a` | 2 | — |
| `transfere` | `destinação-de` | 2 | — |
| `transfere` | `orienta-destinação-em` | 2 | — |
| `transfere` | `recebeu-visitas-de` | 2 | — |
| `transfere` | `carrega` | 1 | — |
| `transfere` | `destinatário` | 1 | — |
| `transfere` | `transferiu-doença-para` | 1 | — |
| `transfere` | `trouxe` | 1 | — |
| `envolve` | `protagoniza` | 11 | — |
| `envolve` | `agente` | 9 | — |
| `envolve` | `envolve` | 4 | — |
| `envolve` | `participa-de` | 4 | — |
| `envolve` | `agentes` | 2 | — |
| `envolve` | `autores` | 2 | — |
| `envolve` | `co-executa` | 2 | — |
| `envolve` | `está-envolvido` | 2 | — |
| `envolve` | `pertence-a` | 2 | — |
| `envolve` | `protagonistas` | 2 | — |
| `envolve` | `é-protagonista-de` | 2 | — |
| `envolve` | `doadores` | 1 | — |
| `envolve` | `envolvida-em` | 1 | — |
| `envolve` | `habitantes` | 1 | — |
| `envolve` | `integrante` | 1 | — |
| `envolve` | `portadores` | 1 | — |
| `envolve` | `é-agente-de` | 1 | — |
| `envolve` | `é-coautor-de` | 1 | — |
| `envolve` | `é-coautora-de` | 1 | — |
| `envolve` | `é-criminoso-de` | 1 | — |
| `é-um` | `é-um` | 16 | — |
| `é-um` | `é-alvo-de` | 4 | — |
| `é-um` | `é-família-de` | 3 | — |
| `é-um` | `é-progressivamente-livre-de` | 3 | — |
| `é-um` | `primeiro-caso` | 2 | — |
| `é-um` | `é-da-espécie` | 2 | — |
| `é-um` | `é-estado-de` | 2 | — |
| `é-um` | `é-evento-de` | 2 | — |
| `é-um` | `é-fenômeno-de` | 2 | — |
| `é-um` | `é-uma-espécie-de` | 2 | — |
| `é-um` | `é-1ª-tentativa` | 1 | — |
| `é-um` | `é-1ª-tentativa-fracassada` | 1 | — |
| `é-um` | `é-2ª-tentativa-de` | 1 | — |
| `é-um` | `é-2ª-tentativa-fracassada` | 1 | — |
| `é-um` | `é-3ª-tentativa-sucesso` | 1 | — |
| `é-um` | `é-biodemo` | 1 | — |
| `é-um` | `é-biodemo-com` | 1 | — |
| `é-um` | `é-biodemo-de` | 1 | — |
| `é-um` | `é-espécie-de` | 1 | — |
| `é-um` | `é-irmão-de` | 1 | — |
| `é-um` | `é-mente-desmembrada-em` | 1 | — |
| `é-um` | `é-tragado-em` | 1 | — |
| `é-um` | `é-vingança-via` | 1 | — |
| `representa` | `manifesta-se-em` | 20 | — |
| `representa` | `expressão` | 4 | — |
| `representa` | `personifica-em` | 4 | — |
| `representa` | `tem-forma` | 3 | — |
| `representa` | `expressa-sociabilidade-por` | 2 | — |
| `representa` | `manifesta-descontinuidade-em` | 2 | — |
| `representa` | `manifesta-se-no-discurso-como` | 2 | — |
| `representa` | `retrata-antes-da-queda` | 2 | — |
| `representa` | `expressa-se-como` | 1 | — |
| `representa` | `expressa-se-em` | 1 | — |
| `representa` | `manifesta-em` | 1 | — |
| `representa` | `manifesta-se-via` | 1 | — |
| `representa` | `personifica-se-como` | 1 | — |
| `representa` | `tem-expressão` | 1 | — |
| `representa` | `é-expressão-de` | 1 | — |
| `representa` | `é-manifestação-de` | 1 | — |
| `representa` | `é-personificação-de` | 1 | — |
| `representa` | `é-representante-de` | 1 | — |
| `sucede` | `sucede` | 15 | — |
| `sucede` | `desdobramento` | 11 | — |
| `sucede` | `encerra-com` | 4 | — |
| `sucede` | `marca-fim-de` | 4 | — |
| `sucede` | `continua` | 2 | — |
| `sucede` | `desfecho-de` | 2 | — |
| `sucede` | `ocorre-após` | 2 | — |
| `sucede` | `sucedido-por` | 2 | sim |
| `sucede` | `termina-com` | 2 | — |
| `sucede` | `encerra` | 1 | — |
| `sucede` | `encerra-se-com` | 1 | — |
| `sucede` | `é-posterior` | 1 | — |
| `sucede` | `é-último-de` | 1 | — |
| `danifica` | `rompe` | 6 | — |
| `danifica` | `rompida-por` | 4 | sim |
| `danifica` | `colapsa` | 3 | — |
| `danifica` | `contaminou-via` | 2 | — |
| `danifica` | `destruiu-mito-de` | 2 | — |
| `danifica` | `destruído-em` | 2 | — |
| `danifica` | `destrói` | 2 | — |
| `danifica` | `mata` | 2 | — |
| `danifica` | `obscurece` | 2 | — |
| `danifica` | `pode-colapsar-em` | 2 | — |
| `danifica` | `reaparece-como-destruição-em` | 2 | — |
| `danifica` | `vitima` | 2 | — |
| `danifica` | `apaga-via` | 1 | — |
| `danifica` | `apagou` | 1 | — |
| `danifica` | `combate` | 1 | — |
| `danifica` | `corrompe-via` | 1 | — |
| `danifica` | `desestrutura` | 1 | — |
| `danifica` | `destruiu-centralizado-em` | 1 | — |
| `danifica` | `destruiu-clone-de` | 1 | — |
| `danifica` | `distorce` | 1 | — |
| `danifica` | `freia` | 1 | — |
| `danifica` | `interrompeu` | 1 | — |
| `danifica` | `rompe-com` | 1 | — |
| `danifica` | `rompeu-lacre-de` | 1 | — |
| `danifica` | `são-primeiras-vítimas-de` | 1 | — |
| `danifica` | `tem-problemas-com` | 1 | — |
| `danifica` | `trucidou-via` | 1 | — |
| `danifica` | `vitimas` | 1 | — |
| `protege` | `sustenta` | 6 | — |
| `protege` | `alimenta` | 4 | — |
| `protege` | `suporta` | 4 | — |
| `protege` | `sustentada-por` | 4 | sim |
| `protege` | `liberta-de` | 3 | — |
| `protege` | `protege` | 3 | — |
| `protege` | `alimentada-por` | 2 | sim |
| `protege` | `estabiliza` | 2 | — |
| `protege` | `guarda` | 2 | — |
| `protege` | `reabilita` | 2 | — |
| `protege` | `regenera-na-narrativa` | 2 | — |
| `protege` | `sustenta-ponte-não-local` | 2 | — |
| `protege` | `sustentam` | 2 | — |
| `protege` | `valoriza` | 2 | — |
| `protege` | `alimenta-se-de` | 1 | — |
| `protege` | `antídoto` | 1 | — |
| `protege` | `apoia` | 1 | — |
| `protege` | `dá-suporte-a` | 1 | — |
| `protege` | `liberta` | 1 | — |
| `precede` | `precede` | 12 | — |
| `precede` | `antecede` | 7 | — |
| `precede` | `inicia` | 7 | — |
| `precede` | `inicia-em` | 3 | — |
| `precede` | `iniciado-por` | 2 | sim |
| `precede` | `superior-a` | 2 | — |
| `precede` | `acima-de` | 1 | — |
| `precede` | `começa-em` | 1 | — |
| `precede` | `nível-abaixo-de` | 1 | — |
| `precede` | `primeiro-ocorreu-em` | 1 | — |
| `precede` | `é-memória-mais-antiga-de` | 1 | — |
| `precede` | `é-primeiro-demo` | 1 | — |
| `parte-de` | `parte-de` | 25 | — |
| `parte-de` | `é-fase-de` | 4 | — |
| `parte-de` | `fase-de` | 2 | — |
| `parte-de` | `é-ilha-de` | 2 | — |
| `parte-de` | `é-componente-de` | 1 | — |
| `parte-de` | `é-extensão-de` | 1 | — |
| `parte-de` | `é-parte-de` | 1 | — |
| `parte-de` | `é-parte-mais-bela-de` | 1 | — |
| `explica` | `explica` | 11 | — |
| `explica` | `qualifica` | 7 | — |
| `explica` | `explicado-por` | 4 | sim |
| `explica` | `descreve-transferência-de` | 2 | — |
| `explica` | `diagnosticou` | 2 | — |
| `explica` | `reescreveu-história-de` | 2 | — |
| `explica` | `revela` | 2 | — |
| `explica` | `revelada-a` | 2 | — |
| `explica` | `revelado-por` | 2 | sim |
| `explica` | `reescreveu` | 1 | — |
| `explica` | `é-qualificada-como` | 1 | — |
| `comunica` | `proferida-por` | 5 | sim |
| `comunica` | `responde-por` | 5 | sim |
| `comunica` | `comunica-com` | 3 | — |
| `comunica` | `responde-a` | 3 | — |
| `comunica` | `resposta-a` | 3 | — |
| `comunica` | `anunciada-por` | 2 | sim |
| `comunica` | `escrita-por` | 2 | sim |
| `comunica` | `escrito-por` | 2 | sim |
| `comunica` | `primeira-resposta-a` | 2 | — |
| `comunica` | `é-resposta-a` | 2 | — |
| `comunica` | `anuncia` | 1 | — |
| `comunica` | `convoca` | 1 | — |
| `comunica` | `mensageiros` | 1 | — |
| `comunica` | `mensagem` | 1 | — |
| `comunica` | `reconhece-que-humanos-são` | 1 | — |
| `comunica` | `replica-resposta-a` | 1 | — |
| `requer` | `necessário-a` | 8 | — |
| `requer` | `requer` | 6 | — |
| `requer` | `base-de` | 4 | — |
| `requer` | `baseada-em` | 4 | — |
| `requer` | `depende-de` | 4 | — |
| `requer` | `condição-de` | 3 | — |
| `requer` | `base-do` | 2 | — |
| `requer` | `subordinada-a` | 2 | — |
| `requer` | `base` | 1 | — |
| `requer` | `tem-condição` | 1 | — |
| `observa` | `observa` | 4 | — |
| `observa` | `mapeia` | 3 | — |
| `observa` | `descoberto-por` | 2 | sim |
| `observa` | `estudado-por` | 2 | sim |
| `observa` | `experimenta` | 2 | — |
| `observa` | `mapeado-por` | 2 | sim |
| `observa` | `mede` | 2 | — |
| `observa` | `medida-por` | 2 | sim |
| `observa` | `observa-de-dentro` | 2 | — |
| `observa` | `observado-de-dentro-por` | 2 | sim |
| `observa` | `percebido-por` | 2 | — |
| `observa` | `reconhece` | 1 | — |
| `observa` | `reconheceu` | 1 | — |
| `observa` | `reconhecida-por` | 1 | sim |
| `observa` | `registra` | 1 | — |

## 4. Novos rótulos (13) e justificativa do ganho semântico

| Novo rótulo | Ocorrências | Por que não coube nos 10 aprovados |
|---|---|---|
| `origina` | 212 | Separa "quem gera/gera-se de quem" de mera associação; 212 ocorrências, o maior domínio novo. |
| `causa` | 96 | Distingue consequência/efeito de origem genealógica; evita fundir criação e causalidade. |
| `precede` | 39 | Anterioridade temporal/hierárquica não é redutível a inclusão nem a causalidade. |
| `sucede` | 48 | Posterioridade, desdobramento e encerramento formam o par temporal de `precede`. |
| `explica` | 36 | Interpretar/definir/revelar é uma operação sobre o sentido, não sobre a coisa. |
| `requer` | 35 | Dependência e premissa invertem a leitura de `usa`/`inclui`; exigem rótulo próprio. |
| `representa` | 49 | Manifestação/expressão difere de `variação`: o termo é suporte de outro, não seu sinônimo. |
| `comunica` | 35 | Mensagem, resposta e anúncio têm emissor/destinatário; não cabem em `associado`. |
| `transfere` | 54 | Movimento e destinação têm origem e destino explícitos; difere de `usa` e de `contexto`. |
| `protege` | 45 | Sustentação/benefício é o polo positivo ausente do vocabulário aprovado. |
| `danifica` | 47 | Dano/destruição é o polo negativo; `opõe-se-a` cobre contraste, não agressão. |
| `controla` | 57 | Comando/gestão/regência é relação de poder, distinta de `usa` (instrumento). |
| `observa` | 29 | Percepção, medição e avaliação são atos epistêmicos, não de participação (`envolve`). |

## 5. Regras de direção aplicadas

1. `← ` no tipo bruto → `<-`; ausência de seta → `->`.
2. Raiz semântica `associado` → `<->` (decisão curatorial 3).
3. Formas passivas/inversas (`-por`, `-de`, `resulta-de`, `é-obra-de` etc.) → direção invertida. 126 linhas foram ajustadas; a inversão está registrada em `notas_de_normalizacao`.
4. `<->` nunca é invertido (relação simétrica).

## 6. Governança das células vazias (decisão do curador)

- As linhas sem relação controlada (família "sem aresta", `—` e congêneres) **permanecem** na tabela final de cinco colunas `Termo | Código | Relação | Direção | Notas`, com a observação em `Notas`.
- Na **materialização** da tabela de cinco colunas, toda célula de `Relação` ou `Direção` que deva ficar vazia será preenchida com **um único hífen ASCII `-`** — nunca com célula vazia, `—` (traço longo) ou `n/a`. Isso preserva a integridade estrutural da tabela Markdown.
- Na **matriz CSV**, essas células continuam **estritamente vazias**, conforme a decisão anterior do curador ("*(deixar em branco)*"). O `-` é uma regra de saída, não um valor do vocabulário controlado.

## 7. O que ficou de fora desta rodada

- **48 linhas `REVISAR`** (51 ocorrências): resolvidas em 2026-10-25 pelo fallback aprovado (seção 9); nenhuma permanece pendente.
- **31 linhas `APROVADO`** (5.975 ocorrências): nenhum campo foi alterado.
- 6 rótulos das 45 seções não conformes que não têm linha no CSV; 91 itens de lista livre; 4 rótulos de tabelas padrão embutidas; 3 linhas `aresta pré-existente; arquivo existe`.
- 17 linhas de 4 colunas em fichas conformes (RC-671, RC-672, RC-684) — cobertas pela nota de `—`, ainda sem regra de conversão estrutural.

## 8. Checklist para aprovação final

- [x] Aprovar as 23 relações controladas.
- [x] Aprovar as 13 novas relações e suas definições.
- [x] Aprovar o mapeamento dos 567 clusters (seção 3).
- [x] Aprovar as inversões de direção (seção 5).
- [x] Confirmar a regra do hífen `-` (seção 6).
- [x] Definir o tratamento das 48 linhas `REVISAR` (seção 9).
- [x] Autorizar a implementação da tabela de cinco colunas — **Fase 1 (776 fichas conformes) executada**; Fase 2 (45 exceções) aguarda aprovação do Anexo B.

> Até a aprovação, nenhuma ficha será modificada. A matriz pode ser revertida a qualquer momento: as colunas `tipo_bruto` e `ocorrencias` permanecem idênticas à extração T1 (SHA-256 `43ad4e8083ce83d5facb39b082488031625d81dd92e827f56938fdafa7d05213`; soma 7.761).

## 9. Resolução da cauda longa e Implementação Física — Fase 1

**Data:** 2026-10-25 · **Despacho:** aprovação integral dos itens 1 a 5 do checklist + autorização de reescrita das 776 seções conformes.

### 9.1 Matriz 100% concluída

| Ação | Resultado |
|---|---|
| 48 linhas `REVISAR` | `relaciona-se-a` / `->`; texto bruto original **integral** transferido para `notas_de_normalizacao` com o prefixo `texto bruto original: ` |
| `decisao_curatorial` | **todas as 998 linhas = `APROVADO`** |
| `tipo_bruto` / `ocorrencias` | inalterados — SHA-256 `43ad4e8083ce83d5facb39b082488031625d81dd92e827f56938fdafa7d05213`; soma 7.761 |
| Relações controladas | 23 + 12 linhas sem relação (família "sem aresta" e `—`), que geram `-` nas fichas |

### 9.2 Reescrita das 776 seções conformes

Novo cabeçalho aplicado: `| Termo | Código | Relação | Direção | Notas |` com separador de 5 colunas.

| Métrica | Valor |
|---|---|
| Fichas reescritas | **776** (100% das seções conformes) |
| Linhas de relação convertidas | **7.761** (7.744 de 3 células + 17 de 4 células) |
| Tipos brutos da matriz efetivamente aplicados | **998 / 998** |
| Linhas com `Notas` preenchidas | 2.017 |
| Linhas com `Relação = -` e `Direção = -` | 297 |
| Seções com conteúdo extra fora da tabela | 44 (143 linhas preservadas literalmente) |
| Fichas **não** tocadas | 50 (45 exceções + 5 sem seção) |

Aplicação por linha: `Relação` e `Direção` vindas da matriz (ou `-` quando vazias); `Notas` = `notas_de_normalizacao` da matriz + eventuais notas originais da ficha (4ª célula das 17 linhas anômalas), unidas por `; `. Quando não há nota, a célula também recebe `-` — mesma regra de integridade estrutural aprovada para `Relação`/`Direção` (extensão registrada para sua confirmação).

As 17 linhas de 4 colunas (RC-671, RC-672, RC-684) tiveram `Termo`/`Código` preservados **na ordem original** (código-fonte na 1ª coluna, título na 2ª) e a 4ª célula migrada para `Notas`; nenhuma inversão de colunas foi feita.

### 9.3 Conteúdo preservado literalmente

As 143 linhas extras das 44 seções conformes **não** foram convertidas nem fundidas em `Notas`: são remissões (`- RC-xxx — ver ficha correspondente`, 53), listas suplementares de termos com código (70), blocos de citação/remissão (14), avisos de quarentena epistemológica (3) e subseções `### Remissão` (3). Convertê-las exigiria inventar relações — ficam para uma fase separada, se você autorizar.

### 9.4 Validação executada

- `git diff` linha a linha contra o HEAD: **0 alterações fora do bloco da tabela** nas 776 fichas.
- `Termo` e `Código` de cada uma das 7.761 linhas conferidos com o original.
- Todas as novas linhas têm exatamente 5 células; nenhuma contém `|` não escapado.
- 50 fichas não tocadas comparadas byte a byte com o HEAD: **0 divergências**.
- 45 exceções continuam com suas estruturas originais (classes A, B e C intactas).
- Finais de linha, ausência de newline final em 7 arquivos e codificação UTF-8 preservados.

## 10. Próxima etapa — 45 exceções

O método de conversão das classes A, B e C está detalhado no **Anexo B** de `admin/logs/T2-EXCECOES-RELACOES.md` e **aguarda sua aprovação**. Nenhuma dessas 45 seções foi modificada.
