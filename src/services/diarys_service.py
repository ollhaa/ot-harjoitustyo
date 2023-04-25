#from entities.exercise import Exercise
from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.excercise_repository import (
    exercise_repository as default_excercise_repository
)



class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class DiarysService:

    def __init__(self, user_repository=default_user_repository,
        exercise_repository = default_excercise_repository):
        self.user = None,
        self.user_repository = user_repository
        self.exercise_repository = exercise_repository

    def create_user(self, username, password, login=True):
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self.user_repository.create(User(username, password))
        if login:
            self.user = user

        return user

    def find_all_exercises(self, username):
        exercises = self.exercise_repository.find_all_exercises(username)
        return exercises

    def add_new_exercise(self, excercise_name, username):
        self.exercise_repository.add_new_exercise(excercise_name, username)

    def login(self, username, password):

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self.user = user

        return user

    def logout(self):
        self.user = None


diarys_service = DiarysService()
