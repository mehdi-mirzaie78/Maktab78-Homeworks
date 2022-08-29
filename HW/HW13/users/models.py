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


# user1 = User('mehdi', 'mirzaie', 3242157397, 'Mehdi1378', 1000, id=5)
# user2 = User('reza', 'amin', 3242157137, 'Reza1379', 1000)
# db.create(user1)
# db.create(user2)
# db.read(User, 5)
# db.read(User, 6)
# db.delete(user1)
# print(user1.PK)
