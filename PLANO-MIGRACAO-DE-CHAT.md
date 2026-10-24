# Plano de Migração de Chat — Projeto RC

> **⚠️ ARQUIVO HISTÓRICO** (marcado na revisão de 2026-08-25 — AGENTE 10). Plano de 2026-08-18; migração já concluída. **Não usar como estado vigente** — prevalece `prompts/PROMPT-PROXIMA-SESSAO.md`.

**Versão:** 1.1  
**Data:** 18/08/2026  
**Objetivo:** mudar de conversa sem perder estado canônico, decisões curatoriais, rastreabilidade, quarentenas ou fluxo editorial.

## 1. Princípio central

A migração não deve depender da memória resumida do chat. O estado do projeto deve viajar por **arquivos persistentes e verificáveis**.

Ordem de autoridade:

1. `ferramentas/dados_termos.py` — fonte canônica;
2. decisões oficiais do curador em cada pasta de palestra;
3. `admin/logs/CONTINUIDADE.md`;
4. Dossiê/itens travados/auditorias da palestra em curso;
5. `README.md` e `apostilas/INDICE-PALESTRAS.md`;
6. pacote de migração do checkpoint;
7. histórico da conversa, apenas como apoio.

## 2. Condições para migrar

A migração é segura quando:

- o ciclo anterior está fechado ou há um checkpoint explícito;
- o original da palestra em curso está preservado;
- o estado da Base foi validado;
- o próximo código disponível está registrado;
- decisões pendentes estão num Dossiê ou arquivo de itens travados;
- checksums dos arquivos centrais foram calculados;
- nenhuma autorização do curador existe apenas no chat.

**Checkpoint atual (18/08/2026):** adequado para migração. Base em **767 termos / 1.531 relações** (RC-768 em seguida); **13 apostilas concluídas** em `apostilas/CONCLUIDAS/` (incl. P2024-11-02 Fantasmas, P2024-02-03 Jainismo e as 5 da pausa estratégica: Enki, Bastidores, Thot, Sethianos, Ifá). Pausa estratégica de palestras novas **concluída**; retomada de novas palestras depende de novo material-fonte do curador. Pacote de migração atualizado: `admin/logs/PACOTE-MIGRACAO-CHAT-2026-08-18.md`.

## 3. Arquivos obrigatórios do handoff

### Camada canônica

- `ferramentas/dados_termos.py`
- `indice-mestre.md`
- `base-terminologica.xlsx`
- `base-terminologica-leitura.docx`
- `termos/`

### Camada operacional

- `README.md`
- `admin/logs/CONTINUIDADE.md`
- `convencoes-editoriais-rc.md`
- `apostilas/INDICE-PALESTRAS.md`

### Palestra em curso

- `apostilas/2024-11-02_fantasmas_passado_mitologico/original.txt`
- `ficha_ingresso.md`
- `analise/METADADOS-INGRESSO.json`
- `analise/LEITURA-1-MACROESTRUTURA.md`
- `analise/LEITURA-2-TERMINOLOGICA.md`
- `analise/DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md`

### Pacotes anexáveis no novo chat

Como a plataforma não aceita upload de `.md`, usar:

- `reconstrucao/PACOTE-DE-REGENERACAO-2026-08-16.txt` — Base, builders, continuidade, plano e palestra pausada;
- `reconstrucao/PACOTE-DE-FICHAS-2026-08-16.txt` — 301 fichas detalhadas;
- `reconstrucao/GUIA-MESTRE-RC-APOSTILA-v1.0-2026-08-14.pdf` — continua válido;
- `reconstrucao/MANIFESTO-PACOTES-2026-08-16.txt` — checksums.

O pacote de regeneração já embute `PACOTE-MIGRACAO-CHAT-2026-08-16.md` e este plano.

## 4. Procedimento antes de sair do chat atual

1. registrar qualquer aprovação do curador nos arquivos da palestra;
2. executar:

```bash
cd /home/user/rc-terminologia
python3 ferramentas/dados_termos.py
```

