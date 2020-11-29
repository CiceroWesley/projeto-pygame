import pygame,sys
from random import randint
from outros import *
#from funcoes import *
from time import sleep

pygame.init()

#jogador
jogadorfoto = pygame.image.load('imagens/clown.png')
jogadorX = 0
jogadorY = 300
jogadorXmuda=0
jogadorYmuda=0
#global dificuldade
dificuldade=1 #não utilizado ainda
#global vidas
vidas=3

#bala jogador
balafoto = pygame.image.load('imagens/moon.png')
balaX=0
balaY=0
balaXmuda=8 #velocidade bala jogador
balaYmuda=0
balaatira=1

#print jogador
def jogador(x,y):
    tela.blit(jogadorfoto,(x,y))

'''
#print bala do jogador
def bala(x,y):
    global balaatira
    balaatira=0
    tela.blit(balafoto,(x,y))
'''