try:
    import pygame, sys
except:
    print("Erro na importação.")
# abertura
def animation():
    lagalt = (900, 600)
    tela = pygame.display.set_mode(lagalt)
    jogadorfoto = pygame.image.load('imagens/jogador.png')
    fonte = pygame.font.Font('fontes/BebasNeue.ttf', 32)
    fontef = pygame.font.Font('fontes/BebasNeue.ttf', 64)

    # nome do jogo e icone
    pygame.display.set_caption('Magic Shooters')
    icone = pygame.image.load('imagens/icone.png')
    pygame.display.set_icon(icone)

    fundo0 = pygame.image.load('imagens/0.png')
    running = True
    playerX = 150
    playerY = 260
    playerXmuda = 2.3

    enemyfoto = []
    enemyX = [0, 0, 0]
    enemyY = []
    enemyXmuda = []
    enemy = 3
    posY = [130, 260, 390]

    enemyfoto.append(pygame.image.load('imagens/inimigo1.png')) 
    enemyfoto.append(pygame.image.load('imagens/inimigo2.png'))
    enemyfoto.append(pygame.image.load('imagens/inimigo3.png'))

    for i in range(enemy):
        enemyY.append(posY[i])
        enemyXmuda.append(2.5)
    while running:
        tela.blit(fundo0, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    running = False

        for i in range(enemy):
            enemyX[i] += enemyXmuda[i]
            tela.blit(enemyfoto[i], (enemyX[i], enemyY[i]))

        playerX += playerXmuda
        tela.blit(jogadorfoto,(playerX, playerY))

        pularanimacao = fonte.render('Pressiona P para pular...', True, (0, 0, 0))

        # print 'Pressiona P para pular...'
        if playerX > 100 and playerX < 1200:
            tela.blit(pularanimacao, (0, 550))

        # print nome do jogo
        if playerX > 900:
            gamename = fontef.render('Magic Shooters', True, (0, 0, 0))
            tela.blit(gamename, (260, 250))  # centralizar na tela

        if playerX > 1200:
            running = False
        pygame.display.update()