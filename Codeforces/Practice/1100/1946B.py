# --- TEMPLATE 1 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter, deque
from itertools import accumulate
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

MOD = 10 ** 9 + 7

def max_subarray(arr):
    cur = best = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

for _ in range(inint()):
    n, k = invars()
    a = inlist()
    
    s = sum(a)
    maxsum = max(0, max_subarray(a))
    
    final_sum = (s + (pow(2, k, MOD) - 1) * maxsum) % MOD
    print(final_sum)

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #