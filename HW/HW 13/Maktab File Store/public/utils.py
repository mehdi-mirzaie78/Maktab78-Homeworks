from configs import INFO as information
from users.models import User, Seller
from file.models import File


def about_us(*args):
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )


def show_all_files(*args):
    File.show_all_files()


def _exit(*args):
    exit()


def register_user(*args):
    User.register()


def login_user(*args):
    return User.login_user()


def buy_files(*args):
    user: User = args[0]
    user.buy_files()


def charge_account_balance(*args):
    user: User = args[0]
    user.charge_account_balance()


def update_info(*args):
    user: User = args[0]
    user.update_information()


def show_user_files(*args):
    user: User = args[0]
    user.show_user_files()


def delete_account(*args):
    user: User = args[0]
    user.delete_account()


##########################################################
def register_seller(*args):
    Seller.register()


def login_seller(*args):
    return Seller.login_seller()


def create_files(*args):
    seller: Seller = args[0]
    seller.create_files()


def show_my_files(*args):
    seller: Seller = args[0]
    seller.show_my_files()
