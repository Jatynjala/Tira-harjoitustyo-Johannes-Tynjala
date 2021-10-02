### Testikattavauusraportti
[Testikattavuusraportin saa näkyviin avaamalla tiedoston index.html](https://github.com/Jatynjala/Tira-harjoitustyo-Johannes-Tynjala/tree/main/htmlcov)
### Millä testaus tehtiin?
Ohjelman funktioiden yksikkötestaus suoritetaan pytestilla.
### Testien toisto
Varmista, että koneessa on asennettuna poetry. Koska pyproject.toml-tiedosto on jo olemassa, suorita komento 'poetry install' tarvittavien riippuvuuksien asentamiseksi.
Tämän jälkeen yksikkötestit voidaan suorittaa projektin juurihakemistossa komennolla 'poetry run pytest koodi'.
Testikattavuusraportti voidaan generoida suorittamalla juurihakemistossa ensin komento 'poetry run coverage run --branch -m pytest koodi' ja sitten 'poetry run coverage html'. Tämän jälkeen raportin saa näkyviin avaamalla tiedosto index.html projektin htmlcov-hakemistosta.
