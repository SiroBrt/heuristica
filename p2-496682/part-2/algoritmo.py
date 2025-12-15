import math
from abierta import open_list
from abierta import open_node
from cerrada import close_list


def straight_distance_heuristic(n, goal):
    return math.sqrt((n.long - goal.long)**2 + (n.lat - goal.lat)**2)


def brute_force_heuristic(n, goal):
    return 0 if n.id == goal.id else 1


def solve(start, goal, g, heuristica):
    print("Solving")
    l_open = open_list()
    l_open.add(open_node(0, heuristica(start, goal), start, start))
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
