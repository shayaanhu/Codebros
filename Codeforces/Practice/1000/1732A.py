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

t = inint()
for _ in range(t):
    n = inint()
    a = inlist()
    g = a[0]
    for num in a[1:]:
        g = math.gcd(g, num)
    
    # if the global gcd is already 1, no operations are needed.
    if g == 1:
        print(0)
    elif math.gcd(g, n) == 1:
        print(1)
    elif math.gcd(g, n - 1) == 1:
        print(2)
    else:
        print(3)