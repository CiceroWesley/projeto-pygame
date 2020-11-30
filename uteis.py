'''
try:
    imports..
except:
    print("Erro na importação.")
'''

import pygame, sys
from random import randint
from colisoes import colisaoCinimigo, colisaoCbalas, colisaoCjogador, colisaoCjogadorEinimigo
from impressoes import jogador, bala, inimigo, balaI, placar, life, level

def resetarfase(n):
    #definindo o valor de todas as globais
    global lagalt, tela, jogadorfoto, fonte, fontef
    lagalt = (900, 600)
    tela = pygame.display.set_mode(lagalt)
    jogadorfoto = pygame.image.load('imagens/jogador.png')
    fonte = pygame.font.Font('fontes/BebasNeue.ttf', 32)
    fontef = pygame.font.Font('fontes/BebasNeue.ttf', 64)
    global vidas, pontos, jogadorX, jogadorY, jogadorXmuda, jogadorYmuda
    vidas = 3
    pontos = 0
    jogadorX = 0
    jogadorY = 300
    jogadorXmuda = 0
    jogadorYmuda = 0
    global pontosX, pontosY, balafoto, balaX, balaY, balaXmuda, balaYmuda, balaatira
    pontosX = 0
    pontosY = 0
    balafoto = pygame.image.load('imagens/balajogador.png')
    balaX = 0
    balaY = 0
    balaXmuda = 8  # velocidade bala jogador
    balaYmuda = 0
    balaatira = 1
    global balaIfoto, balaIX, balaIY, balaIXmuda, balaIatira, balasom
    balaIfoto = []
    balaIX = []
    balaIY = []
    balaIXmuda = []
    balaIatira = []
    balasom = pygame.mixer.Sound('sons/fogojogador.wav')
    global inimigos, inimigoATV, inimigofoto, inimigoX, inimigoY, inimigoXmuda, inimigoYmuda
    inimigos = 5
    inimigoATV = True
    inimigofoto = []
    inimigoX = []
    inimigoY = []
    inimigoXmuda = []
    inimigoYmuda = []

    if n == 1:
        fundo1 = pygame.image.load('imagens/1.png')
        tela.blit(fundo1, (0, 0))
    if n == 2:
        fundo2 = pygame.image.load('imagens/2.png')
        tela.blit(fundo2, (0, 0))
    if n == 3:
        fundo3 = pygame.image.load('imagens/3.png')
        tela.blit(fundo3, (0, 0))        
    
    #jogador
    jogadorX = 0
    jogadorY = 300
    jogadorXmuda = 0
    jogadorYmuda = 0
    vidas = 3

    #pontos
    pontos = 0
    pontosX = 0
    pontosY = 0

    #inimigo
    inimigofoto = []
    inimigoX = []
    inimigoY = []
    inimigoXmuda = []
    inimigoYmuda = []
    inimigoATV = True
    inimigos = 5
    for i in range(inimigos):
        if n == 1:
            inimigofoto.append(pygame.image.load('imagens/inimigo1.png'))
        if n == 2:
            inimigofoto.append(pygame.image.load('imagens/inimigo2.png'))
        if n == 3:
            inimigofoto.append(pygame.image.load('imagens/inimigo1.png'))
        inimigoX.append(randint(700, 836))  #900-64=836
        inimigoY.append(randint(0, 536))  #600-64=536
        inimigoXmuda.append(0)
        inimigoYmuda.append(3*n) #velocidade do inimigo aumenta com a fase

    #bala jogador
    balaX = 0
    balaY = 0
    balaXmuda = 8
    balaYmuda = 0
    balaatira = 1

    #bala inimigo
    balaIfoto = []
    balaIX = []
    balaIY = []
    balaIXmuda = []
    balaIatira = []
    for i in range(inimigos):
        if n == 1:
            balaIfoto.append(pygame.image.load('imagens/tiro1.png'))
        if n == 2:
            balaIfoto.append(pygame.image.load('imagens/tiro2.png'))
        if n == 3:
            balaIfoto.append(pygame.image.load('imagens/tiro3.png'))
        balaIX.append(0)
        balaIY.append(0)
        balaIXmuda.append(-5)
        balaIatira.append(1)

