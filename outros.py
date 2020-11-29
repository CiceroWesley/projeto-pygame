import pygame,sys
from random import randint
#from funcoes import *
from time import sleep

pygame.init()

lagalt= (900,600)
tela = pygame.display.set_mode(lagalt)
fundo=pygame.image.load('imagens/fundo.png')

#música do jogo
pygame.mixer.music.load('sons/KoopaCastle.mp3')
pygame.mixer.music.play(-1)

#nome do jogo e icone
pygame.display.set_caption('Magic Shooters')
icone = pygame.image.load('imagens/hat.png')
pygame.display.set_icon(icone)

#pontos
#global pontos
pontos=0
fonte = pygame.font.Font('fontes/OldLondon.ttf',32)
pontosX=0
pontosY=0
fontef = pygame.font.Font('fontes/OldLondon.ttf',64)

#print 'Vc morreu'
def gameover():
    fim = fontef.render('Vc morreu',True,(0,0,0))
    continua = fonte.render('Jogar de novo?(s ou n)',True,(0,0,0))
    tela.blit(fim,(300,250))
    tela.blit(continua,(310,315))

#Print 'Parabens, vc ganhou'
def ganhou():
    vitoria = fontef.render('Parabens, ganhou', True, (0, 0, 0))
    tela.blit(vitoria, (200, 250))
    continua = fonte.render('Jogar de novo?(s ou n)', True, (0, 0, 0))
    tela.blit(continua, (310, 315))

