from database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def create(self, user):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert or ignore into users (username, password, created) values (?, ?, ?)",
            (user.username, user.password, user.created)
        )
        self.connection.commit()
        return user

    def delete_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from users")

        self.connection.commit()

    def find_by_username(self, username):
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,))

        founded = cursor.fetchone()

        return get_user_by_row(founded)

    def find_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]


user_repository = UserRepository(get_database_connection())
