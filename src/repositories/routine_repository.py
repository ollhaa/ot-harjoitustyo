from database_connection import get_database_connection

class RoutineRepository:

    def __init__(self, connection):
        self.connection = connection

    def add_new_routine(self, date, exr, sets, reps, kilos):
        
        cursor = self.connection.cursor()
        cursor.execute("insert into routines (date, exercise, sets, reps, kilos) values(?,?,?,?,?)",
        (date,exr, sets, reps, kilos,)
        )
        self.connection.commit()


routine_repository = RoutineRepository(get_database_connection())
