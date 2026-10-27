# Diagnóstico — falha T14 e regeneração de espelhos (27/10/2026)

**Natureza:** registro de dívida estrutural conhecida + certidão da regeneração da cadeia de espelhos.
**Despacho do Curador:** cadeia completa autorizada; falha T14 **apenas reportada, não corrigida**.
**Commit de partida:** `ccc443e` (mapa de dados). Nenhuma ficha, fonte, relação ou registro-mestre foi alterado.

---

## 1. O achado

Ao censar o repositório para `docs/MAPA-DADOS-DA-BASE-RC.md` (26/10/2026), constatou-se que os espelhos de estado divergiam da realidade:

| Artefato | Dizia | Real |
|---|---|---|
| `README.md` (gerado 23/10/2026) | 946 termos · **820 fichas** · 1887 relações · 104 obras | 946 · **826** · 1887 · 104 |
| `admin/logs/STATE-MIRROR.md` (manual) | 946 · **689 fichas** · 1887 · **102 obras** | 946 · **826** · 1887 · **104** |
| `base/canonico.json` | **820** `ficha=true` | **826** |
| `termos/*.md` no disco | — | **826 arquivos** |

### Causa raiz

`base/canonico.json` é espelho de `ferramentas/dados_termos.py` via `ferramentas/exportar_json.py`.
Estava desatualizado desde 24/10/2026:

- **6 códigos** com `ficha` `False → True`: `RC-054`, `RC-199`, `RC-254`, `RC-306`, `RC-839`, `RC-874` (arquivos presentes no disco, status `provisório`/`candidato` no mestre).
- **274 adições** de siglas de fonte, **0 remoções**:
  `STT26-SOCIEDADE_CONTEMPORANEA` (54), `STT26-EXPERIENCIA_ESPIRITUAL_ETICA` (53),
  `STT26-MITOLOGIAS_REINTEGRACAO` (45), `OIDR26-01..04` (25 cada),
  `STT26-EXTRATERRESTRES_TECNOLOGIA` (22).

Como `build_readme.py`, `build_xlsx.py`, `build_word.py` e `build_indice.py` leem
`loader.carregar_canonico()`, **todos os espelhos herdavam o número errado**. Rodar apenas
`build_readme.py` teria reproduzido 820 fichas.

---

## 2. Cadeia executada

Ordem respeitada: `build_readme.py` antes de `build_word.py` (a PARTE 6 do DOCX consome a seção
`## ⚠️ Pontos de atenção` do README por regex — restrição B-errata-1).

| # | Comando | Saída |
|---|---|---|
| 1 | `python3 ferramentas/exportar_json.py` | `base/canonico.json` — 946 termos, **826 fichas**, 1887 relações; round-trip semântico limpo; `meta` e relações idênticos |
| 2 | edição manual | `admin/logs/STATE-MIRROR.md` — identidade, números, fase + nova §8 |
| 3 | `python3 ferramentas/build_readme.py` | `README.md` — 946/826/1887/104 |
| 4 | `python3 ferramentas/build_indice.py` | `indice-mestre.md` — 946 linhas, **826 links de ficha** |
| 5 | `python3 ferramentas/build_xlsx.py` | `base-terminologica.xlsx` — 7 abas, aba `Fichas` 821 → **827** linhas |
| 6 | `python3 ferramentas/build_word.py` | `base-terminologica-leitura.docx` — 826 fichas disponíveis/marcadas |

`base/biblio.json` (104 obras) e `INVENTARIO-APOSTILAS.json` (81) já estavam corretos — intocados.

**Nota de ambiente:** `openpyxl` e `python-docx` precisaram ser instalados
(`pip install --user --break-system-packages`) duas vezes, pois o sandbox recria o site-packages
do usuário entre chamadas. Versão usada: `openpyxl 3.1.5`.

### Preservação do histórico no STATE-MIRROR

A linha 9 (`- Base: ...`) continha 9.196 caracteres, dos quais 4.858 eram a narrativa de fase
historicamente acumulada (levas P6/P7/U25–U47). A edição:

- substituiu apenas o trecho `**946 termos · 689 fichas · 1887 relações · 102 obras**` pelos números reais;
- antepôs uma fase concisa e atual (426 caracteres) — é esse trecho que `build_readme.py` captura;
- **preservou integralmente os 9.132 caracteres do parêntese histórico**, reposicionados sob o rótulo `[Histórico de levas — arquivo integral]`;
- preservou integralmente as 119.350 caracteres das linhas 10–82 (seções 1 a 7);
- acrescentou a §8 com 38 linhas de registro.

Verificação: `parêntese histórico ⊂ nova linha 9` e `bloco linhas 10–82 ⊂ novo arquivo` — ambos `True`.

---

## 3. A falha T14 (reportada, não corrigida)

`python3 ferramentas/test_suite.py` → **23 testes, 1 falha**.

```
FAIL: test_T14_tabelas_relacionados
AssertionError: ['RC-001', 'RC-002', ...] != []
[T13] 826 fichas com frontmatter (2.1 piloto + expansão)
[T14] tabelas == cadastro (M3) · divergentes: 821
[T15] motor.fm_toml == frontmatter das fichas · 826 conferidas · divergentes: 0
```

**A falha é pré-existente a esta regeneração** — confirmada por execução da suíte antes de qualquer
alteração (baseline idêntico: 23 testes, 1 falha, 821 divergentes).

**Mecanismo:** `test_T14_tabelas_relacionados` procura a seção com
`re.search(r"(?ms)^## Termos Relacionados\n(.*?)(?=^## |\Z)", carta)`. A **Onda 2** rebaixou essa
seção para `### Termos Relacionados`, dentro de `## 1. Gênese e Definição`. O regex não casa,
`have` fica vazio e todas as fichas que têm relacionados no cadastro são acusadas como divergentes.

**Por que não corrigir agora:** ajustar o regex para aceitar `###` faria o teste passar a comparar
o conteúdo real das tabelas de 5 colunas com o cadastro `t[6] ∪ RELACOES`. Isso pode revelar
divergências reais de conteúdo (a T2 consolidou 998 tipos e a Onda 2 moveu a tabela de posição),
abrindo uma frente de curadoria nova que exige despacho específico. Registra-se a dívida para
rodada própria.

---

## 4. Validação final

| Verificação | Resultado |
|---|---|
| Arquivos alterados | **6**, exatamente o conjunto esperado |
| `termos/`, `fontes/`, `ferramentas/dados_termos.py` com diff | **0 / 0 / 0** |
| Suíte antes × depois | 23 testes / 1 falha **×** 23 testes / 1 falha — **0 regressões** |
| `verificar_verbetes.py` | 118 verbatim · 48 códigos · **0 falhas** · "946 termos · 826 fichas · 1887 relacoes" |
| `dados_termos.py` self-test | `OK: 946 termos, 1887 relações — dados válidos` |
| `exportar_json.roundtrip_check` | limpo |
| Números em todos os espelhos | **946 · 826 · 1887 · 104** |

**Estado congelado:** 946 termos · 826 fichas · 1887 relações · 104 obras ·
status 572 🟢 / 212 🟡 / 102 🟠 / 60 ⚪. Matriz T2 inalterada (998 `APROVADO`, soma 7.761).
