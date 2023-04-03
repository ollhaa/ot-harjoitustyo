from user import User
from datetime import datetime

class Exercise:

    def __init__(self, user: User):
        self.user = user
        self.time = datetime.now()
        self.performances = {}
