# CHECKPOINT DE SESSÃO — 2026-08-21

> **Documento de retomada** — para qualquer nova sessão do Agente Base-first continuar exatamente de onde esta parou, sem depender da janela de contexto anterior.

---

## 1. ESTADO CANÔNICO (verificar antes de tudo)

```text
OK: 777 termos (RC-001–RC-777), 1849 relações — dados válidos.
Próximo código disponível: RC-778.
Obras: 86 (B001–B083 + ART-2025-08-01/02/03).
Fichas físicas: 428 (427 canônicas + RC-004 investigação).
Apostilas concluídas: 32 em apostilas/CONCLUIDAS/.
Apostilas temáticas: 8 + 2 mapas + 1 tratado + 1 guia (pedagogico/).
GitHub: institutocura-maker/Termos-RC · HEAD: ed1bf36 (+5e10226 CONTINUIDADE).
Pacotes de reconstrução: reconstrucao/pacotes/ + cópia versionada em backups/pacotes/ (no GitHub).
```

**Validação:** `python3 ferramentas/dados_termos.py` → deve imprimir `OK: 777 termos, 1849 relações — dados válidos.`

## 2. COMO RETOMAR (procedimento padrão)

1. `cd /tmp && git clone https://x-access-token:${GH_TOKEN}@github.com/institutocura-maker/Termos-RC.git` (token: `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`; nunca salvar em arquivo; `x-access-token:` funciona no clone; push usa o token como username direto);
2. Copiar o clone para `/home/user/rc-terminologia/` (remover `.git` do workspace);
3. `python3 ferramentas/dados_termos.py` (validar) → `python3 ferramentas/build_indice.py` → `build_xlsx.py` → `build_word.py` (regenerar artefatos);
4. Se necessário reconstruir: `python3 ferramentas/restaurar_pacotes.py` (aponta para `reconstrucao/pacotes/`; XLSX/DOCX são regeneráveis, não embutidos);
5. Ler: `GUIA-MESTRE-RC-APOSTILA-v1.1.md`, `PROMPT-INICIAL-DO-AGENTE.md`, `CONTINUIDADE.md` (histórico + Colecionar Incertezas), `convencoes-editoriais-rc.md`.

## 3. O QUE FOI FEITO NESTA SESSÃO (cronologia resumida)

| Ordem | Ciclo | Resultado |
|---|---|---|
| 1 | P2021-01-23 — Vyasa e o Descortinar de um Novo Paraíso | Re-curadoria completa: 16 fichas ampliadas; **B082** cadastrada; apostila 12 PARTES (25.240 palavras — maior da série); commits `db492fe`+`93fbefb` |
| 2 | Correção de padrão | Notas verdinhas restauradas nas apostilas P2021-12-04 (21) e P2021-01-23 (24); commit `ade934e`+`82ba7b9` |
| 3 | P2021-12-04 — Os Archeons de Ereon e os Seres Adhy | Re-curadoria da faixa RC-596–619: 25 fichas ampliadas (Ogdóade 6+2; Apolônio=Olm; coma em Perpérion); apostila 10 PARTES (17.515 palavras); commits `895ff33`+`982349a` |
| 4 | Tratado filosófico | "A Ilha Estacionária e a Arca de Perguntas" (pedagogico/, 14 capítulos); índice temático com abordagem filosófica; commits `39238ac`+`b1cd65c` |
| 5 | ART-2025-08-01 — Fornos Replicadores | **RC-771 criado** (exceção); RC-500 corrigido (remissão); RC-499 promovido; RC-132 materializado; 10 fichas ampliadas; STT "Alamaior"=Awaymaion resolvido; **B083**; commits `3b0e140`+`d9b3389` |
| 6 | Apostila do ART-2025-08-01 | Padrão TOP (3 PARTES, 9 notas); pasta para CONCLUIDAS (30 apostilas); commit `e2cd2ca`+`c9e6ec3` |
| 7 | TRILOGIA DO PROJETO TALM (ART-02 + ART-03) | **6 códigos novos RC-772–777** (Morlens, Nanotecnologia Prânica, PEP, Éon das Três Esferas, Ginnungagap, Anã); acrônimo expandido do TALM; 15 ampliações; RC-064/RC-165 materializadas; apostilas TALM (4 PARTES) e Fenvans (3 PARTES); Guia da Trilogia; commit `768ad8d` (interrompido no workspace) |
| 8 | Correção pós-interrupção | Workspace ressincronizado; apostilas 02/03 regeneradas no padrão TOP completo (13+9 notas); DOCX reconstruídos; seção ART no índice; commit `f581a7e`+`92131c0` |
| 9 | Reorganização da Trilogia | Pastas órfãs removidas (workspace+GitHub); scripts arquivados nas pastas corretas; ferramentas/ limpa; commit `ed1bf36`+`5e10226` |
| 10 | **Checkpoint (esta etapa)** | Pacotes regenerados e **testados** (549 arquivos, 548 idênticos, base valida); cópia versionada em `backups/pacotes/`; este CHECKPOINT-SESSAO criado |

## 4. PENDÊNCIAS E PRÓXIMOS PASSOS

