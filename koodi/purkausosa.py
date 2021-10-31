from salausosa1 import muuta_listaksi
from salausosa3 import RSA_salaus

def RSA_purku(luku: str, d: int, n: int):
    """Purkaa RSA-salauksen"""
    verrattava_luku=int(luku)
    a=verrattava_luku**d
    jakojaannos=a%n
    while (verrattava_luku/3)%n!=jakojaannos:
        verrattava_luku-=1
    return str(int(verrattava_luku/3))

def pura_lukumuunnos(purettava_luku: str, purkaja: str, matriisi: list):
    """Purkaa lukumuunoksen"""
    purettavan_i=0
    tuloslista=[]
    for i in range(0, len(purkaja)):
        if purkaja[i]=="2":
            verrattava_luku=int(purettava_luku[purettavan_i:purettavan_i+2])
            for k in range(0, len(matriisi[0])):
                if matriisi[2][k]==verrattava_luku:
                    tuloslista.append(matriisi[0][k])
                    break
            purettavan_i+=2
        else:
            verrattava_luku=int(purettava_luku[purettavan_i])
            for k in range(0, len(matriisi[0])):
                if matriisi[2][k]==verrattava_luku:
                    tuloslista.append(matriisi[0][k])
                    break
            purettavan_i+=1
    yhdistaja=""
    tulosmerkkijono=yhdistaja.join(tuloslista)
    return tulosmerkkijono

def palauta_merkit(merkkijono: str, matriisi: list):
    """Palauttaa alkuperäiset merkit"""
    merkkilista=muuta_listaksi(merkkijono)
    for indeksi1 in range(0, len(merkkilista)):
        for indeksi2 in range(0, len(matriisi[1])):
            if matriisi[1][indeksi2]==merkkilista[indeksi1]:
                merkkilista[indeksi1]=matriisi[0][indeksi2]
                break
    yhdistaja=""
    uusimerkkijono=yhdistaja.join(merkkilista)
    return uusimerkkijono

if __name__=="__main__":
    uusiluku=RSA_purku("260704", 263543, 383233)
    print(uusiluku)
    matriisi=[["m", "o", "r"], ["m", "o", "r"], [3, 6, 11]]
    print(pura_lukumuunnos(uusiluku, "1121", matriisi))
    avain=(589597, 35303, 423767)
    testiluku=RSA_salaus(111724327, avain)
    print(testiluku)
    print(RSA_purku(testiluku, avain[2], avain[0]))