import datetime


# Modifies str format of datetime to convert to datetime object
def modify(date: str) -> tuple:
    temp = date.split('-')
    result = tuple(map(int, temp))
    return result


# Determines a year is a leap year or not
def leap(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 100 != 0:
        return True


# Counts the leap years and shows which years were leap years
def count_leap(dt1: str, dt2: str) -> None:
    date1 = datetime.datetime(*modify(dt1))
    date2 = datetime.datetime(*modify(dt2))
    if date1 < date2:
        start, end = date1.year, date2.year
    else:
        start, end = date2.year, date1.year

    result = list(filter(leap, list(range(start, end))))
    print(f"We have {len(result)} leap years:", *result)

# leap year: 1992 & 2000
# print(leap(1900))
