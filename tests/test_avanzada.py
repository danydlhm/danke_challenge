# -*- coding: utf-8 -*-
"""Pruebas calculadora AVANZADA"""

import unittest
from proyecto.avanzada import CalculadoraAvanzada


class TestCalculadoraAvanzada(unittest.TestCase):
    """Test calculadora AVANZADA"""

    ca = CalculadoraAvanzada()

    def test_pow(self):
        """Test operación POTENCIA"""
        r = self.ca.pow(3)
        self.assertEqual(r, 9)

    def test_pown(self):
        """Test operación POTENCIA N"""
        r = self.ca.pown(3, 3)
        self.assertEqual(r, 27)

    def test_sqrt(self):
        """Test operación RAIZ CUADRADA"""
        r = self.ca.sqrt(9)
        self.assertEqual(r, 3.0)


if __name__ == '__main__':
    unittest.main()