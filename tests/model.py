import unittest

from src.model import Antena, calcular_contratos, NoHayResultado


class CalcularContratosTestCase(unittest.TestCase):
    def test_unica_antena_con_resultado_1(self):
        antenas = [Antena(50, 50, 1)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, antenas)

    def test_unica_antena_con_resultado_2(self):
        antenas = [Antena(50, 100, 1)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, antenas)

    def test_unica_antena_con_resultado_3(self):
        antenas = [Antena(-50, 500, 1)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, antenas)

    def test_unica_antena_con_resultado_4(self):
        antenas = [Antena(200, 500, 1)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, antenas)

    def test_sin_antenas_sin_resultado(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([], 100))

    def test_unica_antena_sin_resultado_1(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(50, 50, 1)], 101))

    def test_unica_antena_sin_resultado_2(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(49, 50, 1)], 101))

    def test_unica_antena_sin_resultado_3(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(50, 49, 1)], 100))

    def test_unica_antena_sin_resultado_4(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(-10, 50, 1)], 101))

    def test_unica_antena_sin_resultado_5(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(110, 50, 1)], 101))

    def test_unica_antena_sin_resultado_6(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([
            Antena(10, 10, 1),
            Antena(10, 10, 2),
            Antena(10, 10, 3)
        ], 100))

    def test_pequenia_antena_en_el_medio(self):
        antenas = [Antena(10, 50, 1), Antena(15, 10, 2), Antena(20, 50, 3), Antena(60, 40, 4)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, [antenas[2], antenas[3]])

    def test_superposicion_de_antenas(self):
        antenas = [Antena(10, 50, 1), Antena(10, 15, 2), Antena(20, 50, 3), Antena(60, 40, 4)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, [antenas[2], antenas[3]])

    def test_hueco_sin_resultado(self):
        self.assertRaises(NoHayResultado, lambda: calcular_contratos([Antena(20, 30, 1), Antena(90, 30, 1)], 100))

    def test_superposicion_exacta(self):
        antenas = [Antena(30, 30, 1), Antena(80, 20, 2)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, antenas)

    def test_varias_antenas_iguales(self):
        antenas = [Antena(10, 10, 1), Antena(90, 10, 2), Antena(50, 30, 3), Antena(50, 30, 4), Antena(50, 30, 5)]
        resultado = calcular_contratos(antenas.copy(), 100)
        self.assertEqual(resultado, [antenas[0], antenas[2], antenas[1]])


if __name__ == '__main__':
    unittest.main()
