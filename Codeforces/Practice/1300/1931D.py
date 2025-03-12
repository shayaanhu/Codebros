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
    array_length, divisor_sum, divisor_diff = invars()
    array = inlist()
    remainder_count = dict()
    beautiful_pairs = 0
    
    for number in array:
        remainder_x = number % divisor_sum
        remainder_y = number % divisor_diff
        beautiful_pairs += remainder_count.get(((divisor_sum - remainder_x) % divisor_sum, remainder_y), 0)
        remainder_count[(remainder_x, remainder_y)] = remainder_count.get((remainder_x, remainder_y), 0) + 1

    print(beautiful_pairs)