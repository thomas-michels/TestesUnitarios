import unittest
from unittest import TestCase
from TesteComFramework.teste import soma
from TesteComFramework.teste import subtracao


class TestComFramework(TestCase):

    def test_soma(self):
        # Arrange (Organizar)

        # Action (Ação)
        resultado = soma(2, 2)

        # Assertion (Afirmações)
        self.assertEqual(resultado, 4, "Erro: Soma errada")

    def test_subtracao(self):
        resultado = subtracao(2, 2)
        self.assertEqual(resultado, 0, "Erro: Subtração errada")
