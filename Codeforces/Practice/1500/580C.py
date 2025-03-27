# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

sys.setrecursionlimit(10**6)

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

# --- END TEMPLATE --- #

o = 0  # This will count the number of valid leaves
a = []  # adjacency list for the tree
c = []  # values for each node
m_limit = 0  # global limit m (from input)

def go(v, parent, k):
    global o, a, c, m_limit
    if k > m_limit:
        return
    is_leaf = True
    for nxt in a[v]:
        if nxt != parent:
            is_leaf = False
            new_k = c[nxt] * (k + 1)
            go(nxt, v, new_k)
    if is_leaf:
        o += 1

def solve():
    global o, a, c, m_limit
    n_m = inlist()
    if not n_m:
        return
    n, m_limit = n_m[0], n_m[1]
    c_values = inlist()
    c = c_values[:]  # c[i] for i from 0 to n-1
    
    a = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = inlist()
        x -= 1
        y -= 1
        a[x].append(y)
        a[y].append(x)
    
    o = 0
    go(0, -1, c[0])
    print(o)

if __name__ == "__main__":
    solve()
