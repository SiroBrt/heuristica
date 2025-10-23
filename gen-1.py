import sys
infile = sys.argv[1]
datfile = sys.argv[2]

with open(infile, 'r') as f_in:
    content = f_in.read()

[sn, sm, skd, skp, sd, sp] = content.split()

n = int(sn)
m = int(sm)
kd = int(skd)
kp = int(skp)
d = sd.split(",")
p = sp.split(",")

# possible checks here

with open(datfile, 'w') as f_dat:
    f_dat.write("data;\n\n")
    f_dat.write(f"param n := {n};\n")
    f_dat.write(f"param m := {m};\n")
    f_dat.write(f"param kd := {kd};\n")
    f_dat.write(f"param kp := {kp};\n")
    f_dat.write("\nparam: \td\t\t\tp :=")
    for i in range(0, m):
        f_dat.write(f"\n  {i+1}\t\t\t{d[i]}\t\t\t{p[i]}")
    f_dat.write(";\n\nend;")
