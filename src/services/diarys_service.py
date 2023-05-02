#from entities.exercise import Exercise
from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.excercise_repository import (
    exercise_repository as default_excercise_repository
)

from repositories.routine_repository import (
    routine_repository as default_routine_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class DiarysService:

    def __init__(self, user_repository=default_user_repository,
        exercise_repository = default_excercise_repository,
        routine_repository = default_routine_repository):
        self.user = None,
        self.user_repository = user_repository
        self.exercise_repository = exercise_repository
        self.routine_repository = routine_repository

    def create_user(self, username, password, login=True):
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self.user_repository.create(User(username, password))
        if login:
            self.user = user

        return user

    def find_all_exercises(self):
        exercises = self.exercise_repository.find_all_exercises()
        return exercises

    def add_new_exercise(self, excercise_name):
        self.exercise_repository.add_new_exercise(excercise_name)

    def add_new_routine(self, routine):
        for key, values in routine.items():
            for i in range(0, len(values[0])):
                ex = values[0][i]
                s = values[1][i]
                r = values[2][i]
                k = values[3][i]
                self.routine_repository.add_new_routine(key, ex, s, r, k)
                

    def login(self, username, password):

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self.user = user

        return user

    def logout(self):
        self.user = None


diarys_service = DiarysService()
