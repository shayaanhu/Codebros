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

sys.setrecursionlimit(10 ** 6)

MAX_N = (10 ** 6) + 1
MOD = (10 ** 9) + 7
DP = [0] * MAX_N
DP[0] = 1

def diceComb(num):
    if DP[num] != 0:
        return DP[num]

    for i in range(1, 7):
        if num - i >= 0:
            DP[num] += diceComb(num - i)
            DP[num] %= MOD
            
    return DP[num]

def diceCombIter(num):
    for i in range(1, num + 1):
        for j in range(1, 7):
            if i - j >= 0:
                DP[i] += DP[i - j]
                DP[i] %= MOD
                
    return DP[num]

n = inint()
print(diceCombIter(n))
        
# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #