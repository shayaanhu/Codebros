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

def main():
    t = inint()  # Number of test cases
    for _ in range(t):
        n = inint()
        a = inlist()
        # Initialize an array h for storing the level (depth) of each node in BFS order.
        h = [0] * n  # h[0] = 0 for the root.
        lst = 0  # pointer for the current parent (starting from the root).
        for i in range(1, n):
            # For i > 1 (i.e. when i-1 > 0) check if a[i-1] > a[i].
            # When this happens, it means that the children of the current parent are done, so we move to the next parent.
            if i - 1 > 0 and a[i - 1] > a[i]:
                lst += 1
            # The depth of the current node is one more than the depth of its parent (which is a[lst]).
            h[i] = h[lst] + 1
        print(h[n - 1])

if __name__ == '__main__':
    main()

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
