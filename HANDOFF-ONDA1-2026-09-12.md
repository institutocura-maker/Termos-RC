# Handoff — retomada Onda 1 em nova sessão (12/09/2026, HEAD `ecdd45a`)

## Para colar como 1ª mensagem da nova sessão
> Branch `arena/01a08907-termos-rc`, HEAD `ecdd45a`. Leia `HANDOFF-ONDA1-2026-09-12.md` (este arquivo) + `STATE-MIRROR.md` §1 + `diagnostico/PLANO-APRIMORAMENTO-KB-2026-09-11.md`. Rode `python3 ferramentas/test_suite.py` (esperado: 17 OK) e confirme leitura. Aguarde ordem.

## Estado (tudo commitado e pushed)
- Onda 0: 7/7 ✅ (suite 17 OK, loader, HOLD.csv, README vivo, legacy/, pacotes tag, ritos).
- Onda 1: 1.2 ✅ despacho JSON · 1.1 ✅ `base/canonico.json` · 1.3+1.6 ✅ `base/biblio.json` + doc fantasmas · **1.4 núcleo ✅** (`c102df6`: hierarquia declarada, 168 reconciliados, 9 dupes → **1889 relações**).
- Base: 946 termos · 671 fichas · **1889 relações** · 102 obras · 60⚪/241🟡/166🟠/479🟢.

## Pendente (retomar aqui)
1. **Detalhe 1.4**: despacho "tipos = rótulo livre" dado pelo Curador — falta executar nos 21 clusters (`diagnostico/CENSO-TIPOS-RELACAO-2026-09-12.md`): fundir flexões óbvias OU manter tudo + declarar. **Perguntar antes de fundir.**
2. **1.5**: campos `via` + `confianca_fonte` (166 termos P7 → `via=P7-conhecimento`).
3. **1.7**: builds lendo o canônico JSON (um por vez, com paridade).

## Ritos inegociáveis (causas de todos os incidentes passados)
- **Amnésia `.git`**: todo turno começa com `fetch` + `reset --soft FETCH_HEAD` + restaurar `.arena/SESSION-NOTES.md`; nunca commitar direto.
- **Libs somem**: `pip install -q --user --break-system-packages openpyxl python-docx` antes de rebuilds.
- **Nunca** `comando && git commit && git push` em cadeia (vide `d0cb5a6`); auditar → conferir → commitar.
- **Nunca** 2 edições paralelas no mesmo arquivo (vide `68d9adf`→`9709567`).
- `ask_user` sempre ≥2 opções. CSVs: `;`, utf-8-sig. 1 unidade = 1 commit + push na MESMA branch.
- Suite verde antes de cada leva/commit de dados. Detalhes: `ferramentas/RITO-COMMIT.md`.

## Verificação (nova sessão roda e reporta)
`python3 ferramentas/test_suite.py` → 17 OK · `git log --oneline -1` → `ecdd45a` · `git status --short` → vazio.
