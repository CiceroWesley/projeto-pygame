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

    while nivel != 4:

        resetarfase(nivel)
        while nivel <= 3:
            fase(nivel)
            if vidas <= 0:
                gameover(nivel)
                resetarfase(nivel)
            if pontos >= 10:
                if nivel < 3:
                    passoudefase()
                nivel += 1

    fim()
except SystemError:
    print("Erro interno detectado.")
except:
    print("Erro desconhecido.")