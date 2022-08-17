import argparse

parser = argparse.ArgumentParser(description='This is a script to calculate average of entered grades',
                                 epilog='Created By Mark')

parser.add_argument('-g', '--grades', action='store', nargs='*', help='Your grades with space between')
parser.add_argument('-f', '--float', action='store', type=int, default=2, help='Number of digits after floating point')
res = parser.parse_args()


def avg(args: tuple, fl: int) -> str:
    nums = map(float, args)
    return f"Average= {sum(nums) / len(args):.{fl}f}"


print(avg(res.grades, res.float))
