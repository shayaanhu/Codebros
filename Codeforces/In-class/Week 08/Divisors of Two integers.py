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
a = inlist()

freq = Counter(a)
x = max(a)

for d in range(1, int(math.sqrt(x)) + 1):
    if x % d == 0:
        if d in freq and freq[d] > 0:
            freq[d] -= 1
            
        other = x // d
        if other != d and other in freq and freq[other] > 0:
            freq[other] -= 1

y = max(d for d in freq if freq[d] > 0)

print(x, y)