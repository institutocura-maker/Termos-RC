#!/usr/bin/env python3
"""Preserva e separa as camadas de P2025-07-25 (Jesus e a Dinastia das Sophias);
gera unidades analíticas U#### e metadados de ingresso."""
from pathlib import Path
import hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parent.parent
UPLOAD = Path('/home/user/uploads/2026-25-07 - Jesus e a Dinastia das Sophias A Elite dos Arcontes Personificados.txt')
ORIGINAL = ROOT / 'original.txt'
ROOT.mkdir(parents=True, exist_ok=True)
(ROOT / 'analise').mkdir(parents=True, exist_ok=True)
if not ORIGINAL.exists():
    shutil.copyfile(UPLOAD, ORIGINAL)
assert ORIGINAL.read_bytes() == UPLOAD.read_bytes(), "original divergente do upload"

raw = ORIGINAL.read_text(encoding='utf-8-sig')
linhas = raw.splitlines()

# ---- localizar marcos por conteúdo (robusto) ----
i_titulo = 0                      # linha 0 = título
# primeira linha de =====
i_linha_eq = next(i for i, l in enumerate(linhas) if l.startswith('=====') and len(l) > 10)
i_sugestao = next(i for i, l in enumerate(linhas) if 'SUGEST' in l.upper() and 'ÍNDICE' in l.upper())
i_transc = next(i for i, l in enumerate(linhas) if 'TRANSCRI' in l.upper() and 'NA ÍNTEGRA' in l.upper())
assert i_titulo < i_sugestao < i_transc, f"marcos inesperados: {i_titulo}/{i_sugestao}/{i_transc}"

camada0 = linhas[i_titulo].strip() + '\n'
camada1 = '[CAMADA CONTEXTUAL AUSENTE NO ARQUIVO RECEBIDO]\n'
camada2 = '\n'.join(linhas[i_sugestao:i_transc]).strip() + '\n'
camada3 = '\n'.join(linhas[i_transc + 1:]).strip() + '\n'

(ROOT / 'analise/camada-0.txt').write_text(camada0, encoding='utf-8')
(ROOT / 'analise/camada-1.txt').write_text(camada1, encoding='utf-8')
(ROOT / 'analise/camada-2.txt').write_text(camada2, encoding='utf-8')
(ROOT / 'analise/camada-3.txt').write_text(camada3, encoding='utf-8')

# ---- segmentação em unidades analíticas (mesmo critério da P2024-11-02) ----
ABREV = {'Dr.': 'Dr§', 'Sr.': 'Sr§', 'Sra.': 'Sra§', 'Prof.': 'Prof§', 'etc.': 'etc§'}
unidades = []
for paragrafo in camada3.splitlines():
    p = paragrafo.strip()
    if not p:
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

meta = {
    'sha256_original': hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
    'bytes_original': ORIGINAL.stat().st_size,
    'lines_original': len(linhas),
    'words_original': len(raw.split()),
    'layers': {
        'camada-0.txt': {'bytes_utf8': len(camada0.encode()), 'words': len(camada0.split()), 'lines': len(camada0.splitlines())},
        'camada-1.txt': {'bytes_utf8': len(camada1.encode()), 'words': len(camada1.split()), 'lines': len(camada1.splitlines())},
        'camada-2.txt': {'bytes_utf8': len(camada2.encode()), 'words': len(camada2.split()), 'lines': len(camada2.splitlines())},
        'camada-3.txt': {'bytes_utf8': len(camada3.encode()), 'words': len(camada3.split()), 'lines': len(camada3.splitlines())},
    },
    'analytic_units': len(unidades),
    'source_status': 'sequência aparentemente completa; abertura, exposição e perguntas finais presentes; intervalo não marcado',
    'nota_divergencia_data': 'arquivo nomeado 2026-25-07 pelo curador; base cataloga a palestra como P2025-07-25 — divergência registrada [REVISAR]',
}
(ROOT / 'analise/METADADOS-INGRESSO.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

# ---- chunks de leitura (~2200 palavras cada) ----
palavras = camada3.split()
CHUNK = 2200
n_chunks = (len(palavras) + CHUNK - 1) // CHUNK
for i in range(n_chunks):
    trecho = ' '.join(palavras[i * CHUNK:(i + 1) * CHUNK])
    (ROOT / f'analise/leitura/chunk-{i + 1:02d}.txt').write_text(trecho + '\n', encoding='utf-8')

print('=== INGRESSO OK ===')
print(f'título: {camada0.strip()}')
print(f'camada-2 (índice): {len(camada2.split())} palavras')
print(f'camada-3 (transcrição): {len(camada3.split())} palavras')
print(f'unidades analíticas: {len(unidades)}')
print(f'chunks: {n_chunks}')
print(f'SHA-256 original: {meta["sha256_original"]}')