def movimentajogador():
    global jogadorX, jogadorY, jogadorXmuda, jogadorYmuda
    jogadorX += jogadorXmuda
    jogadorY += jogadorYmuda

    if jogadorX <= 0:
        jogadorX = 0
    if jogadorX >= 836:  # 900-64=836
        jogadorX = 836
    if jogadorY <= 0:
        jogadorY = 0
    if jogadorY >= 536:  # 600-64=536
        jogadorY = 536

def esperar():
    #esperar usuario apertar s, f, n ou fechar o programa
    for evento in pygame.event.get():
        while evento.key != pygame.K_s or evento.key != pygame.K_f or evento.key != pygame.K_n or evento.type != pygame.QUIT:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_n or evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

#printar que morreu
def gameover(n):
    global tela,fonte,fontef
    morte = fontef.render('Você morreu', True, (0, 0, 0))
    denovo = fonte.render('Jogar de novo? (s ou n)', True, (0, 0, 0))
    tela.blit(morte, (300, 250))
    tela.blit(denovo, (310, 315))

    esperar()

#printar que passou de fase
def passoudefase():
    global tela,fonte,fontef
    passou = fontef.render('Você passou de fase', True, (0, 0, 0))
    continua = fonte.render('Continuar? (s ou n)', True, (0, 0, 0))
    tela.blit(passou, (200, 250))
    tela.blit(continua, (310, 315))

    esperar()


def checarevento():
    global jogadorXmuda, jogadorYmuda, pontos, balaatira, balasom, balaX, balaY
    try:
        #usuario
        for evento in pygame.event.get():
            #fechar o programa
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #apertar algum botao (keydown)
            if evento.type == pygame.KEYDOWN:
                #teclas para jogador se mover
                if evento.key == pygame.K_LEFT:
                    jogadorXmuda = -5
                if evento.key == pygame.K_RIGHT:
                    jogadorXmuda = 5
                if evento.key == pygame.K_UP:
                    jogadorYmuda = -5
                if evento.key == pygame.K_DOWN:
                    jogadorYmuda = 5

                #tecla secreta (f)
                if evento.key == pygame.K_f:
                    pontos = 10

                #atirar (z)
                if evento.key == pygame.K_z:
                    if balaatira == 1:
                        balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                        balasom.play()
                        balaX = jogadorX
                        balaY = jogadorY + 32  #32 para a bala sair no meio do jogador (64/2=32)
                        bala(balaX, balaY,tela,balafoto)
                        balaatira = 0

            #soltar algum botao (keyup)
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    jogadorXmuda = 0
                    jogadorYmuda = 0
    except KeyboardInterrupt:
        print("Execução interrompida.")

