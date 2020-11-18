#nivel 1


#resertar fase 1 (colocando valores iniciais)
def resetarfase1():
    #criando a tela
    lagalt = (900, 600)
    tela = pygame.display.set_mode(lagalt)
    fundo1 = pygame.image.load('imagens/1.png')

    #jogador
    jogadorfoto = pygame.image.load('imagens/jogador.png')
    jogadorX = 0
    jogadorY = 300
    jogadorXmuda = 0
    jogadorYmuda = 0
    vidas = 3
    n = 1 #nivel 1

    #pontos
    pontos = 0
    fonte = pygame.font.Font('fontes/BebasNeue.ttf', 32)
    pontosX = 0
    pontosY = 0
    fontef = pygame.font.Font('fontes/BebasNeue.ttf', 64)

    #inimigo
    inimigofoto = []
    inimigoX = []
    inimigoY = []
    inimigoXmuda = []
    inimigoYmuda = []
    inimigoATV = True
    inimigos = 5
    for i in range(inimigos):
        inimigofoto.append(pygame.image.load('imagens/inimigo1.png'))
        inimigoX.append(randint(700, 836))  # 836=900-64
        inimigoY.append(randint(0, 536))  # 536=600-64
        inimigoXmuda.append(0)
        inimigoYmuda.append(3)

    #bala jogador
    balafoto = pygame.image.load('imagens/balajogador.png')
    balaX = 0
    balaY = 0
    balaXmuda = 8  # velocidade bala jogador
    balaYmuda = 0
    balaatira = 1

    # bala inimigo
    balaIfoto = []
    balaIX = []
    balaIY = []
    balaIXmuda = []
    balaIatira = []
    for i in range(inimigos):
        balaIfoto.append(pygame.image.load('imagens/tiro1.png'))
        balaIX.append(0)
        balaIY.append(0)
        balaIXmuda.append(-7)  # velocidade bala inimigo
        balaIatira.append(1)

    tela.blit(fundo1, (0, 0))

#print jogador
def jogador(x, y):
    tela.blit(jogadorfoto, (x, y))
#print inimigo
def inimigo(x, y, i):
    tela.blit(inimigofoto[i], (x, y))
#print bala do jogador
def bala(x, y):
    global balaatira
    balaatira = 0
    tela.blit(balafoto, (x, y))
#print balas dos inimigos
def balaI(x, y, i):
    global balaIatira
    balaIatira[i] = 0
    tela.blit(balaIfoto[i], (x, y))
#print pontos
def placar(x, y):
    ponto = fonte.render('Pontos:' + str(pontos), True, (0, 255, 0))
    tela.blit(ponto, (x, y))
#print vida
def life(x, y):
    vida = fonte.render('Vidas:' + str(vidas), True, (255, 0, 0))
    tela.blit(vida, (x, y))
#print nivel
def level(x, y):
    nivel = fonte.render('Dificuldade:' + str(n), True, (0, 0, 0))
    tela.blit(nivel, (x, y))


def gameover1():
    fim = fontef.render('Você morreu', True, (0, 0, 0))
    continua = fonte.render('Jogar de novo?(s ou n)', True, (0, 0, 0))
    tela.blit(fim, (300, 250))
    tela.blit(continua, (310, 315))
    tecla=''
    while tecla!='s' or tecla!='n' or tecla!='f':
        tecla=input()
    if tecla=='s' or tecla!='f':
        resetarfase1()
    if tecla!='n':
        pygame.quit()
        sys.exit()

def passoudefase():
    passou = fontef.render('Você passou de fase', True, (0, 0, 0))
    continua = fonte.render('Continuar?(s ou n)', True, (0, 0, 0))
    tela.blit(passou, (200, 250))
    tela.blit(continua, (310, 315))
    tecla = ''
    while tecla != 's' or tecla != 'n' or tecla != 'f':
        tecla = input()

    if tecla != 'n':
        pygame.quit()
        sys.exit()

def fase1():
    #fase1
    global n, jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira, pontos, vidas

    #usuario apertar algum botão (evento)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #usuario soltou o botao (keydown)
        if evento.type == pygame.KEYDOWN:
            # teclas para jogador se mover
            if evento.key == pygame.K_LEFT:
                jogadorXmuda = -5
            if evento.key == pygame.K_RIGHT:
                jogadorXmuda = 5
            if evento.key == pygame.K_UP:
                jogadorYmuda = -5
            if evento.key == pygame.K_DOWN:
                jogadorYmuda = 5

            # tecla secreta
            if evento.key == pygame.K_f:
                pontos = 10

            # tecla z para atirar
            if evento.key == pygame.K_z:
                if balaatira == 1:
                    balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                    balasom.play()
                    balaX = jogadorX
                    balaY = jogadorY + 32  # 32 para a bala sair no meio do jogador (32=64/2)
                    bala(balaX, balaY)

        #usuario soltou o botao (keyup)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jogadorXmuda = 0
                jogadorYmuda = 0

    #jogador
    jogadorX+=jogadorXmuda
    jogadorY+=jogadorYmuda

    if jogadorX<=0:
        jogadorX=0
    if jogadorX>=836: #900-64=836
        jogadorX=836
    if jogadorY<=0:
        jogadorY=0
    if jogadorY>=536: #600-64=536
        jogadorY=536

    #inimigo
    for i in range(inimigos):
        inimigoY[i] += inimigoYmuda[i]

        if inimigoY[i]>=536:  # 600-64=536
            inimigoYmuda[i]=-3 * n
            inimigoXmuda[i]=-25  # o inimigo se aproxima do jogador
            inimigoX[i]+=inimigoXmuda[i]
        if inimigoY[i]<=0:
            inimigoYmuda[i]=3 * n
            inimigoXmuda[i]=-25  # o inimigo se aproxima do jogador
            inimigoX[i] += inimigoXmuda[i]
        if inimigoX[i] <= 0:  # inimigo quando chega no limite da tela, aparece do outro lado
            inimigoXmuda[i] = 836  # 900-64=836
            inimigoX[i] += inimigoXmuda[i]

        #colisao com o inimigo
        colisao = colisaoCinimigo(inimigoX[i], inimigoY[i], balaX, balaY)
        if colisao == True:
            somCI = pygame.mixer.Sound('sons/acertainimigo.wav')
            # os volumes dos sons não estão iguais
            somCI.play()
            balaX = jogadorX
            balaatira = 1
            pontos += 1
            inimigoX[i] = randint(750, 836)  # intervalo horizontal que o inimigo surge (836=900-64)
            inimigoY[i] = randint(0, 536)  # intervalo vertical que o inimigo surge (536=600-64)

        #salvando valores para gerar o inimigo novo
        inimigo(inimigoX[i], inimigoY[i], i)

        if inimigoATV == True:

            #bala inimigo
            #inimigo atirando ('criando' a bala)
            if balaIatira[i] == 1:
                balaIX[i] = inimigoX[i]
                balaIY[i] = inimigoY[i] + 32  # +32 para a bala sair no meio do inimigo (32=64/2)
                balaI(balaIX[i], balaIY[i], i)

        #inimigo atirando quando a bala desaparece do mapa
        if balaIX[i] <= 0:
            balaIX[i] = inimigoX[i]
            balaIatira[i] = 1

        #deslocamento da bala
        if balaIatira[i] == 0:
            balaI(balaIX[i], balaIY[i], i)
            balaIX[i] += -7

        #colisao entre as balas
        colisaoB = colisaoCbalas(balaIX[i], balaIY[i], balaX, balaY)
        if colisaoB == True:
            balasomIJ = pygame.mixer.Sound('sons/acertabalas.wav')
            balasomIJ.play()
            balaX = jogadorX
            balaIX[i] = inimigoX[i]
            balaatira = 1
            balaIatira[i] = 1

        #colisao com o jogador
        colisaoJ = colisaoCjogador(jogadorX, jogadorY, balaIX[i], balaIY[i])
        if colisaoJ == True:
            somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
            somCJ.play()
            balaIX[i] = inimigoX[i]
            balaIatira[i] = 1
            vidas -= 1

        #colisao com o jogador e o inimigo
        colisaoJeI = colisaoCjogadorEinimigo(jogadorX, jogadorY, inimigoX[i], inimigoY[i])
        if colisaoJeI == True:
            somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
            somCJ.play()
            vidas = 0  # morte automática do jogador, se encostar no inimigo

    #bala jogador
    if balaX >= 900:
        balaX = jogadorX
        balaatira = 1

    if balaatira == 0:
        bala(balaX, balaY)
        balaX += balaXmuda

    #print valores do jogo
    jogador(jogadorX, jogadorY)
    placar(pontosX, pontosY)
    life(0, 27)
    level(750, 0)

    # update da tela do jogo
    pygame.display.update()