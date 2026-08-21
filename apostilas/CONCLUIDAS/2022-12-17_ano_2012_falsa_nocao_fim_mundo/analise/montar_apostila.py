#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta apostila.md (P2022-12-17 — O Incompreendido Ano de 2012 e a Falsa Noção do Fim do Mundo).
Lê leitura-segmentada.txt, aplica curadoria (grafias canônicas + [REVISAR]),
estrutura em 10 PARTES, marca o intervalo (U0437) e isola a pergunta final da plateia."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2022-12-17_ano_2012_falsa_nocao_fim_mundo")
FONTE = BASE / "analise" / "leitura-segmentada.txt"
SAIDA = BASE / "apostila.md"

REPL = [
    # precessão
    (r"\bpreção equinocial\b", "precessão equinocial"), (r"\bprestação dos equinócios\b", "precessão dos equinócios"),
    (r"\bpressionão eceal\b", "precessão equinocial"), (r"\bpreceção epinocial\b", "precessão equinocial"),
    (r"\bpreceção eceal\b", "precessão equinocial"), (r"\bprceção eceal\b", "precessão equinocial"),
    (r"\bprceção equinocial\b", "precessão equinocial"), (r"\bpreceção equinocial\b", "precessão equinocial"),
    (r"\bprecessão equinocial\b", "precessão equinocial"), (r"\bpreceção dos equinócios\b", "precessão dos equinócios"),
    (r"\bpreceção ecial\b", "precessão equinocial"), (r"\bpreceção ecinocial\b", "precessão equinocial"),
    (r"\bprecessão ecial\b", "precessão equinocial"), (r"\bprecessão ecinocial\b", "precessão equinocial"),
    (r"\bera equinocial\b", "era equinocial"), (r"\bera ecoincial\b", "era equinocial"), (r"\bera ecoinocial\b", "era equinocial"),
    (r"\bera inocceal\b", "era equinocial"), (r"\bera eceal\b", "era equinocial"),
    (r"\bera zodiacal\b", "era zodiacal"), (r"\bera odiacal\b", "era zodiacal"),
    # Alcíone / cinturão
    (r"\bAlceione\b", "Alcíone"), (r"\bAlce\b", "Alcíone"), (r"\bociônio\b", "Alcíone"), (r"\bAlcion\b", "Alcíone"),
    (r"\bAlceo\b", "Alcíone"), (r"\bAlcíone\b", "Alcíone"),
    (r"\bcinturão de fotos\b", "cinturão de fótons"), (r"\bcinturão de fótons\b", "cinturão de fótons"),
    # Baktun / Diego de Landa
    (r"\bbactum\b", "Baktun"), (r"\bBactum\b", "Baktun"), (r"\bbacktom\b", "Baktun"), (r"\bbaktuns\b", "Baktuns"),
    (r"\bDiego Dilanda\b", "Diego de Landa"),
    # Anunnaki
    (r"\bAnonax\b", "Anunnaki"), (r"\bAnunac\b", "Anunnaki"), (r"\banunac\b", "Anunnaki"), (r"\banunaque\b", "Anunnaki"),
    (r"\bAnunaque\b", "Anunnaki"), (r"\banunaques\b", "Anunnaki"), (r"\bAnunaques\b", "Anunnaki"), (r"\banunx\b", "Anunnaki"),
    (r"\bAnunx\b", "Anunnaki"), (r"\banuna\b", "Anunnaki"), (r"\bAnuna\b", "Anunnaki"),
    (r"\bHenk eu\b", "Enki"), (r"\bEnqu\b", "Enki"), (r"\bEnk\b", "Enki"), (r"\benqu\b", "Enki"),
    (r"\bEliuen anué\b", "Enlil e Anu"), (r"\bEliu\b", "Enlil"), (r"\benl\b", "Enlil"), (r"\bEnl\b", "Enlil"),
    (r"\bDibiru\b", "Nibiru"), (r"\bNibiru\b", "Nibiru"),
    (r"\bIgigis\b", "Igigi"), (r"\bIgigi\b", "Igigi"),
    (r"\bracchaças\b", "Rakshasas"), (r"\bracchaço\b", "Rakshasa"), (r"\bRakshasa\b", "Rakshasa"), (r"\bRakshasas\b", "Rakshasas"),
    (r"\bRavana\b", "Ravana"), (r"\bRamaiana\b", "Ramayana"), (r"\bRamayana\b", "Ramayana"),
    # deuses
    (r"\bBrama\b", "Brahma"), (r"\bbrama\b", "Brahma"), (r"\bVirgem\b", "Vishnu"), (r"\bVirgo\b", "Vishnu"),
    (r"\bVirgna\b", "Vishnu"), (r"\bVígno\b", "Vishnu"), (r"\bvion\b", "Vishnu"), (r"\bVion\b", "Vishnu"),
    (r"\bChiva\b", "Shiva"), (r"\bchiva\b", "Shiva"), (r"\bChira\b", "Shiva"), (r"\bChíva\b", "Shiva"),
    (r"\bSofia\b", "Sophia"), (r"\bsofia\b", "Sophia"),
    (r"\bJahé\b", "Javé"), (r"\bJosé\b", "Javé [REVISAR — STT 'José']"), (r"\bJaavé\b", "Javé"),
    (r"\bJahvel\b", "Javé [REVISAR — STT 'Jahvel']"), (r"\bJavé\b", "Javé"),
    (r"\bPrabragen\b", "Prabrajna"), (r"\bPrabrajna\b", "Prabrajna"),
    (r"\bTrimurte\b", "Trimurti"), (r"\bTrimurti\b", "Trimurti"),
    (r"\bMarra barata\b", "Mahabharata"), (r"\bMarrabarata\b", "Mahabharata"), (r"\bmarrabar\b", "Mahabharata"), (r"\bMahabharata\b", "Mahabharata"),
    (r"\bVia e a turma\b", "Vyasa e a turma"), (r"\bVia\b", "Vyasa"),
    (r"\bMatusalém\b", "Matusalém"), (r"\bMatosal\b", "Matusalém"),
    (r"\bNoreia\b", "Noreia"),
    (r"\bMadi\b", "Mahdi [REVISAR — STT 'Madi']"), (r"\bavatar cal\b", "avatar Kalki [REVISAR — STT 'cal']"),
    (r"\bAESTA\b", "Avesta"), (r"\bAvesta\b", "Avesta"), (r"\bCalevala\b", "Kalevala"),
    (r"\bGudrum\b", "Gudrun [REVISAR — STT]"), (r"\bYima\b", "Yima"), (r"\bYima\b", "Yima"),
    (r"\bDiego de Landa\b", "Diego de Landa"),
    (r"\bAntroposófica\b", "Antroposófica"),
    (r"\bcom maricandã\b", "com maricandã [REVISAR — STT: provável 'Tamil']"),
    (r"\bMaric Candã\b", "Tamil [REVISAR — STT 'Maric Candã']"),
    (r"\bcom mar e candão\b", "Tamil [REVISAR — STT 'com mar e candão']"),
    (r"\bAnunnaki\b", "Anunnaki"), (r"\banunnaki\b", "Anunnaki"),
    (r"\bIgrazil\b", "Yggdrasil [REVISAR — STT 'Igrazil']"),
    (r"\bB Frost\b", "Bifrost [REVISAR — STT 'B Frost']"),
    (r"\bZecha\b", "Zecharia Sitchin [REVISAR — STT 'Zecha']"),
    (r"\bSitchin\b", "Sitchin"),
    (r"\bTártaro\b", "Tártaro"), (r"\bTartaro\b", "Tártaro"),
    (r"\bYel Luzbel\b", "Yel Luzbel"), (r"\bLúcifer\b", "Lúcifer"), (r"\bLucifer\b", "Lúcifer"),
    (r"\bVal\b", "Val"),
    (r"\bIEPP\b", "IEEA [REVISAR — STT 'IEPP']"),
    (r"\bMentalma\b", "Mentalma"),
    (r"\bDionísio\b", "Dionísio"), (r"\bDionisio\b", "Dionísio"),
    (r"\bMarduc\b", "Marduk"), (r"\bMarduk\b", "Marduk"),
    (r"\bNinurta\b", "Ninurta"), (r"\bAnu\b", "Anu"),
    (r"\bRudolf Steiner\b", "Rudolf Steiner"), (r"\bSteiner\b", "Steiner"),
    (r"\bGeof\b", "Geoffrey [REVISAR — STT 'Geof']"), (r"\bChittatel\b", "[REVISAR — STT 'Chittatel']"),
    (r"\bestrela Matusalém\b", "estrela Matusalém"),
    (r"\bEstrela Azul\b", "Estrela Azul"),
]

