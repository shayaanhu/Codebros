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

h, w = invars()
s = [input().strip() for _ in range(h)]
a, b, c, d = invars()
a -= 1; b -= 1; c -= 1; d -= 1

INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]
dq = deque()
dist[a][b] = 0
dq.append((a, b))

while dq:
    i, j = dq.popleft()
    cur = dist[i][j]

    # 1) walk to adjacent roads at cost 0
    for di, dj in ((1, 0),(-1, 0),(0, 1),(0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and s[ni][nj]=='.':
            if dist[ni][nj] > cur:
                dist[ni][nj] = cur
                dq.appendleft((ni, nj))

    # 2) front kicks in 4 directions, cost 1
    for di, dj in ((1, 0),(-1, 0),(0, 1),(0, -1)):
        for step in (1, 2):
            ni, nj = i + di * step, j + dj * step
            if not (0 <= ni < h and 0 <= nj < w):
                break

            # if it's already a road, we can still stand there after kick,
            # but kicking beyond a road doesn't clear further walls, so stop
            if s[ni][nj] == '.':
                if dist[ni][nj] > cur + 1:
                    dist[ni][nj] = cur + 1
                    dq.append((ni, nj))
                break

            # it's a wall: kick clears it and we can stand there
            if dist[ni][nj] > cur + 1:
                dist[ni][nj] = cur + 1
                dq.append((ni, nj))

            # continue to next step to clear up to 2 walls

print(dist[c][d])

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #