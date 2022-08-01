from Subway.exceptions import *
from datetime import datetime


# Class of card for creating card for trip
class Card:
    CARDS = ('single_trip', 'credit', 'term')

    def __init__(self, name: str, charge: int | float | str = '', expiration_date: datetime | str = '') -> None:
        self.name = name
        self.charge = charge
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"card {self.name} - charge: {self.charge}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        if value not in self.__class__.CARDS:
            raise CardError("Invalid card.")
        self._name = value

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        if self.name != 'single_trip':
            if isinstance(value, int):
                if value <= 0:
                    raise ChargeError("charge can't be negative")
                self._charge = value
            else:
                raise TypeError("charge must be an int number")
        else:
            self._charge = 10  # price for only one trip

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if self.name == 'term':
            if not isinstance(value, datetime):
                raise TypeError("expiration date must be an instance of datetime")
            if value < datetime.today():
                raise DateError("your card has expired")
            self._expiration_date = value
        else:
            self._expiration_date = None

    # def charge_card(self, price):
    #     if self.name != 'single_trip':
    #         self.charge += price
    #     else:
    #         raise CardError("you can't charge single trip card")

    def pay(self, cost=10):
        if self.name == 'single_trip':
            if self.charge >= cost:
                self._charge -= cost
            else:
                raise ChargeError("you used your card before sorry")
        else:
            if self.charge >= cost:
                self.charge -= cost
            else:
                raise ChargeError("you don't have enough charge to pay the trip sorry")
