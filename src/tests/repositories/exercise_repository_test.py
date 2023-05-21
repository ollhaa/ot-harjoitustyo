import unittest
from repositories.exercise_repository import exercise_repository
from repositories.user_repository import user_repository
from entities.exercise import Exercise
from entities.user import User
from initialize_database import initialize_database

class TestExcerciseRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.exr_eka = Exercise("Mave")
        self.exr_toka = Exercise('Penkki')

    def test_create_base(self):
        self.assertEqual(self.exr_eka.name, "Mave")
        name = self.exr_toka.get_name()
        self.assertEqual(name, "Penkki")

    def test_find_all_exercises(self):
        exrs = exercise_repository.find_all_exercises("qwerty")
        self.assertEqual(len(exrs), 3)
        exrs2 = exercise_repository.find_all_exercises("matti")
        self.assertEqual(len(exrs2), 0)

    def test_add_new_exercise(self):
        exercise_repository.add_new_exercise("Dippi", "qwerty")
        exrs = exercise_repository.find_all_exercises("qwerty")
        self.assertEqual(len(exrs), 4)
        exrs2 = exercise_repository.find_all_exercises("matti")
        self.assertEqual(len(exrs2), 0)

    def test_delete_all_exercises(self):
        exrs = exercise_repository.find_all_exercises("qwerty")
        self.assertEqual(len(exrs), 3)
        exercise_repository.delete_all_exercises()
        exrs = exercise_repository.find_all_exercises("qwerty")
        self.assertEqual(len(exrs), 0)





