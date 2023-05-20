import unittest
from datetime import datetime
from repositories.routine_repository import routine_repository
from initialize_database import initialize_database

class TestRoutineRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()

    def test_find_all_routines(self):
        date = datetime.strptime('01-01-2023', '%d-%M-%Y').date()
        exr = "bench press"
        sets = 4
        reps = 4
        kilos = 50
        username = "qwerty"
        routine_repository.add_new_routine(username, date, exr, sets, reps, kilos)
        routines = routine_repository.find_all_routines("qwerty")
        self.assertEqual(len(routines), 1)

    def test_delete_all_routines(self):
        date = datetime.strptime('01-01-2023', '%d-%M-%Y').date()
        exr = "bench press"
        sets = 4
        reps = 4
        kilos = 50
        username = "qwerty"
        routine_repository.add_new_routine(username,date, exr, sets, reps, kilos)
        routine_repository.delete_all_routines()
        routines = routine_repository.find_all_routines("qwerty")
        self.assertEqual(len(routines), 0)
        
    def test_delete_routine_by_id(self):
        date = datetime.strptime('01-01-2023', '%d-%M-%Y').date()
        exr = "bench press"
        sets = 4
        reps = 4
        kilos = 50
        username = "qwerty"
        routine_repository.add_new_routine(username, date, exr, sets, reps, kilos)
        routines = routine_repository.find_all_routines("qwerty")
        self.assertEqual(len(routines), 1)
        routine_repository.delete_routine_by_id(1)
        routines = routine_repository.find_all_routines("qwerty")
        self.assertEqual(len(routines), 0)
