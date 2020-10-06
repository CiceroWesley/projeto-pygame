def colisaoCinimigo(Xinimigo,Yinimigo,Xbala,Ybala):
    distancia = (((Xinimigo - Xbala)**2)+((Yinimigo - Ybala)**2))**0.5
    if distancia <20:
        return True
    else:
        return False

def colisaoCbalas(XbalaI,YbalaI,Xbala,Ybala):
    distancia = (((XbalaI - Xbala)**2)+((YbalaI - Ybala)**2))**0.5
    if distancia <20:
        return True
    else:
        return False

def colisaoCjogador(Xjogador,Yjogador,XbalaI,YbalaI):
    distancia = (((Xjogador - XbalaI)**2)+((Yjogador - YbalaI)**2))**0.5
    if distancia <20:
        return True
    else:
        return False

#as outras funções não foram passadas por causa do "tela"