# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne perustuu kolmikerrosmalliin, joissa eri tehtävät on pyritty eriyttämään. 

### Pakkausrakenne:

* UI vastaa käyttöliittymän asioista.
* SERVICES hoitaa varsinaisen sovelluslogiikan.
* REPOSITORIES vastaa yhteydestä tietokantaan eli tallentaa ja hakee tietoa kannasta.
* ENTITIES: user ja exercise luokat, joista käyttäjää ja harjoitusta kuvaavia olioita luodaan tiettujä tarpeita varten.

![arkkitehtuuri_kuva](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri.png)

## Käyttöliittymä

Sovellus koostuu viidestä eri näkymästä.

### Kirjatumisnäkymä 
- Käyttäjä voi kirjautua sovellukseen, jos on jo rekisteröitynyt. Aloitusnäkymä.
![Login](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Log.png)

### Rekisteröitymismisnäkymä
- Mikäli uudellä käyttäjällä ei vielä ole tunnuksia, niin tässä ne voi luoda.
![Create](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Create_new_user.png)

### Lisäämisnäkymä
- Kirjatunut käyttäjä voi valita päivämäärä, kilot ja muut, ja tämän jälkeen tallenetaa tiedot väliaikaisen näkymän kautta.
![Add](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Add_view.png)

### Muokkaamisnäkymä
- Kirjautunut käyttäjä voi poistaa yhden (korkeintaan) kymmenestä viimeisimmästä lisäämästään harjoitustapahtumasta kerrallaan.
![Edit](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Edit_view.png)

### Yhteenvetonäkymä
- Kirjatunut käyttäjä voi muodostaa yhteenvedon tallentamistaa harjoitustapahtumista.
![Analytics](https://github.com/ollhaa/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Analytics_view.png)

## Tallentaminen

Repositories pakkauksen luokat UserReposirory, ExerciseRepository ja RoutineRepository ovat yhteydessä Sqlite-tietokantaan eli tallentavat ja hakevat tietoa kannasta. Tietokantatauluja on yhteensä kolme: Users, Exercises ja Routines. Käyttäjän omien tietojen tallentamisessa ja tietojen hakemisessa hyödynnetään kirjatuneen käyttäjän nimeä, joten tauluista voidaan hakea tietoa ilman liitoksia. 

Tietokanta alustetaan komennolla `poetry run invoke build` ja konfiguraatiotiedot ovat .env tiedostossa. 

Testaamisesta varten käytetään (tässä ongelmia) testitietokantaa.

## Toiminta

Sovelluksen toiminnallisuuksia on käsitelty käyttöohjeessa melko kattavasti. Alla käsitellään esimerkinomaisesti joitakin toimintoja sekvenssikaavion avulla.

### Uuden käyttäjän luominen

Kun käyttäjä on syöttänyt oman uuden käyttäjänimensä ja salasanansa (kahteen kertaan tarkastuksen kanssa),ja pituudet yms. ovat sallittuja, ja painaa tämän jälkeen 
"Register", niin tapahtuu seuraavasti:


### Kirjautuminen sisään 

Kun käyttäjä on syöttänyt jo olemassa olevan käyttäjänimen ja salasanan, ja painaa "Log In", niin tapahtuu seuraavaa:

