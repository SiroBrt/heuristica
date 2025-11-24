class node:
    def __init__(self, identifier):
        self.id = identifier
        self.connections = []
    # we don't really care for longitude or latitude for the exercise
    # def __init__(self, identifier, long, lat):
    #     self.id = identifier
    #     self.long = long
    #     self.lat = lat
    #     self.connections = []

    def __str__(self):
        # return f"{self.id}: {self.lat}, {self.long}"
        return str(self.id)

    def connect(self, other, cost):
        self.connections.append((other, cost))


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
        trim = line[2:-1]
        identifier, _, trim = trim.partition(" ")
        # long, _, lat = trim.partition(" ")
        # new_node = node(identifier, int(long), int(lat))
        new_node = node(identifier)
        g.insert_node(new_node)
        vertex_processed += 1
    file = open(infile + ".gr", 'r')
    for line in file:
        trim = line[2:-1]
        id1, _, trim = trim.partition(" ")
        id2, _, cost = trim.partition(" ")
        edges_processed += 1
        if g.connect_nodes(id1, id2, int(cost)) == -1:
            print(f"Unknown node: {id1}\nEnding program")
            exit(-1)
    return g, vertex_processed, edges_processed


