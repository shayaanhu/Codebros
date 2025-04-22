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

n = inint()
a = []
b = []
c = []
for _ in range(n):
    ai, bi, ci = invars()
    a.append(ai)
    b.append(bi)
    c.append(ci)

# dp[i][j] = max total happiness up to day i doing activity j on day i
# j: 0 = A (swim), 1 = B (bugs), 2 = C (homework)
dp = [[0]*3 for _ in range(n)]

dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a[i]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b[i]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c[i]

print(max(dp[n - 1]))

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #