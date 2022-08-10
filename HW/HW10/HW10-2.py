# 2022-08-10 15:08:08.066037
# Armstrong number:
# n = 153 = 1 ** 3 + 5 ** 3 + 3 ** 3

# states function is for storing amount of each digit ** 3
def states(number: int):
    for i in str(number):
        res = int(i) ** 3
        yield res


# is_armstrong function compares summation of states with the given number
# if both are equal then returns True otherwise returns False
def is_armstrong(num: int):
    return sum(states(num)) == num


print(is_armstrong(153))
