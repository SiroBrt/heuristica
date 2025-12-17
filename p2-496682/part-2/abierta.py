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
        if self.cost + self.heuristic_cost == other.cost + other.heuristic_cost:
            return self.heuristic_cost < other.heuristic_cost
        else:
            return self.cost + self.heuristic_cost < other.cost + other.heuristic_cost

    def __eq__(self, other):
        return (self.graph_node.id == other.graph_node.id)


class open_list:
    def __init__(self, n: node):
        self.elements = [open_node(0, 0, n, n)]
        heapq.heapify(self.elements)

    def add(self, n: open_node):
        if n not in self.elements:
            heapq.heappush(self.elements, n)
        else:
            index = self.elements.index(n)
            if self.elements[index].cost > n.cost:
                self.elements[index] = n
                heapq.heapify(self.elements)
            # print("repe")

    def get(self):
        return heapq.heappop(self.elements)
