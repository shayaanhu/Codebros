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

def lcm(a, b):
    return a * b // math.gcd(a, b)

t = inint()
for _ in range(t):
    n = inint()
    multipliers = inlist()
    
    lcm_val = 1
    for multiplier in multipliers:
        lcm_val = lcm(lcm_val, multiplier)
    
    total_bets = sum(lcm_val // multiplier for multiplier in multipliers)
    
    if total_bets < lcm_val:
        bets = [lcm_val // multiplier for multiplier in multipliers]
        print(" ".join(str(bet) for bet in bets))
    else:
        print(-1)