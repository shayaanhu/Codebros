# --- TEMPLATE 0 --- #

# -- IMPORTS -- #

import sys
import os
import math
import bisect
from collections import defaultdict

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

t = inint()
for _ in range(t):
    n = inint()
    a = inlist()
    
    # Store positions of each number
    pos = defaultdict(list)
    for i, num in enumerate(a):
        pos[num].append(i)
    
    count = 0
    
    # Check all pairs (a,b) where 1 ≤ a < b ≤ n
    for a_val in range(1, n + 1):
        for b_val in range(a_val + 1, n + 1):
            a_pos = pos[a_val]
            b_pos = pos[b_val]
            
            # Skip if either a or b are already adjacent
            if a_pos[1] == a_pos[0] + 1 or b_pos[1] == b_pos[0] + 1:
                continue
            
            # Check if we can make both pairs adjacent through swaps
            # For two pairs to become adjacent through swaps, they need to be in a specific pattern
            
            a1, a2 = a_pos
            b1, b2 = b_pos
            
            positions = sorted([a1, a2, b1, b2])
            
            # Check if positions form a continuous segment
            # This can be positions[0], positions[1], positions[2], positions[3] being consecutive
            # OR two pairs of consecutive positions
            if (positions[3] - positions[0] == 3 and 
                positions[1] - positions[0] == 1 and 
                positions[2] - positions[1] == 1 and 
                positions[3] - positions[2] == 1):
                count += 1
                
            # Check if there are two pairs of adjacent positions with a gap between them
            elif ((positions[1] - positions[0] == 1 and positions[3] - positions[2] == 1) and 
                  ((a1 == positions[0] and a2 == positions[1]) or 
                   (b1 == positions[0] and b2 == positions[1]) or
                   (a1 == positions[2] and a2 == positions[3]) or 
                   (b1 == positions[2] and b2 == positions[3]))):
                count += 1
    
    print(count)