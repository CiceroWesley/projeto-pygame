#esboço do codigo main.py

import pygame
#e importar td q precisar

pygame.init()

#com imagens novas da abertura (todos os 3 inimigos perseguindo o jogador)
animation()

jogo=1
nivel=1

while jogo==1:

    while nivel==1:
        fase1()
        if vidas<=0:
            #esperar usuario apertar "s" ou "n"
            #(como o jogo vai parar aqui a tela tb vai congelar)
            gameover() #continuar a jogar ou não (se "n" o jogo fecha)
            resetarfase() #pode ser redefinindo as posiçoes e velocidades de td para as iniciais (dos inimigos sendo aleatórias)
        if pontos>=10:
            passoudefase() #continuar a jogar ou não (se "n" o jogo fecha)
            nivel+=1

    while nivel==2:
        fase2()
        if vidas<=0:
            gameover()
            resetarfase()
        if pontos>=10:
            passoudefase()
            nivel+=1
    while nivel==3:
        fase3()
        if vidas<=0:
            gameover()
            resetarfase()
        if pontos>=10:
            jogo=0 #vitoria na ultima fase

#printar vitoria na ultima imagem da fase3 e opçao de fechar o jogo
vitoria() #mais pygame.quit() e sys.exit()