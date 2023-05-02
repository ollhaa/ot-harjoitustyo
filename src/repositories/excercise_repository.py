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
        self.connection = connection

    def find_all_exercises(self):
        """Palauttaa kaikki harjoitukset tietokannasta.

        Returns:
            Palauttaa listan Exercise-luokan olioita.
        """
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from exercises").fetchall()
        return [Exercise(row["name"]) for row in rows]

    def add_new_exercise(self, excercise_name):
        """Tallentaa  uuden harjoituksen tietokantaan.

        Args:
            excercise_name: Tallennettavan harjoituksen nimi.
        """
        exr = excercise_name
        cursor = self.connection.cursor()
        cursor.execute("insert into exercises values(?)",
        (exr,)
        )
        self.connection.commit()

    def delete_all_excercises(self):
        """Poistaa kaikki harjoitukset tietokannasta.
        """
        cursor = self.connection.cursor()
        cursor.execute("delete from exercises")

        self.connection.commit()


exercise_repository = ExcerciseRepository(get_database_connection())
