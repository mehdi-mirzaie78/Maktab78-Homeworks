from Decorator import process_timer, cache
# from functools import cache
from sys import setrecursionlimit


@process_timer
def fibo_no_cache(num: int):
    def fibonacci(n=num):
        if n in (0, 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci()


@process_timer
def fibo_cache(num: int):
    @cache
    def fibonacci(n=num):
        if n in (0, 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci()


@process_timer
def fact_no_cache(num):
    def factorial(number=num):
        if number == 1:
            return 1
        else:
            return number * factorial(number - 1)

    return factorial()


@process_timer
def fact_cache(num):
    @cache
    def factorial(number=num):
        if number == 1:
            return 1
        else:
            return number * factorial(number - 1)

    return factorial()


print(f'{fibo_cache(35)=}')
print(f'{fibo_no_cache(35)=}')

# Because of RecursionError maximum recursion depth exceeded
setrecursionlimit(20000)

print(f'{fact_no_cache(500)=}')
print(f'{fact_cache(500)=}')

# As it is obvious, when we use cache decorator.
# computer doesn't recalculate repetitive values.
# Once the calculation is done for a part of a program,
# In the next calculations, program just uses what has calculated before
# => Using cache makes calculations and process really fast.
