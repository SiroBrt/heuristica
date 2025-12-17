import sys
import time
from grafo import read_graph_from
from grafo import graph
from algoritmo import brute_force_heuristic
from algoritmo import straight_distance_heuristic
from algoritmo import curved_distance
from algoritmo import solve

precision = 5  # decimal places

# input
if len(sys.argv) < 5:
    print("not enough arguments\n")
    exit(-1)
start_id = sys.argv[1]
end_id = sys.argv[2]
infile = sys.argv[3]
outfile = sys.argv[4]
debug = 0
if len(sys.argv) > 5:
    if sys.argv[5] == "-debug":
        debug = 1
with open(outfile, 'w') as f_out:
    f_out.write("")

# get data
g = graph()
t1 = time.time()
g, vertex_processed, edges_processed = read_graph_from(infile)
t2 = time.time()
print(f"load time: { round((t2 - t1) * 10**precision) / 10**precision}s\n# vertices = {vertex_processed}\n# edges = {edges_processed}")

start = g.nodes[start_id]
end = g.nodes[end_id]


def run(start, end, heuristic):
    t1 = time.time()
    chain, n_expanded = solve(start, end, g, heuristic, outfile, debug)
    t2 = time.time()
    t = round((t2 - t1) * 10**precision) / 10**precision
    # maybe print to file
    print(f"t = {t}sec, nodes expanded = {n_expanded}\n{round(n_expanded/t)} nodes/sec\n")
    with open(outfile, 'w') as f_out:
        f_out.write(f"{start_id}")
        prev = start_id
        for i in chain[1:]:
            f_out.write(f" - ({g.nodes[prev].connections[i]}) - {i}")
            prev = i
        f_out.write("\n")


# solving with different heuristics
print("curved distance heuristic")
run(start, end, curved_distance)

print("\"straight\" distance heuristic")
run(start, end, straight_distance_heuristic)

print("brute force heuristic")
run(start, end, brute_force_heuristic)
