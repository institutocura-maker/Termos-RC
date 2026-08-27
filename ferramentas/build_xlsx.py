#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a planilha consolidada da Base Terminológica RC (base-terminologica.xlsx)
a partir da tabela-mestra ferramentas/dados_termos.py.
Execute a partir de rc-terminologia/ :  python3 ferramentas/build_xlsx.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from dados_termos import TERMOS, RELACOES

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "base-terminologica.xlsx")

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
TITLE_FONT = Font(bold=True, size=16, color="1F3864")
SUB_FONT = Font(italic=True, size=10, color="595959")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
STATUS_FILL = {"candidato": None, "provisório": "FFF2CC", "em análise": "FCE4D6", "verificado": "E2EFDA"}

STATUS_LABEL = {"candidato": "⚪ candidato", "provisório": "🟡 provisório",
                "em análise": "🟠 em análise", "verificado": "🟢 verificado"}

CATS = [
    ("Seres & Entidades", ["1.1 Divindades / Criadores", "1.2 Coletivos criadores", "1.3 Extraterrestres / Raças cósmicas",
                           "1.4 Anjos / Arcanjos / Querubins", "1.5 Decaídos / Exilados / Demônios",
                           "1.6 Figuras humanas (históricas/míticas)", "1.7 Híbridos / Seres de transição", "1.8 Consciências coletivas / Logos"]),
    ("Conceitos Cosmológicos", ["2.1 Cosmogonia / Criação", "2.2 Leis e princípios cósmicos", "2.3 Dimensões / Planos de existência",
                                "2.4 Espiritualidade / Doutrina", "2.5 Propósitos / Destinos", "2.6 Ética / Carma / Compromissos"]),
    ("Lokas & Geografias", ["3.1 Planetas / Sistemas estelares", "3.2 Lokas / Mundos interiores", "3.3 Localidades terrestres",
                            "3.4 Regiões cósmicas / Portais"]),
    ("Processos & Fenômenos", ["4.1 Processos biológicos / genéticos", "4.2 Fenômenos espirituais / mediúnicos",
                               "4.3 Transmigração / Reencarnação", "4.4 Fenômenos físicos / energéticos"]),
    ("Tecnologias & Artefatos", ["5.1 Naves / Tecnologia extraterrestre", "5.2 Artefatos sagrados / Relíquias",
                                 "5.3 Dispositivos / Instrumentos", "5.4 Escrituras / Objetos documentais"]),
    ("Genealogias & Linhagens", ["6.1 Famílias divinas / Celestiais", "6.2 Linhagens humanas", "6.3 Dinastias extraterrestres",
                                 "6.4 Árvores genealógicas"]),
    ("Eventos & Eras", ["7.1 Guerras / Rebeliões / Conflitos", "7.2 Eras / Épocas / Ciclos", "7.3 Profecias / Anúncios",
                        "7.4 Catástrofes / Dilúvios / Quedas", "7.5 Missões / Expedições / Encontros"]),
    ("Termos Específicos", ["8.1 Sânscrito / Hinduísmo", "8.2 Hebraico / Cabala", "8.3 Sumério / Acádio / Babilônio",
                            "8.4 Grego / Latim", "8.5 Outros idiomas / jargão técnico"]),
]

