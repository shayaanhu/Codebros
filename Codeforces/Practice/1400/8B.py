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

# --- END TEMPLATE --- #

moves = input().strip()
x, y = 0, 0
visited = dict()
visited[(0, 0)] = 0

dir_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

is_bug = False

for i, move in enumerate(moves, 1):
    dx, dy = dir_map[move]
    x, y = x + dx, y + dy

    if (x, y) in visited:
        is_bug = True
        break

    for adj in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if adj in visited:
            if visited[adj] != i - 1:
                is_bug = True
                break
    if is_bug:
        break

    visited[(x, y)] = i

if is_bug:
    print("BUG")
else:
    print("OK")