def aplicar(txt):
    for pat, rep in REPL:
        txt = re.sub(pat, rep, txt)
    return txt

def carregar_unidades():
    u = {}
    for linha in FONTE.read_text(encoding="utf-8").splitlines():
        if linha.startswith("U") and "\t" in linha:
            cod, _, texto = linha.partition("\t")
            u[cod] = texto.strip()
    return u

def paragrafos_de(faixa, unidades):
    texto = aplicar(" ".join(unidades[k] for k in faixa))
    frases = re.split(r"(?<=[.!?…])\s+", texto)
    paragrafos, atual = [], ""
    for f in frases:
        if len(atual) + len(f) > 400:
            paragrafos.append(atual); atual = f
        else:
            atual = (atual + " " + f).strip()
    if atual:
        paragrafos.append(atual)
    return [p for p in paragrafos if p.strip()]

CABECALHO = """@titulo: O Incompreendido Ano de 2012 e a Falsa Noção do Fim do Mundo
@autor: Jan Val Ellam
@data: 17/12/2022
@local: Natal/RN (transmissão remota)
@subtitulo: Apostila de estudo — Transcrição editada integral, com correção gramatical e terminológica, organização temática e notas editoriais.
@nota_editor: Esta apostila é a transcrição editada integral da palestra de 17/12/2022 (fonte P2022-12-17) — **a última palestra do ano de 2022** —, organizada tematicamente em 10 PARTES para estudo. É a **fonte original da faixa RC-566–RC-595** (30 termos: Protocolo da Busca, Precessão Equinocial, Eras Equinociais/Zodiacais, Janelas Cósmicas, 2012 como Divisor de Ciclos, Fim dos Tempos × Fim do Mundo, Cinturão de Fótons, Alcíone, Ancoragem do Conglomerado Trimurtiano, Baktun 13, Xamanismo Cósmico, Fim do Experimento Humano, Noreia, Igigi, Rakshasas, Ravana, Guerra Nuclear Anunnaki, Rama, Vyasa, Rishis, Anu, Ninurta, Nibiru, Yima, Profecia Hopi, Era de Peixes, Mahabharata, Linhagem de Seth, Avesta). Preservamos a voz, os marcadores orais, o humor e as digressões do autor; corrigimos apenas erros claros de STT (precessão, Alcíone, Baktun, Diego de Landa, Rakshasas, Igigi, Nibiru etc.), com nota na primeira ocorrência. Passagens duvidosas ficam marcadas como [REVISAR]. O **intervalo de 20 minutos** (U0437) está marcado, e a **pergunta final da plateia** (U0968 — passagens entre eras × calamidades) está isolada em seção própria (PARTE X) e **não compõe a ontologia**. Termos com remissão RC-### referem-se à Base Terminológica RC. Alegações teológicas, históricas, geopolíticas, astronômicas e clínico-científicas são **leitura de Ellam, não consenso validado** — em especial: a crítica a líderes e religiões; o "juízo final frustrado de Javé"; o Cinturão de Fótons, Alcíone e a "estrela Matusalém"; "novas proteínas corrigem o genoma"; a guerra nuclear Anunnaki (quarentenas estritas). A palestra passou por re-curadoria (Dossiê + Devolutiva do curador, 21/08/2026 — O-1 a O-7 aprovados): auditoria da faixa confirmada; **28 fichas ampliadas** (RC-145 Zeus e RC-306 Apolo retidos — sem ficha física); **nenhum código novo consumido** (base blindada em 777 termos; RC-778 preservado).
"""

