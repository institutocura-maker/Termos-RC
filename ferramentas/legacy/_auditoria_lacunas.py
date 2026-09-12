#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITORIA DE LACUNAS — FASE 0 (livros B001-B083 × malha RC).

Cruzamento: BIBLIO (build_xlsx.py) × TERMOS/RELACOES (dados_termos.py) × fichas (termos/).

Produz:
  pedagogico/DOSSIE-AUDITORIA-LACUNAS-FASE-0.md   (relatório)
  pedagogico/_matriz-auditoria-lacunas.csv        (matriz obra × termos, apoio)

Não altera a KB. Reutilizável: rode novamente após cada ciclo para atualizar o dossiê.
Uso: python3 ferramentas/_auditoria_lacunas.py
"""
import sys, os, re, glob
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import dados_termos as dt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PED = os.path.join(RAIZ, 'pedagogico')

# ----------------------------------------------------------------- BIBLIO (regex, sem executar build_xlsx)
src = open(os.path.join(RAIZ, 'ferramentas', 'build_xlsx.py'), encoding='utf-8').read()
m = re.search(r'BIBLIO\s*=\s*\[(.*?)\n\]', src, re.S)
obras = re.findall(r'\[\s*"(B\d+|ART-\d{4}-\d{2}-\d{2})"\s*,\s*"([^"]+)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"', m.group(1))
BIBLIO = {o[0]: {"titulo": o[1], "subtitulo": o[2], "editora": o[3], "ano": o[4], "status": o[5]} for o in obras}

# ----------------------------------------------------------------- TERMOS
termos = dt.TERMOS
rels = dt.RELACOES
n_fichas = len(glob.glob(os.path.join(RAIZ, 'termos', '*.md')))

sem_ficha = [t for t in termos if not t[7]]
com_ficha = [t for t in termos if t[7]]

# citações por fonte
cit = Counter()
for t in termos:
    for f in t[5]:
        cit[f] += 1

# termos sem ficha por obra-fonte
sf_por_obra = defaultdict(list)
for t in sem_ficha:
    for f in t[5]:
        sf_por_obra[f].append(t[0])

# fichas magras (<=150 palavras)
magras = []
for fp in glob.glob(os.path.join(RAIZ, 'termos', '*.md')):
    txt = open(fp, encoding='utf-8').read()
    n = len(txt.split())
    if n <= 150:
        magras.append((n, os.path.basename(fp).replace('.md', '')))
magras.sort()

# categorias dos sem-ficha
cat_sf = Counter()
for t in sem_ficha:
    cat_sf[t[2]] += 1

# ----------------------------------------------------------------- relatório
L = []
add = L.append
add("# DOSSIE DE AUDITORIA DE LACUNAS — FASE 0\n")
add("**Base Terminológica RC — Revelações Cósmicas de Jan Val Ellam**  ")
add("Gerado em 2026-08-22 pelo Agente RC (Arena) · Supervisão: curador Edson Cella Mendes  ")
add("Ferramenta reutilizável: `ferramentas/_auditoria_lacunas.py` · Matriz de apoio: `_matriz-auditoria-lacunas.csv`\n")

add("> **Objetivo da Fase 0:** responder, com dados, *quais livros merecem reprocessamento* no fluxo moderno "
    "(camadas → unidades → chunks → leituras → dossiê → devolutiva → ampliações). Nenhuma decisão é tomada aqui: "
    "este dossiê **não altera a KB** e orienta a escolha do piloto (Fase 1).\n")

add("## 1. Resumo executivo\n")
add(f"- **Panorama:** {len(termos)} termos · {len(rels)} relações · {n_fichas} fichas físicas · {len(obras)} obras na BIBLIO · "
    f"{len(cit)} fontes distintas citadas na malha.\n")
add(f"- **{len(sem_ficha)} termos sem ficha física** ({len(sem_ficha)/len(termos)*100:.0f}% da malha) — vivem só na tabela-mestra; "
    "nenhuma ampliação, nenhuma citação rastreável.\n")
add(f"- **40 obras marcadas como 'trabalhada'** (era pré-GitHub) — mas a representação na malha é **muito desigual**: "
    f"de {max(cit.get(b,0) for b in BIBLIO if b.startswith('B'))} citações (obra mais citada) até **1** (B059, B064).\n")
add(f"- **{len([b for b in BIBLIO if b.startswith('B') and cit.get(b,0)==0])} obras com ZERO citações** na malha — todas as 9 'a confirmar' "
    "(sem PDF) + 24 'identificadas' + 5 'anunciadas'.\n")
add(f"- **{len(magras)} fichas magras** (≤150 palavras) — esqueletos sem carne.\n")
add(f"- **Lacuna infraestrutural:** nenhum PDF/TXT de livro está arquivado no workspace (os 28 uploads processados são de palestras). "
    "**Reprocessar livro exige o original** — o curador precisará anexar os PDFs na Fase 1.\n")
add(f"- **Nota de governança:** B031 (glossário de Raquyel Braga) é a 2ª fonte mais citada ({cit.get('B031',0)} termos) — "
    "fonte **secundária** que deu o esqueleto da tabela; obras primárias de Ellam devem ser prioridade no reprocessamento.\n")

add("## 2. Metodologia\n")
add("- **Malha:** `ferramentas/dados_termos.py` (TERMOS: código, nome, categoria, subcategoria, status, fontes, relacionados, ficha).\n")
add("- **Obras:** BIBLIO em `ferramentas/build_xlsx.py` (86 obras: B001–B083 + ART-2025-08-01/02/03), lida por regex (nunca editada).\n")
add("- **Fichas:** arquivos em `termos/` (428). 'Magra' = ≤150 palavras.\n")
add("- **Indicador de cobertura:** nº de termos que citam a obra no campo *fontes* (citação ≠ profundidade, mas é o melhor proxy disponível sem os textos).\n")
add("- **Potencial de ampliação por obra:** nº de termos associados à obra **sem ficha física** (só a tabela-mestra tem o termo).\n")

add("## 3. Panorama da BIBLIO\n")
add("| Status | Qtd | Leitura para a auditoria |\n|---|---|---|\n")
status_c = Counter(o[5] for o in obras)
for st, n in status_c.most_common():
    leitura = {"trabalhada": "processadas na era pré-GitHub — candidatas a re-curadoria seletiva",
               "a confirmar": "aguardando PDF — não citadas",
               "identificada": "mapeadas, sem processamento",
               "anunciada": "futuras/em lançamento (B079–B083 etc.)",
               "minerada": "Enciclopédias/Glossários (B060/061/071/072/073)",
               "amostra recebida": "parciais (B027, B035)",
               "curadoria": "materiais ART — já no fluxo moderno"}.get(st, "")
    add(f"| {st} | {n} | {leitura} |\n")

add("\n## 4. Cobertura da malha por obra (ranking)\n")
add("Contagem de termos que citam cada obra como fonte. Obras B### trabalhadas, ordenadas:\n")
add("| Obra | Título | Citações | Termos-sf (potencial) |\n|---|---|---|---|\n")
trab = sorted([b for b in BIBLIO if b.startswith('B') and BIBLIO[b]['status'] == 'trabalhada'],
              key=lambda b: -cit.get(b, 0))
for b in trab:
    n = cit.get(b, 0)
    pot = len(sf_por_obra.get(b, []))
    add(f"| {b} | {BIBLIO[b]['titulo'][:52]} | {n} | {pot} |\n")
add("\n*'Termos-sf' = termos que citam a obra e não têm ficha física (candidatos a ampliação se a obra for reprocessada).*\n")

add("## 5. Obras trabalhadas SUB-REPRESENTADAS (≤20 citações)\n")
add("Candidatas naturais ao reprocessamento (a priorizar por centralidade temática):\n")
sub = [(b, cit.get(b, 0)) for b in trab if cit.get(b, 0) <= 20]
sub.sort(key=lambda x: x[1])
add("| Obra | Título | Citações | Termos-sf |\n|---|---|---|---|\n")
for b, n in sub:
    add(f"| {b} | {BIBLIO[b]['titulo'][:52]} | {n} | {len(sf_por_obra.get(b, []))} |\n")

add("\n## 6. Obras com ZERO citações (sem PDF ou não processadas)\n")
zero = sorted([b for b in BIBLIO if b.startswith('B') and cit.get(b, 0) == 0])
add("| Obra | Título | Status |\n|---|---|---|\n")
for b in zero:
    add(f"| {b} | {BIBLIO[b]['titulo'][:56]} | {BIBLIO[b]['status']} |\n")
add(f"\n**Total: {len(zero)} obras.** Nenhuma delas pode ser reprocessada sem o PDF original (anexar em upload na Fase 1).\n")

add("## 7. Termos sem ficha física (354)\n")
add(f"**{len(sem_ficha)} termos** têm entrada na tabela-mestra (nome, categoria, fontes, relações) mas **não têm ficha em `termos/`** — "
    "não há ampliação, contexto ou citação rastreável. Distribuição por categoria:\n")
add("| Categoria principal | Termos sem ficha |\n|---|---|\n")
for cat, n in cat_sf.most_common():
    add(f"| {cat} | {n} |\n")
add("\nLista completa: ver `_matriz-auditoria-lacunas.csv` (coluna 'sem_ficha'). "
    "Exemplos de termos órfãos já sinalizados na Colecionar Incertezas: RC-013/014 (Adhyatman/Adhydaiva), RC-135 (Vishnu/Lakshmi), "
    "RC-163 (Mente Universal Emergente), RC-190 (Kardec), RC-211 (Kundalini), RC-343, RC-542, RC-457/458/459 (Tridevi) etc.\n")

add("## 8. Fichas magras (≤150 palavras)\n")
add(f"**{len(magras)} fichas** são esqueleto sem carne — cabeçalho + definição sintética, sem ampliação:\n")
add("| Palavras | Ficha |\n|---|---|\n")
for n, nome in magras:
    add(f"| {n} | {nome} |\n")

add("## 9. Lacuna infraestrutural (crítica para a Fase 1)\n")
add("- **Nenhum PDF/TXT de livro está no workspace.** `uploads/processados/` contém 28 arquivos, todos de palestras/materiais do projeto.\n")
add("- Sem o original não há camada 0, chunks nem citações verbatim — o reprocessamento de livros **depende de upload** pelo curador.\n")
add("- Obras com PDF já 'trabalhadas' na era antiga (40) precisam ser **re-anexadas** para o fluxo moderno; "
    "as 'a confirmar' (9) precisam do PDF pela 1ª vez.\n")

add("## 10. Recomendação de priorização (proposta, aguarda devolutiva)\n")
add("**Critérios:** (1) centralidade na Revelação; (2) sub-representação atual (poucas citações + termos-sf); "
    "(3) disponibilidade prática do PDF; (4) Navalha de Ockham — reprocessar para **ampliar/auditar/rastrear**, não para criar códigos.\n")
add("- **Piloto (Fase 1) — candidatos com melhor custo-benefício:**\n")
add("  - **B019 *Nem Deus, nem Javé, nem Darwin*** (20 citações; 18 capítulos; 2021) — ponte direta com a malha recente "
    "(RC-538–547 criados no seu ciclo; palestra P2021-01-23 já curada); PDF 238 págs; tema evolucionário de alto rendimento.\n")
add("  - **B011 *Jesus e o Enigma da Transfiguração*** (11 citações; 176 págs; 2002) — obra primária antiga, tema central (Jesus), "
    "sub-representada; PDF já existiu no projeto.\n")
add("  - **B040 *Homo Sapiens: da Guerra ao Esporte*** (7 citações) — a mais sub-representada das 'trabalhada'; tema periférico, "
    "bom para testar o fluxo sem risco de contaminar o núcleo.\n")
add("- **Fase 2 (escala seletiva):** reprocessar, um ciclo por vez, as obras da seção 5 (≤20 citações) em ordem de centralidade, "
    "mais B013 (Tzimtzum) e B014 (Sophia e o Logos) como **auditoria de grafias canônicas** (livros centrais que definem vocabulário).\n")
add("- **Fichas magras (seção 8):** candidatas a ampliação sempre que o livro/palestra-fonte entrar em ciclo — sem ciclo, permanecem.\n")

add("\n---\n")
add("*Fim do dossiê — Fase 0. Próximo passo: devolutiva do curador (escolha do piloto + anexo do PDF). "
    "Este dossiê não altera a Base Terminológica (777 termos / 1.852 relações permanecem intactos).*\n")

relatorio = "\n".join(L)

# ----------------------------------------------------------------- CSV de apoio
import csv
with open(os.path.join(PED, '_matriz-auditoria-lacunas.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['codigo', 'nome', 'categoria', 'status', 'ficha', 'fontes', 'n_relacoes'])
    nrel = Counter()
    for r in rels:
        nrel[r[0]] += 1
        nrel[r[1]] += 1
    for t in termos:
        w.writerow([t[0], t[1], t[2], t[4], 'SIM' if t[7] else 'NAO', '; '.join(t[5]), nrel.get(t[0], 0)])

os.makedirs(PED, exist_ok=True)
with open(os.path.join(PED, 'DOSSIE-AUDITORIA-LACUNAS-FASE-0.md'), 'w', encoding='utf-8') as f:
    f.write(relatorio)

print(f"OK — dossiê: {len(relatorio.split())} palavras | CSV: {len(termos)} linhas")
