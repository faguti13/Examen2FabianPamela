
from Examen2 import MiClase

def test_Encuentra():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.Encuentra([1,2,3,4,5],1) == True

def test_Encuentra2():
    objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert objeto.Encuentra([0,4,6,7],1) == False

