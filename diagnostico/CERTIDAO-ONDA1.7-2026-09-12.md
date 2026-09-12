# Certidão — Onda 1.7 · builders no canônico JSON (um por vez, paridade)

**Aceite do plano (1.7):** "3 espelhos idênticos" = cada build, ao trocar o import do registro por `loader.carregar_canonico()`, deve regenerar o espelho **byte-idêntico** ao do modo antigo. Única diferença pré-acordada: a placa de procedência no cabeçalho do artefato (diz a verdade sobre a fonte).

**a) build_indice.py → `indice-mestre.md` — ✅ 12/09/2026 (Agente 25).**
- Paridade: diff = 1 linha (placa "a partir de `base/canonico.json`"); 946 linhas de dados idênticas.
- Pré-chec estrutural: TERMOS e RELACOES reconstruídos do JSON == tuplas do registro (IDÊNTICO nos 946+1887) — inclusive `relacionados` (o `"; ".join` reproduz o byte a byte; '—'/limpezas já tratados no split do exportador).
- Loader ganhou `carregar_canonico()` (única janela JSON; produtores: `exportar_json` continua registro→JSON; `dados_termos.validar` continua porta dos dados).

**b) build_xlsx.py → `base-terminologica.xlsx` — ✅ 12/09/2026 (Agente 25, commit `6246986`).**
- Paridade POR CONTEÚDO (o artefato é zip com timestamps): 0 células diferentes nas 7 abas, dimensões idênticas. Suite 18 OK.

**c) build_word.py + build_readme.py → `base-terminologica-leitura.docx` + `README.md` — ✅ 12/09/2026 (commit `4fe076d`).**
- Docx: `word/document.xml` **byte-idêntico** ao do modo antigo (paridade máxima possível).
- README: diff = exatamente a linha 4 dos pontos de atenção (placa "verdade-mestra" atualizada: builds já leem o canônico). Docstring do `build_word` descravada da era-AST (BIBLIO via `biblio.json` desde 1.3).

**Fecho — ONDA 1.7 CONCLUÍDA (a/b/c, todos com paridade lavrada).** Os três espelhos (índice/xlsx/docx) + README agora fluem `registro → exportar_json → canonico.json → builds`, exatamente como o despacho 1.2 (Opção A) prescreveu; `dados_termos.py` permanece a porta de escrita (validador + suite 18 como guardas). Pendência futura natural (Onda 2+): placas DORMENTE/LEGADO nos atalhos aposentados e guarda "builds ≠ registro ⇒ alarme". **Onda 1 inteira (1.1–1.7) fechada — aguarda a certidão de aceite do Curador (regra do plano: 'cada onda exige chancela antes e certidão ao terminar').**

Rito de cada letra: patch ancorado (dry→apply) → rebuild → diff byte-a-byte → suite 18 OK → commit único → push.
