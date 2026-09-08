# Expansão da Enciclopédia — os verbetes por volume

**Enciclopédia de Referência das Revelações Cósmicas · edição 2026.1** · laboratório aberto em 08/09/2026

Sumário analítico: `../INDICE-ENCICLOPEDIA-RC.md` (650 fichas mapeadas, 0 pendências).
Forma fixada em `../verbetes-modelo/` (3 modelos homologados) e `../verbetes-secao-24/` (3 tratados).

---

## 1. Despacho vigente (08/09/2026)

| Decisão | Escolha homologada |
|---|---|
| **Critério de prioridade** | **nós-hub primeiro** — os 35 nós com grau ≥ 10 em `RELACOES`, em lotes de ~6 |
| **Camadas** | **três** (abaixo) |
| **Destino** | `verbetes/V<N>/`, arquivo = endereço + slug |
| **Lote 1** | 6 verbetes — um por volume + o maior hub + o 2º mais central |

## 2. As três camadas

| Camada | Faixa | Destinatárias | Critério |
|---|---|---|---|
| **Verbete-Pilar** | 1.300–1.500 palavras | ~40–60 entradas | macroconceitos; nós-hub; âncoras de seção |
| **Verbete-Médio** | 600–900 palavras | ~250 entradas | fichas com lastro médio (ampliação + citação) |
| **Verbete-Notícia** | 150–300 palavras | ~340 entradas | fichas de lastro curto e termos de passagem |

Escala: ~350 mil palavras. A alternativa — tudo-Pilar — daria ~900 mil e inviabilizaria a obra.

**Critério objetivo de camada:** o *lastro* da ficha (palavras · fontes · citações) e a *centralidade* do nó (grau em `RELACOES`). Ficha curta não sustenta Pilar; nó-hub não cabe em Notícia. Onde os dois critérios divergem, registra-se a divergência na seção **Tensões** do verbete.

## 3. O que todo verbete tem de ter

1. **Cabeçalho** — código · endereço `V.SEÇÃO.SUBSEÇÃO` · classificação da Base (área › subárea) · status · caminho da ficha canônica;
2. **Aviso** de que o verbete não substitui a ficha (a ficha é a fonte de verdade);
3. **Definição** (100–150 palavras);
4. **Desenvolvimento** em 3–5 movimentos;
5. **«Na voz do autor»** — verbatim + fonte, conferido byte a byte;
6. **«Tensões»** — com os selos de quarentena (clínica · científica · teológica · mediúnica · política · ufológica) e as divergências registradas, não arbitradas;
7. **Remissivas** por código;
8. **Fecho** com edição, censo da Base e modelo de citação.

**Regras que não se negociam:** nenhuma aspa composta à mão · nenhum código criado · nenhuma harmonização forçada de divergência · a Base não é alterada pela redação.

## 4. Lotes

| Lote | Data | Verbetes | Estado |
|---|---|---|---|
| **1** | 08/09/2026 | `V1/RC-706` Bhavaṅga · `V2/RC-658` Wyrd · `V3/RC-009` Sophia · `V3/RC-454` Elm · `V4/RC-692` Kit de Elétrons · `V5/RC-708` Ser Humano Não Local | ✅ redigido |

**Lote 1 — medida final:** 1.086–1.391 palavras · **141 verbatim byte a byte · 75 códigos · 0 falhas** · 0 código criado · Base intacta (946/650/1898).

| Verbete | Endereço | Palavras | Camada efetiva |
|---|---|---|---|
| Bhavaṅga / Janela da Percepção | I.3.1 | 1.086 | Pilar de lastro curto (ficha 434 p., 1 fonte) |
| Wyrd / Urd | II.8.1 | 1.391 | Pilar |
| Sophia | III.11.2 | 1.303 | Pilar |
| Elm (Moros) | III.13.5 | 1.390 | Pilar |
| Kit Reencarnatório de Elétrons | IV.19.2 | 1.154 | Pilar de lastro curto (ficha 711 p.) |
| Ser Humano Não Local | V.22.1 | 1.112 | Pilar de lastro curto (ficha 528 p.) |

**Achado editorial do lote 1:** em 3 dos 6 nós-hub, a **centralidade** (grau) e o **lastro** (tamanho da ficha) divergem — o nó é central porque as remissivas convergem nele, não porque haja documento abundante. Nesses casos o verbete fica no tamanho que a fonte sustenta, e a divergência é registrada na seção Tensões em vez de ser resolvida com paráfrase.
| 2 | — | próximos 6 nós-hub (RC-696 · RC-072 Jesus · RC-604 Fatiamento · RC-690 · RC-694 · RC-664) | ⏳ aguardando |

**Nós-hub restantes após o lote 1 (grau ≥ 10, 29 de 35):** RC-696 · RC-072 · RC-604 · RC-690 · RC-694 · RC-664 · RC-717 · RC-081 · RC-414 · RC-700 · RC-704 · RC-720 · RC-761 · RC-395 · RC-474 · RC-655 · RC-697 · RC-698 · RC-709 · RC-092 · RC-476 · RC-693 · RC-699 · RC-703 · RC-705 · RC-710 · RC-718 · RC-721 · RC-736.

## 5. Como conferir

```
python3 ferramentas/verificar_verbetes.py pedagogico/enciclopedia/verbetes
```

Varredura recursiva: todo trecho entre «» tem de ocorrer byte a byte em `termos/` (ou no documento-fonte declarado, para verbetes de redação); todo `RC-NNN` citado tem de existir no registro-mestre. Censo de código = `ferramentas/dados_termos.py`, nunca `ls termos/`.
