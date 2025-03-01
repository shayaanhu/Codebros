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

n = inint()

grid = [[''] * n for _ in range(n)]
# print(grid)

for i in range(1, n + 1):
    j = n + 1 - i
    if i > j:
        break

    color = '#' if i % 2 == 1 else '.'

    for a in range(i - 1, j):
        for b in range(i - 1, j):
            grid[a][b] = color

    # print(grid)

for row in grid:
    print("".join(row))