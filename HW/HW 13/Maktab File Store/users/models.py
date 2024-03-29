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

    @classmethod
    def read_all(cls, dbman: DBManager = db):
        return db.read_all_data(cls)


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
        list_of_items = []
        while True:
            File.show_all_files()
            print('---------------------------------')
            file_id = int(input('Enter The file_id: '))
            file = File.get(file_id)
            seller_id = int(input('Enter The seller_id: '))
            shopping_item = ShoppingItem(self.id, seller_id, file_id)
            shopping_item.register_in_database()
            # So far we have the item and we did not pay the price yet
            if self.balance < file.price:
                print("NOT Enough Balance!")
                break
            self.balance -= file.price
            dbman.update(self)
            shopping_item.payment_status = True
            list_of_items.append(shopping_item)
            control_key = input('[C]:Continue\n[F]:Finished\n =>> ').upper()
            if control_key == 'C':
                pass
            elif control_key == 'F':
                break
            else:
                print('Invalid Input!')

        report = Reports(self.id)
        report_id = report.register_in_database()
        for shopping_item in list_of_items:
            if shopping_item.payment_status:
                shopping_item.report_id = report_id
                dbman.update(shopping_item)
        else:
            print('Transaction Has Done Successfully')

    def charge_account_balance(self, dbman: DBManager = db):
        value = int(input('Amount: '))
        if value <= 0:
            raise ValueError("Money can't be zero and negative for charging your acount balance")
        self.balance += value
        dbman.update(self)
        print('Transaction Has Done Successfully')

    def update_information(self, dbman: DBManager = db):
        self.first_name = input("First Name: ")
        self.last_name = input("Last Name: ")
        self.password = input("Password: ")
        self.phone = input("Phone Number: (Skip: Press Enter) ")
        self.age = input("Age: (Skip: Press Enter) ")
        db.update(self)

    def show_user_files(self, dbman: DBManager = db):
        query = f"""SELECT filename, files.size, path, price FROM users
                JOIN shopping_item ON shopping_item.user_id = users.id
                JOIN files ON files.id = shopping_item.file_id
                WHERE user_id = {self.id};"""
        results = db.query(query)
        for item in results:
            print(item)

    def delete_account(self, dbman: DBManager = db):

        # This part is for the users who don't have any files
        db.delete(self)
        print('Your Account Has Deleted Successfully!')


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

    def create_files(self):
        while True:
            File.create(self.id)
            c = input('[C]: Create Another\n[F]: Finished\n =>> ').upper()
            if c == 'C':
                pass
            elif c == 'F':
                break
            else:
                print('Invalid Input!')

    def show_my_files(self):
        File.show_seller_files(self.id)