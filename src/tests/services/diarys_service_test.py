import unittest
from services.diarys_service import diarys_service
#from repositories.exercise_repository import exercise_repository
#from repositories.user_repository import user_repository
from entities.exercise import Exercise
from entities.user import User
from initialize_database import initialize_database

class TestDiarysSercise(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.test_service = diarys_service

    def test_login(self):
        self.test_service.login("qwerty", "1234")
        self.assertEqual(self.test_service._user.username, "qwerty")



