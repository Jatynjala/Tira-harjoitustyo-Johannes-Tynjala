from salausosa1 import aseta_kirjaimet_ja_numerot, korvaa_merkit
from salausosa2 import RSA_avainten_muodostus
from salausosa3 import muuta_luvuksi, RSA_salaus
from tiedostonkasittely import kirjoita_oma_RSA_avain, lue_tiedosto_ja_tallenna_sisalto, tarkista_sisallon_sopivuus, kirjoita_salattu_viesti

def generoi_avain():
    avain=RSA_avainten_muodostus()
    kirjoita_oma_RSA_avain(avain)

def kayttoliittyma():
    matriisi=aseta_kirjaimet_ja_numerot()
    print("Tervetuloa viestin salauskoneeseen!")
    while True:
        komento=input("Haluatteko: 0-tarkistaa viestinne salattavuuden, 1-generoida oman avaimen, 2-salata viestinne vai 3-sulkea koneen? :")
        if komento=="0":
            sisalto=lue_tiedosto_ja_tallenna_sisalto()
            sopiiko=tarkista_sisallon_sopivuus(sisalto, matriisi)
            if sopiiko:
                print("Viestisi sopii salattavaksi")
            print("")
        elif komento=="1":
            generoi_avain()
            print("Avain generoitu")
            print("")
        elif komento=="2":
            sisalto=lue_tiedosto_ja_tallenna_sisalto()
            sopiva=tarkista_sisallon_sopivuus(sisalto, matriisi)
            if not sopiva:
                continue
            salattu_sisalto=[]
            n=int(input("Mikä on vastaanottajan N? :"))
            e=int(input("Mikä on vastaanottajan e? :"))
            avain=(n, e)
            print("Salataan")
            for i in range(0, len(sisalto)):
                uusirivi=korvaa_merkit(sisalto[i], matriisi)
                luku=muuta_luvuksi(matriisi, uusirivi)
                uusiluku=RSA_salaus(luku, avain)
                salattu_sisalto.append(uusiluku)
            kirjoita_salattu_viesti(salattu_sisalto)
            print("Viesti salattu")
            print("")
        elif komento=="3":
            print("Kiitos salauskoneen käytöstä ja hyvää päivänjatkoa!")
            break
        else:
            print("Tuntematon komento")
            print("")

if __name__=="__main__":
    kayttoliittyma()