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

for _ in range(inint()):
    n, m = map(int, input().split())
    a = input().split()
    b = [input().split() for _ in range(m)]
    
    # for each position j, check at least one b[i][j] equals a[j]
    possible = True
    for j in range(n):
        valid_for_j = False

        for i in range(m):
            if b[i][j] == a[j]:
                valid_for_j = True
                break
            
        if not valid_for_j:
            possible = False
            break
    
    if not possible:
        print(-1)
        continue
    
    # maxK = max_i (number of j such that b[i][j] == a[j])
    maxK = 0
    for i in range(m):
        count = 0
        for j in range(n):
            if b[i][j] == a[j]:
                count += 1
        maxK = max(maxK, count)
    
    # in the worst case, each cell costs 3 ops, fill, reset, forced fill
    # each matching position saves 2 operations
    # hence total ops = 3 * n - 2 * maxK
    ops = (3 * n) - (2 * maxK)
    print(ops)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #