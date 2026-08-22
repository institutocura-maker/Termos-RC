#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Correções de páginas em LEITURA-2 (rodada 3, fragmentos exatos)."""
F = 'livros/B019_nem-deus-nem-jave-nem-darwin/analise/LEITURA-2-TERMINOLOGICA.md'
linhas = open(F, encoding='utf-8').read().split('\n')

# (âncora da linha, fragmento antigo, fragmento novo) — ou (âncora, None, linha nova completa)
correcoes = [
("**RC-164 Criaturas-ferramenta**", "vêm como", "vivem como"),
("**RC-538 Consórcio de Mundos", "(p. 144/184/203):", "(pp. 144/155/165/184) e 'Consórcio de Mundos (Arquitetos Universais)' (p. 5, sinopse):"),
("**RC-540 Molécula-mãe", "(p. 145)", "(p. 146–149, cap. 13)"),
("**RC-547 Evolução Criativa", "ancorada na 'Causação Formativa' de Rupert Sheldrake\" (p. 163)", "ancorada na 'Causação Formativa' de Rupert Sheldrake\" (p. 95, cap. 8; 'Formação Causativa' em p. 105, cap. 10)"),
("**RC-547 Evolução Criativa", "Ampliar com a ancoragem em Sheldrake (p. 163)", "Ampliar com a ancoragem em Sheldrake (p. 95/105)"),
("**RC-152 Prabrajna**", "Prajapati**\" (p. 107);", "Prajapati**\" (p. 65, cap. 5);"),
("| \"Prabrajna — ou **Prajapati**\" |", "\"Prabrajna — ou **Prajapati**\" |", "\"Prabrajna — ou **Prajapati**\" (p. 65) |"),
("**RC-153 CFDP", "\"CFDP 'doentio'\" (p. 151)", "\"o 'CFD doentio' do Criador, o 'Grande Predador' de toda a história desta Criação (p. 151, cap. 13)\""),
("**RC-699 Imantação", "comecem a perecer\" (p. 170)", "comecem a perecer\" (p. 70, cap. 5; 'imantar' também em p. 139, 188 e 205)"),
("**RC-658 Wyrd/Urd**", "integrantes\" (p. 202) — verificar", "integrantes\" (p. 93, cap. 8) — verificar"),
("**RC-229 A Lógica de Javé", "fora da 'blindagem'\" (p. 172); \"a Lógica de Javé\" (p. 172–173) — cruzar", "fora da 'blindagem', esta Obra 'indevida' é apenas um 'Micro-padrão Mental colapsado'\" (p. 65, cap. 5) — ('a Lógica de Javé' não consta no livro) — cruzar"),
("**RC-622 Kama", "(p. 175/130)", "(p. 78, cap. 6)"),
("**RC-622 Kama", "primeira semente do pensamento'\" (p. 78, cap. 6) |", "primeira semente do pensamento'\" (p. 78, cap. 6); \"um Ser chamado pelo epíteto de 'Phanes' (avatar de Eros) ou 'Kama' (avatar de Vishnu) optou por criar o desejo para fazer emergir a confiança entre os seres\" (p. 88, cap. 8); \"a polaridade sexual teria sido gerada por Shiva e alguns de seus avatares\" (p. 88); \"Entre os animais biológicos, Shiva criou o sexo e Vishnu fez surgir o desejo sexual\" (p. 130, cap. 11) |"),
("**RC-091 Projeto Talm", "(p. 154) — **o B019 narra o MESMO evento do TALM com o nome \"Projeto Talm\" (cruzar RC-091 com p. 154!)**", "(p. 69, cap. 5) — **o B019 narra o MESMO evento do TALM com o nome \"Projeto Talm\" (cruzar RC-091 com p. 69!)**"),
("**RC-710 Genes Críticos", "(p. 224–229)", "(p. 152, cap. 13; cf. p. 181–184, cap. 15)"),
("**RC-708 Ser Humano Não Local", "(p. 229) — cruzar", "(p. 202, cap. 18) — cruzar"),
("| C1 |", "p. 17, 118, 214, 222", "p. 17, 83, 118, 222"),
("| C2 |", "p. 11, 123, 141, 200", "p. 11, 93, 123 ('ponte quântica'); 141 ('ponte vibratória'); 200 ('via quântica')"),
("| C4 |", "p. 19, 140, 198", "p. 67/78 ('Mente Cósmica'); p. 140 ('Mente Maior'/'Biocosmos Inteligente'); p. 221 (nota: tese de James Gardner)"),
("| C9 |", "| p. 107 | — |", "| p. 65 | — |"),
("| C34 |", "p. 12, 17, 181, 184", "'jogo da vida': p. 12, 52, 92, 139, 156, 206; 'jogo das mutações': p. 59, 65 (cap. 5)"),
("| \"Mavatna\"/\"Mavatma\" |", "| \"Mavatna\"/\"Mavatma\" |", "| \"Mavatna\" (pp. 66/67/68/113/114/198) × \"Mavatma\" (p. 70) |"),
("| \"Kundaline\" (p. 111) |", "(p. 111)", "(p. 112)"),
("| \"Tikum\" (pp. 114/199) |", "(pp. 114/199)", "(p. 114; 'tikun' correto em p. 199/204)"),
("| \"Consórcio Cósmico\" (p. 144/184) ×", "(p. 144/184)", "(pp. 144/155/165/184)"),
("| \"buraco branco\" (p. 17/118/214)", "(p. 17/118/214) × \"buraco mental branco\" (p. 121)", "(p. 17/83/118/222) × \"buraco mental branco\" (p. 83)"),
("| \"Mente Cósmica\" (p. 19/140)", "(p. 19/140) × \"Mente Maior\" (p. 198) × \"Biocosmos Inteligente\" (p. 198)", "(p. 67/78) × \"Mente Maior\" (p. 140) × \"Biocosmos Inteligente\" (p. 140; p. 221 nota Gardner)"),
("3. **Clínica/biológica:**", "(p. 177–178", "(p. 177"),
("3. **Clínica/biológica:**", "Tay-Sachs (p. 223–224)", "Tay-Sachs (p. 191, cap. 16)"),
("3. **Clínica/biológica:**", "oxitocina/vasotocina/isotocina (cap. 8)", "oxitocina (cap. 8, p. 85–95) / vasotocina-isotocina (cap. 11, p. 125–126)"),
("7. **Gênero:**", "(p. 223) — [fonte externa", "(p. 116, cap. 10) — [fonte externa"),
("7. **Obra B045", "(p. 154:", "(p. 69:"),
("1. **Nota 1 do cap. 12 (p. 228):**", None, "1. **Verificação de notas (caps. 12/13, 2026-08-22):** o corpo do cap. 12 (p. 135) cita Jeffrey Sattinover (coerente com a nota 1 do cap. 12, p. 228: 'O Cérebro Quântico'), e o corpo do cap. 13 (p. 142) + cap. 17 (p. 190) cita Jared Diamond/'O Terceiro Chipanzé' (coerente com a nota 1 do cap. 13, p. 228) → **sem inconsistência entre corpo e notas** (verificação sistemática);"),
("2. **Mavatna × Mavatma** (pp. 66/68/69 × 70)", None, "2. **Mavatna × Mavatma** (pp. 66/67/68/113/114/198 × p. 70) — variação de grafia interna;"),
("7. **\"Mente Cósmica\" × \"Mente Maior\" ×", None, "7. **\"Mente Cósmica\" × \"Mente Maior\" × \"Biocosmos Inteligente\"** (p. 67/78 × p. 140 × p. 221) — variações do mesmo conceito;"),
("18. **\"Prabrajna — ou Prajapati\"** (p. 107)", None, "18. **\"Prabrajna — ou Prajapati\"** (p. 65) — variação de nome (canônico RC: Prabrajna = RC-152);"),
("19. **\"Kundaline\"** (p. 111)", None, "19. **\"Kundaline\"** (p. 112) — erro (Kundalini);"),
("20. **\"Tikum\"** (pp. 114/199)", None, "20. **\"Tikum\"** (p. 114; 'tikun' correto em p. 199/204) — variação (canônico RC: Tikun);"),
]
aplicadas = 0
falhas = []
for ancora, antigo, novo in correcoes:
    achou = False
    for i, l in enumerate(linhas):
        if ancora in l:
            if antigo is None:
                linhas[i] = novo
            elif antigo in l:
                linhas[i] = l.replace(antigo, novo)
            else:
                falhas.append((ancora[:40], antigo[:60]))
            achou = True
            aplicadas += 1
            break
    if not achou:
        falhas.append((ancora[:40], "LINHA NÃO ACHADA"))
open(F, 'w', encoding='utf-8').write('\n'.join(linhas))
print(f"aplicadas: {aplicadas}/{len(correcoes)}")
for a, b in falhas:
    print("FALHOU:", a, "|", b)
