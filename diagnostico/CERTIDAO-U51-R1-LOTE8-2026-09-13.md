# CERTIDÃO — U51 · DOIS ATOS
## (A) Homologação do censo v3 e guarda E3 · (B) R1 · LOTE 8: os 6 da B005

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** (1) censo v3 **homologado** como instrumento de referência, para o censo de *gaps* **e para a guarda E3**, substituindo integralmente a v2; (2) RC‑309 sai do congelamento da R3, integra o poço da R1 e **não deve ser processada isoladamente** — aguarda o lote natural da B022; (3) lote 8 APROVADO (os 6 da B005); (4) R3 e R4 congelados
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

# ATO A — Homologação do censo v3

## A.1 O que mudou, em código

`ferramentas/materializar_lote.py` — a guarda **E3** passa a ler os censos nesta ordem:

1. `CENSO-V3-ESPACADAS-2026-09-13.json` **(v3 — referência homologada)**
2. `CENSO-RECLASSIFICADO-2026-09-13.json` (v2, se a v3 faltar)
3. `CENSO-GAP-FICHAS-2026-09-13.json` (v1, por último)

A v2 **não foi apagada**: fica arquivada como histórico e contraprova, reproduzível por `python3 ferramentas/censo_gap_v2.py --sem-espacadas --saida=<base>` (0 divergências em 273 códigos).

Despacho lavrado em `diagnostico/DESPACHO-CENSO-V3-HOMOLOGADO-2026-09-13.md`.

## A.2 RC‑309 — reportada e intocada

Conforme a diretriz, RC‑309 «Ordem dos Indecifráveis» **não foi processada**: nenhuma ficha aberta, nenhum fragmento extraído, nenhuma aresta tocada. Ela deixa o bloco congelado da R3 (era D) e passa a integrar o poço da R1 (agora B), **à espera do lote natural da B022**.

## A.3 Três reparos de governança no driver

Ao materializar a gaveta da RC‑362 (que traz uma tabela), três defeitos do `materializar_lote.py` vieram à tona. Todos reparados:

| # | Defeito | Reparo |
|---|---|---|
| 1 | O driver prefixava **cada** linha da gaveta com «‑ », decidindo ele a formatação — o que quebrava tabelas e parágrafos | **Renderização neutra**: o driver grava o que o lote diz; o lote decide (listas, parágrafos, tabelas) |
| 2 | Re-executar um lote já materializado **abortava** («linha não casa com o padrão da tupla») porque o cadastro já está `True` | **Idempotência**: `True)` é aceite como «já feito» |
| 3 | O driver recusava sobrescrever ficha existente, o que **impedia o ritual da prova de regeneração** | **`--sobrescrever`**, explícito: compara byte a byte, só reescreve se divergir, e deixa `.bak` quando reescreve |

**Prova das três ao mesmo tempo:** para que as três fichas com gaveta do lote 4 (RC‑116, RC‑138, RC‑140) continuassem idênticas depois de o driver parar de pôr os «‑ », os marcadores passaram a constar explicitamente do `U47-R1-LOTE4-2026-09-13.json`. Re-executou-se o lote 4 inteiro com `--sobrescrever`:

```
U47 (25 fichas) re-executado → 25/25 idênticas ao HEAD, byte a byte
   · o JSON do lote mudou (3 fichas ganharam «- » explícito)
   · NENHUMA ficha mudou
```

É a compensação exacta: o que o driver deixou de fazer, o lote passou a dizer.

## A.4 Dívida registrada — RC‑118

A gaveta de **RC‑118 (Val Dimon)** foi lavrada **à mão** na U48, porque RC‑118 **não pertence a nenhum lote**: a sua ficha é anterior ao driver `materializar_lote.py` (foi materializada fora da esteira R1). Com a renderização neutra, o arquivo fica correcto tal como está — ele já traz os «‑ » literais —, mas **não é regenerável por lote**, o que contraria a regra de que gavetas se regeneram pelo driver.

Fica registrado como **dívida de governança**, a sanar quando RC‑118 for reprocessada. Nenhuma outra ficha está nessa condição: todas as demais gavetas (RC‑116, RC‑138, RC‑140, RC‑362) nascem do JSON do respectivo lote.

---

# ATO B — R1 · LOTE 8: os 6 que declaram a B005 (*Fator Extraterrestre*, 2004)

## B.1 As seis fichas

| Cód. | Verbete | Frag. | Nota |
|---|---|---:|---|
| RC‑356 | Fonte da Vida (metáfora da ilha/oceano) | 6 | cap. 1 |
| RC‑358 | Terra de Ninguém (cósmica) | 5 | conceito |
| RC‑361 | Antropocentrismo (crítica) | 6 | conceito |
| RC‑362 | Apego aos Conceitos Terrenos | 8 | cap. 10 · **divergência interna** |
| RC‑363 | Ótica e Ética Cósmicas | 7 | cap. 11 |
| RC‑364 | A Missão do Mestre | 7 | cap. 6 · declara também B042 |
| | **6 fichas** | **39** | |

**B005: 6 → 0.** Quarta obra liquidada de um só golpe (B031 · B044 · B001 · B005).

