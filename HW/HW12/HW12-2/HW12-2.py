import re
import json


class User:
    users_data = {'users': []}
    users_object = {}

    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.__class__.users_data['users'].append(self.return_dict())

    def __repr__(self):
        return f'name: {self.name}, email: {self.email}, phone: {self.phone}'

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
        phone_pattern = re.compile(r'^(\+989|09)+\d{9}$')
        if not phone_pattern.match(value):
            raise ValueError("Invalid Phone Number")
        self._phone = value

    def return_dict(self):
        return {'name': self.name, 'email': self.email, 'phone': self.phone}

    @classmethod
    def save_json(cls):
        with open('users.json', 'w') as f:
            temp = cls.users_data
            json.dump(temp, f, indent=2, sort_keys=True)
        print(f'Your Data Has Successfully Saved in user.json')

    @classmethod
    def restore_json(cls):
        with open('users.json') as f:
            data = json.load(f)
            cls.users_object = {i['name']: User(**i) for i in data['users']}


try:
    user1 = User('Reza', 'reza@email.com', '09188524345')
    user2 = User('mehdi', 'mehdi@email.com', '09182251753')
except ValueError as ve:
    print(ve)

User.save_json()
User.restore_json()
print(User.users_object['Reza'], type(User.users_object['Reza']))
print(User.users_object['mehdi'], type(User.users_object['mehdi']))

# Now we have the User objects here.
# Thanks for your consideration
