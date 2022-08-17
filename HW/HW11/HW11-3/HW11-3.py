import datetime
from leap_year import modify, count_leap


# Shows difference of two datetime in seconds and years
# Plus shows the number of changing clock time
# And show number of leap years with the leap years
def diff(dt1: str, dt2: str) -> None:
    date1 = datetime.datetime(*modify(dt1))
    date2 = datetime.datetime(*modify(dt2))
    difference = date2 - date1 if date2 > date1 else date1 - date2
    years = difference.days // 365
    print(' Time Difference In Seconds '.center(70, '-'))
    print(f"Difference(second): {difference.seconds + difference.days * 24 * 3600}"
          f" - Difference(year): {years}")
    print(' leap years '.center(70, '-'))
    count_leap(dt1, dt2)
    print(f"Number Of Changing Clock Time: {years * 2} times")


# dat1 = input('Enter the first date-time with this format YYYY-MM-dd-hh-mm-ss: ')
# dat2 = input('Enter the second date-time with this format YYYY-MM-dd-hh-mm-ss: ')

dat1 = '2022-8-17-10-30-20'
dat2 = '1999-7-21-22-30-53'

diff(dat1, dat2)
