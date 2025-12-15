import sys
import time
from grafo import read_graph_from
from grafo import graph
from algoritmo import brute_force_heuristic
from algoritmo import straight_distance_heuristic
from algoritmo import solve


if len(sys.argv) < 5:
    print("not enough arguments\n")
    exit(-1)
start_id = sys.argv[1]
end_id = sys.argv[2]
infile = sys.argv[3]
outfile = sys.argv[4]
if len(sys.argv) > 5:
    if sys.argv[5] == "-debug":
        debug = 1

g = graph()
g, vertex_processed, edges_processed = read_graph_from(infile)

start = g.nodes[start_id]
end = g.nodes[end_id]

# solving
precision = 5

print("straight distance heuristic")
t1 = time.time()
chain, n_expanded_sl = solve(start, end, g, straight_distance_heuristic)
t2 = time.time()
time_sl = round((t2 - t1) * 10**precision) / 10**precision
print(f"path = {chain}, t = {time_sl}sec, nodes = {n_expanded_sl}\n")

print("brute force heuristic")
t1 = time.time()
chain, n_expanded_bf = solve(start, end, g, brute_force_heuristic)
t2 = time.time()
time_bf = round((t2 - t1) * 10**precision) / 10**precision
print(f"path = {chain}, t = {time_bf}sec, nodes = {n_expanded_bf}\n")
