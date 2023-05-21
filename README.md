# Ohjelmistotekniikka: Gym Diaries
Sovelluksen avulla voi seurata omia kuntosaliharjoituksiaan. Sovelluksessa käyttäjä voi lisätä omia liikeitään, valita sarjat, toistot, kilot sekä päivämäärän. Viimeisiä lisättyjä harjoitustapahtumia voi poistaa. Sovelluksen avulla voi myös seurata kuorman jakautumista eri liikkeiden välillä.

Huomaa, että voit halutessasi kokeilla sovellusta lataamisen ja asennuksen jälkeen testitunnuksilla:

username: qwerty
password: 1234

## Dokumentit

[Määrittelydokumentti](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) \
[Käyttöohje](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6ohje.md) \
[Arkkitehtuuri](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md) \
[Testausdokumentti](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md) \
[Tuntikirjanpito](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md) \
[Changelog](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md) \
[Viikon 6 Release](https://github.com/ollhaa/ot-harjoitustyo/releases/tag/viikko6)

## Huomioita

Vaatimuksina on `Python 3.8` tai uudempi ja `poetry 1.5.0` tai uudempi

## Ohjeet lyhyesti

Tarkemmin käyttämisestä `Käyttöohjeessa`

### Asennus

Lataa uusin release: Linkki uusimpaan löytyy hieman ylempää kohdasta Dokumentit.

Suorita `poetry install` hakemistossa ot-harjoitustyo.

Alustustoimenpiteet `poetry run invoke build`

### Käynnistäminen

Suorita komento `poetry run invoke start` hakemistossa ot-harjoitustyo.

### Testikattavuus ja Pylint

Testit voidaan suorittaa komennolla:
`poetry run invoke test`

Testiraportin saa komennolla:
`poetry run invoke coverage-report`

Testiraportin löydät htmlcov-hakemista.

Pylint voidaan suorittaa komennolla:
`poetry run invoke lint`

