from Decorator import process_timer


@process_timer
def function(num: int):
    def fibonacci(n=num):
        if n in (0, 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci()


def fact(number: int):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)


print(fact(3))

# for i in range(30):
#     print(fibonacci(i), end=' ')

print(function(30))
