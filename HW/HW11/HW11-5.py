import datetime
import jdatetime


def modify(date: str) -> datetime.date:
    temp = date.split('-')
    result = tuple(map(int, temp))
    return datetime.date(*result)


def date_convert(date: datetime.date):
    return jdatetime.date.fromgregorian(day=date.day, month=date.month, year=date.year)


def gen(dt1: datetime.date, dt2: datetime.date, num: int):
    date1 = date_convert(dt1)
    date2 = date_convert(dt2)
    start_date = date1 if date1 < date2 else date2
    end_date = date1 if date1 > date2 else date2
    weekday = start_date.isoweekday() - 1
    num_days = abs(weekday - num)

    if weekday < num:
        start_date += datetime.timedelta(days=num_days)

    elif weekday > num:
        start_date += jdatetime.timedelta(days=7 - num_days)

    diff = end_date - start_date
    print(diff)
    for i in range(0, diff.days, 7):
        yield start_date.strftime('%Y / %m / %d - %A ')
        start_date += datetime.timedelta(days=7)


# Date1 = datetime.date(2022, 8, 16)
# Date2 = Date1 + datetime.timedelta(days=31)
# number = 6

Date1 = modify(input('Enter the first date: '))
Date2 = modify(input('Enter the second date: '))
number = int(input('Enter a number in between 0 (saturday) and 6 (friday): '))

for j in gen(Date1, Date2, number):
    print(j)

# 2022-8-17
# 2022-9-17
# print(jal.isoweekday() - 1)
# print(jal.jweekday())
# print(jal.strftime('%Y / %m / %d'))

# datetime.date.strftime()
