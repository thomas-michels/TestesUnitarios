
from unittest import TestCase
from TDD.Par.calcular_par import calcular_par

class TestComTdd(TestCase):

    def test_calcular_par(self):

        # action
        resultado = calcular_par(2)
        resultado2 = calcular_par(3)
        resultado3 = calcular_par(('a'))

        # assertions
        self.assertTrue(resultado)
        self.assertFalse(resultado2)
        self.assertEqual(resultado3, 'valor não informado')