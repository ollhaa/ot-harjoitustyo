import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.user_opa = User("opa", "opa1234")
        self.user_masa = User('masa', "masa5678")
        self.user_vili = User("vili", "vilili")

    def test_create_base(self):
        self.assertEqual(self.user_opa.username, "opa")
        self.assertEqual(self.user_opa.password, "opa1234")
        self.assertEqual(str(self.user_opa.created.year), "2023")

    def test_create(self):
        user_repository.create(self.user_opa)
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_opa.username)

    def test_find_all_users(self):
        user_repository.create(self.user_opa)
        user_repository.create(self.user_masa)
        user_repository.create(self.user_vili)
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 3)

    def test_delete_all_users(self):
        user_repository.create(self.user_opa)
        user_repository.create(self.user_masa)
        user_repository.create(self.user_vili)
        users = user_repository.find_all_users()

        user_repository.delete_all_users()
        users = user_repository.find_all_users()
        self.assertEqual(len(users), 0)

    #def test_find_by_username(self):
    #    user_repository.create(self.user_opa)
    #    user = user_repository.find_by_username("opa")
    #    self.assertEqual(user[0], "opa")


        



