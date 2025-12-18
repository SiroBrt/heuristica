import sys
import time
import constraint
from problem_generator import random_populate

empty = -1
cross = 0
circle = 1

punto = 0
cruz = 1
circulo = 2


def show_tablero(tablero, n):
    print("+" + "---+" * n)
    for i in range(n * n):
        if (i % n == 0) and (i != 0):
            print("|")
        print("| " + ("  " if tablero[i] == empty else ("x " if tablero[i] == cross else "o ")), end='')
    print("|\n+" + "---+" * n)


def show_constraint_solution(solution, n):
    new_board = [0] * n * n
    for i in solution:
        new_board[i] = solution[i]
    show_tablero(new_board, n)


def de_una(tablero, n):
    anterior = [tablero[i] for i in range(len(tablero))]
    two_in_a_row(tablero, n)
    same_number(tablero, n)
    while anterior != tablero:
        anterior = [tablero[i] for i in range(len(tablero))]
        two_in_a_row(tablero, n)
        same_number(tablero, n)
    # show_tablero(tablero, n)


def two_in_a_row(tablero, n):
    for i in range(len(tablero) - 1):
        if tablero[i] != punto:
            # check horizontal
            if tablero[i] == tablero[i + 1]:
                if i % n < n - 2:
                    if tablero[i + 2] == punto:
                        tablero[i + 2] = (tablero[i] * 2) % 3
                if i % n > 0:
                    if tablero[i - 1] == punto:
                        tablero[i - 1] = (tablero[i] * 2) % 3
            if i % n < n - 2:
                if (tablero[i] == tablero[i + 2]) and (tablero[i + 1] == 0):
                    tablero[i + 1] = (tablero[i] * 2) % 3
            # check vertical
            if i < n * (n - 1):
                if tablero[i] == tablero[i + n]:
                    if i > n - 1:
                        if tablero[i - n] == punto:
                            tablero[i - n] = (tablero[i] * 2) % 3
                    if i < n * (n - 2):
                        if tablero[i + 2 * n] == punto:
                            tablero[i + 2 * n] = (tablero[i] * 2) % 3
                if i < n * (n - 2):
                    if (tablero[i] == tablero[i + 2 * n]) and (tablero[i + n] == punto):
                        tablero[i + n] = (tablero[i] * 2) % 3


def contar(tablero, n):
    row_cross = [0] * n
    row_circle = [0] * n
    column_cross = [0] * n
    column_circle = [0] * n
    for i in range(len(tablero)):
        if tablero[i] == cruz:
            row_cross[i // n] += 1
            column_cross[i % n] += 1
        if tablero[i] == circulo:
            row_circle[i // n] += 1
            column_circle[i % n] += 1
    return row_cross, row_circle, column_cross, column_circle


def same_number(tablero, n):
    row_cross, row_circle, column_cross, column_circle = contar(tablero, n)
    # rellenamos filas
    for i in range(n):
        if row_cross[i] == n / 2:
            for j in range(n):
                if tablero[j + i * n] == 0:
                    tablero[j + i * n] = 2
                    column_circle[j] += 1
        if row_circle[i] == n / 2:
            for j in range(n):
                if tablero[j + i * n] == 0:
                    tablero[j + i * n] = 1
                    column_cross[j] += 1

    for i in range(n):
        if column_cross[i] == n / 2:
            for j in range(n):
                if tablero[j * n + i] == 0:
                    tablero[j * n + i] = 2
        if column_circle[i] == n / 2:
            for j in range(n):
                if tablero[j * n + i] == 0:
                    tablero[j * n + i] = 1


def check(tablero, n):
    row_cross, row_circle, column_cross, column_circle = contar(tablero, n)
    for i in range(n):
        if row_cross[i] > n / 2:
            return 0
        if row_circle[i] > n / 2:
            return 0
        if column_cross[i] > n / 2:
            return 0
        if column_circle[i] > n / 2:
            return 0
    for i in range(len(tablero) - 2):
        if tablero[i] != 0:
            # check horizontal
            if i % n < n - 2:
                if tablero[i] == tablero[i + 1] and tablero[i] == tablero[i + 2]:
                    return 0
            # check vertical
            if i < n * (n - 2):
                if tablero[i] == tablero[i + n] and tablero[i] == tablero[i + 2 * n]:
                    return 0
    return 1


def dale(tablero, n):
    posibilidad = [tablero[i] for i in range(len(tablero))]
    de_una(posibilidad, n)
    if check(posibilidad, n) == 0:
        return 0
    if punto in posibilidad:
        pos = posibilidad.index(punto)
        posibilidad[pos] = cruz

        if dale(posibilidad, n):
            return 1
        else:
            posibilidad[pos] = circulo
            return dale(posibilidad, n)
    else:
        # show_tablero(untransform_board(posibilidad), board_size)
        return 1


def solve_board(tablero, n):  # new solver
    prob = constraint.Problem()
    for i in range(n * n):
        prob.addVariable(i, ([0, 1] if tablero[i] == empty else [tablero[i]]))
    for j in range(n):
        prob.addConstraint((lambda *arg: sum([i for i in arg]) == n / 2), [(i * n + j) for i in range(n)])  # sum of rows
        prob.addConstraint((lambda *arg: sum([i for i in arg]) == n / 2), [(i + n * j) for i in range(n)])  # sum of columns

        for i in range(n - 2):
            prob.addConstraint((lambda a, b, c: (b != a) or (b != c)), (i * n + j, (i + 1) * n + j, (i + 2) * n + j))  # no three equal vertically
            prob.addConstraint((lambda a, b, c: (b != a) or (b != c)), (i + n * j, (i + 1) + n * j, (i + 2) + n * j))  # no three equal horizontally
    solution = prob.getSolution()
    # print(prob._constraints)

    return solution


def transform_board(board):
    return [board[i] + 1 for i in range(len(board))]


def untransform_board(board):
    return [board[i] - 1 for i in range(len(board))]


if len(sys.argv) < 4:
    print("not enough arguments\n")
    exit(-1)
min_board_size = int(sys.argv[1])
max_board_size = int(sys.argv[2])
tests = sys.argv[3]


for board_size in range(min_board_size, max_board_size + 1):
    if board_size % 2 != 0:
        continue
    print(f"size {board_size}")
    for i in range(int(tests)):
        print(i + 1, end='', flush=True)
        board = [-1] * board_size * board_size
        board = random_populate(board, board_size)
        # print(i + 1)
        # show_tablero(board, board_size)

        other_board = transform_board(board)
        out_old = 0
        t1 = time.time()
        if check(other_board, board_size):
            out_old = dale(other_board, board_size)
        t2 = time.time()
        with open("old1.csv", 'a') as f_out:
            f_out.write(f"{board_size},{out_old},{t2-t1}\n")
        print(".", end='', flush=True)
        # if out_old == 1:
        #     show_tablero(board, board_size)

        # t1 = time.time()
        # out_new = solve_board(board, board_size)
        # t2 = time.time()
        # # print(f"solution: {out_new}")
        # with open("new.csv", 'a') as f_out:
        #     if out_new is None:
        #         f_out.write(f"{board_size},0,{t2-t1}\n")
        #     else:
        #         # show_constraint_solution(out_new, board_size)
        #         f_out.write(f"{board_size},1,{t2-t1}\n")
        # print(".", end=', ', flush=True)
        #
    print()
