#esboço do codigo main.py
try:
    import pygame
    import sys
    from random import randint
    from colisoes import *
    from abertura import *
    from impressoes import *
    from uteis import *
except ImportError:
    print("Erro na importação.")
except:
    print("Erro desconhecido.")
try:
    pygame.init()

    animation()

    nivel = 1

    while nivel <= 3:
        fase(nivel)
            #esperar usuario apertar "s" ou "n"
        if vidas <=0:
            gameover(nivel) #continuar a jogar ou não (se "n" o jogo fecha)
            resetarfase(nivel) #pode ser redefinindo as posiçoes e velocidades de td para as iniciais (dos inimigos sendo aleatórias)
        if pontos >= 10:
            if nivel < 3:
                passoudefase() #continuar a jogar ou não (se "n" o jogo fecha)
            nivel += 1

    #printar vitoria
    fim()
except SystemError:
    print("Erro interno detectado.")
except:
    print("Erro desconhecido.")