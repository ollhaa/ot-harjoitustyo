from datetime import datetime

class User:

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        self.created = datetime.now()

