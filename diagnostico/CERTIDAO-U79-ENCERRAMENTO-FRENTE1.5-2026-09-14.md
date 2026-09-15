# CERTIDÃO — U79 · ENCERRAMENTO · FRENTE 1.5
## Normalização atómica TAB → ESPAÇO na B049 e reemissão da RC‑372

**Data:** 14/09/2026 · **Despacho:** U79 — «Segregação de Escopo (Operação Atómica)»
**Executor:** motor (Arena Agent Mode) · **Suíte:** 21/21 · **EXIT=0** · verificação dupla de HEAD

---

## 0. Antes de começar: a 4.ª regressão do git, contida pelo duplo cinturão

A checagem de **abertura** acusou divergência:

```
HEAD local : 0a640cf        (o commit BASE da branch — U40)
remoto     : 57da368        (U78)
igual      : NÃO — ABORTAR
pendentes  : 242
```

**A operação foi abortada antes de qualquer escrita.** Diagnóstico:

- O **disco estava íntegro** — 820 fichas presentes, cadastro no ponto da U77 (RC‑931 com `True`), nenhum conteúdo perdido.
- Quem regrediu foi a **ref do git**: `refs/heads/arena/01a09ca0-termos-rc` apontava para `0a640cf`, o commit de onde a branch partiu.
- O remoto tinha o trabalho: `FETCH_HEAD` = `57da368`, e o objecto existia no *object store* (`git cat-file -t 57da368` → `commit`).

Aplicada a receita das U48/U61/U67: salvaguarda de 826 ficheiros em `/tmp`, `git reset --mixed FETCH_HEAD` (**nunca `--hard`**), e restauro de `.arena/SESSION-NOTES.md` pelo HEAD — que reaparecera trocado pelo ficheiro de **outra branch** (`arena/01a071c8-termos-rc`, de 10/09). Verificação final: `HEAD == remoto`, **0 pendentes**, 820 fichas, blocos U75–U78 presentes no espelho.

É a **quarta** ocorrência (U48, U61, U67, U79). O duplo cinturão da U68 conteve-a sem dano.

## 1. O raio de acção, medido antes de disparar

**Prova de que a normalização só podia afectar uma ficha:** as 767 citações da Base foram varridas por obra. **A B049 é citada por exactamente uma ficha — a RC‑372, nos seus 10 fragmentos.** As outras 10 fichas que mencionam «B049» apenas a *declaram* no campo `fontes` (matéria da Frente 2); nenhuma a cita.

## 2. A regra, e por que é segura

Três passos, todos **só sobre artefatos provados**:

1. `'\t'` → `' '`
2. colapsar runs de 2+ espaços → 1 espaço
3. podar espaços nas pontas da linha

**Prova do passo 2:** o ficheiro continha **0 (zero)** linhas com 2+ espaços seguidos antes da troca. Logo, qualquer run de 2+ espaços após ela **só pode provir de um TAB** — colapsar não destrói nada pré-existente.

## 3. O resultado

| | Antes | Depois |
|---|---:|---:|
| TABs (U+0009) | **70 994** | **0** |
| Linhas com TAB | 7 886 | 0 |
| Linhas com 2+ espaços | 0 | 0 |
| Linhas com espaço nas pontas | 707 | 0 |
| **Linhas (contagem total)** | **8 959** | **8 959** |

A **contagem de linhas foi preservada** — condição essencial, pois todas as citações da Base referenciam `original.txt L<n>`.

```
sha256 antes : 9e647924758f0b49ae3679c7bf1da0f6161e91b20dc5805bda64f8952adee750
sha256 depois: bf76ac9facbbb22d5d0ad837e4f7b38f4298ff5f66e8b8600ea1889b68e5c2c4
```

Exemplo — L65: `'O\tSer\tHumano\tEmancipado'` → `'O Ser Humano Emancipado'`.

## 4. ⚠️ O segundo artefato — encontrado, registrado e **NÃO** tocado

A extracção digital da B049 também inseriu **espaços DENTRO de palavras**. O caso mais claro é o próprio título de uma secção:

```
L106 (depois da normalização):  'Reflex ão Neces s á ria'
```

Isto é, «Reflexão Necessária». **Não foi corrigido**, por duas razões: não constava do despacho, e saná-lo exigiria confronto com o impresso — não é substituição mecânica de um carácter, é decisão sobre onde o espaço pertence. Fica registrado para frente própria.

## 5. Reemissão da RC‑372 pelo Portão B

As **10 citações** foram reextraídas do ficheiro normalizado, reconferidas byte a byte e reemitidas (`--sobrescrever`):

```
RC-372: 10 fragmento(s) conferidos
~ RC-372-ser-humano-emancipado.md: REGERADO
```

A ficha passou de 8 491 B para 8 774 B e contém **0 TABs**. As notas do lote 32 foram reescritas para contar a história inteira — achado (U75), recusa do Portão B, homologação (U76), execução atómica (U79) —, e **corrigiu-se uma afirmação obsoleta** da U75 que dizia «a ficha cita a forma impressa», o que a recusa do Portão desmentira no mesmo dia.

## 6. Verificação

```
suíte 21/21 EXIT=0 (T13 820 · T14 0 · T15 820/0)
verificador: OK — todo verbatim confere byte a byte (767 citações, 33 obras)
             Base intacta: 946 · 820 fichas · 1887 relacoes
docx: 0 TABs no bloco da RC-372; «Este é o ser humano emancipado, livre, aquele
      que pensa» presente; o encerramento do artefato está registrado no corpo
```

Os espelhos `.xlsx`/`.docx` foram reconstruídos porque incorporam o texto da ficha. O sandbox perdeu `openpyxl`/`python-docx` pela **4.ª vez** (instalados em `.local`, fora dos *snapshots*); reinstalados.

## 7. Estado das frentes

| Frente | Estado |
|---|---|
| 1 — Espelhos .xlsx/.docx | ✅ U78 |
| **1.5 — Normalização atómica da B049** | ✅ **U79 (esta)** |
| 2 — Higienização substitutiva de `fontes` | ⏳ aguardando |
| 3 — Certidão Final da Campanha R1 | ⏳ aguardando |

O delta do turno: `original.txt` da B049 (7 886 linhas), a ficha RC‑372, o lote 32, os índices e os dois binários. **Nenhum outro dado tocado.**

---

*Lavrada sob o rito: 1 unidade = 1 commit + push na branch da sessão, sem `--amend`; verificação dupla de HEAD (abertura e encerramento).*
