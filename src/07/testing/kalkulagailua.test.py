import unittest
import kalkulagailua

class TestStringMethods(unittest.TestCase):
    def test_batura(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.batura(40, 2), 42)

    def test_restar(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.kendu(40, 2), 38)

    def test_multiplicar(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(c.biderkatu(40, 2), 80)

    def test_dividir(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(c.zatitu(40, 2), 20)

if __name__ == '__main__':
    unittest.main()