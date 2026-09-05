# Decisão do Curador — ciclo F030 (Colégio Druídico — Estudo Continuado, Daniela D. Ferro)

**Data do despacho:** 05/09/2026 · **Transição:** LEVANTAMENTO/DEVOLUTIVA → **APLICACAO** (`altera_base = true`)
**Natureza deste registro:** memória lavrada fiel ao despacho do curador sobre a Devolutiva (Q-F030-A…F + D-12). Onde o texto aqui parafraseia, a fonte de autoridade é o despacho do curador na conversa da esteira — este arquivo existe para fixar o que FOI ordenado, item a item, e o que foi **terminantemente proibido**.

---

## 1. VEDAÇÃO-MESTRA (terminante)

> O documento F030 **não pode** ser âncora de: (a) nenhuma citação aspeada em ficha; (b) nenhuma datação nova (1976, 3194, "20 mil", "15 mil" etc.); (c) nenhuma formulação de mitologia externa ("Liguriano", "52 mitologias", "Bohr/pai de Odin").

F030 fica admittedo apenas como **contexto de convergência** (auditoria de leitura), nunca como fonte.

## 2. Despacho por questão

| Questão | Decisão | Conteúdo operativo |
|---|---|---|
| **Q-F030-A** (sigla/estado) | **Aprovada** | sigla F030 homologada; ciclo registrado na caixa da Família F |
| **Q-F030-B** (enriquecimentos) | **Opção C** | B1–B3 executados **ancorados exclusivamente nas fontes originais** (P2022-09-18, B017, B052); F030 só como contexto de convergência — ver §3 |
| **Q-F030-C** (Benem) | **Sim — na fila** | Benem na fila aberta, `ficha=False`, fonte estrita **B018**; grafia do doc ("Benen") registrada como variação/distorção, sem propagar. **RETIFICAÇÃO DE EXECUÇÃO (§4.1):** a fila já continha Benem — materializado no **RC-032** (existente), não em código novo |
| **Q-F030-D** (radar de palestras) | **Radar apenas** | R-1 (Palestras 22/44 do Grupo 4 IEEA) fica como radar do acervo; **nenhuma peça fantasma** é criada nem preanunciada |
| **Q-F030-E** (texto incompleto) | **Fechar-assim** | o ciclo fecha sobre o material existente; a lacuna [TEXTO INCOMPLETO] é **declarada formalmente** (sem especulação de conteúdo) |
| **Q-F030-F** (brutos na caixa) | **Preparar auditoria** | auditoria SHA-a-SHA da Família F registrada em `backups/` como **preparatória**; **exclusão física aguarda comando final do curador** |
| **D-12** (relíquias) | **Navalha mantida + enriquecimento** | **nenhuma ficha nova para os artefatos**; enriquecer **RC-398 e RC-068** com a precisão mitográfica (Lugh, Dagda, Nuada, Fál) **citando obrigatoriamente P2022-09-18**; F030 vale como **bússola para corrigir a perda fonética do STT**, não como fonte |

## 3. Escopo aprovado da aplicação (opção C)

- **B1 — RC-403 (Collegiado Druídico):** nota de convergência do tríptico 270M/230M/4M — o material já está ancorado em RC-025/RC-109/RC-092; F030 entra registrado como contexto, **zero dados novos**.
- **B2 — RC-398 + RC-068:** bloco de ampliação com a aspa verbatim de P2022-09-18 (U0002 · chars 876–1423) e a precisão mitográfica das quatro relíquias; datação do episódio = «há 14.000 anos atrás» (âncora da palestra; as datas do doc não entram). Vínculo `P2022-09-18` acrescentado às fontes das duas fichas no cadastro.
- **B3 — RC-437 (Joctan e Faleg):** cena do mensageiro com aspa byte-exata de B052 p. 111; registro explícito da distorção do doc ("neto" onde a base canônica mantém **filho**; o mensageiro como portador da instrução). F030 **não entra como fonte**.
- **Fila — Benem (retificado: RC-032, não RC-930):** reforço na linha **existente** RC-032 «Benem» (provisório, `ficha=False`, fontes B031/B017/B018/B061 — B018 já presente ✓); 3 arestas `relaciona-se-a` acrescentadas, cada uma sustentada byte a byte por B018 (→RC-022 «As duas bases — Benem e Antlar —…»; →RC-058 «Frota Norte, em torno da nave “espheron”»; →RC-109 «os 126 Val despertos de Benem») + relacionados da linha atualizados; ficha RC-062 corrigida onde registrava «sem aresta».
- **Q-F030-F:** `backups/REGISTRO-LIMPEZA-2026-09-05-13.json` (preparatório; nenhum `rm`).

## 4. Efeito material medido (05/09/2026)

- `ferramentas/dados_termos.py`: **+0 termos · +3 relações (RC-032)** → `OK: 929 termos, 1887 relações — dados válidos.`; fontes de RC-398 e RC-068 acrescidas de `P2022-09-18`.
- Fichas alteradas (5, com RC-062): `termos/RC-398-thuata-de-dannan.md`, `termos/RC-068-hiperborea.md`, `termos/RC-403-colegiado-druidico.md`, `termos/RC-437-joctan-e-faleg-filhos-de-heber.md` — todas com "Última atualização" → 2026-09-05.
- Espelhos regenerados: `indice-mestre.md` (929 linhas), `base-terminologica.xlsx` (7 abas), `base-terminologica-leitura.docx` (Termos: 929 · Relações: 1887 · Obras: 102 · Fichas: 623).

### 4.1 Retificação de execução (transparência de erro)

O LEVANTAMENTO propusera código novo (fila "RC-### Benem" — D-5) porque a varredura antifabricação foi feita **por número/código**, não **por nome**. Na aplicação, o scan nominal contra `dados_termos.py` revelou **RC-032 «Benem»** e **RC-065 «Frota Norte»** já cadastrados (fila, ficha=False, B018 entre as fontes) — e a própria ficha RC-062 registrava «Benem | RC-032 | sem aresta em RELACOES». Criar RC-930 seria duplicação proibida pela regra (e). O despacho foi cumprido sobre a peça existente (3 arestas + relacionados), com D-5 e mapeamento retificados no lugar. **Nenhum código foi eliminado; nenhum número de RC foi queimado** (930 nunca existiu fora desta pasta).
- Portão verbatim das aspas novas: **5/5 PASS** contra `ciclos/P2022-09-18/original.txt`, `livros/CONCLUIDOS/B052_…/original.txt` e (para o trecho F030 citado como distorção) `consolidacoes/F030_colegio-druidico/fonte.txt` — normalização apenas de quebras de linha/nbsp da extração, texto íntegro (inclusive a grafia do livro "descentes").
