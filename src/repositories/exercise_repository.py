from database_connection import get_database_connection
from entities.exercise import Exercise

class ExerciseRepository:
    """Harjoituksien tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-luokan olio
        """
        self._connection = connection

    def find_all_exercises(self, username):
        """Palauttaa kaikki kirjatuneen käyttäjän harjoitukset tietokannasta.

        Args:
            username: Kirjatuneen käyttäjän nimi

        Returns:
            Palauttaa listan Exercise-luokan olioita.
        """
        cursor = self._connection.cursor()
        rows = cursor.execute("select * from exercises where username ==?", [username]).fetchall()
        return [Exercise(row["name"]) for row in rows]

    def add_new_exercise(self, exercise_name, username):
        """Tallentaa kirjatuneen käyttäjän uuden harjoituksen tietokantaan.

        Args:
            exercise_name: Tallennettavan harjoituksen nimi
            username: Kirjatuneen käyttäjän nimi

        """
        exr = exercise_name
        usrname = username
        cursor = self._connection.cursor()
        cursor.execute("insert into exercises (name, username) values(?,?)",
        (exr, usrname,)
        )
        self._connection.commit()

    def delete_all_exercises(self):
        """Poistaa kaikki harjoitukset tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from exercises")

        self._connection.commit()

exercise_repository = ExerciseRepository(get_database_connection())
