def lue_tiedosto_ja_tallenna_sisalto():
    """Lukee annetun tekstitiedoston ja ottaa sen rivien sisällöt talteen listaan"""
    with open("salattava_sisalto.txt") as viesti:
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

def kirjoita_salattu_viesti(sisalto: list):
    """Kirjoittaa salatun viestin erilliseen tekstitiedostoon"""
    with open("salattu_viesti.txt", "w") as viesti:
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
            rivi=rivi.replace(", ", "")
            lista.append(rivi)
    n=lista[0][0]
    e=lista[0][1]
    d=lista[0][2]
    return (n, e, d)