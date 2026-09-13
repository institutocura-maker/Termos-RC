# Certidão U27 — leva P7k aplicada: P7-4.4-fenomenos (13/09/2026)

Curador devolveu a proposta com **V nos 27 termos**. Execução:
1. **Entrada** — `uploads_recepcao/P7-4.4-fenomenos_retorno.csv` canonizada byte a byte em
   `chancela/P7-4.4-fenomenos_retorno.csv` (SHA `48ab5052d188…`), caixa expurgada,
   **REGISTRO-LIMPEZA nº 24** em `backups/`.
2. **Higiene** — parser da casa (parse_decisao + validate_retorno_rows + flag_hold, portão 0.3):
   27 linhas, 27 V, zero HOLD, zero código fora do cadastro, zero ficha ausente.
3. **Aplicação** — `dados_termos.py`: 27× `em análise` → `verificado` (âncora por linha do termo,
   assert de unicidade). Fichas: só o frontmatter, regerado pelo **molde `fm_toml` do motor**
   (paridade T15; `via`/`confianca_fonte` derivados pela regra do loader). Corpo de todas intacto
   (zero reescrita de prosa); `RELACOES` intocado.
4. **Contas** — status da base agora: 60⚪·241🟡·138🟠·507🟢. Base 946·671·1887·102; verificador ok; builds
   regenerados; suíte sola 21/21.

Fila do tema 4.4: restam 15 candidatos (nova proposta gerada na sequência — U28).
Nota de rito: o commit principal levou os dados; esta certidão e o ledger saíram em adendo
porque um script de documentação com truque json quebrado antecedeu a lavragem — sem --amend.
