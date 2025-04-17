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
results = []
for _ in range(t):
    q = inint()
    dq = deque()
    current_rizz = 0
    current_sum = 0
    is_reversed = False
    
    for _ in range(q):
        parts = input().split()
        op_type = int(parts[0])
        n = len(dq)
        
        if op_type == 3:
            k = int(parts[1])
            current_rizz += (n + 1) * k
            current_sum += k
            if not is_reversed:
                dq.append(k)
            else:
                dq.appendleft(k)
                
        elif op_type == 1:
            if n > 1:
                if not is_reversed:
                    x = dq.pop()
                    dq.appendleft(x)
                else:
                    x = dq.popleft()
                    dq.append(x)
                current_rizz += current_sum - n * x
                
        elif op_type == 2:
            if n > 0:
                current_rizz = current_sum * (n + 1) - current_rizz
                is_reversed = not is_reversed
        
        results.append(str(current_rizz))

for i in results:
    print(i)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #