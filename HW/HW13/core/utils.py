from os import name as os_name, system as terminal
import re


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


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
        pattern = re.compile(r'[A-Z]+[a-z]+\d+')
        if not pattern.match(password):
            raise ValueError("Invalid Password. Password must contain")
        return password
