# PAUSA-DESPACHO 2026-09-05 → PROTOCOLO TRILHA LEVE (regime de entrada da caixa)

> Codificação operacional do DESPACHO DE PAUSA E REDIRECIONAMENTO DE ESTEIRA (05/09/2026). Substitui o rito cheio como porta de entrada para documentos derivados; o rito cheio vive agora nos Lotes do MUTIRÃO REVISAR (ver `consolidacoes/F037_mutirao-revisar-lote-1/PLANO-MUTIRAO.md`).

## Regra-mãe

Todo bruto recebido em `uploads_recepcao/` entra pela **Trilha Leve**, salvo auto-escalada. A presunção de trabalho: documento derivado (espelha a base) até que a varredura prove conteúdo genuíno.

## Protocolo Trilha Leve (1 página, 1 despacho, 3 saídas)

1. **Cópia canônica + byte-identidade** (mesma regra de sempre: `consolidacoes/FXXX_*/fonte.txt`, SHA lavrado).
2. **Varredura de derivação** (sem dossiê): (a) taxa de linhas ≥80c verbatim no corpus; (b) taxa de citações ≥8w; (c) numerais sem par; (d) nomes próprios novos (guarda «nome ??» B060).
3. **Relatório de 1 página** atestando o GRAU DE DERIVAÇÃO:
   - **G0 — espelho integral** (≥95% verbatim, 0 nomes novos, 0 numerais novos) → despacho **Aprovo** = arquivar com registro, 0 fichas, e limpar a caixa na cadência acordada;
   - **G1 — derivação com ruído** (verbatim alto mas com numerais/identidades divergentes do corpus) → despacho **Quarentena**: quarentenar as divergências nominais/datadas (nota de quarentena, nunca preenchimento);
   - **G2 — conteúdo inédito ancorável** (trechos sem par no corpus + âncora primária localizável em livro/palestra) → **ESCALA para rito cheio** Família F (dossiê + devolutiva Q… + despacho).
4. **Despacho do curador**: uma linha por caso (Aprovo / Rejeito / Quarentena / Escala). Sem Q-A…F para G0/G1.
5. **Registro de caixa**: limpezas seguem a regra física (cópia byte-idêntica re-conferida imediatamente antes do rm), mas a cadência pode agrupar N aprovações num único Registro (a definir no despacho do caso).

## Primeiro paciente (pronto para despachar)

`LISTA SIMPLES DE TERMOS CHAVE DA RC.txt` — hóspede não-apto da caixa desde o registro nº 13 (nunca teve cópia byte-idêntica versionada). Pré-diagnóstico: se for lista-chave derivada da própria base, é G0/G1 clássico e a Trilha Leve encerra em 1 página + 1 despacho o que o regime antigo adiava indefinidamente.

## O que NÃO muda

Nenhum preenchimento de ficha sem despacho · notas grafam EXATAMENTE a âncora primária · base invariada fora do assinado · espelhos consolidados por ciclo · «nome ??» só com fonte primária.
