# A5 — Reanexação das citações legadas: U91 (infraestrutura + piloto)

**Unidade:** U91 · **Lote:** `diagnostico/U91-R1-LOTE35-A5-2026-09-15.json`
**Data:** 15/09/2026 · **Rota:** R1 · **Despacho:** aparelho R1 estrito, sem tag nova
**Estado:** aplicado · suíte 21/21 · Portão B 778/778 + 100 · 17 verbetes reemitidos

---

## 1. A correcção de base: 439 / 219, não 418 / 240

O despacho de arquitectura dividia a dívida em «418 ancorados» e «240 à deriva».
A medição directa do censo (`A5-CITACOES-PRE-PORTAO-B-2026-09-14.json`) diz outra
coisa, e a diferença **favorece o determinismo**:

| | blocos | classes |
|---|---|---|
| **com localização** (`ancora != null`) | **442** | NULO 418 · PARCIAL 21 · EXATO 3 |
| **sem localização** | **221** | NULO 219 · AMBIGUO 2 |
| **dívida real (não-verbatim)** | **658** | **439** com localização + **219** sem |

Os 418 contavam só a classe `NULO`. Os **21 blocos `PARCIAL` também trazem
localização** e são os mais fáceis de todos — o único motivo de não fecharem é
uma elisão — e o despacho mandava-os para a triagem heurística. Os 3 `EXATO`
já são verbatim: só lhes falta o aparelho. `658 − 439 = 219`, não 240.

**Verificação de segurança:** os 442 e os 221 blocos caem **todos** em fichas
**sem lote**. Zero sobreposição com as 147 fichas regeneráveis — a A5 e o
*driver* nunca se cruzam.

## 2. A correcção de arquitectura: não é injecção, é substituição

O despacho previa «localizar a âncora e injectar o bloco imediatamente após
ela». Isso duplicaria o texto: os 658 blocos **já estão escritos nas fichas** —
foi de lá que o censo os leu. A âncora é uma coordenada **no corpus**
(`{obra, linha}`), não uma lacuna na ficha.

Medição que o prova (maior janela verbatim do parágrafo-fonte já presente na
própria ficha, 436 blocos ancorados):

| maior janela verbatim do fonte já na ficha | blocos |
|---|---|
| ≥ 20 palavras | 331 |
| ≥ 8 palavras | **426 de 436** |
| mediana | **28 palavras** |
| zero | 10 |

**O conhecimento nunca se perdeu.** O que faltava era a exactidão byte a byte e
o aparelho de linha. Consequência: o modo de falha é seguro. Se estivéssemos a
injectar texto novo, uma âncora errada produziria conteúdo alucinado; como
estamos a substituir uma transcrição pelo seu próprio original, uma âncora
errada faz o Portão B **falhar ruidosamente**.

## 3. O que foi construído

Duas ferramentas novas, o *driver* intocado (U83):

- **`ferramentas/extrair_fragmentos_a5.py`** — alinha as palavras do trecho
  legado contra o parágrafo-fonte (`difflib.SequenceMatcher`), agrupa as
  correspondências **por linha física**, recolhe o substring real de cada linha
  (o que faz o Portão B passar por construção) e emite o **lote declarativo**.
- **`ferramentas/reintegrar_citacoes.py`** — o aplicador cirúrgico. Substitui
  uma linha por outra, nada mais. **Importa `conferir()` de
  `materializar_lote`**: o Portão B é o mesmo código, não uma reimplementação.
- **`ferramentas/reemitir_verbetes_a5.py`** — a outra metade do mesmo commit
  (doutrina U87): um verbete que cite o trecho reanexado deixa de conferir e
  tem de ser reemitido na mesma unidade.

Por que não `materializar_lote.py`: o seu `corpo()` regenera a ficha inteira a
partir de um molde de 7 secções e destruiria `Ampliação`, `Atualização`,
`Reforço`. A A5 precisa de cirurgia — mas a cirurgia continua a ser **dados**.

## 4. As comportas

| | critério | reprovados |
|---|---|---|
| **G1** | cobertura 100% — nada do que a ficha diz se perde | 324 |
| **G2** | ≤ 6 fragmentos e ≤ 60 palavras (citação, não capítulo) | 25 |
| **G3** | nenhum fragmento só de símbolos (o `◆ ◆ ◆` separador de verbetes) | 0 |
| **G4** | nenhuma marca de censura/elisão da transcrição | 1 |
| **G5** | o Portão B (`conferir`) aceita cada fragmento na sua linha | 0 |
| **G6** | **contiguidade**: fragmentos consecutivos têem de ser contíguos na fonte | **14** |
| — | linha fora de qualquer parágrafo | 6 |

