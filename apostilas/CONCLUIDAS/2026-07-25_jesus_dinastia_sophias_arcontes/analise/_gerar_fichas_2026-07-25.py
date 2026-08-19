#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria as fichas novas do ciclo P2026-07-25 (RC-768/769/770)
e fichas para termos centrais existentes sem ficha física."""
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "termos"

def ficha(cod, nome, cat, sub, status, definicao, secoes, citacao, relacionados, observacoes, fontes):
    L = []
    L.append(f"# {nome} — {cod}\n")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append(f"| **Categoria Principal** | {cat} |")
    L.append(f"| **Subcategoria** | {sub} |")
    L.append(f"| **Status** | {status} |")
    L.append("| **Última atualização** | 2026-08-19 |")
    L.append("\n## Definição Sintética\n")
    L.append(definicao + "\n")
    for titulo, corpo in secoes:
        L.append(f"## {titulo}\n")
        L.append(corpo + "\n")
    L.append("## Fontes\n")
    L.append("| Fonte | Localização | Tipo |")
    L.append("|---|---|---|")
    for f, loc, t in fontes:
        L.append(f"| {f} | {loc} | {t} |")
    if citacao:
        L.append("\n## Citação-chave\n")
        L.append(f"> {citacao}\n")
    L.append("## Termos Relacionados\n")
    L.append("| Termo | Código | Relação |")
    L.append("|---|---|---|")
    for t, c, r in relacionados:
        L.append(f"| {t} | {c} | {r} |")
    L.append("\n## Observações\n")
    L.append(observacoes + "\n")
    L.append("---\n")
    return "\n".join(L)

FONTES = [("P2026-07-25", "Jesus e a Dinastia das Sophias (Dossiê aprovado 19/08/2026)", "palestra/STT pré-curada")]

# ---------------- RC-768 ----------------
(P / "RC-768-principio-da-externalizacao.md").write_text(ficha(
 "RC-768", "Princípio da Externalização", "PROCESSOS & FENÔMENOS", "4.4 Fenômenos físicos / energéticos", "⚪ Candidato",
 "Mecanismo de criação dos seres do universo vizinho **sem o recurso da sexualidade**: o CFD (Código Fonte Definidor, RC-040) do ser, ao externalizar algo, dava vida a esse algo — um tipo de clonagem. Na leitura da palestra, é o \"princípio evolutivo mais importante desses seres antes de surgir a sexualidade\". Exemplos citados: a Deusa Dev/Aurora surgida da cólera de todos os deuses (RC-475); Cama/Kama como egrégora do desejo (RC-622); Atena saindo da coxa de Zeus. Nos tempos atuais, nenhum desses seres consegue mais idealizar o que gostaria de externalizar — o processo saiu do controle (entropia).",
 [],
 "\"O princípio da externalização é o princípio evolutivo mais importante desses seres antes de surgir a sexualidade. É assim que esses seres surgiram.\" — P2026-07-25",
 [("CFD", "RC-040", "relaciona-se-a"), ("CFDP", "RC-153", "relaciona-se-a"), ("Deva/Aurora", "RC-475", "relaciona-se-a"),
  ("Kama", "RC-622", "relaciona-se-a"), ("Egrégora", "RC-385", "relaciona-se-a"), ("Trimurti", "RC-104", "relaciona-se-a"),
  ("Corpos Fenvã", "RC-769", "relaciona-se-a")],
 "Leitura do autor sobre a dinâmica do universo antimaterial; a sexualidade como perda de controle da clonagem é tese da RC, não fato científico.",
 FONTES))

# ---------------- RC-769 ----------------
(P / "RC-769-corpos-fenva-terceira-forma-de-vida.md").write_text(ficha(
 "RC-769", "Corpos Fenvã", "SERES & ENTIDADES", "1.3 Extraterrestres / Raças cósmicas", "⚪ Candidato",
 "Terceira forma de vida do universo vizinho segundo a palestra: 1ª) corpos ígneos de plasma (anjos clones); 2ª) corpos daiva primitivos; 3ª) **corpos Fenvã** — \"daivas modernos com menos problemas\" (STT: \"menos problemas de Fose\" [REVISAR]). Corpos de plasma metamorfoseáveis do universo antimaterial, associados ao segundo conselho (Deusa Dev/Aurora e Cama/Kama) e à geração regenerada de Brahma (Brahma tetracéfalo em versão Fenvã).",
 [],
 "—",
 [("Corpo Daiva", "RC-630", "relaciona-se-a"), ("Deva/Aurora", "RC-475", "relaciona-se-a"), ("Geração Regenerada de Brahma", "RC-696", "relaciona-se-a"),
  ("Trimurti", "RC-104", "relaciona-se-a"), ("Brahma", "RC-037", "relaciona-se-a"), ("Princípio da Externalização", "RC-768", "relaciona-se-a")],
 "Grafia \"Fenvã\" provém de STT da palestra P2026-07-25; manter [REVISAR] até confirmação em fonte publicada (provável termo do autor em B068).",
 FONTES))

# ---------------- RC-770 ----------------
(P / "RC-770-hipostase-dos-arcontes.md").write_text(ficha(
 "RC-770", "Hipóstase dos Arcontes", "TECNOLOGIAS & ARTEFATOS", "5.4 Escrituras / Objetos documentais", "⚪ Candidato",
 "Livro gnóstico (séculos I–III d.C.), também chamado \"A Realidade dos Regentes\", considerado pelos estudiosos uma exegese gnóstica dos seis primeiros capítulos do Gênesis. Uma cópia em copta foi encontrada em 1945 na Biblioteca de Nag Hammadi. Apresentado como discurso de revelação entre um anjo (provavelmente Sophia, que produziu Jesus) e um interrogador. Para Ellam, é o livro que melhor descreve o conselho dos arcontes, com seus oito personagens principais: Samael/Saklas/Ialdabaoth/Sabaoth (= Javé); a mulher espiritual que estimula Adão e engana os soberanos; a águia mentora (a \"serpente\" do Éden); Noreia, filha de Eva; o anjo Eleleth, que revela a Noreia a origem e o destino do poder dos arcontes; Pistis Sophia (epíteto do criador antes da queda = Prabrajna); Moros (o único que sabe o destino dos arcontes); e a teia do destino (Wyrd/Moiras/Nornas).",
 [],
 "\"Os gnósticos cristãos podem e devem ter esperança... No fim, os arcontes perecerão, enquanto os humanos gnósticos [prevalecerão].\" — P2026-07-25 (leitura da Hipóstase)",
 [("Arcontes", "RC-474", "relaciona-se-a"), ("Ialdabaoth", "RC-482", "relaciona-se-a"), ("Pistis Sophia", "RC-530", "relaciona-se-a"),
  ("Noreia", "RC-579", "relaciona-se-a"), ("Elm (Moros)", "RC-454", "relaciona-se-a"), ("Wyrd/Urd", "RC-658", "relaciona-se-a"),
  ("Prabrajna", "RC-152", "relaciona-se-a"), ("Jesus", "RC-072", "relaciona-se-a")],
 "Conteúdo gnóstico sob quarentena teológica (Teologia Comparada/Crítica) — leitura do autor, não fato histórico validado.",
 FONTES))

# ---------------- RC-286 (existente, sem ficha) ----------------
(P / "RC-286-tartaro-eros-vishnu-tartaro-shiva.md").write_text(ficha(
 "RC-286", "Tártaro", "LOKAS & GEOGRAFIAS", "3.4 Regiões cósmicas / Portais", "🟡 Provisório",
 "Loca/morada do universo vizinho usada como prisão: abrigava os seres demoníacos derrotados nas guerras do universo antimaterial (titãs após a luta com Zeus/Cronos, por exemplo). A base registra a correspondência \"Eros = Vishnu / Tártaro = Shiva\" (RC-286). Na leitura da palestra P2026-07-25, o Tártaro ganhou nova função: o arconte Hades (\"Ades/Reides\", irmão de Zeus) passou a aprisionar ali os **eus mentais** dos humanos mortos (descendência de Adão vinculada ao DNA de Javé) — a \"tecnologia de aprisionamento\" que Jesus confrontou na cruz (os 500 passos).",
 [("## Ampliação — P2026-07-25 (Hades/Reides absorvido)", 
   "Devolutiva do curador (19/08/2026): o candidato **Hades/Reides** foi absorvido neste termo — dinâmicas de aprisionamento mental. Conteúdo: Hades (STT \"Ades/Reides/Reid/Reis\") = arconte dono do Tártaro, um dos irmãos de Zeus; para aumentar sua Timé, aprendeu a capturar o eu mental (\"a alma\") de humanos ao morrerem, desde Adão; criou um grupo de seres para isso; Javé depositara em Adão uma herança única (DNA), o que tornou toda a descendência aprisionável. Jesus, na cruz, invadiu o Tártaro (500 passos — Evangelho de Bartolomeu), aprisionou Hades e Belial e libertou os espíritos presos — ato tipificado como crime contra a Timé (processo aberto contra Jesus, sem resolução).")],
 "\"Eu dei 500 passos em direção ao inferno e, em chegando lá, libertei o inferno de Belial... e de o dono do inferno, que era Reides, o irmão de Zeus. Eu aprisionei os dois e soltei todas as almas de humanos que lá estavam.\" — P2026-07-25 (Jesus, segundo o Evangelho de Bartolomeu)",
 [("Satã", "RC-074", "relaciona-se-a"), ("Jesus", "RC-072", "relaciona-se-a"), ("Herança Cósmica", "RC-519", "relaciona-se-a"),
  ("Pandora", "RC-086", "relaciona-se-a")],
 "A leitura do Tártaro como prisão de eus mentais é tese da RC (quarentena teológica/ufológica). Cruzamento com RC-074 (Satã) aprovado na devolutiva.",
 FONTES))

# ---------------- RC-494 (existente, sem ficha) ----------------
(P / "RC-494-dinastia-das-sophias.md").write_text(ficha(
 "RC-494", "Dinastia das Sophias", "SERES & ENTIDADES", "1.2 Coletivos criadores", "🟡 Provisório",
 "Nome do terceiro conselho dos deuses na leitura da RC: a dinastia dos arcontes (\"Conselho dos 70\", \"Eloim\", \"Conselho dos Arcontes\", \"Dinastia das Sophias\" são faces do mesmo colegiado). Composta por consciências fatiadas dos espíritos Emá (En Ma) e Ensá; surgiu quando a humanidade emergiu (últimos ~25.000 anos; fixada em 70 membros nos últimos ~4.000 anos). Na palestra P2026-07-25: \"Sofia não é nome — é epíteto (personificação de um tipo de sabedoria)\"; cada arconte é dono de um clã humano (70 clãs desde a Torre de Babel); a dinastia está em crise terminal (universo vizinho colapsando, sem novos membros, alguns se retirando — \"dias contados\").",
 [("## Ampliação — P2026-07-25", 
   "- **Três conselhos** (esqueleto da palestra): 1º Trimurti (deuses primevos, ~4 bi anos) → 2º Dev/Aurora + Cama/Kama + descendência trimurtiana → 3º Dinastia das Sophias/70 arcontes (com os humanos).\n- **Função declarada:** manter o criador caído vivo (administrar o caos, retirar dele o que servir à reconstrução do eu de Javé).\n- **Lógica não humana:** nenhum membro pensa como humano; o único arconte humano legítimo rejeitado foi Jesus; Saibaba não quis entrar.\n- **Valores supremos:** ritos de passagem e Timé (RC-293).\n- **Crise:** colapso do universo vizinho; decisão recente atribuída a Krishna (\"desde a semana passada\"); fim da dinastia como transição (arcontes nascendo como humanos).")],
 "\"A nossa palestra é sobre o Eloim, o conselho dos arcontes ou o conselho das Sophias ou a dinastia das Sophias, porque são conceitos que significam a mesma coisa.\" — P2026-07-25",
 [("Arcontes", "RC-474", "relaciona-se-a"), ("Emá (En Ma)", "RC-476", "relaciona-se-a"), ("Ensá", "RC-477", "relaciona-se-a"),
  ("Timé", "RC-293", "relaciona-se-a"), ("Sophia", "RC-009", "relaciona-se-a"), ("Hipóstase dos Arcontes", "RC-770", "relaciona-se-a")],
 "B068 (O Funeral da Evidência) contém o capítulo \"A Dinastia das Sophias\" — base publicada relacionada. Termo central da palestra P2026-07-25.",
 FONTES))

# ---------------- RC-495 (existente, sem ficha) ----------------
(P / "RC-495-arabot-raquia-shekinah-merkabah.md").write_text(ficha(
 "RC-495", "Arabot-Ráquia", "LOKAS & GEOGRAFIAS", "3.2 Lokas / Mundos interiores", "🟡 Provisório",
 "Morada principal de Javé no Brahmaloka (universo antimaterial): uma loca com uma grande base laboratorial dentro da qual há uma pequena nave antimaterial que leva o eu/corpo de Javé ao mundo material. Edificada \"nos últimos tempos\" (~25.000 anos, segundo a palestra P2026-07-25), desde o último estado de coma de Javé (que ficava milhões de anos apagado, mantido pelos anjos clones).",
 [("## Ampliação — P2026-07-25 (Shekinah e Merkabah absorvidas)", 
   "Devolutiva do curador (19/08/2026): **Shekinah** e **Merkabah** absorvidas neste termo.\n- **Shekinah:** artefato/vestimento antimaterial (\"trono móvel\") que os seres do universo antimaterial usam para interagir com os humanos; o brilho da Shekinah de Javé era superior ao do sol (relato dos tempos de Adão — as famílias se sentavam no jardim do Éden vendo-a pousar sobre a árvore do conhecimento; quem a contemplava e saía ileso ficava imune a doenças); também descrita como nave antimaterial que unia o universo vizinho ao nosso. Relato pessoal do autor: encontro com a Shekinah num quarto de hotel em Pinheiros (SP), 2007 — \"meu filho, você precisa fazer um pacto comigo\".\n- **Merkabah:** artefato/veículo de deslocamento no âmbito do universo vizinho, usado por Javé quando investido da Shekinah; associada aos príncipes da Merkabah (RC-485) e aos salões descritos pelo rabino Ismael.")],
 "\"Chequiná nada mais é do que um artefato, vestimento, um adaptador antimaterial que os seres do universo antimaterial usam para interagir com os humanos... Mercabá seria um artefato que Javé, quando investido da sua chequiná, nele ele se desloca no âmbito do universo vizinho.\" — P2026-07-25",
 [("Classes de anjos de Arabot-Ráquia", "RC-485", "relaciona-se-a"), ("Universo Antimaterial", "RC-106", "relaciona-se-a"),
  ("Javé", "RC-001", "relaciona-se-a"), ("Enoque", "RC-489", "relaciona-se-a")],
 "Grafias STT: chequiná/chequar/chequá/chekinah (Shekinah); mercabá/merquebá (Merkabah). Relato Pinheiros 2007 = vivência pessoal do autor, não fato validado.",
 FONTES))

# ---------------- RC-482 (existente, sem ficha) ----------------
(P / "RC-482-ialdabaoth-jave-samael-saklas-sabaoth.md").write_text(ficha(
 "RC-482", "Ialdabaoth", "SERES & ENTIDADES", "1.1 Divindades / Criadores", "⚪ Candidato",
 "Epíteto gnóstico de Javé (o demiurgo): \"Samael, o soberano cego; Saklas, o ignorante; Ialdabaoth, o blasfemador contra o divino; Sabaoth\" — todos nomes do mesmo ser na leitura da RC (na Hipóstase dos Arcontes, RC-770). Na palestra P2026-07-25, o autor enumera esses epítetos ao apresentar os personagens do livro gnóstico.",
 [("## Ampliação — P2026-07-25", 
   "A palestra confirma e amplia os epítetos: Samael/Sáclas/Aldabaof/Sabaof (STT de Samael/Saklas/Ialdabaoth/Sabaoth) = os \"muitos nomes de Javé\" na Hipóstase dos Arcontes; Pistis Sophia é o epíteto do mesmo ser **antes** da queda (condição paradisíaca), enquanto Ialdabaoth é o ser reconstruído depois da queda (ver RC-530 e RC-152).")],
 "\"Samael, o soberano cego, também chamado de Sácala, o ignorante, e de Aldabaof, que é o blasfemador contra o divino, e de Sabaov... tudo isso é sinônimo pro nome de Javé.\" — P2026-07-25",
 [("Hipóstase dos Arcontes", "RC-770", "relaciona-se-a"), ("Javé", "RC-001", "relaciona-se-a"), ("Pistis Sophia", "RC-530", "relaciona-se-a"),
  ("Prabrajna", "RC-152", "relaciona-se-a")],
 "Grafias STT registradas: Aldabaof, Aldabaofelo, Sácala/Sáclas, Sabaov/Sabaof — normalizar para as canônicas (Ialdabaoth, Saklas, Sabaoth).",
 FONTES))

# ---------------- RC-479 (existente, sem ficha) ----------------
(P / "RC-479-belial-arconte-sata-do-livro-de-jo.md").write_text(ficha(
 "RC-479", "Belial", "SERES & ENTIDADES", "1.5 Decaídos / Exilados / Demônios", "🟡 Provisório",
 "Arconte do conselho (\"Satã\" no Livro de Jó): começou como anjo clone de Javé, tomou \"fórmulas de poder mental\" e transitou da condição de anjo para ser demoníaco (metamorfoseável) — um dos poucos a conseguir o trânsito; tornou-se arconte. Na leitura da RC, é o protagonista (com Javé) da aposta do Livro de Jó e um dos dois arcontes aprisionados por Jesus no Tártaro (junto com Hades/Reides).",
 [("## Ampliação — P2026-07-25", 
   "- Reuniões semanais do conselho (fuso horário terrestre) na época de Jó — a aposta Javé × Belial nasceu de um desses encontros.\n- Obra relacionada: **B080 Perversa Gratidão** (o autor: \"o penúltimo livro que eu lancei chama-se Perversa Gratidão. É sobre o livro de Jó\").\n- Aprisionado por Jesus nos 500 passos (Evangelho de Bartolomeu) — ver RC-072 e RC-286.\n- \"Belial, também chamado de Satã\" (STT da fala; cruzamento com RC-074 aprovado na devolutiva).")],
 "\"Esse ser chamado de Satã na Bíblia era Belial. Belial é um dos arcontes na época... Tinha assento nesse conselho chamado Elohim ou Eloim.\" — P2026-07-25",
 [("Satã", "RC-074", "relaciona-se-a"), ("Tártaro", "RC-286", "relaciona-se-a"), ("Jesus", "RC-072", "relaciona-se-a"),
  ("Arcontes", "RC-474", "relaciona-se-a")],
 "Quarentena teológica: leitura da RC sobre o Livro de Jó; a correspondência Belial=Satã é do autor.",
 FONTES))

# ---------------- RC-565 (existente, sem ficha) ----------------
(P / "RC-565-hochmah-2a-sefirah-sabedoria-sophia.md").write_text(ficha(
 "RC-565", "Hochmah", "TERMOS ESPECÍFICOS", "8.2 Hebraico / Cabala", "🟡 Provisório",
 "Grafia canônica para a 2ª Sefirah (Sabedoria) da Cabala, epíteto hebraico de Sophia (RC-009). Decisão canônica do curador: **Hochmah**, nunca \"Rockman/Rockma\" (veto estrito).",
 [("## Ampliação — P2026-07-25", 
   "Na palestra, o ser que inseminou Maria para gerar Jesus aparece em variações STT: **Rockma / Rockman / Hotman / Hman / Shockma** — todas normalizadas para **Hochmah** (ou Sophia) na edição, com nota na primeira ocorrência. Conteúdo: \"Jesus nasceu via uma humana, Maria, mas via uma inseminação artificial em Maria feita por um ser chamado Rockma ou Sofia\"; \"Sofia aparece como sendo o espírito ou tutor de Pistis na criação como Vishnu ou Shockma\" — Hochmah/Sophia como agente da inseminação (ver RC-072 e RC-009).")],
 "\"Jesus nasceu como via uma humana Maria, mas via uma inseminação artificial em Maria feita por um ser chamado Rockma ou Sofia.\" — P2026-07-25 [STT normalizado: Hochmah/Sophia]",
 [("Sophia", "RC-009", "relaciona-se-a"), ("Jesus", "RC-072", "relaciona-se-a"), ("Pistis Sophia", "RC-530", "relaciona-se-a")],
 "Fonemas \"Rockma/Rockman\" continuam na Colecionar Incertezas (não resolvem identidade sem áudio) — veto estrito do curador mantido.",
 FONTES))

# ---------------- RC-530 (existente, sem ficha) ----------------
(P / "RC-530-pistis-sophia-feminino-cosmico-gnostico.md").write_text(ficha(
 "RC-530", "Pistis Sophia", "SERES & ENTIDADES", "1.1 Divindades / Criadores", "🟡 Provisório",
 "Epíteto gnóstico do ser criador na sua condição paradisíaca, **antes da queda**: na leitura da RC, Pistis Sophia = o ser que a base registra como Prabrajna (RC-152); depois da queda, o mesmo ser se reconstruiu como o \"monstro\" Ialdabaoth/Javé (RC-482). Não é nome próprio — é \"um tipo de Sofia\".",
 [("## Ampliação — P2026-07-25", 
   "Na Hipóstase dos Arcontes (RC-770): \"Javé é Pistis Sophia... caída. Mas antes da queda, o ser que eu chamo de Prabrajna, nesse livro ele aparece com o nome de Pist Sophia, que não é nome, é um epíteto, é um tipo de Sofia — Pistis Sophia\". A palestra consolida a cadeia: Pistis Sophia (pré-queda) → Javé/Samael/Ialdabaoth (pós-queda).")],
 "\"Antes da queda, o ser que eu chamo de Prabrajna, nesse livro ele aparece com o nome de Pist Sophia.\" — P2026-07-25",
 [("Prabrajna", "RC-152", "relaciona-se-a"), ("Hipóstase dos Arcontes", "RC-770", "relaciona-se-a"), ("Ialdabaoth", "RC-482", "relaciona-se-a"),
  ("Sophia", "RC-009", "relaciona-se-a")],
 "Quarentena teológica (gnosticismo) — leitura do autor.",
 FONTES))

# ---------------- RC-485 (existente, sem ficha) ----------------
(P / "RC-485-classes-de-anjos-de-arabot-raquia.md").write_text(ficha(
 "RC-485", "Classes de anjos de Arabot-Ráquia", "SERES & ENTIDADES", "1.4 Anjos / Arcanjos / Querubins", "🟡 Provisório",
 "As diversas classes de anjos clones de Javé que povoam Arabot-Ráquia (RC-495): serafins flamejantes, querubins, ofanins, galgalim, chayot, chashmalim — \"os anjos de Javé não são de um só tipo\". Anjos são \"robôs\" de Javé (clones robotizados); ninguém aceita anjo sentado no conselho dos arcontes — só seres demoníacos.",
 [("## Ampliação — P2026-07-25", 
   "- **Príncipes da Merkabah:** arcontes da aristocracia em torno dos três grandes seres (equivalência com os 70 clãs: cada nação comandada por um príncipe).\n- **Anjos ministradores:** Uzza, Azza e Azael (STT \"Usá, Azá e Aziel\") — anjos com poder de não ser robotizados e de criar processos; acusaram Javé de ter criado a humanidade; resposta de Javé: \"Eu fiz e eu carrego, e eu carrego e eu livro\" (frase reproduzida pelo profeta Isaías).\n- **Anafiel e Raziel:** anjos que levaram Enoque em sua primeira ida a Arabot-Ráquia (\"todos os habitantes perceberam o cheiro dele mesmo à distância\").\n- **Rabino Ismael:** levado aos céus (época de Enoque/Metatron); descreve os seis salões + sétimo onde acampa a Shekinah; príncipes da Merkabah, serafins, águias da Merkabah, ofanins, galgalim, chayot, chananiim.\n- **Anjo \"Português\" [REVISAR]:** anjo responsável pela \"Ofiúsa\" (terra das serpentes, Galícia/norte da Espanha; rainha e rei serpentes — seres teriantrópicos); questionou a presença de Enoque-Metatron; STT provavelmente deformou o nome original. Desafiado por Javé (\"Quem é você para entrar e falar na minha presença?\").")],
 "\"Os anjos de Javé não são de um só tipo, é de vários tipos.\" — P2026-07-25",
 [("Arabot-Ráquia", "RC-495", "relaciona-se-a"), ("Enoque", "RC-489", "relaciona-se-a"), ("Metatron", "RC-671", "relaciona-se-a"),
  ("Javé", "RC-001", "relaciona-se-a")],
 "STT a normalizar com nota: Usá/Azá/Aziel (Uzza/Azza/Azael), mercabá (Merkabah), Rquia (Ráquia), chequar (Shekinah).",
 FONTES))

# ---------------- RC-477 (existente, sem ficha) ----------------
(P / "RC-477-ensa-espirito-primordial-companheiro-de-en-ma.md").write_text(ficha(
 "RC-477", "Ensá", "SERES & ENTIDADES", "1.8 Consciências coletivas / Logos", "🟡 Provisório",
 "Espírito primordial companheiro de En Ma (Emá, RC-476). Na leitura da RC, os 70 membros do conselho dos arcontes são consciências fatiadas de Emá **e de Ensá**; os seres de Ensá resolveram sair do conselho — Saibaba foi o penúltimo a sair (\"o último não, o penúltimo\"), recusando assento.",
 [("## Ampliação — P2026-07-25", 
   "\"Todos os 70 membros do conselho dos Arcontes hoje são consciências fatiadas de Emá e de Ensá, só que os seres de Ensá resolveram sair. E o último deles que foi Saibaba... o penúltimo, resolveu não... não se sentou.\" — A saída dos seres de Ensá como sinal do esvaziamento/fim da dinastia (ver RC-494).")],
 "\"Todos os 70 membros do conselho dos Arcontes hoje são consciências fatiadas de Emá e de Ensá.\" — P2026-07-25",
 [("En Ma (Emá)", "RC-476", "relaciona-se-a"), ("Arcontes", "RC-474", "relaciona-se-a"), ("Dinastia das Sophias", "RC-494", "relaciona-se-a")],
 "Relação com a figura de Sathya Sai Baba sob quarentena teológica (leitura do autor).",
 FONTES))

# ---------------- RC-480 (existente, sem ficha) ----------------
(P / "RC-480-indra-titulo-de-arconte.md").write_text(ficha(
 "RC-480", "Indra", "TERMOS ESPECÍFICOS", "8.1 Sânscrito / Hinduísmo", "🟡 Provisório",
 "Título/epíteto, não nome próprio: na leitura da RC, \"um Indra é um arconte\". Diversos Indras existiram ao longo da história; Zeus, ao se tornar rei dos deuses, tornou-se \"o último Indra\" (na mitologia ariana hindu). As referências a Indras nos Puranas, Upanishads e Mahabharata são referências aos arcontes.",
 [("## Ampliação — P2026-07-25", 
   "- Arcontes = Indras = Sophias (epítetos do mesmo conceito).\n- \"Zeus quando se tornou rei dos deuses, ele se tornou na mitologia ariana hindu um Indra.\"\n- Apolo e Ares (\"Áries\" no STT), arcontes mais novos, passaram a ter assento no conselho dos 70 desde que Zeus se tornou o mais novo Indra; cada assento aumentava a Timé do ser — motivo de guerras e perseguição aos humanos (\"Ó, Apolo, a sua timé é muito maior que a minha. Você tem que se livrar de pelo menos umas 50 personagens humanas...\").")],
 "\"Um Indra é um arconte, é um epíteto, não é nome próprio.\" — P2026-07-25",
 [("Arcontes", "RC-474", "relaciona-se-a"), ("Timé", "RC-293", "relaciona-se-a"), ("Zeus", "—", "relaciona-se-a")],
 "Zeus não possui código próprio na base (mitologia grega registrada em correspondências — ver RC-286).",
 FONTES))

# ---------------- RC-518 (existente, sem ficha) ----------------
(P / "RC-518-genoma-derivado-interacao-genoma-trajetoria.md").write_text(ficha(
 "RC-518", "Genoma Derivado", "PROCESSOS & FENÔMENOS", "4.1 Processos biológicos / genéticos", "🟡 Provisório",
 "Conceito da RC sobre a interação genoma × trajetória do eu. Na palestra P2026-07-25, o genoma humano é apresentado como \"a grande joia\" da criação de 13,8 bilhões de anos — não o corpo, mas **o que um eu faz do seu genoma**: a construção interior (padrões de genética pessoal, como Jesus e Sidarta Gautama) como preciosidade disputada pelos conselhos.",
 [("## Ampliação — P2026-07-25 (Genoma como Joia absorvido)", 
   "Devolutiva do curador (19/08/2026): \"Genoma Humano como Joia\" absorvido aqui (e em RC-732). Conteúdo: analogia ONU/conselho nuclear (quem domina a joia domina a criação e o criador caído); o eu humano como \"bomba atômica\" de dignidade; o conselho domina o DNA de quem não constrói poder sobre si mesmo. Quarentena científica: nada disso é genética validada — é leitura do autor.")],
 "\"Não é o ser humano que é a joia. É o que um eu de um ser humano faz do seu genoma.\" — P2026-07-25",
 [("Invasão Ancestral do Genoma", "RC-732", "relaciona-se-a"), ("DNA como Projeção Holográfica", "RC-217", "relaciona-se-a"),
  ("Genoma da Liberdade", "RC-619", "relaciona-se-a")],
 "Quarentena científica — leitura do autor.",
 FONTES))

print("Fichas criadas:", sorted(p.name for p in P.glob("RC-76*.md"))[:3], "+ existentes:", 
      len([p for p in P.glob("RC-*.md")]))
