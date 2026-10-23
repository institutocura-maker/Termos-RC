# STATUS-HANDOFF — 09/09/2026 (Linha Enciclopédia/verbetes · 10º anel, grau 2)

**Branch da sessão:** `arena/01a085d1-termos-rc` · **HEAD:** `aa22a7c` (Lote 68) · remoto sincronizado (mesmo hash) · árvore limpa · **427 verbetes** em disco · Base intacta.

---

## ⚠️ 0. PRIMEIRO: re-hidratar o git (o ambiente recria o `.git` / clone novo perde histórico)

Os arquivos persistem (snapshot + git), mas os refs/histórico locais podem sumir. Procedimento padrão desta linha:

```bash
cd /home/user/Termos-RC
git fetch origin "+refs/heads/arena/01a085d1-termos-rc:refs/remotes/origin/arena/01a085d1-termos-rc"
git reset --hard refs/remotes/origin/arena/01a085d1-termos-rc
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
git branch --set-upstream-to=origin/arena/01a085d1-termos-rc arena/01a085d1-termos-rc
```

Depois: `git status` limpo · HEAD = remoto = `aa22a7c`. Conferência sempre por `git ls-remote origin refs/heads/arena/01a085d1-termos-rc` (a branch não tem upstream configurado nesta linha — normal; usar `git push origin arena/01a085d1-termos-rc`).

---

## 1. Bootstrap de leitura (nesta ordem)

1. **Este arquivo** (`STATUS-HANDOFF-2026-09-09.md`, raiz, versionado).
2. `pedagogico/enciclopedia/verbetes/README.md` — log completo dos lotes (59→68), fechos de anel, fila. O bloco do Lote 68 está antes do "Fecho do 8º anel".
3. `.arena/SESSION-NOTES.md` — diário da sessão; conferir o último bloco (**Lote 68**).
4. Validação de partida: `python3 ferramentas/dados_termos.py` → **OK: 946 termos, 1898 relações**; e `python3 ferramentas/verificar_verbetes.py pedagogico/enciclopedia/verbetes` → **0 falhas** (hoje: 427 verbetes · 7.743 verbatim · 3.988 códigos). Se divergir, PARE e audite.
5. Modelos de verbete aceitos: `V3/V3.14.03-RC375-druidas-celtas-contexto-rc.md` (materialização) e `V5/V5.22.01-RC287-enigma-da-esperanca-caixa-de-pandora.md` (Lote 67, mesmo volume V.22.1).

---

## 2. MISSÃO VIGENTE (aguardar despacho do Lote 69)

Linha aberta pelo F045-item-3 + ÍNDICE (07–08/09/2026): a Enciclopédia de Referência das Revelações Cósmicas (ed. 2026.1) em `pedagogico/enciclopedia/verbetes/`. O Curador despacha lotes de **6 verbetes de grau 2** (nós com ficha 🟡 provisório em `termos/` e sem verbete ainda), sempre **por ordem decrescente de código** — o agente **não** escolhe a fila. Cada lote é confirmado por mensagem de despacho («Lote NN confirmado >>> [`RC-###`, …]»).

**Rito por lote (fixado nos lotes 59–68):**
1. Ler **integralmente** as 6 fichas em `termos/` (a fonte é a ficha, não o cadastro).
2. Censo/arestas: `ferramentas/dados_termos.py` (grau 2, `ficha=True`) + greps no ÍNDICE (`pedagogico/enciclopedia/INDICE-ENCICLOPEDIA-RC.md`) para endereço e legenda canônica da subseção.
3. Levantar os vizinhos da subseção (ler `head -1` + linha Endereço de cada arquivo da pasta) para anotar divergências de legenda.
4. Redigir os 6 arquivos planos (ver §3 e §4), com **pré-teste byte a byte** das citações antes do verificador.
5. Auto-revisão → verificador oficial (0 falhas) → atualizar README (bloco do lote + fila) e `.arena/SESSION-NOTES.md`.
6. Commit + push na branch da sessão; conferir HEAD × remoto.

---

## 3. Critérios de aceite permanentes (restrições do Curador)

- **Arquivo plano:** `pedagogico/enciclopedia/verbetes/V{n}/V{n}.{ss}.{sub}-RC####-slug.md` (dentro da pasta do volume, ex.: `V2/V2.06.01-RC262-…md`).
- **Cabeçalho-tabela:** código · Endereço **no formato do ÍNDICE** (legenda da subseção + Volume em itálico) · Classificação da Base espelhando a ficha (ex.: CONCEITOS COSMOLÓGICOS › 2.2) · Status 🟡 provisório · Ficha canônica com contagem `wc -w` da ficha.
- **Aviso** «Este verbete não substitui a ficha» com as quarentenas específicas de cada ficha.
- **Seções:** Definição → Desenvolvimento → Tensões e quarentenas → Remissivas. Fecho datado `(lote NN — 10º anel, grau 2)` com «Base de referência: 946 termos · 650 fichas · 1.898 relações — nenhuma alterada por esta redação» + «Para citar».
- **Citações:** somente entre « », **byte a byte contra a ficha** (o verificador exige substring exata no corpus `termos/`); aspas internas preservadas como na ficha (retas ou curvas, sem troca); nada nosso dentro de « »; sem `**` dentro de aspa; sem ponto-final nosso dentro do fecho; sem caminho `.md` entre crases no corpo (só na linha "Ficha canônica").
- **0 códigos novos · 0 relações novas:** Base, `relacoes/`, fichas e cadastro intactos; nenhum verbo de aresta criado/alterado.
- **Sem fusão** entre fontes de uma mesma ficha; **quarentenas rotuladas** (clínica, científica, teológica, de retenção etc.); **STT preservado** como dito.
- **Divergências anotadas, não harmonizadas:** legendas de subseção divergentes (aspas retas `"…"` nossas), status, notas "sem ficha" defasadas — registrar em Tensões e no README, nunca corrigir.
- **Remissivas** com títulos canônicos do cadastro (conferir em `dados_termos.py`), marcando "(sem ficha)"/"(sem aresta)" quando verificado.
- README e SESSION-NOTES sempre atualizados; commit+push conferido.

