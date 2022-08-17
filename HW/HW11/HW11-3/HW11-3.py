import datetime
from functions import modify, count_leap, date_convert


# Shows difference of two datetime in seconds and years
# Plus shows the number of changing clock time
# And show number of leap years with the leap years
# At last converts the given dates to jalali dates

def diff(dt1: str, dt2: str) -> None:
    # ############################ Modifying Dates #################################
    date1 = datetime.datetime(*modify(dt1))
    date2 = datetime.datetime(*modify(dt2))
    # ############################### Difference ###################################
    difference = date2 - date1 if date2 > date1 else date1 - date2
    years = difference.days // 365
    print(' Time Difference In Seconds '.center(70, '-'))
    print(f"Difference(second): {difference.seconds + difference.days * 24 * 3600}"
          f" - Difference(year): {years}")
    # ############################### Leap Years ###################################
    print(' Leap Years '.center(70, '-'))
    count_leap(dt1, dt2)
    print(f"Number Of Changing Clock Time: {years * 2} times")
    # ############################### Convert Date #################################
    print(' Convert Date '.center(70, '-'))
    print(f"{date1.date()} =>", date_convert(date1))
    print(f"{date2.date()} =>", date_convert(date2))


dat1 = input('Enter the first date-time with this format YYYY-MM-dd-hh-mm-ss: ')
dat2 = input('Enter the second date-time with this format YYYY-MM-dd-hh-mm-ss: ')

# dat1 = '2022-8-17-10-30-20'
# dat2 = '1999-7-21-22-30-53'

diff(dat1, dat2)
