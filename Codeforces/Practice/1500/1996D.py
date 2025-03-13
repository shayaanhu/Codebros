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
    n, x = inlist()
    ans = 0
    # a goes from 1 to min(n, x)
    for a in range(1, min(n, x) + 1):
        # b must satisfy: a * b <= n and a + b <= x
        # This is equivalent to b <= min(n // a, x - a)
        b_max = min(n // a, x - a)
        for b in range(1, b_max + 1):
            # Calculate highestC as per: min((n - a * b) // (a + b), x - (a + b))
            highestC = min((n - a * b) // (a + b), x - (a + b))
            ans += highestC
    print(ans)