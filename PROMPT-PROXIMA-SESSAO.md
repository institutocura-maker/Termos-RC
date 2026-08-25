# PROMPT DA PRÓXIMA SESSÃO — Base Terminológica RC

> **Ritual de continuidade.** Este arquivo é o prompt a colar (ou anexar) no chat seguinte.
>
> **Última atualização:** 2026-08-25 · AGENTE 9 · **PAUSA** pedida pelo curador (janela de contexto cheia) · HEAD **`3fa96c1`** · branch `arena/01a02e74-termos-rc`.
>
> **Tarefa da sessão nova:** revisão de continuidade + Workspace × GitHub + artefatos de leitura + mapa do patrimônio da KB. **Não** abrir ciclo de livro até o curador pedir.

---

## Como usar

1. Anexe **este arquivo primeiro** no chat novo.
2. Em seguida, se precisar de fundo: `CHECKPOINT-SESSAO-2026-08-21.md` (histórico; contagens parciais podem estar velhas) → `CONTINUIDADE.md` (diário; cabeçalho prevalece) → `GUIA-MESTRE-RC-APOSTILA-v1.1.md` → `PROMPT-INICIAL-DO-AGENTE.md` (identidade histórica; contagens 767/1531 **velhas**) → `convencoes-editoriais-rc.md`.
3. Diga: *leia `PROMPT-PROXIMA-SESSAO.md`, monte o ambiente e apresente o estado. Esta sessão é de revisão, não de livro.*

**Este arquivo prevalece** para o estado vigente.

---

## PROMPT PARA COLAR NO NOVO CHAT

```
Continue o projeto Base Terminológica RC — as Revelações Cósmicas de Jan Val Ellam. Esta é uma sessão de continuidade após PAUSA (chat anterior estourou contexto). A esteira do AGENTE 9 fechou B022 e parou de propósito.

AUTORIDADE: o curador (Edson Cella Mendes) é a autoridade máxima. Você organiza, cruza, edita e audita. Nunca decida ontologia sem autorização. Conclusões são sempre sugestões.

PRIMEIRA AÇÃO (antes de qualquer edição):
1. O clone já vem na raiz. Branch da sessão: arena/01a02e74-termos-rc. Se HEAD local for só b420f14 (main) e o working tree estiver limpo: git fetch origin arena/01a02e74-termos-rc && git reset --hard FETCH_HEAD. Esperado: 3fa96c1 (ou mais à frente se o curador tiver feito upload).
2. pip install --break-system-packages markdown openpyxl python-docx
3. python3 ferramentas/dados_termos.py → deve retornar exatamente: OK: 777 termos, 1852 relações — dados válidos.
4. Leia PROMPT-PROXIMA-SESSAO.md (este) por inteiro — inclusive as seções Workspace × GitHub e Patrimônio da KB.
5. Resuma estado + o que está velho nos arquivos de continuidade + próximo passo da REVISÃO.
6. Aguarde confirmação. NÃO abrir livro. NÃO abrir PR.

ESTADO CANÔNICO: 777 termos (RC-001–RC-777) · 1.852 relações · próximo RC-778 · 428 fichas físicas (427 ficha=True + RC-004 investigação False) · 86 obras (B001–B083 + ART-2025-08-01/02/03) · 37 apostilas em apostilas/CONCLUIDAS/ · 34 livros em livros/CONCLUIDOS/ · 2 amostras em livros/AMOSTRAS/ (B027, B035) · nenhum ciclo em andamento.

FONTE DA VERDADE: o GitHub (branch da sessão). O Workspace da Arena é sandbox efêmero — o curador trabalha pelo GitHub, não pelo painel de arquivos da Arena.

ARTEFATOS DE LEITURA: base-terminologica.xlsx e base-terminologica-leitura.docx NÃO estão no GitHub (hábito: regeneráveis, não versionar). Gerar com python3 ferramentas/build_xlsx.py e python3 ferramentas/build_word.py. Só commitar se o curador mandar (ele usa o GitHub para baixar).

TAREFA DESTA SESSÃO (revisão, ordem do curador):
A. Mapear e higienizar arquivos de continuidade que estão sobrepostos/desatualizados (PROMPT-PROXIMA, CHECKPOINT, CONTINUIDADE, README, PLANO-MIGRACAO-DE-CHAT, STATUS-RESTAURACAO, PACOTE-MIGRACAO-CHAT). Não apagar história; marcar o que é vigente × arquivo.
B. Decidir com o curador o papel do Workspace da Arena (hoje quase sem uso) versus GitHub.
C. Regenerar xlsx + docx de leitura se o curador quiser tê-los no GitHub para baixar.
D. Confirmar o mapa do patrimônio da KB (seção abaixo) e ajustar se faltar alguma peça.

NÃO começar B074/B075 nem obra completa de B027/B035 até o curador dizer «Em frente».

REGRAS DE OURO: não inventar / [REVISAR] / [TEXTO INCOMPLETO]; plateia e cartas isoladas; Navalha de Ockham (quase sempre zero códigos); nada antes da Devolutiva O-1..O-8; quarentenas (clínica, política, ufológica, teológica, biográfica, institucional); grafias canônicas (Brahma, Tikun, Sophia, Nefilins, Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo, Wyrd/Urd, Kapila, Vaishnavismo, Hochmah, Moros, Malkuth=Hochmah=Sophia, Orlog=Moros, Awayen/Awaylengan/Awaymaion, Morlens, Ginnungagap, Orunmilá, Obatalá, En Ma, Deva/Aurora, Mohen So); jamais editar BIBLIO de build_xlsx.py programaticamente; nunca colar token/PAT.

LIÇÃO DA SESSÃO 8: push ANTES de abrir PR; PR por último e só se o curador pedir.

Comece agora: valide a base, leia este arquivo e apresente o estado da revisão. Aguarde confirmação.
```

