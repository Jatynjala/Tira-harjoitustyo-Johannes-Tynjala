import unittest
from salausosa1 import korvaa_merkit, aseta_kirjaimet_ja_numerot, muuta_listaksi

class Testsalausosa1(unittest.TestCase):
    def test_merkkijono_muutettaan_listaksi_oikein(self):
        testimerkkijono="keqmdo"
        testattava_lista=muuta_listaksi(testimerkkijono)
        verrattava_lista=["k", "e", "q", "m", "d", "o"]
        self.assertEqual(testattava_lista, verrattava_lista)
    def test_kirjaimet_ja_numerot_asetetaan_oikein(self):
        testi_matriisi=aseta_kirjaimet_ja_numerot()
        self.assertNotEqual(testi_matriisi[0], testi_matriisi[1])
    def test_korvaa_merkit(self):
        korvattava_merkkijono="hbeoaw"
        matriisi=aseta_kirjaimet_ja_numerot()
        verrattava_merkkijono=korvaa_merkit(korvattava_merkkijono, matriisi)
        self.assertNotEqual(verrattava_merkkijono, korvattava_merkkijono)