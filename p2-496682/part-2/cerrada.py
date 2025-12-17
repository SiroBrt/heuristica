from grafo import node


# We care about existence of node
class closed_node:
    def __init__(self, cost, n: node, previous_node: node):
        self.id = n.id
        self.prev = previous_node.id
        self.cost = cost


class close_list:
    def __init__(self):
        self.elements = {}  # id-> closed_node

    def add(self, cost, n: node, prev: node):
        if n.id in self.elements.keys():
            if cost < self.elements[n.id].cost:
                self.elements[n.id].cost = cost
                self.elements[n.id].prev = prev.id
        else:
            self.elements[n.id] = closed_node(cost, n, prev)
