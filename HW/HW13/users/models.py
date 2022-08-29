from core.models import DBModel
from core.managers import db
from users.utils import Validator


class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, first_name, last_name, national_id, password, balance, phone=None, age=None, id=None) -> None:
        self.first_name = Validator.name_validator(first_name)
        self.last_name = Validator.name_validator(last_name)
        self.national_id = Validator.national_id_validator(national_id)
        self.password = Validator.pass_validator(password)
        self.balance = Validator.balance_validator(balance)
        if phone:
            self.phone = Validator.phone_validator(phone)
        if age:
            self.age = Validator.age_validator(age)
        if id:
            self.id = id


user = User('mehdi', 'mirzaie', 3242157397, 'Mehdi1378', 1000)
db.create(user)