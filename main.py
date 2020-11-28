import pygame
import sys
from random import randint
from colisoes import *
from abertura import *
from impressoes import *
from uteis import *
from globo import *
pygame.init()
animation(tela,jogadorfoto,fonte,fontef)
nivel = 1
while nivel != 4:
    resetarfase(nivel,jogadorX,jogadorY,jogadorXmuda,jogadorYmuda,pontos,vidas,inimigos,inimigofoto,inimigoX,inimigoXmuda,inimigoY,inimigoYmuda)
    while nivel <= 3:
        fase(nivel,tela,pontos,vidas,balasom,inimigos, jogadorX, jogadorY, jogadorXmuda, jogadorYmuda, balaX, balaY, balaXmuda, balaYmuda, inimigoATV, balaatira)
        if vidas <= 0:
            gameover(nivel, tela)
            resetarfase(nivel,jogadorX,jogadorY,jogadorXmuda,jogadorYmuda,pontos,vidas,inimigos)
        if pontos >= 10:
            if nivel < 3:
                passoudefase(tela,fonte,fontef)
            nivel += 1
fim(fonte,fontef)