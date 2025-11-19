import sys


punto = 0
cruz = 1
cir_culo = 2


def leer_tablero(infile):
    file = open(infile, 'r')
    temp = file.read()
    n = temp.find(temp[-1])
    tablero = []
    for i in range(len(temp)):
        if temp[i] == ".":
            tablero.append(punto)
        elif temp[i] == "x":
            tablero.append(cruz)
        elif temp[i] == "o":
            tablero.append(cir_culo)

    return tablero, n


def print_tablero(tablero, n, outfile):
    with open(outfile, 'a') as f_out:
        f_out.write("+" + "---+" * n + "\n")
        for i in range(n * n):
            if (i % n == 0) and (i != 0):
                f_out.write("|\n")
            f_out.write("| " + ("  " if tablero[i] == punto else ("x " if tablero[i] == cruz else "o ")))
        f_out.write("|\n+" + "---+" * n + "\n")


def de_una(tablero, n):
    anterior = [tablero[i] for i in range(len(tablero))]
    two_in_a_row(tablero, n)
    same_number(tablero, n)
    while anterior != tablero:
        anterior = [tablero[i] for i in range(len(tablero))]
        two_in_a_row(tablero, n)
        same_number(tablero, n)


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
        if tablero[i] == cir_culo:
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


def dale(tablero, n, outfile):
    posibilidad = [tablero[i] for i in range(len(tablero))]
    de_una(posibilidad, n)
    if check(posibilidad, n) == 0:
        return 0
    if punto in posibilidad:
        pos = posibilidad.index(punto)
        posibilidad[pos] = cruz

        if dale(posibilidad, n, outfile):
            return 1
        else:
            posibilidad[pos] = cir_culo
            return dale(posibilidad, n, outfile)
    else:
        print_tablero(posibilidad, n, outfile)
        return 1


if len(sys.argv) < 3:
    print("not enough arguments\n")
    exit(-1)
infile = sys.argv[1]
outfile = sys.argv[2]
with open(outfile, 'w') as f_out:
    f_out.write("")
tablero, n = leer_tablero(infile)

print_tablero(tablero, n, outfile)
print("done")
dale(tablero, n, outfile)
