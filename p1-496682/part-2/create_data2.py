import os
# import math

bus = [i + 1 for i in range(9)]
slots = [i + 1 for i in range(9)]
# workshops is automatically computed in problem_generator2.py
print("buses: ", end=' ')
print(bus)
print("slots: ", end=' ')
print(slots)
tries = 1
times = []
for i in bus:
    aux = []
    for j in slots:
        t = 0
        for k in range(tries):
            os.system(f"python problem_generator2.py aa.in {i+1} {j+1} && python gen-2.py aa.in aa.dat && glpsol -m parte-2-2.mod -d aa.dat > out.txt && rm aa.in && rm aa.dat")
            with open("out.txt", 'r') as f:
                content = f.read()
            y = 0
            while y != -1:
                y = content.find("Time")
                if y != -1:
                    x = y
                    content = content[x + 10:]

            content = content[:content.find("secs")]
            t += float(content)
        aux.append(round(t / tries, 2))
    print(aux)
    times.append(aux)


with open("data2.csv", 'w') as f_d:
    f_d.write("bus slots time\n")
    for i in range(len(bus)):
        for j in range(len(slots)):
            f_d.write(f"{bus[i]} {slots[j]} {times[i][j]}\n")

