import unittest
from salausosa2 import RSA_avainten_muodostus, SYT

class Testsalausosa2(unittest.TestCase):
    def test_RSA_avain_toimii_oikein1(self):
        testi_avain=RSA_avainten_muodostus()
        self.assertNotEqual(testi_avain[0], testi_avain[1])
    def test_RSA_avain_toimii_oikein2(self):
        testiavain=RSA_avainten_muodostus()
        self.assertNotEqual(testiavain[0], testiavain[2])
    def test_RSA_avain_toimii_oikein3(self):
        testiavain=RSA_avainten_muodostus()
        self.assertNotEqual(testiavain[1], testiavain[2])
    def test_avaimessa_vain_kokonaislukuja(self):
        testi_avain=RSA_avainten_muodostus()
        vastaus=True
        if isinstance(testi_avain[0], int)==False: vastaus=False
        if isinstance(testi_avain[1], int)==False: vastaus=False
        if isinstance(testi_avain[2], int)==False: vastaus=False
        self.assertTrue(vastaus)
    def test_SYT_toimii_oikein_jaottomat_luvut(self):
        tulos=SYT(47, 100)
        self.assertEqual(1, tulos)
    def test_SYT_toimii_oikein_jaolliset_luvut(self):
        testitulos=SYT(25, 400)
        self.assertEqual(testitulos, 25)