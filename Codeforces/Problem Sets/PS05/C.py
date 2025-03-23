import sys
import os
import math
import bisect
from collections import Counter, deque
import time

# -- LOCAL DEBUG SETUP -- #
LOCAL = os.environ.get("TERM_PROGRAM", "").lower() == "vscode"

def debug(*args, **kwargs):
    if LOCAL:
        print("DBG:", *args, **kwargs)

# -- INPUT SECTION -- #

def inint():
    return(int(input()))

def inlist():
    return(list(map(int,input().split())))

def instr():
    s = input()
    return(list(s))

def invars():
    return(map(int,input().split()))

# -- TESTING SECTION -- #

base_path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_path, "input.txt")
if os.path.exists(input_path):  
    sys.stdin = open(input_path, "r")

# -- START TIMER FOR EXECUTION TIME TRACKING -- #
if LOCAL:
    start_time = time.perf_counter()
    
# --- BEGIN PROBLEM LOGIC --- #

# Kosaraju from TRD
def kosaraju_scc(graph):
    """
    Computes strongly connected components (SCCs) using Kosaraju's algorithm.
    Uses iterative DFS.
    graph: dict mapping vertex -> list of neighbors.
    Returns a list of sets, each set is one SCC.
    """
    # First pass: record the finish order.
    visited = set()
    finish_order = []
        
    def dfs(start):
        stack = [start]
        visited_in_current_dfs = set()
        
        while stack:
            vertex = stack[-1]  # Peek at the top
            
            if vertex in visited_in_current_dfs:
                # We've fully processed this vertex, add to finish order
                stack.pop()
                if vertex not in visited:
                    finish_order.append(vertex)
                    visited.add(vertex)
                continue
                
            visited_in_current_dfs.add(vertex)
            
            # Add unvisited neighbors
            any_added = False
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited and neighbor not in visited_in_current_dfs:
                    stack.append(neighbor)
                    any_added = True
                    
            if not any_added:
                # If no neighbors were added, we're done with this vertex
                stack.pop()
                if vertex not in visited:
                    finish_order.append(vertex)
                    visited.add(vertex)

    for u in graph:
        if u not in visited:
            dfs(u)

    # Reverse graph.
    reversed_graph = {}
    for u in graph:
        for v in graph[u]:
            reversed_graph.setdefault(v, []).append(u)
    # Ensure every vertex appears, even if it has no incoming edges in reversed_graph
    for u in graph:
        if u not in reversed_graph:
            reversed_graph[u] = []

    # Second pass: explore in reverse finish order.
    visited.clear()
    scc = []
                
    def dfs_rev(start):
        component = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                component.add(vertex)
                for neighbor in reversed_graph.get(vertex, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return component

    for u in reversed(finish_order):
        if u not in visited:
            component = dfs_rev(u)
            scc.append(component)
            
    return scc

t = inint()
for _ in range(t):
    n, m = invars()

    graph = {i: [] for i in range(1, n+1)}
    for __ in range(m):
        s1, s2 = invars()
        graph[s1].append(s2)

    if n == 1:
        print(0)
        continue

    sccs = kosaraju_scc(graph)
    k = len(sccs)
    if k == 1:
        print(0)
        continue

    scc_map = {}
    for i, comp in enumerate(sccs):
        for node in comp:
            scc_map[node] = i

    in_degree = [0] * k
    out_degree = [0] * k
    
    for u in range(1, n + 1):
        for v in graph[u]:
            cu = scc_map[u]
            cv = scc_map[v]
            if cu != cv:
                out_degree[cu] += 1
                in_degree[cv] += 1
    
    count_zero_in = sum(1 for i in range(k) if in_degree[i] == 0)
    count_zero_out = sum(1 for i in range(k) if out_degree[i] == 0)
    
    ans = max(count_zero_in, count_zero_out)
    print(ans)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")