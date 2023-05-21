# Vaatimusmäärittely: Gym Diaries
---
Sovelluksen avulla voi seurata omia kuntosaliharjoituksiaan. Sovelluksessa käyttäjä voi lisätä omia liikeitään, valita sarjat, toistot, kilot sekä
päivämäärän. Viimeisiä lisättyjä harjoitustapahtumia voi poistaa. Sovelluksen avulla voi myös seurata kuorman jakautumista eri liikkeiden välillä.

## Käyttäjät
Samaa sovellusta on mahdollisuus käyttää useamman käyttäjän omilla tunnuksillaan. Jokainen käyttäjä lisää omat liikeensä valikkoon ja näkee yhteenvedon vain omista harjoitustapahtumistaan.

## Käyttöliittymä
Sovellus koostuu viidestä eri näkymästä:

1. Kirjatumisnäkymä: Käyttäjä voi kirjautua sovellukseen, jos on jo rekisteröitynyt. Aloitusnäkymä.
2. Rekisteröitymismisnäkymä: Mikäli uudellä käyttäjällä ei vielä ole tunnuksia, niin tässä ne voi luoda.
3. Lisäämisnäkymä: Kirjatunut käyttäjä voi valita päivämäärä, kilot ja muut, ja tämän jälkeen tallenetaa tiedot väliaikaisen näkymän kautta.
4. Muokkaamisnäkymä: Kirjautunut käyttäjä voi poistaa yhden (korkeintaan) kymmenestä viimeisimmästä lisäämästään harjoitustapahtumasta kerrallaan.
5. Yhteenvetonäkymä: Kirjatunut käyttäjä voi muodostaa yhteenvedon tallentamistaa harjoitustapahtumista.

## Toiminnallisuudet

### Kirjatumisnäkymä: Aloitusnäkymä
* Käyttäjä voi kirjautua sovellukseen, jos on jo rekisteröitynyt.
    - Pyydetään nimeä ja salasanaa.
    - Voi siirtymä rekisteröitymään, jos tunnuksia ei ole.
    - Tulee lisäämisnäkymä automaattisesti, jos kirjatuminen on onnistunut

### Rekisteröitymismisnäkymä:
* Käyttäjä voi rekisteröityä sovellukseeen.
    - Pyydetään nimeä ja salasanaa kahdesti.
    - Voi siirtyä kirjatumisnäkymään, jos muistaa että tunnukset ovat olemassa.
    - Tulee kirjatumisnäkymä automaattisesti, jos rekisteröityminen on onnistunut.

### Lisäämisnäkymä:
* Käyttäjä voi tallentaa harjoituksiaan.
    - Voi lisätä oman kuntosaliharjoituksen listaan.
    - Pystyy valisemaan lisätyn harjoituksen, kilot, sarjat, toistot ja päivämäärän ja lisätä tapahtuman väliaikaiseen näkymään.
    - Voi poistaa väliaikaiseen tilaan lisätyt tiedot tai tallentaa nämä tietokantaan.
    - Käyttäjä voi kirjatua ulos, saada ohjeita painamalla 'Help' tai siirtymä muihin näkymiin.

### Muokkaamisnäkymä:
* Käyttäjä voi poistaa lisäämiään harjoitustapahtumiaan.
    - Käyttäjä saa haettua kymmenen viimeksi lisäämäänsä harjoitustapahtumaa.
    - Voi poistaa näistä yhden kerrallaan.
    - Käyttäjä voi kirjatua ulos, saada ohjeita painamalla 'Help' tai siirtymä muihin näkymiin.

### Yhteenvetonäkymä:
* Käyttäjä voi muodostaa yhteenvedon lisäämistään harjoitustapahtumista.
    - Voi valita aikaväliksi tämän päivän, kuluvan kuukauden, kuluvan vuoden tai kaikki.
    - Muodostetaan yhteenveto mm. tehdyistä harjoituksista ja nostetuista kiloista.
    - Muodostetaan nostettujen kilojen perusteella jakaumakuva eri liikkeiden välillä.
    - Käyttäjä voi kirjatua ulos, saada ohjeita painamalla 'Help' tai siirtymä muihin näkymiin.

## Puutteita ja epäonnistumisia:
- Ulkoasu ei täysin miellytä, esim. suhteelliset painikkeiden sijainnit yms.
- Koodin nimeäminen olisi voinut olla vielä kuvaavampaa.
- Joitakin luokkia olisi voinut jakaa kahdeksi saadun palautteen perusteella.
- Salasanat pitäisi tallentaa salattuna tietokantaan.

## Jatkokehitysideoita
- Harjoitusten (liikkeet poistaminen) valikosta.
- Harjoitustapahtumien poistamisen sijaan esim. päivämäärän muokkaaminen.
- Yhteenvetonäkymä mahdollistaisi todella paljon enemmän erilaista analyysia harjoitustapahtumista. Esim. viikkoatason rasitus yli ajan.
- Käyttäjä voi luoda samalla tunnuksella useamman harjoituspäiväkirjan erilaisia projekteja varten.