---

## Workspace da Arena × GitHub (2026-08-25)

| O quê | Papel real |
|---|---|
| **GitHub** `institutocura-maker/Termos-RC` · branch `arena/01a02e74-termos-rc` | **Fonte da verdade.** O curador sobe PDFs, baixa arquivos, vê o histórico. |
| **`main`** | Ainda em `b420f14` (PR #2, Windows). O trabalho desta esteira **não** está no `main`. |
| **Workspace Arena** | Sandbox do agente. Some com a sessão. Downloads no preview **pausados**. O visor (`ferramentas/visor_workspace.py`) existe, mas o curador não o usa. |
| **Como o curador entrega PDF** | *Add files via upload* no GitHub → `uploads_recepcao/` → o agente faz `fetch`/`pull --ff-only`. Anexos de chat **não** caem em `/home/user/uploads/`. |

Se o Workspace «não tem uso»: está correto. Não investir nele nesta pausa, salvo pedido explícito.

---

## Artefatos de leitura (xlsx / docx)

Não estão no disco nem no Git (por hábito, desde que o versionamento de binários inchou o repo).

```bash
python3 ferramentas/build_xlsx.py    # → base-terminologica.xlsx (7 abas)
python3 ferramentas/build_word.py    # → base-terminologica-leitura.docx
```

`indice-mestre.md` **está** no Git (regenerado a cada ciclo). Apostilas e tratados em DOCX **estão** no Git (`apostilas/CONCLUIDAS/`, `pedagogico/`). Faltam DOCX só de *Javé/Buraco Negro* e *Thot/Hermes*.

Decisão para a sessão nova: o curador quer o xlsx/docx **no GitHub** (para baixar) ou continua só regenerável?

---

## Patrimônio da KB — o que é canônico

Camadas, da mais dura para a mais mole:

### 1. Núcleo (se isto sumir, a Base some)

| Arquivo | O que é |
|---|---|
| `ferramentas/dados_termos.py` | **Fonte única.** 777 termos + 1.852 relações. Validar sempre. |
| `ferramentas/build_xlsx.py` | BIBLIO das 86 obras. **Edição só manual.** |
| `termos/*.md` | 428 fichas (a carne da ontologia). |
| `indice-mestre.md` | Índice gerado; versionado. |

### 2. Governança (sem isto o próximo agente se perde)

| Arquivo | O que é |
|---|---|
| `PROMPT-PROXIMA-SESSAO.md` | **Vigente.** Estado + primeira ação. |
| `convencoes-editoriais-rc.md` | Grafias, quarentenas, Navalha. |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Método (dossiê → Devolutiva → ampliação). |
| `CONTINUIDADE.md` | Diário da jornada (longo; cabeçalho = agora). |
| `CHECKPOINT-SESSAO-2026-08-21.md` | Retomada antiga; útil como história. **Não** usar o procedimento de clone com token. |
| `PROMPT-INICIAL-DO-AGENTE.md` | Identidade histórica (contagens velhas). |

### 3. Acervo trabalhado (a jornada)

| Pasta | Conteúdo |
|---|---|
| `livros/CONCLUIDOS/` | 34 obras integrais com PDF + extract + dossiê + ampliações. |
| `livros/AMOSTRAS/` | B027 e B035 (Sample; obra completa pendente). |
| `apostilas/CONCLUIDAS/` | 37 palestras/lives (original.txt + apostila.md + DOCX). |
| `pedagogico/` | 10 apostilas temáticas + 2 tratados + 2 mapas + Guia TALM + Dossiê Fase 0. |
| `materiais_externos/` | EXT (terceiros; **não** toca ontologia). |
| `uploads_recepcao/` | PDFs que o curador subiu (fonte bruta). |
| `backups/pacotes/` | MANIFESTO + FICHAS + REGENERAÇÃO (seguro versionado). |

### 4. Regenerável / não versionar

`base-terminologica.xlsx` · `base-terminologica-leitura.docx` · `reconstrucao/` · `__pycache__/`

### 5. Arquivos históricos — não confundir com o vigente

`README.md` (contagens 760/1433) · `STATUS-RESTAURACAO.md` · `PLANO-MIGRACAO-DE-CHAT.md` · `PACOTE-MIGRACAO-CHAT-2026-08-18.md`

---

## Ciclos desta esteira (AGENTE 9) — ENCERRADOS

B019 · B011 · B052 · B043 · B013 · B014 · B016 · B044 · B024 · B041 · B036 · B034 · B042 · B048 · B040 · B037 · B049 · B009 · B023 · B001 · B002 · B033 · B017 · B018 · B039 · B003 · B025 · B026 · B015 · B020 · B021 · B005 · B006 · **B022** · amostras B035 e B027 · Carbono.

Trilogias Dramas / Terra Atlantis / Queda e Ascensão: **ENCERRADAS.**

HEAD: **`3fa96c1`** `feat: aplica Devolutiva B022 — 9 fichas, 0 códigos`. PR **não** aberto.

Pendências de livro (quando o curador quiser): B074 *Mentalma I*, B075 *Mentalma II*; obras completas de B027 e B035.

---

## Encerramento de sessão (checklist)

1. Última atualização (data, agente, branch, HEAD).
2. ESTADO CANÔNICO — só se `dados_termos.py` mudou.
3. Pendências de fundo — o curador escolhe a ordem.
4. Bloco *PROMPT PARA COLAR* — a sessão seguinte não depende do chat anterior.
