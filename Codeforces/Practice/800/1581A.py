# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import Counter

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

# --- END TEMPLATE --- #

MOD = 1000000007
MAX_N = 100000

# Precompute f[1..MAX_N]
# f[1] = 1 and for i >= 2, f[i] = ((2*i - 1) * f[i-1] % MOD) * (2*i) % MOD
f = [0] * (MAX_N + 1)
f[1] = 1
for i in range(2, MAX_N + 1):
    f[i] = ((2 * i - 1) * f[i - 1] % MOD) * (2 * i) % MOD

# First input is the number of test cases
t = inint()
for _ in range(t):
    n = inint()
    print(f[n])