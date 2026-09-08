# Laboratório de redação — Seção V.24 (Os Tratados)

**Enciclopédia de Referência das Revelações Cósmicas · edição 2026.1** · aberto em 07/09/2026 (F045, passo seguinte)
Destino final: Volume V › Seção 24 — *Ontologia do Perfeito × Imperfeito — os Tratados*

---

## 1. O que é esta seção

A **V.24** é a única seção do índice inteiramente composta de **documentos do Projeto** — não de termos da Base. São os três Tratados: textos de autoria do curador e do agente, escritos como leitura estruturada das palestras e das obras de Jan Val Ellam.

| Endereço | Verbete | Documento-fonte | Natureza |
|---|---|---|---|---|
| **V.24.1** | O Arsenal do Sistematizador | `pedagogico/Apostila-Estudo-Arsenal-do-Sistematizador.md` | o **método** — a governança da Arca |
| **V.24.2** | A Ilha Estacionária e a Arca de Perguntas | `pedagogico/TRATADO-ILHA-ESTACIONARIA-ARCA-DE-PERGUNTAS.md` | a **ontologia** — o Perfeito × o Imperfeito |
| **V.24.3** | O Fim da Justiça Divina e o Início dos Algoritmos | `pedagogico/TRATADO-FIM-DA-JUSTICA-DIVINA-INICIO-DOS-ALGORITMOS.md` | o **sistema** — a cosmologia como engenharia falha |

Os três formam um **tripé** (método · ontologia · sistema), leitura consolidada na 10ª apostila top-down `pedagogico/top-down/Apostila-Estudo-Tratados-Arsenal-Justica-Ilha-Estacionaria.md`.

## 2. Regra de ouro desta seção: **0 códigos**

Nenhum dos três tratados tem entrada no registro-mestre — a Base (946 termos) **não contém** Verbetes para eles, e `termos/` não tem uma única ficha que cite a palavra «Tratado». Consequências práticas, aplicadas nos três verbetes:

- o cabeçalho declara *sem código na Base — seção de redação editorial* em vez de inventar um `RC-NNN`;
- o campo *ficha canônica* é substituído por **documento-fonte** (o caminho do tratado);
- a seção **Tensões** registra explicitamente que a criação de códigos depende de despacho (Navalha de Ockham);
- a **verificação de verbatim** usa o corpus `termos/` **mais** os documentos declarados entre crases no próprio verbete (`ferramentas/verificar_verbetes.py`).

## 3. Estado da redação

| Verbete | Extensão | Situação |
|---|---|---|
| **V.24.1 — O Arsenal do Sistematizador** | 1.428 palavras | ✅ redigido (08/09/2026) |
| **V.24.2 — A Ilha Estacionária** | 1.500 palavras | ✅ redigido (07/09/2026) |
| **V.24.3 — O Fim da Justiça Divina** | 1.496 palavras | ✅ redigido (08/09/2026) |

**Tripé fechado em 08/09/2026** — os três verbetes na faixa homologada (1.300–1.500 palavras), todos com 0 código criado e verificação mecânica em 0 falhas (48 verbatim byte a byte · 48 códigos).

Ordem de redação: V.24.2 (a ontologia, que dá nome à seção) → V.24.3 (o sistema) → V.24.1 (o método).

## 4. ⚠️ Dois títulos citados no despacho que **não constam do acervo**

O despacho de 07/09/2026 menciona o *Tratado de Termópolis* e o *Tratado das Três Espiritualidades*. Levantamento feito no repositório:

- *Termópolis* — ocorre **uma única vez** em todo o acervo, e não como título de tratado: *«Termópolis checara se os critérios dos desdobramentos da Ogdóade»* — translado da aula 01 do curso F044 (`ciclos/F044_misterios-da-vida-de-jesus/translado/01-Adolescência e a Juventude de Jesus.txt`). O mapeamento do F044 registra a linha `| Ogdóade | RC-609 | 2 | critérios de Termópolis |`.
- *Três Espiritualidades* — **zero ocorrências** em qualquer arquivo do repositório.

Não há, portanto, texto-fonte para redigir esses dois verbetes. **Aguardam despacho:** (a) o envio dos documentos, ou (b) a indicação de que são títulos planejados e ainda não escritos — caso em que ficam como seção de redação vazia, como as demais.

## 5. Como conferir

```
python3 ferramentas/verificar_verbetes.py pedagogico/enciclopedia/verbetes-secao-24
```

Dois asserts, sem indulgência: todo trecho entre «» tem de ocorrer byte a byte em `termos/` ou no documento-fonte declarado; todo `RC-NNN` citado tem de existir no registro-mestre.
