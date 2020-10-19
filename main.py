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
dificuldade=1  #alterar a dificuldade no menu inciail em 1, 2 e 3. (há ser feito)
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
for i in range(inimigos): #5 inimigos toda hora
    
    inimigofoto.append(pygame.image.load('imagens/spiral.png'))
    inimigoX.append(randint(750,836))
    inimigoY.append(randint(0,536))
    inimigoXmuda.append(0)
    inimigoYmuda.append(3)

#bala jogador
balafoto = pygame.image.load('imagens/moon.png')
balaX=0
balaY=0
balaXmuda=8
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
    tela.blit(balafoto,(x,y+16))

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

#nova funçao - print passar fase
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
                if evento.key == pygame.K_LEFT:
                    jogadorXmuda = -5 #aumentei a velocidade de 3 para 5 do jogador
                if evento.key ==  pygame.K_RIGHT:
                    jogadorXmuda = 5
                if evento.key == pygame.K_UP:
                    jogadorYmuda = -5
                if evento.key == pygame.K_DOWN:
                    jogadorYmuda = 5
                if evento.key == pygame.K_z:
                    if balaatira == 1 :
                        balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                        balasom.play()
                        balaX=jogadorX
                        balaY=jogadorY
                        bala(balaX,balaY)
                if evento.key == pygame.K_h:
                    inimigoATV= False
                if evento.key == pygame.K_s and (vidas==0 or pontos>=10): #estabeleci como sendo 10 pontos para acabar a fase
                    vidas=3
                    pontos=0
                    #dificuldade=1 dificuldade vai para o menu inicial do jogo (há ser feito)
                    jogadorX=0
                    jogadorY=300
                    for j in range(inimigos):
                        inimigoX[j] = randint(750,836)
                        inimigoY[j] = randint(0,536)
                if evento.key == pygame.K_n and (vidas==0 or pontos>=10):
                    #pygame.mixer.music.stop #colocar isso em outro canto
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
                inimigoYmuda[i]=-3*dificuldade #aumento de velocidade vertical do inimigo com a dificuldade
                inimigoXmuda[i]=-25
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoY[i] <=0:
                inimigoYmuda[i]=3*dificuldade #aumento de velocidade vertical do inimigo com a dificuldade
                inimigoXmuda[i]=-25
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoX[i] <=450:
                inimigoXmuda[i]=386
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
                inimigoX[i] = randint(750,836)
                inimigoY[i]= randint(0,536)
            inimigo(inimigoX[i],inimigoY[i],i)
            if inimigoATV== True:
                if balaIatira[i] == 1:
                    #balasomI=pygame.mixer.Sound('sons/fogoinimigo.wav')
                    #balasomI.play()
                    balaIX[i] = inimigoX[i]
                    balaIY[i] = inimigoY[i]
                    balaI(balaIX[i],balaIY[i],i)
            #bala inimigo
            if balaIX[i]<=0:
                balaIX[i]=inimigoX[i]
                balaIatira[i]=1

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
            if colisaoJ == True:   #emcima não pega nele
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
                vidas-=1 #por algum motivo dá morte automática do jogador

        #bala jogador
        if balaX >=900:
             balaX = jogadorX
             balaatira=1

        if balaatira == 0:
             bala(balaX,balaY)
             balaX += balaXmuda
        #níveis


        #fim de jogo

        #ganhou
        if pontos >=10:
            passoudefase()
            for k in range(inimigos):
                inimigoX[k]=3000
                inimigoY[k]=3000
            jogadorX=3000
            jogadorY=3000
            #dificuldade era pra aumentar em 1 quando passa de fase
            #dificuldade += 1 #bugou quando fiz isso

        #perdeu
        elif vidas == 0:
            gameover()
            for k in range(inimigos):
                inimigoX[k]=3000
                inimigoY[k]=3000
            jogadorX=3000
            jogadorY=3000
            #dificuldade = 1 #quando morrer, dificuldade volta a ser 1

        jogador(jogadorX,jogadorY)
        placar(pontosX,pontosY)
        life(0,27)
        dificult(750,0)
        pygame.display.update()

animation() #abertura do jogo

gameloop() #jogo
