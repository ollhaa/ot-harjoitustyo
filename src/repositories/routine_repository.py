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

    def add_new_routine(self, username, date, exr, sets, reps, kilos):
        """Tallentaa  uuden harjoitustapahtuman tietokantaan.

        Args:
            username: Kirjautuneen käyttäjän nimi
            date: Harjoituskerran paivamaara
            exr: Harjoituskerran harjoitus
            sets: Harjoituskerran sarjat
            reps: Harjoituskerran toistot
            kilos: Harjoituskerran kilos

        """
        cursor = self._connection.cursor()
        cursor.execute(
        "insert into routines (username, date, exercise, sets, reps, kilos) values(?,?,?,?,?,?)",
        (username,date,exr, sets, reps, kilos,)
        )
        self._connection.commit()

    def delete_all_routines(self):
        """Poistaa kaikki harjoitustapahtumat tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from routines")

        self._connection.commit()

    def delete_routine_by_id(self, id_num):
        """Poistaa harhoitustapahtuman tämän id:n perusteella.

        Args:
            id_num: harjoitustapahtuman id
        """
        id_ = id_num
        cursor = self._connection.cursor()
        cursor.execute("delete from routines where id==?",[id_])
        self._connection.commit()

    def find_all_routines(self,username):
        """Palauttaa kaikki harjoitustapahtumat tietokannasta.

        Args:
            username: Kirjautuneen käyttäjän nimi

        Returns:
            Palauttaa listan harhoitustapahtumista.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from routines where username==?",[username])
        routines = cursor.fetchall()
        return routines

routine_repository = RoutineRepository(get_database_connection())
