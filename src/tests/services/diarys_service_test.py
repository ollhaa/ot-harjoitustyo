import unittest
from services.diarys_service import diarys_service
from entities.exercise import Exercise
from entities.user import User
from initialize_database import initialize_database

class TestDiarysService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.test_service = diarys_service
        self.test_service.logout()

    def test_login(self):
        self.assertEqual(self.test_service._user, None)
        self.test_service.login("qwerty", "1234")
        self.assertEqual(self.test_service._user.username, "qwerty")

    def test_login1(self):
        with self.assertRaises(ValueError):
            self.test_service.login("akin", "1234")

    def test_login2(self):
        with self.assertRaises(ValueError):
            self.test_service.login("qwerty", "99999")

    def test_logout(self):
        self.test_service.logout()
        self.assertEqual(self.test_service._user, None)

    def test_create_user(self):
        new_user = self.test_service.create_user("matt", "14141")
        self.assertEqual(new_user, True)

    def test_find_all_exercises(self):
        with self.assertRaises(AttributeError):
            exr = self.test_service.find_all_exercises()
        self.test_service.login("qwerty", "1234")
        exr = self.test_service.find_all_exercises()
        self.assertEqual(len(exr), 3)







