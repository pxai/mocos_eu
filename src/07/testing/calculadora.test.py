import unittest
import calculadora

class TestStringMethods(unittest.TestCase):
    def test_sumar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.sumar(40, 2), 42)

    def test_restar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.restar(40, 2), 38)

    def test_multiplicar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.multiplicar(40, 2), 80)

    def test_dividir(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.dividir(40, 2), 20)

if __name__ == '__main__':
    unittest.main()