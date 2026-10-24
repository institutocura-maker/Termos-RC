# NOTAS DE LEITURA — P2023-12-03 (o que ficou fora das camadas e não é dossiê)

1. **Este é o bruto mais concentrado já entrado na Arca.** Uma linha (U0004) tem 77.49% da fala
   — 79.509 caracteres seguidos, sem quebra. O efeito não é de relevância, é de **método**: foi preciso fatiar por fronteira
   de frase em 6 pedaços (ver `leitura-segmentada.txt`) e a cobertura foi provada por igualdade de texto. Registrar isso no
   ciclo serve de aviso a quem reler: quem disser `a fonte fala X na palestra` sem um `Uxxxx` **não leu a palestra**.

2. **O STT aqui tem outra patologia, não a mesma.** P2022-03-26 degradava termos técnicos (`processo ador`). Esta degrada
   **onomástica por contato**: os nomes próprios são os que pagam — `Túatha Dé Danann` sai como `toatas de Danão`,
   `tuatas de Danã`, `Estata de Danã`, `tos toatas de Danan de Serei`; o nome da experiência da nave sai em **4 formas**
   (`out long`, `auto langron`, `Alto Longró`, `alto langron`) dentro de um parágrafo; `chitta-vṛtti-nirodha` sai como
   `cita... Frits... niroda`. Nada foi corrigido na leitura, e o dicionário (§2 da camada 2) grava as formas como achado.

3. **Defeito encontrado no instrumento herdado — e consertado aqui.** O caça-âncoras dos ciclos anteriores normalizava por
   decomposição NFD, que **não decompõe `ç`** (U+00E7 não tem mapeamento canônico de decomposição). Toda âncora atravessando
   uma cedilha falhava e a falha era atribuída a quem digitou. Este ciclo traz o mapa `_EXTRA` no próprio `_aspas_P2023-12-03.py`
   (`ç→c`, `ø→o`, `đ→d`, `æ→ae`, `ß→ss`, `ð→d`, `þ→th`). Consequência prática: nos ciclos anteriores, toda âncora com `peça`,
   `cabeça`, `força` etc. **teria** abortado — o que levanta a questão de quantas âncoras foram reescritas para contornar o
   instrumento. Nada foi reaberto neste ciclo; fica declarado para o arquivo da casa.

4. **As máscaras são do STT, não da fonte.** Medido: 9 ocorrências (`p****`, `m****`, `m****`, `m****`, `e******`, `b******`), todas
   dentro de frase, nenhuma em posição de ênfase. A regra D-4 de P2022-03-26 vale: transcreve-se **como recebido**, sem
   purificação silenciosa e sem substituição por eufemismo. A fonte xinga mais do que mascara (`babacas`, `dementes`,
   `depravad*`, `bandidos`, `fracasso`), e a xingação é o **argumento**, não o desabafo: serve para descrever a conduta dos
   arcontes e a de quem governa. Por isso ela vai para a apostila e **não** para ficha de termo.

5. **A fonte diz o que não sabe — três vezes, com a razão.** `não sei quantos` (249.400), `não dá para falar aqui porque seria
   muito complexo` (o terceiro fator que parou o expurgo), `foram contra-atacados por uma força que eu não sei de quem é` e
   `isso eu não vou explicar aqui não, mas lá as gerações futuras vão entender`. Estas quatro automarcas de ignorância são as
   que autorizam a apostila a dizer *o que a fonte não disse*, e são a razão pela qual o dossiê propõe **0 códigos novos**.

6. **Há um trecho em que a frase se contradiz dentro do mesmo fôlego, e não é erro de digitação.** A definição triada de
   biodemo/demobio/demobiol: primeiro `aqui prevalece o biológico` para o biodemo, depois `prevalece o demo` para o demobio e,
   logo em seguida, para o demobiol, `o que prevalece é o biológico` — e o fecho usa `as duas últimas` (biodemo e demobiol) como
   os dois ingredientes do humano. O texto é assim; o glossário endereça com `[REVISAR]` e a apostila não resolve.

7. **A autocorreção numérica em direto é o melhor dado metodológico do ciclo.** `cerca de 1300 e pouco, não, 1700 e pouco,
   perto de 2000` — a fonte **refaz a conta ao vivo**. É a mesma conduta que P2022-03-26 tinha registrado no par dos números
   936/984. Consequência para a malha: os três valores entram com endereço; nenhum entra como `o` número.

8. **Duas frases que a Arca precisa decidir como tratar, porque nomeiam pessoas reais.** Chico Xavier aparece três vezes —
   uma como autoridade que `falou para a humanidade do século XX` (com data dada pelo autor: «no livro lançado em 1947, A Caminho da Luz.» (U0004)),
   uma numa história de bastidor (a fila, o ajoelhar, o `Eu sou castro` [REVISAR]) e uma como par do canal (`à moda do que
   Chico Xavier e Emanuel sinalizaram`). Divaldo Franco e `Valdemar Matoso` aparecem em testemunho de terceira mão, declarado
   como tal: `isso eu tô contando que Valdemar me contou`. Nenhuma dessas pessoas tem ficha, e nenhuma ganha: **0 fichas de
   pessoas** (D-12). O único endereço legítimo para a cadeia de encarnações do canal é RC-071 (Jan Val Ellam), com moldura.

9. **A palestra inteira é a resposta a uma pergunta feita um dia antes.** É o que a vizinha `P2023-12-02` registrou como
   `palestra preparatória`, e a fonte confirma três vezes com `ontem`. Para o índice, o par 02/12–03/12 de 2023 passa a ser
   a única dupla do acervo em que o segundo membro **estava anunciado pelo primeiro** — o que legitima, mas não antecipa,
   as 30 fichas que já carregam `P2023-12-02`.

10. **O que não é da fonte não entra no registro.** A coincidência entre o `máximo glacial há 23.000 anos` e as datas
    geológicas correntes, entre `12.800` e o Dryas recente, e entre `1 Enoque 69-70` e a lista dos vigilantes não serão
    escritas em ficha alguma: a esteira cataloga o que a fonte disse, com endereço, e nada além.
