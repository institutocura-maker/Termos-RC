# Handoff T1 → T2 — refatoração terminológica

## 1. Estado atualizado da árvore

- **FON-RECEPÇÃO** está estabilizada em rotas canônicas distribuídas: a caixa residual `uploads_recepcao/` conserva apenas `README.md` e `.gitkeep`; os objetos deliberados vivem em `admin/logs/`, `admin/documentos/`, `fontes/docx_originais/`, `fontes/pilotos_historicos/` e `fontes/stt-lote-2026-10/`.
- **FON-APOSTILAS-CONCLUIDAS** está estabilizada em `fontes/apostilas/`, com 82 cápsulas modulares e 1.629 arquivos. A rota antiga `apostilas/CONCLUIDAS/` foi removida após a prova R3 e a limpeza R4 autorizada.

## 2. Diagnóstico técnico — Fase T1 (somente leitura)

- Pasta analisada: `termos/`.
- Fichas Markdown lidas: **826**.
- Frontmatter: **826/826** válidos, sem ausências, sem malformação e sem falta dos campos `codigo`, `nome`, `categoria`, `subcategoria`, `status`, `fontes`, `via`, `confianca_fonte` e `atualizado`.
- Tabelas `Termos Relacionados` padronizadas: **776**, com **7.761** linhas de relação.
- Tipos de relação brutos deduplicados: **998**. A lista bruta ordenada possui SHA-256 `43ad4e8083ce83d5facb39b082488031625d81dd92e827f56938fdafa7d05213`.
- Exceções não conformes: **45** seções chamadas `Termos Relacionados` não usam a tabela padrão; incluem tabelas com `Estado na malha`, tabelas `Código | Relação` e listas Markdown livres.
- Sinais de heterogeneidade: 262 tipos distintos com direção `←`, 151 tipos com qualificadores entre parênteses e 197 tipos livres com espaços; a redução conservadora de direção e qualificador final ainda deixa 627 rótulos distintos.
- Cabeçalhos de citações/ampliações: **877**, todos nível `##`:
  - `## Ampliação`: 603;
  - `## Ampliação — STT26-* (...)`: 174, nos eixos `STT26-EXTRATERRESTRES_TECNOLOGIA`, `STT26-EXPERIENCIA_ESPIRITUAL_ETICA`, `STT26-MITOLOGIAS_REINTEGRACAO` e `STT26-SOCIEDADE_CONTEMPORANEA`;
  - `## Ampliação — OIDR26-01` a `OIDR26-04`: 100;
  - `## Fontes`: 778 ocorrências exatas.
- A T1 não modificou fichas, tabelas, relações ou citações.

## 3. Escopo da próxima sessão — Fase T2

1. Gerar `admin/logs/T2-MAPEAMENTO-RELACOES.csv` a partir dos 998 tipos brutos, com `tipo_bruto` e `ocorrencias` preenchidos e colunas de mapeamento inicialmente em branco: `relacao_controlada`, `direcao_controlada`, `notas_de_normalizacao` e `decisao_curatorial`.
2. Gerar o log de exceções `admin/logs/T2-EXCECOES-RELACOES.md`, discriminando as 45 seções não conformes e sua estrutura atual, sem normalizá-las automaticamente.
3. Definir, por deliberação curatorial, o vocabulário controlado e o De-Para antes de qualquer alteração de ficha.
4. Implementar somente após essa deliberação o novo padrão de tabela de cinco colunas:

   ```text
   Termo | Código | Relação | Direção | Notas
   ```

5. Preservar a semântica, a direção e as anotações históricas; nenhuma normalização textual ou estrutural deve ser executada antes da matriz T2 aprovada.
