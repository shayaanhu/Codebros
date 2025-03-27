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

# --- END TEMPLATE --- #

def main():
    n = inint()
    parents = inlist()
    
    depth = [0] * (n + 1)
    depth[1] = 0
    
    for i in range(2, n+1):
        p = parents[i-2]
        depth[i] = depth[p] + 1
    
    cnt = Counter(depth[1:])  # ignore index 0 since nodes are 1-indexed
    
    result = sum(c % 2 for c in cnt.values())
    
    print(result)

if __name__ == '__main__':
    main()
