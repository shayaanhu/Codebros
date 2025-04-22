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

MOD = 10**9 + 7

n = inint()

grid = []
for _ in range(n):
    grid.append(input())

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 if grid[0][0] == '.' else 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            continue
            
        # each cell, the number of paths is the sum of paths
        # from the cell above and the cell to the left
        if i > 0:
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            
        if j > 0:
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

print(dp[n - 1][n - 1])

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #