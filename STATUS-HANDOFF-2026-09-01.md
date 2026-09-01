# STATUS-HANDOFF — 01/09/2026 (vigente)

**Branch:** `arena/01a059e0-termos-rc` · **HEAD:** `f419ec2` (devolutiva P2021-06-26 aplicada) · remoto sincronizado.
Este arquivo **substitui** o `STATUS-HANDOFF-2026-08-31.md` (branch antiga, não vigente).

---

## ⚠️ PRIMEIRO: re-hidratar o git (o ambiente recria o `.git` do zero a cada sessão)

O sandbox re-inicializa o repositório no ponto-base (`58edc7e`, clone de `main` + checkout da branch). **Os arquivos persistem** (snapshot), mas os refs/histórico locais somem. Procedimento (verificado em 01/09/2026):

```bash
cd /home/user/Termos-RC
git fetch origin "+refs/heads/arena/01a059e0-termos-rc:refs/remotes/origin/arena/01a059e0-termos-rc"
# conferir que a árvore de trabalho é idêntica ao remoto (hash a hash; divergência = investigar ANTES):
git ls-tree -r -z refs/remotes/origin/arena/01a059e0-termos-rc | python3 -c "
import sys, hashlib
data = sys.stdin.buffer.read()
tot = fal = div = 0
for rec in data.split(b'\0'):
    if not rec: continue
    tab = rec.index(b'\t'); h = rec[tab-40:tab].decode(); p = rec[tab+1:].decode(); tot += 1
    try:
        raw = open(p,'rb').read()
        wh = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if wh != h: div += 1; print('DIVERGE', p)
    except FileNotFoundError:
        fal += 1; print('FALTANDO', p)
print(f'total={tot} faltando={fal} diverge={div}')"
git reset --hard refs/remotes/origin/arena/01a059e0-termos-rc
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"   # refspec padrão (o clone vem single-branch)
git branch --set-upstream-to=origin/arena/01a059e0-termos-rc arena/01a059e0-termos-rc
# dependências (ambiente novo):
python3 -m pip install --quiet --break-system-packages openpyxl python-docx
```

Após isso: `git status` limpo, HEAD = remoto = `f419ec2`. **Nunca** `git add -A`/commit sem antes fazer o reset acima (senão o estado inteiro vira um commit paralelo em cima do ponto-base).

## Estado da Base

- **886 termos · 1.857 relações · 580 arquivos · 579 `ficha=True`** · 102 obras.
- Espelhos `base-terminologica.xlsx` (7 abas) e `base-terminologica-leitura.docx` **regerados e commitados** (886 termos). Regenerar é **data-idêntico** — só muda timestamp em `docProps/core.xml`/headers zip; **não commitar esse churn** (conferido: se `git status` mostrar só os 2 espelhos como M após regenerar, é timestamp — `git checkout --` neles).
- Fila aberta de materialização (**24 códigos**): RC-857, 861, 862, 864, 866, 867, 868, 869, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, **883 Rara, 884 Bemisia tabaci/Mosca branca, 885 Savant, 886 Campo de Higgs** + 6 ordens órfãs (RC-093, 189, 280, 035, 375, 344).

## Ciclos

- **P2021-06-26 «Shiva - A Reconstrução do Erro de Brahma e o Tikum» — FECHADO** (garimpo `cb22b96` + aplicação `f419ec2`, push OK). 25/25 aprovadas; 19 fichas ampliadas; RC-883..886 na fila aberta `ficha=False`; yoga do sono/sonho absorvida em RC-557+RC-725 (sem código); veto `m****`×5 com 0 vazamentos; Δ 0/4/0/0/23 vs `e95a2ec`. Banner 🔔 no topo do `CONTINUIDADE.md` (devolutiva verbatim).
- **P2022-09-17 «A Hipóstase dos Arcontes» — SUBMETIDO (`fefeeca`), AGUARDANDO DEVOLUTIVA do Curador.** 25 pérolas/18 códigos; 7 candidatos para fila aberta (Maria Madalena, Zou, Jesus o Vivo, Elelev/Eleleth, Pitágoras, Boécio, Nag Hammadi «Naghama»); ampliar 18 fichas; RC-872/RC-063 registrados sem pérola; **operação prato retida**; quarentenas/13 vetos homologados.
- Fechados anteriores (não refazer): P2021-04-10 (`e95a2ec`), P2021-02-28 (`6dcafbc`), P2022-09-18 (`5fb4642`), P2022-07-16 (`a4624d3`), P2026-03-21 (`6633903`).

## Ritos inegociáveis (resumo)

1. GARIMPO → DEVOLUTIVA → APLICAÇÃO em **commits separados**; portões A/B/C/D; selftest 9/9 antes de ciclo; RAG só `aprovada`.
2. **Nenhuma aspa digitada à mão** — sempre `motor.py busca` (recorte byte a byte); vale para pacote, dossiê e ficha; resumo sem aspas angulares.
3. **Máscaras do bruto (`m****` etc.) não transitam em lugar nenhum** — nem a string mascarada literal em glosa (descrever sem citar o padrão). Nunca inventar citações/dados/grafias — marcar `[REVISAR]`.
4. Não harmonizar números (D-9: divergência coexiste com selo datado); preservar `original.txt` byte a byte; DELTA vs baseline do `ciclo.toml`; devolutiva VERBATIM no `CONTINUIDADE.md` (banner 🔔) e no relatório.
5. Grafias canônicas: **Sophia, Brahma, Yel Luzbel/Lúcifer**, Aya/RC-834, Aye/RC-835; STT tem variantes (Brama, Jaavé, Higumig=Higgs, Benésia tabate=Bemisia tabaci…) — verbatim mantém o bruto, glosa usa canônica.
6. Consertar o gerador, nunca o produto; idempotência; config validada é config lida.

## Próximo passo da esteira

- A cada turno: `git fetch` para conferir se o Curador subiu TXT novo (uploads chegam por commit no GitHub; o último upload, `c775764`, era commit vazio — sem TXT). Quando chegar TXT: novo GARIMPO.
- Aguardar devolutiva do **P2022-09-17**.
- Uploads de `uploads_recepcao/` (37 arquivos) já têm ciclo; P2019-08-25 é legado pesado em `apostilas/CONCLUIDAS/` — **não regenerar**.
