from datetime import datetime

class User:
    """Luokka, jonka avulla luodaan käyttäjä.

    Attributes:
        username:  Userin nimi
        password: Userin salasana
        created: Usersin luomisaika.
    """

    def __init__(self, username: str, password: str):
        """Luokan konstruktori, joka luo uuden Userin.

        Args:
            username: Userin nimi
            password: Userin salasana.
        """
        self.username = username
        self.password = password
        self.created = datetime.now()
