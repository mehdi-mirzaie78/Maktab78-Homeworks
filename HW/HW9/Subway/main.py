from Subway.exceptions import *
# from Subway.models.card import Card
from Subway.models.bank import BankAccount
# from Subway.models.user import User
# from Subway.models.trip import Trip
# from Subway.models.logger import *
"""Welcome to the best part of the programming which means creating interface"""
while True:
    print("""
    [1]: Register User
    [2]: Account Management
    [3]: Register On Trip
    [4]: Manager
    [5]: Exit
    """)
    control_key = int(input("Enter: "))

    if control_key == 1:
        from Subway.models.bank import BankAccount
        while True:
            print()
            name = input('Full name: ')
            age = int(input('Age: '))
            na_code = int(input('National code: '))
            balance = int(input('Balance: '))

            try:
                account = BankAccount(name, age, na_code, balance)
            except FullNameError:
                pass
            except AgeError:
                pass
            except NationalCodeError:
                pass
            except BalanceError:
                pass
            else:
                print(account)
                break
    elif control_key == 2:
        pass
    elif control_key == 3:
        pass
    elif control_key == 4:
        print('This part of the site is temporary down')
    else:
        print("Thanks for choosing us ☺")
        break
