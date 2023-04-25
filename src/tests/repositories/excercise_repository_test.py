import unittest
from repositories.excercise_repository import exercise_repository
from entities.exercise import Exercise

class TestExcerciseRepository(unittest.TestCase):
    def setUp(self):
        exercise_repository.delete_all_excercises()
        self.exr_eka = Exercise("Mave", "opa1234")
        self.exr_toka = Exercise('Penkki', "opa1234")


    def test_create_base(self):
        self.assertEqual(self.exr_eka.name, "Mave")
        self.assertEqual(self.exr_eka.username, "opa1234")

