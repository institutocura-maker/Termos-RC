#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicação F044 — Anel A (fonte) + Anel B (ampliação verbatim).

Regras:
- Códigos de fonte: P2023-12-25-0N (curso lançado no Natal de 2023; sufixo = aula).
- Âncoras verbatim byte-exatas extraídas do traslado (CENSO estrito já validado).
- NÃO cria código novo (Anel C aguarda despacho editorial). NÃO muda relacoes/ (0 arestas).
- Só toca: coluna de FONTES de dados_termos.py + seção ## Ampliação e linha na tabela ## Fontes das fichas.
"""
import re, glob, os, importlib.util

spec = importlib.util.spec_from_file_location("motor", "ferramentas/motor.py")
mot = importlib.util.module_from_spec(spec); spec.loader.exec_module(mot)

AULAS = {
 'P2023-12-25-01': 'Aula 01 — Adolescência e a Juventude de Jesus',
 'P2023-12-25-02': 'Aula 02 — Os Anos de Pregação e a Promessa do Retorno',
 'P2023-12-25-03': 'Aula 03 — Dias Difíceis: Crucificação e Ressurreição',
 'P2023-12-25-04': 'Aula 04 — O Nascimento do Cristianismo',
 'P2023-12-25-05': 'Aula 05 — A Verdadeira Face de Maria Madalena',
}

BASE = {
 'a1':'ciclos/F044_misterios-da-vida-de-jesus/translado/01-Adolescência e a Juventude de Jesus.txt',
 'a2':'ciclos/F044_misterios-da-vida-de-jesus/translado/02-Os Anos de Pregação e a Promessa do Retorno.txt',
 'a3':'ciclos/F044_misterios-da-vida-de-jesus/translado/03-Dias Difíceis- Crucificação e Ressureição.txt',
 'a4':'ciclos/F044_misterios-da-vida-de-jesus/translado/04-O Nascimento do Cristianismo.txt',
 'a5':'ciclos/F044_misterios-da-vida-de-jesus/translado/05-A Verdadeira Face de Maria Madalena.txt',
}

# ------------------------------------------------------------------ dados_termos.py fontes
FONTES_REGISTRO = {
 'RC-072': ['P2023-12-25-01','P2023-12-25-02'],
 'RC-001': ['P2023-12-25-01'], 'RC-009': ['P2023-12-25-01'], 'RC-052': ['P2023-12-25-01'],
 'RC-135': ['P2023-12-25-01'], 'RC-102': ['P2023-12-25-01'], 'RC-037': ['P2023-12-25-01'],
 'RC-104': ['P2023-12-25-01'], 'RC-671': ['P2023-12-25-01'], 'RC-489': ['P2023-12-25-01'],
 'RC-609': ['P2023-12-25-01'], 'RC-329': ['P2023-12-25-01'], 'RC-854': ['P2023-12-25-03'],
 'RC-142': ['P2023-12-25-03'], 'RC-041': ['P2023-12-25-01'], 'RC-096': ['P2023-12-25-04'],
 'RC-003': ['P2023-12-25-03'],
 'RC-565': ['P2023-12-25-02'], 'RC-280': ['P2023-12-25-03'], 'RC-376': ['P2023-12-25-02'],
 'RC-005': ['P2023-12-25-02'], 'RC-752': ['P2023-12-25-01'], 'RC-647': ['P2023-12-25-03'],
 'RC-904': ['P2023-12-25-03'], 'RC-273': ['P2023-12-25-04'], 'RC-193': ['P2023-12-25-01'],
}

# ------------------------------------------------------------------ Anel B ampliações
# (codigo, sigla, aula_key, [verbatim exato], nota)
ANEL_B = [
 ('RC-072','P2023-12-25-01','a1',
   ['Jesus não era um avatar de Javé ou Brahma, era um avatar de Vishnu, emprestado a Brahma',
    'Jesus foi amplamente noticiado. Nenhum outro avatar foi tão noticiado quanto Jesus.'],
   'Aula 01 fixa com precisão o enquadramento de Jesus no panteão: **não** é avatar de Javé/Brahma, mas **avatar de Vishnu emprestado a Brahma**, e sublinha a **notoriedade** ímpar entre os avatares. Corrobora o vínculo RC-072 ↔ RC-135 (Vishnu).'),
 ('RC-072','P2023-12-25-02','a2',
   ['Jesus, depois de muita hesitação, depois de muita cobrança da parte dos seus familiares'],
   'Aula 02 descreve a **hesitação** de Jesus e a pressão familiar/disciplular (João Batista) que o arrasta ao batismo — reforça a recusa da agenda messiânica já registrada na ficha.'),
 ('RC-565','P2023-12-25-02','a2',
   ['o modus operandi que o seu genoma trazia do ser chamado rockmah ou Sophia'],
   'Aula 02 usa a grafia **«rockmah»** (= Hochmah) e o liga explicitamente a **Sophia**; a aula 01 introduz **«em hebraico esse ser se chama Hohkmah»**. Confirma o par Hochmah=Sophia.'),
 ('RC-280','P2023-12-25-03','a3',
   ['Pôncio Pilatos queria logo produzir para ninguém acreditar que Jesus ressuscitou',
    'Jesus o Vivo, o Ressuscitado que através de Madalena, criou uma outra revelação totalmente diferente'],
   'Aula 03 dá a **versão político-jurídica da ressurreição** (suborno do centurião por José de Arimatéia; Pilatos pressionado por Caifás/Anás) e a **revelação pós-ressurreição** intermediada por **Madalena** — expande o eixo Sophia/Ressurreição.'),
 ('RC-376','P2023-12-25-02','a2',
   ['José de Arimatéia'],
   'Aula 02 (contexto das caravanas e do zelo pelo Jesus jovem) confirma o papel de **José de Arimatéia** como tutor/protetor — já registrado na ficha.'),
 ('RC-005','P2023-12-25-02','a2',
   ['Retorno'],
   'O título da própria aula 02 («…e a Promessa do Retorno») e o verbatim da apostila ecoam o **Segundo Advento** — o prometido retorno na condição do Cristo Cósmico.'),
 ('RC-752','P2023-12-25-01','a1',
   ['O homem Jesus estava se recusando a cumprir a agenda de seu próprio espírito'],
   'Aula 01 cunha a expressão **«agenda do seu próprio espírito»** e o messianato hesitado — núcleo da AGENDA ESPIRITUAL (RC-752).'),
 ('RC-647','P2023-12-25-03','a3',
   ['conversando com Judas Dídimo Tomé, que além de apóstolo de Jesus, era também irmão dele'],
   'Aula 03 cita **Judas Dídimo Tomé** (irmão de Jesus) como destinatário da revelação — contexto do Evangelho de Judas/Tomé; reforça RC-647.'),
 ('RC-904','P2023-12-25-03','a3',
   ['conversando com Judas Dídimo Tomé, que além de apóstolo de Jesus, era também irmão dele'],
   'Aula 03 situa a revelação pós-ressurreição a **apóstolos + mulheres** (Tomé, Filipe, Bartolomeu, Madalena) — contexto do Evangelho de Bartolomeu (RC-904).'),
 ('RC-273','P2023-12-25-04','a4',
   ['O Concílio de Nicéia, ferou com Ário, ferrou com o Arianismo e surgiu então o que? Os trinitaristas.'],
   'Aula 04 narra o **Concílio de Niceia** e a imposição do trinitarismo (Ário derrotado) — corrobora e amplia a Falsa Trindade (RC-273).'),
 ('RC-193','P2023-12-25-01','a1',
   ['rebanho humano'],
   'Aula 01/02 usa «rebanho humano» no contexto do messianato e da submissão — corroborado; ver flag de duplicidade RC-193 × RC-941 (não resolvida aqui).'),
]

# ------------------------------------------------------------------ helpers
def get_ficha(cod):
    f = glob.glob(f'termos/{cod}-*.md')
    return f[0] if f else None

def fontes_linha_tpl(cod):
    f = get_ficha(cod); txt = open(f, encoding='utf-8').read()
    m = re.search(r'^## Fontes\s*\n(.*?)(?=^## |\Z)', txt, re.M|re.S)
    if not m: return None
    first = [ln for ln in m.group(1).split('\n') if '|' in ln and '---' not in ln]
    if not first: return '| {sigla} | {titulo} (curso) | — | citação verbatim |'
    h = first[0].strip()
    if 'Localização' in h: return ('| Fonte | Localização | Tipo |', '| {sigla} | {titulo} (palestra) | — | transcrição automatizada; citação |')
    if 'Página' in h: return ('| Obra (sigla) | Título | Página | Tipo |', '| {sigla} | {titulo} (curso) | — | citação verbatim |')
    if 'Capítulo' in h: return ('| Obra (sigla) | Capítulo | Página | Tipo |', '| {sigla} | {titulo} (curso) | — | citação verbatim |')
    return (None, '| {sigla} | {titulo} (curso) | — | citação verbatim |')

def verbatim_ok(ak, q):
    t = open(BASE[ak], encoding='utf-8').read()
    return q.lower() in t.lower()

def aplicar_registro():
    caminho = 'ferramentas/dados_termos.py'
    txt = open(caminho, encoding='utf-8').read()
    cont = {}
    for cod, siglas in sorted(FONTES_REGISTRO.items()):
        for sig in siglas:
            txt, st = mot.inscreve_fonte(txt, cod, sig)
            cont[(cod, sig)] = st
    open(caminho, 'w', encoding='utf-8').write(txt)
    bad = {k:v for k,v in cont.items() if v in ('sem-linha','sem-lista')}
    print(f"[registro] inseriu {sum(1 for v in cont.values() if v=='inseriu')} · "
          f"ja-estava {sum(1 for v in cont.values() if v=='ja-estava')} · problemas {len(bad)}")
    return bad

def aplicar_anel_b():
    n_secoes=0
    for cod, sig, ak, quotes, nota in ANEL_B:
        arq = get_ficha(cod)
        if not arq:
            print(f"  !! {cod} sem ficha"); continue
        for q in quotes:
            if not verbatim_ok(ak, q):
                print(f"  !! {cod}::{sig} verbatim NÃO encontrado em {ak}: {q[:50]!r}")
        corpo = open(arq, encoding='utf-8').read()
        titulo = AULAS.get(sig, sig)
        secao = f"## Ampliação — {sig} ({titulo})\n\n"
        for q in quotes:
            secao += f"- **«{q}»**\n"
        secao += f"- {nota}\n\n"
        m = re.search(r"^## Ampliação — " + re.escape(sig) + r".*?(?=^## |\Z)", corpo, re.M|re.S)
        if m:
            corpo = corpo[:m.start()] + secao + corpo[m.end():]
        else:
            i = corpo.find('\n## Fontes')
            corpo = (corpo[:i] + '\n' + secao + corpo[i:] if i>=0 else corpo.rstrip()+'\n\n'+secao)
        # linha na tabela Fontes
        sig_f = fontes_linha_tpl(cod)
        if sig_f and f"| {sig} |" not in corpo:
            _, ln_tpl = sig_f
            mf = re.search(r'^## Fontes\s*\n(.*?)(?=^## |\Z)', corpo, re.M|re.S)
            if mf:
                i_fontes = corpo.index('## Fontes')
                j = corpo.find('|---|', i_fontes)
                if j >= 0:
                    linha = ln_tpl.format(sigla=sig, titulo=AULAS.get(sig, sig))
                    k = corpo.index('\n', j)
                    corpo = corpo[:k+1] + linha + corpo[k:]
        open(arq,'w',encoding='utf-8').write(corpo)
        assert f"## Ampliação — {sig}" in corpo, f"{cod}: seção não entrou"
        n_secoes += 1
        print(f"  · {cod}: {sig} ampliada ({os.path.relpath(arq)})")
    print(f"[anel B] {n_secoes} seções aplicadas em {len(set(c for c,_,_,_,_ in ANEL_B))} fichas")
    return n_secoes

if __name__ == '__main__':
    print("== APLICANDO F044 ==")
    bad = aplicar_registro()
    if bad: print("!! problemas no registro:", bad)
    aplicar_anel_b()
    print("== FIM ==")
