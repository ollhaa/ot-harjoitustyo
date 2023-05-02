import unittest
from datetime import datetime
from repositories.routine_repository import routine_repository

class TestRoutineRepository(unittest.TestCase):
    def setUp(self):
        routine_repository.delete_all_routines()

    
    def test_find_all_routines(self):
        date = datetime.strptime('01-01-2023', '%d-%M-%Y').date()
        exr = "bench press"
        sets = 4
        reps = 4
        kilos = 50
        routine_repository.add_new_routine(date, exr, sets, reps, kilos)
        routines = routine_repository.find_all_routines()

        self.assertEqual(len(routines), 1)

    def test_delete_all_routines(self):
        date = datetime.strptime('01-01-2023', '%d-%M-%Y').date()
        exr = "bench press"
        sets = 4
        reps = 4
        kilos = 50
        routine_repository.add_new_routine(date, exr, sets, reps, kilos)
        routines = routine_repository.delete_all_routines()
        
        self.assertEqual(routines, None)
        