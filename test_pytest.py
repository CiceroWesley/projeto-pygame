import pytest
from colisoes import *

def test_colisaoCinimigo():
    assert colisaoCinimigo(700,300 , 699, 299) == True

def test_colisaoCinimigo2():
    assert colisaoCinimigo(700,500 , 200, 300) == False

def test_colisaoCbalas():
    assert colisaoCbalas(450, 300, 447, 297) == True

def test_colisaoCbalas2():
    assert colisaoCbalas(450, 300, 440, 290) == True

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

'''
(231-200)^2 + (345-300)^2 = 961 + 3136 = 4097 > 4096 = 64^2
'''
def test_colisaoCjogadorEinimigo():
    assert colisaoCjogadorEinimigo(231, 345, 200, 300) == False

'''
(316-300)^2 + (262-200)^2 = 256 + 3844 = 5000 > 4096 = 64^2
'''
def test_colisaoCjogadorEinimigo2():
    assert colisaoCjogadorEinimigo(316,262,300,200) == False

'''
(345-300)^2 + (155-200)^2 = 2025 + 2025 = 4050 < 4096 = 64^2
'''
def test_colisaoCjogadorEinimigo3():
    assert colisaoCjogadorEinimigo(345,145,300,200) == True