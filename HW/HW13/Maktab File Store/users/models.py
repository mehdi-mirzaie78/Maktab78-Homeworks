from core.models import DBModel
from core.managers import db, DBManager
from users.utils import Validator


class User(DBModel):
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
        if bool(age):
            self.age = Validator.age_validator(int(age))
        if id:
            self.id = id

    def register_in_database(self, dbman: DBManager = db):
        print('Your User ID is:', dbman.create(self))

    @staticmethod
    def register():
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        national_id = int(input("National ID: "))
        password = input("Password: ")
        balance = int(input("Balance: "))
        phone = input("Phone Number: (Skip: Press Enter) ")
        age = input("Age: (Skip: Press Enter) ")
        user = User(firstname, lastname, national_id, password, balance, phone, age)
        user.register_in_database()

    @classmethod
    def login_user(cls, dbman: DBManager = db):
        user_id = int(input("Enter User ID: "))
        password = input('Enter Password: ')
        user = dbman.read(cls, user_id)
        if user.password != password:
            raise ValueError("Wrong Password!")
        print(f"Wellcome {user.first_name} {user.last_name}")
        return user


class Seller(DBModel):
    TABLE = 'seller'
    PK = 'id'

    def __init__(self, first_name, last_name, password, id=None):
        self.first_name = Validator.name_validator(first_name)
        self.last_name = Validator.name_validator(last_name)
        self.password = Validator.pass_validator(password)
        if id:
            self.id = id

    def register_in_database(self, dbman: DBManager = db):
        print('Your Seller Id is:', dbman.create(self))

    @staticmethod
    def register():
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        password = input("Password: ")
        seller = Seller(firstname, lastname, password)
        seller.register_in_database()

    @classmethod
    def login_seller(cls, dbman: DBManager = db):
        seller_id = int(input("Enter Seller ID: "))
        password = input('Enter Password: ')
        seller: "Seller" = dbman.read(cls, seller_id)
        if seller.password != password:
            raise ValueError("Wrong Password!")
        print(f"Wellcome {seller.first_name} {seller.last_name}")
        return seller

# print(User.login_user())
# seller1 = Seller('mahdi', 'farokhi', 'Mahdi1380')
# seller1.register()

# user1 = User('mehdi', 'mirzaie', 3242157397, 'Mehdi1378', 1000, id=5)
# user1.register()
# user2 = User('reza', 'amin', 3242157137, 'Reza1379', 1000)
# db.create(user1)
# db.create(user2)
# db.read(User, 5)
# db.read(User, 6)
# db.delete(user1)
# print(user1.PK)