**Nuance assinalada:** o despacho autorizou «6 códigos oriundos exclusivamente da obra B005». Cinco são exclusivos; **RC‑364 «A Missão do Mestre» declara também B042** no cadastro. Incluí-a por ser um dos 6 do poço reportado, e assinalo a diferença para o Curador decidir se a exclusividade é critério de corte.

## B.2 Divergência interna da fonte (RC‑362) — **nova ocorrência do caso Val Bon × Val Dimon**

A B005 grafa o título do capítulo 10 de **duas maneiras**:

| Posição | Linha | Grafia |
|---|---|---|
| Índice | B005 L30 | «Apego aos Conceitos **Terrenos**» |
| Corpo (cabeçalho do capítulo) | B005 L2959 | «10. APEGO AOS CONCEITOS **TERRESTRES**» |

Aplicou-se o despacho de 13/09/2026 (U48) sem adaptação: **as duas grafias são citadas *verbatim*, nenhuma foi normalizada, nenhuma foi eleita como «correcta»**, e a divergência está declarada na gaveta `## 6. Histórico Curatorial e Auditoria` com a etiqueta **[⚠️ DIVERGÊNCIA INTERNA DA FONTE]**. Diferentemente do caso Val Bon × Val Dimon, aqui a divergência é **dentro de um mesmo verbete**, entre duas posições da mesma obra — pelo que há uma gaveta, não duas, e nenhum cruzamento entre verbetes.

## B.3 Artefatos da B005

Cinco dos seis verbetes são **títulos de capítulo**, grafados em **caixa alta no corpo** e em caixa normal no Índice; as duas posições são citadas em cada ficha. Nenhuma normalização.

## B.4 Método e governança

- **39 fragmentos, 0 falhas.** A pré-conferência em bloco único pegou **2 erros meus** antes de o driver rodar: um deslocamento de uma linha em RC‑362 (o fecho «coisas sempre foram assim por aqui» está em L2981, não L2980) e outro em RC‑363 («impõe a conclusão de que os fins justificam o meio» está em L3259, não L3258). Ambos por transcrever de memória — a lição da U47, outra vez confirmada.
- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 6 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada.

## B.5 Efeito na Base

| Indicador | Antes (U50) | Depois (U51) |
|---|---:|---:|
| **Fichas** | 762 | **768** |
| **GAP** | 184 | **178** |
| Família B v3 — restantes | 78 | **72** |
| **B005 — restantes** | 6 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

Próximos poços: **P2024‑11‑30 6 · B015 5 · B048 5 · P2021‑02‑28 5 · B052 4 · B019 4 · B006 4 · B036 3**.

---

# INCIDENTE DE AMBIENTE (2ª vez, mesma receita da U48)

No meio desta unidade, **o sandbox foi recriado e perdeu os objetos do git**: o HEAD local voltou ao **U40** (`0a640cf`), enquanto o remoto já tinha **U41–U50**. Sintoma: `git show HEAD:termos/RC-110-val-am.md` → «exists on disk, but not in HEAD», e `remote.origin.fetch` apontava apenas ao ramo antigo.

**Nenhum conteúdo se perdeu** — as 768 fichas e todos os artefatos estavam no disco; perderam-se só os objetos do git. Receita aplicada:

1. `git config --add remote.origin.fetch '+refs/heads/arena/01a09ca0-termos-rc:…'` (senão o fetch não vê o ramo da sessão);
2. `git fetch origin arena/01a09ca0-termos-rc` → `FETCH_HEAD = 0e0ad58` (U50);
3. `git reset --mixed FETCH_HEAD` — **nunca `--hard`** — reancorando no remoto, que é a fonte da verdade;
4. `git checkout FETCH_HEAD -- .arena/SESSION-NOTES.md`, pois esse diretório fica fora do snapshot e perde os blocos de unidade (voltou com os 7 blocos U41–U50);
5. reanexo do bloco da U51 e commit.

O delta caiu de 133 para 11 arquivos — exactamente o da U51. Também se perderam `openpyxl`/`python-docx` (incidente U39, 3ª vez): reinstalados antes dos builds.

---

# VERIFICAÇÃO

```
python3 ferramentas/build_indice.py     -> 946 linhas
python3 ferramentas/exportar_json.py    -> 946 termos, 1887 relações, round-trip limpo
python3 ferramentas/build_xlsx.py       -> 946 | 768 | 1887 | 102
python3 ferramentas/build_word.py       -> 946 | 1887 | 102 | 768
python3 ferramentas/build_readme.py     -> 946/768/1887/102

python3 ferramentas/test_suite.py       -> 21/21  EXIT=0
   [T13] 768 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 768 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                             Base intacta: 946 · 768 fichas · 1887 relacoes

Lote 4 re-executado com --sobrescrever   -> 25/25 fichas idênticas ao HEAD
```

**Artefatos:** `diagnostico/DESPACHO-CENSO-V3-HOMOLOGADO-2026-09-13.md` · `ferramentas/materializar_lote.py` (E3 + 3 reparos) · `diagnostico/U47-R1-LOTE4-2026-09-13.json` (`- ` explícito nas gavetas) · `diagnostico/U51-R1-LOTE8-2026-09-13.json` · `termos/RC-356…RC-364-*.md` (6 fichas) · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