---

## 4. Estado atual (09/09/2026, pós-Lote 68 = commit `aa22a7c`)

- **Verificados agora:** HEAD == remoto == `aa22a7c`; árvore limpa; verificador **427 verbetes · 7.743 verbatim · 0 falhas**; Base intacta **946 termos · 650 fichas · 1.898 relações**; 0 código criado no lote.
- **Contagens de arquivos:** 427 verbetes (sem README) · 650 fichas em `termos/` · 4 verbetes-modelo · 4 verbetes-secao-24 · ÍNDICE e README presentes; as 6 fichas do Lote 68 em `termos/` confirmadas.
- **Lote 68 entregue (todos 🟡, consistente ficha = cadastro = ÍNDICE):**
  | Verbete | Endereço | Posição | Palavras | Ficha |
  |---|---|---|---|---|
  | Daath (a Criação na Cabala) `RC-262` | II.6.1 | 9º | 954 | 600 p. |
  | Prisioneiros da Brahmaloka `RC-260` | III.12.1 | 12º | 737 | 559 p. |
  | Coreografia Cósmica (vinda de Sophia) `RC-258` | III.11.2 | 7º | 725 | 454 p. |
  | A Humanização do Criador `RC-245` | V.22.1 | 28º | 1.114 | 729 p. |
  | Genética da Confiança `RC-243` | II.8.1 | 28º | 845 | 496 p. |
  | O Mal: Subproduto da Ignorância Espiritual `RC-223` | IV.21.1 | 18º | 770 | 520 p. |
- **10º anel (grau 2): 60 de 76** (lotes 59–68).

---

## 5. Fila (grau 2, 16 restantes, por código decrescente)

`RC-218`, `RC-210`, `RC-196`, `RC-195`, `RC-186`, `RC-155`, `RC-118`, `RC-103`, `RC-093`, `RC-080`, `RC-075`, `RC-056`, `RC-052`, `RC-047`, `RC-035`, `RC-010` — **aguardar o despacho do Lote 69** (próximos 6 a confirmar pelo Curador). Não iniciar nada sem o despacho.

---

## 6. Armadilhas e lições recentes (não repetir)

- **Notas "sem ficha" dentro de fichas antigas podem estar defasadas:** a ficha do `RC-262` anota `RC-190` como sem ficha, mas o censo atual tem ficha — sempre conferir com `ls termos/RC-###-*.md` antes de afirmar.
- **Transcrever citações dos bytes da ficha, nunca de memória:** no rascunho inicial do `RC-243`, B040 foi atribuída à obra errada com citações não conferidas — reescrito contra a ficha (B040 = *Homo Sapiens: da Guerra ao Esporte*) antes do verificador.
- **Legendas dos vizinhos:** ler o arquivo real (H1 + linha Endereço); não confiar em notas de memória (ex.: RC-251 é "Laboratórios do Criador", não "Wyrd/Urd").
- **Contagem oficial de palavras = `wc -w`** (padrão histórico dos lotes).
- **Verificador:** roda sobre `pedagogico/enciclopedia/verbetes` inteiro; READMEs de laboratório ficam fora; arquivos `.md` entre crases no corpo entram no corpus de conferência (por isso nada de caminhos no corpo).
- **HEAD × remoto:** conferir por `git ls-remote` (sem upstream configurado nesta linha).

---

## 7. Arquivos-chave

- `ferramentas/dados_termos.py` — registro-mestre (946 termos; validador).
- `ferramentas/verificar_verbetes.py` — guardião (verbatim byte a byte + códigos).
- `ferramentas/build_indice_enciclopedia.py` — gerador do ÍNDICE.
- `pedagogico/enciclopedia/INDICE-ENCICLOPEDIA-RC.md` — endereços/legendas/status oficiais.
- `pedagogico/enciclopedia/verbetes/README.md` — log dos lotes e fila.
- `pedagogico/enciclopedia/verbetes-modelo/` — os 3 modelos + README de método; `verbetes-secao-24/` — seção de redação editorial.
- `termos/RC-###-….md` — fichas-fonte (650; intocáveis).
- `.arena/SESSION-NOTES.md` — diário da sessão (até o Lote 68).
- `STATE-MIRROR.md` — identidade operacional do repositório (ver §6 anexado em 09/09/2026).
