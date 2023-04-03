import unittest
#from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_opa = User('opa', 'opa1234')
        self.user_masa = User('masa', 'masa5678')

    def test_create(self):
        self.assertEqual(self.user_opa.username, "opa")
        self.assertEqual(self.user_opa.password, "opa1234")
        self.assertEqual(str(self.user_opa.created.year), "2023")
        
        
