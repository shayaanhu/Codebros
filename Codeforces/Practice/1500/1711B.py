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

t = inint()
for _ in range(t):
    n, m = invars()
    costs = inlist()
    
    degree = [0] * n
    
    edges = []
    for _ in range(m):
        u, v = inlist()
        u -= 1
        v -= 1
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    
    if m % 2 == 0:
        answer = 0
    else:
        answer = float('inf')
    
    for i in range(n):
        if degree[i] % 2 == 1:
            answer = min(answer, costs[i])
    
    for u, v in edges:
        if degree[u] % 2 == 0 and degree[v] % 2 == 0:
            answer = min(answer, costs[u] + costs[v])
    
    print(answer)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #