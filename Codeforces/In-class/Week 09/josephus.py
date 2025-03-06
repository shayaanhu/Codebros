# 1 2 3 4 5 6 7

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

# q = inint()

# for _ in range(q):
#     n, k = invars()
#     if k <= n//2:
#         print(2*k)
#     else:
#         print(2*(k-n//2))
#         # print(n//2+k//2)

q = inint()

for _ in range(q):
    n, k = invars()
    
    
    # odd_count = (n + 1) // 2  # Total odd numbers in the sequence

    # if k <= odd_count:
    #     print(2 * k - 1)  # k-th odd number
    # else:
    #     print(2 * (k - odd_count))  # k-th even number
    
    # 1 3 5 7

    # Odd = 2*i - 1
    # Even = 2*i    