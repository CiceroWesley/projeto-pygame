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
