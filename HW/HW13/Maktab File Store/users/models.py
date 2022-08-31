from core.models import DBModel
from core.managers import db, DBManager
from users.utils import Validator
from file.models import File
from datetime import datetime


class ShoppingItem(DBModel):
    TABLE = 'shopping_item'
    PK = 'id'

    def __init__(self, user_id, seller_id, file_id, report_id=None, payment_status=False, id=None):
        self.user_id = user_id
        self.seller_id = seller_id
        self.file_id = file_id
        self.report_id = report_id
        self.payment_status = payment_status
        if id:
            self.id = id

    def register_in_database(self, dbman: DBManager = db):
        return dbman.create(self)


class Reports(DBModel):
    TABLE = 'reports'
    PK = 'id'

    def __init__(self, user_id, id=None):
        self.user_id = user_id
        self.date = datetime.today().date()
        if id:
            self.id = id

    def register_in_database(self, dbman: DBManager = db):
        return dbman.create(self)


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

    def buy_files(self, dbman: DBManager = db):
        File.show_all_files()
        print('---------------------------------')
        file_id = int(input('Enter The file_id: '))
        file = File.get(file_id)
        seller_id = int(input('Enter The seller_id: '))
        shopping_item = ShoppingItem(self.id, seller_id, file_id)
        shopping_item.register_in_database()
        # So far we have the item and we did not pay the price yet
        if self.balance < file.price:
            raise ValueError("NOT Enough Balance!")
        self.balance -= file.price
        dbman.update(self)
        shopping_item.payment_status = True

        report = Reports(self.id)
        shopping_item.report_id = report.register_in_database()
        dbman.update(shopping_item)
        print('Transaction Successfully')

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
# db.read(User, 6)
# db.delete(user1)
# print(user1.PK)
