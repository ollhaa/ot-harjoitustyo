from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.exercise_repository import (
    exercise_repository as default_exercise_repository
)

from repositories.routine_repository import (
    routine_repository as default_routine_repository
)

class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass

class DiarysService:
    """Sovelluslogiikasta vastaa luokka
    
    Attributes:
        user: kirjautunut käyttäjä
        user_repository: käyttäjätietojen käsittelyyn
        exercise_repository: harjoitusten käsittelyyn
        routine_repository: harjoitustapahtumien käsittelyyn
    """
    def __init__(self, user_repository=default_user_repository,
        exercise_repository = default_exercise_repository,
        routine_repository = default_routine_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-luokan olio.
            exercise_repository:
                Vapaaehtoinen, oletusarvoltaan ExerciseRepository-luokan olio.
            routine_repository:
                Vapaaehtoinen, oletusarvoltaan RoutineRepository-luokan olio.
        """
        self._user = None
        self._user_repository = user_repository
        self._exercise_repository = exercise_repository
        self._routine_repository = routine_repository

    def create_user(self, username, password):
        """Luo uuden käyttäjän.
        Args:
            username: Käyttäjän käyttäjänimi
            password: Käyttäjän salasana
        
        Returns:
            Luotu käyttäjä User-luokan oliona.
        """
        return self._user_repository.create(User(username, password))

    def find_all_exercises(self):
        """Palauttaa kaikki harjoitukset.

        Returns:
            Lista harjoituksista
        """
        username = self._user.username
        exercises = self._exercise_repository.find_all_exercises(username)
        return exercises

    def add_new_exercise(self, exercise_name):
        """Lisää tietokantaan uuden harjoituksen.

        Args:
            excercise_name: harjoituksen nimi
        """
        username = self._user.username
        self._exercise_repository.add_new_exercise(exercise_name, username)

    def add_new_routine(self, routine):
        """Lisää uuden harjoitustapahtuman

        Args:
            routine: sanakirja, jossa tiedot
        """
        username = self._user.username
        for key, values in routine.items():
            for i in range(0, len(values[0])):
                exr_ = values[0][i]
                sets_ = values[1][i]
                reps_ = values[2][i]
                kilos_ = values[3][i]
                self._routine_repository.add_new_routine(username,key, exr_, sets_, reps_, kilos_)

    def find_all_routines(self):
        """Palauttaa kaikki kirjatuneen käyttäjän harjoitustapahtumat.

        Returns:
            Lista harjoitustapahtumista
        """
        username = self._user.username
        routines = self._routine_repository.find_all_routines(username)
        return routines

    def delete_routine_by_id(self, id_num):
        """Poistaa harjoitustapahtuman tämän id-numeron perusteella.

        Args:
            id_num: Harjoitustapahtuman id-numero
        """
        id_ = id_num
        self._routine_repository.delete_routine_by_id(id_)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.
        Args:
            username: Käyttäjän antama nimi
            password: Käyttäjän antama salasana

        """
        user = self._user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise ValueError

        self._user = user
        #return user

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None


diarys_service = DiarysService()
