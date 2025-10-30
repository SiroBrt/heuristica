import sys
import random
import math

infile = sys.argv[1]
limit = 100

try:
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    if (sys.argv[4] == "random-cost"):
        creation = 1
    else:
        creation = 0
except:
    m = int(input("numero de buses: "))
    n = int(input("numero de slots: "))
    creation = 0


if creation:
    kd = math.floor(random.random() * limit)
    kp = math.floor(random.random() * limit)
else:
    kd = int(input("coste por km: "))
    kp = int(input("coste por persona: "))

d = []  # distancias por bus
p = []  # personas en cada bus

math.floor(random.random() * limit)


with open(infile, 'w') as f_dat:
    f_dat.write(f"{n} {m}\n")
    f_dat.write(f"{kd} {kp}\n")
    for i in range(m - 1):
        f_dat.write(f"{math.floor(random.random() * limit)},")
    f_dat.write(f"{math.floor(random.random() * limit)}\n")
    for i in range(m - 1):
        f_dat.write(f"{math.floor(random.random() * limit)},")
    f_dat.write(f"{math.floor(random.random() * limit)}\n")
