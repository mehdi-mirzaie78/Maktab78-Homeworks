from abc import ABC


class DBModel(ABC):  # abstract base Database model
    TABLE: str  # table name
    PK: str  # primary key column of the table

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {vars(self)}>"


class User(DBModel):
    TABLE = 'users'
    PK = 'id'

    def __init__(self, fullname, username, password, email, id=None):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        if id:
            self.id = id


user = User('mehdi', 23, '09182251753', 'mehdi@gmail.com')
