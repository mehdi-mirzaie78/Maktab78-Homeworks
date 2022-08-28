from core.models import DBModel


class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, first_name, last_name, phone, national_id, age, password, id=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.national_id = national_id
        self.age = age
        self.password = password
        if id:
            self.id = id
