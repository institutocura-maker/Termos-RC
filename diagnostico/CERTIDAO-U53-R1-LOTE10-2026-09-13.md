# CERTIDÃO — U53 · R1 · LOTE 10
## O lote natural da B015 (*O Guardião do Éden*) + congelamento da série P

**Data:** 13/09/2026 (dia curatorial da campanha R1)
**Despacho:** lote 10 APROVADO (os 5 da B015) · **congelamento de todas as fontes da série P** (palestras/transcrição STT) decidido pelo Curador, com foco exclusivo no saldo das fontes série B até esgotar a literatura consolidada
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0**

---

## 1. As cinco fichas

| Cód. | Verbete | Frag. |
|---|---|---:|
| RC‑244 | Germe da Desconfiança | 6 |
| RC‑246 | Dez Sagrados (primeira geração do Criador) | 6 |
| RC‑247 | Endrelnianos | 8 |
| RC‑248 | Viajores da Rebelião | 7 |
| RC‑250 | Mundo das Águas | 6 |
| | **5 fichas** | **33** |

Os 5 são **exclusivos** da B015. 33 fragmentos verbatim intra-linha conferidos byte a byte, **0 falhas** na primeira passada. **B015: 5 → 0.**

## 2. O que a fonte diz — e o que a ficha não diz

O narrador da B015 é o **En Drel 29** (Zont), o guardião escalado para a Terra. A obra dá, de uma só vez, a génese dos Endrelnianos («organismos programados» para o exercício do poder do Criador, 374 membros, psiquismo grupal), a dos Dez Sagrados (os dez seres primordiais que «sobraram» da primeira geração, um dos quais foi «o mentor dos En Drel»), a dos Viajores da Rebelião (corpos animalizados como castigo, doentes a bordo, hibernação, e o surgimento dos «gigantes vindos de fora ou anunnakis»), e o **Germe da Desconfiança** como herança «do modo de ser do Criador» — a causa apontada para a «dificuldade insuperável» de as células unicelulares se reunirem em corpo pluricelular ao longo de cerca de 3 bilhões de anos.

Três abstinências, todas da mesma espécie:

- **«Mundo das Águas» = Terra?** A ficha **não** afirma por inferência. Ancora a identificação em duas falas do próprio narrador — «o mundo que chamais Terra» (L438) e «a raça humana do mundo das águas» (L579) — e cita as duas.
- **«Germe da desconfiança» como queda?** A fonte não o diz; a ficha não transporta leitura teológica.
- **Relação entre os Dez Sagrados e os Endrelnianos?** Só a que a fonte escreve («um deles foi o mentor dos En Drel»); nenhuma outra foi deduzida.

## 3. Duas grafias, uma só fonte (RC‑247)

A obra grafa a classe de **duas maneiras na mesma página**: «Endrelnianos» (L185, com maiúscula) e «os endrelnianos» (L448, com minúscula), além de «En Drel» e «em existência endrelniana» (L228). As formas estão todas citadas **verbatim**, sem normalização — mesmo critério do travessão × hífen da RC‑313 (U52) e do par Terrenos × TERRESTRES da RC‑362 (U51).

## 4. Nota de grafia de ficheiro (uniformização da campanha)

O slug de RC‑244 fora redigido `germe-da-desconfiança`, com cedilha. Verifiquei que **as 64 fichas da R1 sem excepção usam slug ASCII** (os 18 ficheiros com acentos em `termos/` são todos de unidades anteriores à campanha). Uniformizei para `germe-da-desconfianca` **antes** de materializar. Fica registrado como convenção da R1.

## 5. Congelamento da série P

Despacho lavrado em `diagnostico/DESPACHO-CONGELAMENTO-SERIE-P-2026-09-13.md`, com:

- o **motivo** (transcrição automática de fala: homófonos, truncamentos, oscilação de nomes próprios, ausência de paratexto estável — isto é, nenhum dos artefatos que o censo v3 aprendeu a ler);
- o **inventário** do poço congelado: **19 códigos** em 14 palestras;
- a **salvaguarda dos códigos mistos**: quem declare livro **e** palestra continua elegível, desde que se sustente só nas passagens do livro (mesmo critério que afastou RC‑300 do lote da B022);
- a **regra de reabertura**: por despacho expresso, com protocolo próprio (texto de referência, hesitações, oscilação gráfica, ancoragem da linha).

**Nada foi apagado:** os 19 códigos continuam no cadastro e no censo v3; o congelamento é de método, não de mérito.

| Poço da R1 (família B v3, após o lote 10) | Códigos |
|---|---:|
| **Activo — livros (série B)** | **46** |
| **Congelado — só palestras (série P)** | **19** |

Activo por obra: **B048 5 · B052 4 · B019 4 · B006 4 · B036 3 · B023 3 · B050 3 · B002 2 · B014 2 · B020 2 · B021 2 · B003 2 ·** demais 1 cada.

## 6. Governança e efeito na Base

- **V revogado mantido:** o lote declara `"v_revogado": true`, sem `aplicar_V`; as 5 nascem 🟡 provisório, `ficha False→True`, status preservado. **Nenhum 🟢 acrescentado**: 572 continuam 572.
- Nenhuma aresta nova em `relacoes/`; nenhuma memória deletada. O `diff` do registro-mestre são só os 5 sinalizadores `ficha`.
- **Espelhos .xlsx/.docx continuam adiados** por despacho vigente: congelados em **768 fichas**, com a Base em **775**. Nenhum teste da suíte os fiscaliza (T10–T15).

| Indicador | Antes (U52) | Depois (U53) |
|---|---:|---:|
| **Fichas** | 770 | **775** |
| **GAP** | 176 | **171** |
| Família B v3 — restantes | 70 | **65** (46 activos + 19 congelados) |
| **B015 — restantes** | 5 | **0** |
| Status do cadastro | 572🟢 · 212🟡 · 102🟠 · 60⚪ | inalterado |

---

## VERIFICAÇÃO

```
python3 ferramentas/test_suite.py        -> 21/21  EXIT=0
   [T13] 775 fichas com frontmatter
   [T14] tabelas == cadastro (M3) · divergentes: 0
   [T15] motor.fm_toml == frontmatter · 775 conferidas · divergentes: 0

python3 ferramentas/verificar_verbetes.py -> OK — todo verbatim confere byte a byte.
                                              Base intacta: 946 · 775 fichas · 1887 relacoes
```

**Artefatos:** `diagnostico/DESPACHO-CONGELAMENTO-SERIE-P-2026-09-13.md` · `diagnostico/U53-R1-LOTE10-2026-09-13.json` · `termos/RC-244-germe-da-desconfianca.md` · `termos/RC-246-dez-sagrados-primeira-geracao-do-criador.md` · `termos/RC-247-endrelnianos.md` · `termos/RC-248-viajores-da-rebeliao.md` · `termos/RC-250-mundo-das-aguas.md` · esta certidão.

---

*Lavrada pelo motor sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`.*
