#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F044 — Despacho do Curador 06/09/2026: Anel C + merge de duplicidade + materializações.

1. Merge RC-941 → RC-193 (delete RC-941 do registro; absorver conteúdo GKA na RC-193).
2. Renumera Hipocampo RC-942 → RC-941 (unreferenciado; garante sequência do validador).
3. Novos códigos Anel C: RC-942 Messias · RC-943 Maria Madalena · RC-944 João Batista
   · RC-945 Pedro · RC-946 Pôncio Pilatos / Caifás / Sinédrio (clúster da paixão).
4. Materializa RC-887 Nag Hammadi e RC-862 Essênios (ficha=False -> ficha=True + fichas).
relacoes/ BLINDADO (0 arestas).
"""
import re, os, glob, importlib.util

spec = importlib.util.spec_from_file_location("motor", "ferramentas/motor.py")
mot = importlib.util.module_from_spec(spec); spec.loader.exec_module(mot)

P = "provisório"; C = "candidato"
SER_HUM = ("Seres & Entidades", "1.6 Figuras humanas (históricas/míticas)")
SER_COL = ("Seres & Entidades", "1.2 Coletivos criadores")
TER_GRE = ("Termos Específicos", "8.4 Grego / Latim")
TEC_ESC = ("Tecnologias & Artefatos", "5.4 Escrituras / Objetos documentais")
SER_ANJ = ("Seres & Entidades", "1.4 Anjos / Arcanjos / Querubins")

# categoria na ficha (string de exibição) e subcategoria
CAT = {
 'SER_HUM': ("SERES & ENTIDADES", "1.6 Figuras humanas (históricas/míticas)"),
 'TER_GRE': ("TERMOS ESPECÍFICOS", "8.4 Grego / Latim"),
 'TEC_ESC': ("TECNOLOGIAS & ARTEFATOS", "5.4 Escrituras / Objetos documentais"),
 'SER_ANJ': ("SERES & ENTIDADES", "1.4 Anjos / Arcanjos / Querubins"),
}

AULAS = {
 'P2023-12-25-01': 'Aula 01 — Adolescência e a Juventude de Jesus',
 'P2023-12-25-02': 'Aula 02 — Os Anos de Pregação e a Promessa do Retorno',
 'P2023-12-25-03': 'Aula 03 — Dias Difíceis: Crucificação e Ressurreição',
 'P2023-12-25-04': 'Aula 04 — O Nascimento do Cristianismo',
 'P2023-12-25-05': 'Aula 05 — A Verdadeira Face de Maria Madalena',
}

# ------------------------------------------------------------------ 1. merge + renumeração
def merge_e_renumerar():
    p='ferramentas/dados_termos.py'
    txt=open(p,encoding='utf-8').read()
    lines=txt.split('\n')
    out=[]
    for l in lines:
        # remover RC-941 (Rebanho humano dup)
        if re.match(r'\s*\("RC-941"\s*,\s*"Rebanho humano"', l):
            out.append('    # [F044-MERGE 06-09-2026] RC-941 "Rebanho humano" (F043) DELETADO — '
                       'duplicidade com RC-193; conteúdo absorvido na RC-193. Código imutável porém '
                       'excluso por despacho; ver sistema de notas.')
            continue
        # renumerar RC-942 (Hipocampo) -> RC-941
        if re.match(r'\s*\("RC-942"\s*,\s*"Hipocampo"', l):
            l=l.replace('"RC-942"','"RC-941"',1)
            l=l.replace('# F043-T3 06-09-2026','# [F044-MERGE] renumeração RC-942->941 (vaga aberta pelo delete RC-941); F043-T3',1) if 'F043-T3' in l else l
            l=l + '  # F043-T3 06-09-2026' if 'F043' not in l else l
        out.append(l)
    txt='\n'.join(out)
    open(p,'w',encoding='utf-8').write(txt)
    print("[merge] RC-941 removido; RC-942->RC-941 (Hipocampo)")

# ------------------------------------------------------------------ 2. inserir novos códigos (Anel C)
# (codigo, nome, cat_const, cat_tup, status, fontes, relacionados, ficha)
NOVOS = [
 ('RC-942', 'Messias', 'TER_GRE', TER_GRE, P, ['P2023-12-25-01','P2023-12-25-02','P2023-12-25-03'], 'RC-072; RC-005; RC-752', True),
 ('RC-943', 'Maria Madalena', 'SER_HUM', SER_HUM, P, ['P2023-12-25-03','P2023-12-25-05'], 'RC-072; RC-280; RC-904', True),
 ('RC-944', 'João Batista', 'SER_HUM', SER_HUM, P, ['P2023-12-25-01','P2023-12-25-02'], 'RC-072; RC-862; RC-752', True),
 ('RC-945', 'Pedro (apóstolo)', 'SER_HUM', SER_HUM, P, ['P2023-12-25-03'], 'RC-072; RC-904', True),
 ('RC-946', 'Pôncio Pilatos / Caifás / Sinédrio', 'SER_HUM', SER_HUM, P, ['P2023-12-25-03','P2023-12-25-04'], 'RC-072; RC-280; RC-273', True),
 # materializações
 ('RC-887', 'Nag Hammadi (a biblioteca egípcia onde em 1945 foi encontrada a cópia copta da Hipóstase dos Arcontes — STT «Naghama»; marco físico e histórico da recuperação da revelação gnóstica original)', 'TEC_ESC', TEC_ESC, C, ['P2022-09-17','P2023-12-25-04'], 'RC-770; RC-474; RC-530', True),
 ('RC-862', "Essênios (seita judaica puritana; criadores de João Batista)", 'SER_HUM', SER_HUM, C, ['P2023-02-11','P2023-12-25-01'], 'RC-072', True),
]

def inserir_novos():
    p='ferramentas/dados_termos.py'
    txt=open(p,encoding='utf-8').read()
    # insert before the closing "]\n\n# Validação" of TERMOS list (right after RC-941/Hipocampo line)
    # find the last TERMOS line then the "]" that closes it
    # We locate the line "    (\"RC-941\", \"Hipocampo\"" and insert after it.
    idx = txt.index('    ("RC-941", "Hipocampo"')
    end = txt.index('\n', idx)
    # Build insertion block in matching style
    block = ''
    for cod, nome, catk, catt, st, fontes, rel, ficha in NOVOS:
        fl='['+', '.join('"%s"'%f for f in fontes)+']'
        block += f'    ("{cod}", "{nome}", {catt[0]}, {catt[1]}, {st}, {fl}, "{rel}", {ficha}),\n'
    txt = txt[:end+1] + block + txt[end+1:]
    open(p,'w',encoding='utf-8').write(txt)
    print(f"[novos] {len(NOVOS)} linhas inseridas após RC-941 (Hipocampo)")

if __name__ == '__main__':
    print("== F044 ANEL C + MERGE ==")
    merge_e_renumerar()
    inserir_novos()
    print("== FIM edição registro ==")
