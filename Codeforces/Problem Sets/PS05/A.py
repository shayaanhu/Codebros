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

debug("TEST")

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

# directions: right, left, up, down
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(maze, start_row, start_col, rows, cols):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    if maze[start_row][start_col] != '#':
        queue.append((start_row, start_col))
        visited[start_row][start_col] = True

    while queue:
        current_row, current_col = queue.popleft()
        for d_row, d_col in directions:
            new_row = current_row + d_row
            new_col = current_col + d_col
            if (0 <= new_row < rows and 0 <= new_col < cols and
                not visited[new_row][new_col] and maze[new_row][new_col] != '#'):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
    return visited

for _ in range(inint()):
    rows, cols = inlist()
    maze = [list(input().strip()) for _ in range(rows)]
    
    valid_configuration = True
    
    # block empty cells adjacent to a bad person.
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 'B':
                for d_row, d_col in directions:
                    adj_row = row + d_row
                    adj_col = col + d_col
                    if 0 <= adj_row < rows and 0 <= adj_col < cols:
                        if maze[adj_row][adj_col] == 'G':
                            valid_configuration = False
                        if maze[adj_row][adj_col] == '.':
                            maze[adj_row][adj_col] = '#'
    
    if not valid_configuration:
        print('NO')
        continue

    # perform BFS starting from the escape cell (bottom-right cell).
    visited_cells = bfs(maze, rows - 1, cols - 1, rows, cols)
    
    # check that all good persons ('G') can escape and no bad person ('B') can.
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 'G' and not visited_cells[row][col]:
                valid_configuration = False
            if maze[row][col] == 'B' and visited_cells[row][col]:
                valid_configuration = False
    
    print('YES' if valid_configuration else 'NO')

# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #