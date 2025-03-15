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

R, C = invars()
pasture = [list(input().strip()) for _ in range(R)]

# Check if a wolf is adjacent to a sheep
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'W':
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < R and 0 <= nj < C and pasture[ni][nj] == 'S':
                    print("No")
                    sys.exit()

# Place dogs in all empty spaces
for i in range(R):
    for j in range(C):
        if pasture[i][j] == '.':
            pasture[i][j] = 'D'

print("Yes")
for row in pasture:
    print("".join(row))