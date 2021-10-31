def lue_tiedosto_ja_tallenna_sisalto(tiedostonimi: str):
    """Lukee annetun tekstitiedoston ja ottaa sen rivien sisällöt talteen listaan"""
    with open(tiedostonimi) as viesti:
        sisaltolista=[]
        for rivi in viesti:
            rivi=rivi.replace("\n", "")
            sisaltolista.append(rivi)
    return sisaltolista

def tarkista_sisallon_sopivuus(sisalto: list, matriisi: list):
    """Tarkistaa, että rivit sisältävät vain pieniä kirjaimia"""
    for n in range(0, len(sisalto)):
        for i in range(0, len(sisalto[n])):
            if sisalto[n][i] not in matriisi[0]:
                print("Viestin sisältö ei valitettavasti sovi salattavaksi.")
                print("Varmista, että viesti sisältää vain pieniä kirjaimia a:sta z:taan ilman välilyöntejä, tyhjiä rivejä tai turhia rivinvaihtoja.")
                return False
    return True

def kirjoita_sisalto(sisalto: list, tiedostonimi: str):
    """Kirjoittaa annetun sisällön erilliseen tekstitiedostoon"""
    with open(tiedostonimi, "w") as viesti:
        for i in range(0, len(sisalto)):
            uusirivi=sisalto[i]+"\n"
            viesti.write(uusirivi)

def kirjoita_oma_RSA_avain(avain: tuple):
    with open("oma_RSA_avain.txt", "w") as rsaavain:
        rsaavain.write(str(avain[0])+", "+str(avain[1])+ ", "+str(avain[2]))

def lue_oma_RSA_avain():
    lista=[]
    with open("oma_RSA_avain.txt") as rsaavain:
        for rivi in rsaavain:
            rivi=rivi.replace("\n", "")
            lista.append(rivi)
    uusilista=list(lista[0].split(", "))
    n=int(uusilista[0])
    e=int(uusilista[1])
    d=int(uusilista[2])
    return (n, e, d)

def kirjoita_merkkimatriisi(matriisi: list):
    yhdistaja=","
    rivi1=yhdistaja.join(matriisi[0])
    rivi2=yhdistaja.join(matriisi[1])
    kolmannen_rivin_merkit=[str(y) for y in matriisi[2]]
    rivi3=yhdistaja.join(kolmannen_rivin_merkit)
    rivit=[rivi1, rivi2, rivi3]
    with open("merkkimatriisi.txt","w") as tiedosto:
        for x in range(0, len(rivit)):
            uusirivi=rivit[x]+"\n"
            tiedosto.write(uusirivi)

def lue_merkkimatriisi():
    valiaikaislista=[]
    with open("merkkimatriisi.txt") as tiedosto:
        for rivi in tiedosto:
            rivi=rivi.replace("\n", "")
            valiaikaislista.append(rivi)
    rivi1=list(valiaikaislista[0].split(","))
    rivi2=list(valiaikaislista[1].split(","))
    rivi3beta=list(valiaikaislista[2].split(","))
    rivi3=[int(alkio) for alkio in rivi3beta]
    matriisi=[rivi1, rivi2, rivi3]
    return matriisi