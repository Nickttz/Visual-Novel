# ---------------------------------------------------------
# DEFINIÇÕES DE PERSONAGENS
# ---------------------------------------------------------

define m = Character("Matthew")
define a = Character("Ashley")
define tj = Character("Thomas Jr.")
define t = Character("Thomas")
define j = Character("Judy Littlewell")
define npc = Character("???")
define h = Character("Morador de rua")
define p = Character("Pensamentos")

# Flags
default viu_judy_amanha = False

# ---------------------------------------------------------
# CAPÍTULO 1
# ---------------------------------------------------------


label start:

    scene bg apartamento
    with fade

    # -----------------------------
    # CENA 1 — A DISCUSSÃO
    # -----------------------------

    "O apartamento está silencioso… silencioso demais."
    "Até que a porta do quarto se abre com força."
    play sound porta_forte
    pause(2.0)

    show ashley irritada
    a "Matthew, sério…? Você chegou atrasado de novo, nem avisou, e ainda age como se não fosse nada demais!"
    a "E ainda por cima bate a porta desse jeito??!!"

    m "Ashley, eu só perdi a hora. O dia foi uma merda, eu—"

    show ashley cruzado
    a "E você nunca escuta! Nunca leva nada a sério! Eu falo, falo… e parece que tô conversando com uma parede!"

    "A tensão no ar é quase palpável. Matthew sente o estômago afundar."

    menu:
        "Responder com calma":
            jump final_pacifico

        "Responder grosso":
            jump briga_principal


# --- FINAL ALTERNATIVO (GAME OVER PACÍFICO) ---

label final_pacifico:

    m "Ashley… você tem razão. Eu tô errado. A gente precisa conversar, não brigar."

    show ashley surpresa
    a "Matthew… eu… não esperava que você dissesse isso."
    a "Vamos tentar resolver isso juntos."

    scene black
    with fade

    centered "FINAL ALTERNATIVO — AMADURECIMENTO PREMATURO"
    centered "Fim do jogo"

    return


# --- LINHA DO TEMPO PRINCIPAL ---

label briga_principal:

    m "Ah, pronto! Lá vem você dizer que eu nunca faço nada direito!"
    m "Você reclama de tudo, Ashley! Tudo!"

    show ashley discutindo:
        zoom 1.15
    a "Matthew… acabou. Eu tô cansada. De verdade. Acabou."

    m "Ashley… não. Espera. Eu—"

    show ashley apontando:
        zoom 1.25
    a "Matthew. Saia agora. Por favor."

    "A palavra 'por favor' dói mais que um grito."

    scene black
    with fade

    play sound porta
    pause(1.0)

    jump bar_presente


# -----------------------------
# CENA 2 — O BAR NO PRESENTE
# -----------------------------

label bar_presente:
    
    "Mais tarde no bar..."
    scene black
    with fade
    
    play music som_bar_presente
    
    scene bg bar_present

    m "Uma bebida... depois outra... e outra..."

    show thomasjr falando
    tj "Cara, você tá bem? Parece que tomou um pé do tamanho da Austrália. Sou Thomas Jr."

    m "Matthew. Muito prazer..."

    menu:
        "Ela terminou comigo porque eu sou um merda…":
            show thomasjr falando
            tj "Um merda? Cara, você acabou de tentar beber o saleiro."
            show thomasjr questionando
            tj "E também, não sou terapeuta."

        "A culpa é dela! Eu estava certo em tudo!":
            show thomasjr questionando
            tj "Beleza… mas você percebeu que tá dizendo isso pra um copo vazio né?"

    # Escolhas de bêbado
    menu:
        "Achye urusimams kiashsiw?":
            show thomasjr falando
            tj "O quê? Tá falando russo? Acho melhor esse ser seu último copo."

        "A física quântica temporal tá fazendo a Nasa tirar foto da Lua por um relógio... tenho provas!":
            show thomasjr questionando
            tj "A Nasa podia fazer você parar de beber, senão vai destruir meu bar."

    m "Eu... vou só... ali... dar uma volta..."
    
    scene black
    with dissolve
    stop music

    jump acorda_1950


# -----------------------------
# CENA 3 — 1950?!
# -----------------------------

label acorda_1950:
    
    scene black
    with fade
    "Enquanto Matthew voltava para casa, ele apagou na rua de tão bêbado..."
    "Após umas horas, ele acordou na rua com todos em volta dele o encarando."
    with dissolve

    scene bg street_1950
    
    play music murmuro
    
    npc "É um artista experimental?"
    npc "Ou será que ele tá possuído?"

    m "Uhhh... onde...?"

    menu:
        "Ignorar e sair correndo":
            m "SAIAM DA FRENTE SEUS ESQUISITOS!!!"
            m "AAAAAAAAAAH!!"
            npc "Esse cara saiu do hospício?!"
            play sound carro_freio
            pause(1.7)
            npc "EI! VOCÊ NÃO PODE CORRER NO MEIO DA RUA ASSIM!"
            npc "Quase virou um tapete humano!"
            npc "Se continuar assim, não chega nem no almoço de domingo."
        
        "Ofender e sair correndo":
            m "Qual é o circo? Vocês tão vestidos como se a vida de vocês tivesse parado em preto e branco."
            npc "QUE GROSSO!!"
            npc "Esse moleque chegou do nada e insultou nossas roupas!"
            npc "Melhor que isso só se mijasse no poste."
            npc "Claramente é só um idiota mesmo!"
            m "Você está vestido igual meu avô num casamento e EU que sou o idiota?!"
            npc "PEGUEM ELE!"
            m "ATÉ NO PASSADO TEM GENTE SEM NADA PRA FAZER??!!"

    stop music
    "Após Matthew correr e despistar as pessoas, ele encontrou uma banca de jornal."
    
    m "Ham!? Uma banca de jornal..."
    
    scene bg journal
    
    m "Data: 1950."

    m "Cara… que merda eu bebi ontem?!"
    
    scene black
    "Matthew voltou para o bar para reencontrar o Thomas Jr."
    with fade

    jump bar_passado


# -----------------------------
# CENA 4 — O BAR NO PASSADO
# -----------------------------

label bar_passado:

    scene bg bar_1950

    play music som_bar_passado
    
    m "Meu Deus, o que houve aqui!!??"
    
    show thomas falando
    t "Você parece perdido, rapaz. Quer uma água? Ou um médico?"

    m "Cadê o Thomas Jr.?"

    show thomas falando_fechado
    t "Junior? Meu filho? Ele tá no colégio."

    p "Voltei no tempo...?"

    stop music
    
    jump palco_judy


# -----------------------------
# CENA 5 — O PALCO E JUDY LITTLEWELL
# -----------------------------

label palco_judy:

    scene bg stage_1950

    play sound aplausos

    npc "Senhoras e senhores, com vocês… a maravilhosa Judy Littlewell!"

    j "Obrigada, obrigada...!"

    stop sound

    scene black
    with fade
    "Judy Littlewell encarou curiosamente Matthew a maior parte de sua apresentação até ela se encerrar..."
    with dissolve
    
    play music som_bar_passado
    
    scene bg bar_1950

    m "Eu preciso de um drink..."
    show thomas falando
    t "É pra já!"
    
    scene bg bar_1950
    
    m "..."
    
    "Um toque inesperado no ombro interrompe seus pensamentos."

    pause(0.3)

    show judy curiosa
    j "Ei... você veio de onde? Nunca vi alguém vestido assim."

    m "Eu... vim de um país muito distante."

    show judy falando
    j "Hahaha! Caubói galáctico!"
    
    m "Aliás, deixa eu te perguntar... por que vocês todos parecem figurantes de um episódio antigo do Mickey?"

    show judy curiosa
    j "Mickey? Quem é esse? Algum estilista do seu país distante?"
    
    m "Ah… deixa pra lá. Se eu te explicar, vou parecer ainda mais maluco do que já tô parecendo."
    
    show judy rindo
    j "Hahahaha você é muito engraçado!"
    
    show judy risada_apaixonada
    j "Eu sei que já fui apresentada para você, mas Judy Littlewell é só o meu nome artístico. Eu me chamo Judy Miller, mas pode só me chamar de Judy"
    
    m "Ah... prazer, eu me chamo Matthew. Até que seu nome artístico é muito da hora!!"
    
    show judy rindo
    j "Muito da hora? O que isso quer dizer? Enfim haha..."
    j "Prazer em te conhecer Matthew!"
    
    m "O prazer é todo meu."

    scene black
    with fade
    "Após 2 horas de conversa..."
    with dissolve
    
    scene bg bar_1950
    
    show judy desabafando
    j "Sabe... sonho em crescer na carreira... mas aqui é difícil. Muito difícil."

    m "Você seria uma excelente cantora. Sério."

    show judy risada_apaixonada
    j "Obrigada..."

    jump fim_da_noite


# -----------------------------
# CENA 6 — O ENCERRAMENTO DA NOITE
# -----------------------------

label fim_da_noite:

    show judy lembrando
    j "Ah não... já está tão tarde!"

    show judy risada_leve
    j "Você acha que eu vou te ver de novo? Amanhã… no mesmo local? No mesmo horário?"

    menu:
        "SIM, eu venho amanhã":
            $ viu_judy_amanha = True
            jump escolha_sim

        "NÃO, é melhor não nos vermos de novo":
            $ viu_judy_amanha = False
            jump escolha_nao


label escolha_sim:
    show judy risada_leve
    j "Então… até amanhã, Matthew-do-país-estranho. Não me faça esperar!"
    
    show judy beijando
    "Judy beija a bochecha de Matthew."
    pause(3)
    
    scene bg bar_1950
    
    show thomas falando_fechado
    t "Ela é encantadora, não é? Os homens daqui são loucos por ela!"
    t "Para a sua sorte, eu acho ela gostou de você."
    show thomas falando
    t "Só não estrague tudo com essas roupas futuristas."

    m "Futuristas?"
    show thomas falando_fechado
    t "Você parece artista experimental... daqueles que apanham muito."

    stop music
    jump caminho_noite


label escolha_nao:

    show judy falando
    j "Entendo… às vezes a vida chama mais alto que a gente."
    show judy risada_apaixonada
    j "Mesmo assim… obrigada pela companhia."

    scene bg bar_1950

    show thomas falando_fechado
    t "Você cria drama mais rápido que novela de rádio!"

    m "Obrigado... eu acho."

    stop music
    jump caminho_noite


# -----------------------------
# CENA 7 — CAMINHO DE VOLTA
# -----------------------------

label caminho_noite:

    scene black
    with fade
    "Depois que Judy se despediu, Matthew caminhou sem direção pela rua, tentando entender a confusão temporal e emocional em que tinha se metido."
    with dissolve
    
    play music night_ambiente
    scene bg street_1950_night

    m "Tá… calma. Respira."
    m "Eu realmente tô nos anos 50. Anos. Cinquenta."
    m "E acabei de conversar por DUAS horas com uma cantora que parece ter saído direto de um pôster antigo de refrigerante."

    m "Ela era… legal. Até demais."
    m "A Ashley uma vez mencionou que a avó dela era uma estrela de bar dos anos 50…"

    m "..."

    m "Pera aí."
    m "Como era mesmo o nome da avó da Ashley?"
    m "Judy… alguma coisa. Judy… Mi…"

    m "…"

    m "MILL..."

    play sound danger
    m "MILLER!!"

    play music suspense_piano
    m "NÃO. NÃO. NÃO, NÃO, NÃO—"

    m "SE AQUELA JUDY É A MESMA JUDY MILLER—"
    m "ENTÃO EU ACABEI DE FLERTAR SEM QUERER COM A AVÓ DA MINHA EX."

    m "Meu Deus."
    m "Eu virei um problema psicanalítico intergeracional."

    m "Ok, Matthew. Foco."
    m "Você precisa andar com mais cuidado."
    m "Bem mais cuidado."
    m "Tipo… ‘não respira forte pra não alterar a linha do tempo’."

    m "Se eu fizer alguma besteira aqui… sei lá…"
    m "Talvez eu volte pro presente e descubra que deixei de existir."
    m "Ou pior: que a Ashley existe… mas com minha personalidade."
    m "Ser avô da minha ex seria completamente bizarro."
    m "...isso seria MUITO aterrorizante."
    m "Bom... pelo menos ela herdou a beleza da avó, se for ela mesmo..."

    stop music
    
    scene bg dog
    play sound latido
    npc "Au au!"
    m "AH—"
    m "Cara… até o cachorro tá me julgando."
    m "Obrigado, amigo. Realmente precisava de mais pressão existencial hoje."
    
    play music night_ambiente
    
    scene bg street_1950_night
    
    m "Bom, agora preciso decidir o que fazer..."

    # Menu que não muda a história (todas voltam pro presente)
    menu:
        "Investigar a cidade":
            pass
        "Voltar ao bar para falar com Thomas":
            pass
        "Procurar um quarto barato":
            pass
        "Seguir Judy discretamente":
            pass

    scene black
    with fade

    stop music

    jump volta_presente

# -----------------------------
# FINAL DO CAPÍTULO — VOLTA AO PRESENTE
# -----------------------------

label volta_presente:

    scene black
    with fade
    "Após Matthew seguir seu caminho, ele tropeçou e caiu no chão."
    with dissolve
    
    play music street_cars
    
    scene bg mendigo
    h "Mas o quê!? Ele apareceu do nada?!"
    m "MAS QUE PO@$# ACABOU DE ACONTECER!!!??"
    
    scene bg street_present
    
    show mendigo_entediado
    h "Você tem super-poderes?"
    m "Como assim?"
    h "Você apareceu do nada e ainda acordou falando sozinho."
    h "Ou isso… ou cachaça é mais forte do que eu imaginava."
    m "Eu não tenho super-poderes!"
    h "Então tem uns trocados pra mim?"
    m "..."
    h "O poder de sumir com dinheiro dos outros você deve ter, né?"

    if viu_judy_amanha:

        m "Tem algum espelho aí?"
        show mendigo_vantagi
        h "Tenho um quebrado... se me der uns trocados."
        m "Toma."
        
        scene bg street_present
        
        show mendigo_entediado
        h "Tá aqui."
        h "Mas cuidado... ele mostra a verdade. Eu mesmo parei de usar."
        m "Minha bochecha... tem batom?!"
        m "QUE CARA@$# TÁ ACONTECENDO??"
        h "Batom na bochecha…"
        h "No meu tempo isso era sinal de encontro."
        h "Hoje em dia é só sinal de que você é facilmente enganável."
        m "Talvez você esteja certo..."

    else:

        m "Minha mão... glitter?!"
        m "Isso é dela?!"
        m "ENTÃO NÃO ERA UM SONHO!!!"
        h "Relaxa, glitter gruda mais que boleto atrasado."
        h "Se fosse radiação, você já teria virado super-herói."

    scene black
    with fade
    
    centered "FIM DO CAPÍTULO 1"
    
    return