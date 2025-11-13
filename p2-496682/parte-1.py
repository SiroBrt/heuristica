import sys
import constraint

empty = -1
cross = 0
circle = 1


def read_board(infile):
    file = open(infile, 'r')
    temp = file.read()
    n = temp.find(temp[-1])
    tablero = []
    for i in range(len(temp)):
        if temp[i] == ".":
            tablero.append(empty)
        elif temp[i] == "x":
            tablero.append(cross)
        elif temp[i] == "o":
            tablero.append(circle)
    return tablero, n


def print_board(tablero, n, outfile):
    with open(outfile, 'a') as f_dat:
        f_dat.write("+" + "---+" * n + "\n")
        for i in range(n * n):
            if (i % n == 0) and (i != 0):
                f_dat.write("|\n")
            f_dat.write("| " + ("  " if tablero[i] == empty else ("x " if tablero[i] == cross else "o ")))
        f_dat.write("|\n+" + "---+" * n + "\n")


def variable_sum(*arg):
    result = 0
    for i in arg:
        print(i)
        result += i
    return result


def solve_board(tablero, n):  # creates the problem for the given  board
    prob = constraint.Problem()
    for i in range(n * n):
        prob.addVariable(i, ([0, 1] if tablero[i] == empty else [tablero[i]]))
    for j in range(n):
        # arreglar
        prob.addConstraint((lambda *arg: sum([i for i in arg]) == n / 2), [(i * n + j) for i in range(n)])  # sum of rows
        prob.addConstraint((lambda *arg: sum([i for i in arg]) == n / 2), [(i + n * j) for i in range(n)])  # sum of columns

        for i in range(n - 2):
            prob.addConstraint((lambda a, b, c: (b != a) or (b != c)), (i * n + j, (i + 1) * n + j, (i + 2) * n + j))  # no three equal vertically
            prob.addConstraint((lambda a, b, c: (b != a) or (b != c)), (i + n * j, (i + 1) + n * j, (i + 2) + n * j))  # no three equal horizontally
    solutions = prob.getSolutions()
    # print(prob._constraints)
    if (len(solutions) > 0):
        final = solutions[0]
    else:
        final = None
    return final, len(solutions)


def transform_solution(solution):
    new_board = [0] * n * n
    for i in solution:
        new_board[i] = solution[i]
    return new_board


if len(sys.argv) < 3:
    print("not enough arguments\n")
    exit(-1)
infile = sys.argv[1]
outfile = sys.argv[2]
tablero, n = read_board(infile)

with open(outfile, 'w') as f_dat:  # clean output file
    f_dat.write("")
print_board(tablero, n, outfile)
solution, num = solve_board(tablero, n)

with open(outfile, 'a') as f_dat:  # clean output file
    f_dat.write(str(num) + " solution" + ("" if num == 1 else "s") + " found\n")
tablero_resuelto = transform_solution(solution)
print_board(tablero_resuelto, n, outfile)

# print(variable_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))


