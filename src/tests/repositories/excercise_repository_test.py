import unittest
from repositories.excercise_repository import exercise_repository
from entities.exercise import Exercise

class TestExcerciseRepository(unittest.TestCase):
    def setUp(self):
        exercise_repository.delete_all_excercises()
        self.exr_eka = Exercise("Mave")
        self.exr_toka = Exercise('Penkki')


    def test_create_base(self):
        self.assertEqual(self.exr_eka.name, "Mave")
        
    def test_find_all_exercises(self):
        exercise_repository.add_new_exercise("Mave")
        exrs = exercise_repository.find_all_exercises()
        self.assertEqual(len(exrs), 1)

