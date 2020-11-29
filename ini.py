import pygame,sys
from random import randint
from outros import *
#from funcoes import *
from time import sleep

pygame.init()

#inimigo
inimigofoto = []
inimigoX = []
inimigoY= []
inimigoXmuda=[]
inimigoYmuda=[]
inimigoATV=True
inimigos=5
for i in range(inimigos):
    
    inimigofoto.append(pygame.image.load('imagens/spiral.png'))
    inimigoX.append(randint(750,836))
    inimigoY.append(randint(0,536))
    inimigoXmuda.append(0)
    inimigoYmuda.append(3)

#bala inimigo
balaIfoto=[]
balaIX=[]
balaIY=[]
balaIXmuda=[]
balaIatira=[]
for i in range(inimigos):
    balaIfoto.append(pygame.image.load('imagens/taoism.png'))
    balaIX.append(0)
    balaIY.append(0)
    balaIXmuda.append(-7)
    balaIatira.append(1)


#print inimigo
def inimigo(x,y,i):
    tela.blit(inimigofoto[i],(x,y))

#print balas dos inimigos
def balaI(x,y,i):
    global balaIatira
    balaIatira[i]=0
    tela.blit(balaIfoto[i],(x,y))
