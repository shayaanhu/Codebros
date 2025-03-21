# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

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

# --- END TEMPLATE --- #

n = inint()
graph = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    u, v = inlist()
    graph[u].append(v)
    graph[v].append(u)

level = {i: -1 for i in range(1, n+1)}

stack = [(1, 0, -1)]
while stack:
    u, lvl, parent = stack.pop()
    if level[u] != -1:
        continue
    level[u] = lvl
    for v in graph[u]:
        if v == parent:
            continue
        if level[v] == -1:
            stack.append((v, lvl + 1, u))

odd = sum(1 for i in range(1, n+1) if level[i] % 2 == 1)
even = n - odd

ans = odd * even - (n - 1)
print(ans)