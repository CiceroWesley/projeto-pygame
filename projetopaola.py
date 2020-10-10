import pygame,sys
from pygame.locals import *
from random import randint
from funcoes import *

pygame.init()

#criando a tela
lagalt= (900,600)
tela = pygame.display.set_mode(lagalt)

fundo=pygame.image.load('imagens/fundo.png')

pygame.mixer.music.load('sons/KoopaCastle.mp3')
pygame.mixer.music.play(-1)


#nome do jogo e icone
pygame.display.set_caption('Magic')
icone = pygame.image.load('imagens/hat.png')
pygame.display.set_icon(icone)

#jogador
jogadorfoto = pygame.image.load('imagens/clown.png')
jogadorX = 0
jogadorY = 300
jogadorXmuda=0
jogadorYmuda=0
dificuldade=1
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

def jogador(x,y):
    tela.blit(jogadorfoto,(x,y))

def inimigo(x,y,i):
    tela.blit(inimigofoto[i],(x,y))

def bala(x,y):
    global balaatira
    balaatira=0
    tela.blit(balafoto,(x,y))

def balaI(x,y,i):
    global balaIatira
    balaIatira[i]=0
    tela.blit(balaIfoto[i],(x,y))


def placar(x,y):
    ponto = fonte.render('Pontos:'+str(pontos),True,(0,255,0))
    tela.blit(ponto,(x,y))

def life(x,y):
    vida = fonte.render('Vidas:'+str(vidas),True,(255,0,0))
    tela.blit(vida,(x,y))

def dificult(x,y):
    dificu = fonte.render('Nível:'+str(dificuldade),True,(0,0,0))
    tela.blit(dificu,(x,y))

def gameover():
    fim = fontef.render('FIM DE JOGO',True,(0,0,0))
    continua = fonte.render('Continuar?(s ou n)',True,(0,0,0))
    tela.blit(fim,(300,250))
    tela.blit(continua,(310,315))
def gameloop():
    #loop do jogo
    global jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira, pontos, vidas, dificuldade
    while True:

        #tela.fill((0,0,0))
        tela.blit(fundo,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogadorXmuda = -3
                if evento.key ==  pygame.K_RIGHT:
                    jogadorXmuda = 3
                if evento.key == pygame.K_UP:
                    jogadorYmuda = -3
                if evento.key == pygame.K_DOWN:
                    jogadorYmuda = 3
                if evento.key == pygame.K_z:
                    if balaatira == 1 :
                        balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                        balasom.play()
                        balaX=jogadorX
                        balaY=jogadorY
                        bala(balaX,balaY)
                if evento.key == pygame.K_h:
                    inimigoATV= False
                if evento.key == pygame.K_s and vidas==0:
                    vidas=3
                    pontos=0
                    dificuldade=1
                    jogadorX=0
                    jogadorY=300
                    for j in range(inimigos):
                        inimigoX[j] = randint(750,836)
                        inimigoY[j] = randint(0,536)
                if evento.key == pygame.K_n and vidas==0:
                    pygame.mixer.music.stop #colocar isso em outro canto
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
        if jogadorX >=800:
            jogadorX=800
        if jogadorY <=0:
            jogadorY=0
        if jogadorY >=536:
            jogadorY=536

        #inimigo
        for i in range(inimigos):
            inimigoY[i]+=inimigoYmuda[i]

            if inimigoY[i] >= 536:
                inimigoYmuda[i]=-3*dificuldade
                inimigoXmuda[i]=-25
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoY[i] <=0:
                inimigoYmuda[i]=3*dificuldade
                inimigoXmuda[i]=-25
                inimigoX[i]+=inimigoXmuda[i]
            if inimigoX[i] <=450:
                inimigoXmuda[i]=386
                inimigoX[i] += inimigoXmuda[i]
            #if inimigoX[i] >=900:
             #   inimigoXmuda[i]=25
              #  inimigoX[i]+=inimigoXmuda[i]
            #colisao com o inimigo
            colisao=colisaoCinimigo(inimigoX[i],inimigoY[i],balaX,balaY)
            if colisao == True:
                somCI = pygame.mixer.Sound('sons/acertainimigo.wav')
                #um pouco atrasado,cortar mais
                somCI.play()
                balaX=jogadorX
                balaatira=1
                pontos+=1
                inimigoX[i] = randint(750,836)
                inimigoY[i]= randint(0,536)
            inimigo(inimigoX[i],inimigoY[i],i)
            if inimigoATV== True:
                if balaIatira[i] == 1:
                    balasomI=pygame.mixer.Sound('sons/fogoinimigo.wav')
                    balasomI.play()
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
            colisaoJ = colisaoCjogador(jogadorX,jogadorY+32,balaIX[i],balaIY[i])
            if colisaoJ == True:   #emcima não pega nele
                somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
                somCJ.play()
                balaIX[i] = inimigoX[i]
                balaIatira[i]=1
                vidas-=1
        #bala jogador
        if balaX >=900:
             balaX = jogadorX
             balaatira=1

        if balaatira == 0:
             bala(balaX,balaY)
             balaX += balaXmuda
        #dificuldade
        if pontos==10:
            dificuldade=2
        elif pontos==20:
            dificuldade=3
        elif pontos==40:
            dificuldade=4
        #fim de jogo
        if vidas == 0:
            gameover()
            for k in range(inimigos):
                inimigoX[k]=3000
                inimigoY[k]=3000
            jogadorX=3000
            jogadorY=3000
        jogador(jogadorX,jogadorY)
        placar(pontosX,pontosY)
        life(0,27)
        dificult(800,0)
        pygame.display.update()
gameloop()
