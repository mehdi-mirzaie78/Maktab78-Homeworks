# 2022-07-27 16:05:31.567031
class DiscountError(Exception):

    def __init__(self, message='DiscountError! discount must be between 0 to 1'):
        super().__init__(message)


def apply_discount(price: int, discount: float) -> int | DiscountError:
    """
         This Function Calculates the Final Price
    --------------------------------------------------
    :param price: price of the product
    :param discount: discount for specific product
    :return final: final price with applying discount
    :raises `DiscountError`
    --------------------------------------------------
    """

    # final = int(price * (1 - discount))
    # assert 0 <= final <= price, DiscountError
    # return final

    final = int(price * (1 - discount))
    try:
        assert 0 <= final <= price
        return final
    except AssertionError:
        try:
            raise DiscountError
        except DiscountError as error:
            return error


print(apply_discount(10000, .2))    # 8000
print(apply_discount(10000, 1))     # 0
print(apply_discount(10000, -0.2))  # AssertionError DiscountError

# I really don't understand your questions.
# I hope this is the answer.
