# Guess Game
import argparse
import random

parser = argparse.ArgumentParser(description='This is a guessing game', epilog='Created By Mark')

parser.add_argument('-s', '--start', action='store', type=int, required=True, help='Start Number')
parser.add_argument('-e', '--end', action='store', type=int, required=True, help='End Number')
parser.add_argument('-g', '--guess', action='store', type=int, default=False, help='Number of Guesses')
parser.add_argument('-cheat', action='store_true', default=False, help='Cheat you will get the answer')
args = parser.parse_args()

answer = random.randint(args.start, args.end)

if args.cheat:
    print(answer)


def game(num: int, ans=answer) -> bool:
    if num < ans:
        print('Enter Higher Number: ')
        return False
    elif num > ans:
        print('Enter Lower Number: ')
        return False
    print('Congratulations. You Won!! :)')
    return True


for i in range(1, args.guess + 1):
    n = int(input(f'Guess number {i}: '))
    if game(n):
        print('Comeback soon!')
        break
else:
    print('Sorry you lost :(')
