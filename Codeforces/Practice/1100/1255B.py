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

for _ in range(inint()):
    n, m = invars()
    a = inlist()
    
    if n == 2 or m < n:
        print(-1)
        continue
    
    min1, min2 = float('inf'), float('inf')
    idx1, idx2 = -1, -1
    for i in range(n):
        if a[i] < min1:
            min2, idx2 = min1, idx1
            min1, idx1 = a[i], i
        elif a[i] < min2:
            min2, idx2 = a[i], i

    total_cost = 2 * sum(a) + (m - n) * (min1 + min2)
    print(total_cost)
    
    for i in range(1, n):
        print(i, i + 1)
    print(n, 1)
    
    for _ in range(m - n):
        print(idx1 + 1, idx2 + 1)