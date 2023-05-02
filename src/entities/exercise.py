class Exercise:
    """Luokka, jonka avulla luodaan harjoituksia.

    Attributes:
        name: Exercisen nimi.
    """
    def __init__(self, name):
        """Luokan konstruktori, joka luo uuden Exercisen.

        Args:
            name: Exercisen nimi.
        """
        self.name = name

    def get_name(self):
        """Palauttaa harjoituksen nimen
        """

        return self.name

