#!/usr/bin/env python3
"""Preserva e separa as camadas de P2024-11-02; gera unidades analíticas."""
from pathlib import Path
import hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parent.parent
UPLOAD = Path('/home/user/uploads/2024-11-02 - Fantasmas do Passado Mitológico.txt')
ORIGINAL = ROOT / 'original.txt'
ROOT.mkdir(parents=True, exist_ok=True)
(ROOT / 'analise').mkdir(parents=True, exist_ok=True)
if not ORIGINAL.exists():
    shutil.copyfile(UPLOAD, ORIGINAL)
assert ORIGINAL.read_bytes() == UPLOAD.read_bytes()
raw = ORIGINAL.read_text(encoding='utf-8-sig')
linhas = raw.splitlines()
assert linhas[0].startswith('2024-11-02')
assert linhas[67].startswith('===')

camada0 = '\n'.join(linhas[:2]).strip() + '\n'
camada1 = '[CAMADA CONTEXTUAL AUSENTE NO ARQUIVO RECEBIDO]\n'
camada2 = '\n'.join(linhas[3:67]).strip() + '\n'
camada3 = '\n'.join(linhas[69:]).strip() + '\n'
(ROOT/'analise/camada-0.txt').write_text(camada0, encoding='utf-8')
(ROOT/'analise/camada-1.txt').write_text(camada1, encoding='utf-8')
(ROOT/'analise/camada-2.txt').write_text(camada2, encoding='utf-8')
(ROOT/'analise/camada-3.txt').write_text(camada3, encoding='utf-8')

ABREV = {'Dr.':'Dr§','Sr.':'Sr§','Sra.':'Sra§','Prof.':'Prof§','etc.':'etc§'}
unidades=[]
for paragrafo in camada3.splitlines():
    p=paragrafo.strip()
    if not p: continue
    for a,b in ABREV.items(): p=p.replace(a,b)
    p=re.sub(r'([.!?][\"”]?)\s+', r'\1\n', p)
    for a,b in ABREV.items(): p=p.replace(b,a)
    for trecho in p.splitlines():
        trecho=trecho.strip()
        if not trecho: continue
        while len(trecho)>700:
            cortes=[trecho.rfind(z,250,620) for z in ['; ', ', ', ': ', ' — ']]
            corte=max(cortes)
            if corte<250: corte=trecho.rfind(' ',250,620)
            unidades.append(trecho[:corte+1].strip())
            trecho=trecho[corte+1:].strip()
        if trecho: unidades.append(trecho)

seg='\n'.join(f'U{i:04d}\t{x}' for i,x in enumerate(unidades,1))+'\n'
(ROOT/'analise/leitura-segmentada.txt').write_text(seg,encoding='utf-8')
meta={
 'sha256_original':hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
 'bytes_original':ORIGINAL.stat().st_size,
 'lines_original':len(linhas),
 'words_original':len(raw.split()),
 'layers':{
   'camada-0.txt':{'bytes_utf8':len(camada0.encode()),'words':len(camada0.split()),'lines':len(camada0.splitlines())},
   'camada-1.txt':{'bytes_utf8':len(camada1.encode()),'words':len(camada1.split()),'lines':len(camada1.splitlines())},
   'camada-2.txt':{'bytes_utf8':len(camada2.encode()),'words':len(camada2.split()),'lines':len(camada2.splitlines())},
   'camada-3.txt':{'bytes_utf8':len(camada3.encode()),'words':len(camada3.split()),'lines':len(camada3.splitlines())},
 },
 'analytic_units':len(unidades),
 'source_status':'sequência aparentemente completa; abertura, intervalo, perguntas e encerramento presentes',
}
(ROOT/'analise/METADADOS-INGRESSO.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(meta)
