# Käyttöohje

Lataa ensin uusin release.

## Vaatimukset
  * python 3.8 tai uudempi 
  * poetry 1.5.0 tai uudempi

## Asennus
Suorita `poetry install` hakemistossa ot-harjoitustyo.

Tee alustustoimenpiteet `poetry run invoke build`

## Käynnistäminen
Suorita komento `poetry run invoke start` hakemistossa ot-harjoitustyo.

## Testiraportti

Suorita komento `poetry run invoke coverage-report`

## Lint

Suorita komento `poetry run invoke lint`

## Sovelluksen käyttäminen
Sovelluksen painikkeet, virheilmoitukset ja erityisesti ikkuna `HELP` pyrkivät ohjaamaan käyttäjää. 
Ylhäällä näkyvät `LOGOUT`, `ADD?`, `EDIT?`, `ANALYTICS` ovat näkymiä joihin voit siirtyä, kun olet kirjatunut.

### Kirjatumismisnäkymä:
- Anna nimi ja salasana ja paina `Log In`.
- Siirry rekisteröitymään, jos tunnuksia ei ole painamalla `I do not have an account yet`

### Rekisteröitymismisnäkymä:
- Anna haluamasi nimi ja keksimäsi salasana kahdesti. Paina `Register`
- Tai siirry takaisin kirjatumisnäkymään painamalla `I already have an account` 

### Lisäämisnäkymä:
* Oman harjoituksen lisääminen
    - Lisää uusi liike kirjoittamalla nimi (esim. punnerrus) ja paina `Add to alternatives`
* Oman harjoitustapahtuman luominen
    - Valitse päivä kalenterista ja paina `Confirm date`
    - Valitse sarjat (=Sets), toistot (=Reps) ja kilot (=Kilos)
    - Varmista, että sinulla on liike valittuna, esim. aiemmin lisäämäsi punnerrus.
    - Paina `Add to routine` ja lisäämäsi tiedot siirtymät väliaikaiseen tilaan.
    - Nyt voit joko poistaa lisäämäsi painalalla `Delete added` tai tallentaa ne `Save the routine` 

### Muokkaamisnäkymä:
- Hae kymmentä (jos näitä on - et voi hakea tapahtumia, jos olet lisännyt vain yhden) viimeksi lisäämääsi harjoitustapahtumaa painamalla `Find`
- Poista näistä yksi kerrallaan valitsemalla tämä ja painamalla `Delete`

### Yhteenvetonäkymä:
- Valitse Today/This Month/This Year/All ja paina `Get stats`