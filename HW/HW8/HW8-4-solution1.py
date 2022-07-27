# 2022-07-27 12:51:45.617801
# HW8-4
# ===========================================================
# As we know assertion is for debugging,
# and it should not be used for validations of input data
# the reason is it can be deactivated by -O command.
# if we run a python file in terminal with -O command
# it deactivates all assertions in the python file.

"""
In general, you shouldn't use assertions for
data processing or data validation, 
because you can disable assertions in your production code,
which ends up removing all your assertion-based processing and validation code.
"""


class DiscountError(Exception):
    pass


def discount_normalize(discount: float) -> float:
    """
    :param discount: discount of the product
    :return normalized discount
    :raises `DiscountError`
    """
    if discount <= 0:
        raise DiscountError("Discount can't be negative!")
    elif discount >= 1:
        raise DiscountError("Discount can't be >= 1")
    return discount


def apply_discount(price: int, discount: float) -> int:
    """
         This Function Calculates the Final Price
    --------------------------------------------------
    :param price: price of the product
    :param discount: discount for specific product
    :return final: final price with applying discount
    :raises `DiscountError`
    --------------------------------------------------
    """
    final = ''
    try:
        final = int(price * (1 - discount_normalize(discount)))
    except DiscountError as de:
        print('DiscountError!', de, end=' ')
    return final


print(apply_discount(10000, .2))    # 8000
print(apply_discount(10000, -.2))   # DiscountError! Discount can't be negative!
print(apply_discount(10000, 1))     # DiscountError! Discount can't be >= 1
print(apply_discount(10000, .6))    # 4000
