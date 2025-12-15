import sys
import time
from grafo import read_graph_from
from grafo import graph
from algoritmo import brute_force_heuristic
from algoritmo import straight_distance_heuristic
from algoritmo import solve

nodes_expanded = 0

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

print("straight distance heuristic")
t1 = time.time()
chain = solve(start, end, g, straight_distance_heuristic)
t2 = time.time()
t_straight_line = t2 - t1
print(f"path = {chain}, t = {t_straight_line}sec\n")

print("brute force heuristic")
t1 = time.time()
chain = solve(start, end, g, brute_force_heuristic)
t2 = time.time()
t_brute_force = t2 - t1
print(f"path = {chain}, t = {t_brute_force}sec")
