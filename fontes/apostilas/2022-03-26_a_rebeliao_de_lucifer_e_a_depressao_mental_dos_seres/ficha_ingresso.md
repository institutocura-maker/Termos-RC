# Ficha de ingresso — P2022-03-26 · *A Rebelião de Lúcifer e a Depressão Mental dos Seres*

## 1. Identificação

| campo | valor |
|---|---|
| código da fonte | `P2022-03-26` |
| arquivo recebido | `uploads_recepcao/2022-03-26 A Rebelião de Lúcifer e a Depressão Mental dos Seres.txt` |
| título curatorial | A Rebelião de Lúcifer e a Depressão Mental dos Seres |
| **tema nomeado pelo Curador** | o próprio ciclo: o Curador **indicou a palestra** (28-29/08/2026), sem abrir tema novo |
| data da fala | **sábado, 26/03/2022** (calendário, não memória) |
| local dito pela fonte | **São Paulo** — a única âncora de lugar do bruto (*se nós vamos continuar a fazer palestras aqui em São Paulo*) |
| ciclo de palestra | `apostilas/2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres/` |
| autor da fala | Jan Val Ellam (o próprio nome civil aparece 12× no bruto: *Rogério*) |
| formato | STT bruta, sem revisão, sem travessão de turno, com falas do auditório partidas em linhas próprias |

## 2. Cadeia de custódia

| elo | o que aconteceu | prova |
|---|---|---|
| upload | `Add files via upload` na branch `arena/01a04969-termos-rc`, **em cima do commit que fechou o ciclo anterior** | commit **`a02f12b`** (1 arquivo · +50 linhas) |
| workspace | o disco tinha sido **re-materializado** no commit-base da sessão: o bruto estava no remoto, não no índice do trabalho | `git status` após `git reset --mixed FETCH_HEAD` mostrava **exatamente 1** diferença: o arquivo novo |
| recuperação | adiantou-se o ponteiro da branch por **fast-forward** sobre `a02f12b` (sem reescrever história, sem `force-push`) e o arquivo veio com ela | `git merge-base --is-ancestor HEAD FETCH_HEAD` ✓ antes do movimento |
| integridade | SHA-256 do arquivo recebido | `1cc8a8c0777af896a0d96a160d535cabf008cb5bd5c76e9bd8c529f6b99253b9` |
| cópia | `cp` byte a byte para `original.txt` | `cmp` sem saída + SHA-256 **idêntico** nos dois lados |
| texto | nenhuma normalização aplicada | **150.335 bytes · 145.458 chars · 51 linhas · 50 CRLF preservados · 0 LF soltos · sem BOM** |
| ferramenta do ingresso | `_analise/_ingresso_P2022-03-26.py` (cópia, `cmp`, mapa de linhas, chunks, METADADOS-INGRESSO.json) | reexecutável; o bruto não é tocado por ela |

## 3. Estrutura medida

| grandeza | valor |
|---|---|
| chars totais / chars de fala | 145.458 / 145.295 |
| linhas lógicas com fala | 48 (+1 de título +1 vazia = 51 linhas) |
| palavras | 25.628 |
| períodos (ponto, interrogação, exclamação) | 1.609 |
| linhas pesadas (> 3.000 c) | **11**, somando 133.999 c = **92,2% da fala** |
| maior linha | U0005 · 27.614 c (18,9% da fala) — a cosmogonia inteira, sem quebra |
| falas curtas (3–150 c, o auditório) | **24** |
| o que o arquivo NÃO tem | 0 anunnaki · 0 Nibiru · 0 Enki/Enlil · 0 das grafas de 2020 (Shanlung, Shanai, *Alto Langron*, *isolamento cósmico*) · 0 Zont En Drel · 0 Moiras/Nornes |

Detalhe por linha em `analise/leitura-segmentada.txt`; mapa endereçado de 165 seções em
`analise/camada-0.txt` (toda seção resolvida por âncora, com o span medido).

## 4. O que este ingresso já corrige (e por isso fica registrado)

1. **A data de calendário, não a de memória.** A fonte diz *Ano passado, 756 defuntos norte-americanos* e
   *no ano 2019, Sofia esteve* e *há 3 anos atrás* — três ancoragens que **só fecham** se a fala é de
   **26/03/2022** (2019 + 3 anos = 2022 ✓; o ano anterior = 2021 ✓). A data do título está certa.
2. **O bruto é maior que qualquer um já processado.** +30.190 caracteres sobre P2020-04-25 (115.232), o
   anterior recordista. Não houve edição nenhuma para chegar aí.
3. **Não há turnos marcados, mas há duas vozes.** As 24 linhas curtas são interlocução; a linha U0004 é a
   única **repetição** pura do arquivo: as duas últimas palavras do fim de U0003 (*… Alagoano.*) reaparecem
   inteiras em U0004 — registro de defeito do STT, não escolha de quem transcreve.
4. **A piada recorrente tem dono.** O interlocutor gozado é chamado de *baiano* 8× e há 3 ocorrências de
   *Alagoan* — a primeira delas **dentro** da fala principal (fim de U0003), o que prova que a plateia está
   na transcrição e não só entre as linhas.
5. **Os seis nomes da roda ao vivo** (Marcelo 5×, Solange, Mara, Lila 2×, Elô, Narras) aparecem na
   última linha, quando a fonte pergunta a cadência que quer para as palestras. Ficam **no bruto**; não
   viram nada na Base.

