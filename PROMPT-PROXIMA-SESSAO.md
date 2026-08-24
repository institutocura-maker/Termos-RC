# PROMPT DA PRÓXIMA SESSÃO — Base Terminológica RC

> **Ritual de continuidade.** Este arquivo é o prompt a colar (ou anexar) no chat seguinte. Vive no GitHub junto com `CHECKPOINT-SESSAO-2026-08-21.md` e `PROMPT-INICIAL-DO-AGENTE.md`.
>
> **Hábito obrigatório:** a sessão que estiver encerrando atualiza este arquivo *antes* do último commit — estado canônico, tarefas feitas, pendências e o próximo passo. A sessão nova lê este arquivo primeiro.
>
> **Última atualização:** 2026-08-24 · AGENTE 9 (Devolutiva B039 aplicada — 8 fichas, 0 códigos; trilogia Terra Atlantis encerrada) · branch `arena/01a02e74-termos-rc`.

---

## Como usar

1. Anexe **este arquivo primeiro** no chat novo.
2. Em seguida: `CHECKPOINT-SESSAO-2026-08-21.md` → `CONTINUIDADE.md` → `GUIA-MESTRE-RC-APOSTILA-v1.1.md` → `PROMPT-INICIAL-DO-AGENTE.md` → `convencoes-editoriais-rc.md`.
3. Cole o bloco abaixo (ou diga: *leia `PROMPT-PROXIMA-SESSAO.md`, monte o ambiente e apresente o estado*).

O `PROMPT-INICIAL-DO-AGENTE.md` permanece como identidade histórica do fluxo (contagens antigas 767/1531). **Este arquivo prevalece** para o estado vigente e para a primeira ação.

---

## PROMPT PARA COLAR NO NOVO CHAT

```
Continue o projeto Base Terminológica RC — as Revelações Cósmicas de Jan Val Ellam. Esta é uma sessão de continuidade; a anterior (AGENTE 9) criou o visor (downloads no preview da Arena pausados a pedido do curador) e concluiu o ciclo de higienização.

AUTORIDADE: o curador é a autoridade máxima e final. Você é a ferramenta que organiza, cruza, edita e audita. Nunca decida ontologia sem autorização expressa; suas conclusões são sempre sugestões, o curador valida. Só interrompa por ambiguidade realmente impeditiva. O fluxo é a lei.

PRIMEIRA AÇÃO OBRIGATÓRIA (antes de qualquer edição):
1. Verifique o workspace (o clone já vem pronto na raiz do repositório);
2. Instale as dependências, que NÃO persistem entre sessões:
   pip install --break-system-packages markdown openpyxl python-docx
3. Valide a base: python3 ferramentas/dados_termos.py
   → deve retornar exatamente: OK: 777 termos, 1852 relações — dados válidos.
4. Leia nesta ordem: PROMPT-PROXIMA-SESSAO.md (este) → CHECKPOINT-SESSAO-2026-08-21.md (inclui a atualização de 2026-08-22) → CONTINUIDADE.md (cabeçalho, HEAD e "Colecionar Incertezas") → GUIA-MESTRE-RC-APOSTILA-v1.1.md → PROMPT-INICIAL-DO-AGENTE.md → convencoes-editoriais-rc.md;
5. Resuma ao curador: estado verificado + pendências + próximo passo sugerido;
6. Aguarde a confirmação do curador antes de editar qualquer coisa.

ESTADO CANÔNICO ESPERADO: 777 termos (RC-001–RC-777) · 1.852 relações · próximo código livre RC-778 · 428 fichas físicas (427 canônicas com ficha=True + RC-004 investigação False) · 86 obras (B001–B083 + ART-2025-08-01/02/03) · 37 apostilas em apostilas/CONCLUIDAS/ (todas com DOCX e original.txt) · pedagógico com 10 MD temáticas (8 com DOCX; faltam DOCX de Javé/Buraco Negro e Thot/Hermes) + 2 tratados + 2 mapas + Guia da Trilogia TALM + Dossiê Fase 0 + índices · visor em ferramentas/visor_workspace.py.

TAREFA Nº 1 — VISOR (FEITO, downloads no preview PAUSADOS): ferramentas/visor_workspace.py existe; tema escuro areia/lilás; somente leitura. O download/ZIP no iframe da Arena não conclui (o arquivo chega, o painel bloqueia gravar). Não retomar a menos que o curador peça.

TAREFA Nº 2 — CICLO DE HIGIENIZAÇÃO (FEITO em 2026-08-23):
1. Flags True: RC-064, RC-132, RC-165, RC-499. RC-004 permanece False.
2. 13 DOCX regenerados.
3. original.txt restaurados (Irmãos Dias = TXT da raiz SHA bf54fba1…; Prabrajna = extract validado leitura-pdf-completo.txt; PDF-fonte SHA cee4ef97…).

CORREÇÃO JÁ APLICADA (não refazer): compatibilidade com Windows 11 — PR #2, merge b420f14: dois DOCX em pedagogico/ tinham ':' no nome (proibido no NTFS, abortava o git clone) e o gerador ganhou nome_seguro_windows() em build_apostila.py. Confirmado no clone da sessão 9: a função existe; nenhum ':' em pedagogico/. Os DOCX de Javé/Buraco Negro e Thot/Hermes NÃO estão na árvore (só os .md) — regenerar só se o curador pedir. O hash 4af6e6c pode não aparecer (clone raso).

PENDÊNCIAS DE FUNDO (eu escolho a ordem): **B003 *Reintegração Cósmica*** — piloto aberto (`livros/B003_reintegracao_cosmica/`); dossiê enxuto aguarda Devolutiva O-1..O-8; 0 códigos; B025 e B026 na gaveta (mesmo PDF, págs 104+ e 197+). **B027 *Nos Céus da Grécia*** — Devolutiva da amostra aplicada (2 fichas; pasta em `livros/B027_nos_ceus_da_grecia/`; obra completa ainda pendente). **B035 *O Big Data do Criador*** — Devolutiva da amostra aplicada (7 fichas; pasta em `livros/B035_o_big_data_do_criador/`; obra completa ainda pendente). Portal das Apostilas Temáticas (guardado); ampliações retidas sem ficha; Mapa do Buraco Negro Javé; B079/B080/B081/B083. B019, B011, B052, B043, B013, B014, B016, B044, B024, B041, B036, B034, B042, B048, B040, B037, B049, B009, B023, B001, B002, B033, B017, B018, B039 e Carbono: ENCERRADOS. Devolutivas B035/B027 (amostras) e B023/B001/B002/B033/B017/B018/B039 (integrais): ENCERRADAS. Trilogia dos Dramas: ENCERRADA. Trilogia Terra Atlantis: ENCERRADA.

REGRAS DE OURO (inegociáveis): não inventar, não completar, não interpolar — marcar [REVISAR], [TEXTO INCOMPLETO], [frase truncada], [NÃO REVELADO]; falas da plateia sempre isoladas e nunca viram ontologia; Navalha de Ockham — quase sempre zero códigos novos, prefira ampliar fichas existentes (protege o RAG local); nenhum código é consumido antes da Devolutiva (O-1..O-8); quarentenas clínico/científica, político/geopolítica, ufológica, teológica e biográfica — tudo é leitura de Ellam, não fato validado; grafias canônicas: Brahma, Tikun, Sophia (não Sofia), Nefilins, Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo (com X), Wyrd/Urd (RC-658; RC-560 é remissão), Kapila, Vaishnavismo, Hochmah, Moros (não Morus), Malkuth=Hochmah=Sophia, Orlog=Moros, Norns Urd/Verdandi/Skuld, Awayen/Awaylengan/Awaymaion, Morlens, Ginnungagap, Orunmilá, Obatalá, En Ma, Deva/Aurora, Mohen So; preservar a voz de Ellam (marcadores, humor, digressões) — o editor é menor que o autor; jamais editar a lista BIBLIO de build_xlsx.py programaticamente (já corrompeu 2×) — edição manual.

FIM DE TODO CICLO (hábito obrigatório): validar dados_termos.py → regenerar artefatos (build_indice.py, build_xlsx.py, build_word.py) → apostila/DOCX se houver → atualizar CONTINUIDADE.md e os índices → atualizar ESTE arquivo (PROMPT-PROXIMA-SESSAO.md) → python3 ferramentas/gerar_pacotes.py → atualizar backups/pacotes/ → commit e push no branch da sessão → abrir PR só quando eu pedir.

LIÇÃO DA SESSÃO 8: o merge/fechamento do PR encerra a sessão de código e bloqueia todo acesso remoto ao GitHub. Portanto: faça o push do trabalho ANTES de abrir o PR final, e deixe o PR por último.

Comece agora: monte o ambiente, valide a base, leia os documentos e me apresente o estado + o próximo passo. Aguarde minha confirmação antes de editar.
```

