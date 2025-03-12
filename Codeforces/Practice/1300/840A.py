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

# Read the length of the arrays.
m = inint()
# Read array A and array B.
A = inlist()
B = inlist()

# Create list of (index, value) pairs for array B.
# This allows us to later restore the original positions.
B_indexed = list(enumerate(B))
# Sort B in descending order by value.
B_indexed.sort(key=lambda x: -x[1])

# Sort A in ascending order.
A_sorted = sorted(A)

# Create a result array to hold the rearranged A.
result = [0] * m

# According to the rearrangement inequality, pairing the smallest A
# with the largest B maximizes the overall sum.
for i, (index, _) in enumerate(B_indexed):
    result[index] = A_sorted[i]

# Print the rearranged array.
print(" ".join(map(str, result)))