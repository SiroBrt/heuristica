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
    print(chosen_ones)
    for i in chosen_ones:
        board[i] = round(random.random())


# rotates a 2x2 matrix clockwise
def rotate(board):
    return [board[2], board[0], board[3], board[1]]


def start_populate():
    match random.randint(0, 2):
        case 0:
            board = [circle, cross, cross, cross]
            for i in range(random.randint(0, 3)):
                board = rotate(board)
        case 1:
            board = [circle, cross, circle, cross]
            for i in range(random.randint(0, 1)):
                board = rotate(board)
        case 2:
            board = [circle, circle, cross, cross]
            for i in range(random.randint(0, 3)):
                board = rotate(board)

    if random.randint(0, 1):  # flip colors
        for i in range(4):
            board[i] = 1 - board[i]
    return board


def expand(board, n):
    new_board = [empty] * (n + 2) * (n + 2)
    for i in range(n):
        for j in range(n):
            new_board[i * (n + 2) + j] = board[i * n + j]
    return new_board


# since we expand always from up-left corner we don't check anything to the right or down
def two_in_a_row(board, n, pos):
    opinions = []
    # check horizontal
    if pos % n >= 2:  # not on first columns
        if (board[pos - 1] == board[pos - 2]) and (board[pos - 1] != empty):
            opinions.append(1 - board[pos - 1])

    # check vertical
    if pos >= n * 2:  # not on first rows
        if (board[pos - n] == board[pos - 2 * n]) and (board[pos - n] != empty):
            opinions.append(1 - board[pos - n])
    if opinions == []:
        return empty
    for i in opinions:
        if i != opinions[0]:
            return empty
    return opinions[0]


def contar(board, n):
    row_cross = [0] * n
    row_circle = [0] * n
    column_cross = [0] * n
    column_circle = [0] * n
    for i in range(len(board)):
        if board[i] == cross:
            row_cross[i // n] = row_cross[i // n] + 1
            column_cross[i % n] = column_cross[i % n] + 1
        if board[i] == circle:
            row_circle[i // n] = row_circle[i // n] + 1
            column_circle[i % n] = column_circle[i % n] + 1
    return row_cross, row_circle, column_cross, column_circle


def same_number(board, n):
    change = 0
    row_cross, row_circle, column_cross, column_circle = contar(board, n)
    # fill sets with enough of one type with the other
    for i in range(n):
        if row_cross[i] == n / 2:
            for j in range(n):
                if board[j + i * n] == empty:
                    board[j + i * n] = circle
                    column_circle[j] = column_circle[j] + 1
                    change = 1
        elif row_circle[i] == n / 2:
            for j in range(n):
                if board[j + i * n] == empty:
                    board[j + i * n] = cross
                    column_cross[j] = column_cross[j] + 1
                    change = 1
    for i in range(n):
        if column_cross[i] == n / 2:
            for j in range(n):
                if board[j * n + i] == empty:
                    board[j * n + i] = circle
                    change = 1
        if column_circle[i] == n / 2:
            for j in range(n):
                if board[j * n + i] == empty:
                    board[j * n + i] = cross
                    change = 1
    return change


def correct(board, n):
    for i in range(n * n):
        if (two_in_a_row(board, i) == empty) and (board[i] != empty):
            return 0


def aux_fill(old_board, n, old_decisions):
    board = old_board
    decisions = old_decisions
    change = 1
    while change:
        change = 0
        for i in range(len(board)):
            if board[i] != empty:
                continue
            value = two_in_a_row(board, n, i)
            if value != empty:
                board[i] == value
                change = 1

        if same_number(board, n):
            change = 1
    # if -1 not in board:

    return board, decisions


def fill(board, n, decisions):
    # sides
    for i in range(n - 2):
        value = two_in_a_row(board, n, i + n * (n - 2))
        if value != empty:
            board[i + n * (n - 2)] = value
            board[i + n * (n - 1)] = 1 - value
        value = two_in_a_row(board, n, i * n + (n - 2))
        if value != empty:
            board[i * n + (n - 2)] = value
            board[i * n + (n - 1)] = 1 - value
    return aux_fill(board, n, decisions)
    # return board, decisions


def expanding_populate(board, n):
    kernel = start_populate()
    decisions = [(0, kernel[0]), (1, kernel[1]), (2, kernel[2]), (3, kernel[3])]
    print_board(kernel, 2)
    for i in range(1, int(n / 2)):
        kernel = expand(kernel, i * 2)
        kernel, decisions = fill(kernel, (i + 1) * 2, decisions)
        # DEBUG
        # print_board(kernel, (i + 1) * 2)
        #
    return kernel, decisions


board, decisions = expanding_populate(board, n)
with open(infile, 'w') as f_out:
    print("expected solution:")
    print_board(board, n)
    for i in range(1, n * n + 1):
        f_out.write("." if board[i - 1] == empty else ("x" if board[i - 1] == cross else "o"))
        if (i % n == 0):
            f_out.write("\n")

