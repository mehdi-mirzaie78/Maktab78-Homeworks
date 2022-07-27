import pickle
with open("numbers.pickle", 'rb') as f:
    unpickled = pickle.load(f)

print(unpickled)


# def calculate_divides(file_path: str) -> list[float | None]:
#     """Unpickled File & Returned Result Divide Numbers"""
#     file = open(file_path, 'rb')
#     numbers = pickle.load(file)
#     try:
#         result = list(map(lambda t: t[0] / t[1], numbers))
#     except TypeError:
#         result = [None for _ in numbers]
#     file.close()
#     return result


# print(calculate_divides("numbers.pickle"))


def calculate_divides(file_path: str) -> list[float | None]:
    """Unpickled File & Returned Result Divide Numbers"""
    file = open(file_path, 'rb')
    numbers = pickle.load(file)
    file.close()
    result = []
    for t in numbers:
        try:
            result.append(t[0] / t[1])
        except TypeError:
            # result.append('TypeError')
            result.append(None)
        except ZeroDivisionError:
            # result.append('ZeroDivisionError')
            result.append(None)
    return result


print(calculate_divides("numbers.pickle"))

"""
1. We don't need the file to be opened in entire process.
   so I closed it right after that I read the numbers.

2. We want to have the None for each exceptions in the list
   not that we assign all the members of the list None.
   so I add a for above the try & except block.
   and for each member of numbers that has an error I assign
   None for that member in result
"""