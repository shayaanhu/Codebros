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

for _ in range(n):
    a, b, c = invars()
    if c == 0:
        print(a)
        continue
    if b == 0:
        print(1)
        continue
    bc = pow(b, c, int(1e9) + 6)
    print(pow(a, bc, int(1e9) + 7))
    