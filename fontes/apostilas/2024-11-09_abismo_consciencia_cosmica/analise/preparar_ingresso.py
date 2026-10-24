#!/usr/bin/env python3
"""Ingresso P2024-11-09 — O Abismo da Consciência Cósmica (re-curadoria)."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parent.parent
UPLOAD = [f for f in Path('/home/user/uploads').iterdir() if '2024-11-09' in f.name][0]
ORIGINAL = ROOT / 'original.txt'
(ROOT / 'analise').mkdir(parents=True, exist_ok=True)
assert ORIGINAL.read_bytes() == UPLOAD.read_bytes(), "original divergente"

raw = ORIGINAL.read_text(encoding='utf-8-sig')
linhas = raw.splitlines()
seps = [i for i, l in enumerate(linhas) if l.startswith('===') and len(l) > 10]
assert len(seps) == 2, f"seps: {seps}"

camada0 = linhas[0].strip() + '\n'
camada1 = '[CAMADA CONTEXTUAL AUSENTE NO ARQUIVO RECEBIDO]\n'
camada2 = '\n'.join(linhas[seps[0]+1:seps[1]]).strip() + '\n'
camada3 = '\n'.join(linhas[seps[1]+1:]).strip() + '\n'

for nome, cont in [('camada-0.txt', camada0), ('camada-1.txt', camada1), ('camada-2.txt', camada2), ('camada-3.txt', camada3)]:
    (ROOT / 'analise' / nome).write_text(cont, encoding='utf-8')

ABREV = {'Dr.': 'Dr§', 'Sr.': 'Sr§', 'Sra.': 'Sra§', 'Prof.': 'Prof§', 'etc.': 'etc§'}
unidades = []
for paragrafo in camada3.splitlines():
    p = paragrafo.strip()
    if not p: continue
    for a, b in ABREV.items(): p = p.replace(a, b)
    p = re.sub(r'([.!?]["”]?)\s+', r'\1\n', p)
    for a, b in ABREV.items(): p = p.replace(b, a)
    for trecho in p.splitlines():
        trecho = trecho.strip()
        if not trecho: continue
        while len(trecho) > 700:
            cortes = [trecho.rfind(z, 250, 620) for z in ['; ', ', ', ': ', ' — ']]
            corte = max(cortes)
            if corte < 250: corte = trecho.rfind(' ', 250, 620)
            unidades.append(trecho[:corte+1].strip())
            trecho = trecho[corte+1:].strip()
        if trecho: unidades.append(trecho)

(ROOT / 'analise' / 'leitura-segmentada.txt').write_text(
    '\n'.join(f'U{i:04d}\t{x}' for i, x in enumerate(unidades, 1)) + '\n', encoding='utf-8')

meta = {
    'sha256_original': hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
    'bytes_original': ORIGINAL.stat().st_size,
    'lines_original': len(linhas),
    'words_original': len(raw.split()),
    'layers': {n: {'words': len(c.split()), 'lines': len(c.splitlines())} for n, c in
               [('camada-0.txt', camada0), ('camada-1.txt', camada1), ('camada-2.txt', camada2), ('camada-3.txt', camada3)]},
    'analytic_units': len(unidades),
    'source_status': 'sequência completa aparente; abertura, exposição e encerramento presentes; sem intervalo/perguntas marcados (confirmar na leitura); camada contextual ausente',
    'nota': 'RE-CURADORIA: base já contém RC-721–RC-727 (7 termos, todos com ficha) com fonte P2024-11-09 — ciclo de auditoria/ampliação, sem consumo de códigos novos salvo decisão do curador',
}
(ROOT / 'analise' / 'METADADOS-INGRESSO.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

palavras = camada3.split()
CHUNK = 2200
n_chunks = (len(palavras) + CHUNK - 1) // CHUNK
for i in range(0, len(palavras), CHUNK):
    (ROOT / f'analise/leitura/chunk-{i//CHUNK+1:02d}.txt').write_text(' '.join(palavras[i:i+CHUNK]) + '\n', encoding='utf-8')

print('=== INGRESSO OK (re-curadoria) ===')
print(f'título: {camada0.strip()}')
print(f'camada-2 (índice): {len(camada2.split())} palavras')
print(f'camada-3 (transcrição): {len(camada3.split())} palavras')
print(f'unidades: {len(unidades)} | chunks: {n_chunks}')