---

## Estado verificado na abertura da sessão 9 (2026-08-23)

Não alterar ontologia com base neste bloco — é auditoria, não devolutiva.

| Item | Resultado |
|---|---|
| Validação | `OK: 777 termos, 1852 relações — dados válidos.` |
| Sequência | RC-001–RC-777 contínua; próximo livre **RC-778** |
| Fichas físicas | 428 `.md` em `termos/` |
| Flags `ficha=True` | 423 (todos com arquivo) |
| Flags `ficha=False` com arquivo | RC-004 (investigação — não mexer), **RC-064, RC-132, RC-165, RC-499** (desatualizados) |
| Obras | 86 ids em BIBLIO |
| Apostilas CONCLUIDAS | 37 pastas |
| Sem DOCX | 13 (lista da Tarefa 2.2) |
| Sem `original.txt` | Prabrajna 2024-05-04; Podcast Irmãos Dias 2026-08-04 |
| `visor_workspace.py` | ausente no clone |
| Windows / `:` | `nome_seguro_windows()` presente; nenhum `:` em `pedagogico/` |
| Clone | raso; só o merge `b420f14` do PR #2 |
| Uploads não processados | 2 PDFs em `uploads_recepcao/` |

---

## Encerramento de sessão (checklist deste arquivo)

Antes do último commit, a sessão corrente deve atualizar:

1. **Última atualização** (data, número do agente, branch, HEAD).
2. **ESTADO CANÔNICO ESPERADO** — só se `dados_termos.py` tiver mudado.
3. **Tarefas 1 e 2** — marcar feito / parcial / ainda pendente; não apagar o enunciado enquanto restar recorte.
4. **Pendências de fundo** — o curador escolhe a ordem; não promover item à ontologia.
5. O bloco *PROMPT PARA COLAR* — para a sessão seguinte abrir sem depender do chat anterior.
