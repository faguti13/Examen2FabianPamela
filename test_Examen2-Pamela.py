'''Unit Test'''

import pytest

from Examen2 import MiClase

def test_ObtieneValencia():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.ObtieneValencia(1234567) == 4

def test_ObtieneValencia2():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.ObtieneValencia(555) == 3

def test_DivisibleTempo():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.DivisibleTempo(10) == [1, 2, 5, 10]

def test_DivisibleTempo2():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.DivisibleTempo(15) == [1, 3, 5,15]

def test_ObtieneMasBailable():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.ObtieneMasBailable([0.8, 0.9, 0.7]) == 0.9

def test_ObtieneMasBailable2():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.10, 0.7])
    assert objeto.ObtieneMasBailable([0.8, 0.10, 0.7]) == 0.8

def test_VerificaListaCanciones():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]) == True

def test_VerificaListaCanciones2():
    objeto = MiClase(5, 120, 12, ["Torero", "Cactus", "Sway"], [0.8, 0.9, 0.7])
    assert objeto.VerificaListaCanciones(["Torero", "Cactus", "Sway"]) == True