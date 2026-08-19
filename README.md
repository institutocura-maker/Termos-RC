# Termos-RC — Curadoria Terminológica Espiritual

> Repositório de curadoria, glossário e apostilas da tradição **RC** (Revelação Cósmica).
> Owner: **institutocura-maker**
> Iniciado em: 2026-08-19 (sessão Apostila(6))

---

## 🎯 Propósito

Este repositório é o **lar versionado** do projeto de curadoria terminológica que vinha sendo desenvolvido em sessões anteriores da plataforma Arena.ai (sessões APOSTILA(1) a APOSTILA(5)).

Ele contém:
- **Base terminológica** dos termos da Revelação Cósmica (RC-001 a RC-767+)
- **Apostilas concluídas** (13 palestras curadas)
- **Ferramentas Python** de apoio (build de índices, .docx, .xlsx, pacotes)
- **Material pedagógico** (estudos temáticos)
- **Pacotes de migração** entre chats (CONTINUIDADE, RELATÓRIOS, etc.)

---

## 📁 Estrutura

```
rc-terminologia/
├── README.md                              ← este arquivo
├── STATUS-RESTAURACAO.md                  ← controle de migração entre chats
├── indice-mestre.md                       ← índice geral (em restauração)
├── CONTINUIDADE.md                        ← guia de continuidade entre sessões
├── GUIA-MESTRE-RC-APOSTILA.txt            ← documento-mestre (em restauração)
├── 01-ficha-modelo.md
├── 02-vocabulario-controlado.md
├── convencoes-editoriais-rc.md
├── INDICE-PALESTRAS.md
├── PACOTE-MIGRACAO-CHAT-2026-08-16.md
├── PACOTE-MIGRACAO-CHAT-2026-08-18.md
├── PLANO-MIGRACAO-DE-CHAT.md
├── RELATORIO-DE-RESTAURACAO-2026-08-17.md
├── RELATORIO-NOVOS-TERMOS-RC-728-745.md
│
├── apostilas/
│   └── CONCLUIDAS/                        ← 13 apostilas finalizadas
│       ├── 2021-03-27_enki_enlil_fim_babilonia/
│       │   ├── Apostila - Enki, Enlil e o Fim Súbito da Babilônia.docx
│       │   ├── apostila.md
│       │   ├── ficha_ingresso.md
│       │   ├── original.txt
│       │   └── analise/
│       │       ├── camada-0.txt ... camada-3.txt
│       │       ├── DECISAO-DO-CURADOR.md
│       │       ├── DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md
│       │       ├── leitura-segmentada.txt
│       │       ├── METADADOS-INGRESSO.json
│       │       ├── RELATORIO-DE-CICLO.md
│       │       └── leitura/
│       │           └── chunk-01.txt ... chunk-NN.txt
│       ├── ... (12 outras apostilas)
│
├── ferramentas/                          ← scripts Python
│   ├── build_apostila.py
│   ├── build_indice.py
│   ├── build_word.py
│   ├── build_xlsx.py
│   ├── criar_pasta_palestra.py
│   ├── dados_termos.py
│   ├── gerar_pacotes.py
│   └── restaurar_pacotes.py
│
├── pedagogico/                            ← estudos temáticos
│   ├── Apostila - Javé_ O Buraco Negro da Revelação Cósmica.docx
│   ├── Apostila-Estudo-Jave-Buraco-Negro.md
│   ├── MAPA-JAVE-CONEXOES.md
│   └── mapa-jave-conexoes.svg
│
├── reconstrucao/                          ← backups e pacotes
│   ├── backups/                           ← versões históricas de dados_termos.py
│   └── pacotes/                           ← pacotes agregados para migração
│       ├── MANIFESTO-PACOTES-2026-08-18.txt
│       ├── PACOTE-DE-APOSTILAS-2026-08-18.txt
│       ├── PACOTE-DE-FICHAS-2026-08-18.txt
│       ├── PACOTE-DE-ORIGINAIS-2026-08-18.txt
│       └── PACOTE-DE-REGENERACAO-2026-08-18.txt
│
├── referencias-curador/                   ← artigos de referência
│   └── artigos/
│       └── 2026-08-18_quarto_cerebro_pandora_denise/
│
└── termos/                                ← 378 fichas terminológicas
    ├── RC-001-jave.md
    ├── RC-002-rebeliao-de-lucifer.md
    ├── ...
    └── RC-767-os-256-caminhos-profetizaveis-de-orunmila.md
```

---

## 🚀 Como usar (na plataforma Arena.ai)

### Restauração da sessão
1. Em uma nova sessão, peça ao agente para "ler o `STATUS-RESTAURACAO.md`"
2. O agente vai entender onde paramos e sugerir os próximos passos

### Versionamento com GitHub
- Repositório: https://github.com/institutocura-maker/Termos-RC
- Clone: `git clone https://github.com/institutocura-maker/Termos-RC.git`
- Push: `git push origin main`

---

## 📊 Status atual

- ✅ Estrutura de pastas reconstruída (164 pastas)
- ⏳ ~831 arquivos a restaurar (em andamento)
- ⏳ 10 arquivos críticos pendentes (ver `STATUS-RESTAURACAO.md`)

---

## 📜 Histórico de sessões

| Sessão | Data | Backup | Observação |
|--------|------|--------|------------|
| APOSTILA(5) V5.0 FINAL | até 2026-08-19 | `BKP_APOSTILA(5)V5.0_FINAL` | backup local em C:\RC News\IEEA\_BACKUP_ |
| **APOSTILA(6)** | **2026-08-19 →** | **este repo** | **migração para GitHub** |

---

*"A continuidade entre sessões é o que mantém vivo o trabalho do curador."*
