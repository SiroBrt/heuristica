from grafo import node
import heapq


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
