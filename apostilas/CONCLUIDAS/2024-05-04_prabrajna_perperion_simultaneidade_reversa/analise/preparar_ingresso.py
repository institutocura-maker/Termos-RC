#!/usr/bin/env python3
"""Ingresso da VERSÃO REFATORADA de P2024-05-04 (PDF com 5 capturas de tela).

Preserva o PDF byte a byte; extrai o texto (camadas 0-3); gera unidades
analíticas U#### e chunks de leitura. O material é uma reelaboração
estruturada (não a fala literal) — nota registrada no METADADOS.
"""
from pathlib import Path
import hashlib, json, re, shutil
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
UPLOAD = Path('/home/user/uploads/2024-05-04 - Prabrajna em Perpérion_Simultaneidade Reversa-Refatorada.pdf')
ORIGINAL = ROOT / 'original.pdf'
ROOT.mkdir(parents=True, exist_ok=True)
(ROOT / 'analise').mkdir(parents=True, exist_ok=True)
if not ORIGINAL.exists():
    shutil.copyfile(UPLOAD, ORIGINAL)
assert ORIGINAL.read_bytes() == UPLOAD.read_bytes(), "original divergente do upload"

doc = pymupdf.open(str(ORIGINAL))
paginas = []
for i, page in enumerate(doc):
    t = page.get_text()
    paginas.append(f'\n===== [PÁGINA {i+1}] =====\n' + t)
texto = ''.join(paginas)
linhas = texto.splitlines()

# camada-0: título (linha 1)
camada0 = linhas[0].strip() + '\n' if linhas else ''
# camada-1: contextual ausente
camada1 = '[CAMADA CONTEXTUAL AUSENTE — material refatorado; sem dados do evento]\n'
# camada-2: sumário/índice do documento (cabeçalho da palestra + título dos capítulos)
i_sumar = next((i for i, l in enumerate(linhas) if l.strip().startswith('1.') and 'Introdução' in l), 1)
sumario_linhas = [l for l in linhas[:i_sumar] if l.strip()]
camada2 = '\n'.join(sumario_linhas).strip() + '\n'
# camada-3: todo o texto (documento integral — estrutura em capítulos)
camada3 = texto.strip() + '\n'

(ROOT / 'analise/camada-0.txt').write_text(camada0, encoding='utf-8')
(ROOT / 'analise/camada-1.txt').write_text(camada1, encoding='utf-8')
(ROOT / 'analise/camada-2.txt').write_text(camada2, encoding='utf-8')
(ROOT / 'analise/camada-3.txt').write_text(camada3, encoding='utf-8')
# também o texto puro integral p/ leitura
(ROOT / 'analise/leitura-pdf-completo.txt').write_text(camada3, encoding='utf-8')

# ---- unidades analíticas (frases do texto refatorado; mesmo critério) ----
ABREV = {'Dr.': 'Dr§', 'Sr.': 'Sr§', 'Sra.': 'Sra§', 'Prof.': 'Prof§', 'etc.': 'etc§'}
unidades = []
for paragrafo in camada3.splitlines():
    p = paragrafo.strip()
    if not p or p.startswith('====='):
        continue
    for a, b in ABREV.items():
        p = p.replace(a, b)
    p = re.sub(r'([.!?]["”]?)\s+', r'\1\n', p)
    for a, b in ABREV.items():
        p = p.replace(b, a)
    for trecho in p.splitlines():
        trecho = trecho.strip()
        if not trecho:
            continue
        while len(trecho) > 700:
            cortes = [trecho.rfind(z, 250, 620) for z in ['; ', ', ', ': ', ' — ']]
            corte = max(cortes)
            if corte < 250:
                corte = trecho.rfind(' ', 250, 620)
            unidades.append(trecho[:corte + 1].strip())
            trecho = trecho[corte + 1:].strip()
        if trecho:
            unidades.append(trecho)

seg = '\n'.join(f'U{i:04d}\t{x}' for i, x in enumerate(unidades, 1)) + '\n'
(ROOT / 'analise/leitura-segmentada.txt').write_text(seg, encoding='utf-8')

# ---- figuras ----
(ROOT / 'analise/figuras').mkdir(exist_ok=True)
n_fig = 0
for i, page in enumerate(doc):
    for img in page.get_images(full=True):
        xref = img[0]
        pix = pymupdf.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        n_fig += 1
        out = ROOT / f'analise/figuras/figura-{n_fig:02d}-pag{i+1:02d}.png'
        pix.save(str(out))

meta = {
    'sha256_original': hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
    'bytes_original': ORIGINAL.stat().st_size,
    'pages': doc.page_count,
    'words_text': len(camada3.split()),
    'figuras_extraidas': n_fig,
    'layers': {
        'camada-0.txt': {'words': len(camada0.split()), 'lines': len(camada0.splitlines())},
        'camada-1.txt': {'words': len(camada1.split()), 'lines': len(camada1.splitlines())},
        'camada-2.txt': {'words': len(camada2.split()), 'lines': len(camada2.splitlines())},
        'camada-3.txt': {'words': len(camada3.split()), 'lines': len(camada3.splitlines())},
    },
    'analytic_units': len(unidades),
    'source_status': 'VERSÃO REFATORADA (PDF; autor do documento: Edson Cella Mendes) — texto estruturado em 7 capítulos, NÃO é a fala literal; contém 5 capturas de tela (figuras) referenciadas ao texto; sem perguntas de plateia; palestra já processada na base como P2024-05-04 (RC-628–RC-642)',
    'nota': 'RE-CURADORIA DA VERSÃO REFATORADA: base já contém RC-628–RC-642 (15 termos, todos com ficha) — ciclo de auditoria/ampliação/apostila, sem consumo de códigos salvo decisão do curador',
}
(ROOT / 'analise/METADADOS-INGRESSO.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

# ---- chunks (~2200 palavras) ----
palavras = camada3.split()
CHUNK = 2200
n_chunks = (len(palavras) + CHUNK - 1) // CHUNK
(ROOT / 'analise/leitura').mkdir(exist_ok=True)
for i in range(n_chunks):
    trecho = ' '.join(palavras[i * CHUNK:(i + 1) * CHUNK])
    (ROOT / f'analise/leitura/chunk-{i + 1:02d}.txt').write_text(trecho + '\n', encoding='utf-8')

print('=== INGRESSO PDF OK ===')
print(f'título: {camada0.strip()}')
print(f'páginas: {doc.page_count} | palavras: {len(camada3.split())}')
print(f'unidades analíticas: {len(unidades)} | chunks: {n_chunks} | figuras: {n_fig}')
print(f'SHA-256 original: {meta["sha256_original"]}')
