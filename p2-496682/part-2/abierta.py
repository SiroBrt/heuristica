from grafo import graph
from grafo import node
import heapq


class heap_node:
    def __init__(self, cost, h, n: node):
        self.cost = cost
        self.heuristic_cost = h
        self.graph_node = n

# We care about most promising node
# heap by heuristic+cost, tiebreaker is lowest h
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.heuristic_cost < other.heuristic_cost
        else:
            return self.cost < other.cost

    def __eq__(self, other):
        return (self.cost == other.cost) and (self.heuristic_cost == other.heuristic_cost)

    def __str__(self):
        return f"node: {self.graph_node}, cost: {self.cost}, estimated distance to solution: {self.heuristic_cost}"


class open_list:
    def __init__(self, g: graph):
        self.elements = []
        heapq.heapify([])  # key = node id, value = cost
        self.graph = g

    def add(self, n: heap_node):
        heapq.heappush(self.elements, n)
        graph_node = n.graph_node
        nodes_to_expand = []
        for i in self.graph.nodes[graph_node].connections:
            if n in self.elements:
                # if self.elements[i] > cost + self.graph[n].connections
                nodes_to_expand.append(i)
        return nodes_to_expand


