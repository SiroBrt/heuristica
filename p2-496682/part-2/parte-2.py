import sys
import heapq
import math
import time
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
    return 0 if n.id == goal.id else 1


def solve(start, goal, g, heuristica):
    print("Solving")
    l_open = open_list()
    l_open.add(open_node(0, heuristica(start, end), start, start))
    l_close = close_list()
    while len(l_open.elements) > 0:
        to_expand = l_open.get()
        # print(f"opening ({to_expand})")
        l_close.add(to_expand.cost, to_expand.graph_node, to_expand.prev)
        if to_expand.graph_node.id == goal.id:
            print(f"solution found with cost {to_expand.cost}")
            break
        for i in to_expand.graph_node.connections.keys():
            hn = open_node(to_expand.graph_node.connections[i] + to_expand.cost, heuristica(to_expand.graph_node, goal), g.nodes[i], to_expand.graph_node)
            l_open.add(hn)

    # make chain from close_list
    print("doing chain")
    chain = []
    n_id = goal.id
    while n_id != start.id:
        chain.append(n_id)
        n_id = l_close.elements[n_id].prev
    chain.append(n_id)
    chain.reverse()
    return chain


# ----------------------------------------------------------------
# abierta.py
# ----------------------------------------------------------------
class open_node:
    def __init__(self, cost, h, n: node, prev: node):
        self.cost = cost
        self.heuristic_cost = h
        self.graph_node = n
        self.prev = prev

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
    def __init__(self):
        self.elements = []
        heapq.heapify(self.elements)  # key = node id, value = cost

    def add(self, n: open_node):
        heapq.heappush(self.elements, n)

    def get(self):
        return heapq.heappop(self.elements)


# ----------------------------------------------------------------
# cerrada.py
# ----------------------------------------------------------------
# We care about existence of node
class closed_node:
    def __init__(self, cost, n: node, previous_node: node):
        self.id = n.id
        self.prev = previous_node.id
        self.cost = cost


class close_list:
    def __init__(self):
        self.elements = {}

    def add(self, cost, n: node, prev: node):
        if n.id in self.elements.keys():
            if cost < self.elements[n.id].cost:
                self.elements[n.id].cost = cost
                self.elements[n.id].prev = prev.id
        else:
            self.elements[n.id] = closed_node(cost, n, prev)


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

t1 = time.time()
chain = solve(start, end, g, straight_distance_heuristic)
t2 = time.time()
t_straight_line = t2 - t1
print(f"path found through {chain}, t = {t_straight_line}sec")

t1 = time.time()
chain = solve(start, end, g, brute_force_heuristic)
t2 = time.time()
t_brute_force = t2 - t1
print(f"path found through {chain}, t = {t_brute_force}sec")
