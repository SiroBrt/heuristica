import sys
import random
# import math

# IMPORTANT: cross+circle = 1
empty = -2
cross = 0
circle = 1

infile = sys.argv[1]
try:
    n = int(sys.argv[2])
    if n % 2 == 1:
        raise ValueError("not even")
except:
    while (n % 2 == 1) | (n < 3):
        print("Choose an even size")
        n = int(input("size: "))

board = [empty] * n * n


def print_board(board, n):
    print("+" + "---+" * n)
    for i in range(n * n):
        if (i % n == 0) and (i != 0):
            print("|")
        print("| " + ("  " if board[i] == empty else ("x " if board[i] == cross else "o ")), end='')
    print("|\n+" + "---+" * n)


def random_populate(board, n):
    chosen_ones = random.sample(range(0, n * n), random.randint(n, (n * n) / 2))
    # print(chosen_ones)
    for i in chosen_ones:
        board[i] = round(random.random())
    return board


board = random_populate(board, n)
# print_board(board, n)
with open(infile, 'w') as f_out:
    for i in range(1, n * n + 1):
        f_out.write("." if board[i - 1] == empty else ("x" if board[i - 1] == cross else "o"))
        if (i % n == 0):
            f_out.write("\n")

