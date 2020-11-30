#printar jogador
def jogador(x, y, tela, jogadorfoto):
    tela.blit(jogadorfoto, (x, y))

#printar bala do jogador
def bala(x, y,tela,balafoto):
    tela.blit(balafoto, (x, y))

#printar inimigo
def inimigo(x, y, i, tela, inimigofoto):
    tela.blit(inimigofoto[i], (x, y))

#printar balas dos inimigos
def balaI(x, y, i, tela, balaIfoto, balaIatira):
    balaIatira[i] = 0
    tela.blit(balaIfoto[i], (x, y))

#printar pontos
def placar(x, y, tela ,pontos ,fonte):
    p = fonte.render('Pontos:' + str(pontos), True, (0, 255, 0))
    tela.blit(p, (x, y))

#printar vida
def life(x, y, tela, vidas, fonte):
    v = fonte.render('Vidas:' + str(vidas), True, (255, 0, 0))
    tela.blit(v, (x, y))

#print nivel
def level(x, y, tela, n, fonte):
    nvl = fonte.render('Dificuldade:' + str(n), True, (0, 0, 0))
    tela.blit(nvl, (x, y))