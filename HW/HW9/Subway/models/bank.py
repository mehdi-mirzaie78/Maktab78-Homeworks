from Subway.exceptions import FullNameError, AgeError, \
    NationalCodeError, BalanceError, DepositError, \
    WithDrawError, LoginError
from uuid import uuid4
from Subway.models.logger import logger
logger.name = 'BANK'


class BankAccount:
    __clients = {}

    def __init__(self, full_name, age, national_code, balance):
        self.account_number = uuid4().node % 1000000
        print(f'your account number is: {self.account_number}')
        self.full_name = full_name
        self.age = age
        self.national_code = national_code
        self.min_balance = 100
        self.balance = balance
        self.__class__.__clients[self.account_number] = self
        logger.info(f"Bank account with {self.account_number} account number for {self.full_name} with {self.balance} balance has created.")

    def __repr__(self):
        return f"Bank account with {self.account_number} account number for {self.full_name} with {self.balance} balance has created."

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str):
            logger.error("FullNameError: your name must be string of characters")
            raise FullNameError("your name must be string of characters")
        if len(value) < 3:
            logger.error("FullNameError: name must be at least 3 characters")
            raise FullNameError("name must be at least 3 characters")
        if not all([x.isalpha() or x.isspace() for x in value]):
            logger.error("FullNameError: name must be alphabetic")
            raise FullNameError("name must be alphabetic")
        self._full_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            logger.error("AgeError: your age must be a number")
            raise AgeError("your age must be a number")
        if value <= 0:
            logger.error("AgeError: your age can't be zero or negative")
            raise AgeError("your age can't be zero or negative")
        self._age = value

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, value):
        if not isinstance(value, int):
            logger.error("NationalCodeError: you should enter your national code as a number")
            raise NationalCodeError("you should enter your national code as a number")
        if len(str(value)) != 10:
            logger.error("NationalCodeError: your national code must be 10 digits")
            raise NationalCodeError("your national code must be 10 digits")
        self._national_code = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            logger.error("BalanceError: balance must be int or float")
            raise BalanceError("balance must be int or float")
        if value < self.min_balance:
            logger.error("BalanceError: minimum balance is 100")
            raise BalanceError("minimum balance is 100")
        self._balance = value

    @classmethod
    def login_bank(cls, code):
        if not isinstance(code, int):
            logger.error("LoginError: Account number is an int number")
            raise LoginError("Account number is an int number")
        if code not in cls.__clients:
            logger.error("LoginError: Wrong Account Number")
            raise LoginError("Wrong Account Number")
        return cls.__clients[code]

    def deposit(self, money):
        if not isinstance(money, int) or not (isinstance(money, float)):
            logger.error("DepositError: money must be int or float number")
            raise DepositError("money must be int or float number")
        if money < self.min_balance:
            logger.error("DepositError: minimum money to deposit is 100")
            raise DepositError("minimum money to deposit is 100")
        self.balance += money
        logger.info(f"{money} deposited to {self.account_number} account with balance: {self.balance}")

    def withdraw(self, money):
        if not (isinstance(money, int) or isinstance(money, float)):
            logger.error("WithDrawError: money must be int or float number")
            raise WithDrawError("money must be int or float number")
        if money < 10:
            logger.error("WithDrawError: minimum money to withdraw is 10")
            raise WithDrawError("minimum money to withdraw is 10")
        if self.balance < money + 10:
            logger.error("WithDrawError: you don't have enough money")
            raise WithDrawError("you don't have enough money")
        self.balance -= money
        logger.info(f"{money} Withdraw from {self.account_number} account your current balance: {self.balance}")
