import unittest
import sys
sys.path.append("src")


class Creditcardtest(unittest.TestCase):
    def testcreditcardnormal1(self):

        # varaiables de entrada
        compra = 200000
        interes = 3.10
        plazos = 36

        # resultado esperado
        resultado_esperado_compra = 9297.959116
        resultado_esperado_intereses = 134726.53
        # proceso
        resultado_compra = calculate_rate(compra, interes, plazos)
        resultado_intereses = calculate_interest(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_compra, 2), round(resultado_compra, 2))
        self.assertEqual(round(resultado_esperado_intereses, 2), round(resultado_intereses, 2))

    def testcreditcardnormal2(self):

        # varaiables de entrada
        compra = 850000
        interes = 3.4
        plazos = 24

        # resultado esperado
        resultado_esperado_compra = 52377.49864
        resultado_esperado_intereses = 407059.97

        # proceso
        resultado_compra = calculate_rate(compra, interes, plazos)
        resultado_intereses = calculate_interest(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_compra, 2), round(resultado_compra, 2))
        self.assertEqual(round(resultado_esperado_intereses, 2), round(resultado_intereses, 2))

    # Casos Excepcionales    

    def testcreditcardplazos1(self):

        # varaiables de entrada
        compra = 90000
        interes = 2.40
        plazos = 1

        # resultado esperado
        resultado_esperado_compra = 90000
        resultado_esperado_intereses = 0

        # proceso
        resultado_compra = calculate_rate(compra, interes, plazos)
        resultado_intereses = calculate_interest(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_compra, 2), round(resultado_compra, 2))
        self.assertEqual(round(resultado_esperado_intereses, 2), round(resultado_intereses, 2))

    def testcreditcardtasacero(self):

        # varaiables de entrada
        compra = 480000
        interes = 0
        plazos = 48

        # resultado esperado
        resultado_esperado_compra = 10000
        resultado_esperado_intereses = 0

        # proceso
        resultado_compra = calculate_rate(compra, interes, plazos)
        resultado_intereses = calculate_interest(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_compra, 2), round(resultado_compra, 2))
        self.assertEqual(round(resultado_esperado_intereses, 2), round(resultado_intereses, 2))

    # Casos de Error


    def testcreditcardusura(self):

        # variables de entrada
        compra = 50000
        interes = 12.4
        plazos = 60

        # Verificar que salte el error
        with self.assertRaises(PeriodError):
            calculate_rate(compra, interes, plazos)

    def testcreditcardcompra0(self):
        
        # variables de entrada
        compra = 0
        interes = 2.4
        plazos = 60

        # Verificar que salte el error
        with self.assertRaises(PurchaseError):
            calculate_rate(compra, interes, plazos)

    def testcreditcardnegativo(self):

        # variables de entrada
        cuota = 50000
        interes = 1
        plazos = -10

        # Verificar que salte el error
        with self.assertRaises(NegativeError):
            calculate_rate(compra, interes, plazos)

if __name__ == '__main__':
    unittest.main()