def fim():
    v = fontef.render('Você ganhou!', True, (0, 0, 0))
    sair = fonte.render('Aperte qualquer tecla para sair do jogo', True, (0, 0, 0))
    tela.blit(v, (200, 250))
    tela.blit(sair, (280, 315))
    tecla = ''
    while tecla != '':
        tecla = input()

    pygame.quit()
    sys.exit()