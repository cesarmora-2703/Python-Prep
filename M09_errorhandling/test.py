import unittest
from suma import *

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()

'''
unittest.main(argv=[""], verbosity=3, exit=False)
test_suma_dos_positivos(__main__.CajanegraTest)
test_suma_dos_negativos(__main__.CajanegraTest)

https://ellibrodepython.com/python-testing
https://www.geeksforgeeks.org/python-assertion-error/
'''