# DESPACHO — CENSO v3 HOMOLOGADO
## 13/09/2026 · U51 · substitui a referência da v2 «no que conflitar»

**Decisão do Curador (transcrita do despacho que autorizou o lote 8):**

> «O Censo v3 fica oficialmente chancelado como o novo instrumento de
> referência para o censo de *gaps* e para a guarda E3, substituindo
> integralmente a v2. O resgate cirúrgico da RC-309 ("Ordem dos
> Indecifráveis") sem gerar falsos positivos valida perfeitamente a regra da
> caixa alta espaçada.»

---

## 1. Referência vigente

A partir desta unidade, o censo de referência é:

```
diagnostico/CENSO-V3-ESPACADAS-2026-09-13.json   ← referência
diagnostico/CENSO-V3-ESPACADAS-2026-09-13.md     ← relatório
```

Gerado por `python3 ferramentas/censo_gap_v2.py` (~20 s, 158 obras).

A v2 (`CENSO-RECLASSIFICADO-2026-09-13.*`) e a v1
(`CENSO-GAP-FICHAS-2026-09-13.*`) **não são apagadas**: continuam arquivadas
como histórico e como contraprova. A v2 é reproduzível a qualquer momento,
bit a bit, por `python3 ferramentas/censo_gap_v2.py --sem-espacadas
--saida=<base>` (0 divergências em 273 códigos, conferido na U50).

## 2. Guarda E3 atualizada

`ferramentas/materializar_lote.py` passa a ler os censos nesta ordem:

1. `CENSO-V3-ESPACADAS-2026-09-13.json` **(v3 — referência)**
2. `CENSO-RECLASSIFICADO-2026-09-13.json` (v2, se a v3 faltar)
3. `CENSO-GAP-FICHAS-2026-09-13.json` (v1, se as duas faltarem)

Efeito prático: a guarda E3 («família E — não achado no corpus») deixa de
barrar códigos que a v3 reconheceu como família B. **RC‑309** é o primeiro
caso: barrada como D pela v2, livre como B pela v3.

## 3. Diretriz para a RC‑309

> «A ficha sai oficialmente do congelamento (R3) e passa a integrar o poço da
> R1. Não a processe isoladamente agora. Deixe-a no poço aguardando o momento
> em que processarmos o lote natural da obra B022.»

RC‑309 «Ordem dos Indecifráveis» fica, portanto:

- **fora** do bloco congelado da R3 (era D);
- **dentro** do poço da R1 (agora B);
- **não processada** nesta unidade nem em lote avulso — aguarda o lote natural
  da **B022**, conforme o critério preferencial do Curador (liquidar
  agrupamentos de uma mesma fonte de um só golpe).

## 4. O que a v3 mudou, em suma

| Família | v1 | v2 | **v3** |
|---|---:|---:|---:|
| A · alias-variação | 6 | 6 | 6 |
| B · prosa citável na fonte declarada | 71 | 166 | **167** |
| C · prosa fora das fontes declaradas | 41 | 17 | 17 |
| D · só-estrutural | 104 | 21 | **20** |
| E · não achado no corpus | 40 | 52 | 52 |
| F · nome ambíguo | 11 | 11 | 11 |

A regra nova (colapso da caixa alta espaçada, **aplicada só no localizador**)
moveu **1 código em 273**: RC‑309, D → B. Nenhum código se perdeu; nenhum C e
nenhum E foi recuperado; nenhum falso positivo.

## 5. R3 e R4 permanecem congelados

R3 (17 C + 20 D) e R4 (52 E) seguem fora da esteira automatizada da R1.

## 6. ADENDO (U65) — o Censo é um ACHADOR, não uma CERCA

**Decisão do Curador (despacho do lote 22), homologando o alargamento de
leitura praticado na RC‑289 (U64):**

> «O Censo é um **ACHADOR (Finder)**, não uma **Cerca (Fence)**. […] O motor do
> censo existe para localizar a âncora inicial (o *hit* da *string*), mas a
> extração do conhecimento exige contexto. Desde que a expansão da leitura
> obedeça aos limites do capítulo/verbete e passe pelo Portão de Paridade
> Verbatim (garantindo que o texto extraído seja *byte a byte* idêntico à
> fonte), você tem total autonomia para alargar o raio de captura para
> encontrar a definição real. Excelente precedente arquitetural.»

**Regra, com as suas duas condições cumulativas:**

1. **Limite:** o alargamento vale **dentro da obra e do verbete** (o capítulo
   que sustenta o termo, ou o desenvolvimento do mesmo termo na mesma obra) —
   nunca para mudar de obra nem para importar conteúdo de outro código.
2. **Portão:** todo fragmento colhido por alargamento passa pelo **Portão de
   Paridade Verbatim**, exactamente como os do bloco original.

**Transparência:** sempre que uma ficha colher fragmentos fora dos blocos
indicados pelo censo, o facto é registrado nas observações da ficha, no
`../admin/logs/STATE-MIRROR.md` e na certidão da unidade, com as linhas alcançadas.

**Primeiras aplicações:** RC‑289 (U64) — o bloco do censo era só a abertura do
capítulo 5 da B020, e o vício só é nomeado em L2097–L2105; RC‑353 (U65) — os
blocos do censo (L304‑316, L87‑91, L325‑328 da B003) trazem apenas aplicações
da expressão, e a **definição** está em L973–L976.

---

*Despacho lavrado pelo motor a partir da decisão do Curador de 13/09/2026; a
guarda E3 foi atualizada na mesma unidade (U51). Adendo §6 lavrado na U65 por
decisão do Curador.*