**G6 foi acrescentada depois de ler o inventário.** Na casa, `» … «` significa
*quebra de hard-wrap* («quando uma sentença foi partida, o seu início e o seu
fecho aparecem como fragmentos distintos»). Ora em RC-266 e RC-193 o alinhamento
saltava uma palavra — «à» na ficha contra «a» na fonte — e o marcador estaria a
encobrir uma **omissão** com o sinal de uma **quebra**. Mentira estrutural.
Os 14 blocos saíram do piloto para juízo curatorial.

**G2 existe porque truncar é suprimir.** Não se encolhe uma citação de 26
fragmentos para caber num blockquote: isso apagaria conteúdo da ficha.

## 5. O aplicador: comportas de execução

| | comporta |
|---|---|
| **A** | `conferir()` em cada fragmento **antes** de escrever; um falha → o lote aborta inteiro |
| **B** | a chave de localização tem de bater em **exactamente 1** linha; 0 ou 2 → aborta |
| **C** | nenhuma ficha com duas citações da mesma tupla |
| **D** | linha já com aparelho R1 → *idêntico* se for a que o lote produz, **conflito** se for outra |
| **E** | número de ficheiros por código == 1 |

## 6. Resultado

- **72 citações reanexadas · 100 fragmentos · 58 fichas**
- **27 fichas** com a quarentena epistemológica **levantada**; **31 parciais**
- **17 verbetes reemitidos** (20 citações distintas, 26 ocorrências)
- **zero linhas de corpo suprimidas** fora das 100 substituídas declaradas

Notas: onde todos os trechos da ficha foram reanexados, a nota da U86 é
substituída pela certidão (que cita a U86 — a cadeia de custódia fica). Onde
só alguns foram, a nota de quarentena **fica** (continua verdadeira) e
acrescenta-se um bullet a dizer quantos saíram. Uma ficha nunca mente sobre si.

## 7. Validação

| | |
|---|---|
| suíte | **21/21 OK** |
| Portão B (35 lotes) | **778/778** · 35/35 |
| Portão B (U91) | **100/100** fragmentos |
| idempotência | 2.ª corrida: **0 reescritas · 58 idênticas** |
| T5 verbetes | **0 falhas · 8 563 verbatim conferidos** |
| Base intacta | 946 termos · 820 fichas · 1 887 relações |
| diferencial | 100 linhas removidas · 131 inseridas · **0 anomalias** |

## 8. Três erros meus, todos apanhados pelas comportas

1. **Comporta C somava a tupla por fragmento, não por citação** — RC-002
   auto-colidia nos seus 4 fragmentos.
2. **Comporta B demasiado ingénua**: a chave de RC-002 bate em 2 linhas — a
   citação (L75) e uma nota curatorial que reproduz o mesmo trecho (L121).
   Passou a preferir linhas de blockquote de citação.
3. **Chave (`sigla`, `linha`) demasiado estrita**: `P2025-04-06` L32 tem
   **3 980 caracteres** e a ficha extrai-lhe duas citações distintas e
   legítimas (RC-794). A chave passou a incluir o primeiro fragmento.

Suspeitei ainda — e era falso — que `conferir()` estivesse a aceitar um
fragmento ausente da linha. Não estava: eu lia impressões truncadas a 110
caracteres. O Portão B está são.

## 9. Backlog para as unidades seguintes

| fila | blocos | unidade prevista |
|---|---|---|
| cobertura 90–99% | 169 | U92 |
| cobertura 70–89% | 117 | U93 |
| cobertura < 70% | 51 | U94 |
| G2 (citações longas, ≥ 7 fragmentos) | 25 | U94 — exigem decisão curatorial |
| G6 (fragmentos não contíguos) | 14 | U94 |
| linha fora de parágrafo | 6 | U94 — investigar |
| G4 (censura na transcrição) | 1 | U94 |
| **órfãos sem localização** | **219** | U95 — artefacto de diagnóstico |

**U95 não criará ficha de quarentena.** Um termo fora do cadastro quebraria os
números do selo (946/820/1887), o `build_indice` e o T14. A contenção já está
feita pela nota da U86 (478/478 fichas); os 219 órfãos ficarão isolados num
artefacto legível por máquina em `diagnostico/` — o *dataset* para a triagem
semântica futura, **tocando zero fichas**.

---

# U92 — a faixa 90–99% e o fosso que não era de truncamento

