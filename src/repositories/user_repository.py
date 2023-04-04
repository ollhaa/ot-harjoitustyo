from database_connection import get_database_connection
from entities.user import User



class UserRepository:
    
    def __init__(self, connection):
        self.connection =connection


    def create(self, user):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert or ignore into users (username, password, created) values (?, ?, ?)",
            (user.username, user.password, user.created)
        )
        self.connection.commit()
        return user

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from users")

        self.connection.commit()

    def find_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

user_repository = UserRepository(get_database_connection())