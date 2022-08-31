from core.router import Router, Route, CallBack

register_user = Route("Register Users", "Register Users Description...",
                      callback=CallBack("public.utils", "register_user"))

register_seller = Route("Register Sellers", "Register Sellers Description ...",
                        callback=CallBack("public.utils", "register_seller"))

register_users = Route("Register Sellers and Users", children=(register_user, register_user))

login_user = Route("Login User", callback=CallBack("public.utils", "login_user"))

about_us = Route("About us", callback=CallBack("public.utils", "about_us"))

main_menu = Route("Main Menu", "Main menu description ...", children=(about_us, register_user, login_user))

router = Router("File Store Router", main_menu)

# router = Router("File Store Router", Route(
#     "Main Menu",
#     "Main menu description ...",
#     children=(
#         Route("About us", callback=CallBack("public.utils", "about_us")),
#
#     )
# ))
