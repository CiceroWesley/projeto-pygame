#algumas funcoes uteis
'''
try:
    from impressoes import *
    from colisoes import *
    from globo import *
except:
    print("Erro na importação.")
'''
from impressoes import *
from colisoes import *
from globo import *

def resetarfase(n,jogadorX,jogadorY,jogadorXmuda,jogadorYmuda,pontos,vidas,inimigos,inimigofoto,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda):
    #criando a tela
    #lagalt = (900, 600)
    #tela = pygame.display.set_mode(lagalt)
    
    if n == 1:
        #fundo = pygame.image.load('imagens/1.png')
        fundo1 = pygame.image.load('imagens/1.png')
        tela.blit(fundo1, (0, 0))
    if n == 2:
        #fundo = pygame.image.load('imagens/2.png')
        fundo2 = pygame.image.load('imagens/2.png')
        tela.blit(fundo2, (0, 0))
    if n == 3:
        #fundo = pygame.image.load('imagens/3.png')
        fundo3 = pygame.image.load('imagens/3.png')
        tela.blit(fundo3, (0, 0))        
    
    #jogador
    #jogadorfoto = pygame.image.load('imagens/jogador.png')
    #jogadorX = 0
    #jogadorY = 300
    #jogadorXmuda = 0
    #jogadorYmuda = 0
    #vidas = 3

    #pontos
    #pontos = 0
    #fonte = pygame.font.Font('fontes/BebasNeue.ttf', 32)
    #pontosX = 0
    #pontosY = 0
    #fontef = pygame.font.Font('fontes/BebasNeue.ttf', 64)

    #inimigo
    #inimigofoto = []
    #inimigoX = []
    #inimigoY = []
    #inimigoXmuda = []
    #inimigoYmuda = []
    #inimigoATV = True
    #inimigos = 5
    for i in range(inimigos):
        if n == 1:
            inimigofoto.append(pygame.image.load('imagens/inimigo1.png'))
        if n == 2:
            inimigofoto.append(pygame.image.load('imagens/inimigo2.png'))
        if n == 3:
            inimigofoto.append(pygame.image.load('imagens/inimigo1.png'))
        inimigoX.append(randint(700, 836))  # 836=900-64
        inimigoY.append(randint(0, 536))  # 536=600-64
        inimigoXmuda.append(0)
        inimigoYmuda.append(3)

    #bala jogador
    #balafoto = pygame.image.load('imagens/balajogador.png')
    #balaX = 0
    #balaY = 0
    #balaXmuda = 8  # velocidade bala jogador
    #balaYmuda = 0
    #balaatira = 1

    # bala inimigo
    #balaIfoto = []
    #balaIX = []
    #balaIY = []
    #balaIXmuda = []
    #balaIatira = []
    for i in range(inimigos):
        if n == 1:
            balaIfoto.append(pygame.image.load('imagens/tiro1.png'))
        if n == 2:
            balaIfoto.append(pygame.image.load('imagens/tiro2.png'))
        if n == 3:
            balaIfoto.append(pygame.image.load('imagens/tiro3.png'))
        balaIX.append(0)
        balaIY.append(0)
        balaIXmuda.append(-7)  # velocidade bala inimigo
        balaIatira.append(1)
    '''
    if n == 1:
        tela.blit(fundo1, (0, 0))
    if n == 2:
        tela.blit(fundo2, (0, 0))
    if n == 3:
        tela.blit(fundo3, (0, 0))
    '''

def movimentajogador(jogadorX, jogadorY, jogadorXmuda, jogadorYmuda):
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

def gameover(n, tela):
    fim = fontef.render('Você morreu', True, (0, 0, 0))
    continua = fonte.render('Jogar de novo?(s ou n)', True, (0, 0, 0))
    tela.blit(fim, (300, 250))
    tela.blit(continua, (310, 315))
    #esperar apertar o comando certo
    for evento in pygame.event.get():
        while evento.key != pygame.K_s or evento.key != pygame.K_f or evento.key != pygame.K_n or evento.type != pygame.QUIT:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s or evento.key == pygame.K_f:
                    resetarfase(n,jogadorX,jogadorY,jogadorXmuda,jogadorYmuda,pontos,vidas,inimigos,inimigofoto,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda)
                if evento.key == pygame.K_n or evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def checarevento(jogadorXmuda, jogadorYmuda, pontos, balaatira, balasom, balaX, balaY):
    try:
         # usuario apertar algum botão (evento)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # usuario apertou o botao (keydown)
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
                        #balasom = pygame.mixer.Sound('sons/fogojogador.wav')
                        balasom.play()
                        balaX = jogadorX
                        balaY = jogadorY + 32  # 32 para a bala sair no meio do jogador (32=64/2)
                        bala(balaX, balaY)

            # usuario soltou o botao (keyup)
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    jogadorXmuda = 0
                    jogadorYmuda = 0
    except KeyboardInterrupt:
        print("Execução interrompida.")

def movimentainimigo(n, inimigos,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda, jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira, pontos, vidas):
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

def atualizabala(jogadorX, balaX, balaY, balaatira, balaXmuda):
    if balaX >= 900:
        balaX = jogadorX
        balaatira = 1

    if balaatira == 0:
        bala(balaX, balaY)
        balaX += balaXmuda

def fase(n,tela,pontos, vidas,balasom,inimigos,jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira):
    #global jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira

    # checando qual botão o jogador apertou (qual evento aconteceu)
    #checarevento(n, jogadorXmuda, jogadorYmuda, pontos, balaatira, balasom, balaX, balaY)
    checarevento(jogadorXmuda, jogadorYmuda, pontos, balaatira, balasom, balaX, balaY)

    #movimentando o jogador
    #movimentajogador(n, jogadorY, jogadorY, jogadorXmuda, jogadorYmuda)
    movimentajogador(jogadorX, jogadorY, jogadorXmuda, jogadorYmuda)

    #movimentando o inimigo
    movimentainimigo(n, inimigos,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda, jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira, pontos, vidas)

    #bala jogador
    atualizabala(jogadorX, balaX, balaY, balaatira, balaXmuda)

    #print valores do jogo
    jogador(tela,jogadorfoto,jogadorX, jogadorY)
    placar(tela,pontos,pontosX, pontosY)
    life(tela,vidas,fonte,0, 27)
    level(tela,nivel,fonte,fontef750, 0)

    # update da tela do jogo
    pygame.display.update()

def fim(fonte,fontef):
    v = fontef.render('Você ganhou!', True, (0, 0, 0))
    sair = fonte.render('Aperte qualquer tecla para sair do jogo', True, (0, 0, 0))
    tela.blit(v, (200, 250))
    tela.blit(sair, (280, 315))
    tecla = ''
    while tecla != '':
        tecla = input()

    pygame.quit()
    sys.exit()
