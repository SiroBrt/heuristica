import sys
import constraint

empty = -1
cross = 0
circle = 1
debug = 0


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
    with open(outfile, 'a') as f_out:
        f_out.write("+" + "---+" * n + "\n")
        for i in range(n * n):
            if (i % n == 0) and (i != 0):
                f_out.write("|\n")
            f_out.write("| " + ("  " if tablero[i] == empty else ("x " if tablero[i] == cross else "o ")))
        f_out.write("|\n+" + "---+" * n + "\n")


def solve_board(tablero, n):  # creates the problem for the given  board
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

    if debug == 1:
        num = len(prob.getSolutions())
        print(str(num) + " solution" + ("" if num == 1 else "s") + " found")

    return solution


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
if len(sys.argv) > 3:
    if sys.argv[3] == "-debug":
        debug = 1
tablero, n = read_board(infile)

if n % 2 != 0:
    exit(-1)

with open(outfile, 'w') as f_out:  # clean output file
    f_out.write("")
print_board(tablero, n, outfile)
solution = solve_board(tablero, n)

with open(outfile, 'a') as f_out:  # clean output file
    if solution is None:
        f_out.write("no solution found\n")
    else:
        tablero_resuelto = transform_solution(solution)
        print_board(tablero_resuelto, n, outfile)