3. conferir contagens e próximo código;
4. atualizar `admin/logs/CONTINUIDADE.md` e o índice de palestras;
5. calcular checksums dos arquivos centrais;
6. gerar/atualizar o pacote de migração;
7. não iniciar integração de códigos parcialmente.

## 5. Procedimento no chat novo

### Mensagem inicial recomendada

> Continue o projeto “Base Terminológica das Revelações Cósmicas de Jan Val Ellam”. O curador é a autoridade e a IA é ferramenta. Leia, nesta ordem: `PLANO-MIGRACAO-DE-CHAT.md`, `PACOTE-MIGRACAO-CHAT-2026-08-16.md`, `admin/logs/CONTINUIDADE.md`, `README.md`, `ferramentas/dados_termos.py` e o Dossiê em `apostilas/2024-11-02_fantasmas_passado_mitologico/analise/`. Responda em PT-BR. A palestra P2024-11-02 está PAUSADA: não solicite decisão, não atribua códigos e não inicie a apostila até autorização expressa do curador. Preserve originais, separe a plateia e mantenha as quarentenas clínicas, científicas, históricas, políticas e fonéticas. Confirme apenas as contagens, a pausa e o próximo código; depois aguarde a próxima orientação.

### Verificação obrigatória

O novo agente deve confirmar:

```text
Base: 727 termos, 1218 relações.
Faixa: RC-001–RC-727.
Próximo código: RC-728.
Palestra em curso: P2024-11-02.
Estado: Dossiê produzido; palestra PAUSADA por decisão do curador; aguardar autorização expressa de retomada.
```

Depois deve verificar o checksum de `dados_termos.py` indicado no pacote.

## 6. Teste de aceitação do handoff

A migração só é considerada concluída se o novo chat responder corretamente:

1. Qual é a fonte canônica? — `ferramentas/dados_termos.py`.
2. Quantos termos/relações há? — 727/1.218.
3. Qual é o próximo código? — RC-728.
4. Qual palestra está em curso? — P2024-11-02.
5. Pode gerar códigos agora? — Não, somente após devolutiva oficial.
6. Quais riscos prioritários? — autismo/teriantropia/licantropia, genética/Marte/IA, Ucrânia/Japão/Great Reset, grafias mitológicas.
7. O índice da Camada 2 vale como evidência? — Não.

## 7. Regras que não podem se perder

- apostila é transcrição editada integral, não resumo;
- preservar oralidade, humor, palavrões, digressões e autocorreções;
- não inventar/completar; usar `[REVISAR]`, `[TEXTO INCOMPLETO]` e `[frase truncada]`;
- separar absolutamente a plateia;
- Base canônica define grafias, mas só corrige STT quando o contexto permite;
- toda correspondência mitológica é atribuída a Ellam;
- alegações extraordinárias recebem ressalva;
- eBooks de IA não entram na camada canônica sem proveniência;
- Elm/Olm vêm de Tempérion e foram enviados a Perpérion;
- En Ma ≠ Elm;
- Enoque humano ≠ Metatron;
- Mohen So = Phanes/Protogonos, mas Mohen So ≠ Moros;
- Wyrd/Urd não deve ser automaticamente fundida a WD;
- Hochmah é grafia canônica, mas fonemas duvidosos continuam em revisão;
- Xamanismo sempre com X.

## 8. Estratégia de rollback

Se o novo chat detectar divergência:

1. não editar a Base;
2. comparar checksums;
3. restaurar o último backup em `reconstrucao/backups/` somente após identificar a diferença;
4. executar novamente a validação;
5. registrar a divergência em auditoria, sem apagar a versão conflitante.

## 9. Frequência de atualização

Gerar novo pacote de migração:

- após cada decisão oficial;
- após cada integração de códigos;
- após cada apostila aprovada;
- antes de trocar de chat;
- sempre que contagens ou próximo código mudarem.

## 10. Resultado

O projeto possui condições técnicas e documentais para migração de chat **sem perda de continuidade**, desde que o novo chat seja iniciado pelo pacote e valide o checkpoint antes de editar a Base.
