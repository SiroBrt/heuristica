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
        os.system(f"python problem_generator.py test.in {i}")

        initial = time.time()
        os.system("python parte-1.py test.in test.out")
        final = time.time()
        t += final - initial
    times.append(round(t / tries, 2))
    print(f"size: {i}, time: {times[-1]}")
print(times)
