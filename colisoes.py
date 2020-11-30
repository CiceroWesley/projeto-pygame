#para o calculo de distancia entre 2 objetos, vamos considerar as coordenadas de seus centros e que eles são circulos
#jogador tem raio 32, já que é 64x64 pixels, analogamente:
#inimigo tem raio 32
#bala do jogador tem raio 16
#bala do inimigo tem raio 16


#colisao bala do jogador e inimigo
def colisaoCinimigo(iX, iY, balaX, balaY):
    d1 = (((iX+16-balaX)**2)+((iY+16-balaY)**2))**0.5 #32-16=16
    if d1<48: #32+16=48
        return True
    else:
        return False

#colisao bala do jogador e bala do inimigo
def colisaoCbalas(bIX, bIY, balaX, balaY):
    d2 = (((bIX-balaX)**2)+((bIY-balaY)**2))**0.5 #16-16=0
    if d2<32: #16+16=32
        return True
    else:
        return False

#colisao jogador e bala do inimigo
def colisaoCjogador(jogadorX, jogadorY, bIX, bIY):
    d3 = (((jogadorX+16-bIX)**2)+((jogadorY+16-bIY)**2))**0.5 #32-16=16
    if d3<48: #32+16=48
        return True
    else:
        return False

#colisao jogador e inimigo
def colisaoCjogadorEinimigo(jogadorX,jogadorY,iX,iY):
    d4 = (((jogadorX-iX)**2)+((jogadorY-iY)**2))**0.5 #32-32=0
    if d4<64: #32+32=64
        return True
    else:
        return False