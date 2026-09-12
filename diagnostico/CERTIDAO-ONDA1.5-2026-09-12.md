# Certidão — Onda 1.5 · campos `via` + `confianca_fonte` (12/09/2026)

**Despacho:** Curador escolheu a **Opção A — regra interim derivada** (12/09/2026, ask_user `portador_1_5`), em vez de schema novo (B) ou carimbo em 166 fichas (C).

**Regra (cristalizada em `ferramentas/loader.py`, doc `via_de`/`confianca_de`):**
- `via`: status `em análise` → **P7-conhecimento** (os 166 da linha de auditoria; P7a–j é o conjunto hoje em análise); demais → **P6-evidência**.
- `confianca_fonte`: **alta** = verificado com ≥1 fonte B### (papel impresso); **baixa** = candidato ou em análise; **média** = demais.

**Portadores:** `base/canonico.json` (formato `canonico-1.1`, campos por termo) · validador de schema aceita os enums (opcional p/ retro-compatibilidade) · suite ganhou **T12** (canônico == regra do loader; conjunto P7 == conjunto `em análise`; suporta mudança futura de status sem quebrar) · README vivo mostra a linha `Via/confiança`.

**Números oficiais:** via — P7-conhecimento **166** · P6-evidência **780**; confiança — alta **233** · média **487** · baixa **226** (946 ✓). Round-trip semântico limpo; suite **18 OK**.

**Reversibilidade:** nenhum byte mudado em registro-mestre de DADOS (só docstring), fichas e verbetes — a regra vive em 4 ferramentas; mudar a regra = editar `loader.py` e regenerar. Migração p/ schema próprio (Opção B) pode ser onda futura sem retrabalho curatorial.
