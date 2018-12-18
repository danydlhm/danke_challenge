#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from test_simple import TestCalculadoraSimple
from test_avanzada import TestCalculadoraAvanzada

if __name__ == '__main__':
    try:
        # Test Suite 
        test = unittest.TestSuite()
        test.addTest(TestCalculadoraSimple('test_sum'))
        test.addTest(TestCalculadoraSimple('test_res'))
        test.addTest(TestCalculadoraSimple('test_mul'))
        test.addTest(TestCalculadoraSimple('test_div'))
        test.addTest(TestCalculadoraAvanzada('test_pow'))
        test.addTest(TestCalculadoraAvanzada('test_pown'))
        test.addTest(TestCalculadoraAvanzada('test_sqrt'))
        # Run
        unittest.TextTestRunner().run(test)
    except KeyboardInterrupt:
        print("\nInterrumpido")
        sys.exit(0)
    except Exception as e:
        print("\nError: " + str(e))
        sys.exit(1)