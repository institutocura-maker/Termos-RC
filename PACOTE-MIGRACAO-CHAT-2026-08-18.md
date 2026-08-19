# Pacote de Migração de Chat — Checkpoint 2026-08-18

## Identidade do projeto

**Base Terminológica das Revelações Cósmicas de Jan Val Ellam** e produção de apostilas integrais a partir de transcrições automatizadas.

Para migração entre chats, anexar preferencialmente:

- `PACOTE-DE-REGENERACAO-2026-08-18.txt` (núcleo canônico + builders + docs);
- `PACOTE-DE-FICHAS-2026-08-18.txt` (378 fichas);
- `PACOTE-DE-APOSTILAS-2026-08-18.txt` (apostilas CONCLUIDAS + temáticas);
- `PACOTE-DE-ORIGINAIS-2026-08-18.txt` (originais byte a byte);
- `MANIFESTO-PACOTES-2026-08-18.txt`;
- `GUIA-MESTRE-RC-APOSTILA.txt` (guia editorial).

O usuário é o **curador e autoridade final**. A IA organiza, cruza, edita e audita; não decide ontologia sem autorização.

## Espelhamento no GitHub (fonte alternativa de handoff)

O projeto também está espelhado num **repositório GitHub privado**, sincronizado com o estado canônico (2026-08-19):

- **URL:** `https://github.com/institutocura-maker/Termos-RC` (privado — requer token de acesso);
- **Branch:** `main` · **Último commit de sincronização:** `ba82bfe` ("feat: sincroniza estado completo");
- **Conteúdo:** núcleo canônico (`dados_termos.py` + 378 fichas + builders) + `apostilas/CONCLUIDAS/` com **dossiês de curadoria** (`analise/`) + temáticas (`pedagogico/`) + docs de migração + README atualizado;
- **O que NÃO está no repo (regenerável ou volumoso):** DOCX/XLSX (regeneráveis pelos builders), `reconstrucao/` (pacotes/backups — estão nos arquivos TXT deste pacote), `__pycache__`.

**Como clonar (novo chat):**
```bash
git clone https://x-access-token:SEU_TOKEN@github.com/institutocura-maker/Termos-RC.git
cd Termos-RC
python3 ferramentas/dados_termos.py   # deve validar: OK: 767 termos, 1531 relações
```

O **token** deve ser fornecido pelo curador ao novo chat (não está gravado em nenhum arquivo persistente). O GitHub é **fonte de espelhamento/backup** — o workspace local (`/home/user/rc-terminologia`) permanece a fonte primária de trabalho.

## Estado canônico (2026-08-18)

```text
OK: 767 termos, 1531 relações — dados válidos.
Faixa: RC-001–RC-767.
Próximo código disponível: RC-768.
Termos com ficha: 377.
Fichas físicas: 378 (377 canônicas + RC-004 como investigação).
Obras: 79.
Apostilas concluídas: 13 (em apostilas/CONCLUIDAS/).
```

Fonte única de verdade:

`/home/user/rc-terminologia/ferramentas/dados_termos.py`

Checksum SHA-256 (2026-08-18):

```text
7a95c8dd5bdb9b981b55f43e9dd1e34229f155be548e232870b27d9e69d028ac  ferramentas/dados_termos.py
652519f1ecb94b6583780b1f2d9d70d4306934e35ed0a0df2673bd10fc7caabb  indice-mestre.md
ef27809ec850bcb4c26d3d741d8fc60d1740c7f2ea8c97534f43b302de80af00  base-terminologica.xlsx
df493bc143133e22321a4bee386a71f846f1c887da95a716510da99546a7547b  base-terminologica-leitura.docx
8445ab5f17a2ac026253ddd745d5ead6afd055793c1432aaaa684a85a968db90  README.md
f3ee7f53496da76fa7176e43071ec476e6581d0ef112ed53ef2b3690e62fff78  CONTINUIDADE.md
ce4930b6356ded246c4a8eedb617bf5a756e73f57ec14b9b671cb887fe388fde  apostilas/INDICE-PALESTRAS.md
```

## Ciclos concluídos nesta sessão (18/08/2026)

| Palestra | Códigos | Status |
|---|---|---|
| P2023-05-13 — Bastidores da Revelação Cósmica | RC-761 | Base + **apostila concluída** |
| P2023-12-02 — Thot, o Enigmático Hermes Trimegisto | RC-762/763 | Base + **apostila concluída** |
| P2021-03-27 — Enki, Enlil e o Fim Súbito da Babilônia | RC-764/765 | Base + **apostila concluída** |
| P2024-09-28 — A Raça Inabalável dos Sethianos Emancipados | RC-766 | Base + **apostila concluída** |
| P2025-11-29 — A Revelação de Ifá e o Destino dos Seres | RC-767 | Base + **apostila concluída** |
| P2024-02-03 — O Jainismo e o Druidismo Ancestrais | RC-759/760 | Base + **apostila concluída** |

**13 apostilas DOCX concluídas** em `apostilas/CONCLUIDAS/` (incl. as 7 anteriores + estas 6).

## Maratonas e decisões curatoriais recentes

