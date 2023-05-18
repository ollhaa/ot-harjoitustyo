from database_connection import get_database_connection

class RoutineRepository:
    """Harjoitustapahtuman tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-luokan olio
        """
        self._connection = connection

    def add_new_routine(self, date, exr, sets, reps, kilos):
        """Tallentaa  uuden harjoitustapahtuman tietokantaan.

        Args:
            date: Harjoituskerran paivamaara
            exr: Harjoituskerran harjoitus
            sets: Harjoituskerran sarjat
            reps: Harjoituskerran toistot
            kilos: Harjoituskerran kilos

        """
        cursor = self._connection.cursor()
        cursor.execute("insert into routines (date, exercise, sets, reps, kilos) values(?,?,?,?,?)",
        (date,exr, sets, reps, kilos,)
        )
        self._connection.commit()

    def delete_all_routines(self):
        """Poistaa kaikki harjoitustapahtumat tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from routines")

        self._connection.commit()

    def delete_routine_by_id(self, id):
        cursor = self._connection.cursor()
        cursor.execute("delete from routines where id==?",[id])
        self._connection.commit()



    def find_all_routines(self):
        """Palauttaa kaikki harjoitustapahtumat tietokannasta.

        Returns:
            Palauttaa listan.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from routines")
        rows = cursor.fetchall()
        return rows



routine_repository = RoutineRepository(get_database_connection())
