import os, re, shutil, hashlib, subprocess, json

SRC = 'uploads_recepcao/2022-03-26 A Rebelião de Lúcifer e a Depressão Mental dos Seres.txt'
SLUG = '2022-03-26_a_rebeliao_de_lucifer_e_a_depressao_mental_dos_seres'
CICLO = f'apostilas/{SLUG}'
os.makedirs(f'{CICLO}/analise/leitura', exist_ok=True)

# ---------- 1. ingresso byte a byte ----------
dst = f'{CICLO}/original.txt'
shutil.copyfile(SRC, dst)
cmp = subprocess.run(['cmp', SRC, dst], capture_output=True, text=True)
b = open(dst, 'rb').read()
sha = hashlib.sha256(b).hexdigest()
t = b.decode('utf-8')
lines = t.split('\n')
lines = [l.rstrip('\r') for l in lines]
assert cmp.returncode == 0 and len(b) == os.path.getsize(SRC)

# ---------- 2. mapa de linhas lógicas (Uxxxx) e segmentação ----------
# U0001 é o cabeçalho-título do arquivo; U0002 a linha vazia; U0003.. a fala.
n = len(lines)
# offsets contados no texto decodificado, separando por \r\n (2 chars por quebra) para bater com o bruto
segs = t.split('\r\n')
assert len(segs) == n
offsets, acc = [], 0
for s in segs:
    offsets.append(acc)
    acc += len(s) + 2

def tag(i):
    return f'U{i+1:04d}'

# ---------- 3. leitura-segmentada.txt (mapa endereçado de cada linha) ----------
out = [f'# LEITURA SEGMENTADA — P2022-03-26 · transcrição bruta endereçada por linha lógica',
       f'arquivo: `original.txt` · {len(b)} bytes · {len(t)} chars · SHA-256 `{sha}`',
       f'marcador ⟦Uxxxx⟧ = número da linha lógica; offset = posição em caracteres do texto decodificado\n']
for i, s in enumerate(segs):
    if not s.strip():
        out.append(f'### {tag(i)} · offset {offsets[i]}–{offsets[i]+len(s)} · {len(s)} chars · LINHA VAZIA\n')
        continue
    out.append(f'### {tag(i)} · offset {offsets[i]}–{offsets[i]+len(s)} · {len(s)} chars\n{s}\n')
open(f'{CICLO}/analise/leitura-segmentada.txt', 'w', encoding='utf-8').write('\n'.join(out))

# ---------- 4. chunks de ~16.000 chars (corte em fim de linha lógica) ----------
CHUNK = 16000
chunks, cur, curlen, first = [], [], 0, 0
for i, s in enumerate(segs):
    body = f'⟦{tag(i)}⟧ {s}' if s.strip() else f'⟦{tag(i)}⟧'
    if curlen + len(body) > CHUNK and cur:
        chunks.append(cur)
        cur, curlen, first = [], 0, i
    cur.append(body)
    curlen += len(body) + 1
if cur:
    chunks.append(cur)
for k, c in enumerate(chunks, 1):
    open(f'{CICLO}/analise/leitura/chunk-{k:02d}.txt', 'w', encoding='utf-8').write('\n'.join(c) + '\n')

# ---------- 5. medidas de estrutura e vocabulário ----------
fala = [s for s in segs[1:] if s.strip()]
chars_fala = sum(len(s) for s in fala)
periodos = sum(len(re.findall(r'[.!?]', s)) for s in fala)
palavras = sum(len(s.split()) for s in fala)
big = max(range(len(segs)), key=lambda i: len(segs[i]))
termos = ['Rebelião', 'rebelião', 'Lúcifer', 'Luzbel', 'depressão', 'Depressão', 'Javé', 'Jah', 'Sofia', 'Sophia',
          'biodemo', 'biodevo', 'espécie', 'processador', 'vírus', 'isolamento', 'Antares', 'Capela', 'família',
          'Mentalma', 'mentalma', 'fatiamento', ' kolobos', 'anunnaki', 'Nibiru', 'Enki', 'pandemia', 'coronavírus',
          'mediano', 'médiun', 'espírito', 'psique', 'psiquiatr', 'remédio', 'medicação', 'sofrimento', 'obsessão',
          'desdobramento', 'arconte', 'Archon', 'demônio', 'demoníaco', 'inferno', 'alma', 'reencarnac']
marks = {}
low = t
for w in termos:
    c = len(re.findall(re.escape(w), low))
    if c:
        marks[w] = c
nums = {}
for m in re.finditer(r'\b\d{1,3}(?:[.,]\d{3})*\b|\b\d+\s?(?:mil|milhão|milhões|bilhão|bilhões)\b', t):
    nums[m.group(0)] = nums.get(m.group(0), 0) + 1
top_nums = sorted(nums.items(), key=lambda kv: -kv[1])[:28]

meta = {
  'schema': 'ingresso-palestra-v1',
  'recebido_em': '2026-08-29',
  'como_chegou': ('commit `a02f12b` «Add files via upload» na branch arena/01a04969-termos-rc (upload do Curador '
                  'pela interface do GitHub), **em cima** do commit do BLOCO B do ciclo anterior; o workspace tinha '
                  'sido re-materializado no commit-base da sessão e o arquivo **não** estava no disco — o ponteiro '
                  'foi adiantado por fast-forward sobre `a02f12b` e o bruto veio com ele'),
  'arquivo_recebido': SRC,
  'slug': SLUG,
  'codigo_fonte': 'P2022-03-26',
  'tema_nomeado': ('A Rebelião de Lúcifer e a Depressão Mental dos Seres (título indicado pelo Curador ao nomear o '
                   'ciclo, 28-29/08/2026 — sem tema novo aberto: a palestra É o tema)'),
  'bytes': len(b), 'sha256_original': sha,
  'cmp_byte_a_byte': 'identidade verificada por `cmp` contra o arquivo de `uploads_recepcao/`',
  'chars_total': len(t), 'chars_fala': chars_fala,
  'linhas_fisicas': len(lines), 'crlf': t.count('\r\n'), 'linhas_logicas_com_texto': len(fala) + 1,
  'megabloco': tag(big), 'megabloco_chars': len(segs[big]),
  'periodos': periodos, 'palavras': palavras,
  'data_da_fala': 'sábado, 26/03/2022 (calendário, não memória)',
  'contexto_de_data': ('a 8 dias do aniversário de P2020-04-18/25 (o cluster de abril de 2020) e no intervalo '
                       '2021→2023 que a Base hoje cobre com lacunas; não há palestra de 2022 na Base além de '
                       'P2022-09-24 e P2022-12-17'),
  'chunks_de_leitura': len(chunks),
  'marcas_no_bruto': marks,
  'cifras_mais_frequentes': dict(top_nums),
  'estado': ('CICLO ABERTO — ETAPA 1 EM CURSO (leitura integral + camadas 0–3 + LEITURA-1 + dossiê + auditor '
             'verbatim A/B). ⚠️ AGUARDA DEVOLUTIVA DO CURADOR; 0 alterações na malha.'),
  'gerado_em': subprocess.run(['date', '+%Y-%m-%d %H:%M'], capture_output=True, text=True).stdout.strip(),
  'observacao': 'arquivo NÃO corrigido: aspas retas, números trocados e grafias instáveis são do STT e ficam como estão',
}
open(f'{CICLO}/analise/METADADOS-INGRESSO.json', 'w', encoding='utf-8').write(
    json.dumps(meta, ensure_ascii=False, indent=2) + '\n')

print(f'bytes={len(b)} chars={len(t)} sha={sha[:12]}… linhas={n} fala_linhas={len(fala)}')
print(f'chars_fala={chars_fala} palavras={palavras} periodos={periodos}')
print(f'megabloco={tag(big)} com {len(segs[big])} chars ({100*len(segs[big])/chars_fala:.1f}% da fala)')
print(f'chunks={len(chunks)}')
print('comprimentos das linhas lógicas:', [len(s) for s in segs][:16])
