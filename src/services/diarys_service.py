#from entities.exercise import Exercise
from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class DiarysService:

    def __init__(self, user_repository=default_user_repository):
        self.user = None,
        self.user_repository = user_repository

    def create_user(self, username, password, login=True):
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self.user_repository.create(User(username, password))
        if login:
            self.user = user

        return user

    def login(self, username, password):

        user = self.user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self.user = user

        return user


diarys_service = DiarysService()
