# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import math
import sys
import os

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
    n = inint()
    a = inlist()
    
    last_occurrence = {}
    for i, val in enumerate(a):
        last_occurrence[val] = i + 1

    ans = -1
    for x in last_occurrence:
        for y in last_occurrence:
            if x == y and x != 1:
                continue
            if math.gcd(x, y) == 1:
                ans = max(ans, last_occurrence[x] + last_occurrence[y])
        
    print(ans)            