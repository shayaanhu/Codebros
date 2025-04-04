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

def union(parent, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx != ry:
        parent[rx] = ry

# Read inputs
n, m1, m2 = map(int, input().split())

# Initialize union-find structures for both forests.
parent_mocha = [i for i in range(n+1)]
parent_diana = [i for i in range(n+1)]

# Process edges for Mocha's forest.
for _ in range(m1):
    u, v = map(int, input().split())
    union(parent_mocha, u, v)

# Process edges for Diana's forest.
for _ in range(m2):
    u, v = map(int, input().split())
    union(parent_diana, u, v)

ans = []

# Try every pair (i, j), if they are in different components in both forests,
# then add the edge and merge the sets.
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if find(parent_mocha, i) != find(parent_mocha, j) and find(parent_diana, i) != find(parent_diana, j):
            ans.append((i, j))
            union(parent_mocha, i, j)
            union(parent_diana, i, j)

print(len(ans))
for u, v in ans:
    print(u, v)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #