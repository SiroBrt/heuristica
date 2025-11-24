import os
import time
# import math

sizes = [2 * i for i in range(2, 10)]
# sizes = [6, 8]
# workshops is automatically computed in problem_generator2.py
print("sizes: ", end=' ')
print(sizes)
tries = 5
times = []
for i in sizes:
    # print(f"#buses = {i}")
    aux = []
    t = 0
    for k in range(tries):
        os.system(f"python problem-generator.py test.in {i}")

        initial = time.time()
        os.system("python parte-1.py test.in test.out")
        final = time.time()
        t += final - initial
    times.append(round(t / tries, 2))
    print(f"size: {i}, time: {times[-1]}")
os.system("rm test.in test.out")


with open("time.out", 'w') as f_out:
    f_out.write("size\t time\n")
    for i in range(len(sizes)):
        f_out.write(f"{sizes[i]}\t {times[i]}s\n")

print(times)
