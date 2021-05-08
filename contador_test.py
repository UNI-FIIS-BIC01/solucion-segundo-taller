import io
import string
import sys
from typing import List, Tuple
from unittest import mock
from unittest.mock import MagicMock

import contador
from contador import contador_letras, es_pangrama
from pruebabase import PruebaBase


class ContadorTest(PruebaBase):

    def test_contador_letras_vallejo(self):
        resultado: List[Tuple[string, int]] = contador_letras("Hay, hermanos, muchisimo que hacer.")
        self.assertEqual(13, len(resultado))

        self.assertEqual(("a", 3), resultado[0])
        self.assertEqual(("c", 2), resultado[1])
        self.assertEqual(("e", 3), resultado[2])
        self.assertEqual(("h", 4), resultado[3])
        self.assertEqual(("i", 2), resultado[4])
        self.assertEqual(("m", 3), resultado[5])
        self.assertEqual(("n", 1), resultado[6])
        self.assertEqual(("o", 2), resultado[7])
        self.assertEqual(("q", 1), resultado[8])
        self.assertEqual(("r", 2), resultado[9])
        self.assertEqual(("s", 2), resultado[10])
        self.assertEqual(("u", 2), resultado[11])
        self.assertEqual(("y", 1), resultado[12])

    def test_contador_letras_anagrama(self):
        resultado: List[Tuple[string, int]] = contador_letras("Jovencillo emponzonado de whisky, que mala" +
                                                              " figurota exhibes.")
        self.assertEqual(26, len(string.ascii_lowercase))

        self.assertEqual(("a", 4), resultado[0])
        self.assertEqual(("b", 1), resultado[1])
        self.assertEqual(("c", 1), resultado[2])
        self.assertEqual(("d", 2), resultado[3])
        self.assertEqual(("e", 6), resultado[4])
        self.assertEqual(("f", 1), resultado[5])
        self.assertEqual(("g", 1), resultado[6])
        self.assertEqual(("h", 2), resultado[7])
        self.assertEqual(("i", 4), resultado[8])
        self.assertEqual(("j", 1), resultado[9])
        self.assertEqual(("k", 1), resultado[10])
        self.assertEqual(("l", 3), resultado[11])
        self.assertEqual(("m", 2), resultado[12])
        self.assertEqual(("n", 3), resultado[13])
        self.assertEqual(("o", 6), resultado[14])
        self.assertEqual(("p", 1), resultado[15])
        self.assertEqual(("q", 1), resultado[16])
        self.assertEqual(("r", 1), resultado[17])
        self.assertEqual(("s", 2), resultado[18])
        self.assertEqual(("t", 1), resultado[19])
        self.assertEqual(("u", 2), resultado[20])
        self.assertEqual(("v", 1), resultado[21])
        self.assertEqual(("w", 1), resultado[22])
        self.assertEqual(("x", 1), resultado[23])
        self.assertEqual(("y", 1), resultado[24])
        self.assertEqual(("z", 1), resultado[25])

    def test_es_pangrama(self):
        resultado = es_pangrama("Hay, hermanos, muchisimo que hacer.")
        self.assertFalse(resultado)

        resultado = es_pangrama("Jovencillo emponzonado de whisky, que mala figurota exhibes.")
        self.assertTrue(resultado)

    @mock.patch('contador.input', create=True)
    def test_iniciar_vallejo(self, input_mock: MagicMock):
        input_mock.side_effect = ["Hay, hermanos, muchisimo que hacer."]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        contador.iniciar()

        self.assert_over_file(resultado_test, "test/vallejo_test.txt")

    @mock.patch('contador.input', create=True)
    def test_iniciar_pangrama(self, input_mock: MagicMock):
        input_mock.side_effect = ["Jovencillo emponzonado de whisky, que mala figurota exhibes."]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        contador.iniciar()

        self.assert_over_file(resultado_test, "test/pangrama_test.txt")
