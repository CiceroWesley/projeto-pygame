import pygame, sys
from random import randint
from funcoes import *
from funcoesfase1 import *
from funcoesfase2 import *
from funcoesfase3 import *
from abertura import *
from vitoria import *

pygame.init()
animation()

jogo=1
nivel=1

while jogo==1:

    resetarfase1()
    while nivel==1:
        fase1()
        if vidas<=0:
            gameover1() #continuar a jogar ou não (se "n" o jogo fecha)
            resetarfase1()
        if pontos>=10:
            passoudefase() #continuar a jogar ou não (se "n" o jogo fecha)
            nivel+=1

    resetarfase2()
    while nivel==2:
        fase2()
        if vidas<=0:
            gameover2()
            resetarfase2()
        if pontos>=10:
            passoudefase()
            nivel+=1

    resetarfase3()
    while nivel==3:
        fase3()
        if vidas<=0:
            gameover3()
            resetarfase3()
        if pontos>=10:
            jogo=0 #vitoria na ultima fase

#printar vitoria
fim()