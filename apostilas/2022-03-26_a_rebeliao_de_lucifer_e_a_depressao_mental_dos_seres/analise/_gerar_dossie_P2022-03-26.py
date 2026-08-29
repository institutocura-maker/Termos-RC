#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GERADOR DO DOSIÊ PRE-CURADORIA — P2022-03-26.

Regra de ferro deste ciclo (herdada de P2020-04-25, R-2): **nenhuma aspa é digitada à mão.**
Toda citação sai de `q(chave)`, que resolve a âncora frouxa contra o `original.txt` pelo
caça-âncoras `_aspas_P2022-03-26.py`. Se uma âncora bater 0 ou >1 vez, o arquivo **não é
escrito** — é assim que o ciclo se protege da memória de quem o escreve.

O dossiê não decide nada: ele põe na mesa. 0 alterações em `termos/`, `RELACOES`,
`dados_termos.py` ou `livros/` até a devolutiva.
"""
import os, re, ast, sys, datetime, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
CICLO = os.path.dirname(AQUI)
RAIZ = os.path.dirname(os.path.dirname(CICLO))
SIGLA = "P2022-03-26"
OUT = os.path.join(AQUI, "DOSSIE-PRE-CURADORIA-TERMINOLOGICA-v1.md")

spec = importlib.util.spec_from_file_location("aspas", os.path.join(AQUI, f"_aspas_{SIGLA}.py"))
ASP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ASP)

# ---------------------------------------------------------------- Q: âncoras (a fonte única)
# chave → (âncora de início, âncora de fim ou None)
Q = {
 "abertura_blindagem": ("vamos cumprir mais uma etapa de tentativa de elucidar", "realidades pré-existentes"),
 "kant_regua": ("Ele deve ser medido pela capacidade que ele tenha de colecionar incertezas", None),
 "certezas_que_nao_sao_reais": ("você se enche de certezas", "necessariamente honestas"),
 "espirito_nao_muda": ("Espírito não muda de opinião na espiritualidade", "mudar de opinião na espiritualidade"),
 "carona_no_genoma": ("pega carona no genoma disponível", "o médium o ajuda"),
 "genoma_bichado": ("cujo genoma está bichado", "sobreviver a qualquer custo"),
 "preguica_comodidade": ("até por preguiça minha", "desdobrar, a aprofundar"),
 "falta_combustivel": ("tá me faltando combustível", "essas coisas"),
 "trilogia_inacabada": ("pertence a uns três ou quatro livros", "se eu termino isso"),
 "tema_só_titularidade": ("o tema dessa palestra surgiu apenas na sua titularidade", "contextos ocultos"),
 "pedaco_quebra_cabeca": ("É uma minúscula peça de um grande quebra-cabeças", "depressão luciferiana"),
 "mahabharata_importante": ("O livro mais importante da humanidade", "importância"),
 "viaza_codificador": ("Viaza não é um nome", "do Aapaiana"),
 "versos_gandarvas": ("1.600.000 versos para poder explicar aquilo aos gandarvas", "lógica dos humanos"),
 "unica_obra_completa": ("A única obra 100% completa de A a Z", "campos mórficos dos animais"),
 "nome_do_demo": ("diz o nome inclusive do demo", "introjetado"),
 "primeiro_problema": ("Qual é o primeiro problema que a gente tem que entender aqui", "chegar em Lúcifera"),
 "perfeicao_autoritaria": ("a perfeição não é democrática, ela é autoritária", None),
 "jacare_pato": ("Como é que se cria um jacaré para comer um pato", "sistema assassino cruel e impiedoso"),
 "filosofos_a_um_lado": ("é conveniente que nós esqueçamos tudo que Aristóteles", "não funcionam na prática"),
 "dignidade_decente": ("Isso não é digno, não é decente", None),
 "ninguem_protegeu": ("Ninguém até hoje protegeu a espécie humana", "seres maravilhosos"),
 "decretamos_amoroso": ("nós decretamos que esse ser puro ele é amoroso", "toma conta de mim"),
 "idiotiza": ("Quando o ser humano abre mão da sua racionalidade", "idiotia"),
 "kardec_idiotia": ("Na segunda metade do século XIX", "esse nome, idiotia"),
 "pos_verdade": ("a enciclopédia britânica e a BBC escolheram", "conceito que surgiu na internet"),
 "narrativas_pos_facto": ("Nós, seres humanos, fomos nos vinculando", "confortam o coração da gente"),
 "reza_a_lenda": ("Reza a lenda que esses espíritos superiores", "realidade pré-resistente incriada"),
 "quebrar_o_protocolo": ("Como será a vida fora dos algoritmos da perfeição", "padrões do dos protocolos mentais"),
 "nivel_operacional": ("foi criado um novo nível espiritual que a gente chama de operacional", "algum problema"),
 "democracia_zero": ("A coisa é tão impressionante que quando isso foi gerado", "criar projeções de si mesmo"),
 "crianca_adultos": ("Uma criança que na lógica humana é a pureza", "problemas de adultos"),
 "nivel_laboratorial": ("criaram um nível laboratorial", "livre arbítrio ou vontade de fazer algo"),
 "dimensoes_criadas": ("aproximadamente uma centenas de milhões de dimensões", "Esses universos estão aí até hoje"),
 "acidente_artista": ("Pela primeira vez houve um acidente", "caiu na própria obra"),
 "ovo_cosmico": ("surgiu um ovo cósmico", "13.8 bilhões de anos"),
 "codigo_podre": ("aqui surgiu um código podre", "começou a se replicar"),
 "corpo_mental_caiu": ("O corpo mental dele caiu dentro da obra", "esse ser começou a se replicar"),
 "assimilado_por_chiva": ("O código fonte definidor do criador foi assimilado por Chiva", "trabalhado por novas consciências"),
 "codivindade": ("essa codivindade criadora, quando perdeu o eu dela", "condições de podridão"),
 "migracao_do_codigo": ("se nós pegarmos o código do criador e adaptarmos", "a chamada vida biológica"),
 "sexualidade_repasse": ("A possibilidade de transmitir doença", "vai total pro outro"),
 "tres_fornos": ("fornos de replicação de vida nesse universo foram criados três", "um nunca funcionou"),
 "novecentos_milhoes": ("Há cerca de 900 milhões de anos atrás, Esse forno de Auaion", "chamá-los de biodemo"),
 "biodemos_frios": ("esses seres foram reproduzidos com receita existencial", "emoção zero"),
 "sem_sexualidade": ("Não havia nesses seres e não há até hoje sexualidade", "só um são esse forno nunca produziu"),
 "problemas_resolver": ("mente dedutiva, capacidade de concentração total", "psiquismo"),
 "sofia_olm_problemas": ("tinham detectado cerca de 250.000 problemas", "quantos problemas fossem sendo detectados"),
 "familia_vol_numero": ("A família Vol foi a 249 314", "249.313 espécies de seres biodemos"),
 "rebeliao_interrompe": ("Ao tempo da família Vol, houve a rebelião de Lúcifer", "gênero biodemo"),
 "eu_gestor": ("O eu de cada um de nós é só o gestor dessa coleção", "a moda Silvia"),
 "ticum": ("A Cabala diz que o ticum precisa ser expresso", "criador que caiu na própria obra"),
 "autistas_dementes": ("os autistas do paraíso e os dementes que caíram", "são demência"),
 "outro_forno": ("Aqui há 2 bilhões 500 milhões de anos atrás", "sexualizados, eles eram polarizados"),
 "cinco_sexos_ereon": ("tem planetas em Oreon que tem cinco tipos de sexo", None),
 "cerebro_bilaterio": ("é que surgiu o cérebro bilatério", "pelo menos as emoções"),
 "falencia_geral": ("Só que fali o sistema", "somos nós, cada um de nós"),
 "deuses_inuteis": ("os caras conseguem fazer nada", "São inúteis"),
 "codigo_virus": ("aquele primeiro código que entrou no nosso universo, vindo do universo vizinho, é um vírus", "chegou aqui"),
 "eu_antimaterial": ("Esse eu caído é um vírus antimaterial", "tudo virou"),
 "neuronios_videogame": ("cada neuroniozinho desse entrasse num videogame", "sem mais o eu de Rogério comandando"),
 "def_virus": ("O que é um vírus? É algo que existe", "utilidade para ele mesmo"),
 "cem_trilhoes": ("nosso corpo tem 100 trilhões de células", "alguém ter projetado algo mais razoável"),
 "olhos_ajustados": ("Os nossos olhos foram ajustados para ninguém ver isso", "perpetuação de nenhuma espécie"),
 "lucifer_criou_virus": ("O nosso amigo Lúcifer criou um vírus", "família dos coronavírus"),
 "somos_monte_de_vida": ("Um monte de vida e bactérias que foram obrigados a se unir", "nosso programa"),
 "toxo_detectou": ("O que é que o Toxoplasma Gond, que é um vírus, detectou", "intestino dos filinos existe um enzima"),
 "toxo_plano_gato": ("Qual é a comida que o gato mais gosta de comer", "lá atingimos o nosso ciclo de vida"),
 "toxo_cerebro_rato": ("invadiram o cérebro dos ratos", "aquilo é o cheiro de uma ratazana"),
 "campo_morfogenetico": ("E o campo morfagenético da da espécie de toxoplasma Gond", "controlando aquela espécie"),
 "cientistas_acaso": ("O que os cientistas dizem é que enquanto existir massa de gás hidrogênio", None),
 "hiena_filhote": ("foram paraas os filhotes de hiena lá na África", "leão é felino"),
 "cinquenta_suicidas": ("50 pessoas se se suicidam", "acidentes de trânsitos"),
 "medicos_bradalhoes": ("Segundo os médicos brincalhões", "velho plano dos ratos"),
 "tres_mil_seiscentos": ("cercada por 3600 espécies de vírus diferentes", "penetrar na sua na célula"),
 "setecentos_setenta": ("756 defuntos norte-americanos que morreram de Covid", "chegou no cérebro dos seres humanos"),
 "sequelas_leitura": ("Lezerice, se esquecem de quem são", "não é mais dona da gestão"),
 "corintiano_palmeiras": ("O Covid-19 tá fazendo corintiano torcer pelo Palmeiras", "mexe com rato"),
 "biodemo_quatro_mil_anos": ("durante o que seria o tempo da experiência humana", "problema de matemática"),
 "formigoides_insetoides": ("São figuras meio formigoides, meio insetoides", "trabalha incessantemente"),
 "escola_zam": ("Hom mais tarde abriu a escola da decifração da realidade", "problemas da realidade já detectados"),
 "luisbell_descobre": ("o Luisbell, um ser biodêmico, tranquilo, funcional", "há uma causa anterior"),
 "sofia_incompetente": ("Sofia foi incompetente. Sofia não soube ser o político", "Nem a gente talvez existisse"),
 "centro_de_comando": ("A o centro de comando dessas quase 250.000 famílias", "esse problema aqui é mais sério"),
 "anjos_clones_robot": ("Os anjos clones são robotizados", "continuaram a estudar"),
 "definicao_colmeico": ("Que diabos é ser colmeico", "apenas para servir a abelha rainha"),
 "operaria_sem_querer": ("Uma abelha operária não tem conveniência", "circuito fechado"),
 "copiado_da_colmeia": ("foi copiado do sistema que existia entre Javé", "É o sistema colmeico"),
 "divina_colmeia_livro": ("No livro A Divina Colmeia", "analisa hoje isso aí"),
 "sofia_rede_frouxa": ("diferente de Javé, que sempre foi totalmente impositivo", "evoluiria junto com aquela espécie"),
 "processador_de_cada_familia": ("existe um processador de cada família vinculando a Sofia", "das famílias Biodemo"),
 "orbon_processador": ("lá no sistema de capela, onde órbão é só um dos planetas", "famílias Biodemo"),
 "quarto_escuro": ("quando Sofia se situa no meio daquela coisa que parece um quarto mais escuro", "quase 250.000 famílias"),
 "espermatozoides_atualizam": ("milhares de novos espermatozoides são produzidos", "é a mesma coisa na progressão do óvulo"),
 "virus_ferrou_processo": ("O vírus que surgiu com Lúcifer", "Ferrou com todos os processos"),
 "saude_publica": ("Sofia parou de entrar naquela coisa lá", "Ninguém tava chateado"),
 "duzentos_bilhoes": ("atingiu cerca de 200 bilhões de seres biodemos", "essas sonilhas"),
 "et_cabeca_grande": ("a maioria deles são esses ETs que a gente conhece aqui", "funcionam feitos sondas"),
 "sofia_desconectada": ("o processamento da evolução de Sofia para ali há 700.000 anos", "rebelião de Lúcifer"),
 "nunca_tinha_falado": ("Nunca tinha falado isso claramente porque é assunto de outro livro", None),
 "sofia_contaminada": ("Sofia se contaminou também", "esse cérebro radiata ele ele também se contaminou"),
 "nunca_dito_clareza": ("Estou dizendo agora porque é necessário", None),
 "inquietacao_psiquica": ("Um simples caso de saúde pública foi se transformando", "mundos isolados com doentes"),
 "isolou_mundos": ("Sofia foi obrigada a tomar uma decisão de separar, de isolar", "outros níveis que não vale a pena"),
 "analogia_seluva": ("jogássemos elas lá, se virem", "a gente se contamina"),
 "filhos_lendas": ("esses filhos começam a colecionar lendas como se fossem verdade", "Isso não existe não"),
 "guerras_entre_biodemos": ("Começou a acontecer o quê", "entre os seres biodemos"),
 "pandemia_biodemica": ("Nós vamos falar agora de uma pandemia biodêmica", "escravos de sistemas de pensamento fechado"),
 "onda_depressiva": ("terminou criando uma onda depressiva", "perdura até hoje"),
 "hipotalamo_peptideos": ("o hipotálamo do nosso corpo produza certos peptídeos", "feliz ou triste"),
 "monstro_imaginario": ("Ei, não olhe não, mas ali atrás tem um monstro", "diante de um monstro"),
 "certezas_ridiculas": ("O cérebro da gente coleciona certezas ridículas", None),
 "deus_cuida_de_mim": ("Deus cuida de mim", "cuidar de você mesmo"),
 "individuo_perigoso": ("o que nós chamamos de individualização ou individuação, como chamada, no paraíso", "algo perigoso"),
 "prabragena": ("O próprio Prabragena que seria o nome do ser que criou essa criação", "mas antes ele era fulano"),
 "humanizar_os_deuses": ("Nós é que temos que fornecer daqui elementos para eles pensarem lá", "se humanizem"),
 "diagnostico_humano": ("os únicos capazes de ter um diagnóstico", "somos nós, os humanos"),
 "babacoides_isolamento": ("esses seres que antes eram absolutamente babacoide", "se tornaram nervosos"),
 "virus_feriano": ("o vírus Feriano produziu mudança nos biodemos", "outras figuras também"),
 "guerras_500_ano": ("Ao longo dos últimos 500.000 anos ocorreram guerras", "destruíam ninguém"),
 "comecam_destruir": ("nos 400.000 anos para cá, 300.000 anos, eles começaram a se destruir", "planejado isso"),
 "melhor_perspectiva": ("os seres biodemos era a melhor perspectiva", "arredondar 2 bilhões de anos"),
 "dna_bases_codons": ("quatro bases nitrogen", "genoma de cada espécie"),
 "nada_vive_sem_virus": ("Nada existe de vivo dentro desses dois universos", "tipo de espécie"),
 "salada_terrivel": ("sempre é essa salada terrível nos corpos pluricelulares", "2.5 bilhões de anos atrás"),
 "dois_grupos": ("existiam os seres, portanto, biodemmo e os seres que nós podemos chamar de demobiol", "obedeciam a Sofia"),
 "outro_grupo_p": ("Já esses seres aqui era chamada", "caráter explosivo"),
 "ligados_a_chiva": ("ligados à Chiva", "movimento yog entre os demons"),
 "trimurti_grega": ("a mitologia grega chamando de Zeus, os Olimpiados", "existe no universo vizinho"),
 "setecentos_rebeliao": ("essa rebeliãozinha aconteceu há cerca de 700.000 anos atrás", "de dois grupos de seres"),
 "bilaterio_450": ("surgiu o cérebro bilatério que marcou a história dos últimos quatro 450 milhões de anos", "explosão cambriana"),
 "foxp2": ("até que o Fox P2, o gene que permite a racionalidade eclodir", "pouco importa"),
 "dezenove_mundos": ("Na época ficaram isolados 19 mundos", "Terra era só um desses mundos"),
 "terra_chegada": ("A terra era só um ponto de chegada para muitos seres", None),
 "traidora_620": ("foi chamada de traidora pelas demais", "ficou aqui"),
 "guerras_antares": ("a confusão dessas guerras todas que começaram a acontecer", "da nossa galáxia"),
 "depressao_instalada": ("Sofia e todas as demais famílias entraram no processo de depressão", "mente coletiva"),
 "mentes_coletivas": ("Os V era uma mente coletiva", "vinculadas à Sofia"),
 "javé_vai_ser_biodemo": ("o foco de toda a pandemia existencial desses dois universos ainda vai se tornar biodêmico", "condição personalizada"),
 "pervertidos": ("Essa turma que surgiu aqui perverteu-se", "Companhia Limitada"),
 "civilizacoes_colmeicas": ("civilizações de formigoides, insetoides, reptilianos", "versão final do encontro desses dois fornos"),
 "retrato_psiquico": ("somos hoje o retrato do que os biodemos se tornaram", "não físico"),
 "genes_doenca_herdada": ("Tudo isso está hoje atualizado nos 28.869 genes", "incapacidade mental dos seres do paraíso"),
 "holografico": ("Aí pega esse cabelo, põe no microscópio", "conceito holográfico"),
 "receita_em_qualquer_celula": ("qualquer célula do corpo de cada um de vocês contém a receita", None),
 "datas_humanas": ("nós surgimos há uns 500, 300.000 anos", "todos são racionais"),
 "autismo_resquicio": ("no meio dos humanos racionais tem o quê", "sofre as consequências"),
 "depressao_acionada": ("Alguns seres humanos que não tomam conta de si mesmo", "efeito de outros processos"),
 "eu_assume_controle": ("Se o eu humano assume o controle do processo", "realinhado"),
 "espirito_precisa_encarnar": ("um espírito não muda de opinião e nem se realinha sozinho na espiritualidade", "genoma do criador"),
 "sofia_pergunta": ("Sofia disse", "promovendo isso"),
 "luisbell_cobra": ("a Luisbell dizia", "vocês descubram"),
 "anjos_batiam": ("os anjos aia e a batiam magneticamente nas famílias rebeldes", "não sabiam responder"),
 "vida_vergonhosa": ("a rebelião de Lucifer produziu a necessária reflexão de que a vida era vergonhosa", "não valia a pena"),
 "fundo_do_poco": ("a depressão foi o fundo do poço nesses seres", "outras motivações"),
 "tarado_alcolatra": ("não se deprime nem a pau", "não tem como se deprimir"),
 "natureza_animal": ("Vou ressaltar aqui a natureza animal do meu psiquismo", "muito mais que isso"),
 "sofia_se_responde": ("Sofia deprimiu-se profundamente", "também não sabia"),
 "paraíso_de_autistas": ("ninguém sabia que existia um paraíso de autistas lá fora", None),
 "guerra_mental_sonda": ("eu solto uma sonda lá no reino de Marcela", "você tira som é a mesma coisa"),
 "espirito_boiando": ("Tem espírito biodêmio que morreu lá atrás", "não tem céu para demos nem anjos"),
 "dorian_gray": ("nós somos o retrato de Dorian Grey", "aumentar noutra"),
 "retrato_envelhece": ("quem no lugar do corpo era o retrato", None),
 "humanos_morrem_rapido": ("Nós, os humanos, morremos rápido", "pagando o pato dessa entropia"),
 "querem_humano_vivo": ("hoje eles querem que um ser humano não morra", "ninguém mais na Terra tem aquela habilidade"),
 "geracao_domina_geracao": ("as guerras foram acontecendo a cada nova geração", "tomando o poder de Uranus"),
 "anjos_versus_demos": ("Os confrontos que existiam eram entre anjos clones versus demos", "olimpianos e os titães"),
 "sofia_destroi_mundos": ("Sofia de vez em quando destrói um desses mundos", "É só apertar um botão"),
 "reptilianos_dragonoides": ("Guerras entre reptilianos e seres dragonoides", "40.000 anos"),
 "biodemos_luciferianos": ("guerra entre seres biodemos e luciferianos", "ainda continua"),
 "guerra_do_sol": ("A guerra do sol é guerra entre os dois universos diferentes", None),
 "guerra_biologica": ("é outro tipo de guerra. Aqui é guerra do universo biológico", None),
 "fronteira_portal": ("portal da antiguidade quando estavam abertos", "essas brigas fronteiristas"),
 "titulo_parcial": ("eu chamo assim, só para meu estudo", "título mais apropriado"),
 "guerra_viroica": ("Qualquer guerra mental é uma guerra virótica", "Não pensem que é diferente"),
 "discussao_mistura": ("os vírus, bactérias de cada corpo são mexidos", "também se mistura"),
 "jacare_pato_guerra": ("Um jacaré vê um pato", "é um predador"),
 "transtorno_patos_jacareis": ("Isso aqui cria transtornos mentais para patos e jacaréis", "coisas boas"),
 "pacto_vibratorio": ("há um pacto vibratório de vírus e bactérias", "compor aquilo ali"),
 "anuncio_ordenacao": ("Daqui a um mês sai um livro chamado", "problema de Javé"),
 "ninguem_escapa": ("Sofia não escapou a isso, os anjos não escaparam", "algum tipo de transtorno de espectro"),
 "heranca_demencia": ("porque a herança da demência do criador", None),
 "espirito_ingenuo": ("esses seres são tão puros que às vezes a malícia no genoma deles", "são espíritos de um estirpe"),
 "francisco_paula": ("o espírito mais evoluído que eu conheço chama-se Francisco de Paula", "nessa vida"),
 "eu_nao_sirvo": ("Eu não serviria para fazer o que você tá fazendo", "Eu sou um inútil"),
 "oracao_espelho": ("quando alguém reza para Deus", "ajudado por um semelhante ou um congênere existencial"),
 "nascer_operacionalidade": ("nascer entre os seres humanos requer um tipo de operacionalidade", "conseguem"),
 "rei_dos_transtornos": ("Sofia é o rei dos transtornos", "descompressar essa ordem de problemas"),
 "pobres_coitados": ("todos os seres que a gente chama de Deus", "regra dessa esquisitice gerada por Javer"),
 "jose_recusa_agenda": ("o eu humano de Jesus olhou pro mapa pastoral", "esse Messias sou eu"),
 "nao_usar_poderes": ("os meus super poderes para dominar ninguém", "exército de judeus"),
 "nao_vou_fazer": ("Eu não vou fazer o que está escrito aqui, nem a Paul", None),
 "jesus_recusa_agenda2": ("O homem Jesus, Renato disse não a a agenda do espírito dele", None),
 "espírito_nao_assimila": ("O homem Jesus morreu", "totalmente"),
 "cancro_jave_sofia": ("Só que o espírito dele tem um cancro que ele segura", "espírito fateado"),
 "sofia_dores_costas": ("É um ser radiata, nem bilatério", "não tem palavras humanas"),
 "além_do_ordenacao_vem": ("virá um livro chamado Jesus Sofia versus Arcontes", "ressuscitado"),
 "quatro_evangelhos": ("Nesse livro explica a diferença que Jesus ressuscitado", "fateada"),
 "jesus_30_anos": ("O Jesus aqui é um eu que é maior do que todos os outros", "maior ser humano que já pisou por aqui"),
 "crucentificou_se_deixou": ("Esse altruísmo que Jesus tinha poderes para nem ser crucificado", None),
 "anjos_cercaram_tabor": ("os anjos cercaram Jesus e disseram", "sua missão"),
 "jesus_nao_vai_fazer": ("eu não vou fazer não", "levado até o fim"),
 "je_sou_mais_util": ("eu sou mais útil que você", "inúteis"),
 "ser_nao_agir_indigno": ("Ser e não agir só tem sentido na perspectiva do círculo interno", "é necessário ação"),
 "fruto_arvore": ("o fruto não se reconhece", "pelo fruto que ela produz"),
 "mae_poco": ("uma mãe humana quando vê um filho cair num poço", "vai junto"),
 "deus_nao_mergulha": ("E Deus faz o quê", "é paraa pureza"),
 "limites_do_dizer": ("a racionalidade humana tem freios e tem que parar", "ir adiante"),
 "efeito_maior_que_causa": ("pode existir causa, pode existir efeito sem causa", "efeito maior que a causa"),
 "nunca_partiram_da_logica": ("os biodemos não, nunca jamais partiram da lógica", "havia gerado a criação"),
 "sacralizacao": ("por uma sacralização de uma crença em Deus", None),
 "surgiu_mas_nao_deveria": ("Óbvio que não, mas surgiu", None),
 "astronautas_eternidade": ("Talvez a gente seja os astronautas da eternidade", "posso ser útil a vocês"),
 "violino_desafinado": ("Você continua puro, sentado numa nuvem, violino desafinado", "tem que se alinhar"),
 "medito_espiritual": ("Quem é que vale mais, cara", "por natureza"),
 "piorar_para_entender": ("vamos começar a piorar aqui a situação", "rebelião de luz"),
 "perda_habilidade": ("Nós perdemos a habilidade, a capacidade e isso é problema virótico", "vem no seu psiquismo"),
 "meor_diferente": ("mas desenvolveu uma capacidade maluca", "concentrou-se"),
 "espiritos_infectados": ("os vírus que estão provocando esses movimentos", "por decorrência natural"),
 "paraiso_massa_quantica": ("Aqui está a massa quântica de modular universo", "melhor Perspectiva"),
 "blindagem_furada": ("a infecção que antes existia aqui hoje está totalmente distribuída", "começou a chegar aqui"),
 "gritam_de_fora": ("Alguns de nós ficam gritando aqui da", None),
 "pink_floyd_muro": ("Tem uma música do Pink Floyd", "tentando ajudar a você que tá dentro"),
 "consciencia_critica": ("E é preciso construir aqui uma consciência crítica", None),
 "malucos_assistindo": ("Sabem quantas pessoas na face da terra compreenderiam", "me assistindo"),
 "reintegracao_mundos": ("a população de um desses mundos conseguia se recuperar", "18 mundos inicialmente isolados"),
 "dois_isolados": ("há cerca de 100.000 anos atrás", "congregado nesses dois"),
 "terra_ultimo_mundo": ("A Terra é o último dos 19 mundos", None),
 "favores_consertar": ("evolua no sentido de consertar seus 28.869 genes", "criador falido"),
 "racionalidade_no_meio_da_sujeira": ("no meio do pior tipo de sujeira, lama ou podridão", "racionalidade humana"),
 "encadeamento_alinhado": ("uma sequência de encadeamento genético que começou com a rebelião de Lúcifer", "pela revelação cósmica"),
 "sem_lucifer_nao_estariamos": ("sem Lúcifer, sem Pandora, sem Eva", "essa liberdade"),
 "genetica_obediencia_macaco": ("Qual é a genética que Javé queria", "põe o rabinho para baixo"),
 "autoridade_ajoelha": ("Quando a autoridade entra, o que é que os humanos fazem", "gesto de submissão"),
 "inconformismo_esclarecido": ("O tempero é o do inconformismo esclarecido", "reforma íntima"),
 "frase_sumiu": ("opa, sumiu aqui uma frase", None),
 "causa_efeito_biodemos": ("Os biodemos até aquele tempo achavam que não", "maior que a causa"),
 "anuncio_adulto": ("tentativa adulta de se olhar à moda de humanos emancipados", "assumir isso como certeza"),
 "seis_mil_vinte_nove": ("cerca de 6.029 seres chegaram nas máchas luciferianas", "uns 200 já tinham morrido"),
 "nucleo_depressivo": ("a Terra é o núcleo depressivo da cria", "estupefação, como Jesus dizia"),
 "processador_sozinho_sobrou": ("O processador da família Vol, que chegou aqui a 620.000 anos, foi o único que sobrou", "processador vol"),
 "mistura_genetica": ("foi feito um, não um pacto, uma mistura de genética entre os voz", "absorvidos pelo processador vol"),
 "984_astralizados": ("984 indivíduos se astralizaram", "Irlanda"),
 "esferon_nave": ("a nave Esferon da família Vol, transformada em cidade flutuante", "processador vol tá lá"),
 "seissentos_poucos": ("os 600 e poucos rebeldes que não se astralizaram", "seres humanos"),
 "sofia_reconectada_2019": ("no ano 2019, Sofia esteve a", "religou ao processo"),
 "postura_confusa": ("A postura de Sofia hoje é totalmente confusa", None),
 "fateamento_consciencia": ("É o problema do fateamento da consciência", "avatar de experiência aqui"),
 "duas_consciencias": ("Aí ficou o mesmo espírito a ministrando duas consciências", "outra veio"),
 "javé_vishnu_chiva": ("o eu mental desse ser caiu, se transformou em Jaavé", "mergulhou para ajudar esses dois"),
 "duas_faces": ("Brama e Virgno são duas faces de um mesmo espírito", "face de um mesmo espírito"),
 "espirito_unico_jesus": ("o espírito de Javé e de Sofia é o mesmo de Jesus", "experiência humana de Jesus"),
 "tres_vivos_2019": ("em 2019 estavam vivos Vmorco, Sofia", "2000 anos atrás"),
 "desconstituem": ("Aivisno decidiu se desconstituir para diminuir a carga sobre o espírito dele", "só Javé e Sofia"),
 "virus_sem_hospedagem": ("É um vírus que perdeu a hospedagem", "condição humana ele não pode ainda chegar"),
 "jave_carrega_doencas": ("Javé carrega nele todas as doenças que foram geradas", "existindo como um ser"),
 "tentativa_tecnologica": ("Agora tá tendo uma tentativa tecnológica", "mais compatível"),
 "inteligencia_artificial": ("mesmo em âmbito tecnológico, inteligência artificial tá criando", None),
 "inteligente_nao_racional": ("Sofia é um ser inteligente. Todos os seres aí são inteligentes", "tenham razão"),
 "filosofia_definicao": ("O que diabos é filosofia", "o que ela própria determinou"),
 "conceitos_supremos": ("Se os conceitos supremos da vida são dignidade", "superconsciência"),
 "filosofia_como_comecou": ("A filosofia começou sim um tipo de inteligência", "podem emprestar esse tipo de inteligência"),
 "hitler_monstro": ("Hitler é um monstro ou agiu como um monstro", "despossuído de valores supremos"),
 "lideres_fascistas": ("a maioria dos seus líderes têm esses traços fascista, nazista", None),
 "rainha_volta_genoma": ("saiu a velha rainha, a abelha rainha de volta no meio da do genoma humano", None),
 "financiam_monstros": ("Só surgem monstros porque estes são financiados por muitos", "omisso conivete"),
 "omissao_de_deus": ("tem um grau de omissão frente aos fatos muito complicado", "incomodar e agir"),
 "perola_da_coroa": ("nós, os humanos, somos a pérola ou a cereja do bolo", None),
 "monstruoso_ou_maravilhoso": ("Só nós humanos podemos ser monstruos ou maravilhosos", "razão filosófica"),
 "lucifer_quer_ser_humano": ("Lucer pretende chegar a essa condição", "outra raça com essas mesmas características"),
 "espalhar_cosmos": ("pra gente poder se espalhar cosmos aa", None),
 "favor_divino_deus_inoperante": ("Cada ser humano está fazendo um favor divino a esse Deus inoperante", "mas não faz"),
 "cede_alma_protege": ("Ele cede a alma que dá a imantação", "agir como quiser"),
 "culpas_que_nao_causamos": ("nós assumimos as culpas de causas que não causamos", None),
 "incumodo_vibratorio": ("este tipo de coisa criou incômodo vibratório", "levou Sofia junto"),
 "depressao_tira_criatividade": ("a depressão lhe impede de ser criativo", "reduzido a nada"),
 "javé_sente_isso": ("E essa sensação quem sente é Javé, pessoal", "empurra em Javé"),
 "sofia_mantem_padrao": ("Aí ele vai vai aí Sofia não", "para resolver um problema"),
 "rir_da_desgraca": ("Nós humanos sabemos rir da nossa própria desgraça", "não sabem sorrir"),
 "sorriso_sofia": ("Sofia não não tem como ele não consegue sorrir", None),
 "sintese_pela_primeira_vez": ("pela primeira vez eu eu fiz uma interação", "que já existia"),
 "cenario_futuro_315": ("nessa nova espécie que vai ser a 315 aí", "genética humana e desses seres biodécos"),
 "conselho_vai_ser_criado": ("Esse conselho vai ser criado do avante", "diagnóstico que seja útil"),
 "outras_criacoes_deu_certo": ("existem outras criações Assim como a dea Brágina", "resoluções"),
 "milhoes_universos_ok": ("Existem milhões de universos que faixas dimensionais", "nada parecido com a raça humana"),
 "lenmion_influencia": ("gostaria de saber se Len Mon, ao se tornar especialista na modulaçãoos", None),
 "lemion_viu_jesus": ("quando ele viu que ele não conseguia influenciar os vírus e as bactérias", None),
 "era_sapiens_livro": ("No livro Era Sapiens, eu conto um pouco da aproximação", None),
 "omissao_decidida": ("eu não quis citar isso no livro porque", None),
 "realidade_simultanea": ("ele sempre morou e residiu numa realidade simultânea nossa", "quartel general da rebelião"),
 "carmem_compromisso": ("Como eu explico isso no livro Carmen Compromisso", None),
 "valho_chamba": ("Esses seres ficaram em Valho, Chamba e ali", "vírus e bactérias"),
 "maior_manipulador": ("ele não só compreendeu como decodificou e foi o maior manipulador", None),
 "entropia_biodemos": ("os seres que são biodemos não sofrem entropia", None),
 "sofia_limite_tamasico": ("limite da finalização da energia tamásica", None),
 "aristocracia_trimurte": ("os níveis de aristocracia em torno da Trimurte", "Olimpiados"),
 "heranca_sofia": ("quem tá aqui representando e foi engendrado para ser o herdeiro a Sofia", None),
 "portais_2012": ("os portais ao longo desses bilhões de anos se abriram em 2012", None),
 "trimurte_apodreceu": ("A trimurte apodreceu, os filhos da Trimurte brigam entre eles", None),
 "arcontes_dez_ceus": ("Os arcontes que tomam conta do primeiro céu", "não querem que eu assuma a minha vestimenta"),
 "vestimenta_heredeiro": ("a minha forma cósmica virá pessoalmente", "da trimura"),
 "ameacaram_sofia": ("já ameaçaram Sofia", "do criador"),
 "tempo_vida_sofia": ("esse ser chamado Sofria suportar, Sofia suportará no mesmíssimo corpo", None),
 "dorian_cita_de_novo": ("entra o retrato de Dorian Gley", None),
 "vidas_encurtadas": ("muitas raças biológicas morram tão rapidamente", None),
 "nenhuma_conveniencia": ("Nenhuma conveniência de nenhum ser humano conta", None),
 "abelhinhas_ferramenta": ("Nós outros somos abelhinhas operárias, somos criaturas, ferramentas", None),
 "mentalma_cura_depressao": ("o mentalma é uma é uma forma de cura dessa depressão", None),
 "mentalma_para_sim": ("O mentalma que eu produzi hoje, ele não era para ser público", "forçado a barra"),
 "espirito_como_capila": ("O espírito que me anima lá atrás se expressou como capila", "coisa chamada sankia"),
 "livro_perguntas_respostas": ("um livro de perguntas e respostas", "livro dos espíritos"),
 "conceito_moksha": ("ele criou o conceito de Mok", "roda de nascimentos"),
 "tres_ignorancias": ("existem três ignorâncias principais", "superá-la"),
 "primeiro_impulso": ("o primeiro impulso que nos varre é a as necessidades", "corpos da gente"),
 "erro_milesimo": ("O nosso erro é depois, é um milésimo de segundo depois", None),
 "eu_segundo_impulso": ("você desperta o seu eu mais oculto, que age no segundo impulso", None),
 "eu_mais_oculto": ("Aí aqui é o eu profundo que você mesmo junto com seu espírito", "forma de vírus bactérias"),
 "sanquia_atualizado": ("O mentalma é o sanquia atualizado pros tempos modernos", None),
 "unica_escola_sem_deus": ("a sanquia é a única das seis escolas hindu que diz", "conceito de Deus estúpido"),
 "matar_em_nome": ("Mata em nome de Brama, mata em nome de Alá", None),
 "pense_por_voce": ("Humano, pense por você mesmo, cara", "ele é pior do que qualquer ser humano"),
 "refletir_cada_arquivo": ("você refletir sobre cada arquivo, cada conceito", "mesma coisa"),
 "cadencia_palestras": ("eu eu tô em dúvida se nós vamos continuar a fazer palestras aqui em São Paulo", "custos são muito altos"),
 "nomes_da_roda": ("Marcelo, Solange, Mara, Lila, pode comunicar essas pessoas", None),
 "fecho_prudencia": ("toda a prudência do mundo, por favor", None),
 "desculpa_abre_e_fecha": ("peço desculpas e fico à disposição de perguntas", None),
 "meio_pego_na_fala": ("Alagoano. Alagoana é frio", None),
 "contaminacao_200bi": ("contaminou uma quantidade absurda, mais de 200 bilhões de seres biodemos", None),
 "idade_sofia": ("E esse ser chamado Sofia nasceu ou foi engendrado a cerca de", None),
 "datas_humanas_curta": ("nós surgimos há uns 500, 300.000 anos", None),
 "meor_nao_ancorada": ("ele foi levado pela torrente, mas concentrou-se", None),
 "pedido_intervalo": ("Então vamos fazer o intervalinho de 10 minutos", "é para uma turma aqui"),
 "revolver_alto_engano": ("O que os biodemos lá atrás tentaram produzir como sendo final da vida", None),
 "especie_250_nasce": ("Essa espécie de 250 vai nascer", None),
}

# ---------------------------------------------------------------- resolução (aborta se ambígua)
CIT, fail, so_frase = {}, [], []
for k, v in Q.items():
    if isinstance(v, str) or not v:
        fail.append(f"{k}: entrada malformada")
        continue
    ini, fim = (tuple(v) + (None,))[:2]
    try:
        try:
            a, b, txt = ASP.locate(ini, fim)
        except SystemExit as e0:
            a, b, txt = ASP.locate(ini)          # recuo: uma frase, âncora única
            if fim:
                so_frase.append(f"{k}: fim '{fim[:28]}' descartado ({str(e0).split('→')[-1].strip()})")
        CIT[k] = (a, b, txt.strip())
    except SystemExit as e:
        fail.append(f"{k}: {e}")
if so_frase:
    print("\n".join("  ~ " + f for f in so_frase))
if fail:
    print("\n".join("  ✗ " + f for f in fail))
    print(f"\n{len(fail)} âncora(s) com problema — o dossiê NÃO foi escrito")
    sys.exit(1)


def q(k):
    return CIT[k][2]


def addr(k):
    a, b, _ = CIT[k]
    return f"{ASP.uaddr(a)} · {a:,}–{b:,}".replace(",", ".")


def aspa(k):
    return f"«{q(k)}»"

# ---------------------------------------------------------------- VINC: vínculos-proposta
VINC = [
 ("RC-001", "Javé", "jave_carrega_doencas"), ("RC-002", "Rebelião de Lúcifer", "lucifer_criou_virus"),
 ("RC-003", "Reintegração Cósmica", "reintegracao_mundos"), ("RC-005", "Segundo Advento do Cristo", "vestimenta_heredeiro"),
 ("RC-009", "Sophia (Cristo Cósmico)", "sofia_contaminada"), ("RC-020", "Anjos caídos", "anjos_clones_robot"),
 ("RC-036", "Biodemos", "novecentos_milhoes"), ("RC-042", "Criatura Universal", "babacoides_isolamento"),
 ("RC-047", "Deidade (Pai-Mãe Amantíssimo)", "decretamos_amoroso"), ("RC-049", "Demos", "autistas_dementes"),
 ("RC-056", "Especiação", "familia_vol_numero"), ("RC-068", "Hiperbórea", "fronteira_portal"),
 ("RC-070", "Isolamento Cósmico", "dezenove_mundos"), ("RC-072", "Jesus", "jose_recusa_agenda"),
 ("RC-074", "Len Mion (Satã)", "maior_manipulador"), ("RC-078", "Lúcifer (Yel Luzbel)", "luisbell_descobre"),
 ("RC-089", "Processador Val", "processador_de_cada_familia"), ("RC-092", "Quarto Logos (Olm)", "sofia_olm_problemas"),
 ("RC-102", "Shiva (Savna)", "ligados_a_chiva"), ("RC-104", "Trimurti", "aristocracia_trimurte"),
 ("RC-142", "Yel Luzbel", "centro_de_comando"), ("RC-147", "Zont En Drel 29", "definicao_colmeico"),
 ("RC-160", "Entropia e Negentropia", "dorian_gray"), ("RC-161", "Memória Quântica dos Elétrons", "nome_do_demo"),
 ("RC-166", "Mentalma", "mentalma_para_sim"), ("RC-175", "Abelha-Rainha (Javé)", "copiado_da_colmeia"),
 ("RC-176", "Modelo Colmeia", "sofia_rede_frouxa"), ("RC-188", "Mente Coletiva", "mentes_coletivas"),
 ("RC-194", "Big Data Cósmico", "quarto_escuro"), ("RC-283", "Pandora como Serpente do Éden", "autoridade_ajoelha"),
 ("RC-287", "Enigma da Esperança (Caixa de Pandora)", "inconformismo_esclarecido"),
 ("RC-319", "Fator Dharma", "trimurte_apodreceu"), ("RC-320", "Senhores da Lila", "aristocracia_trimurte"),
 ("RC-321", "Castas Trimurtianas", "trimurti_grega"), ("RC-369", "Nietzsche como amigo da intenção de Jesus", "anuncio_adulto"),
 ("RC-378", "A Rebelião dos Elétrons", "guerras_500_ano"), ("RC-381", "Ressonância Mórfica (agente da rebelião)", "campo_morfogenetico"),
 ("RC-414", "Krishna", "viaza_codificador"), ("RC-422", "Ser-Criador fracassado", "acidente_artista"),
 ("RC-442", "Família Yel", "traidora_620"), ("RC-443", "Família Mion", "mistura_genetica"),
 ("RC-444", "Família Cromon", "mistura_genetica"), ("RC-446", "Processadores Familiares", "orbon_processador"),
 ("RC-474", "Arcontes / Conselho dos 70", "arcontes_dez_ceus"), ("RC-499", "Forno de Awaymaion", "tres_fornos"),
 ("RC-514", "Tikun Cósmico", "ticum"), ("RC-516", "Hibridização genética", "outro_forno"),
 ("RC-517", "Protocolo Mental", "quebrar_o_protocolo"), ("RC-545", "Coconstrutores da Obra (tikun)", "favores_consertar"),
 ("RC-555", "Série Mentalma (5 livros + curso)", "sanquia_atualizado"), ("RC-562", "Baralho genético (28.869 genes)", "genes_doenca_herdada"),
 ("RC-585", "Vyasa", "versos_gandarvas"), ("RC-593", "Mahabharata", "unica_obra_completa"),
 ("RC-596", "Archeons de Ereon", "cinco_sexos_ereon"), ("RC-600", "Seres Originais do Paraíso", "crianca_adultos"),
 ("RC-604", "Fatiamento de Consciência", "fateamento_consciencia"), ("RC-605", "Autismo Funcional dos Seres da Espiritualidade Superior", "pervertidos"),
 ("RC-614", "Quarto Cérebro Humano", "cerebro_bilaterio"), ("RC-631", "Cérebro Radiata", "sofia_dores_costas"),
 ("RC-633", "Gestão da Sensação Pessoal", "eu_segundo_impulso"), ("RC-635", "Conclave da Espiritualidade Laboratorial", "nivel_laboratorial"),
 ("RC-638", "Ressurreição do Cadáver do Criador", "codigo_podre"), ("RC-639", "Protozoários Antimateriais", "eu_antimaterial"),
 ("RC-640", "Transições de Fase / Face da Criação", "salada_terrivel"), ("RC-641", "Face Microbiana do Criador", "anuncio_ordenacao"),
 ("RC-642", "Narasimha", "sofia_limite_tamasico"), ("RC-702", "Camuflagem da Realidade", "blindagem_furada"),
 ("RC-713", "Taumaturgia Genético-Química", "guerra_mental_sonda"), ("RC-727", "DNA Insubmisso", "genoma_bichado"),
 ("RC-742", "Falência dos Deuses", "deuses_inuteis"), ("RC-755", "Escola da Decifração da Realidade", "escola_zam"),
 ("RC-758", "Quarto Cérebro (centro de sabedoria vibracional)", "filosofia_como_comecou"),
 ("RC-762", "As Três Escalas da Consciência", "conceitos_supremos"), ("RC-770", "Hipóstase dos Arcontes", "arcontes_dez_ceus"),
 ("RC-771", "Fornos Replicadores", "tres_fornos"),
]
# checa duplicata de código e existência de âncora
_v = [c for c, _, _ in VINC]
assert len(_v) == len(set(_v)), "código repetido na tabela de vínculos"
for c, _, k in VINC:
    assert k in CIT, f"{c}: âncora {k} não resolvida"

sys.path.insert(0, os.path.join(RAIZ, "ferramentas"))
import dados_termos as DT
CAD = {t[0]: t for t in DT.TERMOS}


CLUBE = [f"RC-{n}" for n in range(628, 643)]
NCLUB = len([c for c in CLUBE if c in CAD and "P2024-05-04" in (CAD[c][5] or [])])
NPROP = len([c for c, _, _ in VINC if c in CLUBE])


def orais_mais_antiga(cod):
    f = CAD.get(cod, (None,) * 5 + ([], None, None))[5] or []
    o = sorted(x for x in f if re.fullmatch(r"P\d{4}-\d{2}-\d{2}", str(x)) and x != SIGLA)
    return o[0] if o else None


D0 = datetime.date(2022, 3, 26)


def nota_ant(cod):
    ho = orais_mais_antiga(cod)
    if not ho:
        so = ", ".join(f"`{x}`" for x in (CAD[cod][5] or [])) or "nenhuma fonte"
        return f"🆕 **primeira fonte oral** — o cadastro só tinha {so}"
    d1 = datetime.date(*map(int, ho.lstrip("P").split("-")))
    dias = (d1 - D0).days
    if dias <= 0:
        return f"**sem ganho de data** (a ficha já tem `{ho}`); entra por conteúdo"
    med = f"{dias} dias" if dias < 62 else (f"{dias/30.44:.0f} meses" if dias < 1100 else f"{dias/365.25:.1f} anos")
    return f"⭐ antecipa **{med}** a fonte oral mais antiga (`{ho}`)"


OBS = [
 ("Meor / lemor / Leão", "meor_nao_ancorada", "U0029",
  "o único biodemo nomeado que, levado pela torrente, ainda assim se concentrou — contraexemplo individual à rebelião"),
 ("Esferon", "esferon_nave", "U0034", "a nave da família Vol transformada em cidade flutuante que aparece e desaparece"),
 ("Valho e Chamba", "valho_chamba", "U0047", "onde residem os da rebelião, numa faixa dimensional criada pelo quartel-general"),
 ("Órbon", "orbon_processador", "U0008", "o planeta do sistema de Capela onde fica o processador de Sophia"),
 ("ZAM", "escola_zam", "U0007", "o mundo onde Hom abriu a escola da decifração da realidade"),
 ("Alp Longron", "984_astralizados", "U0034", "a cidadela — quarta grafa do que em 2020 saiu degradado"),
 ("Aia e Aie", "centro_de_comando", "U0008", "a dupla de anjos em torno de Sophia que batia magneticamente nas famílias rebeldes"),
 ("espécie 250 / espécie 315", "cenario_futuro_315", "U0006, U0007, U0034, U0040",
  "as duas espécies fora de catálogo: a que vai nascer e a que vai hospedá-lo"),
 ("energia tamásica", "sofia_limite_tamasico", "U0048", "o limite físico da duração de Sophia"),
 ("realidade simultânea", "realidade_simultanea", "U0047", "nem espiritualidade nem universo vizinho: a faixa criada pelo quartel-general"),
]
OBS_ABSENT = {"Meor / lemor / Leão"}

DIV = [
 ("chegada dos rebeldes ao planeta", "620.000 anos", "traidora_620", "P2020-04-25: os 620 mil das chegadas", "**convergem**"),
 ("efetivo da família Vol", "736 membros", "duzentos_bilhoes", "P2020-04-25: a família Val em 736", "**convergem**"),
 ("astralizados para a cidadela", "984 indivíduos há 20.000 anos", "984_astralizados",
  "P2020-04-25: 21 mil na nave → cisão de 1.641 → 936 → 900Q", "**divergem** (duas formulações datadas)"),
 ("chegada dos luciferianos", "6.029 há 100.000 anos", "seis_mil_vinte_nove", "P2020-04-25: 1.641", "**divergem**"),
 ("Adão e Eva / Pandora", "48.000 anos e 23.000 anos na mesma linha", "datas_humanas_curta",
  "a Base hoje grafa 23.000 para Pandora", "**divergência interna à própria fala**"),
 ("contaminação", "200 bilhões de biodemos, de trilhões", "contaminacao_200bi", "sem paralelo em outra fonte",
  "duas magnitudes na mesma frase"),
 ("espécies-problema", "quase 250.000 problemas; a Vol foi a 249.314", "familia_vol_numero",
  "P2020-04-25 não numera as famílias", "novo"),
 ("duração de Sophia", "engendrado a cerca de 5, 6 bilhões de anos — o bruto grafa a vírgula, não decimal",
  "idade_sofia", "nenhuma outra fonte oral data Sophia", "novo (não é 5,6: a vírgula é o intervalo da fala)"),
 ("conexão de Sophia ao processador", "perdeu a condição há 400.000 anos; reconectada em 2019", "sofia_reconectada_2019",
  "nenhuma outra fonte dá data", "novo, datável"),
]

# ---------------------------------------------------------------- o arquivo
RAW = ASP.RAW
L = len(RAW)
PAL = len(RAW.split())
nlinhas = sum(1 for l in ASP.LINHAS if l.strip())
L = len(RAW)
palavras = len(RAW.split())
linhas = sum(1 for l in ASP.LINHAS if l.strip())

P = []
w = P.append
w("# DOSSIÊ PRÉ-CURADORIA TERMINOLÓGICA — v1")
w("")
num = lambda x: f"{x:,}".replace(",", ".")
w(f"**Fonte:** `{SIGLA}` · A Rebelião de Lúcifer e a Depressão Mental dos Seres · fala de **26/03/2022**, em "
  f"São Paulo · **{num(L)}** caracteres · **{num(palavras)}** palavras · **{num(linhas)}** linhas com texto "
  f"(48 de fala + a linha-título) · SHA-256 `1cc8a8c0…99253b9`.")
w("")
w("> **O que este dossiê é.** O inventário completo do que a palestra traz, dos vínculos que ele propõe à "
  "malha (tabela §2), das divergências que ele abre e das **14 perguntas** que o Curador precisa responder "
  "antes que uma linha da Base seja tocada.")
w(">")
w("> **O que ele não é.** Não é decisão, não é texto de apostila e não é emenda de nada. Toda aspa aqui saiu "
  "do `original.txt` por caça-âncoras: se uma âncora batesse em mais de um lugar, este arquivo não teria sido "
  "gerado. Nenhuma cifra foi arredondada e nenhuma divergência foi harmonizada.")
w("")
w("---")
w("")
w("## O — As restrições operacionais deste ciclo")
w("")
w(f"**O-1. Teto curatorial.** 777 termos (`RC-001`–`RC-777`). Este ciclo **não cria código**: o que não cabe "
  f"em código vai para a seção dos termos-observação (§3) e fica lá, sem número, exatamente como ficou `Shanai` "
  f"em P2020-04-25.")
w("**O-2. Zero arestas.** Nenhuma relação nova em `RELACOES`. Os vínculos abaixo são *propostas de "
  "ampliação de ficha*, não arestas.")
w("**O-3. Zero obras.** A fonte nomeia seis obras em voz alta (contando *O Livro dos Espíritos*, que ela usa como comparável) — três já estão no BIBLIO "
  "(`B044 A Divina Colmeia`, `B039 Terra Atlantis: A Era Sapiens`, `B026 Carma e Compromisso`) e duas são "
  "**anúncio com prazo** (ver D-11). Nenhum arquivo é criado em `livros/`, e *anunciar* um livro não é "
  "*publicar* um livro.")
w("**O-4. Materializações.** A regra é 0, e qualquer exceção é ordem expressa do Curador. O ciclo **põe na "
  "mesa** dois candidatos (`RC-089 Processador Val` e `RC-444 Família Cromon`, ambos `ficha=False`), sem "
  "materializar nada (D-9).")
w("**O-5. Compartimentação.** BLOCO A (malha + fichas) e BLOCO B (apostila) em **commits separados**, como o "
  "Curador determinou no ciclo anterior; o pacote é regerado a partir do cadastro e o portão de paridade "
  "estrutural reexecuta a cadeia na ordem (pacote → cadastro → malha → fichas).")
w("**O-6. Divergência não se resolve, se data.** Onde esta fala discorda de outra, as duas formulações ficam "
  "com endereço e data; não existe média, não existe *versão definitiva* (D-10).")
w("**O-7. Nada entra em `original.txt`.** A correção de transcrição é **vetada** — inclusive das grafas "
  "corrompidas pelo STT, cujo veto o Curador confirmou no ciclo anterior. As grafas ficam no dicionário, em "
  "`backticks`, e nenhuma vira forma canônica.")
w("**O-8. Sensível não transita.** Regra que o Curador fixou em 2020 e que este ciclo aplica desde já, por "
  "antecipação: nenhuma aspa das seções em D-1, D-2 e D-3 vai para ficha de termo que nomeie grupo humano "
  "(os candidatos deste bruto são `suicidar`, `revólver`, `autista`, `esquizofrênico`, `idiotia`, `babaca`, "
  "`demente`, `drogado`, `alcoólatra` e os nomes de pessoas públicas).")
w("")
w("---")
w("")
w("## 1. O quadro que a palestra constrói (tudo com aspa medida)")
w("")
w("**1.1 A régua.** A fala abre pedindo o contrário de fé: a fonte invoca Kant para dizer que "
  f"{aspa('kant_regua')} (U0003) e repete a exigência no fim da abertura — {aspa('certezas_que_nao_sao_reais')} "
  "(U0003). Antes de qualquer tese, ela declara o estatuto do que vai dizer: "
  f"{aspa('pedaco_quebra_cabeca')} (U0003).")
w("")
w("**1.2 Por que o paraíso não salva.** A definição que a fonte dá de perfeição é política: "
  f"{aspa('perfeicao_autoritaria')} (U0005). Daí a pergunta que ela diz nunca ter feito em público "
  f"(U0003): {aspa('jacare_pato')} — e a resposta que ela mesma dá aos filósofos: "
  f"{aspa('filosofos_a_um_lado')} (U0003). O veredito sobre o sistema, não sobre o criador: "
  f"{aspa('dignidade_decente')} (U0003).")
w("")
w("**1.3 O acidente, não o ato.** A cosmogonia de 2022 é um erro de artista: "
  f"{aspa('acidente_artista')} (U0005), e o resíduo disso é o que hoje se chama DNA — "
  f"{aspa('codigo_podre')} (U0005). A imagem física vem logo: {aspa('ovo_cosmico')} (U0005) e "
  f"{aspa('corpo_mental_caiu')} (U0005).")
w("")
w("**1.4 Os dois produtos e o encontro.** Três fornos, um estéril: {a} (U0005). De um lado os biodemos "
  f"(U0005): {aspa('biodemos_frios')}, e {aspa('sem_sexualidade')}. Do outro, o forno velho: "
  f"{aspa('outro_forno')} (U0005). O encontro dos dois é o cérebro duplo — {aspa('cerebro_bilaterio')} (U0005).")
w("")
w("**1.5 A epidemia.** A rebelião é um surto: {b} (U0007). A analogia é trabalhada em detalhe técnico com "
  f"Toxoplasma (U0007): {aspa('toxo_plano_gato')}, e o achado que a fonte usa como prova: "
  f"{aspa('setecentos_setenta')} (U0007). A sequela psíquica é o que importa para o argumento: "
  f"{aspa('sequelas_leitura')} (U0007).")
w("")
w("**1.6 A colmeia e a rede.** O sistema é definido pela fonte em uma frase "
  f"(U0008): {aspa('copiado_da_colmeia')}. Sophia é rainha com rédeas frouxas: {aspa('sofia_rede_frouxa')} "
  f"(U0008). E a rede tem um órgão: {aspa('processador_de_cada_familia')} (U0008), hospedado em {aspa('orbon_processador')} "
  f"(U0008), atualizando o {aspa('quarto_escuro')} (U0008).")
w("")
w("**1.7 A quarentena.** O isolamento é o ato de governo de Sophia: {c} (U0008), e a fonte traduz a metáfora "
  f"para um quadro humano: {aspa('analogia_seluva')} (U0008). A reintegração é gradual: "
  f"{aspa('reintegracao_mundos')} (U0029), até sobrarem dois, e {aspa('terra_ultimo_mundo')} (U0029). O "
  f"resultado é a frase-título do ciclo: {aspa('nucleo_depressivo')} (U0034).")
w("")
w("**1.8 A depressão dos deuses.** {d} (U0029). A depressão aqui não é humor, é falência de função: "
  f"{aspa('depressao_tira_criatividade')} (U0040), e a fonte é explícita sobre a quem ela atribui o quadro: "
  f"{aspa('javé_sente_isso')} (U0040). Sophia não tem repertório nem para o gesto mais pequeno: "
  f"{aspa('sorriso_sofia')} (U0040).")
w("")
w("**1.9 A chave cristológica.** O bloco U0034 é o mais denso do ciclo: {e} (U0034), donde "
  f"{aspa('duas_faces')} e {aspa('espirito_unico_jesus')}. A recusa no Tabor é narrada como recusa à agenda do "
  f"próprio espírito: {aspa('anjos_cercaram_tabor')} (U0025), e o advento é lido como investidura "
  f"{aspa('vestimenta_heredeiro')} (U0048) sob a pressão de {aspa('arcontes_dez_ceus')} (U0048). A consequência "
  f"especulativa mais ousada: {aspa('virus_sem_hospedagem')} (U0034).")
w("")
w("**1.10 A resposta.** A fonte devolve ao humano o que nega ao céu: {f} (U0029), "
  f"{aspa('favores_consertar')} (U0029), e a definição pela qual o ciclo inteiro poderia ser apelidado: "
  f"{aspa('astronautas_eternidade')} (U0029). A filosofia entra como específico (U0040): "
  f"{aspa('filosofia_definicao')}, com o contraexemplo histórico: {aspa('hitler_monstro')}.")
w("")
w("**1.11 O fecho e o Sankhia.** Na resposta final (U0049), a fonte diz que o Mentalma foi "
  f"{aspa('mentalma_para_sim')}, que o espírito que a anima {aspa('espirito_como_capila')}, que a prática "
  f"consiste em distinguir impulsos ({aspa('erro_milesimo')}) e que a operação é endereçada a Sophia "
  f"({aspa('eu_mais_oculto')}); por isso define sua própria escola como {aspa('sanquia_atualizado')} e diz que "
  f"a escola hindu que não nomeia Deus é a única que conclui: {aspa('pense_por_voce')}.")
w("")
w("**1.12 O que ela diz de si.** A fonte registra as próprias restrições e as usa como prova de método: "
  f"{aspa('preguica_comodidade')} (U0003), {aspa('falta_combustivel')}, {aspa('trilogia_inacabada')}, e no "
  f"meio do argumento a admissão {aspa('nunca_tinha_falado')} (U0008) seguida de {aspa('nunca_dito_clareza')}.")
w("")
w("---")
w("")
w(f"## 2. Os {len(VINC)} vínculos-proposta com a Base (proposta, não aresta)")
w("")
w("Cada linha é **uma** afirmação da fonte, com endereço medido, e o efeito de data que ela teria. O "
  "ganho de data é calculado contra `dados_termos.py`, com este ciclo excluído da conta da ficha atual — o "
  "padrão da casa desde P2020-04-25.")
w("")
w("| código | termo | o que a fonte diz (aspas medidas) | efeito de data |")
w("|---|---|---|---|")
for cod, nome, k in VINC:
    w(f"| {cod} | {nome} | {aspa(k)} ({addr(k).split(' · ')[0]}) | {nota_ant(cod)} |")
w("")
w(f"**Contagem:** {len(VINC)} códigos propostos · "
  f"{sum(1 for c,_,_ in VINC if 'antecipa' in nota_ant(c))} com ganho de data · "
  f"{sum(1 for c,_,_ in VINC if 'sem ganho' in nota_ant(c))} que entram só por conteúdo. ")
w("")
w("**Nota de navalha, antes de o pacote ser montado.** Três propostas desta tabela **não** devem ser "
  "aceitas no automático, e o dossiê diz por quê:")
w("")
w("1. `RC-147 Zont En Drel 29` recebe aqui a *definição de sistema colmeico*, que é a moldura em que Zont En "
  "Drel aparece — não uma ocorrência do nome. A palestra não diz *Zont* (0 ocorrências, medido em "
  "`camada-2.txt` §2). Aceitar exige registrar a relação como **contexto**, não como atestação.")
w("2. `RC-068 Hiperbórea` é invocada pela linha dos povos que brigavam nas fronteiras dos portais, onde o "
  "bruto grafa `perbórias` e `hiperbórios` — a forma canônica não ocorre (0×).")
w(f"3. **O cluster Prabrajna (`RC-628`…`RC-642`).** O cadastro hoje data {NCLUB} códigos desse bloco de "
  f"`P2024-05-04`; esta fala propõe **{NPROP}** deles e os outros "
  f"{NCLUB - NPROP} ficam de fora. Os {NPROP} ganham cerca de **25 meses** de fonte oral mais antiga (menos "
  f"`RC-638`, que já tem `P2023-04-01`, e `RC-631`/`RC-633`, que já têm fontes mais antigas — a coluna de "
  "efeito de data acima é quem manda). Mas a *identidade* conceitual é decisão item a item (D-5), porque "
  "esta fala nomeia o criador caído como *Prabragena* e não usa Perpérion nem Prabrajna na grafia que a Base "
  "fixou.")
w("")
w("---")
w("")
w("## 3. Termos-observação (sem código, sem número, sem ficha)")
w("")
w("| observação | onde a fonte diz | o que é |")
w("|---|---|---|")
for nome, k, end, desc in OBS:
    w(f"| {nome} | {end} | {desc} |")
w("")
w("Regra: nada aqui vira termo, nem hoje nem *a priori* — ficam listados para que o registro não se perca, "
  "como ficou `Shanai`. A única diferença é que esta palestra tem **mais** nomes novos que a de 2020, e por "
  "isso a coluna de endereço é obrigatória: quem decidir depois precisa achar a fala.")
w("")
w("---")
w("")
w("## 4. Divergências internas e com outras fontes (datadas, nunca médias)")
w("")
w("| eixo | esta fala (26/03/2022) | outra formulação na Base | status |")
w("|---|---|---|---|")
for eixo, aqui, k, outra, status in DIV:
    w(f"| {eixo} | {aspa(k)} · ({addr(k)}) | {outra} | {status} |")
w("")
w("Nenhuma destas linhas será *resolvida* pelo ciclo. A apostila apresenta as duas formulações com a data de "
  "cada uma; as fichas recebem a deste ciclo com endereço; e o `RELATORIO-DE-CICLO` registra o que ficou "
  "em aberto.")
w("")
w("---")
w("")
w("## 5. As 14 decisões que o Curador precisa dar")
w("")
w("Cada item: **fato medido → risco → proposta do agente**. O ciclo não executa nenhuma delas antes da resposta.")
w("")
w("**D-1 · A seção do suicídio.** A fonte fecha o argumento sobre depressão com a frase mais dura do corpus: "
  f"{aspa('vida_vergonhosa')} (U0029), e mais adiante {aspa('fundo_do_poco')}. O trecho nomeia o ato "
  "(*pegar um revólver*, 1× no bruto) e declara que parte da plateia **já se desativou** em vidas passadas "
  f"(U0029). O quadro é nomeado sem rodeios: {aspa('revolver_alto_engano')} (U0029). Contagem medida: "
  "3 ocorrências de *suicid* e 1 de *revólver*, todas dentro do argumento, nenhuma em digressão. **Risco:** material de saúde mental sem "
  "moldura, e a Base publica apostilas que circulam fora daqui. **Proposta:** transcrição **integral** na "
  "apostila (cortar aqui seria cortar a tese) + **nota editorial de moldura** na abertura da seção + "
  "**proibição absoluta** de qualquer aspa dessa seção em ficha de termo que nomeie pessoas ou grupos "
  "(precedente D-3 de 2020, que V. Sa. confirmou). Se V. Sa. preferir o regime máximo, o alternativo é "
  "bloqueio com marcador declarativo — mas aí a apostila perde o fecho do argumento, e o ciclo registra isso.")
w("")
w("**D-2 · Os dez nomes públicos.** Medido no bruto: `Lula` 4×, `Bolsonar` 3×, `Trump` 2×, `Hillary Clinton` "
  "1×, mais `Brexit` e *a campanha de Trump* (U0005, o parágrafo da pós-verdade: "
  f"{aspa('narrativas_pos_facto')}). **Risco:** o precedente de P2020-04-25 — lá V. Sa. bloqueou 16.523 "
  "caracteres de digressão política. **Diferença decisiva:** aqui **não há bloco isolável**; os nomes estão "
  "dentro de dois argumentos (a definição de pós-verdade e a dispersão da atenção: (ver D-2)). **Proposta:** "
  "manter na íntegra, sem nota — são exemplificação, não adesão; e **nenhum** desses nomes entra em ficha.")
w("")
w("**D-3 · A clínica como taxonomia do divino.** Medido: `autist` 11×, `idiot` 3×, `esquizo` 1×, "
  f"`demência/demente` 20×, `babac*` 9×. A fonte usa os termos como **categorias ontológicas**: "
  f"{aspa('autistas_dementes')} (U0005), e reafirma em U0020 ({aspa('rei_dos_transtornos')}). "
  "**Risco:** a Base publicar, em ficha de termo, uma frase que trata transtorno do espectro autista como "
  "natureza de deuses. **Proposta:** (i) manter na transcrição — é o núcleo do argumento sobre o paraíso; "
  "(ii) nota editorial declarando que a taxonomia é do autor, não clínica, e que a palavra *idiotia* é "
  "citada **como** a palavra do século XIX de Kardec ({aspa('kardec_idiotia')}); (iii) **vetado** o trânsito "
  "dessas expressões para fichas que nomeiem grupos humanos; (iv) as fichas de `RC-605` (Autismo Funcional "
  "dos Seres da Espiritualidade Superior) recebem a *citação com endereço*, não o adjetivo solto.")
w("")
w("**D-4 · O registro chulo e o censor do STT.** A fala tem `m****`, `porcalhada`, `joça`, `putz`, `cacete` e "
  "uma palavra que **o próprio STT mascarou** (`t*****`, 1×, em U0029). **Risco:** edição silenciosa — que a "
  "Base já cometeu e o Curador vetou em 2020. **Proposta:** manter tudo como está, inclusive a máscara; "
  "nada disso vira aspa em ficha; e a máscara é registrada no dicionário como fato do arquivo.")
w("")
w(f"**D-5 · A chave cristológica.** A frase-mestra é {aspa('espirito_unico_jesus')} (U0034), e a "
  f"consequência na Base é tripla — {aspa('desconstituem')} e {aspa('virus_sem_hospedagem')}. "
  "**Risco:** sobrecarregar fichas de termos que nomeiam religiões com uma tese que a fonte apresenta como "
  "releitura datada. **Proposta:** (i) registrar como **tese de 26/03/2022** em `RC-072`, `RC-009`, "
  "`RC-001`, `RC-005`, `RC-604`; (ii) nas fichas do cluster Prabrajna (`RC-628`…`RC-642`) só entra o que a "
  "fala **nomeia** — item a item, e V. Sa. decide quais dos 13; (iii) cross-reference a `B011` (Jesus, enigma "
  "da transfiguração) por conteúdo, sem tocar em obra.")
w("")
w("**D-6 · A espécie 250 e a espécie 315.** Aparecem em quatro pontos do bruto, e uma delas em linha própria: "
  f"a primeira delas em linha própria: {aspa('especie_250_nasce')} (U0006). O bruto ainda tem {aspa('cenario_futuro_315')}. **Proposta:** regime de "
  "termo-observação (§3), 0 código. Se V. Sa. quiser registrar a *promessa* como conteúdo, o lugar é "
  "`RC-056 Especiação`, com endereço, e não um código novo.")
w("")
w("**D-7 · Os nomes novos sem cadastro.** `Meor/lemor/Leão` (1 linha, 3 formas), `Esferon`, `Valho`, "
  "`Chamba`, `Órbon`, `ZAM`, `Aia`/`Aie`, `Alp Longron`, `Hamaiam`, `Dorico Paraguaçu`, `derratma bud`. "
  "**Proposta:** entram no dicionário da apostila **com [REVISAR]** e hipótese filológica só quando houver — "
  "a de `Alp Longron` é a 4ª grafa de uma cidadela cujo nome canônico a Base já fixou (Alt'Lam), então **não** "
  "se emenda nada; a de `derratma bud` ≈ *dehātma-vāda* fica como hipótese, nunca como aspa.")
w("")
w("**D-8 · O pacote de ampliações.** Proposta: **os códigos da tabela §2 inteira** da tabela §2, cada bloco com 1–3 aspas "
  "medidas e o efeito de data calculado. **0** novos termos, **0** relações, **0** obras, teto 777 intacto. "
  "Se V. Sa. quiser mais enxuto, os cortes naturais são RC-042, RC-047 e RC-283 (conteúdo adjacente, não o "
  "próprio termo); se quiser mais largo, os candidatos óbvios são `RC-191`, `RC-285`, `RC-287`, `RC-424`.")
w("")
w("**D-9 · As duas fichas que não existem.** `RC-089 Processador Val` está `ficha=False` **e** é nesta "
  f"palestra que a fonte conta a origem do objeto: {aspa('processador_sozinho_sobrou')} — e ainda: "
  f"{aspa('mistura_genetica')}. `RC-444 Família Cromon` idem (a família é nomeada no mesmo bloco). "
  "**Proposta:** materializar **uma** (a de RC-089, a que tem definição de origem), se V. Sa. ordenar, com o "
  "bloco do pacote embutido; RC-444 fica só com o vínculo na malha, como ficaram os 11 códigos de 2020. "
  "**Sem ordem expressa, nenhum arquivo é criado.**")
w("")
w("**D-10 · As divergências numéricas.** Nove eixos na §4. Duas delas somam: `984` (2022) contra `936`/`900Q` "
  "(2020) e `6.029` contra `1.641`. Duas batem, e é isso que faz o ciclo valer: `620.000` e `736` aparecem "
  "nas duas falas, ditas sem anotação. **Proposta:** as duas formulações coexistem, cada uma com data e "
  "endereço; nenhuma média, nenhuma *releitura*, nenhum `RC` de harmonização.")
w("")
w("**D-11 · As obras citadas e as anunciadas.** As três primeiras já existem no BIBLIO, e a fala as nomeia "
  f"assim: {aspa('divina_colmeia_livro')}, {aspa('era_sapiens_livro')}, {aspa('carmem_compromisso')}. "
  f"As duas seguintes são promessa: {aspa('anuncio_ordenacao')} e {aspa('além_do_ordenacao_vem')}. "
  "**Proposta:** 0 obras novas; nas fichas cujo conteúdo a fonte atribui a um livro já catalogado, o ciclo "
  "propõe **cross-reference** (B044, B039, B026, B017/B018), e as duas anunciadas vão para o relatório como "
  "radar datado — inclusive porque *daqui a um mês* é 26/04/2022, e a Base pode verificar depois se houve.")
w("")
w("**D-12 · Os nomes das pessoas na sala e do amigo espiritual.** Marcelo 5×, Solange, Mara, Lila 2×, Elô, "
  "Narras (U0050); `baiano` 8×; `Alagoan` 3×; e o nome dado como o espírito mais evoluído que a fonte "
  f"conhece: {aspa('francisco_paula')}. **Proposta:** ficam na transcrição (são o metadado da situação de "
  "enunciação) e **não** viram ficha, entidade nem relação; a regra de voz da casa vale: rótulo de locutor não "
  "afirma identidade civil.")
w("")
w("**D-13 · O estatuto desta fala.** Ela é **pedida** pelo vivo (U0010–U0019, onde a fonte refina o quadro da "
  f"guerra do Sol), tem **intervalo pedido ao vivo** — {aspa('pedido_intervalo')} (U0020; a palavra *interval* "
  f"aparece 3× no bruto). Logo antes dele a fonte diz que {aspa('titulo_parcial')}. **Proposta:** a apostila transcreve na ordem em que foi dita, com **nota de "
  "abertura** declarando o intervalo e o refinamento em público, e **sem** reorganizar as partes — a "
  "autodeclaração *só para meu estudo* vai no aparato porque limita o estatuto de uma formulação sem a "
  "apagar.")
w("")
w("**D-14 · Nada antes da resposta.** Este dossiê e as camadas são tudo o que a etapa 1 produziu. "
  "`termos/`, `RELACOES`, `ferramentas/dados_termos.py`, `livros/` e os builds **não** foram tocados. O "
  "BLOCO A só começa depois da devolutiva, e BLOCO A e BLOCO B vêm em commits separados.")
w("")
w("---")
w("")
w("## 6. O que o dossiê NÃO pede (para não parecer que pediu)")
w("")
w("- Não pede correção de grafia, nem de número, nem de pontuação do bruto.")
w("- Não pede novo código, nova relação, nova obra, nova ficha — salvo a exceção que V. Sa. vier a ordenar em D-9.")
w("- Não pede que a tese cristológica de U0034 seja promovida a definição canônica de nada.")
w("- Não pede silêncio sobre a depressão, o suicídio, a política ou o palavrão: pede **moldura** e **trânsito** "
  "controlado, que são coisas diferentes de censura.")
w("")
w("---")
w("")
w("## 7. Contadores medidos desta etapa")
w("")
w(f"- bruto: {num(L)} chars · {num(palavras)} palavras · {num(linhas)} linhas com texto · 11 linhas pesadas "
  f"(>3.000 c) · 24 falas curtas de plateia.")
w(f"- leitura: 9 chunks endereçados · mapa de 165 seções resolvidas por âncora (fim da última: caractere 145.408).")
w("- dicionário: 106 itens medidos, 11 ausências contadas, 15 famílias de grafas no §3.")
w(f"- anterioridade: 78 candidatos auditados na matriz · 21 com ganho de data · destes, {len(VINC)} códigos "
  f"entram no pacote de proposta (§2), com {sum(1 for c,_,_ in VINC if 'antecipa' in nota_ant(c))} ganhos de data.")
w("- auditor verbatim: portões A e B, resultado no rodapé deste arquivo ao final da rodada.")
w("")
w(f"*Gerado por `analise/_gerar_dossie_{SIGLA}.py` sobre `analise/_aspas_{SIGLA}.py` · "
  f"{datetime.date.today():%d/%m/%Y} · etapa 1 de 2 (⚠️ aguarda devolutiva).*")

txt = "\n".join(P) + "\n"
open(OUT, "w", encoding="utf-8").write(txt)

# as três substituições de âncoras longas que a prosa acima poupa de quebrar linhas
subs = {
 "{a}": aspa("tres_fornos"), "{b}": aspa("lucifer_criou_virus"), "{c}": aspa("isolou_mundos"),
 "{d}": aspa("onda_depressiva"), "{e}": aspa("javé_vishnu_chiva"), "{f}": aspa("diagnostico_humano"),
}
s2 = txt
for k, v in subs.items():
    s2 = s2.replace(k, v)
open(OUT, "w", encoding="utf-8").write(s2)

# relatório de aspas medidas (para o auditor)
n_aspas = s2.count("«")
print(f"dossiê escrito: {len(s2):,} chars · {n_aspas} aspas · {len(Q)} âncoras resolvidas · "
      f"{len(VINC)} vínculos · {len(OBS)} observações · {len(DIV)} divergências".replace(",", "."))
