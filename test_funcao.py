import pytest
from funcao import *

def test_soma ():
    assert somar( 5,10) == 15
    assert somar (7,2) == 9
    assert somar (1527, 10) == 1537

def test_subtrair ():
    assert subtrair (10, 5) == 5
    assert subtrair (-10, -5) == -5
    assert subtrair (-15, 5) == -20

def test_multiplicar ():
    assert multiplicar (5,6) == 30
    assert multiplicar (20,5) == 100
    assert multiplicar (0, 5) == 0

def test_dividir ():
    assert dividir (100, 4) == 25
    assert dividir (-50, 4) == -12.5
    assert dividir (10,0) == "não é possível dividir por zero"