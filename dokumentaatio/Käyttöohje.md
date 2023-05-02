### Käyttöohje
---
Tämä sisältää käyttöohjeet sovellukselle. Päivittyvät jatkuvasti. 

## Vaatimukset
  * python 3.8 tai uudempi 
  * poetry 1.2.2 tai uudempi

## Asennus
Suorita `poetry install` hakemistossa ot-harjoitustyo.

Alustustoimenpiteet `poetry run invoke build`

## Käynnistäminen
Suorita komento `poetry run invoke start` hakemistossa ot-harjoitustyo.

## Testiraportti

Suorita komento `poetry run invoke coverage-report`

## Lint

Suorita komento `poetry run invoke lint`

## Sovelluksen käyttäminen

Päivittyy. Sovelluksen painikkeet ohjaavat käyttäjää. Ensimmäisessä näkymässä luodaan käyttäjänimi ja salasana. Mikäli ne on luotu, niin voidaan siityä kirjautumisnäkymään, jossa salasana ja käyttäjänimi annetaan. Harjoituksen lisäämisnäkymässä valitaan liike, päivämäätä, sarjat, toistot ja kilot, jonka jälkeen valinnat siirretään "add to routine" -painikkeella eteenpäin. Nämä valinnat voidaan tallentaa tietokantaan "Save the routine" -painikkeella. Tai poistaa "Delete selected" -painikkeella. 