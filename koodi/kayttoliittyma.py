from purkausosa import RSA_purku, pura_lukumuunnos, palauta_merkit
from salausosa1 import aseta_kirjaimet_ja_numerot, korvaa_merkit
from salausosa2 import RSA_avainten_muodostus
from salausosa3 import muuta_luvuksi, RSA_salaus
from tiedostonkasittely import kirjoita_oma_RSA_avain, lue_tiedosto_ja_tallenna_sisalto, tarkista_sisallon_sopivuus, kirjoita_sisalto, lue_oma_RSA_avain, kirjoita_merkkimatriisi, lue_merkkimatriisi

def generoi_avain():
    avain=RSA_avainten_muodostus()
    kirjoita_oma_RSA_avain(avain)

def kayttoliittyma():
    matriisi=aseta_kirjaimet_ja_numerot()
    print("Tervetuloa viestin salauskoneeseen!")
    while True:
        komento=input("Haluatteko: 0-tarkistaa viestinne salattavuuden, 1-generoida oman avaimen, 2-salata viestinne, 3-purkaa salauksen vai 4-sulkea ohjelman? :")
        if komento=="0":
            sisalto=lue_tiedosto_ja_tallenna_sisalto("salattava_sisalto.txt")
            sopiiko=tarkista_sisallon_sopivuus(sisalto, matriisi)
            if sopiiko:
                print("Viestisi sopii salattavaksi")
            print("")
        elif komento=="1":
            print("Generoidaan")
            generoi_avain()
            print("Avain generoitu")
            print("")
        elif komento=="2":
            sisalto=lue_tiedosto_ja_tallenna_sisalto("salattava_sisalto.txt")
            sopiva=tarkista_sisallon_sopivuus(sisalto, matriisi)
            if not sopiva:
                print("")
                continue
            salattu_sisalto=[]
            n=int(input("Mikä on vastaanottajan N? :"))
            e=int(input("Mikä on vastaanottajan e? :"))
            valiaikaisavain=(n, e)
            print("Salataan")
            luvuksi_muunnon_purkaus=[]
            for i in range(0, len(sisalto)):
                uusirivi=korvaa_merkit(sisalto[i], matriisi)
                luku=muuta_luvuksi(matriisi, uusirivi)
                luvuksi_muunnon_purkaus.append(luku[1])
                uusiluku=RSA_salaus(luku[0], valiaikaisavain)
                salattu_sisalto.append(uusiluku)
            kirjoita_sisalto(salattu_sisalto, "salattu_viesti.txt")
            kirjoita_sisalto(luvuksi_muunnon_purkaus, "luvuksi_muunnon_purkaus.txt")
            kirjoita_merkkimatriisi(matriisi)
            print("Viesti salattu")
            print("")
        elif komento=="3":
            print("Puretaan")
            purettava_sisalto=lue_tiedosto_ja_tallenna_sisalto("salattu_viesti.txt")
            kayttoavain=lue_oma_RSA_avain()
            kayttomatriisi=lue_merkkimatriisi()
            luvunpurku=lue_tiedosto_ja_tallenna_sisalto("luvuksi_muunnon_purkaus.txt")
            purettu_sisalto=[]
            for x in range(0, len(purettava_sisalto)):
                rsapurettu=RSA_purku(purettava_sisalto[x], kayttoavain[2], kayttoavain[0])
                luku_purettu=pura_lukumuunnos(rsapurettu, luvunpurku[x], kayttomatriisi)
                taysin_purettu=palauta_merkit(luku_purettu, kayttomatriisi)
                purettu_sisalto.append(taysin_purettu)
            kirjoita_sisalto(purettu_sisalto, "purettu_viesti.txt")
            print("Salaus purettu")
            print("")
        elif komento=="4":
            print("Kiitos salauskoneen käytöstä ja hyvää päivänjatkoa!")
            print("")
            break
        else:
            print("Tuntematon komento")
            print("")

if __name__=="__main__":
    kayttoliittyma()