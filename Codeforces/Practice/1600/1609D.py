# --- TEMPLATE 1 --- #

# -- IMPORTS -- #

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

# Alternate 1
# from pathlib import Path
# base_path_2 = Path(__file__).parent
    
# Alternate 2
# if os.path.exists("input.txt"):
#     sys.stdin = open("input.txt", "r")

# -- START TIMER FOR EXECUTION TIME TRACKING -- #
if LOCAL:
    start_time = time.perf_counter()
    
# --- BEGIN PROBLEM LOGIC --- #

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False  # union did not merge; this is a redundant edge.
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

# Read input
n, d = map(int, input().split())
conditions = []
for _ in range(d):
    x, y = map(int, input().split())
    # convert to 0-indexed
    conditions.append((x-1, y-1))

# For each i from 1 to d, process the first i conditions independently.
for i in range(1, d+1):
    parent = list(range(n))
    comp_size = [1] * n
    extra = 0  # count of redundant edges
    # Process the first i conditions.
    for j in range(i):
        u, v = conditions[j]
        if not union(parent, comp_size, u, v):
            extra += 1
    # Count the sizes of all connected components.
    comp = {}
    for x in range(n):
        root = find(parent, x)
        if root not in comp:
            comp[root] = comp_size[root]
    # Get all component sizes and sort in descending order.
    sizes = sorted(comp.values(), reverse=True)
    # With extra edges we can "connect" extra+1 components.
    # (If extra is r, we can merge r+1 largest components.)
    num_to_merge = min(extra + 1, len(sizes))
    max_acquaintances = sum(sizes[:num_to_merge]) - 1
    print(max_acquaintances)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #