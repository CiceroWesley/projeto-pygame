# abertura
def animation():
    fundo0 = pygame.image.load('imagens/0.png')
    running = True
    playerX = 150
    playerY = 260
    playerXmuda = 2.3
    playerYmuda = 0

    enemyfoto = []
    enemyX = []
    enemyY = []
    enemyXmuda = []
    enemyYmuda = []
    enemy = 3
    posY = [130, 260, 390]

    enemyfoto[1].append(pygame.image.load('imagens/inimigo1.png')) #será q é assim?
    enemyfoto[2].append(pygame.image.load('imagens/inimigo2.png'))
    enemyfoto[3].append(pygame.image.load('imagens/inimigo3.png'))

    for i in range(enemy):
        enemyX.append(0)
        enemyY.append(posY[i])
        enemyXmuda.append(2.50)
        enemyYmuda.append(0)
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
        jogador(playerX, playerY)
        pularanimacao = fonte.render('Pressiona P para pular...', True, (0, 0, 0))

        # print 'Pressiona P para pular...'
        if playerX > 100 and playerX < 1000:
            tela.blit(pularanimacao, (0, 550))

        # print nome do jogo
        if playerX > 950:
            gamename = fontef.render('Magic Shooters', True, (0, 0, 0))
            tela.blit(gamename, (260, 250))  # centralizar na tela

        if playerX > 1000:
            sleep(2)
            running = False
        pygame.display.update()