- **Pausa estratégica de palestras novas** (decisão do curador, 18/08): elaborar apostilas das palestras processadas antes de retomar novas — **CONCLUÍDA**;
- **RC-761** — As Cinco Lentes da Realidade (COS_PRO 2.5); absorções NT-BR02/03/05; veto NT-BR04 (quachadas);
- **RC-762** — As Três Escalas da Consciência; **RC-763** — As Sete Leis Herméticas; RC-463 elevado a fonte primária (Maat/Kybalion absorvidos);
- **RC-764** — Ao Vencedor as Batatas; **RC-765** — Relógio Messiânico; RC-487 (Enlil) com ficha criada; quarentena histórica (guerras atômicas);
- **RC-766** — A Raça Inabalável dos Sethianos Emancipados; desambiguação Elohim (RC-004) × Nefelins (RC-488);
- **RC-767** — Os 256 Caminhos Profetizáveis de Orunmilá; RC-655/665/666 elevados a fonte primária; absorções NT-IF02/03/04.

## Distinções canônicas permanentes

- Elm/Moros é ser LM de Tempérion; Perpérion ≠ Tempérion.
- En Ma ≠ Elm.
- Enoque humano ≠ Metatron.
- Mohen So = Phanes/Protogonos; Mohen So não é Moros.
- **WD (RC-560) foi FUNDIDO em Wyrd/Urd (RC-658)** — RC-560 é remissão histórica (`RC-560 —variação→ RC-658`).
- Hochmah é canônica; fonemas Rockma/Rockman são STT não resolvidos.
- Brahma, Tikun, Sophia, Nefilins, Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo (sempre com X), Vaishnavismo, Kapila seguem grafias canônicas.
- **Keshava**: STT "quachadas/quechada" (P2023-05-13; P2023-12-02) provavelmente distorce "Keshava" (pista do curador) — **VETO ESTRITO**, Colecionar Incertezas.

## Quarentenas vigentes

- **Clínico/científico:** leitura de Ellam, não fato (genótipos AA/AG/GG; identidade de gênero; vrittis/cittas; Penrose/Hameroff).
- **Político/geopolítico:** supremacia; pandemia; bases secretas nos EUA; silos; núcleos de poder; imperador japonês.
- **Ufológico:** encontros/Eisenhower; invasão de raças; guerras atômicas na antiguidade; tunelamento quântico de Ganga; portais.
- **Teológico:** Teologia Comparada/Crítica (Islã/Maomé; Krishna; Jesus/gnose; Niceia/Ário; Obatalá; Sai Baba).
- **Histórico:** cronologia interna do autor (450.000 anos; 6 bilhões; 13,8 bilhões; 2012; 2021; 2050; 4.000; 5.000).
- **STT duvidoso:** tudo que consta em "Colecionar Incertezas" de cada dossiê — não vira ontologia.
- **Falas da plateia:** sempre isoladas, nunca viram ontologia.

## Colecionar Incertezas (resumo ativo)

- "quachadas/quechada" (= Keshava? — pista do curador, 2026-08-18);
- "Hen Orl" / "20171" (colapso Trimurti) / "Prima Sai" / "Quinara" / "demo hesitante" / "hipócase";
- "Hainarok" (= Ragnarök) / "Osamaro Ibier" / "4.261 a.C." (alfabeto) / "morrensor/moruself";
- "Sinal de Lel/Lzen" (= provável "O Sinal de Lemur");
- "Paul Hiller" / "La de Confúcio" (frase truncada) / "Tubaral" / "imoléis" / "Vaius";
- Kybalion (1900 × 1908) / "Moci" / "NEPT" / "Dieck Eno" / "Nelsag Nimar" / "Rem e Renete".

## Correções de engenharia (2026-08-18)

1. **Gerador/restaurador de pacotes:** fidelidade byte a byte corrigida (concatenação sem join; busca binária do FIM-ARQ); teste 434/434 arquivos.
2. **Manifesto dinâmico:** `gerar_pacotes.py` agora computa o estado canônico automaticamente (antes hardcoded — ficava desatualizado).
3. **Duplicata órfã removida:** `apostilas/2024-11-02_fantasmas_passado_mitologico/` (raiz) era cópia parcial redundante da versão em `CONCLUIDAS/` — removida; a apostila DOCX permanece em CONCLUIDAS.
4. **Espelhamento GitHub (2026-08-19):** repositório privado `institutocura-maker/Termos-RC` sincronizado com o estado canônico (docs de migração, dossiês de curadoria `analise/`, temática Thot, README); commit `ba82bfe`; 727 arquivos rastreados; ver seção "Espelhamento no GitHub".

## Restaurador e pacotes

- Restaurador: `ferramentas/restaurar_pacotes.py` (v3, binário; aponta para `reconstrucao/pacotes/` e aceita caminhos por argumento).
- Formato: `===ARQ: caminho===` / `[conteúdo]` / `===FIM-ARQ: caminho===`.
- Última fidelidade verificada: **435/435 arquivos** (pacote == manifesto == workspace).

## Comando inicial de validação

```bash
cd /home/user/rc-terminologia
python3 ferramentas/dados_termos.py
```

Resultado obrigatório antes de qualquer edição:

```text
OK: 767 termos, 1531 relações — dados válidos.
```

## Próximas ações possíveis (aguardando curador)

1. Retomar palestras novas (faltam material-fonte: **Faces de Javé** P2024-02-25; **Dinastia das Sophias** P2025-07-25; **Setianos** já processado);
2. Regenerar o **Mapa do Buraco Negro Javé** (SEGURADO — aguardando mais palestras agregadas);
3. Revisar apostilas concluídas com o curador;
4. P2024-11-02 (Fantasmas) — **apostila concluída** (CONCLUIDAS), sem pendência.

> **Regra vigente:** nenhum código consumido além do aprovado; Base em 767/1.531; próximo código RC-768.
