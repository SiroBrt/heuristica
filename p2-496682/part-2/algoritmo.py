import math
from abierta import open_list
from abierta import open_node
from cerrada import close_list
from grafo import node


def brute_force_heuristic(n, goal):
    return 0


# in general not admisible because angles don't work like that
def straight_distance_heuristic(n: node, goal: node):
    if n.id == goal.id:
        return 0
    return math.sqrt((n.long - goal.long)**2 + (n.lat - goal.lat)**2)


def curved_distance(n: node, goal: node):
    if n.id == goal.id:
        return 0

    dLat = goal.lat - n.lat
    dLong = goal.long - n.long

    a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLong / 2), 2) * math.cos(n.lat) * math.cos(goal.lat))
    rad = 6371000  # in meters
    c = 2 * math.asin(math.sqrt(a))
    # rounded to make sure it is admisible
    return math.floor(rad * c) * 10  # for some reason the cost is in decimeters so we can be more informed multiplying


def solve(start, goal, g, heuristica, outfile, debug):
    l_open = open_list(start)
    l_close = close_list()
    it = 0
    next_print = 1000
    while len(l_open.elements) > 0:
        if debug:
            if it == next_print:
                next_print *= 2
                print(f"{it} nodes expanded")

        if debug:
            with open(outfile, 'a') as f_out:
                f_out.write(f"\niteration {it}\n")
                for i in l_open.elements:
                    f_out.write(f"{i}\n")

                to_expand = l_open.get()
                f_out.write(f"opening ({to_expand})\n")
        else:
            to_expand = l_open.get()
        l_close.add(to_expand.cost, to_expand.graph_node, to_expand.prev)
        if to_expand.graph_node.id == goal.id:
            print(f"solution found with cost {to_expand.cost}")
            break
        for i in to_expand.graph_node.connections.keys():
            # already expanded?
            if i in l_close.elements.keys():
                # expanded with higher cost?
                if l_close.elements[i].cost < (to_expand.cost + to_expand.graph_node.connections[i]):
                    continue

            hn = open_node(to_expand.graph_node.connections[i] + to_expand.cost, heuristica(g.nodes[i], goal), g.nodes[i], to_expand.graph_node)
            l_open.add(hn)
        it += 1

    # make chain from close_list
    chain = []
    n_id = goal.id
    while n_id != start.id:
        chain.append(n_id)
        n_id = l_close.elements[n_id].prev
    chain.append(n_id)
    chain.reverse()
    return chain, it
