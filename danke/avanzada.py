# -*- coding: utf-8 -*-
"""Calculadora AVANZADA"""

import math


class CalculadoraAvanzada(object):
  """Clase calculadora AVANZADA"""

  def pow(self, a):
      """
      Operación POTENCIA
      Parámetros:
        a - Operador A
      """
      return pow(a, 2)

  def pown(self, a, n):
      """
      Operación POTENCIA N
      Parámetros:
        a - Operador A
        n - Operador N
      """
      return pow(a, n)

  def sqrt(self, a):
      """
      Operación RAIZ CUADRADA
      Parámetros:
        a - Operador A
      """
      return math.sqrt(a)