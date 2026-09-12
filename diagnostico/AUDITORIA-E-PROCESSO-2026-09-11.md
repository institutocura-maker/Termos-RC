# Auditoria Interna — Frente E: Processo P6/P7 — 11/09/2026

Leitura do histórico git + `chancela/*.csv`. Pergunta: o ritual de chancela funciona? Quanto custa? Onde falha?

## E1. Throughput (10–11/09/2026)

| Fase | Commits de leva | Chancelas 🟢 | Período | Ritmo |
|---|---|---|---|---|
| P6 (baseada em evidência) | 37 | 291 | 10/09 (1 dia) | ~35 levas/dia |
| P7 (por conhecimento) | 10 | 155 | 10–11/09 (2 dias) | ~5 levas/dia |
| **Total** | **47** | **446** | 2 dias | 🟢 22→479 |

P6 foi maratona (chunks pequenos, decisão em bloco por `ask_user`); P7 é ritmo sustentável (1 chunk, template→retorno→aplicação, ~3 turnos por leva). Os dois ritmos funcionam; o limite do P7 é a atenção do Curador, não a engenharia.

## E2. Custo por leva (P7, medido)

- ~22 arquivos alterados/leva (fichas + cadastro + 3 espelhos + CSV);
- ~1 min de rebuild; ~3 interações (template → upload → aplicação);
- Decisões totais nos 10 retornos: **166 V · 1 X (RC-859) · 2 ? (RC-024/769) · 1 linha em branco** (P7-2.5, resíduo de edição — inofensiva, mas o parser deveria rejeitar);
- Travas: **0 violações em 10 levas** (sem-ficha, REVISAR-real e status-fonte nunca dispararam — ou a base está sã, ou as travas são estreitas; C4 sugere o segundo: faltam "sem-fantasma" e "Fontes bemformada").

## E3. Retrabalho: 4 incidentes em 47 levas (~8%), todos recuperados no dia, zero perda de dados

| Incidente | Causa | Cura |
|---|---|---|
| `d0cb5a6` commit vazio (P6c) | Assert falhou após `&&`; commit correu mesmo assim | Rito: separar auditoria de mutação; nunca commitar em cadeia com `&&` |
| Template 5.4 vazio (`40afd50`) | Nome de chunk errado, sem assert de contagem | Rito: `assert n_linhas == esperado` na geração (aplicado desde então) |
| Errata A4 (Frente A) | `t[6]` lido como lista (é string) | Rito: número que não reconcilia não publica + errata lavrada |
| Amnésia `.git` entre turnos (recorrente) | Sandbox ressincroniza a árvore | Rito `fetch + reset --soft + restaurar + add + commit + push` |

Nenhum incidente tocou dados curatoriais — todos foram de ferramental/ritual. O processo é **resiliente, mas manual**: cada cura virou rito oral, não portão automático. Proposta: codificar os 4 ritos no test-suite/Onda 0.

## E4. O ritual sob pressão: 3 salvamentos documentados

1. **P7c**: Curador decidiu na coluna errada (OBS em vez de DECISÃO) → fallback "letra única no OBS vale" incorporado ao protocolo sem bronca, sem perda.
2. **P7i (RC-833)**: "V em todos" em bloco atingiria um termo com exclusão deliberada no P6 → interceptado por pergunta, retenção repetida e lavrada.
3. **P7j (RC-565)**: "V em todos" atingiria grafia sob suspeita expressa → interceptado; o V virou despacho de liberação, lavrado.

Leitura: o modo de falha do P7 não é técnico — é **"V em todos" em bloco varrendo retenções anteriores**. As 3 interceptações foram humanas (atenção do agente). Proposta: **lista HOLD legível-por-máquina** (`chancela/HOLD.csv`: 833, 769, 859, 500, 795 + motivo + desde-quando) — todo retorno com V em código HOLD dispara pergunta automática, mesmo sem memória do agente.

## E5. Diferença não-declarada: P6 × P7 atestam coisas distintas

- P6 = verificação **baseada em evidência** (refs, lastro, auditoria de fonte);
- P7 = verificação **por conhecimento do Curador** (166 termos sem re-auditoria de fonte).

Ambos viram o mesmo selo 🟢. Nada errado — mas a distinção deveria ser **rastreável**: proposta de campo `via` no schema futuro (`P6-evidencia` / `P7-conhecimento`), que alimenta `confianca_fonte` e permite priorizar re-auditoria. Ínterim: os CSVs de retorno já são o rastro (não apagar `chancela/` jamais).

## E6. Gargalos e fricções observados

1. **Upload/download manual** de CSV por leva (GitHub web) — 2 operações manuais do Curador por leva; aceitável no ritmo atual, gargalo se acelerar.
2. **Template por chunk, sob demanda** — gera 1 turno extra por leva ("qual gero?"); alternativa: fila pré-gerada de 2–3 chunks.
3. **Spot audit ~5% unidimensional** (só existência de menção na fonte) — propor rotação de dimensões: existência → verbatim → sanidade de relações → fonte-fantasma.
4. **Sessão paralela** (P7d aplicado por outro chat) funcionou por sorte + protocolo verbal — sem trava técnica contra aplicação dupla. Proposta: lock por arquivo (`chancela/.lock-<chunk>` ou convenção de branch).

## Síntese da Frente E (e dos diagnósticos A→E)

O ritual P6/P7 é **disciplinado, auditável e resiliente** (446 chancelas, 0 perdas, 3 salvamentos) — mas **manual e oral**: ritos vivem na conversa, retenções vivem na memória, travas são estreitas. Recomendação central: **codificar o ritual** (HOLD.csv + 4 portões novos + `via`) antes de acelerar o ritmo. A base aguenta 5 levas/dia para sempre; com o ritual codificado, aguenta qualquer ritmo.

---

*Frente E encerra a fase de diagnósticos (A→E). Consolidar em: Plano de Aprimoramento da KB (ondas 0–3).*
