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

MAX_NODES = 6000009
ch0 = [-1] * MAX_NODES
ch1 = [-1] * MAX_NODES
mx = [-1] * MAX_NODES
node_count = 0
BITS = 30

def create_node():
    global node_count
    idx = node_count
    ch0[idx] = -1
    ch1[idx] = -1
    mx[idx] = -1
    node_count += 1
    return idx

def insert(root, num, pos):
    global node_count
    cur = root
    mx[cur] = max(mx[cur], pos)

    for i in range(BITS - 1, -1, -1):
        bit = (num >> i) & 1

        if bit == 0:
            if ch0[cur] == -1:
                ch0[cur] = create_node()
            cur = ch0[cur]

        else:
            if ch1[cur] == -1:
                ch1[cur] = create_node()
            cur = ch1[cur]
            
        mx[cur] = max(mx[cur], pos)

def query(root, aj, k):
    cur = root
    best = -1

    for i in range(BITS - 1, -1, -1):
        if cur == -1:
            break

        b_bit = (aj >> i) & 1
        k_bit = (k >> i) & 1

        if (1 ^ b_bit) == 0:
            p1 = ch0[cur]
            p0 = ch1[cur]

        else:
            p1 = ch1[cur]
            p0 = ch0[cur]

        if k_bit == 1:
            cur = p1

        else:
            if p1 != -1:
                best = max(best, mx[p1])
            cur = p0

    if cur != -1:
        best = max(best, mx[cur])

    return best

for _ in range(inint()):
    n, k = invars()
    arr = inlist()
    
    if k == 0:
        print(1)
        continue

    if n < 2:
        print(-1)
        continue

    node_count = 0
    root = create_node()
    min_len = float('inf')
    
    insert(root, arr[0], 0)
    
    for j in range(1, n):
        p = query(root, arr[j], k)
        if p != -1:
            min_len = min(min_len, j - p + 1)
        insert(root, arr[j], j)
        
    print(min_len if min_len != float('inf') else -1)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #

if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #