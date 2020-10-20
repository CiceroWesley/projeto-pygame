import pygame,sys
from random import randint
from funcoes import *
from time import sleep

pygame.init()

#criando a tela
lagalt= (900,600)
tela = pygame.display.set_mode(lagalt)
fundo=pygame.image.load('imagens/fundo.png')

#música do jogo
pygame.mixer.music.load('sons/KoopaCastle.mp3')
pygame.mixer.music.play(-1)

#nome do jogo e icone
pygame.display.set_caption('Magic Shooters')
icone = pygame.image.load('imagens/hat.png')
pygame.display.set_icon(icone)

#jogador
jogadorfoto = pygame.image.load('imagens/clown.png')
jogadorX = 0
jogadorY = 300
jogadorXmuda=0
jogadorYmuda=0
dificuldade=1 #não utilizado ainda
vidas=3

#pontos
pontos=0
fonte = pygame.font.Font('fontes/OldLondon.ttf',32)
pontosX=0
pontosY=0
fontef = pygame.font.Font('fontes/OldLondon.ttf',64)

#inimigo
inimigofoto = []
inimigoX = []
inimigoY= []
inimigoXmuda=[]
inimigoYmuda=[]
inimigoATV=True
inimigos=5
for i in range(inimigos):
    
    inimigofoto.append(pygame.image.load('imagens/spiral.png'))
    inimigoX.append(randint(750,836))
    inimigoY.append(randint(0,536))
    inimigoXmuda.append(0)
    inimigoYmuda.append(3)

#bala jogador
balafoto = pygame.image.load('imagens/moon.png')
balaX=0
balaY=0
balaXmuda=8 #velocidade bala jogador
balaYmuda=0
balaatira=1

#bala inimigo
balaIfoto=[]
balaIX=[]
balaIY=[]
balaIXmuda=[]
balaIatira=[]
for i in range(inimigos):
    balaIfoto.append(pygame.image.load('imagens/taoism.png'))
    balaIX.append(0)
    balaIY.append(0)
    balaIXmuda.append(-7)
    balaIatira.append(1)

#print jogador
def jogador(x,y):
    tela.blit(jogadorfoto,(x,y))

#print inimigo
def inimigo(x,y,i):
    tela.blit(inimigofoto[i],(x,y))

#print bala do jogador
def bala(x,y):
    global balaatira
    balaatira=0
    tela.blit(balafoto,(x,y))

#print balas dos inimigos
def balaI(x,y,i):
    global balaIatira
    balaIatira[i]=0
    tela.blit(balaIfoto[i],(x,y))

#print pontos
def placar(x,y):
    ponto = fonte.render('Pontos:'+str(pontos),True,(0,255,0))
    tela.blit(ponto,(x,y))

#print vida
def life(x,y):
    vida = fonte.render('Vidas:'+str(vidas),True,(255,0,0))
    tela.blit(vida,(x,y))

#print dificuldade
def dificult(x,y):
    dificu = fonte.render('Dificuldade:'+str(dificuldade),True,(0,0,0))
    tela.blit(dificu,(x,y))

#print 'Vc morreu'
def gameover():
    fim = fontef.render('Vc morreu',True,(0,0,0))
    continua = fonte.render('Jogar de novo?(s ou n)',True,(0,0,0))
    tela.blit(fim,(300,250))
    tela.blit(continua,(310,315))

#print 'Parabens, vc passou de fase'
def passoudefase():
    vitoria = fontef.render('Parabens, vc passou de fase', True, (0, 0, 0))
    continua = fonte.render('Continuar?(s ou n)', True, (0, 0, 0))
    tela.blit(vitoria, (200, 250))
    tela.blit(continua, (310, 315))

#abertura
def animation():
    fundo2 = pygame.image.load('imagens/fundoab.png')
    running = True
    playerX = 150
    playerY = 260
    playerXmuda = 2.3
    playerYmuda = 0

    enemyX = []
    enemyY = []
    enemyXmuda = []
    enemyYmuda = []
    enemy = 5
    posY = [0,130,260,390,520]
    for i in range(enemy):

        #enemyfoto.append(pygame.image.load('imagens/spiral.png'))
        enemyX.append(0)
        enemyY.append(posY[i])
        enemyXmuda.append(2.50)
        enemyYmuda.append(0)
    while running:
        tela.blit(fundo2,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    running = False


        for i in range(enemy):
            enemyX[i] += enemyXmuda[i]
            inimigo(enemyX[i], enemyY[i], i)

        playerX+=playerXmuda
        jogador(playerX,playerY)
        pularanimacao = fonte.render('Pressiona P para pular...', True, (0,0,0))

        #print 'Pressiona P para pular...'
        if playerX > 50 and playerX < 1000:  #(50 é maior q 150)
            tela.blit(pularanimacao,(0,550))

        #print nome do jogo
        if playerX > 950:
            gamename = fontef.render('Magic Shooters',True,(0,0,0))
            tela.blit(gamename,(260,250)) #centralizar na tela

        if playerX > 1000:
            sleep(2)
            running=False
        pygame.display.update()

#jogo
def gameloop():
    #loop do jogo
    global jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira, pontos, vidas, dificuldade
    while True:

        tela.blit(fundo,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                #teclas para jogador se mover
                if evento.key == pygame.K_LEFT:
                    jogadorXmuda = -5
                if evento.key ==  pygame.K_RIGHT:
                    jogadorXmuda = 5
                if evento.key == pygame.K_UP:
                    jogadorYmuda = -5
                if evento.key == pygame.K_DOWN:
                    jogadorYmuda = 5

                #tecla z para atirar
                if evento.key == pygame.K_z:
                    if balaatira == 1:
                        balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                        balasom.play()
                        balaX=jogadorX
                        balaY=jogadorY+32 #32 para a bala sair no meio do jogador (32=64/2)
                        bala(balaX,balaY)

                #tecla h para inimigos pararem de atirar e suas balas não tem efeito
                if evento.key == pygame.K_h:
                    inimigoATV= False

                #tecla s para jogar de novo (codigo para reiniciar o jogo)
                if evento.key == pygame.K_s and (vidas==0 or pontos>=10):
                    vidas=3
                    pontos=0
                    jogadorX=0
                    jogadorY=300

                    #gerando os inimigos
                    for j in range(inimigos):
                        inimigoX[j] = randint(750,836)
                        inimigoY[j] = randint(0,536)

                #tecla n para sair quando jogo acabar
                if evento.key == pygame.K_n and (vidas==0 or pontos>=10):
                    pygame.quit()
                    sys.exit()
            if evento.type== pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_UP or evento.key==pygame.K_DOWN:
                    jogadorXmuda=0
                    jogadorYmuda=0
                if evento.key == pygame.K_h:
                    inimigoATV= True

        #jogador
        jogadorX+=jogadorXmuda
        jogadorY+=jogadorYmuda

        if jogadorX <=0:
            jogadorX=0
        if jogadorX >=836: #900-64=836
            jogadorX=836
        if jogadorY <=0:
            jogadorY=0
        if jogadorY >=536: #600-64=536
            jogadorY=536

        #inimigo
        for i in range(inimigos):
            inimigoY[i]+=inimigoYmuda[i]

            if inimigoY[i] >= 536: #600-64=536
                inimigoYmuda[i]=-3*dificuldade
                inimigoXmuda[i]=-25 #o inimigo se aproxima do jogador
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoY[i] <=0:
                inimigoYmuda[i]=3*dificuldade
                inimigoXmuda[i]=-25 #o inimigo se aproxima do jogador
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoX[i] <=0: #inimigo quando chega no limite da tela, aparece do outro lado
                inimigoXmuda[i]=836 #900-64=836
                inimigoX[i] += inimigoXmuda[i]

            #colisao com o inimigo
            colisao=colisaoCinimigo(inimigoX[i],inimigoY[i],balaX,balaY)
            if colisao == True:
                somCI = pygame.mixer.Sound('sons/acertainimigo.wav')
                #os volumes dos sons não estão iguais
                somCI.play()
                balaX=jogadorX
                balaatira=1
                pontos+=1
                inimigoX[i] = randint(750,836) #intervalo horizontal que o inimigo surge (836=900-64)
                inimigoY[i]= randint(0,536) #intervalo vertical que o inimigo surge (536=600-64)

            #salvando valores para gerar o inimigo novo
            inimigo(inimigoX[i],inimigoY[i],i)

            if inimigoATV== True:

            #bala inimigo
                #inimigo atirando ('criando' a bala)
                if balaIatira[i] == 1:
                    balaIX[i] = inimigoX[i]
                    balaIY[i] = inimigoY[i]+32 #+32 para a bala sair no meio do inimigo (32=64/2)
                    balaI(balaIX[i],balaIY[i],i)

            #inimigo atirando quando a bala desaparece do mapa
            if balaIX[i] <= 0:
                balaIX[i]=inimigoX[i]
                balaIatira[i]=1

            #deslocamento da bala
            if balaIatira[i] == 0:
                balaI(balaIX[i],balaIY[i],i)
                balaIX[i] += -7

            #colisao entre as balas
            colisaoB=colisaoCbalas(balaIX[i],balaIY[i],balaX,balaY)
            if colisaoB == True:
                balasomIJ = pygame.mixer.Sound('sons/acertabalas.wav')
                balasomIJ.play()
                balaX=jogadorX
                balaIX[i]=inimigoX[i]
                balaatira=1
                balaIatira[i]=1


            #colisao com o jogador
            colisaoJ = colisaoCjogador(jogadorX,jogadorY,balaIX[i],balaIY[i])
            if colisaoJ == True:
                somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
                somCJ.play()
                balaIX[i] = inimigoX[i]
                balaIatira[i]=1
                vidas-=1


            #colisao com o jogador e o inimigo
            colisaoJeI = colisaoCjogadorEinimigo(jogadorX,jogadorY, inimigoX[i],inimigoY[i])
            if colisaoJeI == True:
                somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
                somCJ.play()
                vidas=0 #morte automática do jogador, se encostar no inimigo

        #bala jogador
        if balaX >= 900:
             balaX = jogadorX
             balaatira=1

        if balaatira == 0:
             bala(balaX,balaY)
             balaX += balaXmuda


        #fim de jogo

        #erro achado #melhor elaborar o codigo para quando "acaba o jogo", pois o jogador ainda pode atirar e marcar pontos

        #ganhou
        if pontos >= 10:
            passoudefase()

            #aqui o "erro"
            for k in range(inimigos):
                inimigoX[k]=3000
                inimigoY[k]=3000
            jogadorX=1000
            jogadorY=0


        #perdeu
        elif vidas == 0:
            gameover()

            #aqui o "erro"
            for k in range(inimigos):
                inimigoX[k]=3000
                inimigoY[k]=3000
            jogadorX=1000
            jogadorY=0


        #print valores do jogo
        jogador(jogadorX,jogadorY)
        placar(pontosX,pontosY)
        life(0,27)
        dificult(750,0)

        #update da tela do jogo
        pygame.display.update()


#abertura do jogo
animation()

#jogo
gameloop()
