# Auditoria Interna — Frente B: Builders — 11/09/2026

Leitura pura. Universo: `ferramentas/*.py` (10.265 linhas, das quais 3.178 são `dados_termos.py`). Pergunta: o que os builders realmente fazem, de onde bebem e onde quebram.

## B1. O espelho principal não lê as fichas (confirmação sistêmica do achado A)

`build_xlsx.py` (384 linhas) menciona `termos/` **apenas como texto** — literalmente a string `"(ver ficha completa em termos/)"` repetida nas células. Nenhuma linha de nenhuma ficha chega ao `.xlsx`. O mesmo vale para `build_indice.py` (só links) — e o `build_word.py` segue o mesmo padrão (cadastro + BIBLIO). **Os 2.323 blocos de conteúdo curatorial são invisíveis aos 3 espelhos.** Não é bug — é arquitetura: mas é arquitetura não-declarada, e o Curador deve decidir na Onda 2 *o que* o espelho deve conter (resumos? contagens? lastro?).

## B2. Três mecanismos de carga, zero módulo compartilhado

| Builder | Como carrega TERMOS/RELACOES |
|---|---|
| `build_xlsx.py`, `build_indice.py`, `verificar_verbetes.py` | `import` Python normal |
| `build_word.py` | `ast.parse` + `literal_eval` **do texto-fonte** de `dados_termos.py` (nunca importa!) |
| `build_word.py` ← `build_xlsx.py` | `ast`-scraping do **código-fonte de outro builder** para extrair a tabela BIBLIO |

Nenhum builder importa outro via Python (`grep` em `ferramentas/`: zero imports cruzados). Consequência: se `dados_termos.py` ganhar qualquer construção não-literal, o xlsx continua funcionando e o docx quebra — **os espelhos divergem silenciosamente por mecanismo de carga distinto**. Proposta (Onda 0/1): um `loader.py` único — uma função, três consumidores.

## B3. A bibliografia mora dentro do builder (dados-no-código, parte 2)

A tabela `BIBLIO` ("Lista bibliográfica completa") está hardcoded no `build_xlsx.py` — e o comentário diz **50 obras** enquanto há **100 entradas B**, contra **102 obras** na base. Três números, zero reconciliação. Notas como `"Aguardando PDF"` e datas de ago/2026 estão congeladas no código. É o mesmo anti-padrão do R1, em menor escala: **dado que muda com o tempo morando em arquivo que finge ser lógica**. Proposta: BIBLIO migra para os dados canônicos (Onda 1) junto com o cadastro.

## B4. Metadados congelados nos builders

Textos de cabeçalho de sheet, carimbo `"2026-08-14"` em linhas geradas, notas editoriais — tudo literal no código. Cada rebuild "novo" republica metadados de agosto. Baixo dano hoje (ninguém lê o carimbo), mas é o mecanismo pelo qual **espelhos gerados apodrecem sem ninguém notar**. Proposta: carimbo = data do build (`datetime.now`, já importado no word) + versão da base.

## B5. Zero tratamento de erro nos 3 builders principais

`try:` aparece **0 vezes** em `build_xlsx.py`, `build_word.py` e `build_indice.py`. Uma linha malformada no cadastro aborta o build com traceback cru, sem dizer *qual termo* quebrou. Fail-fast é bom; fail-cryptic não. Proposta (Onda 0, junto com o test-suite): validar antes de construir, e embrulhar o loop por termo com contexto (`raise ... from` com o código RC).

## B6. ~3.900 linhas fora do fluxo P6/P7 (dormência a decidir, não a presumir)

| Script | Linhas | Invocado pelo P6/P7? | Último uso conhecido |
|---|---|---|---|
| `motor.py` | 1.547 | Não | Era esteira-leve (docs 29–31/08) |
| `visor_workspace.py` | 1.177 | Não (servidor HTTP; inviável no sandbox) | Idem |
| `build_apostila.py` | 371 | Não | Linha apostilas (outro fluxo) |
| `build_mapa_abstracao.py` | 341 | Não | Uso pontual |
| `gerar/restaurar_pacotes.py` | 355 | Não | Era migração de chats |
| `build_indice_enciclopedia*.py` | 1.005 | Não | Linha Enciclopédia/verbetes (outro fluxo) |
| `_*.py` (6 legados) | ~1.300 | Não | Uso único, históricos |

Nenhum `.py` os importa; todas as referências estão em `.md` da era anterior. **Não estou propondo apagar** — parte serve a outros fluxos (Enciclopédia, apostilas). Proposta: cada script ganha uma linha de "dono e status" no cabeçalho (`ATIVO-FLUXO-X` / `DORMENTE-DESDE-<data>` / `LEGADO-ARQUIVAR`), e os legados `_*.py` mudam para `ferramentas/legacy/` (Onda 0, consensual com o auditor).

## B7. Workaround são, para contraste

`build_indice.py::ficha_link` resolve o arquivo real por glob em vez de derivar slug — com comentário datado explicando o motivo ("o slug derivado errava 101/652 links"). É assim que workaround deve envelhecer: **datado, explicado e com fallback**. O `slug()` de 25 linhas segue ali como fallback — candidato a remoção quando o loader único existir.

## B8. `verificar_verbetes.py`: pequeno, bom, estreito

88 linhas, 3 regex, zero dependência externa — o melhor código do diretório. Limitação conhecida e assumida: só cobre verbetes, não fichas, não relações, não badges. Proposta: mantê-lo intacto e construir o test-suite *ao redor* dele (ele vira um dos checks, não o único).

## Síntese da Frente B

Os builders são **fiéis ao cadastro e cegos às fichas**, carregam a verdade por **três mecanismos distintos**, hospedam **dados (BIBLIO) no código**, e dividem o diretório com **~5.200 linhas** de outros fluxos/eras sem placa de status. Nenhum desses problemas quebra o build de hoje — todos são do tipo que quebra o build de amanhã, na véspera de uma entrega. Recomendação central: **loader único + BIBLIO-nos-dados + placas de status** (todos Onda 0/1, nenhum quebra compatibilidade).
