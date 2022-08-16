# 2022-08-10 14:05:10.695266


class Indenter:

    def __init__(self):
        self.number = -1

    def print(self, value):
        print(self.number * '\t' + str(value))

    def __enter__(self):
        self.number += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.number -= 1
        return True


# Testing
with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the code...")
    indent.print("Torvalds")

# output
# ----------
# Hi
# 	Talk is Cheap!
# 		Show me the code...
# Torvalds
# ________________________________

# Explanation:
# Every time we use with statement __enter__ is called, we need to indent
# So number attribute will be added to 1. since we got out of the scope
# __exit__ is called and, we need to undo what we did so we subtract numer from 1.
