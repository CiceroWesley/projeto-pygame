#funções que printam

#printar jogador
def jogador(x, y):
    tela.blit(jogadorfoto, (x, y))

#printar bala do jogador
def bala(x, y):
    global balaatira
    balaatira = 0
    tela.blit(balafoto, (x, y))

#printar inimigo
def inimigo(x, y, i):
    tela.blit(inimigofoto[i], (x, y))

#printar balas dos inimigos
def balaI(x, y, i):
    global balaIatira
    balaIatira[i] = 0
    tela.blit(balaIfoto[i], (x, y))

#printar pontos
def placar(x, y):
    ponto = fonte.render('Pontos:' + str(pontos), True, (0, 255, 0))
    tela.blit(ponto, (x, y))

#printar vida
def life(x, y):
    vida = fonte.render('Vidas:' + str(vidas), True, (255, 0, 0))
    tela.blit(vida, (x, y))

#print nivel
def level(x, y):
    nivel = fonte.render('Dificuldade:' + str(n), True, (0, 0, 0))
    tela.blit(nivel, (x, y))

#printar que passou de fase
def passoudefase():
    passou = fontef.render('Você passou de fase', True, (0, 0, 0))
    continua = fonte.render('Continuar?(s ou n)', True, (0, 0, 0))
    tela.blit(passou, (200, 250))
    tela.blit(continua, (310, 315))
    tecla = ''
    while tecla != 's' or tecla != 'n' or tecla != 'f':
        tecla = input()
    if tecla == 'n':
        pygame.quit()
        sys.exit()