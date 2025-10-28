import sys
infile = sys.argv[1]
datfile = sys.argv[2]

with open(infile, 'r') as f_in:
    content = f_in.read()

lines = content.split("\n")
# print(lines)

[sn, sm, su] = lines[0].split()

n = int(sn)
m = int(sm)
u = int(su)

sc = lines[1:m + 1]
c = []
for i in sc:
    c.append(i.split(","))
so = lines[m + 1:-1]
o = []
for i in so:
    o.append(i.split(","))

# possible checks here


with open(datfile, 'w') as f_dat:
    f_dat.write("data;\n\n")
    f_dat.write(f"param n := {n};\n")
    f_dat.write(f"param m := {m};\n")
    f_dat.write(f"param u := {u};\n")

    f_dat.write("\nparam\tc:")
    for i in range(0, m):
        f_dat.write(f"\t{i+1}\t")
    f_dat.write(":=")
    for i in range(0, m):
        f_dat.write(f"\n\t{i+1}\t\t")
        for j in range(0, m):
            f_dat.write(f"\t\t{c[i][j]}")
    f_dat.write(";\n")

    f_dat.write("\nparam\to:")
    for i in range(0, u):
        f_dat.write(f"\t{i+1}\t")
    f_dat.write(":=")
    for i in range(0, n):
        f_dat.write(f"\n\t{i+1}\t\t")
        for j in range(0, u):
            f_dat.write(f"\t\t{o[i][j]}")
    f_dat.write(";\n\nend;")
