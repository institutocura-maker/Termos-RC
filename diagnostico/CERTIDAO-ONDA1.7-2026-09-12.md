# Certidão — Onda 1.7 · builders no canônico JSON (um por vez, paridade)

**Aceite do plano (1.7):** "3 espelhos idênticos" = cada build, ao trocar o import do registro por `loader.carregar_canonico()`, deve regenerar o espelho **byte-idêntico** ao do modo antigo. Única diferença pré-acordada: a placa de procedência no cabeçalho do artefato (diz a verdade sobre a fonte).

**a) build_indice.py → `indice-mestre.md` — ✅ 12/09/2026 (Agente 25).**
- Paridade: diff = 1 linha (placa "a partir de `base/canonico.json`"); 946 linhas de dados idênticas.
- Pré-chec estrutural: TERMOS e RELACOES reconstruídos do JSON == tuplas do registro (IDÊNTICO nos 946+1887) — inclusive `relacionados` (o `"; ".join` reproduz o byte a byte; '—'/limpezas já tratados no split do exportador).
- Loader ganhou `carregar_canonico()` (única janela JSON; produtores: `exportar_json` continua registro→JSON; `dados_termos.validar` continua porta dos dados).

**b) build_xlsx.py → `base-terminologica.xlsx` — pendente (próxima unidade).**
**c) build_word.py + build_readme.py → docx-leitura + README vivo — pendentes.**
Após c): placas DORMENTE/LEGADO nos atalhos aposentados (padrão 0.5) e suite ganha guarda "builds ≠ registro ⇒ alarme" se necessário.

Rito de cada letra: patch ancorado (dry→apply) → rebuild → diff byte-a-byte → suite 18 OK → commit único → push.
