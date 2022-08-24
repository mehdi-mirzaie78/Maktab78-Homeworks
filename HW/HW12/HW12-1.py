import re


class User:
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_pattern = re.compile(r'[a-zA-Z_]{4,14}')
        if not name_pattern.match(value):
            raise ValueError("Invalid Name!")
        self._name = value

    @property
    def email(self):
        return self._email

    # [a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-] Complete Regex
    # I knew how to write complete regex but, you didn't ask for
    @email.setter
    def email(self, value):
        email_pattern = re.compile(r'[a-zA-Z]{4,}@[a-zA-Z]+\.[a-zA-Z]+')
        if not email_pattern.match(value):
            raise ValueError("Invalid Email!")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        phone_pattern = re.compile(r'(\+989|09)+\d{9}')
        if not phone_pattern.match(value):
            raise ValueError("Invalid Phone Number")
        self._phone = value

    def __repr__(self):
        return f'name: {self.name} email: {self.email} phone number: {self.phone}'


try:
    user = User('Reza', 'reza@email.com', '09188524345')
except ValueError as ve:
    print(ve)
else:
    print(user)
