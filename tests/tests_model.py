import unittest
from criptos.models import CriptoValorModel, APIError

class TestModel(unittest.TestCase):
    def test_la_moneda_debe_existir (self):
        cv= CriptoValorModel('BTC','lolilo')

        with self.assertRaisesRegex (APIError,550):
            cv.obtener_tasa()