import pytest
from colisoes import *
from impressoes import *
#Os pontos das colisões
def printc(x, y, tela, fonte):
    #colisao bala do jogador e inimigo
    a = fonte.render('.', True, (200, 100, 0))
    #colisao bala do jogador e bala do inimigo
    b = fonte.render('.', True, (0, 100, 200))
    #colisao jogador e bala do inimigo
    c = fonte.render('.', True, (200, 0, 100))
    #colisao jogador e inimigo
    d = fonte.render('.', True, (100, 0, 200))
    tela.blit(a, (699, 299))
    tela.blit(a, (200, 300))
    tela.blit(b, (447, 297))
    tela.blit(b, (440, 290))
    tela.blit(c, (225, 309))
    tela.blit(c, (323, 212))
    tela.blit(c, (318, 217))
    tela.blit(d, (231, 345))
    tela.blit(d, (316, 262))
    tela.blit(d, (345, 145))


#colisao bala do jogador e inimigo

def test_colisaoCinimigo():
    assert colisaoCinimigo(700,300 , 699, 299) == True

def test_colisaoCinimigo2():
    assert colisaoCinimigo(700,500 , 200, 300) == False

#colisao bala do jogador e bala do inimigo

def test_colisaoCbalas():
    assert colisaoCbalas(450, 300, 447, 297) == True

def test_colisaoCbalas2():
    assert colisaoCbalas(450, 300, 440, 290) == True

#colisao jogador e bala do inimigo

'''
(225+16-200)^2 + (309+16-300)^2 = 1681 + 625 = 2306 > 2304 = 48^2
'''
def test_colisaoCjogador():
    assert colisaoCjogador(225,309,200,300) == False

'''
(323+16-300)^2 + (212+16-200)^2 = 1521 + 784 = 2305 > 2304 = 48^2
'''
def test_colisaoCjogador2():
    assert colisaoCjogador(323, 212, 300, 200) == False

'''
(318+16-300)^2 + (217+16-200)^2 = 1156 + 1089 = 2245 < 2304 = 48^2
'''
def test_colisaoCjogador3():
    assert colisaoCjogador(318, 217, 300, 200) == True

#colisao jogador e inimigo


def test_colisaoCjogadorEinimigo():
    assert colisaoCjogadorEinimigo(231, 345, 200, 300) == True


def test_colisaoCjogadorEinimigo2():
    assert colisaoCjogadorEinimigo(316,262,300,200) == False


def test_colisaoCjogadorEinimigo3():
    assert colisaoCjogadorEinimigo(345,145,300,200) == False