- **Próxima aventura:** a definir com o curador (ele indicou que "vamos iniciar uma nova aventura" após este checkpoint). Possibilidades: mais palestras da repassada (o curador marcou P2024-04-14, P2024-04-13, P2024-03-03 e P2024-03-02 como **concluídas/atualizadas** — NÃO reprocessar sem novo pedido), novas palestras inéditas que ele trouxer, ou novos materiais ART do curador;
- **Ampliações retidas sem ficha física (aguardando autorização para materializar):** RC-013/014 (Adhyatman/Adhydaiva), RC-135 (Vishnu), RC-163 (Mente Universal Emergente), RC-190 (Kardec), RC-343, RC-499 (já promovida — OK), RC-542, RC-019, RC-156, RC-075, RC-035, RC-457/458/459 (Tridevi), RC-211 (Kundalini) + anotações: Teurgia, Saccidanandhagana (candidato), Discurso Interior, Sanscaras, Kapila, Campos Morfogenéticos;
- **Colecionar Incertezas acumulada** (ver CONTINUIDADE.md — seção completa): inclui "o espírito que anima Ellam foi Vyasa"; "Parashara viveu mais de 10.000 anos"; DNA de Enoque fertilizando demos/minérios [REVISAR]; "forno de Alamaior" (RESOLVIDO = Awaymaion); 18.000 anos; grafia "Awayem"×"Awayen" [REVISAR — B083]; datas [REVISAR — conferir B050] (Shiva ~12,17 bi; Vishnu ~4,1 bi; bilatério ~4 bi; TALM ~7,5–7,7 bi; Olm 6–7 bi; biodemos ~900 mi; Trimurti presa 2012; desfeita 2015–2018); "Sophia autor do Apocalipse"; "YHWH no DNA" [QUARENTENA]; Toxoplasma Gondii [QUARENTENA CLÍNICA CRÍTICA]; "geral Lud"; Urantia (epíteto); Anã [REVISAR grafia];
- **Segurados:** Mapa do Buraco Negro Javé (regenerar quando pedido); Portal das Apostilas Temáticas (retomar quando o curador quiser); revisão de apostilas concluídas;
- **Obras pendentes de confirmação bibliográfica:** B079 (Inquisição Espiritual), B080, B081, B082, B083 (todas "identificadas"/"anunciadas" — aguardando editora/ISBN).

## 5. ARQUIVOS-CHAVE PARA A NOVA SESSÃO

| Arquivo | Função |
|---|---|
| `ferramentas/dados_termos.py` | Tabela-mestra (TERMOS + RELAÇÕES) — fonte única de verdade |
| `ferramentas/build_xlsx.py` | BIBLIO (obras B001–B083 + ARTs) — **nunca editar BIBLIO programaticamente**; editar manualmente |
| `ferramentas/build_indice.py` / `build_word.py` / `build_apostila.py` | Geradores de artefatos/apostilas |
| `ferramentas/gerar_pacotes.py` / `restaurar_pacotes.py` | Gerar/restaurar pacotes (hábito ao fim de cada ciclo) |
| `CONTINUIDADE.md` | Histórico de ciclos + Colecionar Incertezas + HEAD |
| `backups/pacotes/` (versionado) | Cópia de segurança dos pacotes no GitHub |
| `pedagogico/GUIA-TRILOGIA-TALM.md` | Narrativa integrada da Trilogia TALM |
| `pedagogico/TRATADO-ILHA-ESTACIONARIA-ARCA-DE-PERGUNTAS.md` | Tratado filosófico |
| `PROMPT-INICIAL-DO-AGENTE.md` / `GUIA-MESTRE-RC-APOSTILA-v1.1.md` | Instruções de operação |

## 6. REGRAS DE OURO (recordatório rápido)

- Curador = autoridade máxima; nada é consumido sem Devolutiva (O-1..O-7+); quase sempre ZERO códigos novos (Navalha de Ockham) — exceções autorizadas nesta sessão: RC-771 (ART-01) e RC-772–777 (Trilogia);
- Não inventar/não completar/não interpolar → `[REVISAR]`/`[NÃO REVELADO]`; falas da plateia nunca viram ontologia;
- Quarentenas: clínico/científico (Toxoplasma, DNA lixo, YHWH no DNA, 28.869 genes), político/geopolítico, ufológico, teológico — tudo leitura de Ellam;
- Grafias canônicas: Brahma, Tikun, Sophia (não Sofia), Nefilins, Ialdabaoth, Olm, Elm, Adhy, Javé, Vishnu, Xamanismo, Wyrd/Urd, Kapila, Vaishnavismo, Hochmah, Moros (não Morus), Malkuth=Hochmah=Sophia, Orlog=Moros, Norns Urd/Verdandi/Skuld, Awayen/Awaylengan/Awaymaion, Morlens, Ginnungagap;
- A cada ciclo: validar → ampliar (método `_ampliacoes_<data>.txt` + `_aplicar_ampliacoes_<data>.py`) → regenerar artefatos → apostila (se for o caso) → CONTINUIDADE/índices → `gerar_pacotes.py` → atualizar `backups/pacotes/` → git push.

---

**Checkpoint criado em 2026-08-21 pelo Agente RC (Arena), sob supervisão do curador Edson Cella Mendes.**
