import pygame
import sys
from random import randint
from colisoes import *
from abertura import *
from impressoes import *
pygame.init()
global lagalt
lagalt = (900, 600)
global tela 
tela = pygame.display.set_mode(lagalt)
global nivel
nivel = 1
global vidas
vidas = 3
global pontos
pontos = 0
global jogadorfoto
jogadorfoto = pygame.image.load('imagens/jogador.png')
global jogadorX
jogadorX = 0
global jogadorY
jogadorY = 300
global jogadorXmuda
jogadorXmuda = 0
global jogadorYmuda
jogadorYmuda = 0
#global tecla
global pontosX
pontosX = 0
global pontosY
pontosY = 0
global balafoto
balafoto = pygame.image.load('imagens/balajogador.png')
global balaX
balaX = 0
global balaY
balaY = 0
global balaXmuda
balaXmuda = 8  # velocidade bala jogador
global balaYmuda
balaYmuda = 0
global balaatira
balaatira = 1
global balaIfoto
balaIfoto = []
global balaIX
balaIX = []
global balaIY
balaIY = []
global balaIXmuda
balaIXmuda = []
global balaIatira
balaIatira = []
global fonte
fonte = pygame.font.Font('fontes/BebasNeue.ttf', 32)
global fontef
fontef = pygame.font.Font('fontes/BebasNeue.ttf', 64)
global balasom
balasom = pygame.mixer.Sound('sons/fogojogador.wav')
global inimigos
inimigos = 5
global inimigoATV
inimigoATV = True
global inimigofoto
inimigofoto = []
global inimigoX
inimigoX = []
global inimigoY
inimigoY = []
global inimigoXmuda
inimigoXmuda = []
global inimigoYmuda
inimigoYmuda = []