# Arkkitehtuutikuvaus

## Rakenne

Sovelluksen rakenne perustuu kolmikerrosmalliin, joissa eri tehtävät on pyritty eriyttämään. 

### Pakkausrakenne:

* UI vastaa käyttöliittymän asioista.
* SERVICES hoitaa varsinaisen sovelluslogiikan.
* REPOSITORIES vastaa yhteydestä tietokantaan eli tallentaa ja hakee tietoa kannasta.
* ENTITIES: user ja exercise luokat, joista käyttäjää ja harjoitusta kuvaavia olioita luodaan tiettujä tarpeita varten.

![arkkitehtuuri_kuva](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri_1.jpg)

## Käyttöliittymä

Sovellus koostuu viidestä eri näkymästä.

### Kirjatumisnäkymä 
- Käyttäjä voi kirjautua sovellukseen, jos on jo rekisteröitynyt. Aloitusnäkymä.

### Rekisteröitymismisnäkymä
- Mikäli uudellä käyttäjällä ei vielä ole tunnuksia, niin tässä ne voi luoda.

### Lisäämisnäkymä
- Kirjatunut käyttäjä voi valita päivämäärä, kilot ja muut, ja tämän jälkeen tallenetaa tiedot väliaikaisen näkymän kautta.

### Muokkaamisnäkymä
- Kirjautunut käyttäjä voi poistaa yhden (korkeintaan) kymmenestä viimeisimmästä lisäämästään harjoitustapahtumasta kerrallaan.

### Yhteenvetonäkymä
- Kirjatunut käyttäjä voi muodostaa yhteenvedon tallentamistaa harjoitustapahtumista.

## Tallentaminen

Repositories pakkauksen luokat UserReposirory, ExerciseRepository ja RoutineRepository ovat yhteydessä Sqlite-tietokantaan eli tallentavat ja hakevat tietoa kannasta. Tietokantatauluja on yhteensä kolme: Users, Exercises ja Routines. Käyttäjän omien tietojen tallentamisessa ja tietojen hakemisessa hyödynnetään kirjatuneen käyttäjän nimeä, joten tauluista voidaan hakea tietoa ilman liitoksia. 

Tietokanta alustetaan komennolla `poetry run invoke build` ja konfiguraatiotiedot ovat .env tiedostossa. 

Testaamisesta varten käytetään (tässä ongelmia) testitietokantaa.

## Toiminta
