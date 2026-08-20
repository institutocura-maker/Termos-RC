#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "termos"

def ficha(cod, nome, cat, sub, status, definicao, ampliacao, citacao, rels, obs):
    L = [f"# {nome} — {cod}", "", "| Campo | Valor |", "|---|---|",
         f"| **Categoria Principal** | {cat} |", f"| **Subcategoria** | {sub} |",
         f"| **Status** | {status} |", "| **Última atualização** | 2026-08-19 |",
         "", "## Definição Sintética", "", definicao,
         "", "## Ampliação — P2025-05-31", "", ampliacao,
         "", "## Fontes", "", "| Fonte | Localização | Tipo |", "|---|---|---|",
         "| P2025-05-31 | O Mistério da Árvore da Vida e a Urdidura de Metatron (re-curadoria; devolutiva M-2/M-4 aprovada 19/08/2026) | palestra/STT pré-curada |",
         "", "## Citação-chave", "", f"> {citacao}", "", "## Termos Relacionados", "", "| Termo | Código | Relação |", "|---|---|---|"]
    for t, c in rels:
        L.append(f"| {t} | {c} | relaciona-se-a |")
    L += ["", "## Observações", "", obs, "", "---", ""]
    return "\n".join(L)

D = {}
D["RC-467-moiras-nornes-parcas-destino.md"] = ficha(
 "RC-467", "Moiras / Nornes / Parcas (destino)", "SERES & ENTIDADES", "1.8 Consciências coletivas / Logos", "🟡 Provisório",
 "As fiandeiras do destino na mitologia grega (Moiras), nórdica (Nornes) e romana (Parcas) — na leitura da RC, ligadas ao processador da teia do destino (Wyrd/Urd, RC-658).",
 "- **As três Norns na fala (P2025-05-31):** Orlog (Moros), pressionado, criou três seres: **Urd** (STT \"Urdre\") — o fluxo de informações do que aconteceu até aquele instante (passado); **Verdandi** (STT \"vivendre\") — processa o presente livre do passado; **Skuld** (STT \"scult\") — o que ainda não aconteceu, mas tinha que acontecer para complementar o passado pendente.\n- \"Como o passado pendente exige destino a ser cumprido, é por isso que o futuro já está escrito para quem tem problemas com o passado.\"\n- As Moiras/Nornes não têm noção de passado/presente/futuro como os humanos — é o conceito básico de compreensão desses seres.\n- **Absorção M-4 (devolutiva):** Urd/Verdandi/Skuld detalhadas aqui, cruzando firmemente com RC-658 (Wyrd).",
 "Orlog ficou tão pressionado que ele resolveu criar três seres: Urd, Verdandi e Skuld.",
 [("Wyrd/Urd", "RC-658"), ("Elm (Moros)", "RC-454"), ("Teia quântica", "RC-559")],
 "Quarentena mitológica — leitura do autor.")

D["RC-262-daath-a-criacao-na-cabala.md"] = ficha(
 "RC-262", "Daath (a Criação na Cabala)", "TERMOS ESPECÍFICOS", "8.2 Hebraico / Cabala", "🟡 Provisório",
 "Daath (Da'at) na Cabala: a sefirá oculta do conhecimento — na leitura da palestra, um conceito à parte da Otz Chim: Da'at significa incongruência — Da significa um abismo de luz (a luz que criou o que não devia, caiu onde não devia e ficou refém do próprio abismo).",
 "- **Na palestra (P2025-05-31):** na Otz Chim original da Cabala não é uma sefirá — Enoque apresentou a Shimon bar Yochai a Otz Chim com Da'at como um conceito à parte.\n- Da'at é o abismo onde essas 10 emanações atuam; só Assiah e Yetzirah são os dois mundos dentro do abismo.\n- Distorção judaica: os judeus mantiveram isso, só que mudaram a história (nacionalismo — Deus mergulhou por causa dos judeus).\n- Livro do autor: B013 Tzimtzum (o barulho quântico da queda ou do exílio forçado de uma divindade em sua própria criação).",
 "Existia uma luz que criou o que não devia, caiu onde não devia e por isso a sua luz se tornou refém do abismo que ela própria criou.",
 [("Sefirot/Árvore da Vida", "RC-263"), ("Tzimtzum", "RC-008"), ("Isaac Luria", "RC-267")],
 "Quarentena teológica (Cabala) — leitura do autor.")

D["RC-266-sepher-ha-zohar-e-shimon-bar-yochai.md"] = ficha(
 "RC-266", "Sepher ha-Zohar (e Shimon Bar Yochai)", "TERMOS ESPECÍFICOS", "8.2 Hebraico / Cabala", "🟡 Provisório",
 "O Zohar (Livro do Esplendor) é atribuído pela tradição ao rabino Shimon bar Yochai (séc. II d.C.) — na leitura da RC, o rabino teria recebido de Javé (via anjos) a Otz Chim e informações sobre a Cabalá.",
 "- **Na palestra (P2025-05-31):** no século 2 depois de Cristo, após a morte de Jesus, Javé (pé da vida se achando traído) deu ordens para a Cabalá ser criada; os anjos (com Metatron desativado) apareceram ao rabino Shimon bar Yochai (STT \"Shimon Bariokai/Yariosai\") e entregaram a Otz Chim e mais uma série de informações sobre a Cabalá; esse rabino agiu da forma mais séria possível e guardou; contraponto à derrota de Javé pela ressurreição de Jesus (e pelos livros via Maria Madalena).",
 "Javé precisava criar um sistema que servisse de contraponto à derrota dele pelo fato de Jesus ter ressuscitado.",
 [("Sefirot/Árvore da Vida", "RC-263"), ("Isaac Luria", "RC-267"), ("Javé", "RC-001")],
 "Quarentena teológica — leitura do autor; STT Bariokai normalizado.")