**Lote:** `diagnostico/U92-A5-LOTE36-2026-09-15.json` · **Data:** 15/09/2026

## 1. A premissa do despacho estava errada, e a medição prova-o

O despacho previa para esta faixa «validação mais fina nos limites de
truncamento». Medidos os 161 blocos da faixa 90–99%, **o fosso não está nos
limites**:

| posição do fosso | blocos |
|---|---|
| **meio** | 113 |
| fim + meio | 29 |
| fim | 13 |
| início + meio | 3 |
| início | 3 |

E a sua natureza não é conteúdo perdido:

| natureza do fosso | ocorrências |
|---|---|
| 1–2 palavras | 149 |
| artefacto de edição (`**negrito**`, `[...]`, `…`) | 91 |
| **aspas divergentes** (`'x'` na ficha contra `"x"` na fonte) | 91 |
| edição real de prosa | **2** |

**159 dos 161 blocos divergem por artefacto, não por conteúdo.** A ficha não
truncou a fonte: reescreveu-lhe a pontuação.

## 2. O remédio: alinhamento frouxo, emissão estrita

Duas camadas, com funções distintas:

- **Alinhar** com uma chave que despreza pontuação editorial (`frouxo()`), para
  que `'tzimtzum'` e `"tzimtzum"` contem como o mesmo token;
- **Emitir** sempre o substring REAL da linha-fonte, conferido byte a byte.

A ficha ganha assim a pontuação da **fonte**, não a do transcriptor. Nada se
perde, porque o artefacto nunca foi texto-fonte: `**negrito**` era formatação
da ficha; `[...]` era elisão do transcriptor.

## 3. Colheita

Corrida do extractor com `--frouxo` sobre os 442 blocos com localização:

| | |
|---|---|
| aprovados (G1–G6) | **103** |
| G1 cobertura < 100% | 243 |
| G2 citação longa | 44 |
| G6 não contíguos | 31 |
| já aplicados pela U91 | 47 |
| **NOVOS (U92)** | **56** |

## 4. Resultado

- **56 citações · 158 fragmentos · 55 fichas**
- **45 fichas** com a quarentena **levantada**; **10 parciais**
- **32 verbetes reemitidos** (42 ocorrências)

## 5. Validação

| | |
|---|---|
| suíte | **21/21 OK** |
| T5 verbetes | **0 falhas · 8 646 verbatim conferidos** |
| Portão B | **778/778** (R1) + **258** (A5: 100 U91 + 158 U92) = **1 036** |
| idempotência | 2.ª corrida: **0 reescritas · 55 idênticas** |
| Base intacta | 946 · 820 · 1 887 |

## 6. Três erros meus nesta unidade

1. **Comporta B insuficiente**: em RC-016 a chave bate em duas linhas — L49,
   que começa pelo trecho, e L51, uma citação maior que o contém no MEIO. Os
   filtros «é blockquote» e «começa por aspa» não separavam. Passou a exigir-se
   que a linha **COMECE** pelo trecho.
2. **A nota não era cumulativa**: RC-800 já trazia «1 de 3» da U91; a U92
   reescrevia «1 de 3» em vez de «2 de 3». A conta passou a ser derivada do
   **estado do arquivo** (quantos trechos legados já não existem como texto
   solto), o que a torna cumulativa entre unidades **e** idempotente.
3. **Nota duplicada**: quando a ficha passava a completa, eu substituía a linha
   de quarentena e deixava a nota parcial anterior ao lado — 5 fichas ficaram
   com duas notas (RC-785, RC-791, RC-797, RC-800, RC-826, RC-829). Corrigido
   removendo a anterior; as 5 foram repostas da baseline e reaplicadas.

## 7. Higiene

O lote da U91 foi lavrado como `U91-R1-LOTE35-A5-…json` e **colidia com o glob
`U*-R1-LOTE*.json`** dos lotes de materialização — o Portão B tentava
materializá-lo como lote R1 e falhava. Renomeados para
`U9x-A5-LOTEnn-2026-09-15.json`. Verificado: 35/35 lotes R1, 778 fragmentos,
0 falhas.

## 8. Backlog actualizado

| fila | blocos | unidade |
|---|---|---|
| cobertura 70–89% | 117 | U93 |
| cobertura < 70% | 51 | U94 |
| G2 (≥ 7 fragmentos) | 44 | U94 |
| G6 (não contíguos) | 31 | U94 |
| linha fora de parágrafo | 6 | U94 |
| G4 (censura) | 1 | U94 |
| **órfãos sem localização** | **219** | U95 |
