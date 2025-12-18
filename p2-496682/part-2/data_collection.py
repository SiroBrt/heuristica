import sys
import random
import time
from grafo import read_graph_from
from grafo import graph
from algoritmo import brute_force_heuristic
from algoritmo import curved_distance
from algoritmo import solve


repetitions = 1  # to even out random noise

if len(sys.argv) < 4:
    print("not enough arguments\n")
    exit(-1)
tests = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]
heuristic = curved_distance
if len(sys.argv) > 4:
    if sys.argv[4] == "brute":
        heuristic = brute_force_heuristic

# get data
g = graph()
g, vertex_processed, edges_processed = read_graph_from(infile)


def run(start, end, heuristic):
    t1 = time.time()
    chain, n_expanded = solve(start, end, g, heuristic, outfile)
    t2 = time.time()
    t = t2 - t1
    return t, n_expanded, len(chain)


class test:
    def __init__(self, c, t, n):
        self.chain_length = c
        self.time = t
        self.nodes = n

    def __str__(self):
        return f"{self.chain_length},{self.nodes},{self.time}"


with open(outfile, 'a') as f_out:
    # f_out.write("stepsToSolution,nodesExpanded,time\n")
    for i in range(int(tests)):
        print(i + 1, end=', ', flush=True)
        start = g.nodes[str(random.randint(1, vertex_processed))]
        end = g.nodes[str(random.randint(1, vertex_processed))]
        t_avg = 0
        for i in range(repetitions):
            # c should always be the same, n only changes only with inbetween tests and t changes every iteration
            t, n, c = run(start, end, heuristic)
            t_avg += t / repetitions
        f_out.write(f"{test(c, t_avg, n)}\n")
print()
