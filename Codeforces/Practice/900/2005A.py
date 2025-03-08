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
vowels = "aeiou"
for _ in range(t):
    n = inint()
    # Create a list of 5 integers, each n//5
    v = [n // 5] * 5
    # Distribute the remainder among the first (n % 5) vowels
    for i in range(n % 5):
        v[i] += 1
    # Build the result string: each vowel repeated its assigned count
    res = ""
    for i in range(5):
        res += vowels[i] * v[i]
    print(res)