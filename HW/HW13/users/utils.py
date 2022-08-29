import re


class Validator:
    @staticmethod
    def name_validator(name):
        pattern = re.compile(r'[a-zA-Z]{3,}')
        if not pattern.match(name):
            raise ValueError("Name must be alphabetic and more than 3 characters.")
        return name

    @staticmethod
    def phone_validator(phone):
        pattern = re.compile(r'^(\+989|09)\d{9}$')
        if not pattern.match(phone):
            raise ValueError("Invalid Phone number")
        return phone

    @staticmethod
    def national_id_validator(national_id):
        if not isinstance(national_id, int):
            raise ValueError("National ID must be an integer")
        if len(str(national_id)) < 10:
            raise ValueError("Invalid National ID")
        return national_id

    @staticmethod
    def age_validator(age):
        if age < 10:
            raise ValueError("Invalid age. Age must be over 10 years old")
        return age

    @staticmethod
    def pass_validator(password):
        if len(password) < 6:
            raise ValueError("Length of entered password must be more than 5")
        pattern = re.compile(r'[A-Z]+[a-z]+\d+')
        if not pattern.match(password):
            raise ValueError("Invalid Password. Password must contain at least 1 lowercase 1 uppercase and numbers")
        return password

    @staticmethod
    def balance_validator(balance):
        if balance < 100:
            raise ValueError("Minimum balance for each user is 100")
        return balance
