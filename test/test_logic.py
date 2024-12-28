import unittest
import sys
sys.path.append("src")
from model.creditcard import CalculadoraDeTarjetasDeCredito as Calculadora
from model.creditcard import ExcepcionDeCompraNoValida, ExcepcionDeNumeroDePagosNoValido, ExcepcionPorInteresesExcesivos


class tarjetatest(unittest.TestCase):
    def test_tarjeta_normal1(self):

        # varaiables de entrada
        compra = 200000
        interes = 3.10
        plazos = 36

        # resultado esperado
        resultado_esperado_cuota = 9297.959116
        # proceso
        resultado_cuota = Calculadora.calcular_pago(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_cuota, 2), round(resultado_cuota, 2))

    def test_tarjeta_normal2(self):

        # varaiables de entrada
        compra = 850000
        interes = 3.4
        plazos = 24

        # resultado esperado
        resultado_esperado_cuota = 52377.49864

        # proceso
        resultado_cuota = Calculadora.calcular_pago(compra, interes, plazos)
        # verificación
        self.assertEqual(round(resultado_esperado_cuota, 2), round(resultado_cuota, 2))

    # Casos Excepcionales    

    def test_tarjeta_plazos1(self):

        # varaiables de entrada
        compra = 90000
        interes = 2.40
        plazos = 1

        # resultado esperado
        resultado_esperado_cuota = 90000

        # proceso
        resultado_cuota = Calculadora.calcular_pago(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_cuota, 2), round(resultado_cuota, 2))

    def test_tarjeta_tasa_cero(self):

        # varaiables de entrada
        compra = 480000
        interes = 0
        plazos = 48

        # resultado esperado
        resultado_esperado_cuota = 10000
        resultado_esperado_intereses = 0

        # proceso
        resultado_cuota = Calculadora.calcular_pago(compra, interes, plazos)

        # verificación

        self.assertEqual(round(resultado_esperado_cuota, 2), round(resultado_cuota, 2))

    # Casos de Error


    def test_tarjeta_usura(self):

        # variables de entrada
        compra = 50000
        interes = 12.4
        plazos = 60

        # Verificar que salte el error
        with self.assertRaises(ExcepcionPorInteresesExcesivos):
            Calculadora.calcular_pago(compra, interes, plazos)

    def test_tarjeta_compra_0(self):
        
        # variables de entrada
        compra = 0
        interes = 2.4
        plazos = 60

        # Verificar que salte el error
        with self.assertRaises(ExcepcionDeCompraNoValida):
            Calculadora.calcular_pago(compra, interes, plazos)

    def test_tarjeta_valor_negativo(self):

        # variables de entrada
        compra = 50000
        interes = 1
        plazos = -10

        # Verificar que salte el error
        with self.assertRaises(ExcepcionDeNumeroDePagosNoValido):
            Calculadora.calcular_pago(compra, interes, plazos)

if __name__ == '__main__':
    unittest.main()