PARTES = [
    ("PARTE I — A Abertura: Lentes, Protocolo da Busca e Notícias Falsas", "U0001", "U0060", [
        ("Olá, pessoal", "## As lentes do eu e o protocolo da busca"),
        ("E esses véus, eles atendem por muitos nomes", "## Os véus e a ignorância"),
        ("pegar as 100 maiores autoridades", "## Quem inventou o fim do mundo?"),
        ("Desde que Adão e Eva", "## As notícias falsas desde Adão e Eva"),
        ("Mas há uma diferença entre final dos tempos e final do mundo", "## Fim dos tempos × fim do mundo"),
    ]),
    ("PARTE II — As Falsas Profecias Maias e o Ano 2012", "U0061", "U0110", [
        ("Só que nos anos 60, 70 e 80", "## Os dois movimentos dos anos 60–80"),
        ("E olha, muita gente", "## A paranoia de 2012"),
        ("E em fazendo isso, nós vamos entender como Javé pensa", "## O contexto: 104.000 anos"),
        ("eixo inclinado cerca de 23.4", "## O eixo da Terra e o giro de peão"),
    ]),
    ("PARTE III — A Precessão Equinocial e a Ancoragem da Trimurti", "U0111", "U0200", [
        
        ("Mas assim, os alguns espíritos de alguns de nós", "## O tempo para os espíritos"),
        ("Então quando no livro Terra Atlantis", "## A ancoragem na Terra há 104.000 anos"),
        ("E se nós prestarmos bem atenção", "## Quatro ciclos terminando em 2012"),
        ("E o nome desse rapaz é Zeus ou Indra", "## Zeus, o regente aceito"),
    ]),
    ("PARTE IV — Eras Equinociais, Eras Zodiacais e as Apostas dos Deuses", "U0201", "U0300", [
        ("mas esses descendentes que que herdaram o legado", "## A arrogância dos herdeiros"),
        ("existe um outro mecanismo de eras", "## As eras zodiacais de 2.160 anos"),
        ("Então, em vez de apostar", "## As apostas da Trimurti"),
        ("Então, quando eles perceberam que tinha gente que vivia aqui na terra", "## Os Anunnaki e o zodíaco"),
        ("foi quando, depois de muita confusão, a chamada astrologia védica", "## A astrologia védica e os avatares"),
    ]),
    ("PARTE V — Alcíone, o Cinturão de Fótons e a Era de Aquário", "U0301", "U0436", [
        ("Quando ele olhar pro sol", "## As constelações e as três Marias"),
        ("há muito tempo atrás começou a surgir notícias canalizadas", "## O Sol em torno de Alcíone"),
        ("E essa estrela chamada, de fato, tá aí aos 400 e poucos anos luz", "## O sistema de Alcíone"),
        ("E seria um campo de fótons", "## O cinturão de fótons"),
        ("desde o ano 2012, nós começamos a entrar", "## A entrada no cinturão em 21/12/2012"),
        ("E que esse período em que nós vamos ficar dentro desse cinturão", "## A Era de Aquário e os exilados de Alcíone"),
        ("Então, assim, Nós vimos as duas janelas principais", "## As janelas cósmicas e o pacto Zeus–Apolo"),
    ]),
    ("PARTE VI — INTERVALO e Pós-Intervalo: Steiner e a Matrix", "U0437", "U0500", [
        ("Então assim, a gente vai fazer agora o intervalo de 20 minutos", "## INTERVALO — 20 minutos"),
        ("Então 20 minutinhos e voltamos daqui a pouco", "## INTERVALO — 20 minutos (retorno)"),
        ("Vamos nós, vamos retomar", "## Formas de entender o tempo cósmico"),
        ("A turma que tá fora tem seus próprios elementos", "## Dentro ou fora da Matrix"),
        ("Então, decorridos muitas eras equinociais", "## O fardo das eras e a semeadura"),
        ("gente olha pros anos", "## As estelas e os intérpretes do século XX"),
        ("entender aqui um detalhe", "## Os toltecas e a descendência de Caim"),
    ]),
    ("PARTE VII — Os Maias, Diego de Landa e o Baktun 13", "U0501", "U0644", [
        
        
        ("só muito tardeamente se começou a deixar claro", "## Maias, incas e astecas: herdeiros dos toltecas"),
        ("E se não fosse Diego de Landa", "## Diego de Landa e a destruição dos códices"),
        ("diabos é um Baktun", "## O Baktun 13"),
        ("Então assim, o ano 2012, no sentido de que foi incompreendido", "## O 2012 incompreendido"),
    ]),
    ("PARTE VIII — Steiner, as Eras Culturais e Yima", "U0645", "U0700", [
        ("Então, indo adiante na nossa análise", "## Rudolf Steiner e as eras culturais"),
        
        
    ]),
    ("PARTE IX — As Cinco Eras do Último Ciclo de 26.000 Anos", "U0701", "U0955", [
        
        
        ("da Turquia para através dele Javé criar um segmento humano", "## A escolha de Adão e Eva"),
        ("E a Sim. Sabem qual foi um dos acontecimentos mais importantes", "## Zeus aceito como regente"),
        ("Então, indo agora paraa segunda era", "## 2ª era: Igigi, Enoque e os Rakshasas"),
        ("E foi nessa época que o que em outras palestras eu já contei", "## Os Rakshasas, Ravana e Rama"),
        ("O a terceira era equinocial", "## 3ª era: cataclismo, era do gelo e dilúvio"),
        ("E assim, Sem, ou Shem, Cam e Jafé", "## O repovoamento e a 4ª era"),
        ("cada dessa tem 50 fatos importantes", "## A 4ª era: arianos e Dionísio"),
        ("Então, na chamada quinta era", "## 5ª era: Vedas, Abraão e Marduk"),
        ("Aí foi quando os esses dois clãs produziram a guerra nuclear", "## A guerra nuclear Anunnaki"),
        ("E para complicar mais ainda, eles levaram uma surra feia", "## O fim do domínio Anunnaki"),
        ("Aí quando os anunqu se ferram", "## Jesus e a Era de Peixes"),
        ("Mas por que é que não foi foi concluído", "## Os arcontes que não aceitaram Sophia"),
    ]),
]

def main():
    unidades = carregar_unidades()
    linhas = [CABECALHO]
    for titulo, ini, fim, secoes in PARTES:
        chaves = [k for k in unidades if ini <= k < fim]
        paras = paragrafos_de(chaves, unidades)
        linhas.append(f"\n# {titulo}\n")
        alvos = []
        for ancora, subtitulo in secoes:
            a = ancora[:42].lower()
            achou = None
            for i, pp in enumerate(paras):
                if a in pp.lower():
                    achou = i; break
            if achou is None:
                print(f"!! ÂNCORA NÃO ENCONTRADA [{titulo[:24]}]: {ancora[:45]}")
                continue
            alvos.append((achou, subtitulo))
        alvos.sort(key=lambda x: x[0], reverse=True)
        for idx, subtitulo in alvos:
            paras.insert(idx, subtitulo)
        linhas.extend(f"> {p}" if not p.startswith("##") else p for p in paras)
        linhas.append("")
    # PARTE X — pergunta da plateia
    def bloco(faixa):
        return "\n".join(f"> {p}" for p in paragrafos_de(faixa, unidades))
    q1 = [k for k in unidades if "U0968" <= k <= "U1015"]
    fim = [k for k in unidades if "U1016" <= k <= "U1023"]
    linhas.append("\n# PARTE X — Pergunta da Plateia e Encerramento\n")
    linhas.append("## Pergunta 1 — As passagens entre eras acarretam calamidades?\n")
    linhas.append("*Pergunta da plateia:*\n")
    linhas.append(bloco(q1) + "\n")
    linhas.append("## Encerramento — O Jazz da Improvisação Diária\n")
    linhas.append(bloco(fim) + "\n")
    linhas.append("""## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Protocolo da Busca | RC-566 | termo de abertura; ampliado |
| Precessão Equinocial | RC-567 | ampliada (25.920 anos; 4 ciclos → 2012) |
| Eras Equinociais | RC-568 | ampliadas (5 × 5.200) |
| Eras Zodiacais | RC-569 | ampliadas (12 × 2.160) |
| Janelas Cósmicas | RC-570 | ampliadas (pactos; Zeus–Apolo) |
| Ano de 2012 como Divisor | RC-571 | ampliado (juízo final frustrado de Javé) |
| Fim dos Tempos × Fim do Mundo | RC-572 | ampliado |
| Cinturão de Fótons | RC-573 | ampliado (entrada 21/12/2012) |
| Alcíone | RC-574 | ampliada (órbita do Sol; exilados) |
| Ancoragem do Conglomerado Trimurtiano | RC-575 | ampliada (104.000 anos; Marte 300 mi) |
| Baktun 13 | RC-576 | ampliado (Diego de Landa) |
| Xamanismo Cósmico | RC-577 | contexto |
| Fim do Experimento Humano | RC-578 | ampliado |
| Noreia | RC-579 | contexto (filha de Eva) |
| Igigi | RC-580 | ampliados |
| Rakshasas / Ravana | RC-581 / RC-582 | ampliados (vampiros; ser mais forte) |
| Guerra Nuclear Anunnaki | RC-583 | ampliada (sete armas de Nibiru; Sidim) |
| Rama | RC-584 | ampliado (Ramayana) |
| Vyasa / Rishis | RC-585 / RC-586 | contexto (Puranas/Mahabharata) |
| Anu / Ninurta / Nibiru | RC-587 / RC-588 / RC-589 | ampliados |
| Yima | RC-590 | ampliado (cidades subterrâneas) |
| Profecia Hopi da Estrela Azul | RC-591 | ampliada |
| Era de Peixes | RC-592 | ampliada (Jesus; liberdade) |
| Mahabharata | RC-593 | contexto |
| Linhagem de Seth | RC-594 | ampliada (patriarcas; Mar Negro–Cáspio) |
| Avesta | RC-595 | ampliado (Yima; Steiner) |
| Zeus / Apolo | RC-145 / RC-306 | ampliações retidas (sem ficha física) |

### B. Conceitos desta palestra absorvidos como ampliações (zero códigos novos)

| Conceito | Absorvido em | Conteúdo |
|---|---|---|
| Ancoragem 104.000 anos | RC-575 | Trimurti ancora no sistema solar; Marte 300 mi (Yggdrasil/Bifrost); Val 600.000 anos |
| Cinturão de fótons / Alcíone | RC-573 / RC-574 | entrada 21/12/2012; Era de Aquário; exilados |
| Baktun 13 / Diego de Landa | RC-576 | estelas 1 e 6; destruição dos códices |
| Yima / cidades subterrâneas | RC-590 | Turquia; cometa por +1.000 anos |
| Guerra nuclear Anunnaki | RC-583 | sete armas de Nibiru; vale do Sidim; vento radioativo |
| 2012 = juízo final frustrado | RC-571 | "10 anos atrasados"; falta Sophia/reintegração |
| "com maricandã" = Tamil | RC-102 | [REVISAR — STT; confirma P2021-01-23] |

### C. Incertezas do STT (marcadas [REVISAR] no corpo)

"preção/prestação eceal" (= precessão); "Alce/ociônio" (= Alcíone); "bactum" (= Baktun); "Diego Dilanda" (= Diego de Landa); "racchaças" (= Rakshasas); "Igigis" (= Igigi); "Dibiru" (= Nibiru); "com maricandã" (= Tamil); "Via" (= Vyasa); "Madi" (= Mahdi); "cal" (= Kalki?); "estela um e seis"; "era Ior de peixe"; "Gudrum/GR" (livro de Steiner); "Geof/Chittatel" (O Homem que Caiu na Terra); "Abel nasceu afeminado"; "José" (= Javé).

### D. Quarentenas aplicadas

- **Política (crítica):** líderes/religiões/corrupção; "consenso de Washington"; "guerra Ucrânia–Rússia"; Torres Gêmeas; Islã/Meca/Marte — leitura de Ellam, não fato sociológico;
- **Teológica:** Javé/Trimurti/Zeus/Apolo/Marduk; "juízo final frustrado"; "Deus não está no comando"; sacrifícios — leitura do autor;
- **Científica:** Cinturão de Fótons; Alcíone binária; "estrela Matusalém"; "novas proteínas corrigem o genoma"; "Terra congelada há 24.000 anos" — leitura do autor, jamais dado validado;
- **Falas da plateia:** a pergunta final está isolada e não compõe a ontologia da Base.
""")
    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    n_cit = sum(len(l.split()) for l in linhas if l.startswith(">"))
    n_ed = sum(len(l.split()) for l in linhas if not l.startswith(">"))
    print(f"apostila.md: {len(linhas)} linhas | citações ~{n_cit} | editorial ~{n_ed}")

if __name__ == "__main__":
    main()
