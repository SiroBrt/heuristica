from grafo import graph
from grafo import node
import math


def straight_distance_heuristic(n, goal):
    straight_distance = math.sqrt((n.long - goal.node)**2 + (n.lat - goal.lat)**2)
    return straight_distance


def brute_force_heuristic(n, goal):
    return 0


def solve_better(start, goal, g):
    chain = [start, goal]
    return chain

