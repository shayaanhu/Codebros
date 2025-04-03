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

def force(i, forced, q, forced_count):
    if not forced[i]:
        forced[i] = True
        forced_count[0] += 1
        q.append(i)

def bfs(q, forced, a, b, forced_count):
    while q:
        current = q.popleft()
        for next in b[current]:
            if a[next] != 0 and not forced[next]:
                force(next, forced, q, forced_count)

t = inint()
for _ in range(t):
    n = inint()
    p = inlist()         
    queries = inlist()
    queries = [x - 1 for x in queries]
    
    a = p[:]
    b = [[] for __ in range(n)]
    for i in range(n):
        if a[i] != 0:
            b[a[i] - 1].append(i)
    
    forced = [False] * n
    forced_count = [0]  
    q = deque()
    ans = []
    
    for pos in queries:
        if a[pos] != 0:
            a[pos] = 0
            force(pos, forced, q, forced_count)
        
        bfs(q, forced, a, b, forced_count)

        print(forced_count[0], end=" ")

    print()
        
# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #