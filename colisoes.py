#funções relacionadas à colisões

# Para as colisões, vamos calcular com base no centro de cada objeto

#inimigo tem 64x64 pixels (64 de largura e 64 de comprimento)
#jogador tem 64x64 pixels
#bala tem 32x32 pixels
#balaI tem 32x32 pixels

#para calcular a distancia entre esses objetos devemos usar as coordenadas do centro de cada objeto
#com a formula para calcular distancia entre pontos


def colisaoCinimigo(Xinimigo,Yinimigo,Xbala,Ybala):
    distancia = (((Xinimigo+16 - Xbala)**2)+((Yinimigo+16 - Ybala)**2))**0.5 #(64/2)-(32/2)=32-16=16
    if distancia <48: #32+16=48
        return True
    else:
        return False

def colisaoCbalas(XbalaI,YbalaI,Xbala,Ybala):
    distancia = (((XbalaI - Xbala)**2)+((YbalaI - Ybala)**2))**0.5 #(32/2)-(32/2)=16-16=0
    if distancia <32: #16+16=32
        return True
    else:
        return False

def colisaoCjogador(Xjogador,Yjogador,XbalaI,YbalaI):
    distancia = (((Xjogador+16 - XbalaI)**2)+((Yjogador+16 - YbalaI)**2))**0.5 #(64/2)-(32/2)=32-16=16
    if distancia <48: #32+16=48
        return True
    else:
        return False

#nova funçao - colisao jogador e inimigo
def colisaoCjogadorEinimigo(Xjogador,Yjogador, Xinimigo,Yinimigo): #por algum motivo dá morte automática do jogador
    distancia = (((Xjogador - Xinimigo)**2)+((Yjogador - Yinimigo)**2))**0.5 #(64/2)-(64/2)=32-32=0
    if distancia <64: #32+32=64
        return True
    else:
        return False

#as outras funções não foram passadas por causa do "tela"