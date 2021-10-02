import unittest
from salausosa1 import aseta_kirjaimet_ja_numerot
from salausosa2 import RSA_avainten_muodostus
from salausosa3 import muuta_luvuksi, RSA_salaus

class Testsalausosa3(unittest.TestCase):
    def test_luvuksi_muuttaminen_toimii_oikein(self):
        matriisi=aseta_kirjaimet_ja_numerot()
        testisana="okrajacl"
        testiluku=muuta_luvuksi(matriisi, testisana)
        toimiiko=True
        for x in range(0, len(testiluku)):
            if testiluku[x] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                toimiiko=False
        self.assertTrue(toimiiko)
    def test_RSA_salaus_toimii_oikein(self):
        matriisi=aseta_kirjaimet_ja_numerot()
        sana="voiveljet"
        avain=RSA_avainten_muodostus()
        vanhaluku=muuta_luvuksi(matriisi, sana)
        uusiluku=RSA_salaus(vanhaluku, avain)
        n=avain[0]
        e=avain[1]
        vastaus=False
        if (int(uusiluku)-(int(vanhaluku)**e))%n==0:
            vastaus=True
        self.assertTrue(vastaus)