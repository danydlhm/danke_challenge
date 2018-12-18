# -*- coding: utf-8 -*-
"""Pruebas calculadora SIMPLE"""

import unittest
from proyecto.simple import CalculadoraSimple


class TestCalculadoraSimple(unittest.TestCase):
    """Test calculadora SIMPLE"""

    cs = CalculadoraSimple()

    def test_sum(self):
        """Test operación SUMA"""
        r = self.cs.sum(2, 3)
        self.assertEqual(r, 5)

    def test_res(self):
        """Test operación RESTA"""
        r = self.cs.res(3, 2)
        self.assertEqual(r, 1)

    def test_mul(self):
        """Test operación MULTIPLICACIÓN"""
        r = self.cs.mul(5, 2)
        self.assertEqual(r, 10)

    def test_div(self):
        """Test operación DIVISIÓN"""
        r = self.cs.div(10, 2)
        self.assertEqual(r, 5.0)


if __name__ == '__main__':
    unittest.main()