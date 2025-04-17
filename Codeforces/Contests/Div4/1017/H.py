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

max_val = 100001
pos = [[] for _ in range(max_val)]

def get_divisors(k):
    divisors = []
    if k <= 1:
        return divisors
    sqrt_k = int(math.isqrt(k))

    for i in range(1, sqrt_k + 1):
        if k % i == 0:
            if i >= 2:
                divisors.append(i)
            other = k // i
            if other != i and other >= 2:
                divisors.append(other)
    return divisors

t = inint()
output_lines = []

for _ in range(t):
    n, q = invars()
    
    distinct_a_values = []
    
    a = [0] * (n + 1)
    arr = inlist()
    for i in range(1, n + 1):
        val = arr[i - 1]
        a[i] = val
        if not pos[val]:
            distinct_a_values.append(val)
        pos[val].append(i)
    
    for _ in range(q):
        k_init, l, r = invars()
        current_k = k_init
        total_ans = 0
        current_idx = l 
        
        while current_idx <= r:
            if current_k == 1:
                total_ans += (r - current_idx + 1)
                break
            
            divisors = get_divisors(current_k)
            next_index = r + 1
            
            for d in divisors:
                if d < max_val:
                    positions = pos[d]
                    if positions:
                        idx = bisect.bisect_left(positions, current_idx)
                        if idx < len(positions) and positions[idx] <= r:
                            next_index = min(next_index, positions[idx])
            
            if next_index > r:
                total_ans += (r - current_idx + 1) * current_k
                break
            else:
                if next_index > current_idx:
                    total_ans += (next_index - current_idx) * current_k
                
                current_idx = next_index
                val_at_idx = a[current_idx]

                while current_k % val_at_idx == 0:
                    current_k //= val_at_idx

                total_ans += current_k
                current_idx += 1
        
        output_lines.append(str(total_ans))
    
    for v in distinct_a_values:
        pos[v].clear()

print("\n".join(output_lines))

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #