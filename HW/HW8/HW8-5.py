import pickle
with open("numbers.pickle", 'rb') as f:
    unpickled = pickle.load(f)

print(unpickled)


# 1st solution
def calculate_divides1(file_path: str) -> list[float | None]:
    """Unpickled File & Returned Result Divide Numbers"""
    file = open(file_path, 'rb')
    numbers = pickle.load(file)
    result = numbers
    try:
        result = list(map(lambda t: t[0] / t[1], numbers))
    except (TypeError, ZeroDivisionError):
        result = [None for _ in numbers]
    finally:
        file.close()
        return result


print(calculate_divides1("numbers.pickle"))


# 2nd solution
def calculate_divides2(file_path: str) -> list[float | None]:
    """Unpickled File & Returned Result Divide Numbers"""
    file = open(file_path, 'rb')
    numbers = pickle.load(file)
    file.close()
    result = []
    for t in numbers:
        try:
            result.append(t[0] / t[1])
        except (TypeError, ZeroDivisionError):
            result.append(None)
    return result


print(calculate_divides2("numbers.pickle"))

"""
# 2nd solution
1. We don't need the file to be opened in the entire process.
   so I closed it right after that I read the numbers.

2. We want to have the None for each exceptions in the list
   not that we assign all the members of the list None.
   so I add a for above the try & except block.
   and for each member of numbers that has an error I assign
   None for that member in result
   if I found that right ☺ I don't know
"""
