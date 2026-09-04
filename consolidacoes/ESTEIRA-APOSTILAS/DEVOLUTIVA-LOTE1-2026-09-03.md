# DEVOLUTIVA — LOTE 1 · Esteira de Consolidação sobre Apostilas Refatoradas (v3.1)

**Data:** 03/09/2026 · **Branch:** `arena/01a06429-termos-rc` · **Fase:** LEVANTAMENTO/AUDITORIA (nada altera a base)

---

## 1. O que foi feito
- Aplicado o fluxo validado no exemplar (fonte.txt → mapeamento → ledger de divergências) às **4 apostilas do Lote 1** (v3.1).
- Estrutura: `consolidacoes/ESTEIRA-APOSTILAS/<slug>/mapeamento.md` + `fonte.txt` por apostila, e ledger consolidado em `DIVERGENCIAS-LOTE1-2026-09-03.md`.

## 2. Principais achados

### A) As 4 apostilas do Lote 1 JÁ estão integradas (auditoria, não mineração)
| Apostila | Conceitos alegados | Existem na base? | Fonte P no cadastro? |
|---|---|---|---|
| 2019-08-25 (Fornos) | RC-836/837 (+ampliações) | ✓ | ✓ |
| 2018-05-20 (Pandora→Eva/Lilith) | RC-813..818 | ✓ | ✓ |
| 2019-04-14 (Javé×Pandora) | RC-819..825 | ✓ | ✓ |
| 2023-12-17 (Lúcifer/Elétrons) | RC-826..833 | ✓ | ✓ |

**Total: 21 códigos + RC-836/837 + 3 ampliações já existentes** — todos citando a fonte P correta.
→ **Nenhum termo novo a criar (decisão G3); nenhuma elevação de status (decisão G1).**

### B) Divergência transversal relevante: V-1 (ficha ↔ cadastro)
O padrão descoberto no exemplar se confirma como risco estrutural: a ficha **RC-828** narra "## Ampliação — P2019-08-25"
e ao mesmo tempo é o código **RC-828** criado a partir de P2023-12-17 — os dois vínculos (P2019-08-25 e P2023-12-17)
estão corretos e no cadastro, mas a coexistência de "ampliações de ficha" não registradas no cadastro (RC-035/499/828
para P2019-08-25) permanece. **Recomendo a decisão Q-V1** (autoridade = cadastro; regularizar ampliações).

### C) Ruído editorial nas apostilas (V-4..V-9) — NÃO propagar
As apostilas v3.1 são produtos de curadoria de IA e trazem **rótulos RC divergentes** dos códigos canônicos da base:
`Zeus RC-149`(→145), `Prometeu RC-270`(→301), `Epimeteu RC-271`(→302), `Shiva RC-148`(→102), `Agar RC-455`(→817),
`Lilith RC-308`(→787/794), `Kvasir RC-378`(→396), `Krishna RC-081`(→414), `Morenu RC-316`(→454), `Aya/Aye RC-369`(→834/835),
`Jesus RC-006`(→072), `elétrons RC-378`(→162), `plasma RC-162`, `antielétron RC-379`, `Genoma RC-330`(→518), `Odin RC-489`.
**Conclusão:** o conteúdo RC (tese) foi absorvido corretamente; a **numeração citada no corpo** das apostilas não é
confiável e **não deve ser usada para relações/remissões** — sempre validar contra `dados_termos.py`.

### D) Quarentenas preservadas
As fichas RC-826..833 já nascem com as quarentenas (científica: elétrons sem vontade; **social** em RC-832 sobre
afetividade/identidade de gênero — leitura possível de transfobia; teológica em RC-831). Nada a acrescentar.

## 3. Propostas (aguardando aprovação)
1. **Aplicação nesta rodada:** NENHUMA alteração na base é necessária nem recomendada para o Lote 1 — os conceitos já
   existem. O valor entregue é a **auditoria confirmatória** + o **ledger**.
2. **Regularização V-1 (se aprovado):** acrescentar `P2019-08-25` à lista de fontes do cadastro de **RC-035, RC-499,
   RC-828** (que já a citam em ampliação de ficha) — restaura consistência ficha↔cadastro. Requer seu aval (Q-V1).
3. **Não propagar** V-4..V-9 (rótulos divergentes das apostilas).
4. **Marcar o Lote 1 como concluído** e, mediante aval, avançar ao **Lote 2** (apostilas de tema central 2023–2026:
   Morus/Arquivos do Destino, Colapso da Trimurti, Buraco Negro Mental, Falência dos Deuses, Prabrajna, Ano 2012).

## 4. Decisões solicitadas ao curador
| # | Pergunta | Opções |
|---|---|---|
| Q-L1-A | Como o Lote 1 está **já integrado** e **sem termos novos**, aprovo marcar a rodada como **auditoria confirmada (sem alteração na base)**? | Sim / não |
| Q-L1-B | Aprovo **regularizar V-1**: acrescentar `P2019-08-25` à fonte do cadastro de RC-035/RC-499/RC-828 (que já a citam em ficha)? | Sim / não / caso a caso |
| Q-L1-C | Confirmo avançar ao **Lote 2** (tema central 2023–2026) na mesma esteira? | Sim / revisar antes |

---

## 5. RESOLUÇÃO DO CURADOR (03/09/2026)
| # | Decisão |
|---|---|
| **Q-L1-A** | **Aprovado.** Lote 1 marcado como **AUDITORIA CONFIRMADA** — conceitos já integrados; nenhuma alteração de conteúdo/status na base decorrente do Lote 1. |
| **Q-L1-B** | **Aprovado.** **V-1 regularizada**: `P2019-08-25` acrescentado à fonte do cadastro de **RC-035, RC-499, RC-828** (que já o citavam em ampliação de ficha) → consistência ficha↔cadastro restaurada. Validador OK (929 termos / 1884 relações). Espelhos regenerados. |
| **Q-L1-C** | **SUSPENSO (pausa estratégica).** O avanço ao Lote 2 foi **pausado a pedido do curador**, para reavaliar a prioridade da esteira de apostilas frente a outros arquivos não processados de maior potencial de consolidação da KB. Ver `AVALIACAO-PRIORIDADE-ESTEIRA-2026-09-03.md`. |
