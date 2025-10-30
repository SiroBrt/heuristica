import sys
import random
import math

infile = sys.argv[1]

n = 1
m = 5
u = 1
while (n * u < m):
    m = int(input("numero de buses: "))
    n = int(input("numero de slots: "))
    u = int(input("numero de workshops: "))
    if n * u < m:
        print("nope\n")

c = []  # collisions
o = []  # unavailable slots

limit = 100

for i in range(m):
    aux = []
    for j in range(m - i - 1):
        aux.append(math.floor(random.random() * limit))
    aux.append(0)
    c.append(aux)
c.reverse()

for i in range(m):
    for j in range(m - 1 - i):
        c[i].append(c[j + 1 + i][i])

for i in range(n):
    aux = []
    for j in range(u):
        aux.append(1)
    o.append(aux)

espacios_libres = n * u - m
para_bloquear = round(random.random() * espacios_libres)

for b in range(para_bloquear):
    i = 0
    j = 0
    while (o[i][j] == 0):
        i = math.floor(random.random() * n)
        j = math.floor(random.random() * u)
    o[i][j] = 0


with open(infile, 'w') as f_dat:
    f_dat.write(f"{n} {m} {u}\n")
    for i in range(m):
        for j in range(m - 1):
            f_dat.write(f"{c[i][j]},")
        f_dat.write(f"{c[i][m-1]}\n")
    for i in range(n):
        for j in range(u - 1):
            f_dat.write(f"{o[i][j]},")
        f_dat.write(f"{o[i][u-1]}\n")
