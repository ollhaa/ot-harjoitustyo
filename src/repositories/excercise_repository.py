from database_connection import get_database_connection
from entities.exercise import Exercise


class ExcerciseRepository:

    def __init__(self, connection):
        self.connection = connection

    def find_all_exercises(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from exercises").fetchall()
        print("rows: ")
        print(rows)
        return [Exercise(row["name"]) for row in rows]

    def add_new_exercise(self, excercise_name):
        exr = excercise_name
        cursor = self.connection.cursor()
        cursor.execute("insert into exercises values(?)",
        (exr,)
        )
        self.connection.commit()

    def delete_all_excercises(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from exercises")

        self.connection.commit()


exercise_repository = ExcerciseRepository(get_database_connection())
