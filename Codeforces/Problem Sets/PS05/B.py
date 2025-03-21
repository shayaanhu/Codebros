# --- TEMPLATE 1 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter, deque
import time

# -- LOCAL DEBUG SETUP -- #
LOCAL = "VSCODE_PID" in os.environ

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

# Alternate 1
# from pathlib import Path
# base_path_2 = Path(__file__).parent
    
# Alternate 2
# if os.path.exists("input.txt"):
#     sys.stdin = open("input.txt", "r")

# -- START TIMER FOR EXECUTION TIME TRACKING (only in local mode) -- #
if LOCAL:
    start_time = time.perf_counter()
    
# --- BEGIN PROBLEM LOGIC --- #

MOD = 10**9 + 7

n, m = invars()
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = invars()
    graph[a].append(b)
    graph[b].append(a)

shortest_distance = [None] * (n + 1)
paths = [0] * (n + 1)

shortest_distance[1] = 0
paths[1] = 1

queue = deque([1])
while queue:
    current_city = queue.popleft()
    for neighbor in graph[current_city]:
        # if the neighbor hasn't been visited, update distance and path count
        if shortest_distance[neighbor] is None:
            shortest_distance[neighbor] = shortest_distance[current_city] + 1
            paths[neighbor] = paths[current_city]
            queue.append(neighbor)

        # elif add the path counts
        elif shortest_distance[neighbor] == shortest_distance[current_city] + 1:
            paths[neighbor] = (paths[neighbor] + paths[current_city]) % MOD

print(paths[n])

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME (and memory usage if desired) -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #