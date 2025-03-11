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
    x = inint()
    ans = -1

    # if x power of 2 or that -1 OR x all ones
    if (x & (x - 1) == 0) or (x & (x + 1) == 0):
        print(-1)
        continue

    if x % 2 == 0:
        print(x - 1)
    else:
        a = x // 2
        b = a + 1

        c = x ^ a
        d = x ^ b

        if a + x > c and a + c > x and x + c > a:
            print(a)
        elif b + x > d and b + d > x and x + d > b:
            print(b)
        else:
            print(-1)
