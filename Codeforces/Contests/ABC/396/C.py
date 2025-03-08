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

n, m = invars()
black = inlist()
white = inlist()

pos_black = [x for x in black if x >= 0]
neg_black = [x for x in black if x < 0]
neg_black.sort(reverse=True)

current_black = sum(pos_black)
count_pos = len(pos_black)

white_pos = [x for x in white if x > 0]
white_pos.sort(reverse=True)

extra_index = 0  
current_white_sum = 0
best = current_black  
q = 0  

for w in white_pos:
    q += 1
    current_white_sum += w
    if q > count_pos:
        if extra_index < len(neg_black):
            current_black += neg_black[extra_index]
            extra_index += 1
        else:
            break
    candidate = current_black + current_white_sum
    best = max(best, candidate)

best = max(best, 0)
print(best)