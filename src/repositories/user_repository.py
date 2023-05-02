from database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Käyttäjän tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-luokan olio
        """
        self.connection = connection

    def create(self, user):
        """Tallentaa  uuden käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-luokan oliona.
        Returns:
            Tallennettu käyttäjän User-luokan oliona.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "insert or ignore into users (username, password, created) values (?, ?, ?)",
            (user.username, user.password, user.created)
        )
        self.connection.commit()
        return user

    def delete_all_users(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """
        cursor = self.connection.cursor()
        cursor.execute("delete from users")

        self.connection.commit()

    def find_by_username(self, username):
        """Etsii käyttäjän käyttäjätiedot tietokannasta.

        Args: 
            username: Etsittävän käyttäjän nimi
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,))

        founded = cursor.fetchone()

        return get_user_by_row(founded)

    def find_all_users(self):
        """Palauttaa kaikki käyttäjät tietokannasta.

        Returns:
            Palauttaa listan User-luokan olioita.
        """
        cursor = self.connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]


user_repository = UserRepository(get_database_connection())
