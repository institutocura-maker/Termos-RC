# CERTIDÃO — U20 · B061: guilhotina ao Anel A — 2026-09-12

**Despacho:** questão 2 do doc 1.6 (`FANTASMAS-QUESTOES-2026-09-12.md`): a política BIBLIO proibia citar B061 como fonte, mas 67 termos a citavam. Curador escolheu **A — guilhotina ao Anel A** (12/09/2026).

## Execução (mecânica, bifásica dry-run→APPLY)
- **Registro-mestre** (`ferramentas/dados_termos.py`): B061 removida de `fontes` nos **67 termos**; 21 menções históricas fora de `fontes` (comentários/prosa de código) preservadas; asserção global pós-edição: zero B061 em fontes no módulo recarregado.
- **Fichas** (`termos/`): **53** patcheadas — TOML `fontes` sem B061 + `atualizado="2026-09-12"` + **4 linhas de aparato** `| B061 |` ceifadas; **14** termos do censo não têm ficha física (só registro; listados no ledger). Gold verbatim das cartas intocado (G1 preservado — as edições são de metadado e aparatus de fontes); RAG intacto (G2); metadado no TOML (G3).
- **9 candidatos** (RC-477/478/484/485/492/493/495/501/502) tinham B061 como fonte única → `fontes = []` agora; entram na triagem (adjacente à fila A5). Candidatos sem fonte própria não perdem o verbete; a pista B061 fica documentada aqui e no ledger.
- **Rastro:** `diagnostico/B061-GUILHOTINA-67.json` (67 itens, um a um, com ficha/sem ficha/solo); nota de política acrescida na entrada B061 em `base/biblio.json`; dossiê instrutório `B061-RECON-2026-09-12.md` (fecho formal da questão 1: mesma linhagem, chancela 1.3; v3.0 = coleção das 5 apostilas, sem arquivo próprio, P2026-02-28 materializada na U19).
- **Doc 1.6** atualizado: questões 1, 3 e 4 formalmente FECHADAS (3=2.6/F044; 4=U19); questão 2 fechada por esta certidão.

## Pós-verificação
- Suíte completa verde (T8 sem sanções; T13 671; T14 0-divergentes); verificador: "Base intacta: 946 termos · 671 fichas · 1887 relacoes".
- Reconstruções: `base/canonico.json` (946), `indice-mestre.md`, XLSX, DOCX (cartas só com ouro — sem envelope), README. Nenhum outro arquivo mutado (RELACOES 1887 intacto; `notas/` e `relacoes/` blindados).
- Git: esta certidão fecha U20; commit único da unidade.
