# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

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

t = inint()
for _ in range(t):
    n, k = invars()

    # the smallest sum S_min that is a multiple of k and at least n.
    S_min = ((n + k - 1) // k) * k
    
    # binary search for the minimum possible maximum element m
    # such that n * m >= S_min.
    low, high = 1, S_min  # worst-case: when n=1, m must be S_min.
    while low < high:
        mid = (low + high) // 2
        if n * mid >= S_min:
            high = mid
        else:
            low = mid + 1
    print(low)