D["RC-267-isaac-luria-e-o-conceito-do-tzimtzum.md"] = ficha(
 "RC-267", "Isaac Luria e o conceito do Tzimtzum", "TERMOS ESPECÍFICOS", "8.2 Hebraico / Cabala", "🟡 Provisório",
 "Isaac Luria (séc. XVI, Safed) — cabalista que sistematizou o conceito do Tzimtzum (contração divina) e a Cabala lurianica.",
 "- **Na palestra (P2025-05-31):** séculos depois, Isaac Lúria, já na idade média europeia, resgatou isso (a Otz Chim) e outros rabinos e, com a melhor das intenções, criaram 100 interpretações e passaram a chamar isso de árvore da vida.\n- Tzimtzum distorcido: Isaac Lúria disse que é por isso que tem luz no abismo — o Deus que criou mergulhou no abismo por amor aos que estavam no abismo; Deus mergulhou por causa dos judeus (crítica do autor ao viés nacionalista); cabalistas profundos, porém descuidados.\n- Ver B013 (livro do autor sobre o Tzimtzum).",
 "Com a melhor das intenções criaram 100 interpretações e passaram a chamar isso de árvore da vida.",
 [("Tzimtzum", "RC-008"), ("Sepher ha-Zohar", "RC-266"), ("Sefirot/Árvore da Vida", "RC-263")],
 "Quarentena teológica — leitura do autor.")

D["RC-005-segundo-advento-do-cristo-volta-de-jesus.md"] = ficha(
 "RC-005", "Segundo Advento do Cristo (Volta de Jesus)", "EVENTOS & ERAS", "7.3 Profecias / Anúncios", "🟡 Provisório",
 "A promessa da volta de Jesus (Segunda Vinda) — na leitura da RC, ligada à profecia de Enoque e à vinda de Hochmah/Sophia (Malkuth) como suzerano.",
 "- **Na palestra (P2025-05-31):** promessa (via Enoque): eu vou morrer, vou ressuscitar, mas lá na frente eu volto de novo, não nascendo como ser humano, mas na minha personalidade celeste — todos os olhos da terra verão; nesse dia, o que foi profetizado pelo profeta Enoque terá total cumprimento.\n- E nós estamos vivendo os dias em que só falta o sétimo anjo tocar a sétima trombeta (B004 A Sétima Trombeta do Apocalipse); humor do autor: a torcida do Corinthians vai fazer gol... mas Sofia chega, é maluco.\n- A volta se dá na personalidade celeste (Hochmah/Sophia), não como nascimento humano.",
 "Todos os olhos da terra verão... Eu, como filho do homem, cercado pelas hostes angelicais.",
 [("Jesus", "RC-072"), ("Hochmah", "RC-565"), ("Sophia", "RC-009"), ("Urdidura de Metatron", "RC-674")],
 "Quarentena teológica — leitura do autor; ver B004.")

D["RC-329-kumari-kandan-tradicao.md"] = ficha(
 "RC-329", "Kumari Kandan (tradição)", "LOKAS & GEOGRAFIAS", "3.3 Localidades terrestres", "🟡 Provisório",
 "Kumari Kandam — o continente lemuriano do sul da Índia (tradição tâmil), citado na RC como o território onde Shiva estabeleceu seu quartel general.",
 "- **Na palestra (P2025-05-31):** antes do máximo glacial, há cerca de 23.000 anos, Shiva resolveu criar o seu quartel general na Terra para dominar a raça humana; existia um continente da Lemúria, continente de Mu, basicamente ligado ao continente hindu — a cultura que aí existia chama-se Kumari Kandam; expressões avatáricas Anahata/Pashupati [STT — REVISAR] comprovadas por registros arqueológicos de +20.000 anos; dravidianos (Mohenjo-Daro/Harapa) como povo de Shiva; a palavra Deus não existia (surgiu na Trácia, 4–5.000 anos).",
 "Quando esse processo começou, Shiva resolveu criar o seu quartel general na Terra para dominar a raça humana... e assim ele criou expressões avatáricas ou adhyajnas de si mesmo.",
 [("Shiva", "RC-102"), ("Nefilins", "RC-488")],
 "Quarentena cronológica/arqueológica — leitura do autor.")

D["RC-490-caim-leitura-rc-segundo-a-nascer.md"] = ficha(
 "RC-490", "Caim (leitura RC: segundo a nascer)", "SERES & ENTIDADES", "1.6 Figuras humanas (históricas/míticas)", "🟡 Provisório",
 "Na leitura da RC, Caim não foi o primogênito — Abel nasceu primeiro; Caim teria sido usado por Javé para anular a primogenitura de Abel.",
 "- **Na palestra (P2025-05-31):** o primeiro filho dele não foi Caim, foi Abel — a Bíblia diz que foi Caim, mas foi Abel; Javé covardemente criou uma confusão entre eles e os anjos de Javé levaram Caim a matar Abel; Caim exilado (não punido); Sete (3º filho) tornou-se o patriarca dos escolhidos; Enos (filho de Sete) o primeiro a louvar Javé.",
 "Javé covardemente criou uma confusão entre eles e os anjos de Javé levaram Caim a matar Abel.",
 [("Abel", "RC-684"), ("Enoque", "RC-489"), ("Adão", "RC-226")],
 "Quarentena teológica — leitura do autor sobre Gênesis.")

n = 0
for nome, conteudo in D.items():
    (P / nome).write_text(conteudo, encoding="utf-8")
    n += 1
print(f"fichas criadas: {n}")
