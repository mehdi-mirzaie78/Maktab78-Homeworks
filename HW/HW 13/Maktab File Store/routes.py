from core.router import Router, Route, CallBack

# ################################# USERS ####################################
register_user = Route("Register Users", "Register Users Description...",
                      callback=CallBack("public.utils", "register_user"))

buy_files = Route("Buy Files", callback=CallBack("public.utils", "buy_files"))

charge_balance = Route("Charge Account Balance", callback=CallBack("public.utils", "charge_account_balance"))

update_info = Route("Update Information", callback=CallBack("public.utils", "update_info"))

show_user_files = Route("Show My Files", callback=CallBack("public.utils", "show_user_files"))

delete_account = Route("Delete Account", callback=CallBack("public.utils", "delete_account"))

login_user = Route("Login Users", "Login Users Description...",
                   callback=CallBack("public.utils", "login_user"),
                   children=(buy_files, charge_balance, show_user_files, update_info, delete_account))

users = Route("Users", children=(register_user, login_user))

# ################################# SELLERS ####################################
register_seller = Route("Register Sellers", "Register Sellers Description ...",
                        callback=CallBack("public.utils", "register_seller"))
create_files = Route("Create File", callback=CallBack("public.utils", "create_files"))

show_my_files = Route("Show My Files", callback=CallBack("public.utils", "show_my_files"))

login_seller = Route("Login Seller", callback=CallBack("public.utils", "login_seller"),
                     children=(create_files, show_my_files))

sellers = Route("Sellers", children=(register_seller, login_seller))

# ################################# ABOUT US ####################################
about_us = Route("About us", callback=CallBack("public.utils", "about_us"))

# #################################### EXIT #####################################
_exit = Route("Exit", callback=CallBack("public.utils", "_exit"))

# ################################# MAIN MENU ###################################
show_all_files = Route("Show All Files", callback=CallBack("public.utils", "show_all_files"))

main_menu = Route("Main Menu", "Main menu description\n",
                  children=(show_all_files, about_us, users, sellers, _exit))

# Creating router for menu
router = Router("File Store Router", main_menu)
