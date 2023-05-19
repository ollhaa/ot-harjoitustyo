from database_connection import get_database_connection
from entities.exercise import Exercise


class ExcerciseRepository:
    """Harjoituksien tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-luokan olio
        """
        self._connection = connection

    def find_all_exercises(self, username):
        """Palauttaa kaikki harjoitukset tietokannasta.

        Returns:
            Palauttaa listan Exercise-luokan olioita.
        """
        cursor = self._connection.cursor()
        rows = cursor.execute("select * from exercises where username ==?", [username]).fetchall()
        return [Exercise(row["name"]) for row in rows]

    def add_new_exercise(self, excercise_name, username):
        """Tallentaa  uuden harjoituksen tietokantaan.

        Args:
            excercise_name: Tallennettavan harjoituksen nimi.
        """
        exr = excercise_name
        username= username
        cursor = self._connection.cursor()
        cursor.execute("insert into exercises (name, username) values(?,?)",
        (exr, username,)
        )
        self._connection.commit()

    def delete_all_excercises(self):
        """Poistaa kaikki harjoitukset tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from exercises")

        self._connection.commit()


exercise_repository = ExcerciseRepository(get_database_connection())
