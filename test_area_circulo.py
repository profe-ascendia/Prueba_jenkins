import unittest
from math import pi
from area_circulo import area

class TestAreaCirculo(unittest.TestCase):
    def test_area_nulo(self):
        #c = area(None)
        self.assertRaises(TypeError, area, None)
        
    def test_area_cadena(self):
        #c = area('Hola')
        with self.assertRaises(TypeError):
            area('Hola')

    def test_numero_negativo(self):
        #c = area(-1)
        self.assertRaises(ValueError,area, -1)

    def test_numero_complejo(self):
        self.assertRaises(TypeError, area, 3+2j)

    def test_radio_1(self):
        c = area(1)
        self.assertEqual(pi,c,1)
    

if __name__ == '__init__':
    unittest.main()