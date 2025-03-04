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
    x, y, k = invars()

    while k > 0 and x != 1:
        amount = ((x // y) + 1) * y - x # the amount needed to reach the next multiple of y
        amount = max(1, amount)         # ensure at least 1 is added
        amount = min(amount, k)         # do not add more than k
        x += amount

        while x % y == 0:               # divide out factors of y as long as possible
            x //= y
        k -= amount

    print(x + k % (y - 1)) # add the remainder of k modulo (y-1)