import os

bus = [10, 100, 200, 500, 1000, 2000]
slots = [10, 20, 50, 100, 200, 500]
tries = 1
times = []
for i in bus:
    aux = []
    for j in slots:
        t = 0
        for k in range(tries):
            os.system(f"python problem_generator1.py aa.in {i+1} {j+1} random-cost && python gen-1.py aa.in aa.dat && glpsol -m parte-2-1.mod -d aa.dat > out.txt && rm aa.in && rm aa.dat")
            with open("out.txt", 'r') as f:
                content = f.read()
            x = content.find("Time")
            important = content[x + 11:]
            important = important[:important.find("secs")]
            t += float(important)
        aux.append(round(t / tries, 2))
    print(aux)
    times.append(aux)


with open("data.csv", 'w') as f_d:
    f_d.write("bus slots time\n")
    for i in range(len(bus)):
        for j in range(len(slots)):
            f_d.write(f"{bus[i]} {slots[j]} {times[i][j]}\n")



