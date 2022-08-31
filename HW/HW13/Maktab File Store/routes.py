from core.router import Router, Route, CallBack

# ################################# Users ####################################
register_user = Route("Register Users", "Register Users Description...",
                      callback=CallBack("public.utils", "register_user"))

login_user = Route("Login Users", "Login Users Description...",
                   callback=CallBack("public.utils", "login_user"))

users = Route("Users", children=(register_user, login_user))

# ################################# Sellers ####################################
register_seller = Route("Register Sellers", "Register Sellers Description ...",
                        callback=CallBack("public.utils", "register_seller"))

login_seller = Route("Login Seller", callback=CallBack("public.utils", "login_seller"))

sellers = Route("Sellers", children=(register_seller, login_seller))

# ################################# ABOUT US ####################################
about_us = Route("About us", callback=CallBack("public.utils", "about_us"))

main_menu = Route("Main Menu", "Main menu description ...", children=(about_us, users, sellers))

router = Router("File Store Router", main_menu)

# router = Router("File Store Router", Route(
#     "Main Menu",
#     "Main menu description ...",
#     children=(
#         Route("About us", callback=CallBack("public.utils", "about_us")),
#
#     )
# ))
