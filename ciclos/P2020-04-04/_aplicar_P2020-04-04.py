#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicação P2020-04-04 — Anel A (fonte) + Anel B (ampliação verbatim).

Palestra: «Javé, Sophia e Jesus: a Trindade Jamais Percebida» (04/04/2020, Q&A).
Tema afim ao curso F044 («Os Mistérios da Vida de Jesus») — mesma constelação
Javé · Sophia · Jesus, expandida pela mecânica da Trimurti, dos elétrons e da
«vinda de Sofia». Executada na sequência do F044, como palestra autônoma.

Regras (mesmas do F044):
- Código de fonte: P2020-04-04 (único).
- Âncoras verbatim byte-exatas do original.txt (censo estrito).
- NÃO cria código novo; NÃO muda relacoes/ (0 arestas).
- Só toca: coluna FONTES de dados_termos.py + seção ## Ampliação e linha ## Fontes das fichas.
"""
import re, glob, os, importlib.util

spec = importlib.util.spec_from_file_location("motor", "ferramentas/motor.py")
mot = importlib.util.module_from_spec(spec); spec.loader.exec_module(mot)

SIG = 'P2020-04-04'
TITULO = 'Javé, Sophia e Jesus: a Trindade Jamais Percebida (palestra Q&A)'
FONTE_TXT = 'ciclos/P2020-04-04/original.txt'
text = open(FONTE_TXT, encoding='utf-8').read()

# ---------------------------------------------------------------- Anel A: registrar fonte
# Códigos corroborados (censo): os que têm ficha + os sem ficha (ficha=False) que a palestra cita.
FONTES_REGISTRO = [
 'RC-001','RC-009','RC-072','RC-049','RC-692','RC-102','RC-003','RC-604','RC-942','RC-145',
 'RC-061','RC-059','RC-378','RC-097','RC-148','RC-306','RC-091','RC-135','RC-565','RC-366','RC-193',
 'RC-063','RC-060','RC-192','RC-019',
]

# ---------------------------------------------------------------- Anel B: ampliações verbatim
# (codigo, [verbatim exato], nota curativa)
ANEL_B = [
 ('RC-001',
   ['Javé e Jesus são duas faces de uma mesma moeda',
    'que Javé e Jesus são dois seres sustentados pelo mesmo espírito, só que um deles está apartado',
    'Ele é um ser desalmado'],
   'A palestra trava a tese do título no eixo Javé: **Javé é um ser desalmado** (eu apartado do próprio espírito) e **Javé e Jesus são duas faces da mesma moeda** — o mesmo espírito alfa da criação, só que Javé está apartado. Jesus teria sido a via de recompor esse eu desalmado ("o espírito dele que está tentando juntar três em um só").'),
 ('RC-009',
   ['Javé, Sofia e Jesus representam a trindade que a turma nunca percebeu',
    'é muito melhor para Javé que seja Sofia conduzir esse processo',
    'Sofia vai herdar tudo'],
   '**Sophia (RC-009)** é o terceiro vértice da "trindade jamais percebida" (Javé · Sofia · Jesus), a face viva do espírito alfa que herdará o universo vizinho e conduzirá a "vinda". O título ironiza a Santíssima Trindade católica — a que "não existe" — em favor da trindade cósmica de Ellam.'),
 ('RC-072',
   ['a destinação terrível de ser aquele Messias violento',
    'Ele nunca quis assumir aquilo'],
   'Reafirma o núcleo do F044: Jesus **não assumiu** a "destinação terrível de ser aquele Messias violento" e não cumpriu as profecias das escrituras judaicas. A palestra expande o mecanismo interno (o eu que recusa o script) já ancorado na ficha.'),
 ('RC-003',
   ['A reintegração cósmica meio que é refém da vinda de Sofia'],
   'Qualifica a **Reintegração Cósmica** como "meio refém da vinda de Sofia" — a fase clássica (intercâmbio cósmico) só começa oficialmente após a vinda; a extraterrestre já ocorre de forma limitada.'),
 ('RC-049',
   ['disputa dos seres demo pelos campos mórficos'],
   'Situa os **Demos** na tese: a "história do universo" é a disputa dos seres demo pelos campos mórficos das espécies; os demos são especialistas em criar campos mórficos e novas classes de vírus.'),
 ('RC-692',
   ['a revolta dos elétrons é uma autoproteção de Javer'],
   'Amplia a mecânica dos **elétrons**: a "revolta dos elétrons" (rejeição das marcações viciadas) é uma **autoproteção de Javé** para permitir a reconstrução de uma mente universal emergente.'),
 ('RC-604',
   ['Fateamento de consciência'],
   'Fia o conceito de **Fateamento de Consciência** à queda da Trimurti e ao drama de Javé/Sofia/Jesus — três seres fateados de um só espírito alfa.'),
]

# ---------------------------------------------------------------- helpers
def get_ficha(cod):
    f = glob.glob(f'termos/{cod}-*.md')
    return f[0] if f else None

def verbatim_ok(q):
    return q.lower() in text.lower()

def fontes_linha_tpl(cod):
    f = get_ficha(cod); txt = open(f, encoding='utf-8').read()
    m = re.search(r'^## Fontes\s*\n(.*?)(?=^## |\Z)', txt, re.M|re.S)
    if not m: return '| {sigla} | {titulo} (palestra) | — | transcrição; citação |'
    first = [ln for ln in m.group(1).split('\n') if '|' in ln and '---' not in ln]
    if not first: return '| {sigla} | {titulo} (palestra) | — | transcrição; citação |'
    h = first[0].strip()
    if 'Localização' in h: return '| {sigla} | {titulo} (palestra) | — | transcrição; citação |'
    if 'Página' in h or 'Capítulo' in h: return '| {sigla} | {titulo} (palestra) | — | citação |'
    return '| {sigla} | {titulo} (palestra) | — | citação |'

def aplicar_registro():
    caminho = 'ferramentas/dados_termos.py'
    txt = open(caminho, encoding='utf-8').read()
    cont = {}
    for cod in FONTES_REGISTRO:
        txt, st = mot.inscreve_fonte(txt, cod, SIG)
        cont[cod] = st
    open(caminho, 'w', encoding='utf-8').write(txt)
    bad = {k:v for k,v in cont.items() if v in ('sem-linha','sem-lista')}
    print(f"[registro] inseriu {sum(1 for v in cont.values() if v=='inseriu')} · "
          f"ja-estava {sum(1 for v in cont.values() if v=='ja-estava')} · "
          f"problemas {len(bad)} {bad if bad else ''}")
    return bad

def aplicar_anel_b():
    n=0
    for cod, quotes, nota in ANEL_B:
        arq = get_ficha(cod)
        if not arq:
            print(f"  !! {cod} sem ficha"); continue
        for q in quotes:
            if not verbatim_ok(q):
                print(f"  !! {cod} verbatim NÃO encontrado: {q[:50]!r}")
        corpo = open(arq, encoding='utf-8').read()
        secao = f"## Ampliação — {SIG} ({TITULO})\n\n"
        for q in quotes:
            secao += f"- **«{q}»**\n"
        secao += f"- {nota}\n\n"
        m = re.search(r"^## Ampliação — " + re.escape(SIG) + r".*?(?=^## |\Z)", corpo, re.M|re.S)
        if m:
            corpo = corpo[:m.start()] + secao + corpo[m.end():]
        else:
            i = corpo.find('\n## Fontes')
            corpo = (corpo[:i] + '\n' + secao + corpo[i:] if i>=0 else corpo.rstrip()+'\n\n'+secao)
        lin = fontes_linha_tpl(cod)
        if f"| {SIG} |" not in corpo:
            mf = re.search(r'^## Fontes\s*\n(.*?)(?=^## |\Z)', corpo, re.M|re.S)
            if mf:
                i_fontes = corpo.index('## Fontes')
                j = corpo.find('|---|', i_fontes)
                if j >= 0:
                    linha = lin.format(sigla=SIG, titulo=TITULO)
                    k = corpo.index('\n', j)
                    corpo = corpo[:k+1] + linha + corpo[k:]
        open(arq,'w',encoding='utf-8').write(corpo)
        assert f"## Ampliação — {SIG}" in corpo, f"{cod}: seção não entrou"
        n += 1
        print(f"  · {cod}: {SIG} ampliada ({os.path.relpath(arq)})")
    print(f"[anel B] {n} seções em {len(set(c for c,_,_ in ANEL_B))} fichas")
    return n

if __name__ == '__main__':
    print("== APLICANDO P2020-04-04 ==")
    bad = aplicar_registro()
    if bad: print("!! problemas no registro:", bad)
    aplicar_anel_b()
    print("== FIM ==")
