# Testausdokumentti
### Testikattavauusraportti
![Kattavuusraportti](https://github.com/Jatynjala/Tira-harjoitustyo-Johannes-Tynjala/blob/main/dokumentaatio/kuvat/Kattavuusraportti.png)
### Millä testaus tehtiin?
Ohjelman funktioiden yksikkötestaus suoritetaan pytestilla.
### Testien toisto
Varmista, että koneessa on asennettuna poetry. Koska pyproject.toml-tiedosto on jo olemassa, suorita komento *poetry install* tarvittavien riippuvuuksien asentamiseksi.
Tämän jälkeen yksikkötestit voidaan suorittaa projektin juurihakemistossa komennolla *poetry run pytest koodi*.
Testikattavuusraportti voidaan generoida suorittamalla juurihakemistossa ensin komento *poetry run coverage run --branch -m pytest koodi* ja sitten *poetry run coverage html*. Tämän jälkeen raportin saa näkyviin avaamalla tiedosto index.html projektin htmlcov-hakemistosta.
### Suorituskyky testit
Testaamiseen käytetyt viestit(/-merkki ilmaisee rivinvaihtoa):

viesti 1: moro

viesti 2: moromaoonjonsku

viesti 3: moro/ma/oon/jonsku

viesti | salaus | salauksen purku
------ | ------ | ---------------
viesti 1 | 1 sekuntti | 1 sekuntti
viesti 2 | 1 sekuntti | reilusti yli 5 minuuttia
viesti 3 | 1 sekuntti | vajaa 2 sekunttia

Huomataan, että ohjelma toimii nopeammin, kun jokaisella rivillä enintään kuusi merkkiä. Pitemmät viestit kannattaa siten jakaa enintään kuuden merkin pituisiin osiin.
