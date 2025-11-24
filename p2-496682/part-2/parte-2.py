import sys
from grafo.py import read_graph_from
from grafo.py import graph

nodes_expanded = 0

if len(sys.argv) < 5:
    print("not enough arguments\n")
    exit(-1)
start = sys.argv[1]
end = sys.argv[2]
infile = sys.argv[3]
outfile = sys.argv[4]
if len(sys.argv) > 5:
    if sys.argv[5] == "-debug":
        debug = 1


g = graph()
g, vertex_processed, edges_processed = read_graph_from(infile)


