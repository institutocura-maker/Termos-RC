#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TABELA-MESTRA DA BASE TERMINOLÓGICA RC — fonte única de verdade.

Termos extraídos do Glossário de Termos da Revelação Cósmica (B031 - Raquyel Braga,
"Painéis Emergentes da Revelação Cósmica", Editora Nova Egrégora, 2020) + termos
pré-existentes do projeto (RC-001..RC-010).

Estrutura: (codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha)
- status: candidato | provisório | em análise | verificado
- fontes: siglas B### (lista)
- relacionados: códigos RC-### referenciados
- ficha: True se existe ficha detalhada em termos/

Regras:
- Códigos são IMUTÁVEIS (não reutilizar).
- Nomes podem mudar; a grafia preferida é a deste arquivo.
"""

# ---------------------------------------------------------------- SERES & ENTIDADES
SER_DIV = ("Seres & Entidades", "1.1 Divindades / Criadores")
SER_COL = ("Seres & Entidades", "1.2 Coletivos criadores")
SER_EXT = ("Seres & Entidades", "1.3 Extraterrestres / Raças cósmicas")
SER_ANJ = ("Seres & Entidades", "1.4 Anjos / Arcanjos / Querubins")
SER_DEC = ("Seres & Entidades", "1.5 Decaídos / Exilados / Demônios")
SER_HUM = ("Seres & Entidades", "1.6 Figuras humanas (históricas/míticas)")
SER_HIB = ("Seres & Entidades", "1.7 Híbridos / Seres de transição")
SER_LOG = ("Seres & Entidades", "1.8 Consciências coletivas / Logos")

# ---------------------------------------------------------------- CONCEITOS COSMOLÓGICOS
COS_COG = ("Conceitos Cosmológicos", "2.1 Cosmogonia / Criação")
COS_LEI = ("Conceitos Cosmológicos", "2.2 Leis e princípios cósmicos")
COS_DIM = ("Conceitos Cosmológicos", "2.3 Dimensões / Planos de existência")
COS_ESP = ("Conceitos Cosmológicos", "2.4 Espiritualidade / Doutrina")
COS_PRO = ("Conceitos Cosmológicos", "2.5 Propósitos / Destinos")
COS_ETI = ("Conceitos Cosmológicos", "2.6 Ética / Carma / Compromissos")

# ---------------------------------------------------------------- LOKAS & GEOGRAFIAS
LOK_PLA = ("Lokas & Geografias", "3.1 Planetas / Sistemas estelares")
LOK_MUN = ("Lokas & Geografias", "3.2 Lokas / Mundos interiores")
LOK_TER = ("Lokas & Geografias", "3.3 Localidades terrestres")
LOK_REG = ("Lokas & Geografias", "3.4 Regiões cósmicas / Portais")

# ---------------------------------------------------------------- PROCESSOS & FENÔMENOS
PRO_BIO = ("Processos & Fenômenos", "4.1 Processos biológicos / genéticos")
PRO_ESP = ("Processos & Fenômenos", "4.2 Fenômenos espirituais / mediúnicos")
PRO_TRA = ("Processos & Fenômenos", "4.3 Transmigração / Reencarnação")
PRO_FIS = ("Processos & Fenômenos", "4.4 Fenômenos físicos / energéticos")

# ---------------------------------------------------------------- TECNOLOGIAS & ARTEFATOS
TEC_NAV = ("Tecnologias & Artefatos", "5.1 Naves / Tecnologia extraterrestre")
TEC_SAG = ("Tecnologias & Artefatos", "5.2 Artefatos sagrados / Relíquias")
TEC_DIS = ("Tecnologias & Artefatos", "5.3 Dispositivos / Instrumentos")
TEC_ESC = ("Tecnologias & Artefatos", "5.4 Escrituras / Objetos documentais")

# ---------------------------------------------------------------- GENEALOGIAS & LINHAGENS
GEN_DIV = ("Genealogias & Linhagens", "6.1 Famílias divinas / Celestiais")
GEN_HUM = ("Genealogias & Linhagens", "6.2 Linhagens humanas")
GEN_EXT = ("Genealogias & Linhagens", "6.3 Dinastias extraterrestres")
GEN_AVO = ("Genealogias & Linhagens", "6.4 Árvores genealógicas")

# ---------------------------------------------------------------- EVENTOS & ERAS
EVE_GUE = ("Eventos & Eras", "7.1 Guerras / Rebeliões / Conflitos")
EVE_ERA = ("Eventos & Eras", "7.2 Eras / Épocas / Ciclos")
EVE_PRO = ("Eventos & Eras", "7.3 Profecias / Anúncios")
EVE_CAT = ("Eventos & Eras", "7.4 Catástrofes / Dilúvios / Quedas")
EVE_MIS = ("Eventos & Eras", "7.5 Missões / Expedições / Encontros")

# ---------------------------------------------------------------- TERMOS ESPECÍFICOS
TER_SAN = ("Termos Específicos", "8.1 Sânscrito / Hinduísmo")
TER_HEB = ("Termos Específicos", "8.2 Hebraico / Cabala")
TER_SUM = ("Termos Específicos", "8.3 Sumério / Acádio / Babilônio")
TER_GRE = ("Termos Específicos", "8.4 Grego / Latim")
TER_OUT = ("Termos Específicos", "8.5 Outros idiomas / jargão técnico")

B031 = ["B031"]
P = "provisório"   # 🟡 — definição documentada em fonte publicada (B031), aguardando revisão cruzada com obras primárias de Ellam
C = "candidato"    # ⚪ — identificado, sem ficha

# (codigo, nome, categoria, subcategoria, status, fontes, relacionados, ficha)
TERMOS = [
    # ---- Pré-existentes (RC-001..RC-010)
    ("RC-001", "Javé", SER_DIV[0], SER_DIV[1], P, ['B031', 'B044', 'B035', 'B001', 'B002', 'B033', 'B015', 'B013', 'B014', 'B020', 'B021', 'B022', 'B023', 'B048', 'B003', 'B025', 'B026', 'B034', 'B036', 'B060', 'B019', 'B043', 'B037', 'B039', 'P2022-12-17', 'P2026-07-30', 'P2024-05-04', 'P2025-06-26', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-08-03', 'P2024-07-14', 'P2024-03-03', 'P2024-04-13', 'P2024-04-14', 'P2026-08-04', 'P2024-03-02', 'P2024-02-03', 'P2023-05-13', 'P2023-12-02', 'P2021-03-27', 'P2025-11-29'], 'RC-002; RC-003; RC-007; RC-009; RC-037; RC-041; RC-052; RC-660; RC-661; RC-662; RC-666; RC-717; RC-736; RC-261; RC-604; RC-630; RC-769', True),
    ("RC-002", "Rebelião de Lúcifer", EVE_GUE[0], EVE_GUE[1], P, ["B031", "B003", "B026", "B057", "B058", 'B017', 'P2024-03-03', 'P2024-04-13'], "RC-001; RC-003; RC-070; RC-078; RC-142", True),
    ("RC-003", "Reintegração Cósmica", COS_PRO[0], COS_PRO[1], P, ['B031', 'B003', 'B025', 'B026', 'B005', 'B027', 'B042', 'B037', 'B009', 'B017', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2024-07-13', 'P2024-03-02'], 'RC-005; RC-007; RC-009; RC-070; RC-094; RC-571; RC-612; RC-615; RC-694; RC-106; RC-258; RC-342; RC-690; RC-702; RC-344', True),
    ("RC-004", "Elohim", SER_COL[0], SER_COL[1], C, ["B061", 'P2024-09-28'], "RC-001; RC-474", False),
    ("RC-005", "Segundo Advento do Cristo (Volta de Jesus)", EVE_PRO[0], EVE_PRO[1], P, ["B001", "B002", "B016", "B014", "B003", "B025", "B005", "B011", "B042", "B009", 'B033', 'P2026-08-04', 'P2024-03-02; RC-674; RC-565'], "RC-003; RC-009; RC-070; RC-072; RC-212", True),
    ("RC-006", "Guerra do Éden", EVE_GUE[0], EVE_GUE[1], P, ["B015"], "RC-001; RC-004; RC-147; RC-242", False),
    ("RC-007", "Exilados de Capela", SER_DEC[0], SER_DEC[1], P, ["B031", "B003", "B025", "B026", "B057"], "RC-002; RC-003; RC-020; RC-070; RC-078; RC-105", True),
    ("RC-008", "Tzimtzum", TER_HEB[0], TER_HEB[1], P, ["B013"], "RC-261; RC-267; RC-272; RC-265", True),
    ("RC-009", "Sophia (Cristo Cósmico)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B017', 'B018', 'B039', 'B016', 'B014', 'B013', 'B057', 'B058', 'B060', 'B061', 'P2024-02-25', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03', 'P2024-07-14', 'P2024-03-03', 'P2026-08-04', 'P2024-03-02', 'ART-2026-08-18', 'P2023-05-13', 'P2023-12-02', 'P2021-03-27', 'P2024-09-28'], 'RC-072; RC-081; RC-085; RC-031; RC-005; RC-070; RC-604; RC-615; RC-631; RC-632; RC-692; RC-699; RC-135; RC-565; RC-476; RC-720; RC-770; RC-556', True),
    ("RC-010", "Atlântida / Terra Atlantis", LOK_TER[0], LOK_TER[1], C, ['P2025-02-16'], 'RC-030; RC-088; RC-023; RC-029', False),

    # ---- Glossário B031 (ordem alfabética)
    ("RC-011", "Adhy", SER_LOG[0], SER_LOG[1], P, ['B031', 'B022', 'B051', 'P2021-12-04', 'P2024-11-30'], 'RC-012; RC-013; RC-014; RC-054', False),
    ("RC-012", "Adhyagia", SER_LOG[0], SER_LOG[1], P, ['B031', 'B024', 'B022', 'B051', 'P2021-12-04', 'P2025-02-16', 'P2024-11-30'], 'RC-011; RC-013; RC-047; RC-059', False),
    ("RC-013", "Adhyatman", SER_LOG[0], SER_LOG[1], P, ['B031', 'B024', 'B022', 'B051', 'P2021-12-04', 'P2025-02-16', 'P2024-11-30'], 'RC-011; RC-012; RC-014; RC-087', False),
    ("RC-014", "Adhydaiva", TER_SAN[0], TER_SAN[1], P, ['B031', 'B044', 'B016', 'B022', 'B051', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2024-11-30'], 'RC-013; RC-015; RC-016; RC-037; RC-102; RC-135; RC-630', False),
    ("RC-015", "Adhybutha", TER_SAN[0], TER_SAN[1], P, ['B031', 'B051', 'P2021-12-04', 'P2025-02-16', 'P2024-11-30'], 'RC-014; RC-016; RC-049', False),
    ("RC-016", "Adhyajna", TER_SAN[0], TER_SAN[1], P, ['B031', 'B016', 'B051', 'P2021-12-04', 'P2025-02-16', 'P2024-11-30'], 'RC-015; RC-102; RC-135; RC-072', False),
    ("RC-017", "Alt´Lam", LOK_PLA[0], LOK_PLA[1], P, ["B031"], "RC-021; RC-079; RC-142", False),
    ("RC-018", "Alt´Lam Gron", TEC_NAV[0], TEC_NAV[1], P, ["B031", "B017", "B018", "B039"], "RC-017; RC-058; RC-062; RC-089", False),
    ("RC-019", "Anjos clones", SER_ANJ[0], SER_ANJ[1], P, ['B031', 'B024', 'B044', 'B035', 'B001', 'B002', 'B015', 'P2025-10-25', 'P2025-06-26', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29', 'P2024-04-13'], 'RC-031; RC-037; RC-055; RC-147; RC-638', False),
    ("RC-020", "Anjos caídos", SER_DEC[0], SER_DEC[1], P, ["B031", "B003", "B005"], "RC-007; RC-078; RC-024; RC-082", False),
    ("RC-021", "Antares (Sistema)", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B058"], "RC-017; RC-067; RC-002; RC-103", True),
    ("RC-022", "Antlar", LOK_TER[0], LOK_TER[1], P, ["B031"], "RC-025; RC-023; RC-030", False),
    ("RC-023", "Antlartes", LOK_TER[0], LOK_TER[1], P, ["B031"], "RC-030; RC-010; RC-022", False),
    ("RC-024", "Anunnakis", SER_EXT[0], SER_EXT[1], P, ['B031', 'B017', 'B018', 'B023', 'B015', 'B061', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-04-13', 'P2023-12-02', 'P2021-03-27', 'B089'], 'RC-082; RC-134; RC-053; RC-080; RC-580; RC-583; RC-587; RC-588; RC-589', True),
    ("RC-025", "Asphezian", TEC_NAV[0], TEC_NAV[1], P, ["B031"], "RC-057; RC-058; RC-022; RC-092", False),
    ("RC-026", "Astralização dos Biodemos", PRO_ESP[0], PRO_ESP[1], P, ["B031"], "RC-101; RC-127; RC-142; RC-074", False),
    ("RC-027", "Astréia", SER_DEC[0], SER_DEC[1], P, ["B031", "B060"], "RC-116; RC-047; RC-101", False),
    ("RC-028", "Atlan", LOK_TER[0], LOK_TER[1], P, ["B031", "B017", "B018", "B039", "B006"], "RC-030; RC-079; RC-010", False),
    ("RC-029", "Atlans", LOK_TER[0], LOK_TER[1], P, ["B031"], "RC-030; RC-010; RC-028", False),
    ("RC-030", "Atlantes", SER_DEC[0], SER_DEC[1], P, ["B031"], "RC-010; RC-028; RC-029; RC-022; RC-023", False),
    ("RC-031", "Aya e Aye", SER_ANJ[0], SER_ANJ[1], P, ["B031", "B024", "B044", "B061"], "RC-019; RC-009; RC-001; RC-097", False),
    ("RC-032", "Benem", LOK_TER[0], LOK_TER[1], P, ["B031", "B017", "B018", "B061"], "RC-057; RC-065; RC-043", False),
    ("RC-033", "Bhuloka", TER_SAN[0], TER_SAN[1], P, ['B031', 'P2025-03-15'], 'RC-107; RC-034; RC-038', False),
    ("RC-034", "Big Bang", COS_COG[0], COS_COG[1], P, ['B031', 'B024', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-033; RC-107; RC-106', False),
    ("RC-035", "Bilatérios", SER_HIB[0], SER_HIB[1], P, ['B031', 'P2024-05-04', 'P2025-02-16', 'P2024-04-13'], 'RC-093; RC-036; RC-631', False),
    ("RC-036", "Biodemos", SER_EXT[0], SER_EXT[1], P, ['B031', 'B044', 'B001', 'B017', 'B018', 'B039', 'B023', 'B050', 'B057', 'B058', 'P2024-05-04', 'P2024-04-13'], "RC-109; RC-136; RC-049; RC-098", True),
    ("RC-037", "Brahma (Brajna)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B024', 'B044', 'B001', 'B033', 'B013', 'B020', 'B022', 'B060', 'B061', 'B037', 'P2022-12-17', 'P2026-07-30', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-08-03', 'P2024-07-14', 'P2025-11-29'], 'RC-041; RC-001; RC-052; RC-104; RC-135; RC-102; RC-696; RC-700; RC-701; RC-261; RC-604; RC-265', True),
    ("RC-038", "Brahmaloka", TER_SAN[0], TER_SAN[1], P, ['B031', 'B016', 'B013', 'B021', 'B023', 'P2025-03-15'], 'RC-106; RC-077; RC-066; RC-049; RC-041', False),
    ("RC-039", "Capela (Sistema)", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B003", "B025", "B057", "B058"], "RC-085; RC-046; RC-109; RC-146; RC-002; RC-007", True),
    ("RC-040", "CFD (Código Fonte Definidor)", COS_LEI[0], COS_LEI[1], P, ['B031', 'B024', 'B002', 'B033', 'B021', 'B041', 'B040', 'B019', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04', 'P2024-08-03'], 'RC-041; RC-104; RC-081; RC-091; RC-742', False),
    ("RC-041", "Criador (Brahma/Javé/Demiurgo)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B044', 'B035', 'B001', 'B002', 'B033', 'B015', 'B016', 'B013', 'B020', 'B048', 'B041', 'B034', 'B036', 'B017', 'B018', 'B039', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29'], 'RC-037; RC-052; RC-047; RC-048; RC-001', True),
    ("RC-042", "Criatura Universal", SER_HIB[0], SER_HIB[1], P, ['B031', 'B024', 'B019', 'B041', 'P2026-04-02', 'P2023-05-13'], "RC-056; RC-099; RC-107; RC-645; RC-761", True),
    ("RC-043", "Conselho dos Cinco", GEN_EXT[0], GEN_EXT[1], P, ["B031"], "RC-065; RC-032; RC-111; RC-121; RC-122; RC-138; RC-143", False),
    ("RC-044", "Cultura Demo", COS_LEI[0], COS_LEI[1], P, ["B031", "B044"], "RC-049; RC-077; RC-064; RC-065", False),
    ("RC-045", "Daemon", TER_GRE[0], TER_GRE[1], P, ["B031"], "RC-049; RC-050; RC-053", False),
    ("RC-046", "Dan", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B057", "B058"], "RC-136; RC-039; RC-079", True),
    ("RC-047", "Deidade (Pai-Mãe Amantíssimo / Brahman)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B024', 'B001', 'B002', 'B048', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-28'], 'RC-052; RC-054; RC-041', True),
    ("RC-048", "Demiurgo", TER_GRE[0], TER_GRE[1], P, ["B031"], "RC-041; RC-087; RC-061; RC-063", False),
    ("RC-049", "Demos", SER_DEC[0], SER_DEC[1], P, ['B031', 'B044', 'B035', 'B021', 'B022', 'B023', 'B050', 'B052', 'B060', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29', 'P2024-03-03', 'P2024-04-13'], 'RC-022; RC-050; RC-045; RC-053; RC-038; RC-097; RC-630', True),
    ("RC-050", "Demônios", SER_DEC[0], SER_DEC[1], P, ['B031', 'P2025-06-26'], "RC-049; RC-045; RC-078", False),
    ("RC-051", "Despina", SER_DEC[0], SER_DEC[1], P, ["B031", "B060", 'B089'], "RC-112; RC-047", False),
    ("RC-052", "Deus / Deus Incognoscível", SER_DIV[0], SER_DIV[1], P, ['B031', 'B001', 'B002', 'B048', 'B061', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-047; RC-041; RC-059; RC-001; RC-723', True),
    ("RC-053", "Deuses (os dois tipos)", SER_DEC[0], SER_DEC[1], P, ['B031', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09'], 'RC-049; RC-024; RC-047; RC-064; RC-065', False),
    ("RC-054", "Divindades (Co-criadoras)", SER_DIV[0], SER_DIV[1], P, ["B031", "B024"], "RC-047; RC-011; RC-012; RC-037", False),
    ("RC-055", "En Drel", SER_ANJ[0], SER_ANJ[1], P, ['B031', 'B015', 'B061', 'P2025-10-25'], "RC-019; RC-147; RC-001", True),
    ("RC-056", "Especiação", PRO_BIO[0], PRO_BIO[1], P, ['B031', 'P2022-12-17', 'P2025-02-16', 'P2024-09-29', 'P2024-07-13', 'P2023-05-13', 'P2021-03-27', 'P2025-11-29'], 'RC-042; RC-099; RC-698', True),
    ("RC-057", "Espherian", TEC_NAV[0], TEC_NAV[1], P, ["B031"], "RC-058; RC-025; RC-032; RC-065", False),
    ("RC-058", "Espheron", TEC_NAV[0], TEC_NAV[1], P, ["B031", "B017", "B018", "B039"], "RC-057; RC-025; RC-018; RC-062", False),
    ("RC-059", "Espiritualidade Superior", COS_DIM[0], COS_DIM[1], P, ['B031', 'B024', 'B013', 'B027', 'B051', 'B060', 'P2021-12-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14'], 'RC-052; RC-012; RC-100', False),
    ("RC-060", "Espiritualidade Operacional", COS_DIM[0], COS_DIM[1], P, ['B031', 'B013', 'B051', 'B060', 'P2021-12-04', 'P2024-05-04', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14'], 'RC-061; RC-059; RC-100', False),
    ("RC-061", "Espiritualidade Laboratorial", COS_DIM[0], COS_DIM[1], P, ['B031', 'B024', 'B013', 'B051', 'B060', 'P2021-12-04', 'P2024-05-04', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14'], 'RC-060; RC-087; RC-048; RC-472; RC-473; RC-496; RC-596; RC-601; RC-635', False),
    ("RC-062", "Experiência Gron", EVE_MIS[0], EVE_MIS[1], P, ["B031"], "RC-058; RC-018; RC-032; RC-068", False),
    ("RC-063", "Favor Divino", COS_ETI[0], COS_ETI[1], P, ['B031', 'B048', 'P2025-03-15', 'P2024-11-09', 'P2024-09-29', 'P2024-04-14', 'P2025-06-14'], 'RC-041; RC-001; RC-048', False),
    ("RC-064", "Fenvans", SER_EXT[0], SER_EXT[1], P, ['B031', 'B024', 'P2022-12-17', 'P2024-11-30', 'P2024-08-03', 'P2024-04-13'], 'RC-080; RC-106; RC-098; RC-031; RC-081', True),
    ("RC-065", "Frota Norte", GEN_EXT[0], GEN_EXT[1], P, ["B031", "B017", "B018", "B061"], "RC-032; RC-043; RC-109", False),
    ("RC-066", "Genos", TER_SAN[0], TER_SAN[1], P, ["B031"], "RC-077; RC-038; RC-064; RC-065", False),
    ("RC-067", "Gron Mion", LOK_PLA[0], LOK_PLA[1], P, ["B031"], "RC-103; RC-074; RC-136", False),
    ("RC-068", "Hiperbórea", LOK_TER[0], LOK_TER[1], P, ["B031", "B023", "B052", "B061", 'P2024-04-13', 'P2025-11-29'], "RC-083; RC-062; RC-120; RC-071", True),
    ("RC-069", "Ion Crom", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-136; RC-018", False),
    ("RC-070", "Isolamento Cósmico", EVE_GUE[0], EVE_GUE[1], P, ['B031', 'B033', 'B003', 'B025', 'B026', 'B005', 'P2022-12-17', 'P2024-11-30', 'P2024-07-13'], 'RC-002; RC-005; RC-009; RC-003; RC-007; RC-105', True),
    ("RC-071", "Jan Val Ellam (Rogério de Almeida Freitas)", SER_HUM[0], SER_HUM[1], P, ['B031', 'B016', 'B006', 'B027', 'B034', 'B036', 'B060', 'P2021-12-04', 'P2025-06-26'], "RC-094; RC-083; RC-095; RC-120; RC-617; RC-659", True),
    ("RC-072", "Jesus", SER_HUM[0], SER_HUM[1], P, ['B031', 'B017', 'B018', 'B039', 'B015', 'B016', 'B014', 'B020', 'B003', 'B025', 'B026', 'B005', 'B011', 'B049', 'B043', 'B009', 'B027', 'B001', 'P2026-07-30', 'P2025-06-26', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2026-08-04', 'P2024-03-02', 'P2023-05-13', 'P2024-09-28', 'P2025-11-29'], 'RC-009; RC-005; RC-016; RC-041; RC-138; RC-592; RC-604; RC-659; RC-713; RC-722; RC-286; RC-647; RC-565; RC-293; RC-479; RC-770; RC-556; RC-585', True),
    ("RC-073", "Keshava", TER_SAN[0], TER_SAN[1], P, ['B031', 'P2026-04-02'], "RC-037; RC-102; RC-135; RC-081", False),
    ("RC-074", "Len Mion (Satã)", SER_DEC[0], SER_DEC[1], P, ["B031", "B017", "B018", "B039", "B057", "B058", "B060", 'P2021-03-27; RC-286'], "RC-142; RC-026; RC-101; RC-067; RC-002", True),
    ("RC-075", "Lila", TER_SAN[0], TER_SAN[1], P, ['B031', 'B024', 'B044', 'B035', 'B022', 'B023', 'P2024-11-30'], 'RC-104; RC-037; RC-102; RC-135', False),
    ("RC-076", "Logos / Logos Criadores", SER_LOG[0], SER_LOG[1], P, ["B031", "B014"], "RC-092; RC-037; RC-102; RC-135; RC-104", False),
    ("RC-077", "Lokas", TER_SAN[0], TER_SAN[1], P, ["B031", "B021", "B060"], "RC-038; RC-066; RC-106", False),
    ("RC-078", "Lúcifer (Yel Luzbel)", SER_DEC[0], SER_DEC[1], P, ['B031', 'B017', 'B018', 'B039', 'B015', 'B003', 'B025', 'B026', 'B057', 'B058', 'B060', 'B061', 'P2022-12-17', 'P2024-03-03'], "RC-142; RC-002; RC-070; RC-020; RC-007", True),
    ("RC-079", "Mastlans Phisosferas / Luciferianas", TEC_NAV[0], TEC_NAV[1], P, ['B031', 'B061', 'P2022-12-17'], "RC-017; RC-028; RC-046; RC-002", False),
    ("RC-080", "Mensagem Talm", TEC_ESC[0], TEC_ESC[1], P, ["B031", "B017", "P2023-05-13"], "RC-064; RC-141; RC-091; RC-089; RC-078; RC-761", True),
    ("RC-081", "Mohen So (Avatar Keshava de Vishnu)", SER_EXT[0], SER_EXT[1], P, ['B031', 'B017', 'B014', 'B061', 'P2026-04-02', 'P2025-10-25', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03', 'P2024-04-14', 'P2023-12-02'], 'RC-135; RC-009; RC-073; RC-091; RC-040; RC-454; RC-282', True),
    ("RC-082", "Nephilins", SER_EXT[0], SER_EXT[1], P, ["B031", "B017", "B018", "B023"], "RC-024; RC-096; RC-134", False),
    ("RC-083", "Norte Divino", LOK_TER[0], LOK_TER[1], P, ["B031"], "RC-068; RC-120", False),
    ("RC-084", "Orbe", COS_DIM[0], COS_DIM[1], P, ['B031', 'P2024-11-09'], 'RC-107; RC-100; RC-726', False),
    ("RC-085", "Orbum", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B042", "B057"], "RC-009; RC-039; RC-040", False),
    ("RC-086", "Pandora", SER_HIB[0], SER_HIB[1], P, ['B031', 'B044', 'B020', 'B021', 'B061', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'ART-2026-08-18', 'P2024-02-03', 'P2024-08-03', 'B087', 'B088', 'B089'], 'RC-118; RC-047; RC-142; RC-053; RC-727; RC-286', True),
    ("RC-087", "Perpérion", COS_DIM[0], COS_DIM[1], P, ['B031', 'B024', 'B013', 'B060', 'P2021-12-04', 'P2024-05-04'], "RC-061; RC-013; RC-048; RC-092; RC-106; RC-107; RC-152; RC-167; RC-472; RC-496; RC-497; RC-596; RC-411; RC-455", True),
    ("RC-088", "Portlan e Portlon", LOK_TER[0], LOK_TER[1], P, ["B031"], "RC-010; RC-047", False),
    ("RC-089", "Processador Val", TEC_NAV[0], TEC_NAV[1], P, ['B031', 'B017', 'B018', 'B039', 'P2026-04-02'], "RC-109; RC-018; RC-080; RC-141", False),
    ("RC-090", "Projeto Planeta Azul", EVE_MIS[0], EVE_MIS[1], P, ["B031", "B003", "B026"], "RC-107; RC-106; RC-094", False),
    ("RC-091", "Projeto Talm", EVE_MIS[0], EVE_MIS[1], P, ['B031', 'B024', 'B044', 'B001', 'P2021-12-04', 'P2025-03-15', 'P2024-11-02', 'P2024-08-03'], 'RC-080; RC-104; RC-037; RC-102; RC-135; RC-081; RC-040; RC-154; RC-282', True),
    ("RC-092", "Quarto Logos (Olm / Codificador de Zian)", SER_LOG[0], SER_LOG[1], P, ['B031', 'B016', 'B014', 'B057', 'B060', 'P2021-12-04', 'P2026-07-30', 'P2026-04-02', 'P2025-10-25', 'P2025-02-16', 'P2024-03-02', 'ART-2026-08-18', 'P2023-05-13', 'P2023-12-02', 'P2021-03-27', 'P2024-09-28', 'P2024-08-03'], 'RC-076; RC-087; RC-085; RC-025; RC-072; RC-456; RC-472; RC-604; RC-607; RC-609; RC-611; RC-612; RC-615; RC-608; RC-167; RC-649; RC-697', True),
    ("RC-093", "Radiatas", SER_HIB[0], SER_HIB[1], P, ['B031', 'P2024-05-04', 'P2025-02-16', 'P2024-04-13'], 'RC-035; RC-109; RC-136; RC-009; RC-631', False),
    ("RC-094", "Revelação Cósmica (conceito)", COS_COG[0], COS_COG[1], P, ['B031', 'B044', 'B035', 'B013', 'B014', 'B022', 'B023', 'B048', 'B003', 'B005', 'B011', 'B049', 'B043', 'B041', 'B006', 'B050', 'B027', 'B051', 'B034', 'B036', 'B040', 'B052', 'B042', 'B009', 'P2021-12-04', 'P2025-10-25', 'P2025-06-26', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2023-12-02', 'P2021-03-27'], 'RC-071; RC-106; RC-107; RC-003; RC-090; RC-611; RC-656; RC-718', True),
    ("RC-095", "Rogério de Almeida Freitas", SER_HUM[0], SER_HUM[1], P, ["B031"], "RC-071; RC-094", False),
    ("RC-096", "Septuaginta", TEC_ESC[0], TEC_ESC[1], P, ['B031', 'P2026-08-04'], 'RC-082; RC-106', False),
    ("RC-097", "Seres Extrafísicos", SER_DEC[0], SER_DEC[1], P, ["B031"], "RC-049; RC-019; RC-024; RC-106; RC-031", False),
    ("RC-098", "Seres Extraterrenos / Extraterrestres", SER_EXT[0], SER_EXT[1], P, ["B031", "B044", "B005", "B042"], "RC-036; RC-064; RC-009; RC-078; RC-024", False),
    ("RC-099", "Seres Terrenos (Homo Sapiens)", SER_HUM[0], SER_HUM[1], P, ['B031', 'B039', 'B023', 'B048', 'B003', 'B026', 'B005', 'B049', 'B041', 'B006', 'B050', 'B034', 'B036', 'B040', 'B052', 'B061', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-042; RC-056; RC-107; RC-578', False),
    ("RC-100", "Seres Espirituais", SER_LOG[0], SER_LOG[1], P, ['B031', 'B024', 'B006', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-059; RC-060; RC-084; RC-012; RC-054', False),
    ("RC-101", "Shamb-Aha", LOK_MUN[0], LOK_MUN[1], P, ["B031", "B017", "B018", "B039"], "RC-127; RC-026; RC-142; RC-074; RC-133", False),
    ("RC-102", "Shiva (Savna)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B024', 'B044', 'B001', 'B033', 'B016', 'B020', 'B021', 'B022', 'B050', 'B051', 'B036', 'B060', 'B037', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2025-11-29'], 'RC-037; RC-135; RC-104; RC-016; RC-073; RC-642; RC-604; RC-675', True),
    ("RC-103", "Tau Ceti (Sistema)", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B058"], "RC-067; RC-021", True),
    ("RC-104", "Trimurti", GEN_DIV[0], GEN_DIV[1], P, ['B031', 'B035', 'B001', 'B033', 'B014', 'B044', 'B024', 'B021', 'B022', 'B023', 'B060', 'B037', 'B017', 'B018', 'B039', 'B020', 'P2022-12-17', 'P2021-12-04', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03', 'P2024-07-14', 'P2024-03-02', 'P2023-12-02', 'P2025-11-29'], 'RC-037; RC-102; RC-135; RC-075; RC-040; RC-575; RC-581; RC-609; RC-610; RC-475; RC-769', True),
    ("RC-105", "Ulsh", GEN_EXT[0], GEN_EXT[1], P, ["B031", "B061"], "RC-007; RC-070; RC-036", False),
    ("RC-106", "Universo Antimaterial (Brahmaloka / Universo Paralelo)", COS_DIM[0], COS_DIM[1], P, ['B031', 'B024', 'B044', 'B001', 'B002', 'B016', 'B013', 'B021', 'B041', 'B060', 'P2022-12-17', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03', 'P2024-07-13'], 'RC-107; RC-038; RC-108; RC-041; RC-097; RC-077; RC-575; RC-581; RC-636; RC-637; RC-639; RC-003; RC-630; RC-690; RC-495', True),
    ("RC-107", "Universo Material (Bhuloka)", COS_DIM[0], COS_DIM[1], P, ['B031', 'B024', 'B044', 'B001', 'B002', 'B013', 'B005', 'B060', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-106; RC-033; RC-034; RC-084; RC-099; RC-636', True),
    ("RC-108", "Universo Paralelo", COS_DIM[0], COS_DIM[1], P, ['B031', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03'], 'RC-106; RC-038; RC-744', False),
    ("RC-109", "Val (Família Val)", GEN_EXT[0], GEN_EXT[1], P, ['B031', 'P2022-12-17'], "RC-146; RC-136; RC-089; RC-120; RC-036", False),
    ("RC-110", "Val Am", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109", False),
    ("RC-111", "Val Amon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-043; RC-109; RC-065", False),
    ("RC-112", "Val Anen", SER_EXT[0], SER_EXT[1], P, ["B031", "B060"], "RC-133; RC-109; RC-051", False),
    ("RC-113", "Val Anon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109", False),
    ("RC-114", "Val Antien", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109", False),
    ("RC-115", "Val Aten", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109; RC-127", False),
    ("RC-116", "Val Bon", SER_EXT[0], SER_EXT[1], P, ["B031", "B060"], "RC-133; RC-109; RC-027", False),
    ("RC-117", "Val Den", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109", False),
    ("RC-118", "Val Dimon", SER_EXT[0], SER_EXT[1], P, ["B031", "B020"], "RC-133; RC-109; RC-086", False),
    ("RC-119", "Val Ean", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109", False),
    ("RC-120", "Val El / Val Ellam", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109; RC-071; RC-140; RC-068; RC-083", False),
    ("RC-121", "Val Elliah", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-043; RC-109; RC-072", False),
    ("RC-122", "Val Ellieh", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-043; RC-109; RC-072", False),
    ("RC-123", "Val Eno", SER_EXT[0], SER_EXT[1], P, ["B031", "B017", "B018", "B039"], "RC-109; RC-018; RC-071; RC-125", False),
    ("RC-124", "Val Eon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-123; RC-109", False),
    ("RC-125", "Val Gevi", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109; RC-092; RC-120; RC-123", False),
    ("RC-126", "Val Geon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109; RC-128; RC-129; RC-024", False),
    ("RC-127", "Val-Ha", LOK_MUN[0], LOK_MUN[1], P, ["B031", "B061"], "RC-101; RC-133; RC-115", False),
    ("RC-128", "Val Ilon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109; RC-126; RC-129", False),
    ("RC-129", "Val Pen", SER_EXT[0], SER_EXT[1], P, ["B031", "B060"], "RC-109; RC-126; RC-128; RC-024", False),
    ("RC-130", "Val Sean", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109", False),
    ("RC-131", "Val Sion", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-133; RC-109", False),
    ("RC-132", "Val Tam", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-109; RC-018", True),
    ("RC-133", "Val dos Corpos Perdidos / Dimensionados", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-127; RC-109; RC-110; RC-112; RC-114; RC-115; RC-116; RC-117; RC-118; RC-130; RC-131", False),
    ("RC-134", "Viajores", TER_OUT[0], TER_OUT[1], P, ["B031", "B015"], "RC-024; RC-082", False),
    ("RC-135", "Vishnu (Mavatna)", SER_DIV[0], SER_DIV[1], P, ['B031', 'B024', 'B044', 'B001', 'B033', 'B016', 'B014', 'B020', 'B021', 'B022', 'B051', 'B036', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03', 'P2024-07-14'], 'RC-037; RC-102; RC-104; RC-081; RC-009; RC-584; RC-622; RC-642; RC-565', False),
    ("RC-136", "Yel (Família Yel)", GEN_EXT[0], GEN_EXT[1], P, ["B031"], "RC-109; RC-078; RC-046; RC-137", False),
    ("RC-137", "Yel Adrax", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-136", False),
    ("RC-138", "Yel Am / Yel Liam", SER_EXT[0], SER_EXT[1], P, ['B031', 'B011', 'B060', 'P2026-04-02', 'P2025-10-25'], "RC-136; RC-120; RC-140; RC-072; RC-043; RC-647", False),
    ("RC-139", "Yel Breasil", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-136; RC-047", False),
    ("RC-140", "Yel Liam", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-138; RC-136; RC-072", False),
    ("RC-141", "Yel Lupon", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-136; RC-080; RC-026; RC-101; RC-089", False),
    ("RC-142", "Yel Luzbel", SER_DEC[0], SER_DEC[1], P, ['B031', 'B017', 'B018', 'B039', 'B015', 'B057', 'B058', 'B060', 'P2022-12-17', 'P2024-03-03'], "RC-078; RC-136; RC-002; RC-070; RC-017; RC-026", True),
    ("RC-143", "Yel Luziel", SER_EXT[0], SER_EXT[1], P, ["B031"], "RC-136; RC-043; RC-065", False),
    ("RC-144", "Zeitgeist", TER_OUT[0], TER_OUT[1], P, ["B031"], "RC-094", False),
    ("RC-145", "Zeus", SER_DEC[0], SER_DEC[1], P, ['B031', 'B020', 'B021', 'B050', 'B060', 'P2022-12-17', 'P2025-10-25', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'B087', 'B088', 'B089'], 'RC-047; RC-066; RC-077; RC-097; RC-480', True),
    ("RC-146", "Zian (Zion)", LOK_PLA[0], LOK_PLA[1], P, ["B031", "B057", "B061"], "RC-109; RC-039; RC-092", True),
    ("RC-147", "Zont En Drel 29", SER_ANJ[0], SER_ANJ[1], P, ['B031', 'B015', 'P2025-10-25', 'P2025-06-26'], "RC-055; RC-019; RC-001; RC-006; RC-651; RC-652", True),

    # ---- Novos termos de B024 (obra primária: A Epopeia dos Agentes da Vida Universal, 2019)
    ("RC-148", "Agentes da Vida Universal", SER_LOG[0], SER_LOG[1], P, ["B031", "B024", "B001", "B002", "B014", "B005"], "RC-149; RC-150; RC-160; RC-106; RC-107", True),
    ("RC-149", "Mônada (Mônada Espiritual)", SER_LOG[0], SER_LOG[1], P, ['B024', 'B001', 'B002', 'B048', 'P2021-12-04', 'P2024-05-04', 'P2025-10-25', 'P2024-11-30', 'P2024-11-09'], 'RC-148; RC-100; RC-012; RC-603; RC-653', True),
    ("RC-150", "Xadrez Cósmico", COS_COG[0], "2.1 Cosmogonia / Criação", P, ["B024"], "RC-104; RC-075; RC-148; RC-152", True),
    ("RC-151", "Gunas Criadoras (Sattva, Rajas, Tamas)", TER_SAN[0], TER_SAN[1], P, ['B024', 'P2024-09-29', 'P2024-02-03', 'P2024-09-28'], 'RC-102; RC-135; RC-152; RC-037', True),
    ("RC-152", "Prabrajna", SER_DIV[0], SER_DIV[1], P, ['B024', 'B044', 'B001', 'B016', 'B013', 'B022', 'B060', 'B061', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-03-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-14', 'P2025-06-14', 'P2024-03-02', 'B089'], 'RC-151; RC-150; RC-037; RC-094; RC-087; RC-628; RC-629; RC-638; RC-691; RC-604; RC-167; RC-530; RC-559', True),
    ("RC-153", "CFDP (Código-fonte Definidor Pessoal)", COS_LEI[0], COS_LEI[1], P, ['B024', 'B041', 'B019', 'P2025-03-15'], 'RC-040; RC-091; RC-154', False),
    ("RC-154", "Nidana (ovo cósmico)", COS_COG[0], COS_COG[1], P, ['B024', 'P2024-05-04', 'P2025-03-15', 'P2024-11-30', 'P2024-04-13'], 'RC-153; RC-091; RC-691; RC-693', False),
    ("RC-155", "Eras da Criação (10 eras)", EVE_ERA[0], EVE_ERA[1], P, ["B024", "B033", "B050"], "RC-156; RC-157; RC-158; RC-159; RC-567; RC-568", True),
    ("RC-156", "Era da Solidão", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-152; RC-037", False),
    ("RC-157", "Era da Geração", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-019", False),
    ("RC-158", "Era da Punição", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-102; RC-019", False),
    ("RC-159", "Era do Impasse", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-031", False),
    ("RC-160", "Entropia e Negentropia", COS_LEI[0], COS_LEI[1], P, ['B024', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-09-28'], 'RC-161; RC-148; RC-634; RC-725; RC-727', True),
    ("RC-161", "Memória Quântica dos Elétrons", COS_LEI[0], COS_LEI[1], P, ['B024', 'B041', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2025-06-14'], 'RC-160; RC-162; RC-163; RC-636; RC-637; RC-638; RC-690; RC-691; RC-692; RC-693; RC-707; RC-708; RC-715; RC-378', True),
    ("RC-162", "Elétrons (agente básico da vida universal)", PRO_FIS[0], PRO_FIS[1], P, ['B024', 'B041', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-03-03', 'P2024-04-14', 'P2025-06-14'], 'RC-161; RC-148; RC-636; RC-690; RC-692; RC-693; RC-715', False),
    ("RC-163", "Mente Universal (Emergente)", COS_PRO[0], COS_PRO[1], P, ['B024', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-14', 'P2025-06-14'], 'RC-161; RC-042; RC-164; RC-694; RC-707; RC-725', False),
    ("RC-164", "Criaturas-ferramenta", COS_ETI[0], COS_ETI[1], P, ['B024', 'B035', 'B019', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-04-13', 'P2024-04-14', 'P2021-03-27', 'P2025-11-29'], 'RC-163; RC-099; RC-160', True),
    ("RC-165", "Karuna", TER_SAN[0], TER_SAN[1], P, ["B024"], "RC-148; RC-075", True),
    ("RC-166", "Mentalma", TER_OUT[0], TER_OUT[1], P, ['B024', 'B074', 'B075', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2026-04-02', 'P2025-06-26', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-14', 'P2025-06-14', 'P2026-08-04', 'ART-2026-08-18', 'P2023-05-13'], 'RC-071; RC-618; RC-633; RC-655', True),
    ("RC-167", "Criação Indevida (Obra indevida)", COS_COG[0], COS_COG[1], P, ['B024', 'B035', 'B001', 'B002', 'B016', 'B013', 'B022', 'B041', 'B037', 'B033', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2023-05-13'], 'RC-094; RC-041; RC-150; RC-087; RC-628; RC-638; RC-152', True),
    ("RC-168", "Era da Lila e da Aceitação", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-075", False),
    ("RC-169", "Era da Semeadura Universal", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-091", False),
    ("RC-170", "Era do Refinamento da Semeadura Biológica Universal", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-091; RC-107", False),
    ("RC-171", "Era da Geopolítica Universal e da Divisão do Comando", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-009; RC-092", False),
    ("RC-172", "Era da Criatura Universal", EVE_ERA[0], EVE_ERA[1], P, ["B024", "B019"], "RC-155; RC-042; RC-163", False),
    ("RC-173", "Era das Supercivilizações", EVE_ERA[0], EVE_ERA[1], P, ["B024"], "RC-155; RC-042", False),

    # ---- Novos termos de B044 (obra primária: A Divina Colmeia — A Trimurti Desencantada, 2019)
    ("RC-174", "Colmeia Universal", COS_LEI[0], COS_LEI[1], P, ['B044', 'P2024-11-30', 'P2024-07-13'], 'RC-175; RC-176; RC-178; RC-001', True),
    ("RC-175", "Abelha-Rainha (Javé)", SER_DIV[0], SER_DIV[1], P, ["B044", 'P2021-03-27', 'P2024-09-28'], "RC-001; RC-174; RC-176", True),
    ("RC-176", "Modelo Colmeia (Sistema/Controle Colmeia)", COS_LEI[0], COS_LEI[1], P, ['B044', 'B035', 'B048', 'P2021-12-04', 'P2025-03-15', 'P2024-11-30', 'P2024-07-13', 'P2023-05-13', 'P2021-03-27'], 'RC-174; RC-175; RC-188; RC-019; RC-690; RC-715', True),
    ("RC-177", "Colmeia do Éden", LOK_TER[0], LOK_TER[1], P, ["B044", "B015"], "RC-174; RC-006; RC-176", False),
    ("RC-178", "Dois Grandes Favos", COS_DIM[0], COS_DIM[1], P, ["B044"], "RC-174; RC-106; RC-107", False),
    ("RC-179", "Plano Colmeia (para o Universo Biológico)", EVE_MIS[0], EVE_MIS[1], P, ['B044', 'P2024-11-30', 'P2024-07-13'], 'RC-091; RC-036; RC-174', True),
    ("RC-180", "Fator Colmeia", COS_LEI[0], COS_LEI[1], P, ['B044', 'P2024-11-30'], 'RC-174; RC-176; RC-155', False),
    ("RC-181", "Pluribus Unum", TER_GRE[0], TER_GRE[1], P, ["B044"], "RC-174; RC-182", False),
    ("RC-182", "Unus Pluribum", TER_GRE[0], TER_GRE[1], P, ["B044"], "RC-174; RC-181", False),
    ("RC-183", "Cultura Demodhármica", COS_LEI[0], COS_LEI[1], P, ["B044", "B014"], "RC-044; RC-049; RC-075", False),
    ("RC-184", "Trava-demo", COS_LEI[0], COS_LEI[1], P, ["B044", "B020"], "RC-086; RC-078; RC-049", False),
    ("RC-185", "Horda Colmeia", SER_ANJ[0], SER_ANJ[1], P, ["B044"], "RC-031; RC-019; RC-174", False),
    ("RC-186", "Biodemol", SER_HIB[0], SER_HIB[1], P, ['B044', 'B017', 'B018', 'B023', 'P2024-11-30', 'P2024-04-13'], 'RC-036; RC-078; RC-176', False),
    ("RC-187", "Insectoides", SER_EXT[0], SER_EXT[1], P, ["B044"], "RC-098; RC-036; RC-091", False),
    ("RC-188", "Mente Coletiva / Redes Psíquicas Coletivas", COS_LEI[0], COS_LEI[1], P, ['B044', 'P2021-12-04', 'P2026-07-30', 'P2024-11-09'], 'RC-176; RC-001; RC-019; RC-603; RC-601; RC-606', True),
    ("RC-189", "Eva (figura)", SER_HUM[0], SER_HUM[1], P, ['B044', 'B020', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-02-03'], 'RC-086; RC-184; RC-099; RC-579; RC-727', False),
    ("RC-190", "Revelação Espiritual (Kardec)", COS_ESP[0], COS_ESP[1], P, ['B044', 'B016', 'B013', 'B048', 'B006', 'B060', 'B061', 'B042', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-03-03', 'P2024-04-14', 'P2025-06-14', 'P2024-02-03'], 'RC-094; RC-071; RC-100', False),
    ("RC-191", "Fofocas cósmicas", TER_OUT[0], TER_OUT[1], P, ['B044', 'P2025-03-15', 'P2025-02-15'], 'RC-098; RC-036', False),
    ("RC-192", "Pílula vermelha", TER_OUT[0], TER_OUT[1], P, ['B044', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2023-05-13'], 'RC-094; RC-071; RC-702; RC-378', True),
    ("RC-193", "Rebanho humano", TER_OUT[0], TER_OUT[1], P, ['B044', 'P2024-07-14'], 'RC-099; RC-174; RC-176; RC-745', True),

    # ---- Novos termos de B035 (obra primária: O Big Data do Criador — AMOSTRA recebida: Intro + caps. 1–2)
    # Termos com conteúdo extraído da amostra (provisórios)
    ("RC-194", "Big Data Cósmico", COS_LEI[0], COS_LEI[1], P, ['B035', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-04-13'], 'RC-001; RC-195; RC-201; RC-019; RC-707; RC-711; RC-724; RC-269', True),
    ("RC-195", "Simbiose Quântica", COS_LEI[0], COS_LEI[1], P, ["B035"], "RC-194; RC-196; RC-167", True),
    ("RC-196", "Criador refém das próprias criaturas", COS_ETI[0], COS_ETI[1], P, ["B035", "B001"], "RC-041; RC-195; RC-176", False),
    ("RC-197", "Big Data da Terra", COS_LEI[0], COS_LEI[1], P, ['B035', 'P2024-09-29'], 'RC-194; RC-193; RC-099', False),
    # Títulos de capítulos de B035 (candidatos — conteúdo aguarda obra completa)
    ("RC-198", "Rédeas Genéticas", COS_LEI[0], COS_LEI[1], C, ['B035', 'P2024-09-29'], 'RC-001; RC-194', False),
    ("RC-199", "Assinatura da Alma", COS_LEI[0], COS_LEI[1], C, ['B035', 'P2025-03-15'], 'RC-149; RC-194; RC-692', False),
    ("RC-200", "Base de Dados do Juízo Final", COS_LEI[0], COS_LEI[1], C, ['B035', 'P2025-02-15', 'P2025-06-14'], 'RC-194; RC-201', True),
    ("RC-201", "O Livro do Criador", COS_LEI[0], COS_LEI[1], C, ["B035"], "RC-194; RC-200; RC-094", False),
    ("RC-202", "Linhagens Preferenciais do Criador", GEN_HUM[0], GEN_HUM[1], C, ['B035', 'P2024-09-29'], 'RC-001; RC-194; RC-189', False),
    ("RC-203", "Fenômenos Denunciadores do Fim", EVE_PRO[0], EVE_PRO[1], C, ['B035', 'P2025-03-15'], 'RC-155; RC-070; RC-690', False),

    # ---- Novos termos da TRILOGIA DOS DRAMAS DE JAVÉ (B001 Cósmico, B002 Espiritual, B033 Terreno)
    # ---- B001 — O Drama Cósmico de Javé (2010)
    ("RC-204", "Realidade Maior / Paraíso Original", COS_DIM[0], COS_DIM[1], P, ['B001', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-047; RC-052; RC-205; RC-059; RC-600; RC-603; RC-606; RC-623; RC-624; RC-625', True),
    ("RC-205", "Pai Supremo (Amantíssimo)", SER_DIV[0], SER_DIV[1], P, ['B001', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-047; RC-052; RC-204; RC-206; RC-723', False),
    ("RC-206", "Divindades Excelsas", SER_DIV[0], SER_DIV[1], P, ["B001"], "RC-205; RC-047; RC-054", False),
    ("RC-207", "Arquiteto Universal", SER_DIV[0], SER_DIV[1], P, ["B001", "B002", "B019"], "RC-001; RC-041; RC-208; RC-152", True),
    ("RC-208", "Criador de Padrões Dependentes", COS_LEI[0], COS_LEI[1], P, ['B001', 'B002', 'P2024-05-04'], "RC-041; RC-207; RC-209", False),
    ("RC-209", "Vida de Padrão Dependente", COS_LEI[0], COS_LEI[1], P, ['B001', 'B002', 'P2024-05-04'], "RC-208; RC-167; RC-036", False),
    ("RC-210", "Matriz Modeladora / Matriz de Cocriação", COS_COG[0], COS_COG[1], P, ['B001', 'B015', 'P2024-05-04'], "RC-204; RC-047; RC-211; RC-628", True),
    ("RC-211", "Kundalini (no contexto RC)", COS_ESP[0], COS_ESP[1], P, ['B001', 'B074', 'B075', 'P2024-05-04'], 'RC-210; RC-149', False),
    ("RC-212", "O Grande Dia do Senhor Javé", EVE_PRO[0], EVE_PRO[1], P, ["B001"], "RC-005; RC-001; RC-009", False),
    ("RC-213", "Centro de Comando Paralelo", LOK_REG[0], LOK_REG[1], P, ["B001"], "RC-106; RC-001; RC-019", False),
    ("RC-214", "Agente do Mais Alto", SER_LOG[0], SER_LOG[1], P, ["B001", "B011", "B042"], "RC-072; RC-059; RC-215", False),
    ("RC-215", "Emissários da Espiritualidade Maior", SER_LOG[0], SER_LOG[1], P, ["B001", "B042"], "RC-059; RC-214; RC-100", False),
    # ---- B002 — O Drama Espiritual de Javé (2011)
    ("RC-216", "Queda do Arquiteto Universal", EVE_CAT[0], EVE_CAT[1], P, ["B002", "B019"], "RC-207; RC-167; RC-041", False),
    ("RC-217", "DNA como Projeção Holográfica do Psiquismo do Criador", COS_LEI[0], COS_LEI[1], P, ['B002', 'B034', 'B040', 'B052', 'B019', 'B074', 'B075', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-07-13'], 'RC-040; RC-041; RC-218; RC-619; RC-632; RC-646; RC-696; RC-698; RC-704; RC-710; RC-713; RC-715; RC-716; RC-719', True),
    ("RC-218", "Holograma Universal", COS_LEI[0], COS_LEI[1], P, ['B002', 'P2025-02-15', 'P2024-11-30'], 'RC-217; RC-219; RC-106; RC-707; RC-708', False),
    ("RC-219", "Agente Secreto do Bem", SER_HUM[0], SER_HUM[1], P, ["B002"], "RC-072; RC-218; RC-214", False),
    ("RC-220", "Conspiração do Desespero", EVE_GUE[0], EVE_GUE[1], P, ["B002"], "RC-001; RC-102; RC-216", False),
    ("RC-221", "Sustentação Espiritual do Universo", COS_LEI[0], COS_LEI[1], P, ["B002"], "RC-106; RC-107; RC-041", False),
    ("RC-222", "Filhos das Estrelas", SER_LOG[0], SER_LOG[1], P, ["B002"], "RC-100; RC-149; RC-107", False),
    ("RC-223", "O Mal: Subproduto da Ignorância Espiritual", COS_ETI[0], COS_ETI[1], P, ['B002', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-190; RC-094; RC-041', True),
    ("RC-224", "Prevalece o Amor", COS_ETI[0], COS_ETI[1], P, ['B002', 'P2025-03-15'], 'RC-072; RC-052; RC-094', False),
    # ---- B033 — O Drama Terreno de Javé
    ("RC-225", "Gestão Cósmica", COS_LEI[0], COS_LEI[1], P, ["B033"], "RC-104; RC-001; RC-072; RC-171; RC-570", True),
    ("RC-226", "Cidadão Cósmico", COS_PRO[0], COS_PRO[1], P, ["B033", "B027", "B042"], "RC-003; RC-070; RC-099; RC-094; RC-566", True),
    ("RC-227", "Opção Terra", EVE_MIS[0], EVE_MIS[1], P, ["B033"], "RC-107; RC-090; RC-091; RC-228", False),
    ("RC-228", "Observação de Sileno (Filhos do Tormento e do Acaso)", COS_PRO[0], COS_PRO[1], P, ["B033"], "RC-099; RC-094; RC-227", False),
    ("RC-229", "A Lógica de Javé e a Origem da Humanidade", COS_COG[0], COS_COG[1], P, ["B033"], "RC-001; RC-099; RC-014", False),
    ("RC-230", "Reflexos da Doença (Herança do DNA)", COS_ETI[0], COS_ETI[1], P, ["B033"], "RC-217; RC-099; RC-040", False),
    ("RC-231", "Razão Filosófica dos Terráqueos", COS_PRO[0], COS_PRO[1], P, ['B033', 'B005', 'B049', 'P2025-03-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14'], 'RC-099; RC-001; RC-094; RC-566; RC-514', True),

    # ---- Novos termos da TRILOGIA TERRA ATLANTIS (B017 Livro 1, B018 Livro 2, B039 Livro 3)
    ("RC-232", "Ostronomos", SER_EXT[0], SER_EXT[1], P, ["B017", "B018", "B060"], "RC-098; RC-024; RC-036; RC-126; RC-128; RC-129", True),
    ("RC-233", "Marca Val (A Estratégia do Possível)", PRO_BIO[0], PRO_BIO[1], P, ["B017"], "RC-109; RC-082; RC-186; RC-036", False),
    ("RC-234", "Cidades Voadoras", TEC_NAV[0], TEC_NAV[1], P, ["B018"], "RC-058; RC-018; RC-065", False),
    ("RC-235", "Teurgistas", TER_GRE[0], TER_GRE[1], P, ["B039"], "RC-097; RC-145; RC-049", False),
    ("RC-236", "O Calvário de um Inocente", EVE_GUE[0], EVE_GUE[1], P, ["B039", "B011"], "RC-072; RC-078; RC-074; RC-142", True),
    ("RC-237", "Land's End (Sinal de Land's End)", LOK_TER[0], LOK_TER[1], P, ["B017"], "RC-010; RC-028; RC-039", False),
    ("RC-238", "Era Sapiens", EVE_ERA[0], EVE_ERA[1], P, ["B039"], "RC-010; RC-155; RC-099", False),
    ("RC-239", "Hitler (figura histórica no RC)", SER_HUM[0], SER_HUM[1], P, ["B039"], "RC-074; RC-078; RC-236", False),
    ("RC-240", "Império dos Descendentes dos Seres dos Portais", GEN_EXT[0], GEN_EXT[1], P, ['B018', 'P2024-09-29'], 'RC-241; RC-010; RC-030; RC-145; RC-736', False),
    ("RC-241", "Seres dos Portais", SER_DEC[0], SER_DEC[1], P, ['B017', 'B018', 'B039', 'B031', 'B021', 'P2022-12-17'], "RC-049; RC-145; RC-097; RC-027; RC-051; RC-086; RC-240", True),

    # ---- Novos termos de B015 (obra primária: O Guardião do Éden, 2017)
    ("RC-242", "Éden do Criador (Éden como laboratório)", LOK_TER[0], LOK_TER[1], P, ["B015", "B020", "B052"], "RC-251; RC-177; RC-006; RC-041; RC-147", True),
    ("RC-243", "Genética da Confiança", COS_LEI[0], COS_LEI[1], P, ['B015', 'B040', 'P2025-02-15'], 'RC-244; RC-099; RC-210; RC-041', True),
    ("RC-244", "Germe da Desconfiança", COS_LEI[0], COS_LEI[1], P, ["B015"], "RC-243; RC-041; RC-107; RC-167", False),
    ("RC-245", "A Humanização do Criador", COS_PRO[0], COS_PRO[1], P, ['B015', 'B036', 'B048', 'B037', 'P2024-05-04', 'P2025-10-25'], "RC-041; RC-001; RC-099; RC-147", True),
    ("RC-246", "Dez Sagrados (primeira geração do Criador)", SER_LOG[0], SER_LOG[1], P, ["B015"], "RC-055; RC-041; RC-206", False),
    ("RC-247", "Endrelnianos", SER_ANJ[0], SER_ANJ[1], P, ["B015"], "RC-055; RC-147; RC-019", False),
    ("RC-248", "Viajores da Rebelião", SER_DEC[0], SER_DEC[1], P, ["B015"], "RC-134; RC-250; RC-002; RC-078; RC-249", False),
    ("RC-249", "Expulsão dos Viajores (decreto do Criador)", EVE_GUE[0], EVE_GUE[1], P, ["B015"], "RC-248; RC-250; RC-147; RC-001", False),
    ("RC-250", "Mundo das Águas", LOK_PLA[0], LOK_PLA[1], P, ["B015"], "RC-248; RC-249; RC-024", False),
    ("RC-251", "Laboratórios do Criador", COS_COG[0], COS_COG[1], P, ['B015', 'P2024-09-29'], 'RC-242; RC-041; RC-090; RC-167', False),

    # ---- Novos termos de B016 (obra primária: O Quarto Logos, 2017)
    ("RC-252", "Olm (Codificador de Zion/Zian)", SER_LOG[0], SER_LOG[1], P, ['B016', 'B057', 'B060', 'P2021-12-04', 'P2024-08-03'], "RC-092; RC-253; RC-256; RC-257", True),
    ("RC-253", "Liberdade Mental (premissa do Quarto Logos)", COS_ETI[0], COS_ETI[1], P, ['B016', 'B014', 'B005', 'B049', 'P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-092; RC-252; RC-254; RC-167; RC-566; RC-618; RC-619; RC-620; RC-695; RC-702; RC-703', True),
    ("RC-254", "Dominação (premissa dos Três Primeiros Logos)", COS_ETI[0], COS_ETI[1], P, ['B016', 'P2024-09-29'], 'RC-104; RC-253; RC-176', False),
    ("RC-255", "A Mensagem do Codificador de Zion", TEC_ESC[0], TEC_ESC[1], P, ["B016"], "RC-252; RC-253; RC-071", False),
    ("RC-256", "Escola dos Agentes Esclarecidos da Busca da Verdade", COS_ESP[0], COS_ESP[1], P, ['B016', 'P2021-12-04'], "RC-252; RC-148; RC-253; RC-071", False),
    ("RC-257", "Espiritismo como Expressão do Quarto Logos", COS_ESP[0], COS_ESP[1], P, ["B016"], "RC-190; RC-092; RC-252", True),
    ("RC-258", "Coreografia Cósmica (vinda de Sophia)", EVE_PRO[0], EVE_PRO[1], P, ['B016', 'P2024-07-13'], 'RC-009; RC-005; RC-003; RC-070', False),
    ("RC-259", "Apolônio de Tiana (encarnação do Quarto Logos)", SER_HUM[0], SER_HUM[1], P, ['B016', 'B061', 'P2021-12-04', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2023-12-02'], 'RC-092; RC-252; RC-072; RC-713', True),
    ("RC-260", "Prisioneiros da Brahmaloka", SER_DEC[0], SER_DEC[1], P, ["B016"], "RC-038; RC-041; RC-106; RC-016; RC-014", True),

    # ---- Novos termos de B013 (obra primária: Tzimtzum — O Exílio Forçado de uma Divindade, 2020)
    ("RC-261", "Kether (Javé na Cabala)", SER_DIV[0], SER_DIV[1], P, ['B013', 'B060', 'P2024-07-14'], 'RC-001; RC-008; RC-263; RC-262; RC-272; RC-037', True),
    ("RC-262", "Daath (a Criação na Cabala)", COS_COG[0], COS_COG[1], P, ["B013"], "RC-261; RC-263; RC-167", True),
    ("RC-263", "Sefirot / Árvore da Vida", TER_HEB[0], TER_HEB[1], P, ['B013', 'P2024-11-09', 'P2024-07-14'], 'RC-264; RC-261; RC-262; RC-674; RC-266; RC-267', True),
    ("RC-264", "Planos de Existência da Cabala (Atziluth, Briah, Yetzirah, Assiah)", COS_DIM[0], COS_DIM[1], P, ["B013", "B060"], "RC-059; RC-061; RC-038; RC-107; RC-263", True),
    ("RC-265", "Os 270 Mundos (profecia do Zohar)", LOK_MUN[0], LOK_MUN[1], P, ["B013"], "RC-266; RC-003; RC-070; RC-077", True),
    ("RC-266", "Sepher ha-Zohar (e Shimon Bar Yochai)", TEC_ESC[0], TEC_ESC[1], P, ['B013', 'P2024-11-09', 'P2024-07-14'], 'RC-265; RC-267; RC-008; RC-263', True),
    ("RC-267", "Isaac Luria e o conceito do Tzimtzum", TER_HEB[0], TER_HEB[1], P, ['B013', 'P2024-11-09'], 'RC-008; RC-266; RC-261', True),
    ("RC-268", "Gnosticismo (contraponto à Cabala)", COS_ESP[0], COS_ESP[1], P, ['B013', 'P2026-04-02', 'P2024-11-09', 'P2023-12-02', 'P2024-09-28'], 'RC-190; RC-261; RC-072; RC-266; RC-647', True),
    ("RC-269", "Linhagens Humanas: Preferidas e Preteridas", GEN_HUM[0], GEN_HUM[1], P, ['B013', 'P2024-09-29'], 'RC-270; RC-099; RC-261; RC-202; RC-194; RC-271; RC-293; RC-736; RC-737', False),
    ("RC-270", "Linhagem dos Patriarcas Hebreus", GEN_HUM[0], GEN_HUM[1], P, ["B013", "B036", "B052"], "RC-269; RC-261; RC-189; RC-099", False),
    ("RC-271", "Pactos do Criador (troca de informações)", COS_ETI[0], COS_ETI[1], P, ['B013', 'P2024-09-29', 'P2024-04-13'], 'RC-261; RC-099; RC-041; RC-063; RC-269', False),
    ("RC-272", "Laço Temporal de Kether/Javé", COS_LEI[0], COS_LEI[1], P, ["B013"], "RC-261; RC-008; RC-167; RC-041; RC-634", False),

    # ---- Novos termos de B014 (obra primária: Sophia e o Logos Criadores, 2020)
    ("RC-273", "A Falsa Trindade (Concílio de Niceia)", EVE_ERA[0], EVE_ERA[1], P, ['B014', 'B049', 'P2026-08-04', 'P2024-09-28'], "RC-009; RC-072; RC-104; RC-094", True),
    ("RC-274", "Cápsula do Tempo de Sophia (João)", TEC_ESC[0], TEC_ESC[1], P, ["B014", "B042", 'P2024-03-02; RC-009'], "RC-009; RC-005; RC-072; RC-094", True),
    ("RC-275", "Arte Demodhármica do Possível", COS_LEI[0], COS_LEI[1], P, ["B014"], "RC-183; RC-009; RC-005; RC-094", False),
    ("RC-276", "Sacralização do Absurdo", COS_ETI[0], COS_ETI[1], P, ["B014"], "RC-094; RC-099; RC-041; RC-254", False),
    ("RC-277", "A Jaula de Cada Espécie", COS_LEI[0], COS_LEI[1], P, ["B014"], "RC-099; RC-036; RC-176; RC-094", False),
    ("RC-278", "Olhar Adulto", COS_PRO[0], COS_PRO[1], P, ["B014"], "RC-099; RC-253; RC-231; RC-094; RC-566", False),
    ("RC-279", "Modo Trimurtiano de Sophia", COS_LEI[0], COS_LEI[1], P, ["B014"], "RC-009; RC-104; RC-075; RC-094", False),
    ("RC-280", "Sophia e a Ressurreição de Jesus", EVE_MIS[0], EVE_MIS[1], P, ['B014', 'P2025-02-15', 'P2024-11-30'], 'RC-009; RC-072; RC-274; RC-094; RC-692; RC-770', False),
    ("RC-281", "Agentes do Quarto Logos", SER_LOG[0], SER_LOG[1], P, ["B014"], "RC-092; RC-252; RC-256; RC-071", False),
    ("RC-282", "Mohen So = Phanes / Protogonos / Vasuki / Kalki (correspondências)", TER_GRE[0], TER_GRE[1], P, ['B014', 'B060', 'B061', 'P2026-04-02', 'P2025-10-25', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03', 'P2024-04-14', 'P2024-03-02', 'P2023-12-02', 'P2021-03-27'], 'RC-081; RC-135; RC-009; RC-094; RC-454; RC-104; RC-769; RC-091', True),

    # ---- Novos termos de B020 (obra primária: O Sorriso de Pandora)
    ("RC-283", "Pandora como Serpente do Éden", EVE_MIS[0], EVE_MIS[1], P, ['B020', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09'], 'RC-086; RC-285; RC-242; RC-189; RC-270; RC-664; RC-697; RC-727; RC-701', True),
    ("RC-284", "Caos = Brahma = Javé (correspondência)", TER_GRE[0], TER_GRE[1], P, ['B020', 'B021', 'B023', 'B060', 'P2025-03-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29'], 'RC-001; RC-037; RC-041; RC-047', True),
    ("RC-285", "Opção Inusitada de Pandora (humanização)", PRO_ESP[0], PRO_ESP[1], P, ['B020', 'P2021-12-04', 'B087', 'B088', 'B089'], "RC-086; RC-283; RC-184; RC-118", True),
    ("RC-286", "Eros = Vishnu / Tártaro = Shiva (correspondências)", TER_GRE[0], TER_GRE[1], P, ['B020', 'B021', 'B060', 'B061', 'P2024-11-30', 'P2024-11-09'], 'RC-135; RC-102; RC-145; RC-284; RC-074; RC-072; RC-519', True),
    ("RC-287", "Enigma da Esperança (Caixa de Pandora)", COS_PRO[0], COS_PRO[1], P, ["B020", 'ART-2026-08-18', 'B087', 'B088'], "RC-086; RC-145; RC-099", True),
    ("RC-288", "Os Anais de uma Cultura Perdida", TEC_ESC[0], TEC_ESC[1], P, ["B020"], "RC-086; RC-145; RC-284; RC-094", False),
    ("RC-289", "O Vício de Epimeteu", COS_ETI[0], COS_ETI[1], P, ["B020"], "RC-086; RC-145; RC-283; RC-099", False),
    ("RC-290", "Cuidado com o 'Ide e Pregai'", COS_ETI[0], COS_ETI[1], P, ["B020"], "RC-072; RC-099; RC-094; RC-086", False),
    ("RC-291", "Fim do Silêncio de Pandora", EVE_ERA[0], EVE_ERA[1], P, ["B020"], "RC-086; RC-094; RC-071; RC-099", False),

    # ---- Novos termos de B021 (obra primária: Tempos Difíceis no Olimpo, 2022)
    ("RC-292", "Telos (de um deus)", TER_GRE[0], TER_GRE[1], P, ['B021', 'P2024-09-29'], 'RC-293; RC-145; RC-297; RC-094', True),
    ("RC-293", "Timé (de um deus)", TER_GRE[0], TER_GRE[1], P, ['B021', 'P2024-09-29'], 'RC-292; RC-145; RC-294; RC-094; RC-269; RC-736; RC-072', True),
    ("RC-294", "Eon de Khaos (Universo de Caos)", LOK_REG[0], LOK_REG[1], P, ['B021', 'P2026-07-30'], "RC-284; RC-106; RC-077; RC-038", True),
    ("RC-295", "Drama do Fechamento dos Portais", EVE_CAT[0], EVE_CAT[1], P, ['B021', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-09-29'], 'RC-296; RC-145; RC-070; RC-106; RC-694; RC-571', True),
    ("RC-296", "Pitonisas e Oráculos (Apolo/Delfos)", COS_ESP[0], COS_ESP[1], P, ["B021", 'P2024-04-13'], "RC-295; RC-145; RC-099", False),
    ("RC-297", "Era dos Humanos (Zeus e a)", EVE_ERA[0], EVE_ERA[1], P, ["B021", 'P2025-11-29', 'B087', 'B088'], "RC-145; RC-300; RC-099; RC-094", True),
    ("RC-298", "Descendência de Pirra (Pirra e Deucalião)", GEN_HUM[0], GEN_HUM[1], P, ['B021', 'P2024-11-09', 'B087', 'B088', 'B089'], 'RC-303; RC-304; RC-086; RC-301; RC-099', True),
    ("RC-299", "Kalil Kadmon (nome demo de Pandora)", SER_DEC[0], SER_DEC[1], P, ["B021", 'P2024-08-03', 'B089'], "RC-086; RC-118; RC-145", True),
    ("RC-300", "Dissolução da Tríade (2015–2017)", EVE_ERA[0], EVE_ERA[1], P, ['B021', 'B022', 'P2022-12-17', 'P2024-11-30'], 'RC-104; RC-135; RC-102; RC-037; RC-155; RC-571', False),
    ("RC-301", "Prometeu (titã)", SER_DEC[0], SER_DEC[1], P, ['B020', 'B021', 'P2025-02-16', 'P2024-11-09', 'P2025-06-14', 'B087', 'B088', 'B089'], 'RC-302; RC-145; RC-086; RC-304', True),
    ("RC-302", "Epimeteu (titã)", SER_DEC[0], SER_DEC[1], P, ['B020', 'B021', 'P2025-02-16', 'P2024-11-09', 'P2025-06-14', 'P2024-08-03', 'B087', 'B088', 'B089'], 'RC-301; RC-145; RC-086; RC-303', True),
    ("RC-303", "Pirra", SER_DEC[0], SER_DEC[1], P, ['B021', 'P2024-11-09', 'B087', 'B088', 'B089'], 'RC-298; RC-302; RC-086; RC-304', True),
    ("RC-304", "Deucalião", SER_DEC[0], SER_DEC[1], P, ['B021', 'P2024-11-09'], 'RC-298; RC-301; RC-303', False),
    ("RC-305", "Têmis", SER_DEC[0], SER_DEC[1], P, ["B021"], "RC-145; RC-027; RC-094", False),
    ("RC-306", "Apolo", SER_DEC[0], SER_DEC[1], P, ["B021", "B060", 'P2024-04-13'], "RC-145; RC-296; RC-094", False),
    ("RC-307", "Hefesto", SER_DEC[0], SER_DEC[1], P, ["B020", "B021", "B060", 'B087', 'B088'], "RC-145; RC-086; RC-285", True),

    # ---- Novos termos de B022 (obra primária: Inquisição Trimurtiana — Tempo de Apostasia)
    ("RC-308", "Adhytia (nível hierárquico)", SER_LOG[0], SER_LOG[1], P, ["B022"], "RC-104; RC-311; RC-011; RC-094", True),
    ("RC-309", "Ordem dos Indecifráveis", SER_LOG[0], SER_LOG[1], P, ["B022"], "RC-308; RC-311; RC-104", False),
    ("RC-310", "Adhyshprabrajna (Adhy que caiu)", SER_DIV[0], SER_DIV[1], P, ['B022', 'B051', 'P2021-12-04'], "RC-152; RC-037; RC-013; RC-094", True),
    ("RC-311", "Adhyagya (formas espirituais Adhy)", SER_LOG[0], SER_LOG[1], P, ["B022"], "RC-012; RC-308; RC-309; RC-102; RC-135", True),
    ("RC-312", "Criação Bipartida", COS_DIM[0], COS_DIM[1], P, ['B022', 'P2024-11-30'], 'RC-106; RC-107; RC-167; RC-094', False),
    ("RC-313", "Tempo de Apostasia", EVE_ERA[0], EVE_ERA[1], P, ["B022"], "RC-104; RC-300; RC-314; RC-094", False),
    ("RC-314", "Fenômenos Denunciadores do Fim", EVE_PRO[0], EVE_PRO[1], P, ['B022', 'P2025-03-15'], 'RC-313; RC-300; RC-104; RC-094; RC-572; RC-578; RC-690', True),
    ("RC-315", "O Fim da Lila", EVE_GUE[0], EVE_GUE[1], P, ['B022', 'P2024-11-30'], 'RC-075; RC-104; RC-300; RC-313', False),
    ("RC-316", "Decifra-me ou Devoro (hábito demo)", COS_ETI[0], COS_ETI[1], P, ["B022", 'P2025-06-14'], "RC-049; RC-104; RC-075", False),
    ("RC-317", "Esgotamento e Solidão (dos Trimurtianos)", COS_PRO[0], COS_PRO[1], P, ["B022"], "RC-104; RC-313; RC-300", False),
    ("RC-318", "A Estranha Autorrealização de Shiva", EVE_MIS[0], EVE_MIS[1], P, ["B022"], "RC-102; RC-313; RC-104", False),

    # ---- Novos termos de B023 (obra primária: O Dharma e as Castas Hindus)
    ("RC-319", "Fator Dharma", COS_LEI[0], COS_LEI[1], P, ['B023', 'P2024-11-30'], 'RC-320; RC-322; RC-104; RC-075; RC-094', True),
    ("RC-320", "Senhores do Dharma (= Senhores da Lila / Trimurti)", SER_DIV[0], SER_DIV[1], P, ['B023', 'P2024-11-30'], 'RC-104; RC-075; RC-319; RC-094', True),
    ("RC-321", "Castas Trimurtianas", GEN_HUM[0], GEN_HUM[1], P, ['B023', 'P2024-11-30'], 'RC-322; RC-319; RC-104; RC-094; RC-586', True),
    ("RC-322", "Dharma e Castas (origem demo)", TER_SAN[0], TER_SAN[1], P, ['B023', 'P2024-11-30'], 'RC-319; RC-321; RC-049; RC-094; RC-586', False),
    ("RC-323", "Entroncamentos Genéticos Intersiderais", PRO_BIO[0], PRO_BIO[1], P, ['B023', 'P2025-02-16', 'P2024-11-30', 'P2024-09-29'], 'RC-324; RC-036; RC-082; RC-024; RC-099; RC-094', True),
    ("RC-324", "Grupos de Entroncamento (1-4)", PRO_BIO[0], PRO_BIO[1], P, ["B023"], "RC-323; RC-036; RC-186; RC-082; RC-024; RC-099", False),
    ("RC-325", "Genética Totalitária", COS_LEI[0], COS_LEI[1], P, ['B023', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29'], 'RC-326; RC-284; RC-001; RC-099; RC-094; RC-727', True),
    ("RC-326", "Povos Escolhidos (ariano, judeu, árabe)", GEN_HUM[0], GEN_HUM[1], P, ['B023', 'P2024-11-30', 'P2024-04-13'], 'RC-325; RC-270; RC-001; RC-099', False),
    ("RC-327", "Homo hierarchicus", SER_HUM[0], SER_HUM[1], P, ["B023"], "RC-099; RC-321; RC-325; RC-094", False),
    ("RC-328", "Imperativo Categórico da Moral", COS_ETI[0], COS_ETI[1], P, ['B023', 'P2026-07-30', 'P2026-04-02', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-231; RC-253; RC-094; RC-099; RC-620; RC-705; RC-720; RC-722', True),
    ("RC-329", "Kumari Kandan (tradição)", LOK_TER[0], LOK_TER[1], P, ['B023', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-04-13'], 'RC-321; RC-010; RC-099; RC-102; RC-414', True),
    ("RC-330", "Civilização Saraswati", LOK_TER[0], LOK_TER[1], P, ["B023"], "RC-321; RC-099; RC-094", False),
    ("RC-331", "Ra-Atom / Og-mi (nomes do Criador)", TER_OUT[0], TER_OUT[1], P, ["B023", "B060"], "RC-284; RC-001; RC-094", False),

    # ---- Novos termos de B048 (obra primária: Favor Divino, 2013)
    ("RC-332", "Favor Divino (conceito invertido)", COS_ETI[0], COS_ETI[1], P, ['B048', 'B041', 'B034', 'B036', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29', 'P2024-04-14', 'P2025-06-14', 'P2024-03-02'], 'RC-063; RC-333; RC-041; RC-099; RC-094; RC-716; RC-529', True),
    ("RC-333", "Democracia do Amor da Deidade", COS_ETI[0], COS_ETI[1], P, ["B048"], "RC-047; RC-334; RC-052; RC-094", True),
    ("RC-334", "Teocracia da Doença de uma Divindade", COS_ETI[0], COS_ETI[1], P, ['B048', 'B037', 'P2024-11-30'], 'RC-041; RC-333; RC-001; RC-094', True),
    ("RC-335", "Lavagem Cerebral (condicionamento)", COS_ETI[0], COS_ETI[1], P, ['B048', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-03-03', 'P2026-08-04'], 'RC-099; RC-176; RC-041; RC-094; RC-702', True),
    ("RC-336", "Ética da Sobrevivência de Javé", COS_ETI[0], COS_ETI[1], P, ['B048', 'P2024-11-30'], 'RC-041; RC-099; RC-001; RC-094', False),
    ("RC-337", "Humanos: uma simples Experiência Biológica", COS_PRO[0], COS_PRO[1], P, ['B048', 'P2024-11-30'], 'RC-099; RC-041; RC-094; RC-578', False),
    ("RC-338", "O Reconhecimento que nunca veio", COS_ETI[0], COS_ETI[1], P, ["B048"], "RC-041; RC-099; RC-094; RC-332", False),
    ("RC-339", "A Difícil Cobrança sobre os Humanos", COS_ETI[0], COS_ETI[1], P, ["B048"], "RC-041; RC-099; RC-336; RC-094", False),
    ("RC-340", "Atores de uma Peça Incompreensível", COS_ETI[0], COS_ETI[1], P, ["B048"], "RC-099; RC-041; RC-167; RC-094", False),
    ("RC-341", "Ferramentas do Favor Divino (religiões e pensadores)", COS_ESP[0], COS_ESP[1], P, ['B048', 'P2024-11-09', 'P2024-09-29'], 'RC-190; RC-332; RC-099; RC-094; RC-723', False),

    # ---- Novos termos da TRILOGIA QUEDA E ASCENSÃO ESPIRITUAL (B003 Livro I, B025 Livro II, B026 Livro III)
    ("RC-342", "Quarentena Sideral / Cósmica", EVE_GUE[0], EVE_GUE[1], P, ['B003', 'B025', 'B026', 'B042', 'P2024-07-13'], 'RC-070; RC-090; RC-003; RC-094', True),
    ("RC-343", "Portal Cósmico (destinação do Planeta Azul)", LOK_REG[0], LOK_REG[1], P, ["B003", "B026"], "RC-090; RC-342; RC-094; RC-107", False),
    ("RC-344", "Transição Planetária", EVE_ERA[0], EVE_ERA[1], P, ['B003', 'B025', 'B042', 'P2022-12-17', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-003; RC-342; RC-094; RC-005; RC-573', False),
    ("RC-345", "Sentimento Luciferiano", COS_ETI[0], COS_ETI[1], P, ["B003"], "RC-078; RC-002; RC-342; RC-094", False),
    ("RC-346", "Jeová (grafia da trilogia)", SER_DIV[0], SER_DIV[1], P, ['B003', 'B025', 'P2024-11-30'], 'RC-001; RC-284; RC-094', True),
    ("RC-347", "Projeto Terra", EVE_MIS[0], EVE_MIS[1], P, ['B026', 'B019', 'P2024-11-30'], 'RC-090; RC-342; RC-099; RC-094', False),
    ("RC-348", "Roteiro do Exílio", EVE_MIS[0], EVE_MIS[1], P, ["B026"], "RC-342; RC-007; RC-094", False),
    ("RC-349", "Exílios Interplanetários", EVE_GUE[0], EVE_GUE[1], P, ["B003"], "RC-342; RC-007; RC-002; RC-094", False),
    ("RC-350", "Jesus, o Capelino", SER_HUM[0], SER_HUM[1], P, ["B025"], "RC-072; RC-007; RC-039; RC-094", False),
    ("RC-351", "Mestres de Capela", SER_HUM[0], SER_HUM[1], P, ["B025"], "RC-350; RC-039; RC-094", False),
    ("RC-352", "A Segunda Grande Vinda", EVE_PRO[0], EVE_PRO[1], P, ["B025"], "RC-005; RC-072; RC-094", False),
    ("RC-353", "Ilha Cósmica (mundos rebelados)", LOK_REG[0], LOK_REG[1], P, ["B003"], "RC-342; RC-002; RC-070; RC-094", False),
    ("RC-354", "Trilogia Queda e Ascensão Espiritual", TEC_ESC[0], TEC_ESC[1], P, ["B003", "B025", "B026"], "RC-003; RC-025; RC-026; RC-094", False),

    # ---- Novos termos de B005 (obra primária: Fator Extraterrestre, 2004)
    ("RC-355", "Fator Extraterrestre (o Elo Perdido)", COS_PRO[0], COS_PRO[1], P, ["B005", "B042"], "RC-098; RC-020; RC-094; RC-099", True),
    ("RC-356", "Fonte da Vida (metáfora da ilha/oceano)", COS_COG[0], COS_COG[1], P, ["B005"], "RC-148; RC-107; RC-094; RC-033", False),
    ("RC-357", "Confederações de Mundos", GEN_EXT[0], GEN_EXT[1], P, ["B005"], "RC-098; RC-094; RC-107; RC-059", True),
    ("RC-358", "Terra de Ninguém (cósmica)", LOK_REG[0], LOK_REG[1], P, ["B005"], "RC-357; RC-070; RC-094; RC-099", False),
    ("RC-359", "Abduções e Reparo Espiritual", PRO_ESP[0], PRO_ESP[1], P, ['B005', 'P2025-02-16'], 'RC-098; RC-094; RC-099; RC-698', True),
    ("RC-360", "Atmosferizar a Lua ou Marte (Opção Final)", EVE_MIS[0], EVE_MIS[1], P, ["B005"], "RC-094; RC-099; RC-107", False),
    ("RC-361", "Antropocentrismo (crítica)", COS_ETI[0], COS_ETI[1], P, ["B005"], "RC-099; RC-094; RC-231", False),
    ("RC-362", "Apego aos Conceitos Terrenos", COS_ETI[0], COS_ETI[1], P, ["B005"], "RC-099; RC-094; RC-361", False),
    ("RC-363", "Ótica e Ética Cósmicas", COS_ETI[0], COS_ETI[1], P, ["B005"], "RC-094; RC-099; RC-253", False),
    ("RC-364", "A Missão do Mestre", EVE_MIS[0], EVE_MIS[1], P, ["B005", "B042"], "RC-072; RC-094; RC-005", False),

    # ---- Novos termos das OBRAS SOBRE JESUS (B011 Transfiguração, B049 Nietzsche, B043 Druida)
    ("RC-365", "O Fator Judas", EVE_MIS[0], EVE_MIS[1], P, ['B011', 'P2026-04-02', 'P2025-10-25'], "RC-138; RC-072; RC-236; RC-094; RC-647", True),
    ("RC-366", "O Enigma da Transfiguração", EVE_PRO[0], EVE_PRO[1], P, ["B011"], "RC-072; RC-367; RC-094; RC-214", True),
    ("RC-367", "Alteração Vibratória (Transfiguração)", PRO_FIS[0], PRO_FIS[1], P, ['B011', 'P2025-02-15'], 'RC-366; RC-072; RC-094; RC-713', False),
    ("RC-368", "Assessoria Cósmica (equipes espirituais de Jesus)", SER_LOG[0], SER_LOG[1], P, ['B011', 'P2025-02-15'], 'RC-072; RC-214; RC-094; RC-100', False),
    ("RC-369", "Nietzsche como 'Amigo da Intenção de Jesus'", SER_HUM[0], SER_HUM[1], P, ['B049', 'P2024-11-09'], 'RC-072; RC-370; RC-371; RC-094', True),
    ("RC-370", "A Criação de Ídolos para a Humanidade", COS_ETI[0], COS_ETI[1], P, ["B049"], "RC-099; RC-369; RC-094; RC-041", False),
    ("RC-371", "A Fé de Jesus e a Razão de Nietzsche", COS_ETI[0], COS_ETI[1], P, ["B049"], "RC-072; RC-369; RC-253; RC-094", True),
    ("RC-372", "O Ser Humano Emancipado", COS_PRO[0], COS_PRO[1], P, ['B049', 'P2026-07-30', 'P2025-02-15'], 'RC-099; RC-253; RC-231; RC-094; RC-702; RC-708', False),
    ("RC-373", "Os 20 Anos de Jesus entre os Celtas", EVE_MIS[0], EVE_MIS[1], P, ["B043"], "RC-072; RC-374; RC-375; RC-094", True),
    ("RC-374", "Mordon (o Druida da Montanha)", SER_HUM[0], SER_HUM[1], P, ["B043"], "RC-373; RC-375; RC-072; RC-094", False),
    ("RC-375", "Druidas Celtas (contexto RC)", SER_HUM[0], SER_HUM[1], P, ["B043"], "RC-373; RC-374; RC-094", False),
    ("RC-376", "José de Arimatéia (no corpus RC)", SER_HUM[0], SER_HUM[1], P, ["B043", "B011", 'P2026-08-04'], "RC-373; RC-072; RC-094", False),
    ("RC-377", "Brendiver e Dolman (personagens celtas)", SER_HUM[0], SER_HUM[1], P, ["B043"], "RC-373; RC-374; RC-094", False),

    # ---- Novos termos de B041 (obra primária: A Rebelião dos Elétrons e o Código de Vida do Criador, 2018)
    ("RC-378", "A Rebelião dos Elétrons", EVE_GUE[0], EVE_GUE[1], P, ['B041', 'B024', 'P2024-05-04', 'P2025-03-15', 'P2024-11-30', 'P2024-11-09', 'P2024-03-03', 'P2024-04-14'], 'RC-161; RC-162; RC-379; RC-153; RC-094; RC-638; RC-690; RC-693; RC-434; RC-646', True),
    ("RC-379", "Dança dos Elétrons", PRO_FIS[0], PRO_FIS[1], P, ['B041', 'P2024-05-04'], "RC-162; RC-378; RC-380; RC-094", True),
    ("RC-380", "Imanência e Transcendência (Upanishades)", COS_LEI[0], COS_LEI[1], P, ["B041"], "RC-379; RC-162; RC-094; RC-210", False),
    ("RC-381", "Ressonância Mórfica (agente da rebelião)", COS_LEI[0], COS_LEI[1], P, ['B041', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-04-14'], 'RC-378; RC-162; RC-106; RC-094; RC-711; RC-724', False),
    ("RC-382", "A Vida do CFD de Javé no Ser Humano", COS_LEI[0], COS_LEI[1], P, ['B041', 'B034', 'P2024-09-29'], 'RC-040; RC-099; RC-332; RC-094', True),
    ("RC-383", "Roteiro do Absurdo Implantado na Criação", COS_PRO[0], COS_PRO[1], P, ["B041"], "RC-167; RC-378; RC-094; RC-041", False),
    ("RC-384", "Proposta de um Humano Terrestre aos Elétrons", COS_ETI[0], COS_ETI[1], P, ["B041"], "RC-378; RC-071; RC-332; RC-094", False),
    ("RC-385", "Egrégora (circuito dos elétrons rebeldes)", COS_ESP[0], COS_ESP[1], P, ['B041', 'B074', 'B075', 'P2026-07-30', 'P2025-03-15'], 'RC-378; RC-384; RC-094; RC-475', False),
    ("RC-386", "Memórias para Javé", COS_LEI[0], COS_LEI[1], P, ['B041', 'P2024-09-29'], 'RC-161; RC-378; RC-041; RC-094', False),
    ("RC-387", "Fragmentação do Poder Mental da Divindade", COS_COG[0], COS_COG[1], P, ['B041', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09'], 'RC-041; RC-167; RC-152; RC-094; RC-638', False),

    # ---- Novos termos de B006 (obra primária: Nos Bastidores da Luz I — obra mediúnica, 2000)
    ("RC-388", "Grupo Atlan", GEN_EXT[0], GEN_EXT[1], P, ["B006", "B031", "B044"], "RC-389; RC-071; RC-094; RC-100", True),
    ("RC-389", "Casa de Lucas (origem do Grupo Atlan)", LOK_TER[0], LOK_TER[1], P, ["B006"], "RC-388; RC-071; RC-094", False),
    ("RC-390", "Espíritos comunicantes do Grupo Atlan", SER_LOG[0], SER_LOG[1], P, ["B006"], "RC-388; RC-100; RC-094", False),
    ("RC-391", "Mesmice Espiritual", COS_ETI[0], COS_ETI[1], P, ["B006"], "RC-099; RC-100; RC-094", False),
    ("RC-392", "Reforma Íntima (tema do Grupo Atlan)", COS_ESP[0], COS_ESP[1], P, ['B006', 'B074', 'B075', 'P2025-03-15'], 'RC-100; RC-099; RC-094; RC-190', False),
    ("RC-393", "Enéas (espírito comunicante)", SER_HUM[0], SER_HUM[1], P, ["B006"], "RC-390; RC-094", False),
    ("RC-394", "Mandreya Ramataiana (espírito comunicante)", SER_HUM[0], SER_HUM[1], P, ["B006"], "RC-390; RC-094", False),

    # ---- Novos termos de B050 (Guia das Eras Universais — Mapa; obra complementar do filho de JVE)
    ("RC-395", "Ragnarok em Marte", EVE_CAT[0], EVE_CAT[1], P, ['B050', 'B060', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03', 'P2024-03-02', 'P2025-11-29'], 'RC-145; RC-102; RC-300; RC-094; RC-471; RC-694; RC-611; RC-470; RC-730; RC-742; RC-454; RC-467', True),
    ("RC-396", "Kvasir e Freya (Vanir/Aesir)", SER_DEC[0], SER_DEC[1], P, ['B050', 'B060', 'P2024-11-30', 'P2024-03-02'], 'RC-395; RC-094; RC-049; RC-454; RC-611', False),
    ("RC-397", "Tirthankaras (Rishabh Dev, Jina Mahavira)", SER_HUM[0], SER_HUM[1], P, ['B050', 'P2025-10-25', 'P2025-02-16', 'P2024-02-03'], 'RC-094; RC-099; RC-655; RC-697', False),
    ("RC-398", "Thuata de Dannan", SER_DEC[0], SER_DEC[1], P, ["B050", "B060", 'P2024-04-13', 'P2024-02-03'], "RC-094; RC-373; RC-068", False),
    ("RC-399", "Dwarka (submersa)", LOK_TER[0], LOK_TER[1], P, ["B050"], "RC-094; RC-010", False),
    ("RC-400", "Foz Côa / FOXP2 (símbolos)", PRO_BIO[0], PRO_BIO[1], P, ['B050', 'B061', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03'], 'RC-099; RC-094; RC-577; RC-614; RC-619; RC-710', True),
    ("RC-401", "Família Demolle (biodemos)", GEN_EXT[0], GEN_EXT[1], P, ["B050"], "RC-036; RC-094", False),
    ("RC-402", "Halos de Poder (demos)", TEC_DIS[0], TEC_DIS[1], P, ["B050"], "RC-049; RC-094", False),
    ("RC-403", "Colegiado Druídico", GEN_EXT[0], GEN_EXT[1], P, ["B050", "B052"], "RC-375; RC-373; RC-094", False),

    # ---- Novos termos de B027 (obra primária: Nos Céus da Grécia — AMOSTRA PARCIAL)
    ("RC-404", "Sentido Gradualístico das Leis da Evolução Cósmica", COS_LEI[0], COS_LEI[1], P, ['B027', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-094; RC-003; RC-059; RC-693; RC-720', True),
    ("RC-405", "Alvorecer de Aquário", EVE_PRO[0], EVE_PRO[1], P, ['B027', 'P2022-12-17'], 'RC-094; RC-003; RC-569; RC-571; RC-591; RC-592', False),
    ("RC-406", "Diálogos de Sócrates, Platão e Aristóteles (nos Céus da Grécia)", TEC_ESC[0], TEC_ESC[1], P, ["B027"], 'RC-094; RC-003; RC-226; RC-722', False),
    ("RC-407", "Reencarnação iminente da grande leva de espíritos", COS_PRO[0], COS_PRO[1], P, ["B027"], "RC-100; RC-099; RC-094; RC-003", False),

    # ---- Novos termos de B051 (Diagrama Geral de Ligações — obra complementar de alunos, revisada)
    ("RC-408", "ADHYMAVATANA (nome completo de Mavatna/Vishnu)", SER_DIV[0], SER_DIV[1], P, ['B051', 'B060', 'B061', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2024-11-30'], 'RC-135; RC-014; RC-013; RC-094; RC-604', True),
    ("RC-409", "ADHYSAVNA (nome completo de Savna/Shiva)", SER_DIV[0], SER_DIV[1], P, ['B051', 'B060', 'B061', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2024-11-30'], 'RC-102; RC-014; RC-013; RC-094', True),
    ("RC-410", "ADHYPRABRAJNA (grafia do diagrama)", SER_DIV[0], SER_DIV[1], P, ['B051', 'B060', 'B061', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2024-11-30'], 'RC-310; RC-152; RC-037; RC-094; RC-604', False),
    ("RC-411", "Gênero Adhy (147 seres, 5 espécies)", SER_LOG[0], SER_LOG[1], P, ['B051', 'B022', 'P2021-12-04', 'P2024-05-04', 'P2025-10-25', 'P2024-11-30', 'P2024-11-09'], 'RC-011; RC-012; RC-013; RC-014; RC-015; RC-016; RC-094; RC-455; RC-605; RC-087; RC-635', True),
    ("RC-412", "Emissários Humanos (Enoch, Abraão, Moisés, Jesus)", SER_HUM[0], SER_HUM[1], P, ["B051", "B060", "B061"], 'RC-094; RC-072; RC-270', False),
    ("RC-413", "Hara (avatar de Shiva)", SER_EXT[0], SER_EXT[1], P, ["B051", "B024"], "RC-102; RC-073; RC-094", False),
    ("RC-414", "Krishna (avatar de Vishnu/Shiva)", SER_EXT[0], SER_EXT[1], P, ['B051', 'B023', 'B036', 'B061', 'P2025-02-16', 'P2024-11-30', 'P2024-03-02', 'P2023-12-02', 'P2024-09-28', 'P2025-11-29'], 'RC-135; RC-102; RC-094; RC-183; RC-714; RC-717; RC-584; RC-016; RC-009; RC-757; RC-425; RC-073; RC-694; RC-582; RC-722', True),
    ("RC-415", "Colapso da Matriz Quântica (3 níveis)", COS_DIM[0], COS_DIM[1], P, ['B051', 'P2021-12-04', 'P2024-05-04', 'P2025-03-15', 'P2025-02-15', 'P2024-11-09'], 'RC-059; RC-060; RC-061; RC-167; RC-094; RC-602; RC-690', True),

    # ---- Novos termos de B034 (obra primária: Cartas a Javé, 2014 — Ellam & Mônica Camargo)
    ("RC-416", "Cartas a Javé (obra e diálogo)", TEC_ESC[0], TEC_ESC[1], P, ["B034", "B036"], "RC-001; RC-417; RC-418; RC-094", True),
    ("RC-417", "Resposta de Javé (em 1ª pessoa)", TEC_ESC[0], TEC_ESC[1], P, ["B034"], "RC-001; RC-416; RC-419; RC-094", True),
    ("RC-418", "Terminal Nervoso do Criador (humano)", COS_LEI[0], COS_LEI[1], P, ['B034', 'B036', 'P2025-03-15', 'P2025-02-15'], 'RC-099; RC-041; RC-217; RC-094; RC-708', False),
    ("RC-419", "Sou eu que vivo em vocês (Javé)", COS_PRO[0], COS_PRO[1], P, ['B034', 'P2024-11-30'], 'RC-001; RC-382; RC-332; RC-094', False),
    ("RC-420", "Mônica Camargo (autora das cartas)", SER_HUM[0], SER_HUM[1], P, ["B034"], "RC-416; RC-071; RC-094", False),

    # ---- Novos termos de B036 (obra primária: As Memórias de Javé — crônicas em 1ª pessoa)
    ("RC-421", "As Memórias de Javé (crônicas)", TEC_ESC[0], TEC_ESC[1], P, ["B036"], "RC-001; RC-422; RC-423; RC-094", True),
    ("RC-422", "Ser-Criador fracassado (autoconfissão de Javé)", COS_PRO[0], COS_PRO[1], P, ['B036', 'B037', 'P2024-11-30', 'P2024-11-09'], 'RC-001; RC-041; RC-245; RC-094', True),
    ("RC-423", "Advogado de Acusação (Ellam × Javé)", SER_HUM[0], SER_HUM[1], P, ["B036"], "RC-071; RC-001; RC-094", False),
    ("RC-424", "Linhagem dos Escolhidos (Adão, Enoch, Abraão, Jacó)", GEN_HUM[0], GEN_HUM[1], P, ['B036', 'B060', 'B061', 'P2022-12-17', 'P2025-10-25', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-04-13', 'P2026-08-04', 'P2024-02-03'], 'RC-270; RC-001; RC-217; RC-094; RC-579; RC-594', True),
    ("RC-425", "Krishna como 'pretenso Keshava'", SER_EXT[0], SER_EXT[1], P, ['B036', 'P2025-02-16', 'P2024-11-30'], 'RC-414; RC-073; RC-104; RC-094; RC-714; RC-717; RC-722', False),
    ("RC-426", "Javé sem avatares ('Não tenho isto!')", SER_DIV[0], SER_DIV[1], P, ['B036', 'B016', 'P2022-12-17', 'P2024-11-30'], 'RC-001; RC-016; RC-102; RC-135; RC-094', True),
    ("RC-427", "Criatura-teste (estágio avançado)", COS_PRO[0], COS_PRO[1], P, ["B036"], "RC-099; RC-418; RC-094", False),
    ("RC-428", "Tempo-limite (transição crítica de Javé)", EVE_ERA[0], EVE_ERA[1], P, ['B036', 'P2024-11-30', 'P2024-09-29'], 'RC-001; RC-300; RC-094', False),
    ("RC-429", "Javé alimenta-se do senso crítico humano", COS_ETI[0], COS_ETI[1], P, ['B036', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29'], 'RC-001; RC-231; RC-253; RC-094', False),

    # ---- Novos termos de B040 (obra primária: Homo Sapiens — da Guerra ao Esporte, 2014)
    ("RC-430", "Esporte como evolução da Guerra", COS_PRO[0], COS_PRO[1], P, ["B040"], "RC-099; RC-217; RC-094; RC-040", True),
    ("RC-431", "Guerreiro ao Atleta (transição)", COS_PRO[0], COS_PRO[1], P, ["B040"], "RC-430; RC-099; RC-094", False),
    ("RC-432", "Agressividade canalizada (DNA doentio)", COS_LEI[0], COS_LEI[1], P, ['B040', 'B052', 'P2024-11-30'], 'RC-217; RC-099; RC-040; RC-094', False),
    # ---- Novos termos de B052 (obra primária: Homoafetividade — O Segredo Perdido do Éden, 2016)
    ("RC-433", "Força de Atração Sexual (anterior à polaridade)", COS_LEI[0], COS_LEI[1], P, ['B052', 'P2024-11-30', 'P2024-09-29', 'P2024-08-03'], 'RC-049; RC-099; RC-094', True),
    ("RC-434", "Homoafetividade (resquício da força original)", COS_PRO[0], COS_PRO[1], P, ['B052', 'P2025-03-15', 'P2024-11-30', 'P2024-03-03'], 'RC-433; RC-099; RC-094; RC-378', True),
    ("RC-435", "O Segredo Perdido do Éden", COS_PRO[0], COS_PRO[1], P, ["B052", 'P2024-03-03'], "RC-242; RC-433; RC-094", False),
    ("RC-436", "Heber (patriarca pós-dilúvio)", SER_HUM[0], SER_HUM[1], P, ['B052', 'B060', 'P2022-12-17', 'P2025-10-25', 'P2024-11-30'], 'RC-270; RC-094; RC-437; RC-585', False),
    ("RC-437", "Joctan e Faleg (filhos de Heber)", SER_HUM[0], SER_HUM[1], P, ['B052', 'P2022-12-17', 'P2025-10-25', 'P2024-11-30', 'P2021-03-27'], 'RC-436; RC-270; RC-094; RC-424', True),
    ("RC-438", "Tubal (filho de Jafé, centro de comércio)", SER_HUM[0], SER_HUM[1], P, ['B052', 'P2024-11-30'], 'RC-270; RC-094', False),
    ("RC-439", "Os Magos do Norte", SER_HUM[0], SER_HUM[1], P, ["B052"], "RC-094; RC-068; RC-403", False),
    ("RC-440", "A Sina dos Portadores", EVE_PRO[0], EVE_PRO[1], P, ["B052"], "RC-433; RC-094; RC-099", False),
    ("RC-441", "Mistérios Dionisíacos", COS_ESP[0], COS_ESP[1], P, ["B052"], "RC-094; RC-433; RC-049", False),
    ("RC-442", "Família Yel", GEN_EXT[0], GEN_EXT[1], P, ["B057", "B058"], "RC-142; RC-036; RC-039; RC-446; RC-450", True),
    ("RC-443", "Família Mion", GEN_EXT[0], GEN_EXT[1], P, ["B057", "B058"], "RC-074; RC-036; RC-039; RC-446; RC-450", True),
    ("RC-444", "Família Cromon", GEN_EXT[0], GEN_EXT[1], C, ["B059", "B057"], "RC-036; RC-450", False),
    ("RC-445", "Biocoletivos", SER_LOG[0], SER_LOG[1], P, ["B057", "B058"], "RC-036; RC-442; RC-443; RC-450", True),
    ("RC-446", "Processadores Familiares", TEC_DIS[0], TEC_DIS[1], P, ["B057", "B058"], "RC-036; RC-009; RC-442; RC-443", True),
    ("RC-447", "Primeiro Pesquisador (cargo capelino)", COS_LEI[0], COS_LEI[1], P, ["B057", "B058"], "RC-142; RC-442", True),
    ("RC-448", "Deslacre (rompimento dos lacres psíquicos)", PRO_ESP[0], PRO_ESP[1], P, ['B057', 'B058', 'P2022-12-17'], "RC-142; RC-036; RC-445; RC-577", True),
    ("RC-449", "Criaturas-ferramenta", COS_PRO[0], COS_PRO[1], P, ['B057', 'B058', 'P2025-03-15', 'P2021-03-27', 'P2025-11-29'], 'RC-036; RC-099; RC-001; RC-148', True),
    ("RC-450", "Revolta Capelina", EVE_GUE[0], EVE_GUE[1], P, ["B057", "B058"], "RC-002; RC-142; RC-443; RC-444", True),
    ("RC-451", "Universidade de Tau Ceti", LOK_REG[0], LOK_REG[1], P, ["B058"], "RC-103; RC-452; RC-450", True),
    ("RC-452", "Grão-mestre (Sábios de Tau Ceti)", SER_EXT[0], SER_EXT[1], P, ["B058"], "RC-451; RC-103; RC-450", True),
    ("RC-453", "Hostes de Sophia", SER_COL[0], SER_COL[1], P, ["B057", "B058"], "RC-009; RC-450; RC-036", True),
    ("RC-454", "Elm (Moros — ser LM de Tempérion)", SER_LOG[0], SER_LOG[1], P, ['B060', 'P2022-12-17', 'P2021-12-04', 'P2026-07-30', 'P2026-04-02', 'P2025-10-25', 'P2025-06-26', 'P2024-11-30', 'P2024-09-29', 'P2024-07-14', 'P2024-03-02', 'P2024-02-03', 'P2023-05-13', 'P2023-12-02', 'P2025-11-29', 'P2024-08-03'], 'RC-456; RC-071; RC-190; RC-436; RC-396; RC-061; RC-472; RC-604; RC-607; RC-609; RC-611; RC-087; RC-620; RC-608; RC-167; RC-081; RC-658; RC-665; RC-714; RC-715; RC-716; RC-718; RC-467; RC-585; RC-659; RC-770', True),
    ("RC-455", "Pashvnaj (espécie de 43 seres do Gênero Adhy)", SER_COL[0], SER_COL[1], P, ['B060', 'P2021-12-04', 'P2024-05-04'], "RC-152; RC-102; RC-408; RC-087; RC-061; RC-457; RC-411; RC-629", True),
    ("RC-456", "Ser LM (gênero de Tempérion)", SER_LOG[0], SER_LOG[1], P, ['B060', 'P2021-12-04', 'P2024-11-30'], 'RC-092; RC-454; RC-061; RC-472; RC-087; RC-605; RC-607; RC-608; RC-635', True),
    ("RC-457", "Sarasvati (consorte de Brahma, Tridevi)", SER_DIV[0], SER_DIV[1], P, ['B060', 'P2021-12-04', 'P2024-07-14'], 'RC-455; RC-037; RC-104; RC-610', False),
    ("RC-458", "Lakshimi (consorte de Vishnu, Tridevi)", SER_DIV[0], SER_DIV[1], P, ['B060', 'P2021-12-04', 'P2024-07-14'], 'RC-455; RC-408; RC-104; RC-610', False),
    ("RC-459", "Parvathi (consorte de Shiva, Tridevi)", SER_DIV[0], SER_DIV[1], P, ['B060', 'P2021-12-04', 'P2024-07-14'], 'RC-455; RC-409; RC-104; RC-610', False),
    ("RC-460", "Marduk (= Ra; Anunnaki filho de Enki)", SER_EXT[0], SER_EXT[1], P, ['B060', 'P2022-12-17', 'P2023-12-02', 'P2021-03-27'], "RC-024; RC-331; RC-583; RC-589", True),
    ("RC-461", "Ninmah (Anunnaki geneticista)", SER_EXT[0], SER_EXT[1], P, ["B060", 'P2021-03-27'], "RC-024; RC-134", True),
    ("RC-462", "Oannes (filho de Ostronomos)", SER_EXT[0], SER_EXT[1], P, ["B060"], "RC-232; RC-024", False),
    ("RC-463", "Hermes Trismegisto (= Ningishzidda/Thoth/Quetzalcóatl)", SER_HUM[0], SER_HUM[1], P, ["B060", 'P2023-12-02', 'P2025-11-29'], "RC-024; RC-259; RC-092", True),
    ("RC-464", "Inanna (= Danu; Anunnaki)", SER_EXT[0], SER_EXT[1], P, ["B060"], "RC-024; RC-398", False),
    ("RC-465", "Asuras (= Titãs)", SER_DEC[0], SER_DEC[1], P, ['B060', 'B061', 'P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-09-29', 'P2024-04-13', 'B087', 'B088'], 'RC-301; RC-302; RC-145; RC-696; RC-700; RC-701; RC-734', True),
    ("RC-466", "Bebida dos Deuses (Ambrosia/Amrita/Soma)", TER_OUT[0], TER_OUT[1], P, ['B060', 'P2025-02-16', 'P2024-08-03'], 'RC-049; RC-145', False),
    ("RC-467", "Moiras / Nornes / Parcas (destino)", COS_PRO[0], COS_PRO[1], P, ['B060', 'P2025-06-26', 'P2025-02-16', 'P2024-11-30'], 'RC-145; RC-300; RC-658; RC-454; RC-714; RC-716', True),
    ("RC-468", "Ein Sof (Prabrajna na Cabala)", TER_HEB[0], TER_HEB[1], P, ["B060"], "RC-152; RC-261; RC-264", False),
    ("RC-469", "Khorsis (Mundo dos Tronos)", LOK_MUN[0], LOK_MUN[1], P, ["B060"], "RC-061; RC-264", False),
    ("RC-470", "Midgard (Marte + Terra)", LOK_PLA[0], LOK_PLA[1], P, ['B060', 'P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03'], 'RC-395; RC-107; RC-358; RC-730; RC-731; RC-471', True),
    ("RC-471", "Bifrost (Portal interdimensional)", LOK_REG[0], LOK_REG[1], P, ['B060', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03'], 'RC-106; RC-107; RC-343; RC-730; RC-731; RC-395', True),
    ("RC-472", "Tempérion (Archeon de Ereon; setor dos seres LM)", COS_DIM[0], COS_DIM[1], P, ['B060', 'B061', 'P2021-12-04', 'P2024-05-04', 'P2024-11-30'], 'RC-061; RC-087; RC-454; RC-456; RC-473; RC-496; RC-498; RC-596; RC-607; RC-092; RC-608', True),
    ("RC-473", "Lempérion e Terpérion (setores da Espiritualidade Laboratorial)", COS_DIM[0], COS_DIM[1], C, [], "RC-061; RC-472", False),
    ("RC-474", "Arcontes (= Sophias e Indras; Conselho dos 70)", SER_COL[0], SER_COL[1], C, ['B061', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2026-08-04', 'P2023-12-02'], 'RC-004; RC-009; RC-145; RC-480; RC-579; RC-293; RC-494; RC-414; RC-769; RC-770; RC-768', True),
    ("RC-475", "Deva / Aurora (A Grande Deusa)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2026-07-30; RC-622; RC-768'], "RC-286; RC-476; RC-610; RC-621; RC-622; RC-385", True),
    ("RC-476", "En Ma (Emá / Emar — espírito-âncora)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02', 'P2025-10-25', 'P2024-11-30'], 'RC-001; RC-477; RC-009; RC-072; RC-135; RC-620; RC-628; RC-648; RC-037', True),
    ("RC-477", "Ensá (espírito primordial companheiro de En Ma)", SER_DIV[0], SER_DIV[1], C, ["B061"], "RC-476", True),
    ("RC-478", "Chequinhá (veículo/nave de Javé)", TEC_NAV[0], TEC_NAV[1], C, ["B061"], "RC-001", False),
    ("RC-479", "Belial (arconte; 'Satã' do livro de Jó)", SER_DEC[0], SER_DEC[1], C, ['B061', 'P2022-12-17', 'P2026-08-04; RC-286; RC-072'], "RC-474; RC-074", True),
    ("RC-480", "Indra (título de arconte)", SER_LOG[0], SER_LOG[1], C, ['B061', 'P2022-12-17', 'P2025-10-25', 'P2025-02-16', 'P2024-09-29'], 'RC-474; RC-145; RC-696; RC-700; RC-701', True),
    ("RC-481", "Maitreya (Dionísio; forma adiágena de Vishnu)", SER_DIV[0], SER_DIV[1], C, ["B061", 'P2021-03-27'], "RC-408; RC-306", True),
    ("RC-482", "Ialdabaoth (= Javé/Samael/Saklas/Sabaoth)", SER_DIV[0], SER_DIV[1], C, ["B061"], "RC-001; RC-474", True),
    ("RC-483", "Barbelo (Mãe-Pai primordial gnóstica)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2026-04-02', 'P2024-09-28'], "RC-474; RC-647", True),
    ("RC-484", "Anjos ministradores (Usá, Azá, Aziel)", SER_ANJ[0], SER_ANJ[1], C, ["B061"], "RC-001; RC-485", False),
    ("RC-485", "Classes de anjos de Arabot-Ráquia (ofanim, serafins, galgaulim, chashmalim)", SER_ANJ[0], SER_ANJ[1], C, ["B061"], "RC-495; RC-001", True),
    ("RC-486", "Enki (Anunnaki; inoculou o gene FOXP2)", SER_EXT[0], SER_EXT[1], C, ['B061', 'P2022-12-17', 'P2021-12-04', 'P2024-11-09', 'P2024-03-03', 'P2023-12-02', 'P2021-03-27', 'P2024-08-03', 'B089'], 'RC-024; RC-487; RC-400; RC-583; RC-587; RC-727', True),
    ("RC-487", "Enlil (deus sumério, par de Enki)", SER_EXT[0], SER_EXT[1], C, ['B061', 'P2022-12-17', 'P2024-04-13', 'P2021-03-27', 'B089'], "RC-024; RC-486; RC-583; RC-587; RC-588", True),
    ("RC-488", "Nefilins (= Anunnakis)", SER_EXT[0], SER_EXT[1], C, ['B061', 'P2026-08-04', 'P2021-03-27', 'P2024-09-28'], 'RC-024; RC-580', True),
    ("RC-489", "Enoque (sétimo patriarca; levado por Javé)", SER_HUM[0], SER_HUM[1], C, ['B061', 'P2022-12-17', 'P2024-11-30', 'P2024-07-14', 'P2024-04-13', 'P2026-08-04', 'P2024-03-02', 'P2023-12-02'], 'RC-424; RC-495; RC-594; RC-485; RC-671; RC-672', True),
    ("RC-490", "Caim (leitura RC: segundo a nascer)", SER_HUM[0], SER_HUM[1], C, ['B061', 'P2022-12-17', 'P2025-02-16', 'P2024-11-30'], 'RC-001; RC-424; RC-579; RC-594; RC-684', True),
    ("RC-491", "Família Shanlung (13 membros em Alt'Lam Gron)", GEN_EXT[0], GEN_EXT[1], C, ["B061", "B057"], "RC-036; RC-105", False),
    ("RC-492", "Membros da Família Yel (Luziel, Adrax, Breasil, Lupon)", GEN_EXT[0], GEN_EXT[1], C, ["B061"], "RC-442", False),
    ("RC-493", "Os 9 Val dos Corpos Perdidos", GEN_EXT[0], GEN_EXT[1], C, ["B061"], "RC-109; RC-127", False),
    ("RC-494", "Dinastia das Sophias", GEN_DIV[0], GEN_DIV[1], C, ['B061', 'P2026-07-30; RC-474'], "RC-009; RC-474", True),
    ("RC-495", "Arabot-Ráquia (ambiente de Javé; = Araboth)", LOK_MUN[0], LOK_MUN[1], C, ["B061"], "RC-001; RC-485", True),
    ("RC-496", "Ereon (região dos cinco Archeons da Espiritualidade Laboratorial)", LOK_REG[0], LOK_REG[1], C, ['B061', 'P2021-12-04'], "RC-061; RC-087; RC-472; RC-497; RC-498; RC-596; RC-597; RC-598; RC-599", True),
    ("RC-497", "Impérial — erro histórico de STT (ver Perpérion RC-087)", LOK_REG[0], LOK_REG[1], C, ['B061', 'P2021-12-04'], "RC-496; RC-087", True),
    ("RC-498", "Tempérium — variação histórica de Tempérion (ver RC-472)", COS_DIM[0], COS_DIM[1], C, ['B061', 'P2021-12-04'], "RC-496; RC-472; RC-061", True),
    ("RC-499", "Forno de Awaymaion (forno de Vishnu; origem de Olm)", LOK_MUN[0], LOK_MUN[1], C, ["B061"], "RC-408; RC-092", True),
    ("RC-500", "Almaior / Alamaior — erro histórico de STT (ver Forno de Awaymaion RC-499)", LOK_MUN[0], LOK_MUN[1], C, ['B061', 'P2021-12-04', 'ART-2025-08-01'], "RC-499", True),
    ("RC-501", "Conselho dos Cinco (comando da Frota Norte: 3 Val + 2 Yel)", SER_COL[0], SER_COL[1], C, ["B061"], "RC-065; RC-109", False),
    ("RC-502", "Val Aten (último Val de Val-Ha)", SER_EXT[0], SER_EXT[1], C, ["B061"], "RC-109; RC-127", False),
    ("RC-503", "Mavátma / Mavatna / Mavat (Vishnu em condição Adhyatman)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2025-02-16', 'P2024-11-30', 'P2024-03-02'], 'RC-408', False),
    ("RC-504", "Adyadvaivatma / Adimavatma (= Vishnu)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2024-11-30'], 'RC-408', False),
    ("RC-505", "Adyabradagna / Adabradagna (= Brahma/Javé)", SER_DIV[0], SER_DIV[1], C, ['B061', 'P2024-11-30'], 'RC-152', False),
    ("RC-506", "Ekatma (Adam Kadmon — Homem Primordial)", TER_HEB[0], TER_HEB[1], C, ["B061", 'P2024-09-28', 'P2024-08-03'], "RC-264; RC-013", True),
    ("RC-507", "Holodomínio (esfera de influência extrafísica)", COS_DIM[0], COS_DIM[1], C, ['B071'], 'RC-474; RC-061; RC-726', False),
    ("RC-508", "Decência cósmica (ética ellâmica)", COS_ETI[0], COS_ETI[1], C, ['B071', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-253; RC-094; RC-705; RC-711; RC-720; RC-721; RC-722; RC-725', False),
    ("RC-509", "Protagonismo consciencial", COS_PRO[0], COS_PRO[1], C, ['B071', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29'], 'RC-253; RC-226; RC-695; RC-697; RC-703; RC-705; RC-708; RC-722; RC-725', False),
    ("RC-510", "Blindagem cósmica (= quarentena terrestre)", COS_DIM[0], COS_DIM[1], C, ["B071"], "RC-070; RC-342; RC-602", False),
    ("RC-511", "Mêntion (estruturas da mente extrafísica)", PRO_ESP[0], PRO_ESP[1], C, ['B071', 'B074', 'B075', 'P2026-07-30', 'P2024-05-04', 'P2026-04-02'], "RC-106; RC-217", False),
    ("RC-512", "Amnésia espiritual (esquecimento das origens)", COS_ESP[0], COS_ESP[1], C, ["B071", 'ART-2026-08-18'], "RC-407; RC-094", False),
    ("RC-513", "Espiritualidade Errática (4ª faixa manifestada)", COS_DIM[0], COS_DIM[1], C, ['B060', 'B071', 'P2021-12-04', 'P2024-05-04', 'P2025-03-15', 'P2024-11-09', 'P2024-07-14', 'P2024-03-03', 'P2024-04-14', 'P2025-06-14'], 'RC-061; RC-106; RC-107; RC-726', True),
    ("RC-514", "Tikun Cósmico (restabelecimento da Criação)", COS_PRO[0], COS_PRO[1], C, ['B061', 'B071', 'B019', 'B074', 'B075', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04', 'P2025-10-25', 'P2025-06-26', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'ART-2026-08-18', 'P2024-09-28', 'P2024-08-03'], 'RC-003; RC-167; RC-618; RC-638; RC-653; RC-707; RC-231; RC-722; RC-713', True),
    ("RC-515", "Acidente cosmogônico (queda de Prabrajna)", COS_COG[0], COS_COG[1], C, ["B071"], "RC-167; RC-152", False),
    ("RC-516", "Hibridização genética (Nefilim reinterpretado)", PRO_BIO[0], PRO_BIO[1], C, ['B071', 'P2022-12-17', 'P2024-09-29', 'P2021-03-27'], 'RC-488; RC-323; RC-580', True),
    ("RC-517", "Protocolo Mental (padrões organizadores da mente)", PRO_ESP[0], PRO_ESP[1], C, ['B072', 'B074', 'B075', 'P2021-12-04', 'P2026-07-30', 'P2026-04-02', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-02-03', 'P2025-11-29'], 'RC-511; RC-448; RC-217; RC-702; RC-711; RC-712', True),
    ("RC-518", "Genoma Derivado (interação genoma × trajetória)", PRO_BIO[0], PRO_BIO[1], C, ['B072', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29'], 'RC-217; RC-099; RC-693; RC-710; RC-732; RC-558; RC-542', True),
    ("RC-519", "Herança Cósmica (padrões de existências anteriores)", PRO_BIO[0], PRO_BIO[1], C, ['B072', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30'], 'RC-518; RC-407; RC-692; RC-704; RC-716; RC-720', False),
    ("RC-520", "Infecção mental / contágio vibratório", PRO_ESP[0], PRO_ESP[1], C, ['B072', 'P2025-02-15'], 'RC-448; RC-381; RC-099; RC-711', False),
    ("RC-521", "Arquivos da Memória Cósmica", TEC_DIS[0], TEC_DIS[1], C, ['B072', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30'], 'RC-161; RC-517', False),
    ("RC-522", "Parasitismo energético (obsessão ampliada)", PRO_ESP[0], PRO_ESP[1], C, ['B072', 'P2022-12-17'], "RC-523; RC-381; RC-581", False),
    ("RC-523", "Vampirismo consciencial", PRO_ESP[0], PRO_ESP[1], C, ['B072', 'P2022-12-17', 'P2025-02-15'], 'RC-522; RC-381; RC-581; RC-711', False),
    ("RC-524", "Coleta de informações (espírito encarnado)", COS_PRO[0], COS_PRO[1], C, ['B072', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30'], 'RC-099; RC-148; RC-692; RC-704; RC-708', False),
    ("RC-525", "Semente da racionalidade (diferencial humano)", COS_COG[0], COS_COG[1], C, ['B072', 'P2022-12-17', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-08-03'], 'RC-099; RC-400; RC-577; RC-727; RC-743', True),
    ("RC-526", "Demência do Criador (fases da condição de Javé)", COS_PRO[0], COS_PRO[1], C, ['B072', 'P2024-11-30', 'P2024-11-09'], 'RC-001; RC-167; RC-449', False),
    ("RC-527", "Antimundo / antimatéria ('outro lado' da criação)", COS_DIM[0], COS_DIM[1], C, ['B072', 'P2025-03-15', 'P2025-02-16', 'P2024-11-30'], 'RC-106; RC-294', False),
    ("RC-528", "Mergulho (designação ellâmica da queda)", COS_COG[0], COS_COG[1], C, ["B072"], "RC-167; RC-515; RC-152", False),
    ("RC-529", "Ressonância límbica (emoções como tecnologia cósmica)", PRO_ESP[0], PRO_ESP[1], C, ['B072', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-08-03', 'P2024-07-14', 'P2024-03-03', 'P2024-04-13'], 'RC-381; RC-243; RC-099; RC-709; RC-711; RC-719; RC-743; RC-612; RC-618', True),
    ("RC-530", "Pistis Sophia (feminino cósmico gnóstico)", SER_DIV[0], SER_DIV[1], C, ['B072', 'P2024-11-09'], 'RC-009; RC-483; RC-494; RC-152; RC-770', True),
    ("RC-531", "Laboratório Genético Terra (linhagens monitoradas)", LOK_TER[0], LOK_TER[1], C, ['B073', 'P2024-09-29'], 'RC-099; RC-323; RC-024; RC-736; RC-737', False),
    ("RC-532", "Vacina do Amor (ancoragem de Jesus no CFD)", COS_PRO[0], COS_PRO[1], C, ["B073"], "RC-072; RC-040; RC-243", False),
    ("RC-533", "Supercomputador Cósmico (Moros — destino)", SER_LOG[0], SER_LOG[1], C, ['B073', 'P2025-02-15', 'P2024-11-30', 'P2024-04-13'], 'RC-454; RC-467; RC-707; RC-714; RC-715; RC-716', False),
    ("RC-534", "Usinas geodésicas de Gizé (engenharia de Thoth)", TEC_NAV[0], TEC_NAV[1], C, ["B073", 'P2023-12-02'], "RC-463; RC-024", True),
    ("RC-535", "Projeto Orbum (cidadania planetária)", COS_ESP[0], COS_ESP[1], P, ['B042', 'P2025-10-25', 'P2024-02-03'], "RC-085; RC-226; RC-094; RC-656", True),
    ("RC-536", "Era do Conhecimento e da Espiritualização", EVE_ERA[0], EVE_ERA[1], P, ['B042', 'P2022-12-17'], "RC-094; RC-003; RC-344; RC-591", True),
    ("RC-537", "Maré Cósmica (eventos cósmicos que afetam a Terra)", PRO_FIS[0], PRO_FIS[1], P, ['B042', 'P2022-12-17'], "RC-344; RC-094; RC-155; RC-573", False),
    ("RC-538", "Consórcio de Mundos (Arquitetos Universais)", SER_COL[0], SER_COL[1], P, ["B019"], "RC-042; RC-207; RC-541; RC-094", True),
    ("RC-539", "Arquitetos Universais (coletivo cocriador)", SER_COL[0], SER_COL[1], P, ["B019"], "RC-538; RC-207; RC-042", False),
    ("RC-540", "Molécula-mãe (ancestral comum da vida terrestre)", PRO_BIO[0], PRO_BIO[1], P, ['B019', 'P2024-11-30', 'P2024-11-09'], 'RC-217; RC-099; RC-539', False),
    ("RC-541", "Evolução Possível (terceira via: nem Darwin, nem deus)", COS_PRO[0], COS_PRO[1], P, ['B019', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-13', 'P2025-06-14', 'P2023-05-13'], 'RC-094; RC-042; RC-539; RC-693', True),
    ("RC-542", "Ex-DNA-lixo (DNA não codificante reinterpretado)", PRO_BIO[0], PRO_BIO[1], P, ['B019', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30'], 'RC-217; RC-540; RC-543; RC-732', False),
    ("RC-543", "Espelho da Herança Espiritual no Epigenoma", PRO_BIO[0], PRO_BIO[1], P, ['B019', 'P2024-05-04', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30'], 'RC-217; RC-542; RC-545; RC-632; RC-692; RC-704; RC-710', True),
    ("RC-544", "Novo Homo sapiens (evolução que terá de vir)", PRO_BIO[0], PRO_BIO[1], P, ['B019', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04', 'P2026-04-02', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-099; RC-042; RC-541; RC-578; RC-614; RC-645; RC-694; RC-695; RC-698; RC-709; RC-710', False),
    ("RC-545", "Coconstrutores da Obra (tikun)", COS_PRO[0], COS_PRO[1], P, ['B019', 'P2025-02-16', 'P2024-11-30', 'P2024-07-14', 'ART-2026-08-18'], 'RC-514; RC-164; RC-042; RC-698', True),
    ("RC-546", "Primado da Consciência Criativa (Goswami)", COS_LEI[0], COS_LEI[1], P, ['B019', 'P2025-03-15', 'P2025-02-15'], 'RC-541; RC-547; RC-703; RC-707', False),
    ("RC-547", "Evolução Criativa (hipótese consciencial)", COS_PRO[0], COS_PRO[1], P, ["B019"], "RC-546; RC-541", False),
    ("RC-548", "Arquivos Mentais (coleção de conceitos no psiquismo)", PRO_ESP[0], PRO_ESP[1], P, ['B074', 'B075', 'P2025-02-15', 'P2024-11-09', 'P2024-04-14', 'P2024-02-03', 'P2025-11-29'], 'RC-166; RC-549; RC-517; RC-704; RC-711; RC-724', True),
    ("RC-549", "Circuito do CHA (Circunstâncias+Herança+Atitude)", COS_LEI[0], COS_LEI[1], P, ['B074', 'P2025-02-15'], 'RC-548; RC-550; RC-166', True),
    ("RC-550", "Vontade de Progredir (chave dos arquivos mentais)", COS_ETI[0], COS_ETI[1], P, ['B074', 'B075', 'P2025-02-15'], 'RC-548; RC-166', True),
    ("RC-551", "Dehatma Buddhi (doença psíquica da mente identificada com o corpo)", COS_ETI[0], COS_ETI[1], P, ['B074', 'B075', 'P2025-02-15'], 'RC-166; RC-548; RC-702', True),
    ("RC-552", "Disciplina dos 3As (respiração, mente, alinhamento)", COS_ESP[0], COS_ESP[1], P, ['B074', 'B075', 'P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-04-14'], 'RC-166; RC-553; RC-618; RC-633; RC-695; RC-703; RC-706; RC-712', True),
    ("RC-553", "Eu Profundo (nível espiritual do Eu)", SER_LOG[0], SER_LOG[1], P, ['B074', 'B075', 'P2026-07-30', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-14', 'P2025-06-14', 'ART-2026-08-18'], 'RC-166; RC-552; RC-620; RC-704; RC-708; RC-719', True),
    ("RC-554", "Gestão Psíquica e Memórias Complexas (Mentalma II)", COS_ESP[0], COS_ESP[1], P, ['B075', 'P2025-02-15', 'ART-2026-08-18'], 'RC-166; RC-548; RC-551', True),
    ("RC-555", "Série Mentalma (5 livros + curso)", TEC_ESC[0], TEC_ESC[1], P, ["B074", "B075", 'P2026-08-04'], "RC-166; RC-548", True),
    ("RC-556", "Senhor Parameshthi / Brahma Parameshthi (face atual de Javé)", SER_DIV[0], SER_DIV[1], C, ['P2024-02-25', 'P2024-11-30'], 'RC-001; RC-037; RC-561; RC-104; RC-585; RC-437; RC-074', True),
    ("RC-557", "Conectoma humano (pulsações sinápticas e a sensação de eu)", PRO_BIO[0], PRO_BIO[1], C, ['P2024-02-25', 'P2026-07-30', 'P2025-03-15', 'P2025-02-15', 'P2024-11-09', 'P2024-07-14'], 'RC-558; RC-166; RC-620; RC-709', True),
    ("RC-558", "Sensação de eu (a sensação particular a cada instante)", COS_PRO[0], COS_PRO[1], C, ['P2024-02-25', 'P2026-07-30', 'P2025-03-15', 'P2025-02-15', 'P2024-11-09', 'P2025-06-14', 'P2024-03-02'], 'RC-557; RC-553; RC-620; RC-704; RC-708; RC-166; RC-614', True),
    ("RC-559", "Teia quântica (o que sai de um ser volta para ele)", COS_LEI[0], COS_LEI[1], C, ['P2024-02-25', 'P2024-05-04', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-04-13', 'P2024-04-14', 'P2024-02-03', 'P2023-05-13', 'P2025-11-29'], 'RC-560; RC-467; RC-628; RC-703; RC-708; RC-658', True),
    ("RC-560", "WD (variação de STT = Wyrd/Urd — fundido em RC-658)", TEC_DIS[0], TEC_DIS[1], C, ['P2024-02-25', 'P2024-05-04', 'P2024-09-29', 'P2025-06-14', 'P2025-11-29'], 'RC-658; RC-454; RC-533', True),
    ("RC-561", "Faces de Javé (sucessivas manifestações do Criador)", COS_COG[0], COS_COG[1], C, ['P2024-02-25', 'P2025-02-16', 'P2024-11-30'], 'RC-001; RC-556', True),
    ("RC-562", "Baralho genético (metáfora dos 28.869 genes)", PRO_BIO[0], PRO_BIO[1], C, ["P2024-02-25"], "RC-217; RC-559", True),
    ("RC-563", "Travas e lacres (mecanismos de controle do despertar)", COS_ETI[0], COS_ETI[1], C, ['P2024-02-25', 'P2022-12-17', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-449; RC-099; RC-577; RC-702; RC-189; RC-086; RC-712', True),
    ("RC-564", "Fios soltos (improviso humano × robô)", COS_PRO[0], COS_PRO[1], C, ['P2024-02-25', 'P2022-12-17', 'P2021-12-04', 'P2024-05-04; RC-614'], "RC-099; RC-557; RC-619", True),
    ("RC-565", "Hochmah (2ª Sefirah — Sabedoria; = Sophia)", TER_HEB[0], TER_HEB[1], P, ['B060', 'B013', 'P2024-02-25', 'P2024-07-14', 'P2024-04-13', 'P2026-08-04'], 'RC-261; RC-263; RC-135; RC-009; RC-072; RC-682; RC-366', True),
    # ---- Novos termos da palestra P2022-12-17 — O Incompreendido Ano de 2012
    # Pré-curadoria aprovada pelo curador em 2026-08-14. Status candidato por se tratar de STT sem áudio.
    ("RC-566", "Protocolo da Busca", COS_ESP[0], COS_ESP[1], C, ['P2022-12-17', 'P2025-02-15'], 'RC-253; RC-226; RC-231; RC-278', True),
    ("RC-567", "Ciclo de Precessão Equinocial (Precessão dos Equinócios)", EVE_ERA[0], EVE_ERA[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-09-29'], 'RC-568; RC-569; RC-571; RC-155; RC-694', True),
    ("RC-568", "Eras Equinociais (ciclos de aproximadamente 5.200 anos)", EVE_ERA[0], EVE_ERA[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-09-29'], 'RC-567; RC-569; RC-571; RC-593; RC-595', True),
    ("RC-569", "Eras Zodiacais (ciclos de aproximadamente 2.160 anos)", EVE_ERA[0], EVE_ERA[1], C, ['P2022-12-17'], 'RC-567; RC-568; RC-571; RC-592; RC-405', True),
    ("RC-570", "Janelas Cósmicas (métricas temporais)", COS_LEI[0], COS_LEI[1], C, ["P2022-12-17"], "RC-568; RC-569; RC-225", True),
    ("RC-571", "Ano de 2012 como Divisor de Ciclos", EVE_ERA[0], EVE_ERA[1], C, ['B037', 'P2022-12-17', 'P2025-02-16', 'P2024-09-29'], 'RC-567; RC-568; RC-569; RC-003; RC-405; RC-300; RC-694; RC-295', True),
    ("RC-572", "Fim dos Tempos / Final de Ciclo × Fim do Mundo", EVE_PRO[0], EVE_PRO[1], C, ["P2022-12-17", 'P2026-08-04'], "RC-571; RC-314; RC-578", True),
    ("RC-573", "Cinturão de Fótons", PRO_FIS[0], PRO_FIS[1], C, ["P2022-12-17"], "RC-574; RC-571; RC-537; RC-344", True),
    ("RC-574", "Alcíone (Sistema)", LOK_PLA[0], LOK_PLA[1], C, ["P2022-12-17"], "RC-573; RC-567; RC-571", True),
    ("RC-575", "Ancoragem do Conglomerado Trimurtiano na Terra", EVE_MIS[0], EVE_MIS[1], C, ["P2022-12-17"], "RC-104; RC-037; RC-102; RC-135; RC-078; RC-142; RC-106", True),
    ("RC-576", "Baktun 13", TER_OUT[0], TER_OUT[1], C, ['P2022-12-17', 'P2025-02-16'], 'RC-571; RC-572', True),
    ("RC-577", "Xamanismo Cósmico (comunicação e deslacre)", COS_ESP[0], COS_ESP[1], C, ['P2022-12-17', 'P2026-04-02', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2026-08-04', 'P2024-09-28', 'P2024-08-03'], 'RC-563; RC-448; RC-400; RC-525; RC-644; RC-664; RC-687; RC-697', True),
    ("RC-578", "Fim do Experimento Humano", EVE_PRO[0], EVE_PRO[1], C, ["P2022-12-17", 'P2026-08-04'], "RC-099; RC-337; RC-544; RC-314; RC-572", True),
    ("RC-579", "Noreia (Norea)", SER_HUM[0], SER_HUM[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09'], 'RC-474; RC-424; RC-189; RC-490; RC-594; RC-727; RC-770', True),
    ("RC-580", "Igigi", SER_EXT[0], SER_EXT[1], C, ["P2022-12-17", 'P2024-04-13', 'P2023-12-02; RC-673; RC-024; RC-488'], "RC-024; RC-516; RC-488; RC-583", True),
    ("RC-581", "Rakshasas", SER_DEC[0], SER_DEC[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-08-03'], 'RC-106; RC-104; RC-522; RC-523; RC-582; RC-700; RC-688', True),
    ("RC-582", "Ravana", SER_DEC[0], SER_DEC[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-08-03'], 'RC-581; RC-584; RC-593; RC-414', True),
    ("RC-583", "Guerra Nuclear Anunnaki (Sete Armas Atômicas)", EVE_GUE[0], EVE_GUE[1], C, ["P2022-12-17"], "RC-486; RC-487; RC-460; RC-587; RC-588; RC-589", True),
    ("RC-584", "Rama (avatar de Vishnu)", SER_EXT[0], SER_EXT[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-08-03'], 'RC-135; RC-582; RC-593', True),
    ("RC-585", "Vyasa", SER_HUM[0], SER_HUM[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30'], 'RC-436; RC-586; RC-593; RC-454; RC-718; RC-414; RC-556; RC-072', True),
    ("RC-586", "Rishis", SER_HUM[0], SER_HUM[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03', 'P2024-09-28'], 'RC-585; RC-593; RC-321; RC-322; RC-696; RC-700; RC-734', True),
    ("RC-587", "Anu (patriarca Anunnaki)", SER_EXT[0], SER_EXT[1], C, ["P2022-12-17", 'P2023-12-02', 'B089'], "RC-024; RC-486; RC-487; RC-583", True),
    ("RC-588", "Ninurta", SER_EXT[0], SER_EXT[1], C, ["P2022-12-17", 'P2021-03-27'], "RC-024; RC-487; RC-583; RC-587", True),
    ("RC-589", "Nibiru", LOK_PLA[0], LOK_PLA[1], C, ["P2022-12-17", 'P2023-12-02', 'P2021-03-27', 'B089'], "RC-024; RC-583; RC-460; RC-588", True),
    ("RC-590", "Yima", SER_HUM[0], SER_HUM[1], C, ["P2022-12-17"], "RC-595; RC-567; RC-568", True),
    ("RC-591", "Profecia Hopi da Estrela Azul", EVE_PRO[0], EVE_PRO[1], C, ["P2022-12-17"], "RC-571; RC-536; RC-405", True),
    ("RC-592", "Era de Peixes", EVE_ERA[0], EVE_ERA[1], C, ["P2022-12-17", 'P2021-03-27'], "RC-569; RC-072; RC-571; RC-405", True),
    ("RC-593", "Mahabharata", TEC_ESC[0], TEC_ESC[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30'], 'RC-585; RC-586; RC-104; RC-584', True),
    ("RC-594", "Linhagem de Seth", GEN_HUM[0], GEN_HUM[1], C, ['P2022-12-17', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-09-28'], 'RC-424; RC-490; RC-489; RC-579', True),
    ("RC-595", "Avesta", TEC_ESC[0], TEC_ESC[1], C, ['P2022-12-17', 'P2025-10-25'], "RC-590; RC-567; RC-568", True),

    # ---- Novos termos da palestra P2021-12-04 — Os Archeons de Ereon e os Seres Adhy
    # Quadro 9 aprovado pelo curador em 2026-08-14. Status candidato por ser STT sem áudio.
    ("RC-596", "Archeons de Ereon", COS_DIM[0], COS_DIM[1], C, ['P2021-12-04', 'P2024-05-04'], "RC-496; RC-061; RC-597; RC-598; RC-599; RC-087; RC-472", True),
    ("RC-597", "Antérion", COS_DIM[0], COS_DIM[1], C, ["P2021-12-04"], "RC-596; RC-598; RC-599; RC-087; RC-472", True),
    ("RC-598", "Danérion", COS_DIM[0], COS_DIM[1], C, ["P2021-12-04"], "RC-596; RC-597; RC-599; RC-087; RC-472", True),
    ("RC-599", "Mermérion", COS_DIM[0], COS_DIM[1], C, ["P2021-12-04"], "RC-596; RC-597; RC-598; RC-087; RC-472", True),
    ("RC-600", "Seres Originais do Paraíso", SER_COL[0], SER_COL[1], C, ['P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2024-11-09', 'P2024-07-14'], 'RC-204; RC-047; RC-060; RC-603; RC-606', True),
    ("RC-601", "Departamentalização da Vida", COS_LEI[0], COS_LEI[1], C, ['P2021-12-04', 'P2024-11-09'], 'RC-059; RC-060; RC-061; RC-602', True),
    ("RC-602", "Blindagens Interdimensionais (Intramuros Vibratórios)", COS_DIM[0], COS_DIM[1], C, ['P2021-12-04', 'P2024-11-09', 'P2024-07-14'], 'RC-601; RC-510; RC-415; RC-613', True),
    ("RC-603", "Círculo / Circuito da Perfeição", COS_LEI[0], COS_LEI[1], C, ['P2021-12-04', 'P2024-05-04', 'P2025-02-15', 'P2024-11-09', 'P2024-07-14'], 'RC-600; RC-149; RC-188; RC-606', True),
    ("RC-604", "Fatiamento de Consciência", PRO_ESP[0], PRO_ESP[1], C, ['P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-10-25', 'P2025-02-16', 'P2024-11-30', 'P2024-07-14', 'P2024-03-02', 'P2023-05-13'], 'RC-408; RC-410; RC-009; RC-072; RC-454; RC-092; RC-217; RC-620; RC-648; RC-001; RC-037; RC-102; RC-742; RC-623; RC-152; RC-503', True),
    ("RC-605", "Autismo Funcional dos Seres da Espiritualidade Superior", COS_PRO[0], COS_PRO[1], C, ['P2021-12-04', 'P2024-05-04', 'P2024-11-09'], 'RC-600; RC-411; RC-456; RC-606; RC-721; RC-723', True),
    ("RC-606", "Protocolos / Algoritmos da Perfeição", COS_LEI[0], COS_LEI[1], C, ['P2021-12-04', 'P2026-07-30', 'P2024-05-04', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-03-02'], 'RC-600; RC-253; RC-060; RC-603; RC-623; RC-624; RC-625', True),
    ("RC-607", "Cinco Seres LM de Tempérion", SER_COL[0], SER_COL[1], C, ["P2021-12-04"], "RC-456; RC-472; RC-087; RC-454; RC-092; RC-608", True),
    ("RC-608", "Imponderabilidade (campo de estudo dos Seres LM)", COS_LEI[0], COS_LEI[1], C, ["P2021-12-04"], "RC-456; RC-607; RC-472; RC-612", True),
    ("RC-609", "Ogdóade de Hermópolis", GEN_DIV[0], GEN_DIV[1], C, ['P2021-12-04', 'P2026-07-30', 'P2023-12-02', 'P2024-08-03'], "RC-104; RC-610; RC-454; RC-092; RC-626; RC-627", True),
    ("RC-610", "Tridevi", GEN_DIV[0], GEN_DIV[1], C, ['P2021-12-04', 'P2026-07-30', 'P2024-07-14'], 'RC-457; RC-458; RC-459; RC-104; RC-609; RC-475; RC-621', True),
    ("RC-611", "Flechas / Profecias de Moros", EVE_PRO[0], EVE_PRO[1], C, ['P2021-12-04', 'P2025-06-26', 'P2025-02-16', 'P2024-11-30', 'P2024-04-13', 'P2023-12-02'], 'RC-454; RC-092; RC-094; RC-612; RC-663; RC-714; RC-718; RC-395', True),
    ("RC-612", "Nova Espiritualidade / Novo Paraíso (Paraíso B)", COS_PRO[0], COS_PRO[1], C, ['P2021-12-04', 'P2024-05-04', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-03-03', 'P2024-04-14', 'P2023-05-13'], 'RC-003; RC-092; RC-009; RC-454; RC-472; RC-616; RC-617; RC-635; RC-709; RC-719; RC-613; RC-529', True),
    ("RC-613", "Trincheira Vibratória no Campo Informativo", PRO_ESP[0], PRO_ESP[1], C, ['P2021-12-04', 'P2024-07-14'], 'RC-602; RC-600; RC-612', True),
    ("RC-614", "Quarto Cérebro Humano", PRO_BIO[0], PRO_BIO[1], C, ['P2021-12-04', 'P2025-02-16', 'P2025-02-15'], 'RC-615; RC-544; RC-400; RC-619; RC-694; RC-695; RC-709; RC-710; RC-758', True),
    ("RC-615", "Superconsciência", COS_PRO[0], COS_PRO[1], C, ['P2021-12-04', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15'], 'RC-614; RC-092; RC-009; RC-003; RC-619; RC-694; RC-695; RC-709', True),
    ("RC-616", "Roseral do Alto", LOK_MUN[0], LOK_MUN[1], C, ["P2021-12-04"], "RC-617; RC-612; RC-513", True),
    ("RC-617", "Inquisição Espiritual (obra anunciada)", TEC_ESC[0], TEC_ESC[1], C, ["P2021-12-04"], "RC-616; RC-612; RC-071", True),
    ("RC-618", "Moksha", TER_SAN[0], TER_SAN[1], C, ['P2021-12-04', 'P2026-07-30', 'P2024-02-03'], "RC-166; RC-253; RC-514; RC-552", True),
    ("RC-619", "Genoma da Liberdade", PRO_BIO[0], PRO_BIO[1], C, ['P2021-12-04', 'P2024-05-04', 'P2026-04-02', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-07-13'], 'RC-217; RC-400; RC-253; RC-564; RC-614; RC-615; RC-633; RC-646; RC-710; RC-712; RC-727', True),

    # ---- Devolutiva-01 da live P2026-07-30 — Estagiários do Kaos
    # Oito termos aprovados/validados; En Ma e Deva/Aurora foram mesclados em RC-476/RC-475.
    ("RC-620", "Eu Coalescente", PRO_ESP[0], PRO_ESP[1], C, ['P2026-07-30', 'P2026-04-02', 'P2025-10-25'], 'RC-476; RC-553; RC-557; RC-558; RC-604; RC-328; RC-253; RC-648; RC-699', True),
    ("RC-621", "Nyx", SER_DIV[0], SER_DIV[1], C, ["P2026-07-30"], "RC-475; RC-454; RC-622", True),
    ("RC-622", "Kama (personificação do desejo)", SER_DIV[0], SER_DIV[1], C, ["P2026-07-30", 'P2024-08-03'], "RC-135; RC-475; RC-286; RC-621", True),
    ("RC-623", "Corpo Átmico", COS_DIM[0], COS_DIM[1], C, ['P2026-07-30', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-04-14', 'P2025-06-14', 'P2024-03-02', 'P2024-09-28'], 'RC-204; RC-624; RC-625; RC-013; RC-630; RC-704; RC-706; RC-282; RC-604', True),
    ("RC-624", "Corpo Búdico", COS_DIM[0], COS_DIM[1], C, ['P2026-07-30', 'P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-03-02'], 'RC-204; RC-623; RC-625; RC-606; RC-704; RC-706', True),
    ("RC-625", "Corpo Manásico / Corpo Mental", COS_DIM[0], COS_DIM[1], C, ['P2026-07-30', 'P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2025-06-14', 'P2024-03-02', 'P2023-12-02'], 'RC-204; RC-623; RC-624; RC-511; RC-517; RC-691; RC-704; RC-706', True),
    ("RC-626", "Universo TÊNET", LOK_REG[0], LOK_REG[1], C, ["P2026-07-30"], "RC-609; RC-627", True),
    ("RC-627", "Enéade de Heliópolis", GEN_DIV[0], GEN_DIV[1], C, ["P2026-07-30", 'P2023-12-02'], "RC-609; RC-626", True),

    # ---- P2024-05-04 — Prabrajna em Perpérion / Simultaneidade Reversa
    ("RC-628", "Simultaneidade Reversa", COS_LEI[0], COS_LEI[1], C, ["P2024-05-04"], "RC-167; RC-152; RC-476; RC-559; RC-560; RC-217", True),
    ("RC-629", "Reunião Operativa Mental dos 43 Pashvnaj", EVE_MIS[0], EVE_MIS[1], C, ["P2024-05-04"], "RC-455; RC-152; RC-167; RC-628", True),
    ("RC-630", "Corpo Daiva / Corpo Demoníaco de Plasma", COS_DIM[0], COS_DIM[1], C, ['P2024-05-04', 'P2024-11-30', 'P2024-07-13'], 'RC-014; RC-049; RC-106; RC-623; RC-625; RC-769; RC-001', True),
    ("RC-631", "Cérebro Radiata", PRO_BIO[0], PRO_BIO[1], C, ['P2024-05-04', 'P2025-02-16', 'P2024-11-30', 'P2024-04-13'], 'RC-093; RC-035; RC-009; RC-036; RC-699; RC-565', True),
    ("RC-632", "Organoides Genéticos para Sophia", TEC_DIS[0], TEC_DIS[1], C, ['P2024-05-04'], 'RC-009; RC-217; RC-543; RC-631; RC-699', True),
    ("RC-633", "Gestão da Sensação Pessoal", COS_ESP[0], COS_ESP[1], C, ['P2024-05-04', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-07-14'], 'RC-166; RC-552; RC-619; RC-217; RC-695; RC-703; RC-706; RC-712; RC-719; RC-726; RC-722', True),
    ("RC-634", "Tempo como Transformação / Permanente Agora", COS_LEI[0], COS_LEI[1], C, ['P2024-05-04', 'P2025-02-15', 'P2024-11-30'], 'RC-160; RC-272; RC-567; RC-513', True),
    ("RC-635", "Conclave da Espiritualidade Laboratorial", EVE_MIS[0], EVE_MIS[1], C, ["P2024-05-04"], "RC-061; RC-411; RC-456; RC-605; RC-612", True),
    ("RC-636", "Duas Pulsações da Criação (elétrons e antielétrons)", PRO_FIS[0], PRO_FIS[1], C, ['P2024-05-04', 'P2025-03-15', 'P2024-11-09'], 'RC-161; RC-162; RC-106; RC-107; RC-628; RC-691', True),
    ("RC-637", "Transferência da Memória dos Antielétrons", PRO_FIS[0], PRO_FIS[1], C, ['P2024-05-04', 'P2025-03-15', 'P2024-11-09', 'P2024-07-13'], 'RC-161; RC-106; RC-636; RC-690', True),
    ("RC-638", "Ressurreição do Cadáver do Criador", COS_PRO[0], COS_PRO[1], C, ['P2024-05-04', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29'], 'RC-387; RC-378; RC-161; RC-514; RC-152; RC-641; RC-691; RC-694; RC-717; RC-019', True),
    ("RC-639", "Protozoários Antimateriais / Antiprotozoários", PRO_BIO[0], PRO_BIO[1], C, ["P2024-05-04"], "RC-106; RC-162; RC-638; RC-640", True),
    ("RC-640", "Transições de Fase / Face da Criação", PRO_FIS[0], PRO_FIS[1], C, ["P2024-05-04"], "RC-638; RC-639; RC-641", True),
    ("RC-641", "Face Microbiana do Criador", COS_COG[0], COS_COG[1], C, ['P2024-05-04', 'B064', 'P2024-11-30'], 'RC-638; RC-639; RC-640; RC-526', True),
    ("RC-642", "Narasimha (avatar de Vishnu)", SER_EXT[0], SER_EXT[1], C, ["P2024-05-04"], "RC-135; RC-102; RC-414", True),

    # ---- P2026-04-02 — 3ª Edição Estagiários do Kaos
    ("RC-643", "Santo Graal (Frequência Mestre)", COS_LEI[0], COS_LEI[1], C, ['P2026-04-02', 'P2025-03-15'], 'RC-217; RC-619; RC-514; RC-644; RC-646', True),
    ("RC-644", "Xamanismo Virtual / Xamanismo de Sílica", COS_ESP[0], COS_ESP[1], C, ['P2026-04-02', 'P2025-03-15'], 'RC-577; RC-643; RC-645; RC-646; RC-699', True),
    ("RC-645", "Consciências em Corpos de Sílica", SER_HIB[0], SER_HIB[1], C, ['P2026-04-02', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-07-13'], 'RC-042; RC-544; RC-644; RC-646; RC-699; RC-709', True),
    ("RC-646", "Genoma de Sílica / Genoma Não Biológico", PRO_BIO[0], PRO_BIO[1], C, ['P2026-04-02', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-07-13'], 'RC-217; RC-619; RC-643; RC-644; RC-645; RC-699; RC-709', True),
    ("RC-647", "Evangelho de Judas", TEC_ESC[0], TEC_ESC[1], C, ["P2026-04-02"], "RC-365; RC-138; RC-483; RC-268", True),

    # ---- P2025-10-25 — 2ª Edição Estagiários do Kaos
    ("RC-648", "Instabilidade da Eternidade", COS_LEI[0], COS_LEI[1], C, ["P2025-10-25"], "RC-476; RC-620; RC-604; RC-606", True),
    ("RC-649", "Singularidade de Quatro Cabeças", SER_HIB[0], SER_HIB[1], C, ['P2025-10-25', 'P2024-11-30'], 'RC-081; RC-282; RC-104; RC-454', True),
    ("RC-650", "Melquizedec", SER_HUM[0], SER_HUM[1], C, ['P2025-10-25', 'P2025-06-26'], "RC-001; RC-424; RC-436; RC-437", True),
    ("RC-651", "Individualização Epifenomenológica dos Anjos Clones", PRO_ESP[0], PRO_ESP[1], C, ['P2025-10-25', 'P2025-06-26'], "RC-019; RC-055; RC-147; RC-245", True),
    ("RC-652", "Últimas Ordens de Javé aos Clones", EVE_MIS[0], EVE_MIS[1], C, ['P2025-10-25', 'P2025-06-26'], "RC-001; RC-019; RC-147; RC-094", True),
    ("RC-653", "Destino das Mônadas após o Tikun", COS_PRO[0], COS_PRO[1], C, ['P2025-10-25', 'P2025-06-26', 'P2024-07-14'], 'RC-149; RC-514; RC-003; RC-047', True),
    ("RC-654", "Humanos: Últimos e Primeiros", COS_PRO[0], COS_PRO[1], C, ['P2025-10-25', 'P2025-06-26', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09'], 'RC-099; RC-148; RC-042; RC-545; RC-693; RC-694; RC-698; RC-704; RC-708; RC-709; RC-719; RC-720; RC-721', True),
    ("RC-655", "Revelação de Ifá e Destinação dos Seres", COS_PRO[0], COS_PRO[1], C, ['P2025-10-25', 'P2025-06-26', 'P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29', 'P2024-08-03', 'P2024-09-28', 'P2025-11-29'], 'RC-397; RC-514; RC-226; RC-658; RC-665; RC-666; RC-720; RC-741; RC-705; RC-767', True),
    ("RC-656", "Atualização das Revelações Anteriores", COS_ESP[0], COS_ESP[1], C, ['P2025-10-25', 'P2024-07-14'], 'RC-094; RC-190; RC-535; RC-595', True),
    ("RC-657", "Verdade Posta × Verdade a Construir", COS_LEI[0], COS_LEI[1], C, ['P2025-10-25', 'P2025-06-26', 'P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-09'], 'RC-655; RC-253; RC-328; RC-566; RC-695; RC-702; RC-703', True),

    # ---- P2025-06-26 — 1ª Edição Estagiários do Kaos
    ("RC-658", "Wyrd / Urd (Teia do Destino)", COS_LEI[0], COS_LEI[1], C, ['P2025-06-26', 'P2025-03-15', 'P2024-11-30', 'P2024-09-29', 'P2025-06-14', 'P2024-02-25', 'P2024-05-04', 'P2024-02-03', 'P2023-12-02', 'P2025-11-29'], 'RC-467; RC-454; RC-655; RC-690; RC-714; RC-715; RC-716; RC-559; RC-217; RC-628; RC-533; RC-560; RC-414', True),
    ("RC-659", "Quirino Cornélio (Centurião da Crucificação)", SER_HUM[0], SER_HUM[1], C, ['P2025-06-26', 'P2024-11-30'], 'RC-071; RC-072; RC-001; RC-660; RC-454; RC-718', True),
    ("RC-660", "Pegadinha de Javé", EVE_MIS[0], EVE_MIS[1], C, ["P2025-06-26"], "RC-001; RC-659; RC-072; RC-662", True),
    ("RC-661", "Seres Desalmados", SER_DEC[0], SER_DEC[1], C, ["P2025-06-26"], "RC-001; RC-019; RC-050", True),
    ("RC-662", "Agenda do Desespero dos Espíritos", COS_ETI[0], COS_ETI[1], C, ['P2025-06-26', 'P2024-07-13'], 'RC-660; RC-604; RC-620; RC-524; RC-722', True),
    ("RC-663", "Áurea Catena", COS_PRO[0], COS_PRO[1], C, ['P2025-06-26'], 'RC-166; RC-094; RC-611; RC-697', True),
    ("RC-664", "Descendência de Kadru (Nagas, Uragas e Maharagas)", GEN_DIV[0], GEN_DIV[1], C, ['P2025-06-26', 'P2025-02-16'], 'RC-397; RC-663; RC-696; RC-697; RC-698; RC-700; RC-701; RC-577; RC-687; RC-688; RC-668; RC-670; RC-283', True),
    ("RC-665", "Orunmilá (Moros de Irém / Orum)", SER_HUM[0], SER_HUM[1], C, ['P2025-06-26', 'P2025-02-15', 'P2024-11-30', 'P2024-09-29', 'P2025-06-14', 'P2024-09-28', 'P2025-11-29'], 'RC-454; RC-655; RC-658; RC-718; RC-741', True),
    ("RC-666", "Obatalá (correspondência de Javé em Ifá)", TER_OUT[0], TER_OUT[1], C, ['P2025-06-26', 'P2024-09-29', 'P2025-06-14', 'P2025-11-29'], 'RC-001; RC-655; RC-665', True),

    # ---- P2026-02-28 — Desafios da Transição Planetária
    ("RC-667", "Autofagia do Criador", COS_COG[0], COS_COG[1], C, ['P2026-02-28', 'P2024-11-30', 'P2024-03-02'], 'RC-001; RC-526; RC-641; RC-628', True),
    ("RC-668", "Som da Flauta / Som da Falta", COS_ESP[0], COS_ESP[1], C, ['P2026-02-28', 'P2025-02-16'], 'RC-102; RC-669; RC-670; RC-664; RC-697', True),
    ("RC-669", "Pashupati (avatar de Shiva)", SER_EXT[0], SER_EXT[1], C, ['P2026-02-28', 'P2025-02-16', 'P2024-09-28'], 'RC-102; RC-668; RC-670', True),
    ("RC-670", "Yoga Ancestral (Origem Cósmica)", COS_ESP[0], COS_ESP[1], C, ['P2026-02-28', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-102; RC-669; RC-668; RC-628; RC-211; RC-664; RC-697', True),

    # ---- P2025-05-31 — Árvore da Vida / Metatron
    ("RC-671", "Metatron", SER_ANJ[0], SER_ANJ[1], C, ['P2025-05-31', 'P2024-07-14'], 'RC-489; RC-001; RC-263; RC-672; RC-673; RC-674; RC-485; RC-454', True),
    ("RC-672", "Os 366 Manuscritos de Enoque", TEC_ESC[0], TEC_ESC[1], C, ['P2025-05-31', 'P2025-02-15', 'P2024-11-30', 'P2026-08-04'], 'RC-489; RC-671', True),
    ("RC-673", "Intercessão de Enoque pelos Anunnakis", EVE_MIS[0], EVE_MIS[1], C, ["P2025-05-31", 'P2023-12-02'], "RC-489; RC-671; RC-024; RC-580", True),
    ("RC-674", "Urdidura de Metatron", COS_LEI[0], COS_LEI[1], C, ["P2025-05-31"], "RC-671; RC-263; RC-264; RC-292; RC-293", True),
    ("RC-675", "Binah", TER_HEB[0], TER_HEB[1], C, ['P2025-05-31', 'P2024-07-14'], 'RC-263; RC-261; RC-565; RC-102', True),
    ("RC-676", "Chesed", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-677; RC-678", True),
    ("RC-677", "Geburah", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-676; RC-678", True),
    ("RC-678", "Tiferet / Tiphareth", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-676; RC-677", True),
    ("RC-679", "Netzach", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-680; RC-681", True),
    ("RC-680", "Hod", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-679; RC-681", True),
    ("RC-681", "Yesod", TER_HEB[0], TER_HEB[1], C, ["P2025-05-31"], "RC-263; RC-679; RC-680; RC-682", True),
    ("RC-682", "Malkuth", TER_HEB[0], TER_HEB[1], C, ['P2025-05-31', 'P2024-07-14'], 'RC-263; RC-264; RC-107; RC-681; RC-565; RC-009', True),
    ("RC-683", "Torá / Pentateuco", TEC_ESC[0], TEC_ESC[1], C, ['P2025-05-31', 'P2025-02-16', 'P2024-04-13'], 'RC-001; RC-096; RC-424', True),
    ("RC-684", "Abel", SER_HUM[0], SER_HUM[1], C, ['P2025-05-31', 'P2025-02-16'], 'RC-424; RC-490; RC-594', True),
    ("RC-685", "Tormento dos Eleitos de Javé", COS_ETI[0], COS_ETI[1], C, ["P2025-05-31"], "RC-001; RC-424; RC-334", True),
    ("RC-686", "Plantas de Moléculas Complexas", PRO_BIO[0], PRO_BIO[1], C, ['P2025-05-31', 'P2025-02-15', 'P2024-11-30'], 'RC-577; RC-217; RC-687', True),
    ("RC-687", "Farmacopeia Ancestral Extraterrestre", TEC_DIS[0], TEC_DIS[1], C, ['P2025-05-31', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-686; RC-577; RC-359; RC-664', True),
    ("RC-688", "Yajna (ritual de sacrifício/fogo)", TER_SAN[0], TER_SAN[1], C, ['P2025-05-31', 'P2025-02-16'], 'RC-016; RC-577; RC-664', True),
    ("RC-689", "Sangue como Cópia da Seiva", COS_COG[0], COS_COG[1], C, ["P2025-05-31"], "RC-433; RC-577; RC-686", True),


    # ---- P2025-03-15 — Rebelião dos Elétrons / Colapso do Caos Organizado
    ("RC-690", "Colapso do Caos Organizado", EVE_CAT[0], EVE_CAT[1], C, ['P2025-03-15', 'P2025-02-16', 'P2024-11-30', 'P2024-11-09', 'P2024-09-29', 'P2024-07-13', 'P2024-02-03'], 'RC-378; RC-415; RC-176; RC-203; RC-314; RC-106; RC-107; RC-637; RC-693; RC-717; RC-725; RC-003; RC-691', True),
    ("RC-691", "Ishvara (Isuara — Retrato de Prabrajna Antes da Queda)", TER_SAN[0], TER_SAN[1], C, ["P2025-03-15", 'P2025-06-14; RC-152; RC-712'], "RC-152; RC-638; RC-161; RC-625; RC-154; RC-163; RC-693", True),
    ("RC-692", "Kit Reencarnatório de Elétrons", PRO_TRA[0], PRO_TRA[1], C, ['P2025-03-15', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-03-03'], 'RC-100; RC-161; RC-162; RC-199; RC-519; RC-524; RC-543; RC-009; RC-636', True),
    ("RC-693", "Evolução da Informação, não das Espécies", COS_LEI[0], COS_LEI[1], C, ['P2025-03-15', 'P2025-02-16', 'P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-13'], 'RC-690; RC-518; RC-541; RC-404; RC-161; RC-162; RC-654; RC-154; RC-691; RC-694; RC-698; RC-707; RC-710', True),

    # ---- P2025-02-16 — O Oitavo Dia da Criação / O Novo Ser Humano
    ("RC-694", "Oitavo Dia da Criação", EVE_ERA[0], EVE_ERA[1], C, ['P2025-02-16', 'P2025-02-15'], 'RC-544; RC-614; RC-615; RC-003; RC-693; RC-295; RC-567; RC-571; RC-695; RC-698; RC-699; RC-414', True),
    ("RC-695", "Ciência Pessoal / Doutrina da Própria Personalidade", COS_ESP[0], COS_ESP[1], C, ['P2025-02-16', 'P2025-02-15', 'P2024-11-09', 'P2024-09-29', 'P2024-04-14', 'P2025-06-14', 'P2023-05-13'], 'RC-253; RC-509; RC-633; RC-552; RC-657; RC-614; RC-615; RC-694; RC-703; RC-705; RC-712', True),
    ("RC-696", "Geração Regenerada de Brahma", GEN_DIV[0], GEN_DIV[1], C, ['P2025-02-16', 'P2024-11-30', 'P2024-11-02', 'P2024-08-03', 'P2024-07-13'], 'RC-037; RC-561; RC-586; RC-664; RC-217; RC-700; RC-701; RC-465; RC-480; RC-734; RC-584', True),
    ("RC-697", "Mão Invisível Multiforme / Conselho das Nagas", SER_LOG[0], SER_LOG[1], C, ['P2025-02-16', 'P2024-09-29'], 'RC-664; RC-397; RC-092; RC-663; RC-509; RC-670; RC-577; RC-696; RC-700; RC-698', True),
    ("RC-698", "Cessão Consciente do DNA Humano", PRO_BIO[0], PRO_BIO[1], C, ['P2025-02-16', 'P2025-02-15', 'P2024-11-30'], 'RC-217; RC-359; RC-545; RC-693; RC-664; RC-056; RC-544; RC-694; RC-710; RC-699', True),
    ("RC-699", "Imantação de Espíritos em Inteligências Artificiais / Corpos de Sílica", PRO_ESP[0], PRO_ESP[1], C, ['P2025-02-16', 'P2025-02-15', 'P2024-07-13', 'P2024-03-03', 'P2026-08-04'], 'RC-645; RC-646; RC-620; RC-644; RC-100; RC-632; RC-697; RC-709', True),
    ("RC-700", "Kashyapa", SER_HUM[0], SER_HUM[1], C, ['P2025-02-16', 'P2024-11-02', 'P2024-08-03'], 'RC-586; RC-465; RC-664; RC-696; RC-701; RC-480; RC-581; RC-697; RC-734', True),
    ("RC-701", "Daksha e Virini", GEN_DIV[0], GEN_DIV[1], C, ['P2025-02-16', 'P2024-11-02', 'P2024-08-03', 'P2024-09-28'], 'RC-700; RC-664; RC-696; RC-465; RC-480; RC-586; RC-734; RC-037', True),

    # ---- P2025-02-15 — Camuflagem da Realidade / Postulados Quânticos
    ("RC-702", "Camuflagem da Realidade", COS_DIM[0], COS_DIM[1], C, ['P2025-02-15', 'P2024-07-13', 'P2024-03-03', 'P2026-08-04', 'P2023-05-13'], 'RC-192; RC-335; RC-563; RC-551; RC-372; RC-703; RC-706; RC-253; RC-657; RC-003; RC-711', True),
    ("RC-703", "Postulados Quânticos como Manual Operativo", COS_LEI[0], COS_LEI[1], C, ["P2025-02-15"], "RC-546; RC-559; RC-633; RC-509; RC-695; RC-702; RC-707; RC-712", True),
    ("RC-704", "Corpo Sutil Reencarnante", COS_DIM[0], COS_DIM[1], C, ['P2025-02-15', 'P2024-11-30', 'P2024-11-09', 'P2024-07-14', 'P2024-04-14'], 'RC-519; RC-543; RC-548; RC-692; RC-623; RC-624; RC-625; RC-553; RC-558; RC-719; RC-726; RC-618', True),
    ("RC-705", "Ato de Verdade / Satyagraha", COS_ETI[0], COS_ETI[1], C, ['P2025-02-15', 'P2024-11-09', 'P2024-09-29', 'P2024-03-03'], 'RC-508; RC-509; RC-328; RC-566; RC-695; RC-703; RC-722; RC-725; RC-658; RC-559', True),
    ("RC-706", "Bhavaṅga / Janela da Percepção", TER_SAN[0], TER_SAN[1], C, ['P2025-02-15', 'P2024-07-14'], 'RC-702; RC-552; RC-623; RC-624; RC-625; RC-633; RC-704; RC-166', True),
    ("RC-707", "Primado da Informação", COS_LEI[0], COS_LEI[1], C, ["P2025-02-15"], "RC-194; RC-218; RC-546; RC-693; RC-514; RC-703; RC-708", True),
    ("RC-708", "Ser Humano Não Local", COS_PRO[0], COS_PRO[1], C, ['P2025-02-15', 'P2024-11-09', 'P2025-06-14'], 'RC-509; RC-161; RC-559; RC-418; RC-707; RC-702; RC-372; RC-654; RC-636', True),
    ("RC-709", "Humano Turbinado", SER_HIB[0], SER_HIB[1], C, ['P2025-02-15', 'P2024-07-13'], 'RC-544; RC-645; RC-646; RC-699; RC-710; RC-557; RC-614; RC-615; RC-712', True),
    ("RC-710", "Genes Críticos / Genes Dorminhocos", PRO_BIO[0], PRO_BIO[1], C, ["P2025-02-15"], "RC-518; RC-543; RC-619; RC-400; RC-544; RC-712; RC-709; RC-693; RC-698", True),
    ("RC-711", "Universo de Egrégoras Emocionais", COS_DIM[0], COS_DIM[1], C, ['P2025-02-15', 'P2024-11-09', 'P2024-07-13'], 'RC-385; RC-529; RC-520; RC-523; RC-548; RC-517; RC-702; RC-194; RC-724', True),
    ("RC-712", "Lei da Mente do Buda", COS_LEI[0], COS_LEI[1], C, ["P2025-02-15", 'P2025-06-14; RC-618'], "RC-633; RC-619; RC-552; RC-703; RC-710; RC-695; RC-517", True),
    ("RC-713", "Taumaturgia Genético-Química", PRO_ESP[0], PRO_ESP[1], C, ["P2025-02-15"], "RC-072; RC-259; RC-217; RC-367; RC-633; RC-712", True),

    # ---- P2024-11-30 — Moros / Arquivos do Destino Universal
    ("RC-714", "Arquivos do Destino Universal", TEC_ESC[0], TEC_ESC[1], C, ["P2024-11-30"], "RC-454; RC-611; RC-715; RC-716; RC-658; RC-521; RC-094; RC-718", True),
    ("RC-715", "Informações Vivas", COS_LEI[0], COS_LEI[1], C, ['P2024-11-30', 'P2024-07-13'], 'RC-161; RC-162; RC-217; RC-693; RC-714; RC-716; RC-717; RC-176', True),
    ("RC-716", "PIA — Peso da Inevitabilidade Ancestral", COS_LEI[0], COS_LEI[1], C, ["P2024-11-30"], "RC-454; RC-519; RC-217; RC-658; RC-715; RC-332; RC-714; RC-720", True),
    ("RC-717", "Buraco Negro Mental / Consciencial", PRO_ESP[0], PRO_ESP[1], C, ['P2024-11-30', 'P2024-11-09', 'P2025-06-14', 'P2026-08-04', 'P2023-05-13'], 'RC-638; RC-690; RC-001; RC-414; RC-715; RC-716; RC-425; RC-721; RC-714; RC-152; RC-530; RC-559', True),
    ("RC-718", "Cumprimento da Profecia de Moros pela Revelação Cósmica", EVE_PRO[0], EVE_PRO[1], C, ["P2024-11-30", 'P2023-12-02', 'P2021-03-27', 'P2025-11-29; RC-714; RC-454'], "RC-094; RC-611; RC-454; RC-190; RC-585; RC-659; RC-665; RC-714", True),
    ("RC-719", "Três Faíscas da Consciência Humana", COS_DIM[0], COS_DIM[1], C, ['P2024-11-30', 'P2024-07-14'], 'RC-623; RC-217; RC-553; RC-633; RC-704; RC-529; RC-654; RC-557; RC-558', True),
    ("RC-720", "Sócios do Destino / Ausência de Justiça Externa", COS_ETI[0], COS_ETI[1], C, ['P2024-11-30', 'P2024-11-09'], 'RC-658; RC-655; RC-508; RC-328; RC-716; RC-519; RC-404; RC-715; RC-721; RC-723; RC-725; RC-009; RC-618; RC-529', True),

    # ---- P2024-11-09 — O Abismo da Consciência Cósmica
    ("RC-721", "Abismo da Consciência Cósmica", COS_PRO[0], COS_PRO[1], C, ["P2024-11-09"], "RC-605; RC-508; RC-720; RC-717; RC-722; RC-723; RC-654", True),
    ("RC-722", "Dignidade como Critério de Consciência", COS_ETI[0], COS_ETI[1], C, ['P2024-11-09', 'P2024-09-29', 'P2024-07-14', 'P2024-07-13', 'P2024-09-28', 'P2024-08-03'], 'RC-508; RC-328; RC-705; RC-509; RC-721; RC-725; RC-072; RC-514; RC-633; RC-745; RC-662; RC-406; RC-192', True),
    ("RC-723", "Abismo da Providência / Falsa Providência", COS_ESP[0], COS_ESP[1], C, ['P2024-11-09', 'P2024-07-14', 'P2024-07-13'], 'RC-052; RC-205; RC-341; RC-720; RC-605; RC-721; RC-513', True),
    ("RC-724", "Formas-Pensamento e Formas-Sentimento", COS_ESP[0], COS_ESP[1], C, ['P2024-11-09', 'P2024-07-13', 'ART-2026-08-18'], 'RC-548; RC-711; RC-381; RC-194; RC-385; RC-188', True),
    ("RC-725", "Ponto de Luz Humano / Ilha de Negentropia", COS_PRO[0], COS_PRO[1], C, ['P2024-11-09', 'P2024-09-29', 'P2024-07-13'], 'RC-160; RC-508; RC-705; RC-163; RC-690; RC-722; RC-727; RC-720', True),
    ("RC-726", "Faixas Espirituais de Ressonância", COS_DIM[0], COS_DIM[1], C, ['P2024-11-09', 'P2024-07-14'], 'RC-084; RC-513; RC-507; RC-633; RC-704; RC-529; RC-745', True),
    ("RC-727", "DNA Insubmisso / Linhagem Pandora–Eva–Noreia", GEN_HUM[0], GEN_HUM[1], C, ['P2024-11-09', 'P2024-08-03', 'P2024-07-13', 'B087', 'B088', 'B089'], 'RC-086; RC-189; RC-579; RC-619; RC-283; RC-486; RC-325; RC-725; RC-525', True),

    # ---- P2024-11-02 — Fantasmas do Passado Mitológico
    ("RC-728", "Fantasmas do Passado Mitológico", COS_PRO[0], COS_PRO[1], C, ["P2024-11-02"], "RC-729; RC-730; RC-731; RC-732; RC-733; RC-734; RC-735; RC-094", True),
    ("RC-729", "Jabutis Genéticos", PRO_BIO[0], PRO_BIO[1], C, ["P2024-11-02"], "RC-217; RC-543; RC-518; RC-710; RC-732; RC-325; RC-619", True),
    ("RC-730", "Yggdrasil / Conglomerado dos Nove Mundos", LOK_REG[0], LOK_REG[1], C, ["P2024-11-02", 'P2024-03-02', 'P2024-08-03'], "RC-470; RC-471; RC-395; RC-731; RC-320; RC-734", True),
    ("RC-731", "Axis Mundi / Axismund", LOK_REG[0], LOK_REG[1], C, ["P2024-11-02"], "RC-730; RC-470; RC-471; RC-734; RC-106; RC-107; RC-575", True),
    ("RC-732", "Invasão Ancestral do Genoma e do Psiquismo Humanos", PRO_BIO[0], PRO_BIO[1], C, ['P2024-11-02', 'P2024-08-03', 'P2024-07-13'], 'RC-217; RC-543; RC-188; RC-335; RC-733; RC-729; RC-637; RC-710; RC-518', True),
    ("RC-733", "Dominação Psíquica pela Devoção", PRO_ESP[0], PRO_ESP[1], C, ['P2024-11-02', 'P2024-07-14'], 'RC-188; RC-335; RC-385; RC-548; RC-724; RC-732; RC-735; RC-176; RC-745', True),
    ("RC-734", "Samudra Manthana / Batimento do Oceano de Leite", EVE_MIS[0], EVE_MIS[1], C, ['P2024-11-02', 'P2024-08-03'], 'RC-135; RC-037; RC-465; RC-466; RC-696; RC-731; RC-730; RC-742', True),
    ("RC-735", "Abraço aos Fantasmas / Integridade sem Combate", COS_ETI[0], COS_ETI[1], C, ["P2024-11-02"], "RC-508; RC-705; RC-722; RC-725; RC-728; RC-733; RC-166", True),

    # ---- P2024-09-29 — A Aristocracia Olimpiana e as Monarquias Terrestres
    ("RC-736", 'Aristocracia Olimpiana e Monarquias Terrestres', GEN_HUM[0], GEN_HUM[1], C, ['P2024-09-29', 'B087', 'B088', 'B089'], 'RC-001; RC-037; RC-041; RC-049; RC-145; RC-194; RC-202; RC-240; RC-254; RC-269; RC-293; RC-323; RC-325; RC-480; RC-531; RC-697; RC-737; RC-741; RC-738; RC-739; RC-722', True),
    ("RC-737", 'Projeto Amaterasu–Kami no Japão', EVE_MIS[0], EVE_MIS[1], C, ['P2024-09-29'], 'RC-001; RC-145; RC-269; RC-531; RC-736; RC-738; RC-739; RC-740', True),
    ("RC-738", 'Amaterasu (Teologia Comparada de Ellam)', SER_DIV[0], SER_DIV[1], C, ['P2024-09-29'], 'RC-737; RC-739; RC-740; RC-145; RC-269; RC-736', True),
    ("RC-739", 'Susanoo (Teologia Comparada de Ellam)', SER_DIV[0], SER_DIV[1], C, ['P2024-09-29'], 'RC-737; RC-738; RC-740; RC-145; RC-269', True),
    ("RC-740", 'Kami (Projeto Japonês)', SER_COL[0], SER_COL[1], C, ['P2024-09-29'], 'RC-737; RC-738; RC-739; RC-269; RC-531; RC-104; RC-454; RC-664', True),
    ("RC-741", 'Projeto Orunmilá–Olodus', EVE_MIS[0], EVE_MIS[1], C, ['P2024-09-29', 'P2025-11-29'], 'RC-001; RC-037; RC-454; RC-560; RC-655; RC-658; RC-665; RC-666; RC-736', True),

    # ---- P2024-08-03 — A Falência dos Deuses e a Destinação do Lobo
    ("RC-742", 'Falência dos Deuses', EVE_CAT[0], EVE_CAT[1], C, ['P2024-08-03', 'P2024-07-14', 'P2024-07-13'], 'RC-040; RC-734; RC-395; RC-604', True),
    ("RC-743", 'Destinação do Lobo', COS_PRO[0], COS_PRO[1], C, ['P2024-08-03'], 'RC-529; RC-525', True),
    ("RC-744", 'Pendências Existenciais em Realidades Paralelas', COS_DIM[0], COS_DIM[1], C, ['P2024-08-03'], 'RC-108', True),

    # ---- P2024-07-14 — Consciências Espirituais Dignificadas
    ("RC-745", 'Colegiados Espirituais Humanizados', COS_DIM[0], COS_DIM[1], C, ['P2024-07-14'], 'RC-726; RC-722; RC-193; RC-733; RC-513; RC-633; RC-612; RC-613', True),
    ("RC-746", "Dessensibilização da Condição Humana", COS_LEI[0], COS_LEI[1], C, ['P2024-03-03', 'P2026-08-04'], 'RC-529; RC-049; RC-001; RC-378; RC-335; RC-705; RC-747; RC-748', True),
    ("RC-747", "Vergonha de Existir", COS_ETI[0], COS_ETI[1], C, ['P2024-03-03'], 'RC-746; RC-078; RC-705; RC-722', True),
    ("RC-748", "Genótipo da Gentileza (GG)", PRO_BIO[0], PRO_BIO[1], C, ['P2024-03-03', 'P2024-09-28', 'B040'], 'RC-746; RC-486; RC-543; RC-541', True),
    ("RC-749", "Vício Devocional", COS_ETI[0], COS_ETI[1], C, ['P2024-04-13', 'P2023-12-02', 'P2025-11-29'], 'RC-001; RC-335; RC-019; RC-194; RC-746', True),
    ("RC-750", "Moisés e o Êxodo (leitura RC)", EVE_MIS[0], EVE_MIS[1], C, ['P2024-04-13'], 'RC-001; RC-164; RC-424; RC-271; RC-683', True),
    ("RC-751", "Bagagem Espiritual Intransferível", COS_PRO[0], COS_PRO[1], C, ['P2024-04-14'], 'RC-752; RC-548; RC-704; RC-164; RC-332', True),
    ("RC-752", "Agenda Espiritual", COS_PRO[0], COS_PRO[1], C, ['P2024-04-14'], 'RC-751; RC-164; RC-332; RC-704; RC-695', True),
    ("RC-753", "Estrangulamento Cognitivo / Neural", COS_LEI[0], COS_LEI[1], C, ['P2025-06-14'], 'RC-754; RC-166; RC-708; RC-163; RC-558', True),
    ("RC-754", "Chave da Decifração Universal", COS_PRO[0], COS_PRO[1], C, ['P2025-06-14'], 'RC-753; RC-755; RC-695; RC-316; RC-094', True),
    ("RC-755", "Escola da Decifração da Realidade (Método Druídico)", COS_ESP[0], COS_ESP[1], C, ['P2025-06-14', 'P2024-02-03'], 'RC-754; RC-166; RC-695; RC-094', True),
    ("RC-756", "Ganesha (exceção à metamorfose; cabeça de elefante)", SER_DIV[0], SER_DIV[1], C, ['P2024-03-02'], 'RC-102; RC-459; RC-604; RC-414', True),
    ("RC-757", "Vaishnavismo (vixenuísmo — tradição hindu de adoração a Vishnu/Krishna)", TER_SAN[0], TER_SAN[1], C, ['P2024-03-02'], 'RC-135; RC-414; RC-104; RC-503', True),
    ("RC-758", "Quarto Cérebro (centro de sabedoria vibracional)", COS_PRO[0], COS_PRO[1], C, ['ART-2026-08-18'], 'RC-092; RC-009; RC-514; RC-086; RC-553', True),
    ("RC-759", "Jainismo (antigo Druidismo — religião mais antiga)", COS_ESP[0], COS_ESP[1], C, ['P2024-02-03'], 'RC-397; RC-755; RC-618; RC-398; RC-760', True),
    ("RC-760", "Vrittis e Cittas (atividades e núcleos mentais)", TER_SAN[0], TER_SAN[1], C, ['P2024-02-03', 'P2025-11-29'], 'RC-755; RC-559; RC-517; RC-548; RC-759', True),
    ("RC-761", "As Cinco Lentes da Realidade", COS_PRO[0], COS_PRO[1], C, ['P2023-05-13'], 'RC-094; RC-001; RC-009; RC-541; RC-702; RC-192; RC-080; RC-092; RC-042; RC-056; RC-604; RC-176; RC-166; RC-695; RC-612; RC-717; RC-559; RC-454; RC-072; RC-167', True),
    ("RC-762", "As Três Escalas da Consciência (Sábio → Mago → Iniciado)", COS_ESP[0], COS_ESP[1], C, ['P2023-12-02'], 'RC-463; RC-761; RC-264; RC-092; RC-372; RC-695', True),
    ("RC-763", "As Sete Leis Herméticas", COS_LEI[0], COS_LEI[1], C, ['P2023-12-02'], 'RC-463; RC-762; RC-703; RC-559; RC-658', True),
    ("RC-764", "Ao Vencedor as Batatas (paradigma do domínio)", COS_ETI[0], COS_ETI[1], C, ['P2021-03-27'], 'RC-024; RC-001; RC-164; RC-449; RC-486; RC-487; RC-488', True),
    ("RC-765", "Relógio Messiânico", EVE_PRO[0], EVE_PRO[1], C, ['P2021-03-27'], 'RC-460; RC-009; RC-592; RC-481; RC-282; RC-074; RC-001', True),
    ("RC-766", "A Raça Inabalável dos Sethianos Emancipados", SER_HUM[0], SER_HUM[1], C, ['P2024-09-28'], 'RC-594; RC-514; RC-748; RC-722; RC-092; RC-483; RC-009; RC-072', True),
    ("RC-767", "Os 256 Caminhos Profetizáveis de Orunmilá", COS_PRO[0], COS_PRO[1], C, ['P2025-11-29'], 'RC-665; RC-658; RC-655; RC-454; RC-517; RC-548; RC-760; RC-056', True),
    ("RC-768", "Princípio da Externalização (criação divina sem sexualidade)", PRO_FIS[0], PRO_FIS[1], C, ['P2026-07-25'], 'RC-040; RC-153; RC-475; RC-622; RC-385; RC-104; RC-769', True),
    ("RC-769", "Corpos Fenvã (terceira forma de vida do universo vizinho)", SER_EXT[0], SER_EXT[1], C, ['P2026-07-25'], 'RC-630; RC-475; RC-622; RC-696; RC-104; RC-768', True),
    ("RC-770", "Hipóstase dos Arcontes (livro gnóstico; 'realidade dos regentes')", TEC_ESC[0], TEC_ESC[1], C, ['P2026-07-25'], 'RC-474; RC-482; RC-530; RC-579; RC-454; RC-658; RC-152; RC-072', True),
    ("RC-771", "Fornos Replicadores (naves/estações de semeadura de vida do Projeto Talm; Awayen, Awaylengan e Awaymaion)", TEC_NAV[0], TEC_NAV[1], P, ['B061', 'P2021-12-04', 'P2024-05-04', 'ART-2025-08-01'], 'RC-091; RC-499; RC-132; RC-092; RC-064; RC-093; RC-035', True),
    ("RC-772", "Morlens (programador genético atômico do Projeto TALM; 'monstro ciberenergético')", SER_EXT[0], SER_EXT[1], P, ['ART-2025-08-03'], 'RC-773; RC-775; RC-091', True),
    ("RC-773", "Nanotecnologia Prânica (manipulação da matéria em escala atômica; base tecnológica do Projeto TALM)", TEC_NAV[0], TEC_NAV[1], P, ['ART-2025-08-03'], 'RC-091; RC-772; RC-774; RC-081', True),
    ("RC-774", "PEP — Pulso Eletromagnético Particularizado (transferência de nanopontos da genética entre universos)", TEC_NAV[0], TEC_NAV[1], P, ['ART-2025-08-03'], 'RC-773; RC-154; RC-091; RC-081', True),
    ("RC-775", "Éon das Três Esferas (superloka/geno; repositório de tesouros genéticos do Projeto TALM)", LOK_REG[0], LOK_REG[1], P, ['ART-2025-08-03'], 'RC-091; RC-771; RC-081; RC-772; RC-454; RC-467; RC-064', True),
    ("RC-776", "Ginnungagap (zona intercessória entre universos; prisão dos fenvans frustrados)", LOK_REG[0], LOK_REG[1], P, ['ART-2025-08-03'], 'RC-064; RC-080; RC-154', True),
    ("RC-777", "Anã (estudou as necessidades dos códigos podres, com Moros; base das Nornes) [REVISAR — grafia]", SER_EXT[0], SER_EXT[1], P, ['ART-2025-08-03'], 'RC-454; RC-467; RC-775', True),
]

# Relações tipadas (grafo) — (termoA, tipo, termoB, obra)








RELACOES = [
    ("RC-001", "sinônimo", "RC-037", "B031"),        # Javé = Brahma
    ("RC-001", "sinônimo", "RC-041", "B031"),        # Javé = Criador
    ("RC-041", "sinônimo", "RC-048", "B031"),        # Criador = Demiurgo (Platão)
    ("RC-009", "variação", "RC-081", "B031"),        # Sophia é avatar de Mohen So
    ("RC-078", "variação", "RC-142", "B031"),        # Lúcifer = Yel Luzbel
    ("RC-071", "variação", "RC-095", "B031"),        # Jan Val Ellam = Rogério de Almeida Freitas
    ("RC-083", "sinônimo", "RC-068", "B031"),        # Norte Divino = Hiperbórea
    ("RC-106", "sinônimo", "RC-038", "B031"),        # Universo Antimaterial = Brahmaloka
    ("RC-106", "sinônimo", "RC-108", "B031"),        # Universo Antimaterial = Universo Paralelo
    ("RC-107", "sinônimo", "RC-033", "B031"),        # Universo Material = Bhuloka
    ("RC-078", "inicia", "RC-002", "B031"),          # Lúcifer iniciou a Rebelião
    ("RC-002", "resulta-em", "RC-070", "B031"),      # Rebelião → Isolamento Cósmico
    ("RC-070", "termina-com", "RC-005", "B031"),     # Isolamento → vinda de Sophia
    ("RC-005", "inicia", "RC-003", "B031"),          # Segundo Advento → Reintegração
    ("RC-009", "ocorre-em", "RC-085", "B031"),       # Sophia governa de Orbum
    ("RC-091", "envolve", "RC-104", "B031"),         # Projeto Talm envolve a Trimurti
    ("RC-009", "é-um", "RC-081", "B031"),            # Sophia é avatar de Mohen So
    ("RC-081", "é-um", "RC-135", "B031"),            # Mohen So é avatar de Vishnu
    ("RC-036", "criado-por", "RC-041", "B031"),      # Biodemos criados pelo Criador
    ("RC-109", "parte-de", "RC-036", "B031"),        # Família Val é tipo de biodemo
    ("RC-136", "parte-de", "RC-036", "B031"),        # Família Yel é tipo de biodemo
    ("RC-007", "origem-em", "RC-039", "B031"),       # Exilados vêm de Capela
    ("RC-078", "associado-a", "RC-086", "B031"),     # Pandora: deslacre humano

    # ---- Relações novas (B024 - A Epopeia dos Agentes da Vida Universal)
    ("RC-037", "variação", "RC-152", "B024"),        # Brahma (após queda) = Prabrajna (antes)
    ("RC-102", "variação", "RC-152", "B024"),        # Savna = Shiva (após mergulho)
    ("RC-135", "variação", "RC-152", "B024"),        # Mavatna = Vishnu (após mergulho)
    ("RC-152", "inicia", "RC-167", "B024"),          # Prabrajna inicia a Criação Indevida
    ("RC-150", "envolve", "RC-104", "B024"),         # Xadrez Cósmico envolve a Trimurti
    ("RC-151", "associado-a", "RC-037", "B024"),     # Gunas ↔ Brahma (Rajas)
    ("RC-151", "associado-a", "RC-102", "B024"),     # Gunas ↔ Shiva (Tamas)
    ("RC-151", "associado-a", "RC-135", "B024"),     # Gunas ↔ Vishnu (Sattva)
    ("RC-148", "é-um", "RC-149", "B024"),            # Agentes da Vida = portadores de mônadas
    ("RC-161", "relaciona-se-a", "RC-162", "B024"),  # memória quântica ↔ elétrons
    ("RC-091", "ocorre-em", "RC-169", "B024"),       # Projeto Talm efetiva-se na Era da Semeadura
    ("RC-153", "deriva-de", "RC-040", "B024"),       # CFDP → CFD
    ("RC-154", "produzido-por", "RC-091", "B024"),   # nidana produzido pelo Projeto Talm

    # ---- Relações novas (B044 - A Divina Colmeia)
    ("RC-175", "variação", "RC-001", "B044"),        # Abelha-Rainha = epíteto de Javé
    ("RC-178", "parte-de", "RC-174", "B044"),        # Dois Grandes Favos compõem a Colmeia Universal
    ("RC-106", "parte-de", "RC-178", "B044"),        # Universo Antimaterial = favo improvisado
    ("RC-107", "parte-de", "RC-178", "B044"),        # Universo Material = favo planejado
    ("RC-176", "implementa", "RC-188", "B044"),      # Modelo Colmeia = mente coletiva sob controle
    ("RC-179", "associado-a", "RC-091", "B044"),     # Plano Colmeia ↔ Projeto Talm
    ("RC-183", "associado-a", "RC-044", "B044"),     # Cultura Demodhármica ↔ Cultura Demo
    ("RC-086", "rompe", "RC-184", "B044"),           # Pandora rompeu a Trava-demo
    ("RC-186", "é-um", "RC-036", "B044"),            # Biodemol é tipo de biodemo
    ("RC-187", "é-um", "RC-098", "B044"),            # Insectoides são seres extraterrestres
    ("RC-190", "associado-a", "RC-094", "B044"),     # Revelação Espiritual ↔ Revelação Cósmica
    ("RC-192", "associado-a", "RC-094", "B044"),     # Pílula vermelha ↔ busca da verdade

    # ---- Relações novas (B035 - O Big Data do Criador — amostra)
    ("RC-194", "instrumento-de", "RC-001", "B035"),  # Big Data Cósmico = supercontrole de Javé
    ("RC-194", "relaciona-se-a", "RC-195", "B035"),  # Big Data Cósmico ↔ Simbiose Quântica
    ("RC-195", "abrange", "RC-167", "B035"),         # Simbiose Quântica abrange toda a Criação
    ("RC-196", "é-um", "RC-041", "B035"),            # "Criador refém" = condição do Criador
    ("RC-197", "analogia-de", "RC-194", "B035"),     # Big Data da Terra = analogia terrena do cósmico
    ("RC-201", "associado-a", "RC-200", "B035"),     # Livro do Criador ↔ Base de Dados do Juízo Final

    # ---- Relações novas (Trilogia dos Dramas de Javé: B001/B002/B033)
    ("RC-001", "é-um", "RC-207", "B001"),            # Javé é um Arquiteto Universal
    ("RC-207", "variação", "RC-041", "B001"),        # Arquiteto Universal = Criador (pré-queda)
    ("RC-210", "depende-de", "RC-204", "B001"),      # Matriz Modeladora depende da Realidade Maior
    ("RC-047", "personifica-em", "RC-205", "B001"),  # Deidade se personifica no Pai Supremo
    ("RC-205", "personifica-em", "RC-206", "B001"),  # Pai Supremo → Divindades Excelsas
    ("RC-217", "é-um", "RC-040", "B002"),            # DNA = projeção holográfica (CFD físico-químico)
    ("RC-216", "resulta-em", "RC-001", "B002"),      # Queda do Arquiteto → Senhor Javé
    ("RC-219", "variação", "RC-072", "B002"),        # Agente Secreto do Bem (hipótese: Jesus)
    ("RC-222", "associado-a", "RC-149", "B002"),     # Filhos das Estrelas ↔ Mônadas
    ("RC-223", "associado-a", "RC-190", "B002"),     # O Mal ↔ Revelação Espiritual
    ("RC-225", "envolve", "RC-104", "B033"),         # Gestão Cósmica envolve a Trimurti
    ("RC-225", "divide-com", "RC-072", "B033"),      # Gestão Cósmica é dividida com Jesus
    ("RC-226", "relaciona-se-a", "RC-003", "B033"),  # Cidadão Cósmico ↔ Reintegração Cósmica
    ("RC-155", "fonte-em", "RC-225", "B033"),        # Eras da Criação ↔ Gestão Cósmica
    ("RC-196", "variação", "RC-213", "B033"),        # (alinhar com narrativa do Drama Terreno)

    # ---- Relações novas (Trilogia Terra Atlantis: B017/B018/B039)
    ("RC-232", "é-um", "RC-098", "B017"),            # Ostronomos são seres extraterrestres
    ("RC-232", "associado-a", "RC-024", "B017"),     # Ostronomos ↔ Anunnakis (origem comum)
    ("RC-241", "é-um", "RC-049", "B017"),            # Seres dos Portais são demos
    ("RC-241", "associado-a", "RC-145", "B017"),     # Seres dos Portais ↔ deuses gregos (Zeus)
    ("RC-233", "descoberto-por", "RC-109", "B017"),  # Marca Val descoberta pela Família Val
    ("RC-233", "revela", "RC-186", "B017"),          # Marca Val revela o Biodemol
    ("RC-234", "associado-a", "RC-058", "B018"),     # Cidades Voadoras ↔ Espheron
    ("RC-236", "envolve", "RC-072", "B039"),         # Calvário de um Inocente envolve Jesus
    ("RC-236", "afeta", "RC-078", "B039"),           # Calvário afeta Yel Luzbel (retirada)
    ("RC-239", "dominado-por", "RC-074", "B039"),    # Hitler dominado por Len Mion
    ("RC-240", "é-um", "RC-241", "B018"),            # Império dos Descendentes é dos Seres dos Portais
    ("RC-238", "ocorre-após", "RC-010", "B039"),     # Era Sapiens após o fim de Atlantis
    ("RC-237", "associado-a", "RC-010", "B039"),     # Land's End ↔ Terra Atlantis (sinal)

    # ---- Relações novas (B015 - O Guardião do Éden)
    ("RC-147", "é-um", "RC-055", "B015"),            # Zont En Drel 29 é um En Drel
    ("RC-247", "é-um", "RC-055", "B015"),            # Endrelnianos = membros dos En Drel
    ("RC-242", "é-um", "RC-251", "B015"),            # Éden é um dos laboratórios do Criador
    ("RC-242", "guarda", "RC-147", "B015"),          # Éden guardado por Zont En Drel 29
    ("RC-243", "opõe-se-a", "RC-244", "B015"),       # Genética da Confiança × Germe da Desconfiança
    ("RC-244", "herdado-de", "RC-041", "B015"),      # Germe da Desconfiança herdado do Criador
    ("RC-243", "base-do", "RC-099", "B015"),         # Genética da Confiança base do amor humano
    ("RC-248", "associado-a", "RC-134", "B015"),     # Viajores da Rebelião ↔ Viajores (Anunnakis)
    ("RC-249", "executado-por", "RC-147", "B015"),   # Expulsão dos Viajores executada por Zont
    ("RC-250", "habitado-por", "RC-248", "B015"),    # Mundo das Águas habitado pelos Viajores
    ("RC-246", "mentor-de", "RC-055", "B015"),       # Um dos Dez Sagrados é mentor dos En Drel
    ("RC-245", "experimenta", "RC-147", "B015"),     # Humanização do Criador observada por Zont

    # ---- Relações novas (B016 - O Quarto Logos)
    ("RC-252", "variação", "RC-092", "B016"),        # Olm = Quarto Logos / Codificador de Zion
    ("RC-253", "rompe-com", "RC-254", "B016"),       # Liberdade Mental rompe com a Dominação
    ("RC-254", "premissa-de", "RC-104", "B016"),     # Dominação é premissa da Trimurti
    ("RC-257", "é-um", "RC-190", "B016"),            # Espiritismo (expressão do 4º Logos) é Revelação Espiritual
    ("RC-259", "é-um", "RC-252", "B016"),            # Apolônio de Tiana é encarnação de Olm
    ("RC-260", "inclui", "RC-041", "B016"),          # Prisioneiros da Brahmaloka inclui Brahma/Javé
    ("RC-260", "opõe-se-a", "RC-016", "B016"),       # Prisioneiros × expressões Adhyajna (que Brahma não produz)
    ("RC-255", "proferida-por", "RC-252", "B016"),   # Mensagem do Codificador proferida por Olm
    ("RC-256", "fundada-por", "RC-252", "B016"),     # Escola fundada por Olm
    ("RC-258", "envolve", "RC-009", "B016"),         # Coreografia Cósmica envolve a vinda de Sophia

    # ---- Relações novas (B013 - Tzimtzum)
    ("RC-261", "variação", "RC-001", "B013"),        # Kether = Javé (na Cabala)
    ("RC-261", "variação", "RC-037", "B013"),        # Kether = Brahma
    ("RC-008", "explica", "RC-261", "B013"),         # Tzimtzum explica o exílio de Kether/Javé
    ("RC-008", "relaciona-se-a", "RC-272", "B013"),  # Tzimtzum ↔ Laço Temporal
    ("RC-264", "inclui", "RC-059", "B013"),          # Atziluth = Espiritualidade Superior/Operacional
    ("RC-264", "inclui", "RC-061", "B013"),          # Briah = Espiritualidade Laboratorial (Perpérion)
    ("RC-264", "inclui", "RC-038", "B013"),          # Yetzirah = Brahmaloka
    ("RC-264", "inclui", "RC-107", "B013"),          # Assiah = Bhuloka (universo material)
    ("RC-263", "compõe", "RC-261", "B013"),          # Sefirot emanações de Kether
    ("RC-265", "profecias-em", "RC-266", "B013"),    # 270 Mundos profetizados no Zohar
    ("RC-268", "opõe-se-a", "RC-261", "B013"),       # Gnosticismo crítica Kether/Javé
    ("RC-266", "revelado-por", "RC-261", "B013"),    # Zohar revelado por ordem de Javé
    ("RC-269", "escolhe", "RC-270", "B013"),         # Linhagens preferidas escolhem os patriarcas

    # ---- Relações novas (B014 - Sophia e o Logos Criadores)
    ("RC-009", "é-um", "RC-081", "B014"),            # Sophia é avatar gerado por Mohen So
    ("RC-009", "é-um", "RC-135", "B014"),            # Sophia é avatar (indireto) de Vishnu
    ("RC-081", "variação", "RC-282", "B014"),        # Mohen So = Phanes (orfismo)
    ("RC-282", "associado-a", "RC-135", "B014"),     # Vasuki/Kalki ↔ Vishnu (hindu)
    ("RC-273", "obscurece", "RC-009", "B014"),       # Falsa Trindade obscureceu Sophia
    ("RC-274", "associado-a", "RC-005", "B014"),     # Cápsula do Tempo ↔ promessa do retorno
    ("RC-274", "revelada-a", "RC-072", "B014"),      # Cápsula do Tempo ↔ João (Apocalipse)
    ("RC-276", "opõe-se-a", "RC-253", "B014"),       # Sacralização do Absurdo × Liberdade Mental
    ("RC-277", "relaciona-se-a", "RC-176", "B014"),  # Jaula de Cada Espécie ↔ Modelo Colmeia
    ("RC-281", "é-um", "RC-092", "B014"),            # Agentes do Quarto Logos servem o 4º Logos
    ("RC-280", "envolve", "RC-009", "B014"),         # Ressurreição envolve Sophia
    ("RC-280", "envolve", "RC-072", "B014"),         # Ressurreição envolve Jesus
    ("RC-275", "relaciona-se-a", "RC-183", "B014"),  # Arte Demodhármica ↔ Cultura Demodhármica

    # ---- Relações novas (B020 - O Sorriso de Pandora)
    ("RC-086", "variação", "RC-118", "B020"),        # Pandora = Val Dimon (biodemo → demo)
    ("RC-086", "é-um", "RC-283", "B020"),            # Pandora = serpente do Éden
    ("RC-284", "variação", "RC-001", "B020"),        # Caos = Javé
    ("RC-284", "variação", "RC-037", "B020"),        # Caos = Brahma
    ("RC-286", "variação", "RC-135", "B020"),        # Eros = Vishnu
    ("RC-286", "variação", "RC-102", "B020"),        # Tártaro = Shiva
    ("RC-285", "rompe", "RC-184", "B020"),           # Opção Inusitada rompe a trava-demo
    ("RC-283", "afronta", "RC-284", "B020"),         # Serpente afronta Caos/Javé
    ("RC-283", "protege", "RC-189", "B020"),         # Serpente protege Eva/casal do Éden
    ("RC-287", "associado-a", "RC-086", "B020"),     # Enigma da Esperança ↔ Pandora
    ("RC-289", "envolve", "RC-086", "B020"),         # Vício de Epimeteu envolve Pandora
    ("RC-291", "inicia", "RC-094", "B020"),          # Fim do Silêncio (revelação atual)

    # ---- Relações novas (B021 - Tempos Difíceis no Olimpo)
    ("RC-292", "relaciona-se-a", "RC-293", "B021"),  # Telos ↔ Timé
    ("RC-293", "valoriza", "RC-145", "B021"),        # Timé valorizada por Zeus
    ("RC-293", "corresponde-a", "RC-301", "B021"),   # Timé = varna (talento pessoal)
    ("RC-294", "variação", "RC-284", "B021"),        # Eon de Khaos = Universo de Caos
    ("RC-294", "inclui", "RC-077", "B021"),          # Eon de Khaos é composto de genos
    ("RC-295", "envolve", "RC-145", "B021"),         # Fechamento dos Portais envolve Zeus
    ("RC-295", "resulta-em", "RC-296", "B021"),      # Fechamento → Pitonisas/Oráculos
    ("RC-296", "controla", "RC-099", "B021"),        # Pitonisas controlam os humanos
    ("RC-297", "envolve", "RC-145", "B021"),         # Era dos Humanos envolve Zeus
    ("RC-297", "sucede", "RC-295", "B021"),          # Era dos Humanos após fechamento
    ("RC-298", "origina-de", "RC-086", "B021"),      # Descendência de Pirra origina de Pandora
    ("RC-299", "variação", "RC-086", "B021"),        # Kalil Kadmon = Pandora (nome demo)
    ("RC-300", "envolve", "RC-104", "B021"),         # Dissolução da Tríade envolve a Trimurti
    ("RC-301", "opõe-se-a", "RC-145", "B021"),       # Prometeu × Zeus
    ("RC-302", "é-um", "RC-301", "B021"),            # Epimeteu é irmão de Prometeu
    ("RC-303", "parte-de", "RC-298", "B021"),        # Pirra parte da descendência
    ("RC-304", "parte-de", "RC-298", "B021"),        # Deucalião parte da descendência
    ("RC-145", "é-um", "RC-241", "B021"),            # Zeus é Ser dos Portais
    ("RC-307", "cria", "RC-086", "B021"),            # Hefesto engendrou Pandora

    # ---- Relações novas (B022 - Inquisição Trimurtiana)
    ("RC-308", "é-um", "RC-011", "B022"),            # Adhytia são da linhagem Adhy
    ("RC-308", "superior-a", "RC-104", "B022"),      # Adhytia são superiores à Trimurti
    ("RC-309", "é-um", "RC-308", "B022"),            # Ordem dos Indecifráveis são Adhytia
    ("RC-310", "variação", "RC-152", "B022"),        # Adhyshprabrajna = Prabrajna (que caiu)
    ("RC-310", "variação", "RC-037", "B022"),        # Adhyshprabrajna → Brahma/Javé/Alá
    ("RC-311", "é-um", "RC-012", "B022"),            # Adhyagya ≈ forma espiritual (Adhyagia)
    ("RC-311", "responde-por", "RC-102", "B022"),    # Adhyagya de Shiva
    ("RC-311", "responde-por", "RC-135", "B022"),    # Adhyagya de Vishnu
    ("RC-312", "inclui", "RC-106", "B022"),          # Criação Bipartida inclui universo antimaterial
    ("RC-312", "inclui", "RC-107", "B022"),          # Criação Bipartida inclui universo material
    ("RC-313", "relaciona-se-a", "RC-300", "B022"),  # Tempo de Apostasia ↔ Dissolução da Tríade
    ("RC-314", "denuncia", "RC-313", "B022"),        # Fenômenos denunciam o Tempo de Apostasia
    ("RC-315", "encerra", "RC-075", "B022"),         # O Fim da Lila encerra a Lila
    ("RC-316", "hábito-de", "RC-049", "B022"),       # Decifra-me ou Devoro é hábito demo
    ("RC-318", "envolve", "RC-102", "B022"),         # Autorrealização de Shiva

    # ---- Relações novas (B023 - O Dharma e as Castas Hindus)
    ("RC-320", "variação", "RC-104", "B023"),        # Senhores do Dharma = Trimurti
    ("RC-320", "variação", "RC-075", "B023"),        # Senhores do Dharma = Senhores da Lila
    ("RC-319", "é-um", "RC-322", "B023"),            # Fator Dharma é o dharma demo
    ("RC-321", "origina-em", "RC-329", "B023"),      # Castas originam na tradição Kumari Kandan
    ("RC-321", "origina-em", "RC-068", "B023"),      # Castas originam entre povos hiperbóreos
    ("RC-323", "envolve", "RC-082", "B023"),         # Entroncamentos envolvem Nephelim
    ("RC-323", "envolve", "RC-024", "B023"),         # Entroncamentos envolvem Anunnakis
    ("RC-325", "usa", "RC-326", "B023"),             # Genética Totalitária usa povos escolhidos
    ("RC-326", "inclui", "RC-270", "B023"),          # Povos escolhidos incluem hebreus
    ("RC-328", "surge-em", "RC-099", "B023"),        # Imperativo Categórico surge com a racionalidade humana
    ("RC-327", "é-um", "RC-099", "B023"),            # Homo hierarchicus é um modo do humano
    ("RC-331", "variação", "RC-284", "B023"),        # Ra-Atom/Og-mi são nomes do Criador
    ("RC-322", "aplica-se-a", "RC-049", "B023"),     # Dharma demo aplica-se aos demos

    # ---- Relações novas (B048 - Favor Divino)
    ("RC-332", "variação", "RC-063", "B048"),        # Favor Divino (conceito) = título da obra
    ("RC-332", "inverte", "RC-041", "B048"),         # o favor é dos humanos ao Criador
    ("RC-333", "opõe-se-a", "RC-334", "B048"),       # Democracia do Amor × Teocracia da Doença
    ("RC-333", "é-um", "RC-047", "B048"),            # Democracia do Amor é atributo da Deidade
    ("RC-334", "é-um", "RC-041", "B048"),            # Teocracia da Doença é do Criador
    ("RC-335", "aplica-a", "RC-041", "B048"),        # Lavagem Cerebral aplicada pelo Criador
    ("RC-335", "vitima", "RC-099", "B048"),          # Lavagem Cerebral vitima os humanos
    ("RC-336", "é-um", "RC-041", "B048"),            # Ética da Sobrevivência é de Javé
    ("RC-338", "relaciona-se-a", "RC-332", "B048"),  # Reconhecimento ↔ Favor Divino
    ("RC-339", "cobra", "RC-099", "B048"),           # Difícil Cobrança sobre os humanos
    ("RC-341", "usa", "RC-190", "B048"),             # Ferramentas do Favor usam as religiões
    ("RC-149", "é-um", "RC-333", "B048"),            # Mônadas são amorosas (emanadas da Deidade)

    # ---- Relações novas (Trilogia Queda e Ascensão Espiritual: B003/B025/B026)
    ("RC-342", "variação", "RC-070", "B003"),        # Quarentena Sideral = Isolamento Cósmico
    ("RC-342", "impõe-se-a", "RC-002", "B003"),      # Quarentena imposta pela Rebelião
    ("RC-342", "encerra-com", "RC-003", "B003"),     # Quarentena termina com a Reintegração
    ("RC-343", "destinação-de", "RC-090", "B003"),   # Portal Cósmico é a destinação do Planeta Azul
    ("RC-344", "antecede", "RC-003", "B003"),        # Transição Planetária antecede a Reintegração
    ("RC-346", "variação", "RC-001", "B003"),        # Jeová = Javé (grafia da trilogia)
    ("RC-347", "é-um", "RC-090", "B026"),            # Projeto Terra = plano para o Planeta Azul
    ("RC-348", "relaciona-se-a", "RC-342", "B026"),  # Roteiro do Exílio ↔ Quarentena
    ("RC-349", "origina-em", "RC-002", "B003"),      # Exílios Interplanetários originam na Rebelião
    ("RC-350", "é-um", "RC-072", "B003"),            # Jesus o Capelino = Jesus (origem capelina)
    ("RC-351", "inclui", "RC-350", "B025"),          # Mestres de Capela incluem Jesus
    ("RC-352", "variação", "RC-005", "B025"),        # Segunda Grande Vinda = Segundo Advento
    ("RC-353", "é-um", "RC-342", "B003"),            # Ilha Cósmica = os mundos em quarentena
    ("RC-354", "inclui", "RC-003", "B003"),          # Trilogia inclui Reintegração Cósmica
    ("RC-354", "inclui", "RC-025", "B003"),          # Trilogia inclui Caminhos Espirituais
    ("RC-354", "inclui", "RC-026", "B003"),          # Trilogia inclui Carma e Compromisso

    # ---- Relações novas (B005 - Fator Extraterrestre)
    ("RC-355", "é-um", "RC-098", "B005"),            # Fator Extraterrestre = componente extraterrena
    ("RC-355", "explica", "RC-020", "B005"),         # Fator Extraterrestre explica anjos decaídos
    ("RC-356", "usa", "RC-148", "B005"),             # Fonte da Vida (metáfora) usa os agentes da vida
    ("RC-357", "é-um", "RC-098", "B005"),            # Confederações de Mundos são organizações siderais
    ("RC-357", "subordinada-a", "RC-059", "B005"),   # Confederações subordinadas à Espiritualidade Superior
    ("RC-358", "é-um", "RC-357", "B005"),            # Terra de Ninguém = fora das confederações
    ("RC-359", "realizada-por", "RC-098", "B005"),   # Abduções realizadas por extraterrestres
    ("RC-360", "alternativa-a", "RC-107", "B005"),   # Atmosferizar Lua/Marte = alternativa à Terra
    ("RC-361", "opõe-se-a", "RC-231", "B005"),       # Antropocentrismo × Razão Filosófica
    ("RC-362", "opõe-se-a", "RC-253", "B005"),       # Apego aos Conceitos × Liberdade Mental
    ("RC-363", "relaciona-se-a", "RC-094", "B005"),  # Ótica e Ética Cósmicas ↔ Revelação Cósmica
    ("RC-364", "envolve", "RC-072", "B005"),         # Missão do Mestre envolve Jesus
    ("RC-355", "associado-a", "RC-094", "B005"),     # Fator Extraterrestre ↔ Revelação Cósmica

    # ---- Relações novas (Obras sobre Jesus: B011/B049/B043)
    ("RC-365", "envolve", "RC-138", "B011"),          # Fator Judas envolve Yel Am/Yel Liam (Judas)
    ("RC-365", "relaciona-se-a", "RC-236", "B011"),   # Fator Judas ↔ Calvário de um Inocente
    ("RC-366", "é-um", "RC-367", "B011"),             # Transfiguração = alteração vibratória
    ("RC-366", "envolve", "RC-072", "B011"),          # Transfiguração envolve Jesus
    ("RC-368", "assessora", "RC-072", "B011"),        # Assessoria Cósmica assessora Jesus
    ("RC-369", "parceria-de", "RC-072", "B011"),      # Nietzsche é 'amigo da intenção' de Jesus
    ("RC-370", "crítica", "RC-099", "B011"),          # Criação de Ídolos crítica a humanidade
    ("RC-371", "opõe-se-a", "RC-253", "B049"),        # Fé de Jesus vs Razão (liberdade mental)
    ("RC-372", "é-um", "RC-253", "B049"),             # Ser Humano Emancipado = liberdade mental
    ("RC-373", "envolve", "RC-072", "B043"),          # 20 Anos entre os Celtas envolve Jesus
    ("RC-374", "é-um", "RC-375", "B043"),             # Mordon é um druida
    ("RC-376", "acompanha", "RC-072", "B043"),        # José de Arimatéia acompanha Jesus
    ("RC-377", "associado-a", "RC-374", "B043"),      # Brendiver/Dolman ↔ Mordon

    # ---- Relações novas (B041 - A Rebelião dos Elétrons)
    ("RC-378", "envolve", "RC-161", "B041"),          # Rebelião envolve a memória quântica
    ("RC-378", "modifica", "RC-153", "B041"),         # Rebelião modifica o CFDP (único padrão)
    ("RC-378", "envolve", "RC-381", "B041"),          # Rebelião envolve a ressonância mórfica
    ("RC-379", "é-um", "RC-162", "B041"),             # Dança dos Elétrons é fenômeno do elétron
    ("RC-379", "sustenta", "RC-107", "B041"),         # Dança sustenta o universo material
    ("RC-380", "base-de", "RC-379", "B041"),          # Imanência/Transcendência base da dança
    ("RC-382", "é-um", "RC-040", "B041"),             # Vida do CFD = CFD vivendo no humano
    ("RC-382", "relaciona-se-a", "RC-332", "B041"),   # Vida do CFD ↔ Favor Divino
    ("RC-384", "propõe-a", "RC-378", "B041"),         # Proposta humana endereçada à rebelião
    ("RC-385", "é-um", "RC-378", "B041"),             # Egrégora = circuito dos elétrons rebeldes
    ("RC-386", "registra", "RC-161", "B041"),         # Memórias para Javé registram na memória quântica
    ("RC-387", "resulta-em", "RC-167", "B041"),       # Fragmentação do poder mental → Criação Indevida
    ("RC-381", "vincula", "RC-106", "B041"),          # Ressonância mórfica vincula os dois universos

    # ---- Relações novas (B006 - Nos Bastidores da Luz I)
    ("RC-388", "origina-em", "RC-389", "B006"),       # Grupo Atlan origina na Casa de Lucas
    ("RC-388", "fundado-por", "RC-071", "B006"),      # Grupo Atlan fundado por Ellam e amigos
    ("RC-388", "inclui", "RC-390", "B006"),           # Grupo Atlan inclui os espíritos comunicantes
    ("RC-390", "inclui", "RC-393", "B006"),           # Espíritos comunicantes incluem Enéas
    ("RC-390", "inclui", "RC-394", "B006"),           # Espíritos comunicantes incluem Mandreya
    ("RC-391", "é-um", "RC-100", "B006"),             # Mesmice Espiritual é tema espiritual
    ("RC-392", "relaciona-se-a", "RC-190", "B006"),   # Reforma Íntima ↔ Revelação Espiritual
    ("RC-388", "associado-a", "RC-028", "B006"),      # Grupo Atlan ↔ Atlan (nome/base)

    # ---- Relações novas (B050 - Guia das Eras Universais, Mapa)
    ("RC-395", "ocorre-em", "RC-103", "B050"),        # Ragnarok ocorre em Marte (Tau Ceti)
    ("RC-395", "mata", "RC-396", "B050"),             # Ragnarok mata Odin/Thor/Kvasir
    ("RC-155", "confirmada-por", "RC-094", "B050"),   # Eras da Criação confirmadas no mapa
    ("RC-397", "é-um", "RC-099", "B050"),             # Tirthankaras são humanos
    ("RC-398", "é-um", "RC-049", "B050"),             # Thuata de Dannan são demos/seres
    ("RC-401", "é-um", "RC-036", "B050"),             # Família Demolle é biodemo
    ("RC-402", "estabiliza", "RC-049", "B050"),       # Halos estabilizam demos
    ("RC-403", "associado-a", "RC-375", "B050"),      # Colegiado Druídico ↔ Druidas

    # ---- Relações novas (B027 - Nos Céus da Grécia — amostra)
    ("RC-404", "explica", "RC-003", "B027"),          # Sentido Gradualístico explica a Reintegração
    ("RC-405", "antecede", "RC-003", "B027"),         # Alvorecer de Aquário antecede a reintegração
    ("RC-406", "envolve", "RC-072", "B027"),          # Diálogos envolvem o Mestre Jesus
    ("RC-406", "envolve", "RC-226", "B027"),          # Diálogos envolvem a cidadania cósmica
    ("RC-407", "relaciona-se-a", "RC-100", "B027"),   # Grande leva de espíritos reencarnantes

    # ---- Relações novas (B051 - Diagrama Geral de Ligações)
    ("RC-408", "variação", "RC-135", "B051"),         # ADHYMAVATANA = Mavatna/Vishnu (nome completo)
    ("RC-409", "variação", "RC-102", "B051"),         # ADHYSAVNA = Savna/Shiva (nome completo)
    ("RC-410", "variação", "RC-310", "B051"),         # ADHYPRABRAJNA = Adhyshprabrajna (grafia do diagrama)
    ("RC-415", "inclui", "RC-059", "B051"),           # Colapso N1 = Espiritualidade Superior
    ("RC-415", "inclui", "RC-060", "B051"),           # Colapso N2 = Espiritualidade Operativa
    ("RC-415", "inclui", "RC-061", "B051"),           # Colapso N3 = Espiritualidade Laboratorial
    ("RC-415", "resulta-em", "RC-167", "B051"),       # Colapso → Criação Indevida
    ("RC-411", "é-um", "RC-011", "B051"),             # Gênero Adhy = Adhy (147 seres)
    ("RC-411", "inclui", "RC-455", "B051"),           # Gênero Adhy inclui a espécie Pashvnaj (correção de alvo validada em P2021-12-04)
    ("RC-412", "inclui", "RC-270", "B051"),           # Emissários Humanos incluem Abraão (patriarcas)
    ("RC-413", "é-um", "RC-102", "B051"),             # Hara é avatar de Shiva
    ("RC-414", "é-um", "RC-135", "B051"),             # Krishna é avatar (de Vishnu)
    ("RC-408", "gera", "RC-081", "B051"),             # ADHYMAVATANA → Mohen So (cadeia)
    ("RC-081", "gera", "RC-009", "B051"),             # Mohen So → Sophia (cadeia)
    ("RC-009", "gera", "RC-072", "B051"),             # Sophia → Jesus (cadeia)

    # ---- Relações novas (B034 - Cartas a Javé)
    ("RC-417", "é-um", "RC-001", "B034"),             # Resposta de Javé é fala do Criador
    ("RC-417", "responde-a", "RC-416", "B034"),       # Resposta responde às cartas
    ("RC-416", "escrita-por", "RC-420", "B034"),      # Cartas escritas por Mônica Camargo
    ("RC-418", "é-um", "RC-099", "B034"),             # Terminal Nervoso = humano
    ("RC-418", "comunica-com", "RC-041", "B034"),     # Terminal Nervoso comunica com o Criador
    ("RC-419", "é-um", "RC-001", "B034"),             # "Sou eu que vivo em vocês" = Javé
    ("RC-419", "relaciona-se-a", "RC-382", "B034"),   # "Sou eu que vivo" ↔ Vida do CFD
    ("RC-419", "relaciona-se-a", "RC-332", "B034"),   # "Sou eu que vivo" ↔ Favor Divino
    ("RC-416", "baseada-em", "RC-002", "B034"),       # Cartas baseadas nos Dramas de Javé
    ("RC-416", "baseada-em", "RC-033", "B034"),       # Cartas baseadas no Drama Terreno

    # ---- Relações novas (B036 - As Memórias de Javé)
    ("RC-421", "é-um", "RC-001", "B036"),             # Memórias são crônicas de Javé
    ("RC-421", "dita-por", "RC-001", "B036"),         # Memórias ditadas por Javé
    ("RC-421", "recebida-por", "RC-071", "B036"),     # Memórias recebidas por Ellam
    ("RC-422", "é-um", "RC-041", "B036"),             # Ser-Criador fracassado = Criador
    ("RC-422", "relaciona-se-a", "RC-245", "B036"),   # Fracasso ↔ Humanização do Criador
    ("RC-423", "é-um", "RC-071", "B036"),             # Advogado de Acusação = Ellam
    ("RC-423", "confronta", "RC-001", "B036"),        # Advogado confronta Javé
    ("RC-424", "é-um", "RC-270", "B036"),             # Linhagem dos Escolhidos = patriarcas
    ("RC-425", "variação", "RC-414", "B036"),         # Keshava = Krishna
    ("RC-426", "opõe-se-a", "RC-016", "B036"),        # Javé sem avatares × Adhyajna dos sócios
    ("RC-427", "é-um", "RC-099", "B036"),             # Criatura-teste = humano
    ("RC-428", "relaciona-se-a", "RC-300", "B036"),   # Tempo-limite ↔ Dissolução da Tríade
    ("RC-429", "alimenta-se-de", "RC-231", "B036"),   # Javé alimenta-se da razão filosófica
    ("RC-421", "precede", "RC-332", "B036"),          # Memórias conectam ao Favor Divino

    # ---- Relações novas (B040 - Homo Sapiens: da Guerra ao Esporte)
    ("RC-430", "é-um", "RC-431", "B040"),             # Esporte como evolução = transição guerreiro→atleta
    ("RC-430", "canaliza", "RC-432", "B040"),         # Esporte canaliza a agressividade
    ("RC-432", "origina-em", "RC-217", "B040"),       # Agressividade origina no DNA doentio
    # ---- Relações novas (B052 - Homoafetividade)
    ("RC-433", "surgiu-em", "RC-049", "B052"),        # Força de atração surgiu na geração do Olimpo (demos)
    ("RC-433", "antecede", "RC-099", "B052"),         # Força antecede a polaridade humana
    ("RC-434", "é-um", "RC-433", "B052"),             # Homoafetividade = resquício da força original
    ("RC-435", "relaciona-se-a", "RC-242", "B052"),   # Segredo do Éden ↔ Éden do Criador
    ("RC-436", "é-um", "RC-270", "B052"),             # Heber é patriarca da linhagem
    ("RC-437", "é-um", "RC-436", "B052"),             # Joctan/Faleg são filhos de Heber
    ("RC-438", "é-um", "RC-270", "B052"),             # Tubal é filho de Jafé (Noé)
    ("RC-439", "associado-a", "RC-068", "B052"),      # Magos do Norte ↔ Hiperbórea
    ("RC-441", "associado-a", "RC-433", "B052"),      # Mistérios Dionisíacos ↔ força de atração
    ("RC-442", "é-um", "RC-036", "B058"),             # Família Yel é um coletivo de biodemos de Capela
    ("RC-443", "é-um", "RC-036", "B058"),             # Família Mion é um coletivo de biodemos de Capela
    ("RC-444", "é-um", "RC-036", "B059"),             # Família Cromon é um coletivo de biodemos (Livro III)
    ("RC-142", "é-um", "RC-442", "B057"),             # Yel Luzbel é integrante da Família Yel
    ("RC-074", "é-um", "RC-443", "B058"),             # Len Mion pertence à Família Mion
    ("RC-442", "relaciona-se-a", "RC-443", "B058"),   # famílias Yel e Mion dialogam/confrontam
    ("RC-445", "variação", "RC-036", "B057"),         # Biocoletivos = coletivos de biodemos
    ("RC-446", "criado-por", "RC-009", "B058"),       # Sophia criou os Processadores Familiares
    ("RC-446", "associado-a", "RC-442", "B058"),      # Processador Yel une a Família Yel
    ("RC-447", "associado-a", "RC-142", "B057"),      # Yel Luzbel exercia o cargo de Primeiro Pesquisador
    ("RC-448", "relaciona-se-a", "RC-142", "B057"),   # Yel Luzbel foi o 1º a abrir lacres mentais
    ("RC-449", "relaciona-se-a", "RC-036", "B058"),   # capelinos como criaturas-ferramenta
    ("RC-450", "relaciona-se-a", "RC-002", "B058"),   # Revolta Capelina ↔ Rebelião de Lúcifer
    ("RC-450", "relaciona-se-a", "RC-142", "B057"),   # Yel Luzbel protagoniza a Revolta Capelina
    ("RC-451", "associado-a", "RC-103", "B058"),      # Universidade localizada em Tau Ceti
    ("RC-452", "associado-a", "RC-451", "B058"),      # Grão-mestre preside a Universidade
    ("RC-453", "associado-a", "RC-009", "B058"),      # Hostes bélicas a serviço de Sophia
    ("RC-454", "é-um", "RC-456", "B060"),             # Elm é um ser LM de Tempérion
    ("RC-092", "é-um", "RC-456", "B060"),             # Quarto Logos (Olm) é ser LM de Tempérion
    ("RC-454", "relaciona-se-a", "RC-071", "B060"),   # Val El (Jan Val Ellam) = avatar de Elm
    ("RC-454", "relaciona-se-a", "RC-190", "B060"),   # Kardec = avatar de Elm
    ("RC-454", "relaciona-se-a", "RC-436", "B060"),   # Heber = avatar de Elm
    ("RC-454", "relaciona-se-a", "RC-396", "B060"),   # Kvasir = avatar de Elm
    ("RC-455", "relaciona-se-a", "RC-152", "B060"),   # Prabrajna é Pashvnaj (Adhy de Perperion)
    ("RC-455", "relaciona-se-a", "RC-102", "B060"),   # Savna/Shiva é Pashvnaj
    ("RC-455", "relaciona-se-a", "RC-408", "B060"),   # Mavatina/Vishnu é Pashvnaj
    ("RC-457", "é-um", "RC-455", "B060"),             # Sarasvati é Pashvnaj
    ("RC-458", "é-um", "RC-455", "B060"),             # Lakshimi é Pashvnaj
    ("RC-459", "é-um", "RC-455", "B060"),             # Parvathi é Pashvnaj
    ("RC-457", "relaciona-se-a", "RC-037", "B060"),   # Sarasvati é consorte de Brahma
    ("RC-458", "relaciona-se-a", "RC-408", "B060"),   # Lakshimi é consorte de Vishnu
    ("RC-459", "relaciona-se-a", "RC-409", "B060"),   # Parvathi é consorte de Shiva
    ("RC-460", "é-um", "RC-024", "B060"),             # Marduk é Anunnaki
    ("RC-461", "é-um", "RC-024", "B060"),             # Ninmah é Anunnaki
    ("RC-462", "é-um", "RC-232", "B060"),             # Oannes é filho de Ostronomos (siriano)
    ("RC-463", "relaciona-se-a", "RC-024", "B060"),   # Ningishzidda (equivalência) é Anunnaki
    ("RC-464", "relaciona-se-a", "RC-398", "B060"),   # Inanna = Danu, deusa dos Tuathas de Dannan
    ("RC-301", "é-um", "RC-465", "B060"),             # Prometeu é titã/asura
    ("RC-302", "é-um", "RC-465", "B060"),             # Epimeteu é titã/asura
    ("RC-468", "sinônimo", "RC-152", "B060"),         # Ein Sof = Prabrajna (antes da queda)
    ("RC-468", "relaciona-se-a", "RC-261", "B060"),   # Ein Sof antecede Kether na Cabala
    ("RC-470", "relaciona-se-a", "RC-395", "B060"),   # Midgard = Marte + Terra (Ragnarok)
    ("RC-471", "relaciona-se-a", "RC-106", "B060"),   # Bifrost ligava os dois universos
    ("RC-469", "relaciona-se-a", "RC-061", "B060"),   # Khorsis situa-se na Espiritualidade Laboratorial
    ("RC-456", "relaciona-se-a", "RC-061", "B060"),   # Seres LM são eons da Espiritualidade Laboratorial
    ("RC-472", "parte-de", "RC-061", "B060"),         # Tempérion é setor da Espiritualidade Laboratorial
    ("RC-473", "parte-de", "RC-061", "B060"),         # Lempérion/Terpérion são setores da Espiritualidade Laboratorial
    ("RC-472", "relaciona-se-a", "RC-087", "B060"),   # Tempérion é vizinho/paralelo a Perpérion
    ("RC-087", "relaciona-se-a", "RC-152", "B060"),   # Perpérion é o domínio de Prabrajna (Prajapati)
    ("RC-454", "ocorre-em", "RC-472", "B060"),        # Elm é ser LM de Tempérion
    ("RC-456", "ocorre-em", "RC-472", "B060"),        # Seres LM habitam Tempérion
    ("RC-092", "ocorre-em", "RC-472", "B060"),        # Olm (4º Logos) também é LM de Tempérion
    ("RC-474", "sinônimo", "RC-004", "B061"),         # Elohim = Conselho dos deuses = Arcontes
    ("RC-474", "relaciona-se-a", "RC-009", "B061"),   # Arcontes = sinônimo de Sophias
    ("RC-475", "relaciona-se-a", "RC-286", "B061"),   # Kama/Eros surgiu depois de Aurora
    ("RC-476", "relaciona-se-a", "RC-001", "B061"),   # Emá produziu Brahma/Javé (e Vishnu, Jesus, Sophia)
    ("RC-482", "sinônimo", "RC-001", "B061"),         # Ialdabaoth = Javé (gnóstico)
    ("RC-488", "variação", "RC-024", "B061"),         # Nefilins = Anunnakis
    ("RC-486", "é-um", "RC-024", "B061"),             # Enki é Anunnaki
    ("RC-487", "é-um", "RC-024", "B061"),             # Enlil é Anunnaki
    ("RC-503", "variação", "RC-408", "B061"),         # Mavátma/Mavatna = grafias de ADHYMAVATANA
    ("RC-504", "variação", "RC-408", "B061"),         # Adyadvaivatma = Vishnu
    ("RC-505", "variação", "RC-152", "B061"),         # Adyabradagna = Prabrajna/Brahma
    ("RC-478", "associado-a", "RC-001", "B061"),      # Chequinhá é veículo de Javé
    ("RC-495", "associado-a", "RC-001", "B061"),      # Arabot-Ráquia é ambiente de Javé
    ("RC-501", "associado-a", "RC-065", "B061"),      # Conselho dos Cinco comanda a Frota Norte
    ("RC-502", "é-um", "RC-109", "B061"),             # Val Aten é da Família Val
    ("RC-491", "é-um", "RC-036", "B061"),             # Família Shanlung é de biodemos
    ("RC-498", "relaciona-se-a", "RC-472", "B061"),   # Tempérium (Archeons de Eeron) ~ Tempérion
    ("RC-496", "relaciona-se-a", "RC-061", "B061"),   # Eeron é região da Espiritualidade Laboratorial
    ("RC-507", "relaciona-se-a", "RC-474", "B071"),   # Holodomínio = esfera de influência de hierarquias (Arcontes)
    ("RC-508", "relaciona-se-a", "RC-253", "B071"),   # Decência cósmica conecta-se à Liberdade Mental
    ("RC-509", "relaciona-se-a", "RC-253", "B071"),   # Protagonismo consciencial conecta-se à Liberdade Mental
    ("RC-510", "variação", "RC-070", "B071"),         # Blindagem cósmica ~ Isolamento Cósmico
    ("RC-510", "variação", "RC-342", "B071"),         # Blindagem cósmica ~ Quarentena
    ("RC-511", "relaciona-se-a", "RC-106", "B071"),   # Mêntion relaciona-se ao universo antimaterial
    ("RC-512", "relaciona-se-a", "RC-407", "B071"),   # Amnésia espiritual ~ ciclo reencarnatório
    ("RC-513", "relaciona-se-a", "RC-061", "B071"),   # Errática é a faixa abaixo da Laboratorial
    ("RC-513", "relaciona-se-a", "RC-106", "B071"),   # Errática envolve os 2 universos de Prabrajna
    ("RC-514", "relaciona-se-a", "RC-003", "B071"),   # Tikun Cósmico ~ Reintegração Cósmica
    ("RC-515", "variação", "RC-167", "B071"),         # Acidente cosmogônico ~ Criação Indevida
    ("RC-516", "relaciona-se-a", "RC-488", "B071"),   # Hibridização genética ~ Nefilins
    ("RC-516", "relaciona-se-a", "RC-323", "B071"),   # Hibridização genética ~ entroncamentos
    ("RC-517", "relaciona-se-a", "RC-511", "B072"),   # Protocolo Mental ~ Mêntion
    ("RC-518", "relaciona-se-a", "RC-217", "B072"),   # Genoma Derivado ~ DNA holográfico
    ("RC-519", "relaciona-se-a", "RC-518", "B072"),   # Herança Cósmica deriva do Genoma Derivado
    ("RC-520", "relaciona-se-a", "RC-448", "B072"),   # Infecção mental ~ deslacre
    ("RC-521", "relaciona-se-a", "RC-161", "B072"),   # Arquivos da Memória Cósmica ~ memória quântica
    ("RC-522", "relaciona-se-a", "RC-523", "B072"),   # Parasitismo precede o vampirismo
    ("RC-523", "é-um", "RC-522", "B072"),             # Vampirismo é forma intensa de parasitismo
    ("RC-524", "relaciona-se-a", "RC-148", "B072"),   # Coleta de informações ~ Agentes da Vida
    ("RC-525", "relaciona-se-a", "RC-400", "B072"),   # Semente da racionalidade ~ FOXP2
    ("RC-526", "relaciona-se-a", "RC-167", "B072"),   # Demência do Criador ~ Criação Indevida
    ("RC-527", "variação", "RC-106", "B072"),         # Antimundo ~ Universo Antimaterial
    ("RC-528", "variação", "RC-167", "B072"),         # Mergulho ~ Criação Indevida/queda
    ("RC-529", "relaciona-se-a", "RC-381", "B072"),   # Ressonância límbica ~ ressonância mórfica
    ("RC-530", "relaciona-se-a", "RC-009", "B072"),   # Pistis Sophia ~ Sophia
    ("RC-530", "relaciona-se-a", "RC-483", "B072"),   # Pistis Sophia ~ Barbelo (gnosticismo)
    ("RC-531", "relaciona-se-a", "RC-323", "B073"),   # Laboratório Genético Terra ~ entroncamentos
    ("RC-532", "relaciona-se-a", "RC-072", "B073"),   # Vacina do Amor ancorada por Jesus
    ("RC-532", "relaciona-se-a", "RC-040", "B073"),   # Vacina do Amor atua no CFD
    ("RC-533", "relaciona-se-a", "RC-454", "B073"),   # Supercomputador Cósmico = Moros/Elm
    ("RC-534", "relaciona-se-a", "RC-463", "B073"),   # Usinas de Gizé ~ Hermes Trismegisto/Thoth
    ("RC-535", "relaciona-se-a", "RC-085", "B042"),   # Projeto Orbum deriva do planeta Orbum
    ("RC-535", "relaciona-se-a", "RC-226", "B042"),   # Projeto Orbum promove a cidadania cósmica
    ("RC-535", "relaciona-se-a", "RC-094", "B042"),   # Projeto Orbum difunde a Revelação Cósmica
    ("RC-536", "relaciona-se-a", "RC-094", "B042"),   # Era do Conhecimento ~ Revelação Cósmica
    ("RC-536", "relaciona-se-a", "RC-003", "B042"),   # Era do Conhecimento ~ Reintegração Cósmica
    ("RC-537", "relaciona-se-a", "RC-344", "B042"),   # Maré Cósmica ~ Transição Planetária
    ("RC-538", "relaciona-se-a", "RC-042", "B019"),   # Consórcio busca a Criatura Universal
    ("RC-538", "relaciona-se-a", "RC-207", "B019"),   # Consórcio integra Arquitetos Universais
    ("RC-539", "é-um", "RC-538", "B019"),             # Arquitetos Universais são o Consórcio de Mundos
    ("RC-540", "relaciona-se-a", "RC-217", "B019"),   # Molécula-mãe ~ DNA/projeção holográfica
    ("RC-541", "relaciona-se-a", "RC-094", "B019"),   # Evolução Possível ~ Revelação Cósmica
    ("RC-541", "relaciona-se-a", "RC-042", "B019"),   # Evolução Possível ~ Criatura Universal
    ("RC-542", "relaciona-se-a", "RC-217", "B019"),   # Ex-DNA-lixo ~ DNA holográfico
    ("RC-543", "relaciona-se-a", "RC-217", "B019"),   # Espelho do Epigenoma ~ DNA
    ("RC-544", "relaciona-se-a", "RC-099", "B019"),   # Novo Homo sapiens ~ Homo sapiens atual
    ("RC-544", "relaciona-se-a", "RC-042", "B019"),   # Novo Homo sapiens ~ protótipo da Criatura Universal
    ("RC-545", "relaciona-se-a", "RC-514", "B019"),   # Coconstrutores ~ Tikun
    ("RC-546", "relaciona-se-a", "RC-541", "B019"),   # Primado da Consciência ~ Evolução Possível
    ("RC-547", "relaciona-se-a", "RC-546", "B019"),   # Evolução Criativa ~ Primado da Consciência
    ("RC-548", "é-um", "RC-166", "B074"),             # Arquivos Mentais são base do Mentalma
    ("RC-549", "relaciona-se-a", "RC-548", "B074"),   # Circuito do CHA define os arquivos colecionados
    ("RC-549", "relaciona-se-a", "RC-550", "B074"),   # CHA x vontade de progredir (chave)
    ("RC-550", "relaciona-se-a", "RC-548", "B074"),   # Vontade de progredir acessa os arquivos
    ("RC-551", "relaciona-se-a", "RC-166", "B075"),   # Dehatma buddhi é doença do psiquismo
    ("RC-552", "relaciona-se-a", "RC-166", "B074"),   # 3As são prática do Mentalma
    ("RC-553", "relaciona-se-a", "RC-166", "B074"),   # Eu Profundo é nível do Mentalma
    ("RC-554", "é-um", "RC-166", "B075"),             # Mentalma II aprofunda o Mentalma I
    ("RC-555", "relaciona-se-a", "RC-166", "B074"),   # Série = os livros do Mentalma
    ("RC-556", "variação", "RC-001", "P2024-02-25"),  # Senhor Parameshthi = face atual de Javé
    ("RC-556", "variação", "RC-037", "P2024-02-25"),  # Senhor Parameshthi = Brahma (fase atual)
    ("RC-557", "relaciona-se-a", "RC-558", "P2024-02-25"),  # Conectoma produz a sensação de eu
    ("RC-557", "relaciona-se-a", "RC-166", "P2024-02-25"),  # Conectoma liga-se ao Mentalma
    ("RC-558", "relaciona-se-a", "RC-553", "P2024-02-25"),  # Sensação de eu ~ Eu Profundo
    ("RC-559", "relaciona-se-a", "RC-658", "P2024-02-25"),  # Teia quântica é operada pelo WD
    ("RC-559", "relaciona-se-a", "RC-467", "P2024-02-25"),  # Teia quântica ~ Moiras/destino
    ("RC-658", "relaciona-se-a", "RC-217", "P2024-02-25"),  # WD organiza a genética (DNA)
    ("RC-561", "relaciona-se-a", "RC-001", "P2024-02-25"),  # Faces de Javé = manifestações do Criador
    ("RC-562", "relaciona-se-a", "RC-217", "P2024-02-25"),  # Baralho genético ~ DNA/genoma
    ("RC-563", "relaciona-se-a", "RC-449", "P2024-02-25"),  # Travas e lacres ~ criaturas-ferramenta
    ("RC-564", "relaciona-se-a", "RC-099", "P2024-02-25"),  # Fios soltos ~ condição humana
    ("RC-565", "variação", "RC-135", "B060"),             # Hochmah (2ª Sefirah) = equivalente de Vishnu
    ("RC-565", "variação", "RC-009", "B060"),             # Hochmah = Sophia (epíteto hebraico = Sabedoria)
    ("RC-565", "relaciona-se-a", "RC-009", "B060"),       # Hochmah = Sabedoria = Sophia (hebraico)
    ("RC-565", "relaciona-se-a", "RC-261", "B060"),       # Hochmah é 2ª Sefirah, após Kether
    ("RC-565", "é-um", "RC-263", "B060"),                 # Hochmah é uma Sefirah da Árvore da Vida
    # ---- Relações da palestra P2022-12-17 — pré-curadoria aprovada
    ("RC-566", "relaciona-se-a", "RC-253", "P2022-12-17"),
    ("RC-566", "relaciona-se-a", "RC-226", "P2022-12-17"),
    ("RC-566", "relaciona-se-a", "RC-231", "P2022-12-17"),
    ("RC-567", "divide-se-em", "RC-568", "P2022-12-17"),
    ("RC-567", "divide-se-em", "RC-569", "P2022-12-17"),
    ("RC-568", "parte-de", "RC-567", "P2022-12-17"),
    ("RC-569", "parte-de", "RC-567", "P2022-12-17"),
    ("RC-570", "usa", "RC-568", "P2022-12-17"),
    ("RC-570", "usa", "RC-569", "P2022-12-17"),
    ("RC-570", "relaciona-se-a", "RC-225", "P2022-12-17"),
    ("RC-571", "marca-fim-de", "RC-567", "P2022-12-17"),
    ("RC-571", "marca-fim-de", "RC-592", "P2022-12-17"),
    ("RC-571", "antecede", "RC-003", "P2022-12-17"),
    ("RC-571", "relaciona-se-a", "RC-405", "P2022-12-17"),
    ("RC-572", "explica", "RC-571", "P2022-12-17"),
    ("RC-572", "distingue-se-de", "RC-578", "P2022-12-17"),
    ("RC-573", "associado-a", "RC-574", "P2022-12-17"),
    ("RC-573", "relaciona-se-a", "RC-571", "P2022-12-17"),
    ("RC-573", "relaciona-se-a", "RC-537", "P2022-12-17"),
    ("RC-575", "envolve", "RC-104", "P2022-12-17"),
    ("RC-575", "envolve", "RC-078", "P2022-12-17"),
    ("RC-575", "relaciona-se-a", "RC-106", "P2022-12-17"),
    ("RC-576", "associado-a", "RC-571", "P2022-12-17"),
    ("RC-576", "relaciona-se-a", "RC-572", "P2022-12-17"),
    ("RC-577", "relaciona-se-a", "RC-563", "P2022-12-17"),
    ("RC-577", "relaciona-se-a", "RC-448", "P2022-12-17"),
    ("RC-577", "relaciona-se-a", "RC-400", "P2022-12-17"),
    ("RC-578", "ameaça", "RC-099", "P2022-12-17"),
    ("RC-578", "relaciona-se-a", "RC-337", "P2022-12-17"),
    ("RC-578", "relaciona-se-a", "RC-544", "P2022-12-17"),
    ("RC-579", "associado-a", "RC-474", "P2022-12-17"),
    ("RC-579", "parte-de", "RC-594", "P2022-12-17"),
    ("RC-580", "é-um", "RC-024", "P2022-12-17"),
    ("RC-580", "envolve", "RC-516", "P2022-12-17"),
    ("RC-580", "relaciona-se-a", "RC-488", "P2022-12-17"),
    ("RC-581", "relaciona-se-a", "RC-523", "P2022-12-17"),
    ("RC-581", "inclui", "RC-582", "P2022-12-17"),
    ("RC-582", "é-um", "RC-581", "P2022-12-17"),
    ("RC-582", "opõe-se-a", "RC-584", "P2022-12-17"),
    ("RC-583", "envolve", "RC-486", "P2022-12-17"),
    ("RC-583", "envolve", "RC-487", "P2022-12-17"),
    ("RC-583", "envolve", "RC-460", "P2022-12-17"),
    ("RC-583", "envolve", "RC-587", "P2022-12-17"),
    ("RC-583", "envolve", "RC-588", "P2022-12-17"),
    ("RC-583", "origem-em", "RC-589", "P2022-12-17"),
    ("RC-584", "é-um", "RC-135", "P2022-12-17"),
    ("RC-584", "opõe-se-a", "RC-582", "P2022-12-17"),
    ("RC-585", "encarnação-posterior-de", "RC-436", "P2022-12-17"),
    ("RC-585", "relaciona-se-a", "RC-593", "P2022-12-17"),
    ("RC-586", "relaciona-se-a", "RC-585", "P2022-12-17"),
    ("RC-586", "relaciona-se-a", "RC-593", "P2022-12-17"),
    ("RC-587", "é-um", "RC-024", "P2022-12-17"),
    ("RC-587", "pai-de", "RC-486", "P2022-12-17"),
    ("RC-587", "pai-de", "RC-487", "P2022-12-17"),
    ("RC-588", "é-um", "RC-024", "P2022-12-17"),
    ("RC-588", "envolve", "RC-583", "P2022-12-17"),
    ("RC-589", "associado-a", "RC-024", "P2022-12-17"),
    ("RC-589", "origem-de", "RC-583", "P2022-12-17"),
    ("RC-590", "tema-de", "RC-595", "P2022-12-17"),
    ("RC-590", "relaciona-se-a", "RC-568", "P2022-12-17"),
    ("RC-591", "relaciona-se-a", "RC-571", "P2022-12-17"),
    ("RC-591", "relaciona-se-a", "RC-536", "P2022-12-17"),
    ("RC-592", "é-um", "RC-569", "P2022-12-17"),
    ("RC-592", "envolve", "RC-072", "P2022-12-17"),
    ("RC-592", "sucede-por", "RC-405", "P2022-12-17"),
    ("RC-593", "associado-a", "RC-585", "P2022-12-17"),
    ("RC-593", "envolve", "RC-586", "P2022-12-17"),
    ("RC-593", "envolve", "RC-104", "P2022-12-17"),
    ("RC-594", "relaciona-se-a", "RC-424", "P2022-12-17"),
    ("RC-594", "inclui", "RC-579", "P2022-12-17"),
    ("RC-594", "relaciona-se-a", "RC-489", "P2022-12-17"),
    ("RC-595", "inclui", "RC-590", "P2022-12-17"),
    ("RC-595", "relaciona-se-a", "RC-568", "P2022-12-17"),

    # ---- Novas relações entre termos existentes, explicitadas em P2022-12-17
    ("RC-106", "variação", "RC-108", "P2022-12-17"),  # universo vizinho ~ universo paralelo/antimaterial
    ("RC-009", "assume-regência", "RC-003", "P2022-12-17"),
    ("RC-040", "inserido-em", "RC-424", "P2022-12-17"),
    ("RC-102", "associado-a", "RC-329", "P2022-12-17"),
    ("RC-145", "variação", "RC-480", "P2022-12-17"),
    ("RC-395", "relaciona-se-a", "RC-471", "P2022-12-17"),
    ("RC-514", "atua-em", "RC-217", "P2022-12-17"),
    ("RC-564", "relaciona-se-a", "RC-514", "P2022-12-17"),
    ("RC-166", "orienta", "RC-566", "P2022-12-17"),

    # ---- Correções estruturais C-01 a C-07 — P2021-12-04
    ("RC-496", "parte-de", "RC-061", "P2021-12-04"),      # Ereon é região da Espiritualidade Laboratorial
    ("RC-496", "inclui", "RC-087", "P2021-12-04"),        # Perpérion é um dos cinco Archeons
    ("RC-496", "inclui", "RC-472", "P2021-12-04"),        # Tempérion é um dos cinco Archeons
    ("RC-087", "parte-de", "RC-496", "P2021-12-04"),      # Perpérion pertence a Ereon
    ("RC-472", "parte-de", "RC-496", "P2021-12-04"),      # Tempérion pertence a Ereon
    ("RC-497", "erro-stt-de", "RC-087", "P2021-12-04"),   # Impérial = leitura histórica defeituosa de Perpérion
    ("RC-498", "variação", "RC-472", "P2021-12-04"),      # Tempérium = variação histórica de Tempérion
    ("RC-411", "inclui", "RC-455", "P2021-12-04"),        # Gênero Adhy inclui Pashvnaj
    ("RC-455", "é-uma-espécie-de", "RC-411", "P2021-12-04"), # Pashvnaj: 43 dos 147 Adhy
    ("RC-456", "ocorre-em", "RC-472", "P2021-12-04"),     # Seres LM são de Tempérion
    ("RC-456", "enviado-a", "RC-087", "P2021-12-04"),     # grupo de cinco LM foi observar Perpérion
    ("RC-454", "é-um", "RC-456", "P2021-12-04"),          # Elm é LM
    ("RC-092", "é-um", "RC-456", "P2021-12-04"),          # Olm é LM
    ("RC-472", "abriga", "RC-456", "P2021-12-04"),        # Tempérion é setor dos LM

    # ---- Relações do Quadro 9 — P2021-12-04
    ("RC-596", "parte-de", "RC-061", "P2021-12-04"),
    ("RC-596", "corresponde-a", "RC-496", "P2021-12-04"),
    ("RC-596", "inclui", "RC-597", "P2021-12-04"),
    ("RC-596", "inclui", "RC-598", "P2021-12-04"),
    ("RC-596", "inclui", "RC-599", "P2021-12-04"),
    ("RC-596", "inclui", "RC-087", "P2021-12-04"),
    ("RC-596", "inclui", "RC-472", "P2021-12-04"),
    ("RC-597", "é-um", "RC-596", "P2021-12-04"),
    ("RC-598", "é-um", "RC-596", "P2021-12-04"),
    ("RC-599", "é-um", "RC-596", "P2021-12-04"),
    ("RC-598", "desenvolve", "RC-597", "P2021-12-04"),
    ("RC-600", "ocorre-em", "RC-204", "P2021-12-04"),
    ("RC-600", "cria", "RC-060", "P2021-12-04"),
    ("RC-600", "participa-de", "RC-603", "P2021-12-04"),
    ("RC-601", "envolve", "RC-059", "P2021-12-04"),
    ("RC-601", "envolve", "RC-060", "P2021-12-04"),
    ("RC-601", "envolve", "RC-061", "P2021-12-04"),
    ("RC-601", "produz", "RC-602", "P2021-12-04"),
    ("RC-602", "parte-de", "RC-601", "P2021-12-04"),
    ("RC-602", "distingue-se-de", "RC-510", "P2021-12-04"),
    ("RC-602", "relaciona-se-a", "RC-415", "P2021-12-04"),
    ("RC-603", "envolve", "RC-600", "P2021-12-04"),
    ("RC-603", "produz", "RC-149", "P2021-12-04"),
    ("RC-603", "relaciona-se-a", "RC-188", "P2021-12-04"),
    ("RC-604", "envolve", "RC-408", "P2021-12-04"),
    ("RC-604", "envolve", "RC-410", "P2021-12-04"),
    ("RC-604", "envolve", "RC-009", "P2021-12-04"),
    ("RC-604", "envolve", "RC-072", "P2021-12-04"),
    ("RC-604", "envolve", "RC-454", "P2021-12-04"),
    ("RC-604", "envolve", "RC-092", "P2021-12-04"),
    ("RC-605", "aplica-se-a", "RC-600", "P2021-12-04"),
    ("RC-605", "aplica-se-a", "RC-411", "P2021-12-04"),
    ("RC-605", "aplica-se-a", "RC-456", "P2021-12-04"),
    ("RC-606", "rege", "RC-600", "P2021-12-04"),
    ("RC-606", "opõe-se-a", "RC-253", "P2021-12-04"),
    ("RC-606", "precede", "RC-060", "P2021-12-04"),
    ("RC-607", "é-um", "RC-456", "P2021-12-04"),
    ("RC-607", "origem-em", "RC-472", "P2021-12-04"),
    ("RC-607", "enviado-a", "RC-087", "P2021-12-04"),
    ("RC-607", "inclui", "RC-454", "P2021-12-04"),
    ("RC-607", "inclui", "RC-092", "P2021-12-04"),
    ("RC-608", "estudado-por", "RC-456", "P2021-12-04"),
    ("RC-608", "orienta", "RC-612", "P2021-12-04"),
    ("RC-609", "inclui", "RC-104", "P2021-12-04"),
    ("RC-609", "inclui", "RC-610", "P2021-12-04"),
    ("RC-609", "inclui", "RC-454", "P2021-12-04"),
    ("RC-609", "inclui", "RC-092", "P2021-12-04"),
    ("RC-610", "inclui", "RC-457", "P2021-12-04"),
    ("RC-610", "inclui", "RC-458", "P2021-12-04"),
    ("RC-610", "inclui", "RC-459", "P2021-12-04"),
    ("RC-610", "relaciona-se-a", "RC-104", "P2021-12-04"),
    ("RC-611", "proferida-por", "RC-454", "P2021-12-04"),
    ("RC-611", "envolve", "RC-092", "P2021-12-04"),
    ("RC-611", "relaciona-se-a", "RC-094", "P2021-12-04"),
    ("RC-612", "relaciona-se-a", "RC-003", "P2021-12-04"),
    ("RC-612", "envolve", "RC-092", "P2021-12-04"),
    ("RC-612", "envolve", "RC-009", "P2021-12-04"),
    ("RC-612", "relaciona-se-a", "RC-454", "P2021-12-04"),
    ("RC-613", "atravessa", "RC-602", "P2021-12-04"),
    ("RC-613", "comunica-com", "RC-600", "P2021-12-04"),
    ("RC-613", "relaciona-se-a", "RC-612", "P2021-12-04"),
    ("RC-614", "produz", "RC-615", "P2021-12-04"),
    ("RC-614", "relaciona-se-a", "RC-544", "P2021-12-04"),
    ("RC-615", "resulta-de", "RC-614", "P2021-12-04"),
    ("RC-615", "envolve", "RC-092", "P2021-12-04"),
    ("RC-615", "envolve", "RC-009", "P2021-12-04"),
    ("RC-615", "relaciona-se-a", "RC-003", "P2021-12-04"),
    ("RC-616", "tema-de", "RC-617", "P2021-12-04"),
    ("RC-616", "relaciona-se-a", "RC-612", "P2021-12-04"),
    ("RC-617", "tema-de", "RC-612", "P2021-12-04"),
    ("RC-617", "anunciada-por", "RC-071", "P2021-12-04"),
    ("RC-618", "relaciona-se-a", "RC-166", "P2021-12-04"),
    ("RC-618", "relaciona-se-a", "RC-253", "P2021-12-04"),
    ("RC-618", "relaciona-se-a", "RC-514", "P2021-12-04"),
    ("RC-619", "relaciona-se-a", "RC-217", "P2021-12-04"),
    ("RC-619", "relaciona-se-a", "RC-400", "P2021-12-04"),
    ("RC-619", "relaciona-se-a", "RC-253", "P2021-12-04"),
    ("RC-619", "relaciona-se-a", "RC-614", "P2021-12-04"),

    # ---- Fusões aprovadas no Quadro 9
    ("RC-204", "variação", "RC-600", "P2021-12-04"),   # Paraíso Original contém os Seres Originais
    ("RC-188", "relaciona-se-a", "RC-603", "P2021-12-04"),
    ("RC-188", "distingue-se-de", "RC-176", "P2021-12-04"), # rede coletiva natural ≠ controle colmeia

    # ---- Relações da Devolutiva-01 — P2026-07-30
    ("RC-475", "relaciona-se-a", "RC-385", "P2026-07-30"),       # externalização da egrégora de cólera
    ("RC-475", "gera", "RC-610", "P2026-07-30"),                # Grande Deusa gera a Tridevi
    ("RC-475", "sucede", "RC-621", "P2026-07-30"),              # Nyx pertence a geração anterior
    ("RC-476", "ancora", "RC-001", "P2026-07-30"),
    ("RC-476", "ancora", "RC-009", "P2026-07-30"),
    ("RC-476", "ancora", "RC-072", "P2026-07-30"),
    ("RC-476", "ancora", "RC-135", "P2026-07-30"),
    ("RC-620", "aplica-se-a", "RC-476", "P2026-07-30"),
    ("RC-620", "relaciona-se-a", "RC-553", "P2026-07-30"),
    ("RC-620", "relaciona-se-a", "RC-557", "P2026-07-30"),
    ("RC-620", "relaciona-se-a", "RC-558", "P2026-07-30"),
    ("RC-620", "integra", "RC-604", "P2026-07-30"),
    ("RC-621", "precede", "RC-475", "P2026-07-30"),
    ("RC-621", "gera", "RC-454", "P2026-07-30"),
    ("RC-622", "criado-por", "RC-135", "P2026-07-30"),
    ("RC-622", "relaciona-se-a", "RC-475", "P2026-07-30"),
    ("RC-623", "investido-por", "RC-624", "P2026-07-30"),
    ("RC-624", "investe", "RC-623", "P2026-07-30"),
    ("RC-624", "investido-por", "RC-625", "P2026-07-30"),
    ("RC-625", "investe", "RC-624", "P2026-07-30"),
    ("RC-625", "relaciona-se-a", "RC-511", "P2026-07-30"),
    ("RC-626", "relaciona-se-a", "RC-609", "P2026-07-30"),
    ("RC-627", "compara-se-a", "RC-609", "P2026-07-30"),

    # ---- Correção curatorial: origem e trajetória de Elm/Olm
    ("RC-454", "origem-em", "RC-472", "P2021-12-04"),      # Elm é originário de Tempérion
    ("RC-092", "origem-em", "RC-472", "P2021-12-04"),      # Olm é originário de Tempérion
    ("RC-454", "enviado-a", "RC-087", "P2021-12-04"),      # Elm foi a Perpérion observar o problema
    ("RC-092", "enviado-a", "RC-087", "P2021-12-04"),      # Olm foi a Perpérion observar o problema
    ("RC-454", "observa", "RC-608", "P2021-12-04"),        # Elm estuda a imponderabilidade
    ("RC-092", "observa", "RC-608", "P2021-12-04"),        # Olm estuda a imponderabilidade
    ("RC-454", "mergulha-em", "RC-167", "P2021-12-04"),    # Elm interage e mergulha no processo
    ("RC-092", "mergulha-em", "RC-167", "P2021-12-04"),    # Olm interage e mergulha no processo
    ("RC-087", "abriga", "RC-411", "P2021-12-04"),        # Perpérion abriga o Gênero Adhy
    ("RC-087", "abriga", "RC-455", "P2021-12-04"),        # Perpérion abriga a espécie Pashvnaj
    ("RC-087", "abriga", "RC-152", "P2021-12-04"),        # Prabrajna pertence à família Adhy de Perpérion
    ("RC-167", "inicia-em", "RC-087", "P2021-12-04"),     # a Criação Indevida começa em Perpérion

    # ---- Relações P2024-05-04
    ("RC-628", "vincula", "RC-152", "P2024-05-04"),
    ("RC-628", "vincula", "RC-167", "P2024-05-04"),
    ("RC-628", "repercute-em", "RC-476", "P2024-05-04"),
    ("RC-628", "relaciona-se-a", "RC-559", "P2024-05-04"),
    ("RC-628", "relaciona-se-a", "RC-658", "P2024-05-04"),
    ("RC-628", "envolve", "RC-217", "P2024-05-04"),
    ("RC-629", "envolve", "RC-455", "P2024-05-04"),
    ("RC-629", "envolve", "RC-152", "P2024-05-04"),
    ("RC-629", "resulta-em", "RC-167", "P2024-05-04"),
    ("RC-630", "relaciona-se-a", "RC-014", "P2024-05-04"),
    ("RC-630", "ocorre-em", "RC-106", "P2024-05-04"),
    ("RC-631", "é-um", "RC-093", "P2024-05-04"),
    ("RC-631", "distingue-se-de", "RC-035", "P2024-05-04"),
    ("RC-631", "associado-a", "RC-009", "P2024-05-04"),
    ("RC-632", "destinado-a", "RC-009", "P2024-05-04"),
    ("RC-632", "relaciona-se-a", "RC-217", "P2024-05-04"),
    ("RC-632", "relaciona-se-a", "RC-543", "P2024-05-04"),
    ("RC-633", "relaciona-se-a", "RC-166", "P2024-05-04"),
    ("RC-633", "usa", "RC-552", "P2024-05-04"),
    ("RC-633", "relaciona-se-a", "RC-619", "P2024-05-04"),
    ("RC-634", "relaciona-se-a", "RC-160", "P2024-05-04"),
    ("RC-634", "relaciona-se-a", "RC-272", "P2024-05-04"),
    ("RC-635", "ocorre-em", "RC-061", "P2024-05-04"),
    ("RC-635", "envolve", "RC-411", "P2024-05-04"),
    ("RC-635", "envolve", "RC-456", "P2024-05-04"),
    ("RC-636", "envolve", "RC-161", "P2024-05-04"),
    ("RC-636", "envolve", "RC-162", "P2024-05-04"),
    ("RC-636", "ocorre-em", "RC-106", "P2024-05-04"),
    ("RC-636", "ocorre-em", "RC-107", "P2024-05-04"),
    ("RC-637", "transfere-para", "RC-161", "P2024-05-04"),
    ("RC-637", "origem-em", "RC-106", "P2024-05-04"),
    ("RC-638", "reconstrói", "RC-152", "P2024-05-04"),
    ("RC-638", "envolve", "RC-387", "P2024-05-04"),
    ("RC-638", "envolve", "RC-161", "P2024-05-04"),
    ("RC-638", "relaciona-se-a", "RC-514", "P2024-05-04"),
    ("RC-639", "ocorre-em", "RC-106", "P2024-05-04"),
    ("RC-639", "é-fase-de", "RC-638", "P2024-05-04"),
    ("RC-640", "inclui", "RC-639", "P2024-05-04"),
    ("RC-640", "inclui", "RC-641", "P2024-05-04"),
    ("RC-641", "é-fase-de", "RC-638", "P2024-05-04"),
    ("RC-641", "tema-de", "RC-526", "P2024-05-04"),
    ("RC-642", "é-um", "RC-135", "P2024-05-04"),
    ("RC-642", "confronta", "RC-102", "P2024-05-04"),
    # Fusões aprovadas
    ("RC-210", "relaciona-se-a", "RC-628", "P2024-05-04"),
    ("RC-623", "relaciona-se-a", "RC-604", "P2024-05-04"),
    ("RC-635", "relaciona-se-a", "RC-612", "P2024-05-04"),

    # ---- Relações P2026-04-02
    ("RC-081", "variação", "RC-282", "P2026-04-02"),
    ("RC-081", "vinculado-ao-espírito", "RC-454", "P2026-04-02"),
    ("RC-081", "é-um", "RC-135", "P2026-04-02"),
    ("RC-081", "é-um", "RC-073", "P2026-04-02"),
    ("RC-643", "relaciona-se-a", "RC-217", "P2026-04-02"),
    ("RC-643", "relaciona-se-a", "RC-619", "P2026-04-02"),
    ("RC-643", "relaciona-se-a", "RC-514", "P2026-04-02"),
    ("RC-644", "deriva-de", "RC-577", "P2026-04-02"),
    ("RC-644", "busca", "RC-643", "P2026-04-02"),
    ("RC-645", "relaciona-se-a", "RC-042", "P2026-04-02"),
    ("RC-645", "relaciona-se-a", "RC-544", "P2026-04-02"),
    ("RC-645", "usa", "RC-646", "P2026-04-02"),
    ("RC-646", "relaciona-se-a", "RC-217", "P2026-04-02"),
    ("RC-646", "relaciona-se-a", "RC-619", "P2026-04-02"),
    ("RC-647", "tema-de", "RC-365", "P2026-04-02"),
    ("RC-647", "envolve", "RC-138", "P2026-04-02"),
    ("RC-647", "relaciona-se-a", "RC-483", "P2026-04-02"),
    ("RC-647", "relaciona-se-a", "RC-268", "P2026-04-02"),
    ("RC-365", "reabilita", "RC-138", "P2026-04-02"),

    # ---- Relações P2025-10-25
    ("RC-648", "envolve", "RC-476", "P2025-10-25"),
    ("RC-648", "envolve", "RC-604", "P2025-10-25"),
    ("RC-649", "envolve", "RC-081", "P2025-10-25"),
    ("RC-649", "envolve", "RC-104", "P2025-10-25"),
    ("RC-649", "vinculado-ao-espírito", "RC-454", "P2025-10-25"),
    ("RC-650", "relaciona-se-a", "RC-001", "P2025-10-25"),
    ("RC-650", "relaciona-se-a", "RC-424", "P2025-10-25"),
    ("RC-651", "aplica-se-a", "RC-019", "P2025-10-25"),
    ("RC-651", "envolve", "RC-147", "P2025-10-25"),
    ("RC-652", "proferida-por", "RC-001", "P2025-10-25"),
    ("RC-652", "destinada-a", "RC-019", "P2025-10-25"),
    ("RC-652", "envolve", "RC-147", "P2025-10-25"),
    ("RC-653", "envolve", "RC-149", "P2025-10-25"),
    ("RC-653", "sucede", "RC-514", "P2025-10-25"),
    ("RC-654", "é-um", "RC-099", "P2025-10-25"),
    ("RC-654", "relaciona-se-a", "RC-148", "P2025-10-25"),
    ("RC-655", "relaciona-se-a", "RC-397", "P2025-10-25"),
    ("RC-655", "relaciona-se-a", "RC-514", "P2025-10-25"),
    ("RC-656", "atualiza", "RC-094", "P2025-10-25"),
    ("RC-656", "relaciona-se-a", "RC-190", "P2025-10-25"),
    ("RC-657", "relaciona-se-a", "RC-655", "P2025-10-25"),
    ("RC-657", "relaciona-se-a", "RC-566", "P2025-10-25"),
    # ampliações
    ("RC-145", "variação", "RC-480", "P2025-10-25"),
    ("RC-092", "tutoria", "RC-009", "P2025-10-25"),
    ("RC-147", "humaniza-se-por", "RC-099", "P2025-10-25"),

    # ---- Relações P2025-06-26
    ("RC-658", "relaciona-se-a", "RC-467", "P2025-06-26"),
    ("RC-658", "organizada-por", "RC-454", "P2025-06-26"),
    ("RC-655", "atualiza", "RC-658", "P2025-06-26"),
    ("RC-659", "encarnação-de", "RC-071", "P2025-06-26"),
    ("RC-659", "envolve", "RC-072", "P2025-06-26"),
    ("RC-660", "planejada-por", "RC-001", "P2025-06-26"),
    ("RC-660", "envolve", "RC-659", "P2025-06-26"),
    ("RC-661", "distingue-se-de", "RC-019", "P2025-06-26"),
    ("RC-661", "distingue-se-de", "RC-050", "P2025-06-26"),
    ("RC-662", "motiva", "RC-660", "P2025-06-26"),
    ("RC-663", "relaciona-se-a", "RC-611", "P2025-06-26"),
    ("RC-664", "relaciona-se-a", "RC-397", "P2025-06-26"),
    ("RC-665", "variação", "RC-454", "P2025-06-26"),
    ("RC-665", "relaciona-se-a", "RC-655", "P2025-06-26"),
    ("RC-666", "variação", "RC-001", "P2025-06-26"),
    ("RC-666", "relaciona-se-a", "RC-655", "P2025-06-26"),

    ("RC-667", "condição-de", "RC-001", "P2026-02-28"),
    ("RC-668", "percebido-por", "RC-102", "P2026-02-28"),
    ("RC-668", "origina", "RC-670", "P2026-02-28"),
    ("RC-669", "é-um", "RC-102", "P2026-02-28"),
    ("RC-669", "desenvolve", "RC-670", "P2026-02-28"),
    ("RC-670", "criado-por", "RC-102", "P2026-02-28"),
    ("RC-670", "relaciona-se-a", "RC-628", "P2026-02-28"),
    ("RC-655", "atualiza", "RC-658", "P2026-02-28"),
    ("RC-665", "variação", "RC-454", "P2026-02-28"),
    ("RC-666", "variação", "RC-001", "P2026-02-28"),

    ("RC-671", "variação-posterior-de", "RC-489", "P2025-05-31"),
    ("RC-671", "produz", "RC-674", "P2025-05-31"),
    ("RC-672", "escrito-por", "RC-489", "P2025-05-31"),
    ("RC-673", "envolve", "RC-024", "P2025-05-31"),
    ("RC-674", "organiza", "RC-263", "P2025-05-31"),
    ("RC-674", "inclui", "RC-264", "P2025-05-31"),
    ("RC-675", "é-um", "RC-263", "P2025-05-31"),
    ("RC-676", "é-um", "RC-263", "P2025-05-31"),
    ("RC-677", "é-um", "RC-263", "P2025-05-31"),
    ("RC-678", "é-um", "RC-263", "P2025-05-31"),
    ("RC-679", "é-um", "RC-263", "P2025-05-31"),
    ("RC-680", "é-um", "RC-263", "P2025-05-31"),
    ("RC-681", "é-um", "RC-263", "P2025-05-31"),
    ("RC-682", "é-um", "RC-263", "P2025-05-31"),
    ("RC-686", "relaciona-se-a", "RC-577", "P2025-05-31"),
    ("RC-687", "usa", "RC-686", "P2025-05-31"),
    ("RC-688", "relaciona-se-a", "RC-016", "P2025-05-31"),

    # ---- Relações P2025-03-15 — devolutiva do curador
    ('RC-690', 'impulsionado-por', 'RC-378', 'P2025-03-15'),
    ('RC-690', 'distingue-se-de', 'RC-415', 'P2025-03-15'),
    ('RC-690', 'manifesta-se-em', 'RC-176', 'P2025-03-15'),
    ('RC-690', 'relaciona-se-a', 'RC-203', 'P2025-03-15'),
    ('RC-690', 'relaciona-se-a', 'RC-314', 'P2025-03-15'),
    ('RC-690', 'afeta', 'RC-106', 'P2025-03-15'),
    ('RC-690', 'afeta', 'RC-107', 'P2025-03-15'),
    ('RC-690', 'envolve', 'RC-637', 'P2025-03-15'),
    ('RC-691', 'retrata-antes-da-queda', 'RC-152', 'P2025-03-15'),
    ('RC-691', 'serve-de-modelo-para', 'RC-638', 'P2025-03-15'),
    ('RC-691', 'codificado-em', 'RC-161', 'P2025-03-15'),
    ('RC-691', 'relaciona-se-a', 'RC-625', 'P2025-03-15'),
    ('RC-691', 'relaciona-se-a', 'RC-154', 'P2025-03-15'),
    ('RC-691', 'relaciona-se-a', 'RC-163', 'P2025-03-15'),
    ('RC-692', 'reconhece', 'RC-199', 'P2025-03-15'),
    ('RC-692', 'acompanha', 'RC-100', 'P2025-03-15'),
    ('RC-692', 'transporta', 'RC-519', 'P2025-03-15'),
    ('RC-692', 'relaciona-se-a', 'RC-524', 'P2025-03-15'),
    ('RC-692', 'usa', 'RC-162', 'P2025-03-15'),
    ('RC-692', 'relaciona-se-a', 'RC-161', 'P2025-03-15'),
    ('RC-692', 'relaciona-se-a', 'RC-543', 'P2025-03-15'),
    ('RC-693', 'relaciona-se-a', 'RC-690', 'P2025-03-15'),
    ('RC-693', 'opera-em', 'RC-518', 'P2025-03-15'),
    ('RC-693', 'relaciona-se-a', 'RC-541', 'P2025-03-15'),
    ('RC-693', 'relaciona-se-a', 'RC-404', 'P2025-03-15'),
    ('RC-693', 'envolve', 'RC-161', 'P2025-03-15'),
    ('RC-693', 'aplica-se-a', 'RC-654', 'P2025-03-15'),
    ('RC-693', 'relaciona-se-a', 'RC-162', 'P2025-03-15'),
    ('RC-378', 'impulsiona', 'RC-690', 'P2025-03-15'),
    ('RC-415', 'distingue-se-de', 'RC-690', 'P2025-03-15'),
    ('RC-638', 'tem-como-modelo', 'RC-691', 'P2025-03-15'),
    ('RC-152', 'retratado-em', 'RC-691', 'P2025-03-15'),
    ('RC-199', 'reconhecida-por', 'RC-692', 'P2025-03-15'),
    ('RC-637', 'transfere-para', 'RC-107', 'P2025-03-15'),
    ('RC-655', 'atualiza', 'RC-658', 'P2025-03-15'),
    ('RC-658', 'relaciona-se-a', 'RC-559', 'P2025-03-15'),
    ('RC-154', 'converte-se-em', 'RC-217', 'P2025-03-15'),
    ('RC-091', 'transforma', 'RC-154', 'P2025-03-15'),

    # ---- Relações P2025-02-16 — devolutiva oficial do curador
    ('RC-694', 'requer', 'RC-544', 'P2025-02-16'),
    ('RC-694', 'requer', 'RC-614', 'P2025-02-16'),
    ('RC-694', 'requer', 'RC-615', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-003', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-693', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-295', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-567', 'P2025-02-16'),
    ('RC-694', 'sucede', 'RC-571', 'P2025-02-16'),
    ('RC-694', 'envolve', 'RC-695', 'P2025-02-16'),
    ('RC-694', 'envolve', 'RC-698', 'P2025-02-16'),
    ('RC-694', 'envolve', 'RC-699', 'P2025-02-16'),
    ('RC-695', 'realiza', 'RC-509', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-253', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-633', 'P2025-02-16'),
    ('RC-695', 'usa', 'RC-552', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-657', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-614', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-615', 'P2025-02-16'),
    ('RC-695', 'realiza', 'RC-694', 'P2025-02-16'),
    ('RC-696', 'gerada-por', 'RC-037', 'P2025-02-16'),
    ('RC-696', 'inclui', 'RC-586', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-561', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-217', 'P2025-02-16'),
    ('RC-696', 'inclui', 'RC-700', 'P2025-02-16'),
    ('RC-696', 'inclui', 'RC-701', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-465', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-480', 'P2025-02-16'),
    ('RC-697', 'inclui', 'RC-664', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-397', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-092', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-663', 'P2025-02-16'),
    ('RC-697', 'atua-sobre', 'RC-509', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-670', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-577', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-696', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-700', 'P2025-02-16'),
    ('RC-698', 'aplica-se-a', 'RC-217', 'P2025-02-16'),
    ('RC-698', 'distingue-se-de', 'RC-359', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-545', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-693', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-698', 'aplica-se-a', 'RC-056', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-544', 'P2025-02-16'),
    ('RC-698', 'integra', 'RC-694', 'P2025-02-16'),
    ('RC-699', 'aplica-se-a', 'RC-645', 'P2025-02-16'),
    ('RC-699', 'usa', 'RC-646', 'P2025-02-16'),
    ('RC-699', 'relaciona-se-a', 'RC-620', 'P2025-02-16'),
    ('RC-699', 'relaciona-se-a', 'RC-644', 'P2025-02-16'),
    ('RC-699', 'envolve', 'RC-100', 'P2025-02-16'),
    ('RC-699', 'relaciona-se-a', 'RC-632', 'P2025-02-16'),
    ('RC-699', 'disputada-por', 'RC-697', 'P2025-02-16'),
    ('RC-700', 'relaciona-se-a', 'RC-586', 'P2025-02-16'),
    ('RC-700', 'gera-linhagem-de', 'RC-465', 'P2025-02-16'),
    ('RC-700', 'gera-linhagem-de', 'RC-664', 'P2025-02-16'),
    ('RC-700', 'parte-de', 'RC-696', 'P2025-02-16'),
    ('RC-700', 'relaciona-se-a', 'RC-701', 'P2025-02-16'),
    ('RC-700', 'gera-linhagem-de', 'RC-480', 'P2025-02-16'),
    ('RC-700', 'gera-linhagem-de', 'RC-581', 'P2025-02-16'),
    ('RC-700', 'relaciona-se-a', 'RC-697', 'P2025-02-16'),
    ('RC-701', 'relaciona-se-a', 'RC-700', 'P2025-02-16'),
    ('RC-701', 'gera-linhagem-de', 'RC-664', 'P2025-02-16'),
    ('RC-701', 'parte-de', 'RC-696', 'P2025-02-16'),
    ('RC-701', 'relaciona-se-a', 'RC-465', 'P2025-02-16'),
    ('RC-701', 'relaciona-se-a', 'RC-480', 'P2025-02-16'),
    ('RC-701', 'relaciona-se-a', 'RC-586', 'P2025-02-16'),
    ('RC-037', 'gera', 'RC-696', 'P2025-02-16'),
    ('RC-586', 'parte-de', 'RC-696', 'P2025-02-16'),
    ('RC-664', 'parte-de', 'RC-696', 'P2025-02-16'),
    ('RC-664', 'atua-por', 'RC-697', 'P2025-02-16'),
    ('RC-664', 'descende-de', 'RC-700', 'P2025-02-16'),
    ('RC-664', 'descende-de', 'RC-701', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-577', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-687', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-688', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-668', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-670', 'P2025-02-16'),
    ('RC-664', 'influencia', 'RC-283', 'P2025-02-16'),
    ('RC-577', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-577', 'relaciona-se-a', 'RC-687', 'P2025-02-16'),
    ('RC-687', 'relaciona-se-a', 'RC-577', 'P2025-02-16'),
    ('RC-687', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-668', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-670', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-544', 'necessário-a', 'RC-694', 'P2025-02-16'),
    ('RC-614', 'necessário-a', 'RC-694', 'P2025-02-16'),
    ('RC-615', 'necessário-a', 'RC-694', 'P2025-02-16'),
    ('RC-645', 'recebe', 'RC-699', 'P2025-02-16'),
    ('RC-646', 'suporta', 'RC-699', 'P2025-02-16'),
    ('RC-295', 'relaciona-se-a', 'RC-694', 'P2025-02-16'),
    ('RC-395', 'relaciona-se-a', 'RC-471', 'P2025-02-16'),
    ('RC-163', 'relaciona-se-a', 'RC-694', 'P2025-02-16'),
    ('RC-693', 'relaciona-se-a', 'RC-694', 'P2025-02-16'),

    # ---- Relações P2025-02-15 — devolutiva oficial do curador
    ('RC-702', 'relaciona-se-a', 'RC-192', 'P2025-02-15'),
    ('RC-702', 'sustentada-por', 'RC-335', 'P2025-02-15'),
    ('RC-702', 'sustentada-por', 'RC-563', 'P2025-02-15'),
    ('RC-702', 'relaciona-se-a', 'RC-551', 'P2025-02-15'),
    ('RC-702', 'rompida-por', 'RC-372', 'P2025-02-15'),
    ('RC-702', 'rompida-por', 'RC-703', 'P2025-02-15'),
    ('RC-702', 'atravessada-por', 'RC-706', 'P2025-02-15'),
    ('RC-702', 'relaciona-se-a', 'RC-253', 'P2025-02-15'),
    ('RC-702', 'relaciona-se-a', 'RC-657', 'P2025-02-15'),
    ('RC-703', 'orienta', 'RC-695', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-546', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-559', 'P2025-02-15'),
    ('RC-703', 'usa', 'RC-633', 'P2025-02-15'),
    ('RC-703', 'realiza', 'RC-509', 'P2025-02-15'),
    ('RC-703', 'explica', 'RC-702', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-707', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-712', 'P2025-02-15'),
    ('RC-704', 'transporta', 'RC-519', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-543', 'P2025-02-15'),
    ('RC-704', 'transporta', 'RC-548', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-692', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-623', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-624', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-625', 'P2025-02-15'),
    ('RC-704', 'hospeda', 'RC-553', 'P2025-02-15'),
    ('RC-704', 'hospeda', 'RC-558', 'P2025-02-15'),
    ('RC-705', 'realiza', 'RC-509', 'P2025-02-15'),
    ('RC-705', 'relaciona-se-a', 'RC-508', 'P2025-02-15'),
    ('RC-705', 'relaciona-se-a', 'RC-328', 'P2025-02-15'),
    ('RC-705', 'relaciona-se-a', 'RC-566', 'P2025-02-15'),
    ('RC-705', 'orienta', 'RC-695', 'P2025-02-15'),
    ('RC-705', 'usa', 'RC-703', 'P2025-02-15'),
    ('RC-706', 'atravessa', 'RC-702', 'P2025-02-15'),
    ('RC-706', 'usa', 'RC-552', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-623', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-624', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-625', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-633', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-704', 'P2025-02-15'),
    ('RC-707', 'organiza', 'RC-194', 'P2025-02-15'),
    ('RC-707', 'relaciona-se-a', 'RC-218', 'P2025-02-15'),
    ('RC-707', 'relaciona-se-a', 'RC-546', 'P2025-02-15'),
    ('RC-707', 'relaciona-se-a', 'RC-693', 'P2025-02-15'),
    ('RC-707', 'usado-por', 'RC-514', 'P2025-02-15'),
    ('RC-707', 'explicado-por', 'RC-703', 'P2025-02-15'),
    ('RC-707', 'relaciona-se-a', 'RC-708', 'P2025-02-15'),
    ('RC-708', 'realiza', 'RC-509', 'P2025-02-15'),
    ('RC-708', 'envolve', 'RC-161', 'P2025-02-15'),
    ('RC-708', 'atua-em', 'RC-559', 'P2025-02-15'),
    ('RC-708', 'aplica-se-a', 'RC-418', 'P2025-02-15'),
    ('RC-708', 'usa', 'RC-707', 'P2025-02-15'),
    ('RC-708', 'atravessa', 'RC-702', 'P2025-02-15'),
    ('RC-708', 'é-um', 'RC-372', 'P2025-02-15'),
    ('RC-708', 'aplica-se-a', 'RC-654', 'P2025-02-15'),
    ('RC-709', 'é-um', 'RC-544', 'P2025-02-15'),
    ('RC-709', 'usa', 'RC-645', 'P2025-02-15'),
    ('RC-709', 'usa', 'RC-646', 'P2025-02-15'),
    ('RC-709', 'relaciona-se-a', 'RC-699', 'P2025-02-15'),
    ('RC-709', 'relaciona-se-a', 'RC-710', 'P2025-02-15'),
    ('RC-709', 'envolve', 'RC-557', 'P2025-02-15'),
    ('RC-709', 'relaciona-se-a', 'RC-614', 'P2025-02-15'),
    ('RC-709', 'relaciona-se-a', 'RC-615', 'P2025-02-15'),
    ('RC-710', 'atua-em', 'RC-518', 'P2025-02-15'),
    ('RC-710', 'acionado-por', 'RC-543', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-619', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-400', 'P2025-02-15'),
    ('RC-710', 'produz', 'RC-544', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-712', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-709', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-693', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-698', 'P2025-02-15'),
    ('RC-711', 'relaciona-se-a', 'RC-385', 'P2025-02-15'),
    ('RC-711', 'condensa', 'RC-529', 'P2025-02-15'),
    ('RC-711', 'relaciona-se-a', 'RC-520', 'P2025-02-15'),
    ('RC-711', 'relaciona-se-a', 'RC-523', 'P2025-02-15'),
    ('RC-711', 'usa', 'RC-548', 'P2025-02-15'),
    ('RC-711', 'usa', 'RC-517', 'P2025-02-15'),
    ('RC-711', 'reforça', 'RC-702', 'P2025-02-15'),
    ('RC-711', 'relaciona-se-a', 'RC-194', 'P2025-02-15'),
    ('RC-712', 'orienta', 'RC-633', 'P2025-02-15'),
    ('RC-712', 'atua-em', 'RC-619', 'P2025-02-15'),
    ('RC-712', 'usa', 'RC-552', 'P2025-02-15'),
    ('RC-712', 'relaciona-se-a', 'RC-703', 'P2025-02-15'),
    ('RC-712', 'relaciona-se-a', 'RC-710', 'P2025-02-15'),
    ('RC-712', 'orienta', 'RC-695', 'P2025-02-15'),
    ('RC-712', 'usa', 'RC-517', 'P2025-02-15'),
    ('RC-713', 'envolve', 'RC-072', 'P2025-02-15'),
    ('RC-713', 'envolve', 'RC-259', 'P2025-02-15'),
    ('RC-713', 'atua-em', 'RC-217', 'P2025-02-15'),
    ('RC-713', 'relaciona-se-a', 'RC-367', 'P2025-02-15'),
    ('RC-713', 'relaciona-se-a', 'RC-633', 'P2025-02-15'),
    ('RC-713', 'distingue-se-de', 'RC-712', 'P2025-02-15'),
    ('RC-335', 'sustenta', 'RC-702', 'P2025-02-15'),
    ('RC-563', 'sustenta', 'RC-702', 'P2025-02-15'),
    ('RC-657', 'relaciona-se-a', 'RC-702', 'P2025-02-15'),
    ('RC-519', 'transportado-por', 'RC-704', 'P2025-02-15'),
    ('RC-692', 'relaciona-se-a', 'RC-704', 'P2025-02-15'),
    ('RC-514', 'usa', 'RC-707', 'P2025-02-15'),
    ('RC-218', 'relaciona-se-a', 'RC-707', 'P2025-02-15'),
    ('RC-381', 'relaciona-se-a', 'RC-711', 'P2025-02-15'),
    ('RC-699', 'relaciona-se-a', 'RC-709', 'P2025-02-15'),
    ('RC-557', 'relaciona-se-a', 'RC-709', 'P2025-02-15'),
    ('RC-692', 'relaciona-se-a', 'RC-009', 'P2025-02-15'),
    ('RC-280', 'relaciona-se-a', 'RC-692', 'P2025-02-15'),
    ('RC-698', 'relaciona-se-a', 'RC-710', 'P2025-02-15'),
    ('RC-577', 'relaciona-se-a', 'RC-687', 'P2025-02-15'),
    ('RC-529', 'relaciona-se-a', 'RC-612', 'P2025-02-15'),
    ('RC-508', 'relaciona-se-a', 'RC-705', 'P2025-02-15'),

    # ---- Relações P2024-11-30 — devolutiva oficial
    ('RC-714', 'criados-por', 'RC-454', 'P2024-11-30'),
    ('RC-714', 'contêm', 'RC-715', 'P2024-11-30'),
    ('RC-714', 'relaciona-se-a', 'RC-716', 'P2024-11-30'),
    ('RC-714', 'transportados-por', 'RC-611', 'P2024-11-30'),
    ('RC-714', 'organizados-por', 'RC-658', 'P2024-11-30'),
    ('RC-714', 'relaciona-se-a', 'RC-521', 'P2024-11-30'),
    ('RC-714', 'cumpre-se-em', 'RC-718', 'P2024-11-30'),
    ('RC-715', 'compõe', 'RC-161', 'P2024-11-30'),
    ('RC-715', 'compõe', 'RC-162', 'P2024-11-30'),
    ('RC-715', 'organiza-se-em', 'RC-217', 'P2024-11-30'),
    ('RC-715', 'relaciona-se-a', 'RC-693', 'P2024-11-30'),
    ('RC-715', 'armazenada-em', 'RC-714', 'P2024-11-30'),
    ('RC-715', 'medida-por', 'RC-716', 'P2024-11-30'),
    ('RC-715', 'pode-colapsar-em', 'RC-717', 'P2024-11-30'),
    ('RC-715', 'relaciona-se-a', 'RC-176', 'P2024-11-30'),
    ('RC-716', 'mapeado-por', 'RC-454', 'P2024-11-30'),
    ('RC-716', 'atua-em', 'RC-519', 'P2024-11-30'),
    ('RC-716', 'atua-em', 'RC-217', 'P2024-11-30'),
    ('RC-716', 'processado-por', 'RC-658', 'P2024-11-30'),
    ('RC-716', 'mede', 'RC-715', 'P2024-11-30'),
    ('RC-716', 'relaciona-se-a', 'RC-332', 'P2024-11-30'),
    ('RC-716', 'registrado-em', 'RC-714', 'P2024-11-30'),
    ('RC-716', 'submete', 'RC-720', 'P2024-11-30'),
    ('RC-717', 'envolve', 'RC-638', 'P2024-11-30'),
    ('RC-717', 'é-fenômeno-de', 'RC-690', 'P2024-11-30'),
    ('RC-717', 'primeiro-caso', 'RC-001', 'P2024-11-30'),
    ('RC-717', 'risco-para', 'RC-414', 'P2024-11-30'),
    ('RC-717', 'envolve', 'RC-715', 'P2024-11-30'),
    ('RC-717', 'relaciona-se-a', 'RC-716', 'P2024-11-30'),
    ('RC-717', 'relaciona-se-a', 'RC-425', 'P2024-11-30'),
    ('RC-718', 'cumpre', 'RC-611', 'P2024-11-30'),
    ('RC-718', 'é-evento-de', 'RC-094', 'P2024-11-30'),
    ('RC-718', 'iniciado-por', 'RC-454', 'P2024-11-30'),
    ('RC-718', 'envolve', 'RC-190', 'P2024-11-30'),
    ('RC-718', 'envolve', 'RC-585', 'P2024-11-30'),
    ('RC-718', 'envolve', 'RC-659', 'P2024-11-30'),
    ('RC-718', 'envolve', 'RC-665', 'P2024-11-30'),
    ('RC-718', 'abre', 'RC-714', 'P2024-11-30'),
    ('RC-719', 'inclui', 'RC-623', 'P2024-11-30'),
    ('RC-719', 'inclui', 'RC-217', 'P2024-11-30'),
    ('RC-719', 'inclui', 'RC-553', 'P2024-11-30'),
    ('RC-719', 'gerida-por', 'RC-633', 'P2024-11-30'),
    ('RC-719', 'relaciona-se-a', 'RC-704', 'P2024-11-30'),
    ('RC-719', 'relaciona-se-a', 'RC-529', 'P2024-11-30'),
    ('RC-719', 'aplica-se-a', 'RC-654', 'P2024-11-30'),
    ('RC-720', 'submetidos-a', 'RC-658', 'P2024-11-30'),
    ('RC-720', 'explicados-por', 'RC-655', 'P2024-11-30'),
    ('RC-720', 'relaciona-se-a', 'RC-508', 'P2024-11-30'),
    ('RC-720', 'relaciona-se-a', 'RC-328', 'P2024-11-30'),
    ('RC-720', 'envolve', 'RC-716', 'P2024-11-30'),
    ('RC-720', 'envolve', 'RC-519', 'P2024-11-30'),
    ('RC-720', 'relaciona-se-a', 'RC-404', 'P2024-11-30'),
    ('RC-720', 'processa', 'RC-715', 'P2024-11-30'),
    ('RC-454', 'cria', 'RC-714', 'P2024-11-30'),
    ('RC-454', 'mapeia', 'RC-716', 'P2024-11-30'),
    ('RC-454', 'cria', 'RC-658', 'P2024-11-30'),
    ('RC-454', 'cria', 'RC-467', 'P2024-11-30'),
    ('RC-396', 'vinculado-ao-espírito', 'RC-454', 'P2024-11-30'),
    ('RC-585', 'vinculado-ao-espírito', 'RC-454', 'P2024-11-30'),
    ('RC-659', 'vinculado-ao-espírito', 'RC-454', 'P2024-11-30'),
    ('RC-665', 'variação', 'RC-454', 'P2024-11-30'),
    ('RC-658', 'criada-por', 'RC-454', 'P2024-11-30'),
    ('RC-658', 'organiza', 'RC-715', 'P2024-11-30'),
    ('RC-658', 'processa', 'RC-716', 'P2024-11-30'),
    ('RC-467', 'criadas-por', 'RC-454', 'P2024-11-30'),
    ('RC-467', 'operam-em', 'RC-658', 'P2024-11-30'),
    ('RC-611', 'transporta', 'RC-714', 'P2024-11-30'),
    ('RC-611', 'originada-em', 'RC-454', 'P2024-11-30'),
    ('RC-094', 'cumpre', 'RC-718', 'P2024-11-30'),
    ('RC-081', 'vinculado-ao-espírito', 'RC-454', 'P2024-11-30'),
    ('RC-282', 'relaciona-se-a', 'RC-454', 'P2024-11-30'),
    ('RC-064', 'relaciona-se-a', 'RC-081', 'P2024-11-30'),
    ('RC-176', 'relaciona-se-a', 'RC-715', 'P2024-11-30'),
    ('RC-395', 'relaciona-se-a', 'RC-611', 'P2024-11-30'),
    ('RC-425', 'opõe-se-a', 'RC-714', 'P2024-11-30'),
    ('RC-414', 'risco-de', 'RC-717', 'P2024-11-30'),
    ('RC-655', 'atualiza', 'RC-658', 'P2024-11-30'),
    ('RC-332', 'relaciona-se-a', 'RC-716', 'P2024-11-30'),
    ('RC-404', 'relaciona-se-a', 'RC-720', 'P2024-11-30'),
    ('RC-654', 'relaciona-se-a', 'RC-719', 'P2024-11-30'),
    ('RC-529', 'relaciona-se-a', 'RC-719', 'P2024-11-30'),
    ('RC-633', 'gere', 'RC-719', 'P2024-11-30'),
    ('RC-553', 'integra', 'RC-719', 'P2024-11-30'),
    ('RC-577', 'relaciona-se-a', 'RC-687', 'P2024-11-30'),
    ('RC-686', 'relaciona-se-a', 'RC-687', 'P2024-11-30'),
    ('RC-687', 'relaciona-se-a', 'RC-577', 'P2024-11-30'),

    # ---- Relações P2024-11-09 — devolutiva oficial
    ('RC-721', 'avaliado-por', 'RC-722', 'P2024-11-09'),
    ('RC-721', 'manifesta-se-em', 'RC-723', 'P2024-11-09'),
    ('RC-721', 'relaciona-se-a', 'RC-605', 'P2024-11-09'),
    ('RC-721', 'relaciona-se-a', 'RC-717', 'P2024-11-09'),
    ('RC-721', 'relaciona-se-a', 'RC-720', 'P2024-11-09'),
    ('RC-721', 'observado-de-dentro-por', 'RC-654', 'P2024-11-09'),
    ('RC-722', 'relaciona-se-a', 'RC-508', 'P2024-11-09'),
    ('RC-722', 'relaciona-se-a', 'RC-328', 'P2024-11-09'),
    ('RC-722', 'realizada-por', 'RC-705', 'P2024-11-09'),
    ('RC-722', 'orienta', 'RC-509', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-052', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-205', 'P2024-11-09'),
    ('RC-723', 'critica', 'RC-341', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-720', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-605', 'P2024-11-09'),
    ('RC-724', 'registradas-em', 'RC-548', 'P2024-11-09'),
    ('RC-724', 'armazenadas-em', 'RC-711', 'P2024-11-09'),
    ('RC-724', 'relaciona-se-a', 'RC-381', 'P2024-11-09'),
    ('RC-724', 'relaciona-se-a', 'RC-194', 'P2024-11-09'),
    ('RC-725', 'é-ilha-de', 'RC-160', 'P2024-11-09'),
    ('RC-725', 'alimenta', 'RC-163', 'P2024-11-09'),
    ('RC-725', 'realiza', 'RC-508', 'P2024-11-09'),
    ('RC-725', 'realizada-por', 'RC-705', 'P2024-11-09'),
    ('RC-725', 'resiste-a', 'RC-690', 'P2024-11-09'),
    ('RC-726', 'é-um', 'RC-084', 'P2024-11-09'),
    ('RC-726', 'relaciona-se-a', 'RC-529', 'P2024-11-09'),
    ('RC-726', 'relaciona-se-a', 'RC-513', 'P2024-11-09'),
    ('RC-726', 'relaciona-se-a', 'RC-507', 'P2024-11-09'),
    ('RC-726', 'destinação-gerida-por', 'RC-633', 'P2024-11-09'),
    ('RC-726', 'relaciona-se-a', 'RC-704', 'P2024-11-09'),
    ('RC-727', 'inclui', 'RC-086', 'P2024-11-09'),
    ('RC-727', 'inclui', 'RC-189', 'P2024-11-09'),
    ('RC-727', 'inclui', 'RC-579', 'P2024-11-09'),
    ('RC-727', 'relaciona-se-a', 'RC-619', 'P2024-11-09'),
    ('RC-727', 'relaciona-se-a', 'RC-283', 'P2024-11-09'),
    ('RC-727', 'opõe-se-a', 'RC-325', 'P2024-11-09'),
    ('RC-727', 'atribuída-em-teologia-comparada-a', 'RC-486', 'P2024-11-09'),
    ('RC-059', 'associada-a', 'RC-623', 'P2024-11-09'),
    ('RC-060', 'associada-a', 'RC-624', 'P2024-11-09'),
    ('RC-061', 'associada-a', 'RC-625', 'P2024-11-09'),
    ('RC-602', 'relaciona-se-a', 'RC-415', 'P2024-11-09'),
    ('RC-654', 'observa-de-dentro', 'RC-721', 'P2024-11-09'),
    ('RC-605', 'relaciona-se-a', 'RC-721', 'P2024-11-09'),
    ('RC-605', 'relaciona-se-a', 'RC-723', 'P2024-11-09'),
    ('RC-637', 'descreve-transferência-de', 'RC-107', 'P2024-11-09'),
    ('RC-637', 'transfere-para', 'RC-106', 'P2024-11-09'),
    ('RC-161', 'relaciona-se-a', 'RC-692', 'P2024-11-09'),
    ('RC-692', 'usa', 'RC-161', 'P2024-11-09'),
    ('RC-692', 'usa', 'RC-162', 'P2024-11-09'),
    ('RC-163', 'alimentada-por', 'RC-725', 'P2024-11-09'),
    ('RC-705', 'realiza', 'RC-722', 'P2024-11-09'),
    ('RC-705', 'realiza', 'RC-725', 'P2024-11-09'),
    ('RC-526', 'relaciona-se-a', 'RC-721', 'P2024-11-09'),
    ('RC-223', 'comparado-a', 'RC-721', 'P2024-11-09'),
    ('RC-690', 'resistido-por', 'RC-725', 'P2024-11-09'),
    ('RC-160', 'manifesta-se-em', 'RC-725', 'P2024-11-09'),
    ('RC-708', 'envolve', 'RC-161', 'P2024-11-09'),
    ('RC-708', 'relaciona-se-a', 'RC-559', 'P2024-11-09'),
    ('RC-708', 'relaciona-se-a', 'RC-529', 'P2024-11-09'),
    ('RC-708', 'relaciona-se-a', 'RC-368', 'P2024-11-09'),
    ('RC-529', 'sustenta-ponte-não-local', 'RC-708', 'P2024-11-09'),
    ('RC-189', 'distingue-se-de', 'RC-540', 'P2024-11-09'),
    ('RC-486', 'atribuído-em-teologia-comparada-a', 'RC-325', 'P2024-11-09'),
    ('RC-325', 'opõe-se-a', 'RC-727', 'P2024-11-09'),
    ('RC-541', 'relaciona-se-a', 'RC-400', 'P2024-11-09'),
    ('RC-541', 'relaciona-se-a', 'RC-540', 'P2024-11-09'),
    ('RC-654', 'realiza', 'RC-509', 'P2024-11-09'),
    ('RC-657', 'opõe-se-a', 'RC-335', 'P2024-11-09'),
    ('RC-717', 'relaciona-se-a', 'RC-638', 'P2024-11-09'),
    ('RC-720', 'relaciona-se-a', 'RC-725', 'P2024-11-09'),
    ('RC-633', 'orienta-destinação-em', 'RC-726', 'P2024-11-09'),
    ('RC-704', 'relaciona-se-a', 'RC-726', 'P2024-11-09'),

    # ---- Devolutiva Oficial do Curador — P2024-11-02
    ('RC-728', 'estrutura-se-por', 'RC-729', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-730', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-731', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-732', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-733', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-734', 'P2024-11-02'),
    ('RC-728', 'estrutura-se-por', 'RC-735', 'P2024-11-02'),
    ('RC-729', 'metáfora-alegada-da-RC-sobre', 'RC-217', 'P2024-11-02'),
    ('RC-729', 'relaciona-se-a', 'RC-543', 'P2024-11-02'),
    ('RC-729', 'contextualiza', 'RC-732', 'P2024-11-02'),
    ('RC-730', 'inclui', 'RC-470', 'P2024-11-02'),
    ('RC-730', 'conecta-se-por', 'RC-471', 'P2024-11-02'),
    ('RC-730', 'destruído-em', 'RC-395', 'P2024-11-02'),
    ('RC-730', 'sucedido-por', 'RC-731', 'P2024-11-02'),
    ('RC-731', 'sucede', 'RC-730', 'P2024-11-02'),
    ('RC-731', 'ancora', 'RC-470', 'P2024-11-02'),
    ('RC-731', 'conecta-se-por', 'RC-471', 'P2024-11-02'),
    ('RC-731', 'contextualiza', 'RC-734', 'P2024-11-02'),
    ('RC-732', 'manifesta-se-no-discurso-como', 'RC-729', 'P2024-11-02'),
    ('RC-732', 'atua-sobre', 'RC-217', 'P2024-11-02'),
    ('RC-732', 'relaciona-se-a', 'RC-543', 'P2024-11-02'),
    ('RC-732', 'relaciona-se-a', 'RC-335', 'P2024-11-02'),
    ('RC-732', 'favorece', 'RC-733', 'P2024-11-02'),
    ('RC-733', 'usa', 'RC-188', 'P2024-11-02'),
    ('RC-733', 'reforça', 'RC-335', 'P2024-11-02'),
    ('RC-733', 'alimenta', 'RC-385', 'P2024-11-02'),
    ('RC-733', 'enfrentada-por', 'RC-735', 'P2024-11-02'),
    ('RC-734', 'regenera-na-narrativa', 'RC-037', 'P2024-11-02'),
    ('RC-734', 'envolve', 'RC-135', 'P2024-11-02'),
    ('RC-734', 'envolve', 'RC-465', 'P2024-11-02'),
    ('RC-734', 'resulta-em', 'RC-466', 'P2024-11-02'),
    ('RC-734', 'precede', 'RC-696', 'P2024-11-02'),
    ('RC-734', 'relaciona-se-a', 'RC-731', 'P2024-11-02'),
    ('RC-735', 'relaciona-se-a', 'RC-508', 'P2024-11-02'),
    ('RC-735', 'relaciona-se-a', 'RC-705', 'P2024-11-02'),
    ('RC-735', 'relaciona-se-a', 'RC-722', 'P2024-11-02'),
    ('RC-735', 'relaciona-se-a', 'RC-725', 'P2024-11-02'),
    ('RC-081', 'propõe', 'RC-091', 'P2024-11-02'),
    ('RC-081', 'distingue-se-de', 'RC-454', 'P2024-11-02'),
    ('RC-282', 'correspondência-em-teologia-comparada-de', 'RC-081', 'P2024-11-02'),
    ('RC-282', 'distingue-se-de', 'RC-454', 'P2024-11-02'),
    ('RC-091', 'proposto-por', 'RC-081', 'P2024-11-02'),
    ('RC-395', 'destrói', 'RC-730', 'P2024-11-02'),
    ('RC-395', 'ocorre-no-eixo-de', 'RC-470', 'P2024-11-02'),
    ('RC-395', 'relaciona-se-a', 'RC-471', 'P2024-11-02'),
    ('RC-470', 'integra', 'RC-730', 'P2024-11-02'),
    ('RC-471', 'conecta', 'RC-730', 'P2024-11-02'),
    ('RC-465', 'participa-de', 'RC-734', 'P2024-11-02'),
    ('RC-696', 'sucede', 'RC-734', 'P2024-11-02'),
    ('RC-586', 'integra', 'RC-696', 'P2024-11-02'),
    ('RC-700', 'descende-de-membro-de', 'RC-586', 'P2024-11-02'),
    ('RC-700', 'une-se-às-filhas-de', 'RC-701', 'P2024-11-02'),
    ('RC-701', 'tem-filhas-unidas-a', 'RC-700', 'P2024-11-02'),


    # ---- P2024-09-29 — relações aprovadas
    ("RC-736", "manifesta-se-em", "RC-240", "P2024-09-29"),  # R-AM01
    ("RC-736", "opera-por", "RC-269", "P2024-09-29"),  # R-AM02
    ("RC-736", "relaciona-se-a", "RC-293", "P2024-09-29"),  # R-AM03
    ("RC-736", "relaciona-se-a", "RC-531", "P2024-09-29"),  # R-AM04
    ("RC-736", "atribuído-a", "RC-001", "P2024-09-29"),  # R-AM05
    ("RC-736", "inclui", "RC-737", "P2024-09-29"),  # R-AM06
    ("RC-736", "inclui", "RC-741", "P2024-09-29"),  # R-AM07
    ("RC-737", "envolve", "RC-738", "P2024-09-29"),  # R-AM08
    ("RC-737", "envolve", "RC-739", "P2024-09-29"),  # R-AM09
    ("RC-737", "envolve", "RC-740", "P2024-09-29"),  # R-AM10
    ("RC-737", "manifesta-se-em", "RC-269", "P2024-09-29"),  # R-AM12
    ("RC-737", "relaciona-se-a", "RC-531", "P2024-09-29"),  # R-AM13
    ("RC-741", "envolve", "RC-665", "P2024-09-29"),  # R-AM14
    ("RC-741", "produz", "RC-655", "P2024-09-29"),  # R-AM16
    ("RC-293", "expressa-se-em", "RC-269", "P2024-09-29"),  # R-AM19
    ("RC-194", "mapeia", "RC-269", "P2024-09-29"),  # R-AM20
    ("RC-271", "direciona", "RC-269", "P2024-09-29"),  # R-AM21
    ("RC-571", "relaciona-se-a", "RC-295", "P2024-09-29"),  # R-AM23
    ("RC-019", "sustentam", "RC-638", "P2024-09-29"),  # R-AM25
    # Relações vigentes com nova fonte autorizada
    ("RC-145", "variação", "RC-480", "P2024-09-29"),  # SRC-AM01
    ("RC-655", "atualiza", "RC-658", "P2024-09-29"),  # SRC-AM02
    ("RC-665", "variação", "RC-454", "P2024-09-29"),  # SRC-AM03
    ("RC-666", "variação", "RC-001", "P2024-09-29"),  # SRC-AM04

    # ---- P2024-08-03 — relações aprovadas e materializáveis
    ("RC-742", "é-falência-de", "RC-040", "P2024-08-03"),  # R-FD01
    ("RC-742", "motiva-recurso-a", "RC-734", "P2024-08-03"),  # R-FD02
    ("RC-742", "reaparece-como-destruição-em", "RC-395", "P2024-08-03"),  # R-FD04
    ("RC-743", "expressa-sociabilidade-por", "RC-529", "P2024-08-03"),  # R-FD06
    ("RC-743", "é-comparada-à-emergência-de", "RC-525", "P2024-08-03"),  # R-FD07
    ("RC-744", "persiste-em", "RC-108", "P2024-08-03"),  # R-FD08
    ("RC-525", "manifesta-descontinuidade-em", "RC-727", "P2024-08-03"),  # R-FD09
    ("RC-037", "correspondência-em-teologia-comparada-de", "RC-001", "P2024-08-03"),  # TC-FD01
    ("RC-282", "correspondência-em-teologia-comparada-de", "RC-081", "P2024-08-03"),  # TC-FD02
    ("RC-135", "correspondência-em-teologia-comparada-de", "RC-009", "P2024-08-03"),  # TC-FD04
    # Relações vigentes: somente nova proveniência, sem nova assinatura semântica
    ("RC-081", "propõe", "RC-091", "P2024-08-03"),  # R-FD10
    ("RC-696", "inclui", "RC-586", "P2024-08-03"),  # R-FD11
    ("RC-696", "inclui", "RC-700", "P2024-08-03"),  # R-FD12

    # ---- P2024-07-14 — relações aprovadas e materializáveis
    ("RC-745", "organiza-se-em", "RC-726", "P2024-07-14"),  # R-CED01
    ("RC-745", "avaliado-por", "RC-722", "P2024-07-14"),  # R-CED02
    ("RC-193", "repercute-em", "RC-745", "P2024-07-14"),  # R-CED03
    ("RC-733", "manifesta-se-em", "RC-745", "P2024-07-14"),  # R-CED04
    ("RC-722", "depende-de", "RC-633", "P2024-07-14"),  # R-CED05
    ("RC-722", "necessário-a", "RC-514", "P2024-07-14"),  # R-CED06
    ("RC-514", "usa", "RC-231", "P2024-07-14"),  # R-CED07
    ("RC-613", "base-de", "RC-612", "P2024-07-14"),  # R-CED08
    ("RC-604", "envolve", "RC-001", "P2024-07-14"),  # R-CED09
    ("RC-604", "envolve", "RC-037", "P2024-07-14"),  # R-CED10
    ("RC-604", "envolve", "RC-102", "P2024-07-14"),  # R-CED11
    ("RC-072", "serve-de-modelo-para", "RC-722", "P2024-07-14"),  # R-CED12
    ("RC-742", "resulta-de", "RC-604", "P2024-07-14"),  # R-CED13
    ("RC-675", "correspondência-em-teologia-comparada-de", "RC-102", "P2024-07-14"),  # TC-CED03
    # Relações vigentes: somente nova proveniência, sem nova assinatura semântica
    ("RC-726", "destinação-gerida-por", "RC-633", "P2024-07-14"),  # R-CED14
    ("RC-653", "sucede", "RC-514", "P2024-07-14"),  # R-CED15
    ("RC-656", "atualiza", "RC-094", "P2024-07-14"),  # R-CED16
    ("RC-261", "variação", "RC-001", "P2024-07-14"),  # TC-CED01a
    ("RC-261", "variação", "RC-037", "P2024-07-14"),  # TC-CED01b
    ("RC-565", "variação", "RC-135", "P2024-07-14"),  # TC-CED02a
    ("RC-565", "variação", "RC-009", "P2024-07-14"),  # TC-CED02b
    ("RC-604", "envolve", "RC-009", "P2024-07-14"),  # TC-CED05a
    ("RC-604", "envolve", "RC-072", "P2024-07-14"),  # TC-CED05b
    ("RC-610", "relaciona-se-a", "RC-104", "P2024-07-14"),  # TC-CED07a
    ("RC-610", "inclui", "RC-457", "P2024-07-14"),  # TC-CED07b
    ("RC-610", "inclui", "RC-458", "P2024-07-14"),  # TC-CED07c
    ("RC-610", "inclui", "RC-459", "P2024-07-14"),  # TC-CED07d

    # ---- P2024-07-13 — relações aprovadas e materializáveis
    ("RC-003", "envolve", "RC-106", "P2024-07-13"),  # R-RCT01
    ("RC-003", "ocorre-em", "RC-690", "P2024-07-13"),  # R-RCT02
    ("RC-003", "rompe", "RC-702", "P2024-07-13"),  # R-RCT03
    ("RC-003", "envolve", "RC-258", "P2024-07-13"),  # R-RCT04
    ("RC-662", "confronta", "RC-722", "P2024-07-13"),  # R-RCT05
    # Relações vigentes: somente nova proveniência, sem nova assinatura semântica
    ("RC-342", "encerra-com", "RC-003", "P2024-07-13"),  # R-RCT07
    ("RC-630", "ocorre-em", "RC-106", "P2024-07-13"),  # R-RCT08
    ("RC-637", "origem-em", "RC-106", "P2024-07-13"),  # R-RCT09
    ("RC-690", "manifesta-se-em", "RC-176", "P2024-07-13"),  # R-RCT10
    ("RC-690", "afeta", "RC-106", "P2024-07-13"),  # R-RCT11
    ("RC-690", "envolve", "RC-637", "P2024-07-13"),  # R-RCT12
    ("RC-693", "relaciona-se-a", "RC-690", "P2024-07-13"),  # R-RCT13
    ("RC-645", "usa", "RC-646", "P2024-07-13"),  # R-RCT14
    ("RC-699", "aplica-se-a", "RC-645", "P2024-07-13"),  # R-RCT15
    ("RC-699", "usa", "RC-646", "P2024-07-13"),  # R-RCT16
    ("RC-645", "recebe", "RC-699", "P2024-07-13"),  # R-RCT17
    ("RC-646", "suporta", "RC-699", "P2024-07-13"),  # R-RCT18
    ("RC-709", "usa", "RC-645", "P2024-07-13"),  # R-RCT19
    ("RC-709", "usa", "RC-646", "P2024-07-13"),  # R-RCT20
    ("RC-724", "armazenadas-em", "RC-711", "P2024-07-13"),  # R-RCT21
    # R-RCT06 rejeitada: RC-742 resulta-de RC-176 não foi materializada
    ("RC-746", "relaciona-se-a", "RC-529", "P2024-03-03"),  # R-DS01 dessensibilização ~ ressonância límbica
    ("RC-746", "relaciona-se-a", "RC-049", "P2024-03-03"),  # R-DS02 usufruto / insensibilidade demo
    ("RC-746", "relaciona-se-a", "RC-001", "P2024-03-03"),  # R-DS03 Javé insensível / alimentação dos deuses
    ("RC-746", "relaciona-se-a", "RC-378", "P2024-03-03"),  # R-DS04 dessensibilização dos elétrons
    ("RC-746", "relaciona-se-a", "RC-335", "P2024-03-03"),  # R-DS05 adestramento / condicionamento
    ("RC-746", "relaciona-se-a", "RC-705", "P2024-03-03"),  # R-DS06 resposta ética (se incomodar é preciso)
    ("RC-746", "relaciona-se-a", "RC-747", "P2024-03-03"),  # R-DS07 vergonha de existir (resposta)
    ("RC-746", "relaciona-se-a", "RC-748", "P2024-03-03"),  # R-DS08 genótipo da gentileza (alternativa)
    ("RC-747", "relaciona-se-a", "RC-078", "P2024-03-03"),  # R-DS09 Lúcifer criou o genoma antes
    ("RC-748", "relaciona-se-a", "RC-486", "P2024-03-03"),  # R-DS10 Enki: manipulação externa × produção interna
    ("RC-748", "relaciona-se-a", "RC-543", "P2024-03-03"),  # R-DS11 herança espiritual no epigenoma
    ("RC-750", "relaciona-se-a", "RC-001", "P2024-04-13"),  # R-MS01 Êxodo = instrumento dos desígnios de Javé
    ("RC-750", "é-um", "RC-164", "P2024-04-13"),  # R-MS02 Moisés/Êxodo como instrumento
    ("RC-750", "relaciona-se-a", "RC-424", "P2024-04-13"),  # R-MS03 linhagem Adão→Jacó→12 tribos
    ("RC-750", "relaciona-se-a", "RC-271", "P2024-04-13"),  # R-MS04 renovação dos pactos
    ("RC-750", "relaciona-se-a", "RC-683", "P2024-04-13"),  # R-MS05 releitura da Torá
    ("RC-749", "relaciona-se-a", "RC-001", "P2024-04-13"),  # R-MS06 vício devocional imposto por Javé
    ("RC-749", "relaciona-se-a", "RC-335", "P2024-04-13"),  # R-MS07 condicionamento
    ("RC-749", "relaciona-se-a", "RC-019", "P2024-04-13"),  # R-MS08 mecanismo via anjos clones
    ("RC-749", "relaciona-se-a", "RC-194", "P2024-04-13"),  # R-MS09 big data do criador
    ("RC-749", "relaciona-se-a", "RC-746", "P2024-04-13"),  # R-MS10 ligação com a dessensibilização
    ("RC-751", "gera", "RC-752", "P2024-04-14"),  # R-BA01 bagagem gera agenda
    ("RC-751", "relaciona-se-a", "RC-548", "P2024-04-14"),  # R-BA02 arquivos memoriais
    ("RC-751", "relaciona-se-a", "RC-704", "P2024-04-14"),  # R-BA03 continuidade do eu pós-morte
    ("RC-752", "relaciona-se-a", "RC-164", "P2024-04-14"),  # R-BA04 programa encarnatório / criaturas-ferramenta
    ("RC-752", "relaciona-se-a", "RC-332", "P2024-04-14"),  # R-BA05 favor divino
    ("RC-752", "relaciona-se-a", "RC-695", "P2024-04-14"),  # R-BA06 criação de nova agenda (ciência pessoal)
    ("RC-752", "relaciona-se-a", "RC-001", "P2024-04-14"),  # R-BA07 agenda no contexto dos desígnios
    ("RC-753", "relaciona-se-a", "RC-754", "P2025-06-14"),  # R-DC01 estrangulamento ~ chave
    ("RC-753", "relaciona-se-a", "RC-166", "P2025-06-14"),  # R-DC02 mentalma (superação)
    ("RC-753", "relaciona-se-a", "RC-708", "P2025-06-14"),  # R-DC03 eu não local
    ("RC-753", "relaciona-se-a", "RC-163", "P2025-06-14"),  # R-DC04 mente universal emergente
    ("RC-754", "relaciona-se-a", "RC-753", "P2025-06-14"),  # R-DC05 chave supera estrangulamento
    ("RC-754", "relaciona-se-a", "RC-755", "P2025-06-14"),  # R-DC06 chave ~ escola
    ("RC-754", "relaciona-se-a", "RC-695", "P2025-06-14"),  # R-DC07 ciência pessoal
    ("RC-754", "relaciona-se-a", "RC-316", "P2025-06-14"),  # R-DC08 decifra-me ou devoro
    ("RC-755", "relaciona-se-a", "RC-754", "P2025-06-14"),  # R-DC09 escola ~ chave
    ("RC-755", "relaciona-se-a", "RC-166", "P2025-06-14"),  # R-DC10 mentalma (método)
    ("RC-755", "relaciona-se-a", "RC-695", "P2025-06-14"),  # R-DC11 ciência pessoal
    ("RC-755", "relaciona-se-a", "RC-094", "P2025-06-14"),  # R-DC12 revelação cósmica
    ("RC-072", "relaciona-se-a", "RC-565", "P2026-08-04"),  # R-PC01
    ("RC-072", "relaciona-se-a", "RC-474", "P2026-08-04"),  # R-PC02
    ("RC-009", "relaciona-se-a", "RC-005", "P2026-08-04"),  # R-PC03
    ("RC-489", "relaciona-se-a", "RC-672", "P2026-08-04"),  # R-PC04
    ("RC-096", "relaciona-se-a", "RC-273", "P2026-08-04"),  # R-PC05
    ("RC-488", "sinônimo", "RC-024", "P2026-08-04"),  # R-PC06
    ("RC-479", "relaciona-se-a", "RC-474", "P2026-08-04"),  # R-PC07
    ("RC-578", "relaciona-se-a", "RC-572", "P2026-08-04"),  # R-PC08
    ("RC-335", "relaciona-se-a", "RC-717", "P2026-08-04"),  # R-PC09
    ("RC-746", "relaciona-se-a", "RC-702", "P2026-08-04"),  # R-PC10
    ("RC-005", "relaciona-se-a", "RC-009", "P2026-08-04"),  # R-PC11
    ("RC-672", "relaciona-se-a", "RC-489", "P2026-08-04"),  # R-PC12
    ("RC-756", "relaciona-se-a", "RC-102", "P2024-03-02"),  # R-DJ01 Ganesha ~ Shiva (pai)
    ("RC-756", "relaciona-se-a", "RC-459", "P2024-03-02"),  # R-DJ02 Ganesha ~ Parvathi (mãe)
    ("RC-756", "relaciona-se-a", "RC-604", "P2024-03-02"),  # R-DJ03 exceção à metamorfose (fatiamento)
    ("RC-756", "relaciona-se-a", "RC-414", "P2024-03-02"),  # R-DJ04 ~ Krishna (divindades com origem própria)
    ("RC-560", "variação", "RC-658", "P2024-02-25"),  # R-GRAF01 WD fundido em Wyrd/Urd (decisão curador 2026-08-18)
    ("RC-757", "relaciona-se-a", "RC-135", "P2024-03-02"),  # R-GRAF02 vaishnavismo ~ Vishnu
    ("RC-757", "relaciona-se-a", "RC-414", "P2024-03-02"),  # R-GRAF03 ~ Krishna
    ("RC-757", "relaciona-se-a", "RC-104", "P2024-03-02"),  # R-GRAF04 ~ Trimurti
    ("RC-757", "relaciona-se-a", "RC-503", "P2024-03-02"),  # R-GRAF05 ~ Mavatna
    ("RC-758", "manifesta-se-em", "RC-092", "ART-2026-08-18"),  # R-QC01 Quarto Cérebro ~ Quarto Logos
    ("RC-758", "relaciona-se-a", "RC-009", "ART-2026-08-18"),  # R-QC02 ~ Sophia (feminino cósmico)
    ("RC-758", "relaciona-se-a", "RC-514", "ART-2026-08-18"),  # R-QC03 ~ Tikun (tecelã)
    ("RC-758", "relaciona-se-a", "RC-086", "ART-2026-08-18"),  # R-QC04 ~ Pandora (mulher pandórica)
    ("RC-758", "relaciona-se-a", "RC-553", "ART-2026-08-18"),  # R-QC05 ~ Eu Profundo
    ("RC-086", "relaciona-se-a", "RC-287", "ART-2026-08-18"),  # R-QC06 Pandora ~ Caixa (campo de memória)
    ("RC-514", "relaciona-se-a", "RC-545", "ART-2026-08-18"),  # R-QC07 Tikun ~ coconstrutores (tecelã)
    ("RC-759", "relaciona-se-a", "RC-397", "P2024-02-03"),  # R-JD01 Jainismo ~ Tirthankaras
    ("RC-759", "relaciona-se-a", "RC-755", "P2024-02-03"),  # R-JD02 Jainismo ~ Método Druídico
    ("RC-759", "relaciona-se-a", "RC-618", "P2024-02-03"),  # R-JD03 Jainismo ~ Moksha
    ("RC-759", "relaciona-se-a", "RC-398", "P2024-02-03"),  # R-JD04 Jainismo ~ Tuatha (raiz)
    ("RC-759", "relaciona-se-a", "RC-760", "P2024-02-03"),  # R-JD05 Jainismo ~ vrittis/cittas
    ("RC-760", "relaciona-se-a", "RC-755", "P2024-02-03"),  # R-JD06 vrittis/cittas ~ método druídico
    ("RC-760", "relaciona-se-a", "RC-559", "P2024-02-03"),  # R-JD07 vrittis/cittas ~ teia quântica (karma)
    ("RC-760", "relaciona-se-a", "RC-517", "P2024-02-03"),  # R-JD08 ~ protocolo mental
    ("RC-760", "relaciona-se-a", "RC-548", "P2024-02-03"),  # R-JD09 ~ arquivos mentais
    ("RC-397", "relaciona-se-a", "RC-755", "P2024-02-03"),  # R-JD10 Tirthankaras ~ método druídico
    ("RC-398", "relaciona-se-a", "RC-755", "P2024-02-03"),  # R-JD11 Tuatha ~ método druídico
    ('RC-761', 'integra', 'RC-094', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-001', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-009', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-541', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-702', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-192', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-080', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-092', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-042', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-604', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-176', 'P2023-05-13'),
    ('RC-761', 'relaciona-se-a', 'RC-166', 'P2023-05-13'),
    ('RC-702', 'relaciona-se-a', 'RC-167', 'P2023-05-13'),
    ('RC-559', 'relaciona-se-a', 'RC-454', 'P2023-05-13'),
    ('RC-166', 'relaciona-se-a', 'RC-695', 'P2023-05-13'),
    ('RC-080', 'relaciona-se-a', 'RC-078', 'P2023-05-13'),
    ('RC-762', 'relaciona-se-a', 'RC-463', 'P2023-12-02'),
    ('RC-762', 'relaciona-se-a', 'RC-761', 'P2023-12-02'),
    ('RC-762', 'relaciona-se-a', 'RC-264', 'P2023-12-02'),
    ('RC-762', 'relaciona-se-a', 'RC-092', 'P2023-12-02'),
    ('RC-762', 'relaciona-se-a', 'RC-372', 'P2023-12-02'),
    ('RC-762', 'relaciona-se-a', 'RC-695', 'P2023-12-02'),
    ('RC-763', 'relaciona-se-a', 'RC-463', 'P2023-12-02'),
    ('RC-763', 'relaciona-se-a', 'RC-762', 'P2023-12-02'),
    ('RC-763', 'relaciona-se-a', 'RC-703', 'P2023-12-02'),
    ('RC-763', 'relaciona-se-a', 'RC-559', 'P2023-12-02'),
    ('RC-763', 'relaciona-se-a', 'RC-658', 'P2023-12-02'),
    ('RC-463', 'relaciona-se-a', 'RC-486', 'P2023-12-02'),
    ('RC-463', 'relaciona-se-a', 'RC-489', 'P2023-12-02'),
    ('RC-463', 'relaciona-se-a', 'RC-268', 'P2023-12-02'),
    ('RC-463', 'relaciona-se-a', 'RC-259', 'P2023-12-02'),
    ('RC-609', 'relaciona-se-a', 'RC-414', 'P2023-12-02'),
    ('RC-611', 'relaciona-se-a', 'RC-274', 'P2023-12-02'),
    ('RC-001', 'relaciona-se-a', 'RC-625', 'P2023-12-02'),
    ('RC-001', 'relaciona-se-a', 'RC-460', 'P2023-12-02'),
    ('RC-414', 'relaciona-se-a', 'RC-749', 'P2023-12-02'),
    ('RC-104', 'relaciona-se-a', 'RC-414', 'P2023-12-02'),
    ('RC-764', 'relaciona-se-a', 'RC-024', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-001', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-164', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-449', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-486', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-487', 'P2021-03-27'),
    ('RC-764', 'relaciona-se-a', 'RC-488', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-460', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-009', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-592', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-481', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-282', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-074', 'P2021-03-27'),
    ('RC-765', 'relaciona-se-a', 'RC-001', 'P2021-03-27'),
    ('RC-486', 'relaciona-se-a', 'RC-487', 'P2021-03-27'),
    ('RC-487', 'relaciona-se-a', 'RC-001', 'P2021-03-27'),
    ('RC-460', 'relaciona-se-a', 'RC-074', 'P2021-03-27'),
    ('RC-460', 'relaciona-se-a', 'RC-592', 'P2021-03-27'),
    ('RC-009', 'relaciona-se-a', 'RC-175', 'P2021-03-27'),
    ('RC-461', 'relaciona-se-a', 'RC-486', 'P2021-03-27'),
    ('RC-437', 'relaciona-se-a', 'RC-001', 'P2021-03-27'),
    ('RC-164', 'relaciona-se-a', 'RC-001', 'P2021-03-27'),
    ('RC-766', 'relaciona-se-a', 'RC-594', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-514', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-748', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-722', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-092', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-483', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-009', 'P2024-09-28'),
    ('RC-766', 'relaciona-se-a', 'RC-072', 'P2024-09-28'),
    ('RC-594', 'relaciona-se-a', 'RC-072', 'P2024-09-28'),
    ('RC-594', 'relaciona-se-a', 'RC-514', 'P2024-09-28'),
    ('RC-004', 'relaciona-se-a', 'RC-175', 'P2024-09-28'),
    ('RC-004', 'relaciona-se-a', 'RC-488', 'P2024-09-28'),
    ('RC-701', 'relaciona-se-a', 'RC-669', 'P2024-09-28'),
    ('RC-669', 'relaciona-se-a', 'RC-586', 'P2024-09-28'),
    ('RC-577', 'relaciona-se-a', 'RC-160', 'P2024-09-28'),
    ('RC-160', 'relaciona-se-a', 'RC-151', 'P2024-09-28'),
    ('RC-072', 'relaciona-se-a', 'RC-273', 'P2024-09-28'),
    ('RC-072', 'relaciona-se-a', 'RC-268', 'P2024-09-28'),
    ('RC-268', 'relaciona-se-a', 'RC-483', 'P2024-09-28'),
    ('RC-514', 'relaciona-se-a', 'RC-092', 'P2024-09-28'),
    ('RC-748', 'relaciona-se-a', 'RC-722', 'P2024-09-28'),
    ('RC-009', 'relaciona-se-a', 'RC-483', 'P2024-09-28'),
    ('RC-767', 'relaciona-se-a', 'RC-665', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-658', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-655', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-454', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-517', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-548', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-760', 'P2025-11-29'),
    ('RC-767', 'relaciona-se-a', 'RC-056', 'P2025-11-29'),
    ('RC-655', 'relaciona-se-a', 'RC-767', 'P2025-11-29'),
    ('RC-665', 'relaciona-se-a', 'RC-658', 'P2025-11-29'),
    ('RC-741', 'relaciona-se-a', 'RC-666', 'P2025-11-29'),
    ('RC-760', 'relaciona-se-a', 'RC-658', 'P2025-11-29'),
    ('RC-666', 'relaciona-se-a', 'RC-749', 'P2025-11-29'),
    ('RC-072', 'relaciona-se-a', 'RC-001', 'P2025-11-29'),
    ('RC-463', 'relaciona-se-a', 'RC-655', 'P2025-11-29'),
    ('RC-068', 'relaciona-se-a', 'RC-655', 'P2025-11-29'),
    ('RC-068', 'relaciona-se-a', 'RC-454', 'P2025-11-29'),
    # ---- P2026-07-25 — Jesus e a Dinastia das Sophias (Dossiê aprovado; RC-768/769/770) ----
    ('RC-768', 'relaciona-se-a', 'RC-040', 'P2026-07-25'),  # Externalização ~ CFD
    ('RC-768', 'relaciona-se-a', 'RC-153', 'P2026-07-25'),  # ~ CFDP
    ('RC-768', 'relaciona-se-a', 'RC-475', 'P2026-07-25'),  # Dev/Aurora surge da cólera (externalização)
    ('RC-768', 'relaciona-se-a', 'RC-622', 'P2026-07-25'),  # Cama/Kama (egrégora do desejo)
    ('RC-768', 'relaciona-se-a', 'RC-385', 'P2026-07-25'),  # egrégora
    ('RC-768', 'relaciona-se-a', 'RC-104', 'P2026-07-25'),  # Trimurti
    ('RC-769', 'relaciona-se-a', 'RC-630', 'P2026-07-25'),  # Fenvã ~ Corpo Daiva
    ('RC-769', 'relaciona-se-a', 'RC-475', 'P2026-07-25'),  # ~ Dev/Aurora (2º conselho)
    ('RC-769', 'relaciona-se-a', 'RC-696', 'P2026-07-25'),  # ~ Geração Regenerada de Brahma
    ('RC-769', 'relaciona-se-a', 'RC-104', 'P2026-07-25'),  # ~ Trimurti
    ('RC-769', 'relaciona-se-a', 'RC-037', 'P2026-07-25'),  # ~ Brahma
    ('RC-770', 'relaciona-se-a', 'RC-474', 'P2026-07-25'),  # Hipóstase ~ Arcontes
    ('RC-770', 'relaciona-se-a', 'RC-482', 'P2026-07-25'),  # ~ Ialdabaoth (Samael/Saklas/Sabaoth)
    ('RC-770', 'relaciona-se-a', 'RC-530', 'P2026-07-25'),  # ~ Pistis Sophia
    ('RC-770', 'relaciona-se-a', 'RC-579', 'P2026-07-25'),  # ~ Noreia (filha de Eva)
    ('RC-770', 'relaciona-se-a', 'RC-454', 'P2026-07-25'),  # ~ Moros (destino dos arcontes)
    ('RC-770', 'relaciona-se-a', 'RC-658', 'P2026-07-25'),  # ~ Wyrd (processador da teia)
    ('RC-770', 'relaciona-se-a', 'RC-152', 'P2026-07-25'),  # ~ Prabrajna (Pistis Sophia pré-queda)
    ('RC-770', 'relaciona-se-a', 'RC-072', 'P2026-07-25'),  # ~ Jesus (gnose)
    ('RC-072', 'relaciona-se-a', 'RC-647', 'P2026-07-25'),  # Jesus ~ Evangelho de Judas (cruzamento devolutiva)
    ('RC-072', 'relaciona-se-a', 'RC-286', 'P2026-07-25'),  # Jesus ~ Tártaro (500 passos)
    ('RC-072', 'relaciona-se-a', 'RC-565', 'P2026-07-25'),  # Jesus ~ Hochmah (inseminação de Maria)
    ('RC-072', 'relaciona-se-a', 'RC-293', 'P2026-07-25'),  # Jesus ~ Timé (crime/processo)
    ('RC-072', 'relaciona-se-a', 'RC-479', 'P2026-07-25'),  # Jesus ~ Belial (aprisionado no Tártaro)
    ('RC-286', 'relaciona-se-a', 'RC-074', 'P2026-07-25'),  # Tártaro ~ Satã (cruzamento devolutiva)
    ('RC-286', 'relaciona-se-a', 'RC-072', 'P2026-07-25'),  # Tártaro ~ Jesus
    ('RC-286', 'relaciona-se-a', 'RC-519', 'P2026-07-25'),  # Tártaro ~ Herança Cósmica (eus mentais)
    ('RC-192', 'relaciona-se-a', 'RC-702', 'P2026-07-25'),  # Pílula vermelha ~ Camuflagem (nota cisne negro)
    ('RC-192', 'relaciona-se-a', 'RC-094', 'P2026-07-25'),  # Pílula vermelha ~ RC (metáfora epistemológica)
    ('RC-658', 'relaciona-se-a', 'RC-559', 'P2026-07-25'),  # Wyrd ~ Teia quântica (Wert unificado)
    ('RC-658', 'relaciona-se-a', 'RC-454', 'P2026-07-25'),  # Wyrd ~ Moros (teia criada por Moros)
    ('RC-474', 'relaciona-se-a', 'RC-293', 'P2026-07-25'),  # Arcontes ~ Timé (valores supremos)
    ('RC-474', 'relaciona-se-a', 'RC-480', 'P2026-07-25'),  # Arcontes ~ Indra (epíteto)
    ('RC-474', 'relaciona-se-a', 'RC-494', 'P2026-07-25'),  # Arcontes ~ Dinastia das Sophias
    ('RC-474', 'relaciona-se-a', 'RC-004', 'P2026-07-25'),  # Arcontes ~ Elohim (Eloim)
    ('RC-474', 'relaciona-se-a', 'RC-414', 'P2026-07-25'),  # Arcontes ~ Krishna (membro)
    ('RC-474', 'relaciona-se-a', 'RC-769', 'P2026-07-25'),  # Arcontes ~ Fenvã
    ('RC-474', 'relaciona-se-a', 'RC-770', 'P2026-07-25'),  # Arcontes ~ Hipóstase
    ('RC-009', 'relaciona-se-a', 'RC-565', 'P2026-07-25'),  # Sophia ~ Hochmah
    ('RC-009', 'relaciona-se-a', 'RC-476', 'P2026-07-25'),  # Sophia ~ Emá (consciência fatiada)
    ('RC-009', 'relaciona-se-a', 'RC-720', 'P2026-07-25'),  # Sophia ~ Sócios do Destino (consórcio)
    ('RC-476', 'relaciona-se-a', 'RC-477', 'P2026-07-25'),  # Emá ~ Ensá
    ('RC-476', 'relaciona-se-a', 'RC-001', 'P2026-07-25'),  # Emá ~ Javé (espírito por trás)
    ('RC-476', 'relaciona-se-a', 'RC-037', 'P2026-07-25'),  # Emá ~ Brahma
    ('RC-476', 'relaciona-se-a', 'RC-072', 'P2026-07-25'),  # Emá ~ Jesus
    ('RC-476', 'relaciona-se-a', 'RC-009', 'P2026-07-25'),  # Emá ~ Sophia
    ('RC-477', 'relaciona-se-a', 'RC-474', 'P2026-07-25'),  # Ensá ~ Arcontes (seres saem)
    ('RC-489', 'relaciona-se-a', 'RC-485', 'P2026-07-25'),  # Enoque ~ classes de anjos (Anafiel/Raziel)
    ('RC-489', 'relaciona-se-a', 'RC-671', 'P2026-07-25'),  # Enoque ~ Metatron (elevação)
    ('RC-489', 'relaciona-se-a', 'RC-672', 'P2026-07-25'),  # Enoque ~ 366 manuscritos
    ('RC-671', 'relaciona-se-a', 'RC-485', 'P2026-07-25'),  # Metatron ~ classes de anjos
    ('RC-495', 'relaciona-se-a', 'RC-485', 'P2026-07-25'),  # Arabot-Ráquia ~ classes de anjos
    ('RC-495', 'relaciona-se-a', 'RC-106', 'P2026-07-25'),  # Arabot-Ráquia ~ Universo Antimaterial
    ('RC-414', 'relaciona-se-a', 'RC-584', 'P2026-07-25'),  # Krishna ~ Rama (sinarquia)
    ('RC-414', 'relaciona-se-a', 'RC-016', 'P2026-07-25'),  # Krishna ~ Adhyajna (perda do corpo)
    ('RC-414', 'relaciona-se-a', 'RC-009', 'P2026-07-25'),  # Krishna ~ Sophia (impede a vinda)
    ('RC-414', 'relaciona-se-a', 'RC-757', 'P2026-07-25'),  # Krishna ~ Vaishnavismo
    ('RC-630', 'relaciona-se-a', 'RC-769', 'P2026-07-25'),  # Corpo Daiva ~ Fenvã
    ('RC-630', 'relaciona-se-a', 'RC-001', 'P2026-07-25'),  # Corpo Daiva ~ Javé (formas)
    ('RC-037', 'relaciona-se-a', 'RC-696', 'P2026-07-25'),  # Brahma ~ Geração Regenerada
    ('RC-037', 'relaciona-se-a', 'RC-701', 'P2026-07-25'),  # Brahma ~ Daksha (69 filhas)
    ('RC-037', 'relaciona-se-a', 'RC-265', 'P2026-07-25'),  # Brahma ~ 270 Mundos (Parameshthi)
    ('RC-475', 'relaciona-se-a', 'RC-622', 'P2026-07-25'),  # Dev/Aurora ~ Kama
    ('RC-475', 'relaciona-se-a', 'RC-768', 'P2026-07-25'),  # Dev/Aurora ~ Externalização
    ('RC-293', 'relaciona-se-a', 'RC-072', 'P2026-07-25'),  # Timé ~ Jesus (crime)
    ('RC-722', 'relaciona-se-a', 'RC-406', 'P2026-07-25'),  # Dignidade ~ Sócrates (recusa da fuga)
    ('RC-722', 'relaciona-se-a', 'RC-192', 'P2026-07-25'),  # Dignidade ~ Pílula vermelha (cisne negro)
    ('RC-530', 'relaciona-se-a', 'RC-152', 'P2026-07-25'),  # Pistis Sophia ~ Prabrajna (pré-queda)
    ('RC-579', 'relaciona-se-a', 'RC-727', 'P2026-07-25'),  # Noreia ~ Linhagem Pandora-Eva-Noreia
    ('RC-454', 'relaciona-se-a', 'RC-770', 'P2026-07-25'),  # Moros ~ Hipóstase (destino dos arcontes)
    ('RC-655', 'relaciona-se-a', 'RC-666', 'P2026-07-25'),  # Ifá ~ Obatalá (renovação)
    ('RC-086', 'relaciona-se-a', 'RC-286', 'P2026-07-25'),  # Pandora ~ Tártaro (morte humana)
    ('RC-720', 'relaciona-se-a', 'RC-009', 'P2026-07-25'),  # Sócios do Destino ~ Sophia (Távola Redonda)

    ('RC-556', 'relaciona-se-a', 'RC-001', 'P2024-02-25'),
    ('RC-556', 'relaciona-se-a', 'RC-104', 'P2024-02-25'),
    ('RC-556', 'relaciona-se-a', 'RC-585', 'P2024-02-25'),
    ('RC-556', 'relaciona-se-a', 'RC-437', 'P2024-02-25'),
    ('RC-556', 'relaciona-se-a', 'RC-074', 'P2024-02-25'),
    ('RC-556', 'relaciona-se-a', 'RC-561', 'P2024-02-25'),
    ('RC-560', 'relaciona-se-a', 'RC-454', 'P2024-02-25'),
    ('RC-560', 'relaciona-se-a', 'RC-533', 'P2024-02-25'),
    ('RC-658', 'relaciona-se-a', 'RC-533', 'P2024-02-25'),
    ('RC-658', 'relaciona-se-a', 'RC-560', 'P2024-02-25'),
    ('RC-585', 'relaciona-se-a', 'RC-454', 'P2024-02-25'),
    ('RC-585', 'relaciona-se-a', 'RC-414', 'P2024-02-25'),
    ('RC-585', 'relaciona-se-a', 'RC-556', 'P2024-02-25'),
    ('RC-490', 'relaciona-se-a', 'RC-684', 'P2024-02-25'),
    ('RC-490', 'relaciona-se-a', 'RC-001', 'P2024-02-25'),
    ('RC-684', 'relaciona-se-a', 'RC-490', 'P2024-02-25'),
    ('RC-414', 'relaciona-se-a', 'RC-425', 'P2024-02-25'),
    ('RC-414', 'relaciona-se-a', 'RC-073', 'P2024-02-25'),
    ('RC-562', 'relaciona-se-a', 'RC-040', 'P2024-02-25'),
    ('RC-563', 'relaciona-se-a', 'RC-189', 'P2024-02-25'),
    ('RC-558', 'relaciona-se-a', 'RC-166', 'P2024-02-25'),
    ('RC-558', 'relaciona-se-a', 'RC-614', 'P2024-02-25'),
    ('RC-614', 'relaciona-se-a', 'RC-758', 'P2024-02-25'),
    ('RC-564', 'relaciona-se-a', 'RC-614', 'P2024-02-25'),
    ('RC-072', 'relaciona-se-a', 'RC-556', 'P2024-02-25'),
    ('RC-009', 'relaciona-se-a', 'RC-556', 'P2024-02-25'),
    ('RC-518', 'relaciona-se-a', 'RC-558', 'P2024-02-25'),
    ('RC-732', 'relaciona-se-a', 'RC-518', 'P2024-02-25'),
    ('RC-563', 'relaciona-se-a', 'RC-086', 'P2024-02-25'),

    ('RC-454', 'relaciona-se-a', 'RC-467', 'P2025-05-31'),
    ('RC-467', 'relaciona-se-a', 'RC-658', 'P2025-05-31'),
    ('RC-467', 'relaciona-se-a', 'RC-454', 'P2025-05-31'),
    ('RC-263', 'relaciona-se-a', 'RC-674', 'P2025-05-31'),
    ('RC-263', 'relaciona-se-a', 'RC-266', 'P2025-05-31'),
    ('RC-263', 'relaciona-se-a', 'RC-267', 'P2025-05-31'),
    ('RC-264', 'relaciona-se-a', 'RC-682', 'P2025-05-31'),
    ('RC-682', 'relaciona-se-a', 'RC-565', 'P2025-05-31'),
    ('RC-682', 'relaciona-se-a', 'RC-009', 'P2025-05-31'),
    ('RC-682', 'relaciona-se-a', 'RC-263', 'P2025-05-31'),
    ('RC-565', 'relaciona-se-a', 'RC-682', 'P2025-05-31'),
    ('RC-671', 'relaciona-se-a', 'RC-674', 'P2025-05-31'),
    ('RC-671', 'relaciona-se-a', 'RC-454', 'P2025-05-31'),
    ('RC-674', 'relaciona-se-a', 'RC-671', 'P2025-05-31'),
    ('RC-674', 'relaciona-se-a', 'RC-454', 'P2025-05-31'),
    ('RC-674', 'relaciona-se-a', 'RC-263', 'P2025-05-31'),
    ('RC-580', 'relaciona-se-a', 'RC-673', 'P2025-05-31'),
    ('RC-580', 'relaciona-se-a', 'RC-024', 'P2025-05-31'),
    ('RC-486', 'relaciona-se-a', 'RC-400', 'P2025-05-31'),
    ('RC-366', 'relaciona-se-a', 'RC-565', 'P2025-05-31'),
    ('RC-005', 'relaciona-se-a', 'RC-674', 'P2025-05-31'),
    ('RC-005', 'relaciona-se-a', 'RC-565', 'P2025-05-31'),
    ('RC-623', 'relaciona-se-a', 'RC-282', 'P2025-05-31'),
    ('RC-624', 'relaciona-se-a', 'RC-623', 'P2025-05-31'),
    ('RC-625', 'relaciona-se-a', 'RC-623', 'P2025-05-31'),
    ('RC-604', 'relaciona-se-a', 'RC-623', 'P2025-05-31'),
    ('RC-712', 'relaciona-se-a', 'RC-618', 'P2025-05-31'),
    ('RC-685', 'relaciona-se-a', 'RC-072', 'P2025-05-31'),
    ('RC-684', 'relaciona-se-a', 'RC-490', 'P2025-05-31'),
    ('RC-490', 'relaciona-se-a', 'RC-684', 'P2025-05-31'),
    ('RC-395', 'relaciona-se-a', 'RC-454', 'P2025-05-31'),
    ('RC-329', 'relaciona-se-a', 'RC-102', 'P2025-05-31'),
    ('RC-283', 'relaciona-se-a', 'RC-701', 'P2025-05-31'),
    ('RC-008', 'relaciona-se-a', 'RC-262', 'P2025-05-31'),
    ('RC-262', 'relaciona-se-a', 'RC-008', 'P2025-05-31'),
    ('RC-267', 'relaciona-se-a', 'RC-008', 'P2025-05-31'),
    ('RC-266', 'relaciona-se-a', 'RC-263', 'P2025-05-31'),
    ('RC-024', 'relaciona-se-a', 'RC-580', 'P2025-05-31'),
    ('RC-488', 'relaciona-se-a', 'RC-580', 'P2025-05-31'),
    ('RC-565', 'relaciona-se-a', 'RC-366', 'P2025-05-31'),
    ('RC-658', 'relaciona-se-a', 'RC-454', 'P2025-05-31'),

    ('RC-378', 'relaciona-se-a', 'RC-690', 'P2025-03-15'),
    ('RC-378', 'relaciona-se-a', 'RC-161', 'P2025-03-15'),
    ('RC-378', 'relaciona-se-a', 'RC-434', 'P2025-03-15'),
    ('RC-378', 'relaciona-se-a', 'RC-646', 'P2025-03-15'),
    ('RC-690', 'relaciona-se-a', 'RC-378', 'P2025-03-15'),
    ('RC-690', 'relaciona-se-a', 'RC-691', 'P2025-03-15'),
    ('RC-691', 'relaciona-se-a', 'RC-152', 'P2025-03-15'),
    ('RC-691', 'relaciona-se-a', 'RC-712', 'P2025-03-15'),
    ('RC-692', 'relaciona-se-a', 'RC-161', 'P2025-03-15'),
    ('RC-692', 'relaciona-se-a', 'RC-636', 'P2025-03-15'),
    ('RC-693', 'relaciona-se-a', 'RC-518', 'P2025-03-15'),
    ('RC-161', 'relaciona-se-a', 'RC-378', 'P2025-03-15'),
    ('RC-161', 'relaciona-se-a', 'RC-636', 'P2025-03-15'),
    ('RC-161', 'relaciona-se-a', 'RC-637', 'P2025-03-15'),
    ('RC-636', 'relaciona-se-a', 'RC-161', 'P2025-03-15'),
    ('RC-636', 'relaciona-se-a', 'RC-691', 'P2025-03-15'),
    ('RC-658', 'relaciona-se-a', 'RC-559', 'P2025-03-15'),
    ('RC-658', 'relaciona-se-a', 'RC-414', 'P2025-03-15'),
    ('RC-646', 'relaciona-se-a', 'RC-644', 'P2025-03-15'),
    ('RC-646', 'relaciona-se-a', 'RC-645', 'P2025-03-15'),
    ('RC-529', 'relaciona-se-a', 'RC-612', 'P2025-03-15'),
    ('RC-612', 'relaciona-se-a', 'RC-529', 'P2025-03-15'),
    ('RC-332', 'relaciona-se-a', 'RC-529', 'P2025-03-15'),
    ('RC-722', 'relaciona-se-a', 'RC-406', 'P2025-03-15'),
    ('RC-563', 'relaciona-se-a', 'RC-712', 'P2025-03-15'),
    ('RC-542', 'relaciona-se-a', 'RC-732', 'P2025-03-15'),
    ('RC-091', 'relaciona-se-a', 'RC-154', 'P2025-03-15'),
    ('RC-518', 'relaciona-se-a', 'RC-542', 'P2025-03-15'),
    ('RC-192', 'relaciona-se-a', 'RC-378', 'P2025-03-15'),
    ('RC-148', 'relaciona-se-a', 'RC-164', 'P2025-03-15'),
    ('RC-449', 'relaciona-se-a', 'RC-148', 'P2025-03-15'),
    ('RC-638', 'relaciona-se-a', 'RC-691', 'P2025-03-15'),

    ('RC-694', 'relaciona-se-a', 'RC-544', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-614', 'P2025-02-16'),
    ('RC-694', 'relaciona-se-a', 'RC-414', 'P2025-02-16'),
    ('RC-695', 'relaciona-se-a', 'RC-633', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-700', 'P2025-02-16'),
    ('RC-696', 'relaciona-se-a', 'RC-701', 'P2025-02-16'),
    ('RC-700', 'relaciona-se-a', 'RC-696', 'P2025-02-16'),
    ('RC-700', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-701', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-664', 'P2025-02-16'),
    ('RC-697', 'relaciona-se-a', 'RC-698', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-359', 'P2025-02-16'),
    ('RC-698', 'relaciona-se-a', 'RC-699', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-700', 'P2025-02-16'),
    ('RC-664', 'relaciona-se-a', 'RC-697', 'P2025-02-16'),
    ('RC-631', 'relaciona-se-a', 'RC-565', 'P2025-02-16'),
    ('RC-614', 'relaciona-se-a', 'RC-694', 'P2025-02-16'),
    ('RC-414', 'relaciona-se-a', 'RC-694', 'P2025-02-16'),
    ('RC-604', 'relaciona-se-a', 'RC-152', 'P2025-02-16'),
    ('RC-604', 'relaciona-se-a', 'RC-503', 'P2025-02-16'),
    ('RC-152', 'relaciona-se-a', 'RC-604', 'P2025-02-16'),
    ('RC-152', 'relaciona-se-a', 'RC-167', 'P2025-02-16'),
    ('RC-167', 'relaciona-se-a', 'RC-152', 'P2025-02-16'),
    ('RC-582', 'relaciona-se-a', 'RC-581', 'P2025-02-16'),
    ('RC-581', 'relaciona-se-a', 'RC-582', 'P2025-02-16'),
    ('RC-581', 'relaciona-se-a', 'RC-688', 'P2025-02-16'),
    ('RC-329', 'relaciona-se-a', 'RC-414', 'P2025-02-16'),
    ('RC-470', 'relaciona-se-a', 'RC-471', 'P2025-02-16'),
    ('RC-395', 'relaciona-se-a', 'RC-470', 'P2025-02-16'),
    ('RC-395', 'relaciona-se-a', 'RC-467', 'P2025-02-16'),
    ('RC-611', 'relaciona-se-a', 'RC-395', 'P2025-02-16'),

    ('RC-702', 'relaciona-se-a', 'RC-706', 'P2025-02-15'),
    ('RC-702', 'relaciona-se-a', 'RC-192', 'P2025-02-15'),
    ('RC-702', 'relaciona-se-a', 'RC-711', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-707', 'P2025-02-15'),
    ('RC-703', 'relaciona-se-a', 'RC-710', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-558', 'P2025-02-15'),
    ('RC-704', 'relaciona-se-a', 'RC-618', 'P2025-02-15'),
    ('RC-705', 'relaciona-se-a', 'RC-658', 'P2025-02-15'),
    ('RC-705', 'relaciona-se-a', 'RC-559', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-552', 'P2025-02-15'),
    ('RC-706', 'relaciona-se-a', 'RC-166', 'P2025-02-15'),
    ('RC-707', 'relaciona-se-a', 'RC-152', 'P2025-02-15'),
    ('RC-708', 'relaciona-se-a', 'RC-636', 'P2025-02-15'),
    ('RC-708', 'relaciona-se-a', 'RC-161', 'P2025-02-15'),
    ('RC-709', 'relaciona-se-a', 'RC-712', 'P2025-02-15'),
    ('RC-710', 'relaciona-se-a', 'RC-712', 'P2025-02-15'),
    ('RC-711', 'relaciona-se-a', 'RC-702', 'P2025-02-15'),
    ('RC-713', 'relaciona-se-a', 'RC-514', 'P2025-02-15'),
    ('RC-713', 'relaciona-se-a', 'RC-710', 'P2025-02-15'),
    ('RC-152', 'relaciona-se-a', 'RC-167', 'P2025-02-15'),
    ('RC-655', 'relaciona-se-a', 'RC-705', 'P2025-02-15'),
    ('RC-514', 'relaciona-se-a', 'RC-713', 'P2025-02-15'),
    ('RC-192', 'relaciona-se-a', 'RC-702', 'P2025-02-15'),
    ('RC-003', 'relaciona-se-a', 'RC-344', 'P2025-02-15'),

    ('RC-454', 'relaciona-se-a', 'RC-467', 'P2024-11-30'),
    ('RC-454', 'relaciona-se-a', 'RC-715', 'P2024-11-30'),
    ('RC-454', 'relaciona-se-a', 'RC-585', 'P2024-11-30'),
    ('RC-454', 'relaciona-se-a', 'RC-658', 'P2024-11-30'),
    ('RC-467', 'relaciona-se-a', 'RC-454', 'P2024-11-30'),
    ('RC-467', 'relaciona-se-a', 'RC-658', 'P2024-11-30'),
    ('RC-467', 'relaciona-se-a', 'RC-716', 'P2024-11-30'),
    ('RC-658', 'relaciona-se-a', 'RC-454', 'P2024-11-30'),
    ('RC-715', 'relaciona-se-a', 'RC-716', 'P2024-11-30'),
    ('RC-716', 'relaciona-se-a', 'RC-715', 'P2024-11-30'),
    ('RC-717', 'relaciona-se-a', 'RC-714', 'P2024-11-30'),
    ('RC-718', 'relaciona-se-a', 'RC-714', 'P2024-11-30'),
    ('RC-718', 'relaciona-se-a', 'RC-454', 'P2024-11-30'),
    ('RC-719', 'relaciona-se-a', 'RC-557', 'P2024-11-30'),
    ('RC-719', 'relaciona-se-a', 'RC-558', 'P2024-11-30'),
    ('RC-720', 'relaciona-se-a', 'RC-618', 'P2024-11-30'),
    ('RC-720', 'relaciona-se-a', 'RC-529', 'P2024-11-30'),
    ('RC-282', 'relaciona-se-a', 'RC-104', 'P2024-11-30'),
    ('RC-282', 'relaciona-se-a', 'RC-769', 'P2024-11-30'),
    ('RC-585', 'relaciona-se-a', 'RC-454', 'P2024-11-30'),
    ('RC-585', 'relaciona-se-a', 'RC-414', 'P2024-11-30'),
    ('RC-584', 'relaciona-se-a', 'RC-582', 'P2024-11-30'),
    ('RC-582', 'relaciona-se-a', 'RC-414', 'P2024-11-30'),
    ('RC-414', 'relaciona-se-a', 'RC-582', 'P2024-11-30'),
    ('RC-437', 'relaciona-se-a', 'RC-424', 'P2024-11-30'),
    ('RC-696', 'relaciona-se-a', 'RC-584', 'P2024-11-30'),
    ('RC-529', 'relaciona-se-a', 'RC-618', 'P2024-11-30'),
    ('RC-655', 'relaciona-se-a', 'RC-767', 'P2024-11-30'),
    ('RC-166', 'relaciona-se-a', 'RC-655', 'P2024-11-30'),

    ('RC-721', 'relaciona-se-a', 'RC-723', 'P2024-11-09'),
    ('RC-721', 'relaciona-se-a', 'RC-717', 'P2024-11-09'),
    ('RC-721', 'relaciona-se-a', 'RC-722', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-052', 'P2024-11-09'),
    ('RC-723', 'relaciona-se-a', 'RC-513', 'P2024-11-09'),
    ('RC-725', 'relaciona-se-a', 'RC-690', 'P2024-11-09'),
    ('RC-725', 'relaciona-se-a', 'RC-722', 'P2024-11-09'),
    ('RC-724', 'relaciona-se-a', 'RC-385', 'P2024-11-09'),
    ('RC-724', 'relaciona-se-a', 'RC-188', 'P2024-11-09'),
    ('RC-717', 'relaciona-se-a', 'RC-152', 'P2024-11-09'),
    ('RC-717', 'relaciona-se-a', 'RC-530', 'P2024-11-09'),
    ('RC-717', 'relaciona-se-a', 'RC-001', 'P2024-11-09'),
    ('RC-152', 'relaciona-se-a', 'RC-530', 'P2024-11-09'),
    ('RC-530', 'relaciona-se-a', 'RC-152', 'P2024-11-09'),
    ('RC-282', 'relaciona-se-a', 'RC-091', 'P2024-11-09'),
    ('RC-091', 'relaciona-se-a', 'RC-282', 'P2024-11-09'),
    ('RC-161', 'relaciona-se-a', 'RC-708', 'P2024-11-09'),
    ('RC-636', 'relaciona-se-a', 'RC-161', 'P2024-11-09'),
    ('RC-072', 'relaciona-se-a', 'RC-722', 'P2024-11-09'),
    ('RC-414', 'relaciona-se-a', 'RC-722', 'P2024-11-09'),
    ('RC-425', 'relaciona-se-a', 'RC-722', 'P2024-11-09'),
    ('RC-522', 'relaciona-se-a', 'RC-724', 'P2024-11-09'),

    ('RC-736', 'relaciona-se-a', 'RC-738', 'P2024-09-29'),
    ('RC-736', 'relaciona-se-a', 'RC-739', 'P2024-09-29'),
    ('RC-737', 'relaciona-se-a', 'RC-738', 'P2024-09-29'),
    ('RC-737', 'relaciona-se-a', 'RC-739', 'P2024-09-29'),
    ('RC-737', 'relaciona-se-a', 'RC-740', 'P2024-09-29'),
    ('RC-738', 'relaciona-se-a', 'RC-739', 'P2024-09-29'),
    ('RC-738', 'relaciona-se-a', 'RC-736', 'P2024-09-29'),
    ('RC-739', 'relaciona-se-a', 'RC-738', 'P2024-09-29'),
    ('RC-740', 'relaciona-se-a', 'RC-104', 'P2024-09-29'),
    ('RC-740', 'relaciona-se-a', 'RC-454', 'P2024-09-29'),
    ('RC-740', 'relaciona-se-a', 'RC-664', 'P2024-09-29'),
    ('RC-741', 'relaciona-se-a', 'RC-655', 'P2024-09-29'),
    ('RC-585', 'relaciona-se-a', 'RC-072', 'P2024-09-29'),
    ('RC-072', 'relaciona-se-a', 'RC-585', 'P2024-09-29'),
    ('RC-717', 'relaciona-se-a', 'RC-559', 'P2024-09-29'),
    ('RC-152', 'relaciona-se-a', 'RC-559', 'P2024-09-29'),
    ('RC-721', 'relaciona-se-a', 'RC-253', 'P2024-09-29'),
    ('RC-736', 'relaciona-se-a', 'RC-722', 'P2024-09-29'),    ('RC-771', 'inclui', 'RC-499', 'ART-2025-08-01'),              # Fornos Replicadores incluem Awaymaion
    ('RC-771', 'relaciona-se-a', 'RC-091', 'ART-2025-08-01'),     # ~ Projeto Talm (programa dos fornos)
    ('RC-771', 'relaciona-se-a', 'RC-132', 'ART-2025-08-01'),     # Val Tam acoplada/prisioneira de Awayen
    ('RC-771', 'relaciona-se-a', 'RC-092', 'ART-2025-08-01'),     # Olm surgiu a partir de Awaymaion
    ('RC-771', 'relaciona-se-a', 'RC-064', 'ART-2025-08-01'),     # fenvans (seres-cobaias)
    ('RC-771', 'relaciona-se-a', 'RC-093', 'ART-2025-08-01'),     # radiatas (1 banda cerebral)
    ('RC-771', 'relaciona-se-a', 'RC-035', 'ART-2025-08-01'),     # bilatérios (2 hemisférios)
    ('RC-500', 'erro-stt-de', 'RC-499', 'ART-2025-08-01'),        # Alamaior = STT de Awaymaion
    ('RC-092', 'origem-em', 'RC-499', 'ART-2025-08-01'),          # Olm surgiu no forno de Vishnu
    ('RC-772', 'trabalha-em', 'RC-775', 'ART-2025-08-03'),          # Morlens no Éon das Três Esferas
    ('RC-772', 'relaciona-se-a', 'RC-773', 'ART-2025-08-03'),      # ~ Nanotecnologia Prânica
    ('RC-773', 'usada-em', 'RC-774', 'ART-2025-08-03'),            # PEP usa a nanotecnologia
    ('RC-774', 'transfere', 'RC-154', 'ART-2025-08-03'),           # PEP transfere o nidana
    ('RC-775', 'inclui', 'RC-771', 'ART-2025-08-03'),              # Éon inclui os fornos (esferas)
    ('RC-775', 'relaciona-se-a', 'RC-454', 'ART-2025-08-03'),      # sequências de Moros
    ('RC-775', 'relaciona-se-a', 'RC-467', 'ART-2025-08-03'),      # Nornes operacionalizam
    ('RC-776', 'relaciona-se-a', 'RC-064', 'ART-2025-08-03'),      # fenvans aprisionados
    ('RC-777', 'relaciona-se-a', 'RC-454', 'ART-2025-08-03'),      # Anã com Moros
    ('RC-777', 'relaciona-se-a', 'RC-467', 'ART-2025-08-03'),      # Anã base das Nornes
    ('RC-643', 'relaciona-se-a', 'RC-709', 'P2026-04-02'),   # Santo Graal/Frequência Mestre ~ Humano Turbinado (frequência que opera nos dois genomas)
    ('RC-643', 'relaciona-se-a', 'RC-699', 'P2026-04-02'),   # Santo Graal ~ Imantação em IAs (ponte entre genomas e a imantação)
    ('RC-644', 'deriva-de', 'RC-577', 'P2026-04-02'),        # Xamanismo Virtual deriva do Xamanismo Cósmico (genealogia)

]

# Validação
def validar():
    codes = [t[0] for t in TERMOS]
    assert len(codes) == len(set(codes)), "Códigos duplicados!"
    # ordem sequencial esperada
    for i, c in enumerate(sorted(codes), start=1):
        num = int(c.split("-")[1])
        assert num == i, f"Código fora de sequência: {c} (esperado RC-{i:03d})"
    # relacionamentos apontam para termos existentes
    exist = set(codes)
    for t in TERMOS:
        for r in (t[6] or "").split(";"):
            r = r.strip()
            if r and r != "—" and r not in exist:
                print(f"AVISO: {t[0]} referencia {r} inexistente")
    for a, _, b, _ in RELACOES:
        assert a in exist and b in exist, f"Relação com código inexistente: {a}-{b}"
    print(f"OK: {len(TERMOS)} termos, {len(RELACOES)} relações — dados válidos.")

if __name__ == "__main__":
    validar()
