# Käyttöohje
### Ennen käynnistystä
Jos aiot käyttää ohjelmaa viestin salaamiseen, kopioi salattavan viestin sisältö tekstitiedostoon *salattava_sisalto.txt* siten, että jokainen rivi sisältää pelkkiä pieniä kirjaimia pois lukien ääkköset, eikä tiedostossa ole tyhjiä rivejä eikä yhtäkään välilyöntiä. Lisäksi on tehokkuuden kannalta suositeltavaa, että jokainen rivi sisältää enintään kuusi kirjainta.

Jos taas aiot käyttää ohjelma salatun viestin purkamiseen, kopio salatun viestin sisältö sellaisenaan tekstitiedostoon *salattu_viesti.txt*. Varmista myös, että kyseisen viestin lähettäjä on lähettänyt myös merkkimatriisin ja lukumuunnoksen purkamissisällön, ja että ne ovat kopioituna sellaisenaan vastaavasti tiedostoihin *merkkimatriisi.txt* ja *luvuksi_muunnon_purkaus.txt*. Varmista lopuksi, että oma RSA-avaimesi on tallennettuna tiedostoon *oma_RSA_avain.txt*.
### Käynnistys
Ohjelma käynnistetään ajamalla koodi-hakemistossa komento *python kayttoliittyma.py* tai *python3 kayttoliittyma.py*. Heti käynnistämisen jälkeen ohjelma luo merkkimatriisin, jolla salattaessa korvataan salattavan viestin merkit ensin toisilla merkeillä ja sitten luvuilla. Tämän jälkeen ohjelma kysyy jotakin komennoista 0-4. Syötä komento pelkkänä numerona.
### Komento 0
Komento 0 nolla tarkistaa sopiiko tekstitiedostoon *salattava_sisalto.txt* tallennettu sisältö salattavaksi.
### Komento 1
Komento 1 generoi oman RSA-avaimen, joka koostuu kokonaisluvuista N, e ja d. Tämä avain tallennetaan tiedostoon *oma_RSA_avain.txt* muodossa 'N, e, d'. Tätä komentoa suositellaan ehdottomasti suoritettavaksi heti ensimmäisenä, mikäli käytät ohjelmaa ensimmäistä kertaa.
### Komento 2
Komento 2 kysyy ensin salattavan viestin vastaanottajan RSA-avaimen kokonaislukuja N ja e, ja sitten salaa tiedoston *salattava_sisalto.txt* sisällön. Salattu sisältö kirjoitetaan tiedostoon *salattu_viesti.txt* Lisäksi komento kirjoittaa salaamisessa käytetyn merkkimatriisin tiedostoon *merkkimatriisi.txt* ja lukumuunnoksen purkamiseen tarvittavan sisällön tiedostoon *luvuksi_muunnon_purkaus.txt*. Lähettä näiden kolmen tiedoston sisällöt erikseen vastaanottajalle sellaisenaan.
### Komento 3
Komento 3 purkaa tiedoston *salattu_viesti.txt* sisällön ja kirjoittaa puretun sisällön tiedostoon *purettu_viesti.txt*.
### Komento 4
Komento 4 sulkee ohjelman.