def movimentainimigo(n):
    global pontos,vidas,inimigos,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda,inimigoATV,balaatira
    global jogadorX,jogadorY,jogadorXmuda,jogadorYmuda,balaX,balaY,balaXmuda,balaYmuda
    for i in range(inimigos): #sao 5 inimigos
        inimigoY[i] += inimigoYmuda[i]

        if inimigoY[i]>=536:  #600-64=536
            inimigoYmuda[i]=-3*n #velocidade do inimigo aumenta com a fase
            inimigoXmuda[i]=-25*n  #inimigo se aproxima do jogador
            inimigoX[i]+=inimigoXmuda[i]
        if inimigoY[i]<=0:
            inimigoYmuda[i]=3*n
            inimigoXmuda[i]=-25*n
            inimigoX[i] += inimigoXmuda[i]
        if inimigoX[i] <= 0:  #se inimigo chega no limite da tela, aparece do outro lado
            inimigoXmuda[i] = 836  #900-64=836
            inimigoX[i] += inimigoXmuda[i]

        #colisao com o inimigo
        c1 = colisaoCinimigo(inimigoX[i],inimigoY[i],balaX,balaY)
        if c1 == True:
            somCI = pygame.mixer.Sound('sons/acertainimigo.wav')
            somCI.play()
            balaX = jogadorX
            balaatira = 1
            pontos += 1
            inimigoX[i] = randint(750, 836)  # intervalo horizontal que o inimigo surge (836=900-64)
            inimigoY[i] = randint(0, 536)  # intervalo vertical que o inimigo surge (536=600-64)

        #gerar o inimigo novo
        inimigo(inimigoX[i], inimigoY[i], i, tela, inimigofoto)

        if inimigoATV == True:

            #bala inimigo
            #inimigo atirando ('criando' a bala)
            if balaIatira[i] == 1:
                balaIX[i] = inimigoX[i]
                balaIY[i] = inimigoY[i] + 32  # +32 para a bala sair no meio do inimigo (32=64/2)
                balaI(balaIX[i], balaIY[i], i, tela, balaIfoto, balaIatira)

        #inimigo atirando quando a bala desaparece do mapa
        if balaIX[i] <= 0:
            balaIX[i] = inimigoX[i]
            balaIatira[i] = 1

        #deslocamento da bala
        if balaIatira[i] == 0:
            balaI(balaIX[i], balaIY[i], i, tela, balaIfoto, balaIatira)
            balaIX[i] += -7

        #colisao entre as balas
        c2 = colisaoCbalas(balaIX[i],balaIY[i],balaX,balaY)
        if c2 == True:
            balaX = jogadorX
            balaIX[i] = inimigoX[i]
            balaatira = 1
            balaIatira[i] = 1

        #colisao com o jogador
        c3 = colisaoCjogador(jogadorX,jogadorY,balaIX[i],balaIY[i])
        if c3 == True:
            somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
            somCJ.play()
            balaIX[i] = inimigoX[i]
            balaIatira[i] = 1
            vidas -= 1

        #colisao com o jogador e o inimigo
        c4 = colisaoCjogadorEinimigo(jogadorX,jogadorY,inimigoX[i],inimigoY[i])
        if c4 == True:
            somCJ = pygame.mixer.Sound('sons/acertajogador.wav')
            somCJ.play()
            vidas = 0  #morte automática do jogador, se encostar no inimigo

def atualizabala():
    global jogadorX, balaX, balaY, balaatira, balaXmuda
    if balaX >= 900:
        balaX = jogadorX
        balaatira = 1

    if balaatira == 0:
        bala(balaX, balaY,tela,balafoto)
        balaX += balaXmuda

def fase(n):
    global tela,pontos,vidas,balasom,inimigos,jogadorX,jogadorY,jogadorXmuda,jogadorYmuda
    global balaX,balaY,balaXmuda,balaYmuda,inimigoATV,balaatira

    if n == 1:
        fundo1 = pygame.image.load('imagens/1.png')
        tela.blit(fundo1, (0, 0))
    if n == 2:
        fundo2 = pygame.image.load('imagens/2.png')
        tela.blit(fundo2, (0, 0))
    if n == 3:
        fundo3 = pygame.image.load('imagens/3.png')
        tela.blit(fundo3, (0, 0))

    checarevento()

    #movimentando o jogador
    movimentajogador()

    #movimentando o inimigo
    movimentainimigo(n)

    #bala jogador
    atualizabala()

    #print valores do jogo
    jogador(jogadorX, jogadorY, tela, jogadorfoto)
    placar(pontosX, pontosY, tela ,pontos ,fonte)
    life(0, 27, tela, vidas, fonte)
    level(750, 0, tela, n, fonte)

    #update da tela do jogo
    pygame.display.update()

def fim():
    global fonte,fontef
    v = fontef.render('Você ganhou!', True, (0, 0, 0))
    sair = fonte.render('Aperte qualquer tecla para sair do jogo', True, (0, 0, 0))
    tela.blit(v, (200, 250))
    tela.blit(sair, (280, 315))

    # esperar usuario apertar qualquer tecla ou fechar o programa
    for evento in pygame.event.get():
        while evento.type != pygame.KEYDOWN:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.quit()
    sys.exit()

#jogo
def jogo():
    global vidas, pontos

    nivel = 1
    while nivel != 4:
        resetarfase(nivel)
        while nivel != 4:
            fase(nivel)
            if vidas <= 0:
                gameover(nivel)
                resetarfase(nivel)
            if pontos >= 10:
                if nivel < 3:
                    passoudefase()
                nivel += 1
            pygame.display.update()
    fim()
