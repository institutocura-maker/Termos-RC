# Rito de commit — Onda 0.7 (cura o incidente `d0cb5a6`, commit vazio)

Checklist obrigatório antes de cada `git commit` nesta base:

1. **Auditoria separada de mutação** — nunca `python ... && git commit && git push` em cadeia: se o script falhar, o commit correu mesmo assim. Rode, confira a saída, *depois* commite.
2. **Suite verde** — `python3 ferramentas/test_suite.py` com 0 falhas (16 testes, ~7s).
3. **Reancoragem** (amnésia `.git` entre turnos): `fetch` → `reset --soft FETCH_HEAD` → restaurar `.arena/SESSION-NOTES.md` → `add -A` → commit pequeno → push.
4. **1 unidade = 1 commit** (1 leva, 1 item de onda, 1 reparo) — mensagem no padrão (`P7x: …`, `Onda N.M: …`).
5. **Template gerado?** `assert_template_count(caminho, N)` passou (cura `40afd50`).
