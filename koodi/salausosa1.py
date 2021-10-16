from random import shuffle

def aseta_kirjaimet_ja_numerot():
    """Luo matriisin, johon tallennetaan vanhat merkit, uudet merkit ja vanhoja merkkejä vastaavat numerot"""
    merkit=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    valittavat_merkit=merkit[:]
    while merkit==valittavat_merkit:
        shuffle(valittavat_merkit)
    numerot=[x for x in range(1, 27)]
    shuffle(numerot)
    matriisi=[merkit, valittavat_merkit, numerot]
    return matriisi

def muuta_listaksi(merkkijono: str):
    """Muodostaa annetusta merkkijonosta listan"""
    tuloslista=[]
    for n in range(0, len(merkkijono)):
        tuloslista.append(merkkijono[n])
    return tuloslista

def korvaa_merkit(rivi: str, matriisi: list):
    """Korvaa annetun merkkijonon merkit annetun matriisin perusteella"""
    rivin_merkit=muuta_listaksi(rivi)
    for indeksi1 in range(0, len(rivin_merkit)):
        for indeksi2 in range(0, len(matriisi[0])):
            if matriisi[0][indeksi2]==rivin_merkit[indeksi1]:
                rivin_merkit[indeksi1]=matriisi[1][indeksi2]
                break
    yhdistaja=""
    uusirivi=yhdistaja.join(rivin_merkit)
    return uusirivi

if __name__ == "__main__":
    testi=aseta_kirjaimet_ja_numerot()
    print(testi)
    merkit="ahgdahqso"
    uudetmerkit=korvaa_merkit(merkit, testi)
    print(muuta_listaksi(uudetmerkit))
    print(uudetmerkit)