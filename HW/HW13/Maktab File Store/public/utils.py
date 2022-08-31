from configs import INFO as information
from users.models import User, Seller


def about_us():
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )


def register_user():
    User.register()


def register_seller():
    Seller.register()


def login_user():
    User.login_user()
