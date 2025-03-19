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

lst = []

n, m = invars()
vals = [0]*(n+1)
check = False
for _ in range(m):
    a, b = invars()
    # lst.append([a, b])
    if not check:
        if vals[a] == 0 and vals[b] == 0:
            vals[a] = 1
            vals[b] = 2
        elif vals[a] == vals[b]:
            print('Impossible')
            check = True
        elif vals[a] != 0:
            # vals[a]
            vals[b] = 1 if vals[a] == 2 else 2
        else:
            vals[a] = 1 if vals[b] == 2 else 2
    
    
for i in vals:  
    if i != 0:  
        print(i, end=" ")