import sys

scores = sys.argv
scores = scores[1:]


def avg(args: list | tuple) -> int:
    nums = map(float, args)
    return int(sum(nums) / len(args))


print(f"Average= {avg(scores)}")
