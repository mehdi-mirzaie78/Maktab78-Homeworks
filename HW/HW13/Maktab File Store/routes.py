from core.router import Router, Route, CallBack

# ################################# USERS ####################################
register_user = Route("Register Users", "Register Users Description...",
                      callback=CallBack("public.utils", "register_user"))

buy_files = Route("Buy Files", callback=CallBack("public.utils", "buy_files"))

login_user = Route("Login Users", "Login Users Description...",
                   callback=CallBack("public.utils", "login_user"), children=(buy_files,))

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
main_menu = Route("Main Menu", "< Main menu description >\n",
                  children=(about_us, users, sellers, _exit))

# Creating router for menu
router = Router("File Store Router", main_menu)
