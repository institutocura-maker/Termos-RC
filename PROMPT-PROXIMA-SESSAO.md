# PROMPT DA PRÓXIMA SESSÃO — Base Terminológica RC

> **Ritual de continuidade.** Este arquivo é o prompt a colar (ou anexar) no chat seguinte.
>
> **Última atualização:** 2026-08-25 · AGENTE 10 · **REVISÃO DE CONTINUIDADE FECHADA** (tarefas A/B/C/D) + **CICLO B074 *Mentalma I* FECHADO** (Devolutiva O-1..O-8 aplicada; 0 códigos; B084 cadastrada) · HEAD **`66b01e1`** (handoff; + commits da esteira 10) · branch `arena/01a03913-termos-rc`.
>
> **Tarefa da sessão nova:** retomar o repasse dos livros — **próximo: B075 *Mentalma II*** (PDF já em `uploads_recepcao/`); depois B076–B078 (sem PDF — quando o curador tiver) e obras completas B027 e B035. **A ordem é do curador.** Não abrir ciclo sem a obra nomeada.

---

## Como usar

1. Anexe **este arquivo primeiro** no chat novo.
2. Em seguida, se precisar de fundo: `CONTINUIDADE.md` (diário; cabeçalho prevalece) → `convencoes-editoriais-rc.md` → `GUIA-MESTRE-RC-APOSTILA-v1.1.md` → arquivos HISTÓRICOS (com banner ⚠️; só como história): `CHECKPOINT-SESSAO-2026-08-21.md` · `PROMPT-INICIAL-DO-AGENTE.md` · `README.md` · `PLANO-MIGRACAO-DE-CHAT.md` · `PACOTE-MIGRACAO-CHAT-2026-08-18.md`.
3. Diga: *leia `PROMPT-PROXIMA-SESSAO.md`, monte o ambiente e apresente o estado.*

**Este arquivo prevalece** para o estado vigente (ver tabela "Mapa da vigência").

---

## PROMPT PARA COLAR NO NOVO CHAT

```
Continue o projeto Base Terminológica RC — as Revelações Cósmicas de Jan Val Ellam. Esta é uma sessão de continuidade. A esteira 9 fechou B022 e parou de propósito; a esteira 10 fechou a revisão de continuidade (vigência, Workspace, xlsx/docx, mapa da KB), recebeu os DOCX Javé e Thot/Hermes (coleção pedagico/ completa) e **fechou o ciclo B074 *Mentalma I*** (Devolutiva aplicada: 5 fichas ampliadas + 2 criadas; 0 códigos; B084 *O Legado Esquecido* cadastrada). Aguardando a ordem do repasse de livros.

AUTORIDADE: o curador (Edson Cella Mendes) é a autoridade máxima. Você organiza, cruza, edita e audita. Nunca decida ontologia sem autorização. Conclusões são sempre sugestões.

PRIMEIRA AÇÃO (antes de qualquer edição):
1. O clone já vem na raiz (main, b420f14). O trabalho da esteira está na branch arena/01a03913-termos-rc. Se HEAD local for só b420f14 (main) e o working tree estiver limpo: git fetch origin arena/01a03913-termos-rc && git reset --hard FETCH_HEAD. Esperado: 66b01e1 (ou mais à frente, se o curador tiver feito upload em outra branch da esteira — ex.: arena/01a02e74 — nesse caso cherry-pick/merge antes de editar).
2. SE O WORKSPACE PARECER ANTIGO (ex.: sem livros/CONCLUIDOS/, ou HEAD em b420f14 depois de já ter trabalhado): o sandbox revertia o workspace — refaça fetch + reset ANTES de editar. O store durável é a branch no GitHub; commit + push ao fim de cada turno.
3. pip install --break-system-packages markdown openpyxl python-docx pypdf
4. python3 ferramentas/dados_termos.py → deve retornar exatamente: OK: 777 termos, 1852 relações — dados válidos.
5. Leia PROMPT-PROXIMA-SESSAO.md (este) por inteiro — inclusive as seções Workspace × GitHub e Patrimônio da KB.
6. Resuma o estado e aguarde confirmação do curador. NÃO abrir PR.

ESTADO CANÔNICO: 777 termos (RC-001–RC-777) · 1.852 relações · próximo RC-778 · 430 fichas físicas (429 ficha=True + RC-004 investigação False) · 87 obras (B001–B084 + ART-2025-08-01/02/03) · 37 apostilas em apostilas/CONCLUIDAS/ · 35 livros em livros/CONCLUIDOS/ · 2 amostras em livros/AMOSTRAS/ (B027, B035) · nenhum ciclo em andamento.

FONTE DA VERDADE: o GitHub (branch da sessão). O Workspace da Arena é sandbox efêmero — o curador trabalha pelo GitHub, não pelo painel de arquivos da Arena. (Decisão do curador, 2026-08-25: **sem investimento** no Workspace.)

ARTEFATOS DE LEITURA: base-terminologica.xlsx e base-terminologica-leitura.docx **estão no GitHub** (decisão do curador, 2026-08-25: cópia para download). Regenerar sempre com python3 ferramentas/build_xlsx.py e python3 ferramentas/build_word.py antes de qualquer commit que mude a base (são espelho; a fonte é dados_termos.py + Markdown).

TAREFA DESTA SESSÃO: retomar o repasse dos livros, na ordem do curador — **B074 *Mentalma I* já FECHADO na esteira 10** (Devolutiva aplicada; 0 códigos; B084 cadastrada); pendências: **B075 *Mentalma II*** (PDF já em `uploads_recepcao/`) · B076–B078 (sem PDF) · obras completas de B027 e B035. Não começar nada sem a obra nomeada.

MÉTODO DO CICLO DE LIVRO (padrão B019..B022, B074): PDF em `livros/B0NN_slug/` (original.pdf + original.txt paginado, SHA-256) + `ficha_ingresso.md` + `analise/` (camadas 0–3, LEITURA-1, DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md com O-1..O-8) → **AGUARDA DEVOLUTIVA** (0 códigos) → [aprovada] ampliações via `analise/_ampliacoes_B0NN.txt` + `_aplicar_ampliacoes_B0NN.py` (seção `## Ampliação — B0NN` antes de `## Fontes`) → validar → artefatos (índice, xlsx, docx) → `DECISAO-DO-CURADOR.md` + `RELATORIO-DE-CICLO.md` → mover para `livros/CONCLUIDOS/` → atualizar CONTINUIDADE + `livros/README.md` + PROMPT-PROXIMA → push.

REGRAS DE OURO: não inventar / [REVISAR] / [TEXTO INCOMPLETO]; plateia e cartas isoladas; Navalha de Ockham (quase sempre zero códigos — B074: veto absoluto); nada antes da Devolutiva O-1..O-8; quarentenas (clínica, política, ufológica, teológica, biográfica, institucional — p. 215 de B074: Hitler/biodemos BANIDO da malha); grafias canônicas (Brahma, Tikun, Sophia, Nefilins [no B074: "Nephelim"], Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo, Wyrd/Urd, Kapila, Vaishnavismo, Hochmah, Moros, Malkuth=Hochmah=Sophia, Orlog=Moros, Awayen/Awaylengan/Awaymaion, Morlens, Ginnungagap, Orunmilá, Obatalá, En Ma, Deva/Aurora, Mohen So); jamais editar BIBLIO de build_xlsx.py programaticamente; nunca colar token/PAT.

LIÇÃO DA SESSÃO 8: push ANTES de abrir PR; PR por último e só se o curador pedir.
LIÇÃO DA SESSÃO 10: o workspace Arena reverteu entre turnos sem aviso — o único store durável é o push na branch; re-fetch/re-reset se o tree parecer antigo; commit + push ao fim de cada turno. O curador pode subir arquivos em QUALQUER branch da esteira (viu: subiu em arena/01a02e74) — conferir as branches antes de editar.

Comece agora: valide a base, leia este arquivo e apresente o estado. Aguarde confirmação.
```

---

## Mapa da vigência dos arquivos de continuidade (2026-08-25 — revisão AGENTE 10)

| Arquivo | Papel | Estado |
|---|---|---|
| `PROMPT-PROXIMA-SESSAO.md` | Estado vigente + primeira ação | **VIGENTE** |
| `convencoes-editoriais-rc.md` | Grafias, quarentenas, Navalha | **VIGENTE** |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Método (dossiê → Devolutiva → ampliação) | **VIGENTE** |
| `01-ficha-modelo.md` | Ficha Padrão v2 + guia de preenchimento | **VIGENTE** |
| `02-vocabulario-controlado.md` | Vocabulário controlado (mesmos nomes para a mesma coisa) | **VIGENTE** |
| `CONTINUIDADE.md` | Diário da jornada (cabeçalho = agora) | **VIGENTE** (diário) |
| `INDICE-PALESTRAS.md` | Índice de palestras (estado reconstruído) | **VIGENTE** (índice vivo) |
| `CHECKPOINT-SESSAO-2026-08-21.md` | Retomada antiga | HISTÓRICO (banner; sem procedimento com token) |
| `README.md` | Reconstrução de 2026-08-14 (contagens 760/1.433) | HISTÓRICO (banner) |
| `STATUS-RESTAURACAO.md` | Restauração de 2026-08-19 | HISTÓRICO (banner) |
| `PLANO-MIGRACAO-DE-CHAT.md` | Plano de migração de 2026-08-18 | HISTÓRICO (banner) |
| `PACOTE-MIGRACAO-CHAT-2026-08-18.md` | Snapshot de 2026-08-18 | HISTÓRICO (banner) |
| `PROMPT-INICIAL-DO-AGENTE.md` | Prompt da sessão original (contagens velhas) | HISTÓRICO (banner) |

Nada foi apagado — os históricos conservam a história; o banner ⚠️ no topo de cada um impede confusão com o vigente.

---

## Workspace da Arena × GitHub (2026-08-25 — DECISÃO DO CURADOR)

| O quê | Papel real |
|---|---|
| **GitHub** `institutocura-maker/Termos-RC` · branch `arena/01a03913-termos-rc` (esteira 10) | **Fonte da verdade.** O curador sobe PDFs, baixa arquivos (incl. xlsx/docx de leitura), vê o histórico. |
| **Branches das esteiras anteriores** (`arena/01a02e74` · `arena/01a02c4e` · `arena/01a02a88`) | Histórico versionado; a esteira vigente é a 10. **O curador pode subir arquivos em qualquer branch** (2026-08-25: subiu os DOCX Javé/Thot **e os PDFs Mentalma I/II** em `arena/01a02e74`) — conferir antes de editar. A pasta de obra em processamento fica na branch da sessão o ciclo inteiro (visível trocando a branch no GitHub) e só move para `CONCLUIDOS/` no fechamento. |
| **`main`** | Ainda em `b420f14` (PR #2, Windows). O trabalho desta esteira **não** está no `main`. |
| **Workspace Arena** | Sandbox do agente. Some com a sessão e **reverte entre turnos** (visto em 2026-08-25). **Decisão do curador (2026-08-25): sem investimento** — o curador não o usa; visor/preview ficam parados. |
| **Como o curador entrega PDF** | *Add files via upload* no GitHub → `uploads_recepcao/` → o agente faz `fetch`/cherry-pick. Anexos de chat **não** caem em `/home/user/uploads/`. |

Consequência operacional: **commit + push ao fim de cada turno** — o push é o que dura.

---

## Artefatos de leitura (xlsx / docx)

**Decisão do curador (2026-08-25): cópia versionada no GitHub** para download.

- `base-terminologica.xlsx` (7 abas) e `base-terminologica-leitura.docx` **estão no Git** a partir desta sessão.
- Ficam **regeneráveis**: a fonte continua sendo `dados_termos.py` + Markdown; os binários são espelho. Regenerar sempre antes de qualquer commit que mude a base:

```bash
python3 ferramentas/build_xlsx.py    # → base-terminologica.xlsx (7 abas)
python3 ferramentas/build_word.py    # → base-terminologica-leitura.docx
```

`indice-mestre.md` **está** no Git (regenerado a cada ciclo). Apostilas e tratados em DOCX **estão** no Git (`apostilas/CONCLUIDAS/`, `pedagogico/`) — **coleção completa** (10 apostilas temáticas + 2 tratados; Javé e Thot/Hermes recebidos do curador em 2026-08-25; no nome `Apostila - Javé_ O Buraco Negro...` o `_` é o `:` do título adaptado para Windows).

---

## Patrimônio da KB — o que é canônico

Camadas, da mais dura para a mais mole:

### 1. Núcleo (se isto sumir, a Base some)

| Arquivo | O que é |
|---|---|
| `ferramentas/dados_termos.py` | **Fonte única.** 777 termos + 1.852 relações. Validar sempre. |
| `ferramentas/build_xlsx.py` | BIBLIO das 87 obras. **Edição só manual.** |
| `termos/*.md` | 430 fichas (a carne da ontologia). |
| `indice-mestre.md` | Índice gerado; versionado. |

### 2. Governança (sem isto o próximo agente se perde)

| Arquivo | O que é |
|---|---|
| `PROMPT-PROXIMA-SESSAO.md` | **Vigente.** Estado + primeira ação + mapa da vigência. |
| `convencoes-editoriais-rc.md` | Grafias, quarentenas, Navalha. |
| `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Método (dossiê → Devolutiva → ampliação). |
| `01-ficha-modelo.md` | Ficha Padrão v2 + guia de preenchimento (norma da ficha). |
| `02-vocabulario-controlado.md` | Vocabulário controlado (norma dos nomes). |
| `CONTINUIDADE.md` | Diário da jornada (longo; cabeçalho = agora). |
| `INDICE-PALESTRAS.md` | Índice de palestras (estado reconstruído; atualizado a cada ciclo). |
| `CHECKPOINT-SESSAO-2026-08-21.md` | Retomada antiga; útil como história. **Não** usar o procedimento de clone com token. |
| `PROMPT-INICIAL-DO-AGENTE.md` | Identidade histórica (contagens velhas). |

### 3. Acervo trabalhado (a jornada)

| Pasta | Conteúdo |
|---|---|
| `livros/CONCLUIDOS/` | 35 obras integrais com PDF + extract + dossiê + ampliações (última: B074 *Mentalma I*). |
| `livros/AMOSTRAS/` | B027 e B035 (Sample; obra completa pendente). |
| `apostilas/CONCLUIDAS/` | 37 palestras/lives (original.txt + apostila.md + DOCX). |
| `pedagogico/` | 10 apostilas temáticas (todas com DOCX) + 2 tratados (com DOCX) + 2 mapas + índice temático + Guia TALM + Dossiê Fase 0 + matriz de auditoria. |
| `materiais_externos/` | EXT (terceiros; **não** toca ontologia). |
| `uploads_recepcao/` | PDFs que o curador subiu (fonte bruta; Mentalma II ainda aguardando ciclo). |
| `backups/pacotes/` | MANIFESTO + FICHAS + REGENERAÇÃO (seguro versionado; **manifesto de 2026-08-18 desatualizado** — ver pendências). |

### 4. Regenerável

`reconstrucao/` · `__pycache__/` · `base-terminologica.xlsx` e `base-terminologica-leitura.docx` (regeneráveis, **porém versionados por decisão do curador, 2026-08-25** — regenerar sempre antes de commitar).

### 5. Arquivos históricos — não confundir com o vigente

`README.md` (contagens 760/1433) · `STATUS-RESTAURACAO.md` · `PLANO-MIGRACAO-DE-CHAT.md` · `PACOTE-MIGRACAO-CHAT-2026-08-18.md` · `PROMPT-INICIAL-DO-AGENTE.md` — todos com banner ⚠️ no topo (revisão 2026-08-25).

---

## Ciclos da esteira — ENCERRADOS

**AGENTE 9:** B019 · B011 · B052 · B043 · B013 · B014 · B016 · B044 · B024 · B041 · B036 · B034 · B042 · B048 · B040 · B037 · B049 · B009 · B023 · B001 · B002 · B033 · B017 · B018 · B039 · B003 · B025 · B026 · B015 · B020 · B021 · B005 · B006 · **B022** · amostras B035 e B027 · Carbono.

Trilogias Dramas / Terra Atlantis / Queda e Ascensão: **ENCERRADAS.**

**AGENTE 10 (2026-08-25) — revisão de continuidade + ciclo B074 (zero códigos em tudo):**

- A. Higienização: banners HISTÓRICO em 5 arquivos + MAPA DA VIGÊNCIA (nada apagado).
- B. Workspace da Arena: **sem investimento** (decisão do curador) — GitHub = única interface.
- C. xlsx/docx de leitura: **versionados no GitHub** (decisão do curador) — gerados nesta sessão; coleção `pedagogico/` completa (DOCX Javé + Thot/Hermes recebidos).
- D. Mapa da KB: +3 peças (`01-ficha-modelo.md`, `02-vocabulario-controlado.md`, `INDICE-PALESTRAS.md`); correção `pedagogico/`: **10** apostilas temáticas (não 9).
- **E. B074 *Mentalma I***: Devolutiva O-1..O-8 aplicada — **5 fichas ampliadas** (RC-166/548/549/551/552) + **2 criadas** (RC-550 Vontade de Progredir, RC-553 Eu Profundo); **0 códigos** (veto absoluto); **B084** *O Legado Esquecido: o Yoga dos Trimurtianos* cadastrada (`identificada`); quarentena p. 215 (Hitler/Len Mion/biodemos) **banida da malha**; CIP 290 p. × PDF 227 = `[REVISAR]`; ISBN não gravado; pasta em `CONCLUIDOS/`.

HEAD: **`66b01e1`** `docs: pausa e handoff — mapa da KB, Workspace × GitHub, token removido` + commits da esteira 10 (revisão, DOCX pedagico, B074 — tip da branch `arena/01a03913-termos-rc`). PR **não** aberto.

Pendências de livro (quando o curador quiser): **B075 *Mentalma II*** (PDF já recebido); B076–B078 (sem PDF — quando o curador tiver); obras completas de B027 e B035. Pendências menores: manifest versionado (`backups/pacotes/`, 2026-08-18) ainda com contagens antigas — curador decide regenerar; CIP B074 `[REVISAR]`.

---

## Encerramento de sessão (checklist)

1. Última atualização (data, agente, branch, HEAD).
2. ESTADO CANÔNICO — só se `dados_termos.py` mudou.
3. Pendências de fundo — o curador escolhe a ordem.
4. Bloco *PROMPT PARA COLAR* — a sessão seguinte não depende do chat anterior.
