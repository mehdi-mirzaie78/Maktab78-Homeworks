from uuid import uuid4
from bank import BankAccount
from card import *
import pickle
from logger import logger
logger.name = 'USER'


class User:
    list_of_users = []

    def __init__(self, fullname, age, account: BankAccount):
        self.fullname = fullname
        self.age = age
        self.__id_code = uuid4().node % 1000
        print(f'your user id is: {self.__id_code}')
        self.account = account
        self.wallet = {}
        self.__class__.list_of_users.append(self)
        logger.info(f"User {fullname} with {self.__id_code} and bank account: {account}")
        self.dumper()

    def __repr__(self):
        return f"user: {self.fullname}"

    def dumper(self, filename='users.pickle'):
        with open(filename, 'ab') as file:
            pickle.dump(self, file)
        logger.info(f"user has pickled into {'users.pickle'}")

    def buy_card(self, card, charge=10):
        if card not in Card.CARDS:
            logger.error(f"CardError: You can't buy {card} because it's Invalid")
            raise CardError("You can't buy {card} because it's Invalid")
        if card == 'single_trip':
            self.account.withdraw(10)
            self.wallet[card] = Card(card)
            logger.info(f"{card} card added to {self.fullname}' wallet")

        elif card == 'credit':
            self.account.withdraw(charge)
            self.wallet[card] = Card(card, charge)
            logger.info(f"{card} card added to {self.fullname}' wallet")

        elif card == 'term':
            self.account.withdraw(charge)
            self.wallet[card] = Card(card, charge)
            logger.info(f"{card} card added to {self.fullname}' wallet")


# account1 = BankAccount('mehdi mirzaie', 23, 3242157397, 5000)
# account2 = BankAccount('reza amin', 22, 3242157392, 5000)

# mehdi = User('mehdi mirzaie', 23, account1)
# reza = User('reza amin', 22, account2)
# mehdi.buy_card('single_trip')

# mehdi.buy_card('credit', 230)
# mehdi.buy_card('term', 120)
# print(mehdi.account.balance)
# mehdi.wallet['single_trip'].pay()
# print(mehdi.wallet)
# mehdi.buy_card('single_trip')
# mehdi.wallet['single_trip'].pay()
# print(mehdi.wallet)

# this part is for unpickling data that we pickled in users.pickle
# def load_all(filename):
#     with open(filename, "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break
