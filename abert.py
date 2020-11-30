import pygame,sys
from random import randint
#from funcoes import *
from jog import *
from ini import *
from outros import *
from time import sleep

pygame.init()


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


