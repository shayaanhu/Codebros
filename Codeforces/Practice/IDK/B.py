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

for _ in range(inint()):
    c1, c2, c3 = invars()
    a1, a2, a3, a4, a5, = invars()

    c1 -= a1
    c2 -= a2
    c3 -= a3

    if c1 < 0 or c2 < 0 or c3 < 0:
        print("NO")
        continue

    if c1 - a4 > 0:
        c1 -= a4
        a4 = 0
    else:
        a4 -= c1
        c1 = 0

    if c2 - a5 > 0:
        c2 -= a5
        a5 = 0
    else:
        a5 -= c2
        c2 = 0

    c3 -= a4 + a5

    if c1 < 0 or c2 < 0 or c3 < 0:
        print("NO")
    else:
        print("YES")

    
# --- END PROBLEM LOGIC --- #

# -- PRINT EXECUTION TIME -- #
if LOCAL:
    end_time = time.perf_counter()
    print("Execution time:", end_time - start_time, "seconds")

# --- END TEMPLATE --- #