import unittest
from purkausosa import RSA_purku, pura_lukumuunnos, palauta_merkit, RSA_salaus

class Testpurkaususosa(unittest.TestCase):
    def test_RSA_purku_toimii_oikein(self):
        alkuperainen_luku="4729"
        RSA_salattu_luku=RSA_salaus(alkuperainen_luku, (884339, 365921))
        RSA_purettu_luku=RSA_purku(RSA_salattu_luku, 701417, 884339)
        self.assertEqual(RSA_purettu_luku, alkuperainen_luku)
    def test_luvuksi_muunnon_purku_toimii_oikein(self):
        luku="26178"
        merkkijono="221"
        verrattava_merkkijono="fiv"
        matriisi=[["f", "i", "v"], ["v", "f", "i"], [26, 17, 8]]
        purettu_luku=pura_lukumuunnos(luku, merkkijono, matriisi)
        self.assertEqual(purettu_luku, verrattava_merkkijono)
    def test_merkkien_palautus_toimii_oikein(self):
        kasiteltava_merkkijono="fiv"
        matriisi=[["f", "i", "v"], ["v", "f", "i"], [26, 17, 8]]
        kasitelty_merkkijono=palauta_merkit(kasiteltava_merkkijono, matriisi)
        verrattava_merkkijono="ivf"
        self.assertEqual(verrattava_merkkijono, kasitelty_merkkijono)