## 5. Vocabulário que já se sabe presente (contagens do bruto, para o auditor)

`Sofia` 91 · `espírito` 97 · `vírus` 66 · `virótico` 5 · `biodemo` 46 · `Lúcifer` 39 · `rebelião` 26 ·
`Javé` 28 · `Javer` 1 · `Javel` 1 · `Javet` 1 · `Jah` 1 · `Jahé` 1 (as degradações, medida a medida, em `camada-2.txt` §3) · `depress*` 32 ·
`autist` 11 · `idiot` 3 · `esquizo` 1 · `demência/demente` 20 · `babac*` 9 · `colmei*/calmeic*` 8 · `processador/processadores/processo ador` 8+3+2 ·
`colmei*/calmeic*` — ver `camada-2.txt` §1 para o total · `processo ador` 2 · `28.869` 5 · `700.000` 8 · `suicid` 3 ·
`revólver` 1 · `baiano` 8 · `Alagoan` 3 · `Lula` 4 · `Bolsonar` 3 · `Trump` 2 · `Hillary Clinton` 1 ·
`favor divino` 5 · `2012` 1 · `2016` 1 · `2019` 2 · `São Paulo` 1 · `Mecão/Bahia/Vitória` — no exemplo
futebolístico · `t*****` 1 (o STT mascarou a palavra; fica assim).

## 6. Plano de leitura (executado nesta sessão)

9 chunks de ~16.000 caracteres (`analise/leitura/chunk-01..09.txt`), lidos **por inteiro**; as 11 linhas
pesadas auditadas seção a seção; o dicionário e o mapa produzidos por script (`_gerar_camadas_P2022-03-26.py`);
o dossiê e todas as suas aspas produzidos por `_gerar_dossie_P2022-03-26.py` sobre o caça-âncoras
`_aspas_P2022-03-26.py` (âncora que não bate exatamente **uma** vez aborta o arquivo); o auditor
`_verificar_verbatim_P2022-03-26.py` roda portão A e portão B sobre tudo que este ciclo escreveu.

## 7. Cadência e vizinhança

| | |
|---|---|
| **anterior imediata na Base** | `P2021-12-04` (Os Archeons de Ereon e os Seres Adhy) — 3 meses e 22 dias antes |
| **posterior imediata na Base** | `P2022-09-24` (Sophia, os Arcontes e a Disputa pela Suzerania Universal) — 6 meses depois |
| o vão que esta fonte fecha | **é a única palestra oral da Base no primeiro semestre de 2022**; entre 2021-12 e 2022-09 o acervo estava mudo |
| relação com o ciclo acabado de fechar | `P2020-04-25` é **o mesmo tema, 23 meses antes** — a Base tem agora duas fontes luciferianas com 700.000 anos em comum e números que em parte **batem** (620.000; a família em 736) e em parte **divergem** (984 × 936; 6.029 × 1.641) |
| estado da Base ao abrir o ciclo | **777 termos · 1.856 relações · 102 obras · 457 arquivos de ficha · 456 `ficha=True` · 69 apostilas em `CONCLUIDAS/`** |
| contexto do mundo na data | Brasil no segundo ano da pandemia; a fonte menciona SARS-CoV-2, toxoplasma, pós-verdade (2016), Brexit e as eleições de 2022 como o pano de fundo em que ela própria está falando |

## 8. Perguntas que o ingresso abre (e que o dossiê endereça)

1. Uma fala cujo argumento **depende** de nomes de pessoas públicas e de uma seção sobre suicídio entra na
   apostila integral? (Não há bloco isolável a cortar, como havia em 2020 — a decisão é de **moldura**.)
2. O uso de *autista*, *esquizofrênico*, *idiotia* e *demente* como categorias do divino vai para fichas?
3. A identificação **Javé = Sophia = Jesus = um mesmo espírito fateado** é registrada como tese datada de
   2022, ou como reforço da ficha de `P2023-04-29`?
4. Os **doze códigos do cluster Prabrajna** ganham anterioridade de 25 meses com esta fala? item a item.
5. `RC-089 Processador Val` — que aqui tem a definição de origem — é materializada neste ciclo?
6. *Espécie 250* e *espécie 315*: termo-observação sem código (precedente de *Shanai*)?
7. Os nomes novos sem cadastro (*Meor*, *Esferon*, *Valho*, *Chamba*, *Órbon*, *Aia/Aie*, *ZAM*) entram no
   dicionário da apostila com **[REVISAR]**, ou ficam só em camada-3?
8. O anúncio de livro com prazo (*Além da Ordenação do Caos*, dali a um mês) vai para o radar datado — e as
   **três** obras citadas que já existem viram cross-reference no BIBLIO das fichas?
9. As dez menções a políticos e a *Hillary Clinton* ficam na íntegra da apostila?
10. A correção feita em público (a guerra do Sol × a guerra do universo biológico, U0010–U0019) é transcrita
    como está, ou com nota de que a fonte refez o próprio quadro?

---

**Nada foi aplicado na malha.** O rito está no ponto de **esperar a devolutiva do Curador**: nem `termos/`,
nem `RELACOES`, nem `dados_termos.py`, nem `livros/` foram tocados por esta etapa.
