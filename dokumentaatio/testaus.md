# Testaus

Sovellusta on testattu erityisesti manuaalisesti projektin aikana, mutta myös automatidoiduilla testeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikkaluokkaa `DiarysService` testataan `TestDiarysServise`-testiluokan avulla.

### Repositoriot

Kolmea reposirioluokkaa: `UserRepository`, `ExerciseRepository`, ja `RoutineRepository` -luokkia testataan `TestUserRepository`, `TestExerciseRepository`, ja `TestRoutineRepository` luokkien avulla. 

### Muita huomioita

Testausta varten pitäisi muodostua uusi tietokanta test_databas.sqlite - minulla oli tämän kanssa ongelmia. Jokaista testiä varten tietokanta alustetaan. Huomaa, että alustuksen yhteydessä luodaan mallikäyttäjä, jonka nimi on "qwerty" ja salasana "1234".

Järjestelmätason testausta tehty manuaalisesti.

### Kattavuus

Kattavuus 86 % testatuissa luokissa. Testiraportin ulkopuolella mm. ui, initialize_databe.py, config.py ja index.py.

### Pylint

Koodin laatu 10.00/10.00

