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
    k, l1, r1, l2, r2 = invars()
    ans = 0
    power = 1  # this is k^n, starting with n=0 (k^0 = 1)
    
    # iterate over possible values of n until even the smallest x gives y out of range
    while True:
        # for the current power, we require: l2 <= x * power <= r2
        # so, x must be at least ceil(l2 / power) and at most floor(r2 / power)
        # then x must also be in [l1, r1]
        low_x = max(l1, (l2 + power - 1) // power)
        high_x = min(r1, r2 // power)

        # add all the valid values
        if low_x <= high_x:
            ans += (high_x - low_x + 1)
        
        # check if we can try a higher exponent.
        # if power * k so high that even x = l1 yields x * (power*k) > r2,
        # then no further solutions exist
        if power > r2 // k:
            break

        power = power * k
    
    print(ans)