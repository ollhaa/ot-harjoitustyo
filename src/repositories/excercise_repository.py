from database_connection import get_database_connection


class ExcerciseRepository:

    def __init__(self, connection):
        self.connection = connection

    def find_all_exercises(self, username):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from exercises where username=?", [username]).fetchall()
        return [Excercise(row["name"]) for row in rows]

    def add_new_exercise(self, excercise_name, username):
        cursor = self.connection.cursor()
        cursor.execute("insert into exercises (name, username) values (?, ?)",
        (excercise_name, username)
        )
        self.connection.commit()

    def delete_all_excercises(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from exercises")

        self.connection.commit()


exercise_repository = ExcerciseRepository(get_database_connection())