# Lista bibliográfica completa — 50 obras
BIBLIO = [
    ["B001", "O Drama Cósmico de Javé", "—", "Conectar", "2010", "trabalhada",
     "OBRA PRIMÁRIA (1ª ed. 2010; 327 págs PDF). 17 capítulos. Vol. 1 da trilogia dos Dramas de Javé. Realidade Maior; Pai Supremo; Matriz Modeladora; Deus Refém; Grande Dia do Senhor Javé."],
    ["B002", "O Drama Espiritual de Javé", "—", "Conectar", "2011", "trabalhada",
     "OBRA PRIMÁRIA (241 págs PDF; Intro. Atlan 04/01/2009). 19 capítulos. Vol. 2. DNA como projeção holográfica; Filhos das Estrelas; O Mal: Subproduto da Ignorância Espiritual; Prevalece o Amor."],
    ["B003", "Reintegração Cósmica", "Trilogia Queda e Ascensão Espiritual — Livro I (Os Anjos Decaídos)", "Conectar", "1999", "trabalhada",
     "OBRA PRIMÁRIA — TRILOGIA QUEDA E ASCENSÃO ESPIRITUAL (PDF integral 428 págs). Livro I. Quarentena sideral; Anjos Decaídos; Planeta Azul; Portal Cósmico; grafia Jeová."],
    ["B004", "A Sétima Trombeta do Apocalipse", "A volta de Jesus", "Zian", "2005", "a confirmar", "Aguardando PDF."],
    ["B005", "Fator Extraterrestre", "A Busca do Elo Perdido", "Zian", "2004", "trabalhada",
     "OBRA PRIMÁRIA (126 págs PDF; Zian, 2004). 15 capítulos. Fator extraterrestre como elo perdido; Confederações de Mundos; terra de ninguém cósmica; abduções e reparo espiritual."],
    ["B006", "Nos Bastidores da Luz I", "Revelações do contexto cósmico", "Conhecimento / Zian", "2000", "trabalhada",
     "OBRA PRIMÁRIA (118 págs PDF; obra mediúnica ditada por diversos espíritos). Mensagens das reuniões do Grupo Atlan (antiga 'Casa de Lucas', desde 1986), em perguntas e respostas. Espíritos: Enéas, Rochester, Mandreya Ramataiana, Yammes, Francisco, Teodoro, Pe. Fratélio, François. Temas: carma, reforma íntima, violência, mesmice espiritual, mediunidade."],
    ["B007", "Nos Bastidores da Luz 2", "—", "Zian", "2006", "a confirmar", "Aguardando PDF."],
    ["B008", "Nos Bastidores da Luz 3", "Revelações do contexto cósmico", "Conectar", "2018", "a confirmar", "Aguardando PDF."],
    ["B009", "Muito Além do Horizonte", "A ligação entre Kardec, Ramatis e Rochester", "Zian", "2001", "a confirmar", "Aguardando PDF."],
    ["B010", "O Testamento de Jesus", "—", "Zian", "2006", "a confirmar", "Aguardando PDF."],
    ["B011", "Jesus e o Enigma da Transfiguração", "—", "Conectar", "2017", "trabalhada",
     "OBRA PRIMÁRIA — Jan Val Ellam. PDF arquivado na Arca: 176 págs; créditos Conectar Editora, 2017; ISBN 978-85-62411-39-7; CIP 238 p. (1ª menção BIBLIO: Zian, 2002 — reimpressão/edição do mesmo título). 3 partes: Livro de Tiago o Maior (Fator Judas); Livro de João o Batista; Livro de Moisés (Enigma da Transfiguração). Esclarecimento: Atlan, 11/06/2001. Atualização manual Devolutiva B011 O-6 (2026-08-23)."],
    ["B012", "Recado Cósmico", "As Revelações de Jesus", "Zian", "1999/2002", "a confirmar", "Aguardando PDF."],
    ["B013", "Tzimtzum", "O Exílio Forçado de uma Divindade — Revelações Antigas da Cabala", "Conectar", "2020", "trabalhada",
     "OBRA PRIMÁRIA (185 págs PDF; 1ª ed. 2020; ISBN 978-65-86157-09-3). 11 capítulos + anexo. Tzimtzum = implosão do Corpo Mental; Cabala ↔ RC; 270 mundos."],
    ["B014", "Sophia e o Logos Criadores", "—", "Conectar", "2020", "trabalhada",
     "OBRA PRIMÁRIA (272 págs PDF; 1ª ed. 2020; ISBN 978-65-86157-02-4). 18 capítulos. Sophia = avatar indireto de Vishnu; Falsa Trindade; Cápsula do Tempo."],
    ["B015", "O Guardião do Éden", "—", "Conectar", "2017", "trabalhada",
     "OBRA PRIMÁRIA (120 págs PDF). 17 capítulos, narrativa de Zont En Drel 29. Éden como laboratório; genética da confiança; humanização do Criador."],
    ["B016", "O Quarto Logos", "—", "Conectar", "2017", "trabalhada",
     "OBRA PRIMÁRIA (217 págs PDF; 1ª ed. 2017 Natal-RN; ISBN 978-85-62411-37-3; CIP psicografia). 9 capítulos + apêndices. Olm/Codificador de Zion; Liberdade Mental; espiritismo como expressão do 4º Logos."],
    ["B017", "Terra Atlantis I: O Sinal de Land's End", "Livro 1/3", "Conectar", "2016", "trabalhada",
     "OBRA PRIMÁRIA — TRILOGIA TERRA ATLANTIS (185 págs; Gullan Greyl 23-01-2020; Val Eno 2002–03). 13 capítulos. Rebelião de Lúcifer; Ostronomos; Processador Val; Shamb-Aha. CROSS P2023-04-30: a palestra revela o CONTEÚDO da mensagem na garrafa — o código NIDANA (a última versão do código desses três seres; ver RC-154): 'se você encontrou essa mensagem, SAIBA QUE QUEM MANDOU FOI VOCÊ MESMO, só que numa outra condição... A GENTE VAI PERDER A CONSCIÊNCIA — a nossa consciência vai partir do zero' — a mensagem encomendada por Moros/Protogonos/Phanes [RC-009; RC-080]."],
    ["B018", "Terra Atlantis II: A Frota Norte", "Livro 2/3", "Conectar", "2017", "trabalhada",
     "OBRA PRIMÁRIA — TRILOGIA TERRA ATLANTIS (151 págs; Gullan Greyl 28-01-2020). 11 capítulos. Frota Norte; Seres dos Portais; Cidades Voadoras; Hiperbórea."],
    ["B019", "Nem Deus, nem Javé, nem Darwin", "A Evolução Possível", "Conectar", "2021", "trabalhada",
     "OBRA PRIMÁRIA — Jan Val Ellam (238 págs PDF; 1ª ed. 2021; ISBN Papel 978-65-86157-12-3 / Digital 978-65-86157-11-6). 18 capítulos: Evolução Possível para Quem?; Autor e Ator do Próprio Drama; O Acaso, Deus, Criador Complicado; 'Seleção Natural' e 'Darwinismo'; O Jogo das Mutações; Desenvolvimento Cerebral dos Primatas; Teorias da Evolução; O Acaso Inteligente; O que Moveu o Universo; Goswami/Primado da Consciência Quântica/Evolução Criativa; A Evolução Possível até Agora; O Novo Homo sapiens; Molécula-mãe à Singularidade de Kurzweil; Aspectos Obscuros da Evolução; Ex-DNA-lixo; Espelho da Herança Espiritual no Epigenoma; A Criatura Universal; Coconstrutores de Quê? Tese: terceira via (nem darwinismo, nem criacionismo) — evolução conduzida por agentes cósmicos rumo à Criatura Universal. 10 novos termos (RC-538 a RC-547): Consórcio de Mundos, Arquitetos Universais, Molécula-mãe, Evolução Possível, Ex-DNA-lixo, Espelho da Herança Espiritual/Epigenoma, Novo Homo sapiens, Coconstrutores, Primado da Consciência Criativa, Evolução Criativa; 3 fichas novas (Consórcio, Evolução Possível, Espelho do Epigenoma); 13 relações novas; 10 termos existentes reforçados (CFD, Criatura Universal, CFDP, Criaturas-ferramenta, Era da Criatura Universal, Arquiteto Universal, DNA holográfico, Projeto Terra, Tikun). CROSS P2023-04-29: citada de novo ao vivo ('no livro que eu procurei produzir chamado Nem Deus, nem Javé, nem Darwin: a evolução possível... um pouco do que eu estou falando') — a tese de Darwin ('NÃO HAVIA NINGUÉM NO COMANDO') como a premissa da palestra."],
    ["B020", "O Sorriso de Pandora", "—", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA (136 págs; Gullan Greyl 06-02-2020). 14 capítulos. Serpente do Éden; Caos=Brahma=Javé; Opção Inusitada."],
    ["B021", "Tempos Difíceis no Olimpo", "—", "Conectar", "2022", "trabalhada",
     "OBRA PRIMÁRIA (174 págs PDF; 1ª ed. 2022; ISBN 978-65-86157-20-8). 24 capítulos + Diálogo Inusitado. Telos/timé; Eon de Khaos; fechamento dos portais; Pirra/Deucalião. CROSS P2023-04-30: citada para o DECRETO DE ZEUS sobre a procriação [RC-145] — 'PAREM DE CRIAR FILHOS, seja por clonagem, seja por união de gametas, seja por sexualidade' (perante a descendência defeituosa); o contraste: 'ZEUS TEM DESCENDÊNCIA AQUI. KRISHNA NÃO' [quarentena clínica no trecho adjacente]."],
    ["B022", "Inquisição Trimurtiana", "Tempo de Apostasia", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA (174 págs PDF). 10 capítulos. Adhyshprabrajna; Adhyagya; Adhytia; Criação Bipartida; fim da Lila. CROSS P2023-04-15: citada por Ellam como O LIVRO DA DESCONSTITUIÇÃO DE VISHNU ('ele se desconstituiu NOS TERMOS EM QUE EU CONTO NO LIVRO INQUISIÇÃO TRIMURTIANA' — a Trimurti desconstituída em 2018; 'aí Brahma entrou em coma de novo; SÓ TEM SHIVA AÍ ATUANDO') — a 3ª fonte da cronologia 2018-19 (ver P2023-06-03/P2023-04-30). CROSS P2023-04-29 — **A DATA FENOMENAL DE 2016**: 'isso eu escrevi no livro Inquisição Trimurtiana quando eu lancei LÁ EM 2016' (dita ao vivo — a data de publicação registrada; o colapso dos universos e dos níveis espirituais previstos na obra)."],
    ["B023", "O Dharma e as Castas Hindus", "—", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA (123 págs PDF). 9 capítulos. Dharma/castas como sistema demo; Senhores do Dharma = Trimurti; entroncamentos genéticos; Genética Totalitária."],
    ["B024", "A Epopeia dos Agentes da Vida Universal", "—", "Conectar", "2019", "trabalhada",
     "OBRA PRIMÁRIA (162 págs PDF; ISBN 978-85-62411-57-1). 18 capítulos. Agentes da Vida; Mônadas; Gunas; Prabrajna; Eras da Criação; memória quântica dos elétrons. Roteiro de Leitura. CROSS P2023-04-15: citada no Q&A como a obra que 'talvez fale um pouco disso' — A ADIBUTA [STT — [REVISAR]], a expressão da transferência com que o espírito P1 'jogou' Phanes, Sofia e Jesus; a Prabrajna da obra confirmada no mapa das oito pessoas."],
    ["B025", "Caminhos Espirituais", "Trilogia Queda e Ascensão Espiritual — Livro II", "Conectar", "2000", "trabalhada",
     "OBRA PRIMÁRIA — Livro II da trilogia (no PDF B003_trilogia). Jesus o Capelino; Mestres de Capela; Jeová; A Segunda Grande Vinda."],
    ["B026", "Carma e Compromisso", "Trilogia Queda e Ascensão Espiritual — Livro III", "Conectar", "2000", "trabalhada",
     "OBRA PRIMÁRIA — Livro III da trilogia (no PDF B003_trilogia). Projeto Terra; Missão Planeta Azul; decadência atlante; Império Romano; Século XIX."],
    ["B027", "Nos Céus da Grécia", "—", "Conectar", "2019", "amostra recebida", "⚠️ AMOSTRA PARCIAL (14 págs PDF; 2ª ed. 2019; ISBN eBook 978-85-62411-52-6; Esclarecimento em Atlan, 24/11/1992). Contém: capa, sinopse, Esclarecimento, cap. 1 (O Aviso), cap. 2 (O Encontro, parcial) e início do cap. 3 (Sementes do Passado). Diálogo entre Sócrates, Platão e Aristóteles (e Mestre Jesus) sobre cidadania planetária/cósmica, universalismo, reintegração cósmica. Termos do trecho: Sentido Gradualístico das Leis da Evolução Cósmica; Alvorecer de Aquário; reintegração cósmica. Aguardando obra completa."],
    ["B028", "O Sorriso do Mestre", "—", "Conhecimento", "—", "a confirmar", "Aguardando PDF."],
    ["B029", "Inquisição Poética", "(nome civil)", "Zian", "2005", "a confirmar", "Aguardando PDF."],
    ["B030", "A Teia do Tempo", "(nome civil)", "Zian", "2005", "a confirmar", "Aguardando PDF."],
    ["B031", "Painéis Emergentes da Revelação Cósmica", "Um Guia Prático Para Iniciantes (Livro I)", "Nova Egrégora", "2020", "trabalhada",
     "OBRA COMPLEMENTAR (fonte secundária) — A OBRA FUNDADORA DA BASE: o glossário que originou os 777 termos (cabeçalho de dados_termos.py; 145 termos citam B031, 19% da malha). RaquYel Braga (assinatura da autora, Y maiúsculo), aluna avançada de JVE. ISBN 978-65-992214-1-5. Glossário (143 verbetes) + Cronologia (~74 eventos). PDF em poder da base: conversão e-book calibre 6.25 (2024) com marca d'água 'ebook converter DEMO' em todas as págs (extract limpo); CIP 206 p. × PDF 181 p. (divergência da conversão). CIP: Editor/Diagramação Leonardo Kummer; Capa Luciana Lebel; Nova Egrégora, Curitiba. Paratexto: PREFÁCIO AUTORIZADO de Jan Val Ellam (Natal, 07/09/2020 — a 'trilha cerebral', o 'perspectivo') + prefácio da autora (SP, 26/01/2018) + POSFÁCIO (SP, 07/09/2020 — o paralelo dos 687 mil anos × COVID-19; QUARENTENA CLÍNICA). VERIFICAÇÃO DE FIDELIDADE (2026-08-26): 143 verbetes × 135 termos na malha (94%) — a tabela-mestra é fiel à fonte; os 8 restantes são nomes pessoais/variações já fundidos. Cronologia: 13,7 bi anos (× 13,8 do B088 — divergência da escola registrada). Registro: Devolutiva O-6 (ciclo B031, 2026-08-26)."],
    ["B032", "Queda e Ascensão Espiritual (trilogia)", "—", "—", "1996-2000", "identificada", "Roteiro de B024 (equivale a B003/B025/B026)."],
    ["B033", "O Drama Terreno de Javé", "—", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA (219 págs PDF). 18 capítulos. Gestão Cósmica; Cidadão Cósmico; Opção Terra; fonte das Eras da Criação."],
    ["B034", "Cartas a Javé", "—", "Conectar", "2014", "trabalhada", "OBRA PRIMÁRIA de Jan Val Ellam e Mônica Camargo (94 págs PDF; 1ª ed. 2014; ISBN Ebook 978-85-62411-23-6; 110 p. impresso). 16 cartas de Mônica Senise Ferreira de Camargo (escritas enquanto lia os Dramas Espiritual e Terreno de Javé) + Resposta de Javé em 2 partes + 2 posfácios. Tema: o diálogo direto com o Criador; Javé em 1ª pessoa ('sou eu que vivo em vocês!'); o humano como 'terminal nervoso' do criador; DNA como canal de comunicação; a coragem de Javé em se desnudar. OBS: página 1 (capa) e 72 sem texto — extração das demais OK."],
    ["B035", "O Big Data do Criador", "—", "Conectar", "2016 (intro.)", "amostra recebida",
     "⚠️ AMOSTRA PARCIAL (18 págs: Intro + caps. 1–2). Big Data Cósmico; Simbiose Quântica. Aguardando obra completa."],
    ["B036", "As Memórias de Javé", "—", "Conectar", "—", "trabalhada", "OBRA PRIMÁRIA de Jan Val Ellam (111 págs PDF). Crônicas atribuídas a Javé, em 3 partes: I. Crônicas Espontâneas (7); II. Crônicas espontâneas, mas nem tanto (4); III. Crônicas forçadas (2) + Posfácio. Tema: Javé em 1ª pessoa confessando ser um 'Ser-Criador fracassado'; processo de humanização do Criador; linhagem dos escolhidos (Adão, Enoch, Abraão, Jacó); Krishna como 'pretenso Keshava'; Javé sem avatares; advogado de acusação (Ellam); criatura-teste; tempo-limite. Recebido também um RESUMO (4 págs, B036R) com síntese estruturada das figuras e conceitos."],
    ["B037", "Inquisição Filosófica", "—", "Conectar", "—", "identificada", "Roteiro de B024."],
    ["B038", "Frota Norte", "—", "Conectar", "—", "identificada", "Roteiro de B024."],
    ["B039", "Terra Atlantis III: A Era Sapiens", "Livro 3/3", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA — TRILOGIA TERRA ATLANTIS (177 págs; Gullan Greyl 01-02-2020). 12 capítulos. Fim de Atlantis; Len Mion domina Hitler; Calvário de um Inocente. CROSS P2023-04-01: a trilogia citada AO VIVO com os três títulos ('Sinal de Land's End, Frota Norte e A ERA SAPIENS... uma tentativa de romancear fatos extraterrestres, enquadrando na condição de compreensão humana — deve existir muitos erros de minha parte, mas é o possível de ser feito')."],
    ["B040", "Homo Sapiens: da Guerra ao Esporte", "—", "Conectar", "2014", "trabalhada", 'OBRA PRIMÁRIA (82 págs PDF; 1ª ed. 2014; ISBN 978-85-62411-21-2; assinada com NOME CIVIL: Rogério de Almeida Freitas, organizada por Krysamon Cavalcante e Gabriela de Paula Pessôa). Tema: o esporte como evolução da guerra — em vez de matar adversários, a espécie canaliza a agressividade para a competição esportiva; o DNA/molécula-mãe com tendência doentia de desconfiança; a transição do guerreiro ao atleta.'],
    ["B041", "A Rebelião dos Elétrons e o Código de Vida do Criador", "—", "Conectar", "2018", "trabalhada",
     "OBRA PRIMÁRIA (184 págs PDF; 1ª ed. 2018; ISBN Ebook 978-85-62411-53-3; Intro. Atlan 18/10/2018). 22 capítulos. Memória quântica dos elétrons (Charon); dança dos elétrons; rebelião dos elétrons como único padrão modificador do CFDP; CFD de Javé no ser humano; ressonância mórfica; egregores. ⚠️ SÉRIE DE 9: na P2023-09-09 (09/09/2023) Ellam declara: 'eu escrevi um livro chamado A Rebelião dos Elétrons. Na verdade, são NOVE LIVROS sobre esse tema' — este (2018) é o primeiro; os demais não catalogados (sem material). Registro: Devolutiva P2023-09-09, O-5 (2026-08-26)."],
    ["B042", "Crônicas de um Novo Tempo", "Crônicas reflexivas (Etapa II — ~1999–2002)", "Conectar", "—", "trabalhada",
     "OBRA PRIMÁRIA — Jan Val Ellam (228 págs PDF; ISBN 9788562411137). Coletânea de ~35 crônicas reflexivas em 5 partes (Da Vida; Da Filosofia e das Religiões; Do Cosmos e da Espiritualidade; Da História e da Política; De Mim e de Deus), com epígrafes; mesma fase da trilogia Queda e Ascensão (Etapa II). Crônicas-chave: Revelação Cósmica; A Promessa de Jesus; A Volta do Mestre; Reintegração Cósmica; Efeitos da Maré Cósmica; A Chave do Apocalipse — Ano 2001; O Discreto Avatar do Ocidente (João Evangelista); Sintonia e Vibração. Fecha com o Manifesto do PROJETO ORBUM (cidadania planetária, www.orbum.org). 3 novos termos (RC-535 Projeto Orbum, RC-536 Era do Conhecimento e da Espiritualização, RC-537 Maré Cósmica); 2 fichas novas; 6 relações novas; 14 termos existentes reforçados (Reintegração, Segundo Advento, Orbum, Cidadão Cósmico, Fator Extraterrestre, Kardec, Cápsula do Tempo de Sophia/João, Transição Planetária, etc.)."],
    ["B043", "Jesus e o Druida da Montanha", "Aos 20 Anos entre os Celtas", "Conectar", "2009", "trabalhada",
     "OBRA PRIMÁRIA (117 págs PDF; 1ª ed. 2009 ISBN 978-85-62411-00-7; 2ª ed. 2019; romance espírita). 9 capítulos. 20 anos de Jesus entre os celtas; Mordon; Brendiver; Dolman."],
    ["B044", "A Divina Colmeia", "A Trimurti Desencantada", "Conectar", "2019", "trabalhada",
     "OBRA PRIMÁRIA (163 págs PDF; ISBN 978-85-62411-48-9). 15 capítulos + Notas. Colmeia Universal; Abelha-Rainha; Modelo Colmeia."],
    ["B045", "Projeto Talm: a Gênese da Vida Superior", "—", "Conectar", "anunciado", "anunciada", "Obra ANUNCIADA — citada no B014 (cap. 3, nota 2). CROSS P2020-07-04: citada ao vivo como obra que explica a história ('essa história tá em dois livros mais fortemente explicada — o Projeto Talm e o Xadrez Cósmico'; os fenvans/a zona de intercessão)."],
    ["B046", "Xadrez Cósmico (livro)", "—", "Conectar", "anunciado", "anunciada", "Obra ANUNCIADA — citada no B033 (cap. 7) e B014. CROSS P2020-07-04: citada ao vivo junto ao B045 ('essa história tá em dois livros mais fortemente explicada')."],
    ["B047", "Dramas de Shiva (trilogia anunciada)", "—", "Conectar", "anunciado", "anunciada", "Trilogia ANUNCIADA — citada no B014 (posfácio)."],
    ["B048", "Favor Divino", "O Contexto Problemático que envolve a Vida Terrena", "Conectar", "2013", "trabalhada",
     "OBRA PRIMÁRIA (106 págs PDF; 1ª ed. 2013; ISBN 978-85-62411-19-9). 10 capítulos. Favor divino invertido; Democracia do Amor × Teocracia da Doença; lavagem cerebral."],
    ["B049", "Jesus e Nietzsche", "A Fé de Jesus e a Razão de Nietzsche", "Conectar", "2019", "trabalhada",
     "OBRA PRIMÁRIA (224 págs PDF; 1ª ed. 2019; ISBN 978-85-62411-61-8). 14 capítulos. Nietzsche como 'amigo da intenção de Jesus'; crítica aos ídolos; ser humano emancipado."],
    ["B051", "Diagrama Geral de Ligações entre Termos", "(elaborado por alunos do IEEA)", "—", "2020", "trabalhada",
     "OBRA COMPLEMENTAR (material didático de alunos de Jan Val Ellam; original marcado 'não revisado', REVISADO pelo usuário do projeto em 2026-08-13 — coerente). Diagrama de 1 página (PDF vetorial; renderizado como B051_diagrama_geral.png). Ligações: Espiritualidade Superior → Operativa → Laboratorial → Criação Indevida (3 níveis do colapso da Matriz Quântica); ADHYPRABRAJNA → Brahma (caído); ADHYMAVATANA → Vishnu → Mohen So → Sophia → Jesus; ADHYSAVNA → Shiva → Hara/Krishna/Sai Baba; Emissários Humanos (Enoch, Abraão, Moisés, Jesus); Gênero Adhy (147 seres, 5 espécies — Pashvnaj); taxonomia Adhyagia/Adhyatman/Adhydaiva/Adhybutha/Adhyajna."],
["B052", "Homoafetividade", "O Segredo Perdido do Éden", "Conectar", "2016", "trabalhada", "OBRA PRIMÁRIA de Jan Val Ellam (252 págs PDF; 1ª ed. 2016; ISBN 978-85-62411-31-1; 180 p. impresso). 15 capítulos em 4 partes: I. Narrativas Esquecidas (Logo depois do Dilúvio; Na cidade de Tubal; Sobrevivente Impensável; Marcas de um Enigma; O Patriarca; Mistérios de um Passo Esquecido); II. Narrativas Antigas (A Estranha Linha Temporal; Os Magos do Norte; A Babel de Cada Dia; Os Mistérios Dionisíacos); III. Narrativas Tardias (A Sina dos Portadores; A Liberdade e seus Efeitos; Notícias em Alexandria; A Emblemática Roma); IV. Explicação Necessária (O Poder que Habita em Nós). Tema: a força de atração sexual surgiu ANTES da polaridade macho/fêmea (na geração do Olimpo), para unir seres desconfiados; a homoafetividade como resquício dessa força original; narrativa com Heber, Noé, Joctan, Tubal, Faleg (descendentes de Noé); Despina; identidade de gênero; cultura demo. Créditos revelam obras anunciadas (B053-B056)."],
    ["B053", "O Sentido Gradual das Leis Morais", "—", "Conectar", "anunciado", "anunciada", "Obra citada nos créditos de B052 (Homoafetividade). Registrar quando publicada."],
    ["B054", "Sophia e o Pêndulo Cósmico", "—", "Conectar", "anunciado", "anunciada", "Obra citada nos créditos de B052 (Homoafetividade). Registrar quando publicada."],
    ["B055", "O Incompreendido Norte Divino", "Mitologias Celta e Nórdica", "Conectar", "anunciado", "anunciada", "Obra citada nos créditos de B052 (Homoafetividade). Registrar quando publicada."],
    ["B056", "O Desvio de Rota de Pandora e o Quarto Logos Universal", "—", "Conectar", "anunciado", "anunciada", "Obra citada nos créditos de B052 (Homoafetividade). Registrar quando publicada."],
    ["B057", "Os Livros de Yel Luzbel 1: A Revolta do Anjo Decaído", "Trilogia de Jeane Miranda sobre Yel Luzbel (psicografia)", "Nova Egrégora", "2019", "trabalhada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda (aluna de Ellam; médium; prefácio do próprio Jan Val Ellam). 70 págs PDF. Livro 1 da coleção 'Os Livros de Yel Luzbel'. Yel Luzbel, o Primeiro Pesquisador da Família Yel em Capela (planeta Dan), aponta a 'ferida na realidade' e faz três constatações sobre a Obra do Criador; as três questões a Sophia; a Família Mion (Len Mion); o Mestre Codificador de Zion; olimpianos vs capelinos (seres coletivos); marcações de culpa no código genético. Narrativa em 1ª pessoa ditada por Yel Luzbel à autora. PDF em poder da base: edição 2022 'Corrigido e Adaptado por Gullan Greyl' (PT-PT; www.gullangreyl.pt; 15-11-2022); original: Nova Egrégora 2019. Registro: Devolutiva O-6 (ciclo B057, 2026-08-25)."],
    ["B058", "Os Livros de Yel Luzbel 2: O Início da Revolta Capelina", "Trilogia de Jeane Miranda sobre Yel Luzbel (psicografia)", "Nova Egrégora", "—", "trabalhada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda. 76 págs PDF. Livro 2. A Família Mion contata os demais Biocoletivos; Yel Luzbel se demite do cargo de Primeiro Pesquisador e do Processador Yel; audiência na Universidade de Tau Ceti (Grão-mestre e Sábios); suspeita de que Sophia acessava os Processadores Familiares; Yel Luzbel nomeado 'Primeiro em Comando' das famílias biodemos rebeladas — movimento vira um 'exército' contra Sophia e suas Hostes. Nota 'Imagem e Reflexo' de Yel Luzbel; dedicatória de Adilson Reane. SEM prefácio de Ellam neste volume. PDF em poder da base: edição 2022 'Corrigido e Adaptado por Gullan Greyl' (PT-PT; www.gullangreyl.pt; 28-11-2022) — as notas de rodapé desta edição citam fontes externas (Wikipédia; B031 'Painéis Emergentes') = quarentena institucional. Registro: Devolutiva O-6 (ciclo B058, 2026-08-25)."],
    ["B059", "Os Livros de Yel Luzbel 3: Sinais de Guerra em Capela", "Trilogia de Jeane Miranda sobre Yel Luzbel (psicografia)", "Publicações Europa América", "2026", "identificada",
     "OBRA SECUNDÁRIA — 3º volume da trilogia (126 págs; capa comum; ASIN B0GFPWXVSG; Publicações Europa América, 08/01/2026; ~R$ 240,00). SEM PDF — o usuário informou que não há versão online/e-book (somente físico). Sinopse (Amazon): Yel Luzbel isolado e relutante em liderar; ressurge a antiga Família Cromon ('Desistir, jamais!'); Comando Central da Rebelião; Yel Luzbel conduzido a tornar-se o Comandante Supremo da rebelião contra o comando de Sophia. OBS.: a página da Amazon atribui autoria a 'Jan Val Ellam' (erro de catalogação — a autora é Jeane Miranda, com prefácio de Ellam)."],
    ["B060", "Personagens e Terminologias da Revelação Cósmica", "Equivalências entre mitologias (material de aluno de Ellam)", "—", "—", "trabalhada",
     "OBRA SECUNDÁRIA — material de apoio de um aluno dedicado de Jan Val Ellam (com acesso a palestras). Dicionário alfabético de 48 verbetes com equivalências entre mitologias (Grega, Romana, Hindu, Nórdica, Egípcia, Cabala, Celta, Eslava, Africana, Yanomami...). PDF em poder da base: MATERIALIZADO em 2026-08-26 (SHA f49e9529...; 9 págs; autor do documento: Luís Eugênio Paulino de Mendonça, 25/08/2022) — a FONTE que a fundação usou para as cadeias mitológicas (67 termos citam B060; fichas citam 'B060, p. N'; verificação de fidelidade: ~95% digerido). Confirma e amplia cadeias da base: Val Bon/Astréia, Val Anen/Despina, Val Pen/Rochester; Javé = Prabajna/Prajapati/Brajna (Pashvnaj de Perperion) com ~18 nomes mitológicos (Alá, Atom, Caos, Ein Sof, Kether, Ogni, Omama, Pan Ku, Svarog, Ymir, Eru Ilúvatar...); Elm (Moros) e Olm como seres LM de Tempérion — avatar de Elm em Val El (Jan Val Ellam), Kardec, Heber, Kvasir, Boécio, Kapila, Jacó, Vyasa, Metraton, Niccolo Polo...; Vishnu = Mavatina (3º Logos, Satva; avatares: Ahura Mazda, Baphomet, Nommo, Kurma, Matsya, as 7 Amesa Espenta); Shiva = Savna (2º Logos, Tamas; avatares: Sai Babas, Shankaracharya, Rama); Tridevi (Sarasvati, Lakshimi, Parvathi); as 8 TRÍADES comparativas; Anunnaki: Marduk=Ra, Ninmah, Inanna=Danu; Hermes Trismegisto = Ningishzidda/Thoth/Quetzalcóatl/Viracocha; Oannes filho de Ostronomos; Asuras=Titãs; níveis da Espiritualidade (1-4); Khorsis/Mundo dos Tronos; Midgard (Marte+Terra); Bifrost; Moiras/Nornes/Parcas; Bebida dos Deuses; Hyren (antimaterial)/Hyron (material) da druidística (cross B085); a CADEIA DE ROCHESTER (Astartos, Caio Lucilius, Faraó Mernephtah, John Wilmot, Lotário de Rabenau, Parashara). Devolutiva B060 (2026-08-26): +4 RELAÇÕES na tabela-mestra (Astréia=Val Bon; Despina=Val Anen; Kadmon=Val Dimon [o triângulo Pandora fechado]; Maitreya=avatar futuro de Olm [com a divergência 'forma adiágena de Vishnu' anotada na ficha RC-481, sem fusão]) — 1.852→1.856 relações; 6 fichas ampliadas (RC-454/104/001/106/107/102); Rochester SEM código próprio (Navalha — conteúdo no pacote). OBS.: arquivo antigo/desatualizado segundo o usuário; grafias variantes (Perperion × Tempérion; Mavatina × Mavatna; Ealm × Elm; Prabajna × Prabrajna)."],
    ["B061", "Glossário Mestre — Coleção de Apostilas de Palestras de Jan Val Ellam (v3.0)", "Transcrições automatizadas de 5 palestras, não revisadas (material de aluno/curador)", "—", "2024–2026", "minerada",
     "OBRA SECUNDÁRIA — compilação de aluno/curador a partir de TRANSCRIÇÕES AUTOMATIZADAS (STT) NÃO REVISADAS de 5 palestras do Ellam: 2021-12-04 (Os Archeons de Ereon e os Seres Adhy), 2024-09-28 (A Raça Inabalável dos Sethianos Emancipados), 2025-06-14 (A Consciência Humana e a Chave da Decifração Universal), 2026-02-28 (Desafios Planetário), 2026-07-25 (Jesus e a Dinastia das Sophias). ~500 entradas; marcação [verificado]/[em revisão]/[fonte: Raquyel]; seções A-E (Personagens, Conceitos, Livros, Termos próprios, Glossário Raquyel consolidado); camada metadata YAML para RAG (parcial). USO: apenas como MINERAÇÃO DE CANDIDATOS (status ⚪) e pistas — NÃO citar como fonte primária. 33 termos novos cadastrados como candidatos (RC-474 a RC-506): Arcontes, Aurora/Deva, Emá/Ensá, Chequinhá, Belial, Indra, Maitreya, Ialdabaoth, Barbelo, anjos de Arabot-Ráquia, Enki/Enlil, Nefilins, Enoque, Caim, Família Shanlung, membros da Família Yel, 9 Val dos Corpos Perdidos, Dinastia das Sophias, Arabot-Ráquia, Eeron, Impérial, Tempérium, Forno de Awaymaion, Almaior, Conselho dos Cinco, Val Aten, Mavátma, Adyadvaivatma, Adyabradagna, Ekatma + 31 reforços. Cita 'O Funeral da Evidência' (livro real do Ellam — cadastrada como B068). Divergências registradas na seção E.7 (datas Rebelião: 700 mil vs 742 mil)."],
    ["B062", "Ignorância santificada", "Choques de realidade e o Método Dru' Uid", "Publicações Europa América", "2025", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 140 págs; capa comum; ASIN B0H9734VWT; Publicações Europa América, 17/05/2025; ~R$ 250,00. SEM PDF. Sinopse (Amazon): convite a repensar a vida para os 'choques de realidade' dos 'tempos que são chegados'; crítica aos contextos religioso, científico e político; 'Forças Invisíveis'; o medo do 'deus bíblico' vs Deus Amor/Pureza/Perfeição; consequências das 'certezas' para o Eu Espiritual; o 'Método Dru' Uid' na busca da Verdade para o Criador 'caído', refém das criaturas enquanto 'agentes da vida'."],
    ["B063", "Reflexões Quase Filosóficas: Schopenhauer e o Sofrimento do Mundo", "Tributo a Schopenhauer à luz da RC", "Publicações Europa América", "2026", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 150 págs; ASIN B0GF3BCDZY; Publicações Europa América, 05/01/2026; ~R$ 260,00. SEM PDF. Sinopse (Amazon): análise da obra de Schopenhauer conectada à RC; a 'representatividade da Vontade' como fundamento do mundo; a 'Vontade' identificada como o Criador em estado de queda, encontrando na consciência humana um espelho para a própria redenção; crítica às 'verdades sagradas' e ao condicionamento religioso."],
    ["B064", "A ordenação do caos", "Micro-organismos, abduções e o Criador caído", "Publicações Europa América", "2025", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 184 págs; ASIN B0GBQF2XW8; Publicações Europa América, 21/12/2025; ~R$ 250,00. SEM PDF. Sinopse (Amazon): a 'face microbiana' como o 'rosto desfigurado e desagregado' do Criador caído; objetivo das abduções e possessões diagnosticadas como demência; dignidade humana para o 'conserto' da Obra; tendência de vírus e unicelulares portadores de 'códigos-fonte ancestrais defeituosos' (micropartes do corpo implodido de Brahma/Javé) convergirem para o corpo humano. CROSS P2023-04-01: citada ao vivo com VARIAÇÃO DE TÍTULO — 'Além da Ordenação do Caos, a face microbiana do Criador' (01/04/2023): a divergência documentada SEM fusão (o rito B082→B019); o subtítulo 'face microbiana' confere com a sinopse."],
    ["B065", "O abismo da consciência cósmica", "Daath, a queda de Prabrajna e a leitura adulta da Realidade", "Publicações Europa América", "2025", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 150 págs; ASIN B0GFQ56SXR; Publicações Europa América, 17/05/2025; ~R$ 240,00; 5,0/5 (1 avaliação). SEM PDF. Sinopse (Amazon): os processos de Javé e seus Assessores para 'recuperar' a Divindade pré-queda; os cabalistas e 'Daath' como 'Abismo de Luz'; o 'Abismo' em que Prabrajna arremeteu a Consciência Cósmica ao se apartar da própria Alma; a Reintegração Cósmica e a descoberta de que os demais seres não interpretam os desdobramentos da queda como a sagacidade humana."],
    ["B066", "O Manual da Busca Filosófica do Sentido da Vida", "Quatro marcos: autodescoberta, despertar, caminho pessoal, autorrealização", "Publicações Europa América", "2026", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 130 págs; ASIN B0GHPR2KCJ; Publicações Europa América, 19/01/2026; ~R$ 240,00. SEM PDF. Sinopse (Amazon): convite a arquitetar o próprio manual de conduta; ensinamentos dos Grandes Mestres; quatro marcos (autodescoberta, despertar espiritual, construção do caminho pessoal, autorrealização); Filosofia e Ciência entrelaçadas; o 'Tikun' — restabelecimento do equilíbrio da criação e reencontro do criador com sua essência de Divindade Cocriadora."],
    ["B067", "Prodigium: a Necessidade Criativa do Khaos", "O ser humano como prodigium bioquímico do caos", "Publicações Europa América", "2026", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 150 págs; ASIN B0GF3FJCLR; Publicações Europa América, 05/01/2026; ~R$ 250,00. SEM PDF. Sinopse (Amazon): o Universo como 'Holograma gigantesco' sustentado por mente fragmentada; o Khaos e a necessidade desesperada de a vida se reinventar; o humano como 'singularidade bioquímica' (prodigium) emergida do caos; síntese da oxitocina — a 'molécula da moralidade' — do altruísmo e confiança; a 'arte da imaginação' como conquista evolutiva suprema; a 'ferramenta' capaz de curar a consciência fragmentada do Criador."],
    ["B068", "O Funeral da Evidência", "A personificação da Evidência no Paraíso (narrativa em 1ª pessoa)", "Publicações Europa América", "2025", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 310 págs; ASIN B0H96TT3FJ; Publicações Europa América, 17/05/2025; ~R$ 260,00. SEM PDF. Sinopse (Amazon): 'Evidência' — filha de 'Verdade' — personifica o evidente entre os Seres do Paraíso; vê a mãe adoecer diante da indiferença humana pela verdade; por um escrevente humano, relata em 1ª pessoa a travessia que a aproximou do 'Khaos'; revela os Níveis do Paraíso, as Sophias, os Espíritos e a teia de responsabilidades Eternidade×Terra. OBS.: glossário B061 cita capítulo sobre a 'Dinastia das Sophias' (2026-07-25)."],
    ["B069", "Shiva e a Esquecida Origem do Yoga", "A pacificação mental e a linhagem sacerdotal", "Nova Egrégora", "2021", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 158 págs; capa comum; ISBN-13 978-6586157154 (ISBN-10 6586157153); 01/07/2021; ~R$ 70,76; 4,9/5 (11 avaliações). SEM PDF (usuário não possui). Sinopse (Amazon): por que Shiva e alguns avatares elaboraram um método de pacificação mental; como surgiu o Yoga; o 'Eu nervoso'; o êxtase dos yogis e a entrega a deus(es); a 'linhagem sacerdotal' existente na Índia; 'sementes para reflexão'."],
    ["B070", "A Escola da Decifração da Realidade: O Método Dru'uid Ancestral", "Quarto Logos, Colégios Druídicos e a Escola da Decifração", "Nova Egrégora", "2021", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. 138 págs; capa comum; ISBN-13 978-6586157185 (ISBN-10 6586157188); 01/12/2021; ~R$ 67,88; 4,9/5 (11 avaliações). SEM PDF (usuário não possui). Sinopse (Amazon): a 'busca da Verdade'; relação entre o Quarto Logos, os Colégios Druídicos Ancestrais e a nova Escola da Decifração; os 'agentes' da Escola; por que os mundos extraterrestres/extrafísicos se interessam pela Terra; o 'novo humano' e o 'Método Dru'uid Ancestral'."],
    ["B071", "Enciclopédia da Revelação Cósmica — Parte XVII (Índices Remissivos)", "Compilação de IA sobre o corpus RC (não revisada pelo autor)", "—", "2026", "minerada",
     "OBRA TERCIÁRIA — Enciclopédia sobre a RC gerada com IA pelo usuário (que 'parecia bem atualizada'; dados bibliográficos do Ellam MUITO ERRADOS, segundo o usuário). 21 págs PDF. Parte XVII: Cap. 57 Índice Onomástico (divindades/seres/personagens), Cap. 58 Índice Temático (6 categorias), Cap. 61 Concordância de Termos-Chave (61.1 sânscrito; 61.2 línguas clássicas; 61.3 neologismos com 'primeira ocorrência'; 61.4 tabela de equivalências ellâmico×gnosticismo×hinduísmo×cabala×espiritismo×neoplatonismo). USO: apenas como MINERAÇÃO DE CANDIDATOS (status ⚪) e mapa conceitual — NÃO citar como fonte. 10 termos novos cadastrados como candidatos (RC-507 a RC-516): Holodomínio, Decência cósmica, Protagonismo consciencial, Blindagem cósmica, Mêntion, Amnésia espiritual, Espiritualidade Errática, Tikun Cósmico, Acidente cosmogônico, Hibridização genética + 13 relações. ⚠️ ALERTA: obras citadas como 'primeira ocorrência' ('Holodomínios e a Ressurreição do Criador Caído', 'Recontando a História, Vol...') NÃO confirmadas em fontes reais — provável ALUCINAÇÃO da IA; não cadastrar nem citar. Tabela de equivalências (61.4) útil como mapa comparativo."],
    ["B072", "Enciclopédia da Revelação Cósmica (Volumes I–VI, 63 seções)", "Compilação integral de IA sobre o corpus RC (não revisada pelo autor)", "—", "2026", "minerada",
     "OBRA TERCIÁRIA — ENCICLOPÉDIA COMPLETA gerada com IA pelo usuário (682 págs PDF; autor do arquivo: Edson Cella Mendes; Word/2026). 6 volumes, 17 partes, 44 seções + 19 capítulos (63 unidades): I Fundamentos/Biografia; II Conceitos (Cosmogonia, Seres, Terminologia); III Obras/Hermenêutica; IV Temas (Mitologia, Filosofia, Ciência, História oculta); V Recepção/Debates; VI Aparato crítico (Fontes, Índices, Concordância, Cronologia, Mapas). ⚠️ USO: apenas MINERAÇÃO DE CANDIDATOS (status ⚪) e mapa conceitual — NÃO citar como fonte; camada bibliográfica/biográfica DESCARTADA (dados do Ellam muito errados, alerta do usuário; ex.: Seção 4 'Dados biográficos — muita atenção'; catálogo de obras com títulos inventados). 14 termos novos cadastrados como candidatos (RC-517 a RC-530): Protocolo Mental, Genoma Derivado, Herança Cósmica, Infecção mental, Arquivos da Memória Cósmica, Parasitismo energético, Vampirismo consciencial, Coleta de informações, Semente da racionalidade, Demência do Criador, Antimundo, Mergulho, Ressonância límbica, Pistis Sophia + 15 relações. Núcleo conceitual consistente com a base (CFD/CFDP, Biodemos, Prabrajna, Tikun, Blindagem, Mêntion já estavam corretos)."],
    ["B073", "Enciclopédia da Revelação Cósmica — Apêndices A–H", "Quadros sinóticos e catálogo de entidades (IA, não revisado)", "—", "2026", "minerada",
     "OBRA TERCIÁRIA — Apêndices da Enciclopédia RC gerada por IA (7 págs PDF). A: Quadro sinótico RC×Gnosticismo (Nag Hammadi); B: RC×Espiritismo kardecista; C: RC×Tradição védica; D: RC×Ufologia contatista; E: Catálogo descritivo de entidades (Prabrajna, Javé, Vishnu, Shiva, Sophia, Yel Luzbel, Yeshua, Moros, Enki, Enlil, Thoth); F: Protocolo metodológico acadêmico; G: FAQ (IEEA; Decência Cósmica; Ressonância límbica); H: Diretório de recursos (IEEA www.ieea.com.br, YouTube oficial, Editora Zian). ⚠️ USO: apenas mineração/mapa — NÃO citar. 4 termos novos candidatos ⚪ (RC-531 a RC-534): Laboratório Genético Terra, Vacina do Amor, Supercomputador Cósmico (Moros), Usinas geodésicas de Gizé + 5 relações. Quadros sinóticos úteis como referência comparativa."],
    ["B074", "Mentalma I: A Consciência Esclarecida e a Gestão dos Arquivos Mentais", "Série Mentalma — método de yoga mental (2020)", "Conectar", "2020", "trabalhada",
     "OBRA PRIMÁRIA — Jan Val Ellam (227 págs PDF; Conectar, 2020). Volume I da série Mentalma (paralela às RC): define o método 'Mentalma' (yoga mental de emancipação psíquica), os Arquivos Mentais (cada conceito/crença é um arquivo colecionado pelo psiquismo), a 'Chave' dos Arquivos e o 'Circuito do CHA' (Circunstâncias + Herança espiritual + Atitude), os tipos de vontades da psique, os tipos de arquivos, a Disciplina dos 3As (respirar, acalmar, alinhar), a 'primeira versão' do psiquismo e a doença do 'dehatma buddhi', exercícios mentais. 5 novos termos (RC-548 Arquivos Mentais, RC-549 Circuito do CHA, RC-550 Vontade de Progredir, RC-551 Dehatma Buddhi, RC-552 Disciplina dos 3As) + promoção do RC-166 (Mentalma, ficha nova) + 7 relações. Menciona volumes VI e VII planejados (Qualia; Eu como Computador Quântico)."],
    ["B075", "Mentalma II: Gestão Psíquica e Memórias Complexas", "Série Mentalma — aprofundamento (2022)", "Conectar", "2022", "trabalhada",
     "OBRA PRIMÁRIA — Jan Val Ellam (201 págs PDF; Conectar, 1ª ed. 2022; ISBN 978-65-86157-22...). Volume II: aprofundamento do Mentalma I (dehatma buddhi e educação; velhas ideias enraizadas; cérebro físico e ego; Disciplina dos 3As e vivência interior; capacidade de percepção; reforma íntima; contextos da vida — química corporal e vontade pessoal; tipos de psiquismo); Autoconhecimento como primeiro passo para o progresso; memórias complexas. 3 novos termos (RC-553 Eu Profundo, RC-554 Gestão Psíquica e Memórias Complexas, RC-555 Série Mentalma) + 2 relações."],
    ["B076", "Mentalma III: Autoconhecimento e Emancipação", "Série Mentalma — Samkhya de Kapila adaptado (2025)", "Publicações Europa América", "2025", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam (125 págs; ASIN B0GHQ5Y3L3; Publicações Europa América, 17/05/2025; ~R$ 250,00). SEM PDF. Sinopse (Amazon): baseado no Samkhya (Yoga filosófico de Kapila) adaptado aos ocidentais deste tempo de transição; práticas de exercícios respiratórios, meditativos e Pranayamas; despertar espiritual e autorrealização; alerta sobre egrégoras problemáticas 'ladras de Prana'; bhavanga × ilusão da personalidade × Eu Profundo; 'Eu buscador'/'Eu definidor'; despertar da Kundalini; alinhar chakras; Tikun e Vida Espiritual Eterna."],
    ["B077", "Mentalma IV: Consciência Pessoal e Soberania Espiritual", "Série Mentalma — o ego adestrado (2026)", "Publicações Europa América", "2026", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam (286 págs; ASIN B0GHQBY75J; Publicações Europa América, 19/01/2026; ~R$ 250,00). SEM PDF. Sinopse (Amazon): o ego como instrumento de elevação da consciência (desde que adestrado); o medo da morte desvendado; 'colagens psíquicas' (cicatrizes da mente); o respirar como chave de metamorfose espiritual; emancipação → Tikun; 'Eu humano' → 'Eu Organizador'; os 'quatro mundos do ser'; acumulação de Prana; Soberania Espiritual."],
    ["B078", "Mentalma V: Autorrealização", "Série Mentalma — O Yoga do Cotidiano (2026)", "Publicações Europa América", "2026", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam (150 págs; ASIN B0GHQ5Z8Z4; Publicações Europa América, 19/01/2026; ~R$ 250,00). SEM PDF. Sinopse (Amazon): 'O Yoga do Cotidiano'; filosofia prática em diálogo com tradições espirituais, teorias da consciência e cosmologias heterodoxas; método do Mentalma como emancipação psíquica que rompe com a 'primeira versão do psiquismo'; Samkhya de Kapila ao Raja Yoga de Patanjali; crítica existencial de Heidegger; 'mente bicameral' de Julian Jaynes; exercícios mentais, constatações e protocolos de autogestão; 'ciência pessoal da consciência'."],
    ["B079", "Inquisição Espiritual", "Nova Espiritualidade e Roseral do Alto (título anunciado)", "—", "anunciado em 2021", "anunciada",
     "OBRA ANUNCIADA/EM ELABORAÇÃO — citada por Jan Val Ellam na palestra P2021-12-04. O autor afirma que o livro trataria da cidade espiritual Roseral do Alto e dos primeiros elementos da Nova Espiritualidade/Novo Paraíso. Não há confirmação de publicação, editora, ISBN ou título definitivo. Manter como anunciada até fonte bibliográfica independente."],
    ["B080", "Perversa Gratidão: Humanidade Humilhada", "O Livro de Jó e a dignidade subvertida (leitura da RC); o 2º volume da 'Trilogia do Desespero'", "—", "—", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. Cadastrada a partir da citação na palestra P2026-07-25 ('Jesus e a Dinastia das Sophias'): o autor refere 'o penúltimo livro que eu lancei chama-se Perversa Gratidão. É sobre o livro de Jó' — a aposta entre Javé e Belial/Satã, a 'perversa gratidão' (Jó agradecia a Javé a própria desgraça) e a dignidade subvertida. SUBTÍTULO REVELADO (P2023-05-21, 21/05/2023): 'PERVERSA GRATIDÃO: HUMANIDADE HUMILHADA' — e o enquadramento: 'os três próximos livros que em tese eu poderia lançar seriam esse que vai sair agora, o Ignorância Santificada [B091]; o outro seria Perversa Gratidão, dois pontos, Humanidade Humilhada [B080]; e o terceiro, Fim da Inocência Terrária [B092], que seria A TRILOGIA DO DESESPERO' (o 2º volume da trilogia). Sinopse reconstruída da fala; aguardando confirmação bibliográfica independente (editora/ano/ISBN). SEM PDF. Registro: cadastro no ciclo P2026-07-25 + nota P2023-05-21 via edição manual (Devolutiva O-5, 2026-08-26)."],
    ["B081", "Sophia, os Arcontes e a Disputa pela Suzerania Universal", "O papel de Sophia e a rebelião universal dos arcontes (leitura da RC)", "—", "2023 (aprox.)", "identificada",
     "OBRA PRIMÁRIA — Jan Val Ellam. Cadastrada a partir da citação na palestra P2024-07-13 ('Reintegração Cósmica — Tempos de Ruptura'): 'acho que já faz um ano eu lancei um livro chamado Sofia, os Arcontes e a Disputa pela Suzerania Universal' (U0711). CITAÇÃO MAIS ANTIGA: P2023-06-03 (03/06/2023 — a abertura de junho/2023; ordem da Devolutiva O-5, 2026-08-26): 'EU ESCREVI RECENTEMENTE UM LIVRO, Sofia, os Arcontes e a disputa pela SUZERANIA universal [STT: 'sua Ironia Universal'] — e peguei DOIS LIVROS QUE NEM FAZEM PARTE da biblioteca de Nag Hammadi' (o 'recentemente' em jun/2023 refina a janela de publicação para ~2022-2023). 2ª: P2023-06-17 (17/06/2023): idem, na exposição da Deidade. 3ª: P2023-06-24 (24/06/2023 — a antevéspera da palestra-Krishna): 'Quando eu ESCREVI o livro Sofia, os arcontes e a disputa pela SUZERANIA universal [STT: susirania], nós estamos falando de tentativas de dominar a Terra. JESUS NASCEU DEVIDO A ESSA CONJUNTURA GEOPOLÍTICA CÓSMICA, porque a Terra tava sendo disputada em Javé e CHIVA [Shiva]'. Trata do contexto atual dos arcontes (Zeus, Krishna, Apolo etc.) em disputa pela suzerania universal, não aceitando Sophia como suzerano do universo biológico. Sinopse reconstruída da fala; aguardando confirmação bibliográfica independente (editora/ano/ISBN). SEM PDF. Atenção: grafia canônica Sophia. Registro: notas P2023-06-03/P2023-06-17/P2023-06-24 via edição manual (Devolutivas O-5, 2026-08-26)."],
    ["B082", "Nem Deus, nem Javé, nem Darwin: a evolução do cérebro", "Remissão histórica a B019 (título de trabalho citado em P2021-01-23)", "—", "2021", "remissão",
     "REMISSÃO HISTÓRICA a B019 (Nem Deus, nem Javé, nem Darwin: A Evolução Possível). Título de trabalho citado de memória na palestra P2021-01-23 (U1259–U1260: 'Nem Deus, nem Jahé, nem Darwi. Dois pontos, a evolução do cérebro'). Devolutiva B019 O-5 (2026-08-23): não fundir os textos; B082 permanece como rastro da palestra e aponta para o B019 canônico. Sem PDF próprio."],
    ["B083", "Awayen – A Central de Realidades", "O forno replicador de Brahma/Javé e a consciência de Val Tam (obra anunciada)", "—", "anunciada", "anunciada",
     "OBRA ANUNCIADA/EM ELABORAÇÃO — citada no material do curador ART-2025-08-01 ('Fornos Replicadores – Awayen, Awaylengan e Awaymaion', Parte I): as fontes prometem aprofundar em futuras obras a conexão da 'consciência espiritual de Val Tam' com a estação Awayen. Atenção [REVISAR — grafia]: no ART o título aparece como 'Awayem – A Central de Realidades' (vs. forno 'Awayen'); aguardar confirmação bibliográfica independente (editora/ano/ISBN). Autorização de cadastro: Devolutiva do curador O-6 (ciclo ART-2025-08-01). SEM PDF."],
    ["B084", "O Legado Esquecido: o Yoga dos Trimurtianos", "O legado esquecido do Yoga na era dos Trimurtianos (obra anunciada)", "—", "—", "identificada",
     "ANUNCIADA — Jan Val Ellam. Citada em Mentalma I (B074, p. 23): 'também abordo o mesmo tema no livro \"O Legado Esquecido: o Yoga dos Trimurtianos\", ainda por ser publicado' — o tema: o Yoga 'formulado num tempo em que os humanos sequer existiam', codificação de Ioguis contemporâneos de Kapila (a versão humanizada 'daquela luz ancestralmente acesa para outros tipos de seres que viviam tanto na Terra como nas moradas do universo vizinho'). SEM PDF. Registro: Devolutiva O-5 (ciclo B074, 2026-08-25)."],
    ["B085", "Hyren-Hyron: Universos em Colisão", "Universos em colisão — coautoria sob nome civil (Freitas e Kummer) (obra complementar)", "—", "2021", "identificada",
     "OBRA COMPLEMENTAR — coautoria 'Rogério de Almeida Freitas e Kummer' (nome civil do autor + coautora; Kummer = Maria Helena Kummer, revisora dos volumes Conectar), 2021. Citada em Mentalma II (B075, p. 198, seção 'Outras obras como Rogério de Almeida Freitas', data 2021). GÊNESE REVELADA (P2023-06-24, Q&A — a antevéspera da palestra-Krishna): o projeto surgiu de um encontro com 'algumas FIGURAS LÚCIDAS ENTRE OS DEMOS' que disseram 'que eu deveria levar adiante o projeto [STT: Iren Iron/Irém Iron = HYREN-HYRON], que são SEIS LIVROS, é uma SAGA sobre esses dois universos entrando em ROTA DE COLISÃO'; o autor recusou ('eu não queria mais escrever livros que eu ficava me sentindo mal a escrever... fala de dominação... seres que entram na cabeça de um ser humano' — os 'entrantes' dos ufólogos); aconselhado ('por que você não faz sobre a forma de FICÇÃO?'), convidou os co-autores [STT: 'Rodrigo, Léo Keria Cumer' — Keria Cumer = KUMMER; 'Rodrigo' = Rogério?; 'Léo' — [REVISAR]] para 'inventar personagens humanos e enredos'; 'a gente lançou o primeiro livro... mas são seis ou cinco ou seis, será?' — A SAGA DE 5-6 LIVROS (1 publicado; os restantes como obras futuras não publicadas); 'no ano que a gente lançou JÁ TAVA ACONTECENDO esse tipo de invasão e eu só vim perceber quando lancei o livro'. As demais obras do nome civil já mapeadas: B029 (Inquisição Poética), B030 (A Teia do Tempo), B040 (Homo Sapiens: da Guerra ao Esporte). SEM PDF. Registro: Devolutiva O-5 (ciclo B075, 2026-08-25) + nota P2023-06-24 via edição manual (Devolutiva O-5, 2026-08-26) — status 'identificada' + tag 'obra complementar' (coautoria e uso do nome civil)."],
    ["B086", "Anjos Decaídos: O Legado Cósmico da Humanidade", "Obra de Jeane Miranda sobre os anjos decaídos (psicografia)", "—", "2010", "identificada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda. Citada na nota do B057 (p. 14): 'Ver sobre anjos decaídos em \"Anjos Decaídos – O Legado Cósmico da Humanidade Terrestre\" (2010), da mesma autora' — a página 'LIVROS DA AUTORA' (p. 70) grafa o título SEM 'Terrestre' (variante registrada). SEM PDF. Registro: Devolutiva O-5 (ciclo B057, 2026-08-25)."],
    ["B087", "Os Livros da Vida de Pandora 1: Zeus, os Titãs e a Criação da Espécie Humana Terrestre", "Livro 1 da série Pandora de Jeane Miranda (psicografia)", "Nova Egrégora", "2019", "trabalhada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda, COM PREFÁCIO de Jan Val Ellam. Livro 1 da trilogia Pandora (B087–B089): a 'violência mental' imposta por Zeus na 'Assembleia dos Eleitos'; Pandora como 'primeira mulher, parte humana e parte olimpiana'; os titãs Prometeu/Epimeteu e as 'poções'; a caixa com 'algoritmos virais' (aberta por EPIMETEU — divergência × B020); a criação de Pirra; a primeira palavra ('olá!'). Cross: RC-086/145/301/302/303/307/285/287/298/465/727/736/297. PDF em poder da base: ed. 2022 'Corrigido e Adaptado por Gullan Greyl' (PT-PT; www.gullangreyl.pt; 09-02-2022; nota da autora 'Primavera de 2017'; TOC quebrado; epígrafes externas por capítulo; mito clássico com fonte Gabriel Chalita). Registro: cadastro no ciclo B057 (O-5); materialização no ciclo B087 (Devolutiva O-1/O-6, 2026-08-25 — status 'trabalhada')."],
    ["B088", "Os Livros da Vida de Pandora 2: O Coquetel das Poções e o Iminente Ataque do Olimpo", "Livro 2 da série Pandora de Jeane Miranda (psicografia)", "—", "—", "trabalhada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda; SEM prefácio de Ellam (a nota de abertura é o 'Manifesto de Pandora para a Emancipação Humana', assinado pela própria entidade). Livro 2: o 'coquetel das poções' formulado por Prometeu em transe (Pandora liberta da genética de Zeus mantendo poderes e longevidade); os delírios proféticos (nova linhagem de Pirra + o futuro filho de Prometeu — Deucalião); o artefato de Hefesto que mede longevidade (o segredo: Zeus é mortal); Témis, a mãe de Pandora, conselheira de Zeus; a paranóia e o decreto a Atena/Ares; o refúgio entre as montanhas; o gambito de Prometeu no Olimpo; a profecia de Atena ('acabará muito mal'); o recado final de Témis → B089. Cross: RC-086/145/285/287/297/298/301/302/303/307/465/727/736. PDF em poder da base: ed. 2022 'Corrigido e Adaptado por Gullan Greyl' (PT-PT; www.gullangreyl.pt; 28-02-2022) — ⚠️ TÍTULO INTERNO ALTERADO nesta edição: 'As Poções dos Titãs e a Ameaça do Olimpo' (o original, desta BIBLIO e das listas da autora, se mantém); erros de citação de Pessoa preservados ('Álvaro de Camps', 'Fenando'); notas com fonte Wikipédia; epígrafes de Ítalo Calvino. Registro: cadastro no ciclo B057 (O-5); materialização no ciclo B088 (Devolutiva O-1/O-6, 2026-08-25 — status 'trabalhada')."],
    ["B089", "Os Livros da Vida de Pandora 3: Os Anunnaki e a Disputa pela Genética de Pandora", "Livro 3 da série Pandora de Jeane Miranda (psicografia)", "—", "—", "trabalhada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda; SEM prefácio de Ellam — paratexto TRIPLO: CITAÇÃO (Nietzsche) + NOTA (Jeane — com a Trimurti 'decaída') + 'ALGUMAS CONSIDERAÇÕES SOBRE A PANDORA' DE MANA HELENA KUMMER ('baseado nos ensinamentos de Jan Val Ellam' — terceiros; com KADMON [o nome original de Pandora — cross RC-299], 'Falaia Charis', Astreia/Despina, Deucalião, 13,7 bi anos). Livro 3 — FECHA a trilogia (final ABERTO): os Anunnaki (Príncipe Enlil, filho de Anu e da rainha Ki; meio-irmão de Enki) de Nibiru — o planeta cuja camada protetora se deteriora; o ouro em pó para regenerá-la; a busca por escravos para as minas; o interesse na genética de Pandora ('não está definida enquanto espécie'); a poção de camuflagem genética; a estratégia da 'propriedade'; a GUERRA Olimpo×Anunnaki (Ares e Atena; os Anunnaki destruídos; Enlil foge — destino incerto); Témis sonda a mente de Pirra e é expulsa ('o melhor protótipo das duas estirpes'). Cross: RC-086/024/487/486/587/589/303/145/301/302/299/298/285/727/736 + RC-152/051. PDF em poder da base: ed. 2022 'Corrigido e Adaptado por Gullan Greyl' (PT-PT; www.gullangreyl.pt; 10-05-2022; 108 págs — o maior da trilogia; 2 págs sem texto [59, 85]; anomalias preservadas — o trecho corrompido p. 74, a URL corrompida p. 75, 13,7 × 13,8 bi anos). Registro: cadastro no ciclo B057 (O-5); materialização no ciclo B089 (Devolutiva O-1/O-6, 2026-08-25 — status 'trabalhada')."],
    ["B090", "O Senhor Javé: O Criador deste Universo", "Obra de Jeane Miranda sobre Javé (psicografia)", "—", "—", "identificada",
     "OBRA SECUNDÁRIA — PSICOGRAFIA de Jeane Miranda. Listada na página 'LIVROS DA AUTORA' do B057 (p. 70), sem ano. Cross: Javé (RC-001). SEM PDF. Registro: Devolutiva O-5 (ciclo B057, 2026-08-25)."],
    ["B091", "Ignorância Santificada", "O 1º volume da 'Trilogia do Desespero' (obra anunciada como iminente em maio/2023)", "—", "anunciada", "identificada",
     "OBRA ANUNCIADA — Jan Val Ellam. Citada em P2023-05-21 (21/05/2023, 'A Hebdômada de Apolo/O Ultraje Humano'): 'os três próximos livros que em tese eu poderia lançar seriam ESSE QUE VAI SAIR AGORA, o IGNORÂNCIA SANTIFICADA... que seria [com B080 e B092] A TRILOGIA DO DESESPERO. Corra. Mas não tem para onde a gente correr.' — o 1º volume da trilogia; anunciada como IMINENTE em maio/2023 (a publicação efetiva a confirmar bibliograficamente). ⚠️ Pendência de curadoria: verificar se foi publicada (título editorial/editora/ano/ISBN). SEM PDF. Registro: Devolutiva O-5 (ciclo P2023-05-21, 2026-08-26 — edição manual)."],
    ["B092", "Fim da Inocência Terrária", "O 3º volume da 'Trilogia do Desespero' (obra anunciada)", "—", "anunciada", "identificada",
     "OBRA ANUNCIADA — Jan Val Ellam. Citada em P2023-05-21: 'o terceiro, FIM DA INOCÊNCIA TERRÁRIA, que seria [com B091 e B080] A TRILOGIA DO DESESPERO' — o 3º volume; associada na fala a uma palestra homônima ('tem uma outra palestra que eu fiz, ou não fiz, mas o nome dela é O Fim da Inocência Terra[que]'). SEM PDF. Registro: Devolutiva O-5 (ciclo P2023-05-21, 2026-08-26 — edição manual)."],
    ["B093", "Homatividade: O Segredo Proibido do Éden 2", "Obra inédita sobre a homoafetividade na Grécia/Judeia e o encontro com Jesus (anunciada; quarentena clínica)", "—", "anunciada", "identificada",
     "OBRA INÉDITA ANUNCIADA — Jan Val Ellam. Citada em P2023-05-21: 'No livro HOMATIVIDADE, O SEGREDO PROIBIDO DO ÉDEN NÚMERO DOIS, QUE EU NÃO LANCEI AINDA, eu conto a história de um grupo de gregos que vão falar com Jesus sobre a HOMOAFETIVIDADE, que era algo tido como natural na Grécia e na Judeia' — o diálogo registrado: um grego pergunta a Jesus 'nós lá na Grécia já nos livramos disso [da obediência a um deus] há tanto tempo; nós estamos errados e vocês estão certos?'. VARIANTE DO SUBTÍTULO (P2023-05-20, 20/05/2023): 'UMA AFETIVIDADE, O SEGREDO PERDIDO DO ÉDEN' — 'no livro... eu falo um pouco disso' (sobre a divisão dos filhos de Noé); a grafia do subtítulo a confirmar (proibido × perdido; o 'Éden número dois'). ⚠️ QUARENTENA CLÍNICA: o tema segue o protocolo dos ciclos B041/P2025-03-15 (leitura do autor, jamais fato sociológico/biomédico). SEM PDF. Registro: Devolutiva O-5 (ciclo P2023-05-21, 2026-08-26) + nota P2023-05-20 (Devolutiva O-5, 2026-08-26 — edição manual)."],
    ["B094", "A Hora Mais Sombria Que Ainda Virá", "Obra mediúnica inédita atribuída ao espírito de Odin (anunciada; as transmissões de 20 anos)", "—", "anunciada", "identificada",
     "OBRA MEDIÚNICA INÉDITA — atribuída ao ESPÍRITO DE ODIN. Citada em P2023-05-20 (20/05/2023): 'O ODIN FOI MORTO NO RAGNAROK. O ESPÍRITO DE ODIN HÁ UNS 20 ANOS ME TRANSMITE NOTÍCIAS. E eu comecei a tomar nota disso. TEM UNS LIVROS QUE EU COMECEI A ESCREVER, MAS NÃO VOU TERMINAR, chamado... A HORA MAIS SOMBRIA QUE AINDA VIRÁ... que é exatamente Odin em espírito dizendo umas coisas que eu não sei até que ponto aquilo é real... mas é como se o Ragnarok tivesse a sua parte um, MAS TEM UMA OUTRA PARTE que eu não sei do que se trata porque eu não desenvolvi a escrita' — o título exato a confirmar ([REVISAR]; a fala truncada sugere 'Draup...' ou similar antes do subtítulo). ⚠️ QUARENTENA BIOMEDIÚNICA: obra de recepção mediúnica atribuída — registro fenomênico, não ontologia. SEM PDF. Registro: Devolutiva O-5 (ciclo P2023-05-20, 2026-08-26 — edição manual)."],
    ["ART-2025-08-01", "Fornos Replicadores – Awayen, Awaylengan e Awaymaion", "Dossiê do curador sobre os fornos geradores de vida do Projeto Talm", "—", "2025", "curadoria",
     "OBRA COMPLEMENTAR DO CURADOR — Edson Cella Mendes (material de estudo próprio, baseado estritamente em livros e palestras de Jan Val Ellam; NÃO é obra primária do autor). 3 partes: Awayen (Central de Realidades de Brahma/Javé — falha na replicação; Val Tam acoplada), Awaylengan (forno de Shiva — demol/demobiol, radiata emocionais), Awaymaion (forno de Vishnu — biodemo, radiata racionais; Sophia; Olm; cérebro bilatério ~4 bi anos). Utilidade para a KB: resolve STT 'Alamaior' = Awaymaion (RC-499) e 'projeto tal' = Projeto Talm (RC-091); base do nó RC-771 (Fornos Replicadores). Autorização de registro: Devolutiva do curador O-7 (ciclo ART-2025-08-01)."],
    ["ART-2025-08-02", "Projeto TALM", "A semente cósmica e a arquitetura da vida universal (dossiê do curador)", "—", "2025", "curadoria",
     "OBRA COMPLEMENTAR DO CURADOR — Edson Cella Mendes (material de estudo próprio, baseado estritamente em livros e palestras de Jan Val Ellam; NÃO é obra primária do autor). 4 Partes (Origens · Operacionalização · Jornada Humana · Futuro) + Conclusão + Glossário (~20 verbetes). Confirma o acrônimo expandido do TALM ('Transferência do Código-fonte Definidor Pessoal do Criador para o Universo Material'); DNA humano; Rebelião dos Elétrons; reintegração cósmica. Utilidade: amplia RC-091/RC-064/RC-080/RC-081/RC-009/RC-092/RC-001/RC-104; base da Trilogia TALM (com ART-2025-08-01 e ART-2025-08-03). Autorização: Devolutiva O-8 (ciclo Trilogia TALM)."],
    ["ART-2025-08-03", "Dossiê Fenvans – A Gênese Nanotecnológica e o Sacrifício Cósmico", "A engenharia da vida primordial e o sacrifício dos primeiros astronautas (dossiê do curador)", "—", "2025", "curadoria",
     "OBRA COMPLEMENTAR DO CURADOR — Edson Cella Mendes (material de estudo próprio, baseado estritamente em livros e palestras de Jan Val Ellam; NÃO é obra primária do autor). Dossiê técnico em 3 Partes (Engenharia da Vida Primordial · Natureza e Psique do Fenvan · Legado e Esperança). Introduz Morlens, Nanotecnologia Prânica, PEP, Éon das Três Esferas, Ginnungagap e Anã (RC-772 a RC-777); aprofunda os Fenvans (RC-064) e a Mensagem TALM. Autorização: Devolutiva O-8 (ciclo Trilogia TALM)."],
    ["B050", "Guia das Eras Universais (Mapa)", "Linha do Tempo da Revelação Cósmica", "—", "—", "trabalhada",
     "OBRA COMPLEMENTAR (material didático de apoio, produzido pelo FILHO de Jan Val Ellam — Rodrigo de Freitas; não assinada pelo autor; crédito impresso '© Jan Val Ellam'). Infográfico de 1 página A0 (PDF 3436×2450 pt; Adobe Illustrator 26.1, 30/05/2023): a 'Linha do Tempo da Revelação Cósmica' em 4 trilhas verticais com escalas logarítmicas próprias, leitura em serpente. **143 eventos datados** (13,8 bi a.p. ao presente + o marco 'T=0') + as **7 Eras da Criação transcorridas + o período 'Z' (Vishnu/Eros)** — âncoras IDÊNTICAS ao B024 cap. 16 (verificação de fidelidade, 2026-08-26). PDF em poder da base: materializado em 2026-08-26 (SHA c6d6ef73...); extração VETORIAL sem OCR (298 spans); cronologia transcrita em original.txt (resolvida a pendência do 'cronologia-B050.md' antes não versionado). 13,8 bi = a linha cronológica PRIMÁRIA (B024/B033; também B088) — o 13,7 é desvio de fontes complementares (B031/B089). Eventos exclusivos: Ragnarok em Marte (300 mi), Kvasir/Freya, Tirthankaras, Dwarka, Thuata de Dannan, Foz Côa/FOXP2, Demolle, ordinais das famílias biodemo (168332ª Cromon… 249314ª Val), 'Surge Kalil Kadmon' no Toba (74 mil), marcos do presente (1993/2012/2015/'T=0'). Datas aproximadas — usar como apoio. Registro: Devolutiva O-6 (ciclo B050, 2026-08-26)."],
]


def style_header(ws, row, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = BORDER


def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def finish(ws, header_row, widths):
    set_widths(ws, widths)
    ws.freeze_panes = ws.cell(row=header_row + 1, column=1)
    ws.auto_filter.ref = f"A{header_row}:{get_column_letter(ws.max_column)}{max(header_row + 1, ws.max_row)}"


def write_rows(ws, start_row, rows, ncols, status_col=None):
    for r, row in enumerate(rows, start=start_row):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.alignment = WRAP
            cell.border = BORDER
            if status_col and c == status_col and val in STATUS_FILL and STATUS_FILL[val]:
                cell.fill = PatternFill("solid", fgColor=STATUS_FILL[val])


wb = Workbook()

# ------------------------------------------------------------------ Como usar
ws = wb.active
ws.title = "Como usar"
ws.sheet_view.showGridLines = False
ws["B2"] = "Base Terminológica — Revelações Cósmicas (Jan Val Ellam)"
ws["B2"].font = TITLE_FONT
ws["B4"] = ("Planilha consolidada e navegável do projeto. As fichas-fonte vivem em Markdown (pasta termos/ + indice-mestre.md); "
            "esta planilha é uma visão filtrada/consolidada e pode ser regenerada pelo script ferramentas/build_xlsx.py.")
ws["B4"].alignment = WRAP
ws["B4"].font = SUB_FONT
ws.column_dimensions["A"].width = 2
ws.column_dimensions["B"].width = 110

guias = [
    ("1", "Índice Mestre", "Todos os termos (1 linha cada), com status e filtros. É a porta de entrada."),
    ("2", "Fichas", "Ficha completa dos termos centrais (campos da ficha v2)."),
    ("3", "Categorias", "Vocabulário controlado: categorias e subcategorias (códigos 1.1, 7.3 etc.)."),
    ("4", "Bibliografia", "Cadastro das obras do corpus com siglas B###."),
    ("5", "Relações", "Grafo: Termo A — tipo de relação — Termo B (mini-ontologia)."),
    ("6", "Status", "Significado de cada status (candidato, provisório, em análise, verificado)."),
]
r = 6
ws.cell(row=r, column=2, value="Guias desta planilha:").font = Font(bold=True, size=12)
r += 1
for num, nome, desc in guias:
    ws.cell(row=r, column=2, value=f"[{num}] {nome} — {desc}").font = SUB_FONT
    r += 1

# ------------------------------------------------------------------ Índice Mestre
ws = wb.create_sheet("Índice Mestre")
headers = ["Código", "Termo", "Categoria", "Subcategoria", "Status", "Fontes (siglas)", "Termos relacionados", "Ficha completa?", "Última atualização"]
ws.append(headers)
style_header(ws, 1, len(headers))

indice = []
for cod, nome, cat, sub, status, fontes, rel, ficha in TERMOS:
    indice.append([cod, nome, cat, sub, STATUS_LABEL[status], ", ".join(fontes) if fontes else "—",
                   rel, "sim" if ficha else "não", "2026-08-14"])
write_rows(ws, 2, indice, len(headers), status_col=5)
finish(ws, 1, [10, 42, 24, 34, 16, 14, 30, 13, 16])

dv_status = DataValidation(type="list", formula1='"⚪ candidato,🟡 provisório,🟠 em análise,🟢 verificado"', allow_blank=True)
ws.add_data_validation(dv_status)
dv_status.add("E2:E600")

# ------------------------------------------------------------------ Fichas (resumo)
ws = wb.create_sheet("Fichas")
headers = ["Código", "Termo", "Categoria", "Subcategoria", "Status", "Definição sintética",
           "Contexto / Origem", "Etimologia / Grafias", "Fontes (obra, capítulo, página)",
           "Citações-chave", "Termos relacionados", "Seres associados", "Observações", "Última atualização"]
ws.append(headers)
style_header(ws, 1, len(headers))
fichas = []
for cod, nome, cat, sub, status, fontes, rel, ficha in TERMOS:
    if not ficha:
        continue
    fichas.append([cod, nome, cat, sub, STATUS_LABEL[status],
                   "(ver ficha completa em termos/)", "(ver ficha completa em termos/)",
                   "(ver ficha completa em termos/)", ", ".join(fontes), "(ver ficha completa em termos/)",
                   rel, "—", "(ver ficha completa em termos/)", "2026-08-14"])
write_rows(ws, 2, fichas, len(headers), status_col=5)
finish(ws, 1, [10, 34, 24, 30, 16, 30, 30, 30, 20, 30, 30, 20, 30, 15])

dv_cat = DataValidation(type="list",
                        formula1='"Seres & Entidades,Conceitos Cosmológicos,Lokas & Geografias,Processos & Fenômenos,Tecnologias & Artefatos,Genealogias & Linhagens,Eventos & Eras,Termos Específicos"',
                        allow_blank=True)
ws.add_data_validation(dv_cat)
dv_cat.add("C2:C600")

# ------------------------------------------------------------------ Categorias
ws = wb.create_sheet("Categorias")
headers = ["Código", "Categoria", "Subcategoria"]
ws.append(headers)
style_header(ws, 1, len(headers))
cat_rows = []
for cat, subs in CATS:
    for sub in subs:
        cat_rows.append([sub.split(" ")[0], cat, sub])
write_rows(ws, 2, cat_rows, len(headers))
finish(ws, 1, [10, 26, 44])

# ------------------------------------------------------------------ Bibliografia
ws = wb.create_sheet("Bibliografia")
headers = ["Código", "Título", "Subtítulo", "Editora", "Ano", "Status", "Observações"]
ws.append(headers)
style_header(ws, 1, len(headers))
write_rows(ws, 2, BIBLIO, len(headers))
finish(ws, 1, [10, 40, 44, 22, 10, 16, 70])

# ------------------------------------------------------------------ Relações
ws = wb.create_sheet("Relações")
headers = ["Termo A (código)", "Termo A (nome)", "Tipo de relação", "Termo B (código)", "Termo B (nome)", "Obra-fonte"]
ws.append(headers)
style_header(ws, 1, len(headers))
nome = {t[0]: t[1] for t in TERMOS}
rel_rows = []
for a, tipo, b, obra in RELACOES:
    rel_rows.append([a, nome[a], tipo, b, nome[b], obra])
write_rows(ws, 2, rel_rows, len(headers))
finish(ws, 1, [16, 34, 18, 16, 40, 12])

# ------------------------------------------------------------------ Status
ws = wb.create_sheet("Status")
headers = ["Status", "Significado", "Quando aplicar"]
ws.append(headers)
style_header(ws, 1, len(headers))
status_rows = [
    ["⚪ candidato", "Termo identificado, sem ficha ainda", "Só aparece no Índice Mestre"],
    ["🟡 provisório", "Definição documentada em fonte publicada, mas não verificada em obras primárias de Ellam", "Após extração de glossário/PDF"],
    ["🟠 em análise", "Ficha redigida, aguardando revisão e referências página a página", "Após cruzamento com obras primárias"],
    ["🟢 verificado", "Revisado e referenciado (obra + capítulo/página)", "Pode ser citado como consolidado"],
]
write_rows(ws, 2, status_rows, len(headers))
finish(ws, 1, [16, 70, 55])

wb.save(OUT)
print(f"OK -> {OUT} ({len(wb.sheetnames)} abas)")
print(f"Índice: {len(indice)} termos | Fichas-resumo: {len(fichas)} | Relações: {len(rel_rows)} | Obras: {len(BIBLIO)}")
