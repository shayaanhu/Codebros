# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

# -- INPUT SECTION -- #

def inint():
    return int(input())

def inlist():
    return list(map(int, input().split()))

def instr():
    s = input()
    return list(s)

def invars():
    return map(int, input().split())

# --- END TEMPLATE --- #

# Helper function: iterative DFS
def iterative_dfs(graph, start):
    stack = [start]
    seen = {start}
    while stack:
        node = stack.pop()
        yield node
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

# Function to get connected components
def connected_components(graph):
    """
    Finds connected components in an undirected graph.
    graph: dict mapping vertex -> list of neighbors.
    Returns a list of sets, each set is one connected component.
    """
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = set(iterative_dfs(graph, node))
            components.append(comp)
            visited |= comp  # Mark all nodes in this component as visited.
    return components

def main():
    n, m = invars()
    
    costs = [0] + inlist()  # Padding index 0, so that costs[1] corresponds to 1st character
    
    graph = {i: [] for i in range(1, n + 1)}
    
    for _ in range(m):
        u, v = invars()
        graph[u].append(v)
        graph[v].append(u)
    
    components = connected_components(graph)
    
    total_cost = 0
    for comp in components:
        comp_min = min(costs[node] for node in comp)
        total_cost += comp_min
    
    print(total_cost)

if __name__ == '__main__':
    main()
