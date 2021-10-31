from salausosa1 import muuta_listaksi, aseta_kirjaimet_ja_numerot
from salausosa2 import RSA_avainten_muodostus

def muuta_luvuksi(matriisi: list, merkkijono: str):
    """Muuttaa annetun merkkijonon kokonaisluvuksi annetun matriisin avulla"""
    valilista=muuta_listaksi(merkkijono)
    luvusta_muuntamislista=[]
    for n in range(0, len(valilista)):
        for k in range(0, len(matriisi[0])):
            if matriisi[0][k]==valilista[n]:
                valilista[n]=str(matriisi[2][k])
                if matriisi[2][k]>9:
                    luvusta_muuntamislista.append("2")
                else:
                    luvusta_muuntamislista.append("1")
                break
    yhdistaja=""
    tulosluku=yhdistaja.join(valilista)
    luvusta_muuntamismerkkijono=yhdistaja.join(luvusta_muuntamislista)
    return (tulosluku, luvusta_muuntamismerkkijono)

def RSA_salaus(luku: str, avain: tuple):
    """Laskee annetusta luvusta annetun avaimen avulle uuden luvun, joka on salattu viesti"""
    n=avain[0]
    e=avain[1]
    a=(int(luku))**e
    jakojaannos=a%n
    uusiluku=3*(int(luku))
    while uusiluku%n!=jakojaannos:
        uusiluku+=1
    return str(uusiluku)

if __name__ == "__main__":
    avain=RSA_avainten_muodostus()
    print(avain)
    sana="ja"
    matriisi=aseta_kirjaimet_ja_numerot()
    n=muuta_luvuksi(matriisi, sana)
    print(n)
    c=RSA_salaus(n, avain)
    print(c)