# Auditoria pós-commit R4 — FON-RECEPÇÃO

**Data:** 24/10/2026
**Commit auditado:** `bfe0cd09fcf9d8330fcbaaa5824db5a047f1941a`
**Método:** extração independente por `git archive HEAD` em diretório temporário, sem usar os arquivos de trabalho da sessão.

## Resultado

- `FON-RECEPCAO`: **330 arquivos**, **10.982.198 bytes**, SHA-256 agregado `a9f253187a50e3a6e31d1e04054739f534592cefb02c1cbf64f753523efe9ccb` — aprovado.
- `FON-LIVROS` com as averbações 1B, 1D e 1E: **577 arquivos**, **100.540.402 bytes**, SHA-256 agregado `df1607e1328788008dc731b6f007d718e73cc5566c61825a24282edc1f3af3ff` — aprovado.
- `python3 ferramentas/test_suite.py`: **23/23** — aprovado.
- `python3 ferramentas/motor.py selftest`: **10/10** — aprovado.
- Conteúdo residual em `uploads_recepcao/`: somente `.gitkeep` e `README.md`.

A auditoria confirma que o estado commitado, não apenas o diretório de trabalho anterior ao commit, preserva os contratos e a limpeza R4.
