"""Unit tests by Fabian Gutierrez Jimenez"""

from Examen2 import MiClase

def test_obtiene_valencia_1():
    objeto_1 = MiClase(8, 130, 15, ["Song 1", "Song 2", "Song 3"], [0.7, 0.6, 0.8])
    assert objeto_1.ObtieneValencia(1234567) == 4

def test_obtiene_valencia_2():
    objeto_2 = MiClase(7, 140, 10, ["Track 1", "Track 2", "Track 3"], [0.9, 0.6, 0.7])
    assert objeto_2.ObtieneValencia(2468) == 0

def test_divisible_tempo_1():
    objeto_1 = MiClase(9, 110, 20, ["Music 1", "Music 2", "Music 3"], [0.8, 0.9, 0.7])
    assert objeto_1.DivisibleTempo(10) == [1, 2, 5, 10]

def test_divisible_tempo_2():
    objeto_2 = MiClase(6, 150, 9, ["Melody 1", "Melody 2", "Melody 3"], [0.6, 0.9, 0.7])
    assert objeto_2.DivisibleTempo(7) == [1, 7]

def test_obtiene_mas_bailable_1():
    objeto_1 = MiClase(5, 130, 12, ["Beat 1", "Beat 2", "Beat 3"], [0.8, 0.9, 0.7])
    assert objeto_1.ObtieneMasBailable([0.8, 0.9, 0.7]) == 0.9

def test_obtiene_mas_bailable_2():
    objeto_2 = MiClase(6, 120, 10, ["Rhythm 1", "Rhythm 2", "Rhythm 3"], [0.6, 0.9, 0.7])
    assert objeto_2.ObtieneMasBailable([0.8, 0.8, 0.8]) == 0.8

def test_verifica_lista_canciones_1():
    objeto_1 = MiClase(5, 140, 15, ["Song 1", "Song 2", "Song 3"], [0.8, 0.9, 0.7])
    assert objeto_1.VerificaListaCanciones(["Song 1", "Song 2", "Song 3"]) == True

def test_verifica_lista_canciones_2():
    objeto_2 = MiClase(6, 150, 10, ["Track 1", "Track 2", "Track 3"], [0.6, 0.9, 0.7])
    assert objeto_2.VerificaListaCanciones(["Track 1", "Track 2", "Track 3"]) == True
