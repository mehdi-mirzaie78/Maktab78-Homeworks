import datetime


def modify(date: str) -> tuple:
    temp = date.split('-')
    result = tuple(map(int, temp))
    return result


def diff(dt1: str, dt2: str) -> str:
    date1 = datetime.datetime(*modify(dt1))
    date2 = datetime.datetime(*modify(dt2))
    difference = date2 - date1 if date2 > date1 else date1 - date2
    print(difference)
    return f"Difference: {difference.seconds + difference.days * 24 * 3600} seconds"


# dat1 = input('Enter the first date-time with this format YYYY-MM-dd-hh-mm-ss: ')
# dat2 = input('Enter the second date-time with this format YYYY-MM-dd-hh-mm-ss: ')

dat1 = '2022-8-17-10-30-20'
dat2 = '1999-7-21-22-30-53'

print(diff(dat1, dat2))
# print(diff(dat2, dat1))
