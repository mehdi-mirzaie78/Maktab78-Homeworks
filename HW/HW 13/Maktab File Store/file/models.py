from core.models import DBModel
from core.managers import DBManager, db


class File(DBModel):
    TABLE = 'files'
    PK = 'id'

    def __init__(self, seller_id, filename, size, path, price, id=None):
        self.seller_id = seller_id
        self.filename = filename
        self.size = size
        self.path = path
        self.price = price
        if id:
            self.id = id

    def register_in_database(self, dbman: DBManager = db):
        print('Your File ID is:', dbman.create(self))

    @staticmethod
    def create(seller_id: int):
        filename = input("File Name: ")
        size = float(input("Size: "))
        path = input("Path: ")
        price = int(input("Price: "))
        file = File(seller_id, filename, size, path, price)
        file.register_in_database()

    @classmethod
    def get(cls, file_id, dbman: DBManager = db):
        return dbman.read(cls, file_id)

    @classmethod
    def show_all_files(cls, dbman: DBManager = db):
        files = dbman.read_all_data(cls)
        for file in files:
            print(file)

    @classmethod
    def show_seller_files(cls, seller_id: int, dbman: DBManager = db):
        files = dbman.read_with_condition(cls, 'seller_id', seller_id)
        for file in files:
            print(file)
        return files

# file = File(2, 'HTML-CSS.pdf', 10, 'D://Files/New', 300)
# print(file)
# file.register_in_database()

# File.show_seller_files(1)
# print(60 * '-')
# File.show_seller_files(2)

# File.show_all_files()
# print('--------seller 1----------')
# File.show_seller_files(1)
# print('--------seller 2----------')
# File.show_seller_files(2)
