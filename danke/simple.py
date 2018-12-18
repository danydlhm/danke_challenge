# -*- coding: utf-8 -*-
"""Calculadora SIMPLE"""


class CalculadoraSimple(object):
    """Clase calculadora SIMPLE"""

    def sum(self, a, b):
        """
        Operación SUMA
        Parámetros:
          a - Operador A
          b - Operador B
        """
        return a + b

    def res(self, a, b):
        """
        Operación RESTA
        Parámetros:
          a - Operador A
          b - Operador B
        """
        return a - b

    def mul(self, a, b):
        """
        Operación MULTIPLICACIÓN
        Parámetros:
          a - Operador A
          b - Operador B
        """
        return a * b

    def div(self, a, b):
        """
        Operación DIVISIÓN
        Parámetros:
          a - Operador A
          b - Operador B
        """
        return float(a) / b