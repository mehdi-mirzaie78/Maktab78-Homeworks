assert (False, "Why this AssertionError never raises ...?!",)

# We have a SyntaxWarning here, and it's not right to
# put assert condition into parentheses with ','
# because it makes that a tuple

# The reason why the parenthesis-version does not work
# is the assertion always evaluates True.
# This is because, in the boolean context,
# any non-empty tuple evaluates True.
# As a result, if you write the assert statement with parenthesis
# you are essentially writing assert(True).

t = (False,)      # => it's not empty so you know.☺
print(bool(t))    # True
