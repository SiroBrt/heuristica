import sys
import heapq
import math
# from grafo import read_graph_from
# from grafo import graph
# from abierta import heap_node
# from abierta import open_list
# from algoritmo import brute_force_heuristic

# ----------------------------------------------------------------
# grafo.py
# ----------------------------------------------------------------


class node:
    # we don't really care for longitude or latitude for brute force, but we will use it for heuristic
    def __init__(self, identifier, long, lat):
        self.id = identifier
        self.long = long
        self.lat = lat
        self.connections = {}

    def __str__(self):
        return f"{self.id}: {self.lat}, {self.long}"

    def connect(self, other, cost):
        self.connections[other] = cost


class graph:
    def __init__(self):
        self.nodes = {}

    def __str__(self):
        part1 = ""
        part2 = ""
        for i in self.nodes:
            part1 = part1 + str(i) + ", "
            part2 = part2 + str(i) + ": " + str(self.nodes[i].connections) + "\n"
        return "nodes: " + part1[:-2] + "\n" + part2

    def insert_node(self, node):
        self.nodes[node.id] = node

    def connect_nodes(self, s_node, e_node, cost):
        if cost < 0:
            return -1
        if s_node not in self.nodes.keys() or e_node not in self.nodes.keys():
            return -1
        self.nodes[s_node].connect(e_node, cost)
        return 0


def read_graph_from(infile):
    vertex_processed = 0
    edges_processed = 0
    g = graph()
    file = open(infile + ".co", 'r')
    for line in file:
        # ignore comments
        if line[0] != "v":
            continue
        trim = line[2:-1]
        identifier, _, trim = trim.partition(" ")
        long, _, lat = trim.partition(" ")
        new_node = node(identifier, int(long), int(lat))
        g.insert_node(new_node)
        vertex_processed += 1
    file = open(infile + ".gr", 'r')
    for line in file:
        # ignore comments
        if line[0] != "a":
            continue
        trim = line[2:-1]
        id1, _, trim = trim.partition(" ")
        id2, _, cost = trim.partition(" ")
        edges_processed += 1
        if g.connect_nodes(id1, id2, int(cost)) == -1:
            print(f"Unknown node: {id1}\nEnding program")
            exit(-1)
    return g, vertex_processed, edges_processed

# ----------------------------------------------------------------
# algoritmo.py
# ----------------------------------------------------------------


def straight_distance_heuristic(n, goal):
    straight_distance = math.sqrt((n.long - goal.long)**2 + (n.lat - goal.lat)**2)
    return straight_distance


def brute_force_heuristic(n, goal):
    return 0


def solve_better(start, goal, g):
    chain = [start, goal]
    return chain
# ----------------------------------------------------------------
# abierta.py
# ----------------------------------------------------------------


class heap_node:
    def __init__(self, cost, h, n: node):
        self.cost = cost
        self.heuristic_cost = h
        self.graph_node = n

    def __str__(self):
        return f"node: ({self.graph_node}), cost: {self.cost}, estimated distance to solution: {self.heuristic_cost}"

# We care about most promising node
# heap by heuristic+cost, tiebreaker is lowest h
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.heuristic_cost < other.heuristic_cost
        else:
            return self.cost < other.cost

    def __eq__(self, other):
        return (self.cost == other.cost) and (self.heuristic_cost == other.heuristic_cost)


class open_list:
    def __init__(self, g: graph):
        self.elements = []
        heapq.heapify(self.elements)  # key = node id, value = cost
        self.graph = g

    def add(self, n: heap_node):
        heapq.heappush(self.elements, n)

# ----------------------------------------------------------------


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

l1 = open_list(g)
l1.add(heap_node(0, straight_distance_heuristic(start, end), start))
l1.add(heap_node(straight_distance_heuristic(start, end), 0, end))
for i in l1.elements:
    print(i)

